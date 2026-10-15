# Packed Color Callback Semantic Recovery

Date: 2026-10-15. Continue the whole additional-source / Game objective from
[Note 1397](1397-packed-coordinate-preset-direct-match-20261015.md).

## Result And Boundary

Recover the complete semantics of `func_1516E8CC`, VA `0x1516E8CC`, ROM
`0x19BD7C`, **248 words / 992 bytes**, in `asm/19A8B0.s`. Its active owner is
`conker/src/game/generated_19A8B0.c`; the production zero-return stub is
**unchanged**. The new candidate is an experiment, not an installed match.

The prior archive draft emitted 293 words / 291 positional differences. The
clean, behavior-tested candidate emits **241 words / 234 positional
differences**, without diagnostics. A separate nested-return / integer-operand
shape emits **245 words / 153 positional differences**. These counts include
shifted instructions and missing words, not independent scheduling fixes.
Neither result passes the direct-match gate; do not pad it and claim matching.

Bank tools **af89f68** before the consumer pin/docs. No new C body, instruction
guard, compiler profile, conversion or exact-match credit is installed.

## Retail Recovery

- Byte `+0x24` is the countdown. Byte `+0x1F` is intensity, initially widened
  to a full word. With countdown active, add wrapping `delta << 5` and clamp
  signed values above 255. With countdown zero, subtract wrapping `delta << 4`
  and clamp negative signed values to zero. Preserve the live full-word value
  after the byte store: 240 minus negative 16 gives live 256 / stored zero,
  which must not report completion.
- Return 1 only when the freshly read countdown and full live intensity are
  both zero. Otherwise read the live `D_800BE9E4`, grow signed halfword `+0x14`
  by wrapping `10 * delta`, and store the low half to `+0x16`, then `+0x14`.
- Phase is countdown plus eight while active; otherwise reload the stored
  intensity byte and shift right five. Byte `+0x26` selects the ramp start.
  The scan uses a full-width index and at most eight entries for stable input;
  retail reloads the start byte on each unsuccessful iteration.
- On the first threshold at or below phase, compute single-precision weight
  `(phase - current) / (previous - current)` and complement `1 - weight`.
  Interpolate previous/current RGB triples and store bytes `+0x1C..+0x1E`.
  Preserve explicit unsigned-byte-to-float and float-to-u32 conversions.
  Return 0 whether an interval was found or the scan was exhausted.
- This is callback-table index zero at `D_8008CBA0`. It is a leaf with no
  frame. Retail first copies the record into V0, then reuses V0 as the RGB
  pointer only on the found path. Its final duplicate JR RA / NOP is part of
  the 248-word routine, not a zero-alignment allowance.

The archive's word accesses at packed byte/halfword offsets, byte-sized live
accumulators, and float read of the previous threshold are incorrect. The
experiment corrects them and preserves address-based naming and a concise
semantic comment. The original archive remains read-only.

## Tables And Frozen Inputs

Pin **52 distinct inputs**, extending Note 1397's 50 with the actual table
assembly and `conker/conker.us.yaml`. The 48-byte `.rodata` owner at ROM
`0x24B8C0` / VA `0x800A6E00` contains:

- `D_800A6E00`: 12 threshold bytes, `FF 28 23 1E 19 14 0F 00 FF 28 00 00`.
- `D_800A6E0C`: 12 RGB triples, `FFFF00 FFFF00 FF8000 FF8000 FF0000 FF0000
  C00000 800000 5A5A5A 5A5A5A 000000 000000`.

Verify those bytes independently in the retail ROM and frozen linked ELF.
The finite tests use starts 1 and 9, backed by these tables. This does not
prove every byte index is a valid input or establish all actual caller ranges.

| Unchanged Input | SHA-256 |
| --- | --- |
| ELF | 0d6c257e96de73bb11c6280264874c2ef93a6b24c09978fb570d8e7b04e2fdaa |
| Owner | 3bef553a67bbae52a760fea7d8d9363f4416e9344cea75d533384489571822a5 |
| Guards | e48ca462691e03b724b1dfae8542e4a592826157a755bd4dcc62851a00830491 |
| Progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |
| Table assembly | 2f80072f25446241d36ad865a4a17126cfd5501df8bdd26f2bb01d12fc3f72ed |
| Data configuration | d31a14128e74793a2cc5fcb7ca3a65abefc7cafe01528268b0e0af76f94bff1f |

## Fresh Qualification

**Seven checks pass in 29.801 seconds**:

