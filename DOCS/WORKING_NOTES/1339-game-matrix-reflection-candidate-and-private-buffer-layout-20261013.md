# Game Matrix Reflection Candidate And Private Buffer Layout

Date: 2026-10-13

## Scope And Result

Continue the full Game matching goal from consumer `6f8f0785`, tools `c0ca061`
and [Note 1338](1338-game-actor-command-finalizer-guarded-match-20261013.md).
Both active checkouts begin clean. Target **func_15034F30**, VA
`0x15034F30..0x150356C8`, ROM `0x623E0..0x62B78`, **486 words / 1,944 bytes**,
original frame **0x190**. The production source remains its zero-return
placeholder in [generated_61D10.c](../../conker/src/game/generated_61D10.c).

The [complete candidate](../../tools/experiments/game_matrix_reflection_candidates.py)
now emits **486 words / frame 0x190 / 347 differences** under the unchanged
O2/g3/MIPS2/o32 profile. It restores the original conversion scratch address
without padding or register bindings. It is **uninstalled and not matched**:
no source/ELF/guard/profile/progress change, new conversion or matching credit.
The wider goal remains active on this same function.

## Recovered ABI And Control Flow

The original function has **19 argument slots / 76 parameter bytes**: actor,
record, mode, input matrix bank, output matrix bank, signed32 count, eleven
float slots, and two full32 representation flags. Slot9 is unused but must
remain in the prototype. A decompiler omitted it; a compiled missing-slot
control changes the real public result. Do not transplant that inferred ABI.

Both original call sites inside func_15035808 are inspected and executed as
31-word and 47-word windows, each at stack phases0/8. They forward all19 slots,
including the unused float, input/output matrices, three actor coordinates,
opacity and both flags. Window prefixes are seeded; the complete parent and
its opaque providers are not qualified here. The final callback takes only
the actor pointer, not the leftover f12/f14 values inferred by the decompiler.

- Always initialize a local identity matrix. Unsupported modes then return
  without changing public storage or calling the actor finalizer.
- Modes0/1 negate the Y diagonal and iterate64-byte matrices. Fixed inputs
  use guMtxL2F; float inputs have their affine column normalized in place.
  Multiply by the reflection matrix, then apply the original Y translation
  correction using a source read **after** multiplication. Preserve overlap.
- Mode2 negates the X diagonal, builds negative/positive angle matrices, copies
  each input, subtracts the pivot, applies all three products, then adds the
  pivot back. Optional fixed output uses bcopy plus guMtxF2L2.
- Preserve the reloaded loop-count home and output-argument home. The cursor
  advances independently; output conversion still re-reads the output home.
- Modes0/1 use pointY minus pivotY for opacity. Mode0 has its separate ten-unit
  near ramp. Mode2 calls the integer distance provider with four truncated X/Z
  coordinates. Preserve strict comparisons, float operation order and unsigned
  conversion before the final byte store.
- For a nonnull actor with a nonzero **word** at+0x9C, temporarily install the
  output bank at+0x1D4, call func_15034728, and restore the saved bank through
  the post-callback actor home. A byte-only gate and wrong restore are rejected.

## Source And Private-Address Fit

Twenty initial source forms distinguish array ordering, loop expressions and
live incoming homes. The first complete body is481 words/frame0x190/453
differences. The explicit count-home do-loop plus output home restores486
words and reduces the score to347. Ordinary and oversized home alternatives
are measured but not installed.

That first486-word form places the conversion matrix at SP+0x90, versus
retail SP+0x84. Moving **three existing pointer locals** before its declaration
restores SP+0x84. No new/dead local, larger array, arbitrary padding or physical
register binding is introduced. Qualified form: **layout-0-1-2**.

All56 three-local placements emit one identical improved word array. Crucially,
its score is still347: literal comparison finds two changed address words even
though aggregate scores agree. The earlier test requiring identity to the old
array correctly exposed this improvement; do not group bodies by score alone.

The fired, fingerprint-locked compiler capture preserves normal/traced object
and pool identity. Frame writes are88 ->104 ->400; locals/saved/outgoing are
296/88/16. Optimizer definitions are M292 and P76. The four matrix M offsets
are **-268, -192, -128, -64**, yielding SP+0x84/0xD0/0x110/0x150 in this frame.

