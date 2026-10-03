# Game Lowest-Height Query Recovery

Date: 2026-10-03. Baseline: `e6dedaf`.

## Recovery

`func_15045384` replaces its zero-return placeholder with the lowest eligible
height query and result publication body. Its complete slot is 114 words /
456 bytes at VMA `0x15045384..0x1504554C`, ROM `0x72834..0x729FC`.

The production body retains the slice's `-O2 -g3` profile. Fifteen strict
expected-word guards normalize three closed compiler-layout differences.
No arithmetic, floating-point comparison, call, branch, frame size, or
function length is replaced or changed by these guards.

## Retail Contract

The inputs are a three-float position, float upper threshold, and the existing
36-byte `HeightResult71820` layout. If threshold is below position Y, clear
only flag bit 2 and return zero, without initializing height or calling helpers.

Otherwise initialize result height from `D_80098D48`, reset context with
`func_1510F800(3)`, reload position X/Z, truncate them to signed 32-bit integers,
and call the restored handwritten `func_150A4FA0` collector. This routine
does not publish `D_800DBE68/6C/70/74`, unlike the preceding highest-height query.

The retail sentinel is bits `0x47C34FF3` at ROM `0x23D808`:
99999.8984375 as a single-precision float. It is not 10000 or positive infinity.

For each of the returned 16-byte candidate records, convert signed fixed
height to float and multiply by 1/256. Select a height at or above the reloaded
position Y and strictly below the current result height. The first equal-height
candidate wins. Nonpositive counts and no eligible candidate clear only bit 2
after sentinel initialization.

For a selected candidate, cache its three-pointer vertex-array base and byte
offset before copying three signed XYZ halfword triplets. The context-3 offset
is a byte displacement: it is not the context-0 vertex index multiplied by 16.
The C local makes that distinction explicit without changing the shared layout.

Publish zero metadata, flags OR 6, state 4, and zero value. Return one only if
result height is at or below threshold. A selected candidate above threshold
still publishes all fields and sets flags OR 6 before returning zero.
Unordered NaN comparisons follow the original ordered predicates.

## Normalization Proof

The unguarded C body already has the original 114-word length, 0x28-byte frame,
calls, branches, float sequence, and memory-access behavior. Ninety-nine words
emit unchanged; fifteen differing positions form these complete sets:

| Set | Offsets | Proof |
| --- | --- | --- |
| Selected-index spill | `0x060, 0x084` | Move its defining store and reload together from private slot 0x24 to 0x20 |
| Count/index registers | `0x08C, 0x094, 0x0CC, 0x0E0, 0x0E4, 0x0EC, 0x0F0` | Simultaneous a0/v1 rename over their complete scan lifetime |
| Vertex-copy pointer schedule | `0x13C, 0x140, 0x144, 0x148, 0x14C, 0x154` | Same signed-halfword load/store order and addresses; equivalent pointer update timing |

The destination spill slot is above the outgoing argument area, does not
overlap saved s0 at 0x18 or ra at 0x1C, and its address is never passed to a
callee. The count/index lifetimes end before those registers are reused for
vertex copying. Every use in the scan is renamed together.

The compiler increments the destination pointer by six before the first store
and uses offsets -2/0/2; retail uses offsets 4/6/8 and increments in the loop
branch delay slot. Both sequences load X, store X, load Y, store Y, load Z,
store Z, then enter the next iteration with the same pointer. This preserves
the sequence even when source and destination overlap. The branch itself is
unchanged and its delay instruction executes on both outcomes.

Every guard requires its exact original compiler word and empty relocation
set. No inserts, omissions, or mismatch allowances are added.

## Tests

`tools/tests/test_game_lowest_height_query.py` reuses the existing 32-bit
freestanding query harness and shared layouts, extracting the actual new C
definition. Thirteen new tests cover:

- Guest layout and byte-offset vertex access, including a non-record offset.
- All 256 input flag bytes on early rejection, selected failure, and
  nonpositive counts; untouched output bytes and no early calls.
- Lowest eligible selection, first ties, inclusive Y/threshold boundaries,
  strict sentinel bound, signed fractional fixed heights, and truncated X/Z.
- Context-reset/collector ordering, callback mutation reloads, no publication
  of the preceding query's globals, and NaN predicates.
- Metadata/state/value publication and preservation of padding/candidate data.
- Exact closed guard sets and the full register rename.
- Copy-schedule load/store equivalence across thirteen aligned relative
  source/destination placements, including overlapping storage.

All 183 repository tool tests pass, and the thirteen focused tests pass again
after tightening guard-set verification. Project checks pass.

## Linked Validation

The full code build and progress regeneration pass. Independent linked-span
comparison confirms all 456 bytes equal retail; SHA-256:
`7dcb65202f58c76161f7424db82629112cf9fb3ce5c557256f172c4445587d87`.

Constructor, allocator, list pass, overlap, callback wrapper, and neighboring
`func_15045714` remain byte-exact. The next function remains at `0x1504554C`.
The preceding highest-height query remains unchanged at 76 differing words,
with its prior SHA-256 `64640310ebe9fdbfb77fbdd8c9a4794d7a53897feb86f643d838cc449b78ca34`.
All 5,712 collector/context bytes and both complete Init sections remain exact,
with the unchanged hashes recorded in Notes 760 and 761.

The matcher now reports Total 3,256 / 5,455 exact C rows (59.69%), Game
2,583 / 4,782 (54.02%), Init 492 / 492, and Debugger 181 / 181.
There is zero drift and 2,199 differing Game rows. C representation totals
do not change because the old placeholder already counted as C.
README updates only the two affected aggregate matching rows and snapshot date.

No host-port build or gameplay execution is part of this recovery. The
collector was restored to original assembly in Note 760; natural gameplay
qualification remains separate.

## Next

The next untouched query in this slice is `func_1504554C`. Init's two small
leaves remain deferred under Note 762; do not repeat those completed matrices.
