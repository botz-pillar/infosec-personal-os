Load `shared-context/workflows/soc-ticket-triage.md` and enter triage mode.

Read my personal context from `my-context.md` to understand my role and tools.

Then ask me: "What alert or ticket are we triaging? Paste the alert details, ticket ID, or describe what you're seeing."

After I provide the alert, walk me through the triage workflow step by step:
1. Initial classification (true positive, false positive, benign true positive)
2. Severity assessment
3. Scope determination (affected systems, users, data)
4. Recommended investigation steps using my specific tools
5. Suggested response actions

Reference my tools and access levels from my context. If I have Splunk, suggest SPL queries. If I have CrowdStrike, suggest RTR commands. Adapt to what I actually use.
