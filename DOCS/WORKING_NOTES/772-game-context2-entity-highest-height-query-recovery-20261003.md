# Game Context-2 Entity Highest-Height Query

Date: 2026-10-03. Baseline: `d6235c1`.

## Result

`func_15045AE4` in `conker/src/game/generated_71820.c` replaces its
zero-return placeholder with the complete semantic highest-height query for
the `D_800D37E0` scratch context. Its 153-word / 612-byte retail slot contains
150 compiler body words and three padding nops, with 88 differing word
positions. No new word guards or compiler-profile changes were added.
The original reference in `conker/asm/71820.s` remains unchanged.

- VMA: `0x15045AE4..0x15045D48`.
- ROM: `0x72F94..0x731F8`.
- Linked slot SHA-256: `f1b2c53b86520946f861fe841b6eae1ee54a21acae7cfea7859b4299ca6dfe7f`.

This is semantic recovery of an already-classified C row, not a new converted
row or byte-exact match. Aggregate progress and README tables are unchanged.

## Contract

Initialize height from `D_80098D54`: retail ROM offset `0x23D814` contains
bits `0xC61C4000`, or `-10000.0f`. Prepare `input[0]` with
`func_150A44F0(..., D_800D37E0, 0)`, then reload input and position X/Z for
the `func_150A43E0` collector. X/Z truncate to signed integers. There is no
early threshold-rejection gate.

Select the strict highest signed fixed-height candidate satisfying
`height <= positionY`, using `1/256` conversion. Strict improvement over
current result height preserves the first tie and excludes sentinel-equal
entries. Helper-mutated position Y and result height remain observable.

Cache the selected triangle and vertex byte offset before copying nine signed
halfwords. Reload the candidate's fourth word as the entity index after those
copies. Publish entity address to result `value` before loading its metadata
table. Table metadata uses signed triangle-relative indexing minus the unsigned
`firstTriangle`, preserving 32-bit subtraction; otherwise use default metadata.

After metadata publication, OR flags with `6`, reload both the candidate entity
index and global entity-table base, then read entity flag bit `0x80`. If set,
OR result bit `1`. Publish state `2`. Finally return one only when
`threshold <= result->height`, ORing result bit `2` on that path.

A selected result still publishes vertices, metadata, flags, entity address,
and state when the final bound fails. No candidate clears only flag bit `2`,
retaining the initialized/helper-mutated height and other fields. NaN Y produces
no eligible candidate; NaN threshold produces a selected-but-failed result.

The late entity reloads and state `2` distinguish this function from the earlier
highest-height query `func_15045F8C`, which uses scratch `D_800D3830`, state
`3`, and a cached entity pointer for its flag read. They are not interchangeable.

## Verification

Fifteen new tests in `tools/tests/test_game_context2_highest_height_query.py`
compile the actual production body and guest layouts in the existing 32-bit
freestanding fixture. Only the preparation and collector boundaries are mocked.

Coverage includes the exact retail sentinel, highest selection/first ties,
inclusive bounds, selected failure, nonpositive counts, strict sentinel,
all result/entity flag combinations, default and table metadata, unsigned
base indices, negative vertex byte offsets, signed fractional heights, NaNs,
padding preservation, and helper input/position/height mutations.

Alias-sensitive probes check that copies cache triangle/offset but reload entity
index, entity address publication precedes metadata-table load, flag publication
can change the entity index used for the final entity-flag read, and result value
publication can change the global entity-table base used for that read. These
are controlled host fixtures, not guest gameplay acceptance.

All 271 tool tests pass without skips. The optional retail-ROM sentinel assertion
ran successfully. Full `make -C conker NON_MATCHING=1 all match-progress -j4`
and `make tools-check` pass. Independent linked comparison measures all 88
differences across the full slot; next address remains `0x15045D48`.

The adjacent lowest query is unchanged at 88 differences and hash
`eead237486c5d2ceaba87929d5be6fe8065354414e20547d2d8249256e89b9f0`.
The earlier highest entity query remains at 72 differences and hash
`b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.
Both cached queries, their recovered dispatch wrappers, typed three-argument
caller, both count helpers, and both context-3 queries remain exact. The
520-byte producer/return closure and 5,712-byte collector group remain exact.
Both entire Init sections retain the retail hashes from Note 768.
No guest execution, compressed-ROM build, or natural gameplay test occurred.

## Next

Recover retained `func_15045D48`. Its live assembly uses `D_80098D58`,
scratch `D_800D3830`, lowest-height selection, state `3`, and a cached entity
pointer for the flag read. Audit the complete slot and its sentinel before
reusing existing source or tests. Keep entity-query byte matching separate
from semantic recovery and natural gameplay qualification.

Progress remains 5,459 / 6,042 C rows, 3,262 / 5,459 exact overall; Game
4,786 / 5,321 C rows, 2,589 / 4,786 exact, zero drift and 2,197 different.
Remaining Init conversion gates are unchanged in
[Note 768](768-init-remaining-assembly-current-decision-20261003.md).
The sibling host port and frozen Release artifacts remain untouched.
