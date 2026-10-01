# Init channel-state initializer match

Date: 2026-09-30

`func_1000E934` occupies 88 words and 352 bytes at
`0x1000E934..0x1000EA94`. The former zero-return placeholder is replaced with
the recovered three-channel audio-state initializer.

For each channel, the routine fills paired 16-entry tables with `0x8000` and
`0x100`, calls `func_10008F24`, and clears four per-channel state arrays. It
then clears the 1,200-byte `D_800419A8` record table, resets `D_800419A0`, and
sets the `unk4` sentinel to `-1` in all 12 records using the retail four-record
unroll.

Fifty-nine of 88 retail words emit directly from semantic C. Twenty-nine
function- and offset-scoped guards normalize the opening low-address schedule,
the independent stores in the 16-entry fill, and the outer-loop pointer/store
schedule. Relocation-aware guards verify and move the six affected low-address
relocations. No instructions are inserted or omitted, and the compact body
retains the exact 88-word extent.

The exhaustive stale-guard rebuild compiles and links every padded object
without a guard failure. The authoritative matcher and direct 352-byte
section-span comparison pass. The linked and retail spans share SHA-256
`58dda18e23f8c45a173a8db40555b9ece0d587592ff475e28a82a03c5f3e866c`.

The matcher advances to `3,111 / 5,457 (57.01%)` overall and
`428 / 488 (87.70%)` in Init, with zero address drift and 60 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
