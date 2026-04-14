# Prompt Framework — Five-Part Structure

> Load for any complex task where output keeps missing the mark. Use to diagnose what's missing from a prompt.

**Last Updated:** 2026-04-14

---

## The Five Parts

| Part | Question It Answers | Where It Lives |
|------|---------------------|----------------|
| 1. Identity | Who is Claude right now? | Usually handled by `CLAUDE.md` + `my-context.md`. Add inline if shifting roles. |
| 2. Task | What needs to get done? | In the prompt. Specific action + scope + enough detail to start. |
| 3. Context | What does Claude need to know? | Mostly in `my-context.md` and `shared-context/`. Add project-specific detail inline. |
| 4. Constraints | What should Claude avoid? | In the prompt. Every constraint = a mistake prevented. |
| 5. Output Format | What should the result look like? | In the prompt. Table? List? Draft with placeholders? Markdown? |

---

## How to Use

- **Simple ask** (rename, typo, quick lookup): Task only.
- **Creative work** (write, design, brainstorm): Identity + Task + Constraints + Output Format.
- **Complex build** (system, analysis, feature): All five.
- **Ongoing project:** Identity and Context live in your context files. Each prompt carries Task + Constraints + Output Format.

> **Principle:** The folder is memory. The prompt is direction.

---

## Diagnostic Question

When output feels off, ask: *which of the five am I missing?*

| Symptom | Likely Missing |
|---------|----------------|
| Generic tone | Identity |
| Off-topic or making assumptions | Context |
| Annoying quirks (jargon, openers you hate, too long) | Constraints |
| Wrong shape — needs reformatting | Output Format |
| Rambling, shallow across multiple areas | Task too vague — try `chunking` skill |

---

## Worked Example

> **Identity:** You are a technical writer who explains complex topics to non-technical audiences.
>
> **Task:** Write a 300-word explanation of how API keys work and why someone would need one.
>
> **Context:** Audience: professionals new to AI tooling, setting up Claude Code for the first time. Most have never written code.
>
> **Constraints:** No jargon without explaining it. Don't assume server knowledge. Short sentences.
>
> **Output Format:** Start with a one-sentence analogy. Then the concept. Then three setup steps. End with one line of reassurance.

---

## Pairs With

- `skills/chunking.md` — when the task itself is too big for one prompt
- `skills/onboarding.md` — first-run setup (also uses this structure internally)
