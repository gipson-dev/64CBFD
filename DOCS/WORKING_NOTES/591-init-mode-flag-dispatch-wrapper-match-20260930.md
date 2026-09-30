# Init mode-flag dispatch wrapper match

Date: 2026-09-30

`func_1000CAE4` occupies 49 words and 196 bytes at
`0x1000CAE4..0x1000CBA8`. It treats the low two bits of its first argument as
independent state flags. In global mode `0x42`, it installs sentinel pointer
`4` through `func_10011FA0` and raises event `0x58` when bit zero was clear.
Outside that mode, a set bit zero is cleared through the corresponding event
and timed transition calls.

If bit one was clear, the routine forwards the low byte of its second
argument to `func_10008790` with fixed arguments `0x1000`, zero, and one,
then marks bit one set. It returns the resulting two-bit state. The third and
fourth arguments are unused but remain in the recovered signature because
retail homes all four incoming argument registers.

All 49 words emit directly from semantic C. The 40-byte frame, saved-`s0`
lifetime, four argument-home stores, branches, delay slots, and four call
sequences require no expected-word guards.

The focused object build, linked rebuild, authoritative matcher, and direct
section-span comparison pass. The linked Init section and pristine image
share SHA-256
`aefe1f79eec76c20160be8b0aa7962cd15f8375113ec490913b5bf3240b586ac`
across all 196 bytes.

The matcher advances to `3,089 / 5,457 (56.61%)` overall and
`406 / 488 (83.20%)` in Init, with zero address drift and 82 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
