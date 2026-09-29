# Game actor-slot creation adapter byte match

Date: 2026-09-29

## Scope

This pass completed `func_150E32D0` in
`conker/src/game/generated_1104D0.c`. Its tracked retail slot spans 28 words
and 112 bytes at `0x150E32D0..0x150E3340`.

## Recovered behavior

The routine is a fixed-configuration adapter around `func_150E3020`. It
forwards the first three integer coordinates, supplies zero for the fourth
through sixth arguments, forwards the caller's fifth argument and
single-precision sixth argument, then forwards the caller's fourth argument.
Three float fields and one integer field are zeroed, and the final signed
halfword selector is `-99`.

If `func_150E3020` returns null, the adapter returns zero. Otherwise it reads
the created actor's slot byte at offset `0x48` and returns that slot plus one.

The key ABI correction was giving the still-unrecovered `func_150E3020`
placeholder its full 14-argument signature. Without that declaration, C's
default argument promotions widened the four float arguments to doubles,
producing an 88-byte frame and overflowing this routine's retail slot. The
recovered prototype preserves each float as a single 32-bit stack argument.
The complete wrapper then emits directly from C with no expected-word guards.

## Verification

- The focused compact object matches all 28 retail words and the direct-call
  relocation for `func_150E3020`.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt and linked the complete ELF
  and binary successfully.
- The complete linked ELF and pristine retail spans share SHA-256
  `0c4470a908e85d619883409c95c287e4b01e2232345c2f15cc6984cc0ab0588e`.
- Fresh matcher totals are `2,959 / 5,465 (54.14%)` overall and
  `2,385 / 4,789 (49.80%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 29-word `func_15104170`, at 28
real differences. Keep `func_15194320` and `func_15194394` parked behind
generated-slice jump-table and rodata ownership, `func_151F3D78` parked behind
audio-object layout drift, the tied Init SDK cache routines in their ownership
lane, and `func_10012588` parked on address drift.
