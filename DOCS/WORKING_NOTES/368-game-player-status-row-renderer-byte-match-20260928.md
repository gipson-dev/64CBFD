# Game player-status row renderer byte match - 2026-09-28

## Result

`func_151E966C` is byte-exact across all 427 words and 1,708 bytes at
`0x151E966C..0x151E9D18`. Fresh linked totals are 2,868 / 5,468 (52.45%)
overall and 2,296 / 4,790 (47.93%) in Game.

## Source recovery

The completed source retains the semantic reconstruction documented in
Working Note 365 while restoring the compiler-facing shape visible in retail:

- the incoming `Gfx *` is advanced directly instead of being copied through a
  second cursor lifetime;
- SDK `gDP*` macros reproduce both texture setups, environment colors, and
  the terminal pipe sync;
- the fifth argument remains a volatile byte load, reproducing retail's
  direct `sp+0x113` read and branch-likely shape;
- player and life-count values keep 32-bit lifetimes, with explicit `s16`
  conversion only at the two `func_150859AC` call boundaries;
- one shared center induction serves the visible-row and hidden-icon loops;
  and
- shift spelling for rectangle coordinates restores retail's saved-register
  allocation: cursor `$s2`, player `$s7`, life count `$s4`, box index `$s1`,
  and box coordinate `$s0`.

These changes reduced the unguarded mismatch from 415 words to 116 while
preserving retail's exact `0x6AC` extent, `0x100` frame, calls, control flow,
graphics commands, early returns and terminal return value.

## Compiler boundary

The remaining 116 words are persistent IDO stack-slot, register-allocation and
instruction-scheduling differences. The principal clusters are the compiler's
`sp+0xF0`/`sp+0xF4`/`sp+0xF8` local placement versus retail's
`sp+0x60`/`sp+0xE0`/`sp+0xE4`, the selected-row/color setup schedule, the
inner box-loop increment delay slot, and the hidden-icon color-table lifetime.

Source-order, declaration-order, explicit-lifetime, composite texture-macro,
and volatile-cache experiments either retained these clusters or disturbed
already matching code. The 116 expected-word guards are therefore scoped to
this function and preserve relocation metadata when loads or calls move. Ten
guard rows remove current relocations and ten install the corresponding retail
relocations. The complete guard table contains 1,650 rows with zero duplicate
`(filename, function, offset)` keys; exactly 116 rows belong to this function.

## Verification

The focused generated-slice build, exhaustive guarded rebuild, complete link
and fresh matcher pass all succeed. The matcher no longer lists
`func_151E966C`. The refreshed rebuilt span at
`build/conker.us.game.code.bin+0x1E966C` and pristine retail span at
`conker.us.bin+0x216B1C` compare equal across all 1,708 bytes. Both have
SHA-256:

`a735b0ad3a4c725740401a500844b4ec57b5b5a3f604af796a0593308ac37a07`

The replacement build, outer-ROM build, project-tool checks, all nine focused
Python tests, guard-table integrity audit and whitespace validation also pass.
Fresh gameplay was not run because this is a compiler/codegen match.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified or launched.

## Next boundary

Resume the bounded Init queue at 20-word `func_10001000`, which the fresh
matcher reports at 14 real differences. Keep the much larger reconstructed
HUD renderer `func_151E89A0` and adjacent `func_151EA15C` as separate focused
matching work.
