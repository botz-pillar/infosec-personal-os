# Examples

Reference setups showing what a completed ContextOS looks like. The core template is domain-neutral; examples are organized by domain.

---

## Available Examples

### `infosec/` — Information Security

Three finished setups for security roles:

- `infosec/soc-analyst-example/` — Tier 2 SOC analyst focused on alert triage and incident response
- `infosec/cloud-security-engineer-example/` — AWS/Azure security, IaC scanning, cloud posture management
- `infosec/compliance-manager-example/` — FedRAMP/CMMC audit prep, POA&M management, evidence collection

Each folder contains a complete `CLAUDE.md` and `my-context.md` showing how a finished setup looks — routing tables, personal context, tool lists, project state.

---

## How to Use Examples

1. **Browse the closest role.** Don't copy blindly — use them for structure, not content.
2. **Notice the patterns:** routing tables stay short; context files are specific about tools and access; "what I don't want" sections are concrete.
3. **Adapt, don't replace.** Your actual answers from the 7-step onboarding will produce files specific to you.

---

## Contribute a New Domain Example

Want to add `examples/marketing/`, `examples/data-science/`, `examples/legal/`? Great.

1. Create the folder.
2. Drop in a `CLAUDE.md` and `my-context.md` showing a complete, anonymized setup.
3. Open a PR against `contextOS-personal`.

Good examples are specific enough to be useful but anonymized enough to be shareable.
