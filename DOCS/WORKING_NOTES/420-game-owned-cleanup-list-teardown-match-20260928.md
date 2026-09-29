# Game owned cleanup-list teardown byte match

Date: 2026-09-28

## Scope

This pass completed `func_15178DA4` in
`conker/src/game/generated_1A5440.c`. The retail slot spans 28 words and 112
bytes at `0x15178DA4..0x15178E10`.

## Recovered behavior

The routine first passes the record's unsigned halfword at offset `0x2E` to
`func_100111C8`. It then walks the list headed by `D_800DCF3C`. Each iteration
saves the node at offset `0x08` before doing anything destructive; when the
node's owner at offset `0x14` equals the input record, the current node is
passed to `func_1516972C`. After the list is exhausted, the input record is
passed to `func_15169824` for final teardown.

A compact `CleanupNode` view records only the known next and owner fields.
Declaring both loop cursors at function scope is important to IDO's output:
the saved next pointer lives in `s0`, the input record lives in `s1`, and the
list head survives `func_100111C8` in retail's `sp+0x20` slot. Moving the
declaration into the loop makes IDO duplicate the common cursor update through
branch-likely paths and overrun the slot by one word. With the recovered
declaration order, all 28 words emit directly from semantic C. No
expected-word guards or compiler-profile override are required.

## Verification

- The focused `generated_1A5440.c.o` build passed under the existing
  `-O2 -g3` profile; all 28 words and five relocations match retail.
- The full `wsl make NON_MATCHING=1` rebuild and final relink passed from
  `conker`.
- `match_progress.py` classifies `func_15178DA4` as byte-exact without
  regressing the already-matched neighboring functions in the same slice.
- The linked ELF and retail 112-byte spans share SHA-256
  `4c71e7e00d926b0f5f3d26a468b5e9e78f540befe4c42b7e15adfaadd962c27f`.
- Fresh matcher totals are `2,922 / 5,466 (53.46%)` overall and
  `2,348 / 4,790 (49.02%)` in Game, with one address-drift row.
- `wsl make tools-check` passed, and all 9 tests under `tools/tests` passed.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_1517F3A0`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
