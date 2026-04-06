# Setup Guide

> Detailed walkthrough for setting up your ContextOS.

---

## Prerequisites

Before you start, make sure you have:

1. **Git** installed (`git --version`)
2. **Claude Code** installed and authenticated
   - Install: `npm install -g @anthropic-ai/claude-code` (or via Homebrew)
   - Authenticate: Run `claude` and follow the login prompts
3. **Access to the team repository** (clone permissions)

---

## Step-by-Step Setup

### Step 1: Clone the Repository (with shared context)

```bash
git clone --recurse-submodules https://github.com/YOUR-ORG/contextOS-personal.git ~/context-os
cd ~/context-os
```

The `--recurse-submodules` flag automatically pulls the shared team context into `shared-context/`.

If you already cloned without that flag:
```bash
git submodule update --init --recursive
```

### Step 2: Launch Claude Code

```bash
claude
```

Claude detects that this is your first time (no `my-context.md` exists yet) and automatically starts the onboarding flow. It will ask you questions in sections:

| Section | What Claude Asks | Time |
|---------|-----------------|------|
| Identity | Name, email, title, team, manager | 1 min |
| Role & Responsibilities | What you actually do day-to-day, priorities, focus areas | 2 min |
| Tools & Systems | What you use, access levels, proficiency | 2 min |
| Current Projects | Active work, upcoming, recently completed | 2 min |
| Skills & Learning | Strengths, growth areas, certs, goals | 2 min |
| Working Style | Preferences, what you want/don't want from Claude | 1 min |

**Tips for answering:**
- Be specific — "Splunk SPL queries for alert triage" is better than "SIEM"
- Think about your actual day, not your job description
- Include tools you're learning, not just tools you know
- Tell Claude what frustrates you — it'll shape how it helps

### Step 3: Review Generated Files

After the conversation, Claude generates two files:

1. **`CLAUDE.md`** (updated) — Your personalized AI context
   - This replaces the onboarding router with your personal context
   - Read it through. Does it sound like you?
   - Edit anything that's off or add missing details

2. **`my-context.md`** (new) — Your detailed personal context
   - Review skills, projects, and learning goals
   - Update as things change

### Step 4: Test It

Try these prompts:
- *"Summarize my role and current priorities"* — Claude should know who you are
- *"What tools do I use?"* — Should match your setup answers
- *"Load shared-context/workflows/soc-ticket-triage.md and help me triage an alert"* — Should load the workflow

### Step 5: Keep Shared Context Updated

When the team updates shared knowledge, pull the latest:

```bash
git submodule update --remote
```

Do this weekly or whenever you're notified of shared context updates.

---

## Alternative: Script-Based Setup

If you prefer a non-interactive setup, you can also run:

```bash
python3 setup.py
```

This runs a guided questionnaire in the terminal and generates the same files. Use this if you want a faster, more structured setup experience.

---

## Troubleshooting

### "Claude doesn't seem to know who I am"

- Make sure `CLAUDE.md` is in the root of your working directory
- Make sure you're running `claude` from inside your `context-os/` directory
- Check that `my-context.md` exists (if not, Claude will re-run setup)

### "Claude is trying to run setup again"

- Claude triggers setup when `my-context.md` doesn't exist
- If you've already set up, make sure `my-context.md` is in the root directory
- If it was accidentally deleted, re-run setup or recreate it manually

### "Shared context is empty"

- Run `git submodule update --init --recursive`
- If that doesn't work, check your internet connection and access to the shared repo

### "I want to change my answers"

- Edit `CLAUDE.md` and `my-context.md` directly — they're just markdown
- Or delete `my-context.md` and run `claude` again to re-trigger setup

### "Claude is loading too much context"

- `CLAUDE.md` loads automatically — keep it concise
- Workflows load on demand — only reference the one you're using
- If `CLAUDE.md` is too long, move details to `my-context.md` and reference it

---

## What's Next

After setup, read:
- [Customization Guide](customization-guide.md) — Make it truly yours
- [Collaboration Guide](collaboration-guide.md) — Contribute back to the team

---

## Getting Help

- Ask in the team Slack channel
- Open an issue on the repository
- Ask Claude: *"Help me customize my ContextOS setup"*
