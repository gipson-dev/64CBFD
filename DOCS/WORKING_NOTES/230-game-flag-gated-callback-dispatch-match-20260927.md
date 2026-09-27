# Game flag-gated callback dispatch match - 2026-09-27

## Result

`func_15131C2C` is byte-exact across its 22-word, 88-byte tracked span at
`0x15131C2C..0x15131C84`. Fresh totals are 2,732 / 5,468 exact C functions
overall and 2,161 / 4,790 in Game.

## Recovery

The routine first narrows its third argument to an unsigned byte. It checks
bit `0x4000` in the object word at offset `0x68`, indexes callback table
`D_80089878` with the object byte at offset `0x75`, and forwards the original
object, second argument, and narrowed byte when the callback is nonnull.

Declaring the table with a typed three-argument callback contract reproduces
retail's incoming `a2` spill and narrowing, direct callback lifetime in `v0`,
`jalr` argument preservation, and shared epilogue. Both the flag-clear and
null-callback exits compile as branch-likely instructions with the RA reload
in their delay slots. No guarded retail words are needed.

## Evidence

Linked ELF offset `0x171C2C` and decompressed retail offset `0x15F0DC` compare
equal for all 88 bytes. Both spans have SHA-256
`0f9c9edd02a198a0416dc76b94408c401a85dd821f1989840c3d9a54023f4dec`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,468 / 6,039 (90.54%) | 2,732 / 5,468 (49.96%) | 1 | 2,735 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,790 / 5,319 (90.05%) | 2,161 / 4,790 (45.11%) | 0 | 2,629 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
88-byte span hashes and `cmp`, replacement build, project tool checks, all six
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with empty 24-word `func_1515F0AC`, the next unparked Game C row in
the fresh queue, with 20 real differences.
