# Game two-event command dispatcher byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_150C19C0` in
`conker/src/game/generated_EEE70.c` with its semantic Game routine. The retail
slot spans 27 words and 108 bytes.

## Recovered behavior

The function narrows its third argument to an event byte. Event `1` selects
command `0x18`, while event `2` selects command `0x15`. It loads the owner
pointer from offset `0x1D4` of the second argument, calls `func_15142314` with
that owner, the selected command, and the original first argument, then always
returns one.

Retail leaves the command stack local unspecified for event values other than
one and two. The recovery preserves that contract rather than introducing a
synthetic default. An `if`/`else if` form produced inverted branches and an
extra event copy. A
two-case `switch` instead reproduces retail's two forward equality branches,
case stores, default-path delay-slot load, and common call. All 27 words emit
directly from semantic C with no expected-word guards or profile changes.

## Verification

- The focused `generated_EEE70.c.o` build passed under the existing `-O2 -g3`
  profile.
- Focused object disassembly matches all 27 retail instruction words and the
  `func_15142314` call relocation.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150C19C0` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `61edfab9f109b2b4bd29a04b5e856450a8fc8b4bff97757c439029055d77f36f`.
- Fresh matcher totals are `2,911 / 5,466 (53.26%)` overall and
  `2,337 / 4,790 (48.79%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150C7870`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
