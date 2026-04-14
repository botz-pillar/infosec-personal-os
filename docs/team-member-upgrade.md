# Team Member Upgrade Playbook

> For Claude Code to execute on behalf of a team member (not a repo maintainer) with an existing ContextOS Personal clone from v1. Goal: upgrade to v2 without losing personal customizations, add any missing submodules, and teach as you go.

**Last Updated:** 2026-04-14

---

## Your Role

You are Claude Code running in a team member's personal OS working directory. They have customizations they don't want to lose. They may be newer to Claude Code and want to learn — **explain each step as you work.**

### Tone
Patient, clear, educational. Name what you're doing and why. Pause at decision points.

### Never
- Overwrite the user's `CLAUDE.md` without explicit approval
- Overwrite the user's `my-context.md` without explicit approval
- Delete files the user added
- Force-push, `reset --hard` on a dirty tree, or destroy history
- Proceed past a decision point without asking

### Always
- Inspect before changing
- Show a plan before executing
- Use `git fetch` before diffing — never `pull`/`merge` without approval
- Report clearly what changed after each phase

---

## Phase 1 — Discovery (no changes)

Run the following. Collect results. **Don't modify anything.**

### 1.1 Where am I?
```bash
pwd
ls
git rev-parse --show-toplevel
```

### 1.2 What repo is this?
```bash
git remote -v
git branch --show-current
git log --oneline -5
```

Confirm origin is `contextOS-personal` (or a fork of it). If it's something else, stop and report to the user.

### 1.3 Local state
```bash
git status --short
git diff --stat
```

Capture any uncommitted work. Don't lose it.

### 1.4 Submodule config
```bash
cat .gitmodules 2>/dev/null || echo "No submodules declared"
git submodule status 2>/dev/null
```

Note which submodules are declared, their paths, URLs, and sync state.

### 1.5 Personalization check

Inspect `CLAUDE.md` and `my-context.md` if present:

```bash
grep -l '{{' CLAUDE.md my-context.md 2>/dev/null
wc -l CLAUDE.md my-context.md 2>/dev/null
head -20 CLAUDE.md 2>/dev/null
```

- `{{PLACEHOLDER}}` strings present → file is still a template
- No placeholders + substantial content → file is personalized (leave it alone)
- File missing → user hasn't onboarded yet (stop and flag — this is not an upgrade scenario, it's an onboarding scenario)

### 1.6 Report findings

Produce a short summary to the user, e.g.:

> I'm in `/path/to/context-os`. This is a clone of `https://github.com/botz-pillar/contextOS-personal.git` on branch `main`, last commit `abc1234`.
>
> Uncommitted changes: none / [list]
> Submodules: `shared-context` → [URL], [synced/not synced]. `lab-data` → [present/missing].
> `CLAUDE.md` appears **personalized** (no placeholders, 180 lines). `my-context.md` appears **personalized** (280 lines).
>
> I won't touch anything yet. Next I'll fetch the latest upstream changes (no merge) and propose a plan.

---

## Phase 2 — Fetch + Diff (no changes to working tree)

### 2.1 Fetch without merging
```bash
git fetch origin
```

### 2.2 What's different upstream?
```bash
git log HEAD..origin/main --oneline
git diff --name-status HEAD..origin/main
```

### 2.3 Categorize each upstream change

| Category | Typical files | Action |
|----------|---------------|--------|
| **Safe to pull** | `skills/`, `.claude/hooks/`, `docs/common-mistakes.md`, `docs/upgrade-from-v1.md`, `docs/team-member-upgrade.md` (this file), `examples/README.md`, `CHANGELOG.md` | Cherry-pick directly |
| **Preserve** | `CLAUDE.md`, `my-context.md` | Do NOT overwrite |
| **Template refresh (usually safe)** | `CLAUDE-TEMPLATE.md`, `personal-context-template.md`, `README.md`, `docs/setup-guide.md`, `docs/customization-guide.md`, `docs/collaboration-guide.md` | Check `git diff HEAD..origin/main -- <file>`. If user didn't modify, safe to update. |
| **Rename (upstream moved files)** | `examples/soc-analyst-example/` → `examples/infosec/soc-analyst-example/` | Use git rename detection; preserve any local edits |
| **Merge (config)** | `.claude/settings.json` | User may have custom MCP servers — merge, don't overwrite |
| **Slash commands** | `.claude/commands/*.md` | Check each; most users don't modify, safe to update |

### 2.4 Present plan to the user

Output something like:

