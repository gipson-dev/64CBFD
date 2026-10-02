# Game timed callback lifecycle match

Date: 2026-10-02

`func_1513B798` replaces its zero-return placeholder with the complete
41-word retail routine at `0x1513B798..0x1513B83C`. The callback is referenced
by the retail tables at `D_8008C008` and `D_8008C5B8`.

The record byte at offset `0x10` gates timer handling. When its low bit is
set, the signed halfword at offset `0x14` is reduced by `D_800BE9E4`; a
negative result completes the record. Otherwise, the signed callback index at
offset `0x11` selects an entry from `D_80089C18`. A missing callback uses the
`-1` sentinel, while a callback result of zero also completes the record.
Completed records are released through `func_1516972C`.

Semantic C emits 39 of the 41 words directly, including the 32-byte frame,
timer path, callback-table lookup, indirect call, argument lifetime, branch
delay slots, and release path. Two expected-word guards normalize only IDO's
choice to spill the completion flag as a 32-bit word at `sp+0x1C`; retail
spills the equivalent value as an unsigned byte at `sp+0x1B`. No insertion,
omission, relocation rewrite, rodata anchor, or compiler-profile override is
required.

The full `NON_MATCHING=1` rebuild and linked matcher pass with zero address
drift. The linked span at file offset `0x168C18` and retail span at `0x168C48`
are identical across all 164 bytes, with SHA-256:

```text
5156bec952b2fe5eb91ea175aff389e2a0663f3068d697ee4a3962b3702263ad
```

The patch audit advances to 10,379 total rows, with two rows for
`func_1513B798` and no duplicate patch keys. Game advances to
`2,567 / 4,788 (53.61%)`, with 2,221 different C rows; overall byte-exact C
progress is `3,235 / 5,456 (59.29%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Keep 32-word `func_150A76F0` in the raw-assembly workstream and 19-word
`func_150F631C` in the near-match cleanup queue. Resume the ordinary queue
with 50-word `func_15145128`, currently at 35 real differences.
