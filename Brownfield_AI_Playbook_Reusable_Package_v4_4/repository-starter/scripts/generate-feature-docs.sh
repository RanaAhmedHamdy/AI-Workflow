#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
MANIFEST="$ROOT/docs/ai/feature-docs.tsv"
CREATE_TEMPLATE="$ROOT/docs/ai/prompts/feature-doc-create.md"
REVIEW_TEMPLATE="$ROOT/docs/ai/prompts/feature-doc-review.md"
CHECKPOINT="docs/ai/DOCUMENTATION_CHECKPOINT.md"

MODE="next"
FEATURE_ID=""
EXECUTE=0
RUN_REVIEW=1
REVIEW_ONLY=0
ALLOW_DIRTY=0
MODEL="${OPENCODE_DOC_MODEL:-nvidia/deepseek-ai/deepseek-v4-pro}"
AGENT="${OPENCODE_DOC_AGENT:-build}"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/generate-feature-docs.sh [options]

Selection:
  --next                 Process the first missing feature document (default)
  --feature ID           Process one feature ID from docs/ai/feature-docs.tsv
  --all                  Process every missing feature in manifest order

Execution:
  --execute              Actually invoke OpenCode; otherwise print a dry run
  --create-only          Skip the review/checkpoint pass
  --review-only          Review existing feature pages without creating new ones
  --model PROVIDER/MODEL Override model
  --agent NAME           Override OpenCode agent (default: build)
  --allow-dirty          Permit an initially dirty worktree (not recommended)
  -h, --help             Show help

Examples:
  ./scripts/generate-feature-docs.sh
  ./scripts/generate-feature-docs.sh --next --execute
  ./scripts/generate-feature-docs.sh --feature today --execute
  OPENCODE_DOC_MODEL=nvidia/deepseek-ai/deepseek-v4-pro \
    ./scripts/generate-feature-docs.sh --all --execute

Safety:
  - Requires a Git repository and, by default, a clean worktree.
  - Uses one fresh `opencode run` per create/review pass.
  - Allows changes only to the current feature page and, during review,
    docs/ai/DOCUMENTATION_CHECKPOINT.md.
  - Stops immediately when unexpected files change.
  - Never commits, pushes, merges, or edits source intentionally.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --next) MODE="next"; shift ;;
    --feature) MODE="feature"; FEATURE_ID="${2:?missing feature ID}"; shift 2 ;;
    --all) MODE="all"; shift ;;
    --execute) EXECUTE=1; shift ;;
--create-only) RUN_REVIEW=0; shift ;;
    --review-only) REVIEW_ONLY=1; RUN_REVIEW=1; shift ;;
    --model) MODEL="${2:?missing model}"; shift 2 ;;
    --agent) AGENT="${2:?missing agent}"; shift 2 ;;
    --allow-dirty) ALLOW_DIRTY=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
  esac
done

command -v git >/dev/null || { echo "git is required" >&2; exit 1; }
if [[ "$EXECUTE" -eq 1 ]]; then
  command -v opencode >/dev/null || {
    echo "opencode is not installed or not on PATH" >&2
    exit 1
  }
fi
[[ -f "$MANIFEST" ]] || { echo "Missing $MANIFEST" >&2; exit 1; }
[[ -f "$CREATE_TEMPLATE" ]] || { echo "Missing $CREATE_TEMPLATE" >&2; exit 1; }
[[ -f "$REVIEW_TEMPLATE" ]] || { echo "Missing $REVIEW_TEMPLATE" >&2; exit 1; }
[[ -f "$ROOT/$CHECKPOINT" ]] || { echo "Missing $ROOT/$CHECKPOINT" >&2; exit 1; }

cd "$ROOT"

if [[ "$ALLOW_DIRTY" -eq 0 ]] &&
  [[ ! ("$REVIEW_ONLY" -eq 1 && "$EXECUTE" -eq 0) ]] &&
  [[ -n "$(git status --porcelain)" ]]; then
  echo "Worktree is not clean. Commit/stash changes or use --allow-dirty." >&2
  exit 1
fi

