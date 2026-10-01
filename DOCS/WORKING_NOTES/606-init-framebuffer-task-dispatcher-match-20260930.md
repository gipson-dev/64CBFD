# Init framebuffer task dispatcher match

Date: 2026-09-30

`func_10004DB0` occupies 84 words and 336 bytes at
`0x10004DB0..0x10004F00`. The former zero-return placeholder is replaced with
the recovered per-frame scheduler callback.

In phase zero the routine receives a pending graphics task without blocking,
rejects a task whose framebuffer is current or next in the VI, and applies
the activity/countdown gate before calling `func_10004F00` to submit it. The
countdown threshold is refreshed when appropriate. Phase two retries the
submission after the gate clears, while phase six advances the completion
path through `func_10004FE0`.

Seventy-five of 84 retail words emit directly from semantic C. Nine
function- and offset-scoped guards normalize three branch distances, three
local branch/register choices, and one inserted `D_8003B23A` address
materialization. The insertion shifts the already matching tail into its
retail position; all calls, queue and task relocations, counter updates,
phase dispatch, and the epilogue otherwise emit directly.

The exhaustive stale-guard rebuild completes every padded object without a
guard failure. The expected whole-ROM SHA-1 check still fails because the
project contains unrelated non-matching functions. The authoritative matcher
and direct section-span comparison pass. The linked and retail spans share
SHA-256
`86b7fab90235a558ee8af0ac506a9eed2d888e0bbaef406bb763a1f3a4d66f74`.

The matcher advances to `3,105 / 5,457 (56.90%)` overall and
`422 / 488 (86.48%)` in Init, with zero address drift and 66 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
