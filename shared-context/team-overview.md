# InfoSec Team Overview

> Shared team context. Update via PR to main branch.

---

## Team Mission

Protect the organization's information assets, ensure regulatory compliance, and enable the business to operate securely.

---

## Team Structure

| Role | Name | Focus Area |
|------|------|------------|
| **CISO / Security Lead** | [NAME] | Strategy, risk management, executive reporting |
| **Cloud Security Engineer** | [NAME] | Cloud posture, IaC security, AWS/Azure/GCP hardening |
| **SOC Analyst (Tier 1/2)** | [NAME] | Alert triage, incident response, threat hunting |
| **Compliance Manager** | [NAME] | FedRAMP, CMMC, audit prep, evidence collection |
| **AppSec Engineer** | [NAME] | SAST/DAST, secure code review, DevSecOps |
| **GRC Analyst** | [NAME] | Risk assessments, policy management, vendor security |

*Update this table as the team changes.*

---

## Responsibilities Matrix

### Cloud Security
- Cloud security posture management (CSPM)
- Infrastructure-as-Code scanning
- Cloud access security broker (CASB) management
- Cloud workload protection
- Container and Kubernetes security

### Security Operations
- SIEM monitoring and alert triage
- Incident detection and response
- Threat intelligence integration
- Endpoint detection and response (EDR)
- Log management and correlation

### Governance, Risk & Compliance
- Regulatory compliance (FedRAMP, CMMC, SOC 2, HIPAA)
- Risk assessments and risk register management
- Security policy development and maintenance
- Vendor/third-party risk management
- Audit preparation and evidence collection

### Application Security
- Secure code review
- SAST/DAST/SCA tooling
- Developer security training
- API security
- Secure SDLC process

---

## Escalation Path

1. **Tier 1 SOC** — Initial triage, known-good/known-bad determination
2. **Tier 2 SOC** — Deep investigation, correlation, containment
3. **Security Engineer** — Technical remediation, tool tuning
4. **Security Lead** — Risk decisions, executive communication
5. **Incident Commander** — Major incidents (declared per IR plan)

---

## Key Contacts (Outside InfoSec)

| Role | Who | When to Contact |
|------|-----|-----------------|
| IT Operations | [NAME] | Infrastructure changes, access issues |
| DevOps Lead | [NAME] | CI/CD pipeline, deployment questions |
| Legal/Privacy | [NAME] | Data breach notification, privacy regs |
| HR | [NAME] | Insider threat, security awareness |
| Executive Sponsor | [NAME] | Budget, strategic decisions |

---

## Meeting Cadence

| Meeting | Frequency | Attendees | Purpose |
|---------|-----------|-----------|---------|
| Daily standup | Daily | Full team | Status, blockers, handoffs |
| Vuln review | Weekly | Eng + compliance | Triage new vulns, review SLAs |
| Risk review | Bi-weekly | Lead + GRC | Risk register, assessment updates |
| Compliance sync | Monthly | Compliance + stakeholders | Audit prep, evidence status |
| Security review board | Monthly | Cross-functional | Architecture review, exceptions |

---

## SLAs & Response Times

| Severity | Detection | Triage | Remediation |
|----------|-----------|--------|-------------|
| Critical (P1) | < 15 min | < 1 hour | < 24 hours |
| High (P2) | < 1 hour | < 4 hours | < 72 hours |
| Medium (P3) | < 4 hours | < 24 hours | < 30 days |
| Low (P4) | < 24 hours | < 72 hours | Next cycle |
