# Game matrix-phase update match

Date: 2026-11-13. `func_150F1A00` replaces the zero-return placeholder in
`conker/src/game/generated_11C2B0.c`. Its 82-word retail body occupies
`0x150F1A00..0x150F1B48`, ROM `0x11EEB0..0x11EFF8`.

The function copies three halfword rates and selects one according to the
actor's flags, advances a shared signed phase with wrapped tick arithmetic,
and uses `cosf` to scale the three columns of three matrix rows. The matrix
pointer is read after the cosine call. The existing dispatcher declaration is
corrected to return `void`; its ten functions remain unchanged.

The recovered C emits 82 words under the owner compiler profile. Fifty-eight
words match at the same position after relocations; 24 expected-word guards
normalize the frame, register allocation and loop schedule to the retail
stream. Both padders emit all 82 retail words. This is a guarded match.

Tools commits `599d966` and `ef398c2` provide and pin the qualification suite:

```sh
python3 -m unittest tools.tests.test_game_matrix_phase_150f1a00_screen -v
```

The independent guest model exercises 480 cases per stream with synthetic
floating constants and a stubbed cosine; the stub may change the actor's
matrix pointer, testing the read order. Native32 O0/O2/O3 tests cover 480
cases in each strict and non-strict aliasing configuration with trapping UBSan.
Four deliberately incorrect variants are rejected in both guest and native
screens. The original caller window is exercised in 144 cases per stream,
including its delay-slot argument; a ROM scan identifies the direct call at
`0x15034700`. The checks also cover 144 fired guest fault prefixes, eight GNU
links over four address layouts, both padders and 96 stale-guard rejections.
The native and guest tests are bounded; the cosine stub is not validation of
the real helper or physical gameplay.

Both mounted and independent sibling suites passed before and after
installation; `make tools-check` passed and the sibling's prior dirty state
was preserved.

The production Make build and strict independent image prediction account for 332 changed bytes with zero exclusions and 3 checked symbol-ordering groups. Only this function changes among 6,051; every function address and all 189,088 protected Game-data bytes remain fixed. The 43 owner neighbors, ten caller functions, conversion CSV and earlier guard rows are unchanged. Of 698 fingerprinted linked objects, changed objects were `generated_11C2B0.c.o`. The scoped Graphify refresh retained all 60,078 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,780 / 4,843 (78.05%)**, total **4,453 / 5,516 (80.73%)**, zero drift. **95** more Game matches are needed for 80% at the current denominator.
