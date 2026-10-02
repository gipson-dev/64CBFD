# Game owner-ID effect payload constructor match

Date: 2026-10-02

`func_150F5C08` replaces its zero-return placeholder with the 36-word retail
routine at `0x150F5C08..0x150F5C98`. Its four-argument contract builds a
12-byte payload containing the owner pointer, the owner's byte at offset
`0x3B`, three padding bytes, and a zero float.

The wrapper requests object type `0x51` through `func_15149130`, passing the
signed type selector, a 12-byte payload size, the unsigned variant, and the
final caller argument. When allocation succeeds, it copies the payload to
object offset `0x28`; a null result returns without copying.

The typed local payload reproduces retail's argument homes, owner-ID load,
stack payload layout, allocator arguments, conditional copy, frame, and
epilogue directly from semantic C. No expected-word guards, checked
insertions or omissions, relocation-aware rows, rodata anchor, or
compiler-profile override are required.

The full `NON_MATCHING=1` relink and linked matcher pass with zero address
drift. The linked span at file offset `0x123088` and retail span at `0x1230B8`
are identical across all 144 bytes, with SHA-256:

```text
3e0454c779174a16f23f0c473b717c27c75c4dc20711e5279db09e1837548818
```

The patch audit remains at 10,374 total rows, with zero rows for
`func_150F5C08` and no duplicate patch keys. The refreshed matcher reports
Game at `2,564 / 4,788 (53.55%)`, with 2,224 different C rows; overall
byte-exact C progress is `3,232 / 5,456 (59.24%)`. These aggregate figures
already included the live-tree match when the preceding checkpoint was
measured, so this commit does not claim an artificial one-function increase.
Init remains `487 / 487 (100.00%)` and Debugger remains
`181 / 181 (100.00%)`. `make tools-check` also passes. No fresh gameplay run
was performed.

Keep 32-word `func_150A76F0` in the raw-assembly workstream. Resume the
ordinary queue with 36-word `func_1510D374`, currently at 35 real
differences. The smaller 19-word `func_150F631C` remains a separate near-match
cleanup at four real differences.
