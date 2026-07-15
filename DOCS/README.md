# Documentation

Start here if you are new to this repository or coming back after a while.

## Current progress

Snapshot as of 2026-07-15. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.81% | 1558 / 6034 (25.82%) |
| init | `[#####-------------------]` 20.16% | 232 / 538 (43.12%) |
| game | `[#-----------------------]` 5.11% | 1153 / 5314 (21.70%) |
| debugger | `[##################------]` 74.36% | 173 / 182 (95.05%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`;
"blocked" = only `j`/`jal` targets differ, self-resolves as referenced
functions get matched):

| Section | Byte-exact | Blocked on callees | Still differ |
| --- | --- | --- | --- |
| total | 445 / 1558 (28.56%) | 144 | 969 |
| init | 223 / 232 (96.12%) | 4 | 5 |
| game | 197 / 1153 (17.09%) | 140 | 816 |
| debugger | 25 / 173 (14.45%) | 0 | 148 |

The debugger byte-exact count is temporarily depressed: four
`debugger_257350.c` functions are mid-rematch at non-retail sizes, which
displaces the overlay's rodata, so every already-code-exact debugger
function that references that data shows a few phantom `%lo` diffs and
counts as "still differ". It snaps back once those four reach retail
size (see WORKING_NOTES).

When regenerating, update both tables together with the copies in the
[root README](../README.md) and [Project overview](PROJECT.md).

## Reading order

1. [Project overview](PROJECT.md) - what this repo is, how it is laid out, and how to build it.
2. [Code sub-project](CODE_SUBPROJECT.md) - how the `conker/` code build fits into the full ROM build.
3. [Compressed config sections](CONFIG.md) - how the `config/` YAML files are used for compressed ROM chunks.
4. [IDO 5.3 recomp toolchain](IDO_RECOMP.md) - where the bundled compiler files come from.
5. [Asset formats](ASSET_FORMATS.md) - compression, archive containers, and model/texture/sound payloads.
6. [Working notes](WORKING_NOTES.md) - live log of in-progress work, kept so a crashed session can be resumed.
7. [PC port roadmap](PC_PORT_ROADMAP.md) - phased plan for a keyboard/mouse/controller PC port and a later modern-graphics update.
8. [Update log](UPDATE_LOG.md) - repository documentation, workflow, and maintenance changes.

## Quick notes

- You need your own legally obtained ROM. This repository does not include one.
- Build and extraction commands are expected to run from Linux, WSL, or Docker.
- The `tools/` directories are submodules and keep their own upstream documentation.
