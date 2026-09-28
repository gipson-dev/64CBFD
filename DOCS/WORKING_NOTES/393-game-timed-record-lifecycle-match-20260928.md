# Game timed-record lifecycle byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_1519EA04` in
`conker/src/game/generated_1CBE20.c` with semantic C. The complete 29-word,
116-byte retail routine now emits directly without expected-word guards.

## Recovered behavior

The routine first checks bit zero of the record flags at offset `0x10`. When
the bit is clear, it returns immediately. Otherwise, it subtracts the global
frame delta `D_800BE9E4` from the signed 16-bit timer at offset `0x20`.

If the updated timer is still nonnegative, the routine returns. On expiration,
it checks the suppression byte at offset `0x28`. When that byte is zero, it
follows the owner pointer at offset `0x24` and clears the owner's word at
offset `0x30`. It then passes the record to `func_1516972C` for deletion.

The recovered `void` signature corrects the false placeholder return type.
An explicit `expired` lifetime reproduces retail's `v0` boolean and lets IDO
reuse the same register for the owner pointer after the expiration branch.

## Verification

- The focused `generated_1CBE20` object build passed.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_1519EA04` as byte-exact.
- The linked and retail 116-byte spans share SHA-256
  `8cbe4bb85537d3bd53f45bef0bfb83d5ccc0259c5fc02ed2b1863e8c60b05f45`.
- The routine uses no expected-word guards, and the guard manifest has no
  duplicate `(filename, function, offset)` keys.
- Fresh matcher totals are `2,895 / 5,466 (52.96%)` overall and
  `2,321 / 4,790 (48.46%)` in Game, with one address-drift row.

## Parked audio target

The semantic 24-instruction body for `func_151F3D78` was also recovered and
matched its retail instructions directly, but the unpadded `game_21FC90`
audio object places the function at `0x151F3DA8`, `0x30` bytes after retail
`0x151F3D78`. The drift already exists before `func_151F39E4`; completing this
row requires a separate audio-object layout repair. The experimental source
was removed so this batch does not turn one content mismatch into a new
address-drift row.

## Resume boundary

Continue the ordinary 25-difference Game queue with 30-word
`func_1518CCA8`. Keep `func_151F3D78` parked with the audio-object layout
work, keep the tied Init SDK cache routines in their ownership lane, and keep
address-drift row `func_10012588` parked.
