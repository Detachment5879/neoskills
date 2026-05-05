---
name: git-snapshot
description: Quick git status snapshot — show staged/unstaged/untracked changes, recent commits, and branch info in a compact format
---

# Git Snapshot

Quickly capture a summary of the current git repository state for sharing or logging.

## Instructions

1. Run `git status --short` for a compact overview
2. Run `git log --oneline -5` for recent commit history
3. Run `git diff --stat` for file-level changes
4. Compile into a structured report

## Output Format

```
## Git Snapshot — <branch> @ <date>

### Branch
<current branch>, <ahead/behind origin>

### Recent Commits (5)
<hash> <message>
<hash> <message>

### Changes
<files changed summary>

### Untracked
<list of new files>
```
