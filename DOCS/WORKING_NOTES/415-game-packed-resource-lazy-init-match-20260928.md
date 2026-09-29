# Game packed-resource lazy initializer byte match

Date: 2026-09-28

## Scope

This pass completed `func_15116110` in
`conker/src/game/generated_142560.c`. The retail slot spans 27 words and 108
bytes.

## Recovered behavior

The routine returns immediately when the input record already has a handle at
offset `0x7C`. Otherwise it reads the packed word at offset `0x3C`, extracts a
15-bit selector and two independent bytes, and passes those fields with the
record pointer, a signed `-1` sentinel, and a zero flag to `func_15195FB0`.
The returned handle is stored at offset `0x7C`, then the packed source word is
cleared.

Recovering the selector as `u16` and the two extracted fields as `u8` restores
retail's `0x28` frame, 27-word length, selector-copy lifetime, argument count,
branch layout, call delay slot, result stores, and epilogue. IDO still chooses
a different closed register and instruction schedule for the three independent
masks and the two stack argument stores. Seven expected-word guards normalize
only that cycle. The other 20 words emit directly from semantic C.

## Verification

- The focused `generated_142560.c.o` build passed under the existing
  `-O2 -g3` profile.
- Post-guard object disassembly matches all 27 retail instruction words and
  the `func_15195FB0` call relocation.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed.
- `match_progress.py` classifies `func_15116110` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `d875f1fa9ab49b5c9f16a90e00a78da99489bcd27738cfee3ef6b462d6133135`.
- Fresh matcher totals are `2,917 / 5,466 (53.37%)` overall and
  `2,343 / 4,790 (48.91%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_1514DA38`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