- Compare the complete clean candidate against retail and an independent
  state model in **3,072 paired finite guest cases**: all intensity bytes,
  countdowns 0/85/170/255, 11 delta boundaries, extent wrapping and delta
  aliases with RGB/intensity and extent fields. Compare full memory and return.
- Check **1,024 further original-guest results** and run the candidate against
  their field results in freestanding native32 GCC at **O2 and O0**, with SSE
  single precision, no contraction and no strict aliasing. Only finite table
  cases are accepted; no arbitrary float-to-u32 portability claim.
- Five compiled negatives fail as intended: early byte truncation (7 cases),
  wrong fade speed (27), omitted second extent (247), wrong phase (160) and
  swapped red weights (87). The matching gate also rejects wrong lengths,
  differing words and compiler diagnostics.
- Compile both complete owners. All **29 neighboring routines**, their sizes,
  raw bytes, relative relocations and normalized pools are fixed.
- Recheck all **52 live production input hashes**, reject all 52 corrupted
  immutable captures, and verify all **801 original archive fingerprints**.

Reuse the established `MaskOracle`, `TriangleOracle` and bounded `AreaOracle`
conversion operations. Their nontrapping FCSR model verifies requested
truncation and restoration; it is not a complete hardware FCSR emulator.
Raw instruction read order differs from retail: no guest-fault-prefix,
register-state, arbitrary-alias, connected-lifecycle or gameplay equivalence
claim is made, and those installation gates remain open.

Reproduce from the decomp root in PSBBN with `PYTHONPATH=.`:

```sh
python3 -m tools.experiments.game_packed_color_callback
python3 -m unittest tools.tests.test_game_packed_color_callback -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

The maintained screen has four complete source forms under normal O2/g3 and
the no-unroll profile, eight fresh results; all are rejected. Other local
void-pointer, structured-record, pointer-reuse, signed-arithmetic, do-loop,
shared-exit and explicit countdown probes were also nonmatching. They are
exploratory ignored artifacts, not maintained qualified variants. No-unroll
does not improve the maintained results. Shared tool checks pass; the normal
ELF/progress build is up to date. Its existing duplicate-recipe Makefile
warning is unchanged and unrelated.

## Banking And Next Work

Fresh official matcher remains **Game 2,895/4,828 (59.96%)**, **total
3,568/5,501 (64.86%)**, **1,933 different**, zero address drift. Conversions,
guard history, all production bytes and root README aggregate rows are fixed.
Do not relabel the 245-word experiment as three remaining scheduling words.

Preserve the older standalone tools mirror's independent ddbdd16 HEAD and all
**652 initial dirty fingerprints**. Copy only the two absent owned files;
verify **654 final paths**, Windows syntax and the standalone ROM-free check.
Do not commit/reset that mirror or copy its history. No push, Claude call or
host/Release source/build/launch; preserve real saves/configuration.

Next continue `func_1516E8CC` matching with the original V0 record/color
lifetime, retained loop-bound reload and exit shape. Investigate compiler
allocation/control-flow evidence before any normalization. Retain the full
unsigned FP conversion sequences and all 248 words. Then complete raw/padded,
private register/fault, independent rebases, real updater/cleanup and exact
linked-image gates before replacing the production stub. The adjacent
`func_1516ED68` is another pending callback, not an audited alternative match.

The whole-source obstruction queue and prior 1,717-object audit in
[Note 1396](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md)
are retained, not rerun here. Keep failed-comment/binding repairs,
`func_1516D738`'s inherited-stack C deferral, handwritten Init hardware routines,
`func_1510BF60` and the broader Game objective open. Evidence is ignored under
`conker/build/game-packed-color-callback/`.

## Post-Bank Verification

Consumer **7f267179** banks the working docs and tools **af89f68** pin. All
**seven post-bank checks pass in 61.892 seconds**, including the 52 live
production inputs/capture controls and fresh verification of all 801 archive
files. Both active checkouts are clean before this receipt. The older mirror
retains its independent HEAD, all 652 original fingerprints and **654 final
fingerprints**; the two owned copies remain identical to the tools commit.

Seven documents / **4,984 relative Markdown links** validate without a broken
target. The full graph scan refuses 19,377 nodes against 41,147 existing;
preserve that fail-closed result. The actual commit worker completes with
**41,156 nodes / 81,252 edges / 3,800 communities**, retaining the existing
excluded-but-present corpus without forcing a smaller graph. No push or
host/Release action. No match credit is added; continue the original pointer,
loop-bound and exit-shape investigation described above.
