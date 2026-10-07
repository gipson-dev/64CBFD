# Game Scaled Descriptor Match

Date:2026-10-06. Baseline:`349aa845`
([Note1065](1065-game-random-descriptor-match-20261006.md)).
Continue original Game decomp matching, not host adoption or full gameplay
acceptance. Production source:[game_16EE20.c](../../conker/src/game_16EE20.c).

## Retail Contract

**func_15142180**:80 words /320 bytes, frame0x70,
VA15142180..151422C0, ROM16F630..16F770. Recover five inputs:
`void func_15142180(u8 slot,struct17 *source,s32 word,f32 width,f32 height)`.
Seven original call continuations do not consume a scalar result. Third input
is an opaque32-bit word, not an integer-to-float conversion. Width arrives in
A3; fifth-argument height arrives at entry SP+10.

Build the76-byte descriptor at current SP+24, relative offsets:

| Offset | Original field |
| --- | --- |
| 00/02/04/06 | halfwords0/255/-25/10 |
| 08..13 | three position words copied from source |
| 14/18 | separately rounded2.5*width and2*width |
| 1C/20 | live float words D_800A5470/5474 |
| 24/28 | separately rounded3*height and3.5*height |
| 2C..3A | halfwords3/3/3/1/9/15/180/75 |
| 3C | low-byte slot |
| 3D..3F | untouched private padding, not implicit zeros |
| 40 | positive-zero float |
| 44/46 | halfwords12/21 |
| 48 | full-width opaque input word |

The complete submit ABI is:

```c
func_15153F18(&descriptor, &descriptor.point, 0, 255, 1);
```

Retain point pointer=root+8, not root+4 or the original source. All source/
constant reads finish before submit. No memset or expanded payload is added.
The three-word copy is interleaved read/store in guest code; partial overlap
with private stack storage is guest-only evidence, not legal native struct
assignment overlap.

Constants retain words3DDD2F1B/3E51EB86 at VA800A5470/5474,
ROM249F30/249F34. They belong to the existing640-byte Game-data owner at
800A5200..800A5480, not a new compiler pool. Keep the existing pool anchor,
absolute symbol definitions and all original switch-table targets.

## Direct Compiler Recovery

[Maintained driver](../../tools/experiments/game_scaled_descriptor_candidates.py)
screens16 source shapes across four actual-SDK profiles:64 controls. Empty
standalone diagnostics throughout. Only shape-1110-o2g3 matches all80 words.

Field-wise/float-literal controls emit78 words with many allocation differences.
IDO folds `2.0f * width` into add.s, omitting retail's constant materialization.
The original integer literal `2 * width` recovers80 words/frame0x70 but leaves
ten scheduling differences. Aggregate position copy and placing the -25/10
header assignments immediately before the final3 halfword recover every word.
Reversing those two assignments leaves four differences.

Rejected exploratory double-literal controls have frame0x78, volatile local
controls82 words, and split header/record locals leave scheduling differences.
No rejected frame/type workaround is installed. Production uses the original
O2/g3 profile, no word guards, frame rewrites, insertion/omission, shared header,
Makefile or padding-tool changes. Local layout and helper declaration retain
the full descriptor; the unrelated small SDK struct218 is not adopted.

## Qualification

[Eleven maintained tests](../../tools/tests/test_game_scaled_descriptor_match.py):

- **10800 paired guest cases**:six opaque words, five width/five height values,
  three source aliases, three output aliases, four slot bytes and two stack
  phases. Compare all ordered traces and full storage against original words
  and independent expected fields. Reach all80 words in both bodies; SP/RA/
  saved registers/FPRs survive poisoned submit calls.
- **2240 edge cases**:512 every-byte/full-width slot aliases and1728 special
  width/height/constant/source combinations. Signed zeros, subnormals, overflow,
  infinities and NaNs retained as binary32 values. No hardware FCSR, exception
  flag, rounding-mode or native arithmetic NaN-payload parity claim.
- **28 guest-only private probes**:parameter-home and partially overlapping
  position sources under two stack phases/two poison patterns. Bind saved
  slot/source/opaque/height homes, untouched width home and interleaved copy.
  No native access to private parameter homes or partial struct-overlap claim.
- **20992 actual32-bit native cases**:20736 opaque/float/constant/source/output/
  slot combinations plus256 every-byte cases. Verify known descriptor bytes,
  all five submit arguments and all external storage. Only padding61..63 is
  excluded; arithmetic NaNs are classification-compared. Live constants may
  alias source and submit output without changing their earlier capture.
- **42 connected cases** execute the seven original jal/delay pairs, including
  fifth-argument swc1, under three aliases/two stack phases. Caller continuation
  is a synthetic saved-RA epilogue; **not complete original caller execution**.
- Actual padder preserves all320 bytes and five HI16/LO16/call relocations.
  Alternate constant addresses exercise signed-low-half carry; zero guards.
