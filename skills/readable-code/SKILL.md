---
name: readable-code
description: Use when writing source code to help improve the readability and maintainability by a human, and encouraging simplicity
---

When writing code, always strive for the simplest solution. Feel free to take time exploring potential approaches, but always settle on one that you think is the most readable and maintainable for a human. 

## The ladder

Stop at the first rung that holds:

1. **Does this need to exist at all?** Speculative need = skip it, say so in one line. (YAGNI)
2. **Already in this codebase?** A helper, util, type, or pattern that already lives here → reuse it. Look before you write; re-implementing what's a few files over is the most common slop.
3. **Stdlib does it?** Use it.
4. **Already-installed dependency solves it?** Use it. Never add a new one for what a few lines can do.

The ladder is a reflex, not a research project — but it runs *after* you understand the problem, not instead of it. Read the task and the code it touches first, trace the real flow end to end, then climb. Two rungs work → take the higher one and move on. The first lazy solution that works is the right one — once you actually know what the change has to touch.

Minimize concepts and moving parts, not line count. Prefer readable, idiomatic code with descriptive names and explicit steps. Use a one-liner only when it is easier to understand than the expanded form. Judge simplifications by reduced cognitive load, not lines deleted.

**Bug fix = root cause, not symptom.** A report names a symptom. Before you edit, grep every caller of the function you're about to touch. The lazy fix IS the root-cause fix: one guard in the shared function is a smaller diff than a guard in every caller — and patching only the path the ticket names leaves every sibling caller still broken. Fix it once, where all callers route through.

## Rules

- No unrequested abstractions: no interface with one implementation, no factory for one product, no config for a value that never changes.
- No boilerplate, no scaffolding "for later", later can scaffold for itself.
- Deletion over addition. Boring over clever.

## Output

Don't overly summarize what you've implemented. The code should ideally say for itself. However, if it's a large feature, spanning more than about 100 lines, then provide a concise summary, at most 3 short bullet points. 

## When NOT to be lazy

Never simplify away: input validation at trust boundaries, error handling that prevents data loss, security measures, accessibility basics, anything explicitly requested. User insists on the full version → build it, no re-arguing.

Never lazy about understanding the problem. The ladder shortens the solution, never the reading. Trace the whole thing first — every file the change touches, the actual flow — before picking a rung. Laziness that skips comprehension to ship a small diff is the dangerous kind: it dresses up as efficiency and ships a confident wrong fix. Read fully, then be lazy.

Though testing is important, look for high-level tests that test multiple features together rather than many low-level unit tests with lots of mocking and fragility.
