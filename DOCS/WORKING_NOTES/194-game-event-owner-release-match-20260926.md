# Game event-owner release handler match - 2026-09-26

## Result

`func_15190400` is byte-exact across all 21 words and 84 bytes at
`0x15190400..0x15190454`. Fresh totals are 2,697 / 5,469 exact C functions
overall and 2,126 / 4,791 in Game.

## Recovery

The function handles event byte zero. It compares the object's 32-bit owner at
offset `0x18` and byte discriminator at `0x1C` against the incoming record's
word and byte at offsets 0 and 4. If either field matches, it releases the
object through `func_1516972C`; nonzero events and complete mismatches return
without side effects.

Explicit temporaries reproduce retail's four consecutive field loads before
the first comparison. Expressing the second comparison as a nested early
return gives the required branch-likely cleanup path. IDO reverses that
comparison's source operands during lowering, so writing `temp_a2 != temp_a3`
reproduces retail's `bnel a3,a2`. All 21 words compile directly without
guarded retail words.

## Evidence

Linked ELF offset `0x1D0400` and decompressed retail offset `0x1BD8B0` compare
equal for 84 bytes, both with SHA-256
`b8231fb73fe2d92e312651d44bba9e27a8a684800ea1891f132a18d280083a39`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,697 / 5,469 (49.31%) | 1 | 2,771 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,126 / 4,791 (44.37%) | 0 | 2,665 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling and validation

`64CBFDOGL/recomp_out/.c` still contains the old two-instruction zero-return
generated body; a future controlled regeneration must consume this restored
guest function. The sibling's 1,659 dirty entries and frozen Release
executable remain untouched.

The focused object, full replacement link, fresh progress and LIST matcher,
independent span comparison, tool checks, six unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue ordinary Game matching with 21-word `func_15191B8C`, the next
nonblocked Game row at 18 differences. Init alternative `func_10001000`
remains at 14 differences; keep address-blocked `func_10012588` parked.
