# Game Texture Metadata And Cache Maintenance Recovery

Date: 2026-10-04. Starting HEAD: `7bc7cfc1`.

## Decision

Finish the interrupted Game edits preserved by the Init checkpoints in
[Note 966](966-init-resume-preincrement-bitmap-and-conversion-decisions-20261004.md)
and [Note 967](967-init-decoder-entry-value-lifetime-fitting-trials-20261004.md).
Recover metadata loader `func_15003570` and cache maintainer `func_1510D404`,
then qualify their actual connection to the existing initializer, resolver,
setup, cached lookup and release helpers from
[Note 965](965-game-texture-resource-setup-resolver-and-attachment-recovery-20261004.md).
Both bodies fit without new guards, compiler profiles, data owners or drift.
They remain non-matching. This is source recovery, not instruction parity.

| Function | C body / retail slot words | C / retail frame | Raw differing words |
| --- | ---: | ---: | ---: |
| `func_15003570` metadata | 58 / 62 | 0x30 / 0x30 | 54 |
| `func_1510D404` maintenance | 125 / 129 | 0x40 / 0x60 | 119 |

The maintainer's frame is smaller than retail, not matching. The shared
`D_80091D20` and `D_800B87A0` declarations now reflect measured unsigned
halfword accesses. No table is defined or moved. The existing initializer
`func_150034B4` stays unchanged and raw-exact across all 47 words; fixtures
execute its side effects without reading its legacy missing return value.

## Metadata Contract

The checksum-verified retail ROM supplies this routine's reference; its
per-function assembly file is absent. It allocates `(16,1,2,0)` once, starts
at `D_1A37E0` (`0x001A37E0`), and processes all 7762 records. Each iteration
remembers the source's odd-byte skip, aligns down, and submits a sixteen-byte
mode-1 DMA into the same buffer. The DMA result is ignored. Four big-endian
header bytes assemble the extent with retail's 0/3/1/2 read order, and a
halfword store truncates the value without extra validation.

The compressed length is read freshly after DMA and before the extent store.
The next source is the original unaligned source plus that unsigned length,
not the aligned address plus length alone. Zero lengths still perform DMA
and publish an extent, but leave the source cursor unchanged. The loader frees
the original buffer after all entries and does not update cache, priority,
activity or work counters. The extent table is 15524 bytes, ending at
`0x800BC444`; it is not the compressed-size table targeted by the obsolete
commented draft, which is removed.

There is no invented NULL-allocation guard. Successful allocation qualifies
the complete bounded path. NULL allocation is tested only through the first
DMA-call prefix; a nonreturning fixture exits before the invalid header access.
This does not establish graceful allocation-failure handling.

## Maintenance Contract

Capture the last dirty ID before the early gates. Last ID -1 returns unchanged.
With zero unsigned work counter, nonzero freeze returns unchanged; otherwise
a nonzero counter decrements even while frozen. Capture the first ID afterward,
then reset dirty bounds to `0xFFFF` / -1 before diagnostics or other callbacks.

Preserve retail's diagnostic gate `first < 0 || last >= 0x1E53`, its error write
`0x0C000046`, and call to `func_150AD770`, without adding an early return.
The gate is not tightened to the 7762-entry table limit. Complete table scans
are qualified only for IDs 0..7761. Returning diagnostics are tested only on
empty captured ranges; invalid nonempty ranges are prefix-only tests. The real
hardware diagnostic callee is not newly qualified. In particular, ID 7762
passing this gate is not evidence of a safe nonempty table access.

Set the diagnostic marker to -1, scan the captured inclusive range, and finish
at -2. Callback changes to dirty bounds do not expand that captured scan.
Each entry reads fresh signed priority: zero is skipped; values below four
decrement with byte wrapping. A fresh zero result sets the marker to the ID,
frees the current cache pointer, then overwrites it with `0xFFFFFFFF` after
the callback. Other decremented values requeue using fresh dirty bounds.

For states at least four with bit `0x40`, capture the entry destination and
its temporary address. Decode from the temporary plus entry offset with
32-bit wrapping and fresh scratch-global input. Decoder results, including
zero and negative values, are ignored. Free the captured temporary, clear
only bit `0x40` from the fresh post-callback priority, and requeue against
fresh bounds. Do not restore cache pointers mutated by callbacks. Subsequent
entries read fresh state, cache and scratch. Activity counts are untouched.

## Verification

Seventeen new checks in
[`test_game_texture_metadata_and_maintenance.py`](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_texture_metadata_and_maintenance.py)
extract actual production C bodies. Strict 32-bit host fixtures cover:

- All 7762 metadata entries, odd-source alignment, big-endian assembly,
  unsigned lengths, truncation, callback reloads and adjacent table fences.
