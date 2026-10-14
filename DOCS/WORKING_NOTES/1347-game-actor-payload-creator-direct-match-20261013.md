# Actor Payload Creator Direct Match

Date: 2026-10-13. Continue
[Note 1346](1346-game-matrix-translation-guarded-byte-match-20261013.md) with
`func_1506AA48`: VA `0x1506AA48..0x1506AAE0`, ROM `0x97EF8..0x97F90`,
38 words /152 bytes, original frame `0x48`. The wider Game goal stays active.

## Baseline And Recovered Body

Consumer baseline `52f78290aa0962ec836f77520689732c847d716f`; tools baseline
`4e3cd4c544ad79d2991faf30be37e3cad03c5912`. Production was a zero-return
placeholder in `conker/src/game/generated_97AA0.c`.

Recover the void two-pointer interface: actor plus a readonly eight-byte raw
payload pair. Reuse `ObjectSelector97AA0` as the packet prefix, followed by the
two-word aggregate. The prepared N64 ABI gives prefix8/pair8/complete packet16;
a size assertion checks that contract without introducing padding locals.

Fill actor pointer and actor byte0x3B, then aggregate-copy the payload pair.
Submit the exact nine-slot creator arguments:
`(10,7,0x23,-1,1,0x21,16,255,1)`. On success only, copy all16 packet bytes to
created object+0x28. There is no additional pointer-return C contract; the
original incidental v0 residue is still preserved in guest qualification.

Packet bytes5..7 remain untouched. Do not initialize them or promise their
contents in portable native C. Input reads happen even when creation will fail;
failure skips the destination copy, not the actor/payload reads.

## Direct Compiler Match

New files:

- `experiments/game_actor_payload_creator_candidates.py`
- `tests/test_game_actor_payload_creator_match.py`

Sixteen real source forms across four existing profiles give64 measurements.
The ordinary O2/g3 body initially emits38/frame0x48 with only four differences:
its entire private packet is four bytes too high. Declaring the real `created`
local before the packet restores packet SP+0x34, payload SP+0x3C and copy-source
SP+0x34. No dummy storage, offset guard or compiler-profile change is used.

The selected plain, nonvolatile form matches **all38 words directly from C**,
no pool/diagnostics, no guards. The data-pointer-volatile control also matches
but is not installed. O2 without g3 emits36 words; O1 variants emit41 words;
snapshot and other qualifier controls remain rejected. Matching extents alone
do not qualify the old four-offset-difference layout.

Both original call relocations remain exact: offset0x6C R_MIPS_26 creator and
offset0x80 R_MIPS_26 memcpy. Original incoming homes at SP+0x48/SP+0x4C, saved
RA at SP+0x2C and the original return-delay no-op are recovered without rewriting
emitted instructions.

## Qualification

All14 pre-install target/text checks pass **in29.380s**. The complete installed
suite passes **16 tests in38.245s**:12 target checks, two protected text/data
checks and two focused preceding matrix-function shape regressions.

- 6,400 guest cases cover all256 selector bytes, twelve independent payload
  bit patterns in both words, failure/success, two stack phases and four provider
  modes. Check complete independent external storage, creator/copy packets,
  all38 reached words, full modeled states and the untouched three padding bytes.
- 400 alias cases cover actor/payload destinations, private packet/incoming-home
  inputs, self/forward-overlapping guest memcpy, outgoing-home overwrites and
  before-copy input mutation. Private partial struct overlap is guest evidence,
  not a portable C guarantee.
- Missing actor selector or any of the eight input bytes fails before creation
  even on allocation failure. Failure needs no destination bytes and emits no copy.
- The old real-variable order remains an effective four-word private-layout
  negative, including fired cut5. Five compiled semantic negatives change selector,
  kind, copy length, destination or payload order; all are also effective natively.
- Native32 O2/O0 executes the actual typed body,1,024 cases per profile. Check
  all defined packet bytes and every destination canary, excluding only the three
  unspecified padding contents. A native fixture indentation warning is fixed
  in its source rather than disabling the warning gate.
- Both complete owner padders retain all15 neighboring functions, relative
  relocations and normalized pools; the raw direct target bytes are preserved.
