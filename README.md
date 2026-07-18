# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for the
Nintendo 64.

This repository does not include any game assets or ROMs. You must provide
your own legally obtained copy of the game to build it.

## Current progress

Snapshot as of 2026-07-18 after the 99% total C and 50% init byte-exact milestones. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[########################]` 98.34% | 5973 / 6033 (99.01%) |
| init | `[######################--]` 90.79% | 508 / 538 (94.42%) |
| game | `[########################]` 98.93% | 5284 / 5313 (99.45%) |
| debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 1701 / 5973 (28.48%) | 27 | 4245 |
| init | 255 / 508 (50.20%) | 7 | 246 |
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
An init-focused pass then matched 22 more SDK and game functions by restoring
their retail IDO optimization profiles, native MIPS III 64-bit operations,
and original register-qualified source shapes. Init byte-exact progress is now
over 50% without changing the game, debugger, raw-conversion, or blocker totals.
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

"Blocked on address drift" functions only differ in `j`/`jal` targets or
`%lo` halves of shifted symbol addresses and will self-resolve as the
functions/data they reference get matched. When
regenerating, update these tables together with the copies in
[DOCS/README.md](DOCS/README.md) and [DOCS/PROJECT.md](DOCS/PROJECT.md).

## Documentation

Full documentation lives in [DOCS/](DOCS/README.md):

- [Project overview](DOCS/PROJECT.md) - repository layout and build
  instructions (Docker, Linux, or WSL).
- [Code sub-project](DOCS/CODE_SUBPROJECT.md) - how the `conker/` code
  build fits into the full ROM build.
- [Asset formats](DOCS/ASSET_FORMATS.md) - compression, archive
  containers, and model/texture/audio payloads.
- [Working notes](DOCS/WORKING_NOTES.md) - live log of in-progress work.
- [PC port roadmap](DOCS/PC_PORT_ROADMAP.md) - long-term plan for a native
  PC port.
- [Update log](DOCS/UPDATE_LOG.md) - documentation and workflow changes.
