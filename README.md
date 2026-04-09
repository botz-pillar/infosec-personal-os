# ContextOS

> A personal AI operating system for InfoSec teams. Clone it, run setup, start working with Claude Code in 10 minutes.

## Why This Exists

Security practitioners are drowning in context-switching. You jump between SIEM queries, vulnerability reports, compliance artifacts, cloud consoles, and ticket queues — and every time you reach for an AI tool, you start from zero. You re-explain your role, your tools, your environment, your frameworks. Every. Single. Time.

**ContextOS solves this.** It gives Claude Code persistent knowledge of who you are, what you work on, and how your team operates — so you get useful output from the first prompt of every session.

### What it does for you personally:
- **No more re-explaining yourself.** Claude knows your role, your tools, your access levels, your current projects, and how you like to work.
- **Vetted prompts for real security work.** Stop writing prompts from scratch for CVE triage, SIEM queries, compliance evidence, and cloud scanning. Use the team's battle-tested prompt library.
- **Workflows that match your actual job.** Step-by-step procedures for the tasks you do weekly — not generic AI demos, but real SOC triage, real vuln management, real FedRAMP ConMon.

### What it does for your team:
- **Shared knowledge base that stays in sync.** Compliance frameworks, tool inventory, security guardrails, and approved prompts — maintained once, available to everyone.
- **Institutional knowledge that doesn't walk out the door.** When a senior analyst leaves, their workflows and prompt patterns stay.
- **Consistent quality across the team.** Junior analysts get the same prompt templates and guardrails as senior engineers.

### What it takes:
- **10 minutes to set up.** Clone, run the setup script, answer some questions. Done.
- **Zero maintenance burden.** Shared context updates with one command. Personal context is just markdown you edit when things change.

---

## What Is This?

ContextOS is a **context-first AI assistant system** built for security teams. It gives every team member:

- **Personalized AI context** — Claude Code knows your role, tools, projects, and goals
- **Shared team knowledge** — compliance frameworks, tool inventory, approved prompts, guardrails
- **Ready-to-use workflows** — cloud scanning, vuln management, compliance reporting, SOC triage
- **Always in sync** — shared context updates automatically across the whole team

---

## Architecture: Two Repos, One Experience

```
┌─────────────────────────────────────────────────────────┐
│  YOUR Personal OS (this repo)                           │
│                                                         │
│  CLAUDE.md          ← auto-loaded every session         │
│  my-context.md      ← your role, tools, goals           │
│                                                         │
│  shared-context/    ← git submodule (auto-synced)       │
│  ┌─────────────────────────────────────────────────┐    │
│  │  Team Shared Context (separate repo)            │    │
│  │  team-overview.md, compliance-frameworks.md,    │    │
│  │  tools, prompts, guardrails, workflows          │    │
│  └─────────────────────────────────────────────────┘    │
│                                                         │
│  examples/          ← sample completed setups           │
│  docs/              ← guides                            │
└─────────────────────────────────────────────────────────┘
```

