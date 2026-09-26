# Game packed actor-mask match - 2026-09-26

## Result

`func_1507A428` is byte-exact across all 21 words, or 84 bytes, at
`0x1507A428..0x1507A47C`. The fresh linked matcher reports 2,656 / 5,483 exact
C functions overall and 2,088 / 4,794 in Game.

## Recovered behavior

The existing C behavior is correct. It packs bytes `D_800D1890` through
`D_800D1893` into a 32-bit value, forces bit zero on, complements the packed
mask, and stores it in the current actor's `unk94` field.

Sixteen guarded rows restore retail's compiler schedule. Four relocation pairs
for `D_800D1890..D_800D1893` are preserved while the byte loads move into
retail's `t7`, `t0`, `t4`, and `t9` lifetimes. The rows also restore the
interleaved fourth address materialization, three shifts and combinations,
the final `v0` packed value, and the `t0` force/complement/store lifetime. The
current-actor relocation pair and return words already match, and no C source
change was required. The patch table now contains 1,046 rows with zero
duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0xA78A8` and pristine retail span
`conker.us.bin+0xA78D8` are both 84 bytes and compare equal. Both hash to:

`5db71840ee7756a402ac0cea1be74eecef27f9c9e9bed3ad6970c34d333fcdfb`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all project
tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_1507A428` in generated recompilation outputs and
configuration symbol lists, but no separate maintained hand implementation
was found. Its 1,659 existing dirty entries were left untouched. Frozen
Release was not built, modified, or launched; `build/Release/conker_pc.exe`
retains timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Continue with 20-word `func_15084CB0`, the next ordinary Game C row
with sixteen real differences. Its current C performs a bounded linear search
through the `u16` table at `D_800BE598`, using `D_800BE590` as the count, and
returns the matching index or zero when no entry matches.
