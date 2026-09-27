# Game object-record writer match - 2026-09-27

## Result

`func_150BE438` is byte-exact across all 23 words and 92 bytes at
`0x150BE438..0x150BE494`. Fresh totals are 2,787 / 5,469 (50.96%) exact C
functions overall and 2,216 / 4,791 (46.25%) in Game.

## Recovery

The false zero-return placeholder now recovers the complete record writer. It
indexes the object table at `D_800CC2D0` by `arg1 * 0x32C`, writes constant
halfwords `0x68` and `0x0E`, truncates the object's signed words at offsets
`0x2E8` and `0x2E4` into the remaining two halfwords, and returns the output
pointer advanced by eight bytes.

The C uses a byte-addressed object base and a halfword output pointer. Writing
the fields in logical output order reproduces retail's eight-instruction
shift/add multiplication, table-address relocations, object loads, halfword
stores, and return schedule directly. No guarded retail words are needed.

## Evidence

Linked ELF offset `0xFE438` and decompressed retail offset `0xEB8E8` compare
equal across the complete 92-byte span. Both have SHA-256
`d484a1ceeb46dfcbb7716528fc3e1a2264d29e766db12234881c54607e94459a`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,787 / 5,469 (50.96%) | 1 | 2,681 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,216 / 4,791 (46.25%) | 0 | 2,575 |
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

Continue with 23-word `func_150D1410`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
