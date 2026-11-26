---
name: jj
description: Version control with jj (Jujutsu). Use before committing, rebasing, pushing, or creating bookmarks, workspaces or PRs in a repo where `jj root` succeeds and git shows a detached HEAD.
---

# jj

## Detection

Run `jj root >/dev/null 2>&1 && ! git symbolic-ref -q HEAD >/dev/null`. If it succeeds, the repo is jj-managed and this skill applies. If it fails, the user is working with git on a branch: use git as normal and stop here.

## Tooling

Make every repository change with jj. Read-only git (`git log`, `git blame`, `git show`) and `gh` are fine. Mutating git commands (`commit`, `checkout`, `reset`, `rebase`, `stash`, `push`, `worktree`) are off limits because they bypass jj's view of the repo.

Use raw jj commands rather than the user's aliases, except `jj push` (below). Every command must run non-interactively: pass `-m` to `commit`/`describe`, split with paths (`jj split <paths> -m ...`), and resolve conflicts by editing files instead of `jj resolve`.

## Workflow

- **Commit**: edit files in `@`, then `jj commit -m "..."` at each coherent checkpoint. The finished change becomes `@-` and `@` is a fresh empty change. Match the message style of `jj log`. Bookmarks advance automatically via a hook.
- **Rewrite**: squash, split, rebase, abandon and describe unpushed changes freely. Before rewriting a change in `::remote_bookmarks()`, ask, since it forces a push.
- **Catch up**: `jj git fetch`, then `jj rebase -b @ -d 'trunk()'`. Rebase, never merge trunk in.
- **Conflicts**: edit the git-style conflict markers in the files, then confirm `jj log -r 'conflicts()'` is empty.
- **Bookmarks**: the user creates them. When opening a PR with no bookmark on the work, create a short kebab-case one: `jj bookmark create fix-thing -r @-`.
- **Push**: only when the user has asked for a push in this task. Use `jj push -b <bookmark>`, which runs the repo's hooks first. On hook failure, fix the cause, commit again and push again.
- **Isolated checkout**: `jj workspace add <path>`.
- **Recovery**: `jj op log` to find the state, `jj undo` or `jj op restore <id>` to return to it.
