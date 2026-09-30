# Game 25-byte group deduplicating append byte match

Date: 2026-09-29

## Scope and behavior

`func_1502225C` in `conker/src/game/generated_49D30.c` occupies 33 words and
132 bytes at `0x1502225C..0x150222E0`. It scans the active entries in one
25-byte row of `D_800C3518`, returns without modification when the incoming
byte is already present, and otherwise appends the value and increments the
row's count in `D_800C3510`.

## Source recovery

The previous body was a false zero-return placeholder. The adjacent recovered
`func_15022640` establishes the same deduplicating-append algorithm for a
30-byte table. Giving `D_800C3518` its observed 25-byte row type reproduces
retail's multiply-by-25 address expansion, count lifetime, do-while scan, and
append path. IDO emits the complete routine directly from semantic C with no
expected-word guards.

## Verification

- The focused `generated_49D30` object reproduces all 33 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,025 / 5,463 (55.37%)` overall and
  `2,447 / 4,789 (51.10%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 132 linked bytes at
  Game offset `0x2225C` and retail ROM offset `0x4F70C`.
- Both spans share SHA-256
  `26a69edf89a280a0b5a539dda7f210dadfd03750bc373bb2b445a3b6f565e688`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_15046C80`, an untriaged 32-word placeholder with 31 real
differences. Keep Init `func_1000FF90` parked at its documented compiler-
allocation boundary, `func_15015F40` parked behind unresolved indirect-table
ownership, handwritten `func_150A76F0` in the assembly queue, and
`func_15106E78` parked on its caller-saved allocation cycle.
