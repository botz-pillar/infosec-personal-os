# Tools & Integrations

> Team tool inventory with integration notes. Update via PR when tools change.

---

## Cloud Platforms

### AWS
- **Console:** https://console.aws.amazon.com
- **CLI:** `aws` (v2)
- **Key Services:** EC2, S3, IAM, CloudTrail, GuardDuty, Security Hub, Config, VPC, KMS, Secrets Manager
- **MCP Integration:** Use AWS CLI via Claude Code bash tool
- **Common Tasks:** Security group review, IAM policy analysis, CloudTrail log queries, GuardDuty finding triage

### Azure (if applicable)
- **Portal:** https://portal.azure.com
- **CLI:** `az`
- **Key Services:** Entra ID, Defender for Cloud, Sentinel, Key Vault, NSGs
- **Common Tasks:** Conditional access review, Defender alert triage, NSG rule analysis

### GCP (if applicable)
- **Console:** https://console.cloud.google.com
- **CLI:** `gcloud`
- **Key Services:** IAM, Security Command Center, VPC, Cloud Armor
- **Common Tasks:** IAM binding review, SCC finding analysis

---

## Security Tools

### SIEM
| Tool | Purpose | Access |
|------|---------|--------|
| **Splunk** | Log aggregation, search, alerting | Web UI + SPL queries |
| **Elastic/Kibana** | Alternative SIEM, log analysis | Web UI + KQL queries |
| **Sentinel** | Azure-native SIEM | Azure Portal + KQL |

**Claude Code integration:** Paste log snippets or SPL/KQL queries for analysis. Claude can help build queries, parse results, and identify patterns.

### Vulnerability Management
| Tool | Purpose | Access |
|------|---------|--------|
| **Tenable/Nessus** | Vulnerability scanning | Web UI + API |
| **Qualys** | Cloud-based vuln scanning | Web UI + API |
| **Rapid7 InsightVM** | Vuln management platform | Web UI + API |

**Claude Code integration:** Export scan results (CSV/JSON), paste into Claude for triage prioritization, CVSS analysis, and remediation guidance.

### Endpoint Security
| Tool | Purpose | Access |
|------|---------|--------|
| **CrowdStrike Falcon** | EDR, threat hunting | Web UI + API |
| **SentinelOne** | EDR, automated response | Web UI + API |
| **Carbon Black** | EDR, behavioral analysis | Web UI + API |

**Claude Code integration:** Paste detection details for IOC analysis, help build threat hunting queries.

### Cloud Security
| Tool | Purpose | Access |
|------|---------|--------|
| **Prowler** | AWS/Azure/GCP security auditing | CLI |
| **ScoutSuite** | Multi-cloud security auditing | CLI |
| **Checkov** | IaC security scanning | CLI |
| **tfsec/trivy** | Terraform/container scanning | CLI |
| **AWS Security Hub** | Centralized security findings | AWS Console + API |

**Claude Code integration:** Run CLI tools directly, pipe output for analysis.

### GRC / Compliance
| Tool | Purpose | Access |
|------|---------|--------|
| **Drata** | Compliance automation | Web UI |
| **Vanta** | Compliance automation | Web UI |
| **RegScale** | FedRAMP/CMMC compliance | Web UI + API |
| **OSCAL Tools** | Machine-readable SSP | CLI |

---

## Infrastructure Tools

| Tool | Purpose | Access |
|------|---------|--------|
| **Terraform** | Infrastructure as Code | CLI |
| **Ansible** | Configuration management | CLI |
| **Docker** | Containerization | CLI |
| **Kubernetes** | Container orchestration | kubectl CLI |
| **GitHub/GitLab** | Source control, CI/CD | Web UI + CLI |

---

## Communication & Ticketing

| Tool | Purpose | Access |
|------|---------|--------|
| **Jira** | Ticketing, project management | Web UI + API |
| **ServiceNow** | ITSM, incident management | Web UI + API |
| **Slack** | Team communication | Desktop app + API |
| **Confluence** | Documentation wiki | Web UI |
| **PagerDuty** | On-call alerting | Web UI + API |

---

## MCP Server Setup

MCP (Model Context Protocol) servers extend Claude Code's capabilities. Here are recommended integrations:

### Available MCP Servers
```json
{
  "mcpServers": {
    "github": {
      "description": "GitHub API access for repos, PRs, issues",
      "setup": "npm install -g @modelcontextprotocol/server-github"
    },
    "filesystem": {
      "description": "Extended file system access",
      "setup": "npm install -g @modelcontextprotocol/server-filesystem"
    },
    "slack": {
      "description": "Slack message reading/sending",
      "setup": "npm install -g @anthropic/mcp-server-slack"
    }
  }
}
```

### Adding MCP Servers
1. Install the server package
2. Add configuration to `~/.claude/settings.json` under `mcpServers`
3. Restart Claude Code
4. Verify with: ask Claude to list available MCP tools

### Security Notes for MCP
- Only install MCP servers from trusted sources
- Review permissions before enabling write access
- Never configure MCP servers with production credentials in shared environments
- Use read-only tokens where possible
- Rotate credentials regularly

---

## API Keys & Credentials

**NEVER store credentials in this repository.**

- Use environment variables or secrets managers
- Reference credential locations in your personal `my-context.md` (e.g., "AWS creds in 1Password vault X")
- Rotate credentials per your organization's policy
- Use short-lived tokens (STS, OAuth) over long-lived API keys

---

## Tool Evaluation Criteria

When evaluating new tools for the team:
1. **Security:** Does it meet our security requirements?
2. **Integration:** Does it have API/CLI for automation?
3. **Compliance:** Does it support our framework requirements?
4. **Cost:** Is it within budget?
5. **Maintenance:** Who owns and maintains it?
6. **AI compatibility:** Can Claude Code interact with it effectively?
