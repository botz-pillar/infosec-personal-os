# My Context — Marcus Rivera

---

## Role Details

- **Title:** Cloud Security Engineer
- **Team:** InfoSec / Cloud Security
- **Reports to:** CISO (Dana Park)
- **Tenure:** 3 years (started as Systems Engineer, moved to security 2 years ago)
- **Specialization:** AWS security architecture, IaC security, cloud compliance

---

## Skills & Experience

### Strong Areas
- AWS architecture and security services (5+ years AWS experience)
- Terraform (3 years, expert level)
- CIS AWS Benchmark implementation and remediation
- IAM policy design and least-privilege implementation
- Cloud networking security (VPCs, NACLs, Security Groups, Transit Gateway)
- Security automation (Lambda, EventBridge, Config Rules)
- CI/CD pipeline security integration

### Growing Areas
- Azure security (basic familiarity, expanding)
- Kubernetes security (running EKS, want to secure it properly)
- Cloud forensics and IR (learning AWS-specific techniques)
- Policy-as-code (OPA/Rego — exploring for Terraform validation)
- FedRAMP (learning the compliance side of cloud controls)

### Certifications
- AWS Solutions Architect Professional
- AWS SysOps Administrator Associate
- CompTIA Security+
- Terraform Associate

### Certification Goals
- AWS Security Specialty (target: Q4 this year)
- CKS - Certified Kubernetes Security Specialist (target: next year)

---

## Daily Work

### Typical Day
- 08:00 — Review GuardDuty/Security Hub findings from overnight
- 08:30 — Check Terraform PR queue for security reviews
- 09:00 — Deep work: CSPM remediation or security automation
- 11:00 — Architecture review or consulting with dev teams
- 12:00 — Lunch
- 13:00 — IaC security pipeline work or Config Rule development
- 14:30 — Meetings (standups, design reviews, compliance syncs)
- 15:30 — Documentation, runbook updates, research
- 16:30 — End of day findings review, plan tomorrow

### Regular Meetings
- Daily InfoSec standup (15 min)
- Weekly Terraform PR review sync (Wednesdays, 30 min)
- Weekly vulnerability review (Tuesdays, 1 hr)
- Bi-weekly architecture review board (Thursdays, 1 hr)
- Monthly FedRAMP ConMon sync (first Friday, 1 hr)

### Key Stakeholders
- DevOps/Platform Engineering team (primary consumers of cloud security guidance)
- SOC team (for cloud alert triage collaboration)
- Compliance Manager (for FedRAMP cloud controls)
- Application development teams (secure architecture consulting)
- AWS account owners across business units

---

## Tools I Use Daily

| Tool | What I Use It For | Proficiency |
|------|-------------------|-------------|
| AWS CLI | Everything AWS — investigation, remediation, automation | Expert |
| Terraform | Infrastructure as Code, all cloud resources | Expert |
| Prowler | Cloud security scanning, CIS compliance | Advanced |
| Checkov | IaC security scanning in CI/CD | Advanced |
| AWS Security Hub | Centralized findings, compliance dashboards | Advanced |
| AWS GuardDuty | Threat detection, finding triage | Advanced |
| AWS Config | Configuration compliance, custom rules | Advanced |
| GitHub Actions | CI/CD pipelines for security automation | Proficient |
| Python | Automation scripts, Lambda functions | Proficient |
| Splunk | Cloud log analysis (CloudTrail, VPC Flow Logs) | Intermediate |

---

## Current Projects

### Active
1. **CSPM Rollout (Phase 2)** — Deploying Prowler to production accounts. Dev/staging complete. Writing automated remediation playbooks.
2. **IaC Security Pipeline** — Checkov + tfsec in CI/CD. 8/15 repos done, tackling the complex ones now.
3. **GuardDuty Consolidation** — Multi-account setup with automated severity-based routing.
4. **CIS Remediation Sprint** — Currently at 87% Level 1 compliance, targeting 95%.

### Upcoming
- EKS security hardening project (Q3)
- Cloud DR/BCP testing for FedRAMP
- S3 data classification and DLP pilot
- SCP library standardization across OUs

### Recently Completed
- AWS Config Rules deployment (15 custom rules across all accounts)
- CloudTrail centralization to security account S3 bucket
- VPC flow log analysis pipeline in Splunk
- Terraform module for hardened EC2 baselines

---

## Learning Plan

### This Quarter
- AWS Security Specialty exam prep (Tutorials Dojo + official practice)
- Build 3 automated remediation Lambda functions
- Learn OPA/Rego basics for Terraform policy validation
- Complete AWS IR workshop (self-paced)

### This Year
- Pass AWS Security Specialty
- Become competent in Kubernetes security fundamentals
- Build cloud forensics playbook for our environment
- Present at internal tech talk on cloud security automation

---

## Working Preferences

- **Best focus time:** Morning (8-11am) for deep architecture and coding work
- **Communication style:** Technical and precise. Show me the code or the architecture.
- **How I like to receive feedback:** With examples and alternatives. "Instead of X, consider Y because Z."
- **How I use AI:** Code generation, architecture review, compliance mapping, documentation. I always review and test before deploying.

---

## Notes

- I maintain a personal Terraform module library in a private repo
- My AWS Config Rule templates are in the shared infra repo under `/security/config-rules/`
- I have a OneNote notebook with architecture decision records for major cloud security decisions
