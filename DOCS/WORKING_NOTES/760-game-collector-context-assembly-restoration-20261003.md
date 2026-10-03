# Game Collector / Context Assembly Restoration

Checkpoint: 2026-10-03. Continues the interrupted 2026-10-02 restoration.

## Scope

`generated_D0F20.c` now owns the original assembly through 23 tracked fragments
instead of zero-return placeholders. The six inventory groups cover ROM
`0xD0F20..0xD2570`, VMA `0x150A3A70..0x150A50C0`: 5,712 bytes.
The ignored original `conker/asm/D0F20.s` reference is unchanged.

The collector saves general registers in floating registers, uses interior
entries and shared cleanup, and cannot be restored as isolated ordinary ABI C
functions. Its opening cross-fragment branch now uses
`func_150A49F4+0xA0`, preserving target `0x150A4A94` and word `0x11000406`.
No new word guards or tool-framework changes were needed. Existing interior
absolute aliases and the six-group inventory remain intact.

## Verification

- Full code build and linked progress regeneration pass.
- All 5,712 linked bytes equal retail; SHA-256:
  `1986046720a68f120f612d0de32520c4cb623fc396d13b46073add33be6de04f`.
- Three new tests verify ownership, contiguous reference words, standalone
  assembly/link bytes, and the shared-cleanup branch. All 167 tool tests pass.
- Project checks pass. Constructor, allocator, list pass, overlap, wrapper,
  and the 27-word neighboring `func_15045714` remain exact.
- Both complete Init sections remain exact; hashes are recorded in Note 761.

Original odd floating-register assembler warnings are expected for the
handwritten encodings; byte comparison confirms preservation. No gameplay
execution or host-port build was performed.

## Progress / Next

This corrects false C ownership, not C-decomp completion. Total C rows are
5,455 / 6,042; Game C rows 4,782 / 5,321. Exact C numerators remain 3,255
overall and 2,582 Game, with 2,200 differing Game rows and zero drift.

The collector/context dependency of `func_150450CC` and `func_1510F800`
is no longer a zero-return placeholder. The highest-height query remains a
non-matching semantic C recovery; natural gameplay qualification is still
open. An ordinary next Game candidate is `func_15045384`, separately scoped.
