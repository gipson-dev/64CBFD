# Game quaternion rotation matrix direct C match

Date: 2026-11-15. `func_1504A140` is adopted as semantic C in
`conker/src/game/generated_770F0.c`. All **89 body words / three alignment
words** are byte-exact, with the original **0x48-byte frame** and **F20/F21
save at SP+8**. The slot remains `0x1504A140..0x1504A2B0`, ROM
`0x775F0..0x77760`. The routine takes two float-array pointers and returns
void. It reads a scalar-first quaternion and writes the rotation part of a
4x4 matrix, preserving translation elements **12, 13 and 14**.

This closes the private work in
[Note 2409](2409-game-quaternion-matrix-private-screen-20261114.md).
The complete body emits **directly from ordinary C**, with **zero guards,
zero bindings and no compiler-profile, Makefile or header changes**. The other
three owner functions and normalized pools are preserved; owner **2 / 4 exact**.
The matrix-to-quaternion and interpolation placeholders remain separate work.

## Source shape and ordered floating-point recovery

The old named-input scalar form uses a 0x68 frame and emits 86 words. Four
input temporaries unnecessarily keep more saved floating registers alive.
Direct quaternion reads with the thirteen semantic coefficient locals recover
the original **89 words / 0x48 frame** under the existing **O2/g3** profile.
Other optimization/debug profiles and volatile-array shapes do not recover
the retail body and are not adopted.

Matching the frame alone was insufficient. The first direct-input form still
reordered the norm's floating operands after compilation, differing in all
nine computed rotation expressions. Eight source orientations of the same
parenthesized norm were screened. One emitted the exact original ordered
expression `q3*q3 + ((q0*q0 + q1*q1) + q2*q2)` even though its C source writes
the outer operands in the reverse order. Therefore acceptance is based on the
emitted operations, not a presumed relation between textual operand order and
instruction operands.

That form had **25 scheduling words** left. Assigning the nine rotation cells
in natural row order, followed by the four homogeneous-coordinate constants,
recovers **all 89 words**. No permutation guards or arithmetic substitutions
are needed. The source comment, `quaternion` / `matrix` parameters and named
scaled components/coefficient products make the recovered behavior explicit.

An independent symbolic executor compares ordered floating expressions,
arithmetic-operation multisets, complete private-memory results and the ordered
memory-access trace. All agree, with **no commutative rewrites**. Both streams
read the four input floats before any output write. Three altered arithmetic,
store/stack words are rejected. Exact instruction identity additionally fixes
the instruction schedule, saved-register lifetime and return delay slot.

Raw/direct body SHA-256:
`081a86830124ac6b3bae2579c8ebc51321dc47cefc1d727f8b26b03e5788d206`.

## Guest and native qualification

Fresh original/compiled execution passes **3,640 finite guest cases** and
**1,208 exceptional modeled cases**, with all 89 instructions visited.
Seven input/output arrangements include separate buffers, in-place operation,
partial overlaps and input data in the preserved translation area. Complete
public bytes are compared, including untouched storage and both valid stack
phases. **176 fired access-cut prefixes** compare modeled GPR/FPR, memory,
access trace and instruction/delay context. Three effective instruction
controls reject wrong norm arithmetic, division and output storage.

Exceptional cases cover signed zero, zero norms, subnormal boundaries, overflow,
infinities and quiet/signaling NaN payloads. NaN propagation is tested under
two explicit rules: left or right NaN operand wins with its quiet bit set.
The equal ordered expression graphs do not assume one of those rules to make
the two streams agree. These are bounded low-word guest models; hardware NaN
selection, FCSR traps/flags and full 64-bit FPR semantics are not claimed.

Native32 runs the actual semantic C at **O0/O2/O3**, with **326 cases per
profile**, undefined-behavior traps and all **512 public bytes** checked.
Finite nonzero norms include ordinary, small/subnormal-intermediate and large
finite inputs, plus all seven valid buffer-alias forms. Four compiled C
controls fail in each profile: wrong scale, wrong off-diagonal sign,
overwriting translation and using the wrong quaternion component.
Zero/nonfinite norms and implementation-specific NaN payloads are outside this
portable-C native domain. The existing aligned freestanding entry wrapper is
used; no host application, runtime settings or saves are involved.

