# Game sentinel coordinate distance match

Date: 2026-10-02

`func_15086BD0` replaces its zero-return placeholder with the 40-word retail
routine at `0x15086BD0..0x15086C70`. The function accepts two record indices
and returns `0.0f` when either is the `0xFF` sentinel. Otherwise it addresses
two 16-byte records through `D_800D2350`, subtracts their signed 16-bit X, Y,
and Z coordinates, and returns the Euclidean distance with `sqrtf`.

The semantic C body naturally reproduces the complete floating-point
conversion, square, accumulation, square-root, and return sequence. IDO
hoists the `D_800D2350` high half into the second sentinel branch delay and
chooses an equivalent pointer/load order, while retail materializes the table
address after its early return. Thirteen expected-word replacements normalize
that closed allocation and scheduling difference. Two checked insertions
retain retail's empty sentinel delay and unreachable duplicate `jr ra`.

The patch set contains 15 rows: thirteen changed replacement rows and two
same-word insertion rows. Three replacements are relocation-aware for the
`D_800D2350` high and low halves. There are no checked omissions and no
compiler-profile override.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked span at file offset `0xB4050` and retail span at
`0xB4080` are identical across all 160 bytes, with SHA-256:

```text
b6800438a8c0f5cd9fbd3a632c1418bf8730e5d0b4a391e0d1f61f098450eb7a
```

The patch audit reports 10,358 total rows, 15 rows for `func_15086BD0`, two
checked insertions, zero omissions, and no duplicate patch keys. Game advances
to `2,560 / 4,788 (53.47%)`, with 2,228 different C rows; overall byte-exact
C progress is `3,228 / 5,456 (59.16%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

The fresh ordinary matcher queue begins with 31-word `func_15015F40` at 29
real differences, followed by 32-word `func_150A76F0` at 29. Resume with
`func_15015F40`, while preserving its documented indirect-table ownership
boundary unless new evidence resolves it.
