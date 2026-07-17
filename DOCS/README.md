# Documentation

Start here if you are new to this repository or coming back after a while.

## Current progress

Snapshot as of 2026-07-17 after the latest raw-conversion pass. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 7.72% | 1671 / 6034 (27.69%) |
| init | `[######------------------]` 25.18% | 297 / 538 (55.20%) |
| game | `[#-----------------------]` 5.48% | 1193 / 5314 (22.45%) |
| debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`;
"blocked" = only `j`/`jal` targets or `%lo` halves of shifted symbol
addresses differ, self-resolves as referenced functions/data get
matched):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 591 / 1671 (35.37%) | 825 | 255 |
| init | 76 / 297 (25.59%) | 160 | 61 |
| game | 494 / 1193 (41.41%) | 652 | 47 |
| debugger | 21 / 181 (11.60%) | 13 | 147 |

The debugger overlay's long-standing rodata displacement healed on
2026-07-16: its printf engine was identified as Plauger's Standard C
Library (the N64 SDK's libc) and rematched at exact retail sizes. Later
game-section layout fixes (`func_1504B0FC`, `func_1504BE2C`, and
`func_150721A4`) collapsed most address-drift blockers. The latest passes
then traded some byte-match cleanliness for +20 more game functions in the
current push, +10 debugger functions, and +65 init/libultra functions
converted from raw asm to C. Game raw conversion is now 136 functions short
of the 25% target.
Debugger raw conversion is now complete except `func_16003650`, a CP0/TLB
reader that uses `tlbr`/CP0 register instructions and is intentionally left
as raw assembly. The new C bodies are raw-progress placeholders, so the
byte-match table is expected to stay lower until those functions are
size-matched or padded back into retail layout. The latest init/libultra
push also replaced early-link OS/PI/SI/AI helpers, so many otherwise-good
rows are temporarily classified as address-drift blocked.

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