- Twelve compiled negatives change known external storage/call sequence on
  mapped inputs:placeholder, missing submit, wrong copy/opaque width/slot/
  width factor/height factor/constant/signed header/halfword/subrecord pointer/
  submit flag. Faults, compiler differences or padding-only differences do
  not satisfy the negative gate.
- Unmapped source/source+8/constants/output fails strict guest memory gates.
  This is not a hardware fault or legal native out-of-bounds claim.
- Copied actual-SDK owner has93 functions:target raw bytes/relocations equal
  standalone direct body;92 other raw functions/relocations, original608-byte
  private pool and two warnings unchanged. Baseline reconstruction in tests
  touches only this target in a copy, without historical Git/ignored fixtures.
- Production binds source/prototype, complete80-word slot, six exact neighbors,
  original constant bytes and the entire unchanged10809-row guard file.

Submit func_15153F18 remains a bounded model in behavior fixtures. Its original
168-word body in asm/17CAF0.s is not executed or restored here; generated_17CAF0.c
still has a placeholder. Instruction identity proves this function's retail
code, not allocator/helper acceptance, real effect output or full gameplay.

Initial native gate stopped at -Werror=misleading-indentation in fixture code;
split the check and case-counter statements. Also route expected output through
explicit fixture bank/offset, avoiding relational comparisons of unrelated
array pointers. Corrected20992 native cases pass; production source unchanged
by those harness fixes. The other nine initial tests passed in the95.697-second
bundle; that initial bundle as a whole failed and is not counted as acceptance.

## Production Verification

Explicit `make -j4 VERSION=us build/conker.us.elf` passes. Compared against
349aa845, **only func_15142180 changes across6059 slots**; addresses/extents
stay fixed. Target SHA-256:
`09b73aabc9b9a77ea10a5e919df759408c84a93c1ab904aa39215b8d2caa7499`.
Dispatcher100, actor45, context57, checked caller37, updater80 and prior random
descriptor96 words remain exact. Protected .init/.init_data/.debugger/.game_data
addresses/hashes unchanged; all720 Game-data owners /189088 bytes match, zero
differing owners/bytes. Owner warnings2->2 with identical code/statement/caret
evidence, no new warnings. Full build is not warning-free.

All10809 guard rows remain unchanged, canonical SHA-256:
`e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a`.
Conversion remains5464/6042 total and4791/5321 Game; byte coverage stays85.57%
total/84.89% Game. Exact total **3341/5464 (61.15%)**, Game
**2668/4791 (55.69%)**, **2123 different**, zero drift. Init492/492 and
Debugger181/181 remain exact. Complete-ROM checksum not claimed.

All65 focused post-link tests pass in513.711 seconds, no skips/errors/failures:
11 scaled descriptor,11 prior random descriptor,11 updater, eight actor,
eight context,11 dispatcher and five actual-padder tests. Documentation:
48 documents/3533 relative links/zero broken. Project tool, scoped Python
syntax and `git diff --check` gates pass. Ignored receipts:
`conker/build/game-scaled-descriptor-test/`.

## Next Function

Continue **func_151424F4**,67 words /268 bytes, frame0x68,
VA151424F4..15142600, ROM16F9A4..16FAB0. The intervening six routines already
have semantic C; do not count them again. Target remains a zero-return stub.

1. Recover twelve inputs:output Mtx pointer, two float row factors, three float
   rotation arguments, three float column factors and three float translations.
   Original caller func_15133510 at VA15133510/ROM1609C0 forwards actor words
   +18..40; jal/delay at VA15133568/ROM160A18 stores final translation in SP+2C.
2. Call typed func_150A8050 on a local4x4 float matrix at SP+28. Preserve the
   separately rounded column-factor*row-factor, then matrix-element multiply.
   First/third rows use first row factor; second uses the second factor.
3. Write translations to matrix[3][0..2], preserving provider-built remaining
   elements. Keep guMtxF2L(matrix,output) and its output-pointer lifetime.
4. Screen local-array/explicit-index/source-order shapes under actual SDK
   profiles. Recover67-word frame0x68 before any normalization or installation.
5. Qualify provider mutations, row/column asymmetry, float edges, caller/ABI,
   native/guest behavior, actual padding and complete owner/data/slot audit.
   Rotation provider and fixed conversion need explicit validation boundaries;
   bounded models do not prove hardware FCSR or full rendering.

Initial scratch screen:16 controls (explicit/common-product locals and
translation-before/after shapes times four SDK profiles). Explicit element
updates with translations before scaling under O2/g3 emit **67 words/frame0x68/
zero differences**. O2 leaves four differences; common-product locals enlarge
the frame to0x70. All controls have empty standalone diagnostics. This candidate
is **not installed or behavior/owner/padding qualified**; production remains
the placeholder. Ignored exploratory receipt:
`conker/build/game-scaled-matrix/measurements.json`.

Root README aggregate rows only. No sibling source/build/save, frozen Release,
runtime launch, host adoption, hardware/gameplay acceptance or push.
