# Region emitter private recovery, frame and inductive proof

Date: 2026-11-16. Continue `func_151A5660` after the accepted
[attached-point callback](2504-game-attached-point-emission-callback-full-recovery-and-guarded-byte-match-20261116.md).
This is a **private recovery checkpoint, not a new C match**. Production
`conker/src/game/generated_1D2B10.c` still contains its zero-return placeholder.
No target guard rows, compiler profiles or tools pin have changed.

Accepted progress remains **4,526 / 5,514 (82.08%) total**, Game
**3,853 / 4,841 (79.59%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift and **988** still different. **161** further matches are
required for at least 85%; that goal remains active. The root README keeps
its accepted aggregate rows and receives no function narrative.

## Target and recovered behavior

Owner `generated_1D2B10` has 15 functions and 14 neighbors. The target occupies
**403 words / 1,612 bytes**, VA **0x151A5660..0x151A5CAC**, ROM
**0x1D2B10..0x1D315C**, with a **0x108 frame**. Original body SHA-256:
`d899dd1968e9cfb89b1c45972a413f119da2d41f03c06eb0ad10a63cc021205a`.

The complete private `void func_151A5660(u8 *owner)` samples a source region
and submits effects repeatedly while its accumulator exceeds one. A null
source sets the signed owner lifetime at +0xE to -1. Source byte +0x14 equal
to one, a rejecting optional view mask, or an accumulator at most one causes
an early return. The accumulator update retains the original two multiplies
and addition, including the mutable time-step global.

Four source modes preserve distinct radial, rotated rectangular and direct
coordinate sampling, signed halfword coordinates/extents, the byte angle,
optional height query, randomized lifetime/value/byte fields, six-argument
submission, and the post-submission accumulator reload/decrement. Constant
packet fields are initialized once outside the loop. Providers can change
state and previously exposed packet/query ranges between calls; the proof
does not assume those values remain fixed.

The packet is 72 bytes, with **69 initialized bytes** and indeterminate
padding at **0x35..0x37**. The query vector is 12 bytes. The source descriptor
is 24 bytes and the recovered payload view is 112 bytes. Unknown field codes
retain neutral local names. The submission interface is pointer-returning,
with `u8 / u8 / s32 / u8 / s32` arguments after the packet pointer.

The sole aligned target literal is **D_8008A4E8[6]**, VA **0x8008A500**, ROM
**0x22EFC0**. Its original 45-word parent `func_15149264` and the view-mask
and height wrappers are already literal production matches. This is static
caller evidence; this target's connected dispatcher execution is still open.
The downstream `func_15149550` remains a production stub and is not credited
as restored by this study. Its original 186-word body consumes the packet
through offset +0x44. The actual producer of this callback payload remains
an open audit; adjacent unrelated constructors are not treated as that producer.

## Natural frame and instruction fitting

Private artifacts are in `conker/build/game-next-151a5660-private/`.
The initial full semantic C draft emitted **400 words / frame 0xE8**.
Separate, used cosine/sine/radius temporaries for each mode restore the
original saved floating-register lifetimes and the complete **0x108 frame**.
No unused matrices, oversized query/packet views or artificial padding are used.

A named switch selector and meaningful declaration order restore the packet
to **SP+0xBC** and the query vector to **SP+0x6C**. A byte angle restores the
radial random-word scheduling shape. Two case exits snapshot the query flag
before the shared query entry. A named byte height result replaces a redundant
named floating product; its narrowing is independently justified below.
These are fitting implementation choices, not claims about historical names
or the original source spelling.

The selected **v37** whole-owner compile emits **403 words / frame 0x108**,
preserving all 14 neighbors and normalized pools, without diagnostics.
**356 words are already literal; 47 still differ.** The final 100 words from
offset **0x4BC** through the epilogue are literal. Candidate raw SHA-256:
`02fc65e9c06e740bd1e5dc1bce5dad2062dfbcab08e0a7c2ce546bdd38f597dc`.
No proposed 47-word normalizer has been installed or credited.

Owned read-only compiler traces pass for v2, v7 and v37. The selected trace
has UGEN frame events **0 -> 64 -> 88 -> 264**, comprising **64 saved bytes,
24 outgoing bytes and 176 local bytes**. Normal and observed code, relocation
bindings and pools agree; all owned producers and driver terminate normally.
Both unfired-frame and missing-producer-exit controls reject. This supports
the local-allocation explanation for the old 32-byte gap; it was not a missing
saved-register area. Trace receipt: `frame-observation/v37/summary.json`.

## Height result range and symbolic qualification

`height_return_range.py` performs conservative finite-set GPR dataflow over
complete original routines, with unknown ordinary loads/FP conditions and
opaque o32 call clobbers. Original and current production bodies are literal
for all three routines:

| Function | Words | Normal return values |
| --- | ---: | --- |
| `func_1504697C` | 161 | 0, 1 |
| `func_15047004` | 43 | 0, 1, 2 |
| `func_15046C80` | 32 | 0, 1 |

The wrapper's byte result is therefore lossless on normal returns. Changing
one secondary return from one to **256** expands both its result range and
the connected wrapper's range to include 256; the control is effective.
This is a return-range proof, not a proof of these callees' complete effects.
`caller-audit-v2.json` also corrects the leaf view-mask frame to zero; the first
audit had incorrectly interpreted its first instruction's immediate as a frame.

`prefix_proof.py v37` proves **seven opening paths**: five return paths and
two loop-entry paths. It compares public effects/read epochs, ordered FP/FCSR,
the private frame and callee-save restoration. Expiry-width, disabled-byte and
accumulator-operation controls all reject.

`iteration_proof.py v37` proves **42 inductive iteration paths**, starting
with arbitrary dead scratch roles, arbitrary retained packet bytes and the
original saved-register invariant. Both continuations and returns preserve
the original helper ABI, full private frame at providers/exit, public aliases,
retained-range mutations, and ordered effectful FP/FCSR transitions. Signed
halfword sums/differences fit exactly in binary32; their register-only
conversions are compared as complete operand multisets within each public
memory epoch, rather than incorrectly modeling them as inexact operations.

Two raw multiplies at **0x264** and **0x298** have commuted physical operands.
Only those two words are projected to original operand order for this proof;
the remaining 45 differing words must agree through instruction execution.
The unprojected multiply order, wrong outer fallback coordinate, zero height
mask, loop addition instead of subtraction, and changed lifetime divisor all
reject. A consistent T8/T9 reallocation still passes all 42 paths. Latest
receipt: `iteration-proof-v37-inductive.json`.

The normal unsigned-division domain excludes zero divisors. Abstract FCSR
transitions include the compiler's unsigned-conversion fallback branches.
No physical FCSR/trap behavior, memory-fault state, native exceptional-value
behavior or gameplay acceptance is claimed. The unvisited iteration offsets
are the unreachable conversion copy at **0x204**, retail's duplicate dead
fallback store at **0x4AC**, and excluded BREAK instructions **0x55C/0x5E0**.
Raw has no duplicate dead store at 0x4AC. It visits 333 iteration words and
retail 332; equal instruction counts are not being substituted for equivalence.

## Resume and remaining gates

Production baseline is consumer **954874613c924141883acbe6b6eed512074aacf7**,
tools **13598c535d27e4e40acef2ca6972e90665bdb92c**, and ELF SHA-256
`982f0f31f23210afe687e32313befc8d64462b477eb5d1498c511a4a238b0338`.
The 1,360 frozen production inputs were reverified unchanged during this study.
Retain original snapshots and the complete failed/successful source screens.

1. Finish independent finite guest and SDK32 native O0/O2/O3 execution for all
   modes, threshold/boundary inputs, repeated submissions, aliases and provider
   mutations. Include effective source controls and both stack phases. Keep
   the three packet padding bytes outside defined native output comparisons.
2. Qualify the exact 47-word guard manifest, both production padders, all owner
   neighbors/pools and independent code/data rebases. Preserve all operations;
   no insertion or omission is needed by the selected shape. Explicitly retain
   the two ordered-multiply and normal-return range boundaries.
3. Execute the original slot-6 dispatcher against the callback. Audit the
   actual payload producer and record the still-unrestored submission callee
   separately. Reconcile the proof with fresh guest/native observations.
4. Run both tools copies with sealed imports, actual production Make and the
   independent strict whole-image comparison. Audit every affected object,
   function/address, guard row and protected byte; run required shared checks.
5. Only then adopt, recount the actual ELF, refresh Graphify with old-ID
   retention, update aggregate status, and commit tools before the consumer.

One optional packet-only Claude Pro analysis was attempted with tools disabled,
safe mode, strict empty MCP and no session persistence. Local response saving
failed with a Windows text-encoding error. No answer was retained or used;
there was no second call. Its failure and packet fingerprint remain in the
private study. All findings above come from local code and measured receipts.
