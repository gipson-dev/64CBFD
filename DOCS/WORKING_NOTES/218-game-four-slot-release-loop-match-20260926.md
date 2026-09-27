# Game four-slot release loop match - 2026-09-26

## Result

`func_150C522C` is byte-exact across 21 words and 84 bytes at
`0x150C522C..0x150C5280`. Fresh totals are 2,722 / 5,470 exact C functions
overall and 2,151 / 4,792 in Game.

## Recovery

The function walks the four pointer slots beginning at `D_800D98D0`. Each
non-null entry is passed to `func_1516972C`, and every entry is cleared before
the cursor reaches `D_800D98E0`. A typed four-entry pointer array, explicit
end pointer, and `do/while` loop reproduce retail's frame, saved-register
lifetimes, branch-likely null path, callback, cursor update, delay-slot clear,
and epilogue.

IDO emits 19 of the 21 words directly. Its only difference is the order of
the two independent `addiu` instructions that complete the cursor and end
addresses after their `lui` instructions. Two guarded word-patch entries,
each declaring its expected and replacement `R_MIPS_LO16` relocation, restore
retail's end-before-cursor completion order without changing control flow,
data flow, or either referenced symbol.

## Evidence

Linked ELF offset `0x10522C` and decompressed retail offset `0xF26DC` compare
equal for all 84 bytes. Both spans have SHA-256
`fe3eecef23e97693912477fffab1907f920f93615fa711342dcd7c82ebb484df`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,722 / 5,470 (49.76%) | 1 | 2,747 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,151 / 4,792 (44.89%) | 0 | 2,641 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and full link, fresh progress and matcher, independent
retail/ELF span hashes and `cmp`, replacement build, project tool checks, all
six padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 21-word `func_150C5F40`. Keep the measured compiler boundaries
from Notes 216 and 217 parked unless new compiler or provenance evidence
appears.
