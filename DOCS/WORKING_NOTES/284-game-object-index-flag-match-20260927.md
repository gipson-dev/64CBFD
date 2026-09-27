# Game object-index flag match - 2026-09-27

## Result

`func_150D1410` is byte-exact across all 23 words and 92 bytes at
`0x150D1410..0x150D146C`. Fresh totals are 2,788 / 5,469 (50.98%) exact C
functions overall and 2,217 / 4,791 (46.27%) in Game.

## Recovery

The false zero-return placeholder now recovers the original effect-state
update. It looks up effect `0xF9` through `func_151149AC`; if the lookup
succeeds, it computes the input object's index relative to `D_800CC2D0` using
the `0x32C` object stride. Effect byte `0x6E` becomes one for object index zero
and zero for every other index.

A compact boolean assignment produced equivalent behavior but IDO reduced the
choice to `sltiu`, four words shorter than retail. An explicit `if (index ==
0)`/`else` preserves the retail 23-word form, including the branch-likely zero
store in its delay slot, the one-valued fallthrough path, and the compiler's
otherwise unreachable duplicate zero store. No guarded retail words are
needed.

## Evidence

Linked ELF offset `0x111410` and decompressed retail offset `0xFE8C0` compare
equal across the complete 92-byte span. Both have SHA-256
`180399b2fd93bf50c1f85964a6bf46017f0bff06622fe9a97a30f2905101cff1`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,788 / 5,469 (50.98%) | 1 | 2,680 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,217 / 4,791 (46.27%) | 0 | 2,574 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching ELF relink, fresh
progress and matcher, independent 92-byte hashes, and direct byte comparison
pass. The replacement build, project tool checks, padding-tool unit tests,
outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 23-word `func_150D2054`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
