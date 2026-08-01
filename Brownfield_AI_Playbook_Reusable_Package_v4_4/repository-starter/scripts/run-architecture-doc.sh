#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
MANIFEST="$ROOT/docs/ai/architecture-docs.tsv"
CHECKPOINT="$ROOT/docs/ai/DOCUMENTATION_CHECKPOINT.md"
CREATE_TEMPLATE="$ROOT/docs/ai/prompts/architecture-map-create.md"
REVIEW_TEMPLATE="$ROOT/docs/ai/prompts/architecture-map-review.md"
PROMOTE_TEMPLATE="$ROOT/docs/ai/prompts/architecture-map-promote.md"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/run-architecture-doc.sh --list
  ./scripts/run-architecture-doc.sh --next <create|review|promote>
  ./scripts/run-architecture-doc.sh <document-id> <create|review|promote>
  ./scripts/run-architecture-doc.sh --allow-out-of-sequence <document-id> <create|review|promote>

Examples:
  ./scripts/run-architecture-doc.sh --list
  ./scripts/run-architecture-doc.sh --next create
  ./scripts/run-architecture-doc.sh data-flow review
  ./scripts/run-architecture-doc.sh data-flow promote

The runner:
  - renders one complete Codex prompt;
  - verifies the manifest, prerequisite, target state, and checkpoint order;
  - prints the prompt and copies it to the clipboard when possible;
  - never invokes Codex, edits documentation, changes status, commits, or publishes.

Workflow for each map:
  create -> separate read-only review -> promote
EOF
}

[[ -f "$MANIFEST" ]] || { echo "Missing manifest: $MANIFEST" >&2; exit 1; }
[[ -f "$CHECKPOINT" ]] || { echo "Missing checkpoint: $CHECKPOINT" >&2; exit 1; }
[[ -f "$CREATE_TEMPLATE" ]] || { echo "Missing template: $CREATE_TEMPLATE" >&2; exit 1; }
[[ -f "$REVIEW_TEMPLATE" ]] || { echo "Missing template: $REVIEW_TEMPLATE" >&2; exit 1; }
[[ -f "$PROMOTE_TEMPLATE" ]] || { echo "Missing template: $PROMOTE_TEMPLATE" >&2; exit 1; }

ROWS=()
while IFS=$'\t' read -r order id name output spec prerequisite; do
  [[ -z "${order:-}" || "$order" == \#* ]] && continue
  ROWS+=("$order"$'\t'"$id"$'\t'"$name"$'\t'"$output"$'\t'"$spec"$'\t'"$prerequisite")
done < "$MANIFEST"

[[ "${#ROWS[@]}" -gt 0 ]] || { echo "Architecture manifest is empty." >&2; exit 1; }

document_status() {
  sed -n \
    -e 's/^\*\*Status:\*\*[[:space:]]*//p' \
    -e 's/^Status:[[:space:]]*//p' \
    "$1" |
    head -1 |
    tr -d '\r'
}

list_documents() {
  printf '%-5s %-34s %-10s %s\n' "Order" "ID" "Status" "Output"
  for row in "${ROWS[@]}"; do
    IFS=$'\t' read -r order id name output spec prerequisite <<< "$row"
    status="missing"
    if [[ -f "$ROOT/$output" ]]; then
      status="$(document_status "$ROOT/$output" || true)"
      [[ -n "$status" ]] || status="present"
    fi
    printf '%-5s %-34s %-10s %s\n' "$order" "$id" "$status" "$output"
  done
}

if [[ "${1:-}" == "--list" ]]; then
  [[ $# -eq 1 ]] || { usage; exit 2; }
  list_documents
  exit 0
fi

allow_out_of_sequence=0
if [[ "${1:-}" == "--allow-out-of-sequence" ]]; then
  allow_out_of_sequence=1
  shift
fi

[[ $# -eq 2 ]] || { usage; exit 2; }
selector="$1"
mode="$2"

case "$mode" in
  create|review|promote) ;;
  *) usage; exit 2 ;;
esac

authorized_output="$(
  awk '
    /^## Next authorized task/ { in_section=1; next }
    in_section && /^## / { exit }
    in_section { print }
  ' "$CHECKPOINT" |
    sed -n 's/.*`\(docs\/wiki\/[^`]*\.md\)`.*/\1/p' |
    head -1
)"

[[ -n "$authorized_output" ]] || {
  echo "Could not resolve the next authorized document from the checkpoint." >&2
  exit 1
}

selected_row=""
if [[ "$selector" == "--next" ]]; then
  for row in "${ROWS[@]}"; do
    IFS=$'\t' read -r order id name output spec prerequisite <<< "$row"
    if [[ "$output" == "$authorized_output" ]]; then
      selected_row="$row"
      break
    fi
  done
  [[ -n "$selected_row" ]] || {
    echo "Checkpoint target is not present in the architecture manifest: $authorized_output" >&2
    exit 1
  }
else
  for row in "${ROWS[@]}"; do
    IFS=$'\t' read -r order id name output spec prerequisite <<< "$row"
    if [[ "$id" == "$selector" ]]; then
      selected_row="$row"
      break
    fi
  done
  [[ -n "$selected_row" ]] || {
    echo "Unknown architecture document ID: $selector" >&2
    echo >&2
    list_documents >&2
    exit 2
  }
fi

IFS=$'\t' read -r order id name output spec prerequisite <<< "$selected_row"

if [[ "$allow_out_of_sequence" -eq 0 && "$output" != "$authorized_output" ]]; then
  echo "Checkpoint authorizes $authorized_output, not $output." >&2
  echo "Use --next or obtain explicit authorization before proceeding." >&2
  exit 1
fi

[[ -f "$ROOT/$spec" ]] || { echo "Missing scope specification: $spec" >&2; exit 1; }
[[ -f "$ROOT/$prerequisite" ]] || { echo "Missing prerequisite: $prerequisite" >&2; exit 1; }

if ! grep -Eiq '^\*\*Status:\*\*[[:space:]]*(Reviewed|Reviewed orientation)|^Status:[[:space:]]*(Reviewed|Reviewed orientation)' "$ROOT/$prerequisite"; then
  echo "Prerequisite is not Reviewed: $prerequisite" >&2
  exit 1
fi

case "$mode" in
  create)
    [[ ! -e "$ROOT/$output" ]] || {
      echo "Target already exists; use review or promote: $output" >&2
      exit 1
    }
    template="$CREATE_TEMPLATE"
    ;;
  review)
    [[ -f "$ROOT/$output" ]] || {
      echo "Review target does not exist: $output" >&2
      exit 1
    }
    target_status="$(document_status "$ROOT/$output")"
    [[ "$target_status" == "Draft" ]] || {
      echo "Review target must have status Draft; found '${target_status:-missing}': $output" >&2
      exit 1
    }
    template="$REVIEW_TEMPLATE"
    ;;
  promote)
    [[ -f "$ROOT/$output" ]] || {
      echo "Promotion target does not exist: $output" >&2
      exit 1
    }
    target_status="$(document_status "$ROOT/$output")"
    [[ "$target_status" == "Draft" ]] || {
      echo "Promotion target must have status Draft; found '${target_status:-missing}': $output" >&2
      exit 1
    }
    template="$PROMOTE_TEMPLATE"
    ;;
