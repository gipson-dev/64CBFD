# Trigonometric Camera Output Direct Match - 2026-11-08

`func_150E41C0` now emits all **78 words /312 bytes directly from semantic C**,
with its original **0x40 frame** and **zero new guards**. The complete owner,
both padders and actual Make output agree. The literal full-ELF prediction
changes **249 bytes**, with zero exclusions or metadata permutations.

Production: Total **4,266 /5,513 (77.38%)**, Game **3,593 /4,840 (74.24%)**,
Init **492 /492**, Debugger **181 /181**, zero address drift. There are
**1,247** different converted functions and **145** more exact functions
needed for4,411 /5,513 and the active80% goal. Conversion denominators and
the progress CSV remain unchanged.

## Recovered interface and floating-point sequence

Owner `conker/src/game/generated_111670.c`, original `asm/111670.s`.
VA **0x150E41C0..0x150E42F8**, ROM **0x111670..0x1117A8**.

```c
void func_150E41C0(void);
```

Reuse the existing `struct108` camera layout and SDK math declarations.
D_800DBFF0 points to the camera; D_800D99F0 is the three-halfword output.
The only direct caller ignores the result. The literal emitted MIPS also
retains V0's final output-address value; portable C does not expose that
incidental register as a return contract.

Snapshot/truncate float fields+0x2F8/+0x2FC/+0x300 into signed32 X/Y/Z
before any calls. Cache angle+0x398 in F20, call sinf then cosf using the same
argument bits, and compute vertical=500*sine and horizontal=-500*cosine.
After those two calls, reload the live camera pointer and its angle+0x3A0;
cache it across another sinf/cosf pair. Earlier helper mutations cannot change
the captured integer coordinates, but camera retargeting before the late
angle read is observed. The second cosine must use its cached angle even
if the second sine provider mutates or retargets the camera again.

Retain the original single-precision operations, including explicit zero:

```text
X = trunc(float(savedX) + (0.0f + horizontal * secondSine))
Z = trunc(float(savedZ) + (horizontal * secondCosine - 0.0f))
Y = trunc(float(savedY) + vertical)
```

Store the low16 results at output offsets0,4,2. The shared output address,
operation ordering, signed conversions, helper homes and saved F20/F21 pair
are literal retail. The independent model rounds after each float primitive.

## Source recovery and complete owner

The first scalar draft has the correct78-word/frame0x40 shape and a literal
43-word opening match, but IDO folds the zero arithmetic and changes the tail.
Initializing the zero local before the helper calls preserves the original
add/subtract operations. Updating the named integer coordinates before the
three stores recovers the shared V0 output-address form and the exact schedule.
No volatile accesses, forced instruction text, extra data pools, guards or
compiler-profile changes are used. The isolated and complete-owner bytes
and all10 binding sites agree; raw SHA256
`651429e7a352566b8269954498365931f232d56dbbce7a3a72b900a6c0577cdc`.

Frame homes: saved F20/F21+0x10, RA+0x1C, sine+0x24, horizontal+0x28,
vertical+0x2C and captured Z/Y/X+0x34/+0x38/+0x3C. The zero and angle locals
need no stack stores. The existing O2/g3/MIPS2/O32 profile stays unchanged.
Actual Make's three commands compile, pad and assemble the identical owner.
Both padders preserve all **nine functions /eight neighbors**, pools and the
exact register-mask union. No exported interior labels move. Diagnostics0.

## Behavior and caller qualification

Six focused checks pass before/after installation in both tools copies,
sequentially with exact source/dependency fingerprints:

- **2,215 guest cases** cover fractional/negative coordinates, signed zero,
  small float payloads, cached angle arguments, helper mutations, camera
  retargeting, private-home changes and three code/data/helper layouts.
  Independent complete memory and literal original/C states agree. Every
  one of the78 instructions executes; F20/F21 and all callee-saved FP state
  are preserved, including non-arithmetic saved payloads.
- **72 alias cases** cover output overlapping camera data, the global pointer
  word, captured-coordinate homes and the late vertical home. The model
  preserves the first output store before the final vertical reload.
  Synthetic aliases use a bounded finite conversion domain; they are guest
  address-model probes, not portable C overlap/fault claims.
- **112 interrupted-access cuts** fire and compare literal states, including
  the paired FP save/restore, reads/stores and helper-boundary effects.
