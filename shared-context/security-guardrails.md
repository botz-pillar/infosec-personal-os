# Security Guardrails

> Rules and constraints for using Claude Code in InfoSec work. These protect you, the team, and the organization.

---

## Absolute Rules (Never Break These)

### 1. No Credentials in Chat or Files
- **Never** paste API keys, passwords, tokens, or secrets into prompts
- **Never** store credentials in this repository (even in .gitignore'd files)
- **Never** ask Claude to generate or guess passwords for production systems
- Use environment variables, secrets managers, or reference credential locations (e.g., "the API key in 1Password vault X")

### 2. No Production Changes Without Approval
- Claude Code can **analyze** production configurations — it should **never execute** changes against production
- All production changes go through your change management process
- Test in dev/staging first, always

### 3. No Sensitive Data in Prompts
- **Never** paste PII (names, SSNs, emails of real people) into prompts
- **Never** paste classified or export-controlled data
- **Never** paste customer data, even for "quick analysis"
- Sanitize or redact data before sharing with Claude
- Use synthetic/sample data for testing prompts

### 4. No Blind Trust of AI Output
- Claude can hallucinate CVE details, CVSS scores, and tool outputs
- **Always verify** security findings against authoritative sources (NVD, vendor advisories)
- **Always verify** compliance guidance against official framework documentation
- **Always review** generated code/scripts before execution
- Claude is a **copilot**, not an authority

### 5. No Offensive Operations Without Authorization
- No running exploits, attack tools, or offensive scripts without explicit authorization
- Penetration testing requires signed rules of engagement
- Claude can help **plan** and **document** authorized testing — it doesn't authorize testing
- Red team activities require proper scoping and approval

---

## Working Rules (Follow These Daily)

### Code and Scripts
- **Review before running** — Read every script Claude generates before executing
- **Sandbox first** — Test in isolated environments before touching shared systems
- **Version control** — Commit scripts to a repo, not run as one-off pastes
- **Least privilege** — Scripts should use minimum permissions needed
- **No hardcoded values** — Use variables and config files, not hardcoded IPs/hostnames

### Log and Data Analysis
- **Redact before sharing** — Remove IP addresses, usernames, hostnames from shared analysis
- **Scope your queries** — Don't pull more data than you need
- **Mind retention** — Claude's context is ephemeral, but don't share data you wouldn't put in a report
- **Verify findings** — Cross-reference Claude's analysis with your own investigation

### Compliance Work
- **Claude drafts, you own** — Generated compliance artifacts are drafts until you review and approve
- **Framework versions matter** — Specify which version of a framework you're working against
- **Evidence must be real** — Never use AI-generated evidence for audits
- **Consult official sources** — Claude's training data may be outdated for evolving frameworks

### Vulnerability Management
- **Don't fabricate scores** — If Claude provides a CVSS score, verify it against NVD
- **Context matters** — A Critical CVE on an isolated dev box is different from one on a public-facing prod system
- **Remediation testing** — Always validate that a remediation actually works before closing
- **Disclosure timelines** — Follow responsible disclosure practices

---

## What Claude Code CAN Do (Encouraged Uses)

- Draft security documentation (policies, procedures, runbooks)
- Analyze log snippets and help build SIEM queries
- Explain vulnerabilities and suggest remediation approaches
- Help with IaC security scanning and code review
- Generate compliance artifact templates
- Build threat hunting hypotheses and queries
- Automate repetitive analysis tasks
- Learn and explain security concepts
- Review and improve security architectures
- Parse and correlate security data

---

## What Claude Code SHOULD NOT Do (Discouraged Uses)

- Make risk acceptance decisions
- Execute changes in production environments
- Store or transmit sensitive data
- Replace human judgment on incident severity
- Generate compliance evidence (only templates/guidance)
- Run active scans or offensive tools
- Access systems it shouldn't (even if technically possible)
- Make access control decisions

---

## Incident Response Special Rules

During an active incident:
1. **Speed matters but accuracy matters more** — Don't let Claude rush you into wrong conclusions
2. **Chain of custody** — Don't paste forensic evidence into Claude; describe it
3. **Communication** — Claude can draft comms, but humans approve and send them
4. **Legal hold** — If legal hold is in effect, be mindful of what you put through AI tools
5. **Post-incident** — Claude can help with post-incident reports and lessons learned

---

## Reporting Security Concerns

If you discover that:
- Credentials were accidentally shared with Claude
- Sensitive data was pasted into a prompt
- A script generated by Claude caused unexpected behavior
- Any security guardrail was violated

**Take these steps:**
1. Notify your security lead immediately
2. Rotate any exposed credentials
3. Document what happened and when
4. Update these guardrails if there's a gap

---

## Review Schedule

These guardrails should be reviewed:
- **Quarterly** by the security team
- **After any incident** involving AI tool misuse
- **When new tools** are added to the stack
- **When policies change** at the organizational level

Last reviewed: [DATE]
Next review: [DATE]
