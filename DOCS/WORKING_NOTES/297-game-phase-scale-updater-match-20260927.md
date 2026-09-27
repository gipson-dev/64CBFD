# Game phase/scale updater match - 2026-09-27

## Result

`func_151DADA0` is byte-exact across all 34 words and 136 bytes at
`0x151DADA0..0x151DAE24`. Fresh totals are 2,801 / 5,469 (51.22%) exact C
functions overall and 2,230 / 4,791 (46.55%) in Game.

## Recovery

The existing C had the correct broad behavior but modeled the fields at object
offsets `0x110..0x118` independently. They are now represented by a typed
embedded state containing an unsigned phase byte, signed rate byte, and two
floats. The phase advances by rate times `D_800BE9E4`, wraps through its byte
store, and passes `(phase - 0x40) & 0xFF` to `func_151423D8`. The resulting
scale writes `firstScale * scale + 1.0f` to object offset `0x4C` and
`D_800AB4B0 - secondScale * scale` to offset `0x50`.

The typed state is the source-level key: IDO materializes the shared state base
in `v1` after the call and emits retail's first load/multiply/add/store before
loading the second coefficient. It also reproduces every floating-point
register and constant load directly.

IDO still assigns the phase sum to `t0` rather than retail's `a0` and folds
the masked call argument directly into `a0`. Four guarded rows normalize the
sum, byte store, bias subtraction, and mask; the mask row inserts retail's
explicit `or a0,t1,zero`. That insertion consumes the compiler's trailing
layout padding, preserving the exact 34-word extent. No behavior, constant,
branch, call, floating-point operation, or relocation is replaced.

## Evidence

Linked ELF file offset `0x21ADA0` and decompressed retail offset `0x208250`
compare equal across the complete 136-byte span. Both have SHA-256
`6723b622c69527ac88243bffdc7dc384d71bfc069638272ee12fce606ab64d8f`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,801 / 5,469 (51.22%) | 1 | 2,667 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,230 / 4,791 (46.55%) | 0 | 2,561 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching rebuild and link,
fresh progress and matcher, independent 136-byte hashes, and direct byte
comparison pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass. The guard
table has 1,350 rows with no duplicate-key or relocation validation errors.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its 1,659 pre-existing status entries;
none of its files were changed. Frozen Release was not built, modified, or
launched. Its `conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Init `func_1000B294`, the next ordinary unparked C row
in the fresh queue at 23 real instruction differences. Its current C walks the
three root records and repairs matching owner pointers in each root and child;
begin with its retail loop/addressing shape and repeated-load lifetimes.
