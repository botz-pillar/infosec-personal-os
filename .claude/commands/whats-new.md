Check what's changed in the shared team context since I last updated.

Run this command to see the diff:
```bash
cd shared-context && git fetch origin && git log HEAD..origin/main --oneline --no-merges
```

Then summarize the changes in a readable format:
1. **New files added** — list any new workflows, prompts, integrations, or guides
2. **Updated files** — list files that were modified and summarize what changed
3. **Removed files** — list anything that was deleted

For each change, briefly explain how it might affect my work.

After showing the summary, ask: "Want me to pull these updates? (runs `git submodule update --remote` in the parent repo)"

If there are no changes, just say: "Shared context is up to date. No new changes from the team."