## Caller and invalid guest-pointer boundaries

The original three-word parent window at **0x150397E4..0x150397F0** loads the
quaternion at **SP+0x98** and matrix at **SP+0x220**, with the output pointer
set in the JAL delay slot at **0x150397EC**. It passes **16 cases / two streams**
with the original caller stack, saved registers and full public memory.
Two changed-pointer controls fail. The aligned retail Game-code census finds
one direct JAL, at ROM **0x66C98**, and no aligned literal entry pointers.
The leaf itself neither calls another routine nor produces a V0 return value.
Complete parent execution and dynamically computed external routes are not
claimed by this bounded caller audit.

Six misaligned input/output probes raise matching modeled alignment faults.
Sixteen additional **guest-only callee-private stack alias cases** compare the
complete original/compiled response. Twelve overwrite the saved FPR pair and
reproduce retail's corresponding saved-register corruption; the test catches
the model's post-return ABI invariant failure rather than claiming a hardware
exception. Such pointers violate the portable C/ABI input contract and do not
receive native defined-domain credit. Valid overlaps remain fully covered.

## Actual Make, padding and production image

Both complete-owner padders agree on all four functions and original padding.
Twelve GNU links at four code regions (`0x15000000`, `0x25000000`,
`0x65000000`, `0x95000000`) preserve the complete 92-word target slot. The
independent three-command Make shadow uses the existing plain generated-C
recipe; production selects the same compiler, padder and assembler path.
Its ELF equals the independently predicted image:

- **282 changed ELF bytes**, zero exclusions and no metadata permutations.
- All **6,051 function addresses** remain fixed. Only this function's body
  and expected extent change from the 12-byte stub to **356 bytes**.
- Only `generated_770F0.c.o` changes among **698 production objects**; its
  only changed sections are `.text` and `.symtab`.
- All three owner neighbors and normalized pools remain unchanged.
- All **189,088 protected data bytes / 720 owners** and **80 headers / 82
  include inputs** are unchanged.
- All **817 non-adoption inputs** from the 820-input freeze stay fixed.
  Conversion CSV and the complete guard manifest are byte-identical.

Production ELF SHA-256:
`94d9c66578077a5ba247d661816b7dbd7cdf7aafda11390d71f2eb9f6d3541a4`.
Fresh suite times: **43.463 seconds** pre-install, **53.303 seconds** through
the sibling overlay, **39.003 seconds** installed. Native profiles execute
freshly in each suite. `make tools-check` passes; the existing duplicate
`generated_12D630` recipe warning remains.

The seven-file ignored sibling overlay preserves actual sibling HEAD
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a` and all **2,434 Windows-Git dirty
paths** byte for byte. Its before/after status SHA-256 remains
`a3712de44f2fc37079df4a789a5015f134f6ab977a2c2da90a3fde1851606cd9`.
Scoped Graphify extraction covers eight Python/C files, retains all **61,438
old IDs**, and records **61,485 nodes / 115,401 links**. This is not a full-corpus
re-extraction. The old private screen artifacts remain retained separately.

## Actual recount and resume boundary

The fresh production recount reaches **4,500 / 5,514 total exact C functions
(81.61%)**, Game **3,827 / 4,841 (79.05%)**, Init **492 / 492** and Debugger
**181 / 181**. Address drift remains zero; **1,014 C functions still differ**.
Converted counts/byte percentages are unchanged. **187 more exact C matches**
reach 85% at this denominator; the wider goal remains active.

Next ordinary C target: **`func_150C2898`**, the 86-word randomized effect
dispatcher in `game_EF410.c`. Recover its six-float/owner-pointer argument
interface, unsigned random-result arithmetic, packet and helper sequencing,
then complete the same qualification gates before credit.

`64CBFDOGL` remains only scratch `.codex` / `recomp_scene` directories at the
recorded path, without an active host Git/CMake checkout. No host adoption is
claimed; the frozen Release is untouched. Evidence is retained in ignored
`conker/build/game-quaternion-matrix-1504a140-private/`.

Tools commit: `cb6ceaf753145b11c509c7f0d3c81bda80c65a63`.
Commit source, this note/index handoff, two aggregate README rows and the
consumer tools pin afterward; no push is performed.
