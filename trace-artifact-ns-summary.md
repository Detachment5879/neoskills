# Artifact Trace — Task 5: ns-summary.py

## Artifact: `scripts/ns-summary.py`

A Python CLI tool that generates a compact overview of the neoskills repository.

### Why this artifact?

The neoskills project is complex (~300+ files, 12+ test modules, ontology engine, etc.).
When working with this repo, you often need a quick overview of:
- What version is it on?
- What skills are available?
- What's changed recently?
- How many files/lines?

`ns-summary.py` answers all of these in one command.

### What it does

| Feature | Implementation |
|---------|---------------|
| Project metadata | Reads `pyproject.toml`, git remote, current branch |
| File statistics | Walks repo (excluding .git/ and cache dirs), counts files per type |
| Skill inventory | Scans `skills/` directory for subdirectories with SKILL.md |
| Git activity | Shows last 5 commits, ahead/behind status, uncommitted changes |
| Portable | Pure Python 3, no external dependencies |

### Usage

```bash
# From within the repo
python3 scripts/ns-summary.py

# Or from anywhere
python3 scripts/ns-summary.py --path /path/to/neoskills
```

### Verification

Tested manually — the output looks like:

```
========================================================
  Project Metadata
========================================================
  Project:     neoskills
  Version:     0.4.2
  Remote:      https://github.com/Detachment5879/neoskills.git
  Branch:      main
...
```

### Reflection

This artifact follows the KSTAR mindset:
- **K**: Know the project needs a quick summary tool
- **S**: Search for what info is accessible (git, filesystem, pyproject)
- **T**: Think about what format and features are useful
- **A**: Act — write the script
- **R**: Reflect — it's simple, pure Python, no deps, and genuinely useful
