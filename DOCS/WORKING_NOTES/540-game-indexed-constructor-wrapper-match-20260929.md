# Game indexed constructor wrapper byte match

Date: 2026-09-29

`func_1501D1D4` occupies 33 words and 132 bytes at
`0x1501D1D4..0x1501D258`. It calls `func_1502B6BC` with pointers to two local
outputs, zero, constants `3` and `6`, and the first two incoming arguments.
The third argument selects a `D_800C3668` slot. A successful returned handle
is stored in that slot; failure explicitly clears it. The function returns the
same handle or null result.

The recovered typed body naturally emits retail's 56-byte frame, incoming
argument homes, seven-argument call setup, success/failure branches, indexed
stores, and return lifetime. Declaring the second call output before the first
accounts for IDO's reverse local allocation and places the call pointers at
retail's `sp+0x30` and `sp+0x34`. No expected-word guards are needed.

The production generated object, non-matching link, and fresh matcher succeed.
The matcher reports `3,044 / 5,463 (55.72%)` overall and
`2,465 / 4,789 (51.47%)` in Game with no address drift. Linked Game offset
`0x1D1D4` and retail ROM offset `0x4A684` share SHA-256
`05f16c6812cc11dc9363f53b441b15cb02723d07be71832972168ba7fce45f85`.
The replacement payload build, outer non-matching ROM build, project tool
checks, and all 10 tool unit tests also pass.

Keep Game `func_15015F40` and `func_150A76F0`, Game `func_15106E78`, and Init
`func_1000FF90` parked at their documented ownership/compiler boundaries.
Resume with adjacent 33-word Game `func_1501D2C4`, the next ordinary matcher
row.
