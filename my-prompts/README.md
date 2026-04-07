# My Prompts

> Your personal prompt workshop. Develop, refine, and share prompts.

---

## How It Works

```
my-prompts/
├── README.md              ← You are here
├── working-prompts.md     ← Experiments and works-in-progress
├── favorites.md           ← Your proven, go-to prompts
└── contributions/         ← Prompts ready to share with the team
```

## Workflow

1. **Experiment** — Try new prompts in `working-prompts.md`. Don't worry about format.
2. **Refine** — When a prompt consistently works well, move it to `favorites.md` with proper formatting.
3. **Share** — Copy great prompts to `contributions/` and PR them to the team's `shared-context/prompts/` repo.

## Prompt Format (for favorites and contributions)

```markdown
### Prompt Name
**When to use:** When you need to [situation]
**Prerequisites:** [What data/access/context you need]

> [The prompt — copy-pastable, with [BRACKETED] placeholders]

**What you'll get:** [Description of expected output]
**Safety note:** [What to verify before acting on output]
```

## Contributing to the Team

When you have a prompt that would help others:

1. Copy it to `contributions/` with proper formatting
2. Clone the team repo: `git clone https://github.com/YOUR-ORG/contextOS-team.git`
3. Add your prompt to the appropriate role file in `prompts/`
4. PR it with: what it does, how you tested it, which role benefits
5. See `shared-context/prompts/README.md` for the full contribution process
