# Approved Prompt Library

> Vetted prompts for common InfoSec tasks. Copy, customize, and use with Claude Code.

---

## How to Use

1. Find the prompt category for your task
2. Copy the prompt template
3. Replace `[BRACKETED]` placeholders with your specifics
4. Run in Claude Code

These prompts are designed to produce consistent, high-quality output. They include guardrails to prevent hallucination and enforce security best practices.

---

## Cloud Security

### AWS Security Group Review
```
Review the following AWS security group rules and identify:
1. Rules allowing unrestricted inbound access (0.0.0.0/0 or ::/0)
2. Overly permissive port ranges
3. Rules that violate least-privilege principles
4. Recommendations for tightening each rule

Security Group: [PASTE SG RULES OR RUN: aws ec2 describe-security-groups --group-ids sg-XXXXX]

Output format: Table with columns [Rule | Risk | Recommendation | Priority]
```

### IAM Policy Analysis
```
Analyze this IAM policy for security issues:
1. Identify overly permissive actions (wildcards)
2. Check for missing resource constraints
3. Flag any privilege escalation paths
4. Suggest least-privilege alternatives

Policy: [PASTE POLICY JSON]

Reference against AWS security best practices and CIS AWS Benchmark.
```

### CloudTrail Log Investigation
```
Analyze these CloudTrail events for suspicious activity:
1. Identify unusual API calls or access patterns
2. Flag any privilege escalation attempts
3. Check for data exfiltration indicators
4. Correlate events by source IP and user identity

Events: [PASTE CLOUDTRAIL EVENTS OR QUERY RESULTS]

Provide a timeline of events and risk assessment.
```

### S3 Bucket Security Audit
```
Review this S3 bucket configuration for security issues:
1. Public access settings (Block Public Access, bucket policy, ACLs)
2. Encryption configuration (SSE-S3, SSE-KMS, or none)
3. Logging and versioning status
4. Lifecycle and replication policies
5. Cross-account access

Bucket: [BUCKET NAME]
Run: aws s3api get-bucket-policy --bucket [BUCKET]
Run: aws s3api get-public-access-block --bucket [BUCKET]
Run: aws s3api get-bucket-encryption --bucket [BUCKET]
```

---

## Vulnerability Management

### CVE Triage
```
Triage this vulnerability:
- CVE ID: [CVE-XXXX-XXXXX]
- Affected system: [SYSTEM/APPLICATION]
- Environment: [PROD/STAGING/DEV]
- Current exposure: [INTERNET-FACING/INTERNAL/ISOLATED]

Provide:
1. CVSS score breakdown and exploitability assessment
2. Known exploits in the wild (based on your training data)
3. Compensating controls that reduce risk
4. Remediation options ranked by effort vs. impact
5. Recommended SLA based on our severity matrix (see shared-context/team-overview.md)

Do NOT fabricate CVSS scores — if you're unsure, say so and suggest I check NVD.
```

### Scan Results Prioritization
```
I have [NUMBER] vulnerabilities from a [TOOL] scan. Help me prioritize:

Prioritization criteria (in order):
1. Actively exploited in the wild (KEV list)
2. Internet-facing systems
3. CVSS 9.0+ (Critical)
4. Systems with sensitive data
5. CVSS 7.0-8.9 (High)

Scan results: [PASTE CSV/JSON OR DESCRIBE]

Output: Ranked list with justification for top 10 priorities.
```

### Patch Analysis
```
Analyze this patch/update for:
1. What vulnerabilities it addresses
2. Breaking changes or compatibility concerns
3. Dependencies affected
4. Recommended testing approach before deployment
5. Rollback plan if issues arise

Patch details: [PASTE RELEASE NOTES OR CVE LIST]
System: [TARGET SYSTEM AND VERSION]
```

---

## Compliance & Reporting

### Control Evidence Collection
```
I need to collect evidence for the following control:
- Framework: [FedRAMP/CMMC/SOC2/CIS]
- Control ID: [CONTROL-ID]
- Control description: [DESCRIPTION]

Help me:
1. Identify what evidence satisfies this control
2. List the specific artifacts I need to gather
3. Draft evidence descriptions for each artifact
4. Identify any gaps in our current implementation
5. Suggest automation opportunities for ongoing evidence collection

Reference shared-context/compliance-frameworks.md for framework details.
```

### POA&M Entry Draft
```
Draft a POA&M entry for:
- Finding: [DESCRIBE THE FINDING]
- Source: [SCAN/AUDIT/ASSESSMENT]
- Affected system: [SYSTEM]
- Current risk level: [HIGH/MODERATE/LOW]

Include:
1. Weakness description (clear, specific language)
2. Remediation plan (actionable steps)
3. Milestones with target dates
4. Responsible parties
5. Risk acceptance justification (if applicable)
6. Compensating controls (if applicable)

Follow FedRAMP POA&M template format.
```

