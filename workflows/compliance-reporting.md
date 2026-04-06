# Workflow: Compliance Reporting

> Step-by-step procedure for generating compliance reports, collecting evidence, and preparing for audits.

---

## Prerequisites

- Know which framework(s) apply (see shared-context/compliance-frameworks.md)
- Access to GRC platform or control tracking system
- Access to systems that generate evidence (SIEM, scanners, IAM, etc.)
- Understanding of current compliance posture and open findings

---

## Step 1: Define Report Scope

```
Tell Claude:
"I need to prepare a compliance report:
- Framework: [FedRAMP / CMMC / SOC 2 / CIS / NIST 800-53]
- Scope: [FULL SYSTEM / SPECIFIC CONTROL FAMILY / DELTA FROM LAST PERIOD]
- Period: [DATE RANGE]
- Audience: [AUDITOR / EXECUTIVE / INTERNAL TEAM]
- Deadline: [DATE]

Load shared-context/compliance-frameworks.md for framework reference."
```

---

## Step 2: Assess Current Posture

### Control Status Review
```
Tell Claude:
"Review our control implementation status:

Controls data: [PASTE FROM GRC TOOL OR DESCRIBE]

Categorize each control as:
- Implemented: Fully in place, evidence available
- Partially Implemented: In progress, gaps remain
- Planned: Not yet started, on roadmap
- Not Applicable: Justified exclusion

Output: Summary table with [Control ID | Status | Evidence Status | Gap Description | Owner]"
```

### Gap Analysis
```
Tell Claude:
"Perform a gap analysis for [FRAMEWORK] compliance:

Current state: [DESCRIBE OR PASTE CONTROL STATUS]
Required state: [FRAMEWORK LEVEL/REQUIREMENTS]

For each gap:
1. What's missing
2. Risk of the gap
3. Remediation steps
4. Estimated effort
5. Priority (based on audit timeline)

Reference shared-context/compliance-frameworks.md for control details."
```

---

## Step 3: Collect Evidence

### Evidence Mapping
```
Tell Claude:
"Map evidence to controls for [FRAMEWORK]:

For control family [CONTROL FAMILY]:
1. What evidence satisfies each control
2. Where to collect it (which system/tool)
3. What format the auditor expects
4. How to automate ongoing collection

Output: Evidence collection matrix with
[Control | Evidence Type | Source System | Collection Method | Frequency | Status]"
```

### Common Evidence Types

| Control Area | Evidence Examples | Source |
|-------------|-------------------|--------|
| Access Control | User access lists, RBAC configs, access reviews | IAM, AD, SSO |
| Audit Logging | Log configurations, sample logs, retention policies | SIEM, CloudTrail |
| Vulnerability Mgmt | Scan reports, POA&M, remediation records | Tenable, Jira |
| Config Management | Baseline configs, change records, CM plan | Ansible, Terraform, CM tool |
| Incident Response | IR plan, tabletop records, incident reports | IR tool, documentation |
| Encryption | Encryption configs, key management policies | KMS, TLS configs |
| Backup/Recovery | Backup logs, recovery test results, BCP/DRP | Backup tool, test records |

---

## Step 4: Generate Report Artifacts

### POA&M Update
```
Tell Claude:
"Update the POA&M with these changes:
- New findings: [LIST]
- Closed findings: [LIST]
- Status changes: [LIST]
- Risk adjustments: [LIST]

For each new finding, draft a POA&M entry with:
1. Weakness description
2. Point of contact
3. Remediation plan
4. Scheduled completion date
5. Milestones
6. Risk level
7. Compensating controls (if any)

Follow FedRAMP POA&M template format."
```

### Continuous Monitoring Report (FedRAMP)
```
Tell Claude:
"Generate a ConMon report for [MONTH/YEAR]:

Data sources:
- Vulnerability scans: [SUMMARY OR PASTE]
- POA&M updates: [SUMMARY OR PASTE]
- Inventory changes: [SUMMARY OR PASTE]
- Significant changes: [LIST OR NONE]
- Incidents: [LIST OR NONE]

Format per FedRAMP ConMon requirements:
1. Executive summary
2. Vulnerability scan summary (by severity)
3. POA&M status (new, open, closed, overdue)
4. Inventory delta
5. Significant changes
6. Incident summary
7. Action items for next period"
```

### Executive Compliance Summary
```
Tell Claude:
"Create an executive compliance summary:
- Framework: [FRAMEWORK]
- Period: [DATE RANGE]

Include:
1. Overall compliance score/percentage
2. Trend (improving/stable/declining) with data
3. Key risks (top 3-5)
4. Audit readiness assessment
5. Resource/budget needs
6. Recommended executive actions

Keep it to one page. Use clear, non-technical language.
Include a visual-friendly breakdown (tables, not paragraphs)."
```

---

## Step 5: Audit Preparation

### Pre-Audit Checklist
```
Tell Claude:
"Help me prepare for a [FRAMEWORK] audit:
- Audit date: [DATE]
- Auditor/3PAO: [NAME]
- Scope: [WHAT'S BEING ASSESSED]

Create a preparation checklist:
1. Evidence packages to prepare (by control family)
2. Personnel who need to be available (by role)
3. Systems that need to be accessible
4. Documentation that needs to be current
5. Known gaps to address before audit
6. Talking points for key risk areas
7. Timeline with milestones leading up to audit day"
```

### Auditor Question Prep
```
Tell Claude:
"Prepare me for auditor interviews on [CONTROL FAMILY]:

For each control in this family:
1. What the auditor will likely ask
2. What evidence demonstrates compliance
3. Where to find that evidence
4. Potential follow-up questions
5. Known weaknesses and how to discuss them honestly

Help me practice clear, concise responses. I need to demonstrate
understanding, not just show artifacts."
```

---

## Step 6: Maintain Continuous Compliance

### Monthly Tasks
- [ ] Run and review vulnerability scans
- [ ] Update POA&M (new findings, closures, status changes)
- [ ] Review and update asset inventory
- [ ] Check for significant changes requiring documentation
- [ ] Review access control changes
- [ ] Validate logging and monitoring is functioning

### Quarterly Tasks
- [ ] Review and update security policies
- [ ] Conduct access reviews
- [ ] Test backup and recovery procedures
- [ ] Review and update risk assessments
- [ ] Security awareness training status

### Annual Tasks
- [ ] Full security assessment
- [ ] Business continuity/disaster recovery test
- [ ] Incident response tabletop exercise
- [ ] Policy and procedure comprehensive review
- [ ] Third-party/vendor risk reassessment

---

## Tips for Working With Claude on Compliance

1. **Specify the framework version** — NIST 800-53 Rev 5 is different from Rev 4
2. **Verify control language** — Claude's training data may not have the latest revisions
3. **Evidence must be real** — Use Claude to draft templates, not fabricate evidence
4. **Know your boundary** — Be clear about what's in scope for your authorization boundary
5. **Track inheritance** — Know which controls are inherited from your cloud provider