render() {
  local template="$1" feature_id="$2" feature_name="$3" output="$4"
  local next_output="$5" next_name="$6" revision="$7"
  sed \
    -e "s|{{FEATURE_ID}}|$feature_id|g" \
    -e "s|{{FEATURE_NAME}}|$feature_name|g" \
    -e "s|{{OUTPUT_PATH}}|$output|g" \
    -e "s|{{NEXT_OUTPUT_PATH}}|$next_output|g" \
    -e "s|{{NEXT_FEATURE_NAME}}|$next_name|g" \
    -e "s|{{GIT_REVISION}}|$revision|g" \
    "$template"
}

changed_files() {
  {
    git diff --name-only
    git diff --cached --name-only
    git ls-files --others --exclude-standard
  } | awk 'NF' | sort -u
}

assert_allowed_changes() {
  local output="$1" allow_checkpoint="$2"
  local changed unexpected=""
  changed="$(changed_files)"
  while IFS= read -r file; do
    [[ -z "$file" ]] && continue
    if [[ "$file" == "$output" ]]; then
      continue
    fi
    if [[ "$allow_checkpoint" == "1" && "$file" == "$CHECKPOINT" ]]; then
      continue
    fi
    unexpected+="${file}"$'\n'
  done <<< "$changed"

  if [[ -n "$unexpected" ]]; then
    echo "ERROR: OpenCode changed files outside the allowed scope:" >&2
    printf '%s' "$unexpected" >&2
    echo "Review and revert those changes manually. Automation stopped." >&2
    exit 1
  fi
}

mapfile_compat() {
  # macOS Bash 3.2 has no mapfile.
  ROWS=()
  while IFS=$'\t' read -r order id name output; do
    [[ -z "${order:-}" || "$order" == \#* ]] && continue
    ROWS+=("$order"$'\t'"$id"$'\t'"$name"$'\t'"$output")
  done < "$MANIFEST"
}

mapfile_compat
[[ "${#ROWS[@]}" -gt 0 ]] || { echo "Manifest is empty" >&2; exit 1; }

SELECTED=()
case "$MODE" in
  feature)
    for row in "${ROWS[@]}"; do
      IFS=$'\t' read -r order id name output <<< "$row"
      [[ "$id" == "$FEATURE_ID" ]] && SELECTED+=("$row")
    done
    [[ "${#SELECTED[@]}" -eq 1 ]] || {
      echo "Unknown feature ID: $FEATURE_ID" >&2
      exit 2
    }
    ;;
  next)
    if [[ "$REVIEW_ONLY" -eq 1 ]]; then
      for row in "${ROWS[@]}"; do
        IFS=$'\t' read -r order id name output <<< "$row"
        if [[ -f "$output" ]]; then
          SELECTED+=("$row")
          break
        fi
      done
      [[ "${#SELECTED[@]}" -eq 1 ]] || {
        echo "No existing feature documents found for review." >&2
        exit 0
      }
    else
      for row in "${ROWS[@]}"; do
        IFS=$'\t' read -r order id name output <<< "$row"
        if [[ ! -f "$output" ]]; then
          SELECTED+=("$row")
          break
        fi
      done
    fi
    ;;
  all)
    if [[ "$REVIEW_ONLY" -eq 1 ]]; then
      for row in "${ROWS[@]}"; do
        IFS=$'\t' read -r order id name output <<< "$row"
        [[ -f "$output" ]] && SELECTED+=("$row")
      done
    else
      for row in "${ROWS[@]}"; do
        IFS=$'\t' read -r order id name output <<< "$row"
        [[ -f "$output" ]] || SELECTED+=("$row")
      done
    fi
    ;;
esac

if [[ "${#SELECTED[@]}" -eq 0 ]]; then
  if [[ "$REVIEW_ONLY" -eq 1 ]]; then
    echo "No existing feature documents matched the selection."
  else
    echo "No missing feature documents matched the selection."
  fi
  exit 0
fi

if [[ "$REVIEW_ONLY" -eq 1 ]]; then
  for row in "${SELECTED[@]}"; do
    IFS=$'\t' read -r order id name output <<< "$row"
    [[ -f "$output" ]] || {
      echo "Review target does not exist: $output" >&2
      exit 1
    }
  done

  echo "Mode: review-only (creation skipped)"
  echo "Review prompt: ${REVIEW_TEMPLATE#"$ROOT/"}"
  echo "Checkpoint: $CHECKPOINT"
  echo "Selected pages: ${#SELECTED[@]}"
