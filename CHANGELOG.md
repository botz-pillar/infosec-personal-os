# Changelog

All notable changes to ContextOS Personal are documented here.

If you've forked this repo, check this file when pulling upstream updates to see what's new.

---

## [2.0.0] — 2026-04-14

Major restructure. Template is now domain-neutral. Onboarding is deterministically triggered via a SessionStart hook.

### Breaking
- **InfoSec content moved to `examples/infosec/`.** The core template is domain-neutral. If you were relying on InfoSec-flavored defaults, see `examples/infosec/` for reference.
- **Onboarding mechanism changed.** Previously relied on Claude reading prose instructions in `CLAUDE.md` (which required Claude to interpret and act). Now a SessionStart hook at `.claude/hooks/check-first-run.sh` deterministically detects missing `my-context.md` and injects a trigger. Claude then loads `skills/onboarding.md` to run the flow.
- **`CLAUDE.md` restructured.** Previous version was the setup flow itself. New version is the one-screen master router; setup flow moved to `skills/onboarding.md`.

### Added
- **SessionStart hook** (`.claude/hooks/check-first-run.sh`) — detects first-run and submodule sync issues, injects instructions for Claude
- **`skills/onboarding.md`** — the 7-step flow as a reusable skill
- **`skills/prompt-framework.md`** — five-part structure (Identity / Task / Context / Constraints / Output Format) for diagnosing bad outputs
- **`skills/chunking.md`** — break big projects into single-purpose prompts
- **`docs/common-mistakes.md`** — seven traps to avoid when setting up your folder architecture
- **`examples/README.md`** — overview of available examples + how to contribute new domain flavors
- **"Last Updated" headers** on templates, skills, and docs
- **Routing table** in `CLAUDE.md` and `CLAUDE-TEMPLATE.md` — deterministic task-to-workspace mapping

### Changed
- **`CLAUDE.md`** — shrunk from ~200 lines to ~75; now one-screen routing + rules
- **`CLAUDE-TEMPLATE.md`** — domain-neutral; aligned with `skills/onboarding.md` output shape; uses routing-table pattern
- **`personal-context-template.md`** — domain-neutral; simplified to match what onboarding collects
- **`README.md`** — domain-neutral; explains hook-based onboarding; makes shared submodule explicitly optional for solo users
- **`docs/setup-guide.md`** — updated for hook mechanism; domain-neutral
- **`docs/customization-guide.md`** — domain-neutral examples covering software, marketing, InfoSec
- **`docs/collaboration-guide.md`** — domain-neutral; generic team-repo references

### Known Issues / To-Do
- **`setup.py` is out of sync** with new template structure. It still generates a valid `CLAUDE.md` and `my-context.md`, but the output format matches the old template shape. Recommend using the conversational Claude-native onboarding (primary path) until setup.py is updated. Track: [issue pending].
- **Slash commands in `.claude/commands/`** may reference paths or phrasing that assume the old structure. Audit needed.

### Removed
- **`.gitmodules` unchanged.** `shared-context` and `lab-data` remain as optional submodules. Neither is required for a standalone install.

---

## [1.1.0] — 2026-04-09

### Added
- **Slash commands** — 6 built-in commands: `/plan`, `/draft`, `/research`, `/review`, `/verify`, `/whats-new`
- **Starter prompts** — 5 pre-built in `my-prompts/favorites.md`
- **Extended context directory** — `my-context/` with README guide
- **"Try These First" section** in README
- **MIT LICENSE**
- **CHANGELOG.md**

### Changed
- **README.md** — added setup.py as alternative setup method, added "Try These First"
- **.gitignore** — updated `my-context/` rule to track README.md while ignoring personal files

---

## [1.0.0] — 2026-04-06

### Added
- Initial release of ContextOS Personal (then named `infosec-personal-os`)
- CLAUDE.md with first-run detection and reverse-prompting onboarding (prose-based, no trigger mechanism)
- setup.py interactive terminal questionnaire (alternative setup path)
- Shared team context via git submodule (contextOS-team)
- Three complete InfoSec example setups
- Documentation: setup guide, customization guide, collaboration guide
- Personal prompt workshop (`my-prompts/`)
- Write protection for shared context (`.claude/settings.json` deny rules)
- Templates: `CLAUDE-TEMPLATE.md`, `personal-context-template.md`
