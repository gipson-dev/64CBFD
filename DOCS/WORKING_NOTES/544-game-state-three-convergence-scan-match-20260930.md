# Game state-three convergence scanner byte match

Date: 2026-09-30

`func_1509CDDC` occupies 34 words and 136 bytes at
`0x1509CDDC..0x1509CE64`. It first calls `func_1509CCF4` for the incoming
slot. It then scans all 204 bytes of `D_800D2E70`, calls `func_1509CCF4` for
each entry whose state is `3`, sums the reported changes, and repeats until a
complete pass reports zero changes.

IDO preserves that behavior but hoists the state-array address across the
retry loop, retaining an extra saved register and producing a 37-word body.
Eighteen guarded rows remove that invariant register, restore the five retail
save/load slots, rematerialize the address inside each pass, and normalize the
retry branch and delay slot. The resulting guarded object and linked ELF match
all 34 retail words.

The matcher advances by exactly one row to `3,048 / 5,463 (55.79%)` overall
and `2,469 / 4,789 (51.56%)` in Game with no address drift. Linked Game offset
`0x9CDDC` has SHA-256
`79a48e8c7f7ddf3f651113de5f1827c8645dfa89ed180c301a154838cba28405`.
The full shared-table rebuild and linked matcher pass.

Keep the documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_1509F77C`, the next ordinary matcher row.
