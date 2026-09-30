# Init entry mask value updater match

Date: 2026-09-30

`func_1000E46C` occupies 71 words and 284 bytes at
`0x1000E46C..0x1000E588`. The former zero-return placeholder is replaced with
the recovered entry lookup, percentage conversion, channel dispatch, and
per-mask value update.

The routine resolves the requested `struct151` entry and converts its incoming
percentage to an unsigned-byte scale with saturation at zero and 255. Entries
with a nonnegative channel dispatch through `func_1000886C` or
`func_10008790`, selected by the sign of the fourth argument. Entries without
a channel update their `unk38` mask according to whether the converted value
is zero or positive, then walk the signed input mask and write that byte to
each selected `unk3C` slot.

Mutating the incoming `arg1` percentage and `arg2` mask directly is the key
source shape. A separate converted-value local changes the saved-register
lifetime and overflows the retail slot; explicit `register` declarations do
not recover the schedule. Reusing the parameters preserves retail's `s1` and
`s0` lifetimes, including the signed right-shift loop.

All 71 words emit directly from semantic C. No expected-word guards, compiler
profile changes, or generated insertions are required. The authoritative
matcher and direct section-span comparison pass. The linked Init section and
pristine image share SHA-256
`1e96762e70a9a2b3a72c015cdb62fa7ac620a2e7ba751cee8f29b0bf22a2a686`
for the complete function.

The matcher advances to `3,101 / 5,457 (56.83%)` overall and
`418 / 488 (85.66%)` in Init, with zero address drift and 70 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
