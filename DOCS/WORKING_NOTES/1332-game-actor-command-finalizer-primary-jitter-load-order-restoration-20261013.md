# Game Actor Command Finalizer Primary Jitter Load Order - 2026-10-13

## Result

Resume consumer `a276803b` / tools `9cd126b` from
[Note 1331](1331-game-actor-command-finalizer-direct-byte-input-and-primary-cut9-restoration-20261013.md).
Both active checkouts are clean. Continue the complete `func_15034860` and
existing ABI/O2/g3/MIPS2/o32 profile. Zero Claude calls or host/Release work.

[Production function](../../conker/src/game/generated_61D10.c) changes only
the operand order of its primary integer jitter product: read actor[0x1FE]
before the signed actor[0x202]. Both operands promote to signed32; their product
is in -32640..32385, so the swap changes neither arithmetic nor FP grouping.
The compiler emits the original LBU T3 / LB T9 order and unchanged MULTU.

**Real word differences269->267; still non-matching/no matching credit.** Only
words81/82 change: original90AB01FE and80B90202 replace80AB0202 and90B901FE.
The405-word/1620-byte extent,0x48 frame, first14/last4 words, selector delay
slot, all six live stack slots and full-word selector contracts remain intact.
No guards, padding, physical-register binding, new fields or compiler changes.

## Screens And Fault Evidence

[Schedule screen](../../tools/experiments/game_actor_command_finalizer_schedule.py)
freshly compiles52 complete bodies:32 jitter/timer/lower variants,16 declaration
or parameter hints, and four real integer-input capture forms. Timer predicate
orientation emits identical literal code in the independently regenerated
baseline pair (SHAec266e5a). Hints do not improve shape/score or sampled cuts.

| Form | Words / Frame | Differences | Disposition |
| --- | --- | ---: | --- |
| Banked direct input |405 / 0x48|269|Reference|
| Jitter load order, selected |405 / 0x48|267|Qualified|
| Jitter order with early lower |405 / 0x48|261|Reject: primary cut9 GPR7/FPR16 differ|
| Branch-local lower assignments |406 / 0x48|244..245|Reject: overflow and earlier state loss|
| Delta product capture |405 / 0x48|299..300|Reject: primary cut9 and selector allocation regress|
| Current product capture |405 / 0x48|328|Reject: earlier opening-state loss|

All52 path access counts remain equal; every one of2938 fault pairs fires.
Exact represented states720->1086, with **no previously exact sampled state
lost**, asserted per path rather than inferred from the larger total. The
representative active path also restores the complete states/dispatch words at
cuts17/18. Represented state covers memory/events/GPRs/FPRs/condition/HI/LO/calls,
not hardware PC, branch-delay exception state, FCSR or whole-game acceptance.

The earliest boundaries do not move: primary cut10 on44 paths still differs
in GPR7 at the D_80097D48 load; disabled-primary cut7 on eight paths still loads
second into T9/register25 instead of T3/register11. Do not report either closed.

## Qualification And Banking

[Focused suite](../../tools/tests/test_game_actor_command_finalizer_schedule.py)
reuses the existing contract through scoped adapters and a new ignored baseline.
All13 pre-install tests pass54.970s. All13 installed tests plus both protected
text checks pass together,15 tests in46.959s, no skips. Fresh signed-jitter
negative control targets the actual reversed expression and fails effectively.

Coverage remains15288 guest cases,385 aliases,8192 native32 O2/O0 cases/five
fresh negatives,80 live-slot cases/16 old342 failures,160 incoming-home aliases,
480 independent rebase cases and200 real119-word-parent calls. Owned records
retain M48, offsets -48/-40/-36/-28/-24/-20, frame writes8->24->72 and identical
normal/traced code. Nine owner neighbors, relocations, pools and both padders
agree. Neither opaque PRNG providers nor finite FP tests prove retail hardware.

Linked build passes with the existing duplicate generated_12D630 recipe warning.
Literal whole-ELF proof permits exactly **six changed bytes**, all inside the
same target slot; every other byte, size, address and metadata item is fixed.
All189088 Game-data bytes/720 owners are exact, SHA0bbc00e1. Guards14694 rows,
target0; caller/layout/rodata/profile/conversion CSV fixed. No ROM replacement.

Archive the protected text manifest/ELF before changing only its ELF pin to the
independently proved image; all eight other inputs remain fixed. Both mounted
and older tool checks and Windows syntax/scoped whitespace checks pass.

| Artifact | SHA256 |
| --- | --- |
| Source |76c0c333b9c1de6e9c9cbd3865dc84ea2742692f1b4add3ef6f3a52ef43da27f|
| ELF |9c75bf09dcf23dcfb2266396a565a8ca6196a4d41be59eff9ca1c6d3ae58a52b|
| Guards, unchanged |420eb4c5458868e6b19f5a7eb45f04b38ef96532216f283689eec7e0c5e8d796|

Bank tools `2b16f4f` before the consumer source/docs/gitlink. Only two absent
task files and the independently verified text pin are mirrored. Older
HEADddbdd16b and413 unrelated hashes remain fixed; dirty414->416. No older
commit/reset/stash or push. Verify current links, commit-hook completion and
post-bank image integrity before closing the checkpoint.

Fresh matching remains Game2823/4823 (58.53%), total3496/5496 (63.61%), zero
drift/2000 different, conversion5496/6044. README date/aggregate rows are already
correct and receive no function narrative.

Continue **this same func_15034860** and all267 remaining differences. The next
useful discriminator is owned compiler evidence for the lower=40 placement
around unsigned conversion/tag-home lowering, not another unchanged hint screen.
Keep the primary cut10 and disabled-primary cut7 requirements together with
full private/fault/owner/rebase/image gates. Wider Game, prior guard elimination,
retained text218/114/cut27, translator49/34 and hardware/runtime goals stay open.
