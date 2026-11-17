---
name: my-code-review
description: "Review the changes since a fixed point (commit, branch, tag, or merge-base) along two axes: Standards (does the code follow this repo's documented coding standards?) and Spec (does the code match what the originating issue/spec asked for?). Runs both reviews in parallel sub-agents and reports them side by side. Use when the user wants to review a branch, a PR, work-in-progress changes, or asks to \"review since X\"."
---

Call the `code-review` skill in a subagent.

In another subagent, try to consider more than just the diff. Look for conflicts with recent changes to the files that have been edited. Look for motivation for why the code being replaced was there in the first place. Try to understand the change IN CONTEXT with the codebase, not in isolation.

When subagents have finished, collect their responses, filter out minor nitpicks and present a single list of actionable next steps in descending priority order with
* justification on why the issue is worth changing
* what to implement to resolve the issue
