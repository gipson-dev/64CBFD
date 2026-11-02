# 2002 - Matrix-pair resolver matched as guarded C

Verified 2026-11-02. Production **4,069/5,511 (73.83%)**; Game
**3,396/4,838 (70.19%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,442 different; one existing semantic C function is newly byte-exact.
The active 80% target is **4,409/5,511**, requiring **340 more**. This is
progress toward that goal, not completion.

## Existing semantic source and interface

`s32 func_15031070(u8 *node, u8 *actor, Mtx **primary, Mtx **secondary)`
remains in `conker/src/game/generated_5D2C0.c`. This pass does not replace a
stub or change the complete recursive source recovered in
[Note 1106](1106-game-matrix-pair-resolver-semantic-recovery-20261007.md) and
refined in [Note 1107](1107-game-matrix-pair-bank-phase-and-key-lifetime-fit-20261007.md).

The function resolves a primary/secondary matrix pair through four routes:
an attached matrix bank, a node-owned bank, a keyed recursive parent, or the
actor's default bank. It preserves the established attachment/page rereads,
incoming actor and secondary argument homes, output-alias store order, lazy
failure behavior, recursive offset update, and 32-bit guest address wrapping.

The retail slot is VA `0x15031070`, ROM `0x5E520`, 340 bytes/85 words with a
`0x20` frame. Fresh IDO `-O2 -g3` emits 84 meaningful words; before this pass
the generated-slice padder supplied one trailing zero word and 40 full-slot
word positions differed.

## Guarded compiler match

Nine checked expected-word rows normalize only the remaining compiler lifetime
and scheduling gap. Five substitute branch/key words, one inserts the missing
`move A1,V0`, one omits the compiler's early `li V0,1`, and two move that
success value into retail's recursive branch-delay schedule. The normalized
result is all 85 retail words; the function extent grows from 336 to its full
340-byte slot without moving the following symbol.

The transformation preserves all six symbolic relocation sites. The two
HI16/LO16 pairs for `D_800BE9C0` stay at offsets `0x2C/0x30` and `0x7C/0x80`.
Insertion moves the lookup JAL for `func_1503195C` from `0xC4` to retail
`0xC8`, and moves the recursive self-call from `0xE4` to retail `0xE8`.
Independent rebases of the global, lookup helper and function entry confirm
that the bindings, rather than fixed addresses, are retained.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `f930a85c4640fb0f36cac1750284d15863164fd5d4140010a99dd94a9f6ceb04` |
| Qualified generated owner | `717f411f525b93365de5cc2302afe2923ba990fea6ee93ba6e09bcce164f1d7c` |
| Production/expected linked ELF | `0e1cc15dcf288623c7ad505aad3b4cd4ad8b1af762b5221f90c3578c398b32ca` |
| Predecessor 85-word slot | `3bce84735473b6d019c5ccf1fce00fa628d5247b7e2c91cc8b6b5b5c8ab4e07d` |
| Retail/guarded 85-word slot | `35fc6072ee135716bf0fe7ddf7154f23df68fb1532333e84d01e88a01d6b62ac` |

## Semantic, owner and image qualification

The retained recovery and key-fit suites pass all **22 tests** after
installation. They cover the complete four-route return contract, 2,592 output
aliases, incoming argument-home mutations, lazy faults and partial effects,
recursive chains, the original lookup and matrix-wrapper/helper connection,
native 32-bit controls, 39 owner neighbors, normalized pools, the generated
padder and independently rebased relocations. The three permanent guard/image
tests also pass.

The installed-state padder test exposed one harness-only assumption: its owner
qualification still compared an explicitly supplied candidate against the
class's original isolated object. The test now compiles the candidate it is
actually checking and selects the key-fit source when the nine guards are
installed. Both affected class methods and the complete 22-test suite pass
after that correction. No production source or expected retail word was
changed by the harness fix.

The private complete-image prediction contains 6,051 functions, changes only
`func_15031070`, keeps every canonical address fixed and uses zero strict-image
exclusions. Actual Make reproduced both the predicted owner and expected ELF
byte-for-byte. Protected Game data remains exactly 189,088 bytes across 720
owners with zero different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The shared guard manifest forced a full padded-corpus rebuild. It completed
without stale guards, compiler, padder, assembler or linker failures. `make all
-j2` then generated the development ROM and failed only its expected final
retail SHA-1 check because the wider decomp image is not yet byte-identical.
The linker map remains unchanged at SHA256
`4ceeb40962070eb01cdc286937fdd209862def2bee87dbe33b6f8b7bd6912b38`.

The guard qualification tools were committed first at `7efa9c1`; the installed
padder-test correction is tools commit `704857a`. The retained private stage is
`conker/build/game-matrix-pair-resolver-15031070-match/`. The source was already
counted as converted C, so converted totals do not change. The root README
changes only aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

Graphify's retained graph contains `func_15031070` at
`conker/src/game/generated_5D2C0.c:L421`. The required update extracted 24,070
nodes versus the retained 58,384 and failed closed without `--force`, preserving
31,816 nodes from 3,754 still-existing files outside the reduced scan corpus.
The retained graph SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep
handwritten custom-ABI `func_150A76F0` in its separate assembly workstream and
keep each candidate private until the same ABI, semantic, owner, actual-Make,
whole-image, protected-data, recount, documentation and graph-retention gates
pass.
