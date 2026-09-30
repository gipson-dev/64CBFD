# Game collision-classifier wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_15046C80` in `conker/src/game/generated_71820.c` occupies 32 words and
128 bytes at `0x15046C80..0x15046D00`. It classifies an input position and
collision record through `func_15047004`. Classification zero delegates to
`func_1504697C` with the original 16-bit selector, class one returns false,
and class two returns true.

## Source recovery

The previous body was a false zero-return placeholder. The recovered routine
uses the same three-way switch shape as the nearby byte-exact
`func_1504530C`, extended to the observed four-argument ABI. Explicit
prototypes for the two still-placeholder callees record their observed ABIs
without changing their bodies. IDO emits the complete frame, argument home
stores and reloads, class dispatch, branch-likely return, and epilogue directly
from semantic C. No expected-word guards are used.

## Verification

- The focused `generated_71820` object reproduces all 32 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,026 / 5,463 (55.39%)` overall and
  `2,448 / 4,789 (51.12%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0x46C80` and retail ROM offset `0x74130`.
- Both spans share SHA-256
  `b5786bc19624a7b4064536d78eda93d2752e60b8bda9395662d593924fb6f823`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Recover adjacent Game `func_15046F84`, the corresponding 32-word classifier
wrapper that delegates class zero to `func_15046D00`. Keep the previously
documented parked candidates unchanged.
