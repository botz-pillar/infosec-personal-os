# InfoSec Example Setups

Three complete ContextOS Personal configurations for common InfoSec roles. Each shows a finished `CLAUDE.md` + `my-context.md` pair — the output a real user would have after running the 7-step onboarding.

**Last Updated:** 2026-04-14

---

## What's Here

| Example | Role | Focus |
|---------|------|-------|
| `soc-analyst-example/` | Tier 2 SOC Analyst | Alert triage, incident response, SIEM operations |
| `cloud-security-engineer-example/` | Cloud Security Engineer | AWS/Azure security, IaC scanning, cloud posture management |
| `compliance-manager-example/` | Compliance Manager | FedRAMP/CMMC audit prep, POA&M management, evidence collection |

Each folder contains:
- `CLAUDE.md` — a personalized master router showing what a finished routing table looks like for that role
- `my-context.md` — detailed context covering skills, tools, projects, preferences, learning goals

---

## How to Use

1. **Browse the example closest to your role.** Notice the level of specificity — not "security tools" but "Splunk for SIEM queries, expert."
2. **Study the patterns, not the content:**
   - How short is the `CLAUDE.md`?
   - How are constraints phrased in "What I Don't Want"?
   - How are tools listed (name + version + proficiency)?
   - How does the routing table connect personal tasks to shared-context files?
3. **Run the real onboarding.** Don't copy these files into your setup — the SessionStart hook will walk you through your own 7-step flow. The examples are reference only.

---

## Contributing a New Role Example

Another InfoSec role missing (e.g., Threat Hunter, IR Lead, Pen Tester, Red Team)? Submit a PR.

Requirements:
- Both files (`CLAUDE.md` + `my-context.md`) must be complete and anonymized
- Content should be realistic but not tied to a specific company, client, or identifiable person
- Follow the v2 structure (routing table, naming conventions, etc.)

---

## Non-InfoSec Domains

Want to contribute a non-security example setup? Add a sibling folder under `examples/`:

- `examples/engineering/` — software engineers, DevOps, SRE
- `examples/marketing/` — growth, content, brand
- `examples/legal/` — in-house counsel, firm associates
- `examples/data-science/` — MLE, DS, ML researcher

See [`examples/README.md`](../README.md) for contribution guidelines.
