# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for the
Nintendo 64.

This repository does not include any game assets or ROMs. You must provide
your own legally obtained copy of the game to build it.

## Current progress

Snapshot as of 2026-07-14. Functions converted from raw assembly to C
(`make -C conker progress NON_MATCHING=1`):

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.77% | 1553 / 7644 (20.32%) |
| init | `[#####-------------------]` 20.16% | 232 / 547 (42.41%) |
| game | `[#-----------------------]` 5.11% | 1151 / 6915 (16.64%) |
| debugger | `[#################-------]` 70.26% | 170 / 182 (93.41%) |

Of those C-converted functions, the share that already compiles to the
exact retail bytes (`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on callees | Still differ |
| --- | --- | --- | --- |
| total | 435 / 1553 (28.01%) | 145 | 973 |
| init | 223 / 232 (96.12%) | 4 | 5 |
| game | 197 / 1151 (17.12%) | 141 | 813 |
| debugger | 15 / 170 (8.82%) | 0 | 155 |

"Blocked on callees" functions only differ in `j`/`jal` target addresses
and will self-resolve as the functions they reference get matched. When
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
