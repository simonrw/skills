---
name: ping-pong
description: Improve a deliverable through agent pair programming. Use when the user wants two subagents with complementary focuses to alternate work, with an independent third reviewer and context-aware handoffs.
---

# Pong-pong

Coordinate two subagents that take turns improving the same deliverable, plus a third subagent that reviews it independently. Work in small, verifiable slices. Each partner inspects the other's work before taking the next turn.

You are the coordinator. Own the task brief, baton, and completion decision. The pair owns implementation. The reviewer owns findings. Keep user decisions and progress in the main conversation. Pass the baton autonomously within a small batch, then pause for human review.

## Set up the pair

Read the task and applicable project instructions. Record the requested outcome, acceptance criteria, constraints, existing work, and how to check the result. Capture a baseline that distinguishes this task's changes from pre-existing edits.

Choose two complementary focuses. Default to:

| Agent | Focus |
| --- | --- |
| A | Correctness and coverage. Does the result satisfy the request, including relevant failure cases? |
| B | Simplicity and maintainability. Can the result be easier to understand, use, and change? |
| Reviewer | Independently check the complete result against the request and project constraints. |

Adapt the focuses to the deliverable when useful, such as factual accuracy and editorial clarity for prose. State the chosen focuses once. Both partners remain responsible for the whole task; a focus is a lens, not exclusive ownership of certain files or checks.

Start A and B with only the task brief, their focus, applicable instructions, artifact locations, and their initial assignment. Keep the reviewer slot available until a review checkpoint. Use the available delegation tools without assuming particular model names. Subagents report to you and do not spawn further agents. If delegation is unavailable, explain that this workflow cannot run and offer a single-agent alternative.

## Pass the baton

Only the driver may edit the deliverable or run commands that mutate shared state. The navigator inspects and advises. Transfer ownership only after the previous driver has stopped writing and its mutating commands have finished. The reviewer stays read-only.

1. Assign A one bounded slice with an observable completion condition. A implements it, runs the relevant checks, and returns a handoff. Choose a slice that leaves enough context for verification and explanation.
2. Give B the handoff and access to the actual changes. While read-only, B checks the slice through its focus and reports material concerns with evidence. Agreement does not require a cosmetic edit.
3. Resolve concerns, then give B the baton. B addresses accepted findings and implements the next bounded slice if one remains. B checks the result and returns a handoff.
4. A navigates B's changes, then takes the baton for the next slice. Repeat A to B to A until the acceptance criteria are met.

Keep each turn tied to the shared result. Both partners must inspect the artifact and get an opportunity to drive; a driver may report that no change is needed. For code, use failing-test and implementation swaps when they fit the task or the user requests TDD. For other deliverables, use an equivalent concrete check, such as a supported claim or a working example.

Settle disagreements with the brief, source material, or a focused experiment. Record the decision and its reason. Reopen it only when new evidence appears. If two successive passes make no material progress, diagnose the obstacle and change the slice or approach. Outside scheduled review pauses, ask the user when a missing decision blocks the task.

## Pause for human review

Keep each batch small enough for the user to review comfortably. Default to a pause after two to four driver turns, adjusting for the cumulative changes since the last pause. Pause sooner for substantial code changes, changes spread across several areas, or a consequential design decision. Judge review effort by changed behavior and complexity as well as line count. Split a large proposed slice before assigning it.

At each handoff, decide whether another slice would make the batch too much to review. If so, freeze edits and have the reviewer inspect the changes since the last pause, using the initial baseline for the first batch. Ask it for a concise user-facing summary covering:

- What changed and why, with links to the relevant files or diff.
- Checks performed, results, and unresolved findings or decisions.
- The proposed scope of the next batch.

Present that summary, ask whether to continue or adjust direction, and end the turn. Keep the pair idle until the user responds. Address review findings in the next authorized batch rather than extending the current batch before the user sees it.

Save a stable snapshot or diff reference for the artifact shown at each pause, including uncommitted changes. Record it in the state note so the next summary covers exactly what changed since that point. Preserve unresolved findings across pauses.

## Keep context bounded

Maintain one compact state note in session scratch storage, outside the deliverable unless the project has an established location. Update it after each pass. Keep the current state and consequential decisions; link to artifacts and logs for detail.

Use this handoff shape, normally within 300 words:

```text
Outcome and acceptance criteria:
Current artifact and baseline:
Last human review snapshot and driver turns since that pause:
Completed slice and changed locations:
Checks run, results, and checks still pending:
Decisions and reasons:
Open findings or blockers:
Next driver, slice, and completion condition:
```

Send changes since the previous handoff and pointers to the relevant files. Agents read the smallest useful sections and expand when dependencies require it. Store long logs separately. A handoff reports evidence and uncertainty; it is not a transcript or a substitute for inspecting the artifact.

At every handoff, assess whether each agent has room for another slice, its checks, and a handoff. Use context usage when the runtime exposes it. Otherwise use concrete signals such as repeated rereading, forgotten constraints, or a growing investigation that no longer fits a bounded assignment. Ask agents to checkpoint before they run out of room; never invent token counts or treat a message as clearing context.

When an agent needs replacement, first save its handoff and confirm it has stopped writing. Retire or close it using the runtime's supported lifecycle, then start a fresh instance of the same role with the brief, current state note, and artifact pointers. Avoid forking the full conversation. Have the replacement confirm its assignment and unresolved findings before editing. Keep only two pair roles and one reviewer active. If slots cannot be reclaimed, use supported compaction or report the limitation rather than silently accumulating agents.

After your own context reset, read the state note and reconcile it with the actual artifacts and agent status before assigning work. Establish who holds the baton before any edits resume.

## Review the result

Request independent review at each human review pause, when the pair believes the task is complete, or at a milestone where a wrong assumption would make later work expensive. Pause reviews cover the current batch; final review covers the complete task. Freeze edits for the review so its findings refer to a stable artifact.

Give the third agent the original request, acceptance criteria, applicable instructions, baseline, current artifact, and validation entry points. Let it form its own assessment before reading the pair's reasoning or self-review. It must inspect the result and verify the consequential claims rather than accept the handoffs as proof.

Ask for actionable findings with a location, evidence, impact, and suggested check. Separate defects and unmet requirements from optional preferences. A clean review is a valid outcome.

Return accepted findings to the next driver in the rotation, respecting human review pauses before resuming edits. The partner checks the fix, and the reviewer verifies the affected criteria after the artifact is stable again. Record evidence for any finding you reject. Refresh the reviewer's context by the same handoff process when needed.

## Finish

Finish when the acceptance criteria are satisfied, relevant checks have passed or their limitations are explicit, and the independent review has no unresolved material findings. Stop agents and summarize the deliverable, meaningful decisions, validation, and any remaining limitations to the user. If a blocker or resource limit prevents completion, preserve the handoff and report the work as incomplete.
