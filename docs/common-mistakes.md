# Common Mistakes

> Seven traps people fall into when setting up their folder architecture. Read this before you finalize your structure.

**Last Updated:** 2026-04-14

---

## Mistake 1: Making `CLAUDE.md` too long

`CLAUDE.md` is a router. Its job is to tell Claude where things are and where to go. It is **not** a project brief, a style guide, or a brain dump of everything you want Claude to know.

**Why it hurts:** Claude burns tokens reading info irrelevant to the current task, and the signal (routing) gets buried in noise.

**The fix:** Your `CLAUDE.md` should fit on one screen (40–80 lines). Identity + routing table + naming + rules. Everything else goes in `my-context.md` or a `my-context/` subfile where it only loads when relevant. **If your `CLAUDE.md` is longer than 80 lines, you have context files hiding inside it. Pull them out.**

---

## Mistake 2: Skipping the routing table

Some people write folders and context files, but never put a routing table in `CLAUDE.md`. They assume Claude will figure it out.

**Why it hurts:** Without a routing table, Claude guesses. It might read everything (wasting tokens), or read the wrong context file. Output gets inconsistent — some responses great, some off — and you can't tell why.

**The fix:** A simple table:

| Task | Go To | Read |
|------|-------|------|
| Writing / drafting | (in place) | my-context.md; voice style |
| Team procedures | shared-context/ | relevant workflow |
| Personal prompts | my-prompts/ | favorites.md |

Three columns is enough. Add a Skills column if you wire in Layer 3 skills.

---

## Mistake 3: Too many workspaces

Eight workspaces for a project that really has two or three modes. Every one has its own `CONTEXT.md`. The routing table has twelve rows. The overhead now exceeds the work itself.

**Why it hurts:** Context files go stale. Claude spends more time navigating than working. You multiplied complexity instead of reducing it.

**The fix:** Start with 2–3 workspaces. The question is: *"Do I shift mental modes between these tasks?"* Writing and building are different modes — two workspaces. Drafting and editing are the same mode at different stages — one workspace with a process inside. If you're unsure whether something deserves its own workspace, it doesn't.

---

## Mistake 4: Writing context files about Claude instead of about the work

People fill context files with instructions about Claude's personality: "Be creative. Be concise. Think step by step. Use a warm tone." Thirty lines describing how Claude should behave. Two lines describing the actual work.

**Why it hurts:** Claude responds to context about the *work* far more than context about itself. "You are a senior copywriter" gives it a role. "The audience is mid-market HR directors who have tried three other tools and are skeptical of AI claims" gives it something to actually work with.

**The fix:** Flip the ratio. **80% describing the work** (what it is, who it's for, what's been done, what good looks like, what to avoid). **20% or less describing Claude's behavior.** If your context reads like a personality quiz, rewrite it. If it reads like a project brief a new team member could pick up and run with, you're in the right place.

---

## Mistake 5: Never updating context files

Set up in week one, got great results, never touched them again. Project evolves. New requirements, new direction. Context still says what it said on day one.

**Why it hurts:** Output drifts. You think Claude "got worse" when Claude is doing exactly what the stale context tells it to do.

**The fix:** Treat context files like working notes. Project changed? Edit. Learned something new Claude needs to know? Add it. Constraint no longer applies? Remove it. 30 seconds per edit. Highest-leverage habit in the system.

Add a **"Last Updated"** line at the top of every context file. When you see a date from six weeks ago on something active, you know to review it.

---

## Mistake 6: Everything in one flat folder

Opposite of too many workspaces. Everything lives in one flat directory. Fifty files. No subfolders. `CLAUDE.md` tries to route by file name alone.

**Why it hurts:** Claude reads the whole directory listing, picks what looks relevant, and often picks wrong. Equivalent to dumping every document on one desk.

**The fix:** More than 8–10 files at the same level? Add subfolders. Group by workspace first, then by stage or type within the workspace. The folder structure *is* the architecture — let it do that job.

---

## Mistake 7: Building the whole system before using it

Read `docs/setup-guide.md`. Get inspired. Spend a weekend building the perfect architecture with six workspaces, detailed context, naming conventions, skills wired everywhere, routing table with twenty rows. Haven't used Claude once.

**Why it hurts:** Half the decisions won't match how you actually work. Workspace boundaries wrong. Context files describe what you thought you'd need, not what you actually need. You end up rebuilding.

**The fix:** Build the minimum. One `CLAUDE.md`, 1–2 workspaces, one context file per workspace. Start working. After a few days you'll know what's missing — add it then. After a week you'll know what's wrong — fix it then.

**Your first version should take 15 minutes.** If it took longer, you over-built.

---

## The Pattern Across All Seven

They all point in the same direction: **keep the system small, focused on the work not on Claude, and update it as you go.** Let the structure grow from use, not from planning.

The folder architecture is powerful *because* it's simple. Folders and text files. The moment it starts feeling heavy or complicated, something went wrong. Go back to basics:

- `CLAUDE.md` is the map
- Context files are the rooms
- Skills and workflows are the tools

Each does only its one job. If each part is doing only its job, the system stays clean.
