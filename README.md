# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for the
Nintendo 64.

This repository does not include any game assets or ROMs. You must provide
your own legally obtained copy of the game to build it.

## Current progress

Snapshot as of 2026-07-17 after the ROM-mapping cleanup. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 8.23% | 1700 / 6034 (28.17%) |
| init | `[######------------------]` 25.18% | 297 / 538 (55.20%) |
| game | `[#-----------------------]` 6.02% | 1222 / 5314 (23.00%) |
| debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 693 / 1700 (40.76%) | 826 | 181 |
| init | 76 / 297 (25.59%) | 160 | 61 |
| game | 495 / 1222 (40.51%) | 653 | 74 |
| debugger | 122 / 181 (67.40%) | 13 | 46 |

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
