# Game descriptor-install wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_15094F70` in `conker/src/game/generated_C1D70.c` spans 30 words and
120 bytes. It first passes the source descriptor, selector, and optional owner
to `func_15095060`, which materializes the normalized descriptor in
`D_800D2C90`. It then calls `func_150950D4` with the original output and tail
arguments, one zero slot, and two fixed `0x100` dimensions.

The recovered ten-argument prototype exposes the retail outgoing stack layout.
The complete wrapper emits directly from semantic C with no guarded words. The
still-placeholder `func_150950D4` body is unchanged; only its argument contract
was made explicit so the wrapper can be type-checked.

## Verification

- The focused padded object fits the complete 30-word retail slot.
- The complete non-matching build and relink pass.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `8d9ae7535f57bf56b9ce25835cb5dc2d6cf8b9fd835967b89a85a095ac263f64`.
- The authoritative matcher reports `2,971 / 5,465 (54.36%)` overall and
  `2,397 / 4,789 (50.05%)` in Game, with one address-drift row.

## Resume boundary

Continue with the adjacent `func_15094FE8`, which uses the same setup and
final-dispatch family but forwards all five incoming tail arguments.
