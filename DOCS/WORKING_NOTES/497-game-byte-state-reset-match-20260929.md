# Game byte-state reset byte match

Date: 2026-09-29

## Scope and behavior

`func_15010600` in `conker/src/game_3D9A0.c` occupies 32 words and 128 bytes
at `0x15010600..0x15010680`. It clears six scalar bytes at `D_800D9920`,
`D_800D9921`, `D_800D9928`, `D_800D9929`, `D_800D9938`, and `D_800D9939`,
then clears paired 12-byte regions beginning at `D_800D992A` and
`D_800D993A`.

## Source recovery

The previous body called `bzero(&D_800D9920, 0x27)`. That wrote a broader
contiguous range than retail and compiled as a ten-word call wrapper followed
by padding. A stale commented attempt instead cleared eleven bytes from
`D_800D9920` and `D_800D9930`; the retail addresses and loop extent disprove
that reconstruction.

Six independent scalar assignments recover the opening stores. A
12-iteration chained assignment over `D_800D992A` and `D_800D993A` makes IDO
emit retail's four-way-unrolled loop, including its pointer increments, store
offsets, branch, and delay slot.

## Compiler normalization

Four relocation-aware, stale-checked guards normalize one closed scheduling
window. The compiler emits the independent `D_800D9939` store before the
three loop-pointer additions; retail places it after them. The guards reorder
those four existing words while verifying the unchanged relocations for
`D_800D9939`, `D_800D993A`, and `D_800D992A`. No instruction is inserted or
omitted.

## Verification

- The focused `game_3D9A0` object accepts all four new stale checks.
- A complete guarded-object rebuild and ELF relink pass.
- The authoritative matcher reports `3,001 / 5,463 (54.93%)` overall and
  `2,423 / 4,789 (50.60%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 128 bytes.
- Both spans share SHA-256
  `f731c29b484f488587e75844d64f3b7525bbd46b48dbabc3f4c1521ad4d00c37`.

## Resume boundary

Continue with the next ordinary semantic C candidate. `func_1506DC10` is the
next promising 30-difference body; verify its random-choice and floor-height
control flow against the 37-word retail span before editing. Keep
`func_15015F40` parked behind unresolved indirect-table ownership,
`func_15022640` parked at its measured IDO scheduling boundary, and
handwritten `func_150A76F0` in the assembly lane.
