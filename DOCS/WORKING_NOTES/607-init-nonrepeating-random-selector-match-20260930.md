# Init nonrepeating random selector match

Date: 2026-09-30

`func_1000F568` occupies 84 words and 336 bytes at
`0x1000F568..0x1000F6B8`. The former zero-return placeholder is replaced with
the recovered bounded random-choice selector.

The routine starts from `func_150ADA20() % arg1`, rejects record indices at or
above `0x6E2`, and returns the base index unchanged when fewer than two choices
exist. For choice counts below eight it uses the byte at
`D_80041F5C + arg0` as an availability mask. An invalid or exhausted mask is
reset, an unavailable random choice advances cyclically to the next available
bit, and the selected bit is removed so successive calls avoid repeats. The
mask is replenished when its choice bits are exhausted. Larger choice sets
store the one-based random result directly.

Seventy-three of 84 retail words emit directly from semantic C. Eleven
function- and offset-scoped guards normalize five branch distances and five
commutative operand-order choices, then restore one dead raw-mask assignment
that IDO removes. That inserted `li a0, 0xFF` shifts the otherwise matching
tail into its retail position. The call, table relocations, signed and unsigned
division behavior, bit-mask loop, stores, and epilogue otherwise emit directly.

The exhaustive stale-guard rebuild completes every padded object without a
guard failure. The expected whole-ROM SHA-1 check still fails because the
project contains unrelated non-matching functions. The authoritative matcher
and direct section-span comparison pass. The linked and retail spans share
SHA-256
`f669a659ee095e77b72fdefe06d91f096ad7ed2b43b1552eda234db999bfeb44`.

The matcher advances to `3,106 / 5,457 (56.92%)` overall and
`423 / 488 (86.68%)` in Init, with zero address drift and 65 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
