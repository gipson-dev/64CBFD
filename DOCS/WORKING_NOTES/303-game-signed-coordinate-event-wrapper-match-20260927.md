# Game signed-coordinate event wrapper match - 2026-09-27

## Result

`func_15044D40` is byte-exact across all 24 words and 96 bytes at
`0x15044D40..0x15044DA0`. Fresh totals are 2,807 / 5,469 (51.33%) exact C
functions overall and 2,235 / 4,791 (46.65%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered wrapper reads
three signed coordinates from offsets `0x6`, `0x8`, and `0xA` of the existing
`PositionScaleRecord71820`, converts them to floats, and forwards the signed
halfword at offset `0x10`. It calls `func_1505D1C4` with those four values and
trailing arguments `0xFF, 0, 0, 0`, then returns zero independently of the
void callee.

Declaring the callee's established eight-argument ABI is sufficient for IDO to
reproduce the 40-byte frame, coordinate load order, integer-to-float schedule,
four outgoing stack arguments, call delay slot, and explicit post-call result.
No guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x721C0` and pristine retail span at
`conker.us.bin+0x721F0` compare equal for all 96 bytes. Both have SHA-256
`b848b28be2b8e6f198978fdef7b26edb1566def1a2068d1c50f1e59ab72c736a`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,807 / 5,469 (51.33%) | 1 | 2,661 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,235 / 4,791 (46.65%) | 0 | 2,556 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 96-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,354 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 26-word Game `func_1507488C`, the next ordinary unparked C row
in the fresh 23-real-difference queue. Keep the documented smaller compiler,
SDK, and ownership rows parked in their existing queues.
