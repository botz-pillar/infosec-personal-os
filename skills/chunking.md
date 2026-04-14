# Chunking — Break Big Work Into Single-Purpose Prompts

> Load when a task feels too big for one prompt, or when outputs come back shallow because the ask was too broad.

**Last Updated:** 2026-04-14

---

## The Rule

**Each prompt asks for one clear thing.**

When Claude tries to do everything at once, every part gets less attention. Break the work into steps. Review between steps. Adjust direction before committing further.

---

## Two Kinds of Chunking

### 1. Chunking the Work

**Too big:** "Write me a full marketing strategy with content calendar, email sequences, and social posts for the next quarter."

**Chunked:**
1. "Given our product and audience, outline three main themes for Q2 content." *(review, adjust)*
2. "For theme 1, draft a 4-week content calendar." *(review, adjust)*
3. "Write the first email in the nurture sequence for theme 1."

Each step builds on the last. If something goes wrong at step 3, only step 3 gets redone.

### 2. Chunking the Input

When feeding Claude long documents or large datasets:

1. **Give the structure first:** "I'm giving you a 40-page report in sections. Here's the TOC. Sections come next."
2. **Feed sections in order.** After each, confirm pickup: "What are the key claims in this section?"
3. **After the last section, ask for synthesis** across everything.

Structured sequential input beats one wall of text.

> **Bonus:** Tables and spreadsheets are already token-efficient. Don't convert them to paragraphs before giving them to Claude.

---

## Signals You Need to Chunk

- Output feels shallow across multiple areas
- The prompt you're writing is longer than one screen
- You're combining multiple verbs ("research AND draft AND format")
- Review feedback targets one piece, but you'd have to redo everything

---

## Pairs With

- `skills/prompt-framework.md` — after chunking, structure each sub-prompt with the five-part framework
