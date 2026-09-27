# Game conditional callback and hidden no-op match - 2026-09-26

## Result

`func_15178750` is byte-exact across 21 words and 84 bytes at
`0x15178750..0x151787A4`. Newly inventoried `func_151787A4` is byte-exact
across two words and eight bytes at `0x151787A4..0x151787AC`. Fresh totals are
2,721 / 5,470 exact C functions overall and 2,150 / 4,792 in Game.

## Recovery

`func_15178750` follows the pointer at argument offset `0x14`, tests bit
`arg2` in byte `0x36`, and returns `func_15168118(arg0)` when the bit is set.
Otherwise it returns `arg0`. Typed pointer and signed-halfword arguments make
IDO reproduce all 21 retail words directly, including argument homing,
normalization, bit construction, retained fallback result, and both epilogues.

The old retail layout incorrectly extended this wrapper through
`0x151787AC`. The final `jr ra; nop` pair begins at `0x151787A4`, and
`D_8008CB64` directly stores that address beside two other callback functions.
This proves it is an independent no-op callback rather than padding. Adding
`func_151787A4` to tracked `symbol_addrs.us.txt` and splitting
`retail_layout.us.txt` makes a fresh splat extraction regenerate the separate
assembly label and symbolic table reference. The empty `void` C body emits the
two retail words directly.

## Evidence

Linked ELF offset `0x1B8750` and decompressed retail offset `0x1A5C00` compare
equal for the combined 92 bytes, both with SHA-256
`f307fce3f160a10be38bf97d7a75d49ddee5383998957b956b7498a21c236cd9`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,470 / 6,039 (90.58%) | 2,721 / 5,470 (49.74%) | 1 | 2,748 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,792 / 5,319 (90.09%) | 2,150 / 4,792 (44.87%) | 0 | 2,642 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

Fresh extraction from tracked symbol metadata, the focused object and full
link, fresh progress and matcher, independent combined-span comparison,
replacement build, project tool checks, all six padding-tool unit tests, outer
build, and `git diff --check` pass.

## Next boundary

Continue with 21-word `func_150C522C`. Keep the measured compiler boundaries
from Note 216 parked unless new compiler or provenance evidence appears.
