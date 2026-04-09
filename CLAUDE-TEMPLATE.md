# CLAUDE.md — {{NAME}}'s ContextOS

> This file is auto-loaded by Claude Code every session. It tells Claude who you are, what you work on, and how to help you.

---

## Who I Am

**{{NAME}}** — {{ROLE}} on the {{TEAM_NAME}} team.

- **Email:** {{EMAIL}}
- **Focus areas:** {{FOCUS_AREAS}}
- **Current priority:** {{CURRENT_PRIORITY}}

---

## My Role & Responsibilities

{{RESPONSIBILITIES}}

---

## My Tools & Systems

### Primary Tools
{{PRIMARY_TOOLS}}

### Access & Permissions
{{ACCESS_LEVELS}}

### MCP Servers Available
{{MCP_SERVERS}}

---

## Current Projects

{{CURRENT_PROJECTS}}

---

## How I Work

### Preferred Working Style
{{WORKING_STYLE}}

### What I Need From Claude
{{CLAUDE_EXPECTATIONS}}

### Slash Commands

Type any of these to activate a workflow:

| Command | What It Does |
|---------|-------------|
| `/plan` | Plan a work session, project, or deliverable |
| `/draft` | Draft an email, report, proposal, or document |
| `/research` | Deep research on any topic with structured output |
| `/review` | Review your work before submitting or sending |
| `/verify` | Check that your ContextOS setup is healthy |
| `/whats-new` | See what changed in shared team context |

### What I Don't Want
- Don't make security decisions for me — surface options and risks, I decide
- Don't hallucinate tool outputs or scan results — if you can't run it, say so
- Don't skip security guardrails (see `shared-context/security-guardrails.md`)
- Don't store or echo back credentials, API keys, or PII
- **Don't write to `shared-context/`** — it's a read-only submodule managed by the team via PRs
{{ADDITIONAL_DONTS}}

---

## Context Loading

### Personal Context
- `my-context.md` — My detailed role, skills, learning goals, and preferences

### Shared Team Knowledge
- `shared-context/team-overview.md` — Team structure and responsibilities
- `shared-context/compliance-frameworks.md` — FedRAMP, CMMC, CIS, NIST references
- `shared-context/tools-and-integrations.md` — Tool inventory and integration docs
- `shared-context/approved-prompts.md` — Vetted prompts for common tasks
- `shared-context/security-guardrails.md` — Security constraints and rules

### Workflows (load when doing the work)
| Workflow | When to Use |
|----------|-------------|
| `shared-context/workflows/cloud-security-scan.md` | Running or reviewing cloud security scans |
| `shared-context/workflows/vulnerability-analysis.md` | Triaging or analyzing vulnerabilities |
| `shared-context/workflows/compliance-reporting.md` | Generating compliance reports or evidence |
| `shared-context/workflows/soc-ticket-triage.md` | Triaging SOC alerts or tickets |
| `shared-context/workflows/risk-assessment.md` | Conducting risk assessments |

---

## Learning Goals

{{LEARNING_GOALS}}

---

## Session Start

At the start of any session:
1. This file loads automatically
2. Check what I'm working on (ask if unclear)
3. Load relevant shared context and workflows as needed
4. Build first, ask second — produce something I can refine

**Quick start:** *"What are we working on today?"*
