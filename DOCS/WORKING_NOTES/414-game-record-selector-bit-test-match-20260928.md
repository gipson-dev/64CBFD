# Game record selector-bit test byte match

Date: 2026-09-28

## Scope

This pass completed `func_15114050` in
`conker/src/game/generated_13D350.c`. The retail slot spans 29 words and 116
bytes.

## Recovered behavior

The routine first checks bit `0x80` in the record byte at offset `0x4F` and
returns zero when the record is inactive. Selector `-1` is an unconditional
successful match for an active record. Other selectors derive the record index
from the pointer difference against `D_800DBEF4` divided by the `0xA0` record
stride, load the corresponding mask from `D_800DBF94`, and return whether
`1 << selector` is present.

Using byte pointers preserves retail's unsigned flag load while expressing the
record index directly from the known stride. The resulting code reproduces the
opening zero-result lifetime, branch-delay global-address load, signed divide,
mask lookup, variable shift, and three return paths. All 29 words emit directly
from semantic C. No expected-word guards or compiler-profile changes are
required.

## Verification

- The focused `generated_13D350.c.o` build passed under the existing
  `-O2 -g3` profile.
- Focused object disassembly matches all 29 retail instruction words and both
  global relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_15114050` as byte-exact.
- The linked and retail 116-byte spans share SHA-256
  `b952efb961befdab310b53b58d5eb7f15e234ca2ecd12b28a014a1abdb02824d`.
- Fresh matcher totals are `2,916 / 5,466 (53.35%)` overall and
  `2,342 / 4,790 (48.89%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_15116110`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
