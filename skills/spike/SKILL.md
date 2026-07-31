---
name: spike
description: Spike a technical unknown in a standalone throwaway project. Use when the user wants to find out whether a real library, API, or service works or behaves the way they assume, by trying it in isolation instead of wiring it into the real codebase. Triggers on "spike", "spin up a scratch project to test X", "will this library do what I need", "how does this framework behave", "can I get these two things talking".
---

# Spike

A spike is a **standalone throwaway project that answers a question about the outside world**. You keep the finding; you bin the code.

The question is always the same shape: *is my assumption about some external thing true?* Does this library support what I need. Does this API behave the way the docs imply. Can these two services actually talk. The only way to know is to make **contact with reality** - run the real thing in isolation and watch what it does.

This is the sibling of a `prototype`, split by what's uncertain. A prototype answers a question about *your own* logic, state model, or UI, and lives inside the host project so the good part lifts back out. A spike answers a question about *someone else's* code or service, lives in a scratch project of its own, and lifts nothing back - only the finding survives. If the uncertainty is your own design, that's a prototype, not a spike.

## What makes it a spike

1. **Isolated from the host project.** A fresh scratch directory with its own dependency manifest, never a folder inside the real source tree. Spike dependencies must never touch the real project's manifest - avoiding exactly that pollution is half the reason the spike is separate. Put it in a scratch dir (the session scratchpad, `/tmp`, or a `spikes/` dir), well away from the code it informs.
2. **Make contact with the real unknown.** The whole point is reality, so the thing under question must be real: the real library, the real API endpoint, the real service. Stub the unknown and the spike proves nothing. Everything *around* it can be faked freely - hardcode inputs, paste a token inline, skip anything that isn't the question.
3. **Breadth, not depth.** Trace the *whole scope* of the problem end to end - every stage the real thing has to pass through - but touch each stage as shallowly as it takes to move on. The failure a spike catches is "these pieces don't fit together", and you only see it by spanning the whole path, not by building any one piece well. A robust implementation of the first stage teaches you less than a flimsy pass through all of them.
4. **Shallow everywhere.** No structure, no tests, no error handling, no retries, no config beyond what makes the real thing run. Happy path only - hardcode inputs, assume every call succeeds. Robustness is depth, and depth is what you are deliberately skipping.
5. **The finding is the deliverable, the code is disposable.** What survives is written down: the answer, and the evidence for it. The project exists only to produce that.

## Process

### 1. State the question

Write one falsifiable sentence: what assumption about the outside world are we testing? "Does `<library>` stream partial responses?" "Does the `<service>` webhook retry on a 500?" Vague questions ("check out this library") produce spikes that wander and never resolve. If you can't say what would make the answer yes or no, sharpen it before writing any code.

### 2. Create the isolated project

Spin up a scratch directory outside the real source tree, with its own minimal manifest, and add the real dependency or credentials the question needs. Use the ecosystem's lightest path to a runnable file - `npm init -y`, `uv init`, `cargo new`, a single `go` file, whatever gets you to "I can run code" fastest.

### 3. Walk the whole path

Write throwaway code that touches every stage the real problem has to pass through, end to end, and no more than that at each stage. Hardcode inputs, assume success, skip everything that isn't part of the path. The goal is to reach the far end with all the pieces connected - because "do these actually fit together" is the question a spike exists to answer, and you can only see it once the whole path runs.

### 4. Run it and read reality

Run the one command and read what actually happened - the output, the error, the timing, the shape of the response. Capture it verbatim; the surprising detail in the raw output is usually the finding. A spike's authority is that it *ran*, so never substitute what the docs claim for what the run showed.

### 5. Widen until the scope is covered

Once the happy path runs end to end, fill in any stage you faked or skipped, until every part of the problem's scope has actually been exercised at least once. The gap you fake over is exactly where the nasty surprise hides. Stay shallow while you widen - the aim is to have *touched* the whole scope, not to harden any of it. If the user is around, hand them the run command and let them drive; the interesting moments are "wait, it did *what*?".

### 6. Capture the finding and bin the project

Write the answer and its evidence where the real work will see it - the implementation issue, a decision note, or the commit that acts on it. Then dispose of the scratch project, but preserve it as a **primary source** so the finding stays reproducible: push it to a throwaway branch or archive the scratch dir, and leave a pointer to it beside the finding. The real codebase keeps only the decision the spike settled.

## Anti-patterns

- **Stubbing the unknown.** Mocking the very library or service you're spiking answers nothing. The unknown must be real; everything else can be fake.
- **Going deep instead of wide.** Building one stage robustly - error handling, retries, clean abstractions - while the rest of the path is untouched. That is a half-built product, not a spike. Cover the whole scope shallowly first; depth is what you skip.
- **Letting the spike grow.** Adding structure, config, or "while I'm here" features turns a spike into a half-built project you get attached to. When it has answered its question, it is done.
- **Polluting the host project.** Never add spike dependencies to the real manifest or spike files to the real tree. Isolation is the point.
- **Promoting spike code to production.** It was written to prove a point, with no tests and no error handling. Rewrite the real thing from the finding; don't ship the scratch code.
- **Answering from the docs.** If you didn't run it, it's not a spike - it's a guess. The value is contact with reality.
