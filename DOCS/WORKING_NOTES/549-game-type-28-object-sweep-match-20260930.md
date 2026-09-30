# Game type-0x28 object sweep byte match

Date: 2026-09-30

`func_150FDD10` occupies 36 words and 144 bytes at
`0x150FDD10..0x150FDDA0`, including three trailing padding words. It first
calls `func_15103828`. When mode byte `D_800C35EA` is one, it walks the 25
`0x32C`-byte object records from `D_800CC2D0` up to `D_800D121C`; each record
whose byte at offset `0x4` is `0x28` is passed to
`func_150ED638(record, 0x14, 0x14)`.

The semantic loop recovers retail's 40-byte frame, incoming argument spill,
saved-register lifetime, branch-likely updates, calls, and padding. IDO keeps
the end pointer in `s1` and target type in `s2`, while retail uses the reverse.
Five stale-checked guards normalize that closed allocation cycle. Retail does
not define a return value, so the historical `s32` signature deliberately
leaves `v0` unspecified.

The matcher advances by exactly one row to `3,052 / 5,462 (55.88%)` overall
and `2,473 / 4,788 (51.65%)` in Game with no address drift. Linked Game offset
`0xFDD10` has SHA-256
`56ee5e91620600813e41fa84f7931a7b38a7fecfc30d645b6c37ac1f89edf5fc`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_1510B32C`, the next ordinary matcher row.
