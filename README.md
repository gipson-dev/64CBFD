# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for the
Nintendo 64.

This repository does not include any game assets or ROMs. You must provide
your own legally obtained copy of the game to build it.

## Current progress

Snapshot as of 2026-07-16. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.74% | 1555 / 6034 (25.77%) |
| init | `[#####-------------------]` 20.16% | 232 / 538 (43.12%) |
| game | `[#-----------------------]` 5.11% | 1151 / 5314 (21.66%) |
| debugger | `[################--------]` 66.46% | 172 / 182 (94.51%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 895 / 1555 (57.56%) | 616 | 44 |
| init | 223 / 232 (96.12%) | 8 | 1 |
| game | 525 / 1151 (45.61%) | 608 | 18 |
| debugger | 147 / 172 (85.47%) | 0 | 25 |

The debugger overlay's long-standing rodata displacement healed on
2026-07-16: its printf engine was identified as Plauger's Standard C
Library (the N64 SDK's libc) and rematched at exact retail sizes, which
snapped ~120 previously "still differ" rows back to byte-exact (see
WORKING_NOTES). The small dips in the conversion table (1555 vs 1558
functions) are `func_16001BB4` and the two hand-written PRNG functions
returning to `GLOBAL_ASM` at retail bytes with their verified C kept in
comments.

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
