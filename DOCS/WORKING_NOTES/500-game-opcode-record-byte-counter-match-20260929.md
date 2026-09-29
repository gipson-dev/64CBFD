# Game opcode-record byte counter byte match

Date: 2026-09-29

## Scope and behavior

`func_150027F8` in `conker/src/game_2DF70.c` occupies 32 words and 128 bytes
at `0x150027F8..0x15002878`. It accepts an integer data address, scans the
signed opcode byte at the start of each eight-byte record, and stops at opcode
`-0x21`. Opcode class one contributes four output bytes, opcode six contributes
two, and opcode five contributes one. A zero input address returns zero.

## Source recovery

The previous C declared the input as `s8 *` and indexed it as a flat byte
array. IDO strength-reduced that expression into a running record pointer,
which changed the opening lifetimes and most of the loop register allocation.
The caller and retail code preserve the input in `a0` as an integer address.
Expressing each load as `*(s8 *)(arg0 + (count << 3))` restores retail's
repeated index shift, base addition, signed byte load, branch topology, and
32-word extent.

The recovered semantic body leaves one closed compiler-allocation cycle:
retail keeps the record index in `v0` and current opcode in `a1`, while IDO
chooses those two registers in reverse. Fourteen stale-checked expected-word
guards normalize only that `v0`/`a1` cycle. No words are inserted or omitted,
and the accumulated byte count remains in retail's `v1` directly from C.

## Verification

- The focused `game_2DF70` object emits the complete retail instruction stream
  after the 14 expected-word guards are applied.
- A full guard-table rebuild reaches the linked ELF without any stale-guard
  failure. The ordinary matching-ROM SHA target remains expectedly nonzero for
  the broader non-matching project.
- The authoritative linked matcher reports `3,004 / 5,463 (54.99%)` overall
  and `2,426 / 4,789 (50.66%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 128 bytes.
- Both spans share SHA-256
  `72ef7693e63f911f4b3d0ea14dda74673b109c312244bfea5d48cf2effe0b0b0`.
- `make tools-check`, all 10 tests under `tools/tests`,
  `make -C conker replace NON_MATCHING=1 -j4`, and the outer
  `make NON_MATCHING=1 -j4` build pass.

## Resume boundary

Inspect `func_151420F8` as the next live 31-difference Game candidate. Keep
Init `func_1000FF90` parked at its measured allocation boundary: its semantic
scan and control flow agree with retail, but retail has a second independent
`-1` constant and a closed argument/record-pointer register allocation that
the tested source forms did not reproduce.
