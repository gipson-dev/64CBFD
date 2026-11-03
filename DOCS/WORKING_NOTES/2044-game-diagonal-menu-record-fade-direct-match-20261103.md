# Game Diagonal Menu-Record Fade Direct Match

Date: 2026-11-03

## Result

`func_150B709C` now replaces its zero-return placeholder with byte-exact direct
C. Its complete retail slot is **67 words / 268 bytes**, frame `0x00`, VA
`150B709C..150B71A8`, and ROM `0E454C..0E4658`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,114 / 5,511 (74.65%) | 0 | 1,397 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,441 / 4,838 (71.12%) | 0 | 1,397 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **295 more** exact functions.

## Source recovery and direct closure

The callback receives a diagonal menu-entry record. It reads signed progress at
offset `+0x18`. At the terminal progress value 30, it advances the unsigned
opacity byte at `+0x45` by eight times the live timestep `D_800BE9E4`; values
reaching 256 reset to zero. It then advances progress by twice that timestep,
clamps values at or above 31 back to 30, and stores the result. Finally it
derives the record's floating X and Y positions at `+0x2C/+0x30` from the
retail integer projections `(progress * -84) / 30 + 230` and
`(progress * -50) / 30 + 170`.

The recovered source deliberately keeps the opacity load and timestep addition
as separate statements and expresses both screen slopes as negative constants.
That source shape preserves IDO's original register schedule and signed
division setup. The retail leaf has no stack frame, and all **67 words emit
directly from C** with zero guards, insertions, or omissions.

The compact-object payload, with relocation fields unresolved, has SHA-256
`773d5996f50c8bc8cc1733e3ebf5ec83665f5f41f0ceeec29c2b6e6ed4e5a114`.
The linked retail payload has SHA-256
`3d7561b59f27e10330e521fa0d371a77a238cf9216ed7df6587223c665530745`.
The original four relocations are retained: HI16 `D_800BE9E4` at `+0x008` and
`+0x014`, followed by LO16 `D_800BE9E4` at `+0x018` and `+0x03C`.

## ABI, semantic, and production qualification

The function has no direct JAL callers. Its sole aligned pointer literal is at
ROM `0x231500`, callback registry entry `D_8008CA20[8]`. Both dispatch sites
declare and call this table as `void (*)(void *)`: `generated_196DB0.c` uses
`RecordPhaseCallback`, and `game_1944C0.c` carries the same void callback ABI.
The installed definition therefore uses a properly named
`DiagonalMenuRecord150B709C` and returns `void`.

The big-endian guest oracle runs 648 executions across both phase variants and
checks the complete record, live timestep behavior, signed progress, unsigned
opacity rollover, both integer projections, floating stores, and callback
clobbers. It covers every structurally reachable retail word. Eight division
guard words at `+0x8C`, `+0x9C`, `+0xA0`, `+0xA4`, `+0xE4`, `+0xF4`, `+0xF8`,
and `+0xFC` are unreachable by construction because both divisors are the
nonzero constant 30. Native 32-bit O0, O2, and O3 builds pass, while ten
independent behavior-changing controls fail as intended. Thirty-two combined
pre-install regressions passed in 115.397 seconds, followed by a fresh
four-test installed suite in 35.395 seconds.

The complete owner preserves its other twenty functions. Strict
qualified-versus-production comparison retains all 6,051 function addresses,
uses zero exclusions, and reports only `func_150B709C` changed before
installation and no changed function afterward. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `afd7ce8367d30b6114b34a28cb7df335471c1d8bb3b2392e58691d7522b365f6` |
| Installed source | `2993fba73f1a711d6c7182a645033a9ece6a9e9ec8427311955133994cfa810d` |
| Predecessor linked ELF | `1d77d5a61d9078475f2d7eeca2090c3300f2fb9165f1ac59b7eaad75c4b9a524` |
| Qualified/production linked ELF | `4cf04115a373a08db538e8d4f6a6b1e61f95a4d562c06428b7725432620d6d21` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `2da43f2c2acf5fed809fd5e948b1b1342a1a085801a78751b352a33cd7974664` |

The actual production Make rebuilt the owner and linker script, linked
`conker.us.elf`, and generated `conker.us.bin`. It stopped only at the expected
final whole-ROM SHA mismatch while the decomp remains incomplete. Because this
is a direct match and the guard table did not change, no unrelated guarded
owner needed rebuilding.

The permanent candidate generator, strict qualifier, and installed regression
test were committed before production source as tools commits `a44c695`
(`test(game): qualify diagonal menu record fade`) and `a9a9aca`
(`test(game): keep fade production type minimal`).

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,176-node
graph with 112,139 edges and 5,003 communities; visualization was skipped at
the configured 5,000-node limit. The retained/refreshed
`graphify-out/graph.json` is 75,479,930 bytes with SHA-256
`11d1765b8d86a78757ed309ac7d5895f2591427e16cf477f552e2ee55347ade2`.
This is bounded old-node retention evidence, not a full-corpus extraction
claim.

## Continuation

The first three ultra-low ranking rows remain semantic/nonordinary compiler
boundaries, and the seven documented handwritten/custom-ABI boundary cases
remain outside the ordinary queue. Continue at `func_15132A88` (62 words, 61
real differences), followed by the tied `func_1515858C`. Every candidate still
requires source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount, documentation, and graph-retention gates
before credit.
