# Game configured effect factory match

Date: 2026-11-13. `func_1519C09C` replaces the zero-return placeholder in
`conker/src/game/generated_1C2C60.c`. The 89-word retail body occupies
`0x1519C09C..0x1519C200`, ROM `0x1C954C..0x1C96B0`.

The function builds an effect header, converts three floating coordinates to
signed integers, and submits them with byte arguments to the existing effect
factory. On success it copies a 32-byte fixed configuration and the owner
pointer into the returned effect; on failure it returns null. The sixth byte
of the header is not initialized by the retail body and remains an incoming
stack byte when the helper reads it.

The recovered C emits 89 words under the retail owner profile. Seventy-nine
words match at the same position after relocation; ten expected-word guards
normalize register allocation during initialization. Both
padders produce the full 89-word retail stream. This is a guarded match.

Tools commit `ff95e42` provides the qualification suite:

```sh
python3 -m unittest tools.tests.test_game_effect_config_1519c09c_match -v
```

The independent guest model checks 96 cases per stream, covering allocation
success and failure, output/input overlap, helper mutations and the preserved
header padding byte. Native32 O0/O2/O3 tests cover 96 cases in each strict
and non-strict aliasing configuration with trapping UBSan; four incorrect
variants are rejected. The original caller window has 96 cases per stream,
including its bypass branch, delay-slot argument and returned-pointer store;
an aligned Game-ROM scan identifies the direct call at `0x15199804`. Other
checks cover 137 fired guest fault prefixes, eight GNU links across four
address layouts, both padders and 40 rejected stale guards. The enclosing
caller is not qualified in its entirety. The tested coordinate conversions
are finite and representable; native behavior outside that domain and
physical gameplay are not established by these checks.

Both mounted and independent sibling suites passed before and after
installation; `make tools-check` passed and the sibling's prior dirty state
was preserved.

The production Make build and independent full-image prediction account for 326 changed bytes with zero exclusions and 2 checked symbol-ordering groups. Only this function changes among 6,051; every function address and all 189,088 protected Game-data bytes remain fixed. The 68 owner neighbors, conversion CSV and earlier guard rows are unchanged. Of 698 fingerprinted linked objects, changed objects were `generated_1C2C60.c.o`. The scoped Graphify refresh retained all 60,080 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,781 / 4,843 (78.07%)**, total **4,454 / 5,516 (80.75%)**, zero drift. **94** more Game matches are needed for 80% at the current denominator.
