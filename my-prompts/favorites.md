# My Favorite Prompts

> Proven prompts that consistently produce good output. Formatted and ready to use.

---

### Quick Role Summary
**When to use:** Start of any session to verify Claude has your context loaded correctly.
**Prerequisites:** Completed setup (my-context.md exists)

> Summarize my role, current priorities, and the tools I have available. Keep it under 10 lines.

**What you'll get:** A concise summary confirming Claude knows who you are.
**Safety note:** If anything is wrong, edit my-context.md or CLAUDE.md to correct it.

---

### Available Workflows
**When to use:** When you're not sure what workflows or shared context are available.
**Prerequisites:** Shared context submodule initialized

> List all available files in shared-context/ with a one-line description of each. Then ask me which one I want to load.

**What you'll get:** A menu of all team resources you can jump into.
**Safety note:** None — read-only operation.

---

### Meeting Prep
**When to use:** Before an important meeting, presentation, or conversation.
**Prerequisites:** Your role and projects in my-context.md

> I have a meeting with [PERSON/GROUP] about [TOPIC] in [TIMEFRAME].
>
> Based on my role and current projects, help me prepare:
> 1. Key points I should raise
> 2. Questions I should be ready to answer
> 3. Data or examples I should have on hand
> 4. Potential objections or concerns and how to address them
> 5. A clear ask or desired outcome for the meeting

**What you'll get:** A structured prep sheet tailored to your role and context.
**Safety note:** Review for accuracy — Claude doesn't know internal politics or recent developments you haven't told it about.

---

### Status Update Writer
**When to use:** When you need to write a progress update for leadership, a standup, or a stakeholder report.
**Prerequisites:** Current projects in my-context.md

> Write a status update on my current projects for [AUDIENCE — e.g., my manager, leadership, the team].
>
> For each active project, include:
> 1. Current status (on track / at risk / blocked)
> 2. What was accomplished since the last update
> 3. What's coming next
> 4. Any blockers or decisions needed
>
> Keep it [LENGTH — e.g., under 200 words / one paragraph per project].

**What you'll get:** A polished status update ready to send.
**Safety note:** Always verify facts and dates before sending. Add any recent developments Claude doesn't know about.

---

### Decision Framework
**When to use:** When you're weighing options and need to think through a decision clearly.
**Prerequisites:** None

> I need to decide: [DESCRIBE THE DECISION]
>
> Help me think through it:
> 1. What are my realistic options? (including "do nothing")
> 2. For each option: pros, cons, risks, and effort required
> 3. What information am I missing that would make this easier?
> 4. What would you recommend and why?
> 5. What's the reversibility of each option?

**What you'll get:** A structured decision matrix with a recommendation.
**Safety note:** Claude doesn't know your full organizational context. Use this as a thinking tool, not an oracle.

---

<!-- Add your own battle-tested prompts below using the format above -->
