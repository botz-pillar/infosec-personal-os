# Collaboration Guide

> How to contribute shared knowledge back to the team and keep the system current.

---

## How Shared vs. Personal Content Works

| Content Type | Location | Branch | Who Updates |
|-------------|----------|--------|-------------|
| Your personal context | `CLAUDE.md`, `my-context.md` | `personal/your-name` | You alone |
| Shared team knowledge | `shared-context/*` | `main` | Anyone via PR |
| Workflows | `workflows/*` | `main` | Anyone via PR |
| Examples | `examples/*` | `main` | Anyone via PR |
| Documentation | `docs/*` | `main` | Anyone via PR |

**Rule:** Your personal files stay on your branch. Everything else goes through PRs to `main`.

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

1. **Create a feature branch from main:**
```bash
git checkout main
git pull origin main
git checkout -b feature/add-kubernetes-workflow
```

2. **Make your changes:**
   - Add new files or edit existing shared files
   - Follow existing formatting and structure
   - Include enough context for someone unfamiliar with the topic

3. **Commit and push:**
```bash
git add shared-context/new-file.md  # or whatever you changed
git commit -m "Add Kubernetes security scanning workflow"
git push -u origin feature/add-kubernetes-workflow
```

4. **Open a pull request:**
   - Title: Clear description of what's being added/changed
   - Body: Why this is useful, who it helps, any context needed
   - Reviewers: Tag at least one team member

5. **After merge, update your personal branch:**
```bash
git checkout personal/your-name
git rebase main
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

## Keeping Your Branch Current

Your personal branch (`personal/your-name`) will diverge from `main` as the team adds content. Stay current:

### Weekly Sync (Recommended)

```bash
git checkout main
git pull origin main
git checkout personal/your-name
git rebase main
```

### Handling Conflicts

Conflicts should be rare (you're editing personal files, team edits shared files). If they happen:

1. Read the conflict carefully
2. For shared files: Accept the incoming (`main`) version
3. For your personal files: Keep your version
4. Test after resolving: `claude` → "Summarize my role"

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

**Q: Can I edit shared files on my personal branch?**
A: You can, but your edits won't be visible to others until PRed to `main`. If it's useful for everyone, PR it.

**Q: What if I disagree with a shared context file?**
A: Open an issue or discuss in Slack. The team decides shared content collaboratively.

**Q: How do I know when shared content has been updated?**
A: Watch the repo for notifications, or check `git log main -- shared-context/` periodically.

**Q: Can I add my own workflows without PRing them?**
A: Yes — put them in a `my-workflows/` folder on your personal branch. Only PR if they'd benefit others.

**Q: What if I accidentally push personal context to main?**
A: Ask the security lead to help revert. If it contained credentials, rotate them immediately.
