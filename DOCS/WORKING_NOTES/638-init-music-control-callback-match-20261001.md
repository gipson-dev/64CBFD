# Init music-control callback match

Date: 2026-10-01

`func_1000BCBC` occupies 169 words and 676 bytes at
`0x1000BCBC..0x1000BF5C`. The former C implementation returned zero even
though the function is one of the music callback-table routines used by the
game's runtime audio policy.

On its first invocation, the recovered callback initializes channel 3 to
level `0x10`, clears channel 4, and returns state 1. Later invocations retain
their incoming state unless scene `0x13` is active. In that scene, the routine
computes a squared two-axis distance from the retail reference coordinates,
uses the configured falloff constants to derive channel 3's byte level, and
updates that channel only when the level changes.

The callback then queries event `0x4041`. While the event is inactive it
derives channel 4's level from the third coordinate and the second set of
retail falloff constants, clamping to `0x20..0xFF`; while active it selects
zero. The channel is written only when its current value differs.

The semantic source restores the retail 32-byte frame, five-argument ABI,
branch topology, float comparisons, unsigned conversions, and complete
169-word extent. Ninety-nine words emit directly from C. Seventy
stale-checked rows normalize closed IDO register-allocation and scheduling
cycles around the two float-to-unsigned conversions. Relocation-aware rows
preserve both calls and the `D_8002C230`/`D_8002C234` constant loads that move
within the second cycle.

A repository-wide stale-check rebuild and authoritative linked matcher pass
classify the function byte-exact. The linked and retail 676-byte spans share
SHA-256
`a480744a95151b2487e577091d004e331f215c5f2fa8feb1583a958d2ad8ff9e`.
Project tool checks and all 10 tool unit tests pass.

The matcher advances to `3,137 / 5,457 (57.49%)` overall and
`454 / 488 (93.03%)` in Init, with zero address drift and 34 genuinely
different Init C rows.
