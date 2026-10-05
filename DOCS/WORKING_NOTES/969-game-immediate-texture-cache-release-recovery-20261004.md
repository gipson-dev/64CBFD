# Game Immediate Texture Cache Release Recovery

Date: 2026-10-04. Starting HEAD: `67e22f69`.

## Decision

Completed matching checkpoint: [Note 988](988-game-immediate-texture-release-direct-frame-match-20261005.md)
recovers the original frame and all 46 retail words directly from table-indexed
C. The four-word difference described below records this earlier semantic
recovery, not the current matching state. Host synchronization remains open.

Continue the concrete release gap from
[Note 968](968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md).
Replace `func_1510D7AC`'s zero-return placeholder with its actual void indexed
cache-release body. It fits all 46 words / 184 bytes without new guards,
compiler profiles, data owners or drift. It remains non-matching at **four
frame-related words**. All other 42 words match retail directly from C.

| Measurement | C | Retail |
| --- | ---: | ---: |
| Body / complete slot | 46 / 46 words | 46 words |
| Frame | 0x38 | 0x28 |
| Incoming ID spill/reload | `sp+0x38` | `sp+0x28` |
| Raw differing words | 4 | Reference |

The first body used an unsigned-byte local for the captured activity value:
it fit 46 words with twenty differences. A full-width signed local captures
the unsigned byte load without narrowing and recovers the retail register
allocation. Local-inlining trials recover the smaller frame but change six
pointer-save slots; register qualifiers do not recover the frame. Keep the
clear captured-value form and leave matching open, rather than adding guards
or a compiler override. The activity table itself remains unsigned bytes.

## Retail Contract

The actual reference is the complete assembly in `conker/asm/139FC0.s`,
independently checked against the checksum-verified US ROM at `0x13AC5C`.
The function takes a signed 32-bit index and has no explicit result.
No new ID bounds, cache-sentinel or allocator-result checks are invented.
Complete table behavior is qualified for IDs 0..7761 only.

Capture signed priority first. Zero priority returns without changing activity
or accessing cache contents. Otherwise read unsigned activity; zero activity
also returns without cache dereference. Nonzero activity decrements, with a byte
store, and only the transition from one to zero proceeds to freeing. Counts
above one retain cache and priority. This is immediate release, not the
countdown/dirty-range path in `func_1510D694` or `func_1510D720`.

Captured priority bit `0x40` selects staged cleanup, including negative signed
priority values with that bit set. Read the cached entry's first word and free
that temporary first. Then **reread the cache pointer after the callback** and
free its current value. Without the staged bit, only the latter free occurs.
Preserve the ID/priority location across callbacks. After the final free,
overwrite cache with `0xFFFFFFFF` and priority with zero. Do not clear before
the callback, recheck activity/priority after it, or restore callback changes
to activity, dirty bounds, counters, scratch or diagnostic marker.

The helper does not submit DMA/decode, update dirty bounds, change work/freeze
policy or use the maintenance diagnostic marker. Such changes made by an
opaque free callback persist. It does not add a safe handling policy for
malformed staged pointers or double frees. Pointer-value forwarding tests use
non-dereferencing free mocks; they do not qualify the real allocator on invalid
or sentinel addresses. Staged entries need a valid readable header for complete
path tests; their producer remains a separate gate.

## Verification

Extend the existing actual-body fixtures in
[`test_game_texture_metadata_and_maintenance.py`](../../tools/tests/test_game_texture_metadata_and_maintenance.py)
with six host tests:

- All 65536 priority/activity byte pairs, including negative staged priorities,
  zero gates and exact one-to-zero release semantics.
- All 7762 valid IDs, both staged and direct paths, neighboring entries and
  first/last table fences; metadata stays untouched.
- Direct free callback observation before final clearing, with unrelated
  callback mutations preserved afterward.
- Staged temporary free, callback cache replacement, fresh second-free argument,
  and clearing after the second callback despite changed activity/priority.
- Forwarding NULL/failure/sentinel values only to opaque free mocks, plus zero
  gates that avoid invalid staged-header dereference.
