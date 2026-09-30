# Init spatial-volume callback match

Date: 2026-09-30

`func_1000C7E8` occupies 83 words and 332 bytes at
`0x1000C7E8..0x1000C934`. The former zero-return placeholder is replaced with
the recovered callback that manages the active state and computes a clamped
distance-based channel value.

When global mode `D_800BE9F0` is `0x31`, state two returns zero. Other states
ensure resource nine exists by submitting the retail `0x3E` setup sequence,
then return state two. In other modes the callback initializes
`D_8002B070` to one when needed, selects that active state, and computes
`D_8002C238 - sqrt((z + 4000)^2 + x^2) * 10`. The result is clamped between
`100.0f` and `D_8002C238`, truncated for `func_1000E40C`, and the selected
state is returned.

Thirty-three of 83 retail words emit directly from the semantic C and the
slot's retained trailing padding. Fifty function- and offset-scoped guards
normalize IDO's alternate incoming-float preservation, two resulting branch
distances, and one closed floating-point register/instruction schedule. The
two moved `D_8002C238` relocations and moved final call relocation are checked
explicitly. No instructions are inserted or removed.

The exhaustive stale-guard rebuild completes every padded object without a
guard failure. The expected whole-ROM SHA-1 check still fails because the
project contains unrelated non-matching functions. The authoritative matcher
and direct section-span comparison pass. The linked and retail spans share
SHA-256
`8b0ef26f08fc4e4ac97da787b65fb1e3377e5d9dfd7beaf356e25550c14c6423`.

The matcher advances to `3,104 / 5,457 (56.88%)` overall and
`421 / 488 (86.27%)` in Init, with zero address drift and 67 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
