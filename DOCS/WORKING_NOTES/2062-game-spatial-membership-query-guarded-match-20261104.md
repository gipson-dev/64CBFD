# Game Spatial-Membership Query Guarded Match (2026-11-04)

## Outcome

`func_1503F800` now replaces its zero-return placeholder with the semantic
spatial-membership tree query and matches its complete 65-word / 260-byte
retail body. The recovered C is compiled naturally as a 32-byte-frame routine;
52 checked replacement rows normalize the compiler allocation and schedule to
retail's 24-byte frame. Three rows move the initializer and mutable-root
relocations to their retail positions. There are no inserted or omitted
instructions.

This is a source/ABI/caller, raw and padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and graph-
retention result. It is not a live collision, scene-traversal, or gameplay
acceptance claim.

## Preserved semantic contract

The query truncates the supplied X and Z values to signed 16-bit coordinates,
calls `func_1510F800(0)`, and only then loads the mutable tree head from
`D_800DBE48`. Each node contains a signed category mask, signed sibling and
child byte offsets, an unsigned 16-bit radius, and signed 16-bit X/Z center
coordinates.

The coordinate test uses inclusive bounds on both axes. Radius remains
unsigned while each center and query coordinate remains signed, so the lower
and upper comparisons preserve the retail mixed-width behavior. A matching
node rejects a missing category bit immediately. A matching category descends
through the signed child offset when one exists and returns zero only when the
selected node is a leaf. Out-of-bounds nodes advance through the signed sibling
offset. A zero offset or exhausted chain returns one.

The permanent guest oracle covers both positive and negative relative offsets,
inclusive edge coordinates, signed query truncation, unsigned-radius cases,
category rejection, child and sibling routes, and accepted leaves. It also
changes the root during the initializer call and clobbers caller-saved state,
so neither the required call-before-load ordering nor the retail argument
lifetime can collapse unnoticed.

## ABI, owner, and caller registration

The recovered ABI is
`s32 func_1503F800(void *query, s32 x, s32 z, s32 category, s32 mode)`.
The first and fifth words are supplied by callers but are not consumed by the
retail body. The owner is `conker/src/game/generated_6CCB0.c`, replacing only
the target placeholder while retaining its two owner neighbors.

There are two direct retail calls: ROM `0x6CDFC` in `func_1503F904`, whose
fifth caller word is one, and ROM `0x1400E8` in `func_15112A80`, whose fifth
caller word is zero. There are no aligned code-pointer literals. Both caller
registrations, all five argument positions, the initializer, mutable root, and
the complete target extent are frozen by the qualifier.

## Compiler normalization

The natural compiler body and linked retail slot are both exactly 65 words.
Before normalization, 52 positions differ: the natural body uses a 32-byte
frame and one saved register, whereas retail uses a 24-byte frame and keeps the
query values in its stack/register schedule. The checked replacement rows
form a complete positional replacement set for those differences. They do not
insert or omit words and do not replace any unaccounted natural word.

The three natural relocations are preserved as the three retail relocations:
the `R_MIPS_26` initializer call and the `R_MIPS_HI16`/`R_MIPS_LO16` mutable-
root pair. Every row checks its expected natural word before replacement, and
the permanent mutation test proves that changing any one of the 52 preimages
fails closed.

## Qualification and execution

The permanent qualifier was committed first as tools commit `1797d92`
(`test(game): qualify spatial membership query match`). Its four-test suite
passes in 278.444 seconds:

- all 65 retail words, all three bindings, both owner neighbors, both callers,
  and the strict 6,051-function image are closed;
- 5,394 guest cases across both stack phases exercise every semantic route and
  reach 63 of 65 words;
- the two unexecuted words at `0x1503F8B4` and `0x1503F8E4` are structurally
  unreachable retail branch/delay shadows, remain statically exact, and are
  not claimed as dynamic coverage;
- native 32-bit O0, O2, and O3 builds each pass 1,024 cases with undefined-
  behavior checking enabled;
- ten independent semantic controls are rejected; and
- all 260 raw-byte mutations, all three relocation controls, and all 52 guard
  preimage mutations fail closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 13.219 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

The actual production ELF target rebuilt the complete object corpus because
the shared guard manifest changed. It compiled, padded, assembled, and linked
`generated_6CCB0` normally. The installed qualifier then reproduced the
private result: exactly `func_1503F800` changes among all 6,051 functions, all
addresses remain fixed, there are no strict-image exclusions, and protected
Game data remains exact.

The subsequent `make -C conker all -j2` generated `conker.us.bin` and stopped
only at the expected final retail-ROM SHA mismatch. There was no compile,
padding, assembly, link, or image-generation failure.

| Artifact | SHA-256 |
| --- | --- |
| Natural 65-word compiler body | `4c8096eb757c0b230a31da2df3f133208aec0c4f5acf819c3afb03056a0fc6ce` |
| Complete linked retail target body | `3f57607ae52c1daef89705b8f1734d7b9f2fb3ed04375506c15e7438e75dde77` |
| Installed semantic owner source | `a9db1dc2bad249737fc997e14963c4c7b973a1a00a9ff3032aa476684c39c74e` |
| Qualified/production owner object | `f95de052012287bb2bf7745eb5b0c2951ebd1d435940a393c8b1959c6c993f42` |
| Predecessor linked ELF | `02716dca0f05d48a92d162e942b29c4fa2a14b5aef5f09b363b6ff711fdbc513` |
| Qualified/production linked ELF | `dfd8b8c969ae9c950ce594c1c1e1a29384f5f1b484e51423ee3a07d367ce9117` |
| Production rebuilt ROM image | `d5607acfb961e993a78a372c6ea08eff04115226206d7f138a51af22f5eba4d3` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Guard table | `7e2c7289a90a0c466356a3165b098ad9fdc7bd970ba4a349963adb1fca0eac9e` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,132 / 5,511 (74.98%)**, zero address drift, 1,379 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,459 / 4,838 (71.50%)**, zero drift, 1,379 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **277 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted ten uncached inputs but
proposed only 24,560 nodes against the retained 58,353-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained at 58,353 nodes / 112,219 links with SHA-256
`0a83de14db03e6dbfeeb3ebf5523e8b5f9f098d4d893e8691aa1ed8b5b61853b`.
No forced refresh was used.

An explicit 13-path incremental rebuild with `force=False` then produced
58,364 nodes, 112,229 links, and 5,093 communities. Against the saved
pre-change snapshot, 58,350 / 58,353 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later. Fourteen IDs were
added: the three relocated headings plus the Note 2062 file and its ten
section headings. The ten-link net addition is confined to the explicitly
re-extracted owner, tools, and documentation. The resulting graph SHA-256 is
`6b3a83a4b028877e7b1a891fc24572acb4ec9825dfe3338cb0542efedd085269`.
A final note-only refresh after recording this section preserved the same
58,364-node / 112,229-link topology and completed clustering normally.

## Continuation

The fresh ranking still begins with the seven documented non-ordinary
boundary cases: handwritten/custom-ABI `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue the ordinary Game queue at `func_15075938` (70
words, 63 real differences). Every next candidate still requires source,
ABI/caller, owner, guest/native, actual Make, complete-image, protected-data,
production recount, documentation, and graph-retention gates before credit.
