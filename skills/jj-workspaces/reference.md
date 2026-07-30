# dojjo reference

Reached from [`SKILL.md`](SKILL.md) to install `djo`, automate the workspace lifecycle with hooks, or tune merge and copy behaviour.

## Install

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/tjarvstrand/dojjo/main/install.sh | sh

# or via the Dart package manager
dart pub global activate dojjo
```

On Windows, download `djo-windows-x64.exe` from the latest release, rename it to `djo.exe`, and add it to PATH.

## Config files

`djo` reads TOML, later files overriding earlier ones:

1. `~/.config/worktrunk/config.toml`
2. `.config/wt.toml`
3. `~/.config/dojjo/config.toml`
4. `dojjo.toml`
5. `dojjo.local.toml`

Put repo-wide settings in `dojjo.toml` (committed) and personal overrides in `dojjo.local.toml` (git-ignored).

## Hooks

Hooks fire around each lifecycle stage: `pre-start`/`post-start`, `pre-switch`/`post-switch`, `pre-merge`/`post-merge`, `pre-remove`/`post-remove`. Pre-hooks block and run sequentially; post-hooks run backgrounded.

```toml
[hooks]
# single command
post-start = "npm install"

[hooks.pre-merge]
# map form: named steps run in parallel
test = "cargo test"
lint = "cargo clippy"
```

List-of-maps form is a pipeline: steps run in order, commands within a step run in parallel.

```toml
[hooks]
post-start = [
    { install = "npm install" },
    { build = "npm run build", lint = "npm run lint" },
]
```

To hydrate untracked files automatically on every new workspace (step 2), invoke `copy-ignored` from a `post-start` hook so it runs without a manual command:

```toml
[hooks]
post-start = "djo copy-ignored --from default"
```

## copy-ignored

`djo copy-ignored --from <workspace>` copies untracked, git-ignored files (dependencies, build caches) from the source workspace. On macOS it uses APFS clonefile for instant copy-on-write.

- `--force` — overwrite existing files (default: skip existing)
- `--dry-run` — preview without copying

It respects a `.worktreeinclude` whitelist and an exclude list:

```toml
[step.copy-ignored]
exclude = [".cache/", ".turbo/"]
```

## Merge behaviour

`djo merge <target>` runs, in order: squash, rebase onto target, move bookmark, forget workspace, delete the workspace directory, and push (when `--push` or `merge.push = true`). Each step is configurable:

```toml
[merge]
squash = true
rebase = true
remove = true
verify = true
push = false
```

If a merge fails partway, `jj op undo` reverts it.
