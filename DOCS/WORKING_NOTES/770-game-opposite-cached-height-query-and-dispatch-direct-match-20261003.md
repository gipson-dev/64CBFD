# Game Opposite-Bound Cached Height Query And Dispatch

Date: 2026-10-03. Baseline: `ea29585`.

## Recovery

Two retained assembly routines now emit directly from semantic C in
`conker/src/game/generated_71820.c`. No new word guards or compiler-profile
changes are needed, and the original assembly references remain unchanged.

| Routine | Words / bytes | VMA | ROM | SHA-256 |
| --- | ---: | --- | --- | --- |
| `func_150470B0` | 43 / 172 | `0x150470B0..0x1504715C` | `0x74560..0x7460C` | `83cb59cf4e81f8c22f6691e58fdf1d38b8d780b4822383c78a2a41c51317c4fd` |
| `func_15046C00` | 32 / 128 | `0x15046C00..0x15046C80` | `0x740B0..0x74130` | `0c140ca072757cbcabaf50fce3e44c0841003e40575d8c4627311ae2d23e66bf` |

Unlike Note 769, both routines previously had assembly ownership. This is
two new converted rows and two new exact C rows, totaling 300 bytes.

## Behavior / ABI

The cached query uses the same initial result flag bit `4` gate and existing
handwritten `func_150A3FC4` geometry helper as `func_15047004`, but accepts
the opposite ordered range: `height <= threshold && position[1] <= height`.
It passes float X/Z, a null triangle pointer, the packed result vertices,
and a local height output to the helper.

- Return `0` for a disabled cache or a zero geometry result, with no local
  result publication.
- Return `1` for a nonzero geometry result outside the inclusive range,
  including a failed ordered comparison involving a NaN. Preserve an existing
  result bit `2`; rejection does not clear it.
- Return `2` when accepted, publishing the height and ORing bit `2` into
  the current flags without changing other fields.

After the helper, reload position Y and flags. Do not repeat the initial
cache gate if the helper changes flag bit `4`. The threshold is by value;
the published height preserves its float bits, including negative zero.

The four-argument dispatch maps cached status `1` to zero and `2` to one.
Only status zero calls retained `func_150466F8`, preserving its halfword
selector, float threshold, position/result pointers, and raw signed return.
The complete cached callee establishes the three-case switch's return domain.

The existing three-argument caller `func_1504530C` now has consistent float/
pointer types and an explicit typed declaration for retained `func_15044ED0`.
Its body remains unchanged and its full 30-word / 120-byte slot is exact:
SHA-256 `328e786deff2085910be798eef006116221c3ccb28fe5d7418974696df4439f5`.
Typed declarations avoid implicit float-to-double promotions at assembly
call boundaries. Neither fallback's assembly implementation was changed.

## Tests / Regression

Eleven new tests in `tools/tests/test_game_opposite_cached_height_dispatch.py`
extend the established actual-source cached-height fixture. They compile
`func_150470B0`, `func_15046C00`, and `func_1504530C` together, mocking the
geometry and fallback boundaries rather than reimplementing either dispatch.

Coverage: every initial flag value across cache enabled/disabled cases;
untouched result bytes; zero versus arbitrary nonzero geometry results;
ordered range rejection and NaNs; inclusive endpoints, signed zero, and
infinities; helper-mutated Y/flags; position/result aliasing and by-value
bounds; both caller shapes' cache statuses and raw fallback returns; all
65,536 selectors; and geometry mutations passed into fallback.

All 241 repository tool tests pass without skips. Full
`make -C conker NON_MATCHING=1 all match-progress -j4` and `make tools-check`
pass. Independent linked slot extraction matches both new routines and the
typed existing caller against retail. Following symbols remain at
`0x1504715C` and `0x15046C80`.

Prior cached query/dispatch, both sibling dispatch wrappers, `func_15045780`,
both count forwarding helpers, both context-3 height queries, the 520-byte
producer/return closure, and the 5,712-byte collector group remain exact.
Both entire Init sections retain their retail hashes from Note 768. The
highest-height entity query remains unchanged at 72 differences and hash
`b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.
No guest execution or natural gameplay qualification is claimed.

## Progress / Next

Classified CSV: 5,458 / 6,042 C rows (90.33%), 1,928,772 / 2,256,728 bytes
(85.47%). Game is 4,785 / 5,321 (89.93%), 1,757,336 / 2,072,880 bytes
(84.78%). Remaining assembly: 584 overall and 536 Game. Init/Debugger
classification is unchanged.

Linked matcher: total 3,262 / 5,458 exact (59.77%), Game 2,589 / 4,785
(54.11%), zero drift and 2,196 different Game rows. Init stays 492 / 492
exact, Debugger 181 / 181 exact.

Next recover retained `func_15045880`, the entity-indexed lowest-height
query. Its live assembly uses scratch `D_800D37E0`, a strict lowest-height
selection above position Y, entity metadata, and result state `2`; do not
blindly copy the highest-height query's scratch/state or comparison direction.
Keep the remaining Init gates in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
The sibling host port and frozen Release artifacts remain untouched.

Follow-up: [Note 771](771-game-entity-lowest-height-query-semantic-recovery-20261003.md)
recovers the then-pending lowest-height query in semantic C. It remains
non-matching; the original assembly reference is preserved for matching work.
