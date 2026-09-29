# Game type-selector state handler byte match

Date: 2026-09-29

## Scope and behavior

`func_15033440` in `conker/src/game/generated_5D2C0.c` spans 30 words and
120 bytes. Selectors `0x27` and `0x35` share a path that requires the second
record's byte at offset five to equal five, clears the first record's state
byte at offset two, and increases its signed halfword at offset `0x22` by
`D_800BE9E4 * 0xAAA`. Selector `0x29` performs only the gated state-byte
clear. Other selectors are ignored, and the function returns zero.

A direct three-case `switch` reproduces retail's selector comparisons,
branch-likely exits, shared path, unsigned multiply, and branch-delay store.
All 30 words emit directly from C with no guards.

## Verification

- The focused padded object reproduces all 30 retail instructions.
- The complete ELF and binary relinked successfully.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `d3bddf169bbc128bf1dc34ca2573abeb8614985e05818949bf18e7ee6be2afcb`.
- Fresh totals are `2,967 / 5,465 (54.29%)` overall and
  `2,393 / 4,789 (49.97%)` in Game, with one address-drift row.

## Resume boundary

`func_150AFBF4`'s semantics were recovered during selection, but direct fields
emit 27 words while a retained pointer emits 31; both experiments were
removed. Continue with the next ordinary 29-difference Game placeholder and
keep that pointer-lifetime case parked unless new source-shape evidence appears.
