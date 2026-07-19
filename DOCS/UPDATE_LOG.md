# Update Log

This log tracks repository-facing documentation, workflow, and project maintenance updates.

For code-level progress, run:

```sh
make -C conker progress
```

## 2026-07-19

### Byte-exact matching crossed 40% overall

- Matched roughly 230 more game functions by reconstructing small
  generated-slice placeholders directly against retail instructions, focusing
  on repeated families: typed argument-forwarding wrappers, predicates,
  stack-local event records, jump-table dispatchers, linked-list walkers,
  clamped-store helpers, and float accumulate/scale routines.
- Root-caused a large class of mismatches to missing local prototypes in
  generated slices (implicit declarations reload narrow arguments from home
  slots instead of masking in place) and fixed whole families by adding
  per-file prototypes.
- Identified per-slice retail compile profiles: two slices build with plain
  `-O2` (filled jr-delay slots) and four need `-Wo,-loopunroll,0`; recorded the
  overrides in `conker/Makefile`.
- Corrected two wrong callee identities (`func_100111C8` vs a stale
  `func_140111C8` symbol, and `memcpy`/`bzero`/`allocate_memory`/Pi-access
  libultra callees referenced by name-implied placeholder ids).
- Verified **1860 / 5284 game functions (35.20%)** and **2393 / 5973 overall
  (40.06%)** byte-exact, with one address-drift blocker and no regressions in
  init or debugger sections.

## 2026-07-18

### Documentation topics consolidated

- Rebuilt the root README as a concise project entry point with a clearer
  status explanation, supported build overview, contribution path, and
  purpose-based documentation links.
- Reorganized `DOCS/README.md` into a subject index and made `PROJECT.md` the
  detailed source for build, environment, CI, ROM-layout, and progress
  explanations.
- Added `DOCS/CONTRIBUTING.md` as the durable home for function selection,
  byte-matching workflow, IDO-sensitive source patterns, retail-span rules,
  and required validation.
- Labeled `WORKING_NOTES.md` as an archive/scratchpad, added a topic index, and
  separated the current recovery entry from historical focus snapshots.
- Corrected and expanded the asset specification: documented the real packed
  entry bitfield and 30-entry master table, libaudio `B1`/`S1` structures,
  confirmed game-code archive/XOR layout, vertex-count ambiguity, scoped
  texture evidence, and the complete known/unknown section inventory.
- Updated `tools/asset_dump.py` to derive all `assets00-assets1C` boundaries
  from the retail master table instead of maintaining a partial hardcoded list.

### Repeated wrapper sweep reached 36.28% overall

- Matched 13 more game functions across four repeated two-function families
  and one five-function cleanup family.
- Recovered exact retail argument forwarding, indexed byte lookup, stack-local
  record dispatch, and deliberate repeated volatile field reads in call delay
  slots.
- Verified **1634 / 5284 game functions (30.92%)** and **2167 / 5973 overall
  (36.28%)**, with **0** address-drift blockers. Raw C conversion remains
  **5973 / 6033 functions (99.01%)**.

### Fast byte-matching sweep passed 35% overall

- Matched 246 additional game functions across generated slices, emphasizing
  repeated two-call wrappers, field setters, callback dispatchers, compact
  predicates, argument-forwarding helpers, and fixed-point/float leaves.
- Restored retail IDO schedules with exact argument widths, explicit temporary
  loads, direct boolean expressions, name-implied retail globals, and repeated
  wrapper templates; rejected experiments that exceeded their retail spans.
- Added the missing external routine symbol at `0x140111C8`, allowing two
  retail handle-release wrappers to link and be measured normally.
- Verified **1621 / 5284 game functions (30.68%)** and **2154 / 5973 overall
  (36.06%)**, with **0** address-drift blockers. Raw C conversion remains
  **5973 / 6033 functions (99.01%)**.

### Fast generated game sweep reached 26.02%

- Matched 45 additional compact game functions across generated slices,
  concentrating on direct wrappers, state setters, accessors, flag updates,
  indexed writes, and global resets that reproduce retail IDO code cleanly.
- Recovered exact short-function shapes through argument preservation, call
  delay-slot constants, right-to-left expression ordering, volatile pointer
  reloads where retail reads twice, and explicit field-width/sign choices.
- Kept useful partial reductions for `func_150F02A0`, `func_150CBF5C`, and
  `func_151D0128`; reverted the `func_151EFF70` experiment after its compiled
  body exceeded the retail span.
- Verified **1375 / 5284 game functions (26.02%)** and **1908 / 5973 overall
  (31.94%)**, with zero address-drift blockers and no lost exact matches.

### Difficult game near-matches recovered

- Matched `func_150779D4` and `func_15079570`, two 51- and 59-instruction
  routines that were already behaviorally correct but still differed in
  floating-point temporary allocation and a final address-register choice.
