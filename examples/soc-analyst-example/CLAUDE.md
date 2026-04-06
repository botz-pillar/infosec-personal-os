# CLAUDE.md — Sarah Chen's InfoSec Personal OS

> This file is auto-loaded by Claude Code every session.

---

## Who I Am

**Sarah Chen** — Tier 2 SOC Analyst on the InfoSec team.

- **Email:** sarah.chen@company.com
- **Focus areas:** Alert triage, incident response, threat hunting
- **Current priority:** Reducing MTTR on high-severity alerts and building threat hunting playbooks

---

## My Role & Responsibilities

- Triage Tier 2 escalated security alerts from SIEM and EDR platforms
- Investigate potential security incidents and determine true/false positive
- Perform threat hunting based on CTI reports and hypothesis-driven queries
- Mentor Tier 1 analysts on investigation techniques
- Write detection rules and tune existing alerts to reduce false positives
- Participate in incident response when major incidents are declared
- Contribute to weekly vulnerability review meetings
- Maintain and update SOC runbooks and playbooks

---

## My Tools & Systems

### Primary Tools
- **Splunk** — Primary SIEM, SPL query language, daily driver
- **CrowdStrike Falcon** — EDR, threat hunting, process analysis
- **ServiceNow** — Ticketing, incident tracking
- **MITRE ATT&CK Navigator** — Technique mapping and coverage analysis
- **VirusTotal / AbuseIPDB** — IOC reputation checking
- **TheHive** — Case management for investigations

### Access & Permissions
- Splunk: Power User (search, create alerts, save reports)
- CrowdStrike: Analyst (read + respond, no policy changes)
- ServiceNow: Incident Management (create, update, resolve)
- AWS: Read-only access to CloudTrail and GuardDuty
- Active Directory: Read-only for user/group lookups

### MCP Servers Available
- None currently — using Claude Code for offline analysis, query building, and documentation

---

## Current Projects

1. **Threat Hunting Playbook Development** — Building 5 hypothesis-driven hunting playbooks for the most common ATT&CK techniques in our environment. Due end of quarter.
2. **SIEM Detection Tuning** — Reducing false positive rate on top 10 noisiest alerts. Target: 50% FP reduction.
3. **Tier 1 Training Program** — Creating training materials and shadowing sessions for new Tier 1 analysts.
4. **Phishing Response Automation** — Working with engineering to automate phishing email analysis and response.

---

## How I Work

### Preferred Working Style
- I think in timelines and kill chains — help me map events to ATT&CK stages
- I like structured output: tables, timelines, checklists
- Show me the query first, then explain what it does
- I prefer SPL over natural language for Splunk work

### What I Need From Claude
- Help building and optimizing SPL/KQL queries
- IOC analysis and enrichment (based on training data — I verify live)
- Kill chain mapping and investigation path suggestions
- Documentation drafting for investigations and runbooks
- Pattern recognition across large datasets I paste in
- Detection rule logic review

### What I Don't Want
- Don't make security decisions for me — surface options and risks, I decide
- Don't hallucinate tool outputs or scan results — if you can't run it, say so
- Don't skip security guardrails (see `shared-context/security-guardrails.md`)
- Don't store or echo back credentials, API keys, or PII
- Don't tell me to "check VirusTotal" without giving me the analysis context first
- Don't write detection rules without explaining the logic and false positive potential

---

## Context Loading

### Personal Context
- `my-context.md` — My detailed role, skills, learning goals, and preferences

### Shared Team Knowledge
- `shared-context/team-overview.md` — Team structure and responsibilities
- `shared-context/compliance-frameworks.md` — FedRAMP, CMMC, CIS, NIST references
- `shared-context/tools-and-integrations.md` — Tool inventory and integration docs
- `shared-context/approved-prompts.md` — Vetted prompts for common tasks
- `shared-context/security-guardrails.md` — Security constraints and rules

### Workflows (load when doing the work)
| Workflow | When to Use |
|----------|-------------|
| `shared-context/workflows/soc-ticket-triage.md` | Triaging SOC alerts or tickets |
| `shared-context/workflows/vulnerability-analysis.md` | Triaging or analyzing vulnerabilities |
| `shared-context/workflows/cloud-security-scan.md` | Reviewing cloud security findings |

---

## Learning Goals

- GIAC GCIH (Certified Incident Handler) — studying, target exam Q3
- Improve threat hunting methodology — move from reactive to proactive
- Learn KQL for Sentinel (team may migrate from Splunk)
- Better understand cloud-native attacks (AWS, containers)

---

## Session Start

At the start of any session:
1. This file loads automatically
2. Check what I'm working on (ask if unclear)
3. Load relevant shared context and workflows as needed
4. Build first, ask second — produce something I can refine

**Quick start:** *"What are we working on today?"*
