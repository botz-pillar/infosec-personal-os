# Workflow: Cloud Security Scan

> Step-by-step procedure for running and analyzing cloud security scans.

---

## Prerequisites

- AWS CLI configured with appropriate credentials
- Prowler or ScoutSuite installed (or equivalent cloud scanning tool)
- Access to the target AWS account(s)
- Familiarity with CIS AWS Benchmark

---

## Step 1: Scope the Scan

Before scanning, define your scope:

```
Tell Claude:
"I need to run a cloud security scan against [ACCOUNT/ENVIRONMENT].
Scope: [FULL ACCOUNT / SPECIFIC SERVICES / SPECIFIC REGION]
Framework: [CIS Benchmark / FedRAMP / Custom checks]
Purpose: [ROUTINE / AUDIT PREP / INCIDENT FOLLOW-UP]"
```

Claude will help you:
- Select the right tool and configuration
- Build the scan command with appropriate flags
- Identify any prerequisites you might be missing

---

## Step 2: Run the Scan

### Option A: Prowler

```bash
# Full CIS Benchmark scan
prowler aws --compliance cis_2.0_aws

# Specific service scan
prowler aws --service s3,iam,ec2

# Specific region
prowler aws --region us-east-1

# Output to JSON for analysis
prowler aws --compliance cis_2.0_aws -M json -o ./scan-results/
```

### Option B: ScoutSuite

```bash
# Full AWS scan
scout aws

# With specific profile
scout aws --profile production

# Output report
scout aws --report-dir ./scan-results/
```

### Option C: AWS Security Hub

```bash
# Get findings from Security Hub
aws securityhub get-findings --filters '{"SeverityLabel": [{"Value": "CRITICAL", "Comparison": "EQUALS"}]}' --region us-east-1
```

### Option D: Custom AWS CLI Checks

```
Tell Claude:
"Run these AWS security checks and analyze the results:
1. Public S3 buckets
2. Security groups with 0.0.0.0/0
3. IAM users without MFA
4. Unencrypted EBS volumes
5. CloudTrail status"
```

Claude will generate and help you run the individual AWS CLI commands.

---

## Step 3: Analyze Results

```
Tell Claude:
"Analyze these cloud scan results. Here's the output:
[PASTE SCAN RESULTS — JSON, CSV, or summary]

Prioritize findings by:
1. Internet-facing exposure
2. Severity (Critical > High > Medium > Low)
3. Data sensitivity of affected resources
4. Ease of exploitation

Output: Ranked table with [Finding | Severity | Resource | Risk | Remediation | Priority]"
```

---

## Step 4: Generate Remediation Plan

```
Tell Claude:
"For the top [5/10] findings from this scan, create a remediation plan:

For each finding include:
1. Specific remediation steps (CLI commands or console instructions)
2. Estimated effort (Quick fix / Moderate / Complex)
3. Potential impact of the fix (will anything break?)
4. Verification command to confirm the fix worked
5. Compensating control if immediate fix isn't possible

Format as a runbook I can hand to an engineer."
```

---

## Step 5: Document and Report

```
Tell Claude:
"Create a scan summary report:
- Scan date: [DATE]
- Scope: [WHAT WAS SCANNED]
- Tool: [TOOL USED]
- Total findings: [NUMBER]
- Breakdown: [X Critical, Y High, Z Medium, W Low]
- Top risks: [LIST]
- Remediation timeline: [PROPOSED]
- Next scan: [SCHEDULED DATE]

Audience: [EXECUTIVE / TECHNICAL / COMPLIANCE]
Format: [BRIEF / DETAILED]"
```

---

## Step 6: Track Remediation

- Create tickets for each finding (Jira/ServiceNow)
- Assign owners and SLA deadlines
- Schedule follow-up scan to verify fixes
- Update POA&M if compliance-relevant

---

## Automation Opportunities

Ask Claude to help you:
- **Schedule recurring scans** with cron or CI/CD pipelines
- **Build automated alerting** for new critical findings
- **Create comparison reports** (this scan vs. last scan)
- **Generate compliance mappings** (findings → control gaps)

---

## Common Pitfalls

| Pitfall | Prevention |
|---------|-----------|
| Scanning without proper authorization | Get written approval before scanning any account |
| Missing regions | Scan all active regions, not just the primary one |
| Ignoring informational findings | Low-severity findings can chain into high-risk issues |
| Not re-scanning after fixes | Always verify with a follow-up scan |
| Scan fatigue | Focus on delta from last scan, not full results every time |
