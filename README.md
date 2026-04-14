# ContextOS Personal

> A personal AI operating system. Clone it, run Claude Code, answer a few questions, start working. Claude remembers who you are across every session.

## Why This Exists

Every time you open an AI tool, you start from zero. You re-explain your role, your work, your preferences. Every. Single. Time.

**ContextOS solves this.** It gives Claude Code persistent knowledge of who you are, what you work on, and how you like to work — so you get useful output from the first prompt of every session.

### What it does for you personally
- **No more re-explaining yourself.** Claude knows your role, your tools, your current projects, and how you prefer to work.
- **A prompt workshop you own.** Save your proven prompts in `my-prompts/`. Experiment without polluting shared team space.
- **Diagnostic skills.** When output misses the mark, ask Claude to "load prompt-framework" — it'll ask which of the five parts (identity / task / context / constraints / output format) is missing.

### What it does for your team (optional)
- **Shared knowledge that stays in sync.** Compliance frameworks, tool inventory, approved prompts, workflows — maintained once in a team repo, available to everyone via git submodule.
- **Institutional knowledge that doesn't walk out the door.** Workflows and prompt patterns outlast any one person.

### What it takes
- **~10 minutes to set up.** Clone, run `claude`, answer questions in a conversation.
- **Zero maintenance burden.** Team context updates with one command. Personal context is just markdown you edit when things change.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│  Your Personal OS (this repo, forked per user)          │
│                                                         │
│  CLAUDE.md          ← auto-loaded every session         │
│  my-context.md      ← your role, tools, goals           │
│  skills/            ← reusable processes                │
│  my-prompts/        ← your prompt workshop              │
│                                                         │
│  shared-context/    ← optional git submodule            │
│  ┌─────────────────────────────────────────────────┐    │
│  │  Team Shared Context (separate repo)            │    │
│  │  Team knowledge, workflows, approved prompts    │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

| Repo | What It Is | Who Updates It |
|------|-----------|----------------|
| [contextOS-personal](https://github.com/botz-pillar/contextOS-personal) (this repo) | Template for your personal AI context | You (your fork) |
| [contextOS-team](https://github.com/botz-pillar/contextOS-team) | Team knowledge base, workflows, prompts | Team via PRs |

The team context is included as a git submodule. Claude Code reads it seamlessly — no special config needed. **You can skip it if you're a solo user** — ContextOS Personal works standalone.

---

## Quick Start

### With a team
```bash
git clone --recurse-submodules https://github.com/botz-pillar/contextOS-personal.git ~/context-os
cd ~/context-os
claude
```

### Solo (no team)
```bash
git clone https://github.com/botz-pillar/contextOS-personal.git ~/context-os
cd ~/context-os
claude
```

### What happens next
A SessionStart hook detects you haven't onboarded yet. Claude greets you and walks through a 7-step setup:

| Step | What it covers | Time |
|------|----------------|------|
| 1 | Domain & Identity | 1 min |
| 2 | Role & responsibilities | 2 min |
| 3 | Tools & systems | 2 min |
| 4 | Current projects | 2 min |
| 5 | Skills & learning | 2 min |
| 6 | Working style | 1 min |
| 7 | File generation | — |

Claude writes your personalized `CLAUDE.md` and a detailed `my-context.md`. From then on, every session picks up where your context left off.

> **Alternative (non-interactive):** `python3 setup.py` runs a terminal questionnaire. Note: `setup.py` is legacy (ships v1 template shape); primary path is the SessionStart hook + `skills/onboarding.md`. Both produce working files, but `setup.py` output may diverge slightly from the new template shape. Use it only if you can't run the interactive flow.

---

## Try These First

After setup:

```
/verify         # confirm your setup is wired correctly
/plan           # plan a work session (Claude uses your projects + priorities)
/draft          # draft an email, report, or document in your voice
/research       # structured research brief with recommendations
/review         # critique your work before sending
/whats-new      # see what changed in shared team context
```

Or try a natural prompt:
- *"Summarize my role and current priorities"* — confirms Claude knows you
- *"What workflows are available in shared-context?"* — discover what the team has built
- *"Help me prepare for my meeting with [stakeholder] about [topic]"* — uses your project context

---

## How It Works

### Layer 1 — Personal Context (yours alone)
`CLAUDE.md` (short, routing-focused) + `my-context.md` (detailed depth) describe you. Claude Code auto-loads `CLAUDE.md` every session.

### Layer 2 — Shared Team Knowledge (optional, synced across team)
`shared-context/` is a git submodule pointing to your team's repo. One `git submodule update --remote` pulls the latest.

### Layer 3 — Skills & Workflows (reusable processes)
- `skills/` — loadable procedures (`onboarding`, `prompt-framework`, `chunking`)
- `shared-context/workflows/` — team-standard procedures for specific work
- `shared-context/prompts/` — role-specific prompt libraries

### Layer 4 — Slash Commands & Hooks (automation)
- `.claude/commands/` — slash commands (`/plan`, `/draft`, etc.)
- `.claude/hooks/` — automation (first-run detection, submodule health check)

---

## What Gets Generated After Setup

```
~/context-os/
├── CLAUDE.md              # Your personalized AI router
├── my-context.md          # Your detailed context (role, tools, projects, goals)
├── my-prompts/            # Your prompt workshop
├── skills/                # Reusable processes
├── shared-context/        # Team knowledge (if joined to a team)
├── .claude/
│   ├── commands/          # Slash commands
│   ├── hooks/             # Automation
│   └── settings.json      # Permissions + hook config
└── examples/              # Reference setups (domain-specific)
```

---

## Keeping Shared Context Updated

```bash
git submodule update --remote
```

When someone on the team PRs an update to the shared repo, every member gets it with that one command.

---

## Team Setup (for team leads)

Before rolling out to the team, customize the team repo:

```bash
git clone https://github.com/botz-pillar/contextOS-team.git
cd contextOS-team
claude
```

Claude detects the uncustomized team context and walks you through setup — team structure, standards, tool inventory, guardrails. Commit and push. Team members get the customized context automatically.

---

## Team Member Onboarding Checklist

- [ ] Clone: `git clone --recurse-submodules https://github.com/YOUR-ORG/contextOS-personal.git ~/context-os`
- [ ] Run: `cd ~/context-os && claude`
- [ ] Answer the 7 setup questions (~10 minutes)
- [ ] Review generated files — edit anything that's off
- [ ] Try a workflow: ask Claude to load `shared-context/workflows/[relevant].md`
- [ ] Read `docs/collaboration-guide.md` for contributing back to the team

---

## Documentation

| Guide | Covers |
|-------|--------|
| [Setup Guide](docs/setup-guide.md) | Detailed walkthrough |
| [Customization Guide](docs/customization-guide.md) | Tuning your personal context |
| [Collaboration Guide](docs/collaboration-guide.md) | Contributing to shared team context |
| [Common Mistakes](docs/common-mistakes.md) | Seven traps to avoid when setting up |

---

## Examples

Reference setups in `examples/`. Currently:

- [`examples/infosec/`](examples/infosec/) — SOC Analyst, Cloud Security Engineer, Compliance Manager

More domain flavors coming. Contributions welcome — see `docs/collaboration-guide.md`.

---

## License

MIT — use it, fork it, make it yours.
