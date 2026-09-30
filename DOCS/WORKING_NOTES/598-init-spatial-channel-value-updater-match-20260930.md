# Init spatial channel-value updater match

Date: 2026-09-30

`func_1000C934` occupies 57 words and 228 bytes at
`0x1000C934..0x1000CA18`. The former zero-return placeholder is replaced with
the recovered four-argument routine. It selects limit `12000` or `0x7FFF`
from state bit `D_800DBFF0->unk5F0 & 1`. In level `0x37`, with that bit clear,
it runs the fixed spatial query through `func_100114D0` and subtracts the
query's masked high byte from the selected limit. A changed pending value is
sent to channel `0x54` through `func_1000E40C`, and the function returns the
value with bit 31 set.

Restoring the source's explicit `if/else` limit assignment is essential: a
preinitialized limit lets IDO remove retail's unconditional branch and shifts
the remaining function. With that source shape restored, 39 of 57 words emit
directly from semantic C, including the complete frame, argument homes,
globals, spatial-query call, channel-update call, and all relocations.

Eighteen function- and offset-scoped entries in
`retail_word_patches.us.csv` normalize the remaining non-relocating tail. One
guard selects retail's branch-delay reload; thirteen preserve a closed
value-register rotation around the masked subtraction and optional update;
four restore the equivalent result/epilogue schedule. Every guard checks its
expected compiler word and fails if the source or compiler output drifts.

The focused object build, exhaustive stale-guard rebuild, authoritative
matcher, and direct section-span comparison pass. The linked Init section and
pristine image share SHA-256
`4e561733cb18a6f8daf394a820982539e2d912471df045a9ef3207798cbc4886`
for the complete function.

The matcher advances to `3,097 / 5,457 (56.75%)` overall and
`414 / 488 (84.84%)` in Init, with zero address drift and 74 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
