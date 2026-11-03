# Game Table-Driven Effect Constructor Guarded Match (2026-11-03)

## Outcome

`func_151DA6F8` now matches its complete 144-word / 576-byte retail body and
0xD0-byte frame. The semantic constructor restored in
[Note 1149](1149-game-table-driven-effect-constructor-restoration-20261009.md)
is unchanged; 61 expected-word guards normalize only the remaining closed IDO
register-allocation, local-placement, and scheduling differences. All ten
relocations remain valid and the linked function is byte-exact.

This is a source/ABI review, raw and padded owner, caller, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not live gameplay, renderer, effect-system, or
hardware acceptance.

## Preserved semantic contract

The function retains all 18 mixed O32 arguments and the four recovered local
records from Note 1149. It prepares the 28-byte request, 32-byte descriptor,
12-byte payload, and consumed 32-byte render prefix; derives descriptor and
call flags from the three 16-entry tables; calls `func_15147DA0` with all 15
argument words; returns null without touching the payload destination; and on
success copies the complete 12-byte payload through the created object's
`+0x98` pointer to offset `+0x48`, preserving the original created pointer
instead of `memcpy`'s return value.

The selected source continues to preserve unspecified record padding rather
than inventing a larger render tail or zero-filling bytes the retail routine
does not define. Screening a later kind load reduced the natural mismatch from
61 to 59 words, adding a volatile payload reduced it to 57, and record-order
permutations did not improve the result. A speculative 48-byte render object
changed the frame to 0xE0 and worsened the body. None of those fitting forms
was installed.

## Guards, bindings, and callers

The natural owner already has the correct 144-word length, 0xD0 frame, saved
register lifetime, control flow, helper calls, and returned-pointer behavior.
The 61 guarded words form four closed compiler-layout groups:

- table-address and register allocation from `+0x094` through `+0x130`;
- payload, render-prefix, and stack-local placement from `+0x148` through
  `+0x1D0`;
- outgoing argument allocation at `+0x1F8`, `+0x1FC`, and `+0x204`; and
- result preservation and payload-copy scheduling from `+0x208` through
  `+0x218`.

All rows are fail-closed against the exact natural word. Relocation-aware rows
move the descriptor-table `D_800AB3F4` HI16/LO16 pair from natural offsets
`+0x0D0/+0x0F8` to retail offsets `+0x094/+0x0F4`; the other eight bindings
stay at their natural offsets: `D_800AB404` at `+0x080/+0x0AC`,
`D_800AB330` at `+0x090/+0x0CC`, `D_800AB498` at `+0x0B0/+0x0B4`,
`func_15147DA0` at `+0x200`, and `memcpy` at `+0x220`.

The five direct linked callers remain unchanged:

- `func_15135DD0` at `0x15136210`;
- `func_15136F50` at `0x151373B4`;
- `func_15153CCC` at `0x15153EC8`;
- `func_15153F18` at `0x15154168`; and
- `func_151C577C` at `0x151C5A30`.

An independent ROM JAL-pattern scan finds eleven bit-pattern candidates and no
aligned pointer literals; only the five symbol-qualified ELF calls above are
claimed as callers.

## Qualification and execution

The permanent qualifier was committed first as tools commit `fb28845`
(`test(game): qualify trail effect constructor match`). It adds
`tools/experiments/game_trail_effect_constructor_guard_match.py` and
`tools/tests/test_game_trail_effect_constructor_guard_match.py` and extends
the existing recovery oracle without changing production source.

The final pre-install five-test run passes in 52.457 seconds. The installed
production run passes the same five tests in 74.467 seconds:

- strict owner, linked-image, caller, and protected-data closure;
- all 61 checked raw words and relocation transitions producing one exact
  144-word linked body;
- 1,040 guest cases / 2,080 natural-and-retail executions covering all 144
  words, both stack phases, allocation failure/success, aliases, helper
  clobbers, and payload mutation;
- twelve separately compiled semantic controls, each failing for its intended
  contract change; and
- 32-bit O0, O2, and O3 native builds, each passing 4,096 cases.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 12.316 seconds. The target owner has 61 checked
neighbors, and the strict image compares all 6,051 functions with only
`func_151DA6F8` changing from the predecessor, every address fixed, and zero
exclusions. Protected Game data remains exact at `0x80082760`: 189,088 bytes
across 720 owners, zero different bytes or owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

Because the shared guard manifest changed, the actual `make -C conker all -j2`
recompiled every padded owner. It completed compilation, assembly, padding,
linking, and binary generation, then stopped only at the expected final retail
ROM SHA mismatch. The rebuilt ELF and mixed owner reproduce the independent
pre-install predictions exactly; no compile, assembly, padding, or link error
occurred.

| Artifact | SHA-256 |
| --- | --- |
| Natural compact owner object | `ee54d337ae9f2e82885f8f850fd5fa4deb6b864720e55f6c96e4c44508248df2` |
| Complete linked retail target body | `8243c037cb292d533731712cb67e82e1e559c3bae1911b22fa03734cadf99811` |
| Relocation-normalized retail owner | `f23328c957d8162cacd943eb60ab69bc9e2c307847f8bf95d116345c361061e9` |
| Unchanged semantic owner source | `f0e096816c0414498b58bc39260a553c196898eb06f04ea106d0317d6a6df1a4` |
| Qualified/production owner object | `fcddc62a71529a1d2ec8c71fb684034cb73bcb6756203db65a58fc55c87c5a22` |
| Predecessor linked ELF | `069120cef62c648808f2d9dbe9d6347d42d952cb74c8d3e9a5f501738e3980ca` |
| Qualified/production linked ELF | `0abc440198d59385cea1558814510a4c592e87efa616c3a9ef342ed3945dc751` |
| Production rebuilt ROM image | `ccf1c763bff26e1decab3f8f293d2e8da8a5b69dd6fe35235662cb33b6037768` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `37538a37cf08f000a7dacabb8f46abaeda51504a327901073ad6fa28ff5e8f16` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,126 / 5,511 (74.87%)**, zero address drift, 1,385 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,453 / 4,838 (71.37%)**, zero drift, 1,385 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **283 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,498 nodes against the retained 58,292-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. No forced refresh was used.

An explicit nine-path incremental rebuild with `force=False` then produced
**58,302 nodes, 112,246 edges, and 5,101 communities**. Against the saved
pre-change snapshot, **58,289 / 58,292** old node IDs were retained; three
line-number-derived `DOCS/UPDATE_LOG.md` IDs were replaced and 13 IDs were
added, including all ten headings in this note. The resulting `graph.json` is
75,536,506 bytes with SHA-256
`77ff75c1cb648844f4ded34d4b911f41588e6abf57a5db637fa965bb1c47a584`.

## Continuation

The fresh ordinary queue starts with `func_1504A620` (68 words, 62 real
differences), followed by `func_15172D80`, `func_1519E1F4`, and
`func_151DE6D4` in the same 62-difference tier. The seven smaller documented
handwritten/custom-ABI entries remain in their separate lane. Every next
candidate still requires source, ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
