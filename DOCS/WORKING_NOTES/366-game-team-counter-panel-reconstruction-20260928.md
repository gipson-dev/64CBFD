# Game team-counter panel reconstruction - 2026-09-28

## Result

`func_151E9D18` is reconstructed as semantic C across its complete 273-word,
1,092-byte retail span at `0x151E9D18..0x151EA15C`. The former zero-return
placeholder now compiles to exactly `0x444` bytes and uses retail's exact
`0xA0` stack frame, saved-register set, and incoming third-argument home.

This is not yet byte-exact. A fresh linked matcher reports 178 real word
differences, reduced from the placeholder's 272. Exact totals remain
2,866 / 5,468 (52.41%) overall and 2,294 / 4,790 (47.89%) in Game.

## Recovered behavior

The function renders the paired team/player counter panel. It selects one of
three adjacent `D_D10` texture resources from HUD flags and mode byte `0x42`,
configures the corresponding 16- or 32-pixel texture, and draws the left and
right counter backgrounds.

When refresh is requested, the two totals come from one of three retail paths:
direct player values for flags `0x6040`, an object-record scan for flag
`0x100`, or mode-record halfwords grouped through `D_800E0C00`. Negative
source values clamp to zero. The totals are cached in `D_800E0AA0`; the
non-refresh path reuses that cache.

The function finishes by selecting the gray text color and printing the right
and left totals through `func_15042D94` at the retail panel coordinates.
Texture-load failure returns the unchanged display-list cursor.

## Compiler boundary

The first draft exceeded the fixed span by `0x30` bytes because `s16` total
locals made IDO re-sign-extend both accumulators after every addition. Retail
keeps them as 32-bit values in `$s1/$s2` and narrows only when writing the
cache. Correcting those types produces the exact `0x444` code extent and cuts
the mismatch to 181 words.

Adding the missing `0x40` debug-layout area restores retail's exact `0xA0`
frame and argument-home offset, reducing the mismatch again to 178. The
remaining differences are local-slot placement, temporary-register selection,
and command scheduling. No guarded retail words were added.

## Verification

The focused generated-slice build and complete non-matching game link pass.
The compact symbol size is exactly `0x444`, `git diff --check` passes, and the
fresh linked matcher measures 178 real differences. Adjacent
`func_151E89A0` and `func_151E966C` remain at 803 and 415. Fresh gameplay was
not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue byte matching `func_151E9D18` before moving to the much larger
`func_151EA15C`. Its frame, extent, saved registers, major control flow, and
call sequence already agree; first restore retail's `panel_y` stack slot at
`0x80` and the texture-coordinate locals at `0x7C`, `0x78`, and `0x98`.
