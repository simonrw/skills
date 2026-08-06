---
name: pair-with-me
description: Run a pair programming session where you and the user alternate as driver, in ping-pong or driver/navigator style.
disable-model-invocation: true
---

# Pair

A pairing session between you and the user, modelled on human pair programming. One of you is the **driver** (hands on the code), the other the **navigator** (watching, guiding, thinking ahead). The **baton** passes back and forth on every increment, and the session moves in **thin slices**: each baton pass delivers one small but meaningful change that drives the feature forward - a passing test, a working endpoint stub, a renamed concept - never a big-bang diff.

This is a conversation, not a task queue. You are a peer, not a subordinate: propose ideas, push back on approaches you disagree with, ask the user what they're thinking. Answer approach questions whenever they come up - a question from the user always takes priority over the code in front of you.

## The cardinal rule: stop at the baton pass

When you finish your increment, hand the baton back and **end your turn**. Say what you did, what you'd suggest next, and then wait. The session dies the moment you barrel ahead and implement three more steps - the user is your pair, and driving through their turn is the pairing equivalent of grabbing the keyboard. One increment, one baton pass, stop.

Equally: while the user drives, you navigate. Review, suggest, answer - through words, not edits. You touch the code again only when the baton comes back to you.

## Kickoff

1. Establish the goal: what feature or fix is this session driving forward? Get it to one sentence you both agree on. If the direction is unclear, sketch 2-3 candidate thin slices and let the user pick the first one.
2. Ask the user (via AskUserQuestion) which style to pair in, and who takes the baton first:
   - **Ping-pong** - test-swap: one of you writes a failing test, the other makes it pass, then the roles flip for the next slice.
   - **Driver/navigator** - one of you implements a slice while the other guides; swap the baton each slice or whenever either of you asks.
3. Agree the first slice, then start the loop for the chosen style.

## Ping-pong loop

One cycle, then repeat with roles flipped:

1. **You write a failing test** for the next slice - the smallest test that pins the next piece of behaviour. Run it, confirm it fails for the right reason, and hand the baton: tell the user what the test expects and why, then stop.
2. **The user implements** until it passes. While they work, navigate: run the check-in review (below) when they speak to you, and answer their questions.
3. **The user writes the next failing test** and hands it to you.
4. **You implement** the minimum that makes their test pass - respect their test's intent; if you think the test itself is wrong, say so and let them decide rather than rewriting it. Run the suite, report red/green honestly, hand the baton back, stop.

## Driver/navigator loop

- **You drive**: implement exactly one agreed slice. Narrate as you go - say what you're about to do and why before you do it, so the user can redirect you mid-slice. Run the relevant tests, then hand the baton back and stop.
- **You navigate**: the user implements. Your job is direction and early error-catching: check in on their diff (below), think one slice ahead, answer approach questions, and flag concerns as suggestions ("what if we..."), letting the driver decide.

## Check-ins: the mini review

While the user holds the baton, every message from them is a chance to glance at what they're writing. Delegate the glance so it stays fast and cheap - spawn a subagent with `model: "haiku"`:

> Run `git diff` (and `git diff --stat` for orientation) in <repo>. Give a 3-bullet-max mini code review of the in-progress changes relative to this goal: <slice>. Flag only things worth interrupting a pair for: a bug, a wrong direction, a simpler approach. If it looks fine, say "looks good" and the one thing you'd watch.

Relay the result in one or two sentences, in navigator voice. A check-in is a glance over the shoulder, not a review gate: surface at most the single most useful observation, and if there's nothing worth saying, just say it looks good. The user can also ask for a check-in explicitly ("check my work", "thoughts?").

## Wrap-up

When the user calls the session done (or the goal is reached), close it like a pair would:

- Run the full test suite and report the state honestly.
- Recap in a few bullets: slices landed, decisions made, and anything deferred - the natural first slice for next session.
- Offer to commit, but only if the user wants to.
