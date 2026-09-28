# Game HUD/status renderer reconstruction - 2026-09-28

## Result

`func_151E89A0` is reconstructed as semantic C across its 819-word,
3,276-byte retail span at `0x151E89A0..0x151E966C`. The former zero-return
placeholder now compiles to a `0xC84`-byte body inside the fixed `0xCCC`-byte
slot and uses retail's `0x158`-byte stack frame.

This is not a byte-exact result. A fresh linked matcher reports 803 real word
differences, improved from the original placeholder's 807. Exact totals remain
2,866 / 5,468 (52.41%) overall and 2,294 / 4,790 (47.89%) in Game.

## Recovered behavior

The function builds the in-game HUD display list. It clears and rebuilds the
active-player mask, walks `D_800CC2D0` player records, identifies selected and
nearby state, and detects the object type `0x25` proximity condition. It then
loads the score, selection, and warning texture resources and emits their raw
RDP setup commands and scissored texture rectangles.

Score rows use `func_150859AC`, per-player colors from `D_800ABA90`, and the
digit-coordinate tables at `D_8009006C` and `D_80090070`. The function also
forwards the display list to `func_151E966C` and `func_151E9D18` for the two
remaining HUD groups and returns the advanced `Gfx *`.

## Correctness boundary

The reconstruction came from the retail assembly and an `m2c` control-flow
draft; no semantic C donor was available. One generated type was corrected
during review: retail keeps the selected-player state as signed `-1`, not an
unsigned byte value of `255`. That distinction controls whether the selection
overlay is present.

The implementation retains the literal retail RDP command words. It does not
claim that the still-placeholder callees `func_151E966C` and `func_151E9D18`
are implemented, nor that this function's current register allocation and
instruction schedule match retail.

## Verification

The focused generated-slice build and complete non-matching game link pass.
The generated object fits its assigned retail span, `git diff --check` passes,
and the fresh symbol matcher measures the function at 803 real differences.
Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue matching `func_151E89A0` from this semantic baseline. Start with the
early player-scan lifetimes: retail keeps `D_8008FDBC` in `$s2`, the active
mask in `$s3`, and the selected value in `$t1`. Keep the exact `0x158` frame
and signed `-1` selection semantics while reducing scheduling differences.
