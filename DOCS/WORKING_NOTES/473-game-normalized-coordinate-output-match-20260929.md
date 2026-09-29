# Game normalized coordinate output byte match

Date: 2026-09-29

## Scope and behavior

`func_1510B958` in `conker/src/game/generated_138520.c` spans 30 words and
120 bytes. It indexes a `0x180`-byte record in the table addressed by
`D_800BE628`, normalizes the value at `0x74` against the scale at `0x6C`, and
adds the result to the base value at `0x64`. It repeats the same calculation
for offsets `0x78`, `0x70`, and `0x68`, writing the two results to
`D_800D35E0` and `D_800D35E4`.

The missing `D_800D35E4` absolute symbol is now represented in the tracked
`undefined_syms.us.txt`, allowing the two output stores to retain their
independent retail relocations. Reversing the source-level final-add operand
order reproduces both floating-point register pipelines directly from C.

Twenty-five words emit directly from semantic C. Five fail-closed expected-
word guards normalize only IDO's independent opening record-table load and
scaled-index schedule. The guards include the moved `D_800BE628` HI/LO
relocations and reject stale compiler output.

## Verification

- The focused padded object builds with all five expected-word guards firing.
- The complete non-matching build and relink pass.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `3b4951f5cfb30124cdb1616129dd0a5550a80c40c8f3b0d5ec6c649fe7b399fc`.
- The authoritative matcher reports `2,975 / 5,465 (54.44%)` overall and
  `2,401 / 4,789 (50.14%)` in Game, with one address-drift row.
- The ordinary full-ROM checksum remains expectedly non-matching while the
  broader decomp is incomplete; the symbol-aware matcher is the acceptance
  check for this function.

## Resume boundary

Continue with the next ordinary small Game placeholder. Keep
`func_15022640` and `func_150B66DC` parked at their measured IDO scheduling
boundaries rather than expanding their guard sets.
