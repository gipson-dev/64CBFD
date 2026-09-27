# Game three-slot resource cleanup match - 2026-09-27

## Result

`func_150233E4` is byte-exact across all 23 words and 92 bytes at
`0x150233E4..0x1502343C`. Fresh totals are 2,803 / 5,469 (51.25%) exact C
functions overall and 2,231 / 4,791 (46.57%) in Game.

## Recovery

The old source was a zero-return placeholder. The recovered function walks the
three `0x38`-byte records from `D_800C3CA0` to the end symbol `D_800C3D48`.
For each record whose leading signed halfword is nonzero, it passes the pointer
at offset `0x34` to `func_1516D2E0`, clears that pointer, and clears the active
halfword. Inactive records are skipped.

The existing shared `struct163` already represented these records and retained
the correct `0x38` size. Its leading field is now signed to match retail's
`lh`, and its final four padding bytes are exposed as the resource pointer at
offset `0x34`. The only compiler difference after recovering the typed loop
was the order of two independent LO16 address completions. Two guarded,
relocation-aware rows schedule the `D_800C3D48` completion before the
`D_800C3CA0` completion without replacing any behavior.

## Evidence

The rebuilt span at `build/conker.us.bin+0x50864` and pristine retail span at
`conker.us.bin+0x50894` compare equal for all 92 bytes. Both have SHA-256
`34cb02339eb3c43068a7172810cbfbe8f197106b1f7574581056dc6d71f7f896`.
The function is absent from the fresh mismatch list.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,803 / 5,469 (51.25%) | 1 | 2,665 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,231 / 4,791 (46.57%) | 0 | 2,560 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-slice object build and disassembly, full nonmatching
rebuild and link, fresh progress/matcher scan, direct 92-byte comparison,
replacement build, outer ROM build, project tool checks, all seven
padding/relocation unit tests, guarded-table validation, and whitespace check
pass. The guard table has 1,354 rows with zero duplicate keys.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
no sibling file was changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_1503B95C`, the first ordinary unparked C row
in the fresh queue at 23 real differences. It is a generated-slice placeholder
with preserved retail assembly. Keep the documented lower-difference ownership
and compiler/callback rows in their separate queues.