### Compliance Status Report
```
Generate a compliance status report for [FRAMEWORK]:
- Reporting period: [DATE RANGE]
- Audience: [EXECUTIVE/TECHNICAL/AUDITOR]

Include:
1. Overall compliance posture (% controls implemented)
2. Changes since last period
3. Open findings summary (by severity)
4. Key risks and mitigations
5. Upcoming deadlines and milestones
6. Resource needs or blockers

Keep it [LENGTH: brief executive summary / detailed technical report].
```

---

## SOC / Incident Response

### Alert Triage
```
Triage this security alert:
- Alert source: [SIEM/EDR/IDS/CLOUD]
- Alert name: [ALERT NAME]
- Severity: [CRITICAL/HIGH/MEDIUM/LOW]
- Affected asset: [HOST/USER/SERVICE]
- Raw alert data: [PASTE ALERT DETAILS]

Walk through:
1. Is this a true positive, false positive, or needs investigation?
2. What additional data points would confirm/deny?
3. What queries should I run in [SIEM TOOL] to correlate?
4. If true positive: recommended containment actions
5. If false positive: recommended tuning to reduce noise

Do NOT make containment decisions for me — recommend and I'll decide.
```

### Incident Timeline
```
Help me build an incident timeline from these data sources:
- SIEM logs: [PASTE OR DESCRIBE]
- EDR alerts: [PASTE OR DESCRIBE]
- Network logs: [PASTE OR DESCRIBE]
- User reports: [PASTE OR DESCRIBE]

Output:
1. Chronological timeline (UTC timestamps)
2. Kill chain mapping (which MITRE ATT&CK stages observed)
3. IOCs extracted (IPs, domains, hashes, user accounts)
4. Scope assessment (affected systems, data, users)
5. Recommended next steps for investigation

All timestamps in UTC. Flag any gaps in the timeline.
```

### Threat Hunt Query Builder
```
Build threat hunting queries for:
- Hypothesis: [WHAT ARE WE LOOKING FOR?]
- Data source: [SPLUNK/ELASTIC/SENTINEL/CROWDSTRIKE]
- Time range: [LAST 24H/7D/30D]
- Scope: [ALL SYSTEMS/SPECIFIC SEGMENT]

Provide:
1. Primary detection query
2. Supporting correlation queries
3. Expected baseline (what normal looks like)
4. Indicators of compromise to watch for
5. False positive considerations

Query language: [SPL/KQL/LUCENE]
```

---

## Risk Assessment

### Risk Scenario Analysis
```
Analyze this risk scenario:
- Threat: [DESCRIBE THE THREAT]
- Asset: [WHAT'S AT RISK]
- Vulnerability: [WHAT WEAKNESS COULD BE EXPLOITED]
- Current controls: [EXISTING MITIGATIONS]

Provide:
1. Likelihood assessment (with reasoning)
2. Impact assessment (confidentiality, integrity, availability)
3. Current risk rating
4. Recommended additional controls
5. Residual risk after recommended controls
6. Cost-benefit analysis of top recommendations

Use qualitative scale: Very Low / Low / Moderate / High / Very High
```

### Vendor Security Assessment
```
Evaluate this vendor's security posture:
- Vendor: [VENDOR NAME]
- Service: [WHAT THEY PROVIDE]
- Data access: [WHAT DATA DO THEY TOUCH?]
- Compliance requirements: [FRAMEWORKS THAT APPLY]

Review:
1. SOC 2 report summary (if provided): [PASTE OR DESCRIBE]
2. Security questionnaire responses: [PASTE KEY ITEMS]
3. Identified risks and gaps
4. Recommended contractual requirements
5. Ongoing monitoring recommendations
6. Risk rating: Accept / Accept with conditions / Reject

Flag any deal-breakers based on our compliance requirements.
```

---

## General Utilities

### Security Documentation Writer
```
Write security documentation for:
- Document type: [POLICY/PROCEDURE/STANDARD/GUIDELINE]
- Topic: [SUBJECT]
- Audience: [TECHNICAL/NON-TECHNICAL/EXECUTIVE]
- Framework alignment: [NIST/CIS/ISO/NONE]

Requirements:
1. Follow [ORGANIZATION] documentation template
2. Include purpose, scope, roles & responsibilities
3. Use clear, actionable language
4. Reference specific controls where applicable
5. Include review/update schedule

Draft length: [SHORT: 1-2 pages / MEDIUM: 3-5 pages / DETAILED: 5+ pages]
```

### Log Parser
```
Parse and analyze these logs:
- Log source: [SYSTEM/APPLICATION]
- Log format: [SYSLOG/JSON/CSV/CUSTOM]
- What I'm looking for: [DESCRIBE]

Logs: [PASTE LOG ENTRIES]

Extract:
1. Key events and patterns
2. Anomalies or errors
3. Timeline of significant events
4. Recommendations for follow-up
```

---

## Prompt Engineering Tips

1. **Be specific** — Include system names, frameworks, and output formats
2. **Include guardrails** — Tell Claude what NOT to do (e.g., "don't fabricate scores")
3. **Provide context** — Reference shared-context files for team-specific information
4. **Request structured output** — Tables, timelines, and ranked lists are easier to act on
5. **Verify claims** — Always cross-reference Claude's output with authoritative sources (NVD, vendor docs, official frameworks)
