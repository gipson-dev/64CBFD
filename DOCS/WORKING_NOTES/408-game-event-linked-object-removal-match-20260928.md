# Game event-linked object removal byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_150BE150` in
`conker/src/game/generated_EB340.c` with its semantic Game routine. The retail
slot spans 29 words and 116 bytes.

## Recovered behavior

The function narrows its third argument to an event byte and filters two event
forms against the tracked pointer stored at offset `0x28` of the current
object. Event `0x21` compares that pointer directly with the payload pointer.
Event zero instead compares it with the pointer at offset `0x318` of the
payload object. Either match calls `func_1516972C` for the current object; all
other events and mismatches return without action.

The nested `if`/`else if` structure reproduces retail's event dispatch and
branch-likely return paths. The initial semantic expression emitted the entire
routine except for three event-zero load/allocation words. Materializing
`*arg1` as an explicit local restores retail's `v0` lifetime, payload-first
load order, and nested `0x318` dereference. The complete routine then emits
directly from C with no expected-word guards or compiler-profile changes.

## Verification

- The focused `generated_EB340.c.o` build passed under the existing `-O2 -g3`
  profile.
- Focused object disassembly matches all 29 retail instruction words and both
  `func_1516972C` call relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150BE150` as byte-exact.
- The linked and retail 116-byte spans share SHA-256
  `84d13c435234d104c77b0fc196c0dc32333168538b30046bc6f3b95c2a208484`.
- Fresh matcher totals are `2,910 / 5,466 (53.24%)` overall and
  `2,336 / 4,790 (48.77%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_150C19C0`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
