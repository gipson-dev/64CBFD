# Note 2589: Map-trail curve guarded byte match

Date: 2026-11-20. Consumer baseline `4282ae6a9335b484223bb94266777c215ccba6eb`;
tools baseline `a9380e4a4e9c800ab6c310bd73f909d2c894cdad`.
Qualified tools commit: `b11c48306409daba33cd457723842f0278967da8`.

`func_15106214` is restored from GLOBAL_ASM to complete semantic C. All **168
words / 672 bytes** match retail after **six checked normalization rows**.
Raw C already emits 168 words; its 136-byte frame becomes the original
**128-byte frame**, and an independent four-word opening schedule is restored.
No instructions are inserted or omitted. Floating arithmetic, public access
order, call arguments and relocation bindings are unchanged.

Fresh production recount: **4,575 / 5,526 (82.79%)** total, **3,902 / 4,853 (80.40%)** Game, zero drift and 951 different. Converted C: **5,526 / 6,048 (91.37%)**, 86.52% of bytes; Game **4,853 / 5,327 (91.10%)**, 85.92% of bytes. Init 492/492 and Debugger 181/181 remain exact. **123 more matches** are needed for 85% at the current denominator, which ASM conversions can increase.

## Interface and recovered curve sampling

Owner: `conker/src/game/generated_133190.c`; VA 0x15106214..0x151064B4,
ROM 0x1336C4..0x133964. The original assembly remains unchanged. Both known
callers already use `void(MapTrailRecord133190 *)`: the constructor
`func_15105CE0` and updater `func_1510608C`. Their direct JAL literals occur
at ROM 0x1332BC and 0x1335D4; there are no aligned literal target pointers.
This census does not exclude arbitrary computed callers or execute full parents.

The record's trailing array begins at +0x88. Each 52-byte segment contains a
parameter, position, tangent, normal and binormal. `func_151061E0` now expresses
its actual interface as `MapTrailSegment133190 *(void *)`; its original pointer
addition emits exactly the same words and bindings as the previous integer
declaration. No broad header repair is required.

The curve builder calls that accessor even when the count is nonpositive.
It caches the reciprocal after the call and starts its parameter at that
increment. For each interior segment, it calls all eight cubic basis/derivative
providers in order, then reads the four control points and computes the
position and tangent. Every multiply and add retains its retail single-precision
order. The frame provider receives the three cached addresses at segment
+0x10/+0x1C/+0x28. Its zero return clears only the normal and binormal; other
provider edits are retained. The count is reloaded after each call, whereas
the parameter increment remains cached and runs even after the final segment.

## Six-word derivation

Natural sum, loop and declaration screens reduced the initial 65 differences
to six. The selected C preserves all original saved roles, spill homes and
floating instructions. The derivation checks the complete raw fingerprint,
confirms all 32 explicit private accesses stay inside the retained 128-byte
frame and confirms no private address is materialized for a callee.

It removes eight unused frame bytes by changing the opening/closing SP
adjustments. A closed permutation moves the index initialization, empty-count
branch, FP delay-slot move and cursor assignment into their original order.
The branch displacement increases by one to retain its target. The cursor
assignment becomes conditional on a nonempty count; its saved entry value is
restored on either exit. Every one of the 168 source origins appears once.
No output array is copied from the ROM, and no FP or public-access word is
rewritten. The normalized raw bytes **and bindings** equal original assembly.

Private storage is disjoint from public objects. Callees may modify public
arguments and outgoing homes while preserving o32 saved registers, and cannot
inspect unpassed private locals or implementation PCs. The frame/opening
relation preserves the complete arithmetic/call sequence under that normal
execution contract. It does not assert raw fault, timing or hardware equivalence.

## Fresh qualification and linked audit

Six tests pass before and after installation in each tools configuration.
All **336 imported Python fingerprints** agree; the isolated second overlay
uses 341 matching sibling files, 679 primary fallbacks, five task files and
one empty bootstrap. The real dirty sibling retains its HEAD, full status
and 345 dependency hashes.

The independent MIPS contract passes **320 cases per stream** and covers all
168 words of both raw and retail routines. It checks empty/negative counts,
one/two/four-segment loops, both stack phases, all eight live weights, count
changes, cached increments, late control-point reads, frame success/failure,
provider edits and complete public output/call snapshots. Four effective
instruction mutations reject position, step, fallback and stride errors.

Native SDK32 passes **160 cases each at O0, O2 and O3**, with strict aliasing
and UBSan. It checks the complete record, every segment and trailing guards,
FP argument bits, frame snapshots and call order against independent expected
data. Three compiled source mutations execute and fail. Providers are bounded
models with distinct finite outputs; original polynomial/frame provider bodies
and full parents are not executed by these checks. This is not gameplay or
hardware acceptance.

The other **36 raw functions and bindings**, including the typed accessor,
and all constant pools remain unchanged. Both independent padders reproduce
the entire predecessor object byte-for-byte. The actual five-command mixed
Make recipe retains O2/g3 and existing diagnostics. Six guard rows append to
the exact previous CSV byte prefix; no historical row changes.

Production Make, fresh recount and `make tools-check` pass. All **6,051 named
function slots** and **189,088 protected data bytes** remain fixed. The complete
ELF is identical to the frozen independent prediction, with zero exclusions:
`d428a774da73a7a019242548481f707cc7e7c6d670c233af41189771495dfb04`.
Only this function changes from ASM to C in the progress CSV. Unchanged
neighbor-suite receipts are reused by source/object identity, not counted fresh.

Graphify native update remains fail-closed on the smaller extraction. The
scoped six-file AST merge and explicit note/original-ASM references retain
existing IDs; commit-hook completion and prior qualification metadata are
checked before sealing the checkpoint. This is not full-corpus re-extraction.

Codex owns the work; zero Claude calls. Local commits only; no push, host,
save or Release work. Continue with `func_15106610`, the 106-word sample
updater in the same owner, original frame 112. The 85% goal remains active.
