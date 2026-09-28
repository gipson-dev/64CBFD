# Game actor-target transform byte match

Date: 2026-09-28

## Scope

This pass replaced the zero-return placeholder for `func_151A4E34` in
`conker/src/game/generated_1D0840.c` with semantic C. The complete 26-word,
104-byte retail slot is now byte-exact.

## Recovered behavior

The routine receives a small caller record and an output transform pointer.
It follows the actor pointer at caller offset `0x00`, then reads the actor's
target pointer at offset `0x1D4`. A null target returns `0` without calling
the transform helper.

The second gate reads the actor byte at offset `0x74`. If its low nibble is
`0xF`, the routine also returns `0`. Otherwise, caller byte `0x05` selects a
64-byte target record and the routine calls:

```c
func_15143134(arg0 + 8, arg1, target + (arg0[5] << 6));
```

The successful path returns `1`. The recovered source reproduces retail's
two branch-likely gates, delay-slot loads, frame, call arguments, and return
paths.

## Compiler normalization

IDO emits the commutative address sum in the call delay slot as
`addu a2,t9,v1`; retail uses `addu a2,v1,t9`. One expected-word guard at
function offset `0x50` preserves retail's operand order. It has no relocation
and does not change the computed address, control flow, or memory behavior.

## Verification

- The focused `generated_1D0840` object build passed.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed with
  only the repository's existing IDO warnings.
- `match_progress.py` no longer lists `func_151A4E34` as different.
- The linked and retail 104-byte spans share SHA-256
  `b509f6c7a3fe22a678e98f30ba1602b5bc741eab0666884c09469ef9fdbcab9a`.
- The guard manifest contains exactly one row for this routine and no
  duplicate `(filename, function, offset)` keys.
- Fresh matcher totals are `2,894 / 5,466 (52.95%)` overall and
  `2,320 / 4,790 (48.43%)` in Game, with one address-drift row.

## Resume boundary

Continue the ordinary 25-difference Game queue with 26-word
`func_151F3D78`. Keep the tied Init SDK cache routines in their ownership lane
and keep address-drift row `func_10012588` parked.
