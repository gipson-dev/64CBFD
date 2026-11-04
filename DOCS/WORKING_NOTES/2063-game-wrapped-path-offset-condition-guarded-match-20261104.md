# Game Wrapped Path-Offset Condition Guarded Match (2026-11-04)

## Outcome

`func_15075938` now replaces its zero-return placeholder with the semantic
wrapped path-offset condition and matches its complete 70-word / 280-byte
retail body. The natural compiler body already has retail's 24-byte frame and
differs at only three independent scheduling positions. Three checked
replacement rows, two relocation-aware, normalize those positions without
inserting or omitting an instruction.

This is a source/ABI/registration, raw and padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not a live script, path-following, or gameplay
acceptance claim.

## Preserved semantic contract

The routine derives the actor's current path offset from signed byte fields
`unk21E - unk221`. It indexes the active path's unsigned byte count through
`D_800D2108[D_800D154C->unk13F]` and wraps a negative offset upward by
`pathCount - 1`. A nonnegative offset at or beyond that same limit wraps
downward by `pathCount - 1`.

The command target is `D_800D1891`, except that the `0xFF` sentinel resolves
to `pathCount - 2`. Command mode `D_800D1892` selects equality, inequality,
target-less-than-current, or target-greater-than-current for modes zero, one,
two, and every other value respectively. A true predicate dispatches
`func_15075400(D_800D1890)`; a false predicate has no side effect.

The permanent guest oracle covers negative and positive offsets, both wrap
directions and boundaries, sentinel and literal targets, all four predicate
classes, multiple path-table indices, both dispatch outcomes, and
caller-saved-register clobbering at the helper boundary. It also freezes every
consulted global and path-table byte so the condition cannot pass by mutating
its inputs.

## ABI, owner, and registration

The recovered ABI is `void func_15075938(void)`. It consumes no argument
registers and returns no value. The owner is `conker/src/game_A28B0.c`, where
only the target placeholder and its stale declaration/comment block are
replaced; 210 neighboring function bodies remain fixed.

There are no direct `jal` callers or tail jumps in the retail image. The sole
aligned function-pointer literal is at ROM `0x22B430`, registering the routine
as row 144 of `D_80086730`. The qualifier freezes that pointer, row, no-argument
ABI, owner extent, and all owner neighbors.

## Compiler normalization

The natural and retail functions are both exactly 70 words with a 24-byte
frame and 13 relocations. Only three positions differ:

- offset `0x014` materializes the negative-wrap path-count table through
  retail's `t8` lifetime instead of the natural `t9` lifetime;
- offsets `0x034` and `0x038` exchange two independent loads so retail reads
  the path-count table before the actor path index; and
- the moved `D_800D2108` high/low relocation pair remains bound to the same
  symbol.

Every row checks its expected natural word and relocation before replacement.
There are no inserted words, omitted words, semantic constants, branches, or
calls in the normalization set.

## Qualification and execution

The permanent qualifier was committed first as tools commit `60a48a1`
(`test(game): qualify path offset condition match`). Its pre-install four-test
suite passed in 142.009 seconds. The installed-tree rerun passed in 117.723
seconds:

- all 70 retail words, all 13 bindings, the dispatch registration, 210 owner
  neighbors, and the strict 6,051-function image are closed;
- 4,800 guest cases exercise every semantic route and reach 68 of 70 words;
- the unexecuted words at `0x15075988` and `0x15075A04` are duplicate loads in
  structurally unreachable retail branch shadows, remain statically exact,
  and are not claimed as dynamic coverage;
- native 32-bit O0, O2, and O3 builds each pass 3,600 cases with
  undefined-behavior checking enabled, for 10,800 native runs;
- eleven independent semantic controls are rejected; and
- all 280 raw-byte mutations, all three guard-preimage mutations, and all
  three relocation-binding mutations fail closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 17.065 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

The actual production ELF target rebuilt the complete object corpus because
the shared guard manifest changed. It compiled, padded, assembled, and linked
`game_A28B0` normally. The installed qualifier then reproduced the private
result: exactly `func_15075938` changes among all 6,051 functions, all
addresses remain fixed, there are no strict-image exclusions, and protected
Game data remains exact.

The subsequent `make -C conker all -j2` generated `conker.us.bin` and stopped
only at the expected final retail-ROM SHA mismatch. There was no compile,
padding, assembly, link, or image-generation failure.

| Artifact | SHA-256 |
| --- | --- |
| Natural 70-word compiler body | `a2190411ec96578623e9f15a50a3a7c1240dca229587b88982765afaa9ef1418` |
| Complete linked retail target body | `1c5074ed2ea84fa4f3c3fbe507fe177e68070d3d940680714eb3cdd66e4cc7fb` |
| Installed semantic owner source | `390c9363f62bbec7d33c806e16a8defed2cc80a8f5042680ccb58541822c1174` |
| Qualified/production owner object | `5ec79f0375f8e5a65cc5d0f946401ce2776613f0437302ca00a952d03b09e410` |
| Predecessor linked ELF | `dfd8b8c969ae9c950ce594c1c1e1a29384f5f1b484e51423ee3a07d367ce9117` |
| Qualified/production linked ELF | `1509455ede335a43d049b5a96fa6eff2c3018862ba11a9b4ab64904ff816ca37` |
| Production rebuilt ROM image | `d4957ef3708a9c040c421d723479428f5beaa8d3c4808373889e5273a96933d0` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Guard table | `2e397fc947685b7c0bc10c0b0797b67a8f36a57435a3487e5a71cbcfeaead908` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,133 / 5,511 (75.00%)**, zero address drift, 1,378 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,460 / 4,838 (71.52%)**, zero drift, 1,378 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **276 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,571 nodes against the retained 58,364-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained at 58,364 nodes / 112,229 links with SHA-256
`880dde45fa7a65ecbccd84a4c1554565c58266bfd6cdd144b1b83b96ca72d473`.
No forced refresh was used.

An explicit 13-path incremental rebuild with `force=False` then produced
58,375 nodes, 112,238 links, and 5,086 communities. Against the saved
pre-change snapshot, 58,361 / 58,364 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later. Fourteen IDs were
added: the three relocated headings plus the Note 2063 file and its ten
section headings. The nine-link net addition is confined to the explicitly
re-extracted owner, tools, and documentation. The explicit-refresh graph
SHA-256 is
`a563b6ce8d75eb9a537251a2ec31c34fab637dce9d9a0beab952ddaa98afc95e`.
A final note-only refresh after recording this section preserved the same
58,375-node / 112,238-link topology and completed clustering normally.

## Continuation

The fresh ranking still begins with the seven documented non-ordinary
boundary cases: handwritten/custom-ABI `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue the ordinary Game queue at `func_1509C120` (66 words,
63 real differences). Every next candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount, documentation, and graph-retention gates before credit.
