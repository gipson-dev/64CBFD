# Game Owner-Link Callback Direct Match (2026-11-03)

## Outcome

`func_1519E1F4` now replaces its zero-return placeholder with the semantic
owner-link event callback and emits its complete 68-word / 272-byte retail
body directly from C. The recovered body has the retail 24-byte frame, all
three helper-call relocations, the original branch-likely layout, and zero
positional word differences. No retail-word guards or inserted assembly words
are required.

This is a source/ABI/callback-table, raw and padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not live gameplay, renderer, audio, or hardware
acceptance.

## Preserved semantic contract

The recovered ABI is
`void func_1519E1F4(u8 *record, s32 eventAddress, u8 command)`. The function
loads the bound link through the pointer at record offset `0x98` and treats the
second argument as the event-record address.

Commands zero and seven compare either the first 32-bit identity word or the
identity byte at offset four. A match calls `func_1519CFA0(record)`. Command
six compares the event's first byte against the link byte at offset `0x4C` and
calls the same helper when equal. Command `0x2D` retargets the link in either
direction: when the event's before pointer is current it installs the after
pointer and byte nine; when the after pointer is current it installs the
before pointer and byte eight. All other commands leave the record unchanged.

The byte-oriented declarations are intentional. They preserve the retail
unsigned command promotion and the overlapping identity/category bytes used
by the callback record. A more conventionally typed candidate changes ten
retail words; the selected byte-oriented source shape changes none.

## ABI, owner, and callback registration

The callback has no direct `jal` callers. Its address occupies
`D_8008A390[4]` at ROM pointer `0x22EE60`, and `func_15147D1C` dispatches it
through that table. The owner is
`conker/src/game/generated_1CA420.c`; qualification preserves 22 neighboring
functions and all non-target bytes. The target contains three `R_MIPS_26`
bindings to `func_1519CFA0`, at body offsets `+0x40`, `+0x6C`, and `+0xA8`.

The natural compiler body and the linked retail body are each 68 words with a
24-byte frame and zero positional differences. The installed guard table is
unchanged because the compiler output needs no normalization.

## Qualification and execution

The permanent qualifier was committed first as tools commit `bc45157`
(`test(game): qualify owner link callback match`). Its four-test suite passes
in 45.900 seconds:

- all 68 retail words, all three helper bindings, 22 owner neighbors, the
  callback-table registration, and the strict 6,051-function image are closed;
- 192 guest cases across stack phases zero and eight exercise commands zero,
  six, seven, `0x2D`, and unrelated values, all three pointer relations, and
  both identity/category comparison routes;
- 65 / 68 words are dynamically reachable; the three retail branch-likely
  shadow words at `+0x7C`, `+0xB8`, and `+0xE8` are statically exact and are
  explicitly excluded from the dynamic-coverage claim;
- native 32-bit O0, O2, and O3 builds each pass 96 cases;
- ten independent semantic controls are rejected; and
- all 272 raw-byte mutations plus three relocation-binding controls fail
  closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 6.956 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

The actual production ELF target compiled, padded, assembled, and linked the
changed owner successfully. The installed qualifier then reproduced the
private qualification result. The subsequent `make -C conker all -j2`
generated the ROM image and stopped only at the expected final retail-ROM SHA
mismatch.

| Artifact | SHA-256 |
| --- | --- |
| Natural 68-word compiler body | `8cbc37ae0e1bc2af2c29e86ddcee59bbdee74773b28c88514cf182104b616d45` |
| Complete linked retail target body | `3c5ce5d05c1c92beafacecfd31678146fa0cdd7884a11e3e7b558f92c3245cec` |
| Installed semantic owner source | `9e8aef7db102fbd4dbe1b4b2f5eccf54a7e715330132b810a430d2027cbcb418` |
| Qualified/production owner object | `030a2078f76f1eda2cd2694d7ed0a08478fbeaffd8b3e518d06605d6b2de20f0` |
| Predecessor linked ELF | `d620d4aefe4e6c6b7848f6888d17e9e36368dbac9a80ebcd19e71c43537e3067` |
| Qualified/production linked ELF | `5af028bdaf09038c9d3f51423bbbec0db4601575a87d5e78c197457bc63b4e81` |
| Production rebuilt ROM image | `35606c23963c208a0485061dff0766d8ed140458cde9f5a5eab0cf4b530a5e26` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged guard table | `f2b66960ae84646edff18e3da5e603689d36b0beef32a71482265b4036bd025e` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,129 / 5,511 (74.92%)**, zero address drift, 1,382 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,456 / 4,838 (71.43%)**, zero drift, 1,382 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **280 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,529 nodes against the retained 58,323-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph SHA-256 remained
`3e319af7d4ace44c9530c9bce2e37580e1ae411f256120d69d0cfe59e2846d40`.
No forced refresh was used.

An explicit 11-path incremental rebuild with `force=False` then produced
58,333 nodes, 112,234 links, and 5,107 communities. Against the saved
pre-change snapshot, 58,320 / 58,323 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later; 13 IDs were added for
the Note 2059 file and its section headings. The resulting graph SHA-256 is
`343ebd6bef4422a930bbb1a3306c749c09021b4591e5e25aec1a050a97f865b2`.
A final note-only refresh after recording this section preserved the same
58,333-node / 112,234-link topology and completed clustering normally.

## Continuation

Continue the ordinary Game queue at `func_151DE6D4`. The seven documented
handwritten/custom-ABI boundary cases remain in their separate lane. Every
next candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
