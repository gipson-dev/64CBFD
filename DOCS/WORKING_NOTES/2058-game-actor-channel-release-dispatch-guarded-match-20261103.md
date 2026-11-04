# Game Actor-Channel Release Dispatch Guarded Match (2026-11-03)

## Outcome

`func_15172D80` now replaces its zero-return placeholder with the semantic
actor-channel release dispatcher and matches its complete 63-word / 252-byte
retail slot. The natural IDO body has the correct control flow, calls,
relocations, saved-register lifetime, and return paths. Two fail-closed rows
normalize only the compiler's 64-byte stack frame to retail's 56-byte frame;
all other 61 words emit directly from C.

This is a source/ABI/caller, raw and padded owner, guest/native execution,
strict whole-image, protected-data, production-build, recount, and graph-
retention result. It is not live gameplay, renderer, audio, or hardware
acceptance.

## Preserved semantic contract

The function accepts a promoted signed channel index. It reads the signed
selector from `D_800DD2B0[channel]` and returns immediately when that selector
is `-1`. Otherwise it selects the corresponding `D_800CC2D0` actor record.
When the actor's health byte is zero, it clears the selector and submits the
six-argument channel-release event through `func_1517EE40`.

The channel is then tested through `func_1517F40C`. An inactive channel exits.
An active channel whose selector differs from `D_800BE9F0` dispatches
`func_1501C730(1, selector, 0, 0, 0)` and returns. The matching-selector route
calls `func_15172CA8(channel)` and applies the pending unsigned byte from
`D_800DD2C0[channel]` to the actor through `func_15172D28`. Correcting the
declaration of `D_800DD2C0` from signed to unsigned is required by the retail
`lbu` and by payload values `0x80` through `0xFF`.

## ABI, caller, owner, and guards

The recovered ABI is `void func_15172D80(s32 channel)`. The only direct retail
caller is `func_15018F80(s16)` in `conker/src/game_45B80.c`, at ROM offset
`0x464E8`; it promotes its signed halfword argument into `a0` and ignores the
return value. The owner audit preserves four neighboring functions and all 13
target relocations.

The natural compiler frame is `0x40`; retail uses `0x38`. Checked rows at
function offsets `+0x000` and `+0x0F0` replace only the stack allocation and
restoration immediates. Both rows require their exact compiler preimages and
therefore fail closed if the source or compiler layout changes. No semantic
instruction, relocation, delay-slot operation, or compiler word is omitted.

## Qualification and execution

The permanent qualifier was committed first as tools commit `1f7e730`
(`test(game): qualify actor channel release match`). Its four-test suite passes
in 52.097 seconds:

- all 63 retail words, both checked guards, all 13 relocations, four owner
  neighbors, the sole caller, and the strict 6,051-function image are closed;
- 1,152 guest cases across stack phases zero and eight cover every retail word,
  every control-flow route, and unsigned payload edge values `0x80` and `0xFF`;
- native 32-bit O0, O2, and O3 builds each pass 576 cases with UBSan;
- ten independent semantic controls are rejected; and
- all 252 raw-byte mutations plus both guard-preimage mutations fail closed.

The shared match-progress, guarded-object, generated-PC16, and protected-data
suite passes all 19 tests in 10.590 seconds. Protected Game data remains exact
at `0x80082760`: 189,088 bytes across 720 owners, zero different bytes or
owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Production closure and frozen evidence

Changing the shared guard manifest invalidated every padded C owner, so the
actual production ELF target rebuilt the complete padded corpus. Compilation,
padding, assembly, and linking all completed without a guard-preimage or owner
failure. The subsequent `make -C conker all -j2` generated the ROM image and
stopped only at the expected final retail-ROM SHA mismatch.

| Artifact | SHA-256 |
| --- | --- |
| Natural 63-word compiler body | `282b43219ba5e54b219debc904e6ec17e711d577375df9254f06b84ca2c75f2b` |
| Complete linked retail target body | `599bac44ac0733f5129d617f0349d5bc470026efee412dcb9ae66dcb2d60df7e` |
| Installed semantic owner source | `ce7f7d7293566a38e82c3172120562820ef4af5317a0066b6d0f05a28ac3ae8b` |
| Qualified/production owner object | `1d26201bf8590170003179b9bd694243afb918be553538f6faff989b8ee6c199` |
| Predecessor linked ELF | `b455dfc321bb762f5ea37cbc347cf03cd5af38c70aa1a45d1bf8ba54d1700da7` |
| Qualified/production linked ELF | `d620d4aefe4e6c6b7848f6888d17e9e36368dbac9a80ebcd19e71c43537e3067` |
| Production rebuilt ROM image | `8b5fc88e390aecdbaca0907e07eb599cab8914c2fe6a0f12ca3114c45908833c` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `f2b66960ae84646edff18e3da5e603689d36b0beef32a71482265b4036bd025e` |
| Aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,128 / 5,511 (74.90%)**, zero address drift, 1,383 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,455 / 4,838 (71.41%)**, zero drift, 1,383 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **281 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted nine uncached inputs but
proposed only 24,519 nodes against the retained 58,313-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph SHA-256 remained
`5a37ae99d759982bd636ca18eeb80f9f476c495b513187d78544ae9edfa52412`.
No forced refresh was used.

An explicit 12-path incremental rebuild with `force=False` then produced
58,323 nodes, 112,224 links, and 5,199 communities. Against the saved
pre-change snapshot, 58,310 / 58,313 old node IDs were retained. The three
replaced IDs are line-number-derived `DOCS/UPDATE_LOG.md` headings, and each
has one uniquely relocated replacement two lines later; 13 IDs were added for
the Note 2058 file and its section headings. A final one-path refresh after
recording this section retained **58,323 nodes and 112,224 links**, and its
clustering pass completed normally.

## Continuation

Continue the ordinary Game queue at `func_1519E1F4`, followed by
`func_151DE6D4` in the same prior difference tier. The seven documented
handwritten/custom-ABI boundary cases remain in their separate lane. Every
next candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
