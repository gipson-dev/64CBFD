# Game packed-record activation byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_150A0264` in
`conker/src/game/generated_CD5A0.c` with its semantic Game routine. The retail
slot spans 27 words and 108 bytes.

## Recovered behavior

The function indexes a 12-byte entry in `D_800D3010`. If the entry's top
status bit is already set, it returns zero without modifying the record.
Otherwise it sets status bit `0x80`, clears status bit `0x40`, reads the source
record's word at offset four, clears the destination word at offset four, and
replaces status bits 2 through 5 with `(source_value << 2) & 0x3C` before
returning one.

The source-word read deliberately precedes the destination clear. That order
preserves retail behavior when the source pointer aliases the indexed
destination. The recovered C emits the exact extent, branches, delay slots,
loads, stores, constants, and offsets. IDO assigns the packed status and source
temporaries to a different closed register cycle, so 12 stale-checked
expected-word guards reproduce only retail's temporary-register allocation.

## Verification

- The focused `generated_CD5A0.c.o` build passed under the existing profile.
- Focused object disassembly matches all 27 retail instruction words and
  relocations after the 12 register-allocation guards.
- The exhaustive `wsl make -C conker NON_MATCHING=1` rebuild and relink passed,
  validating every consumer of the shared expected-word table.
- The guard table contains 1,819 rows, zero duplicate
  `(filename, function, offset)` keys, and exactly 12 rows for this function.
- `match_progress.py` classifies `func_150A0264` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `5d4825ac297505b071ef5aa2f75fee798810e57f3134845acde47bdabe72758b`.
- Fresh matcher totals are `2,907 / 5,466 (53.18%)` overall and
  `2,333 / 4,790 (48.71%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_150A3444`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
