# Actor Descriptor Spawn Direct Match

Date: 2026-10-13. Continue
[Note 1349](1349-game-actor-vector-snapshot-direct-match-20261013.md) with
`func_1506A864`: VA `0x1506A864..0x1506A968`, ROM `0x97D14..0x97E18`,
65 words /260 bytes, original frame `0x60`. The wider Game goal stays active.

## Baseline And Recovered Body

Consumer baseline `a66c7ece58248441263eca37b888d1e918fe9ac0`; tools baseline
`7222bfa6bc27df6e407d703422596b66f329f693`. Production was a zero-return
placeholder in `conker/src/game/generated_97AA0.c`.

Reuse the existing SDK/project `Header` (six bytes) and `Header2` (three s32
coordinates), adding only `structs.h` to this owner. Recover the void actor
callback and its unused second 32-bit argument. Truncate actor X/Z to signed
integers and add50.0f to Y before truncation. Set the descriptor to
`(2,15,300,5)` and preserve its untouched `pad5` byte.

Submit the exact eleven-slot call:
`func_151602C0(&header, &position, 0,255,255,90,255,0,16,255,1)`.
Build the four-float payload `(0,80,0,D_80099A28)` before creation, including
the global read on failure. On success only, copy all16 bytes to result+0x18.
There is no synthetic null-actor/conversion clamp or extra pointer-return C
contract. Original incidental v0 values remain machine-level evidence.

The native conversion domain is finite and signed-32-bit in range. Separate
guest invalid-input tests qualify the modeled emitted TRUNC subset, not C
behavior outside its conversion domain or complete hardware exception/FCSR
behavior. Do not initialize the source header's sixth byte merely to make a
native test deterministic.

## Direct Compiler Recovery

New tools:

- `experiments/game_actor_descriptor_spawn_candidates.py`
- `tests/test_game_actor_descriptor_spawn_match.py`

24 real declaration orders across four existing profiles give96 measurements
per screen. The first screen retains65/frame0x60 but differs at six independent
stores. Archive it as `header-before-zero-measurements.json`. Move the two real
zero payload stores before the descriptor assignments; the next96-measurement
screen finds the ordinary O2/g3 body **byte-exact across all65 words**, no pool,
diagnostics or guards. No compiler or profile changes.

Declare the real created pointer, Header, float payload and Header2 in that
order. Their homes are header SP+0x54, payload SP+0x44 and coordinates SP+0x38;
RA stays SP+0x34 and incoming homes SP+0x60/SP+0x64. The unused created home
is not replaced with dummy storage. Other orders, O2 without g3 and O1 remain
rejected. The two JALs and the global HI16/LO16 pair emit directly.

The old six-store schedule is an effective cut11 private-state negative.
Equal length, frame or public output does not justify normalizing those words.

## Qualification

All14 pre-install target/text checks pass **in58.901s**. A further focused
real-factory check passes1.623s, adding the failure/unreadable-pad5 boundary.
The full installed run passes **16 tests in61.688s**: twelve target checks,
two protected text/data gates and fresh prior vector/mask direct-shape checks.

- 20,736 guest cases cover all1,728 independent coordinate patterns, signed
  integer edges and fractional Y behavior, raw coefficient bits, two results,
  three provider modes and two SP phases. Compare the independent ordered
  reference, exact eleven-slot packets, full external storage and modeled states.
  Every one of the65 instructions is reached.
- 216 alias cases cover actor/destination/global overlaps, both incoming homes
  and all relevant private blocks, with independently rebased original/source
  coefficient references. Destinations that overwrite saved RA are explicitly
  terminal-prefix cases: independently check the overwritten return word and
  matching unowned-jump boundary, not successful-return acceptance. These private
  aliases and overlapping forward copies are not portable C guarantees.
- All32 missing required-input-byte prefixes fail before creation even when
  the allocator will fail. Seventy-two bounded invalid-conversion cases agree
  in the emitted-instruction model; no native/hardware exception credit.
- Six compiled semantic negatives are effective in guest and native code:
  wrong height, truncating before Y addition, wrong duration, wrong payload,
  short copy and a late global read.
- Native32 O2/O0 executes the actual typed body,20,736 cases/profile, with
  finite in-range signed conversions, raw coefficient copies, four result/
  alias choices and complete arena canaries. Check descriptor bytes0..4;
  byte5 is unspecified unless the provider writes it, in which case its exact
  value is checked. Preserve SSE/RNE, stack realignment and warning gates.
- Complete copied-owner compilation proves that adding the existing SDK types
  changes none of the fifteen neighboring bodies, relative relocations or pools.
  Both complete padders preserve the raw direct target and agree fully.
- 108 connected cases execute the original47-word factory,32-word object
  wrapper,11-word memcpy and optional38-word parent dispatcher. Each helper's
  complete words/address is checked against frozen ELF and ROM. Verify table6
  at `0x80086128` / ROM `0x22ABE8`, both forwarded inputs and the parent's real
  vector setup. Exercise body-allocation failure, object-allocation failure/
  cleanup and success, including exact six-byte header copy, body pointer,
  flag update and final16-byte copy. Failed creation does not require pad5 to
  be readable. Body allocator, generic object allocator and cleanup stay bounded.
