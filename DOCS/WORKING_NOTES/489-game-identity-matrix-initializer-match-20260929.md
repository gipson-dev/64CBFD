# Game identity-matrix initializer byte match

Date: 2026-09-29

## Scope and behavior

`guMtxIdentF` in `conker/src/libultra/gu/guMtxIdentF.c` occupies 20 words and
80 bytes at `0x150A7BC0..0x150A7C10`. Nineteen words implement the routine;
the final zero word is retail padding tracked with the function.

The recovered body writes a 4-by-4 floating-point identity matrix. Diagonal
entries receive the IEEE-754 value `1.0f`, while all twelve off-diagonal
entries receive the zero bit pattern.

## Compiler shape

The previous nested-loop implementation did not resemble retail's unrolled
leaf routine. Under O3, volatile float and word views preserve the mixed store
order while allowing IDO to schedule the first zero store into the floating
constant hazard slot and the final diagonal store into the return delay slot.
The resulting body has no frame and exactly retail's 19-instruction extent.

Fourteen instruction words and the padding word emit directly from the
recovered C shape. Five stale-checked guards affect the one constant load and
four diagonal stores, normalizing IDO's `$f0` choice to retail's equivalent
`$f4` lifetime. They do not change control flow, memory offsets, values, or
instruction count.

## Verification

- The focused `guMtxIdentF` object emits the complete retail slot after the
  five register-allocation guards.
- A clean Makefile-driven rebuild and complete ELF relink pass.
- Direct linked comparison reports zero differences across all 80 bytes.
- Both spans share SHA-256
  `3314c8cd2632384c565633ca83d65b1b11477a1d6457ecab8d8eb30dfce96408`.
- The authoritative matcher omits `guMtxIdentF` from its non-exact list and
  reports `2,993 / 5,465 (54.77%)` overall and `2,418 / 4,789 (50.49%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next small Game or Init candidate. Keep this SDK helper's O3
profile and five guarded FP-register words together as one matching unit.
