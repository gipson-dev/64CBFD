# Game Active-View Projection Setup Guarded Match (2026-11-04)

## Outcome

`func_15012370` now replaces its zero-return placeholder with the semantic
active-view projection setup and matches its complete 64-word / 256-byte
retail body. The recovered C has the retail 88-byte frame and all nine
relocation bindings. Sixteen checked replacement rows normalize one closed
compiler register-allocation and scheduling cycle; six of those rows carry
relocations. There are no inserted or omitted instructions.

This is a source/ABI/caller, raw and padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and graph-
retention result. It is not renderer, camera, split-screen, or live gameplay
acceptance.

## Preserved semantic contract

The function reads the signed active-view count from `D_80082FA0`. A negative
count performs no work. Otherwise, an unsigned byte index walks every view
from zero through the live inclusive count. Each 0x180-byte view record is
loaded through the mutable base pointer `D_800BE628`; its horizontal and
vertical extents at offsets four and eight are halved.

For each view, the same byte index selects a 0x40-byte matrix from
`D_800DCC10`. The function calls `func_151EF954` with the matrix, symmetric
left/right and bottom/top half extents, near plane `1.0f`, the captured far
plane `D_80096560`, and final scale `1.0f`. The post-call loop check reloads
the mutable active-view count, and the next iteration reloads the mutable
view-base pointer. The permanent guest oracle mutates both values across the
call so neither required reload can silently collapse into a cached value.

The original commented draft identified the broad projection operation but
used an incorrect pointer shape and did not reproduce the retail load order.
The installed private 0x180-byte record type names only the two proven extent
fields and leaves the remaining bytes opaque. An explicit initial signed
guard followed by the inclusive `do`/`while` loop recovers the retail control
flow and load schedule.

## ABI, owner, and caller registration

The recovered ABI is `void func_15012370(void)`. The owner is
`conker/src/game_3F820.c`. The sole direct retail call is at ROM `0x3B9A4`
inside `func_1500E470`; there are no aligned code-pointer literals. The
qualifier preserves both neighboring owner functions and every non-target
byte.

The natural compiler body and linked retail slot are both 64 words with an
88-byte frame. Before normalization, sixteen positions differ. The closed
cycle rotates the matrix-table base, mutable view-base address, and 0x180
stride through `s2`/`s3`/`s4`, and the vertical extent and negated horizontal
extent through `f6`/`f8`. Sixteen fail-closed expected-word rows restore only
that allocation and schedule. They do not replace control flow, data
selection, arithmetic, loop bounds, or the projection call.

## Qualification and execution

The permanent qualifier was committed first as tools commit `60a03ca`
(`test(game): qualify view projection setup match`). Its four-test suite
passes in 26.812 seconds:

- all 64 retail words, all nine bindings, both owner neighbors, the sole
  caller, and the strict 6,051-function image are closed;
- 180 guest cases across stack phases zero and eight exercise negative and
  active counts, byte-index behavior, mutable base/count reloads, and call
  clobbers while reaching all 64 words;
- native 32-bit O0, O2, and O3 builds each pass 2,640 cases;
- nine independent semantic controls are rejected; and
- all 256 raw-byte mutations, all nine relocation-binding controls, and guard
  row mutations fail closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 5.982 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

The actual production ELF target rebuilt the complete object corpus because
the shared guard manifest changed, then compiled, padded, assembled, and
linked `game_3F820` normally. The installed qualifier reproduced the private
qualification result. The subsequent `make -C conker all -j2` generated the
ROM image and stopped only at the expected final retail-ROM SHA mismatch.

| Artifact | SHA-256 |
| --- | --- |
| Natural 64-word compiler body | `5730645ece6040272140a5f46ce5275c9061b7a7e34fc69347872252eff89072` |
| Complete linked retail target body | `d1f0da4ee79135b394b310b8eab130d6a545a7edd4919791c0bf7b9c777756f9` |
| Installed semantic owner source | `be96fc3ac89ef75fd433792348f237e671e4198ce10e2f4ea2ed88c1718963f3` |
| Qualified/production owner object | `6b7a21731a21188b972cc88933ca3aac776f2b380ea188bc223ede894ec47585` |
| Predecessor linked ELF | `0e23d0dd59d6dfce9dc5abc84d803a40450dbaf55b42ca6a184b17aa51032207` |
| Qualified/production linked ELF | `02716dca0f05d48a92d162e942b29c4fa2a14b5aef5f09b363b6ff711fdbc513` |
| Production rebuilt ROM image | `5895c1c74cbf4c7f4d80474bfebd47f74de0546c0bb4b4fe3ea55150dd47a9f1` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Guard table | `7de1c4a4b70f5fca5372f25065193febe29e8bf39742855f220be890b3c85fdd` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,131 / 5,511 (74.96%)**, zero address drift, 1,380 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,458 / 4,838 (71.48%)**, zero drift, 1,380 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **278 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted two uncached inputs but
proposed only 24,549 nodes against the retained 58,343-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained at 58,343 nodes / 112,212 links with SHA-256
`b44a98ca34003a427ab5a956164a81f82b9d695fd05b9f5b61f9dcf8dc9d9e1c`.
No forced refresh was used.

An explicit 12-path incremental rebuild with `force=False` then produced
58,353 nodes, 112,219 links, and 5,152 communities. Against the saved
pre-change snapshot, 58,340 / 58,343 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later. Ten IDs were added
for the Note 2061 file and its section headings. The seven-link net addition
is confined to the explicitly re-extracted owner and documentation, including
the recovered `func_15012370` to `func_151EF954` call and Note 2061
relationships. The resulting graph SHA-256 is
`9a6516bf4d31223d3105fa113b5c32ebc4a2efdc498046e807eef6c82adf6edd`.
A final note-only refresh after recording this section preserved the same
58,353-node / 112,219-link topology and completed clustering normally.

## Continuation

The fresh ranking still begins with the seven documented non-ordinary
boundary cases: handwritten/custom-ABI `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue the ordinary Game queue at `func_1503F800` (65
words, 63 real differences). Every next candidate still requires source,
ABI/caller, owner, guest/native, actual Make, complete-image, protected-data,
production recount, documentation, and graph-retention gates before credit.
