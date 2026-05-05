#!/usr/bin/env python3
"""
ns-summary — neoskills Repository Quick Summary Tool

A small artifact that prints a compact summary of the neoskills project:
- Project metadata (name, version)
- Repository stats (total files, lines of code)
- Skill inventory (all skills in skills/)
- Recent git activity

Usage:
    python3 ns-summary.py [--path /path/to/neoskills]

Created as part of Elite20 Starter coursework (Task 5 — ship an artifact).
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path


def git_cmd(repo_path, cmd):
    """Run a git command and return output."""
    try:
        result = subprocess.run(
            ["git"] + cmd,
            capture_output=True, text=True, cwd=repo_path, timeout=10
        )
        return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return "(unavailable)"


def count_lines(file_paths):
    """Count total lines in a list of files."""
    total = 0
    for fp in file_paths:
        try:
            with open(fp, "r", errors="ignore") as f:
                total += sum(1 for _ in f)
        except (OSError, IOError):
            pass
    return total


def collect_files(repo_path, skip_dirs=None):
    """Collect all non-git, non-cache files."""
    if skip_dirs is None:
        skip_dirs = {".git", "__pycache__", ".ruff_cache", ".pytest_cache", ".mypy_cache", ".venv", "node_modules"}
    files = []
    for root, dirs, names in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in skip_dirs]
        for name in names:
            if name.endswith((".pyc", ".pyo")):
                continue
            files.append(os.path.join(root, name))
    return files


def get_skills(repo_path):
    """Find all skills in skills/ directory."""
    skills_dir = os.path.join(repo_path, "skills")
    if not os.path.isdir(skills_dir):
        return []
    skills = []
    for item in sorted(os.listdir(skills_dir)):
        skill_path = os.path.join(skills_dir, item)
        if os.path.isdir(skill_path) and os.path.isfile(os.path.join(skill_path, "SKILL.md")):
            skills.append(item)
    return skills


def print_header(text):
    """Print a styled header."""
    print(f"\n{'=' * 56}")
    print(f"  {text}")
    print(f"{'=' * 56}")


def main():
    parser = argparse.ArgumentParser(description="neoskills Repository Quick Summary")
    parser.add_argument("--path", default=".", help="Path to neoskills repository")
    args = parser.parse_args()

    repo_path = os.path.abspath(args.path)

    if not os.path.isdir(os.path.join(repo_path, ".git")):
        print(f"Error: {repo_path} is not a git repository.")
        sys.exit(1)

    # --- Project Metadata ---
    print_header("Project Metadata")

    # Try reading version from pyproject.toml
    pyproject_path = os.path.join(repo_path, "pyproject.toml")
    version = "?"
    if os.path.isfile(pyproject_path):
        with open(pyproject_path) as f:
            for line in f:
                if line.strip().startswith("version ="):
                    version = line.split("=")[1].strip().strip('"')
                    break

    print(f"  Project:     neoskills")
    print(f"  Version:     {version}")

    remote = git_cmd(repo_path, ["remote", "get-url", "origin"])
    print(f"  Remote:      {remote}")

    branch = git_cmd(repo_path, ["rev-parse", "--abbrev-ref", "HEAD"])
    print(f"  Branch:      {branch}")

    # --- Repository Stats ---
    print_header("Repository Stats")

    all_files = collect_files(repo_path)
    py_files = [f for f in all_files if f.endswith(".py")]
    md_files = [f for f in all_files if f.endswith(".md")]
    yaml_files = [f for f in all_files if f.endswith((".yaml", ".yml"))]

    total_lines = count_lines(all_files)

    print(f"  Total files:    {len(all_files)}")
    print(f"  Python files:   {len(py_files)}")
    print(f"  Markdown files: {len(md_files)}")
    print(f"  YAML files:     {len(yaml_files)}")
    print(f"  Total lines:    {total_lines}")

    # --- Skill Inventory ---
    print_header("Skill Inventory")

    skills = get_skills(repo_path)
    if skills:
        for i, skill in enumerate(skills, 1):
            print(f"  {i:2d}. {skill}")
    else:
        print("  (no skills in skills/ directory)")

    # --- Recent Git Activity ---
    print_header("Recent Git Activity")

    last_5 = git_cmd(repo_path, ["log", "--oneline", "-5"])
    if last_5:
        for line in last_5.split("\n"):
            print(f"  {line}")

    ahead = git_cmd(repo_path, ["rev-list", "--count", "HEAD..@{u}", "--"])
    behind = git_cmd(repo_path, ["rev-list", "--count", "@{u}..HEAD", "--"])
    print(f"\n  Ahead: {ahead}  |  Behind: {behind}")

    status = git_cmd(repo_path, ["status", "--short"])
    if status:
        print(f"\n  Uncommitted changes ({len(status.split(chr(10)))} files):")
        for line in status.split("\n")[:10]:
            print(f"    {line}")
    else:
        print("\n  Working tree: clean ✨")


if __name__ == "__main__":
    main()
