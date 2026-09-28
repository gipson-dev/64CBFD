# Game player-status row renderer reconstruction - 2026-09-28

> Superseded on 2026-09-28 by the byte-exact result in
> [Working Note 368](368-game-player-status-row-renderer-byte-match-20260928.md).
> This note preserves the initial semantic reconstruction baseline.

## Result

`func_151E966C` is reconstructed as semantic C across its 427-word,
1,708-byte retail span at `0x151E966C..0x151E9D18`. The former zero-return
placeholder now compiles to a `0x698`-byte body inside the fixed `0x6AC`-byte
slot and uses retail's exact `0x100`-byte stack frame and argument-home offsets.

This is not a byte-exact result. A fresh linked matcher reports 415 real word
differences, reduced from the placeholder's 425. Exact totals remain
2,866 / 5,468 (52.41%) overall and 2,294 / 4,790 (47.89%) in Game.

## Recovered behavior

The function renders the per-player status rows used by the adjacent HUD
renderer. It optionally loads and configures the score/status texture,
computes the horizontal row spacing from `D_800E0BB0`, and constructs a
four-bit hidden-player mask from the active-player table at `D_800E0C00`.

For each visible row, it either refreshes or reuses the cached count in
`D_800E0AA0`, applies the selected-row increment, sets the player color from
`D_800ABA90`, and draws `D_80087268` texture rectangles. Once the current
count is reached, the remaining rectangles use retail's `0x40404040` gray.

Hidden rows use the secondary texture at `D_D16 + 1` and draw a larger marker
centered on that row. Both texture-load failures return the current display-
list cursor immediately. The normal path emits the terminal RDP pipe-sync and
returns the advanced `Gfx *`.

## Compiler boundary

The fourth and fifth parameters are recovered as `s8` and `u8`, reproducing
retail's sign extension and stack byte load. A retained incoming-pointer/local-
cursor lifetime reduces the fresh mismatch from 424 to 416 words. Compensating
the debug-layout padding restores the exact `0x100` frame and reduces it once
more to 415.

The remaining differences are register allocation and instruction scheduling;
the current build assigns the cursor to `$s3`, while retail keeps it in `$s2`.
No guarded retail words were added.

## Verification

The focused generated-slice build and complete non-matching game link pass.
The generated object fits its assigned retail span, `git diff --check` passes,
and the fresh symbol matcher measures this function at 415 real differences
while adjacent `func_151E89A0` remains at 803. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue `func_151E966C` from this semantic baseline by reproducing the retail
saved-register allocation: display-list cursor `$s2`, player row `$s7`, count
`$s4`, inner box index `$s1`, and box coordinate `$s0`. If that source shape
does not converge, reconstruct adjacent 273-word `func_151E9D18` before
returning to scheduling-only work.