- All 256 signed priority byte states and all 256 unsigned work-counter
  values under both freeze states; early gates preserve state.
- Captured scan bounds, fresh next-entry reads, callback cache replacement,
  staged decode/free ordering, wrapping offsets and ignored decoder results.
- Complete valid-range scans, empty diagnostic fallthrough and explicitly
  prefix-only invalid-range/NULL-allocation observations.
- Actual metadata -> initializer -> setup/resolver -> cached lookup -> release
  -> three maintenance ticks -> free, including work while frozen.

Allocator, DMA and decoder calls remain opaque mocks. Staged headers are
fixture-supplied; their producer chain is not recovered here. Existing setup's
first unwritten scratch paths remain unqualified. The narrow fixture warnings
suppressed are the unchanged initializer's missing return and setup's existing
possibly unwritten scratch. No production initialization is invented.

Fresh isolated IDO compilation and MIPS linking reproduce both complete
production slots including padding, without instruction normalization. Tests
also compare independently against the checksum-verified retail ROM and
confirm that no new expected-word guards were added.

**All 221 combined checks pass in 42.811 seconds, no skips.** This is the prior
204-check suite plus the seventeen new checks. A forced fresh production link
and regenerated progress/matcher succeed. Existing duplicate
`generated_12D630` recipe warnings remain; no unrelated cleanup is bundled.

```sh
make -C conker NON_MATCHING=1 -W build/conker.ld build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_texture_metadata_and_maintenance -q -f
make tools-check
git diff --check
```

| Complete Slot | SHA-256 |
| --- | --- |
| `func_15003570` | `096cbdac52e624b1a23fd8f3f7430477801c27d22ab78fb3b57418a95138fb06` |
| `func_1510D404` | `eccdb2fdca0e14d179f3f0e7299448b7dd41135e17ae14d53922683f615ee991` |
| Exact `func_150034B4` | `e40b0a2074438b5ae230d482a4c69f67751c42dbbbcd60561de1d9c3dd8c643b` |
| Exact `func_15007830` | `35409e3b55dd3cc62229f6fe0dbb7d58cfa76db9b03e30b1dec4c8c621b22e90` |

Full raw sections remain retail-exact, including every executable byte rather
than only listed C functions:

| Section | Bytes | SHA-256 |
| --- | ---: | --- |
| Init code | 164048 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| Init data | 17376 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |
| Debugger code | 19800 | `f619cd1afa30c26f6b6e91cb597689b52a74e8c072002dbf7b30789e4df0facf` |
| Game data, 720 owners | 189088 | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

Fresh matcher: 3282 / 5463 exact C functions, zero drift, 2181 different.
Init 492 / 492 and Debugger 181 / 181 are exact; Game is 2609 / 4790.
Both recovered placeholders were already counted as C, so README aggregates
stay unchanged. Recovery narration remains in dedicated documentation.

## Sibling And Next

Subsequent checkpoint: [Note 969](969-game-immediate-texture-cache-release-recovery-20261004.md)
recovers immediate release and qualifies its bounded actual resolver/retain/
release/maintenance/reload connection. The remaining matching and real guest
gates here stand; next-source discussion below records this note's checkpoint.

Read-only audit of active sibling `recomp_out/.c` finds the complete original
recompiled initializer at line 92867, metadata at 92983 and maintenance at
822005. Active CMake consumes that file. A nearby stale zero-stub comment is
not current evidence. No host source/import/build, save or frozen Release change
is made; existing recompiled bodies are not fresh PC runtime acceptance.

- [x] Recover metadata and maintenance without new guards or ownership changes.
- [x] Fit complete slots, with explicit non-matching frame/instruction measurements.
- [x] Qualify bounded connected initialization/loading/maintenance/release lifecycle.
- [x] Preserve full Init/Debugger/data sections, exact leaves and prior recoveries.
- [x] Recover immediate cache release `func_1510D7AC` (Note 969).
- [ ] Identify and qualify the staged-entry producer; do not mistake the existing
  countdown helper `func_1510D720` for that producer.
- [ ] Pursue raw instruction matching separately.
- [ ] Qualify actual guest DMA/decompression, hardware diagnostics and natural effects.

`func_1510D7AC` must retain activity decrement, captured priority's `0x40`
temporary-free decision, fresh cache reread after that free, and final cache/
priority clearing after the second free. Its retail assembly is in `139FC0.s`.
Init still has 47 ASM entries: seventeen investigation targets and thirty
intentional owners. Note 967's decoder remains 528 bytes over; no production
Init conversion is adopted. No complete pipeline or gameplay parity is claimed.
