# Game active-object flag scan match - 2026-09-27

## Result

`func_15179AB8` is byte-exact across its 23-word, 92-byte tracked span at
`0x15179AB8..0x15179B14`. Fresh totals are 2,736 / 5,468 (50.04%) exact C
functions overall and 2,165 / 4,790 (45.20%) in Game.

## Recovery

The routine starts at active-object index `D_800DD436 - 1` and scans backward
through the pointer array owned by `D_800DD440`. Null entries are skipped. For
each live object, it reads the word at offset `0x90`; entries already carrying
flag `0x2` are skipped, while the first eligible object receives that bit and
the routine returns immediately.

The matching C uses explicit signed index, object pointer, and flag-value
lifetimes. IDO naturally lowers the array walk to retail's byte offset in
`v1`, cursor in `a0`, and post-load `-4` updates. The null branch, flag test,
early return with the store in the return delay slot, and terminal `bgez`
loop all match directly. No guarded retail-word entries are required.

## Evidence

Linked ELF offset `0x1B9AB8` and decompressed retail offset `0x1A6F68` compare
equal for all 92 bytes. Both spans have SHA-256
`940ef12c88416ed016ef139dad5491ff725c85f7c5c9208d18932f0ede6c643b`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,468 / 6,039 (90.54%) | 2,736 / 5,468 (50.04%) | 1 | 2,731 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,790 / 5,319 (90.05%) | 2,165 / 4,790 (45.20%) | 0 | 2,625 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
92-byte span hashes and `cmp`, replacement build, project tool checks, all
padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Continue with 26-word `func_15194AB4`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep the previously documented
lower-difference rows parked.
