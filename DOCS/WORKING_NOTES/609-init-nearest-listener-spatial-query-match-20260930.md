# Init nearest-listener spatial query match

Date: 2026-09-30

`func_100114D0` occupies 85 words and 340 bytes at
`0x100114D0..0x10011624`. The former empty placeholder is replaced with the
recovered nearest-listener spatial query and output-scale wrapper.

The routine scans `D_80041F68[0..D_80082FA0]` for the entry with the lowest
unsigned squared distance from the incoming position. A zero global count
retains entry zero as the default. It passes the position relative to both
coordinate triplets in the selected entry, the selected field at `0x18`, and
the remaining caller arguments to `func_1000A420`. The returned local value is
multiplied by the caller scale, shifted right by 15, and stored through the
final output pointer.

Thirty-five of 85 retail words emit directly from semantic C and retained
slot padding. Fifty function- and offset-scoped guards normalize the opening
global-address schedule, one closed register allocation through the scan,
selected-entry field loads, call argument setup, the local-result slot, and
the output multiply/store schedule. No instructions are inserted or removed;
the complete loop, branches, call relocation, and epilogue retain their retail
positions.

The exhaustive stale-guard rebuild compiles and links every padded object
without a guard failure. The expected whole-ROM SHA-1 check still fails
because the project contains unrelated non-matching functions. The
authoritative matcher and direct 340-byte section-span comparison pass. The
linked and retail spans share SHA-256
`eb9ee13fc4faf8a4bbbf4cfffbff5e90d51e1bd6d88e9c403f52ba91c0b67818`.

The matcher advances to `3,108 / 5,457 (56.95%)` overall and
`425 / 488 (87.09%)` in Init, with zero address drift and 63 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