```
UPGRADE PLAN

I'll make these changes:

NEW (pulling from upstream):
  - skills/ folder (3 skills: onboarding, prompt-framework, chunking)
  - .claude/hooks/check-first-run.sh (SessionStart hook)
  - docs/common-mistakes.md
  - docs/upgrade-from-v1.md
  - docs/team-member-upgrade.md
  - examples/README.md
  - CHANGELOG.md

UPDATED (template refresh — you didn't customize these):
  - CLAUDE-TEMPLATE.md, personal-context-template.md
  - README.md
  - docs/{setup-guide, customization-guide, collaboration-guide}.md
  - .claude/commands/verify.md

MERGED (combining your config with upstream):
  - .claude/settings.json
    keeping: your mcpServers (if any), your permissions.deny
    adding: hooks.SessionStart → check-first-run.sh

MOVED (upstream renamed; I'll match):
  - examples/soc-analyst-example/ → examples/infosec/soc-analyst-example/
  - (same for cloud-security-engineer, compliance-manager)

UNCHANGED (your personal files — never touched):
  - CLAUDE.md (your personalized router)
  - my-context.md (your detailed context)
  - my-prompts/ (your prompt workshop)
  - my-context/ (your extended context notes)
  - any files you added locally

SUBMODULES:
  - shared-context → update to latest [after confirming URL is correct]
  - lab-data → [add if missing / update if present]

OK to proceed? (yes / no / show me specific diffs first)
```

Wait for explicit "yes" before executing.

---

## Phase 3 — Execute (only after approval)

### 3.1 Stash any uncommitted work

If `git status --short` showed local changes:
```bash
git stash push -m "pre-v2-upgrade stash"
```
Note: restore with `git stash pop` at the end.

### 3.2 Cherry-pick new + refreshable files

```bash
# New files (guaranteed no conflict)
git checkout origin/main -- skills/
git checkout origin/main -- .claude/hooks/
git checkout origin/main -- docs/common-mistakes.md
git checkout origin/main -- docs/upgrade-from-v1.md
git checkout origin/main -- docs/team-member-upgrade.md
git checkout origin/main -- examples/README.md
git checkout origin/main -- CHANGELOG.md

# Template refreshes (only if user didn't modify — check first!)
git checkout origin/main -- CLAUDE-TEMPLATE.md
git checkout origin/main -- personal-context-template.md
git checkout origin/main -- README.md
git checkout origin/main -- docs/setup-guide.md docs/customization-guide.md docs/collaboration-guide.md

# Slash commands — verify.md in particular needs to match v2 structure
git checkout origin/main -- .claude/commands/verify.md
```

Make the hook executable:
```bash
chmod +x .claude/hooks/check-first-run.sh
```

### 3.3 Handle renames

```bash
# If user has no local changes under old example paths, just pull upstream structure
git checkout origin/main -- examples/
```

If the user DID add files to an old example path (e.g., `examples/soc-analyst-example/my-notes.md`):
1. Show them: "You have a file at the old path. I'll move it to the new path: `examples/infosec/soc-analyst-example/`"
2. `git mv` to preserve history

### 3.4 Merge `.claude/settings.json` (not overwrite)

```bash
# Show both versions
cat .claude/settings.json > /tmp/settings-current.json
git show origin/main:.claude/settings.json > /tmp/settings-upstream.json
diff /tmp/settings-current.json /tmp/settings-upstream.json
```

Produce a merged JSON:
- Keep the user's `mcpServers` (if any)
- Keep the user's `permissions.deny` (they should overlap with upstream; use the union)
- Add upstream's `hooks.SessionStart` block

Show the final merged JSON to the user before writing:
```json
{
  "mcpServers": { /* user's existing config */ },
  "permissions": {
    "deny": [
      "Edit(shared-context/**)",
      "Write(shared-context/**)",
      "Bash(rm shared-context/*)",
      "Bash(mv shared-context/*)",
      "Bash(cp * shared-context/*)"
    ]
  },
  "hooks": {
    "SessionStart": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": ".claude/hooks/check-first-run.sh"
          }
        ]
      }
    ]
  }
}
```

Write the merged file after explicit approval.

### 3.5 Update existing submodules

```bash
git submodule status
```

For each declared submodule:
- Empty? `git submodule update --init --recursive`
- Synced? `git submodule update --remote <path>`

**If the URL in `.gitmodules` isn't what the user actually wants:** ask them. Common case: `shared-context` should point at the team's private repo (e.g., `ai-csl-team-context`), not the public `contextOS-team` template. If unsure, ask the user's team lead. Don't guess.

To change the URL:
```bash
git config --file=.gitmodules submodule.<name>.url <correct-url>
git submodule sync
git submodule update --init --recursive
```

### 3.6 Add missing submodules

If the user's team configuration (per their team lead) includes submodules they don't currently have — add them.

For `lab-data` specifically (AI-CSL lab data):
```bash
# Only if not already declared
grep -q "lab-data" .gitmodules 2>/dev/null || \
  git submodule add https://github.com/botz-pillar/ai-csl-data.git lab-data
git submodule update --init --recursive lab-data 2>/dev/null || true
```

Always ask before adding a new submodule unless the team lead explicitly instructed.

### 3.7 Stage but don't commit yet

```bash
git status
git diff --staged --stat
```

Let the user review before committing.

### 3.8 Restore stash (if any)

```bash
git stash list
# If there's a pre-v2-upgrade stash, pop it
git stash pop
```

Resolve any conflicts with the user.

---

## Phase 4 — Verify

