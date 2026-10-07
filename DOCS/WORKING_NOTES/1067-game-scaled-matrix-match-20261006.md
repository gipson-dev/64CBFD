# Game Scaled Matrix Match

Date:2026-10-06. Baseline:`7d57a757`
([Note1066](1066-game-scaled-descriptor-match-20261006.md)).
Production:[game_16EE20.c](../../conker/src/game_16EE20.c);
caller:[generated_15F680.c](../../conker/src/game/generated_15F680.c).
Original Game decomp matching, not host adoption or gameplay acceptance.

## Retail Contract

**func_151424F4**:67 words /268 bytes, frame0x68,
VA151424F4..15142600, ROM16F9A4..16FAB0. Recover12 inputs:
`Mtx *output`, two float row factors, three float rotation arguments, three
float column factors and three float translations. No scalar result is
consumed by the original caller.

Call func_150A8050 on the local4x4 float matrix at SP+28. Set matrix[3][0..2]
to translations, retaining provider values at [0][3]/[1][3]/[2][3]/[3][3].
For each of the first three columns, multiply column factor by the row factor,
round to binary32, then multiply the matrix element and round again. Rows0/2
use row0; row1 uses row1. Preserve guMtxF2L(matrix,output) and the output pointer
through the provider's volatile register/FPR clobbers.

Do not reassociate into `(matrix element * column factor) * row factor`,
cache arguments before providers where retail reloads homes, or replace
provider-built untouched matrix elements with implicit identity constants.

## Caller ABI Correction

Original func_15133510 spans30 words at VA15133510..15133588,
ROM1609C0..160A38. It reads the eleven source words at +18..40, forwards all
12 arguments (last translation stored in the jal delay), and returns1.

The old local declaration called the output/first three input words s32 and
claimed a scalar return. Raw guest words happened to pass in the right registers,
but that declaration is incompatible with the recovered float callee. Correct
the local prototype, output pointer type, and first three source loads to f32.
With the new declaration, retaining integer loads would perform **numeric
int-to-float conversion**, not preserve their float bit images.

Both owners retain local declarations; no shared SDK/header rewrite.
Copied SDK compilation confirms **all31 caller-owner functions' raw bytes and
relocations unchanged**. Caller still emits its exact30 retail words; this
corrects the native type contract without another conversion/matching count.

## Direct Compiler Recovery

[Maintained driver](../../tools/experiments/game_scaled_matrix_candidates.py)
screens four source shapes times four actual-SDK profiles:16 controls, empty
standalone diagnostics. Explicit matrix updates with translations before
scaling under existing O2/g3 emit **all67 words/frame0x68 directly**.
O2 leaves four differences; translation-last O2/g3 has66 words/51 differences;
common-product locals enlarge the frame to0x70. No rejected shape is installed.
No guards, compiler/profile/frame rewriting, insertion/omission or padder change.

The compiler's function symbol is268 bytes. Standalone text has four final
zero alignment bytes; a copied whole owner has its next function there.
Actual padding keeps the symbol extent, not the unrelated section tail.

## Qualification

[Twelve maintained tests](../../tools/tests/test_game_scaled_matrix_match.py):

- **6480 paired guest cases**:five first-row/four second-row factors, three
  column sets, three translations, three provider matrices, three output
  aliases, provider external mutations and two stack phases. All67 words
  reached in both compiled/original bodies. Compare every ordered trace and
  full memory; SP/RA/saved GPR/FPR state survives poisoned provider/converter.
- **696 float-edge cases**:264 every-input/special-bit/stack-phase cases and
  432 first-row/column/provider pairs. Signed zeros, subnormals, overflow,
  infinities and NaNs retained as binary32 values. Separate-product rounding
  is preserved; no native NaN-payload, hardware FCSR/exception-mode claim.
- **48 guest-only home probes**:provider rewrites each of the12 argument homes,
  including redirected output and new scale/translation values. Rotation
  arguments have already been consumed and do not retroactively change.
  Native external access to private parameter homes is not claimed.
- **3372 actual32-bit native caller cases**:3240 factor/translation/provider/
  source-output-alias/mutation cases plus132 special-bit cases across all11
  float inputs. Check complete known matrix fields, provider arguments,
  conversion pointer, return1 and every external byte. Arithmetic NaNs are
  classification-compared; converters capture float payloads in this gate.
- **432 connected cases** execute all30 original caller,67 builder and115
  original guMtxF2L words. Bind all12 arguments, complete fixed output packing,
  ordered storage and saved state under aliases/mutations/two stack phases.
  Conversion is restricted to **finite, exactly integral, signed32-bit
  representable values after multiplication by65536**. Its cvt.w.s therefore
  does not require assuming a FCSR rounding mode. No general fraction/NaN/
  infinity/out-of-range converter acceptance is inferred.
- Actual padder retains all268 bytes and two R_MIPS_26 relocations, excludes
  the four-byte section alignment tail, and qualifies alternate call targets.
- Ten compiled negatives must change known output/call sequence on three valid
  mapped cases each:placeholder, missing provider/converter, wrong row/column/
  translation/provider arguments/output pointer, premature translation and
  reassociated product. No faults or compiler differences alone count.
