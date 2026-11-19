# Actor burst native qualification and address-allocation profile

Date: 2026-11-19. Continue `func_150BBB5C` from
[Note 2559](2559-game-actor-burst-semantic-recovery-and-allocation-boundary-20261119.md).
The committed C candidate is unchanged: **589 words / frame 624 / 58
relocation sites**, versus **587 retail words / frame 624**. It still has
**539 unequal overlapping words, two extra words and an extra saved S4**.
The production source remains a zero-return placeholder. This checkpoint
adds native qualification and allocation evidence, with **zero match credit**.

## Native SDK32 gate

The maintained native harness uses a **512-byte typed actor**, with assertions
for pointer width, total size and every used numeric field offset. Float,
word, halfword and byte subobjects have their actual C types. The sprite and
particle descriptor sizes and field offsets are asserted separately.
Guest-endian fixture fields are converted into those native subobjects;
the entire represented actor and all five globals are checked afterward.

An independent reference, already checked against the original assembly,
supplies **384 non-null cases**: all 16 randomized count pairs, four field
patterns, helper mutation on/off and rejected/inactive/active gates.
The harness compares every helper call and argument word in order:

- All **112 initialized descriptor bytes**, excluding its 12 untouched bytes.
- The **25 initialized sprite-header bytes** at the color helper boundary.
- Both three-float trail vectors and all **18 trail argument words**.
- All **10 sound argument words**, including full caller-side coordinate words.
- Every represented actor byte and all five global float values after helpers.

All 384 cases pass at each of **O0, O2 and O3**, with 32-bit pointers,
strict aliasing, no fast math and UBSan traps enabled. The known caller
ignores the routine's result; the native harness does likewise and suppresses
only the expected return-type diagnostic in addition to the existing native
helper flags. It does not add a synthetic return to the recovered body.

All **12 compiled semantic negatives** fail with the expected exit code 3.
The late-size-base control removes the now-dead local declaration and
assignment so that its intended semantic error is tested under `-Werror`.
The first fixture attempt stopped at that unused-variable diagnostic; it was
not counted as an effective runtime negative. A fresh corrected run passes
all three positives and rejects all 12 controls.

The fixture contains **2,827,780 bytes**, SHA-256
`423cca435e1405de3fa1a4660e5c34507e75a9c702726394fbe1a72a2eb7e43e`.
Its expected results come from the independent reference rather than from
running the candidate natively and recording its output.

This is finite native source/ABI evidence. It does not qualify null C
dereferences, uninitialized descriptor/sprite bytes, hardware FCSR, complete
helper implementations, arbitrary aliases or concrete private stack homes.
The original caller and literal production adoption remain separate gates.

## Extra S4 provenance and rejected profile controls

The repository's existing `-Wo,-no_const_in_reg` option removes the hoisted
descriptor-address register and extra S4 save. For the original semantic
source form it emits **590 words / frame 624 / 505 overlapping differences**.
For the scalar-reuse form it emits **590 / frame 616 / 510 differences**.
Adding the existing no-unroll option makes no further difference.

This is a concrete explanation of the address allocation, not a matching
fix. The same option changes the already matched `func_150BB760` neighbor,
so the full-owner override is rejected. It also prevents the required
floating-constant reuse in the target, including loop constants and the
opening half-speed coefficient. The copied normal-profile control reproduces
the exact committed raw hash, confirming that the comparison starts from
the same candidate.

Explicit source carriers for the half constant and sprite address, alpha
if/else selection, scalar reuse, descriptor order and a typed-decompiler
control do not recover the complete retail layout. The explicit alpha else
recovers its otherwise missing unconditional branch, but the tested profile
forms still emit 590 or 591 words, with incorrect allocation and homes.
No compiler flags, Make recipe, production source or guards were changed.
Copied-owner reports and rejected compiler diagnostics remain in the private
packet; a failed source-generation control is not acceptance evidence.

## Validation, scope and resume

The original four recovery tests and the new native test run freshly in both
the primary tools checkout and an isolated sibling overlay. Per-run results
and exact imported tool fingerprints are retained in the packet.
Both configurations pass all five tests with zero failures, errors or skips,
sealing 320 imported tool files each. Runner times are 61.504s primary and
83.423s sibling; unittest bodies take 53.521s and 60.546s respectively.
The overlay has 880 files: 339 matching sibling files, 537 primary fallbacks,
three new task files and one bootstrap.

Source,
guards, original assembly, progress rows, build profiles, production objects
and the complete ELF remain byte-identical across **1,863 frozen inputs**.
The sibling's existing dirty status, HEAD and 343 dependency hashes are
preserved. Root README aggregate tables are unchanged.

Installed totals stay **4,558 / 5,514 (82.66%)**, Game **3,885 / 4,841
(80.25%)**, zero address drift; **129 more matches** are needed for 85%.
No new byte-exact claim, production Make, production recount, host build,
Release change or gameplay acceptance is implied by this private checkpoint.

Resume the same function from its unchanged manifest and
`conker/build/game-next-150bbb5c-fit-private/`. Native qualification is now
banked. Continue the source-derived descriptor-address, saved-role and
stack-home relation, then complete caller, padder, whole-image and actual
production adoption gates. Preserve the normal profile and matched neighbors
unless a separately qualified target-only change closes the full relation.

Graphify receives a conservative scoped AST refresh with old-ID retention;
its automatic commit producer must finish before the final graph is sealed.
Routine work uses zero Claude calls and no REA/WSL reconfiguration. Commit
tools before their consumer pin and notes, with no push or automatic pause.
