# Game actor water-state flag transition match

Date: 2026-10-02

`func_150DF820` replaces its zero-return placeholder with the 40-word retail
slot at `0x150DF820..0x150DF8C0`. The callback clears actor flag `0x4000`, sets
flag `0x0004`, and clears flags `0x1010`, retaining each intermediate write.
It then tests the attached `struct127::in_water` byte at offset `0xAD`.

When the attached actor is in water, the callback restores flags `0x1010`,
clears flag `0x0004`, and writes the distinct `D_800A0F60` symbol containing
`750.0f` to actor field `0x374`. Otherwise, when field `0x374` equals the
separate `D_800A0F64` symbol containing the same value, it stores state `3` at
offset `0x1B4` and calls `func_15124B18`.

Direct volatile stores retain the three opening intermediate writes while a
normal first store in the water path lets IDO preserve the original 38-word
active body and two trailing padding words. The frame, memory offsets, branch
layout, delay slots, float-symbol relocations, and call relocation all match
the retail routine. Sixteen guarded replacements normalize one closed integer
register-allocation chain; no insertion, omission, rodata anchor, or compiler
profile override is required.

The full `NON_MATCHING=1` rebuild and linked matcher pass with zero address
drift. The linked span at file offset `0x10CCA0` and retail span at `0x10CCD0`
are identical across all 160 bytes, with SHA-256:

```text
94c33e1d4697aea9963e125e120fd14b5610a16e3ec70bf0d5fd95c923cfb70d
```

The patch audit reports 10,374 total rows, 16 rows for `func_150DF820`, and no
duplicate patch keys. Game advances to `2,563 / 4,788 (53.53%)`, with 2,225
different C rows; overall byte-exact C progress is
`3,231 / 5,456 (59.22%)`. Init remains `487 / 487 (100.00%)` and Debugger
remains `181 / 181 (100.00%)`. `make tools-check` also passes. No fresh
gameplay run was performed.

Keep 32-word `func_150A76F0` in the raw-assembly workstream. Resume the
ordinary queue with 36-word `func_150F4D5C`, a five-argument
record-construction wrapper in `generated_121A20.c`, currently at 35 real
differences.
