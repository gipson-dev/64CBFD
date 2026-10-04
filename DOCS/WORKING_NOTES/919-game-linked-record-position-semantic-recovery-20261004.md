# Game Linked Record Position Semantic Recovery

Date: 2026-10-04. Starting HEAD: `7aa24abe`.

## Target Selection

Rechecked the retained MMIO experiments in Notes 737, 750, 762 and 885.
Pointer lifetime, partial volatility and published-address dataflow already
have measured negative results. No new justified source/provenance hypothesis
was found; do not repeat those trials or invent a return type solely to force
`$v0`. Production `func_100038E0` remains original handwritten assembly.

Continue genuine semantic recovery in Game at the next placeholder after
Note 917: `func_150E6FAC` in `generated_113D60.c`.

## Recovered Behavior

The function returns void and accepts an output float triple and actor pointer.
Call `func_1514ECE0` with the actor's node pointer at +0x2F4, key 0x16 and
a local result pointer. Any nonzero result selects the computed-position path.

On lookup failure, copy actor coordinates at +0x14/+0x18/+0x1C sequentially
to output. No RNG or angular helper calls occur, and the unused node result
is never dereferenced.

On success:

1. Sample `func_150ADA68`; radius is sample times 100 plus 80, without clamping.
2. Sample `func_150ADA20`; retain its low byte in a signed-halfword local.
3. Call `func_151423D8` with `(u8)(angle - 0x40)`, then with `(u8)angle`.
4. Read the returned node's record pointer at +0x10 only after those calls.
5. Write X as (actor X plus record +0x38 times -80) plus first helper result
   times radius; Y as (actor Y plus record +0x3C times -80) plus 100;
   Z as (actor Z plus record +0x40 times -80) plus second result times radius.

Preserve float expression grouping and sequential writes/next-axis reads.
Callback changes to actor coordinates or the node's record pointer must be
observed. Output aliasing with later input components must not be changed
into an all-coordinate snapshot. No null guard, extra fallback or new return.
The angular helper is not relabeled as a particular trigonometric function
without independently establishing that contract.

## Production Shape And Matching Boundary

Retail slot is 72 words / 288 bytes at `0x150E6FAC..0x150E70CC`, ROM slice
`0x11445C..0x11457C`. Production emits 71 body words, padded to the original
slot. Both entry and next-function addresses remain fixed; frame remains 0x38.
There are 38 differing aligned word positions and no target word guards.

Remaining differences include stack offsets for radius/angle/first helper
result, floating register allocation and commutative add operand order, and
the success-path output store versus return-load schedule. This is not
presented as a closed register-only normalization or a byte-exact recovery.
No broad patch batch is used to hide the unmatched compiler shape.

## Verification

New `tools/tests/test_game_linked_record_position.py` contains five tests:

- Failed lookup: exact coordinate copies, output sentinels and no RNG calls.
- Seven RNG words and five fractions: 35 combinations covering low-byte wrap,
  signed/high-bit inputs, radius extrapolation, call order and sentinels.
- Last angular callback replaces the node record pointer and changes actor X;
  output observes both mutations.
- Overlapping fallback actor output and successful record output preserve
  sequential read/write behavior across all three axes.
- Warning-clean independent IDO compilation: complete body fits 72 words,
  frame matches and all five call sites target the expected routines in order.

```sh
make -C conker build/src/game/generated_113D60.c.o
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_linked_record_position tools.tests.test_game_random_range_position tools.tests.test_game_object_position_sound_adapter -v -f
```

Thirteen tests pass in 1.709 seconds, no skips. Host fixtures use finite
exactly representable values and stubbed helpers; they do not qualify guest
NaN/FPCSR behavior, real RNG distribution, hardware or gameplay presentation.
The independent compiler check proves shape/call targets, not byte equality.
An initial test-fixture missing final newline was corrected; the final compile
is warning-clean. Project build retains the existing duplicate-recipe warning.

Fresh matcher remains total 3274 / 5463 exact, Game 2601 / 4790, Init 492 / 492,
Debugger 181 / 181, zero drift and 2189 still different. Conversion totals
also remain unchanged because the false placeholder was already counted as C.
README aggregate snapshot therefore needs no numerical update.

Init still has 47 assembly entries; decoder fitting deficit remains 528 bytes.
Unrelated actor/timeline changes are preserved and excluded. No sibling port
source import or build is part of this guest recovery; host adoption requires
its own integration and runtime evidence. Release untouched; no push.
