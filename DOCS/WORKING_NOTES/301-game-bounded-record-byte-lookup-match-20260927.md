# Game bounded record-byte lookup match - 2026-09-27

## Result

`func_1503DA3C` is byte-exact across all 24 words and 96 bytes at
`0x1503DA3C..0x1503DA98`. Fresh totals are 2,805 / 5,469 (51.29%) exact C
functions overall and 2,233 / 4,791 (46.61%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered function indexes
the 187-pointer table at `D_800D19A0`. A nonnull entry follows a `0x38`-byte
header whose final words hold an optional byte-buffer pointer at offset `0x30`
and unsigned byte count at offset `0x34`. Null entries, indices outside that
count, and absent byte buffers return sentinel `0xFF`; valid lookups return the
selected unsigned byte.

The local `RecordByteBuffer` type gives IDO the retail field loads while the
header expression places the `-0x38` adjustment in the null-check delay slot.
The unsigned count comparison produces retail's `sltu` and branch-likely load.
A ternary nullable-buffer expression preserves the initialized `v1` sentinel,
conditional `lbu`, and common return tail. No guarded words are used.

## Evidence

The rebuilt span at `build/conker.us.bin+0x6AEBC` and pristine retail span at
`conker.us.bin+0x6AEEC` compare equal for all 96 bytes. Both have SHA-256
`cd897bcd1ed09dca607a2f374dde0d76ecbdeb299e2806264d6f6a901876d3d3`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,805 / 5,469 (51.29%) | 1 | 2,663 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,233 / 4,791 (46.61%) | 0 | 2,558 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice build and disassembly, full nonmatching link,
fresh progress/matcher scan, direct 96-byte comparison, replacement build,
outer ROM build, project tool checks, all seven padding/relocation unit tests,
guarded-table validation, and whitespace check pass. The guard table remains
at 1,354 rows with zero duplicate keys.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_1503F904`, the first ordinary unparked C row
in the fresh queue at 23 real differences. It is a generated-slice wrapper
placeholder with preserved retail assembly. Keep the documented
lower-difference ownership and compiler/callback rows in their separate queues.
