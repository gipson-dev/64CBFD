# Game callback-table loop match - 2026-09-27

## Result

`func_1516706C` is byte-exact across its 21-word, 84-byte tracked span at
`0x1516706C..0x151670C0`. This brings the project to exactly 2,734 / 5,468
(50.00%) byte-exact C functions overall and 2,163 / 4,790 (45.16%) in Game.

## Recovery

The routine walks three no-argument callback slots beginning at `D_8008CB64`.
It calls each nonnull entry, advances by one pointer, and stops at the distinct
one-past-end symbol `D_8008CB70`.

The former `for` loop used `< &D_8008CB64[3]`, which made IDO emit `sltu` plus
`bnezl` and derive both relocations from the start symbol. Naming
`D_8008CB70` restores endpoint provenance, while a `do/while` expresses the
retail routine's guaranteed first iteration and direct `bnel` loop tail.

That C emits the complete 21-word body with the retail frame, saved-register
lifetimes, callback preload, null branch, `jalr`, cursor increments, loop
branch, and epilogue. IDO constructs the cursor's low half before the
endpoint's; retail schedules the two independent `addiu` instructions in the
opposite order. Two guarded entries swap those words and their
`R_MIPS_LO16:D_8008CB64`/`R_MIPS_LO16:D_8008CB70` relocations.

## Evidence

Linked ELF offset `0x1A706C` and decompressed retail offset `0x19451C` compare
equal for all 84 bytes. Both spans have SHA-256
`2e77ca36f960f7f9e2116dfb8a2453897fe582f432ea2d5726a978f3f2c01fa6`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,468 / 6,039 (90.54%) | 2,734 / 5,468 (50.00%) | 1 | 2,733 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,790 / 5,319 (90.05%) | 2,163 / 4,790 (45.16%) | 0 | 2,627 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
84-byte span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 29-word `func_15168A9C`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
