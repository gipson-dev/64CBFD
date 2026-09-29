# Game five-state impact dispatcher byte match

Date: 2026-09-29

## Scope and behavior

`func_15194794` in `conker/src/game/generated_1C1150.c` occupies 31 words and
124 bytes at `0x15194794..0x15194810`. It first calls `func_151B01B8` with the
two incoming object pointers, then calls `func_151B09BC` with timer `0x3E8`,
owner `0xFF`, and mode zero. State byte `arg1[4]` values zero through four
then dispatch `func_151AF270(arg1, 0xFF, 1)`; other values return after the
two setup calls.

## Source recovery

The previous body was empty. A grouped five-case switch recovers retail's
unsigned range check, five-entry jump table, shared dispatch body, frame,
saved-register lifetimes, call order, and delay-slot schedule.

The compiler emits the complete instruction stream, but initially owns the
jump table as generated `.rodata` at `0x800A8280`. Retail refers instead to
the preserved table `jtbl_800A82BC_game`, whose five entries all target the
shared dispatch body. Two relocation-aware stale checks retarget only that
HI16/LO16 relocation pair. They insert or omit no instructions and leave the
semantic C control flow intact.

## Verification

- The focused `generated_1C1150` object reproduces the complete 31-word
  topology after the two relocation guards are applied.
- The full replacement build, outer non-matching build, and ELF relink pass.
- The authoritative matcher reports `3,012 / 5,463 (55.13%)` overall and
  `2,434 / 4,789 (50.82%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes.
- Both spans share SHA-256
  `dcbbb3f61a3783037fa53380faa1f99774cc4caa431b8c30b6883f8c390b16e7`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_151DDBA0` as the next ordinary 32-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
