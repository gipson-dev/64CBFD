# Temporary DK64 Cross-Port TODO

This checklist records the completed automatic pass against the DK64
decompilation at `/workspaces/64CBFD/dk64-main` and the remaining ways that
repository can support Conker matching.

## Verification and scan

- [x] Verified the US DK64 ROM SHA-1:
  `cf806ff2603640a748fca5026ded28802f1f4a50`.
- [x] Decompressed the ROM with DK64's tools and extracted it with the
  repository's pinned `splat64 0.32.3`/`spimdisasm 1.32.1` environment.
- [x] Built the US ELF with DK64's original mixed profiles: IDO 5.3 for most
  code, IDO 7.1 `-g` for audio, and the documented `-O1`/`-O2`/`-O3`
  overrides.
- [x] Ran DK64's `verify` target. Its reconstructed uncompressed ROM matches
  the decompressed retail ROM.
- [x] Compared all remaining non-exact Conker C rows with 8,100 DK64
  functions using exact words, relocated call targets, and relocated global
  addresses.
- [x] Checked the requested `func_151E50C8`, `func_15017498`, and
  `func_15007A70`. They do not share a DK64 body, but all three are already
  exact in Conker's final linked ELF.

## Batch 1: completed C ports

- [x] `func_1001F28C` from DK64 `_n_loadOutputBuffer`.
- [x] `func_1001F5A4` from DK64 `_n_loadBuffer`.
- [x] `func_1001F79C` from DK64 `_n_saveBuffer`.
- [x] `guMtxXFMF` from DK64 `guMtxXFMF`.

The audio helpers required Rare's older two-channel layouts rather than the
stock Conker SDK header layout. DK64 also established that
`func_1001FA78` is `_doModFunc`; correcting that call target turned
`func_1001F28C` from address-blocked to exact. The matrix translation unit
uses `-O3`; `guMtxCatF` and `guMtxXFMF` are both byte-identical between the
games under that profile.

Verified refreshed diagnostic after the batch:

- total: `2489 / 5978 (41.64%)`
- init: `372 / 508 (73.23%)`
- game: `1951 / 5289 (36.89%)`
- debugger: `166 / 181 (91.71%)`
- blocker: only the unrelated generated helper `func_10012588`

Published stable-corpus progress is total `2486 / 5973 (41.62%)`, init
`373 / 508 (73.43%)`, game `1947 / 5284 (36.85%)`, and debugger
`166 / 181 (91.71%)`.

## Batch 2: structural audio ports

- [x] `func_10018790` from DK64's compact-sequence marker reader.
- [x] `func_1001ED6C` from DK64 `n_alFxParamHdl`.
- [x] `n_alFxNew` from DK64's Rare reverb constructor.
- [x] `func_1001B07C` from DK64 `__n_lookupSoundQuick`, retaining Conker's
  null-instrument guard.
- [x] `n_alCSeqNextEvent` from the shared sequence body, retaining Conker's
  no-track guard.
- [x] `func_10022460` from DK64's modified resampler pull.
- [x] `func_10021E4C` from DK64's decoder DMA helper, retaining Conker's
  null-DMA recovery path.

These candidates came from opcode/control-flow and constant fingerprints after
the exact-word and relocation-masked pools were exhausted. The shared DK64
body supplied the source shape, while Conker retail assembly identified the
small game-specific guards and one deliberate empty scheduling block.

## Batch 3: EEPROM family

- [x] `func_151DD460` — EEPROM probe.
- [x] `func_151DD304` — read-packet builder.
- [x] `func_151DD140` — EEPROM read.
- [x] `func_151DD710` — EEPROM status request.
- [x] `func_151DD65C` — write-packet builder.
- [x] `func_151DD4E0` — EEPROM write.

All six use the DK64/libultra source algorithm with Conker's local PIF RAM and
function names. Each function was counted only after a full link and direct
retail-byte comparison.

## Final broadened pass

- [x] `func_10022040` from DK64's resample/effect wrapper, using Conker's
  extended `N_PVoice` offsets and non-intrinsic `sqrtf` call.
- [x] `func_1001E530` from DK64 `n_alFxPull`. Conker removes DK64's two
  debug-stack padding locals and initializes the pull counter to zero.
- [x] `func_10020ABC` from DK64 `_pullSubFrame`, plus Conker's wave-table
  side effect, wet/dry refresh, and deliberate command-scheduling gap.
- [x] Changed the matcher's disassembly to preserve zero words with
  `objdump -d -z`. This stopped long intentional `nop` runs from appearing as
  `...` and recovered five pre-existing exact rows:
  `D_160036F0`, `D_16003A68`, `D_16003CE0`, `D_16004950`, and `__n_vsVol`.
  The same correction is required to assess the newly matched
  `func_1001ED6C` accurately.
- [x] Added an optional compact-object `.rodata` retail anchor. The restored
  reverb gain constant begins at `D_8002C7A0`, immediately before
  `jtbl_8002C7A4_init`; anchoring the complete compact `.rodata` block there
  keeps the pull routine and the following parameter handler exact.

Final refreshed US corpus:

- converted: `5978 / 6038 (99.01%)`
- total byte-exact: `2510 / 5978 (41.99%)`
- init: `383 / 508 (75.39%)`
- game: `1957 / 5289 (37.00%)`
- debugger: `170 / 181 (93.92%)`
- address-only blocker: `func_10012588`

## Reference-only exact bodies

These cross-game matches are handwritten assembly in DK64. Copying them would
not advance a genuine C decompilation, but they remain useful for signatures,
SDK variants, constants, and semantic checks:

- `bcopy`
- `osInvalDCache`, `osInvalICache`
- `osWritebackDCache`, `osWritebackDCacheAll`
- `__osDisableInt`, `__osGetSR`, `__osSetSR`
- `__osSetCompare`, `__osSetFpcCsr`, `osGetCount`
- Conker `func_150AD780` / DK64 `func_global_asm_80612D10`
- Conker `func_150AD78C` / DK64 `func_global_asm_80612D1C`

The last pair is Rare's fast trigonometry implementation and includes its
polynomial constants and range-reduction behavior. It is especially useful
as semantic evidence if those Conker assembly slots are later represented in
a source language that can preserve handwritten instructions honestly.

## Remaining use

- [x] Exhaust the automatic exact/relocation-masked C pool.
- [x] Exhaust the broader opcode/control-flow candidate pool and port every
  candidate that survived signature, constant, call, and field-offset checks.
- [ ] Continue normal byte matching on the divergent audio candidates
  `func_100214F0`, `func_10020000`, `func_100210C0`, and
  `func_10021C40`; DK64 supplies structure and algorithm evidence, but none is
  a safe whole-body port.
- [ ] Consult DK64 manually when a remaining Conker function calls a shared
  Rare audio, matrix, heap, controller, or fast-math helper.
- [ ] Recheck object profiles before tuning source expressions; DK64 confirms
  `-g`, `-O1`, `-O2`, and `-O3` were all used in adjacent subsystems.
- [ ] Keep handwritten matches reference-only unless the project explicitly
  adopts a source representation for handwritten assembly.
