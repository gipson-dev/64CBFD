# Second Game object-ID state pair byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholders for `func_1519BEB8` and
`func_1519BF20` in `conker/src/game/generated_1C2C60.c` with semantic C. They
are a second clear/set pair with the same retail behavior and instruction
shape as the earlier `func_151993E4` and `func_1519944C` pair documented in
Working Note 390.

## Recovered behavior

Both routines follow the pointer at caller offset `0x98`, dereference its
first object pointer, and read the object identifier byte at offset `0x3B`.
They scan the six identifiers beginning at `D_800A8A9C` using a post-tested
loop with a separate `found` flag. That form preserves retail's branch-likely
path and increments the index only after a mismatch.

On a match, the index selects a pointer from `D_800E0900` and the byte at
offset `0x14` is updated:

| Function | Words | Bytes | State value |
| --- | ---: | ---: | ---: |
| `func_1519BEB8` | 26 | 104 | `0` |
| `func_1519BF20` | 27 | 108 | `1` |

The false placeholder return types were corrected from `s32` to `void`. The
semantic bodies reproduce the complete retail extents, branch topology,
delay slots, relocations, and destination-register choices.

## Compiler normalization

As in the first pair, IDO retained the object identifier in `t1` while retail
used `a3`. Two expected-word guards per function normalize only the byte load
at offset `0x18` and its comparison branch at offset `0x20`. No guard changes
control flow, relocation ownership, memory addressing, or behavior.

## Verification

- The focused `generated_1C2C60` object build passed.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed with
  only the repository's existing IDO warnings.
- `match_progress.py` no longer lists either function as different.
- `func_1519BEB8` matches all 104 linked bytes with SHA-256
  `c8464001c0b64010f305d11578247894a585450784c081b4842195f15ac73c48`.
- `func_1519BF20` matches all 108 linked bytes with SHA-256
  `4d26007fda5e45bafa7f3fa426bb211ab60c73fafbf1ccad91a3147094e7a323`.
- The guard manifest contains exactly two rows for each routine and no
  duplicate `(filename, function, offset)` keys.
- Fresh matcher totals are `2,893 / 5,466 (52.93%)` overall and
  `2,319 / 4,790 (48.41%)` in Game, with one address-drift row.

## Resume boundary

Continue the ordinary 25-difference Game queue with 26-word
`func_151A4E34`. Keep the tied Init SDK cache routines in their ownership lane
and keep address-drift row `func_10012588` parked.
