# Game Texture Resource Setup, Resolver And Attachment Recovery

Date: 2026-10-04. Starting HEAD: `56ed9c28`.

## Decision

Current attachment checkpoint: [Note 990](990-game-attachment-walker-guarded-register-match-20261005.md)
matches its complete linked slot with nine expected-word register/equality
guards. Unguarded C still differs at nine words; setup/resolver matching
remains open. The measurements below record the earlier semantic recovery.

Continue the resource pipeline from
[Note 963](963-game-asset-table-cache-lookup-and-block-load-recovery-20261004.md).
Recover setup `func_1510CE60`, its texture resolver `func_1510D0EC`, and
attachment `func_15168E54`. All three already-counted C placeholders are replaced
with semantic bodies. They fit their original slots with retail frame sizes,
without new word guards, profiles, data owners or address drift. They remain
non-matching; this is source recovery, not retail instruction parity.

| Function | C body / retail words | C / retail frame | Raw differing words |
| --- | ---: | ---: | ---: |
| `func_1510CE60` setup | 152 / 163 | 0x430 / 0x430 | 159 |
| `func_1510D0EC` resolver | 155 / 162 | 0x50 / 0x50 | 142 |
| `func_15168E54` attachment | 45 / 45 | 0x38 / 0x38 | 9 |

The resource helper's local setup declaration is corrected from void to the
actual signed success result. Its existing caller intentionally ignores that
result. The complete constructor/helper/wrapper instruction identities remain
unchanged. Other unrelated placeholder declarations and warning cleanup are not
bundled.

## Resolver Contract

The resolver updates signed minimum/maximum dirty IDs before checking bounds.
Invalid IDs outside 0..7761 return `0x80000000` without table/output accesses.
Compressed sizes use `D_80091D20` halfwords; expanded extents use `D_800B87A0`
halfwords. Local declarations reflect these measured access widths. Cache
`D_800B0E58` uses words, priorities `D_800BC448` signed bytes, and activity
`D_800D9F68` unsigned bytes. No data is defined or relocated.

Zero compressed size overwrites the cache with the failure sentinel, but still
publishes the expanded extent, updates signed priority and optionally increments
activity. Cached entries other than `0xFFFFFFFF` skip loading, including an
already-cached failure sentinel. Priority 63 normalizes to 62 only on a miss,
not on zero-size or already-cached paths. Priority stores retain byte truncation.
Activity increments for any nonzero retain argument and saturates at 255.

A miss sets `D_800DBDBA=5`, obtains the prefix address from the existing exact
`func_1510D374`, aligns odd sources down and remembers the one-byte skip, then
rounds compressed allocation/DMA size to sixteen bytes. Allocation arguments are
`(amount,1,2,1,2)` followed by `(expandedExtent,1,1,0,2)` for `func_10003C6C`.
The second extent is read freshly after DMA. First allocation failure returns
the sentinel without writing output/cache/priority/activity; second failure frees
the compressed temporary and preserves the same unwritten outputs.

Successful allocation decodes from temporary+skip using fresh `D_8003809C`.
Decoder return is ignored, including zero/negative results. The temporary is
freed, expanded pointer cached, activity cleared, then optional output reads the
fresh halfword extent before the return cache word is captured. Output/cache
aliasing therefore affects the captured return. Priority/activity changes follow.
Callback mutation tests check these distinct capture and reload points.

## Setup And Attachment

Setup scans eight-byte commands until signed opcode -33 (`0xDF`). Signed opcode
-3 (`0xFD`) selects texture words. Unresolved-only mode excludes words with a
nonzero top byte; the general top-byte gate excludes values at least `0x06000000`.
The zero-nibble path strips flag bits, calls the actual resolver, writes its
result, and tracks unique original IDs when cleanup output is requested.
Each repeated ID still calls the resolver and increments activity independently;
the cleanup list deduplicates IDs. No balancing change is invented.

The two extent-relative adjustments retain their retail precedence: bit zero
selects extent minus 512, otherwise bit one selects extent minus 32. Arithmetic
and the retained flag OR use original 32-bit wrapping. The 971-byte bitmap is
cleared only when tracking output is supplied. The complete valid-ID fixture
visits all 7762 entries, allocates exactly 15526 bytes and verifies the sorted
halfword list, count and trailing fence. The output allocation always includes
the count halfword, even when the unique count is zero. List allocation failure
writes NULL but does not independently change setup's texture-success result.

Retail retains scratch address/extent across texture commands. A first accepted
already-tagged command can compare an unwritten address; a first adjusted lookup
failure can use an unwritten extent. **These initial-scratch paths remain
unqualified.** C deliberately does not invent zero initialization. A later failed
adjusted lookup with a previously written extent is qualified and preserves that
earlier extent. NULL cleanup output does not initialize/read the tracking bitmap.
Out-of-bitmap IDs and unterminated command streams are not newly made safe.

Attachment scans the same terminator and selects opcode 1, or opcode `0xDC`
with subtype byte 14. It calls the existing exact `func_15168E34` on the second
word with the resource base. That leaf adds the base only when the segment-nibble
mask `0x0F000000` is clear; no extra mask or forced address normalization is added.
Commands after the terminator and unselected commands remain untouched. Original
repeated opening opcode reads are retained using the established volatile form.

