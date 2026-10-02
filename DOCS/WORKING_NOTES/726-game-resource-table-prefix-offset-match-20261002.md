# Game resource-table prefix offset match

Date: 2026-10-02

`func_1510D374` replaces its zero-return placeholder with the 36-word retail
routine at `0x1510D374..0x1510D404`. It computes an address-like resource
offset by starting at linker symbol `D_1A37E0` and adding the first `arg0`
unsigned halfword lengths from `D_80091D20`.

The recovered signed count gate returns the base unchanged for zero or
negative counts. Positive counts use IDO's standard remainder loop followed
by a four-entry unrolled loop. Declaring the table as unsigned halfwords is
essential: retail uses `lhu` for every entry and accumulates each value into
the 32-bit offset.

The direct loop reproduces all 36 words, including the linker-base and table
relocations, modulo-four prologue, pointer construction, four-load unrolled
body, branch delay slots, and return. No expected-word guards, checked
insertions or omissions, relocation-aware rows, rodata anchor, or
compiler-profile override are required.

The full `NON_MATCHING=1` relink and linked matcher pass with zero address
drift. The linked span at file offset `0x13A7F4` and retail span at `0x13A824`
are identical across all 144 bytes, with SHA-256:

```text
f7f5772ba3623a9370e5013672480c7011e8285fb53031a1ebaff445b5c2aaac
```

The patch audit remains at 10,374 total rows, with zero rows for
`func_1510D374` and no duplicate patch keys. Game advances to
`2,565 / 4,788 (53.57%)`, with 2,223 different C rows; overall byte-exact C
progress is `3,233 / 5,456 (59.26%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Keep 32-word `func_150A76F0` in the raw-assembly workstream and 19-word
`func_150F631C` in the near-match cleanup queue. Resume the ordinary queue
with 38-word `func_15133FD8`, currently at 35 real differences.
