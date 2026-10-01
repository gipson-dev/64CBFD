# Init packed audio-state updater match

Date: 2026-10-01

`func_1000C530` occupies 174 words and 696 bytes at
`0x1000C530..0x1000C7E8`. The former implementation returned zero despite
being shared by several five-argument Init audio callbacks.

The recovered routine interprets its first argument as a packed state word.
Bits 0-1 select a sound state, bits 2-7 hold its transition timer, the next two
bytes carry a value and mode, and the high byte tracks a separate fade. A
pending request in `D_80041F08` and `D_80041F0C` can replace those fields while
preserving one active state-2 transition. The timer decreases by
`D_800BE9E4`; expiry clears the active state.

When the state changes, the routine stops the old sound slot and initializes
the new slot's value, mode flag, and mode magnitude. For an unchanged active
state, it submits only the fields that differ from the pending request. This
preserves the retail calls to `func_100085F8`, `func_10008824`,
`func_100086FC`, and `func_10008744` and their byte-width argument semantics.

Flag `0x10` in `D_80041F04` starts or refreshes the packed high-byte fade and
is consumed immediately. Each update subtracts the frame-scaled fade step; at
expiry the routine clears mask `0xC0` through `func_10008790`. Finally it
clears the one-shot state request and repacks all fields into the return value.

The semantic compile reproduces the complete frame, calls, relocations, branch
graph, and 174-word slot. One hundred thirty-eight linked words emit directly
from C. Thirty-six stale-checked non-relocating rows normalize one closed IDO
local-allocation cycle, three instruction-scheduling positions, and
commutative branch or XOR operand order.

The repository-wide stale-check build and final link pass. The authoritative
matcher no longer lists `func_1000C530`; the linked and retail 696-byte spans
share SHA-256
`0bb708b2a657dd68247bd5fc413a15779db6418cda26509bd6aaaefe644881fa`.
Project tool checks pass, and all 10 focused tool tests pass.

The checkpoint is `3,142 / 5,457 (57.58%)` overall and
`459 / 488 (94.06%)` in Init, with zero address drift and 29 genuinely
different Init C rows. The next unparked Init candidates are
`func_100052A0` and `func_10011BB8`, both 180 words.