The actual `func_151336A8` connection proves setup, resolution and attachment
run on the loaded header/data. Only block loading is opaque in this connection;
the independent actual lookup/block/variadic/relocation connection remains in
Note 963. Helper returns one and still attaches when setup reports texture
failure or list allocation fails. It returns zero only for its NULL loaded header.
No new failure propagation is added.

## Verification

Sixteen new tests execute extracted actual production bodies in strict 32-bit
host fixtures. They include all valid IDs, signed priority/byte truncation,
activity saturation, odd-source alignment, both allocation failures, callback
mutations, output aliases, full bitmap/list construction, deduplicated cleanup
through actual `func_1510D630`/`func_1510D694`/`func_1510D608`, and actual helper
setup/resolver/attachment. Allocators, DMA and decoder remain bounded fixtures.
These are not guest DMA, decompression-corpus or natural gameplay acceptance.

An independent fresh IDO O2/g3 compilation and MIPS link reproduce complete
production slots including padding. The internal resolver call relocation is
normalized explicitly by its object relocation record; no arbitrary instruction
differences are normalized. The existing prefix calculator and address-adjuster
remain raw retail-exact across their complete 36- and 8-word slots.

| Complete Slot | SHA-256 |
| --- | --- |
| `func_1510CE60` | `6ab58d90d8e1815a475fb86e64aa89b31da2a19f6f4e531c96dd158e6b98395c` |
| `func_1510D0EC` | `1fde6b630576ea95a7e990c9402eb31491b7271ff8acd7ec181ad3b42b9100c9` |
| `func_15168E54` | `958dcb84bbf375ebdd6c9170744538d8a59afb5385c31977ab50158843aca792` |

**All 204 combined checks pass in 37.952 seconds, no skips.** Fresh production
compile/padding/link/progress/matcher succeeds. Complete Init code/data, Game
data, previous recoveries and exact callers remain intact. Existing duplicate
`generated_12D630` recipe warnings and unrelated pointer/type warnings in
`game_1944C0.c` and `generated_15F680.c` remain. No new warning cleanup is bundled.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_texture_resource_setup -q -f
make tools-check
git diff --check
```

The combined suite is Note 963's command plus
`tools.tests.test_game_texture_resource_setup`. Both opaque setup fixtures in
the old constructor/loader suites now use the corrected signed-return interface;
their deliberate fixture boundaries remain explicit.

## Sibling And Next

Subsequent checkpoint: [Note 968](968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md)
recovers metadata and maintenance and qualifies the connected bounded lifecycle
including this initializer. The next-pair discussion below records this note's
original checkpoint; real guest DMA/decompression remains unqualified.

Read-only sibling audit confirms active `recomp_out/.c` already has recompiled
setup at line 820924, resolver at 821391 and attachment at 1081473, including
diagnostics/host support. These were not replaced or rebuilt. No mechanical
native-pointer transplant, host source/build, save or frozen Release change.
Existing sibling bodies are not fresh PC runtime parity evidence.

The next concrete source pair is:

1. `func_15003570` (62 words): restore expanded-size metadata loading. Fresh
   retail disassembly confirms sixteen-byte aligned DMA, odd-source skip,
   big-endian four-byte header assembly and halfword stores into `D_800B87A0`,
   not the compressed-size table suggested by its obsolete commented draft.
   Preserve late compressed-length reads and exact source cursor advancement.
2. `func_1510D404` (129 words): restore dirty-range cache maintenance, priority
   countdown/free and staged decompression. Qualify lifecycle and failure/alias
   ordering with resolver/setup/release before claiming a complete pipeline.

Cache initialization `func_150034B4` already has C rather than a placeholder;
its lifecycle still needs connected qualification. Do not mistake the unrelated
palette routine `func_1510CB10` for this cache's initializer.

- [x] Recover setup, texture resolver and attachment without new guards.
- [x] Fit complete slots and preserve actual retail frame sizes.
- [x] Qualify all valid IDs, allocation failures, bitmap/list ordering and aliases.
- [x] Connect actual resource helper, setup, resolver, attachment and release bodies.
- [x] Preserve prior identities, exact prefix/adjuster leaves and full Init/Game data.
- [x] Recover metadata loader `func_15003570` and cache maintainer `func_1510D404` (Note 968).
- [x] Qualify connected cache initialization/loading/maintenance/release in bounded fixtures (Note 968).
- [x] Match the complete linked attachment slot with guarded register normalization (Note 990).
- [ ] Pursue direct attachment compiler matching and setup/resolver matching separately.
- [ ] Qualify real guest DMA/decompression and natural effects; synchronize PC child stubs separately.

Init stays 492 C / 47 assembly. Game stays 2609 and total 3282 byte-exact C
functions, zero drift. All edited routines were already counted as C; README
aggregates remain unchanged and recovery narration stays in dedicated docs.
No complete pipeline, ROM promotion, hardware/gameplay acceptance or push is claimed.
