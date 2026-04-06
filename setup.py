#!/usr/bin/env python3
"""
ContextOS — Interactive Setup Script

Asks guided questions about your role, tools, projects, and goals,
then generates personalized CLAUDE.md and my-context.md files.
"""

import sys
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()

# ─── Colors ───────────────────────────────────────────────────────────────────

class C:
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    RESET = "\033[0m"


def banner():
    print(f"""
{C.CYAN}{C.BOLD}╔══════════════════════════════════════════════════════════╗
║           ContextOS — Personal Setup                    ║
║     Personalize your AI-powered security workflow        ║
╚══════════════════════════════════════════════════════════╝{C.RESET}
""")


def section(title):
    print(f"\n{C.GREEN}{C.BOLD}── {title} ──{C.RESET}\n")


def ask(prompt, required=True, default=None, multiline=False):
    """Ask a question and return the answer."""
    suffix = ""
    if default:
        suffix = f" {C.DIM}[{default}]{C.RESET}"
    if multiline:
        suffix += f" {C.DIM}(enter a blank line to finish){C.RESET}"

    print(f"{C.YELLOW}?{C.RESET} {prompt}{suffix}")

    if multiline:
        lines = []
        while True:
            line = input("  ")
            if line.strip() == "":
                break
            lines.append(line.strip())
        answer = "\n".join(lines)
    else:
        answer = input("  > ").strip()

    if not answer and default:
        return default
    if not answer and required:
        print(f"  {C.RED}This field is required.{C.RESET}")
        return ask(prompt, required, default, multiline)
    return answer


def ask_list(prompt, hint="one per line"):
    """Ask for a list of items."""
    print(f"{C.YELLOW}?{C.RESET} {prompt} {C.DIM}({hint}, blank line to finish){C.RESET}")
    items = []
    while True:
        item = input("  - ").strip()
        if item == "":
            break
        items.append(item)
    if not items:
        print(f"  {C.DIM}(none entered){C.RESET}")
    return items


def ask_tools():
    """Ask about tools with proficiency levels."""
    print(f"{C.YELLOW}?{C.RESET} What tools do you use daily? {C.DIM}(enter tool name, then proficiency){C.RESET}")
    print(f"  {C.DIM}Proficiency: beginner / intermediate / proficient / advanced / expert{C.RESET}")
    print(f"  {C.DIM}Enter a blank tool name to finish{C.RESET}")
    tools = []
    while True:
        name = input("  Tool name: ").strip()
        if not name:
            break
        usage = input("  What for: ").strip() or "General use"
        level = input("  Proficiency (b/i/p/a/e): ").strip().lower()
        level_map = {
            "b": "Beginner", "beginner": "Beginner",
            "i": "Intermediate", "intermediate": "Intermediate",
            "p": "Proficient", "proficient": "Proficient",
            "a": "Advanced", "advanced": "Advanced",
            "e": "Expert", "expert": "Expert",
        }
        level = level_map.get(level, "Proficient")
        tools.append({"name": name, "usage": usage, "level": level})
        print(f"  {C.GREEN}+{C.RESET} Added {name} ({level})")
    return tools


