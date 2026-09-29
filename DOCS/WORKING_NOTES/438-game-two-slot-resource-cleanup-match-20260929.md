# Game two-slot resource cleanup byte match

Date: 2026-09-29

## Scope

This pass completed `func_150F739C` in
`conker/src/game/generated_124260.c`. The retail slot spans 28 words and 112
bytes at `0x150F739C..0x150F7408`.

## Recovered behavior

The routine treats owner offset `0x28` as a small resource subrecord. It scans
the two pointer slots at offsets `0x30` and `0x34`, calling `func_1516972C` for
each non-null entry. After the scan it calls `func_1514EDF0` with the owner and
the pointer stored at owner offset `0x28`.

The semantic C uses a byte-indexed two-entry loop. IDO emits 23 of the 28
retail words directly. Five guarded words omit one redundant opening zero
temporary, select the saved counter for the first indexed load, and normalize
the closed `v0`/`t8` lifetime used to truncate, compare, and write back the
incremented byte index. The two immediate wrappers were also corrected to
pointer/void signatures, removing incompatible pointer warnings without
changing their ABI or linked instructions.

## Verification

- The focused `generated_124260.c.o` build matches all 28 retail words and
  both call relocations after the five guarded compiler words.
- The shared patch-table change triggered a complete serial object rebuild;
  the original `wsl make NON_MATCHING=1 -j1` process completed successfully.
- The linked ELF and retail 112-byte spans share SHA-256
  `2224059e793572ec1e461b485fa463d8ed184af981c738c15b8bdfc55d53bb6a`.
- Fresh matcher totals are `2,939 / 5,465 (53.78%)` overall and
  `2,365 / 4,789 (49.38%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150FFB6C`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