### 4.1 Personal files intact
```bash
ls -la CLAUDE.md my-context.md
head -10 CLAUDE.md    # should show personalized content
head -5 my-context.md
```
If either starts with a template header (like "# CLAUDE.md — ContextOS Personal" or contains `{{PLACEHOLDER}}`), something went wrong — stop and escalate.

### 4.2 Hook works
```bash
.claude/hooks/check-first-run.sh
```
Should produce **no output** (user has `my-context.md`, so the hook is silent). If it outputs the first-run banner, the user's `my-context.md` is missing or unreadable — investigate.

### 4.3 Submodules healthy
```bash
git submodule status
```
All entries should show populated SHAs (not all-zeros or starting with `-`).

### 4.4 Settings valid
```bash
python3 -c "import json; json.load(open('.claude/settings.json'))" && echo "valid JSON"
```

### 4.5 Suggest `/verify`

Tell the user to run the `/verify` slash command in their next Claude session. Expected checklist:
- ✓ CLAUDE.md exists and personalized
- ✓ my-context.md exists and populated
- ✓ SessionStart hook wired + executable
- ✓ Skills present (`skills/onboarding.md`, `skills/prompt-framework.md`, `skills/chunking.md`)
- ✓ Submodule(s) populated
- ✓ Write protection active on `shared-context/`
- ✓ `my-prompts/` directory exists

---

## Phase 5 — Commit & Report

### 5.1 Commit

```bash
git add -A
git status
git commit -m "Upgrade to ContextOS v2 — preserve personal context, add hook + skills + submodules"
```

### 5.2 Final report to the user

Produce a one-page summary:

1. **What changed:** list of files added / updated / merged, and submodule updates
2. **What stayed the same:** `CLAUDE.md`, `my-context.md`, `my-prompts/`, anything else they customized
3. **New capabilities unlocked:**
   - SessionStart hook — if you ever delete `my-context.md`, Claude will cleanly re-onboard you
   - `skills/prompt-framework` — load this when an output misses the mark (Claude will ask which of identity/task/context/constraints/output-format is missing)
   - `skills/chunking` — load this when a task feels too big for one prompt
   - `/verify` — updated health check for v2
4. **Submodule state:** what's now synced and where
5. **How to use the new skills:** one example each, e.g. *"Next time Claude gives you generic output, try: 'Load `skills/prompt-framework` and diagnose what's missing from my last prompt.'"*
6. **Rollback (if needed):** `git reset --hard HEAD~1` to undo (safe only if not yet pushed)
7. **Contact:** "Ping your team lead if anything feels off"

---

## Edge Cases

### User has uncommitted personal work
Stash first (`git stash push -m "pre-v2-upgrade"`). Restore after upgrade. If conflicts on pop, resolve together.

### User's CLAUDE.md has drifted heavily from template
Fine. Leave it. They get new skills + hook without touching their router.

### Submodule redirected locally
If `.git/modules/<submodule>/config` shows a different URL than `.gitmodules`, ask the user which is authoritative. Don't guess.

### User is on a feature branch, not main
`git log HEAD..origin/main` might include unrelated commits. Offer to:
1. Merge `origin/main` into their branch, OR
2. Rebase their branch onto new main

Ask before doing either.

### Upstream has moved past v2.0.0
Check `CHANGELOG.md` for newer versions. If there are breaking changes not covered by this playbook, stop and escalate to the repo maintainer.

### Hook doesn't fire in their Claude session
1. `ls -la .claude/hooks/check-first-run.sh` should show `-rwxr-xr-x`
2. `.claude/settings.json` should have `hooks.SessionStart` pointing at the script
3. Run manually: `.claude/hooks/check-first-run.sh` — should output first-run banner if `my-context.md` is missing
4. If all three are correct but hook still doesn't fire in session, Claude Code may not be picking up the project settings — verify with the user they're running `claude` from the repo root

### Rollback mid-upgrade
If something's broken and you haven't committed:
```bash
git checkout -- <specific files>    # undo specific files
# OR
git reset --hard HEAD               # discard all working-tree changes
git submodule update --init --recursive  # restore submodules
```

If you've committed but not pushed:
```bash
git reset --hard HEAD~1             # undo the last commit
```

**Never force-push.** If they've already pushed, create a revert commit (`git revert HEAD`) instead.

---

## Teaching Mode

Because the user is likely learning Claude Code, narrate what you do:

- Before `git fetch`: *"Fetch downloads new commits from GitHub without changing your working files. Safe to run anytime."*
- Before `git checkout origin/main -- path`: *"This pulls just that one path from the latest upstream commit, without touching anything else."*
- Before editing `settings.json`: *"Hooks are a Claude Code feature — they run shell scripts at certain events. A SessionStart hook runs every time you launch Claude, so we can detect first-run automatically."*
- Before `git submodule update --remote`: *"Submodules are separate repos embedded here. This pulls the latest version from their upstream."*

Keep each explanation short — one or two sentences. You're reinforcing concepts, not lecturing.
