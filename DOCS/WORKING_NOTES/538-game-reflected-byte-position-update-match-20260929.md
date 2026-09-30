# Game reflected byte-position update byte match

Date: 2026-09-29

`func_151E55A8` occupies 33 words and 132 bytes at
`0x151E55A8..0x151E562C`. It reads direction byte `D_800E0B98` and position
byte `D_800E0B97`. Direction zero applies `D_800BE9E4 << 3`; direction one
applies the negated step. A result at or above 256 reflects around 510, while
a negative result is negated. Either reflection toggles the direction byte,
and the final position is stored back as a byte.

The recovered `void func_151E55A8(void)` body emits the complete retail
instruction stream directly from C. Widening the direction local to `s32` and
separating the position load from its addition recover retail's `v0`
direction, `v1` offset, and `a0` position lifetimes. The branches, delay slots,
global relocations, arithmetic, and final stores all match without expected-
word guards.

The production generated object, non-matching link, and fresh matcher succeed.
The matcher reports `3,042 / 5,463 (55.68%)` overall and
`2,464 / 4,789 (51.45%)` in Game with no address drift. Linked Game offset
`0x1E55A8` and retail ROM offset `0x212A58` share SHA-256
`2b2a6d2d094e1dafe4f418b34038e4ec1b09c2026358f7dd2694bd6776965182`.
The replacement payload build, outer non-matching ROM build, project tool
checks, and all 10 tool unit tests also pass.

Keep Game `func_15015F40` and `func_150A76F0`, Game `func_15106E78`, and Init
`func_1000FF90` parked at their documented ownership/compiler boundaries.
Resume with 38-word Init `func_1000B1FC`, the next ordinary matcher row.
