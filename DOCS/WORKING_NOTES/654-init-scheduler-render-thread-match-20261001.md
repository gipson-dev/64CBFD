# Init scheduler and render thread match

Date: 2026-10-01

`func_100049E0` occupies 244 words and 976 bytes at
`0x100049E0..0x10004DB0`. Its previous C body was an empty placeholder even
though the retail routine is the Init scheduler and render-thread message
loop.

The recovered semantic body initializes the scheduler state, receives the
seven message classes through `D_8003B218`, and dispatches them through the
retail jump table at `jtbl_8002C0A0_init`. It notifies registered clients on
retrace, maintains frame counters, arms the delayed task timer, handles SP
yield and completion paths, starts pending graphics tasks, advances idle
render work, and starts controller reads while shutdown is inactive. The C
case order follows retail's `0, 2, 1, 3, 6` block layout.

IDO emits the complete live behavior in 239 words with a `0x70` frame instead
of retail's `0x68` frame. It also chooses one shared constant register and a
long-lived `D_8002AC6C` address where retail uses two independent constant
registers and local address materialization. Ninety-one words emit directly
from semantic C. One hundred fifty function-scoped, stale-checked rows
normalize the closed frame, register-allocation, scheduling, and branch-offset
differences. That set contains 148 replacements and five insertions: the
retail status-result move and four unreachable alignment/epilogue words.
Forty-four rows explicitly preserve or move HI16, LO16, J26, or jump-table
relocations; no resolved-address binary patch is used.

The object-specific `RETAIL_RODATA_SYMBOL` mapping keeps the compiler-emitted
switch references anchored to the existing `jtbl_8002C0A0_init` assembly
data. A targeted object rebuild accepts every expected word and relocation,
and the full linked ELF completes successfully. Direct comparison of
`0x100049E0..0x10004DB0` reports zero different bytes. Both 976-byte spans
share SHA-256
`623dd58fd193533d32ee6d6c98a80c1d07bf0926bef273f14b9b58e8f79d68ad`.

The refreshed matcher reports `3,152 / 5,456 (57.77%)` byte-exact C functions
overall and `469 / 487 (96.30%)` in Init, with zero address drift and 18
different Init C rows. The next measured Init candidate is the 252-word
`func_1000BF60`, currently different in 251 words.
