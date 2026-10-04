# Game Random Range Position Recovery And Match

Date: 2026-10-04. Starting HEAD: `5e5a5d11`.

## Recovery

Replace `func_150E6F18`'s zero-return placeholder in `generated_113D60.c`
with its original three-axis range interpolation. The function returns void
and writes three floats through its output pointer.

`D_80088A44` is a table of six pointers, confirmed in `22D4E0.rodata.s`.
Its entries reference `D_800A1200`, `D_800A1218`, `D_800A1230`, `D_800A1248`,
`D_800A1260` and `D_800A1278`. Select with `(u32)func_150ADA20() % 6`,
preserving retail unsigned division even when the RNG word's sign bit is set.
Capture the selected pointer before `func_150ADA68()`; read its six fields
after that call. For each axis, write base plus (end minus base) times the
sampled fraction. Stores remain interleaved with subsequent axis reads.
Do not snapshot all input fields, clamp the fraction or add null handling.

The initial delta-first expression produced three commutative float-add
operand differences. Spelling each expression as base plus delta times
fraction resolves all three directly in C. No instruction guards are added.

## Exact Slot

All 37 words / 148 bytes match retail at `0x150E6F18..0x150E6FAC`, including
the 32-byte frame, saved pointer lifetime, unsigned division, RNG calls,
floating-point register schedule and epilogue. Both entry and next-function
addresses remain unchanged. No target rows exist in `retail_word_patches.us.csv`.

Fresh production ELF bytes equal ROM slice `0x1143C8..0x11445C`.
SHA-256: `8828477f7316bbbe628ae6168d4633058b09976ec18079502e53276cbfac4be2`.
An independent IDO build of the actual extracted body also matches the whole
slot without project padding or word patches.

## Verification

New `tools/tests/test_game_random_range_position.py` contains four tests:

- Sixteen integer RNG samples and six fractions: 96 combinations, including
  unsigned high-bit selection, endpoints and synthetic extrapolation samples.
  Check call order/count, three output stores, sentinels and unchanged inputs.
- Float RNG mutates the selected fields and replaces all table pointers:
  output uses the previously captured pointer but newly read field values.
- Six records and seven overlapping output offsets: 42 cases preserving
  sequential axis reads/stores rather than snapshot semantics.
- Warning-clean independent IDO compilation and complete retail slot equality.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_random_range_position tools.tests.test_game_position_publication tools.tests.test_game_object_position_sound_adapter -v -f
```

The combined run passes all 14 tests in 0.858 seconds, no skips. Host fixtures
use ordinary finite exactly representable values; they do not qualify NaNs,
infinities, FPCSR behavior or hardware. Guest instruction equality preserves
the original floating-point operations and ordering.

Fresh matcher: total 3274 / 5463 exact (59.93%), Game 2601 / 4790 (54.30%),
Init 492 / 492 and Debugger 181 / 181; zero address drift, 2189 still different.
Conversion totals do not change because the placeholder was already counted
as C. README receives aggregate rows only; detailed recovery stays here.

## Remaining Init Work

The 47-entry inventory in Note 909 remains unchanged. `func_10005BE0`
(19 words) and `func_100038E0` (11 words) are small ordinary-C candidates,
but neither currently has a production-ready full match. Bitmap lifetime
trials in Note 910 did not resolve the nineteenth-word limit.

The connected ten-entry decoder now has a qualified 4512-byte candidate,
528 bytes above its 3984-byte retail footprint. Notes 911-914 supersede
Note 909's older 544-byte deficit: both masked CU1 corpora pass, but complete
footprint fitting, private-stack reservation, entry/frame ownership and
hardware/context gates remain open. Passing corpora is not adoption approval.
Retain handwritten SDK, boot and hardware assembly; do not force a 100% C count.

Unrelated actor/timeline edits remain excluded. No sibling port build,
Release change or push.
