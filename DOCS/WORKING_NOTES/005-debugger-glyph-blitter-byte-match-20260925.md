# Working Note 005: Debugger Glyph Blitter Byte Match

Date: 2026-09-25

## Result

`func_160014F0` is byte-exact in the linked US ELF. The restored C retains the
retail 71-word body, ANSI `u8` normalization prologue, four-pixel unroll,
glyph-pointer induction, destination update, and branch delay slots.

The linked checkpoint is:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,522 / 5,497 (45.88%) | 1 | 2,974 |
| Init | 387 / 508 (76.18%) | 1 | 120 |
| Game | 1,959 / 4,808 (40.74%) | 0 | 2,849 |
| Debugger | 176 / 181 (97.24%) | 0 | 5 |

## Allocation Boundary

The remaining 19 words were one coherent IDO allocator rotation through
glyph setup, four unrolled pixel-mask tests, the final shifted-bit value, and
the destination-stride calculation. Pointer and split-index source forms
either rotated persistent loop registers or changed instruction scheduling;
the existing index form preserves all retail control and data flow.

Three setup instructions also require retail's order: form the glyph pointer,
initialize the row, then complete the `D_160038A8` address. Moving only those
words would leave `R_MIPS_LO16:D_160038A8` attached to the wrong instruction.
`pad_c_object.py` therefore supports optional expected and replacement
relocation lists. The table moves the relocation with the low-half load and
fails if either the compiled word or expected relocation differs.

## Verification

The relocation-movement test and existing cross-body padding test pass. A
full shared-tool rebuild succeeded, the US ELF relinked, and the linked retail
scan no longer lists `func_160014F0`.

## Sibling Applicability

`64CBFDOGL` consumes a generated recomp translation of `func_160014F0`; it
does not use this IDO C source or the retail-padding tool. No sibling source or
tool change applies. Its existing dirty work was left untouched, and frozen
Release was neither built nor launched.

## Resume Boundary

Continue with debugger `func_16001BB4`. The matcher reports 27 real
differences, while the restored SDK `_Printf` body remains 401 words against
retail's 402. Isolate the known final `_PAD`/loop-back branch schedule before
changing the formatter body. Keep `func_15135480` as a separate game follow-up.
