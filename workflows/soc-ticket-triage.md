# Workflow: SOC Ticket Triage

> Step-by-step procedure for triaging security alerts, investigating incidents, and documenting findings.

---

## Prerequisites

- Access to SIEM (Splunk/Elastic/Sentinel)
- Access to EDR console (CrowdStrike/SentinelOne)
- Access to ticketing system (Jira/ServiceNow)
- Familiarity with MITRE ATT&CK framework
- Understanding of SLA matrix (see shared-context/team-overview.md)

---

## Step 1: Initial Triage

When a new alert comes in:

```
Tell Claude:
"Triage this security alert:

Source: [SIEM / EDR / IDS / CLOUD / EMAIL]
Alert name: [ALERT TITLE]
Severity: [CRITICAL / HIGH / MEDIUM / LOW]
Timestamp: [WHEN]
Affected asset: [HOSTNAME / IP / USER / SERVICE]
Alert details:
[PASTE THE ALERT — redact any PII or sensitive data]

Questions to answer:
1. True positive, false positive, or needs more investigation?
2. What MITRE ATT&CK technique does this map to?
3. What additional data would confirm or deny?
4. What's the potential impact if this is real?
5. Recommended immediate actions

DO NOT recommend containment actions without my confirmation."
```

---

## Step 2: Gather Context

### Quick Context Checks

```
Tell Claude:
"Help me build context for this alert. Generate queries for:

SIEM ([SPLUNK/ELASTIC/SENTINEL]):
- Activity from the source IP in the last 24 hours
- Activity from the affected user account in the last 7 days
- Similar alerts across all hosts in the last 30 days

EDR:
- Process tree for the affected host at the time of the alert
- Network connections from the host around the alert time
- File modifications on the host in the alert window

Provide queries in [SPL / KQL / LUCENE] syntax."
```

### Threat Intelligence Lookup

```
Tell Claude:
"Check these IOCs against known threat intelligence:
- IP: [IP ADDRESS]
- Domain: [DOMAIN]
- Hash: [FILE HASH]
- User-Agent: [UA STRING]

What do you know about these from your training data?
Flag anything you're uncertain about so I can verify against
VirusTotal, AbuseIPDB, or our TI platform.

NOTE: Your training data has a cutoff — I'll verify current
reputation through live tools."
```

---

## Step 3: Investigate

### Investigation Playbook

Based on alert type, follow the appropriate playbook:

#### Suspicious Login
```
Tell Claude:
"Suspicious login detected:
- User: [USERNAME]
- Source IP: [IP]
- Location: [GEO]
- Time: [TIMESTAMP]
- Method: [SSO/VPN/DIRECT]

Investigation steps:
1. Is this a known travel location for this user?
2. Check for impossible travel (previous login location/time)
3. Check if the source IP has been seen before
4. Look for post-authentication anomalies
5. Check for password spray or brute force preceding this login

Help me build the queries to check each of these."
```

#### Malware Detection
```
Tell Claude:
"Malware detected on endpoint:
- Host: [HOSTNAME]
- Detection: [MALWARE NAME/TYPE]
- File path: [PATH]
- Hash: [SHA256]
- User context: [WHICH USER ACCOUNT]

Investigation steps:
1. What is this malware family known for?
2. What's the typical kill chain?
3. Check for lateral movement indicators
4. Check for persistence mechanisms
5. Check for data exfiltration indicators
6. Identify patient zero and infection vector

Help me build queries to check for each indicator."
```

#### Data Exfiltration Alert
```
Tell Claude:
"Potential data exfiltration detected:
- Source: [INTERNAL HOST/USER]
- Destination: [EXTERNAL IP/DOMAIN]
- Volume: [DATA SIZE]
- Protocol: [HTTP/DNS/FTP/etc.]
- Time window: [START - END]

Investigation steps:
1. Is this destination known/authorized?
2. What data was transferred? (if determinable)
3. Is this a normal pattern for this user/system?
4. Check for DLP alerts on the same data
5. Check for prior reconnaissance activity
6. Assess data sensitivity

Help me build the investigation queries."
```

---

## Step 4: Determine Verdict

```
Tell Claude:
"Based on my investigation, here's what I found:
[PASTE YOUR FINDINGS AND EVIDENCE]

Help me determine:
1. Verdict: [TRUE POSITIVE / FALSE POSITIVE / BENIGN TRUE POSITIVE]
2. Confidence level and reasoning
3. If TP: severity classification and recommended response
4. If FP: root cause and tuning recommendation
5. If BTP: documentation and monitoring adjustments

IMPORTANT: I make the final call — give me your analysis and reasoning."
```

---

## Step 5: Respond (If True Positive)

### Containment Options

```
Tell Claude:
"This is a confirmed true positive. Help me plan containment:

Incident details: [SUMMARY]
Affected systems: [LIST]
Current status: [ACTIVE / CONTAINED / RESOLVED]

Provide containment options ranked by:
1. Effectiveness (how well it stops the threat)
2. Business impact (what breaks if we do this)
3. Reversibility (how easy to undo)
4. Speed (how quickly can we implement)

Include both immediate containment and longer-term remediation.
I will approve containment actions before execution."
```

### Escalation Criteria

| Condition | Escalation |
|-----------|-----------|
| Confirmed compromise of production system | → Security Lead immediately |
| Data exfiltration confirmed | → Security Lead + Legal |
| Ransomware detected | → Incident Commander, activate IR plan |
| Insider threat indicators | → Security Lead + HR |
| Active adversary on network | → Incident Commander |
| Customer data affected | → Security Lead + Legal + Privacy |

---

## Step 6: Document

### Ticket Documentation

```
Tell Claude:
"Document this alert investigation for our ticketing system:

Alert: [TITLE]
ID: [ALERT ID]
Date: [DATE]
Analyst: [YOUR NAME]

Create a structured ticket note with:
1. Alert summary (what triggered)
2. Investigation steps taken (what I checked)
3. Evidence collected (what I found)
4. Verdict and reasoning
5. Actions taken
6. Follow-up items (if any)
7. Tuning recommendations (if FP)

Format for [JIRA / SERVICENOW] ticket."
```

### Metrics to Track

- **MTTD (Mean Time to Detect):** Time from event to alert
- **MTTR (Mean Time to Respond):** Time from alert to resolution
- **True Positive Rate:** TP / (TP + FP)
- **Escalation Rate:** Alerts escalated / total alerts
- **SLA Compliance:** Alerts triaged within SLA / total alerts

---

## Common Alert Categories & Quick Reference

| Category | First Check | Typical Verdict |
|----------|------------|-----------------|
| Failed logins (< 5) | Check if user fat-fingered | Usually FP |
| Failed logins (> 20) | Check for brute force pattern | Investigate |
| Impossible travel | Check VPN/proxy use | Often BTP |
| New admin account | Verify with IT change management | Could be either |
| Outbound to known-bad IP | Check TI reputation + context | Investigate |
| Large data transfer | Check if scheduled backup/sync | Often BTP |
| PowerShell execution | Check if admin/automation task | Context-dependent |
| Unsigned binary execution | Check if legitimate software | Investigate |

---

## Shift Handoff Template

```
Tell Claude:
"Generate a shift handoff summary:

Period: [SHIFT START - END]
Analyst: [YOUR NAME]
Next analyst: [THEIR NAME]

Include:
1. Open investigations (status, next steps)
2. Alerts awaiting response
3. Escalated items and their status
4. Notable observations (unusual patterns, trends)
5. Pending actions for next shift
6. Any environmental changes (maintenance windows, deployments)"
```
