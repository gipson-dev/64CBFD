# Init fixed-point parameter wrapper match

Date: 2026-09-30

`func_10010E78` occupies 46 words and 184 bytes at
`0x10010E78..0x10010F30`. It obtains a scale and packed parameter through
`func_1000F6B8`, multiplies the caller's unsigned 16-bit magnitude by that
scale, and shifts the product right by 15. A zero result returns immediately.
A nonzero result calls `func_10010BE8`, passing the packed value's low seven
bits separately and combining its high bit with the caller's byte flags.

Recovering the first argument as `u16`, keeping the packed output in a signed
32-bit local, and retaining the scaled result as a 32-bit value reproduce the
retail frame, stack arguments, narrowing operations, zero branch, and call
schedule. Forty-five of the 46 words emit directly from semantic C. One
stale-checked expected-word guard preserves retail's commutative `multu`
operand order.

The focused compact-object inspection, complete relink, authoritative
matcher, and direct section-span comparison pass. The linked ELF and retail
spans share SHA-256
`593c63fd1ac1b69d9efa566fd99515abc6d72ae3a4fe946b892928752c35e6bb`.
The matcher advances to `3,086 / 5,458 (56.54%)` overall and
`403 / 489 (82.41%)` in Init, with zero address drift and 86 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90` and
`func_1000FEF0` parked at their documented saved-register allocation
boundaries.
