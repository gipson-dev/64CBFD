# Game Random State-Block Replacement Guarded Match (2026-11-04)

## Outcome

`func_1509C120` now replaces its empty placeholder with the semantic random
state-block replacement routine and matches its complete 66-word / 264-byte
retail body. The natural compiler body already has retail's 80-byte frame and
all 12 retail bindings. Seven checked replacement rows normalize one closed
old-block/selected-block register and stack-home cycle without inserting or
omitting an instruction.

This is a source/ABI/caller, raw and padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not live allocator, scene, save-state, or
gameplay acceptance.

## Preserved semantic contract

The first `func_150ADA20()` result selects one of four allocation ordinals
through `& 3`. The routine preserves the previous `D_800D2E4C` value. If that
value is null, replacement always proceeds; otherwise a second random result
must have bit `4` set.

On the replacement path the routine allocates `index + 1` blocks of 27 bytes
with allocator arguments `(0x1B, 0xFF, 2, 0)`. It releases every earlier
decoy in allocation order, keeps the selected final block, and publishes it
through `D_800D2E4C`. When an old block existed, all 27 bytes are copied into
the selected block before the old block is released. The reject path leaves
the old pointer and block bytes untouched.

## ABI, owner, and callers

The recovered ABI is `void func_1509C120(void)`. It consumes no argument
registers and returns no value. Its owner is `conker/src/game_C8950.c`; only
the target placeholder and stale `need a bigger brain` comment are replaced.
The qualifier freezes all 16 neighboring owner functions.

The retail image contains three direct calls and no tail jump or aligned
function-pointer literal:

- ROM `0x34DEC`, from `func_15007830`;
- ROM `0x44C48`, from `func_15017790`; and
- ROM `0xC897C`, from `func_1509B4A0`.

## Compiler normalization

The natural and retail bodies are both exactly 66 words with an 80-byte frame
and 12 relocations. The seven checked differences are:

- offset `0x030` stores the old block in retail's scalar stack slot `0x34`;
- offset `0x0B8` reloads that old block through retail's `t6` lifetime;
- offset `0x0C0` loads the selected block through retail's `t5` lifetime;
- offset `0x0C8` tests the old block through the same `t6` lifetime;
- offset `0x0CC` publishes the selected `t5` value while preserving the
  `R_MIPS_LO16:D_800D2E4C` binding;
- offset `0x0D8` passes the old `t6` value to `bcopy`; and
- offset `0x0E8` reloads the old block from retail's stack slot for release.

Every row checks its expected natural word before replacement. The global
store row additionally checks the expected relocation and preserves the same
symbol binding. There are no inserted words, omitted words, changed branches,
changed calls, or patched semantic constants.

## Qualification and execution

The permanent qualifier was committed first as tools commit `a8c6152`
(`test(game): qualify random state block match`). Its private pre-install
four-test suite passed in 30.796 seconds. The installed-tree rerun passed in
30.707 seconds:

- all 66 words, all 12 bindings, all three direct callers, all 16 owner
  neighbors, and the strict 6,051-function image are closed;
- exactly `func_1509C120` changes, all function addresses remain fixed, and
  there are zero strict-image exclusions;
- 128 guest cases cover all four allocation choices, null/present old-block
  states, reject/replace gates, four byte patterns, and two stack phases;
- every one of the 66 retail words is dynamically reached, with allocator
  arguments, decoy release order, copy-before-old-release order, memory
  effects, stack restoration, and helper-call clobbering checked;
- native 32-bit O0, O2, and O3 builds each pass all 128 cases with
  undefined-behavior checking enabled, for 384 native runs;
- eleven independent semantic controls are rejected; and
- all 264 raw-byte mutations, all seven guard-preimage mutations, and the
  relocation-binding mutation fail closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 6.203 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

The actual production ELF target rebuilt the complete object corpus because
the shared guard manifest changed. It compiled, padded, assembled, and linked
`game_C8950` normally. The installed qualifier reproduced the private result:
exactly `func_1509C120` changes among all 6,051 functions, every address stays
fixed, there are no strict-image exclusions, and protected Game data remains
exact.

The subsequent `make -C conker all -j2` generated `conker.us.bin` and stopped
only at the expected final retail-ROM SHA mismatch. There was no compile,
padding, assembly, link, or image-generation failure.

| Artifact | SHA-256 |
| --- | --- |
| Natural 66-word compiler body | `3503c3a64e8f810e7b3ffd32de5078f6b8ae90df5093187c3d79c96a577b262d` |
| Complete linked retail target body | `75cf82695ce3cb731fa3147b953390fe5fdba0b60eeb197c531559a91b87dd37` |
| Installed semantic owner source | `85b7d65d351e1c598b633fe633413ed5e310a2b2df8cafd19be2ded9e51fb401` |
| Qualified/production owner object | `32b0f69648cb4bcba880ccbbd001f01d2f7fb4483451eada970d5db97e8f1eab` |
| Predecessor linked ELF | `1509455ede335a43d049b5a96fa6eff2c3018862ba11a9b4ab64904ff816ca37` |
| Qualified/production linked ELF | `f2cf11e6d78671d76757ac9ce232723b540bdb28156007f197e9fd22d51c4cd3` |
| Production rebuilt ROM image | `9667cd3fa05c189d473524e75f20fb7b13a5f2fac3a03d1415cc8f06a719db2a` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Guard table | `83381963e8870d89f72b318b9890fe0941e90c48da48e548b15381ed24069628` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,134 / 5,511 (75.01%)**, zero address drift, 1,377 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,461 / 4,838 (71.54%)**, zero drift, 1,377 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **275 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,582 nodes against the retained 58,375-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained at 58,375 nodes / 112,238 links with SHA-256
`0c45455920147a5d4f3660fe5107071c307bce75e153a8fcd1a567e13bfe96b4`.
No forced refresh was used.

An explicit 13-path incremental rebuild with `force=False` then produced
58,386 nodes, 112,247 links, and 5,058 communities. Against the saved
pre-change snapshot, 58,372 / 58,375 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later. Fourteen IDs were
added: the three relocated headings plus the Note 2064 file and its ten
section headings. The nine-link net addition is confined to the explicitly
re-extracted owner, tools, and documentation. The explicit-refresh graph
SHA-256 is
`a1fdbbd855e16b3b1e72b86725ded888ad21873584ae9d663eb6dc68ac2657ea`.
A final note-only refresh after recording this section preserves the same
58,386-node / 112,247-link topology and completes clustering normally.

## Continuation

The fresh ranking still begins with the seven documented non-ordinary
boundary cases: handwritten/custom-ABI `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue the ordinary Game queue at `func_150C84F4`
(67 words, 63 real differences). Every candidate still requires source,
ABI/caller, owner, guest/native, actual Make, complete-image, protected-data,
production recount, documentation, and graph-retention gates before credit.
