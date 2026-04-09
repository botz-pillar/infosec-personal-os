Load `shared-context/workflows/vulnerability-analysis.md` and enter threat hunting mode.

Read my personal context from `my-context.md` to understand my tools and environment.

Then ask me: "What's the hunting hypothesis? Choose one or describe your own:
1. Lateral movement from a compromised endpoint
2. Data exfiltration via DNS or HTTPS
3. Persistence mechanisms (scheduled tasks, services, registry)
4. Credential harvesting or pass-the-hash
5. Anomalous cloud API activity
6. Custom hypothesis"

After I choose, build a structured hunt plan:
1. **Hypothesis:** Clear statement of what we're looking for
2. **Data sources:** Which logs and telemetry to query
3. **Detection queries:** SIEM queries in my query language (SPL, KQL, etc.)
4. **IOC patterns:** What to look for in the results
5. **Pivot points:** Where to dig deeper if we find something
6. **Documentation:** Template for recording findings

Use my actual SIEM, EDR, and log sources. Build real queries, not pseudocode.
