# Game record-window initializer byte match

Date: 2026-09-29

## Scope and behavior

`func_15183974` in `conker/src/game/generated_1B0740.c` occupies 31 words and
124 bytes at `0x15183974..0x151839F0`. It indexes a table of five-word records,
initializes the selected record when its first word is zero, then initializes
the following record when needed and copies the selected record's fourth word
into the following record's fourth word.

## Source recovery

The previous body was a false zero-return placeholder. The recovered source
models `D_800DDE80` as eleven five-word records, which makes IDO reproduce
retail's multiply-by-20 address calculation, temporary-register allocation,
two null gates, initializer calls, branch-likely delay slots, and final copy.

Semantic C emits 27 of the 31 words directly. Four expected-word guards move
one record-pointer spill/reload lifetime from IDO's local stack offset `0x18`
to retail's equivalent top local slot at `0x1C`. The guards add no words and
carry no relocations.

## Verification

- The focused `generated_1B0740` object reproduces all 31 retail words.
- The linked ELF and non-matching build pass.
- The authoritative matcher reports `3,022 / 5,463 (55.32%)` overall and
  `2,444 / 4,789 (51.03%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes at
  Game offset `0x183974` and retail ROM offset `0x1B0E24`.
- Both spans share SHA-256
  `2fa35f0fd488dbd398137f278e58cd14d8b44842fd89bad6d083c8f5cbdd2c6e`.
- The patch table has 2,221 unique rows with no duplicate keys.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_1518F49C`, the next ordinary 32-word Game candidate with 30 real
differences. Keep `func_15106E78` parked on its 30-versus-32-word caller-saved
allocation cycle, `func_15015F40` parked behind unresolved indirect-table
ownership, and `func_150A76F0` in the handwritten-assembly queue.
