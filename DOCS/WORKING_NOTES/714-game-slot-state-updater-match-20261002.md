# Game slot-state updater match

Date: 2026-10-02

`func_1502FD70` replaces its zero-return placeholder with the 40-word retail
routine at `0x1502FD70..0x1502FE10`. The function uses byte four of its input
record as an index into the 187-byte state table `D_800D2040`.

When `D_80038080` is clear and the current category is `0x1D`, the indexed
state is set to two immediately. The normal path preserves the `0xFF` state
sentinel, reads an optional object pointer at input offset `0x144`, and inspects
that object's byte at `0x2E`. A null object or zero object value publishes the
fallback state three; object sentinel `0xFF` leaves the state unchanged.
Otherwise the object byte is multiplied by 30 and replaces the current state
only when the scaled value is larger.

The shared declaration of `D_800D2040` was corrected from an `s32[187]` to the
retail byte-array contract `u8[187]`. Its other known use clears exactly 187
bytes, so this correction also agrees with the existing reset behavior.

The semantic compile produces the complete control flow and 39 active
instructions plus the retail trailing pad. Seventeen expected-word guards
normalize one closed IDO sentinel-register and fallback-scheduling difference.
There are no relocation-aware rows, checked insertions or omissions, or
compiler-profile override.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked and retail 160-byte spans are identical, with
SHA-256:

```text
e5ec5315c14a42b47a9bdebb9eba5a33843891bf1d40343af65c5527ec07413e
```

The guard audit reports 17 rows for `func_1502FD70` and no duplicate patch
keys. Game advances to `2,554 / 4,788 (53.34%)`, with 2,234 different C rows;
overall byte-exact C progress is `3,222 / 5,456 (59.05%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with 35-word `func_1503D484`, currently
at 35 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
