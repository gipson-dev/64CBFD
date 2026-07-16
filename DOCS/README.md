# Documentation

Start here if you are new to this repository or coming back after a while.

## Current progress

Snapshot as of 2026-07-16 (end of day). Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.71% | 1554 / 6034 (25.75%) |
| init | `[#####-------------------]` 20.16% | 232 / 538 (43.12%) |
| game | `[#-----------------------]` 5.11% | 1151 / 5314 (21.66%) |
| debugger | `[###############---------]` 63.33% | 171 / 182 (93.96%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`;
"blocked" = only `j`/`jal` targets or `%lo` halves of shifted symbol
addresses differ, self-resolves as referenced functions/data get
matched):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 897 / 1554 (57.72%) | 616 | 41 |
| init | 223 / 232 (96.12%) | 8 | 1 |
| game | 525 / 1151 (45.61%) | 608 | 18 |
| debugger | 149 / 171 (87.13%) | 0 | 22 |

The debugger overlay's long-standing rodata displacement healed on
2026-07-16: its printf engine was identified as Plauger's Standard C
Library (the N64 SDK's libc) and rematched at exact retail sizes, which
snapped ~120 previously "still differ" rows back to byte-exact (see
WORKING_NOTES). The small dips in the conversion table (1554 vs 1558
functions) are `func_16001BB4`, `func_16001044`, and the two hand-written
PRNG functions returning to `GLOBAL_ASM` at retail bytes with their
verified C kept in comments. Every debugger overlay *function* is now
byte-exact or drift-blocked-free; the remaining debugger rows are data
content.

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
