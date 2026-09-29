# Game owned float-array allocator byte match

Date: 2026-09-29

## Scope and behavior

`func_15036C70` in `conker/src/game/generated_64120.c` spans 30 words and
120 bytes. It allocates `0x48` bytes, stores the result at owner offset
`0x324`, clears the block, then initializes two three-float arrays at block
offsets zero and `0xC` from `D_80098250`.

The recovered loop intentionally reloads the owner pointer for each store.
Retaining `D_80098250` once as a local float reproduces retail's single `f0`
load and avoids the larger address-register form produced by repeated extern
reads. All 30 words emit directly from C with no guards.

## Verification

- The focused padded object reproduces all 30 retail instructions.
- The complete ELF and binary relinked successfully.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `83af44c1f6ffc8a91ffd89ea28e4c8c6e7e34c55ca89db063f3437378fb516e1`.
- Fresh totals are `2,968 / 5,465 (54.31%)` overall and
  `2,394 / 4,789 (49.99%)` in Game, with one address-drift row.

## Resume boundary

Continue with the next ordinary 29-difference Game placeholder. Keep
`func_150AFBF4` parked at its documented 27-word direct-field versus 31-word
retained-pointer compiler boundary unless new source-shape evidence appears.
