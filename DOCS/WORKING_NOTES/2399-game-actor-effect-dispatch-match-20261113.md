# Game actor-linked effect dispatch match

Date: 2026-11-13. `func_150B3AB0` replaces the zero-return placeholder in
`conker/src/game/generated_E0F60.c`. The retail body is 87 words at
`0x150B3AB0..0x150B3C0C`, ROM `0xE0F60..0xE10BC`.

For a non-null actor with an attached object, the routine selects a player
record, calls `func_1512D748`, transforms a fixed point through the attachment,
submits a randomized effect, constructs an eight-byte record and dispatches
that record and position. The routine leaves two record padding bytes and two
position padding bytes untouched. The second parameter remains a volatile
byte to preserve retail's repeated reads of its incoming argument home; the
bounded guest tests include mutation of that home by a helper. Such deliberate
stack mutation is guest-machine evidence, not a portable C calling convention.

All 87 words emit directly from C using the existing owner profile, with no
word guards. The original direct caller `func_1506FC9C` passes the current
actor and slot 255; a matching typed declaration and cast were added to its
owner. All 328 caller functions and all padded caller object sections remain
unchanged. An aligned Game instruction census found that one direct call; an
aligned whole-input literal-address scan found no direct pointer word. Neither
search rules out computed or externally supplied calls.

Tools commits `a7ce970` and `9e72fbd` supply the qualification suite and align
the recovered helper declarations with their existing types:

```sh
python3 -m unittest tools.tests.test_game_actor_effect_dispatch_150b3ab0_match -v
```

The independent guest model covers 72 cases per instruction stream, including
null paths, helper mutation of the actor and incoming slot, full helper-call
arguments, and observed packet and position padding. The original caller
window covers 24 cases per stream; it does not qualify the complete caller.
Seventy-one fired guest access prefixes compare equal. Native32 tests cover 36
defined-domain cases at O0/O2/O3 under both aliasing modes with trapping UBSan;
four deliberate semantic errors are rejected. Both padders and the original
assembly agree through 12 GNU links across four rebased layouts. These are
bounded checks; helper implementations and physical gameplay are not proven by
the modeled calls. The actual-Make caller diagnostics remain 36 before and
after; the known duplicate Makefile recipe warning is also still present.

Both mounted and independent sibling suites passed before and after installation; `make tools-check` passed and the sibling's pre-existing dirty state was preserved.

The production Make build and independent full-image prediction account for 345 changed bytes with zero exclusions and 1 checked symbol-ordering groups. Only this function changes among 6,051; every function address and all 189,088 protected Game-data bytes remain fixed. The one owner neighbor, 328 caller functions, conversion CSV and entire guard table are unchanged. Of 698 fingerprinted linked objects, changed objects were `generated_E0F60.c.o`. The scoped Graphify refresh retained all 60,084 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,783 / 4,843 (78.11%)**, total **4,456 / 5,516 (80.78%)**, zero drift. **92** more Game matches are needed for 80% at the current denominator.

Next candidate: screen `func_150F97EC` in `generated_124920.c`. Its original
89-word body begins at `0x150F97EC` and checks the actor attachment before
building randomized effect parameters. Its complete behavior, caller ABI,
helper interactions and match have not yet been qualified.
