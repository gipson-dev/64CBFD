# Game display-list address relocator byte match

Date: 2026-09-29

## Scope and behavior

`func_15168F08` in `conker/src/game_1944C0.c` occupies 31 words and 124 bytes
at `0x15168F08..0x15168F84`. It walks eight-byte display-list commands until
the signed opcode byte `-0x21` (`0xDF`). Opcode `1`, and opcode `-0x24`
(`0xDC`) with byte three equal to `0x0E`, identify commands whose second word
contains a 24-bit address. For those commands, the routine clears the upper
byte and adds the supplied relocation base.

## Source recovery

The previous C expressed commands as unsigned bytes, advanced a running
pointer, and combined the mask and relocation into one assignment. The
recovered source uses signed opcode loads, an explicit command index, a cursor
recomputed from the original base, and two distinct mask/add assignments.
Volatile opcode reads preserve retail's opening condition read and independent
body read, as well as the reload on each loop back edge.

IDO reproduces the complete 31-word extent, branch topology, delay slots,
loads, and two-store update sequence. Eighteen stale-checked guards normalize
one closed allocation chain covering the terminator, three command constants,
mask, scaled cursor, and relocated value. No relocations or words are inserted
or omitted.

## Verification

- The focused `game_1944C0` object emits the complete retail instruction
  stream after the 18 expected-word guards are applied.
- A full guard-table rebuild reaches the linked ELF without a stale-guard
  failure.
- The authoritative linked matcher reports `3,008 / 5,463 (55.06%)` overall
  and `2,430 / 4,789 (50.74%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 124 bytes.
- Both spans share SHA-256
  `87b6edb1eaa07348ff987b92fadfd41fe157af7bb3bd4bd60ee33b3b46bc764f`.
- `make tools-check`, all 10 tests under `tools/tests`,
  `make -C conker replace NON_MATCHING=1 -j4`, and the outer
  `make NON_MATCHING=1 -j4` build pass.

## Resume boundary

Inspect `func_1517A9A8` as the next ordinary 29-difference Game candidate.
Keep `func_15015F40` parked behind its unresolved indirect-table ownership,
`func_150A76F0` in the handwritten-assembly queue, and Init `func_1000FF90`
parked at its measured compiler-allocation boundary.
