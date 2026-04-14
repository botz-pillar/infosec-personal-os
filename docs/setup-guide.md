# Setup Guide

> Detailed walkthrough for setting up your ContextOS Personal.

**Last Updated:** 2026-04-14

---

## Prerequisites

1. **Git** installed (`git --version`)
2. **Claude Code** installed and authenticated
   - Install: `npm install -g @anthropic-ai/claude-code` (or via Homebrew)
   - Authenticate: run `claude` and follow the login prompts
3. **Access to your team repo** (if you're joining a team; optional for solo users)

---

## Step 1: Clone

### With a team (includes shared-context submodule)
```bash
git clone --recurse-submodules https://github.com/botz-pillar/contextOS-personal.git ~/context-os
cd ~/context-os
```

### Solo (no team)
```bash
git clone https://github.com/botz-pillar/contextOS-personal.git ~/context-os
cd ~/context-os
```

### Already cloned without `--recurse-submodules`?
```bash
git submodule update --init --recursive
```

If you don't want a team submodule at all, just ignore it — ContextOS Personal works without it.

---

## Step 2: Launch Claude Code

```bash
claude
```

A SessionStart hook (`.claude/hooks/check-first-run.sh`) detects that you haven't onboarded yet (no `my-context.md` exists). It injects a message telling Claude to walk you through setup.

Claude greets you and runs a 7-step flow:

| Step | Covers | Time |
|------|--------|------|
| 1 | Domain & identity (name, title, team, manager) | 1 min |
| 2 | Role & responsibilities (what you actually do) | 2 min |
| 3 | Tools & systems (daily tools, access, MCP servers) | 2 min |
| 4 | Current projects (active, upcoming, recently completed) | 2 min |
| 5 | Skills & learning (strengths, growth, certs) | 2 min |
| 6 | Working style (preferences, dos/don'ts) | 1 min |
| 7 | File generation | — |

**Tips for answering:**
- Be specific. "SPL queries for alert triage in Splunk" beats "SIEM."
- Describe your real day, not your job description.
- Include tools you're learning, not just tools you know.
- Tell Claude what frustrates you — it shapes how Claude helps.

---

## Step 3: Review Generated Files

After the conversation, Claude generates:

**`CLAUDE.md`** — your personalized AI router (replaces the template version). Short; routes Claude based on what you're working on.

**`my-context.md`** — your detailed context. Skills, projects, preferences, learning goals. Edit as your role evolves.

Read them through. Edit anything that's off.

---

## Step 4: Test It

Try:
- *"Summarize my role and current priorities"* — should confirm Claude knows you
- *"What tools do I use?"* — should match your setup answers
- `/verify` — runs the setup health check

If something's wrong, edit the files directly or delete `my-context.md` and re-run `claude` to restart onboarding.

---

## Step 5: Keep Shared Context Updated (if you're on a team)

```bash
git submodule update --remote
```

Do this weekly, or when the team notifies you of updates.

---

## Alternative: Non-Interactive Setup (legacy)

`setup.py` is a terminal questionnaire that ships with the repo. **Status as of v2: legacy fallback.** It still generates working files, but the output shape reflects the v1 template structure, which diverges slightly from v2. The primary path (SessionStart hook + `skills/onboarding.md`) is kept up to date with the templates.

Use `setup.py` only if:
- You can't run the interactive flow (e.g., CI / scripting)
- Claude Code isn't available in your environment

```bash
python3 setup.py
```

After running, compare the generated files against [CLAUDE-TEMPLATE.md](../CLAUDE-TEMPLATE.md) and [personal-context-template.md](../personal-context-template.md) and update as needed.

---

## Troubleshooting

### "Claude doesn't seem to know who I am"

- Confirm `CLAUDE.md` is in the repo root.
- Confirm you're running `claude` from inside the repo.
- Check `my-context.md` exists. If not, the hook will restart onboarding.

### "Claude keeps trying to run setup"

The hook triggers onboarding whenever `my-context.md` doesn't exist. If you already set up, make sure the file wasn't deleted.

### "Shared context is empty"

```bash
git submodule update --init --recursive
```

If that fails, check your access to the team repo and your internet connection.

### "I want to change my answers"

- Edit `CLAUDE.md` and `my-context.md` directly — they're just markdown.
- Or delete `my-context.md` and run `claude` again to re-trigger setup.

### "CLAUDE.md is too long / loading too much"

- Keep `CLAUDE.md` on one screen. Move details to `my-context.md`.
- Workflows load on demand — don't load them all upfront.

### "The hook isn't firing"

- Confirm `.claude/hooks/check-first-run.sh` is executable: `chmod +x .claude/hooks/check-first-run.sh`
- Confirm `.claude/settings.json` references the hook correctly.
- Run the script manually to check output: `.claude/hooks/check-first-run.sh`

---

## What's Next

- [Customization Guide](customization-guide.md) — tune it to how you actually work
- [Collaboration Guide](collaboration-guide.md) — contribute back to the team
- [Common Mistakes](common-mistakes.md) — seven traps to avoid

---

## Getting Help

- Ask in your team's chat channel
- Open an issue on the contextOS-personal repo
- Ask Claude directly: *"Help me customize my ContextOS setup"*
