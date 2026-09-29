# Game record-ID lookup byte match

Date: 2026-09-29

## Scope

This pass completed `func_151149AC` in
`conker/src/game/generated_13D350.c`. The retail slot spans 28 words and 112
bytes at `0x151149AC..0x15114A18`.

## Recovered behavior

The routine accepts an unsigned byte ID. ID zero is reserved and immediately
returns null. For every other ID, it scans the `D_800DBEF0` active records
starting at `D_800DBEF4`. Each record is `0xA0` bytes and stores its ID at
offset `0x72`. The first matching record is returned; an empty table or an
exhausted scan returns null.

Separate index, byte-offset, base, and cursor lifetimes reproduce retail's
single bounded loop. Keeping the global count directly in the loop condition
prevents IDO from unrolling the loop, while spelling the successful result as
`offset + base` preserves retail's commutative operand order. All 28 words and
the HI/LO relocation pairs for both globals emit directly from semantic C;
there are no expected-word guards.

A discarded local-count `do/while` experiment caused IDO to unroll the loop
four ways and expand the function to `0xF4` bytes. The retail-span guard
rejected that object, and none of the expanded form was retained.

## Verification

- The focused `generated_13D350.c.o` build matches all 28 retail words and all
  four data relocations directly from C.
- The incremental full `wsl make -C conker NON_MATCHING=1 -j1` rebuild and
  relink completed successfully.
- The linked ELF and retail 112-byte spans share SHA-256
  `1d8d1610b05bc50bc8c25302965ca183b2a1f4d02e1f8697796056b2166b48f5`.
- Fresh matcher totals are `2,943 / 5,465 (53.85%)` overall and
  `2,369 / 4,789 (49.47%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 29-word `func_151298C0`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
