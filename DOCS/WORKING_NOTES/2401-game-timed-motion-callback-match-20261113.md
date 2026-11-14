# Game timed-motion callback match

Date: 2026-11-13. `func_150F48D0` replaces the zero-return placeholder in
`conker/src/game/generated_121A20.c`. The 90-word retail body occupies
`0x150F48D0..0x150F4A38`, ROM `0x121D80..0x121EE8`.

The callback subtracts the live frame delta from an embedded timer and returns
zero if the result is at most zero. Otherwise it asks `func_1514373C` for a
two-component direction, advances the embedded phase and position, derives
three actor coordinates, and updates three more actor components. Its active
return is the embedded state address represented as an `s32`. Retail's
`D_800898B0` table uses slot 22 for this callback; the observed
`func_151321D0` call window passes the actor and tests the return for zero.
An aligned Game scan found no direct JAL to the target, and an aligned input
scan found this one literal table word. Computed and external callers remain
outside those scans.

IDO emits the complete 90-word semantic C body with 68 words at their retail
positions. Twenty-two expected-word guards restore the complete retail stream:
16 preserve a closed register-role reassignment around the helper call and
six restore the ordering of independent actor loads, floating operations and
the adjacent store. Relocation records for the time global remain attached to
the same symbols. The two actor fields whose accesses move are distinct fixed
offsets; the guarded instruction stream restores retail fault ordering as well.
Five other compiled and padded owner functions remain unchanged.

Tools commit `df4dbb0` provides the qualification suite:

```sh
python3 -m unittest tools.tests.test_game_timed_motion_150f48d0_match -v
```

The bounded guest model checks 96 finite cases for each retail, raw-C and
guarded stream, including a helper that mutates the time global and three
actor/global alias arrangements. Three altered-instruction controls are
rejected. A 123-case actor/private-stack overlap screen found no differences
among the three streams; two cases per stream produced the same modeled
exceptions and are not successful execution cases. An original indirect-call
window and the original 22-word coordinate helper each have 24 cases per
stream; the helper's `sinf`/`cosf` results are modeled. The guarded stream
also agrees with retail across 159 fired guest access prefixes. Native32 tests
cover 24 finite disjoint cases at O0/O2/O3 in both aliasing modes with trapping
UBSan and reject three semantic negative controls. Both padders agree over
12 GNU links across four rebased address layouts. These tests do not establish
unrestricted ISO C alias behavior, hardware floating exceptions, complete
caller execution, real trigonometric implementations or gameplay.

Both mounted and independent sibling suites passed before and after installation; `make tools-check` passed and the sibling's prior dirty state was preserved.

The production Make build and independent full-image prediction account for 283 changed bytes with zero exclusions and 0 checked symbol-ordering groups. Only this function changes among 6,051; every function address and all 189,088 protected Game-data bytes remain fixed. The five owner neighbors, conversion CSV and previous guard rows are unchanged. Of 698 fingerprinted linked objects, changed objects were `generated_121A20.c.o`. The scoped Graphify refresh retained all 60,089 prior node IDs and was not a full-corpus extraction.

Fresh production recount: Game **3,784 / 4,843 (78.13%)**, total **4,457 / 5,516 (80.80%)**, zero drift. **91** more Game matches are needed for 80% at the current denominator.

The private `func_150F97EC` attachment-effect screen in Note 2400 remains a
candidate for further matching; its omitted floating multiply and original
stack layout still need resolution before it can be installed.
