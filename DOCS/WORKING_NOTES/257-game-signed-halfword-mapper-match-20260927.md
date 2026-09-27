# Game signed-halfword mapper match - 2026-09-27

## Result

`func_150FB240` is byte-exact across all 23 words and 92 bytes at
`0x150FB240..0x150FB29C`. Fresh totals are 2,760 / 5,469 (50.47%) exact C
functions overall and 2,189 / 4,791 (45.69%) in Game.

## Recovery

The prior C body was a false zero-return placeholder. Retail accepts a byte
destination and four signed halfwords. If `(arg2 - arg3) < arg1`, it stores
the low byte of `(arg2 - arg1) * arg4`; otherwise it stores `0xFF`.

The typed signature naturally emits the incoming argument homes and signed
halfword normalization. The direct condition and arithmetic then reproduce
retail's signed comparison, `multu`, low-product extraction, early return, and
fallback store without guarded words. The two adjacent callers already supply
the same five-argument halfword contract.

## Evidence

Linked ELF offset `0x13B240` and decompressed retail offset `0x1286F0` compare
equal across the complete 92-byte span. Both have SHA-256
`ed9e5f96fd8e8f732dec356a12071b0c2f1ae9fbc689027f40b0592cb842106d`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,760 / 5,469 (50.47%) | 1 | 2,708 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,189 / 4,791 (45.69%) | 0 | 2,602 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, clean-source full link, fresh
progress and matcher, independent 92-byte span hashes, and `cmp` pass. The
repository-wide padded replacement build, project tool checks, all seven
padding-tool unit tests, outer `NON_MATCHING=1` build, and staged
`git diff --check` also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing normal-status
entries; none were changed. Frozen Release was not built, modified, or
launched, and `build/Release/conker_pc.exe` remains 13,712,896 bytes with
timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 22-word `func_150FFD2C`, the next unparked Game C row in the
fresh queue at 21 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