- Actual resolver load -> second retain -> two immediate releases -> no-op
  repeated release -> maintenance scan -> fresh resolver reload.

The connected test proves retained cache survives the first release, the second
frees once, maintenance does not resurrect or free it again, and a later lookup
really reloads. Allocators, DMA and decoder remain bounded mocks. This is not
guest allocator/DMA/decompression or natural PC gameplay acceptance.

The existing independent IDO O2/g3 compilation/link test now reproduces all
46 production words and checks every differing offset/value against retail.
ROM checks prove signed priority/unsigned activity loads, both actual free call
targets, fresh cache load and final store order. No instruction normalization
or expected-word guards are used. Previous slot identities remain unchanged.

| Offset | C Word | Retail Word | Remaining Difference |
| --- | --- | --- | --- |
| 0x00 | `27BDFFC8` | `27BDFFD8` | Frame allocation |
| 0x68 | `AFA50038` | `AFA50028` | Incoming ID spill |
| 0x6C | `8FA50038` | `8FA50028` | Incoming ID reload |
| 0xAC | `27BD0038` | `27BD0028` | Frame release |

Complete production slot SHA-256:
`66c2e6b5363ad9d29b288807d7c41a9a8ddf76b95070e7f52dd94bf0ec1e55e3`.
Complete retail slot SHA-256:
`21edadf96d05d36e293a9788fe9cfb4dba5a4b5c7b916d978b3b21755070046e`.

**All 227 combined checks pass in 49.701 seconds, no skips.** The texture
metadata/maintenance suite now has 23 checks, six more than Note 968's baseline.
Fresh production compile/padding/link/progress/matcher succeeds. Existing
duplicate `generated_12D630` recipe warnings remain; no new source warning.
Complete Init code/data, Debugger code and Game data stay raw retail-exact,
including exact initializer/startup and the earlier resource/emitter recoveries.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_texture_metadata_and_maintenance -q -f
make tools-check
git diff --check
```

The full combined command is Note 968's 221-check suite with the expanded
texture module. Fresh totals are unchanged: 3282 / 5463 exact C functions,
zero drift, 2181 different; Init 492 / 492, Game 2609 / 4790, Debugger 181 / 181.
The recovered placeholder was already counted as C. README aggregates are
unchanged; recovery narration stays in dedicated docs.

## Sibling And Next

Subsequent checkpoint: [Note 970](970-game-queued-segment-writer-and-big-endian-alias-qualification-20261004.md)
recovers the queued segment writer and qualifies its bounded queue/alias
behavior. Immediate-release matching and host synchronization remain open;
this note's next-source discussion records its original checkpoint.

Read-only sibling audit finds active `recomp_out/.c` line 822784 still has
`func_1510D7AC`'s zero-return stub. The scoped search of host `src` and active
`CMakeLists.txt` finds no named override. CMake consumes the generated `.c`.
Record a separate PC synchronization task; no host source/build/save or frozen
Release change is made. Note 968's original recompiled metadata/maintenance
bodies do not imply this immediate-release helper is implemented in the host.

- [x] Recover immediate release without guards or ownership changes.
- [x] Qualify every priority/activity byte pair and every valid cache ID.
- [x] Verify callback ordering and connected retain/release/maintenance/reload.
- [x] Preserve exact Init/Debugger/data and prior recoveries.
- [x] Recover queued segment writer `func_1510D8C0` (Note 970).
- [ ] Identify and qualify the staged-entry producer separately.
- [x] Match the remaining frame/spill words without weakening the body contract (Note 988).
- [ ] Synchronize the PC immediate-release stub in a separately qualified host change.
- [ ] Qualify real guest allocator/DMA/decompression and natural effects.

`func_1510D8C0` scans the queue built by existing `func_1510D874`, selects by
key, emits one or two `0xDB06` segment commands and returns the advanced Gfx
cursor. Preserve its unsigned queue count, unsigned segment bytes, repeated
second-address/count loads and alias-visible store order; do not add an
unmeasured clamp. It is not the staged texture producer. The nearby
`func_1510D970` is an object constructor, not a cache producer either.
Init retains all 47 assembly entries and its existing conversion decisions.
