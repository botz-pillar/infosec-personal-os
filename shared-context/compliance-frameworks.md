# Compliance Frameworks Reference

> Quick reference for frameworks the team works with. Not a replacement for official documentation — use this for orientation and Claude Code context.

---

## FedRAMP (Federal Risk and Authorization Management Program)

### What It Is
Standardized approach for security assessment, authorization, and continuous monitoring of cloud products used by federal agencies.

### Impact Levels
| Level | Description | Controls |
|-------|-------------|----------|
| **Low** | Public data, minimal impact | ~125 controls |
| **Moderate** | Controlled unclassified, significant impact | ~325 controls |
| **High** | Critical operations, severe impact | ~421 controls |

### Key Processes
- **Initial Authorization:** System Security Plan (SSP), Security Assessment Report (SAR), Plan of Action & Milestones (POA&M)
- **Continuous Monitoring (ConMon):** Monthly vuln scans, annual assessments, POA&M updates, significant change requests
- **Artifacts:** SSP, SAR, POA&M, CIS/CRM, Incident Response Plan, Configuration Management Plan

### ConMon Deliverables (Monthly)
1. Vulnerability scan results (OS, web app, database, container)
2. POA&M updates (new findings, closures, risk adjustments)
3. Inventory updates (hardware, software, ports/protocols/services)
4. Significant change requests (if applicable)
5. Incident reports (if applicable)

### Common Tools
- Nessus/Tenable for vulnerability scanning
- OSCAL for machine-readable SSP
- GRC platform for control tracking

---

## CMMC (Cybersecurity Maturity Model Certification)

### What It Is
DoD framework requiring defense contractors to implement cybersecurity practices based on the sensitivity of data they handle.

### Levels (CMMC 2.0)
| Level | Description | Requirements |
|-------|-------------|-------------|
| **Level 1** | Foundational | 17 practices (basic cyber hygiene) |
| **Level 2** | Advanced | 110 practices (aligned to NIST 800-171) |
| **Level 3** | Expert | 110+ practices (aligned to NIST 800-172) |

### Key Concepts
- **CUI (Controlled Unclassified Information):** Data requiring protection per NIST 800-171
- **FCI (Federal Contract Information):** Info provided by/generated for the government
- **SPRS Score:** Self-assessment score submitted to the Supplier Performance Risk System
- **C3PAO:** Certified Third-Party Assessment Organization (conducts Level 2 assessments)

---

## NIST 800-53 (Security and Privacy Controls)

### Control Families
| ID | Family | Focus |
|----|--------|-------|
| AC | Access Control | Who can access what |
| AU | Audit & Accountability | Logging and monitoring |
| AT | Awareness & Training | Security training |
| CA | Assessment & Authorization | Security assessments |
| CM | Configuration Management | System configuration |
| CP | Contingency Planning | Backup and recovery |
| IA | Identification & Authentication | Identity management |
| IR | Incident Response | Handling security incidents |
| MA | Maintenance | System maintenance |
| MP | Media Protection | Protecting storage media |
| PE | Physical & Environmental | Physical security |
| PL | Planning | Security planning |
| PM | Program Management | Security program |
| PS | Personnel Security | Personnel screening |
| RA | Risk Assessment | Risk identification |
| SA | System & Services Acquisition | Procurement security |
| SC | System & Communications Protection | Data in transit/at rest |
| SI | System & Information Integrity | Patching, malware, monitoring |
| SR | Supply Chain Risk Management | Third-party risk |

---

## CIS Controls (v8)

### Implementation Groups
| Group | Description | Target |
|-------|-------------|--------|
| **IG1** | Essential cyber hygiene | Every organization |
| **IG2** | Expanded controls | Orgs with IT security staff |
| **IG3** | Comprehensive | Orgs handling sensitive data |

### Top 5 Controls (Highest Impact)
1. **Inventory & Control of Enterprise Assets** — Know what you have
2. **Inventory & Control of Software Assets** — Know what's running
3. **Data Protection** — Classify and protect data
4. **Secure Configuration** — Harden defaults
5. **Account Management** — Control access

---

## SOC 2 (Service Organization Control 2)

### Trust Service Criteria
| Criteria | Description |
|----------|-------------|
| **Security** | Protection against unauthorized access (required) |
| **Availability** | System uptime and accessibility |
| **Processing Integrity** | Accurate and complete processing |
| **Confidentiality** | Protection of confidential information |
| **Privacy** | Personal information handling |

### Report Types
- **Type I:** Controls at a point in time
- **Type II:** Controls over a period (typically 6-12 months)

---

## Framework Mapping

Many controls overlap across frameworks. Use these mappings:

| NIST 800-53 | CIS Control | FedRAMP | CMMC |
|-------------|-------------|---------|------|
| AC-2 Account Mgmt | CIS 5 Account Mgmt | Required | L2 3.1.1 |
| AU-2 Audit Events | CIS 8 Audit Log Mgmt | Required | L2 3.3.1 |
| CM-6 Config Settings | CIS 4 Secure Config | Required | L2 3.4.2 |
| IA-2 Authentication | CIS 6 Access Control | Required | L2 3.5.3 |
| SI-2 Flaw Remediation | CIS 7 Vuln Mgmt | Required | L2 3.14.1 |

---

## How to Use This With Claude

When working on compliance tasks, tell Claude:
- Which framework you're working against
- The specific control family or requirement
- Whether you need evidence, documentation, or implementation guidance
- Load `workflows/compliance-reporting.md` for structured compliance work
