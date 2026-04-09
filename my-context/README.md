# My Context — Extended

> Deep context files for specific areas of your work. Referenced from CLAUDE.md when relevant.

---

## How to Use

Create markdown files here for any topic that needs more context than fits in `my-context.md`. Reference them from your `CLAUDE.md` under the Context Loading section:

```markdown
### Additional Context (load when relevant)
- `my-context/aws-accounts.md` — AWS account inventory and access levels
- `my-context/investigation-notes.md` — Context for ongoing investigations
```

Claude loads these on demand — they don't add to your base context size.

## Suggested Files

Create any of these that match your work:

| File | What to Put Here |
|------|-----------------|
| `aws-accounts.md` | Account IDs, regions, roles, access levels, key services per account |
| `investigation-notes.md` | Context for ongoing investigations (reset when case closes) |
| `vendor-contacts.md` | Key vendor relationships, support tiers, escalation paths |
| `architecture-notes.md` | System architecture relevant to your security work |
| `runbooks.md` | Personal runbooks that aren't shared with the team |
| `meeting-notes.md` | Recurring meeting context, action items, decisions |

## Rules

- This directory is gitignored — your files stay local and private
- Keep files focused on one topic each
- Update or delete files when they become stale
- Never put credentials, tokens, or secrets in these files
