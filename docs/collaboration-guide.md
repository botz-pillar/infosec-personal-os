# Collaboration Guide

> How to contribute to shared team knowledge and keep the system current.

**Last Updated:** 2026-04-14

---

## The Two-Repo Model

| Content | Lives In | Who Updates |
|---------|----------|-------------|
| Your personal context (`CLAUDE.md`, `my-context.md`, `my-prompts/`) | Your fork of `contextOS-personal` | You alone |
| Shared team knowledge (workflows, prompts, standards) | `contextOS-team` (or your team's equivalent) | Team via PRs |
| Template itself | `contextOS-personal` upstream | Repo maintainer |

**Personal files are yours.** **Shared files are team property.** The boundary is enforced by `.claude/settings.json` — Claude can't write to `shared-context/`.

---

## When to Contribute to Shared Context

Open a PR to the team repo when you:
- Discover a tool, technique, or process the team would benefit from
- Write a workflow for a task others also perform
- Find an error or outdated info in shared content
- Create a prompt that produces consistently good results
- Learn something from an incident or project that should be documented

Keep it in your personal OS when it's:
- Personal preference (your voice, your focus times)
- Specific to your role only
- Experimental or unvetted
- Private (sensitive clients, internal systems not-yet-documented)

---

## Contributing Workflow

Contributions go to the **team repo**, not your personal OS.

1. **Clone the team repo directly:**
   ```bash
   git clone https://github.com/YOUR-ORG/contextOS-team.git
   cd contextOS-team
   ```

2. **Branch:**
   ```bash
   git checkout -b add-onboarding-checklist
   ```

3. **Make changes, commit:**
   ```bash
   git add workflows/onboarding-checklist.md
   git commit -m "Add onboarding checklist workflow"
   git push -u origin add-onboarding-checklist
   ```

4. **Open a PR:**
   - Title: clear description of what's being added
   - Body: why this is useful, who it helps, how you tested it
   - Reviewers: tag at least one team member (two for major changes)

5. **After merge, everyone pulls:**
   ```bash
   cd ~/context-os
   git submodule update --remote
   ```

---

## PR Template

```markdown
## What Changed
[Brief description]

## Why
[Why this helps the team]

## How I Tested This
[Used it in real work / verified against official docs / ran through with teammate X]

## Checklist
- [ ] Follows existing file format and structure
- [ ] No personal information or credentials
- [ ] Accurate and verified against authoritative sources
- [ ] Would help at least one other team member
```

---

## What NOT to PR

- Personal context or preferences
- Credentials, API keys, sensitive data
- Unverified or speculative content
- Company-specific details that shouldn't be team-visible
- Draft content that isn't ready for team use

---

## Review Process

As a reviewer, check:

1. **Accuracy** — verify against official sources
2. **Usefulness** — would this help you or a teammate?
3. **Consistency** — does it follow existing format?
4. **Security** — any sensitive info that shouldn't be in a shared repo?
5. **Completeness** — enough context for someone to use it without asking questions?

**Review SLA (suggested):**
- Simple additions/fixes: 1 reviewer, 1–2 business days
- New workflows or major changes: 2 reviewers, 2–3 days
- Anything touching guardrails/security rules: requires the owner's approval

---

## Keeping Shared Context Current

```bash
git submodule update --remote
```

Weekly cadence works well. When the team announces a meaningful update, pull immediately.

**What happens:** new files appear; changed files get the latest version; your personal files are untouched; no merge conflicts on submodule pulls.

---

## Content Ownership

Each shared file should have a maintainer. Suggested structure (adapt to your team):

| File | Maintainer | Review Cadence |
|------|-----------|----------------|
| `team-overview.md` | Team Lead | Quarterly |
| `tools-and-integrations.md` | Rotating | Monthly |
| `approved-prompts.md` | All contributors | Ongoing |
| `security-guardrails.md` (if applicable) | Security Lead | Quarterly + post-incident |
| `workflows/*` | Original author | Quarterly |

---

## Deprecating Content

Don't just delete. Open a PR explaining why. If replacing, include the replacement in the same PR. If the info moved, add a redirect note.

---

## Ideas for Contributions

### Low effort, high value
- Fix a typo or outdated tool name
- Add a prompt you use regularly to the approved library
- Update tool versions or access instructions

### Medium effort, high value
- Write a workflow for a task you do frequently
- Document a tool integration or MCP server setup
- Add a new example setup for a different role

### Higher effort, very high value
- Build a new shared context file for a topic the team needs
- Create an onboarding checklist for new team members
- Build automated evidence-collection or reporting guides

---

## Communication

**Announcing changes (after merge):**
- Post in team chat with a brief summary
- Tag people who'd benefit most
- Flag anything that requires action (e.g., "rebase your branch")

**Requesting content:**
- Open a GitHub issue describing what you need and why
- Tag potential contributors
- Offer to review if someone else writes it

**Feedback on existing content:**
- Inaccuracy → issue or PR
- Improvement idea → issue to discuss first if major
- Confusing content → ask in chat, then PR clarification

---

## FAQ

**Q: Can I edit shared context files locally?**
A: Read-only by default (`.claude/settings.json` deny rules). You can override for experiments, but changes won't persist — the next `git submodule update --remote` overwrites them. For persistent changes, PR to the team repo.

**Q: What if I disagree with a shared content file?**
A: Open an issue or discuss in team chat. Shared content is decided collaboratively.

**Q: How do I know when shared context was updated?**
A: Watch the team repo for notifications, or run `git submodule update --remote` regularly. The `/whats-new` slash command lists changes since your last pull.

**Q: Can I add my own workflows without PRing them?**
A: Yes. Put them in `my-workflows/` (or anywhere in your personal OS). Only PR to shared if others would benefit.

**Q: What if I accidentally commit credentials?**
A: Rotate them immediately, then force-push to remove from history (or ask your security lead for help).
