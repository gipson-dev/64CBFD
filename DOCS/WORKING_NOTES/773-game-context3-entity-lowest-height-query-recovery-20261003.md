# Game Context-3 Entity Lowest-Height Query

Date: 2026-10-03. Baseline: `f247cfe`.

## Result

`func_15045D48` in `conker/src/game/generated_71820.c` now has its complete
semantic body instead of retained assembly ownership. The original assembly
reference remains unchanged. The routine is not byte-exact: its 145-word /
580-byte retail slot contains 144 compiler body words plus one padding nop,
with 72 differing word positions. No new guards or compiler profiles were added.

- VMA: `0x15045D48..0x15045F8C`.
- ROM: `0x731F8..0x7343C`.
- Linked slot SHA-256: `c592f5e6c81b7ab9a67ebf554c7e46b8b8471f20eff6fc9006a3fcf24471332a`.

This adds one C row / 580 classified C bytes, not a new exact match. Compiler
spill/register assignment, copy scheduling, and branch layout still differ;
do not substitute a broad guard set for the remaining matching work.

## Contract

Initialize height from `D_80098D58`. Retail ROM offset `0x23D818` contains
bits `0x47C34FF3`, or `99999.8984375f`. Prepare `input[0]` with
`func_150A44F0(..., D_800D3830, 0)`, then reload input and position X/Z
for `func_150A43E0`. X/Z truncate to signed integers at this boundary.
No early threshold gate is present.

Select the strict lowest signed fixed-height candidate satisfying
`positionY <= height`, scaling by `1/256`. Current result height is the strict
upper bound; preserve first ties and exclude sentinel-equal candidates.
Helper-mutated Y and height remain observable.

Cache triangle and vertex byte offset before copying nine signed halfwords.
Reload the candidate entity index after the copies, then calculate and cache
its entity pointer. Publish that address to result `value` before loading
the entity metadata table. Table metadata uses signed triangle-relative
indexing minus unsigned `firstTriangle`, preserving 32-bit subtraction;
otherwise publish default metadata.

OR flags with `6`. Read entity flag bit `0x80` through the cached entity
pointer, not a newly calculated pointer from the candidate/global base. If
set, OR result bit `1`; publish state `3`. Return one only when
`result->height <= threshold`, ORing result bit `2` on that path.

Selected candidates publish the complete result even if the final bound
fails. No candidate clears only bit `2`, preserving other fields and the
initialized/helper-mutated height. NaN Y prevents eligibility; NaN threshold
produces a selected-but-failed result. The scratch buffer, state, and cached
entity flag pointer distinguish this function from `func_15045880`.

## Verification

Fifteen tests in `tools/tests/test_game_context3_entity_lowest_height_query.py`
compile the actual production body and guest layouts in the established
32-bit freestanding harness. Only preparation and collection are mocked.

Coverage includes the retail sentinel, lowest selection/first ties, inclusive
bounds, strict sentinel/no candidates, nonpositive counts, selected failure,
all result/entity flag combinations, default/table metadata and unsigned base
indices, signed fractional heights, negative byte offsets, NaNs, padding,
helper input/position/height reloads, cached triangle versus reloaded entity
index after copies, and entity publication before metadata-table load.

Two controlled alias probes specifically require the cached pointer for the
later entity flag read:

- Result flag publication changes the selected candidate's entity-index word.
  The flags must still come from the earlier entity pointer.
- Result value publication changes the global entity-table-base variable.
  Metadata and subsequent entity flags still use the cached entity.

These cases distinguish this routine from the late-reload behavior tested in
Notes 771/772; they are host source-contract tests, not guest gameplay proof.

All 286 tool tests pass without skips. The optional retail-ROM sentinel
assertion ran successfully. Full
`make -C conker NON_MATCHING=1 all match-progress -j4` and `make tools-check`
pass. Independent comparison checks the complete slot and all 72 differences;
the following symbol stays at `0x15045F8C`.

Both cached queries and recovered dispatch wrappers, the typed three-argument
caller, count forwarding helpers, context-3 non-entity queries, 520-byte
producer/return closure, and 5,712-byte collector group remain exact. Both
entire Init sections retain the retail hashes from Note 768.

Other entity-query slots are unchanged:

- `func_15045880`: 88 differences, hash
  `eead237486c5d2ceaba87929d5be6fe8065354414e20547d2d8249256e89b9f0`.
- `func_15045AE4`: 88 differences, hash
  `f1b2c53b86520946f861fe841b6eae1ee54a21acae7cfea7859b4299ca6dfe7f`.
- `func_15045F8C`: 72 differences, hash
  `b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.

No guest execution, compressed-ROM build, or natural gameplay acceptance
is claimed. The sibling host port and frozen Release artifacts are untouched.

## Progress / Next

Fresh inventory: 5,460 / 6,042 C rows (90.37%), 1,929,964 / 2,256,728 C
bytes (85.52%). Game: 4,787 / 5,321 (89.96%), 1,758,528 / 2,072,880
bytes (84.84%). Remaining assembly: 582 overall, 534 Game.

Exact C numerators remain 3,262 total and 2,589 Game, now 59.74% and 54.08%
of 5,460 and 4,787 respectively. Zero drift and 2,198 differing Game rows.
Init/Debugger classification and matching are unchanged. The formerly exact
assembly slot is now non-matching C; no new exact-match progress is claimed.

Next audit retained `func_150461D0`. Its live assembly copies the full
36-byte result into two local snapshots, prepares separate primary/secondary
counts, calls both lowest-height entity queries, and combines the results.
Preserve the actual count addresses, low-byte return handling, snapshot/copy
order, tie decisions, and fallback paths after inspecting its complete body.
Continue query byte matching and natural qualification separately; remaining
Init gates stay in [Note 768](768-init-remaining-assembly-current-decision-20261003.md).
