# Init record cleanup match

Date: 2026-09-30

`func_1000DEC4` occupies 41 words and 164 bytes at
`0x1000DEC4..0x1000DF68`. It scans the 12 records in `D_800419A8`. Records
whose primary identifier is already `-1` have any remaining secondary
identifier reset. Active records whose state query returns zero release their
entry in `D_800417B0` and reset both identifiers. Every iteration also clears
the final four bytes of the record.

The indexed C loop already gives IDO retail's `struct137` cursor, end pointer,
saved-register set, and branch-likely cleanup schedule. Expressing `pad60` and
`pad62` as one 32-bit store recovers retail's branch-delay clear. Declaring
`func_1000853C` without a parameter prototype preserves its byte-typed
definition but prevents an unnecessary caller-side argument conversion; the
caller's explicit `& 0xFF` then emits directly as retail's `andi a0,v0,0xFF`
call-delay instruction. All 41 words emit directly from semantic C with no
word guards.

The focused compact-object inspection, complete relink, authoritative
matcher, and direct section-span comparison pass. The linked ELF and retail
spans share SHA-256
`01b0138764c7dd80ffaa2bdfa297452223ede4057776661b7927b7ef467dbb0c`.
The matcher advances to `3,083 / 5,458 (56.49%)` overall and
`400 / 489 (81.80%)` in Init, with zero address drift and 89 genuinely
different Init C rows.

Resume with the remaining Init queue after the parked `func_1000FF90`.
