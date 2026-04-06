# Setup Guide

> Detailed walkthrough for setting up your InfoSec Personal OS.

---

## Prerequisites

Before you start, make sure you have:

1. **Git** installed (`git --version`)
2. **Python 3.7+** installed (`python3 --version`)
3. **Claude Code** installed and authenticated
   - Install: `npm install -g @anthropic-ai/claude-code` (or via Homebrew)
   - Authenticate: Run `claude` and follow the login prompts
4. **Access to the team repository** (clone permissions)

---

## Step-by-Step Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-org/infosec-personal-os.git
cd infosec-personal-os
```

### Step 2: Run the Setup Script

```bash
python3 setup.py
```

The script will ask you a series of questions about:

| Section | Questions | Time |
|---------|-----------|------|
| Identity | Name, email, title | 1 min |
| Role | Responsibilities, team, manager | 2 min |
| Tools | Which tools you use daily, proficiency levels | 2 min |
| Projects | Current work, priorities | 2 min |
| Working Style | Preferences, learning goals | 2 min |

**Tips for answering:**
- Be specific — "Splunk SPL queries for alert triage" is better than "SIEM"
- Think about your actual day, not your job description
- Include tools you're learning, not just tools you know
- Mention what frustrates you about current workflows — Claude can help

### Step 3: Review Generated Files

After the script runs, check these files:

1. **`CLAUDE.md`** — Your personalized Claude Code context
   - Read it through. Does it sound like you?
   - Edit anything that's off or add missing details
   - This is what Claude reads every session

2. **`my-context.md`** — Your detailed personal context
   - Review skills, projects, and learning goals
   - This is the deep context — update it as things change

### Step 4: Create Your Personal Branch

```bash
git checkout -b personal/your-name
git add CLAUDE.md my-context.md
git commit -m "Add personal context for [your name]"
```

Your personal context stays on your branch. Shared context stays on `main`.

### Step 5: Test It

```bash
claude
```

Try these test prompts:
- *"Summarize my role and current priorities"* — Claude should know who you are
- *"What tools do I use?"* — Should match your setup answers
- *"Load workflows/soc-ticket-triage.md and help me triage an alert"* — Should load the workflow

### Step 6: Set Up Regular Updates

Your personal branch will fall behind `main` as the team adds shared knowledge. Keep it current:

```bash
# Pull latest shared context
git checkout main
git pull origin main
git checkout personal/your-name
git rebase main
```

Do this weekly or whenever you're notified of shared context updates.

---

## Troubleshooting

### "Claude doesn't seem to know who I am"

- Make sure `CLAUDE.md` is in the root of your working directory
- Make sure you're running `claude` from inside the `infosec-personal-os/` directory
- Check that `CLAUDE.md` has content (not just the template placeholders)

### "The setup script crashed"

- Check Python version: `python3 --version` (needs 3.7+)
- Run with verbose output: `python3 setup.py --verbose` (if supported)
- Manually copy `CLAUDE-TEMPLATE.md` to `CLAUDE.md` and fill in the placeholders

### "I want to change my answers"

- Re-run `python3 setup.py` (it will overwrite your files — back up first if you've made manual edits)
- Or just edit `CLAUDE.md` and `my-context.md` directly — they're just markdown

### "Merge conflicts on rebase"

- Conflicts only happen if you edited shared files (you shouldn't need to)
- If they do happen: keep your personal file changes, accept incoming changes for shared files
- When in doubt: `git checkout --theirs shared-context/` to accept team updates

### "Claude is loading too much context"

- You don't need to load everything every session
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
- Ask Claude: *"Help me customize my InfoSec Personal OS setup"*
