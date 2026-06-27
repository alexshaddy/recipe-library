#!/usr/bin/env bash
set -euo pipefail
REPO_DIR="/Users/alex/recipe-library"
cd "$REPO_DIR"
# Use local agent identity for commits
git config user.name "herdr-agent"
git config user.email "herdr-agent@local"

while true; do
  cd "$REPO_DIR" || exit 1
  # Check for uncommitted or untracked changes
  if [[ -n $(git status --porcelain) ]]; then
    git add -A
    # If there is something staged, commit and push
    if ! git diff --cached --quiet; then
      git commit -m "Auto-commit: changes from herdr agents" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>" || true
      git push origin main || true
    fi
  fi
  sleep 5
done