- **1,490 native32 cases per O0/O2/O3 profile**, trapping UBSan, use real typed
  camera fields, measured offsets, whole-object/output canaries and independently
  precomputed numeric results and argument bits. All **12 semantic controls**
  are effective, including stale camera/angle reads, late coordinate snapshots,
  missing initial truncation, wrong gains/signs/factors and missing/wrong stores.
- Three independent GNU links and12 rebased executions qualify all10 binding
  sites and high/low carry layouts. All78 word,10 binding,72 register-metadata
  and four entire-image corruption controls reject changes.

The pristine aligned census finds one direct call at ROM **0x1119D0 /
VA0x150E4520**, no aligned pointers and no interior entries. A symbolic scan
of all original assembly finds only this call and the function definition.
The complete original15-word **func_150E4514** runs connected in **448 cases**.
It saves its incoming signed argument, calls this routine without arguments,
reloads the saved argument, divides by30, then submits the signed quotient to
func_150E42F8. That followup is a bounded provider with caller-register/home
clobbers. The caller ignores V0 from this target; its complete literal states
and independently predicted memory/calls agree.

Numeric tests keep every float-to-integer conversion finite and in signed32
range. NaN/infinity/signaling angle payloads are controlled-provider ABI probes;
they do not validate actual sinf/cosf behavior for those inputs. FP exception
flags, FCSR/rounding modes, exact math-leaf accuracy, the large followup body,
hardware and gameplay are not newly qualified. The direct instruction match
is separate from those bounded execution/model claims.

## Literal image, production and preservation

The independent predictor replaces only the312-byte target body and its
12-to312-byte symbol extent: **249 changed bytes, zero exclusions**. All
**6,052** disassembled entries retain their addresses; every other body,
extent and metadata byte stays fixed. Protected data is exact across
**720 owners /189,088 bytes**, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Production compiles only this owner and equals the complete prediction.
Makefile, data bindings, guard manifest and progress CSV stay unchanged.
The pre-existing full-ROM checksum mismatch (make all exit2) and duplicate
generated_12D630 recipe warning remain separate from the successful target
compile/link/recount. Shared smoke checks are fresh in both tools copies;
three unchanged helper regressions per copy are reused by exact fingerprints.
The sibling tools' **2,434** dirty paths remain preserved. **102 frozen inputs**
pin original owner/caller, headers, layout, manifest, ROM and compiler inputs.
Baseline consumer `5afd9dd423e7cbc22f1f3e9ac406220dc0c33885`, tools
`395ff89e3c67994e932d2e8aaa27348190b1bee3`. Claude calls: **0**; local compiler,
ABI, execution and literal-image evidence resolve the routine.

ELF SHA256: `60d00a56e5299d1abe61ad43dade8e0ce950362da17880774cb9917872466e73`.
Binary SHA256: `19a4ebda0d608dd3abac90aba17de4068eb7ab868daa81e1abbc53eb977eafbc`.
Owner SHA256: `ea8ff9413cc7d7825a093fde9d64d9ec21dffd11a7407b75ce4810a25c96e324`.
Guards SHA256: `9140ca7fb99506fc43c7be4e910d58eeee9f8bcc21f8743f314b59d7dd3875f8`.

## Resume boundary

Next: **func_150F7E20**, an uncredited78-word sine-driven effect updater in
`conker/src/game/generated_124920.c`, original `asm/124920.s`.
VA150F7E20..150F7F58 /ROM1252D0..125408, frame0x28. Audit the one-pointer
interface, caller return consumers, constant/data bindings and owner profile.

Convert object float+0x128 times D_800A1BD8 to an unsigned32 word and store its
low byte at+0x5C. Preserve the complete CFC1/CTC1 unsigned-conversion fallback,
rounding setup, invalid/negative handling and restored FCSR; do not replace
it with a signed cast. Call sinf(object+0x12C) while saving/reloading the live
incoming object home. Block=object+0x110; sine*block+0x28 plus block+0x24
is written to object+0x30 and+0x2C. Advance block+0x1C by block+0x20 times
the global delta D_800BE9A4 and pass that float to func_15144B68. Save the
block pointer across the call and store the returned phase. Reload delta,
decrement block+0x18, store/reload it and return !(remaining<0.0f), preserving
NaN and signed-zero comparison behavior. Complete all qualification gates
before credit; unsigned FP conversion needs an explicit model boundary.

Receipts: `conker/build/game-trigonometric-output-150E41C0-match/`.
Tools commit before the consumer pin. The scoped Graphify refresh retains
existing unscanned nodes with audit evidence, not full-corpus extraction.
Host Release stays frozen. The80% goal remains active.