- Restored the retail expression shapes with explicit distance and threshold
  temporaries plus the native `struct127.y_position` field access.
- Matched the 54-instruction `func_1507879C` by separating its `struct197`
  pointer load from the float access, restoring retail's `v0` reuse across
  the indexed object lookup.
- Reduced the 55-instruction `func_15135480` from seven real instruction
  differences to two by restoring its reused object value and early-exit
  comparison shape; the two remaining differences are commuted branch
  operands.
- Rejected and reverted experiments that worsened `guMtxCatF`,
  `func_1505D024`, `func_1505841C`, `func_151254F4`, and `func_1514672C`.
- Verified **1330 / 5284 game functions (25.17%)** and **1863 / 5973 overall
  (31.19%)**, with zero address-drift blockers and no lost matches.

### PC-port runtime reference

- Evaluated N64 Modern Runtime as a useful Phase 1/2 candidate instead of a
  generic reference: `ultramodern` covers much of the libultra OS surface and
  `librecomp` bridges N64Recomp output plus ROM/save operations.
- Added a compatibility-inventory step and kept the runtime reference-only
  until Conker's Rare-specific code and microcode are proven compatible; no
  dependency, submodule, or ROM-build change was made.
- Added RT64 as the first renderer to evaluate before committing to a custom
  RSP/RDP display-list interpreter.

### Game byte-exact progress reached 25.11%

- Matched ten additional game functions: `func_15014220`, `func_15015644`,
  `func_15075884`, `func_15075AAC`, `func_1512D368`, `func_1514373C`,
  `func_151927C0`, `func_151D2BA4`, `func_151EEFF0`, and `func_151EF080`.
- Recovered four larger 35-45-word routines alongside compact math, state,
  copy, and generated-slice helpers by restoring retail argument constants,
  statement order, temporary-expression shapes, and the required IDO object
  profile.
- Rejected an optimization-setting tradeoff that would have lost an existing
  exact function; the clean rebuild retains every prior match.
- Published game byte-exact progress at **1327 / 5284 functions (25.11%)**
  and total byte-exact progress at **1860 / 5973 (31.14%)**. Address-drift
  blockers remain zero and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress reached 56.89%

- Matched 26 additional init functions across PI/SI/SP raw I/O, VI state,
  message queues, thread management, timers, audio, libc, and game code.
- Restored the retail IDO `-O1` object profiles and the original
  `register`-qualified status, interrupt-mask, queue-index, and thread-walk
  locals that control allocation and scheduling.
- Reconstructed exact source shapes for `func_1000F1A8`, `func_1001AFEC`,
  `__n_nextSampleTime`, `strchr`, and `osAiSetNextBuffer`; reduced
  `func_1000FE88` from three real instruction differences to two.
- Published init byte-exact progress at **289 / 508 functions (56.89%)** and
  total byte-exact progress at **1735 / 5973 (29.05%)**. Address-drift
  blockers remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress reached 51.77%

- Matched eight additional init functions: `ldiv`, `lldiv`,
  `__osSpRawStartDma`, `osSpTaskYielded`, `osViSwapBuffer`,
  `__osDequeueThread`, `__osTimerInterrupt`, and `__osSetTimerIntr`.
- Recorded the retail IDO optimization profiles per object and restored the
  original `register`-qualified thread-queue source shape.
- Corrected `func_1001091C` to pass the retail pointer value instead of an
  unrelated pointed-to field; the function remains one instruction from an
  exact match.
- Published init byte-exact progress at **263 / 508 functions (51.77%)** and
  total byte-exact progress at **1709 / 5973 (28.61%)**. Address-drift blockers
  remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Init byte-exact progress crossed 50%

- Matched 22 additional init functions, including native 64-bit compiler
  helpers, PI/SI access and raw-I/O routines, SP status helpers, VI framebuffer
  accessors, message-queue helpers, `memcpy`, `strlen`, and one audio event
  walker.
- Restored retail IDO `-O1`/`-O2` profiles, native MIPS III code generation,
  and original `register`-qualified source shapes where they determine exact
  instruction scheduling.
- Published init byte-exact progress at **255 / 508 functions (50.20%)** and
  total byte-exact progress at **1701 / 5973 (28.48%)**. Address-drift blockers
  remain 27 and raw C conversion remains **5973 / 6033 (99.01%)**.

### Byte-exact progress crossed 28%

- Reconstructed 63 compact generated-slice functions as matching C,
  including callbacks, constant handlers, scalar helpers, field initializers,
  table accessors, flag setters, and thin call wrappers.
- Preserved retail incoming registers and call-delay-slot constants through
  explicit legacy declarations, calling-convention-width parameters, and
  targeted `register` annotations.
