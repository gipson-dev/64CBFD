# Game table-record dispatcher byte match

Date: 2026-09-30

`func_15024130` occupies 33 words and 132 bytes at
`0x15024130..0x150241B4`. It accepts a signed record count and a shared dispatch
argument. Positive counts walk the allocation referenced by `D_800C3D50` in
12-byte strides; zero and negative counts return without touching the table.

Each record supplies a word from offset zero, an unsigned byte from offset
eight, an unsigned halfword from offset `0xA`, and a second word from offset
four. The recovered loop forwards those four fields and the shared argument to
`func_1502A8A0`, then advances until the requested count is exhausted. The
routine has no defined return value, matching the callers and retail epilogue.

Thirty-two words emit directly from semantic C. One stale-checked,
non-relocating guard at `+0x3C` preserves retail's commutative table-base
addition operand order: retail emits `addu v0,t6,s1`, while IDO emits the
equivalent `addu v0,s1,t6`. The 56-byte frame, saved-register lifetime, global
relocation, field widths, five call arguments, loop branch, delay slots, and
epilogue all emit naturally.

The focused object, exhaustive shared-guard rebuild, complete relink,
authoritative matcher, direct span comparison, outer `NON_MATCHING=1` ROM
build, project tool checks, and whitespace check pass. The linked ELF and
pristine decompressed retail spans share SHA-256
`94b7a32ec40b961cc226a811d8b5e56961f489be88f3a66d0151e7a4aa3bbe50`.
The matcher advances exactly one row to `3,071 / 5,461 (56.24%)` overall and
`2,492 / 4,788 (52.05%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
34-word Game `func_15041480`, the next ordinary matcher row.
