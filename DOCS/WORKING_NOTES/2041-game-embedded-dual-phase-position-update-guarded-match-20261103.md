# Game Embedded Dual-Phase Position Update Guarded Match

Date: 2026-11-03

## Result

`func_151B1828` now replaces its zero-return placeholder with byte-exact
guarded C. Its complete retail slot is **60 words / 240 bytes**, frame `0x30`,
VA `151B1828..151B1918`, and ROM `1DECD8..1DEDC8`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,111 / 5,511 (74.60%) | 0 | 1,400 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,438 / 4,838 (71.06%) | 0 | 1,400 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **298 more** exact functions.

## Source recovery and guarded closure

The recovered callback takes one state pointer and keeps two phase bytes at
`state+0x120/+0x121`, with signed rates at `+0x122/+0x123`. Each phase advances
with its own live read of `D_800BE9E4` and wraps naturally to eight bits. Both
wrapped phases are shifted by `-0x40` and sampled through `func_151423D8`.

The parameter block begins at `state+0x110`. Its two base coordinates are at
absolute offsets `+0x124/+0x128`, and its two sample scales are at
`+0x12C/+0x130`. The callback computes both targets, then eases the current
planar coordinates at `state+0x2C/+0x30` halfway toward those targets. It
returns one so the callback remains active. This is the same field layout and
behavioral topology as the independently qualified `func_15190F9C`, while the
registry and owner evidence below establish this routine as its own callback.

IDO naturally emits all semantics in 60 words but selects frame `0x20`,
different local homes, and the opposite commutative operand order for two
floating additions. Nine checked positional rows close only those compiler
layout choices:

| Raw offset | Compiler word | Retail word | Qualified action |
| ---: | ---: | ---: | --- |
| `0x000` | `27BDFFE0` | `27BDFFD0` | Use retail's 48-byte frame. |
| `0x05C` | `AFA50020` | `AFA50030` | Move the owner-pointer home with the frame. |
| `0x060` | `8FA50020` | `8FA50030` | Reload the owner from its retail home. |
| `0x064` | `E7A00018` | `E7A00024` | Move the first trigonometric sample home. |
| `0x088` | `C7A60018` | `C7A60024` | Reload that sample from its retail home. |
| `0x08C` | `8FA50020` | `8FA50030` | Reload the owner after the second helper call. |
| `0x0BC` | `46022180` | `46041180` | Preserve retail's first commutative-add operand order. |
| `0x0DC` | `460C3200` | `46066200` | Preserve retail's second commutative-add operand order. |
| `0x0EC` | `27BD0020` | `27BD0030` | Restore retail's frame size. |

Every row checks its expected compiler word and fails closed when stale. The
clock HI16/LO16 bindings remain at offsets `0x004/0x008`, and the two J26
bindings for `func_151423D8` remain at `0x058/0x07C`. The unqualified compact
body has SHA-256
`b5c046431d39dd4c77a3bc03aca9f5851056df1fe2c969c0f28391a8fad73928`;
the qualified retail body has SHA-256
`6b4ac0b0f10c883b55eabac9151fa77e5e24d00cd3589e6483245a3eb6a0fcda`.

## Semantic, registry, and production qualification

The big-endian guest oracle runs 2,752 cases covering signed positive and
negative rates, eight-bit wrapping, independent live clock reads, both helper
callbacks, callback clobbers, and both smoothing outputs. Every one of the 60
retail words is covered. Native 32-bit O0, O2, and O3 builds and ten independent
behavior-changing controls pass. The three focused tests and 19 shared
progress, Game-data-layout, generated-PC16, and guarded-padder tests all pass:
22 installed tests in 38.751 seconds. Nine stale-row mutations prove every
guard is effective.

There are no direct JAL callers. The sole aligned pointer literal is at ROM
`0x22E7BC`, callback entry `D_80089CB8[17]`. The complete 16-function owner
preserves the other 15 functions. Strict qualified-versus-production
comparison retains all 6,051 function addresses, uses zero exclusions, and
reports only `func_151B1828` changed before installation and no changed
function afterward. Protected Game data remains exact at 189,088 bytes across
720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `f3bd9c1d20dca1272a79cd09cb6311fdf360498c08a1e650a1743908fc533515` |
| Installed source | `21de3d8a02559d4d4e10c6746e92568132291fe4aba0e733bb6d303f6665e23d` |
| Predecessor linked ELF | `90127236eafbc92c3ce2d04987ad559ec8618ad62f0084184145c2f9bae45d9b` |
| Qualified/production linked ELF | `c48ba070872f8a762f56a9a5a1ea26ae2904e306717ad2f3c4df7249a4d4996d` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `b266a98dc5e0ee31789c96ff5024a00cc4c1a5a34d40eda1c736dc0a143501f9` |

The actual `make all -j4` rebuilt the complete guarded corpus, regenerated the
linker script, linked `conker.us.elf`, and generated `conker.us.bin`. Every
existing guard remained valid. The build stopped only at the expected final
whole-ROM SHA mismatch while the decomp remains incomplete.

The permanent qualifier and evidence tools were committed first in the tools
submodule as `f9f7fee` (`test(game): qualify embedded dual phase update`).
Production source and the nine checked rows were installed only after that
tools commit.

## Graph retention

The required bounded Graphify update proposed 58,383 nodes versus the retained
58,384 and refused to overwrite without `--force`. Its fail-closed pass also
reported retention of 31,816 nodes from 3,754 still-existing files outside the
reduced scan corpus. The retained `graphify-out/graph.json` remains 77,250,386
bytes with 120,179 links and SHA-256
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

The fresh ranking begins with seven documented non-ordinary boundary cases:
handwritten/custom-ABI `func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, and `func_150A6760`.
Continue the ordinary direct-C queue at `func_151B9214` (63 words, 60 real
differences). Every candidate still requires source, ABI/caller, owner,
guest/native, actual Make, complete-image, protected-data, production recount,
documentation, and graph-retention gates before credit.
