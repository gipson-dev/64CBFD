# Game angle-tolerance match - 2026-09-26

## Result

`func_150767F4` is byte-exact across all 58 words, or 232 bytes, at
`0x150767F4..0x150768DC`. The fresh linked matcher reports 2,655 / 5,483 exact
C functions overall and 2,087 / 4,794 in Game.

## Recovered behavior

The existing C behavior is correct. It selects `D_800CC2D0` using the current
actor's byte at offset `0x222`, computes the horizontal angle from that object
to the actor through `func_1505A630`, and compares the masked angle delta with
twice `D_800D1891`. When the delta is inside that tolerance, it calls
`func_15075400(D_800D1890)`.

Sixteen guarded rows restore retail's integer register allocation after the
angle call. The first two preserve the `D_800D154C` HI16/LO16 relocation pair;
the remaining fourteen select retail's actor-index, shifted-angle, table
stride, doubled-tolerance, subtraction, and final-comparison registers. No C
source change was required. The patch table now contains 1,030 rows with zero
duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0xA3C74` and pristine retail span
`conker.us.bin+0xA3CA4` are both 232 bytes and compare equal. Both hash to:

`b23abcde8e3cf19458c5429db1dc0d397bdb41f008ca91c5ab68271ca270198d`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all project
tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_150767F4` in generated recompilation outputs and
configuration symbol lists, but no separate maintained hand implementation
was found. Its 1,659 existing dirty entries were left untouched. Frozen
Release was not built, modified, or launched; `build/Release/conker_pc.exe`
retains timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked. Its compact live C is intentionally
retained, but IDO emits a measured three-word overflow relative to its retail
slot; converting it back to assembly belongs to the separate raw-assembly
ownership workstream. Continue with 21-word `func_1507A428`, the next ordinary
Game C row with sixteen real differences. It packs four global bytes into a
word, forces bit zero on before complementing it, and stores the result in the
current actor's `unk94` field.
