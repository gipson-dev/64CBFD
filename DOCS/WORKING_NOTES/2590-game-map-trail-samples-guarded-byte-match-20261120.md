# Note 2590: Map-trail sample updater guarded byte match

Date: 2026-11-20. Consumer baseline `498df13298218465e19215a8a8e178da9cef1a18`;
tools baseline `b11c48306409daba33cd457723842f0278967da8`.
Qualified tools commit: `0c8f6368ae986e106c72b2128d55aeb3791edb52`.

`func_15106610` is restored from GLOBAL_ASM to complete semantic C. All **106
words / 424 bytes** match retail after **50 checked normalization rows**,
including one omission row. Raw C emits 107 words with the original **112-byte
frame** and exact exposed float homes at **SP+0x50/SP+0x54**. A duplicated
loop-entry cursor copy is shared; no arithmetic or public data access is lost.

Fresh production recount: **4,576 / 5,527 (82.79%)** total, **3,903 / 4,854 (80.41%)** Game, zero drift and 951 different. Converted C: **5,527 / 6,048 (91.39%)**, 86.54% of bytes; Game **4,854 / 5,327 (91.12%)**, 85.94% of bytes. Init 492/492 and Debugger 181/181 remain exact. **122 more matches** are needed for 85% at the current denominator, which ASM conversions can increase.

## Interface and sample behavior

Owner: `conker/src/game/generated_133190.c`; VA 0x15106610..0x151067B8,
ROM 0x133AC0..0x133C68. The original assembly remains unchanged. Both known
callers use `void(MapTrailRecord133190 *)`: constructor `func_15105CE0` at
ROM 0x1332C4 and updater `func_1510608C` at 0x1335FC. There are no aligned
literal target pointers; this does not exclude arbitrary computed callers.

The builder retains the results of both accessors, copies the first and last
control points to output indices 0 and count+1, then offsets each interior
curve position along its normal and binormal. Each iteration keeps the integer
PRNG result across a separate float PRNG call, reads the live width afterward,
and passes its low eight angle bits and scaled radius to `func_15143874`.
The confirmed helper signature is `void(s16, f32, f32 *, f32 *)`.

The two float locals remain alive throughout the routine. Their exact homes
are exposed to the polar helper and may be retained and changed by later
providers. After the helper, each coordinate is `(normal*first + binormal*second)
+ position`, retaining the retail load/store and FP operation order. Count is
reloaded after each sample. The signed modular count+1 initial gate, cached
array results, final cursor increments and endpoint stores are preserved.

## Checked register and loop derivation

The first pointer loop collapsed two cursors and emitted 102 words/frame96.
The selected indexed loop keeps the required current/cursor lifetimes and
emits 107 words/frame112 with the exact passed homes. The derivation checks
its complete raw fingerprint, closes a body-only S2/S3/S4 role cycle while
preserving entry saves/restores, and moves three independent index/cursor
increments past FP work. Static checks show that crossed instructions do not
read or write those induction registers.

The taken loop edge's repeated output-cursor copy is merged with the existing
loop-entry copy. The branch becomes ordinary BEQ and its delay slot receives
the cached segment increment. The initial exit displacement is adjusted for
the folded word. A complete origin map retains every source instruction
except the duplicate source origin94; no instructions are inserted. One
commutative radius-multiply operand order is restored under the ordinary finite
FP contract. The private SP-relative access sequence and passed pointers are
identical. The result's raw words **and relocation bindings** equal original
assembly, without reading the ROM to generate the normalized body.

CSV encoding is positional: 49 replacement rows and one final omit row emit
the 106-word derived stream. The closing SP adjustment is moved into its proper
output position; the logical omitted operation is the duplicate cursor copy,
not the frame restoration. The complete previous CSV byte prefix is retained.

## Fresh checks and original providers

Seven tests pass before and after installation in each tools configuration.
All **343 imported Python fingerprints** agree. The isolated second bundle
contains 1,038 files: 347 matching sibling files, 684 primary fallbacks, six task
files and an empty bootstrap. The real dirty sibling retains its HEAD, complete
status and **351 dependency hashes**. Conflicting sibling work is not overwritten.

The independent bounded MIPS contract passes **768 cases per stream**, covers
all **107 raw / 106 retail words**, and exercises all 256 angles. It compares
the complete 112-byte frame plus 24 incoming bytes, all public output, ABI
traces and exposed float bytes. Retained pointers are modified by subsequent
integer/float providers; width, segment fields and count change at the relevant
calls. Five effective instruction controls reject output-home, angle-width,
radius-operation, point-stride and endpoint errors.

Native SDK32 passes **384 cases each at O0, O2 and O3**, with strict aliasing,
UBSan and opaque provider functions. It verifies both endpoints, all samples,
record/segment edits, trailing guards, angle/radius bits, call order and retained
float-pointer identity/values. Three compiled source mutations execute and fail.
The first uninitialized float representation is inspected only as guest bytes;
native retained-value reads begin after the helper has initialized both floats.

A further **548 cases** execute all **108 original helper words**: both
accessors, the two handwritten 64-bit PRNGs, polar helper and folded table
lookup. Every lookup angle is exercised. The seed, scale factor and 65-word
lookup table are checked against original bytes; an independent seed/lookup
reference agrees with public output and complete caller-frame bytes. These
connected checks use no opaque providers. Full parent, raw fault, nonfinite
FP, hardware and gameplay acceptance are outside these checks.

## Owner and production closure

All **36 other raw functions and bindings** and constant pools remain fixed.
Both independent padders reproduce the entire predecessor owner object.
The actual five-command mixed Make route retains O2/g3 and existing diagnostics.
Production Make, fresh ELF recount and `make tools-check` pass. All **6,051
named function slots**, addresses and **189,088 protected data bytes** remain
fixed. The **complete ELF** equals the frozen independent prediction, with
zero exclusions: `d428a774da73a7a019242548481f707cc7e7c6d670c233af41189771495dfb04`.
Only this function changes from ASM to C in the progress CSV. Unchanged neighbor
receipts are reused by source/object identity rather than reported fresh.

Graphify native update remains fail-closed on the smaller extraction. A scoped
seven-file AST merge, explicit note/original-ASM references and observed
commit-hook retention preserve existing IDs and preceding qualification metadata.
This is not a full-corpus semantic re-extraction claim.

Codex owns all changes; zero Claude calls. Local commits only; no push or host,
save or Release work. Continue the 85% total matching goal from the new frozen
checkpoint; the next owner function to audit is `func_151067B8`.
