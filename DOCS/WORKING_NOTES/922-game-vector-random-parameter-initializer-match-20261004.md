# Game Vector Random Parameter Initializer Match

Date: 2026-10-04. Starting HEAD: `27833ab5`.

## Semantic Recovery

Replace `func_150E70EC`'s zero-return placeholder in `generated_113D60.c`
with a void four-argument initializer. First two word arguments are unused
by the retail body; the third is a float input vector and fourth an eight-float
output region. Preserve the original four-argument ABI and incoming spills.

The eight stores occur in this order:

| Output index | Value |
| --- | --- |
| 0 | `func_150484A0(vector[0], vector[2])` |
| 2 | First RNG sample times `D_800A1310` |
| 4 | Second RNG sample times `D_800A1314` |
| 6 | Third RNG sample times 0.5 |
| 1 | `func_150484A0(sqrtf(X*X + Z*Z), vector[1]) - D_800A1318` |
| 3 | Fourth RNG sample times `D_800A131C` |
| 5 | Fifth RNG sample times `D_800A1320` |
| 7 | Sixth RNG sample times 0.5 |

The second vector helper's inputs are read after the first four stores and
three RNG calls. Do not snapshot the vector or all global scales at entry;
overlapping output and callback changes must affect later reads. No clamp,
null handling or new return value is added. Helper identity is kept as its
existing symbol rather than inferred from its use here.

Retail constants in `245C90.rodata.s` are respectively words `3DB851EC`,
`40C90FDB`, `3FC90FDB`, `3D8F5C29`, `40C90FDB` (approximately 0.09,
6.283185482, 1.570796371, 0.07 and 6.283185482). Preserve global loads;
do not replace the source data with newly rounded decimal literals.

## Direct Match

The initial X-square plus Z-square source form reverses IDO's load/multiply
sequence. Spelling the sum as Z-square plus X-square restores the retail
emitted order directly. No instruction guards or profile changes are needed.

All 62 words / 248 bytes at `0x150E70EC..0x150E71E4` match pristine ROM
slice `0x11459C..0x114694`, including 0x20 frame, saved registers, first two
argument spills, six RNG calls, output delay-slot stores and square-root
instruction. Entry and next-function addresses are fixed. No target CSV guards.

Fresh linked slot SHA-256:
`8f8b8f790d42fbb9562436f8b0d5b74e6a982dca3266ebd7c7098e42e25a6b94`.

## Verification

New `tools/tests/test_game_vector_random_parameters.py` contains five tests:

- Eight outputs and six distinct samples, including synthetic values outside
  0..1; callbacks verify prior outputs are already published at each call.
- Zero vector/samples still execute all calls and apply the vertical offset.
- RNG callbacks change a scale, vector and offset; later reads observe them.
- Input/output overlap makes the horizontal calculation use earlier output
  stores, with surrounding sentinel checks.
- Independent warning-clean IDO build equals all 248 retail bytes without
  project padding or guards, with only zero trailing section alignment.

The standalone build must include the SDK's `#pragma intrinsic(sqrtf)` from
`PR/gu.h`; the initial test omitted it and attempted to link an external call.
The final test includes the directive and matches retail's inline `sqrt.s`.
The overlap fixture's expected value uses explicit float-rounding steps to
avoid comparing a stored float against an x87 extended intermediate.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_vector_random_parameters tools.tests.test_game_linked_record_position tools.tests.test_game_random_range_position -v -f
```

All fourteen tests pass in 1.777 seconds, no skips. Host fixtures use synthetic
scales, finite values, stubbed RNG/vector helpers and x87 square root; they
do not qualify NaNs, infinities, FPCSR parity, real RNG distribution or hardware.
Complete guest instruction equality is established separately.

Fresh matcher: total 3275 / 5463 exact (59.95%), Game 2602 / 4790 (54.32%),
Init 492 / 492, Debugger 181 / 181; zero drift, 2188 still different.
Conversion counts are unchanged because the placeholder was already counted
as C. README receives aggregate changes only, with detailed progress here.

`func_150E6FAC` still has fifteen differing positions; its return-tail trials
remain rejected. Init inventory and decoder fitting/ownership gates are
unchanged. Unrelated actor/timeline changes are excluded. No sibling adoption,
host build, Release change or push.
