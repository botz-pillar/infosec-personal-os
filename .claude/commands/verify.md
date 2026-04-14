Run a ContextOS setup health check. Verify each of the following and report results as a checklist. Use checkmarks for passing items and X marks for failures. For any failure, include the specific fix command.

1. **CLAUDE.md exists and is personalized** — Check that `CLAUDE.md` exists in the root. If it contains any `{{PLACEHOLDER}}` strings or still starts with `# CLAUDE.md — ContextOS Personal` (the template version), it hasn't been personalized. Fix: run Claude and let the SessionStart hook re-trigger onboarding, or manually delete `my-context.md` to retrigger.

2. **my-context.md exists and is populated** — Check that `my-context.md` exists. If missing, onboarding hasn't run. If present, confirm no `{{PLACEHOLDER}}` strings remain.

3. **SessionStart hook is wired up** — Check that `.claude/settings.json` has a `hooks.SessionStart` entry pointing at `.claude/hooks/check-first-run.sh`. Check that the script is executable (`ls -la .claude/hooks/check-first-run.sh`).

4. **Skills are present** — Check for `skills/onboarding.md`, `skills/prompt-framework.md`, `skills/chunking.md`.

5. **Shared context submodule** (if `.gitmodules` declares it):
   - If declared but `shared-context/` is empty → submodule not synced. Fix: `git submodule update --init --recursive`
   - If declared and populated → confirm the team lead has customized it (look for any `{{PLACEHOLDER}}` in `shared-context/team-overview.md`, `shared-context/tools-and-integrations.md`, or `shared-context/guardrails.md`). If placeholders present, ping the team lead.
   - If not declared → skip (user is solo, no team).

6. **Write protection on shared-context** — Confirm `.claude/settings.json` contains deny rules for `Edit(shared-context/**)` and `Write(shared-context/**)`. Only relevant if a team submodule is in use.

7. **Personal prompts directory exists** — Check `my-prompts/` directory exists, with `favorites.md` and/or `working-prompts.md`.

8. **Domain examples present** — Check that `examples/` exists with at least one subdirectory (e.g., `examples/infosec/`). These are reference-only; their absence isn't a failure, just a note.

End with a summary: "Your ContextOS is [fully operational / needs attention: (list of specific issues)]".
