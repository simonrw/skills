---
name: test-audit
description: Use when considering which tests to write, or when the user asks to "audit my test suite" or "cleanup" my test suite
---

# Writing good tests

Tests should be robust to small implementation detail changes. They should focus on testing the public API or "seam" of a module or component within a codebase.

We should not write endless detailed unit tests with brittle assertions that test in great detail small implementation details that do not matter. I would prefer to have fewer tests with wider coverage than lots of detailed unit tests that are fragile.

## Mocking

Aim for a test suite without mocks if possible. Prefer to integrate two components when testing how they integrate, over mocking the outside world.

Reaching for a mock is an indication that we are not testing the right thing. If you feel a mock object is a better approach, present your argument to the user and let them decide.

## Methods or functions to test

Only test "public" methods and functions, that are called from other modules or packages. Do not test implementation details or helper methods - their behaviour and correctness should be proved from tests that exercise them from the public API of the system.

### Pythoh

* Don't test methods or functions that start with an underscore "_"

### Rust

* Don't test methods that are not marked as `pub`, and prefer integration tests that do not have access to crate/module internals.

## Coverage

We do not need 100% test coverage to gain confidence. Be pragmatic. We don't need every edge case covered, focus on the happy path to start with and discuss with the user additional code paths that should have tests. Always consider your design from the perspective of the user or an outside consumer and present how they might invoke a particular code path that needs testing.

## Assertions

Aim for one assertion per test. This makes it clearer when a test fails what the problem is.

## Examples

Given the Python code

```python
class Foo:
    def __init__(self, bar: Bar | None = None):
        self._bar = bar or Bar()

    def do_something(self) -> int:
        return self._implementation_details()

    def _implementation_details(self) -> int:
        return self._bar.value() * 100
```

* Do not test `Foo._implementation_details`
* Aim to pass a real `Bar` instance into `Foo` rather than a mock object