fi

find_next() {
  local current_order="$1"
  NEXT_OUTPUT="NONE"
  NEXT_NAME="architecture coverage assessment"
  for candidate in "${ROWS[@]}"; do
    IFS=$'\t' read -r c_order c_id c_name c_output <<< "$candidate"
    if (( c_order > current_order )); then
      NEXT_OUTPUT="$c_output"
      NEXT_NAME="$c_name"
      return
    fi
  done
}

for row in "${SELECTED[@]}"; do
  IFS=$'\t' read -r order id name output <<< "$row"
  find_next "$order"
  revision="$(git rev-parse HEAD)"

  echo
  echo "=== $name ==="
  echo "Output: $output"
  echo "Model:  $MODEL"
  echo "Agent:  $AGENT"

  if [[ "$REVIEW_ONLY" -eq 1 ]]; then
    review_message="$(render "$REVIEW_TEMPLATE" "$id" "$name" "$output" "$NEXT_OUTPUT" "$NEXT_NAME" "$revision")"
    if [[ "$EXECUTE" -eq 0 ]]; then
      echo "[dry run] Would run review-only pass:"
      echo "Review prompt: ${REVIEW_TEMPLATE#"$ROOT/"}"
      echo "Checkpoint: $CHECKPOINT"
      echo "opencode run --model '$MODEL' --agent '$AGENT' --title 'Review $name documentation' <rendered prompt>"
    else
      opencode run \
        --model "$MODEL" \
        --agent "$AGENT" \
        --title "Review $name documentation" \
        "$review_message"
      assert_allowed_changes "$output" 1
      if grep -Eq '^\*\*Status:\*\*[[:space:]]*Reviewed|^Status:[[:space:]]*Reviewed' "$output"; then
        echo "  Marked Reviewed."
      else
        echo "  Remains Draft."
      fi
    fi
  else
    create_message="$(render "$CREATE_TEMPLATE" "$id" "$name" "$output" "$NEXT_OUTPUT" "$NEXT_NAME" "$revision")"

    if [[ "$EXECUTE" -eq 0 ]]; then
      echo "[dry run] Would run creation pass:"
      echo "opencode run --model '$MODEL' --agent '$AGENT' --title 'Document $name' <rendered prompt>"
    else
      mkdir -p "$(dirname "$output")"
      opencode run \
        --model "$MODEL" \
        --agent "$AGENT" \
        --title "Document $name" \
        "$create_message"
      assert_allowed_changes "$output" 0
      [[ -s "$output" ]] || {
        echo "Expected document was not created: $output" >&2
        exit 1
      }
    fi

    if [[ "$RUN_REVIEW" -eq 1 ]]; then
      review_message="$(render "$REVIEW_TEMPLATE" "$id" "$name" "$output" "$NEXT_OUTPUT" "$NEXT_NAME" "$revision")"
      if [[ "$EXECUTE" -eq 0 ]]; then
        echo "[dry run] Would run review pass:"
        echo "opencode run --model '$MODEL' --agent '$AGENT' --title 'Review $name documentation' <rendered prompt>"
      else
        opencode run \
          --model "$MODEL" \
          --agent "$AGENT" \
          --title "Review $name documentation" \
          "$review_message"
        assert_allowed_changes "$output" 1
        if grep -Eq '^\*\*Status:\*\*[[:space:]]*Reviewed|Status:[[:space:]]*Reviewed' "$output"; then
          echo "  Marked -> Reviewed."
        else
          echo "  Review pass did not mark the document Reviewed: $output" >&2
          exit 1
        fi
      fi
    fi
  fi

  if [[ "$EXECUTE" -eq 1 ]]; then
    echo
    git diff --stat -- "$output" "$CHECKPOINT"
    echo "Completed $name. Changes remain uncommitted for human review."
  fi
done

if [[ "$EXECUTE" -eq 0 ]]; then
  echo
  echo "Dry run only. Add --execute after reviewing the manifest and prompts."
fi
