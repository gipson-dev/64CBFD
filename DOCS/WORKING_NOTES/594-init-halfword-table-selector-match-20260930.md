# Init halfword-table selector match

Date: 2026-09-30

`func_10011EB8` occupies 58 words and 232 bytes at
`0x10011EB8..0x10011FA0`. It maps its input through `func_1510F8CC`, then
optionally returns the signed scale `0x7FFF / (D_80082FA0 + 1)` through its
second argument, using `0x7FFF` directly for a single-player count of zero.

The mapped index selects a 20-byte row of five four-byte halfword pairs at
`D_8002C240`; the third argument selects one pair in that row. The first
halfword is the default return value. When the second halfword is at least
two, the routine resolves the pair through `func_1000F568`, passing the
selected value and selector, and returns the result narrowed to `u16`.

The semantic C emits the complete table arithmetic, optional divide and its
IDO trap checks, both calls, control flow, and epilogue in retail order, but
IDO removes two redundant opening copies between `a0` and `a3`. Two bounded
stale-checked guards insert those words after the third argument home and
move the existing `func_1510F8CC` call relocation with its instruction. The
insertions consume two of the three trailing padding words, leaving retail's
single final padding word intact.

The focused object build, exhaustive guarded relink, authoritative matcher,
and direct section-span comparison pass. The linked Init section and pristine
image share SHA-256
`4b4a026b8a28e4703983b808e69359a8682c0b7577a6b35144145a2c0cf6a16f`
across all 232 bytes.

The matcher advances to `3,092 / 5,457 (56.66%)` overall and
`409 / 488 (83.81%)` in Init, with zero address drift and 79 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
