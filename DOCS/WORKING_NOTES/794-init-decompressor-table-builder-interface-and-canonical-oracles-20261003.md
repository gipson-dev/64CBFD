# Init Decompressor Table Builder Interface And Canonical Oracles

Date: 2026-10-03.

## Result

The complete retained `func_1000696C` body now has nine executable contract
tests. Its register interface, four-byte table format, canonical bit-reversed
lookup, root-width clamping, output allocation indices, and empty/incomplete
paths are characterized. No production assembly-to-C conversion is claimed.
This advances the connected recovery begun in
[Note 793](793-init-decompressor-shared-contract-and-stored-block-oracle-20261003.md).

## Explicit Interface To Recover

| Input | Meaning |
| --- | --- |
| a0 | Pointer to word-sized code lengths; later reused as loop count |
| a1 | Alphabet length |
| a2 | Number of simple symbols before base/extra table interpretation |
| a3 | Halfword base-value array for non-simple symbols |
| t7 | Byte operation/extra-bit array for non-simple symbols |
| t8 | Halfword output cell for root entry index |
| t9 | Word input/output cell for requested/effective root width |
| s6 | Four-byte-entry workspace base |
| f19 | Integer next allocation index, updated after nonempty construction |
| sp | Parent 0xA88 shared scratch frame; no local allocation |

The builder saves s0..s7, fp, and gp in f2..f11 and restores them. It is not
an independent ordinary-ABI seven-argument function: workspace and allocation
state are also implicit, and the FPR scratch lifetime is part of the connected
caller contract. f16/f17/f18 are not the builder's saved-register bank.

Its scratch regions include seventeen length counters at 0x00..0x40, table
pointer stack starting at 0x44, sorted symbols starting at 0x84, and code
offsets starting at 0x504. Input-length bounds and workspace capacity are not
explicit parameters. Invalid lengths/counts need reachability and separate
failure tests before a C rewrite can choose indexing behavior.

## Table Entry Format

Each four-byte big-endian record contains:

| Offset | Width | Meaning |
| --- | --- | --- |
| 0 | Byte | Operation: 16 literal, 15 end marker, 99 invalid, above 16 subtable width plus 16, otherwise extra-bit operation |
| 1 | Byte | Bits consumed at this table level |
| 2 | Halfword | Literal/base value or absolute workspace entry index of subtable |

Allocation reserves a header entry before each lookup table. Its halfword
at offset two links the next allocated lookup table; root/subtable indices
address the first lookup entry, not that header. Values are entry indices,
not byte pointers. Lookup masks the low reservoir bits and shifts only by
the current entry's consumed-bit byte before following a subtable.

## Oracle Evidence

New file: `tools/tests/test_init_decompressor_tables.py`.

The bounded builder model executes the original 293 instruction words,
including likely branch annulment, integer FPR moves, and zero doubleword
scratch stores. It deliberately models only used instructions and low-word
integer state, not privileged/FPU hardware behavior. Sparse memory rejects
unwritten reads rather than silently supplying zeros.

An independent canonical encoder assigns codes by length/symbol and reverses
them for low-bit-first lookup. Tests cover complete small trees, zero-length
symbols, requested widths 0/1/2/7/16, subtable links, allocation append,
saved-register preservation, single-symbol trees, and incomplete tables.

The fixed 288-symbol length array is 144 eights, 112 nines, 24 sevens, and
eight eights. All 288 canonical lookups match actual base/extra arrays parsed
from retained data assembly, including end marker and reserved operations.
The fixed thirty-symbol distance alphabet likewise matches all thirty base/
extra pairs. This qualifies table lookup, not decoding complete compressed
streams or proving the parser reaches these inputs.

The builder's entire 1,172-byte reference body matches retail ROM when
available, with SHA-256:

`671a7926edb4a0b13a0fda7de90eb090cd9211b8f364aef7f6950d915b3b8b5f`.

## Recovered Fixed Workspace Addresses

The literal/length build has root index one, effective width seven, and
allocation index 625. Appending the fixed distance table starts at root
index 626 and ends at allocation index 658, effective width five.

```text
0x8003BE90 + 1 * 4   = 0x8003BE94  literal/length root
0x8003BE90 + 626 * 4 = 0x8003C858  distance root
```

These exactly explain the two retained pointers used by fixed wrapper
`func_1000692C`. They are fixture-derived allocation/interface evidence,
not an observed startup execution or a new linked data comparison.

## Status And Edge Boundaries

- Zero alphabet count returns one without publishing outputs or allocation
  state. The opening delay slot still writes the s0 snapshot into f2.
- A nonzero all-zero alphabet returns zero and publishes root/width zero;
  allocation state is unchanged.
- Incomplete trees return one but may have usable tables and invalid-operation
  entries. A single one-bit symbol returns zero despite its invalid alternate
  entry. Return status is not a general pointer-validity predicate.
- The thirty-symbol fixed distance tree returns one with two invalid slots;
  all thirty real symbols remain usable. Startup ignores builder statuses.
  Do not turn every nonzero result into an unconditional conversion failure.

A complete synthetic `[1,2,3,3]` alphabet with requested width one returns
zero but leaves a lookup unwritten in this model: the root's odd entry reports
subtable width two at index six, and canonical symbol three indexes unwritten
entry nine. The same alphabet succeeds at requested widths two and seven.
This is pinned as model-observed behavior, not a verified retail gameplay bug
or proof of an emulator-independent defect. Inspected production call sites
request widths seven or five (subsequently clamped to min/max code length).
Do not silently repair the narrow-root behavior during semantic recovery.

## Verification

All nine builder tests, all 37 focused Init tests, and all 492 tool tests
pass (full suite: 53.179 seconds; final allocation assertions also pass in
the focused rerun). Project tool checks and `git diff --check` pass.
Production Init assembly, compiler profiles, word guards,
inventory, and README aggregate values remain unchanged. Pending Game edits
and earlier Init tests/documents are preserved.

## Next

1. Use these generated fixed tables in an instruction-word compressed-decoder
   fixture; exercise literals, end marker, lengths/distances, extra bits, and
   forward overlapping copies. Compare valid output independently with zlib.
2. Add dynamic table-length repetition and multi-block/cursor/header fixtures.
   Pin status propagation and output-count publication on failure.
3. Resolve invalid lengths, oversubscribed trees, workspace exhaustion,
   literal limit handling, and the exception caller's FPR context before
   designing connected C ownership. No independent leaf extraction is made.
