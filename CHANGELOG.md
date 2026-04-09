# Changelog

All notable changes to ContextOS-Personal are documented here.

If you've forked this repo, check this file when pulling upstream updates to see what's new.

---

## [Unreleased]

### Added
- **Slash commands** — 6 built-in commands for common professional workflows:
  - `/plan` — Plan a work session, project, or deliverable
  - `/draft` — Draft emails, reports, proposals, or documents
  - `/research` — Structured research on any topic
  - `/review` — Review work before submitting or sending
  - `/verify` — Setup health check
  - `/whats-new` — Check for shared context updates from the team
- **Starter prompts** — 5 pre-built prompts in `my-prompts/favorites.md` covering role summary, workflow discovery, meeting prep, status updates, and decision frameworks
- **Extended context directory** — `my-context/` with README guide for adding deep context files
- **"Try These First" section** in README — immediate next steps after setup
- **MIT LICENSE file** — proper open source licensing
- **CHANGELOG.md** — this file

### Changed
- **README.md** — Added setup.py as alternative setup method, added "Try These First" section
- **.gitignore** — Updated `my-context/` rule to track README.md template while ignoring personal files

---

## [1.0.0] — 2026-04-06

### Added
- Initial release of ContextOS-Personal
- CLAUDE.md with first-run detection and reverse-prompting onboarding
- setup.py interactive terminal questionnaire (alternative setup path)
- Shared team context via git submodule (contextOS-team)
- Three complete example setups: SOC Analyst, Cloud Security Engineer, Compliance Manager
- Documentation: setup guide, customization guide, collaboration guide
- Personal prompt workshop (`my-prompts/`)
- Write protection for shared context (`.claude/settings.json` deny rules)
- Templates: CLAUDE-TEMPLATE.md, personal-context-template.md