- Native negative retains three integer loads under the corrected callee type;
  known provider arguments **and output matrix** change. This rejects numeric
  conversion rather than just checking a declaration string.
- Missing caller source, provider matrix or conversion output fails strict
  mapped memory gates. No hardware fault/native out-of-bounds claim.
- Copied builder owner:93 functions, target raw bytes/relocations equal the
  standalone body;92 neighbors, original pool and two warnings unchanged.
  Copied caller owner:all31 raw functions/relocations/pools and two warnings
  unchanged. Tests reconstruct only these edited bodies/types in copies,
  without requiring historical Git/ignored fixtures.
- Production binds both typed sources, exact67-word builder, exact30-word
  caller, seven retained neighboring slots and all10809 unchanged guard rows.

Rotation func_150A8050 remains a bounded model; its production C is still
empty and its original body is not executed/restored here. Native converter
fixtures likewise use a bounded payload capture, not the actual SDK converter.
The separate connected gate executes the full original converter only in the
explicit finite/exact domain above. This proves retail instruction identity
and the scoped ABI/storage contract, **not full native rendering or gameplay**.

Harness correction:the initial ten-test bundle failed two extent assertions
in37.616 seconds. It incorrectly treated the section's four alignment bytes
as part of the function and compared them with the next whole-owner function.
Correct the symbol size and slices to268; both affected gates pass in13.712
seconds. No production source change was needed for those harness corrections.

## Production Verification

Explicit `make -j4 VERSION=us build/conker.us.elf` passes. Against7d57a757,
**only func_151424F4 changes across6059 slots**; addresses/extents stay fixed.
Target SHA-256:
`eb508b7dcde22062a6f8772533e276683f9b5b478efedc52751221008d2fb5ec`.
Caller30, dispatcher100, actor45, context57, checked caller37, updater80,
random descriptor96 and scaled descriptor80 words remain exact.
Protected .init/.init_data/.debugger/.game_data addresses/hashes unchanged;
all720 Game-data owners /189088 bytes match, zero differing owners/bytes.
Both builder/caller owners retain two warnings each, code/statement/caret
unchanged, no new warnings. Full build is not warning-free.

All10809 guard rows unchanged, canonical SHA-256:
`e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a`.
Conversion remains5464/6042 total and4791/5321 Game; byte coverage stays85.57%
total/84.89% Game. Exact total **3342/5464 (61.16%)**, Game
**2669/4791 (55.71%)**, **2122 different**, zero drift. Init492/492 and
Debugger181/181 remain exact. Complete-ROM checksum not claimed.

All77 focused post-link tests pass in531.767 seconds, no skips/errors/failures:
12 matrix,11 scaled descriptor,11 random descriptor,11 updater, eight actor,
eight context,11 dispatcher and five actual-padder tests. Documentation:
49 documents/3546 relative links/zero broken. Project tool, scoped Python
syntax and `git diff --check` gates pass. Ignored receipts:
`conker/build/game-scaled-matrix-test/`.

## Next Function

Continue **func_15142600**,142 words /568 bytes, frame0xB8,
VA15142600..15142838, ROM16FAB0..16FCE8. Still a placeholder; no candidate
installed or behavior qualified in this checkpoint.

1. Recover twelve inputs:output pointer, first/second row factors, three column
   factors, start point and end point. Caller func_150B9D14 at VA150B9D14/
   ROME71C4 forwards row factors from source+18/+1C; columns+2C/+30/+34,
   start+38/+3C/+40 and end+20/+24/+28. Its jal/delay is VA150B9D6C/ROME721C.
   The local declaration/first three loads currently have the same raw-word
   type issue just resolved for the scaled builder; qualify that caller too.
2. Recover direction=(end-start) normalized by reciprocal sqrt of the
   separately rounded three-square sum. Build horizontal left from
   (directionZ,0,-directionX), normalize it, then form/normalize direction
   cross left. Preserve the observed order, not an assumed view-matrix API.
3. Apply three column factors and two row factors, retaining separate float
   rounding and original saved F20/F22 lifetime. Set start-point translation,
   zero three fourth-column fields and final1; retain guMtxF2L.
4. Screen vector/array/scalar-local declaration and normalization shapes under
   actual SDK profiles. Original142-word frame0xB8 is required before
   considering any normalization or installation.
5. Qualify direction signs, asymmetric factors, degenerate coincident/vertical
   points, signed zeros/float edges, sqrt/divide behavior, complete caller,
   actual padding/owner lifetime and all-slot/data/guard audit. Do not add a
   new degeneracy fallback absent from retail or infer FCSR/render acceptance.

Initial scratch screen:16 vector-local/declaration-order/profile controls.
The in-place horizontal normalization under O2/g3 emits143 words/frame0xC8/
138 differences, versus retail142/frame0xB8; matrix-first declaration order
does not improve it. Separate normalized-horizontal locals grow to158 words/
frame0xD0. O1 controls are200 words. All standalone diagnostics are empty.
None is installed or behavior qualified. Next compiler pass must recover
the retail private-vector placement and F20/F22 lifetime, not patch an excess
word or frame. Ignored receipt:
`conker/build/game-oriented-matrix/measurements.json`.

Root README aggregate rows only. No sibling source/build/save, frozen Release,
runtime launch, host adoption, hardware/gameplay acceptance or push.
