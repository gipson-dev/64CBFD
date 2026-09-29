# Game coordinate-equality classifier byte match

Date: 2026-09-28

## Scope

This pass completed `func_15159230` in
`conker/src/game/generated_185560.c`. The retail slot spans 34 words and 136
bytes at `0x15159230..0x151592B8`.

## Recovered behavior

The routine canonicalizes its third argument as an unsigned byte and compares
the three floats referenced by its second argument against the coordinates at
offsets `0x14`, `0x18`, and `0x1C` of its first argument. A complete exact
match returns `0`. Any coordinate mismatch returns `2` when the mode byte is
`1` or `2`; every other mode returns `1`.

Nested equality tests reproduce retail's comparison order, floating-point
register allocation, zero-result lifetime, and the two early mismatch paths.
IDO folds the final successful comparison and mismatch selection into
branch-likely forms with delay-slot assignments. Eleven function- and
offset-scoped expected-word guards at `0x54..0x80` preserve retail's
equivalent ordinary branches, explicit assignments, and shared return block.
Twenty-two words emit directly from semantic C, and the generated-slice padder
retains the final retail delay-slot `nop`. No relocation-bearing instruction
is guarded and no compiler-profile override is used.

## Verification

- The focused `generated_185560.c.o` build passed under the existing
  `-O2 -g3` profile and all 34 disassembled words match retail.
- The full `wsl make -C conker NON_MATCHING=1` relink passed across the entire
  expected-word guard manifest.
- `match_progress.py` classifies `func_15159230` as byte-exact.
- The linked ELF and retail 136-byte spans share SHA-256
  `8676af640e21d085de785f26264d34916e066fd5e94c6b0e763c9e9bd664fc8c`.
- Fresh matcher totals are `2,919 / 5,466 (53.40%)` overall and
  `2,345 / 4,790 (48.96%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_15166F6C`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
