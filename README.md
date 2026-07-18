# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for the
Nintendo 64.

This repository does not include any game assets or ROMs. You must provide
your own legally obtained copy of the game to build it.

## Current progress

Snapshot as of 2026-07-18 after the 60% total C milestone. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[###########-------------]` 43.81% | 3646 / 6033 (60.43%) |
| init | `[#######-----------------]` 28.24% | 327 / 538 (60.78%) |
| game | `[###########-------------]` 44.51% | 3138 / 5313 (59.06%) |
| debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 1584 / 3646 (43.44%) | 24 | 2038 |
| init | 236 / 327 (72.17%) | 4 | 87 |
| game | 1182 / 3138 (37.67%) | 20 | 1936 |
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
past 60%, while preserving the retail layout and adding one exact match.
The first matching pass over those generated slices recovered 40 small
retail functions exactly. The current layout-preservation pass then crossed
the 50% byte-exact milestone by retaining every compiled instruction and
relocation while restoring retail-relative function and object addresses.
Oversized non-matching functions remain executable through out-of-line bodies
and short trampolines, so they no longer displace later exact functions.
Debugger raw conversion is now complete except `func_16003650`, a CP0/TLB
reader that uses `tlbr`/CP0 register instructions and is intentionally left
as raw assembly. Generated-slice jump labels are restored by the object-padding
tool instead of a separately linked label object. Only 24 C functions remain
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
