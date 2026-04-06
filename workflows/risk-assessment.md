# Workflow: Risk Assessment

> Step-by-step procedure for conducting security risk assessments, from scoping through reporting.

---

## Prerequisites

- Risk assessment methodology/framework defined (NIST 800-30, ISO 27005, or custom)
- Asset inventory with criticality ratings
- Threat intelligence sources
- Access to vulnerability data
- Stakeholder availability for interviews

---

## Step 1: Define Scope and Approach

```
Tell Claude:
"I'm conducting a risk assessment:
- Type: [SYSTEM / APPLICATION / VENDOR / ORGANIZATION-WIDE]
- Subject: [WHAT'S BEING ASSESSED]
- Methodology: [NIST 800-30 / ISO 27005 / FAIR / CUSTOM]
- Trigger: [ROUTINE / NEW SYSTEM / CHANGE / INCIDENT / AUDIT]
- Deadline: [DATE]

Help me:
1. Define the assessment boundary
2. Identify stakeholders to involve
3. List data sources I'll need
4. Create an assessment timeline
5. Draft a scope statement"
```

---

## Step 2: Asset Identification

```
Tell Claude:
"Identify and categorize assets for this risk assessment:

System/scope: [DESCRIBE THE SYSTEM OR SCOPE]

For each asset, capture:
1. Asset name and description
2. Asset type (hardware, software, data, people, process)
3. Owner/custodian
4. Criticality rating (Critical / High / Medium / Low)
5. Data classification (if applicable)
6. Dependencies (what relies on this asset)

Help me build an asset inventory table."
```

### Criticality Rating Criteria

| Rating | Business Impact | Examples |
|--------|----------------|----------|
| **Critical** | Operations halt, major financial/legal impact | Production databases, auth systems, customer-facing APIs |
| **High** | Significant degradation, notable financial impact | Internal apps, CI/CD pipelines, backup systems |
| **Medium** | Moderate inconvenience, limited impact | Dev environments, internal tools, non-sensitive data |
| **Low** | Minimal impact, easy workaround | Test systems, archived data, deprecated tools |

---

## Step 3: Threat Identification

```
Tell Claude:
"Identify threats relevant to [SYSTEM/SCOPE]:

Consider:
1. External threats (nation-state, cybercrime, hacktivists)
2. Internal threats (malicious insider, negligent user)
3. Environmental threats (natural disaster, power failure)
4. Supply chain threats (vendor compromise, dependency risk)
5. Technical threats (system failure, misconfiguration)

For each threat:
- Threat source and motivation
- Threat actions (what they would do)
- Historical precedent (has this happened before?)
- MITRE ATT&CK mapping (if applicable)
- Relevance to our environment (High / Medium / Low)

Focus on threats realistic for our industry and size."
```

---

## Step 4: Vulnerability Assessment

```
Tell Claude:
"Assess vulnerabilities for [SYSTEM/SCOPE]:

Data sources:
- Recent scan results: [SUMMARY OR PASTE]
- Configuration review findings: [SUMMARY]
- Previous assessment findings: [SUMMARY]
- Known architectural weaknesses: [LIST]

For each vulnerability:
1. Description
2. Affected asset(s)
3. Severity (CVSS or qualitative)
4. Current mitigation status
5. Exploitability (how easy to exploit)
6. Related threats (which threats could exploit this)"
```

---

## Step 5: Risk Analysis

### Qualitative Analysis

```
Tell Claude:
"Analyze risk for each threat-vulnerability pair:

Use this risk matrix:

Likelihood:  Very Low (1) | Low (2) | Moderate (3) | High (4) | Very High (5)
Impact:      Very Low (1) | Low (2) | Moderate (3) | High (4) | Very High (5)
Risk = Likelihood × Impact

Likelihood factors:
- Threat capability and motivation
- Vulnerability ease of exploitation
- Effectiveness of current controls
- Historical incident frequency

Impact factors:
- Confidentiality impact (data exposure)
- Integrity impact (data/system modification)
- Availability impact (service disruption)
- Financial impact
- Regulatory/compliance impact
- Reputational impact

For each risk:
[Risk ID | Threat | Vulnerability | Asset | Likelihood | Impact | Risk Score | Risk Level]"
```

