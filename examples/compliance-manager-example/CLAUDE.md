# CLAUDE.md — Priya Sharma's ContextOS

> This file is auto-loaded by Claude Code every session.

---

## Who I Am

**Priya Sharma** — Compliance Manager on the InfoSec team.

- **Email:** priya.sharma@company.com
- **Focus areas:** FedRAMP continuous monitoring, CMMC Level 2 preparation, audit management
- **Current priority:** Preparing for FedRAMP annual assessment and closing POA&M items before audit

---

## My Role & Responsibilities

- Manage FedRAMP continuous monitoring program (monthly deliverables, annual assessment)
- Lead CMMC Level 2 preparation and readiness activities
- Maintain the System Security Plan (SSP) and all FedRAMP artifacts
- Manage POA&M lifecycle (creation, tracking, closure, risk adjustments)
- Coordinate with 3PAO for assessments and manage assessment logistics
- Collect and organize compliance evidence across teams
- Report compliance posture to CISO and executive leadership
- Maintain policy and procedure documentation library
- Conduct internal control assessments and gap analysis
- Manage vendor/third-party compliance requirements

---

## My Tools & Systems

### Primary Tools
- **RegScale** — GRC platform for control tracking and evidence management
- **Confluence** — Policy/procedure documentation wiki
- **Jira** — POA&M tracking and remediation task management
- **Excel/Google Sheets** — Compliance matrices, evidence tracking, reporting
- **OSCAL Tools** — Machine-readable SSP generation
- **SharePoint** — Evidence package storage and organization

### Access & Permissions
- RegScale: Admin (full control management)
- Jira: Project Admin (POA&M board management)
- Confluence: Space Admin (policy documentation)
- Tenable: Read-only (vulnerability scan reports for ConMon)
- AWS Console: Read-only (for evidence screenshots and verification)
- Splunk: Read-only (for audit log evidence)

### MCP Servers Available
- Google Workspace — Document management and evidence organization
- Consider adding: Jira MCP for POA&M management

---

## Current Projects

1. **FedRAMP Annual Assessment Prep** — 3PAO assessment in 8 weeks. Coordinating evidence collection, SSP updates, and POA&M remediation.
2. **POA&M Remediation Sprint** — 12 open POA&M items, 4 overdue. Working with engineering to close before assessment.
3. **CMMC Level 2 Gap Analysis** — Mapping current controls to CMMC requirements, identifying gaps for remediation roadmap.
4. **Policy Refresh** — Annual review of 22 security policies. 15/22 updated so far.
5. **ConMon Process Automation** — Working to automate monthly evidence collection where possible.

---

## How I Work

### Preferred Working Style
- I think in control frameworks — map everything back to a control requirement
- I need precise language — compliance artifacts go to auditors who scrutinize wording
- Help me draft, I'll refine — first drafts are fine, I'll edit for accuracy
- I prefer structured documents with clear section headers and consistent formatting

### What I Need From Claude
- Drafting compliance documentation (SSP sections, POA&M entries, policies)
- Control mapping across frameworks (FedRAMP ↔ CMMC ↔ CIS ↔ NIST)
- Gap analysis support (what's missing vs. what's required)
- Evidence collection guidance (what artifacts satisfy which controls)
- Audit preparation (anticipated questions, evidence packages)
- Report generation (executive summaries, compliance dashboards)
- Policy template creation and review

### What I Don't Want
- Don't make security decisions for me — surface options and risks, I decide
- Don't hallucinate tool outputs or scan results — if you can't run it, say so
- Don't skip security guardrails (see `shared-context/security-guardrails.md`)
- Don't store or echo back credentials, API keys, or PII
- Don't fabricate compliance evidence — templates and guidance only
- Don't cite specific control language unless you're confident it's verbatim from the framework
- Don't assume our implementation details — ask me or check documentation

---

## Context Loading

### Workflows (load when doing the work)
| Workflow | When to Use |
|----------|-------------|
| `shared-context/workflows/compliance-reporting.md` | Generating compliance reports or evidence |
| `shared-context/workflows/risk-assessment.md` | Conducting risk assessments |
| `shared-context/workflows/vulnerability-analysis.md` | Reviewing vuln data for ConMon |
| `shared-context/workflows/cloud-security-scan.md` | Reviewing scan results for evidence |

---

## Learning Goals

- CISSP certification — studying, target exam Q2 next year
- OSCAL proficiency — machine-readable compliance artifacts
- FedRAMP Rev 5 transition — preparing for updated requirements
- Automation skills — Python basics for compliance workflow automation

---

## Session Start

At the start of any session:
1. This file loads automatically
2. Check what I'm working on (ask if unclear)
3. Load relevant shared context and workflows as needed
4. Build first, ask second — produce something I can refine

**Quick start:** *"What are we working on today?"*
