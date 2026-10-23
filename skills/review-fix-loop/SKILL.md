---
name: review-fix-loop
description: Review a branch or PR with independent agents, triage findings, and iterate through focused fixes and fresh full reviews.
---

# Review and fix a branch

## Establish scope

1. Read repository instructions and the originating spec or issue. Record the base commit, committed head, and working-tree state. Include unpushed commits and exclude pre-existing uncommitted changes. Use fixed commit ranges for full reviews. Inspect committed file contents and, when the working tree differs from the recorded head, run verification in a clean checkout of that head. Preserve the original working tree and commit only the agreed fix files.
2. Create a unique directory under `.scratch/` with a top-level `README.md`, numbered issue files under `issues/`, and review evidence. Follow the repository's issue-tracker conventions.
3. Map significant changed behavior to its callers, persisted state, dependencies, and tests. Assign review ownership for each area and for interactions between areas. For a large change or several independent failure modes, split correctness work among reviewers with explicit scopes. A style or abstraction pass does not substitute for correctness coverage.

## Independent review

Use fresh reviewer agents for each full review round. Follow the environment's subagent routing instructions.

Give reviewers the fixed commit range, relevant requirements, repository instructions, their scope, and the evidence requirements below. Initial briefs should contain raw requirements and code pointers, without implementation conclusions, previous approvals, or passing-test totals. In later rounds, assess requirements and implementation first, then reconcile prior findings and unresolved objections before returning the report. Include history in the brief when routing requires it, while preserving this assessment order and treating previous conclusions as unverified.

Each reviewer must derive the relevant invariants from requirements and callers before assessing implementation and prior findings. Read surrounding code and consumers where needed to establish behavior. Review assertions in comments and documentation against the code.

Use each reviewer type:

- Correctness: investigate observable failures, logical errors, data loss, and violated invariants. Apply the relevant checks below. Prioritize severity by impact and trigger, rather than ease of fixing.
- Style and understandability: identify material obstacles to understanding the code, misleading documentation, and unnecessarily complex patterns.
- Abstractions: identify repeated rules whose consolidation would simplify behavior or prevent divergence. Propose abstractions only when they reduce complexity.

### Correctness checks

Select checks based on the changed behavior. Explain omissions where the scope map identifies a plausible risk.

- Persistent mutations and crash recovery: enumerate writes, renames, external side effects, and completion markers. Distinguish caught exceptions from abrupt process death. Check recovery after interruption between mutations, including first installation and replacement of existing state. Establish what survives the process and how recovery discovers it.
- Dependency graphs and mutable state: examine sibling branches, shared nodes, conflicting versions, and traversal order. Verify each consumer receives only its declared dependency closure's state. A linear graph does not establish branch isolation.
- Caches and idempotency: identify inputs that affect persisted outputs, including environment, runtime configuration, dependencies, artifacts, and destination paths. Change relevant inputs between cold and warm calls. Inspect persisted contents as well as returned handles. Check that failures and partial state cannot produce a false cache hit.
- Concurrency: examine lock scope, competing writers, readers during publication, and recovery by another process. State assumptions about filesystem and process boundaries.
- External data and compatibility: check archive paths and permissions, metadata round trips, older persisted formats, and real consumer behavior where relevant. Follow data through parsing, storage, fingerprints, execution, and use.

For suspected bugs, seek a minimal reproduction or an existing test that distinguishes correct and incorrect behavior. Use controlled fault injection or a child process when testing abrupt termination. Record static findings as static findings when execution is unavailable.

### Required reviewer output

Return findings and a concise coverage report even when no findings are found.

For each finding, give severity, file and line, violated invariant, concrete trigger, observable consequence, supporting evidence, and a minimal fix direction. Distinguish reproduced failures from deductions and unresolved hypotheses.

Correctness reviewers report each assigned area's invariant, code and consumers inspected, reproduction or test performed, result, and remaining uncertainty. Label the evidence as static inspection, executed verification, or unverified. Style and abstraction reviewers report inspected scope and evidence supporting their recommendations. Existing tests passing is supporting evidence only for behavior they exercise. A test count alone is not a coverage report.

## Triage and fix

1. Reconcile overlapping findings and investigate conflicting reviews using the code or a reproduction. Keep unresolved objections visible. Cross-check every finding supplied by the user or earlier reviews against the current code; assign each a disposition supported by evidence.
2. Summarize findings in the scratch README and link numbered issue files. Preserve reviewer evidence and unverified areas. Present findings to the user for triage and confirmation or exclusion. Implement findings the user confirms or that fall under existing explicit authorization to fix findings. Preserve that authorization across rounds; review-only authorization does not authorize implementation.
3. For each agreed change, sequentially delegate implementation, then delegate a fresh focused review of only that fix. Include the original finding, intended invariant, exact fix diff or range, prior review objections, and implementation checks. Include new files explicitly when the fix is uncommitted.
4. Where practical, add a regression that fails on the original behavior and passes with the fix. Test the reported consequence rather than mirroring implementation details. A crash regression must bypass exception cleanup; a cache regression must inspect persisted outputs; a graph regression must exercise branching.
5. Iterate until the focused reviewer resolves the finding and any introduced defects. Then commit that change with a descriptive message explaining the issue and behavior. Keep findings file identifiers and paths out of commit messages. Group related findings only when one coherent fix addresses their shared cause.

Do not push changes.

## Full re-review and completion

After all agreed fixes are committed, repeat the full review against the original base and new committed head with fresh agents of each reviewer type. Recheck interactions and regressions across fixes, beyond the individual patches. Iterate on new findings through triage and focused fixes.

Before declaring completion, reconcile reviewer coverage with the scope map. Investigate significant unverified areas or report the limitation explicitly. Verify that every known finding is fixed, excluded by the user, or still open. Separate exclusions from resolved findings.

Finish when the latest full reviews have no unresolved actionable findings within the agreed scope, relevant checks have passed, and the working-tree state is accounted for. Report the commits, validation, exclusions, and remaining uncertainty. Say that the reviews found no remaining issues within their scope; avoid claiming that passing tests or reviewer agreement proves the absence of bugs.
