# Game periodic actor event callback direct match (2026-11-04)

## Outcome

`func_151905BC` now replaces its zero-return placeholder in
`conker/src/game/generated_1BA1D0.c` with the complete periodic actor event
callback. The typed semantic C emits all 66 retail words directly under the
owner's retail `-O2 -g3` profile, including the original 48-byte frame and all
five relocation records. No expected-word guards, inserted words, omitted
words, assembly body, or source-level compiler override are needed.

Plain `-O2` retains the same 66-word/frame48 semantic shape but differs at 31
retail positions. It is retained as an effective compiler-profile control;
the owner Make rule already and deliberately uses `-O2 -g3`.

This is source, callback ABI/registry, compact/padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention evidence. It is not gameplay, actor-effect, timing feel,
hardware, save, or PC-port runtime acceptance.

## Recovered behavior and ABI

The function takes one `PeriodicActorEventNested151905BC *` and returns one.
Its nested clock begins at record offset `+0x90`: signed period and elapsed
words are followed by an actor pointer. The owner pointer remains at `+0x10`.

The callback adds signed global tick count `D_800BE9E4` to elapsed time. The
installed source uses unsigned intermediates for defined 32-bit wrap while
retaining retail's signed period comparisons. For every complete elapsed
period, it calls `func_1505D024(owner, 0x60021, 0, actorIndex)`, where
`actorIndex` is the signed pointer distance from `D_800CC2D0` divided by the
0x32C-byte `struct127` size, then subtracts one period with defined wrap.

After the loop, it reads the owner's attached target at `struct127::unk31C`.
When that pointer is non-null and target byte `+0x84` is zero, it writes 1000
to target halfword `+0x46`. It then returns one on every route. The concise
installed comment describes only this proven behavior and does not assign an
unverified gameplay name.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x151905BC..0x151906C4` |
| Retail ROM range | `0x1BDA6C..0x1BDB74` |
| Owner | `generated_1BA1D0`, 60 neighboring functions |
| Body / retail slot | 66 / 66 words |
| Frame | 48 bytes |
| Bindings | `D_800BE9E4` HI/LO, `D_800CC2D0` HI/LO, `func_1505D024` |
| Callback registry | ROM `0x23213C`, `D_8008D67C[0]` |
| Natural compact normalized SHA-256 | `4c3aa56dedc13d4ff32b00112f56e2eac6180820e461361b6c50cd2c658288f6` |
| Linked retail body SHA-256 | `52c3b3a1f21596ce6b2eb1af8db52ecb069d12f602508c640d3846ab7539a411` |

## Source provenance and compiler shape

The adjacent `Another Source/CBFD-Recompiled` checkout contains no source body
or symbol for this function, so it supplies no candidate. The recovery is
independently derived from retail assembly, the already recovered
`func_1505D024` four-argument event ABI, the exact `struct127` size and
`unk31C` field, the `D_800CC2D0` actor table, and the sole callback pointer.

The earlier exact `func_1518F7C4` randomized-step callback dispatches through
`D_8008D67C[0]`, retains this callback's integer return, and provides the
connected one-pointer ABI evidence. The retail image contains no direct JAL
to `func_151905BC`.

A flat record form emits 63 words/frame40 and differs at 65 positions. A
nested clock recovers 66 words/frame48 but retains 15 closed register-role
differences. Expressing the period route as an explicit `if` plus `do-while`,
with named base/code/stride locals, recovers the complete retail register
lifetime and schedule. All six independent assignment orders produce the
same exact retail-profile body, so the match does not depend on a fragile
statement-order accident.

## Qualification

The permanent four-test focused suite establishes:

- 4,096 guest cases exercise full-width tick wrap, signed period boundaries,
  zero through four period emissions, actor indices `-1`, `0`, `1`, and `25`,
  null/non-null attached targets, all target gate states, and both stack
  phases; they issue 5,117 callback events and preserve callback-clobbered
  caller-saved registers;
- 62 dynamically reachable retail words execute. The remaining four words
  belong to IDO's constant-812 signed-divide guard: two impossible-path
  branches/nops and its two break opcodes remain statically byte-exact;
- actual 32-bit native O0, O2, and O3 each pass 4,096 cases, for 12,288
  positive executions, while nine independently compiled semantic controls
  fail; and
- all 30 representative active-path root memory-access fault boundaries
  retain their exact instruction and branch-delay context.

The sole aligned callback pointer is at ROM `0x23213C`; there are no direct
JAL sites. All five bindings and 60 owner neighbors are fixed. The strict
6,052-function image changes only `func_151905BC`, preserves every function
address with zero exclusions, and leaves all 189,088 protected Game-data
bytes across 720 owners exact.

The installed focused suite passes all four tests in 34.758 seconds. The
shared match-progress, generated-PC16, guarded-object, and protected-data
suite passes all 19 tests in 6.543 seconds.

## Production closure

The actual Make owner rule rebuilt `generated_1BA1D0`, and the production ELF
equals the independently predicted qualified ELF. The broad `make all` path
generated the binary and stopped only at the expected final retail SHA check.
The inherited duplicate `generated_12D630` recipe warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `c89d1d0150f8f73a8856aea0fcdef2a0c9efaf512fd8ea73b03366853ba17b44` |
| Qualified / production linked ELF | `a338c2134d6aada1dcc3acdd0137f166d8fe455c5a81eac14efecc7ff73f04b4` |
| Production rebuilt ROM image | `fe6d5ffbb1a787b0ddf195ae220d56bd43966a4684a1452c731e020d17ab5c40` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `71831ffd4ee858c68dea19a82641c134fb1f727bb946382074007755ec85c0fb` |
| Guard table | `86559f1ec5fd731636f9ffc1a9960d9fc427cbdc5466bdff7289ea6800f800ab` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,145 / 5,512 (75.20%)**, zero address drift, 1,367 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,472 / 4,839 (71.75%)**, zero drift, 1,367 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **265 more** are needed.

## Continuation

Continue the ordinary Game queue at `func_15191980`, currently a 65-word slot
with 63 real differences. Keep the seven documented handwritten/custom-ABI/
boundary rows (`func_150A76F0`, `func_151F8870`, `func_150A613C`,
`func_150AE280`, `func_15115F68`, `func_151AE2BC`, and `func_150A6760`)
separate until their specific boundaries are addressed. Every ordinary
candidate still requires source/ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.

## Graph retention

The retained graph baseline is 58,488 nodes / 112,343 links with SHA-256
`6f3c78f8a9926262ac4b044472475cbdbd3050373905daa851e6581de84b11ca`.
The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,697 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside that reduced scan. The graph remained
byte-identical at the baseline hash.

An explicit ten-path incremental rebuild with `force=False` then produced
58,499 nodes, 112,353 links, and 5,106 communities. Against the saved
pre-change graph, 58,485 / 58,488 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, each with its corresponding replacement two
lines later. Fourteen IDs were added: those three relocated headings; the
Note 2074 file, title, and eight indexed section headings; and the retained
`PeriodicActorEventNested151905BC` type. The eleven-node and ten-link net
additions are confined to the owned changes. This qualified graph has
SHA-256 `54a424ef06f2f171bcd10a00729a2a8302d3ddc36ff8465b1929d7028ab942a4`.

After adding this receipt, a one-path stabilization retained all 58,499 node
IDs and found no code-graph topology change, leaving the qualified graph and
its SHA-256 untouched.
