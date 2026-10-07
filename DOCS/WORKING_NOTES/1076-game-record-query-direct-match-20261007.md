# Game Record Query Direct Match

Date: 2026-10-07. Baseline: `120ffef9`,
[Note 1075](1075-game-range-clamp-byte-match-20261007.md).
Restore `func_151438D8` from its zero-return C placeholder. No new guards,
shared-header edits, compiler-profile changes or padder-algorithm changes.

## Retail Contract

272 words / 1088 bytes, frame `0x60`, VA `151438D8..15143D18`,
ROM `170D88..1711C8`. Four-input ABI: signed start/end, low-u16 field mask,
query-record pointer. Return the last matching record pointer, or null.

Null query returns before reading globals or calling the range helper.
Otherwise call the now-matched `func_15143D18` on the caller argument homes,
with limits zero and the signed `D_800D3094` count. Its independent endpoint
clipping is retained; an excluded range can stay reversed and scan nothing.
Scan `[start,end)` in ascending order. Do not introduce an inclusive endpoint,
first-match return, empty-range code or a substitute clamp.

`D_800D3098` contains a pointer to records of stride `0x34`. Selected fields:

| Mask | Comparison |
| --- | --- |
| `0x001` | Signed halfword triple at `0,2,4` |
| `0x002` | Signed halfword triple at `6,8,A` |
| `0x004` | Float at `C` |
| `0x008` | Float at `10` |
| `0x010` | Unsigned byte at `14` |
| `0x020` | Query byte at `15` equals record byte at `15` shifted right two |
| `0x040` | Unsigned byte at `16` |
| `0x080` | Unsigned byte at `17` |
| `0x100` | Word at `18` |
| `0x200` | Word at `1C` |
| `0x400` | Word at `20` |

Two u16 accumulators distinguish selected matches from unselected/passing
fields. With `0x1000`, every selected comparison must pass. With no selected
fields that mode accepts every scanned record. Without `0x1000`, at least one
selected comparison must match; an empty selection accepts nothing. Other
mask bits are ignored. Keep triplet short circuits and live table reads.
Floating equality accepts opposite signed zeros and rejects NaNs; general
hardware FCSR/exception behavior is not qualified by these bounded models.

## Direct Compiler Recovery

[Driver](../../tools/experiments/game_record_query_candidates.py) reproduces
98 measurements: 16 mask/loop/order/input-type forms under four profiles,
30 declaration/storage controls and four selected-profile controls.
The first u16 candidate already emits 272 words/frame0x60, but saves its
result pointer at stack `0x5C` rather than retail `0x58`. Declaring the signed
index before the result pointer recovers both private references directly.

Four declaration permutations emit exact O2/g3 code; the selected-profile
measurement repeats one of them. Selected O2 has one scheduling difference;
O1 variants are oversized. Production remains O2/g3. No forced frame padding,
private-offset guard, register patch, instruction insertion or omission.
All 272 words and five relocation identities match the original routine.

The legacy shared header incorrectly declares `D_800D3098` as an inline
`struct178[73]` array. This owner scopes that declaration to an unused legacy
name while including the header, then declares the actual typed pointer.
Other owners and the shared header are unchanged. Existing typed generated
owners already use the pointer interpretation. A cast-through-array accessor
was screened but altered four final temporary-register words; it is not used.

## Qualification

[Ten maintained tests](../../tools/tests/test_game_record_query_match.py):

- 12288 paired raw-C/retail guest cases: every 11-field selection, both modes,
  three record-match patterns and alternating stack phases. Complete mapped
  memory and ordered read/write traces agree with retail, and public pointer
  returns agree with an independent field-selection reference.
- Two additional null cases complete coverage of all 267 reachable words.
  Five duplicated else assignments are unreachable after retail branch-likely
  conversion; do not claim execution coverage of those dead words.
