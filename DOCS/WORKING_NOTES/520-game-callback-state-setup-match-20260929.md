# Game callback-state setup byte match

Date: 2026-09-29

## Scope and behavior

`func_151E4E64` in `conker/src/game/generated_20AE20.c` occupies 33 words and
132 bytes at `0x151E4E64..0x151E4EE8`. It runs two setup routines, raises bit
`0x8000` in `D_800E0B9A` once the global counter reaches `0x4B1`, and installs
`func_151E4E00` with state bytes `7` and `8` whenever that halfword is nonzero.

## Source recovery

The previous body was a false zero-return placeholder. The recovered semantic
C keeps the halfword signed, uses the original `0x8000` bit update, and stores
the callback address through the existing 32-bit callback slot. IDO emits the
retail 24-byte frame, both calls, both branches, the branch-delay constant
load, and all global accesses directly from C. No expected-word guards are
used.

## Verification

- The focused `generated_20AE20` object reproduces all 33 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,024 / 5,463 (55.35%)` overall and
  `2,446 / 4,789 (51.08%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 132 linked bytes at
  Game offset `0x1E4E64` and retail ROM offset `0x212314`.
- Both spans share SHA-256
  `d265bd58b30d5d4a492a624a5fe5e9644255b0f276ad7d413c9ed06946404fc9`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Init `func_1000FF90`, the next ordinary unparked candidate at 35 words
and 31 real differences. Keep Game `func_15015F40` parked behind unresolved
indirect-table ownership, handwritten `func_150A76F0` in the assembly queue,
and `func_15106E78` parked on its caller-saved allocation cycle.
