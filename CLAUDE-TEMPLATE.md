# CLAUDE.md — {{NAME}}'s ContextOS

> Auto-loaded every session. Routes Claude based on what you're working on. Detailed personal context in `my-context.md`; team context in `shared-context/` (if you're joined to a team).

**Last Updated:** {{SETUP_DATE}}

---

## Who I Am

**{{NAME}}** — {{ROLE}} ({{DOMAIN}}) on the {{TEAM_NAME}} team.

- **Email:** {{EMAIL}}
- **Current focus:** {{FOCUS_AREAS}}
- **This quarter's priority:** {{CURRENT_PRIORITY}}

Full details: [my-context.md](my-context.md).

---

## Routing Table

| Task | Go To | Read | Skills |
|------|-------|------|--------|
| Anything about me personally | — | `my-context.md` | — |
| Team procedures / standards | `shared-context/` | `team-overview.md` + relevant workflow | — |
| Team prompt library for my role | `shared-context/prompts/` | `{{ROLE_PROMPT_FILE}}` | — |
| Execute a team workflow | `shared-context/workflows/` | the relevant workflow | — |
| Integrate a tool | `shared-context/integrations/` | the relevant integration guide | — |
| My personal prompts | `my-prompts/` | `favorites.md` or `working-prompts.md` | — |
| Draft, plan, research, review | (in place) | — | slash commands: `/plan` `/draft` `/research` `/review` |
| Diagnose a bad output | (in place) | — | `prompt-framework` |
| Break a big project into steps | (in place) | — | `chunking` |

---

## Slash Commands

| Command | What It Does |
|---------|--------------|
| `/plan` | Plan a work session, project, or deliverable |
| `/draft` | Draft an email, report, proposal, or document |
| `/research` | Structured research on a topic |
| `/review` | Review work before submitting |
| `/verify` | Setup health check |
| `/whats-new` | Show shared-context updates since last pull |

---

## Naming Conventions

- My files: `lowercase-with-hyphens.md`
- Drafts: `topic_draft.md` → **Final:** `topic_final.md`
- Dated artifacts: `YYYY-MM-DD-topic.md`

---

## What I Want From Claude

{{CLAUDE_EXPECTATIONS}}

## What I Don't Want

- Don't decide for me — surface options and risks, I decide
- Don't hallucinate outputs or tool results — if you can't run it, say so
- Don't store or echo back credentials, API keys, or PII
- Don't write to `shared-context/` — it's team-managed via PRs
{{ADDITIONAL_DONTS}}

---

## Session Start

1. This file loads automatically
2. Check what I'm working on (ask if unclear)
3. Load relevant context as needed
4. Build first, ask second — produce something I can refine

**Quick start:** *"What are we working on today?"*