At phase0 the conversion destination moves from **0x3FF00** to the original
**0x3FEF4**. The prior form remains an effective twelve-byte private-layout
negative. The improved candidate matches complete sampled RAM, including its
private frame; it does not match all register/instruction states.

## Qualification And Limits

[Focused suite](../../tools/tests/test_game_matrix_reflection_recovery.py) plus
the two unchanged protected text checks pass **17 tests in 89.139 seconds**.

- 4,800 guest cases cover supported/unsupported modes, negative/zero/positive
  counts, all four representation-flag combinations, falloff boundaries,
  callback gates and two stack phases. Complete sampled RAM and helper-input
  packets match the original, not just the opacity byte.
- 48 overlap cases and18 live-home mutation cases pass. Count/output home
  changes and actor-home replacement after the callback are actually exercised.
- 256 native32 vectors per O2/O0 profile check the actual body, numeric matrix
  words, opacity, callback mutation and bank restoration. Four independently
  compiling runtime negatives reject wrong ramp, byte gate, restore and X/Z
  argument slots. Native scope is float buffers, zero-angle providers and
  defined finite unsigned-conversion inputs, not guest-only sparse aliases.
- Both complete owner padders agree, preserve all nine neighbors and their
  relocations/pools, and emit the entire1,944-byte target without new guards.
- Three independently assembled original links and216 rebased semantic cases
  preserve the code/helper relocation contract. None is claimed byte-exact.
- A mixed float-input/fixed-output cross-alias at count2 reaches the **same**
  rejected fixed conversion in both original and candidate. Packets and memory
  agree at that boundary, but the provider model admits only finite exact
  signed32 values after scaling. Count1 and representation-compatible overlaps
  are separately qualified. The final mixed-format result is unqualified.

Matrix multiplication, rotation, packing and unpacking reuse existing bounded
project models. The distance and actor callback are controlled opaque providers.
This is not execution of those SDK/provider implementations, arbitrary FCSR or
NaN qualification, whole-parent acceptance, emulator/hardware or gameplay proof.
Routine work uses zero Claude calls.

## Remaining Matching Boundary

One fixed-input witness now has identical RAM/FPRs at return but differs in
GPRs **9 and13**. Literal own-access fault probes at phases0/8 agree before the
first memory operation, then diverge at **cut1** in the saved-register schedule:
retail first dispatch is AFB60058; source is AFBE0060. At cut1 the dispatches
are AFBF0064 versus AFB50054, and private memory already differs. Gates fire
from actual instruction accesses; no observer-generated fault or affine
private-frame rebasing is used. Only these opening cuts are tested, not an
exhaustive full-fault claim. Hardware PC/BD/FCSR behavior is unqualified.

Next recover the opening saved-register roles and independent store schedule,
then the remaining347 allocation/control differences. Retain the complete19-slot
ABI, four real private matrices, incoming-home cases and complete sampled RAM
while changing source. Qualify all private/fault/linked-image gates before any
production installation or matching credit; do not normalize this unresolved
body wholesale or add frame guards.

## Banking And Preserved State

Tools **f3e8f92** commits the complete candidate generator and focused tests
first. The consumer records that exact pin with these working docs. The older
tools mirror keeps HEAD ddbdd16 and **all430** initial dirty-path fingerprints;
only two absent files are added, bringing its dirty-path count to432. No push,
history duplication, reset, host edits or Release work.

All seven target production inputs and all nine protected text inputs remain
exact. No immutable fixture rebase is needed. Prior matching totals remain
Game2,824/4,823 and total3,497/5,496 with1,999 different/zero drift: the ELF and
conversion CSV are unchanged, and the root README is untouched.
ROM-free wrapper checks pass in both copies; Windows byte-compilation and
scoped diff checks pass. Direct graph update fails closed at18,699 proposed
versus40,479 existing nodes; preserve its retained-corpus and version warnings
and do not force a purge. Incremental commit-hook completion is checked after
banking.