- 1470 signed-range cases include extrema, excluded/reversed/equal ranges,
  zero/positive/negative signed counts, and both the original clamp and its
  raw semantic-C counterpart. Negative record indices use explicitly mapped
  guest fixtures, not invalid native pointers. Query aliasing, unread
  unselected fields and fail-closed unmapped reads are checked separately.
- 120 field corner cases cover all triplet components, unsigned shifted-byte
  boundaries, signed zeros, infinities and quiet NaNs.
- 196608 actual freestanding 32-bit native calls exhaust all 65536 u16 masks
  under three independent match patterns. Typed pointer returns, stride/field
  offsets, reversed bounds, read-only complete records/query and null gate pass.
- Thirty storage and four profile controls preserve bounded pointer behavior;
  only the selected exact form is installed. Four compiled semantic negatives
  detect first-match returns, missing byte shift and exchanged any/all modes.
  Oversized negative/profile bodies connect the helper at a disposable address
  to avoid overlap; production and exact-body tests use original addresses.
- 32 cases execute nine original setup/call/delay words at `15011E34..15011E54`
  from `func_15011D60`, with the complete query and original clamp connected.
  Check its `0x11A0` mask, stack query, count forwarding and word-18 delay store.
  Earlier caller state and return scaffolding are seeded/synthetic. This is
  not qualification of the complete original caller.
- Copied original/selected owners retain all 89 function symbols, all 88
  neighbors' raw bytes/relative relocations, the 624-byte relocation-owned
  pool and the same two warnings. Raw target agrees with the standalone object.
  Actual assembly post-processing/padding/linking emits all 272 retail words.
- Production source, linked target address/words and the complete existing
  guard history are checked. No target guards exist.

These are bounded guest/native checks, not hardware, gameplay or host adoption.
Earlier fixture errors were confined to oracle inheritance, relocation tuple
representation, native warning hygiene and oversized-control code overlap.
All were corrected before the final post-link run.

## Production Audit

US ELF rebuild passes. Across 6059 linked slots, only `func_151438D8` changes;
all addresses/extents are unchanged. Protected `.init`, `.init_data`,
`.debugger` and `.game_data` sections are unchanged. All 720 Game-data owners /
189088 bytes remain exact. The entire 10855-row guard CSV is unchanged.

Matching: total3348/5465 exact (61.26%), Game2675/4792 (55.82%),
2117 different, zero address drift. Conversion remains total5465/6042 (90.45%),
Game4792/5321 (90.06%); the replaced placeholder was already counted as C.
Root README updates aggregate matching rows only. Detailed progress stays here.

All 121 expanded post-link tests pass in 445.383 seconds, with zero skips,
errors or failures. Final tool/syntax/diff checks pass. Documentation checks:
58 documents / 3657 relative links / zero broken links. The linked audit was
rerun after the regression; only the query target changes from the baseline.

## Resume

Sampler `func_151432BC` still needs its two path-local RA reloads and circle-byte
scheduling; no candidate is installed. Oriented builder `func_15142600` still
has 27 private-layout differences. The next forward placeholder is
`func_15143E94`: inspection confirms 98 words/frame0x38, two input words and
a byte-valued result. Its signed-byte count/index scans actor records at
`D_800CC2D0` with stride0x32C/flag1CA, then calls `func_150A29C8` until a zero
result. The successful path indexes `D_800DBFF0` with `D_800BE9E8`/stride0x9A0,
calls `func_1512D748`, takes two RNG results and submits a small stack descriptor
to `func_151D8868`. Recover exact callback interfaces, signed-byte wrapping,
descriptor fields and lazy/global-read boundaries before installing anything.
This inspection is a resume map, not a C recovery or helper qualification.
The matched query can now support later caller reconstruction, but no complete
caller/host adoption is claimed here.

Ignored receipts: `conker/build/game-record-query/` and
`conker/build/game-record-query-test/`. No sibling project, frozen Release,
saves/runtime or push. The broader Game matching goal remains active.
