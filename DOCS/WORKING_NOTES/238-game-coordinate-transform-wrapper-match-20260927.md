# Game coordinate-transform wrapper match - 2026-09-27

## Result

`func_151A8F1C` is byte-exact across all 20 words and 80 bytes at
`0x151A8F1C..0x151A8F6C`. Fresh totals are 2,741 / 5,469 (50.12%) exact C
functions overall and 2,170 / 4,791 (45.29%) in Game.

## Recovery

The function forwards the pointer at object offset `0x2C` to
`func_151432BC`, followed by `arg1`, `arg1 + 2`, `arg2`, and `arg3`. After the
transform call, it copies `arg2[0]` into `arg1[1]`.

Declaring the callee with its complete five-argument float-pointer contract and
typing the wrapper as `void` reproduces retail directly. IDO emits the original
argument spills, fifth stack argument, call delay-slot store, post-call pointer
reloads, and return-frame teardown without guarded retail-word scheduling.

## Evidence

Linked ELF offset `0x1E8F1C` and decompressed retail offset `0x1D63CC`
compare equal across the complete 80-byte span. Both have SHA-256
`d30780df86a38014cb46919b17c975e7767d1829f0b156339d10252c415e2dfd`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,741 / 5,469 (50.12%) | 1 | 2,727 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,170 / 4,791 (45.29%) | 0 | 2,621 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
80-byte span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 21-word `func_151AA17C`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