- Reverted four exploratory near-matches so the published code batch contains
  only confirmed exact improvements.
- Published byte-exact progress at **1679 / 5973 functions (28.11%)**, with
  address-drift blockers unchanged at 27 and raw C conversion unchanged at
  **5973 / 6033 (99.01%)**.

### Byte-exact progress crossed 27%

- Reconstructed 35 small generated-slice functions as matching C, including
  typed callbacks, constant-return handlers, nested accessors, arithmetic
  helpers, and state setters.
- Preserved IDO's retail argument-home behavior and register scheduling with
  explicit calling-convention-width parameters and targeted `register`
  annotations.
- Published byte-exact progress at **1616 / 5973 functions (27.06%)**, with
  address-drift blockers unchanged at 27 and raw C conversion unchanged at
  **5973 / 6033 (99.01%)**.

### Total raw C conversion crossed 99%

- Replaced 416 validated `GLOBAL_ASM` groups across 105 mixed sources and
  moved 80 tracked libultra functions through 40 typed standalone C slices.
- Extended signature discovery for nested function pointers, local `static`
  declarations, directly included source headers, macro-shadowed names, and
  legacy functions called with inconsistent argument counts.
- Generalized generated-slice Makefile and linker support to nested libultra
  assembly paths, while retaining exact retail symbol placement.
- Published raw conversion at **5973 / 6033 functions (99.01%)** and **98.34%
  by bytes**; game conversion reached **5284 / 5313 (99.45%)**.
- Recorded the complete 60-function raw remainder and the honest byte-exact
  result: **1581 / 5973 (26.47%)**, with 27 address-drift blockers.

### Total raw C conversion crossed 90%

- Added 167 validated standalone game slices and replaced 246 `GLOBAL_ASM`
  groups across the eight largest remaining mixed C sources.
- Added a reproducible mixed-source converter that reuses declared signatures,
  infers consistent legacy-call arity, and validates each referenced asm file.
- Published raw conversion at **5477 / 6033 functions (90.78%)** and **84.09%
  by bytes**; game conversion reached **4968 / 5313 (93.51%)**.
- Kept address blockers at 24. Required legacy-call signatures perturb one
  previously exact caller, leaving **1584 / 5477 (28.92%)** byte-exact.

### Total raw C conversion crossed 80%

- Replaced 82 additional safe text-only game assembly slices with generated
  non-matching C sources, moving 588 tracked functions into C.
- Taught the placeholder generator to recognize indented global entry points
  and reject retail slots smaller than the compiler's eight-byte minimum.
- Excluded one mixed code/data slice and two slices with four-byte entry spans
  instead of weakening the layout validator or dropping symbols.
- Published raw conversion at **4846 / 6033 functions (80.32%)** and **68.37%
  by bytes**; game conversion reached **4338 / 5313 (81.65%)**.
- Retained all **1585** byte-exact functions and kept address blockers at 24.

### Total and game raw C conversion crossed 70%

- Replaced 44 additional text-only game assembly slices with generated
  non-matching C sources, moving 612 tracked functions into C.
- Checked every selected slice for embedded data sections or word tables before
  replacement, then regenerated the retail-layout manifest.
- Published raw conversion at **4258 / 6033 functions (70.58%)** and **55.77%
  by bytes**; the game section independently reached **3750 / 5313 (70.58%)**.
- Preserved all prior exact matches and recovered one additional match, taking
  byte-exact progress to **1585 / 4258 (37.22%)** with 24 address blockers.

### Total raw C conversion crossed 60%

- Replaced 25 additional text-only game assembly slices with generated
  non-matching C sources, moving 613 tracked functions into C.
- Made generated-slice Makefile filtering and linker placement automatic so
  future additions no longer require duplicated hardcoded slice lists.
- Added a reproducible placeholder generator, including compact empty-body
  stubs for functions whose retail slots are only eight bytes.
- Published raw conversion at **3646 / 6033 functions (60.43%)** and **43.81%
  by bytes**. Byte-exact progress is **1584 / 3646 (43.44%)**, with all prior
  exact matches retained and one additional exact function recovered.

## 2026-07-17

### Byte-exact progress crossed 50%

- Added retail-layout manifests and build-time object re-spacing that preserve
  C-compiled instruction words and relocations while restoring function and
  object addresses.
- Kept oversized non-matching functions executable in section-local overflow
  regions through short retail-slot trampolines, preventing them from shifting
  later exact code.
- Restored generated-slice jump labels inside their padded C-derived objects
  and reduced address-drift blockers from 836 to 24.
- Published the new result: **1583 / 3033 C functions byte-exact (52.19%)**,
  with raw C conversion unchanged at **3033 / 6033 (50.27%)**.

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
