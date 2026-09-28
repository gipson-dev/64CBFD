# Game five-bucket byte canonicalizer byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_1503D5F0` in
`conker/src/game/generated_6A3D0.c` with its semantic Game routine. The retail
slot spans 28 words and 112 bytes.

## Recovered behavior

The function searches five byte-table buckets. `D_80098888[group]` gives the
number of entries in each bucket and `D_80084410[group]` points to its byte
table. When the input equals any byte in a bucket, the function returns that
bucket's first byte. If all five searches fail, it returns the original input.

The source uses direct `D_80084410[group][i]` indexing. This is important for
the retail allocation: the input remains in `a2`, the bucket base uses `a3`,
and the scan pointer uses `t0`, with no stack frame.

## Compiler profile

Default IDO `-O2` unrolls the inner byte loop four ways, expanding the
function to `0xFC` bytes. The retail object retains the loop. The
`generated_6A3D0` slice therefore uses the established
`-O2 -g3 -Wo,-loopunroll,0` profile.

A full repository rebuild and linked matcher scan increased the exact count by
exactly one function, confirming that this slice profile caused no collateral
loss among previously exact rows. All 28 target words emit directly from C;
no expected-word guards are required.

## Verification

- The focused `generated_6A3D0.c.o` build passed with the no-unroll profile.
- Focused object disassembly matches all 28 retail instruction words and
  relocations.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed.
- `match_progress.py` classifies `func_1503D5F0` as byte-exact.
- The linked and retail 112-byte spans share SHA-256
  `56c2590b5e3a77f9c9f80f334aa4e5736c07ef83de10fa409d160adf5948adf1`.
- Fresh matcher totals are `2,902 / 5,466 (53.09%)` overall and
  `2,328 / 4,790 (48.60%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_1503E1F4`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
