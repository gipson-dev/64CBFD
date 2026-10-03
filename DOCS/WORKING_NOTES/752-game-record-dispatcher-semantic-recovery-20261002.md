# Game Record Dispatcher: Semantic Recovery

Date: 2026-10-02

## Result

`func_15040CC8` now replaces its zero-return placeholder and obsolete commented
draft with a complete semantic record dispatcher. It is **not byte-exact**.
The existing padded-object overflow mechanism preserves the 38-word retail
slot and routes execution to the 39-word compiled body. No word guards or
compiler overrides were added.

The checkout began clean at `f74d0ea`. This resumes ordinary Game recovery
after the bounded Init trials in
[Note 751](751-init-bitmap-loop-mask-profile-trials-20261002.md).

## Retail Contract

Retail occupies `0x15040CC8..0x15040D60`, 38 words / 152 bytes, with ROM
span `0x6E178..0x6E210`. Its behavior is:

1. Retain a short empty counter loop before dispatch.
2. Visit slots -20 through 9 inclusive, thirty records with an eight-byte stride.
3. Compute each record address directly from the argument base. The argument
   points twenty records into the containing allocation, not to an array of
   loaded record pointers.
4. Read the unsigned first byte and call `D_800844B0[selector]`, passing the
   record address through the existing guest `s32` callback ABI.
5. After all thirty callbacks, load `D_800848B0`. If nonzero, pass it to
   `func_1500390C`; ignore that callee's result.

Step 5 loads the global once after the complete dispatch sequence, not once
after each individual callback. Callback changes to future record selectors,
callback table entries, and the final cleanup global must remain visible.

The recovered signature is `void func_15040CC8(u8 *arg0)`; no defined return
value is established. The generated `s32` placeholder declaration was removed
and the recovered prototype added to `conker/include/functions.h`.
The old commented draft incorrectly indexed `arg0` as an array of pointers;
its removal is part of the recovery, not merely formatting cleanup.

## Compiler Boundary

The production `-O2 -g3` build retains the opening empty delay, all thirty
indirect calls, and the post-dispatch cleanup path. It strength-reduces the
record loop into an advancing pointer and byte-offset counter, requiring four
saved registers instead of retail's three. The body is 39 words / 156 bytes,
one word beyond the retail slot.

Fifty-two isolated shape/profile compilations were inspected under ignored
`conker/build/game-record-dispatch-*` fixtures. Shapes include for/do/goto
loops, direct versus cached address expressions, integer versus pointer bases,
eight-byte struct indexing, and explicit register/table locals. Profiles include
`-O2 -g3`, `-O2`, `-O1`, no-unroll, and selected `-O1 -g3` / `-O2 -g` trials.
No tested form establishes the complete retail instruction sequence.

Some inline `-O1` forms fit 38 words but spill arguments and locals to the
stack and do not preserve retail's frame or loop shape. Merely fitting the
slot is not a matching result. The default-profile semantic body was retained
without changing neighboring functions' compiler behavior or normalizing the
whole loop into retail words. Matching needs a new compiler/source-shape
approach, not a register-only guard batch.

## Behavior Tests

`tools/tests/test_game_record_dispatch.py` extracts the actual production C
body and executes it in a freestanding 32-bit fixture, preserving the guest
pointer-to-`s32` ABI. The fixture passes a base twenty records into a real
thirty-record allocation, with sentinel bytes on both sides.

Eight tests pass:

- All thirty direct addresses in order, including negative and positive slots.
- Unsigned selectors, including 0 and 255.
- Cleanup receives the global only after all callbacks.
- A callback can clear an initially nonzero cleanup global.
- The final callback can publish a previously zero cleanup global.
- A callback's change to a future selector is observed.
- A callback's change to a callback table entry is observed.
- Repeated dispatch restarts at the first record without stale cleanup state.

The tests check complete buffer preservation except for deliberate mock
mutation. They do not qualify null callback entries, invalid record allocations,
guest runtime timing, or gameplay behavior. The opening delay is checked in
the compiled guest body; the host optimizer is free to remove an empty loop.

## Linked Verification

- Focused object build passes.
- `make -C conker NON_MATCHING=1 all match-progress -j4` passes.
- All 99 tests under `tools/tests` pass, including eight new dispatcher tests.
- `make tools-check` passes.
- Linked `func_15040CC8` remains at `0x15040CC8`, occupying 38 words.
- Its first jump resolves to `__retail_overflow_func_15040CC8` at
  `0x15F000B8`, containing the complete 39-word body.
- The following `func_15040D60` remains at `0x15040D60`.
- Independent section extraction confirms all 164,048 Init code bytes and
  all 17,376 initialized-data bytes remain exact, with the hashes in Note 749.

The retail-slot matcher reports 36 differing words for this routine because
it compares the trampoline/padded slot, not the overflow semantic body. Do not
describe this as 36 compiler differences within the recovered body.

Aggregate progress is unchanged: the old placeholder already counted as C.
Total exact C remains 3,251 / 5,461 (59.53%), Game 2,578 / 4,788 (53.84%),
with zero address drift and 2,210 differing Game C rows. README aggregate
tables therefore need no numerical edit. No gameplay qualification or
compressed-ROM replacement build was performed, and the sibling host port
and frozen Release artifacts were untouched.

## Resume

Keep `func_15040CC8` in the semantic-but-nonmatching queue with its overflow
boundary documented. The next ordinary placeholder recovery is
`func_150448D0`, 37 retail words and 36 current retail-slot differences.
Other queued placeholders include `func_1508B20C` and `func_1509F6E8`.
Keep `func_150F631C` in its separate near-match queue and `func_150A76F0`
in the handwritten/register-contract workstream.
