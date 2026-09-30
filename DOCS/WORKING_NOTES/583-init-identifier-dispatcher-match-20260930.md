# Init identifier dispatcher match

Date: 2026-09-30

`func_1000DE1C` occupies 42 words and 168 bytes at
`0x1000DE1C..0x1000DEC4`. It masks the incoming identifier to 12 bits. A
nonzero identifier is dispatched directly through `func_1000D96C`; identifier
zero first runs `func_1000DEC4`, asks `func_1000B548` for a local identifier
list, and dispatches each positive entry with the caller's mode argument.

Masking `arg0` in place rather than introducing a separate `id` local recovers
retail's parameter-copy, mask, branch-delay assignment, `0x48` frame, and the
complete loop/call schedule. Forty words emit directly from semantic C. Two
stale-checked guards move only the compiler's local three-entry array address
from `sp+0x3C` to retail's dead-tail layout at `sp+0x34`; neither word carries
a relocation or changes behavior.

The focused object, exhaustive guard-dependent rebuild, complete relink,
authoritative matcher, and direct span comparison pass. The linked ELF and
retail spans share SHA-256
`10798837035d04b29314204b925729e8be19c77d5ef415a9eacf8f24bfad8bff`.
The matcher advances to `3,082 / 5,458 (56.47%)` overall and
`399 / 489 (81.60%)` in Init, with zero address drift and 90 genuinely
different Init C rows.

Resume with the remaining Init queue after the parked `func_1000FF90`.
