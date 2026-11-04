# Game actor threshold transition direct match (2026-11-04)

## Outcome

`func_1512B630` now replaces its zero-return placeholder in
`conker/src/game/generated_157840.c` with a named
`ActorThresholdTransition` record and a semantic six-argument update. IDO
emits all 64 retail words with the original 32-byte frame. There are no guard
rows, inserted or omitted instructions, compiler-profile changes,
owner-boundary changes, or inventory changes.

This is a source, direct-caller ABI, compact/padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not gameplay, actor-transition, animation, save,
or PC-port acceptance.

## Recovered behavior and ABI

The O32 interface takes an actor pointer, an `ActorThresholdTransition`
pointer, a signed threshold, a signed value, a signed comparison peer, and an
alternate-table selector. Both retail calls pass selector zero, but the body
retains and tests the complete six-argument contract.

The function chooses a signed halfword from `D_800DC204` or `D_800DC206`.
Its byte address combines the actor's signed halfword index at `+0x1B4`, an
eight-byte record stride, the actor's player byte at `+0x23D`, and a 0x20-byte
player stride. Actor flag `0x8000` at `+0x84` doubles the selected value with
signed-16 wrapping. If the selected value is below the caller's threshold,
the two comparison directions select transition state two or one, call
`func_1512B5FC(transition, value, threshold)`, and return one. Otherwise the
active and state bytes are cleared, the transition threshold becomes
`0xFFFC`, and the function returns zero.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x1512B630..0x1512B730` |
| Retail ROM range | `0x158AE0..0x158BE0` |
| Owner | `generated_157840`, 14 neighboring functions |
| Body / retail slot | 64 / 64 words |
| Frame | 32 bytes |
| Relocations | 6: two table HI/LO pairs and two `func_1512B5FC` calls |
| Natural compact raw SHA-256 | `3786acad0df74e808ca73353073c46b140c3221709733038540586fb4ad6a29c` |
| Linked retail body SHA-256 | `140e3fe26d7be7fdf9ddb1795c643e152e070e610e79ca3b10af89d2ba0838c5` |

## Caller and registry evidence

The two aligned direct calls are both in `func_1512B1B8`, at ROM `0x15886C`
/ virtual `0x1512B3BC` and ROM `0x158998` / virtual `0x1512B4E8`. The two
caller windows pass all six arguments, including stack arguments four and
five. Both set the alternate selector to zero and use the return value to
choose whether their surrounding loop exits. There are no aligned pointer
literals for this function.

The permanent caller model executes 128 cases across both windows, return
values, two stack phases, and sixteen seeded register states. It verifies all
six arguments, legal volatile clobbers, and the result-dependent loop update.

## Direct-match boundary

The selected C body compiles directly to all 64 retail words. The only
candidate-source cleanup after qualification was line wrapping for the two
table-address expressions; it does not alter compiler output. No rows were
added to `retail_word_patches.us.csv`.

## Qualification

The permanent five-test suite establishes:

- 640 guest cases exercise both tables, both flag states, five signed input
  values, all four outcomes, two player values, two signed record indices, and
  two stack phases;
- execution reaches 63 / 64 words; `0x1512B670` is a structurally unreachable
  retail branch shadow that remains statically byte-exact;
- both successful directions, the clear route, signed-16 doubling wrap,
  helper calls, field widths, and legal volatile clobbers agree;
- both original caller windows pass all 128 six-argument/result-use cases;
- native 32-bit O0, O2, and O3 each pass 4,096 cases, for 12,288 executions,
  with undefined-behavior trapping and valid actor, transition, and table
  backing storage;
- sixteen independently compiled semantic controls are rejected;
- all 256 compact-body byte mutations and all six relocation-binding controls
  fail closed;
- all 14 neighboring owner functions and normalized pools remain unchanged;
  and
- the strict 6,052-function image changes only `func_1512B630`, preserves
  every function address with zero exclusions, and retains all 189,088
  protected Game-data bytes across 720 owners exactly.

The installed five-test suite passes in 49.860 seconds. The shared
match-progress, protected-data, guarded-object, and generated-PC16 suite passes
all 19 tests in 11.889 seconds. Qualification tools are banked first in tools
commit `d72735a`.

## Production closure

The actual Make rule compiled, padded, assembled, and linked
`generated_157840` from the installed source without a guard table change. The
production owner and full ELF equal the independently qualified artifacts.
`make -C conker all -j2` generated the ROM and stopped only at the expected
final retail-ROM SHA check; there was no compile, padding, assembly, link, or
image-generation failure. The inherited duplicate `generated_12D630` recipe
warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `2083667144663f5b9582b174fbf5b9adacec07bd9e2418ade8bb56b6fda01935` |
| Qualified / production linked ELF | `64692e2ee58d02bcf402b5ee3e1ce6dc1e05aea06fe87fc108afcc731fb197b9` |
| Production rebuilt ROM image | `3fc592b7647d28b4bcb7819f64487c631c6000345780d0dd2c34dac94f11fad6` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `642f4c5f8ef4ba932c7e366ff4d292f4449ed8b8fd41a7148e691b7dda7a3e21` |
| Guard table | `22a502a5d003bc0d0b40de30f69e1b9d7425fa27a4099f055fe5152b8bd2b5dd` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |
| Aggregate progress catalogue | `4f170efa6034414c9a2612153aac6ea69468b99f7523dde4a11370f8b07a2c99` |

## Recount

The fresh production ELF reports:

- Total: **4,140 / 5,512 (75.11%)**, zero address drift, 1,372 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,467 / 4,839 (71.65%)**, zero drift, 1,372 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **270 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,638 nodes against the retained 58,429-node corpus, so
Graphify correctly refused to overwrite `graph.json`. Its fail-closed report
retained 31,816 nodes from 3,754 still-present files outside the reduced scan
corpus. The graph remained byte-identical with SHA-256
`cdabdf38f2cb28241655225e4916debb79755f623acdc1c87187b39d8139bf2b`.
No forced refresh or dependency update was used.

An explicit ten-path incremental rebuild with `force=False` then produced
58,440 nodes, 112,297 links, and 5,077 communities. Against the saved
pre-change snapshot, 58,426 / 58,429 old node IDs were retained, including all
IDs outside the changed-path set. The three replaced IDs are line-derived
`DOCS/UPDATE_LOG.md` headings, and each has one uniquely relocated replacement
two lines later. Fourteen IDs were added: those three relocated headings, the
Note 2069 file and its nine indexed headings, and the
`ActorThresholdTransition` type node. The eleven-node and eleven-link net
additions are confined to the owned changes. The explicit-refresh graph
SHA-256 is
`e73cef0229b5553cfc0fe72d39d468758089eef5bdd7ac91d0d4c03ad9770d60`.
A final one-path refresh after recording this receipt retained all 58,440
scoped node IDs and added only this `Graph retention` heading, producing
58,441 nodes and 112,298 links with no old-ID loss.

## Continuation

The seven smaller rows ahead of the ordinary queue remain the documented
handwritten/custom-ABI/boundary cases: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue with ordinary Game candidate `func_15158920`, a
64-word slot with 63 current real differences.
