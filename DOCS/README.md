# Documentation

Start here if you are new to this repository or coming back after a while.

## Current progress

Snapshot as of 2026-07-18 after the 99% total C milestone. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[########################]` 98.34% | 5973 / 6033 (99.01%) |
| init | `[######################--]` 90.79% | 508 / 538 (94.42%) |
| game | `[########################]` 98.93% | 5284 / 5313 (99.45%) |
| debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`;
"blocked" = only `j`/`jal` targets or `%lo` halves of shifted symbol
addresses differ, self-resolves as referenced functions/data get
matched):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 1679 / 5973 (28.11%) | 27 | 4267 |
| init | 233 / 508 (45.87%) | 7 | 268 |
| game | 1280 / 5284 (24.22%) | 20 | 3984 |
| debugger | 166 / 181 (91.71%) | 0 | 15 |

The debugger overlay's long-standing rodata displacement healed on
2026-07-16: its printf engine was identified as Plauger's Standard C
Library (the N64 SDK's libc) and rematched at exact retail sizes. Later
game-section layout fixes (`func_1504B0FC`, `func_1504BE2C`, and
`func_150721A4`) collapsed most address-drift blockers. The latest game
decomp push crossed the 25% game raw-conversion target, follow-up
init passes pushed total raw conversion over 30%, and generated game-slice C
placeholders pushed total raw conversion over 50%. A further 25 high-yield
game slices then moved 613 functions into generated C and carried the total
past 60%. The next 44 text-only slices moved another 612 tracked functions
and carried both total and game conversion past 70%, while preserving the
retail layout and adding another exact match. A further 82 safe text-only
slices moved 588 tracked functions and carried total conversion past 80% and
game conversion past 81%, without losing any existing exact matches. The 90%
pass then moved 385 functions through 167 standalone slices and replaced 246
validated `GLOBAL_ASM` groups across eight large mixed C sources. Signature
declarations needed for those legacy implicit calls perturb one previously
exact caller; blockers remain unchanged.
The 99% pass then replaced 416 validated `GLOBAL_ASM` groups across 105
mixed sources and moved 80 tracked libultra functions through typed generated
standalone slices. Signature discovery now handles function pointers, local
`static` declarations, directly included source headers, macro-shadowed
function names, and legacy calls with inconsistent arity. The 60-function raw
remainder is deliberately constrained to handwritten TLB code, embedded data
labels or four-byte slots, six mixed code/data functions, two static audio
routines, and the debugger CP0 reader.
A dedicated byte-matching pass then recovered 35 small typed callbacks,
constant-return handlers, accessors, and state setters, raising byte-exact
progress to 27.06% without changing the matcher or raw-conversion totals.
A second compact-function pass matched 63 more callbacks, scalar helpers,
field initializers, accessors, and thin wrappers, carrying byte-exact progress
past 28% while preserving the same raw-conversion and blocker counts.
The first matching pass over those generated slices recovered 40 small
retail functions exactly. The current layout-preservation pass then crossed
the 50% byte-exact milestone by retaining every compiled instruction and
relocation while restoring retail-relative function and object addresses.
Oversized non-matching functions remain executable through out-of-line bodies
and short trampolines, so they no longer displace later exact functions.
Debugger raw conversion is now complete except `func_16003650`, a CP0/TLB
reader that uses `tlbr`/CP0 register instructions and is intentionally left
as raw assembly. Generated-slice jump labels are restored by the object-padding
tool instead of a separately linked label object. Only 27 C functions remain
classified as address-drift blocked.
The ROM mapping helper now reads code-section starts from `conker.<version>.yaml`,
finds `symbol_addrs.<version>.txt` even when using a temporary progress CSV,
and resolves `D_XXXXXXXX` data labels from their name-implied retail VRAM.

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
