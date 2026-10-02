# Game resource-descriptor chain callback match

Date: 2026-10-02

`func_15133FD8` replaces its zero-return placeholder with the 38-word retail
routine at `0x15133FD8..0x15134070`, including the three trailing padding
words. It is the third callback in the `D_800899A4` table, following the two
single-descriptor wrappers `func_15133E84` and `func_15133EB8`.

The record byte at offset `0x170` is the descriptor count. Descriptors begin
four bytes later and occupy eight bytes each: an unsigned resource halfword,
an unsigned mode byte, one padding byte, and a 32-bit argument. The callback
threads the display-list pointer returned by `func_15133EEC` through every
descriptor and returns the final pointer. Its third callback argument is
unused but retains the retail argument home.

The recovered C emits the complete frame, four saved-register lifetimes,
count gate, descriptor loads, call loop, explicit eight-bit counter wrap, and
epilogue. Three expected-word guards normalize compiler ordering only: one
commutative descriptor-pointer addition and the independent publication order
of the masked counter and next display pointer. No insertion, omission,
relocation rewrite, rodata anchor, or compiler-profile override is required.

The full `NON_MATCHING=1` rebuild and linked matcher pass with zero address
drift. The linked span at file offset `0x161458` and retail span at `0x161488`
are identical across all 152 bytes, with SHA-256:

```text
98b177616f874a9ff4efd91cc06c17d68376c4add1ab90a680e07ab176dd1f2c
```

The patch audit advances to 10,377 total rows, with three rows for
`func_15133FD8` and no duplicate patch keys. Game advances to
`2,566 / 4,788 (53.59%)`, with 2,222 different C rows; overall byte-exact C
progress is `3,234 / 5,456 (59.27%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Keep 32-word `func_150A76F0` in the raw-assembly workstream and 19-word
`func_150F631C` in the near-match cleanup queue. Resume the ordinary queue
with 41-word `func_1513B798`, currently at 35 real differences.
