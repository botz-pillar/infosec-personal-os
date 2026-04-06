# InfoSec Personal OS

> A personal AI operating system for InfoSec teams. Clone it, run setup, start working with Claude Code in 10 minutes.

## What Is This?

InfoSec Personal OS is a **context-first AI assistant system** built for security teams. It gives every team member:

- **Personalized AI context** — Claude Code knows your role, tools, projects, and goals
- **Shared team knowledge** — compliance frameworks, tool inventory, approved prompts, guardrails
- **Ready-to-use workflows** — cloud scanning, vuln management, compliance reporting, SOC triage
- **Version-controlled collaboration** — update shared knowledge via PRs, keep personal context private

Think of it as your team's collective security brain, personalized to each individual.

---

## Quick Start (10 Minutes)

### 1. Clone the repo

```bash
git clone https://github.com/your-org/infosec-personal-os.git
cd infosec-personal-os
```

### 2. Run the setup script

```bash
python3 setup.py
```

The script asks you questions about your role, tools, and goals, then generates your personalized `CLAUDE.md` and context files.

### 3. Start using Claude Code

```bash
claude
```

Claude Code auto-loads your `CLAUDE.md` and knows who you are, what you work on, and how to help.

---

## What Gets Generated

After setup, your repo looks like this:

```
infosec-personal-os/
├── CLAUDE.md                    # YOUR personalized AI context (auto-generated)
├── my-context.md                # Your role, tools, projects, goals
├── shared-context/              # Team knowledge (shared across everyone)
│   ├── team-overview.md         # Team structure and responsibilities
│   ├── compliance-frameworks.md # FedRAMP, CMMC, CIS, NIST references
│   ├── tools-and-integrations.md# Tool inventory and MCP server docs
│   ├── approved-prompts.md      # Vetted prompt library for common tasks
│   └── security-guardrails.md   # What Claude should/shouldn't do
├── workflows/                   # Step-by-step procedures
│   ├── cloud-security-scan.md
│   ├── vulnerability-analysis.md
│   ├── compliance-reporting.md
│   ├── soc-ticket-triage.md
│   └── risk-assessment.md
├── examples/                    # Sample completed setups
│   ├── soc-analyst-example/
│   ├── cloud-security-engineer-example/
│   └── compliance-manager-example/
└── docs/                        # Detailed guides
    ├── setup-guide.md
    ├── customization-guide.md
    └── collaboration-guide.md
```

---

## How It Works

### Layer 1: Personal Context (yours alone)
Your `CLAUDE.md` and `my-context.md` contain your role, responsibilities, current projects, and preferences. Claude Code loads this automatically every session.

### Layer 2: Shared Team Knowledge (everyone shares)
The `shared-context/` folder contains team-wide knowledge: architecture, tools, compliance frameworks, approved prompts, and security guardrails. Everyone references the same files.

### Layer 3: Workflows (reusable procedures)
The `workflows/` folder contains step-by-step instructions for common tasks. Load them when doing the relevant work. They reference both your personal context and shared team knowledge.

---

## Branching Strategy

```
main              ← Shared team knowledge (PRs only)
├── personal/NAME ← Your personal context (your branch)
└── feature/X     ← New workflows or shared knowledge (PR to main)
```

- **Never push personal context to `main`** — keep it on your personal branch
- **Shared knowledge updates** go through PRs so the team can review
- **Rebase your personal branch** on main regularly to pick up team updates

---

## Team Onboarding Checklist

- [ ] Clone the repository
- [ ] Run `python3 setup.py` and answer the questions
- [ ] Review your generated `CLAUDE.md` — edit anything that's off
- [ ] Create your personal branch: `git checkout -b personal/YOUR-NAME`
- [ ] Commit your personal context to your branch
- [ ] Test with Claude Code: run `claude` and ask it to summarize your role
- [ ] Try a workflow: load `workflows/cloud-security-scan.md` and run through it
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