### Risk Level Thresholds

| Score | Level | Action Required |
|-------|-------|-----------------|
| 20-25 | **Critical** | Immediate remediation, executive notification |
| 15-19 | **High** | Remediation within 30 days |
| 10-14 | **Medium** | Remediation within 90 days |
| 5-9 | **Low** | Accept or address in next cycle |
| 1-4 | **Very Low** | Monitor, no immediate action |

---

## Step 6: Recommend Controls

```
Tell Claude:
"For each High and Critical risk, recommend controls:

For each recommendation:
1. Control description (specific, actionable)
2. Control type: [Preventive / Detective / Corrective / Compensating]
3. Implementation effort: [Low / Medium / High]
4. Implementation cost: [Low / Medium / High]
5. Risk reduction: How much does this reduce likelihood and/or impact?
6. Residual risk after implementation
7. Framework mapping: Which compliance controls does this satisfy?

Prioritize recommendations by risk reduction per dollar/effort.
Include quick wins (low effort, high impact) separately."
```

---

## Step 7: Document and Report

### Risk Assessment Report

```
Tell Claude:
"Generate a risk assessment report:

Audience: [EXECUTIVE / TECHNICAL / COMPLIANCE / ALL]
Format: [BRIEF (2-3 pages) / STANDARD (5-10 pages) / COMPREHENSIVE (full report)]

Include:
1. Executive summary (one paragraph, key findings + overall risk posture)
2. Scope and methodology
3. Asset summary
4. Threat landscape summary
5. Risk findings (ranked by severity)
6. Risk heat map (likelihood vs. impact matrix)
7. Recommended controls (prioritized)
8. Implementation roadmap (phased approach)
9. Residual risk summary
10. Next assessment date

Appendices:
A. Detailed risk register
B. Control recommendations detail
C. Asset inventory
D. Methodology description"
```

### Risk Register Entry Format

| Field | Description |
|-------|-------------|
| Risk ID | Unique identifier (RISK-001) |
| Risk Title | Short descriptive name |
| Description | Detailed risk description |
| Threat Source | Who/what poses the threat |
| Vulnerability | What weakness is exploited |
| Affected Asset | What's at risk |
| Likelihood | Rating with justification |
| Impact | Rating with justification |
| Inherent Risk | Risk before controls |
| Current Controls | What's already in place |
| Residual Risk | Risk after current controls |
| Recommended Controls | What should be added |
| Target Risk | Risk after recommended controls |
| Risk Owner | Who's accountable |
| Status | Open / Mitigating / Accepted / Closed |
| Review Date | When to reassess |

---

## Step 8: Risk Treatment Decisions

```
Tell Claude:
"Help me prepare risk treatment options for management review:

For each risk above [THRESHOLD]:
1. Mitigate: What controls to implement (with cost/effort)
2. Transfer: Insurance or contractual options
3. Accept: Justification for acceptance (if appropriate)
4. Avoid: How to eliminate the risk entirely (if possible)

Format as a decision brief for [AUDIENCE].
Include a recommendation but make clear that management decides."
```

### Risk Acceptance Requirements
- Documented justification
- Compensating controls identified
- Residual risk clearly stated
- Approved by appropriate authority (based on risk level)
- Review date established
- Monitoring plan in place

---

## Assessment Cadence

| Trigger | Scope |
|---------|-------|
| Annual | Full organizational risk assessment |
| Quarterly | High-risk system reassessment |
| New system | Pre-deployment risk assessment |
| Major change | Change-driven assessment |
| Post-incident | Lessons learned risk update |
| Vendor onboarding | Third-party risk assessment |
| Regulation change | Compliance-driven reassessment |

---

## Tips for AI-Assisted Risk Assessment

1. **Claude analyzes, you decide** — Use Claude for analysis and drafting, make risk decisions yourself
2. **Provide context** — The more Claude knows about your environment, the better the analysis
3. **Verify threat intelligence** — Claude's knowledge has a cutoff; verify current threat data
4. **Customize the matrix** — Adjust likelihood/impact scales to match your organization's risk appetite
5. **Keep it practical** — Focus on actionable findings, not theoretical risks
6. **Iterate** — Use Claude to refine analysis through multiple passes
