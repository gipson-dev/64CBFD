# Init planar direction encoder match

Date: 2026-09-30

`func_1000B060` occupies 84 words and 336 bytes at
`0x1000B060..0x1000B1B0`. The former zero-return placeholder is replaced with
the recovered planar direction encoder.

The routine computes the input vector magnitude, normalizes the first
component when that magnitude exceeds `D_8002C214`, and converts the result
through `func_150487E0` and the double scale `D_8002C218`. A positive second
component folds the signed angle around `+/-0x80`. The caller-provided offset
is then narrowed to a signed byte, values outside `+/-0x60` collapse to zero,
the outer bands fold toward the center, and the central band doubles. The
result is biased by `0x40` and combined with the retained `0x80` flag, which is
cleared only for the central band.

Fifty-eight of 84 retail words emit directly from semantic C and retained
slot padding. Twenty-six function- and offset-scoped guards normalize two
stack-local offsets, one closed floating-point temporary allocation, the
signed-byte temporary chain, and two independent integer scheduling choices.
No instructions are inserted or removed; all branches, calls, relocations,
comparisons, range-fold behavior, and the epilogue otherwise emit directly.

The exhaustive stale-guard rebuild completes every padded object without a
guard failure. The expected whole-ROM SHA-1 check still fails because the
project contains unrelated non-matching functions. The authoritative matcher
and direct section-span comparison pass. The linked and retail spans share
SHA-256
`d12c643410bab7b05ab9364b986eac6839ee1300617681239c6b5299fba2879a`.

The matcher advances to `3,107 / 5,457 (56.94%)` overall and
`424 / 488 (86.89%)` in Init, with zero address drift and 64 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
