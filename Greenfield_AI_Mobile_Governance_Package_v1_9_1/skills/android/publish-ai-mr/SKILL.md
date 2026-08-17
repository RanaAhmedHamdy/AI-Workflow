---
name: publish-ai-mr
description: Prepare and, after separate explicit approval, publish an already reviewed committed focused branch without merging or hiding local state.
---

# Publish AI-Assisted Merge Request

## Stage 1 - read-only preparation

Validate branch/target/worktree/commits/diff; collect exact verification, documentation-impact, architecture-coverage, protected-boundary, risk, and reviewer-focus evidence; ensure intended work is committed; create the MR description outside the repository; present title and full description; stop for explicit approval.

## Stage 2 - remote side effects

Only after explicit approval, reverify unchanged state and invoke the repository publishing script. Report exact output, push/MR result, and URL. Never merge, auto-merge, force-push, bypass failures, expose credentials, publish from protected branches, hide unrelated changes, or invent verification.
