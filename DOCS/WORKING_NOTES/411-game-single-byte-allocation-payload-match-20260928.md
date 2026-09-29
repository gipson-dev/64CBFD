# Game single-byte allocation payload wrapper byte match

Date: 2026-09-28

## Scope

This pass completed `func_150D0134` in
`conker/src/game/generated_FC5F0.c`. The retail slot spans 27 words and 108
bytes.

## Recovered behavior

The wrapper forwards a byte selector, record-data pointer, signed halfword,
secondary byte, and final word to `func_150CFF10`. It supplies allocation mode
`8`, subtype `0`, and a zero auxiliary flag. If allocation succeeds, it reads
the destination pointer at offset `0x48` of the returned record and copies one
zero byte into that destination.

The shared allocator placeholder previously had an old-style `s32` signature.
Recovering its pointer return and argument widths lets IDO canonicalize the
wrapper's `u8` and `s16` formal arguments directly in registers. The local
payload is an eight-byte byte buffer whose first byte is initialized before
the allocator call. That shape reproduces retail's `0x38` frame and payload at
`sp+0x30`; a scalar byte instead produced a `0x30` frame and `sp+0x2F`.

All 27 words emit directly from semantic C. No expected-word guards or
compiler-profile changes are required. The recovered record-data pointer type
was also applied to the two neighboring wrappers that call the same allocator;
this removes incompatible pointer/integer warnings without changing ABI width
or claiming those wrappers as matched.

## Verification

- The focused `generated_FC5F0.c.o` build passed under the existing `-O2 -g3`
  profile without warnings.
- Focused object disassembly matches all 27 retail instruction words and both
  call relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150D0134` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `0d1eadac7711e811b1e7d805fefe01989a18b564686543b50b1a9af057183856`.
- Fresh matcher totals are `2,913 / 5,466 (53.29%)` overall and
  `2,339 / 4,790 (48.83%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_150E8854`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
