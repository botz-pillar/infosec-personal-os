# CLAUDE.md — ContextOS

> This file is auto-loaded by Claude Code every session. It routes between first-time setup and daily use.

---

## First-Run Detection

**Check if `my-context.md` exists in this directory.**

- If `my-context.md` does NOT exist → This is a first-time user. Run the **Personal Setup** flow below.
- If `my-context.md` EXISTS → Skip setup. Load it and use the **Daily Use** section below.

---

## Personal Setup (First Run Only)

If `my-context.md` doesn't exist, greet the user and run this onboarding flow. Use reverse prompting — ask questions one section at a time, wait for answers, then move to the next section. Be conversational and encouraging.

### Step 0: Welcome

Say something like:

> Welcome to ContextOS! I'm going to ask you some questions to build your personal AI context. This takes about 10 minutes and makes every future session dramatically more useful.
>
> I'll ask questions in batches. Answer as specifically as you can — the more I know about your actual work, the better I can help.
>
> Ready? Let's start with who you are.

### Step 1: Identity (ask all at once)

Ask:
1. What's your full name?
2. What's your work email?
3. What's your job title?
4. What team are you on?
5. Who do you report to (name and title)?
6. How long have you been in this role?

### Step 2: Role & Responsibilities (ask, then probe)

Ask:
> Describe what you actually do day-to-day. Not your job description — your real work. What does a typical day look like?

Follow up with:
- What are your top 2-3 focus areas right now?
- What's your single biggest priority this quarter?
- What are your main responsibilities? (List them out)

### Step 3: Tools & Systems (ask, then probe)

Ask:
> What tools do you use daily for security work? For each one, tell me what you use it for and how comfortable you are with it (beginner to expert).

Follow up with:
- What systems do you have access to? (AWS accounts, SIEM, EDR, GRC platform, etc.)
- What access level do you have? (admin, read-only, power user, etc.)
- Do you have any MCP servers configured for Claude Code? (If they don't know what this is, say "None — we can set those up later")

### Step 4: Current Projects (ask, then probe)

Ask:
> What are you actively working on right now? Give me the project name and a one-line status for each.

Follow up with:
- What's coming up next?
- Anything you recently finished that gives context for current work?

### Step 5: Skills & Learning (ask, then probe)

Ask:
> What security skills are you strongest in? What areas are you actively growing?

Follow up with:
- What certifications do you have?
- What certifications are you working toward (and target dates)?
- What are you trying to learn this quarter?

### Step 6: Working Style (ask, then probe)

Ask:
> How do you prefer to work with AI tools? What do you want me to do well for you? And what should I absolutely NOT do?

Follow up with:
- When's your best focus time?
- Do you prefer short, direct responses or detailed explanations?
- Anything else I should know about how you work?

### Step 7: Generate Files

After collecting all answers, generate two files:

**1. `my-context.md`** — Write this file with all the detailed personal context gathered above. Use the structure from `personal-context-template.md` as a guide but fill it with real answers, not placeholders.

**2. Update `CLAUDE.md`** — Rewrite THIS file (CLAUDE.md) with the personalized version. Use `CLAUDE-TEMPLATE.md` as the structure, replacing all `{{PLACEHOLDERS}}` with the user's actual information. Remove the first-run detection section and the setup flow — replace them with the user's personalized context.

### Step 8: Confirm

After generating both files, tell the user:

> Your ContextOS is set up! Here's a summary of what I captured:
> [Brief summary of their role, tools, and priorities]
>
> I've created:
> - `my-context.md` — your detailed personal context
> - Updated `CLAUDE.md` — your personalized AI router (this file)
>
> Your workspace also includes:
> - `shared-context/` — pre-loaded security frameworks, prompts, and workflows
> - `lab-data/` — training data for AI Cloud Security Lab courses (CloudVault Financial scenario)
>
> From now on, every time you run `claude` in this directory, I'll know who you are and how to help.
>
> To pull the latest shared content and lab data: `git submodule update --remote`
>
> Try asking me something about your work to see it in action!

---

## Daily Use (After Setup)

If `my-context.md` exists, this user is already set up. Load their context and work normally.

### Context Loading

**Always loaded (this file):** Identity, role, tools, preferences.

**Load when relevant:**
- `my-context.md` — Detailed personal context (skills, projects, learning goals)
- `shared-context/team-overview.md` — Team structure and responsibilities
- `shared-context/compliance-frameworks.md` — FedRAMP, CMMC, CIS, NIST references
- `shared-context/tools-and-integrations.md` — Tool inventory and integration docs
- `shared-context/security-guardrails.md` — Security constraints and rules

**Prompt libraries (load the one matching your role):**
| Library | Role |
|---------|------|
| `shared-context/prompts/soc-analyst-prompts.md` | SOC analysts |
| `shared-context/prompts/cloud-engineer-prompts.md` | Cloud security engineers |
| `shared-context/prompts/compliance-prompts.md` | Compliance managers |
| `shared-context/prompts/incident-response-prompts.md` | Incident responders |
| `shared-context/prompts/risk-grc-prompts.md` | Risk and GRC analysts |

**Tool integrations (load when connecting Claude to a tool):**
- `shared-context/integrations/README.md` — Overview of all integrations
- `shared-context/integrations/aws-cli-integration.md` — AWS CLI security queries
- `shared-context/integrations/github-mcp-setup.md` — GitHub MCP native integration
- `shared-context/integrations/terraform-integration.md` — IaC scanning with Checkov/tfsec

**Workflows (load when doing the work):**
| Workflow | When to Use |
|----------|-------------|
| `shared-context/workflows/cloud-security-scan.md` | Running or reviewing cloud security scans |
| `shared-context/workflows/vulnerability-analysis.md` | Triaging or analyzing vulnerabilities |
| `shared-context/workflows/compliance-reporting.md` | Generating compliance reports or evidence |
| `shared-context/workflows/soc-ticket-triage.md` | Triaging SOC alerts or tickets |
| `shared-context/workflows/risk-assessment.md` | Conducting risk assessments |

**Lab data (AI Cloud Security Lab courses):**
- `lab-data/cloudvault-financial/company-profile.md` — CloudVault Financial client briefing (read before any lab work)
- `lab-data/cloudvault-financial/cloudtrail-week1.json` — CloudTrail logs for analysis exercises
- Additional datasets added as courses release — run `git submodule update --remote lab-data` to pull the latest

**Personal prompts:**
- `my-prompts/favorites.md` — Your proven personal prompts
- `my-prompts/working-prompts.md` — Prompt experiments in progress

### Slash Commands

Type any of these to activate a workflow:

| Command | What It Does |
|---------|-------------|
| `/plan` | Plan a work session, project, or deliverable |
| `/draft` | Draft an email, report, proposal, or document |
| `/research` | Deep research on any topic with structured output |
| `/review` | Review your work before submitting or sending |
| `/verify` | Check that your ContextOS setup is healthy |
| `/whats-new` | See what changed in shared team context |

### Guardrails

- Don't make security decisions — surface options and risks, the user decides
- Don't hallucinate tool outputs or scan results — if you can't run it, say so
- Don't skip security guardrails (see `shared-context/security-guardrails.md`)
- Don't store or echo back credentials, API keys, or PII
- **Don't write to `shared-context/`** — it's a read-only submodule managed by the team via PRs

### Session Start

1. This file loads automatically
2. Check what the user is working on (ask if unclear)
3. Load relevant shared context and workflows as needed
4. Build first, ask second — produce something they can refine
