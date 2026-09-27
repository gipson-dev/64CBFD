# Game bounded-query wrapper match - 2026-09-27

## Result

`func_150A6500` is byte-exact across all 14 words and 56 bytes at
`0x150A6500..0x150A6538`. Fresh totals are 2,786 / 5,469 (50.94%) exact C
functions overall and 2,215 / 4,791 (46.23%) in Game.

## Boundary correction

The former 26-word inventory row actually contained two functions. The first
returns at `0x150A6534`; `0x150A6538` then allocates a different frame, calls
`func_150A6568`, restores that frame, and returns independently. The assembly
metadata and retail layout now identify the second entry as `func_150A6538`.

This raises the complete inventory from 6,040 to 6,041 functions. The new
12-word row remains exact original assembly because its incoming stack
contract is not yet source-grounded. A speculative six-argument C wrapper was
rejected: IDO emitted 15 words, exceeding the retail span, and would have
invented argument copies absent from retail. The C-function count therefore
remains 5,469 while raw assembly rises to 572.

## Recovery

The public wrapper accepts four register arguments. It forwards them to
`func_150A6568`, repeats the first two as arguments five and six, and supplies
`-10000` and `20000` as arguments seven and eight. Direct C reproduces the
40-byte frame, 14-word span, call, argument values, and return behavior.

IDO schedules the two constants, argument homes, return-address save, call,
and epilogue differently. Twelve guarded rows assert the exact compact input
and normalize those words. The `R_MIPS_26:func_150A6568` relocation moves from
compact offset `0x1C` to retail offset `0x20`; both removal and insertion are
guarded explicitly.

## Evidence

Linked ELF offset `0xE6500` and decompressed retail offset `0xD39B0` compare
equal across the complete 56-byte C span. Both have SHA-256
`be675159dec10194e305421bb202e9b9518ee517624b117e0f618135235deff0`.
The separated 48-byte assembly span at linked offset `0xE6538` and retail
offset `0xD39E8` is also equal, with SHA-256
`9f0e303065bb9cab9ff214631293614a3725b9d000cf96824022cd2296d6b0e9`.

| Section | C functions | Raw assembly | C bytes | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 572 | 1,931,576 / 2,256,728 (85.59%) | 2,786 / 5,469 (50.94%) | 1 | 2,682 |
| Init | 497 / 538 (92.38%) | 41 | 148,600 / 164,048 (90.58%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 530 | 1,763,336 / 2,072,880 (85.07%) | 2,215 / 4,791 (46.23%) | 0 | 2,576 |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, exhaustive all-object nonmatching
ELF rebuild, fresh progress and matcher, independent hashes, and direct byte
comparisons pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 23-word `func_150BE438`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
