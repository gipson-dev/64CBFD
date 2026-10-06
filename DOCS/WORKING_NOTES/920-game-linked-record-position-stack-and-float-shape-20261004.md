# Game Linked Record Position Stack And Float Shape

Date: 2026-10-04. Starting HEAD: `83f618fd`.

Matching continuation: [Note 1028](1028-game-linked-record-position-tail-match-20261006.md)
now closes the tail through three expected-word guards and a single saved-RA
insertion, with an independently tested control-layout proof. The 71-word
semantic C body below remains unchanged; it is not a direct raw-C match.

## Retained Improvement

Continue Note 919's semantic `func_150E6FAC` recovery. Move the record-pointer
local declaration immediately after the node result declaration, before the
float locals. IDO now assigns radius to SP+0x2C, angle to +0x2A and first
angular sample to +0x24, exactly as retail; node remains +0x34.

Spell each inner sum as record component times -80 plus actor component.
Keep the outer sum with radius-scaled angular output, and Y's extra 100.
This restores the complete retail float register allocation and add operand
order emitted by IDO without changing expression grouping or adding guards.
Sequential output and callback/data timing from Note 919 remain intact.

Declaring only the second angular sample `register` did not change the
emitted body; rejected and removed. An explicit success-path `return` also
left the return-tail layout unchanged; rejected and removed.

## Fresh Instruction Evidence

Production retains 71 body words in the 72-word slot and the 0x38 frame.
Differing aligned word positions fall from 38 to **15**. Words 0-9 and 11-57
match retail exactly: 57 non-branch words before the return tail, including
all lookup/RNG/helper calls, data loads and floating-point operations.
Word 10 differs only in the branch-likely target displacement.

At word 58 the compiler emits the success-path branch, with final output
store in its delay slot. Retail first stores output, then branches with a
duplicated RA load in the delay slot. The compiler shares that RA load after
fallback; retail has one on each path. The missing word shifts fallback and
epilogue by one word, accounting for the remaining differing positions
58-71 and branch displacement. This is a control-layout/code-size difference,
not a batch of independent register renames; no word guards are justified.

Entry `0x150E6FAC` and next function `0x150E70CC` remain unchanged.

## Verification

The independent IDO test now asserts exact retail words 0-9 and 11-57,
in addition to body footprint, frame and all five call targets. It does not
claim complete slot equality. Host tests still cover both branches, 35 RNG
word/fraction combinations, callback mutation and overlapping output.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_linked_record_position tools.tests.test_game_random_range_position tools.tests.test_game_object_position_sound_adapter -v -f
```

All thirteen tests pass in 1.806 seconds, no skips. Fresh production linker
and matcher pass: total 3274 / 5463 exact, Game 2601 / 4790, Init 492 / 492,
Debugger 181 / 181, zero drift, 2189 still different. README aggregate snapshot
is unchanged because this remains nonmatching. No hardware/gameplay or
exceptional floating-point fixture qualification is claimed.

Next: explain the original duplicated RA-load return layout through source
or a justified compiler profile. Do not repeat register qualification or
explicit return unchanged. Production assembly ownership in Init and the
528-byte decoder fitting deficit remain untouched. Unrelated actor/timeline
changes are excluded; no host adoption, sibling build, Release change or push.
