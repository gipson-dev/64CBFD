# Game state-to-animation selector match - 2026-09-27

## Result

`func_15194AB4` is byte-exact across its 26-word, 104-byte tracked span at
`0x15194AB4..0x15194B1C`. Fresh totals are 2,737 / 5,468 (50.05%) exact C
functions overall and 2,166 / 4,790 (45.22%) in Game.

## Recovery

The routine sets every low flag bit except bit zero in the object word at
offset `0x9C`, then maps object state `0x75` to animation selector `0x73` and
state `0x80` to selector `0x72`. Other states retain the `-1` sentinel and do
not call `func_15083568`. A valid selector is forwarded with float bits
`0x3F800000` and a zero final argument.

The previous model returned `s32` and explicitly returned zero, which added a
result write and produced the wrong branch layout. Restoring the `void`
contract and expressing the two mappings as a `switch` recovers the retail
registers and branch-likely shape. Placing the default `-1` assignment after
the flag store gives IDO the exact retail store/branch-delay schedule. No
guarded retail-word entries are required.

## Evidence

Linked ELF offset `0x1D4AB4` and decompressed retail offset `0x1C1F64`
compare equal for all 104 bytes. Both spans have SHA-256
`40de0694c6e29793a6fbb3f72e0080b97e0d8e4d940106fa98005d1c23e5aefd`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,468 / 6,039 (90.54%) | 2,737 / 5,468 (50.05%) | 1 | 2,730 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,790 / 5,319 (90.05%) | 2,166 / 4,790 (45.22%) | 0 | 2,624 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
104-byte span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 31-word `func_151957B0`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
