# Game Cached Height Query And Dispatch: Direct C Matches

Date: 2026-10-03. Baseline: `9f93bda`.

## Recovery

Two connected routines in `conker/src/game/generated_71820.c` now match
directly from semantic C, without new word guards or compiler-profile changes:

| Routine | Words / bytes | VMA | ROM | SHA-256 |
| --- | ---: | --- | --- | --- |
| `func_15045800` | 32 / 128 | `0x15045800..0x15045880` | `0x72CB0..0x72D30` | `0ac8fb3398f10c9461b2a306010550d8856fc0f7fe7622d8f8e48807b0cc6554` |
| `func_15047004` | 43 / 172 | `0x15047004..0x150470B0` | `0x744B4..0x74560` | `4b8c4b77e2f71cef4a08195cf1b03ddd68f6cdc9b028eb1dedc423489e8da25f` |

The dispatch wrapper replaces retained assembly ownership. Its callee replaces
a false zero-return placeholder, rather than adding another converted row.
The original assembly references remain unchanged.

## Contracts

The cached query uses result flag bit `4` as its initial gate. When enabled,
call the existing handwritten `func_150A3FC4` with position X/Z, a null triangle
pointer, the result's packed nine-halfword vertices, and a local height output.
That assembly entry accepts the copied-vertex path through its nonnull fourth
argument; the restored collector group already supplies its body and shared
continuations. No geometry implementation was replaced by a mock in production.

The cached query has exactly three return statuses:

- `0`: cache disabled or the triangle query returned zero. Do not publish height
  or alter flags locally.
- `1`: triangle query returned nonzero but its height fails either ordered
  comparison, `threshold <= height` and `height <= position[1]`. NaNs fail
  the corresponding comparison. Do not clear an existing result bit `2`.
- `2`: both inclusive comparisons pass. Publish the computed height, OR bit
  `2` into the current flags, and preserve all other result fields.

Position Y and flags are reloaded after the geometry helper; the initial
cache gate is not repeated after helper mutations. The bound is passed by
value, and X/Z are passed as floats rather than truncated here. The geometry
assembly owns its own coordinate conversion.

`func_15045800` maps status `1` to return zero and status `2` to return one.
Only status zero invokes `func_15045780`, preserving its halfword selector,
float threshold, pointers, count buffer, and raw integer return. Its three-case
switch matches the established sibling dispatch shape. There is no invented
default status: the complete recovered callee proves the return domain 0..2.
An initial explicit status fallback produced 34 words and was discarded before
the successful full build; it is not normalized through word substitutions.

The declarations/definitions of the two sibling wrappers and their existing
fallback placeholders now use consistent float/pointer argument types. This
does not recover those placeholders (`func_1504697C`, `func_15046D00`). Both
sibling wrappers remain retail-exact at 128 bytes each:

- `func_15046C80`: `b5786bc19624a7b4064536d78eda93d2752e60b8bda9395662d593924fb6f823`.
- `func_15046F84`: `70ad2ec1ad364a1b82e41a9c63b2116dea4702ff54c0833feeb3c4e930559646`.

## Verification

Twelve tests in `tools/tests/test_game_cached_height_dispatch.py` compile the
actual three production definitions (`func_15047004`, `func_15045800`, and
`func_15045780`) together in the established 32-bit freestanding host harness.
Only geometry, count production, and the downstream entity query are mocked.

Coverage includes the result layout; every initial flag value across cache
enabled/disabled paths; all untouched result bytes; query failure; inclusive
bounds; NaNs, signed zero, and infinities; helper-mutated Y/flags and position
aliasing; both cached dispatch outcomes; raw fallback returns; all 65,536
halfword selectors; and helper mutations carried into fallback/early rejection.

All 230 repository tool tests pass without skips. Full
`make -C conker NON_MATCHING=1 all match-progress -j4` and `make tools-check`
pass. Independent linked extraction matches both new slots to the ROM, with
following symbols fixed at `0x15045880` and `0x150470B0`.

Both context-3 queries, both count forwarding helpers, `func_15045780`, the
520-byte producer/return closure, and the 5,712-byte collector/context group
remain exact. The entity query retains its 72 differences and hash
`b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.
Both complete Init sections remain exact with the hashes in Note 768.
No guest execution or natural gameplay qualification is claimed.

## Progress / Next

Fresh classified CSV: 5,456 / 6,042 C rows (90.30%), 1,928,472 / 2,256,728
C bytes (85.45%). Game is 4,783 / 5,321 (89.89%),
1,757,036 / 2,072,880 bytes (84.76%). Remaining assembly: 586 overall,
538 Game. Init and Debugger classification is unchanged.

Linked matcher: total 3,260 / 5,456 exact (59.75%); Game 2,587 / 4,783
(54.09%); zero drift and 2,196 different Game rows. Init remains 492 / 492
and Debugger 181 / 181 exact. One new converted row and two new exact rows
are justified, not two new conversions.

Next recover retained `func_150470B0`, the opposite-bound cached query using
the same geometry/result contract. The entity query's matching work and
natural wrapper/gameplay qualification are still open. Remaining Init
conversion gates are unchanged in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
The sibling host port and frozen Release artifacts remain untouched.
