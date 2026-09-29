# Game subsystem-state initializer byte match

Date: 2026-09-29

## Scope and behavior

`func_151DDBA0` in `conker/src/game/generated_20AE20.c` occupies 32 words and
128 bytes at `0x151DDBA0..0x151DDC20`. It clears `D_800D2E40`, invokes
`func_1501C730(6, 0x1D, 0, 0, 1)`, sets mode byte `D_800E0B94` to three, and
clears `D_8008FDA4` and `D_800BEAC1`. It then runs `func_151E557C`,
`func_1000F1A8`, and `func_1000E934` before setting both `D_8008FD8C` and
`D_8008FD90` to one.

## Source recovery

The previous body was a false zero-return placeholder. The direct sequence of
global writes and calls reproduces retail's 32-byte frame, fifth stack
argument, store ordering, call relocations, delay slots, and shared final
constant lifetime. All 32 words emit from semantic C without expected-word
guards.

## Verification

- The focused `generated_20AE20` object reproduces the complete 32-word
  instruction stream directly from C.
- The full replacement build, outer non-matching build, and ELF relink pass.
- The authoritative matcher reports `3,013 / 5,463 (55.15%)` overall and
  `2,435 / 4,789 (50.85%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes.
- Both spans share SHA-256
  `fa65b54c86b9b6abdf04525f540a144ff1760fbf26793da7e5df98d6153cad1b`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_151EC178` as the next ordinary 30-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
