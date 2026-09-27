# Game dual event-record dispatch twin match - 2026-09-27

## Result

`func_151AA210` is byte-exact across all 21 words and 84 bytes at
`0x151AA210..0x151AA264`. Fresh totals are 2,743 / 5,469 (50.16%) exact C
functions overall and 2,172 / 4,791 (45.34%) in Game.

## Recovery

Retail `func_151AA210` is instruction-for-instruction identical to preceding
`func_151AA17C`. It constructs the same local target/code record from object
offsets `0x18` and `0x1C`, submits it to `func_15147D64` and `func_151494E0`
with selector `0xA`, then forwards the original object to `func_1519F3B8`.

The same volatile retained-pointer C shape reproduces 11 retail words and the
complete control flow. Ten new expected-word guards are scoped specifically to
`func_151AA210`; they independently restore this twin's saved-register
lifetime, target/code temporaries, and local slots. No relocation is patched,
and all three call delay slots match directly from C.

## Evidence

Linked ELF offset `0x1EA210` and decompressed retail offset `0x1D76C0`
compare equal across the complete 84-byte span. Both have SHA-256
`504ce272ab00711d2967c19d71cf5bae231fd2d29dbcc278f0a5cfff71cc2153`.
The shared hash is expected because the two retail function bodies are
instruction-identical; this span was nevertheless compared independently.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,743 / 5,469 (50.16%) | 1 | 2,725 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,172 / 4,791 (45.34%) | 0 | 2,619 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and repository-wide patch-table-dependent rebuild, fresh
progress and matcher, independent 84-byte span hashes and `cmp`, replacement
build, project tool checks, all padding-tool unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue with 21-word `func_151CF844`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
