# Update Log

This log tracks repository-facing documentation, workflow, and project maintenance updates.

For code-level progress, run:

```sh
make -C conker progress
```

## 2026-07-17

### Tool reference triage

- Recorded `n64img` as the preferred N64 image-format reference through the
  existing n64splat dependency path (`tools/n64splat/requirements.txt` already
  requires it), avoiding a redundant standalone submodule.
- Added `N64-IPL` as a reference-only upstream for boot/IPL/header/checksum
  context.
- Left `mips-gcc-2.7.2` out of the active toolchain for now; it is useful if a
  KMC/GCC-compiled island is identified, but current matching work is still
  IDO 5.3 based.
- Updated active helper submodules after checking upstream HEADs:
  `tools/asm-differ` to `fdf9c6c`, `tools/asm-processor` to `b29ff12`, and
  the parent repo's `tools/mips_to_c` pointer to the already-checked-out
  `m2c` upstream `554de36`.

## 2026-07-14

### ROM library, EU pipeline, and censorship analysis

- All four target versions (`us`, `eu`, `debug`, `ects`) now have
  hash-verified baseroms available locally for the first time. The EU ROM
  arrived as a byte-swapped `.n64`; converted to big-endian and verified
  against `conker.eu.sha1`. (The local ROM store was reorganized mid-way and
  temporarily lost the us/ects copies; the recovery, including hash
  identification of every file in the store, is logged in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).)
- Modernized `conker.eu.yaml`/`game.eu.rzip.yaml` (and `conker/conker.eu.yaml`)
  to current splat format with version-separated output paths
  (`asm_eu`/`assets_eu`/`src_eu`), so `make extract VERSION=eu` runs clean and
  the decompressed EU code image verifies against `conker/conker.eu.sha1`.
  EU disassembly (5,759 functions) now extractable as a third matched-code
  reference alongside the `debug_proto`/`ects_proto` trees.
  `conker.debug.yaml`/`conker.ects.yaml` still need the same two-line fix.
- Analyzed the "Uncensored" US romhack as a differential probe for asset
  formats: it replaces exactly 15 of 50 `assets06` files and 23 of 453
  `assets16` files strictly in place (offset tables byte-identical). This
  confirms `assets16` as the dialogue-audio MP3 bank and pins down which
  `assets06` files carry per-dialogue-line data. A Spanish translation hack
  independently corroborates this (it rewrites `assets06` far beyond the
  censored lines - subtitle text lives there). Findings folded into
  [`DOCS/ASSET_FORMATS.md`](ASSET_FORMATS.md).

### Windows/WSL build environment for this checkout

- Set up and documented building directly from this Windows checkout through
  WSL (Debian distro, project venv, `binutils-mips-linux-gnu`; the bundled
  IDO recomp binaries run fine from `/mnt/c`). Exact steps and the
  incremental rebuild/verify loop are in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).
- The CRLF/symlink checkout corruption documented below recurred (suspected
  OneDrive interaction) and was re-fixed; diagnosis shortcut now documented:
  splat failing with `could not load segment type 'rzip'` means
  `tools/splat_ext/rareunzip.py` (a git symlink) got checked out as a text
  stub again.

### Byte-matching progress tooling

- Added `tools/match_progress.py` and a `make -C conker match-progress`
  target (add `LIST=1` for a per-function listing): for every C-converted
  function in `progress.csv`, it compares the linked ELF's disassembly
  (keyed by function symbol, so immune to the known init-section layout
  drift) against ground-truth bytes from the pristine `conker.us.bin`, and
  classifies each as byte-exact, blocked-on-callees (only `j`/`jal` targets
  differ), or still differing. This productizes the session's scratchpad
  verification method. First run: **379 / 1553 C functions byte-exact
  (24.40%)** - init 201/232, game 167/1151, debugger 11/170 - now published
  as a second snapshot table in the root `README.md`,
  [`DOCS/README.md`](README.md), and [`DOCS/PROJECT.md`](PROJECT.md).

### Function matching (continued)

- Resolved 6 more of the remaining ECTS-ported non-matching functions:
  5 now byte-exact (`func_16001B00`, `func_15060BA4`, `func_1506196C`,
  `func_150AED9C`, `func_15142A5C`), 1 logically complete pending callees
  (`func_1504CA60`). 26 remain. Two stubborn functions are documented
  non-matching with in-source comments (`func_1514143C`, `func_1507A3E8`).
- Wrote up six reusable IDO/cfe codegen idioms (register-class rules for
  named locals vs temps, `u8` field-update codegen, branch-vs-`slt` return
  forms, operand evaluation order, mips_to_c artifact locals, pointer
  folding) in [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md) - read these
  before brute-forcing rewrites on the rest.

### Build environment and decomp progress

