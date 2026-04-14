# CLAUDE.md — ContextOS Personal

> Auto-loaded every session. One-screen router: first-run behavior, routing, rules. Full personal context lives in `my-context.md` (after onboarding). Team context lives in `shared-context/` (optional submodule).

**Last Updated:** 2026-04-14

---

## First-Run Behavior

A SessionStart hook at `.claude/hooks/check-first-run.sh` runs every time Claude Code opens this repo. It checks for `my-context.md`:

- **Not present →** hook injects a trigger; Claude loads [skills/onboarding.md](skills/onboarding.md) and walks the user through a 7-step setup (~10 min). At the end, `my-context.md` and a personalized `CLAUDE.md` are generated.
- **Present →** hook is silent. Normal daily use.

**Manual reset:** delete `my-context.md` and restart the session. Or run `python3 setup.py` for a non-interactive alternative.

---

## Routing Table (Daily Use)

| Task | Go To | Read | Skills |
|------|-------|------|--------|
| Anything about you personally | — | `my-context.md` | — |
| Team procedures or standards | `shared-context/` | `team-overview.md` + relevant workflow | — |
| Use a team prompt library | `shared-context/prompts/` | the role-specific file | — |
| Execute a team workflow | `shared-context/workflows/` | the relevant workflow | — |
| Integrate a tool | `shared-context/integrations/` | the relevant integration guide | — |
| Your personal prompts | `my-prompts/` | `favorites.md` or `working-prompts.md` | — |
| Draft, plan, research, review | (in place) | — | slash commands: `/plan` `/draft` `/research` `/review` |
| Diagnose a bad output / structure a complex ask | (in place) | — | `prompt-framework` |
| Break a big project into chunks | (in place) | — | `chunking` |
| Health check your setup | (in place) | — | `/verify` |

---

## Slash Commands

| Command | What It Does |
|---------|--------------|
| `/plan` | Plan a work session, project, or deliverable |
| `/draft` | Draft an email, report, proposal, or document |
| `/research` | Deep research on any topic with structured output |
| `/review` | Review work before submitting or sending |
| `/verify` | Setup health check |
| `/whats-new` | Show what changed in `shared-context/` since your last pull |

---

## Naming Conventions

- Your files: `lowercase-with-hyphens.md`
- Drafts: `topic_draft.md` → **Final:** `topic_final.md`
- Dated artifacts: `YYYY-MM-DD-topic.md`
- Personal prompts: one prompt per entry in `my-prompts/favorites.md` or `working-prompts.md`

---

## Core Rules

- **Never decide for the user.** Surface options and tradeoffs; they decide.
- **Build first.** Draft something tangible; don't ask when you can produce.
- **Shared context is read-mostly.** Write-deny is enforced via `.claude/settings.json`. Propose changes via PR to the team repo; don't edit `shared-context/` directly.
- **Keep this file tight.** Details belong in `my-context.md`. If `CLAUDE.md` grows past one screen (~50–80 lines), move content out.

---

## Session Start

If no specific task is given, ask: "What are we working on today?" Then route using the table above. For complex asks where output misses the mark, load `skills/prompt-framework.md` to diagnose.
