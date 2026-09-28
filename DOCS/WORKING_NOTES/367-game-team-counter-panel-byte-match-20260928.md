# Game team-counter panel byte match - 2026-09-28

## Result

`func_151E9D18` is byte-exact across all 273 words and 1,092 bytes at
`0x151E9D18..0x151EA15C`. Fresh linked totals are 2,867 / 5,468 (52.43%)
overall and 2,295 / 4,790 (47.91%) in Game.

## Source recovery

The completed source retains the semantic reconstruction documented in
Working Note 366 and restores the compiler-facing form visible in retail:

- split debug-layout storage places `panel_y` at `sp+0x80`, texture S
  coordinates at `sp+0x7C` and `sp+0x78`, and texture T at `sp+0x98`;
- the texture resource is selected with the retail conditional expression;
- SDK `gDP*` macros reproduce the scoped display-list temporary lifetimes;
- the tile-line mask is left to `_SHIFTL`, and the tile bound is expressed as
  subtract-then-shift so IDO preserves retail's arithmetic order;
- player and sampled values retain 32-bit lifetimes, with an explicit `s16`
  conversion only at the `func_150859AC` call boundary; and
- the record cursor is initialized before the team cursor.

These changes reduced the unguarded mismatch from 178 words to two while
preserving retail's exact `0x444` extent, `0xA0` frame, saved registers,
control flow, calls and delay slots.

## Compiler boundary

IDO schedules two independent operations in the opposite order from retail:
the `D_8008FDD4` record-pointer load and the team-array end-pointer addition.
Source-order, declaration-order and explicit end-pointer lifetime experiments
either retained the same pair or disturbed otherwise matching registers.

Two relocation-aware expected-word guards at relative offsets `0x2E4` and
`0x2E8` exchange only those operations. The first guard removes the record
load and inserts the end-pointer add; the second restores the same record load
with its `R_MIPS_LO16:D_8008FDD4` relocation. No branch, delay slot, address,
value, memory access or function extent changes.

The guard table contains 1,534 rows with zero duplicate
`(filename, function, offset)` keys. Exactly two rows belong to this function.

## Verification

The focused generated-slice build, exhaustive guarded rebuild, complete link
and fresh matcher pass. The matcher no longer lists `func_151E9D18`. The
rebuilt span at `build/conker.us.game.code.bin+0x1E9D18` and pristine retail
span at `conker.us.bin+0x2171C8` compare equal across all 1,092 bytes. Both
have SHA-256:

`47f55c4df009cdb8c23bbd616d785cd5ca215d3d74da3d3d8d15d690175a634a`

The replacement and outer-ROM builds, project-tool checks, all nine focused
Python tests, guard-table integrity audit and whitespace validation also pass.
Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified or launched.

## Next boundary

Continue the adjacent 427-word `func_151E966C` player-status renderer from its
415-difference semantic baseline. Its exact `0x100` frame and behavior are
already reconstructed, making saved-register allocation and SDK command
expression recovery the next focused matching work before much larger
`func_151EA15C`.