- Three independent original/source links qualify actual global HI/LO carries
  and both JALs with36 semantic cases and complete word/state agreement.
- All **1,944 own-instruction fault pairs /72 domains** actually fire and match.
  There are27 encoded accesses; provider reads/writes are excluded. The old
  store schedule fails the cut11 witness. Hardware PC/BD/full FCSR are not claimed.
- Header, target, preceding vector, image tail, source, guards, both affected
  symbol records and their names have effective corruption controls. Incorrect
  baseline symbol definitions also reject the expected serialization transform.

Initial fixture attempts treated a destroyed saved return address as a normal
return and contained a C preprocessing-number spacing/indentation error. Correct
those gates explicitly; do not drop the alias case or disable warnings. The
passing receipts above are separate from those failed attempts. Malformed
metadata is rejected by whole-byte equality before name parsing.

Routine work uses zero Claude calls. No dependency install, REA setup, emulator,
live gameplay or frozen host Release work is performed.

## Whole Image And Symbol Accounting

Install only this body, the existing SDK include and required factory/global
declarations. Original assembly, SDK header itself, all neighbors, ordinary
O2/g3/MIPS2, layouts and15,042 historical guard rows remain unchanged. The normal
ELF/progress build succeeds with no new target diagnostics; the existing
duplicate-recipe warning remains. No ROM or host executable is built/launched.

The first strict post-install image gate correctly rejects additional metadata
serialization. Diagnose it with the existing structured ELF/symbol parsers:
headers/section layout are identical and all named definitions are unchanged
except target size12 ->260. One adjacent record/string pair swaps order:

| Name | Address | Size | Info | Section |
| --- | --- | --- | --- | --- |
| D_80099A28 | 0x80099A28 | 0 | 16 | SHN_ABS |
| __osProbeTLB | 0x100273D0 | 184 | 18 | 3 |

Before: D_80099A28 then __osProbeTLB; after: the reverse. Assert both exact
definitions, adjacent16-byte records, original adjacent strings and offsets
before constructing this single expected permutation. This modifies only the
test's expected image, never production. The complete image must then agree
byte-for-byte, with full named-definition equality and effective mutation gates.
There are no wholesale symbol/string/metadata exclusions.

Exactly **236 bytes change**:195 target instruction bytes, two named size bytes,
17 other symbol-record bytes and22 string bytes. Every other ELF byte stays
fixed. All189,088 Game data bytes /720 owners remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| Source | `2693d762473eda06176457fb4bfa041c953b53258e6ca84a3c443f8bd039e422` |
| ELF | `3f55344bf1320fc76c68057c98eb1f6dfbf80489a62e084bca4a0aa97d59b33c` |
| Guards, unchanged | `8b3792e3d9fe28cc2aec346ee217edc66cf5e5f7190f88193c3213183a5f3661` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

Fresh Game **2,830/4,823 (58.68%)**, total **3,503/5,496 (63.74%)**,
different **1,993**, drift **0**. Converted functions/bytes stay fixed because
the false-C placeholder was already counted. Root README updates aggregate
rows only; recovery details remain here.

After the independent closed-image and corruption gates pass, archive all nine
protected text snapshots and their manifest under
`actor-descriptor-spawn-before-rebase/`. Advance only the verified ELF snapshot
and its single pin in both tools copies. All other inputs, the guard pin and
every effective corruption control remain unchanged.

## Banking And Next Work

Tools **6d547514347e72cc93e6e5e9b9eccb6eb2fb799d** banks the two new files and
one-line verified text ELF pin first; the consumer records that exact pin.
Older tools keeps HEAD ddbdd16 and452 of453 initial fingerprints. Only its
protected text test gets the same verified pin; two absent byte-identical files
bring the dirty count to455. No mirror commit/reset or push. Both copies pass
ROM-free wrapper checks and Windows byte-compilation.

Direct Graphify update refuses18,829 proposed versus40,607 retained nodes,
preserving19,398 nodes from2,972 excluded-but-existing files. Do not force shrink
or install a different package. Record incremental hook/post-bank receipts below.

Next `func_1506A968`: VA `0x1506A968..0x1506AA08`, ROM `0x97E18..0x97EB8`,
40 words /160 bytes, frame0x38, still a placeholder in this owner. It shares
the preceding actor position/global-difference snapshots but submits mode1
to `func_151D3480`, rather than mode0. Reuse the qualified vector helpers with
scoped target/ROM/symbol changes, retaining private offsets, FP/access ordering,
actual table7 caller, owner and image gates. This next body remains unmodified.

Reproduce from the prepared consumer under WSL:

```sh
python3 -m tools.experiments.game_actor_descriptor_spawn_candidates --profiles
python3 -m unittest tools.tests.test_game_actor_descriptor_spawn_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls \
  tools.tests.test_game_actor_vector_snapshot_match.GameActorVectorSnapshotMatchTests.test_01_complete_direct_words_profiles_and_real_frame_measurement \
  tools.tests.test_game_actor_mask_scan_match.GameActorMaskScanMatchTests.test_01_direct_complete_slot_and_source_profile_bank -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
