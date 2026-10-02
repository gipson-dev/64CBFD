# Game trailing marked-record compactor match

Date: 2026-10-02

`func_1503DDD0` replaces its zero-return placeholder with the 40-word retail
slot at `0x1503DDD0..0x1503DE70`. The function occupies 37 active words through
`0x1503DE64`; the generated-slice layout supplies the three trailing retail pad
words.

The recovered routine rejects negative indexes and indexes at or beyond
`D_800C6654`. A valid selection sets the 20-byte record's halfword at offset
six to state bit `2`. It then scans backward from the final active record,
decrementing `D_800C6654` while trailing records retain that bit.

The retail load before indexed access also corrects the global declaration:
`D_800C6650` owns a `struct160 *`, rather than inline `struct160` storage. The
semantic compile recovers the complete extent, validation, selected-record
store, loop, and exits. Sixteen expected-word replacements normalize one
closed IDO tail-compaction register and instruction schedule. No checked
insertions, omissions, relocation-aware rows, or compiler-profile override are
required.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked span at file offset `0x6B250` and retail span at
`0x6B280` are identical across all 160 bytes, with SHA-256:

```text
dafe46e99fdd57fc91a2bd4f616b07427bceabcc65b21016d5160b1e30690005
```

The patch audit reports 10,343 total rows, exactly sixteen rows for
`func_1503DDD0`, no omissions, and no duplicate patch keys. Game advances to
`2,557 / 4,788 (53.40%)`, with 2,231 different C rows; overall byte-exact C
progress is `3,225 / 5,456 (59.11%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Continued in
[Working Note 718](718-game-sixteen-word-varargs-adapter-match-20261002.md),
which matches `func_15042E3C`. Resume the ordinary small-Game queue with
35-word `func_150634E4`, currently at 35 real differences. Keep
`func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
