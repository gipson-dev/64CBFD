# Game midpoint-timestep integrator byte match

Date: 2026-09-30

`func_151CEA20` occupies 35 words and 140 bytes at
`0x151CEA20..0x151CEAAC`. It reads acceleration at offset `0x40` and old
velocity at `0x44`, advances velocity by `acceleration * D_800BE9A4`, and
advances position at `0x38` by the midpoint velocity times the same timestep.
It separately advances the scalar at `0x50` from the rate at `0x4C`, clamps
that scalar to an upper limit of `1.0f`, and returns one.

The recovered C retains acceleration and old velocity explicitly, exposing the
midpoint integration rather than rewriting it as a less precise sequence over
the newly stored velocity. It also preserves retail's three independent reads
of `D_800BE9A4` and its strict greater-than clamp.

Fourteen words emit directly from semantic C. Twenty-one stale-checked,
non-relocating guards normalize closed IDO FP-register-allocation cycles and
one equivalent schedule in which the compiler hoists the second rate/current
loads ahead of retail's position store. The function extent, memory offsets,
floating operations, three timestep loads, HI16/LO16 relocation pair, branch,
clamp condition, and return value are unchanged.

The focused object, complete replacement link, outer `NON_MATCHING=1` ROM
build, and authoritative matcher pass. The linked ELF and pristine
decompressed retail spans share SHA-256
`f62b31514b1fa56a41b3eb39f54ba112e9a37df616d6e21bc62f7c54c68cc0ef`.
The matcher advances exactly one row to `3,068 / 5,462 (56.17%)` overall and
`2,489 / 4,788 (51.98%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
34-word Game `func_151D66F0`, the next ordinary matcher row.