- Fixed a broken local build environment (pre-existing, not caused by this
  session): incorrect `core.symlinks`/`core.autocrlf` git config had left
  ~450 tracked files checked out with CRLF line endings and broken symlinks,
  which silently broke the IDO compiler. Fixed locally; see
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md) for the exact recovery steps
  if this recurs in a fresh clone or devcontainer.
- Fixed two `tools/n64splat` submodule version-compatibility bugs in this
  project's own extension code/config (`tools/splat_ext/rzip.py`,
  `conker/conker.us.yaml`, new `conker/include/asm_processor_prelude.inc`)
  that were blocking `make extract` and the C compile entirely.
- Ported 56 functions (46 `game`, 10 `debugger`) from the untracked
  `ects_proto/` reference checkout (targets the ECTS prototype ROM) into
  this repo's `conker/src/`, replacing raw-assembly stubs with real matched
  C, and added the struct fields/globals/prototypes those functions needed.
  12 of the 56 byte-match the US retail ROM exactly out of the box; the
  other 44 compile cleanly and are marked `// NON-MATCHING: ported from
  ects_proto (ECTS ROM build), not yet byte-verified for us` pending a real
  matching pass. Also fixed one small pre-existing bug found along the way
  (a call site in `game_1944C0.c` missing an argument).
- Fixed a long-standing link-time blocker: 26 jump-table `rodata` segments
  in `conker/conker.us.yaml` were declared as standalone segments, causing
  1153 `undefined reference` errors at link time once code near them got
  matched. Changed them to `bin` (opaque byte blobs - jump table contents
  don't need symbolic disassembly). Full root-cause writeup in
  [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md).
- `make -C conker --jobs` → `make -C conker replace NON_MATCHING=1` →
  `make` (repo root) now runs end to end for the first time, producing a
  real (correctly non-matching, ~20% complete) `build/conker.us.z64`.
  Regenerated the progress table in [`DOCS/PROJECT.md`](PROJECT.md) from
  this working build - it's the first `.map`-file-derived count this
  checkout has actually produced, so it supersedes the previously
  documented (never locally re-verified) numbers.

### Planning docs

- Added [`DOCS/WORKING_NOTES.md`](WORKING_NOTES.md): a live, editable log of
  in-progress work, so a crashed editor/terminal/assistant session can be
  resumed from a known state instead of re-derived from scratch.
- Added [`DOCS/PC_PORT_ROADMAP.md`](PC_PORT_ROADMAP.md): a phased,
  date-free plan covering what's needed to get the game running natively on
  PC with keyboard, mouse, and controller input in a playable state, plus a
  longer-term modern-graphics phase (resolution scaling, widescreen, texture
  filtering/HD packs, enhanced lighting). No PC-port work has started; this
  is planning only.
- Linked both from the `DOCS/README.md` reading order.

## 2026-07-13

### Asset formats

- Added [`DOCS/ASSET_FORMATS.md`](ASSET_FORMATS.md) documenting the asset
  compression (`rzip`), the offset-table container format (confirmed against
  `func_1502B9B4` in `game_57FA0.c`), and per-type payloads.
- Confirmed findings against the retail US ROM and the debug prototype:
  RGBA5551 textures (assets00–05), MP3 streams (assets16), the `"B1"` audio bank
  header (assets17, 22050 Hz + 170-entry sample table), and container payloads.
- Corrected the earlier "assets06 = models" assumption: assets06 is composite
  object/script data (positions, float params, dialogue strings). assets08 is
  chapter-select metadata.
- Decoded the `assets13` model geometry: four-level-nested containers whose leaf
  records are `s16` XYZ vertex arrays (6 bytes/vertex, zero-padded to 16 bytes),
  validated across all 69 records; near-identical arrays within a block are
  vertex-animation frames.
- Established that `assets13` holds **only** vertex positions - 0 display-list
  markers across all 69 records - so face/UV/normal/material data is stored
  separately or built at runtime; locating it needs the model-drawing code.
- Linked the new doc from the `DOCS/README.md` reading order.

### GitHub Actions

- Updated checkout steps from `actions/checkout@v4` to `actions/checkout@v7` so workflows use the Node 24-compatible action.
- Changed the ROM build workflow to skip baserom-dependent steps when `PRIVATE_REPO_ACCESS` or `CONKER_BASEROM_US` is missing.
- Added clear workflow notices explaining which secrets are needed to enable the full ROM build.

### Documentation

- Moved repository-owned README content into the `DOCS/` folder.
- Added the `DOCS/README.md` documentation index.
- Rewrote the project overview, code sub-project notes, compressed config notes, and IDO toolchain notes for clearer reading.
- Added this update log.
- Added `DOCS/ASSET_FORMATS.md` documenting the rzip codec, the offset-table archive container (including the previously undocumented nested-compression layer inside model files), and the model/texture/audio/table payload formats.
