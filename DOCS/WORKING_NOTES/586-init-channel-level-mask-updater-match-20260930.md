# Init channel level/mask updater match

Date: 2026-09-30

`func_1000E588` occupies 51 words and 204 bytes at
`0x1000E588..0x1000E654`. It looks up the requested `struct151` channel
record. A live record clamps the requested percentage to 0 through 100,
converts it to an 8-bit value with `(percentage * 255) / 100`, and applies it
through `func_1000886C` using the record's low identifier byte and the caller's
channel mask. An inactive record sets that mask when the percentage is
nonpositive and clears it when the percentage is positive.

The recovered lookup, signed clamp order, multiply-by-255 expression, low-byte
identifier conversion, and two independent inactive-record sign tests give
IDO retail's complete frame, argument spill/reload schedule, division
sequence, call delay slot, mask operations, and shared returns. All 51 words
emit directly from semantic C with no expected-word guards.

The focused compact-object inspection, complete relink, authoritative
matcher, and direct section-span comparison pass. The linked ELF and retail
spans share SHA-256
`2ad78a07cd78b178c8b0cbc6194b6876624d7175951a0c2a007fe05a62e55e88`.
The matcher advances to `3,085 / 5,458 (56.52%)` overall and
`402 / 489 (82.21%)` in Init, with zero address drift and 87 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90` and
`func_1000FEF0` parked at their documented saved-register allocation
boundaries.
