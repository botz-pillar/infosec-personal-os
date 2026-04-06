# Customization Guide

> How to tune your InfoSec Personal OS to match exactly how you work.

---

## The Two Files That Matter Most

### `CLAUDE.md` — Your AI Interface
This is what Claude reads first, every session. Think of it as your elevator pitch to an extremely capable assistant who has amnesia.

**Keep it:**
- Concise (under 200 lines is ideal)
- Current (update when projects or priorities change)
- Honest (include what you're learning, not just what you know)

**Structure:**
```
Who I Am        → Identity, role, current priority (5 lines)
Responsibilities → What you actually do day-to-day (bullet list)
Tools           → What you use, what access you have
Current Projects → Active work with enough context to be useful
How I Work      → Style preferences, what you want/don't want from Claude
Context Loading  → Pointers to shared context and workflows
Learning Goals  → What you're working toward
```

### `my-context.md` — Your Deep Context
This is the detailed file. Claude reads it when more context is needed. You reference it from `CLAUDE.md`.

**Keep it:**
- Detailed (as long as it needs to be)
- Structured (clear sections with headers)
- Updated (quarterly at minimum)

---

## Customization Areas

### 1. Role-Specific Instructions

The "What I Need From Claude" and "What I Don't Want" sections are the most important customizations. Be specific:

**Generic (less useful):**
```
- Help me with security tasks
- Don't make mistakes
```

**Specific (much better):**
```
- Help me build SPL queries for CrowdStrike log correlation in Splunk
- Don't suggest remediation actions without including the verification step
- Always map findings to MITRE ATT&CK techniques when analyzing alerts
- When reviewing Terraform, check for CIS Benchmark violations first
```

### 2. Tool-Specific Context

List the tools you actually use with enough detail that Claude knows how to help:

```markdown
### Splunk
- Version: 9.x
- My role: Power User (search, alerts, dashboards — no admin)
- Query language: SPL
- Key indexes: main, security, cloudtrail, waf
- Common searches: authentication failures, outbound connections, privilege escalation
- I prefer: Optimized queries with comments explaining each step
```

### 3. Project Context

Keep current projects updated with enough context to be actionable:

```markdown
### CSPM Rollout (Phase 2)
- **Goal:** Prowler scanning across all 12 AWS accounts
- **Status:** Dev/staging complete, production accounts next
- **Blockers:** Need cross-account IAM role in prod-finance account
- **Deadline:** End of quarter
- **Key decisions:** Using centralized S3 for scan results, EventBridge for alerting
```

### 4. Working Style Preferences

These shape how Claude interacts with you. Examples:

```markdown
- Show me the command/code first, explain after
- I prefer tables over paragraphs for structured data
- When I ask for help with a query, start with the simplest version, then optimize
- Don't summarize what I already told you — just respond to it
- If something requires more than 3 steps, break it into a checklist
- Use MITRE ATT&CK technique IDs when discussing threats
```

### 5. Custom Workflows

If the shared workflows don't cover your use case, create your own:

1. Create a new file in `my-workflows/` (e.g., `my-workflows/siem-queries.md`)
2. Follow the same structure as existing workflows
3. Reference it in your `CLAUDE.md` context loading table
4. If it's useful for others, PR it to the [shared context repo](https://github.com/botz-pillar/infosec-shared-context)

---

## Adding MCP Servers

MCP servers give Claude direct access to tools. To add one:

1. Install the server:
```bash
npm install -g @modelcontextprotocol/server-github
```

2. Configure in `~/.claude/settings.json`:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "your-token-here"
      }
    }
  }
}
```

3. Update your `CLAUDE.md` MCP section:
```markdown
### MCP Servers Available
- **GitHub** — PR reviews, issue management, code search
```

4. Restart Claude Code and verify

### Security Notes for MCP
- Use read-only tokens when possible
- Never commit MCP credentials to this repo
- Review MCP server permissions before enabling
- See `shared-context/security-guardrails.md` for full guidelines

---

## Keeping Things Current

### Weekly
- Update "Current Projects" in `CLAUDE.md` if priorities shifted
- Remove completed projects, add new ones

### Monthly
- Review and update `my-context.md` skills and learning sections
- Check if your tool list has changed
- Update certifications progress

### Quarterly
- Full review of both files
- Update learning goals based on progress
- Review shared context for accuracy and contribute updates

### After Major Changes
- New role or responsibilities → Update both files immediately
- New tool adopted → Add to tool list with context
- Project completion → Move to completed, add new projects
- Certification achieved → Update certs list, set new goals

---

## Advanced Customizations

### Custom Context Files

Create additional context files for specific work areas:

```
my-context/
├── aws-accounts.md          # Your AWS account inventory and access
├── investigation-notes.md   # Ongoing investigation context
├── vendor-contacts.md       # Key vendor relationships
└── architecture-notes.md    # System architecture reference
```

Reference them from `CLAUDE.md`:
```markdown
### Additional Context (load when relevant)
- `my-context/aws-accounts.md` — AWS account inventory and access levels
- `my-context/investigation-notes.md` — Context for ongoing investigations
```

### Aliases and Quick Commands

Add instructions for common session starts:

```markdown
## Quick Starts

- **"ConMon mode"** → Load compliance-reporting workflow, focus on monthly deliverables
- **"Triage mode"** → Load soc-ticket-triage workflow, focus on alert queue
- **"Hunting mode"** → Load threat hunting queries, set scope for investigation
- **"Audit prep"** → Load compliance-reporting workflow, focus on evidence collection
```

### Per-Project Context

For long-running projects, create a context file:

```markdown
# Project: CSPM Rollout

## Status
Phase 2 of 3. Dev/staging complete.

## Architecture
- Prowler runs via CodeBuild in security account
- Results stored in S3: s3://security-scan-results/prowler/
- Findings routed via EventBridge to SNS → Slack + Jira
- Dashboard in Security Hub custom insights

## Decisions Made
- Centralized scanning model (not distributed per-account)
- Prowler v3 (not v4 — waiting for stability)
- Weekly full scan, daily delta for high-severity checks

## Open Questions
- Cross-account role for prod-finance (pending approval)
- Retention period for scan results (propose 1 year)
```

---

## Tips

1. **Less is more in `CLAUDE.md`** — Claude has limited context. Keep the main file tight and use references for deep context.
2. **Write for a smart stranger** — Claude doesn't remember previous sessions. Context needs to stand alone.
3. **Test your changes** — After editing, start a new Claude session and ask it to summarize your role. Does it get it right?
4. **Steal from examples** — Check the `examples/` folder for ideas from other roles.
5. **Iterate** — Your first version won't be perfect. Use it for a week, then refine based on what Claude gets wrong.
