# Documentation

Start here if you are new to this repository or coming back after a while.

## Current progress

Snapshot as of 2026-07-16 after the latest layout pass. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.57% | 1550 / 6034 (25.69%) |
| init | `[#####-------------------]` 20.16% | 232 / 538 (43.12%) |
| game | `[#-----------------------]` 4.95% | 1147 / 5314 (21.58%) |
| debugger | `[###############---------]` 63.33% | 171 / 182 (93.96%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`;
"blocked" = only `j`/`jal` targets or `%lo` halves of shifted symbol
addresses differ, self-resolves as referenced functions/data get
matched):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 1466 / 1550 (94.58%) | 50 | 34 |
| init | 227 / 232 (97.84%) | 4 | 1 |
| game | 1090 / 1147 (95.03%) | 46 | 11 |
| debugger | 149 / 171 (87.13%) | 0 | 22 |

The debugger overlay's long-standing rodata displacement healed on
2026-07-16: its printf engine was identified as Plauger's Standard C
Library (the N64 SDK's libc) and rematched at exact retail sizes. Later
game-section layout fixes (`func_1504B0FC`, `func_1504BE2C`, and
`func_150721A4`) collapsed most address-drift blockers, so only 50
C-converted rows remain blocked. The small dips in the conversion table
(1550 vs 1558 functions) are deliberate byte-verified `GLOBAL_ASM`
fallbacks with their verified C kept in comments. Every debugger overlay
*function* is now byte-exact or drift-blocked-free; the remaining debugger
rows are data content.

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
