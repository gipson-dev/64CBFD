# Game object-request wrapper match - 2026-09-27

## Result

`func_1514EE70` is byte-exact across all 23 words and 92 bytes at
`0x1514EE70..0x1514EECC`. Fresh totals are 2,795 / 5,469 (51.11%) exact C
functions overall and 2,224 / 4,791 (46.42%) in Game.

## Recovery

The zero-return placeholder was a false prototype. The function is a
`void(u8 *)` callback that builds an eight-byte request on its stack. The
request contains the incoming object pointer, the object's unique ID from byte
`0x3B`, a zero byte, and the halfword size `0x12C` (300).

The callback passes that request to `func_1515BE50` with arguments zero,
`0xFF`, and one. It then forwards the returned value and original object to
`func_1514EC1C` with event ID `0x16`. Expressing the request as a typed
structure gives IDO the retail frame and store order directly.

No guarded instruction rows are required. The compiler emits the complete
retail body, including the 40-byte frame, saved-return-address lifetime,
incoming argument home, request stores, both call delay slots, and
`R_MIPS_26` relocations for `func_1515BE50` and `func_1514EC1C`.

## Evidence

Linked ELF offset `0x18EE70` and decompressed retail offset `0x17C320` compare
equal across the complete 92-byte span. Both have SHA-256
`b46f3cea976c6aa50753d281c7c1ca16951ec531127b624c67ab126b30c7af4c`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,795 / 5,469 (51.11%) | 1 | 2,673 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,224 / 4,791 (46.42%) | 0 | 2,567 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching rebuild and link,
fresh progress and matcher, independent 92-byte hashes, and direct byte
comparison pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 25-word `func_1514F130`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
