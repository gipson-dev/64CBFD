# Game Camera Heading Normalizer Guarded Match

Date: 2026-11-03

## Result

`func_15123070` now replaces its zero-return placeholder with semantic guarded
C. Its complete retail slot is **67 words / 268 bytes**, frame `0x30`, VA
`15123070..1512317C`, and ROM `150520..15062C`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,117 / 5,511 (74.71%) | 0 | 1,394 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,444 / 4,838 (71.19%) | 0 | 1,394 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **292 more** exact functions.

## Source recovery and compiler closure

The routine accepts one camera pointer and updates its target heading. When
`unk6C8` is active and mode `unk6FC` is 10 or 14, it computes the vector from
the camera's `+0x618` point to `+0x2A4`, converts that vector to an angle, and
stores current heading minus the angle at `+0x390`. Otherwise it subtracts the
current heading and 180 degrees from the tracked actor's heading at `+0x40`,
adds 360 degrees until nonnegative, and stores the result. The common tail adds
360 degrees while the stored heading is below -360 degrees.

Retail deliberately keeps the camera pointer in `$a3` across the three-input
vector helper even though the helper does not consume that fourth argument.
The owner therefore uses the established local old-style declaration pattern:
the global typed prototype is macro-hidden only while including `functions.h`,
then the local four-argument call remains visible to the original compiler.
The public declaration for `func_15123070` is independently corrected to
`void func_15123070(struct108 *camera)`.

The selected source emits the retail 67-word control flow and 48-byte frame.
Its natural compact payload differs at twelve independent floating-register
allocation and scheduling words. Twelve checked expected-word rows normalize
only those words at offsets `+0x050`, `+0x054`, `+0x058`, `+0x05C`, `+0x06C`,
`+0x074`, `+0x078`, `+0x080`, `+0x088`, `+0x0E0`, `+0x0E4`, and `+0x0F8`.
There are no insertions, omissions, frame changes, or semantic call guards.

The unresolved compact payload has SHA-256
`db2db668e6374b268754e75b3c95f421c279c075b2dbba2894377d055a4ca160`.
The linked retail payload has SHA-256
`387f279faed3c335c1d2f8f2c4a3f127bda20779bee10bcaaf8476bdc3ffdc31`.
Both original J26 bindings remain semantic: `func_15048F90` at `+0x038` and
`func_15048FC8` at `+0x040`.

## ABI, caller, and semantic qualification

Four true direct JALs call the routine at ROM `0xEBE08`, `0xF5404`,
`0x135504`, and `0x14FA94`, in `func_150BE83C`, `func_150C7E08`,
`func_15107FE0`, and `func_15122440`. Every caller passes one camera pointer
and ignores the return value. Three other raw image words at `0x32E84`,
`0x150424`, and `0x1504D8` equal the same JAL encoding but are instruction or
data collisions, not calls. There are no aligned pointer literals.

The big-endian guest oracle runs **6,002 cases**, including 1,601 special-mode
routes and 4,500 loop-sensitive routes. It covers two stack phases, helper
argument packets, the unused fourth helper argument, helper clobbers, NaNs,
signed zero, and wide heading ranges. All 67 retail words execute across the
corpus. The compact C, padded owner, and retail-linked body produce the same
result and call behavior.

Native 32-bit O0, O2, and O3 UBSan builds pass **588 selected executions**.
Nine independently compiled controls alter the active gate, mode, vector
direction, special arithmetic, tracked field, bias, either loop bound, or loop
step; every control fails as intended. Three source-contract mutations are
also rejected. The complete installed suite passes four tests in 165.276
seconds with no skips.

## Image, data, and production closure

The complete owner preserves all 44 neighboring functions. Strict
qualified-versus-production reconstruction retains all 6,051 function
addresses, uses zero exclusions, and reports only `func_15123070` changed before
installation and no unexpected change afterward. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `72355d28786888bc64ba259578bd51f4e7ad4028a00102d9fe5b7ad5968d7098` |
| Installed source | `bc18876ff45b07d2ff8115ce6670506e548d70d2e12b0ec20b393a83685421a6` |
| Predecessor linked ELF | `fbdbf2afb3437885c26e06b87e6f4d1154c7d1ac795fb2c466741d856b75a297` |
| Qualified/production linked ELF | `0a3565d7fcb4108f007aa41435d322b74c6a53cc2a513a4388e4832bdfc12a51` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `40181c499def3c079e9cb3ed9a0f8eaf1476bb5750e5fe29670430ffb45b606d` |

The actual production Make used the owner's retail `-O2 -g3` profile, rebuilt
the complete guard-dependent object corpus, linked `conker.us.elf`, generated
`conker.us.bin`, and stopped only at the expected final whole-ROM SHA mismatch
while the decomp remains incomplete. The permanent candidate screen, strict
qualifier, guest/native oracle, caller registry, and mutation controls were
committed before production source as tools commit `e404466`
(`test(game): qualify camera heading normalizer`).

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,200-node
graph with 112,162 edges and 5,027 communities; visualization was skipped at
the configured 5,000-node limit. The retained/refreshed
`graphify-out/graph.json` is 75,493,293 bytes with SHA-256
`3dd4d504650a528f4375c5edad8f4442cedd339d8dc2304bec32c29e7dbe8dbf`.
The successful update used Graphify's incremental changed-path mechanism and
no force flag. This is bounded old-node retention evidence, not a full-corpus
extraction claim.

## Continuation

`func_15123070` is fully adopted and removed from the ordinary unmatched queue.
Rerank the remaining ordinary Game functions from the fresh production ELF;
keep the seven documented handwritten/custom-ABI boundary cases outside that
queue. Every next candidate still requires source, ABI/caller, owner,
guest/native, actual Make, complete-image, protected-data, production recount,
documentation, and graph-retention gates before credit. This static and bounded
qualification does not claim full gameplay or hardware acceptance.
