# Init released-node recycler match

Date: 2026-09-30

`func_1000A348` occupies 54 words and 216 bytes at
`0x1000A348..0x1000A420`. It walks the active `struct54` list rooted at
`D_800406A0.unk4`. Records whose signed state byte at `0x14` and unsigned
state byte at `0x16` are both zero return their retained value through the
pointer at `0xC`, unlink from the active list, and splice into the reusable
list rooted at `D_800406A0.unk10`.

The recovered C preserves the next active node before mutation, repairs both
directions of the active list, handles removal of its head, and distinguishes
an empty reusable list from insertion after its existing head. Thirty-five of
the 54 words emit directly from semantic C. Nineteen stale-checked guards
preserve one closed compiler schedule: eight manager-base register uses and
eleven words covering the reusable-list successor read, backlink, and
branch-delay stores. The opening HI16/LO16 pair remains relocation-aware.

The focused object build, exhaustive guarded relink, authoritative matcher,
and direct section-span comparison pass. The linked Init section and pristine
image share SHA-256
`3b03c2654be6fe46335aeccddb64cca509d8edddb5f980c04918b85486affe7a`
across all 216 bytes.

The matcher advances to `3,087 / 5,457 (56.57%)` overall and
`404 / 488 (82.79%)` in Init, with zero address drift and 84 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
