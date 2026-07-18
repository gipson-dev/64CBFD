# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for the
Nintendo 64.

This repository does not include any game assets or ROMs. You must provide
your own legally obtained copy of the game to build it.

## Current progress

Snapshot as of 2026-07-17 after the 50% total C milestone. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[###---------------------]` 12.71% | 3033 / 6033 (50.27%) |
| init | `[#######-----------------]` 27.89% | 327 / 538 (60.78%) |
| game | `[##----------------------]` 10.06% | 2525 / 5313 (47.52%) |
| debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 740 / 3033 (24.40%) | 836 | 1457 |
| init | 76 / 327 (23.24%) | 164 | 87 |
| game | 542 / 2525 (21.47%) | 659 | 1324 |
| debugger | 122 / 181 (67.40%) | 13 | 46 |

The debugger overlay's long-standing rodata displacement healed on
2026-07-16: its printf engine was identified as Plauger's Standard C
Library (the N64 SDK's libc) and rematched at exact retail sizes. Later
game-section layout fixes (`func_1504B0FC`, `func_1504BE2C`, and
`func_150721A4`) collapsed most address-drift blockers. The latest game
decomp push crossed the 25% game raw-conversion target, follow-up
init passes pushed total raw conversion over 30%, and generated game-slice C
placeholders pushed total raw conversion over 50%.
The first matching pass over those generated slices recovered 40 small
retail functions exactly, including no-op callbacks, constant-return helpers,
global/field stores, flag updates, and short getters.
Debugger raw conversion is now complete except `func_16003650`, a CP0/TLB
reader that uses `tlbr`/CP0 register instructions and is intentionally left
as raw assembly. The new C bodies are raw-progress placeholders, so the
byte-match table is expected to stay lower until those functions are
size-matched or padded back into retail layout. The latest init/libultra
push also replaced early-link OS/PI/SI/AI helpers, so many otherwise-good
rows are temporarily classified as address-drift blocked.
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
