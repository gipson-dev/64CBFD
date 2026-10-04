# Game Fixed Random Parameter Initializer Match

Date: 2026-10-04. Starting HEAD: `8f0cec0a`.

## Recovery

Replace `func_150E71E4`'s zero-return placeholder in `generated_113D60.c`
with a void four-argument initializer. First two word arguments are unused;
the third points to the input vector, fourth to eight output floats.
Retain the four-argument ABI and original incoming argument spills.

Eight output stores occur in this order:

| Output index | Value |
| --- | --- |
| 0 | `func_150484A0(vector[0], vector[2])` |
| 2 | `D_800A1324` |
| 4 | First RNG sample times `D_800A1328` |
| 6 | Second RNG sample times `D_800A132C` |
| 1 | `D_800A1330` |
| 3 | `D_800A1334` |
| 5 | Third RNG sample times `D_800A1338` |
| 7 | Fourth RNG sample times `D_800A133C` |

Exactly one vector-helper call and four independent RNG calls. Input vector
is not reread after the initial helper call. Global constants remain individual
loads at their original times; callbacks may change later fields/scales.
Do not snapshot constants, combine RNG samples, clamp, add null handling or
invent a return value. Store publication before later calls is preserved.

Retail constant words from `245C90.rodata.s`, in declaration order, are
`3EF1463B`, `40C90FDB`, `3E4CCCCD`, `BF10C3BD`, `3EA0D97C`, `40C90FDB`,
`3E19999A`. Global data and its original rounding are unchanged.

## Exact Slot

The first recovered source form emits all 43 words / 172 bytes directly.
Fresh ELF matches ROM slice `0x114694..0x114740` at original function slot
`0x150E71E4..0x150E7290`. Frame is 0x20; saved S0/RA, argument spills, global
loads, float registers, call-delay stores and epilogue match. No target guards,
profile changes or custom instruction emission. Next function address intact.

Slot SHA-256:
`77fbde0000119d5b3d6890dedfbd31eceab9c3dda43a2c311b3cc2640dd8d384`.

## Verification

New `tools/tests/test_game_fixed_random_parameters.py` has five tests:

- Fixed/scaled outputs, four distinct samples including synthetic out-of-range
  values, unused argument words and publication observed by each callback.
- Zero samples retain all three fixed fields and all four calls.
- Callbacks mutate the vector and later global scales/fixed fields; output
  uses captured helper arguments but observes later global reads.
- Overlapping input/output retains original vector arguments and no rereads.
- Warning-clean independent IDO body equals all 172 retail bytes without
  project padding/guards, with only zero trailing section alignment.

The test reuses the preceding initializer's freestanding 32-bit host compile
helper. Import the module, not its TestCase into the module namespace, to avoid
unittest collecting that other class a second time. The final combined run
contains fourteen distinct tests, not the earlier accidental duplicate set.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_fixed_random_parameters tools.tests.test_game_vector_random_parameters tools.tests.test_game_random_range_position -v -f
```

Fourteen tests pass in 1.978 seconds, no skips. Host fixtures use finite,
exactly representable synthetic constants and stubbed helpers; they do not
qualify hardware, real RNG distribution, NaNs, FPCSR behavior or gameplay.
Complete linked guest equality is established separately.

Fresh matcher total 3276 / 5463 (59.97%), Game 2603 / 4790 (54.34%), Init
492 / 492 and Debugger 181 / 181 exact, zero drift, 2187 still different.
Conversion counts do not change because the placeholder was already C.
README receives aggregate rows only. Detailed behavior stays in working notes.

Init gates and `func_150E6FAC`'s fifteen tail differences remain unchanged.
Unrelated actor/timeline changes are preserved and excluded. No sibling
adoption, host build, Release change or push.
