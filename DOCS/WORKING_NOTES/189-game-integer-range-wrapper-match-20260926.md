# Game integer range wrapper match - 2026-09-26

## Result

`func_151444DC` is byte-exact across its complete 19-word, 76-byte span at
`0x151444DC..0x15144528`. The fresh matcher reports 2,692 / 5,469 exact C
functions overall and 2,121 / 4,791 in Game.

## Behavior

The function wraps `arg0` into the integer interval bounded by `arg2` and
`arg1`. Its step is `arg1 - arg2 + 1`. Values above the upper bound repeatedly
subtract the step; values below the lower bound repeatedly add it.

The recovered behavior was already correct, but its initial adjustment was
written separately from a following `while` loop. IDO versioned each loop,
split the first step into arithmetic by `arg1 - arg2` and a separate one-unit
adjustment, and produced a 27-word body that overflowed the 19-word retail
allocation.

## Source recovery

Expressing each range-adjustment path as a `do/while` loop preserves the same
behavior while matching retail's control flow. IDO now materializes the full
step in `v0`, performs the mandatory first adjustment, and emits the repeated
adjustment in each branch-likely delay slot. All 19 words compile directly;
no guarded retail-word rows or overflow trampoline remain.

Changing the scalar to unsigned, wrapping it in a one-word aggregate, and
splitting the subtraction and increment into separate assignments were tested
first. All three retained the same expanded overflow body and were discarded.

## Exact-byte evidence

The linked ELF slice at offset `0x1844DC` and pristine retail slice at offset
`0x17198C` compare equal for all 76 bytes. Both have SHA-256
`682c1fbc5ae2acf2b0199b940b022a45b7610905e88ae616c2dd5ae974104416`.
The fresh matcher moved exactly this row from different to exact:

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,692 / 5,469 (49.22%) | 1 | 2,776 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,121 / 4,791 (44.27%) | 0 | 2,670 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

`64CBFDOGL/recomp_out/.c` still contains an empty generated body for this
function, while its symbol configuration records the correct `0x4C` extent.
A future controlled recomp regeneration should consume the corrected guest
body. The sibling's 1,659 existing dirty entries were preserved, and frozen
Release was not built, modified, or launched; `build/Release/conker_pc.exe`
remains 13,712,896 bytes with timestamp `2026-09-23 05:04:28`.

## Validation

- The focused `game_16EE20.c.o` build emits all 19 retail words directly.
- Full `make -C conker replace NON_MATCHING=1 -j4` passes.
- Fresh `progress` and LIST `match-progress` runs pass.
- The independent 76-byte linked-versus-retail comparison passes.
- `make tools-check`, all six padding-tool unit tests, and the outer
  `make NON_MATCHING=1 -j4` build pass.
- `git diff --check` passes before checkpointing.

## Next boundary

Continue ordinary Game matching with 20-word `func_151464B8`, the next
nonblocked Game C row at 18 real differences. The next ordinary Init C row is
20-word `func_10001000` at 14 real differences; keep address-blocked
`func_10012588` parked.
