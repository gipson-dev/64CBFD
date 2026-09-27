# Init owner-reference repair match - 2026-09-27

## Result

`func_1000B294` is byte-exact across all 24 words and 96 bytes at
`0x1000B294..0x1000B2F0`. Fresh totals are 2,802 / 5,469 (51.23%) exact C
functions overall and 391 / 497 (78.67%) in Init.

## Recovery

The function walks the three root pointers between `D_800417B0` and
`D_800417BC`. For each nonnull root, it replaces an `unk10` owner link equal
to the caller's old owner token with the root's own address. It performs the
same repair for the root's optional `unk60` child.

IDO 5.3 otherwise expands this short table walk. The `init_B1B0` object now
uses `-Wo,-loopunroll,0`, producing retail's rolled loop. A dead initial load
from `D_800417B0` is immediately overwritten but establishes retail's register
allocation. It has no runtime effect. Two guarded, relocation-aware word rows
swap the address-completion schedule for `D_800417BC` and `D_800417B0`; no
branch, comparison, pointer update, or store is replaced.

The object setting initially changed neighboring `func_1000B548`, whose retail
body reflects a four-record compiler unroll. Its source now advances by four
records and spells out those four equivalent probes. This preserves the same
12-record order, three-result cap, pointer updates, and return value while
retaining the existing exact 60-word / 240-byte retail body.

## Evidence

The rebuilt and pristine retail spans at `conker.us.bin+0xB294` compare equal
for all 96 bytes and share SHA-256
`ad0edae69f854280e9d41108ee65b8864678d1970a22f5f81636712fb8bda604`.
The rebuilt and retail `func_1000B548` spans at offset `0xB548` also compare
equal for all 240 bytes and share SHA-256
`eb7707577130996bbd98794241d816573178cc3f7cd949a9b6e8212bfee9ea24`.
Neither function appears in the fresh matcher difference list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,802 / 5,469 (51.23%) | 1 | 2,666 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,230 / 4,791 (46.55%) | 0 | 2,561 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object disassembly, clean full nonmatching rebuild and link, fresh
progress/matcher scan, replacement build, outer ROM build, project tool checks,
all seven padding/relocation unit tests, two direct byte comparisons, and
whitespace validation pass. The two guarded rows include the expected LO16
relocations and pass the tool validator.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 23-word Game `func_150233E4`, the first ordinary unparked C row
in the fresh queue at 23 real differences. Keep handwritten startup and SDK
assembly, and the documented compiler/callback experiments, in their separate
ownership or parked queues.
