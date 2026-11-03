# 2014 - Menu record submitter matched as guarded C

Verified 2026-11-02. Production **4,082/5,511 (74.07%)**; Game
**3,409/4,838 (70.46%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,429 different; one zero-return placeholder is replaced by qualified
semantic C and is newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **327 more**. This is progress toward that goal, not completion.

## Recovery and interface

`func_151E2404` is the 59-word, frame-zero menu record submitter in
`conker/src/game/generated_20AE20.c`. Its retail address is `0x151E2404` and
its ROM offset is `0x20F8B4`.

The routine reads the selected menu slot from `D_8008FDD4[0x42]`, uses that
signed byte to select the ten-byte index in `D_800AB690`, and addresses the
corresponding ten-byte destination record in `D_80082BBC`. It copies the
common settings bytes into destination offsets 0, 1, 2, 3, 4, 8 and 9. The
source mode then controls the remaining payload: mode 0 copies source byte 4;
modes 1 and 2 copy bytes 13 and 14; modes 5 and 7 copy byte 18; and modes 8
and 9 copy bytes 7 and 19. Every path finishes through `func_150076A0()`.

The source pointer is deliberately `volatile s8 *`. Retail keeps its source
base live and performs the byte reads in program order; removing the volatile
qualification rematerializes that base, expands the body to 67 words, and no
longer represents the retail access schedule. The sole original caller at ROM
offset `0x20DF6C` validates the no-argument, void-return O32 contract.

## Guarded compiler closure

IDO naturally emits the complete 59-word extent, frame-zero interface,
switch branches and delay slots. The owner's Make rule binds its generated
switch relocation to the original `jtbl_800AB9BC` anchor.

Twenty words differ from retail at offsets `0x004`, `0x008`, `0x01C`,
`0x034`, `0x038`, `0x03C`, `0x040`, `0x044`, `0x054`, `0x05C`, `0x064`,
`0x06C`, `0x08C`, `0x098`, `0x0A0`, `0x0AC`, `0x0B8`, `0x0C0`, `0x0C8`
and `0x0D0`. Together they form one complete closed `a0`/`v1` compiler
allocation and scheduling cycle. Twenty checked expected-word replacements
normalize only that cycle. The jump-table relocations at offsets `0x078` and
`0x080` remain ordinary relocations and are not guards. Two independent
rebases reproduce every expected linked word, while expected-word and
expected-relocation mutations produce 40 fail-closed cases.

| Artifact | SHA-256 |
| --- | --- |
| Raw candidate object | `2f1ec12e9d1b087eac52752be807e2bcdfc74726cf87c14f4b51cf5657e22d78` |
| Isolated guarded object | `d3d2583d6148bd970b725fef3c59f89d8db8ec66755f69662a1f8cb9b04db015` |
| Isolated guard manifest | `7954b81d3d6b478b21ebf2bfc7ccee3a2f4778e066e84b0b5802ff91992916ec` |
| Qualified/production owner | `ed18e713851dfc7cbd56deb7c6e5b21c6d15c263efe4d3bb39305702a88d4e29` |
| Qualified/production linked ELF | `28d455714328d1ee63465f132a83cd9030ea194596ad60604cc15e7e5efea8b7` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Production guard table | `af513653e0b1af0e4ee85a6d1fa8f8c44724f988904f0f56ebe54699baa1beed` |

## Semantic, owner and image qualification

Five permanent tests pass. Twenty-eight guest fixtures execute retail, raw
candidate and guarded programs for 84 executions and cover all 59 words. They
exercise every switch class, signed menu and record indices, aliased source
and destination storage, and the final submit call. Native O0/O2/O3 controls
run 168 cases against the selected implementation and seven effective
negative variants, for 4,032 executions; every negative control is rejected.
The original caller contract, all 40 stale-guard mutations, both independent
rebases and the owner's non-target neighbors pass.

The qualified owner is byte-identical to the production
`generated_20AE20.c.o`. Strict whole-image prediction proves that every
allocated byte is the literal one-slot prediction and that every address stays
fixed. Adding the recovered external references changes only non-allocated
`.symtab`/`.strtab` row ordering; the symbol-name inventory and semantic
symbol fields remain unchanged except for the target's recovered size. The
production full-corpus rebuild and link reproduce the qualified owner and ELF.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The permanent experiment and qualification suites were committed first in the
tools submodule as `0f613b0`. The retained qualification stage is
`conker/build/game-menu-record-submit-151E2404-guard-match/`. This is
instruction-level and bounded semantic proof, not natural whole-game or
gameplay acceptance. The root README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,146 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep every
new candidate private until source, ABI/callers, owner, guest/native, actual
Make, complete image, protected-data, production recount and documentation
gates pass.
