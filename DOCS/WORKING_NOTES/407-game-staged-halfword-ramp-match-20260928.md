# Game staged halfword ramp byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_150B71A8` in
`conker/src/game/generated_E4070.c` with its semantic Game routine. The retail
slot spans 30 words and 120 bytes.

## Recovered behavior

The function advances two signed halfwords at offsets `0x38` and `0x3A` toward
`0x1000`. The first incomplete field is increased by `D_800BE9E4 << 8` and
clamped at `0x1000`, after which the function returns. The second field is
examined and advanced only when the first field was already exactly `0x1000`
on entry.

The recovered `if`/`else if` shape reproduces retail's first-field priority,
the branch-likely load of the second field, and the early return whose delay
slot performs the first clamp. Direct signed-halfword accesses retain the
post-store reloads used for each clamp comparison. All 30 words emit directly
from semantic C with no expected-word guards or compiler-profile changes.

## Verification

- The focused `generated_E4070.c.o` build passed under the existing `-O2 -g3`
  no-unroll profile.
- Focused object disassembly matches all 30 retail instruction words and the
  four `D_800BE9E4` relocation halves.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150B71A8` as byte-exact.
- The linked and retail 120-byte spans share SHA-256
  `829a2f70ead72049202fa8171e7aaa45b60323401d02e4842e5efa6c9e177acb`.
- Fresh matcher totals are `2,909 / 5,466 (53.22%)` overall and
  `2,335 / 4,790 (48.75%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 29-word `func_150BE150`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
