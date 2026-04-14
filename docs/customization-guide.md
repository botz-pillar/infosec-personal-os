# Customization Guide

> How to tune your ContextOS to match how you actually work.

**Last Updated:** 2026-04-14

---

## The Two Files That Matter Most

### `CLAUDE.md` — your AI router

What Claude reads first, every session. Short. Routing-focused. Think of it as an elevator pitch to an extremely capable assistant with amnesia.

**Keep it:**
- On one screen (~50–80 lines)
- Current (update when projects or priorities change)
- Honest (include what you're learning, not just what you know)

**Should contain:**
- Who you are (one paragraph)
- Routing table (where to go for what task)
- Slash commands
- Naming conventions
- What you want / don't want from Claude
- Session start behavior

### `my-context.md` — your deep context

Where the details live. Claude loads it when it needs depth beyond `CLAUDE.md`.

**Keep it:**
- Detailed (as long as it needs to be)
- Structured (clear sections)
- Updated (at least quarterly)

---

## High-Leverage Customizations

### 1. What You Want / Don't Want From Claude

The most impactful edits. Be specific. Every constraint you add is a mistake prevented.

**Generic (less useful):**
```
- Help me with my work
- Don't make mistakes
```

**Specific (much better), from various domains:**

```
# Software engineer
- Always include TypeScript types on new functions
- Show the diff inline before writing the full file
- When suggesting a refactor, list one alternative approach and why you chose this one

# Marketing strategist
- When drafting copy, give me three variations at different tones
- Don't use "unlock," "revolutionize," or "game-changer"
- Always tag the CTA — is it awareness, consideration, or conversion?

# InfoSec analyst
- Map findings to MITRE ATT&CK when analyzing alerts
- Don't suggest remediation without including the verification step
- When reviewing Terraform, check CIS Benchmark violations first
```

### 2. Tool-Specific Context

List tools with enough detail that Claude knows how to help:

```markdown
### Splunk
- Version: 9.x
- My role: Power User (search, alerts, dashboards — no admin)
- Query language: SPL
- Key indexes: main, security, cloudtrail, waf
- Preference: optimized queries with comments explaining each step

### Notion
- Primary DB: Tasks (properties: Status, Priority, Due, Project)
- Use it for: weekly planning, project tracking, meeting notes
- Preference: always link new pages to parent project
```

### 3. Project Context

Keep current projects actionable:

```markdown
### Q2 Product Launch
- **Goal:** Ship feature X to all users by May 15
- **Status:** Beta in progress with 3 customers
- **Blockers:** Analytics schema change pending DS review
- **Key decisions:** Feature-flagged rollout, 10%/50%/100%
```

### 4. Working Style Preferences

Shape how Claude interacts with you:

```markdown
- Show me the command/code first, explain after
- Prefer tables over paragraphs for structured data
- Start with the simplest version, then optimize
- Don't summarize what I already told you
- If something takes more than 3 steps, break it into a checklist
```

---

## Adding MCP Servers

MCP servers give Claude direct access to tools (Notion, GitHub, AWS, etc.).

1. Install the server:
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```
2. Configure in `~/.claude/settings.json` (user-scoped) or `.claude/settings.json` (project-scoped):
   ```json
   {
     "mcpServers": {
       "github": {
         "command": "npx",
         "args": ["-y", "@modelcontextprotocol/server-github"],
         "env": {"GITHUB_TOKEN": "your-token-here"}
       }
     }
   }
   ```
3. Update your `my-context.md` MCP section to note it's available.
4. Restart Claude Code.

**Security notes:** Use read-only tokens when possible. Never commit MCP credentials to this repo. Review server permissions before enabling.

---

## Keeping Things Current

| Cadence | What to update |
|---------|----------------|
| Weekly | Active projects in `CLAUDE.md` |
| Monthly | Tools list, skills, learning progress |
| Quarterly | Full review of both files; learning goals |
| Ad hoc | New role, new tool, completed project, earned cert |

---

## Advanced Customizations

### Custom context files in `my-context/`

For depth beyond `my-context.md`:

```
my-context/
├── project-X.md           # Long-running project details
├── vendor-contacts.md     # Key vendor relationships
├── architecture-notes.md  # System architecture reference
```

Reference them from `CLAUDE.md`:

```markdown
| Task | Go To | Read |
|------|-------|------|
| Work on Project X | — | my-context/project-X.md |
```

### Mode aliases ("quick starts")

Add shortcuts for common session starts:

```markdown
## Quick Starts

- **"Planning mode"** → load cycle-planning skill, pull this week's priorities
- **"Focus mode"** → only Priority #1, ignore the rest
- **"Review mode"** → load review workflow, walk my PR queue
```

### Per-project CLAUDE.md

For significant projects, add a `project-name/CLAUDE.md` with project-specific routing and rules. Claude auto-loads it when working in that directory.

---

## Tips

1. **Less is more in `CLAUDE.md`.** Claude has limited context. Keep the main file tight; use references for depth.
2. **Write for a smart stranger.** Claude doesn't remember previous sessions. Context must stand alone.
3. **Test your changes.** After editing, start a new Claude session and ask: "Summarize my role and priorities." Does it get it right?
4. **Steal from examples.** `examples/infosec/` shows finished setups for three InfoSec roles. Adapt structure, not specifics.
5. **Iterate.** Your first version won't be perfect. Use it for a week; refine based on what Claude gets wrong.
6. **Don't over-build before using it.** (See [Common Mistakes](common-mistakes.md) — Mistake #7.)
