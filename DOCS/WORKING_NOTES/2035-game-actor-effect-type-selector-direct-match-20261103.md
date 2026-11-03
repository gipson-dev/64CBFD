# 2035 - Actor effect-type selector matched directly from C

Verified 2026-11-03. Production is **4,105/5,511 (74.49%)**; Game is
**3,432/4,838 (70.94%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,406 functions remain different. The active 80% target is
**4,409/5,511**, requiring **304 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_15134070` replaces its zero-return placeholder in
`conker/src/game_161520.c`. It maps an actor identity to the point/effect
descriptor type used by the surrounding actor-effects system. The routine is
at VA `0x15134070`, ROM `0x161520`, owned by `game_161520`, and occupies 63
words with no stack frame. Its recovered interface is
`s32 func_15134070(u8 *actor)`; the only memory access is the unsigned identity
byte at `actor + 0x04`.

The mapping returns categories 0 through 19 for the defined actor identities
and 99 for all other byte values. The result classes are:

| Result | Actor identities |
| ---: | --- |
| 0 | `00, 01, 02, 03, 04` |
| 1 | `11, 14, 3B` |
| 2 | `5A, 5F, 74, 75, 7A` |
| 3 | `58, 5B, 80` |
| 4 | `16, 88, 90` |
| 5 | `9C` |
| 6 | `9D` |
| 7 | `96` |
| 8 | `A0` |
| 9 | `9F` |
| 10 | `47` |
| 11 | `34` |
| 12 | `98` |
| 13 | `10, 38, 91` |
| 14 | `87, B0` |
| 15 | `B1` |
| 16 | `B4` |
| 17 | `70, B2` |
| 18 | `AB` |
| 19 | `9A` |

There are ten direct JAL callers at ROM offsets `0x102FAC`, `0x164138`,
`0x164D04`, `0x16608C`, `0x166154`, `0x1C1AE0`, `0x1C1FD8`, `0x1DD6E4`,
`0x1DDEBC`, and `0x1E21A4`. Retail contains no aligned function-pointer
literal to this entrypoint.

## Natural compiler and table closure

The readable signed-`s32` switch naturally emits all 63 retail words under the
owner's retail `-O2 -g3` profile. It needs no expected-word guards, inserted or
omitted instructions, compiler patches, or source distortions. Eight screened
inline/local-declaration and `-O2`/`-O2 -g3` controls independently produce the
same complete code and table bytes. A `u32` local changes one instruction;
`u8` locals and the `-O1` profiles diverge more broadly.

The compiler emits two fixed jump tables: 129 entries for identities 52
through 180 at `jtbl_800A4350_game`, followed by 23 entries for identities 0
through 22 at `jtbl_800A4554_game`. Their complete 608-byte pool is exact. The
four HI16/LO16 relocations at function offsets `0x1C`, `0x24`, `0x3C`, and
`0x44` are bound by the production owner to the original Game-data table pool;
the padded owner contains no duplicate `.rodata`.

All other functions and normalized pools in `game_161520` remain unchanged.
Across the linked image, only `func_15134070` changed before installation, all
6,051 function addresses remained fixed, and strict comparison used zero
exclusions. After installation, the qualified and production ELFs are
byte-for-byte equal.

| Artifact | SHA-256 |
| --- | --- |
| Natural/retail linked 63-word payload | `87c6650f4d53ddcc1a52b24bcf502d38175637e9f42275f90d9046895338e5a6` |
| Qualified/production owner | `3dff694c94ebe0cdefca73344a0ba227a8f357a7c19275f8c7caee06056a7c5e` |
| Predecessor linked ELF | `4c8c817a25b56fe734a8cfaec6bfdd74509dfed2658e7c9dac5352410d2e8512` |
| Qualified/production linked ELF | `bbbca2e0262e350af9c1d4e312bba8aee38ec189302938413ba2892121a4b46c` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `bf7cafc8aa350f10fb98d59868e260a39e3f64f357740e0a07c5beea9972f935` |

## Semantic and production qualification

The big-endian guest oracle executes every one of the 256 identity bytes over
four actor alignments, four poison patterns, and two stack phases: 8,192 cases
for both candidate and retail. Both cover all 63 words, perform exactly one
byte read at offset four, make no calls, and perform no writes. Native 32-bit
O0/O2/O3 builds each execute 16,384 cases against the actual installed source
with mutation checks. Six independently compiled controls reject a placeholder,
a signed-byte load, a wrong field offset, a missing high identity, a wrong
category, and a wrong default.

The six focused tests pass against the installed production source, owner and
ELF in 55.315 seconds. The 19 shared progress, complete Game-data-layout,
generated-PC16 and guarded-padder tests pass in 8.770 seconds. The caller
census, fixed tables, owner diagnostics, table binding, source state, strict
whole-image prediction and installed-state coherence are checked explicitly.
Protected Game data remains exact at 189,088 bytes across 720 owners, zero
different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` rebuilt the production corpus, regenerated the linker
script, linked the ELF and generated the binary. It stopped only at the expected
whole-ROM SHA mismatch while the decomp remains incomplete. A fresh independent
production recount credits exactly this function.

The older standalone actor-point-effects test could not be rerun after the
prior build cleanup removed its archived input-snapshot fixture. This selector
qualifier independently recompiles and verifies that override object; the
earlier actor-point-effects note remains its connected proof. The unavailable
archived test is not counted among the 25 passing tests above.

The qualifier and permanent tests were committed first in the tools submodule
as `7578874`. This is instruction-level and bounded semantic proof, not natural
whole-game or gameplay acceptance. The README changes only its aggregate
byte-exact rows. No Claude call was needed.

## Graph retention

The required bounded Graphify update extracted 24,305 nodes versus the retained
58,384. It failed closed without `force=True`, preserving 31,816 nodes from
3,754 still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

The fresh ordinary Game ranking keeps the same seven documented boundary cases
outside the direct-C queue: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. The next ordinary candidate is `func_1514654C` (120 words,
60 current real differences), followed by `func_1515EB84` (61 words, 60 real
differences) and the remaining 60-difference ties. Every candidate still
requires source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
