#!/bin/bash
# SessionStart hook — detects first-run and submodule sync state.
# stdout is injected into the session context as info for Claude.

set -e

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

# Check submodule health: if .gitmodules declares a submodule whose directory is empty, flag it.
if [ -f ".gitmodules" ]; then
  while IFS= read -r submodule_path; do
    if [ -d "$submodule_path" ] && [ -z "$(ls -A "$submodule_path" 2>/dev/null | grep -v '^\.git$' || true)" ]; then
      echo "⚠️ SUBMODULE NOT SYNCED: \`$submodule_path\` is empty."
      echo ""
      echo "The user likely cloned without \`--recurse-submodules\`. Tell them to run:"
      echo ""
      echo "    git submodule update --init --recursive"
      echo ""
    fi
  done < <(git config --file .gitmodules --get-regexp path 2>/dev/null | awk '{print $2}')
fi

# Check first-run: missing my-context.md means onboarding needed.
if [ ! -f "my-context.md" ]; then
  cat <<'EOF'
🚀 FIRST-RUN DETECTED — No `my-context.md` found in this repo.

This user has never onboarded to ContextOS Personal. Kick off the onboarding flow immediately:

1. Load `skills/onboarding.md`
2. Greet the user warmly and walk through the 7 steps
3. Do NOT wait for the user to ask — their first prompt may be unrelated; run onboarding first, then resume their original question after setup completes

After both files (`my-context.md` and a personalized `CLAUDE.md`) are generated, confirm completion and resume normal conversation.
EOF
fi
