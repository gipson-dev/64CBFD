# Game Entity Height Query: Semantic Recovery

Date: 2026-10-03. Baseline: `bdd5577`.

## Result

`func_15045F8C` replaces its zero-return placeholder with the complete recovered
entity-indexed highest-height query. It remains non-matching: 144 body words
plus one padding nop occupy its original 145-word / 580-byte slot, with
72 differing aligned word positions. No new word guards or compiler override.

VMA: `0x15045F8C..0x150461D0`; ROM: `0x7343C..0x73680`.
Linked slot SHA-256:
`b574cdd78a8c4921af83d6ca6393ee65f0bf0a3757df0ad2d4565cfadab8ff49`.
The following function remains at `0x150461D0`.

The first candidate exceeded the slot by one word. Explicit 32-bit wrapping
subtraction for the metadata index recovered the original subtract-before-
table-address shape and fits the slot. This follows retail's `subu`; it does
not weaken the size gate or replace instructions with raw words.

## Contract

Arguments: position pointer, float lower threshold, input-buffer pointer,
and the existing 36-byte height result. Only input word zero is consumed.
There is no early threshold rejection in this routine.

Initialize result height from `D_80098D5C`: bits `0xC61C4000` at ROM
`0x23D81C`, exactly -10000.0f. Then:

1. Call `func_150A44F0(input[0], D_800D3830, 0)`.
2. Reload position X/Z and input word zero; truncate coordinates to signed
   32-bit integers and call `func_150A43E0(x, z, input[0], D_800D3830)`.
3. Scan its 16-byte candidates, converting signed fixed height with 1/256.
   Select the highest height at or below reloaded Y and strictly above current
   result height. First ties win.
4. Cache the triangle pointer/vertex-array base and signed byte offset. Copy
   three XYZ signed-halfword triplets using the byte offset, not an element index.
5. Reload the fourth candidate word after copying: here it is an entity index.
   Resolve a 160-byte record from `D_800DBEF4` and publish its address in result
   field 0x20 before loading the entity's metadata-table pointer.
6. If that pointer is nonzero, metadata comes from
   `table[(triangle - D_800DBE3C) - entity.firstTriangle]`, using signed
   triangle division by twelve and unsigned-halfword base index. The subtract
   explicitly wraps to 32 bits. Otherwise use the record's default metadata.
7. Set flags OR 6, additionally OR 1 if the entity's flags contain 0x80, and
   set state 3. Existing flag bits are never cleared on selected results.
8. Return one only when threshold <= result height. A selected result below
   threshold still publishes fields and flags, then returns zero.

No eligible candidate/nonpositive count leaves the sentinel and clears only
flag bit 2, preserving all other output fields. Unordered NaN comparisons retain
the original ordered predicates. No new null checks or hardware identities.

## Entity Layout

The narrowly scoped `HeightEntity71820` view has size 0xA0:

| Field | Offset | Retail access |
| --- | ---: | --- |
| Default metadata | 0x40 | Word |
| Metadata table | 0x44 | Pointer word |
| First triangle | 0x58 | Unsigned halfword |
| Flags | 0x6F | Unsigned byte |

The shared result's existing signed word `value` preserves the entity-address
bits without changing other query layouts. The shared candidate's fourth word
is retained as `padC` to avoid unrelated source/test churn; the local comment
documents its entity-index meaning in this collector.

## Tests / Verification

Twelve new actual-source tests use the established freestanding 32-bit harness:
entity layout and stride; scalar/default and relative-table metadata; unsigned
base index 32768 and negative relative indices; first ties and inclusive bounds;
nonpositive counts and all output flags; all 65,536 output/entity flag pairs;
fractional heights and negative byte offsets; helper ordering/input and position
reloads; no early threshold rejection; NaNs and padding.

Two alias tests establish the important reload boundaries:

- Vertex stores overwrite the candidate triangle pointer and entity index.
  Metadata still uses the cached original triangle, but entity lookup uses the
  new fourth word loaded after copying.
- The published entity address overwrites the entity's metadata-table field.
  The subsequent metadata-table load observes that publication.

All 208 tool tests, the full code build, project checks, and diff checks pass.
Previously recovered constructor,
allocator, list pass, overlap, wrapper, both context-3 height queries, and
`func_15045714` remain exact. All 5,712 collector/context bytes and both complete
Init sections remain exact with unchanged hashes from Notes 760 and 761.

Fresh matching totals are unchanged: Total 3,257 / 5,455, Game 2,584 / 4,782,
Init 492 / 492, Debugger 181 / 181; zero drift and 2,198 differing Game rows.
README aggregates are unchanged because this was already classified as C and
is not newly exact. No host-port build or gameplay execution occurred.

## Upstream Gap / Next

The retained `func_15045780` wrapper passes stack-slot addresses 0x1C and 0x18
to `func_15045714`, then the buffer at 0x18 to this query. The existing
helper's fourth parameter name `context` obscures a pointer-word contract:
it forwards that word through `func_150A6500` to `func_150A6568`.

Live retail inspection of `D3040.s` confirms `func_150A6568` starts with
`sw zero, 0(a2)`, and its shared-register scan branches into `func_150A66FC`
and the earlier shared return. Its production C body still returns zero and
does not perform that output write. Therefore this recovery does not qualify
the wrapper's complete natural query path.

Next audit and restore that producer's entire shared-register assembly group,
preserving cross-entry branches and cleanup. Do not restore just its first
named span or convert the wrapper over uninitialized producer output.
Then reconcile the helper's pointer declaration with its callers and pursue
the remaining 72-word matching differences separately.