| Repo | What It Is | Who Updates It |
|------|-----------|----------------|
| [contextOS-personal](https://github.com/botz-pillar/contextOS-personal) (this repo) | Template for your personal AI context | You (your copy) |
| [contextOS-team](https://github.com/botz-pillar/contextOS-team) | Team knowledge base, workflows, prompts | Team via PRs |

The shared context is included as a **git submodule**. It shows up as a regular `shared-context/` folder. Claude Code reads it seamlessly — no special config needed.

---

## Quick Start (10 Minutes)

### 1. Clone the repo (with shared context)

```bash
git clone --recurse-submodules https://github.com/botz-pillar/contextOS-personal.git ~/context-os
cd ~/context-os
```

### 2. Launch Claude Code

```bash
claude
```

That's it. Claude detects this is your first run, welcomes you, and walks you through a guided setup — asking about your role, tools, projects, and working style via reverse prompting. No scripts to run. Just a conversation.

### 3. Start working

After setup, Claude knows who you are, what you work on, and how to help. Every future session picks up right where your context left off.

**To update shared team context anytime:** `git submodule update --remote`

> **Alternative:** If you prefer a structured terminal questionnaire instead of a conversation with Claude, run `python3 setup.py`. It generates the same files.

---

## Try These First

After setup, try these to see ContextOS in action:

```
# Verify everything is wired up correctly
/verify

# Plan your work session — Claude knows your projects and priorities
/plan

# Draft an email, report, or document — adapted to your audience
/draft

# Research a topic — structured brief with recommendations
/research

# Review your work before you send or submit it
/review
```

Or try a natural prompt:
- *"Summarize my role and current priorities"* — confirms Claude knows who you are
- *"What workflows are available in shared-context?"* — discover what your team has built
- *"Help me prepare for my meeting with [stakeholder] about [topic]"* — uses your project context

---

## What Gets Generated

After setup, your directory looks like this:

```
~/infosec-os/
├── CLAUDE.md                          # YOUR personalized AI context
├── my-context.md                      # Your role, tools, projects, goals
├── shared-context/                    # Team knowledge (git submodule)
│   ├── team-overview.md               #   Team structure and responsibilities
│   ├── compliance-frameworks.md       #   FedRAMP, CMMC, CIS, NIST references
│   ├── tools-and-integrations.md      #   Tool inventory and MCP server docs
│   ├── approved-prompts.md            #   Vetted prompt library for common tasks
│   ├── security-guardrails.md         #   What Claude should/shouldn't do
│   └── workflows/                     #   Step-by-step procedures
│       ├── cloud-security-scan.md
│       ├── vulnerability-analysis.md
│       ├── compliance-reporting.md
│       ├── soc-ticket-triage.md
│       └── risk-assessment.md
├── .claude/commands/                   # Slash commands (type /plan, /draft, etc.)
│   ├── plan.md                        #   Plan a session, project, or deliverable
│   ├── draft.md                       #   Draft emails, reports, documents
│   ├── research.md                    #   Structured research on any topic
│   ├── review.md                      #   Review work before sending
│   ├── verify.md                      #   Setup health check
│   └── whats-new.md                   #   Check for shared context updates
├── my-prompts/                        # Your personal prompt workshop
│   ├── favorites.md                   #   Battle-tested prompts (pre-populated)
│   ├── working-prompts.md             #   Experiments in progress
│   └── contributions/                 #   Ready to PR to the team
├── my-context/                        # Extended personal context (gitignored)
├── examples/                          # Sample completed setups
│   ├── soc-analyst-example/
│   ├── cloud-security-engineer-example/
│   └── compliance-manager-example/
└── docs/                              # Detailed guides
```

---

## How It Works

### Layer 1: Personal Context (yours alone)
Your `CLAUDE.md` and `my-context.md` contain your role, responsibilities, current projects, and preferences. Claude Code loads `CLAUDE.md` automatically every session.

### Layer 2: Shared Team Knowledge (synced across everyone)
The `shared-context/` folder is a git submodule pointing to the team's shared repo. It contains architecture, tools, compliance frameworks, approved prompts, and security guardrails. One `git submodule update --remote` pulls the latest from the team.

### Layer 3: Workflows (reusable procedures)
Workflows live inside `shared-context/workflows/`. Load them when doing the relevant work. They reference both your personal context and shared team knowledge.

---

## Keeping Shared Context Updated

```bash
# Pull latest team knowledge (one command)
git submodule update --remote
```

When someone on the team PRs an update to the shared repo (new workflow, updated prompts, etc.), every team member gets it with that one command.

---

## Team Setup (Team Lead)

Before rolling out to the team, the team lead should customize the shared context:

```bash
git clone https://github.com/botz-pillar/contextOS-team.git
cd contextOS-team
claude
```

Claude detects the uncustomized team context and walks you through setup — team structure, tools, compliance frameworks, SLAs, and guardrails. After setup, commit and push. Your team members get the customized context automatically.

---

## Team Member Onboarding Checklist

- [ ] Clone: `git clone --recurse-submodules https://github.com/YOUR-ORG/contextOS-personal.git ~/context-os`
- [ ] Run: `cd ~/context-os && claude`
- [ ] Answer Claude's setup questions (takes ~10 minutes)
- [ ] Review your generated context — edit `CLAUDE.md` or `my-context.md` if anything's off
- [ ] Try a workflow: ask Claude to load `shared-context/workflows/cloud-security-scan.md`
- [ ] Read `docs/collaboration-guide.md` for contributing back

---

## Documentation

| Guide | What It Covers |
|-------|---------------|
| [Setup Guide](docs/setup-guide.md) | Detailed walkthrough of setup process |
| [Customization Guide](docs/customization-guide.md) | How to tune your personal context |
| [Collaboration Guide](docs/collaboration-guide.md) | Contributing shared knowledge, PR process |

---

## Examples

Check the `examples/` folder for completed setups:

- **SOC Analyst** — Tier 2 analyst focused on alert triage and incident response
- **Cloud Security Engineer** — AWS/Azure security, IaC scanning, cloud posture management
- **Compliance Manager** — FedRAMP/CMMC audit prep, POA&M management, evidence collection

Each example includes a complete `CLAUDE.md` and `my-context.md` showing what a finished setup looks like.

---

## License

MIT — use it, fork it, make it yours.
