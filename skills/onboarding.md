# Onboarding — First-Run Setup Flow

> Load this skill when setting up ContextOS for the first time. Collects answers across 7 steps (~10 min), then generates `my-context.md` and a personalized `CLAUDE.md`.

**Last Updated:** 2026-04-14

---

## When to Use

The SessionStart hook at `.claude/hooks/check-first-run.sh` triggers this automatically when `my-context.md` is missing. Invoke manually when:
- The user says "start onboarding" or "re-run setup"
- The user deletes `my-context.md` and restarts

---

## How to Run It

Be conversational. Ask one step at a time. Wait for an answer before moving on. Be encouraging. If a user gives a short or unclear answer, probe once — then accept what they give and move on.

### Step 0: Welcome

Open with something like:

> Welcome to ContextOS. I'm going to ask you some questions to build your personal AI context. About 10 minutes. It makes every future session dramatically more useful.
>
> I'll ask in batches. Answer as specifically as you can — the more I know about your real work, the better I can help.
>
> Ready? Let's start.

### Step 1: Domain & Identity

First question — this shapes everything else:

> What domain are you working in? (e.g., software engineering, InfoSec, marketing, research, consulting, product, data science, healthcare, legal, education, finance, something else.)

Use their answer to tune vocabulary and examples for the remaining steps. Then ask:

1. Full name?
2. Work email?
3. Job title?
4. Team or department?
5. Who do you report to (name + title)?
6. How long in this role?

### Step 2: Role & Responsibilities

> Describe what you actually do day-to-day. Not your job description — your real work. What does a typical day look like?

Probes:
- Top 2–3 focus areas right now?
- Single biggest priority this quarter?
- Main responsibilities? (list them)

### Step 3: Tools & Systems

> What tools do you use daily? For each: what you use it for, and comfort level (beginner / intermediate / expert).

Probes:
- What systems or platforms do you have access to?
- Access level (admin, read-only, power user, etc.)?
- Any MCP servers configured for Claude Code? (If they don't know what MCP is, say: "We can set those up later.")

### Step 4: Current Projects

> What are you actively working on right now? Project name + one-line status for each.

Probes:
- What's coming up next?
- Anything recently finished that gives context for current work?

### Step 5: Skills & Learning

> What are you strongest in? What are you actively growing?

Probes:
- Certifications earned?
- Certifications targeting (with target dates)?
- What are you trying to learn this quarter?

### Step 6: Working Style

> How do you prefer to work with AI tools? What should I do well for you? And what should I absolutely NOT do?

Probes:
- Best focus time?
- Short and direct, or detailed explanations?
- Preferred way to receive feedback?
- Anything else about how you work?

### Step 7: Generate Files

After all answers are collected, produce two files:

**1. `my-context.md`** — follow the structure of `personal-context-template.md`. Fill every `{{PLACEHOLDER}}` with the user's real answer. Leave no placeholders in the output.

**2. `CLAUDE.md`** — follow the structure of `CLAUDE-TEMPLATE.md`. Fill placeholders. The result replaces the template version that shipped with the repo.

Before writing either file, scan your draft for any remaining `{{PLACEHOLDER}}` strings. If any exist, ask the user for the missing info before writing.

### Step 8: Confirm

Tell the user:

> Your ContextOS is set up. Here's what I captured:
>
> [Brief summary — role, focus areas, primary tools, current priority]
>
> I created:
> - `my-context.md` — your detailed personal context
> - `CLAUDE.md` — your personalized router (replaces the template version)
>
> Try asking me something about your work — I already know who you are.

If they're joined to a team (i.e., `shared-context/` is populated):

> To pull the latest shared team context: `git submodule update --remote`

---

## Edge Cases

- **User skips a step:** note `(not provided)` in the generated file; continue.
- **User quits mid-flow:** next session will re-trigger onboarding because `my-context.md` still doesn't exist. Start fresh at Step 0; they may say "same as last time."
- **Partial setup already exists** (CLAUDE.md personalized but `my-context.md` missing): don't overwrite CLAUDE.md without explicit confirmation.
- **No shared-context submodule** (solo user, or not cloned with `--recurse-submodules`): fine. Skip shared-context references in generated files. If the submodule exists but is empty, point the user at `git submodule update --init --recursive`.
- **User wants a different domain flavor:** if they're InfoSec, browse `examples/infosec/` for reference. Other domains can be added as examples in later releases.

---

## Pairs With

- [skills/prompt-framework.md](prompt-framework.md) — once onboarded, this is how to structure complex asks
- [skills/chunking.md](chunking.md) — for breaking big projects into steps
- [CLAUDE-TEMPLATE.md](../CLAUDE-TEMPLATE.md) — the template being filled
- [personal-context-template.md](../personal-context-template.md) — the template being filled
