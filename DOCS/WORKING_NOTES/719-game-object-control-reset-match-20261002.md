# Game object control reset match

Date: 2026-10-02

`func_150634E4` replaces its zero-return placeholder with the 35-word retail
routine at `0x150634E4..0x15063570`. The function accepts an object from the
26-entry `D_800CC2D0` pool, derives its index, and rebuilds the canonical pool
pointer. It clears attached-state bytes `0x78` and `0x11A`, dispatches object
controls `0x1D` and `0x1E` through `func_150836CC`, then clears the original
object's jump-disable, run-disable, and state bytes.

The generated slice's local declaration of `D_800CC2D0` is corrected from an
untyped byte array to its existing `struct127` array contract. Using the
signed pool-offset division as an `s32` index and casting that index to `u32`
for the array access prevents IDO from sharing the divisor with pointer
scaling. IDO therefore reproduces retail's immediate division and exact
shift/add multiplication sequence. The complete frame, repeated attached
pointer loads, calls, stores, and epilogue emit directly from C.

No expected-word guards, checked insertions or omissions, relocation-aware
rows, or compiler-profile override are required. The neighboring matched
`func_150636A4` retains its byte-exact output after an explicit byte-pointer
cast preserves its prior pool-offset arithmetic.

The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with zero
address drift. The linked span at file offset `0x90964` and retail span at
`0x90994` are identical across all 140 bytes, with SHA-256:

```text
8fab1baad2b3f222dc0235ac2e99626d06fc2d0cb2b5a6e4b6c263985702cdb8
```

The patch audit reports 10,343 total rows, zero rows for `func_150634E4`, and
no duplicate patch keys. Game advances to `2,559 / 4,788 (53.45%)`, with
2,229 different C rows; overall byte-exact C progress is
`3,227 / 5,456 (59.15%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`. `make tools-check` also passes. No fresh
gameplay run was performed.

Continue with
[Working Note 720](720-game-sentinel-coordinate-distance-match-20261002.md),
which completes 40-word `func_15086BD0`. Its fresh matcher scan returns
31-word `func_15015F40` as the next ordinary row at 29 real differences;
preserve the documented indirect-table ownership boundary unless new evidence
resolves it.
