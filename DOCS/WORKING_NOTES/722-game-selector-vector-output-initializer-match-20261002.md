# Game selector vector output initializer match

Date: 2026-10-02

`func_150B060C` replaces its zero-return placeholder with the 41-word retail
routine at `0x150B060C..0x150B06B0`. The function accepts an 8-bit selector
and a 24-byte output record. It resolves the selector through
`func_151149AC`, stores the resulting record pointer at output offset `0x08`,
and returns zero when the lookup fails. On success it stores `-150.0f` and
`4.5f` at offsets `0x00` and `0x04`, converts the record's signed 16-bit
coordinates at offsets `0x10`, `0x12`, and `0x14` to floats, stores them at
output offsets `0x0C`, `0x10`, and `0x14`, and returns one.

A local typed output record captures the mixed float/pointer layout. Reading
the successful record through the output's pointer field, rather than keeping
a separate local pointer, reproduces retail's lifetime: IDO stores and tests
the call result, materializes both float constants, then reloads the pointer
before the coordinate conversions. The complete frame, call, failure path,
success stores, and epilogue emit directly from semantic C.

No expected-word guards, checked insertions or omissions, relocation-aware
rows, rodata anchor, or compiler-profile override are required.

The full `NON_MATCHING=1` relink and linked matcher pass with zero address
drift. The linked span at file offset `0xDDA8C` and retail span at `0xDDABC`
are identical across all 164 bytes, with SHA-256:

```text
713acb8539817349671fea8039b517b6ed788660a0f45d6eff55b0f79f48dd89
```

The patch audit remains at 10,358 total rows, with zero rows for
`func_150B060C` and no duplicate patch keys. Game advances to
`2,562 / 4,788 (53.51%)`, with 2,226 different C rows; overall byte-exact C
progress is `3,230 / 5,456 (59.20%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Keep 32-word `func_150A76F0` in the raw-assembly workstream. Resume the
ordinary queue with 40-word `func_150DF820`, currently at 35 real differences.