- Three independently assembled original/source layouts agree completely,
  including both JAL rebases and full modeled state. All1,728 own-instruction
  access cuts fire over96 domains and match; provider accesses are not counted
  as encoded routine instructions. Hardware PC/BD/full FCSR are not claimed.
- 24 connected cases execute the original38-word indirect dispatcher at table
  index9, original49-word creator wrapper and original11-word memcpy. Check
  forwarded actor/data inputs, `(0x23,1,56,1,255,1)` allocation arguments, header
  and payload bytes, null-result copy gate and allocator home clobbers. Only the
  generic allocator and bzero remain bounded providers.

The initial connected fixture used an incorrect Init ROM offset for memcpy.
Correct it to0x22EC0 and independently compare both helper arrays/addresses
against the frozen linked ELF before interpreting their execution. The failed
fixture is not a production defect or a qualified receipt.

These are bounded compiler/guest/native proofs, not every hardware/provider,
all callback-table entries, complete gameplay or 64-bit host-port acceptance.
Routine work uses no additional Claude call or REA setup/dependency installation.

## Installed Image And Progress

Replace only the target placeholder and add its packet types/two required helper
prototypes. Preserve original assembly, callback table, existing selector type,
all15 neighbors and the ordinary O2/g3/MIPS2 profile.

The standard linked ELF/progress build succeeds, recompiling only this owner
and relinking. The existing duplicate-recipe warning remains; target compilation
adds no diagnostics. No ROM or host executable is built or launched.

The entire ELF equals the archived image with only the152-byte target slot
replaced and that named function's size field updated12 ->152. Exactly113 bytes
differ:112 target code bytes and one size-field byte. Every other byte remains
fixed, with no blanket metadata exclusion. All189,088 Game data bytes /720
owners stay exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| Source | `e7a27f6806b4971ae868dfd528d584d29f2411fdcb9a5478695119cf398b3c3e` |
| ELF | `66e3339437aff16ec21f47afc3029e67deaa476a3b7571887d1e25b5b5365f90` |
| Guards, unchanged | `8b3792e3d9fe28cc2aec346ee217edc66cf5e5f7190f88193c3213183a5f3661` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

All15,042 historical guard rows remain byte-identical; the target has zero guards.
Fresh matching totals: Game2,827/4,823 (58.61%), total3,500/5,496 (63.68%),
different1,996, drift0. Converted functions/bytes stay fixed because the old
false-C placeholder was already counted. Root README updates aggregate rows only.

After literal image proof, archive all nine text-fixture snapshots and their
manifest under `actor-payload-creator-before-rebase/`. Advance only its ELF
snapshot and single verified ELF pin in both tools copies. Guard pin, other
protected inputs and every corruption test remain unchanged.

## Banking And Next Work

Tools **3c7f8cab499603f71a4c95d1079653df6e770fc1** banks the two new files and
one-line protected text ELF-pin update first; the consumer records the exact pin.
Older tools keeps HEAD ddbdd16 and446 of447 initial fingerprints. Only its
protected text test gets the same verified pin; two absent, byte-identical files
bring its dirty count to449. No mirror commit/reset, push, save/configuration or
frozen host Release work. Both copies pass wrapper and Windows syntax checks.

Direct Graphify update refuses18,799 proposed versus40,576 retained nodes.
Preserve19,398 nodes from2,972 excluded-but-existing files and do not force shrink.
Record incremental hook/post-bank receipts below.

Next `func_1506AAE0`:VA `0x1506AAE0..0x1506AB7C`, ROM `0x97F90..0x9802C`,
39 words /156 bytes, frame0x30, still a placeholder in the same owner. Original
code snapshots D_800CC260, scans mask bits over actors at D_800CC2D0 with stride
0x32C, and calls func_15137610 with the two global vectors. Preserve its signed
arithmetic shift/termination behavior; do not silently clamp the mask or turn
negative masks into an unsigned finite loop. This next body remains unmodified.

Reproduce from the prepared consumer under WSL:

```sh
python3 -m tools.experiments.game_actor_payload_creator_candidates --profiles
python3 -m unittest tools.tests.test_game_actor_payload_creator_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