def ask_choice(prompt, options):
    """Ask a multiple choice question."""
    print(f"{C.YELLOW}?{C.RESET} {prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        choice = input("  > ").strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
        except ValueError:
            # Check if they typed the option text
            for opt in options:
                if choice.lower() in opt.lower():
                    return opt
        print(f"  {C.RED}Enter a number 1-{len(options)}{C.RESET}")


# ─── Main Setup Flow ─────────────────────────────────────────────────────────

def main():
    banner()
    print("This script will ask you about your role, tools, and goals,")
    print("then generate personalized CLAUDE.md and my-context.md files.")
    print(f"\n{C.DIM}Takes about 10 minutes. Be specific — the better your answers,")
    print(f"the more useful Claude will be.{C.RESET}\n")

    # Initialize shared context submodule if not already present
    shared_path = SCRIPT_DIR / "shared-context"
    if not (shared_path / "team-overview.md").exists():
        print(f"{C.CYAN}Initializing shared team context...{C.RESET}")
        try:
            subprocess.run(
                ["git", "submodule", "update", "--init", "--recursive"],
                cwd=str(SCRIPT_DIR), check=True, capture_output=True
            )
            if (shared_path / "team-overview.md").exists():
                print(f"  {C.GREEN}+{C.RESET} Shared context loaded successfully")
            else:
                print(f"  {C.YELLOW}!{C.RESET} Shared context submodule initialized but appears empty.")
                print(f"    Run: git submodule update --init --recursive")
        except subprocess.CalledProcessError:
            print(f"  {C.YELLOW}!{C.RESET} Could not initialize shared context submodule.")
            print(f"    Run manually: git submodule update --init --recursive")
        print()

    input(f"Press {C.BOLD}Enter{C.RESET} to begin...")

    data = {}

    # ── Section 1: Identity ──────────────────────────────────────────────────

    section("1/6 — Identity")

    data["name"] = ask("What's your full name?")
    data["email"] = ask("What's your work email?")
    data["title"] = ask("What's your job title?")
    data["team"] = ask("What team are you on?", default="InfoSec")
    data["manager"] = ask("Who do you report to? (name and title)")
    data["tenure"] = ask("How long have you been in this role?", default="Less than 1 year")

    # ── Section 2: Role & Responsibilities ───────────────────────────────────

    section("2/6 — Role & Responsibilities")

    data["specialization"] = ask("What's your primary specialization?",
                                  default="e.g., cloud security, SOC operations, compliance")

    print(f"\n{C.DIM}What are your main responsibilities? Think about what you actually")
    print(f"do day-to-day, not just your job description.{C.RESET}")
    data["responsibilities"] = ask_list("List your key responsibilities")

    data["focus_areas"] = ask("What are your top 2-3 focus areas right now?")
    data["current_priority"] = ask("What's your single biggest priority this quarter?")

    # ── Section 3: Tools & Systems ───────────────────────────────────────────

    section("3/6 — Tools & Systems")

    data["tools"] = ask_tools()

    print()
    data["access_levels"] = ask("Describe your access levels briefly",
                                 multiline=True,
                                 required=False) or "Standard team access"

    data["mcp_servers"] = ask("Do you have any MCP servers configured for Claude Code?",
                               default="None currently",
                               required=False)

    # ── Section 4: Current Projects ──────────────────────────────────────────

    section("4/6 — Current Projects")

    print(f"{C.DIM}List your active projects. For each, give a name and brief status.{C.RESET}")
    data["projects"] = ask_list("Active projects (name — brief status)")

    data["upcoming_projects"] = ask_list("Upcoming projects (name — brief description)")
    data["completed_projects"] = ask_list("Recently completed projects")

    # ── Section 5: Skills & Learning ─────────────────────────────────────────

    section("5/6 — Skills & Learning")

    data["strong_skills"] = ask_list("Skills you're strong in")
    data["growing_skills"] = ask_list("Skills you're actively growing")
    data["certifications"] = ask_list("Current certifications")
    data["cert_goals"] = ask_list("Certification goals")

    data["quarterly_learning"] = ask("What are you learning this quarter?", required=False) or "TBD"
    data["yearly_learning"] = ask("What are your learning goals for this year?", required=False) or "TBD"

    # ── Section 6: Working Style ─────────────────────────────────────────────

    section("6/6 — Working Style & Preferences")

    data["focus_time"] = ask("When's your best focus time?", default="Morning")
    data["comm_style"] = ask("How do you prefer to communicate?",
                              default="Direct and structured")
    data["feedback_pref"] = ask("How do you like to receive feedback?",
                                 default="Specific and actionable")
    data["ai_usage"] = ask("How do you primarily use AI tools?",
                            default="Research, code review, documentation")

    print(f"\n{C.DIM}What do you want Claude to do well for you?{C.RESET}")
    data["claude_expectations"] = ask_list("What I need from Claude")

    print(f"\n{C.DIM}What should Claude avoid doing?{C.RESET}")
    data["claude_donts"] = ask_list("What I don't want from Claude")

    data["typical_day"] = ask("Briefly describe your typical workday", multiline=True,
                               required=False) or "Standard 9-5 with meetings and focus blocks"

    data["additional_notes"] = ask("Any additional notes or context?",
                                    multiline=True, required=False) or ""

    # ── Generate Files ───────────────────────────────────────────────────────

    section("Generating Your Files")

    claude_md = generate_claude_md(data)
    context_md = generate_context_md(data)

    claude_path = SCRIPT_DIR / "CLAUDE.md"
    context_path = SCRIPT_DIR / "my-context.md"

    # Check for existing files
    for path, name in [(claude_path, "CLAUDE.md"), (context_path, "my-context.md")]:
        if path.exists():
            overwrite = ask(f"{name} already exists. Overwrite?", default="y")
            if overwrite.lower() not in ("y", "yes"):
                backup = path.with_suffix(".md.bak")
                path.rename(backup)
                print(f"  {C.DIM}Backed up to {backup.name}{C.RESET}")

    claude_path.write_text(claude_md)
    context_path.write_text(context_md)

    print(f"\n{C.GREEN}{C.BOLD}Done!{C.RESET} Generated:")
    print(f"  {C.GREEN}+{C.RESET} CLAUDE.md — your personalized AI context")
    print(f"  {C.GREEN}+{C.RESET} my-context.md — your detailed personal context")

    print(f"""
{C.CYAN}{C.BOLD}Next Steps:{C.RESET}

  1. Review your files:
     {C.DIM}cat CLAUDE.md{C.RESET}
     {C.DIM}cat my-context.md{C.RESET}

  2. Start using Claude Code:
     {C.DIM}claude{C.RESET}

  3. Test it: Ask Claude "Summarize my role and current priorities"

  4. Update shared context anytime:
     {C.DIM}git submodule update --remote{C.RESET}

{C.DIM}Edit CLAUDE.md and my-context.md anytime to refine your context.{C.RESET}
""")


# ─── File Generators ─────────────────────────────────────────────────────────

def generate_claude_md(d):
    responsibilities = "\n".join(f"- {r}" for r in d["responsibilities"]) if d["responsibilities"] else "- (update with your responsibilities)"

    tools_section = ""
    if d["tools"]:
        tools_section = "\n".join(f"- **{t['name']}** — {t['usage']} ({t['level']})" for t in d["tools"])
    else:
        tools_section = "- (update with your tools)"

    projects_section = ""
    if d["projects"]:
        for i, p in enumerate(d["projects"], 1):
            projects_section += f"{i}. **{p}**\n"
    else:
        projects_section = "1. (update with your current projects)\n"

    expectations = ""
    if d["claude_expectations"]:
        expectations = "\n".join(f"- {e}" for e in d["claude_expectations"])
    else:
        expectations = "- Help with daily security tasks\n- Code and query review\n- Documentation drafting"

    donts = ""
    if d["claude_donts"]:
        donts = "\n".join(f"- {x}" for x in d["claude_donts"])

    learning = ""
    if d["cert_goals"]:
        learning = "\n".join(f"- {g}" for g in d["cert_goals"])
    if d["quarterly_learning"] and d["quarterly_learning"] != "TBD":
        learning += f"\n- This quarter: {d['quarterly_learning']}"

    return f"""# CLAUDE.md — {d['name']}'s ContextOS

> This file is auto-loaded by Claude Code every session.

---

## Who I Am

**{d['name']}** — {d['title']} on the {d['team']} team.

- **Email:** {d['email']}
- **Focus areas:** {d['focus_areas']}
- **Current priority:** {d['current_priority']}

---

## My Role & Responsibilities

{responsibilities}

---

## My Tools & Systems

### Primary Tools
{tools_section}

### Access & Permissions
{d['access_levels']}

### MCP Servers Available
{d['mcp_servers']}

---

## Current Projects

{projects_section}
---

## How I Work

### Preferred Working Style
- Best focus time: {d['focus_time']}
- Communication style: {d['comm_style']}
- AI usage: {d['ai_usage']}

### What I Need From Claude
{expectations}

### What I Don't Want
- Don't make security decisions for me — surface options and risks, I decide
- Don't hallucinate tool outputs or scan results — if you can't run it, say so
- Don't skip security guardrails (see `shared-context/security-guardrails.md`)
- Don't store or echo back credentials, API keys, or PII
- **Don't write to `shared-context/`** — it's a read-only submodule managed by the team via PRs
{donts}

---

## Context Loading

### Personal Context
- `my-context.md` — My detailed role, skills, learning goals, and preferences

### Shared Team Knowledge
- `shared-context/team-overview.md` — Team structure and responsibilities
- `shared-context/compliance-frameworks.md` — FedRAMP, CMMC, CIS, NIST references
- `shared-context/tools-and-integrations.md` — Tool inventory and integration docs
- `shared-context/approved-prompts.md` — Vetted prompts for common tasks
- `shared-context/security-guardrails.md` — Security constraints and rules

### Workflows (load when doing the work)
| Workflow | When to Use |
|----------|-------------|
| `shared-context/workflows/cloud-security-scan.md` | Running or reviewing cloud security scans |
| `shared-context/workflows/vulnerability-analysis.md` | Triaging or analyzing vulnerabilities |
| `shared-context/workflows/compliance-reporting.md` | Generating compliance reports or evidence |
| `shared-context/workflows/soc-ticket-triage.md` | Triaging SOC alerts or tickets |
| `shared-context/workflows/risk-assessment.md` | Conducting risk assessments |

---

## Learning Goals

{learning if learning else '- (update with your learning goals)'}

---

## Session Start

At the start of any session:
1. This file loads automatically
2. Check what I'm working on (ask if unclear)
3. Load relevant shared context and workflows as needed
4. Build first, ask second — produce something I can refine

**Quick start:** *"What are we working on today?"*
"""


def generate_context_md(d):
    strong = "\n".join(f"- {s}" for s in d["strong_skills"]) if d["strong_skills"] else "- (update)"
    growing = "\n".join(f"- {s}" for s in d["growing_skills"]) if d["growing_skills"] else "- (update)"
    certs = "\n".join(f"- {c}" for c in d["certifications"]) if d["certifications"] else "- None yet"
    cert_goals = "\n".join(f"- {g}" for g in d["cert_goals"]) if d["cert_goals"] else "- (update)"

    tools_table = ""
    if d["tools"]:
        for t in d["tools"]:
            tools_table += f"| {t['name']} | {t['usage']} | {t['level']} |\n"
    else:
        tools_table = "| (update) | | |\n"

    active = ""
    if d["projects"]:
        for i, p in enumerate(d["projects"], 1):
            active += f"{i}. {p}\n"
    else:
        active = "1. (update)\n"

    upcoming = ""
    if d["upcoming_projects"]:
        for p in d["upcoming_projects"]:
            upcoming += f"- {p}\n"
    else:
        upcoming = "- (none listed)\n"

    completed = ""
    if d["completed_projects"]:
        for p in d["completed_projects"]:
            completed += f"- {p}\n"
    else:
        completed = "- (none listed)\n"

    return f"""# My Context — {d['name']}

---

## Role Details

- **Title:** {d['title']}
- **Team:** {d['team']}
- **Reports to:** {d['manager']}
- **Tenure:** {d['tenure']}
- **Specialization:** {d['specialization']}

---

## Skills & Experience

### Strong Areas
{strong}

### Growing Areas
{growing}

### Certifications
{certs}

### Certification Goals
{cert_goals}

---

## Daily Work

### Typical Day
{d['typical_day']}

### Key Stakeholders
(Update with your key stakeholders and when you interact with them)

---

## Tools I Use Daily

| Tool | What I Use It For | Proficiency |
|------|-------------------|-------------|
{tools_table}
---

## Current Projects

### Active
{active}
### Upcoming
{upcoming}
### Recently Completed
{completed}
---

## Learning Plan

### This Quarter
{d['quarterly_learning']}

### This Year
{d['yearly_learning']}

---

## Working Preferences

- **Best focus time:** {d['focus_time']}
- **Communication style:** {d['comm_style']}
- **How I like to receive feedback:** {d['feedback_pref']}
- **How I use AI:** {d['ai_usage']}

---

## Notes

{d['additional_notes'] if d['additional_notes'] else '(Add any additional context here)'}
"""


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.YELLOW}Setup cancelled.{C.RESET} Run python3 setup.py again when ready.")
        sys.exit(0)
    except EOFError:
        print(f"\n\n{C.YELLOW}Setup cancelled.{C.RESET}")
        sys.exit(0)
