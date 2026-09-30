# Game motion timestep integrator byte match

Date: 2026-09-30

`func_150DEACC` occupies 35 words and 140 bytes at
`0x150DEACC..0x150DEB58`. It advances the three coordinates at offsets
`0x34`, `0x38`, and `0x3C` by their velocities at offsets `0x110`, `0x114`,
and `0x118` multiplied by global timestep `D_800BE9A4`. It then subtracts the
same timestep from vertical speed at offset `0x11C` and returns whether the
updated speed is nonnegative.

Keeping an explicit pointer to the timestep recovers retail's repeated global
loads and exact floating-point schedule. The complete function emits directly
from semantic C with no expected-word guards.

The matcher advances by exactly one row to `3,050 / 5,462 (55.84%)` overall
and `2,471 / 4,788 (51.61%)` in Game with no address drift. Linked Game offset
`0xDEACC` has SHA-256
`c1609045c6bc30f63ae3ffa4404d008a6ac91ec834ded44a1135c11840981ae3`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
34-word Game `func_150EC3D4`, the next ordinary matcher row.
