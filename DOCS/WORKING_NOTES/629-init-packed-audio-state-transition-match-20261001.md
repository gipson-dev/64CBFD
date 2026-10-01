# Init packed audio state transition match

Date: 2026-10-01

`func_1000C350` occupies 120 words and 480 bytes at
`0x1000C350..0x1000C530`. The former implementation returned zero. Its
recovered five-argument callback signature matches the neighboring audio-state
routines; the final three floating-point arguments are part of that callback
contract but are not consumed by this transition.

When bit `0x80` is clear, the routine sets it and performs first-entry setup.
The ordinary path enables masks `0x1E` and `1` for the selected channel and
sets sound record `0x23` to `0x61A8`. Mode 3 instead applies value `0xFA` and
submits transition 2. Mode 6 applies channel masks `0x1E` and `1` with values
1 and `0x40`, then submits the same transition.

For an already-active state outside level `0x1D`, the routine clears the
selected channel through `func_10008F24`. In level `0x1D`, it compares the low
seven packed state bits with `D_80041F08`. State 1 clears mask `0x1E` and sets
mask 1 to `0x40`; state 2 sets mask `0x18` to `0xFF`, clears mask 6, and sets
mask 1. The return value combines the synchronized state with bit `0x80`.

The recovered C reproduces the complete 120-word frame, calls, branch graph,
delay slots, and epilogue. One stale-checked non-relocating row changes only the
commutative `beql` operand order at function offset `0x12C`; the other 119
words emit directly from C.

The complete ELF link passed. The authoritative matcher no longer lists
`func_1000C350`; direct comparison of all 480 bytes reports zero differences,
and the linked and retail spans share SHA-256
`e3002a2667674611eea979e4716e2117d436bb7d3878a2c78c71062948187d99`.
Project tool checks pass. The focused unit suite passes all 10 tests, with 8
expected skips.

The matcher advances to `3,128 / 5,457 (57.32%)` overall and
`445 / 488 (91.19%)` in Init, with zero address drift and 43 genuinely
different Init C rows.
