---
name: handoff-claude-session
description: Create a handoff document from an existing Claude Code session history without resuming the session or invoking Claude.
argument-hint: "<Claude session ID> [what the next session will focus on]"
disable-model-invocation: true
---

# Handoff a Claude session

Create a handoff for another agent from Claude Code's local session log. Treat the log as the source conversation: the Claude session is unavailable for further prompts.

## Process

1. Require the Claude session ID. If the user did not provide one, ask for it and stop. Do not guess from recent sessions, because the user can retrieve the ID without spending a Claude prompt.
2. Run `python3 scripts/extract_session.py <session-id> --output <scratchpad>/claude-session-<session-id>.md`, resolving `scripts/` relative to this skill. Use the OS temporary directory, not the workspace, for `<scratchpad>`.
3. Read the extracted history. Trace the user's objective, decisions, completed work, verification, failures, unresolved work, and the latest state. Inspect referenced files, diffs, commits, issues, or plans when they are available locally and needed to distinguish current state from stale conversation.
4. Write `<scratchpad>/handoff-<session-id>.md` for the receiving agent. If the user supplied a focus after the session ID, tailor the handoff to it.
5. Return the handoff path and a one-sentence summary.

Use filesystem reads and the bundled extractor only. Do not run `claude`, resume the session, invoke a model through a CLI or API, or send any prompt back into Claude.

## Handoff contents

Make the document concise and operational. Include:

- source session ID and working directory
- objective and relevant user intent
- current state, including completed and partially completed work
- decisions, constraints, and rejected approaches that still matter
- artifacts by path, URL, branch, commit, or issue
- verification already run and its result
- remaining work, blockers, and the clearest next action
- suggested skills for the receiving agent

Reference existing artifacts instead of copying their contents. Distinguish facts observed in the log or workspace from inference. Redact credentials, tokens, private keys, and unnecessary personal information from the handoff.
