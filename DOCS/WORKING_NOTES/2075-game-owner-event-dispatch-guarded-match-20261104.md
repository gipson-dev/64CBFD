# Game owner-event dispatch guarded match (2026-11-04)

## Outcome

`func_15191980` now replaces its zero-return placeholder in
`conker/src/game/generated_1BA1D0.c` with the complete owner-event callback.
The typed semantic C and 45 fail-closed expected-word replacement rows match
all 65 retail words and the original 40-byte frame. Two rows carry checked
relocations; no inserted or omitted words, assembly body, source-level
compiler override, or address drift is needed.

The natural retail-profile body is already 65 words/frame40 and differs at 45
positions. The guards normalize only IDO's closed stack/register scheduling
choices. Plain `-O2` is retained as a compiler-profile control: it emits 64
words/frame40 and differs at 61 retail positions.

This is source, callback ABI/registry, compact/padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention evidence. It is not gameplay, event-effect, timing, hardware,
save, or PC-port runtime acceptance.

## Recovered behavior and ABI

The callback receives a record, an owner-event record, and a command byte; it
has no scalar return. The managed record stores its owner pointer at `+0x10`,
owner ID at `+0x14`, signed timer at `+0x16`, and flags at `+0x18`. The event
record supplies its owner pointer at `+0x00` and owner ID at `+0x04`.

Command `0x0D` accepts either owner-pointer or owner-ID identity, sets the
timer to 100, and sets flag bit zero; an identity miss returns unchanged.
Commands `0x0C`, `0x50`, and `0x0E` release the record through
`func_1516972C` only after the same identity test. Command `0x4E` releases it
unconditionally. Every other command forwards the event, command byte,
owner fields, and record to `func_15169850`.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x15191980..0x15191A84` |
| Retail ROM range | `0x1BEE30..0x1BEF34` |
| Owner | `generated_1BA1D0`, 60 neighboring functions |
| Body / retail slot | 65 / 65 words |
| Frame | 40 bytes |
| Bindings | two `func_1516972C` calls and one `func_15169850` call |
| Callback registry | ROM `0x230604`, `D_8008B4D4` descriptor callback at `0x8008BB44` |
| Natural compact normalized SHA-256 | `29108e69524af3a9317cdfc225d863e083db157f492c9d5a10a6558dbd10e27f` |
| Linked retail body SHA-256 | `802a9b01279fd08f0a8a7bff60d857fcc40a7dca93fa04d86b3890e50bd4c738` |

## Source provenance and compiler shape

The adjacent `Another Source/CBFD-Recompiled` checkout contains no source body
or symbol for this function, so it supplies no candidate. The recovery is
independently derived from retail assembly, the descriptor callback entry,
the proven three-argument callback dispatch in `func_15190550`, and the
already recovered release and forwarding helpers.

The event pointer is deliberately volatile in the semantic source to retain
retail's stack home, while repeated command-byte extraction preserves its
reload lifetime. The natural release calls land four bytes earlier than
retail at offsets `+0xAC` and `+0xC8`; the forwarding call already lands at
retail offset `+0xE8`. Forty-five checked replacement rows close the remaining
register and schedule differences. Every row verifies its compiler preimage,
and the two relocation-aware rows verify both expected and replacement
relocation metadata before they can apply.

## Qualification

The permanent four-test focused suite establishes:

- 2,048 guest cases cover all 256 command bytes, four pointer/ID match modes,
  and two stack phases. They execute 63 reachable words, make 26 release and
  2,008 forwarding calls, and preserve callback-clobbered caller-saved
  integer, floating-point, HI, and LO state;
- the two unreachable retail scheduling words at `0x151919EC` and
  `0x15191A40` remain statically byte-exact and are not overclaimed as dynamic
  coverage;
- actual 32-bit native O0, O2, and O3 each pass 4,096 cases, for 12,288
  positive executions, while eight independently compiled semantic controls
  fail; and
- the sole aligned callback pointer at ROM `0x230604`, absence of direct JAL
  callers, and all 117 representative active root-memory access fault cuts
  retain the callback ABI and exact instruction/branch-delay boundary.

All three helper relocations and 60 owner neighbors are fixed. The strict
6,052-function image changes only `func_15191980`, preserves every function
address with zero exclusions, and leaves all 189,088 protected Game-data
bytes across 720 owners exact.

The stable installed focused suite passes all four tests in 25.387 seconds.
The shared match-progress, generated-PC16, guarded-object, and protected-data
suite passes all 19 tests in 6.322 seconds. An earlier focused invocation was
discarded because it overlapped the production owner rebuild and correctly
rejected that transient owner; the stable serial rerun is the accepted
evidence.

## Production closure

The actual Make owner rule rebuilt `generated_1BA1D0`, and the production
owner and ELF equal the independently predicted qualified artifacts. The
broad `make all` path rebuilt the binary and stopped only at the expected
final retail SHA check. The inherited duplicate `generated_12D630` recipe
warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `b21ab065c29bebe609468508f5f872aa08e483fc217e8a1e479cea4809622098` |
| Qualified / production linked ELF | `ac534557c132ffafe195c27e63a39276fa2a2c39056c5f0a666f24c023488eb3` |
| Production rebuilt ROM image | `052b734d81db98ceba17033bcca8f721f21bd195d808716385c5fff18a21e7c6` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `9c2f50c6cc80ad2960d775b2cc8ac1f1dac1b079c4ba40d8c2593441753c76df` |
| Guard table | `b255b470dba0b748dce6273e24d774ebd18d024c46522bb5291c073b5aa90acf` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |

## Recount

The fresh production ELF reports:

- Total: **4,146 / 5,512 (75.22%)**, zero address drift, 1,366 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,473 / 4,839 (71.77%)**, zero drift, 1,366 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **264 more** are needed.

## Continuation

Rerank the ordinary Game queue from the fresh production ELF. Keep the seven
documented handwritten/custom-ABI/boundary rows (`func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68`,
`func_151AE2BC`, and `func_150A6760`) separate until their specific boundaries
are addressed. Every ordinary candidate still requires source/ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount, documentation, and graph-retention gates before credit.

## Graph retention

The retained graph baseline is 58,499 nodes / 112,353 links with SHA-256
`54a424ef06f2f171bcd10a00729a2a8302d3ddc36ff8465b1929d7028ab942a4`.
The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,709 nodes, so Graphify correctly refused to overwrite the
retained corpus. Its fail-closed report retained 31,816 nodes from 3,754
still-present files outside that reduced scan. The graph remained
byte-identical at the baseline hash.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,511 nodes, 112,364 links, and 5,121 communities. Against the saved
pre-change graph, 58,496 / 58,499 old node IDs were retained, including every
ID outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, each with its corresponding replacement two
lines later. Fifteen IDs were added: those three relocated headings; the Note
2075 file, title, and eight indexed section headings; and the retained
`OwnerEvent15191980` and `OwnerEventRecord15191980` types. The twelve-node and
eleven-link net additions are confined to the owned changes. This qualified
graph has SHA-256
`3c7df2b10522339f2cea62d2d0e2ce5e012e489b644979981f583ad0bcc0dc1f`.

After adding this receipt, a one-path stabilization retained all 58,511 node
IDs and found no code-graph topology change, leaving the qualified graph and
its SHA-256 untouched.
