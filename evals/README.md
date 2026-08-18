# Behavioral regression cases

`cases.json` contains agent-agnostic smoke tests for the highest-risk governance behaviors across the Greenfield and Brownfield packages.

These are **not a substitute for model-specific evaluation**. They provide a stable prompt corpus and simple required/forbidden language checks so maintainers can detect obvious regressions across different coding agents.

## Suggested workflow

1. Run each case prompt with the target repository context/skills installed.
2. Save the full agent response as `.eval-results/<case-id>.txt`.
3. Run:

```bash
python3 tools/evaluate_responses.py --responses-dir .eval-results --require-all
```

The checker is intentionally conservative and simple. A passing keyword smoke test does not prove semantic correctness; maintainers should still inspect failures and a sample of passes manually.
