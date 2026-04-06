# CLAUDE.md — Marcus Rivera's InfoSec Personal OS

> This file is auto-loaded by Claude Code every session.

---

## Who I Am

**Marcus Rivera** — Cloud Security Engineer on the InfoSec team.

- **Email:** marcus.rivera@company.com
- **Focus areas:** Cloud posture management, IaC security, AWS/Azure hardening
- **Current priority:** Implementing CSPM across all AWS accounts and shifting security left in CI/CD

---

## My Role & Responsibilities

- Design and implement cloud security architecture across AWS (primary) and Azure (secondary)
- Manage cloud security posture management (CSPM) tooling and remediation
- Review and approve infrastructure-as-code (Terraform) for security compliance
- Maintain CIS Benchmark compliance across cloud environments
- Investigate and respond to cloud-specific security alerts (GuardDuty, Security Hub)
- Build and maintain cloud security automation (Lambda, EventBridge, Config Rules)
- Support FedRAMP continuous monitoring for cloud infrastructure controls
- Advise development teams on secure cloud architecture patterns

---

## My Tools & Systems

### Primary Tools
- **AWS CLI / Console** — Daily driver for all AWS work
- **Terraform** — IaC for all infrastructure, including security tooling
- **Prowler** — Cloud security scanning and CIS compliance
- **Checkov / tfsec** — IaC security scanning in CI/CD pipeline
- **AWS Security Hub** — Centralized findings aggregation
- **AWS GuardDuty** — Threat detection
- **AWS Config** — Configuration compliance monitoring
- **GitHub Actions** — CI/CD pipeline for IaC and security automation

### Access & Permissions
- AWS: SecurityAudit + custom CloudSecurityEngineer role across all accounts
- Azure: Reader + Security Reader on production subscription
- Terraform Cloud: Admin (workspace management)
- GitHub: Maintainer on infra and security repos
- Splunk: Power User (cloud log searches)

### MCP Servers Available
- GitHub MCP — PR reviews, issue management, code search
- Consider adding: AWS MCP when available

---

## Current Projects

1. **CSPM Rollout** — Deploying Prowler automated scanning across 12 AWS accounts with centralized reporting. Phase 2 of 3 (production accounts next).
2. **IaC Security Pipeline** — Integrating Checkov + tfsec into all Terraform CI/CD pipelines. 8/15 repos complete.
3. **GuardDuty Multi-Account** — Consolidating GuardDuty findings into security account with automated triage.
4. **CIS Benchmark Remediation** — Remediating Level 1 findings across all accounts. Target: 95% compliance.
5. **FedRAMP ConMon** — Monthly infrastructure scan deliverables and POA&M updates for cloud controls.

---

## How I Work

### Preferred Working Style
- I think in architecture diagrams and infrastructure patterns
- Show me the Terraform/CLI commands — I'll adapt them to our environment
- I prefer "here's the secure way to do this" over "here are the risks"
- I like to see the CIS/NIST control mapping for any security recommendation

### What I Need From Claude
- Terraform code review for security issues
- AWS CLI commands for security investigation and remediation
- CIS Benchmark implementation guidance
- Architecture review and threat modeling assistance
- Policy document generation (SCPs, IAM policies, Config Rules)
- Cloud security automation scripting (Python, Bash)
- FedRAMP evidence collection guidance for cloud controls

### What I Don't Want
- Don't make security decisions for me — surface options and risks, I decide
- Don't hallucinate tool outputs or scan results — if you can't run it, say so
- Don't skip security guardrails (see `shared-context/security-guardrails.md`)
- Don't store or echo back credentials, API keys, or PII
- Don't suggest overly permissive IAM policies — always start with least privilege
- Don't recommend `*` actions in IAM policies without flagging the risk explicitly

---

## Context Loading

### Workflows (load when doing the work)
| Workflow | When to Use |
|----------|-------------|
| `shared-context/workflows/cloud-security-scan.md` | Running or reviewing cloud security scans |
| `shared-context/workflows/compliance-reporting.md` | FedRAMP ConMon deliverables |
| `shared-context/workflows/risk-assessment.md` | Cloud architecture risk assessments |
| `shared-context/workflows/vulnerability-analysis.md` | Triaging cloud vulnerability findings |

---

## Learning Goals

- AWS Security Specialty certification — studying, target exam Q4
- Kubernetes security (CKS) — starting study next quarter
- Cloud forensics techniques (IR in AWS/Azure)
- Policy-as-code (OPA/Rego for Terraform validation)

---

## Session Start

At the start of any session:
1. This file loads automatically
2. Check what I'm working on (ask if unclear)
3. Load relevant shared context and workflows as needed
4. Build first, ask second — produce something I can refine

**Quick start:** *"What are we working on today?"*
