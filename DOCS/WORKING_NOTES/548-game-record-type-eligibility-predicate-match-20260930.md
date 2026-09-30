# Game record-type eligibility predicate byte match

Date: 2026-09-30

`func_150EC3D4` occupies 34 words and 136 bytes at
`0x150EC3D4..0x150EC45C`. It first rejects the comparison record itself and
records whose pointer at offset `0x0` is null. It rejects sentinel type
`0xFF`, then accepts type bytes `0`, `1`, `2`, `3`, `4`, `0x28`, and `0x77`.

Separate early returns recover retail's branch-likely loads. Promoting the
cached byte at offset `0x4` to `s32` gives it retail's `v0` lifetime and final
branch-delay update. The complete function emits directly from semantic C
with no expected-word guards.

The matcher advances by exactly one row to `3,051 / 5,462 (55.86%)` overall
and `2,472 / 4,788 (51.63%)` in Game with no address drift. Linked Game offset
`0xEC3D4` has SHA-256
`5f7e19ea141ba700d88ecee856c302cc37b327e096dc9a07b5b10aefd7c785a7`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
36-word Game `func_150FDD10`, the next ordinary matcher row.
