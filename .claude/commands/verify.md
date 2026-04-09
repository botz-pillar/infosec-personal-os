Run a ContextOS setup health check. Verify each of the following and report results as a checklist:

1. **CLAUDE.md exists and is personalized** — Check that CLAUDE.md exists in the root directory. If it still contains "First-Run Detection" or "Personal Setup (First Run Only)", it hasn't been personalized yet.

2. **my-context.md exists** — Check that my-context.md exists in the root directory. If it doesn't, setup hasn't been completed.

3. **Shared context submodule is present** — Check that `shared-context/team-overview.md` exists. If the shared-context directory is empty, the submodule needs to be initialized with `git submodule update --init --recursive`.

4. **Shared context has content** — Check that key files exist: `shared-context/compliance-frameworks.md`, `shared-context/security-guardrails.md`, `shared-context/tools-and-integrations.md`, `shared-context/approved-prompts.md`.

5. **Workflows are available** — Check that at least one workflow exists in `shared-context/workflows/`.

6. **Prompt libraries are available** — Check that at least one prompt file exists in `shared-context/prompts/`.

7. **Write protection is active** — Check that `.claude/settings.json` exists and contains deny rules for `shared-context/`.

8. **Personal prompts directory exists** — Check that `my-prompts/` directory exists.

Report format:
- Use checkmarks for passing items and X marks for failing items
- For any failures, include the specific fix command
- End with a summary: "Your ContextOS is [fully operational / needs attention]"
