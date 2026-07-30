---
name: jj-workspaces
description: Use a jj workspace via the `djo` (dojjo) tool instead of a git worktree for an isolated parallel environment in a jj repo. Use when the user wants to work on parallel tasks or branches in one repo, wants an isolated checkout that leaves the main working copy untouched, or reaches for a git worktree — and when another skill needs a throwaway parallel environment.
---

For a parallel environment in a jj repo, reach for a jj **workspace**, not a git worktree. A workspace is a second working copy backed by the same repo, so parallel tasks never fight over one checkout. `djo` (the dojjo tool) manages the workspace lifecycle — create, hydrate, merge, clean up — and runs hooks at each stage.

Requires a jj repo and the `djo` binary on PATH; see [`reference.md`](reference.md) to install it or set up hooks.

Run every step from inside the repo.

## 1. Create the workspace

```
djo switch <name>
```

Creates a jj workspace plus a bookmark `<name>`, in a sibling directory `../<name>` by default. `cd` into that directory — `djo switch` cannot change your shell's directory for you.

Done when `djo list` shows `<name>` and your shell is in its directory.

## 2. Hydrate untracked files from the original

A fresh workspace holds only jj-tracked files. Untracked, git-ignored files — `node_modules`, `.env`, build caches — are absent, so the toolchain fails until you bring them over.

```
djo copy-ignored --from default
```

`default` is jj's original workspace; name a different source if you branched from one. Add `--dry-run` to preview, `--force` to overwrite. A `post-start` hook can do this automatically (see [`reference.md`](reference.md)).

Done when the build and test commands run without missing-dependency or missing-config errors.

## 3. Work in the workspace

Edit and commit with jj as normal. The original working copy and any other workspaces are untouched.

## 4. Merge back

```
djo merge <target>
```

Squashes the workspace's changes, rebases onto `<target>`, moves the bookmark, and removes the workspace directory. If it fails partway, run `jj op undo` to revert, then retry. Tune squash/rebase/push behaviour in config (see [`reference.md`](reference.md)).

Done when `<target>` contains the changes and the workspace directory is gone.

## 5. Clean up

```
djo prune
```

Removes every workspace already merged into the default branch. To drop one workspace you are abandoning unmerged, use `djo remove <name>`.

Done when `djo list` shows only the workspaces you still want.
