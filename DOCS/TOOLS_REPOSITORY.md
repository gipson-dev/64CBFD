# Decomp Tools Repository

The decomp tool set is owned by
[gipson-dev/64CBFD-Tools](https://github.com/gipson-dev/64CBFD-Tools).
`64CBFD/tools` is a pinned Git submodule of that repository, not another copy
of the tool sources tracked by this repository. The standalone workspace
checkout is the sibling `64CBFD Tools` folder.

## Existing Checkouts

Commit or otherwise preserve any local tool edits before pulling the split.
Then, from the decomp root:

```sh
git pull --ff-only
bash scripts/bootstrap-tools.sh
make tools-check
```

Fresh clones use:

```sh
git clone --recursive https://github.com/gipson-dev/64CBFD.git
```

The bootstrap initializes the new tools parent without deleting or moving the
legacy nested dependency directories, Git metadata, or local caches. It uses
a normal checkout, refuses conflicting files and dirty tools/dependencies,
and then updates recursively to the recorded pin. Do not delete a non-empty
`tools/` directory or force-checkout over uncommitted work. A fresh recursive
clone remains a fallback; keep the old checkout and its private ROM/build
inputs intact until the new one is verified. After the initial migration,
ordinary `git submodule sync --recursive` and
`git submodule update --init --recursive` are sufficient.

On Windows-mounted paths under WSL, the bootstrap uses `git.exe` when available
to retain Windows Git's line-ending rules. On native Linux it uses Linux Git.
This avoids falsely treating CRLF checkouts of upstream dependencies as dirty;
it does not normalize or rewrite those files.

## Paths And Ownership

Build commands, `python3 -m tools...` imports, Splat extension paths, and local
documentation commands are unchanged. The game source, IDO configuration,
retail layout/word-guard manifests, private inputs, and working notes remain
in the decomp repository. Seven upstream tool pins are now nested inside the
tools repository. Use recorded pins, not `git submodule update --remote`.

Matching experiments and most tests must run from a prepared decomp checkout;
their source-relative `conker/` inputs are not available in the standalone
tools root. The standalone repository supports the ROM-free wrapper, matcher,
and guarded-padding checks described in its
[README](https://github.com/gipson-dev/64CBFD-Tools/blob/master/README.md).

GitHub source links to moved tool files point to the tools repository. Local
shell commands keep using `tools/`. Historical tool-file revisions remain
accessible in the decomp history before the split.

## Contribution Workflow

Commit tool changes in the tools repository and game/documentation changes
here. Publish a tools commit before publishing a decomp commit that points to
it. See the tools
[contribution guide](https://github.com/gipson-dev/64CBFD-Tools/blob/master/CONTRIBUTING.md)
for testing changes from the standalone and mounted checkouts.

Existing game-build workflows already check out recursively. The Docker
publication workflow now also checks out recursively because its Dockerfile
copies `tools/n64splat/requirements.txt`. A new read-only, ROM-free workflow
checks the consumer's recorded tools pin without private game secrets.

As verified through GitHub's repository API on 2026-10-08, Actions are disabled
on `64CBFD` (`enabled: false`). That existing setting was preserved, so the
consumer workflow is installed but has not run on GitHub for this split.
The independent tools repository has Actions enabled and its checks pass.

## Split Checkpoint

The 2026-10-08 import started at decomp commit
`f0d7300178dc0a4a32fbb3e4e19810ff98879cb4`. All 480 source file blobs and
seven dependency revisions were preserved. The two project MIPS shell
wrappers gained executable Git modes for fresh Linux checkouts; their bytes
did not change. New repository metadata, contribution guidance, issue/PR
templates, and a small setup test are separate additions.

No game functions, compiler profiles, retail manifests, ROMs, local build
receipts, sibling PC-port sources, or frozen Release binaries were moved.
The game's conversion and matching totals are unchanged by this split.

## Verification

- Standalone checkout: wrapper smoke test and 14 setup/matcher/padder tests
  pass with no ROM. Seven recursive upstream checkouts resolve at their
  original revisions.
- A fresh recursive consumer checkout and an upgrade from the pre-split
  `f0d73001` checkout each pass the bootstrap, wrapper smoke test, and all
  14 ROM-free checks, with every module clean. The upgrade preserves an
  ignored private-cache fixture and the existing seven nested worktrees.
- A dirty-checkout control refuses the bootstrap without changing the local
  fixture bytes or tools HEAD. Initial Windows-cloned/WSL qualification
  exposed CRLF-only false dirty reports in five upstream repositories;
  selecting Windows Git for Windows-mounted paths resolves those reports
  without rewriting any dependency file.
- Existing decomp: `make tools-check` and 28 setup/matcher/padder/linker-layout
  tests pass with no skips. The layout tests use this prepared checkout's
  existing local linker script; they are not part of the fresh-clone CI claim.
- Latest effect-registration qualification: eight tests pass in 36.002s,
  including actual native32 execution, guest/callback/fault cases, owner
  preservation, real padding, and rebased links.
- `make -C conker --jobs=2 build/conker.us.elf` succeeds with its existing
  duplicate-recipe warnings; the target remains up to date. The ELF SHA-256
  remains `4ce58b68db7852bdfafc665968ef05475e63c9d009a39593bd3bfb0f28374f69`.
  The word-guard manifest SHA-256 remains
  `9ea7979500827f798bf12d10158f02b42b8952470d6229551a7f265bed5b2949`.
- 448 tool-source links across 131 tracked Markdown documents were updated
  and validated against the new tools index. No local command paths changed.
- The initial import is `0ca93be1e65c2e3289167a8e51bb8ef95ef9651a`; the
  recorded tools pin is now `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, adding
  bootstrap guidance only. Both are published. The latest
  [ROM-free GitHub Actions run](https://github.com/gipson-dev/64CBFD-Tools/actions/runs/37770089509)
  passed. This is not a full ROM rebuild or gameplay qualification.
