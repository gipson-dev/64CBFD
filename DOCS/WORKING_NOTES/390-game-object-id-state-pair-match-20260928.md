# Game object-ID state pair byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholders for `func_151993E4` and
`func_1519944C` in `conker/src/game/generated_1C2C60.c` with semantic C. The
two adjacent routines are structural twins: the first clears a per-object
state byte and the second sets it.

## Recovered behavior

Each routine follows the pointer at caller offset `0x98`, dereferences its
first object pointer, and reads the object's identifier byte at offset `0x3B`.
It scans the six identifiers beginning at `D_800A8A9C` with retail's
post-tested loop shape. A separate `found` flag keeps the index increment on
the mismatch path and reproduces the branch-likely control flow.

When an identifier matches, the index selects a row from `D_800E0900`. The
byte at row offset `0x14` is written as follows:

| Function | Words | Bytes | State value |
| --- | ---: | ---: | ---: |
| `func_151993E4` | 26 | 104 | `0` |
| `func_1519944C` | 27 | 108 | `1` |

Both return types were corrected from the false placeholder's `s32` to
`void`. The source-level reconstruction naturally reproduces each routine's
length, branches, delay slots, relocations, and destination registers.

## Compiler normalization

IDO retained the object identifier in `t1`, while retail retained it in `a3`.
Two expected-word guards per function normalize only that independent
register lifetime: the byte load at offset `0x18` and comparison branch at
offset `0x20`. The four rows do not alter control flow, relocations, memory
addresses, or observable behavior.

## Verification

- `wsl make NON_MATCHING=1` completed successfully from the repository root.
- `match_progress.py` reports both functions byte-exact and no longer lists
  either routine as different.
- `func_151993E4` linked and retail spans match across all 104 bytes with
  SHA-256 `c8464001c0b64010f305d11578247894a585450784c081b4842195f15ac73c48`.
- `func_1519944C` linked and retail spans match across all 108 bytes with
  SHA-256 `4d26007fda5e45bafa7f3fa426bb211ab60c73fafbf1ccad91a3147094e7a323`.
- Fresh matcher totals are `2,891 / 5,466 (52.89%)` overall and
  `2,317 / 4,790 (48.37%)` in Game, with one address-drift row.

## Resume boundary

Continue the ordinary Game queue with 26-word `func_1519BEB8`, currently at
25 real word differences. Keep the tied Init SDK cache routines in their
ownership lane and keep address-drift row `func_10012588` parked.
