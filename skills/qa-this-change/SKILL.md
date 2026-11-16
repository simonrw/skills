---
name: qa-this-change
description: Black-box QA of a PR, branch, or uncommitted change. Exercise the running software against the user's description of the feature to find bugs and gaps. Use when the user asks to QA, manually test, or try out a change.
---

# QA this change

Test the change as a **black box**. The user's description is the **oracle**: it defines what correct behaviour looks like, and the running software is the only evidence of what the change does.

## Sources

Learn the feature from what a user of the software could see:

- the user's description, plus the PR title, body, and linked issue when the target is a PR
- user-facing docs, `--help` output, API schemas, and UI text
- build and run instructions (README, task runner, CI config)
- the behaviour of the running software

The diff and the implementation source stay closed for the whole session, including when a test fails. A failure is reported as observed behaviour, with its cause left to the author.

## 1. Establish the oracle

Identify the target: a PR, a branch, or the current working tree.

Write down, from the sources above:

- **Behaviour**: what the change lets a user do, or what it does differently from before
- **Entry point**: the command, endpoint, screen, or API a user reaches it through
- **Expected outcome**: what the user observes when it works
- **Preconditions**: data, configuration, accounts, or services it needs

Ask the user for every item you cannot fill in, in one batch, with a concrete question per item. Ask too when the description is ambiguous enough that two readings would produce different expected outcomes. Proceed once each item is filled in by the user or a source, not by a guess.

## 2. Get it running

Check out a PR or branch into a separate worktree so the user's working tree stays untouched. Test an uncommitted change in place, leaving its files as they are.

Build and start the software the way its docs say. Confirm you are running the changed build by observing the new behaviour once through its entry point. If it will not build or start, report that as the first finding and stop.

## 3. Write the charter

Before testing, list the cases you will run. Derive them from the oracle, one or more per row that applies:

| Area | What to probe |
| --- | --- |
| Described behaviour | every statement in the description, each as its own case |
| Boundaries | empty, one, many, maximum, just past the maximum |
| Invalid input | wrong type, malformed, missing, duplicated, oversized, unicode, whitespace |
| Sequence and state | repeat the action, reverse the order, undo, retry after failure, stale state from an earlier run |
| Interruption | cancel midway, kill the process, lose the dependency, then observe recovery |
| Combinations | the feature together with existing flags, modes, and configuration |
| Neighbours | existing behaviour that shares the entry point and should be unchanged |
| Feedback | error messages, exit codes, status codes, logs, and help text match what happened |
| Environment | the platforms, shells, browsers, or versions the description claims to support |

Each case states an action and the outcome the oracle predicts. Where the oracle predicts nothing for a case, run it anyway and record the result as a question for the user.

## 4. Run the charter

Run every case against the real software through its user-facing entry point. For each one, record the exact input, the observed output, and pass or fail against the predicted outcome.

When a case fails or surprises you:

1. Re-run it to confirm it reproduces, and note it as intermittent if it does not.
2. Shrink it to the smallest input and fewest steps that still fail.
3. Probe around it: vary one thing at a time to find where behaviour flips from correct to incorrect.
4. Add the cases this suggests to the charter.

Testing is complete when every charter case has a recorded result and the latest round of probing added no new cases.

## 5. Report

Lead with the verdict: whether the change does what the description says.

Then give:

- **Bugs**: observed behaviour that contradicts the oracle. For each: severity, exact reproduction steps, expected outcome, observed outcome, and whether it reproduces every time.
- **Gaps**: described behaviour that is missing, or that you could not exercise, and what blocked you.
- **Questions**: behaviour the oracle does not cover, with what you observed, for the user to rule on.
- **Coverage**: the charter as a table of case, result, and evidence, including the cases that passed.

State what you built and ran (commit, platform, configuration) so the results can be reproduced. Leave fixing to the user unless they ask for it.
