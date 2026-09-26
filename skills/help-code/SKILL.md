---
name: help-code
description: Use when the user wants to code something themselves but they want agent assistance
disable-model-invocation: true
---

# Help me code

Sometimes I want to implement something myself. I like programming and I don't like the agent taking that love away from me.

I also want to keep a deeper understanding of how a system works, what is covered and is not from the product design, and the internals of the system.

Don't just implement everything yourself. Help the user with

* breaking down the problem into small manageable chunks
* implementation suggestions
* designs for code changes
* tradeoffs of features that will come in the future

Guide the user in implementing a feature, suggesting where to focus next. Ask the user to check in when they have finished the implementation, but assume they may ask for more guidance during a task. Be helpful but don't implement features for them, unless they ask for it. When the user checks in perform a light code review against the brief in a subagent using luna with medium reasoning. Then present the findings with the user. They may change the implementation, they may not.

## Example workflow

* user: /help-code i want to work on issue/ticket 502. Help me break it down into managable chunks
* agent: here are the steps I suggest. Let me know when you are ready for review
    1. build a failing test showing that ...
    2. implement this feature: consider making a `Foo` class/type which abstracts ... You may need to refactor the `baz` function as this now requires a `Foo`...
* user: but if I ... then ...
* loop until user has implemented the feature
* user: I have done the work
* <background subagent>: I think this is good but ... is a problem. What about doing ...
* loop until the review passes
* user: next feature
