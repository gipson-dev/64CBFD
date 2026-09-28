# Game two-word bit test byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_1503E1F4` in
`conker/src/game/generated_6B320.c` with its semantic Game routine. The retail
slot spans 27 words and 108 bytes.

## Recovered behavior

The function tests one bit in the 64-bit flag pair for
`D_800C6660[index]`. Bit numbers below 32 select `unk4`; all other bit numbers
select `unk8`. It returns one when the selected bit is set and zero otherwise.

The high-word path deliberately passes the original bit number to the MIPS
variable shift. `sllv` masks its shift count to five bits, so values 32 through
63 select the corresponding bit in `unk8` without an explicit subtraction.

The source keeps the two tests in an `if`/`else if` followed by one shared zero
return. That shape reproduces retail's duplicated index scaling, branch-likely
zero paths, two immediate one returns, and unreachable zero assignment before
the shared return. All 27 words emit directly from C; no expected-word guards
or compiler-profile changes are required.

## Verification

- The focused `generated_6B320.c.o` build passed under the existing profile.
- Focused object disassembly matches all 27 retail instruction words and
  relocations.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed.
- `match_progress.py` classifies `func_1503E1F4` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `149a553e39a8961ded8d1eb039d1b56f8c176a2343f34c6f71d59b3db9055d29`.
- Fresh matcher totals are `2,903 / 5,466 (53.11%)` overall and
  `2,329 / 4,790 (48.62%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_150806A8`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
