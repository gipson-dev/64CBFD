# Game object-request tracking factory direct match (2026-11-04)

## Outcome

`func_1515BE50` now replaces its zero-return placeholder in
`conker/src/game/generated_188F90.c` with a typed object-request tracking
factory. The semantic C emits all 64 retail words directly under the owner's
retail `-O2 -g3` profile, including the original 48-byte frame and both call
relocations. No expected-word guards, inserted words, omitted words, or
assembly body are needed.

This is source, ABI/caller, compact/padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and
graph-retention evidence. It is not gameplay, tracking behavior, rendering,
save, or PC-port runtime acceptance.

## Recovered behavior and ABI

The O32 function takes an eight-byte object request, an extra-byte count, an
unsigned-byte channel, and a context word. A null requested object returns
null without allocation. Otherwise it allocates category `0x32` with total
size `extraBytes + 0x50`. Allocation failure also returns null without a
copy.

On success, the function copies the complete request to record offset `+0x18`.
It reads the requested object's binary32 XYZ fields at `+0x14..+0x1C` and
duplicates them into the record's current position at `+0x20..+0x28` and
previous position at `+0x2C..+0x34`. It clears all three velocity words and
the list state, stores list index `-1`, marks the record active, clears its
state, and returns the allocated record.

The sole direct caller, `func_1514EE70`, constructs the eight-byte request
from the object pointer, object identity byte `+0x3B`, a zero retained byte,
and size `0x12C`. It passes channel `0xFF` and context one, then forwards the
returned record to `func_1514EC1C` with command `0x16`.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x1515BE50..0x1515BF50` |
| Retail ROM range | `0x189300..0x189400` |
| Owner | `generated_188F90`, 10 neighboring functions |
| Body / retail slot | 64 / 64 words |
| Frame | 48 bytes |
| Bindings | `func_15167A68` and `memcpy` |
| Direct caller | `func_1514EE70`, retail JAL at ROM `0x17C354` |
| Natural compact normalized SHA-256 | `54392dd2d00cc7c415a70a98efd211fb09903f4171cb8ebea65544af189efa03` |
| Linked retail body SHA-256 | `54ef22a94c688b9fa29fc0eca45c961712630d1a1ae00303367dec8a81e750e5` |

## Source provenance and naming

The adjacent `Another Source/CBFD-Recompiled` checkout independently
corroborates the null gates, category, copy extent, position duplication, and
state initialization. Its recovered declaration widens the channel argument
to `s32`, however, while retail explicitly homes argument three and reloads
its low byte. The installed implementation therefore was not copied
verbatim: it uses the caller- and instruction-proven `u8` ABI, named
`ObjectRequest1515BE50`, `RequestedObject1515BE50`, and
`ObjectFollowRecord1515BE50` layouts, and a concise behavior comment. That
properly typed form independently compiles byte-exact.

Without `-g3`, the same semantic body keeps its 64-word size and 48-byte frame
but differs in 14 opening/scheduling words. The exact debug profile is thus a
measured compiler requirement, not an inferred cosmetic flag.

## Qualification

The permanent four-test focused suite establishes:

- 1,440 guest cases cover all 64 words across null-object, allocation-failure,
  success, allocator mutation, post-copy mutation, three low-byte channel
  patterns, wrap-sensitive size/context values, two stack phases, and raw
  zero, signed-zero, finite, infinity, quiet-NaN, and signaling-NaN position
  words;
- 32-bit native O0, O2, and O3 each pass 4,096 cases, for 12,288 positive
  executions, while eight independently compiled semantic controls fail;
- the actual 23-word `func_1514EE70` caller executes 64 connected cases
  through the recovered function and bounded consumer, missing only the two
  target words belonging to the caller-impossible null-object route;
- all 40 successful-path root memory-access fault boundaries retain their
  exact instruction and branch-delay context;
- both relocations and all ten owner neighbors are fixed; and
- the strict 6,052-function image changes only `func_1515BE50`, preserves all
  function addresses with zero exclusions, and leaves all 189,088 protected
  Game-data bytes across 720 owners exact.

The installed focused suite passes all four tests in 29.977 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data
suite passes all 19 tests in 5.120 seconds.

## Production closure

The actual Make owner rule rebuilt `generated_188F90`, and the production ELF
equals the independently predicted qualified ELF. The broad `make all` path
linked the image and generated the binary, stopping only at the expected final
retail SHA check. The inherited duplicate `generated_12D630` recipe warning is
unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `eccf072a9bb5f6907b45638972f56bead039c57f82bde420d81488c285c5057d` |
| Qualified / production linked ELF | `5eeb69cc86385ee93d37996302d4dab5e8c38063cfcff6053859c6973c9de897` |
| Production rebuilt ROM image | `2dfd702f624fa3ff65632a3a8e4c005bc8d99cc16b3dd3b4dbfb5b109b44cf3a` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `a8102c322819976ae187f79f272cc7c5f11c436997b2d80ffcc27134bf71cff3` |
| Guard table | `86559f1ec5fd731636f9ffc1a9960d9fc427cbdc5466bdff7289ea6800f800ab` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,143 / 5,512 (75.16%)**, zero address drift, 1,369 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,470 / 4,839 (71.71%)**, zero drift, 1,369 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **267 more** are needed.

## Continuation

Rerank the ordinary Game queue after this banked direct match. Keep the seven
documented handwritten/custom-ABI/boundary rows (`func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68`,
`func_151AE2BC`, and `func_150A6760`) separate until their specific boundaries
are addressed. Every ordinary candidate still requires source/ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount, documentation, and graph-retention gates before credit.

## Graph retention

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,674 nodes against the retained 58,465-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained byte-identical with SHA-256
`6fdf8e55def5117202a8ddb11203a8e5355d1d6c437fbd63f7d8375d6cc28701`.

An explicit ten-path incremental rebuild with `force=False` then produced
58,476 nodes, 112,334 links, and 5,153 communities. Against the saved
pre-change graph, 58,462 / 58,465 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, and each has one uniquely relocated replacement
two lines later. Fourteen IDs were added: those three relocated headings, the
Note 2072 file plus its title and seven indexed section headings, and the
`ObjectRequest1515BE50` and `ObjectFollowRecord1515BE50` types. The eleven-node
and eleven-link net additions are confined to the owned changes. After adding
this receipt, a one-path stabilization retained all 58,476 prior IDs and
produced 58,477 nodes / 112,335 links with SHA-256
`d9042d20f2ca556cf9c50ef31b2414b8badcf56b42824adbd5bd76e32a27a261`.
