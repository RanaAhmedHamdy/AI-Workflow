#!/usr/bin/env bash
set -euo pipefail

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
PROMPT_DIR="$ROOT/docs/ai/prompts"

usage() {
  cat <<'EOF'
Usage:
  ./scripts/run-doc-phase.sh <phase> <create|review>

Phases:
  feature-map
  testing-map
  dependencies
  project-overview
  architecture

Examples:
  ./scripts/run-doc-phase.sh feature-map create
  ./scripts/run-doc-phase.sh feature-map review

The script prints the prompt path and copies the prompt to the clipboard when
pbcopy, xclip, or wl-copy is available. It does not invoke Codex, edit files,
approve documents, or commit changes.
EOF
}

[[ $# -eq 2 ]] || { usage; exit 2; }

phase="$1"
mode="$2"

case "$phase" in
  feature-map) target="$ROOT/docs/wiki/project/FEATURE_MAP.md"; prereq="$ROOT/docs/wiki/project/MODULES.md" ;;
  testing-map) target="$ROOT/docs/wiki/testing/TESTING_MAP.md"; prereq="$ROOT/docs/wiki/project/FEATURE_MAP.md" ;;
  dependencies) target="$ROOT/docs/wiki/project/DEPENDENCIES.md"; prereq="$ROOT/docs/wiki/project/MODULES.md" ;;
  project-overview) target="$ROOT/docs/wiki/project/PROJECT_OVERVIEW.md"; prereq="$ROOT/docs/wiki/project/DEPENDENCIES.md" ;;
  architecture) target="$ROOT/docs/wiki/project/ARCHITECTURE.md"; prereq="$ROOT/docs/wiki/project/PROJECT_OVERVIEW.md" ;;
  *) usage; exit 2 ;;
esac

case "$mode" in
  create|review) ;;
  *) usage; exit 2 ;;
esac

prompt="$PROMPT_DIR/${phase}-${mode}.md"
[[ -f "$prompt" ]] || { echo "Missing prompt: $prompt" >&2; exit 1; }
[[ -f "$prereq" ]] || { echo "Missing prerequisite: $prereq" >&2; exit 1; }

if ! grep -Eiq '^\*\*Status:\*\* (Reviewed|Reviewed orientation)' "$prereq"; then
  echo "Prerequisite is not marked Reviewed: $prereq" >&2
  exit 1
fi

if [[ "$mode" == "review" && ! -f "$target" ]]; then
  echo "Target does not exist for review: $target" >&2
  exit 1
fi

echo "Repository: $ROOT"
echo "Git revision: $(git -C "$ROOT" rev-parse HEAD)"
echo "Prompt: $prompt"
echo "Target: $target"
echo
cat "$prompt"

if command -v pbcopy >/dev/null 2>&1; then
  pbcopy < "$prompt"
  echo
  echo "Prompt copied to clipboard with pbcopy."
elif command -v wl-copy >/dev/null 2>&1; then
  wl-copy < "$prompt"
  echo
  echo "Prompt copied to clipboard with wl-copy."
elif command -v xclip >/dev/null 2>&1; then
  xclip -selection clipboard < "$prompt"
  echo
  echo "Prompt copied to clipboard with xclip."
else
  echo
  echo "No clipboard command found; copy the prompt printed above."
fi