esac

next_output="PHASE_3_4"
next_name="Phase 3.4 architecture coverage review"
for candidate in "${ROWS[@]}"; do
  IFS=$'\t' read -r candidate_order candidate_id candidate_name candidate_output candidate_spec candidate_prerequisite <<< "$candidate"
  if (( candidate_order > order )); then
    next_output="$candidate_output"
    next_name="$candidate_name"
    break
  fi
done

revision="$(git -C "$ROOT" rev-parse HEAD)"
prompt="$(
  sed \
    -e "s|{{DOCUMENT_ID}}|$id|g" \
    -e "s|{{DOCUMENT_NAME}}|$name|g" \
    -e "s|{{OUTPUT_PATH}}|$output|g" \
    -e "s|{{SPEC_PATH}}|$spec|g" \
    -e "s|{{PREREQUISITE_PATH}}|$prerequisite|g" \
    -e "s|{{NEXT_OUTPUT_PATH}}|$next_output|g" \
    -e "s|{{NEXT_DOCUMENT_NAME}}|$next_name|g" \
    -e "s|{{GIT_REVISION}}|$revision|g" \
    "$template"
)"

echo "Repository: $ROOT"
echo "Document:   $name ($id)"
echo "Mode:       $mode"
echo "Output:     $output"
echo "Checkpoint: $authorized_output"
echo "Revision:   $revision"
echo
printf '%s\n' "$prompt"

if command -v pbcopy >/dev/null 2>&1; then
  if printf '%s\n' "$prompt" | pbcopy; then
    echo
    echo "Prompt copied to clipboard with pbcopy."
  else
    echo
    echo "pbcopy is unavailable in this session; use the prompt printed above."
  fi
elif command -v wl-copy >/dev/null 2>&1; then
  if printf '%s\n' "$prompt" | wl-copy; then
    echo
    echo "Prompt copied to clipboard with wl-copy."
  else
    echo
    echo "wl-copy is unavailable in this session; use the prompt printed above."
  fi
elif command -v xclip >/dev/null 2>&1; then
  if printf '%s\n' "$prompt" | xclip -selection clipboard; then
    echo
    echo "Prompt copied to clipboard with xclip."
  else
    echo
    echo "xclip is unavailable in this session; use the prompt printed above."
  fi
else
  echo
  echo "No clipboard command found; use the prompt printed above."
fi
