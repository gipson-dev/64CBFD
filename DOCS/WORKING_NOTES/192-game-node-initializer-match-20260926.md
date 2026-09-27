# Game node initializer match - 2026-09-26

## Result

`func_15178BE4` is byte-exact across all 20 words and 80 bytes at
`0x15178BE4..0x15178C34`. Fresh totals are 2,695 / 5,469 exact C functions
overall and 2,124 / 4,791 in Game.

## Recovery

The function narrows its selector to `u8`, calls `func_15178B98`, and, when a
node is found, stores the supplied pointer at offset `0x10`, sentinel
`0x80000000` at `0x14`, and a signed halfword at `0x30`.

The direct raw-node implementation matched 19 words immediately. Correcting
the third formal from `s32` to `s16` reproduced retail's big-endian ABI reload
with `lh` from `sp+0x22`; all 20 words then matched without guarded patches or
compiler-steering expressions. The known caller declaration was corrected to
the same signature.

## Evidence

Linked ELF offset `0x1B8BE4` and decompressed retail offset `0x1A6094` compare
equal for 80 bytes, both with SHA-256
`9c710896056e8c17946409cb801951aba3733dc00c0ed26a65bfb8a36b277773`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,695 / 5,469 (49.28%) | 1 | 2,773 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,124 / 4,791 (44.33%) | 0 | 2,667 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling and validation

`64CBFDOGL/recomp_out/.c` still contains the old zero-return generated body;
a future controlled regeneration must consume this restored guest function.
The sibling's 1,659 dirty entries and frozen Release executable remain
untouched.

The focused object, full replacement link, fresh progress and LIST matcher,
independent span comparison, tool checks, six unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue ordinary Game matching with 20-word `func_15187FC0`, the next
nonblocked Game row at 18 differences. Init alternative `func_10001000`
remains at 14 differences; keep address-blocked `func_10012588` parked.
