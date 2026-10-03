# Game Entity Lowest-Height Query: Semantic Recovery

Date: 2026-10-03. Baseline: `258c386`.

## Result

`func_15045880` now has its complete semantic C body in
`conker/src/game/generated_71820.c`, replacing retained assembly ownership.
The original assembly reference is unchanged. This is a C conversion, not a
byte-exact match: the 153-word / 612-byte retail slot contains 150 compiler
body words and three padding nops, with 88 differing word positions.
No word guards or compiler-profile changes were added.

- VMA: `0x15045880..0x15045AE4`.
- ROM: `0x72D30..0x72F94`.
- Linked slot SHA-256: `eead237486c5d2ceaba87929d5be6fe8065354414e20547d2d8249256e89b9f0`.

The compiler differences include the selected-index spill/register assignment,
count/index register choices, vertex-copy scheduling, and metadata/flag branch
layout. The retail body has three more instructions. No broad normalization
is justified by this checkpoint; matching remains a separate task.

## Recovered Contract

Initialize result height from `D_80098D50`. Retail ROM offset `0x23D810`
contains bits `0x47C34FF3`, or `99999.8984375f`, not a rounded sentinel.
Prepare the input using `func_150A44F0(input[0], D_800D37E0, 0)`, then reload
input and position X/Z for `func_150A43E0`. X/Z truncate to signed integers
at this caller boundary. This routine has no early threshold-rejection gate.

Scan the returned candidates in order. Convert their signed fixed height by
`1/256`; select the strict lowest height satisfying `positionY <= height`.
Strict comparison against the current result height preserves the first tie
and excludes sentinel-equal candidates.

When selected, cache the triangle and vertex byte offset before copying nine
signed halfwords. The offset is measured in bytes, not vertex-array indices.
Reload the candidate's fourth word after the copies as an entity index.
Publish the entity address to result `value` before loading its metadata table.
Use the table when present, indexed by the signed relative triangle index
minus the unsigned `firstTriangle`, preserving 32-bit subtraction; otherwise
publish the entity's default metadata.

OR result flags with `6`, then reload both the candidate entity index and the
global entity-table base before reading entity flag bit `0x80`. This differs
from the recovered highest-height query, which uses its cached entity pointer.
If set, OR result bit `1`. Set state `2`. Return one only when the published
height is `<= threshold`, ORing bit `2` again on that path. A selected candidate
still publishes vertices/metadata/state/flags when this final comparison fails.

If no candidate is selected, clear only result bit `2`, retaining the initialized
or helper-mutated height and other fields. Ordered comparisons handle NaN Y
as no eligible candidate and NaN threshold as a selected-but-failed result.

## Tests / Verification

Fifteen tests in `tools/tests/test_game_entity_lowest_height_query.py` compile
the actual production definition and existing guest layouts in the established
32-bit freestanding harness. Only the two preparation/collector calls are
mocked; no production geometry implementation was changed.

Coverage includes the retail sentinel bits, default/table metadata, strict
selection and first ties, inclusive bounds, absent candidates, all result and
entity flag combinations, signed fractional heights and negative byte offsets,
NaNs, untouched padding, input/position/helper-height mutations, cached triangle
versus reloaded entity index, and entity publication before metadata-table load.

Two additional alias probes distinguish this routine's later reloads:

- Result flag publication overlaps the selected candidate's entity-index word.
  Metadata/value use the earlier entity, but the later entity-flag read must
  observe the updated index.
- Result value publication overlaps the entity-table-base variable in a
  controlled union. Metadata uses the cached entity pointer, while the later
  flag read uses the newly published global base.

All 256 repository tool tests pass without skips. The retail-ROM assertion
would explicitly skip when a ROM is unavailable; it ran successfully here.
Full `make -C conker NON_MATCHING=1 all match-progress -j4` and
`make tools-check` pass. Independent linked extraction verifies the full
612-byte slot, all 88 differences, and unchanged next address `0x15045AE4`.

Both cached queries, their recovered dispatch wrappers, the typed three-argument
caller, both count forwarding helpers, both context-3 queries, the 520-byte
producer/return closure, and the 5,712-byte collector group remain exact.
Both entire Init sections retain the retail hashes from Note 768. The highest
entity query is unchanged at 72 differences and hash
`b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.
No guest execution or natural gameplay acceptance is claimed.

## Progress / Next

Fresh classified inventory: 5,459 / 6,042 C rows (90.35%),
1,929,384 / 2,256,728 C bytes (85.49%). Game is 4,786 / 5,321 (89.95%),
1,757,948 / 2,072,880 bytes (84.81%). Remaining assembly: 583 overall,
535 Game. Init/Debugger classification is unchanged.

Exact C numerators remain 3,262 total and 2,589 Game. Their denominators
increase to 5,459 and 4,786, giving 59.75% and 54.10%; zero drift and
2,197 differing Game rows. The former exact assembly slot is now non-matching
C, so no new exact-match progress is claimed.

Next audit and recover the adjacent `func_15045AE4` zero-return placeholder.
Its retail assembly uses `D_80098D54` and the same scratch buffer; establish
its own selection, metadata, reload, and result-state contract before reuse.
Continue lowest/highest entity-query matching separately. Remaining Init gates
are unchanged in [Note 768](768-init-remaining-assembly-current-decision-20261003.md).
The sibling host port and frozen Release artifacts remain untouched.
