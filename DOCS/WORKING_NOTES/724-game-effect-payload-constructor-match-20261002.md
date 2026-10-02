# Game effect payload constructor match

Date: 2026-10-02

`func_150F4D5C` replaces its zero-return placeholder with the 36-word retail
routine at `0x150F4D5C..0x150F4DEC`. Its fixed five-argument contract builds a
12-byte payload containing the owner pointer, a zero float, a signed selector
byte, and an unsigned variant byte.

The wrapper requests effect type `0x56` through `func_15149130`, passing a
12-byte payload size plus the final two caller arguments. When allocation
succeeds, it copies the payload to object offset `0x28`; a null result returns
without copying.

The typed local payload reproduces retail's argument homes, signed and
unsigned byte loads, stack payload layout, allocator arguments, conditional
copy, frame, and epilogue directly from semantic C. No expected-word guards,
checked insertions or omissions, relocation-aware rows, rodata anchor, or
compiler-profile override are required.

The full `NON_MATCHING=1` relink and linked matcher pass with zero address
drift. The linked span at file offset `0x1221DC` and retail span at `0x12220C`
are identical across all 144 bytes, with SHA-256:

```text
7eb5f210d8c4271a307b2dea1e317de0c5a1c4fc93fb36f6840c9b2cd3f234ba
```

The patch audit remains at 10,374 total rows, with zero rows for
`func_150F4D5C` and no duplicate patch keys. Game advances to
`2,564 / 4,788 (53.55%)`, with 2,224 different C rows; overall byte-exact C
progress is `3,232 / 5,456 (59.24%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Keep 32-word `func_150A76F0` in the raw-assembly workstream. Resume the
ordinary queue with 36-word `func_150F5C08` in `generated_1228D0.c`, currently
at 35 real differences.
