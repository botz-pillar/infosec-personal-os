# Collaboration Guide

> How to contribute shared knowledge back to the team and keep the system current.

---

## How the Two-Repo System Works

| Content | Repo | Who Updates |
|---------|------|-------------|
| Your personal context (`CLAUDE.md`, `my-context.md`) | Your copy of `infosec-personal-os` | You alone |
| Shared team knowledge, workflows, prompts | [`infosec-shared-context`](https://github.com/botz-pillar/infosec-shared-context) | Team via PRs |
| Examples and documentation | `infosec-personal-os` (template repo) | Repo maintainer |

**Your personal files** live in your local copy of infosec-personal-os (gitignored from the template).
**Shared knowledge** lives in a separate repo and is pulled in via git submodule at `shared-context/`.

---

## Contributing to Shared Knowledge

### When to Contribute

You should open a PR when you:
- Discover a tool, technique, or process the team would benefit from
- Write a workflow for a task others also perform
- Find an error or outdated info in shared context
- Create a prompt that produces consistently good results
- Learn something from an incident that should be documented

### How to Contribute

Contributions go to the **shared context repo**, not your personal OS.

1. **Clone the shared context repo directly:**
```bash
git clone https://github.com/botz-pillar/infosec-shared-context.git
cd infosec-shared-context
```

2. **Create a branch and make changes:**
```bash
git checkout -b add-kubernetes-workflow
# Add or edit files
```

3. **Commit and push:**
```bash
git add workflows/kubernetes-security.md
git commit -m "Add Kubernetes security scanning workflow"
git push -u origin add-kubernetes-workflow
```

4. **Open a pull request** on the shared context repo:
   - Title: Clear description of what's being added/changed
   - Body: Why this is useful, who it helps, any context needed
   - Reviewers: Tag at least one team member

5. **After merge, everyone pulls the update:**
```bash
# In your personal OS directory
cd ~/infosec-os
git submodule update --remote
```

---

## PR Guidelines

### Good PRs

- **New workflow:** Clear steps, tested in real work, includes example outputs
- **Tool update:** Accurate information, links to docs, access instructions
- **Prompt addition:** Tested prompt with consistent results, clear placeholders
- **Framework update:** Verified against official documentation, dated
- **Bug fix:** Specific correction with source/reference

### PR Template

```markdown
## What Changed
[Brief description of the change]

## Why
[Why this is useful for the team]

## How I Tested This
[How you verified accuracy — used it in real work, checked against official docs, etc.]

## Checklist
- [ ] Follows existing file format and structure
- [ ] No personal information or credentials included
- [ ] Accurate and verified against authoritative sources
- [ ] Would be useful to at least one other team member
```

### What NOT to Put in PRs

- Personal context or preferences
- Credentials, API keys, or sensitive data
- Unverified information or speculative content
- Company-specific details that shouldn't be in a shared repo
- Draft content that isn't ready for team use

---

## Review Process

### As a Reviewer

When reviewing PRs to shared content:

1. **Accuracy:** Is the information correct? Check against official sources.
2. **Usefulness:** Would this help you or someone on the team?
3. **Consistency:** Does it follow the existing format and structure?
4. **Security:** Does it contain any sensitive information?
5. **Completeness:** Is there enough context for someone to use this?

### Review SLA

- Aim to review PRs within 2 business days
- Simple additions/fixes: 1 reviewer sufficient
- New workflows or major changes: 2 reviewers recommended
- Security guardrail changes: Requires security lead approval

---

## Keeping Shared Context Current

Shared context is a git submodule. Updating is one command:

### Weekly Sync (Recommended)

```bash
cd ~/infosec-os
git submodule update --remote
```

That's it. Your personal files are untouched — only shared context updates.

### What Happens When You Update

- New files the team added appear in `shared-context/`
- Changed files get the latest version
- Your `CLAUDE.md` and `my-context.md` are never affected
- No merge conflicts — submodules update cleanly

---

## Content Maintenance

### Shared Content Owners

Each shared file should have a maintainer:

| File | Maintainer | Review Cadence |
|------|-----------|----------------|
| `team-overview.md` | Security Lead | Quarterly |
| `compliance-frameworks.md` | Compliance Manager | Quarterly + framework updates |
| `tools-and-integrations.md` | Rotates | Monthly |
| `approved-prompts.md` | All contributors | Ongoing |
| `security-guardrails.md` | Security Lead | Quarterly + post-incident |
| `workflows/*` | Original author | Quarterly |

*All of these live in the [infosec-shared-context](https://github.com/botz-pillar/infosec-shared-context) repo.*

### Deprecating Content

If something is outdated:
1. Don't just delete it — open a PR explaining why
2. If replacing, include the replacement in the same PR
3. If the information moved elsewhere, add a redirect note

### Version History

Git handles version history. For major changes, include context in commit messages:

```
Update compliance-frameworks.md for NIST 800-53 Rev 5

- Updated control families to match Rev 5 structure
- Added SR (Supply Chain Risk Management) family
- Updated FedRAMP control counts for Rev 5 baselines
- Source: NIST SP 800-53 Rev 5 (Sept 2020, updated Dec 2024)
```

---

## Ideas for Team Contributions

### Low Effort, High Value
- Fix a typo or outdated tool name
- Add a prompt you use regularly to the approved library
- Update tool versions or access instructions
- Add a link to a useful reference

### Medium Effort, High Value
- Write a workflow for a task you do frequently
- Document a tool integration or MCP server setup
- Create a checklist for a common process
- Add a new example setup for a different role

### Higher Effort, Very High Value
- Build a new shared context file for a topic the team needs
- Create an onboarding checklist for new team members
- Document incident response procedures
- Build automated evidence collection guides

---

## Communication

### Announcing Changes

When your PR is merged:
- Post in the team Slack channel with a brief summary
- Tag people who would benefit most
- Include instructions if anything requires action (e.g., "rebase your branch")

### Requesting Content

If you need content that doesn't exist:
- Open a GitHub issue describing what you need and why
- Tag potential contributors
- Offer to review if someone else writes it

### Feedback on Existing Content

- Found something inaccurate? Open an issue or PR
- Have an improvement idea? Open an issue for discussion first if it's a major change
- Content confusing? Ask in Slack, then PR a clarification

---

## FAQ

**Q: Can I edit shared context files locally?**
A: You can for personal experimentation, but changes won't persist — the next `git submodule update --remote` will overwrite them. To make permanent changes, PR them to the shared context repo.

**Q: What if I disagree with a shared context file?**
A: Open an issue or discuss in Slack. The team decides shared content collaboratively.

**Q: How do I know when shared content has been updated?**
A: Watch the [infosec-shared-context](https://github.com/botz-pillar/infosec-shared-context) repo for notifications, or run `git submodule update --remote` regularly.

**Q: Can I add my own workflows without PRing them?**
A: Yes — put them in a `my-workflows/` folder in your personal OS. Only PR to shared context if they'd benefit others.

**Q: What if I accidentally commit credentials?**
A: Rotate them immediately, then force-push to remove from history (or ask the security lead for help).
