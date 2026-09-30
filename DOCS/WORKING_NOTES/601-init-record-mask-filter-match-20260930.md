# Init record mask filter match

Date: 2026-09-30

`func_1000CDA0` occupies 67 words and 268 bytes at
`0x1000CDA0..0x1000CEAC`. The former zero-return placeholder is replaced with
the recovered record mask filter. Its first argument is an unsigned byte, and
its second argument is the existing `struct137` record used by
`D_800419A8`.

The routine accepts a zero mask immediately. For a nonzero mask it validates
the record pointer, signed handle index, active `D_800417B0` slot, and positive
selector. It also accepts records whose indexed handle state from
`func_1000853C` is three. Otherwise it checks selector bit `0x20`, optionally
sets bits zero and one in `D_800418AC[index]`, and reports whether the caller's
mask is fully cleared by the complement of the resulting flag byte.

The narrow `u8` first argument is required for retail's incoming argument-home
store and low-byte normalization. Reloading `arg1->unk0` after
`func_1000853C`, instead of retaining a local index across the call, restores
retail's mask and index register lifetimes. Those source corrections reduce
the function from 64 real differences to 18.

Forty-nine words emit directly from C, including every global relocation, the
`func_1000853C` call, and the complete flag-update block. Eighteen
function- and offset-scoped guards normalize one local-slot offset, the final
mask-result registers, and the redundant default-return schedule. Sixteen are
word replacements; two stale-checked insertions expand IDO's 64-word body to
the complete 67-word retail extent.

The focused object build, exhaustive stale-guard rebuild, authoritative
matcher, and direct section-span comparison pass. The linked Init section and
pristine image share SHA-256
`164c1732fc0ffe8c739238c8e3a4d813fc695781a41d8a5d3bbc5c9a65d92c0e`
for the complete function.

The matcher advances to `3,100 / 5,457 (56.81%)` overall and
`417 / 488 (85.45%)` in Init, with zero address drift and 71 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
