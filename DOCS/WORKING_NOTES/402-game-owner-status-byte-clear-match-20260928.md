# Game owner status-byte clear byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_150806A8` in
`conker/src/game/generated_AD9B0.c` with its semantic Game routine. The retail
slot spans 28 words and 112 bytes.

## Recovered behavior

The function indexes `D_800CC2D0` with its object-slot argument and reads the
object's `unk31C` owner/state pointer. It examines the adjacent bytes at offsets
`0x74` and `0x75`. Each byte is cleared only when it is nonzero and bit `0x80`
is not set; zero values and values carrying the high-bit flag are retained.

The source preserves retail's alias-sensitive lifetime. It caches the first
byte separately, clears it when eligible, and then reloads `object->unk31C`
before examining the second byte. Separate first and second value locals give
IDO retail's `a1` and `v0` allocation while preserving the branch-likely load
of the second byte. All 28 words emit directly from C; no expected-word guards
or compiler-profile changes are required.

## Verification

- The focused `generated_AD9B0.c.o` build passed under the existing profile.
- Focused object disassembly matches all 28 retail instruction words and
  relocations.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed.
- `match_progress.py` classifies `func_150806A8` as byte-exact.
- The linked and retail 112-byte spans share SHA-256
  `3e9c20b8f2a2d5ac38c781068c7119d964c98007c366f73f9d6ad5a8987b754e`.
- Fresh matcher totals are `2,904 / 5,466 (53.13%)` overall and
  `2,330 / 4,790 (48.64%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_15084D00`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
