# Game linked-effect constructor match

Date: 2026-11-13. `func_151CEAAC` replaces the zero-return placeholder in
`conker/src/game/generated_1FA770.c`. Its 89-word retail body occupies
`0x151CEAAC..0x151CEC10`, ROM `0x1FBF5C..0x1FC0C0`.

The constructor snapshots an owner, identity and attachment into a payload,
uses two random values to set effect parameters, obtains a position through
`func_151CEC10`, and copies the 40-byte payload into an allocated effect. It
returns the effect pointer or null. The allocation request is 28 bytes; its
two padding bytes and four trailing bytes are left untouched, as in retail.
The payload also retains its untouched padding. If both source pointers are
null, the original position helper faults when it reads the null owner; the
recovered code does not introduce a different null fallback.

All 89 words emit directly from C under the retail compiler profile, with no
word guards. Both production padders preserve the retail stream. The existing
direct C caller's implicit declaration was corrected; its 16 functions remain
unchanged.

Tools commits `3db1ac6` and `f0884bc` provide the qualification suite:

```sh
python3 -m unittest tools.tests.test_game_linked_effect_constructor_151ceaac_match -v
```

An independent guest model covers 96 cases per stream, including the real
position helper, helper mutations, both null-source behavior and untouched
request and payload bytes. Native32 O0/O2/O3 checks cover 96 cases in each
strict and non-strict aliasing configuration with trapping UBSan, and reject
four incorrect variants. The two original direct-caller windows cover 32
cases per stream, including their stack argument and returned-pointer store;
the enclosing functions are not qualified in full. Other checks cover 128
fired guest fault prefixes, both padders and eight GNU links over four address
layouts. These are bounded tests and do not establish physical gameplay.

Both mounted and independent sibling suites passed before and after
installation; `make tools-check` passed and the sibling's prior dirty state
was preserved.

The production Make build and independent full-image prediction account for 348 changed bytes with zero exclusions and 1 checked symbol-ordering groups. Only this function changes among 6,051; every function address and all 189,088 protected Game-data bytes remain fixed. The 51 owner neighbors, 16 caller functions, conversion CSV and entire guard table are unchanged. Of 698 fingerprinted linked objects, changed objects were `generated_1FA770.c.o`. The scoped Graphify refresh retained all 60,082 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,782 / 4,843 (78.09%)**, total **4,455 / 5,516 (80.77%)**, zero drift. **93** more Game matches are needed for 80% at the current denominator.
