# Game indexed 64-bit flag query byte match

Date: 2026-09-29

`func_1501D2C4` occupies 33 words and 132 bytes at
`0x1501D2C4..0x1501D348`. When global byte `D_800C3670` is nonzero it returns
true immediately. Otherwise it tests bit `arg1` in the 64-bit value at
`D_800C3A60[arg0]` and returns a normalized boolean result. This is the
read-side companion to `func_1501D258`, which sets the same indexed bit.

The recovered typed body naturally emits the 24-byte frame, incoming argument
homes, `__ll_lshift` call for `1LL << bit`, paired high/low array loads, split
word masks, and retail's boolean branches. No expected-word guards are needed.

The production generated object, non-matching link, and fresh matcher succeed.
The matcher reports `3,045 / 5,463 (55.74%)` overall and
`2,466 / 4,789 (51.49%)` in Game with no address drift. Linked Game offset
`0x1D2C4` and retail ROM offset `0x4A774` share SHA-256
`75bd476d39efde90ed25537c9acdc86d0d2ef7744c55d1c4340db96d33a8ad54`.
The replacement payload build, outer non-matching ROM build, project tool
checks, and all 10 tool unit tests also pass.

Keep Game `func_15015F40` and `func_150A76F0`, Game `func_15106E78`, and Init
`func_1000FF90` parked at their documented ownership/compiler boundaries.
Resume with 32-word Game `func_1503B7C0`, the next ordinary matcher row.
