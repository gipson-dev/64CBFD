# Game position/scale initializer match - 2026-09-27

## Result

`func_15044CE4` is byte-exact across all 23 words and 92 bytes at
`0x15044CE4..0x15044D40`. Fresh totals are 2,784 / 5,469 (50.91%) exact C
functions overall and 2,213 / 4,791 (46.19%) in Game.

## Recovery

The false zero-return placeholder now recovers the original record
initializer. It copies three signed halfword position components from the
pointer at record offset `0x18`, divides the signed halfword reached through
offset `0x1C` by 32 with truncation toward zero, writes that result to the
three halfwords at offsets `0x10..0x14`, and calls `func_15044B78`.

Direct C reproduces retail's 24-byte frame, load/store order, negative-value
correction for signed division by 32, call delay slot, and epilogue. IDO uses
`a1` for the second pointer and `t9` for the quotient, while retail uses `t9`
and `t0`. Seven guarded rows assert the exact compiler input and normalize
only those independent register lifetimes. No instruction is inserted, no
relocation is moved, and control flow and behavior are unchanged.

## Evidence

Linked ELF offset `0x84CE4` and decompressed retail offset `0x72194` compare
equal across the complete 92-byte span. Both have SHA-256
`37ca0b9557fb759016a6023c73fee1e8eb5acaf0ff92967480af03dd4bfabaf1`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,040 (90.55%) | 2,784 / 5,469 (50.91%) | 1 | 2,684 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,320 (90.06%) | 2,213 / 4,791 (46.19%) | 0 | 2,578 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, exhaustive all-object nonmatching
ELF rebuild, fresh progress and matcher, independent 92-byte hashes, and
direct byte comparison pass. The replacement build, project tool checks,
padding-tool unit tests, outer nonmatching build, and whitespace check also
pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 36-word `func_1508855C`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
