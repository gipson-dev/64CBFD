# Game actor/view-state reset guarded match (2026-11-04)

## Outcome

`func_151218C4` now replaces its zero-return placeholder in
`conker/src/game/generated_14D110.c` with a typed actor/view-state reset. The
compiler emits 66 executable words with the original 40-byte frame; the retail
slot contains those words plus one trailing alignment NOP. Four fail-closed
replacement rows normalize two independent instruction-order pairs. There are
no inserted or omitted instructions, relocation-bearing guards, compiler-profile
changes, owner-boundary changes, or inventory changes.

This is a source, direct-caller ABI, compact/padded owner, guest/native
execution, strict whole-image, protected-data, production-build, recount, and
graph-retention result. It is not visual, camera, actor-state gameplay, save,
or PC-port acceptance.

## Recovered behavior and ABI

The sole direct caller passes its current actor pointer in `a0` and ignores the
return value. The installed function is therefore `void` and takes a local
typed overlay compatible with the fields observed in retail assembly.

Resource flag `0x10` blocks the reset. Otherwise actor kind `0x40` selects the
special branch: mode `0x0F` clears two late floating accumulators, the linked
target's byte at `+0x198` is cleared, state becomes zero, and the timer becomes
60. Other actor kinds set the same timer and state three. Both routes publish
distances 200.0 and 100.0, truncate the view angle to the integer field, clear
the view-active byte and three floating accumulators, and submit command
`(2, 0xFF, 0x20, actor[0x23D])` through `func_1506160C`. A pending cleanup byte
calls `func_151C9ED4` before being cleared.

| Evidence | Value |
| --- | --- |
| Virtual range | `0x151218C4..0x151219D0` |
| Retail ROM range | `0x14ED74..0x14EE80` |
| Owner | `generated_14D110`, four neighboring functions |
| Executable body / retail slot | 66 / 67 words |
| Frame | 40 bytes |
| Relocations | 2: `func_1506160C`, `func_151C9ED4` |
| Natural compact body SHA-256 | `cf1916459a330b68a9248e0cc24787548e7e7a20018b4857f4dd0813f6522764` |
| Linked retail slot SHA-256 | `6c1dc094e0c5a9c5dfaf0492a38a25029b2a430a7f9e9f0e18774fc134577bc2` |

## Caller and registry evidence

The retail ROM has one aligned direct call, at ROM `0x14E548` in
`func_15120158` (`0x15121098`). The caller passes its saved actor pointer in
`a0`; the JAL delay slot saves live `t0` at `sp+0x54`, and the following word
reloads it after the callee's volatile clobbers. No return value is consumed.
There are no aligned pointer literals for this function.

The permanent caller-window model executes 128 cases with volatile register,
floating-register, and outgoing-home clobbers. It verifies the actor argument,
the delay-slot save, the post-call reload, and the ignored result.

## Guard boundary

The natural compiler output differs at only four executable positions:

| Offset | Natural | Retail | Purpose |
| ---: | --- | --- | --- |
| `0x074` | `A60B084A` | `44800000` | Load the shared floating zero before the fallback timer store. |
| `0x078` | `44800000` | `A60B084A` | Place the fallback timer store after that load. |
| `0x090` | `E6040374` | `26020740` | Form the shared view-state base before publishing distance 200.0. |
| `0x094` | `26020740` | `E6040374` | Publish distance 200.0 after forming the view-state base. |

Each CSV row checks its natural preimage and replaces one word. The rows do not
change behavior, branch topology, relocation ownership, function length, frame,
or alignment. The retail slot's final NOP belongs to owner alignment and is not
counted as an executable compiler word.

## Qualification

The permanent five-test suite establishes:

- 12,096 guest cases execute all 66 executable words across two stack phases;
  the trailing alignment NOP is verified as non-executable;
- resource gating, both kind branches, the mode branch, signed angle
  truncation, every width-specific field update, both helper calls, live
  post-command cleanup, and legal volatile GPR/FPR/home clobbers agree;
- the original caller window passes all 128 cases;
- native 32-bit O0, O2, and O3 each pass 4,096 cases, for 12,288 executions,
  with undefined-behavior trapping and valid backing storage;
- twenty independently compiled semantic controls are rejected;
- all 264 compact-body byte mutations, all 268 retail-slot byte mutations,
  all four actual guard-preimage controls, and both relocation-binding controls
  fail closed;
- all four neighboring owner functions and normalized pools remain unchanged;
  and
- the strict 6,052-function image changes only `func_151218C4`, preserves every
  function address with zero exclusions, and retains all 189,088 protected
  Game-data bytes across 720 owners exactly.

The installed five-test suite passes in 75.336 seconds. The shared
match-progress, guarded-object, generated-PC16, and protected-data suite passes
all 19 tests in 11.905 seconds.

## Production closure

The actual Make rule compiled, post-processed, padded, assembled, and linked
`generated_14D110` from the installed source and four installed guard rows.
The production owner and full ELF equal the independently qualified artifacts.
`make -C conker all -j2` generated the ROM and stopped only at the expected
final retail-ROM SHA check; there was no compile, padding, assembly, link, or
image-generation failure. The inherited duplicate `generated_12D630` recipe
warning is unchanged.

| Artifact | SHA-256 |
| --- | --- |
| Qualified / production owner object | `e1e13b6bace2a4ffd8473615c3bbd55f20dca9d86179183a59b71b28f57ec2d3` |
| Qualified / production linked ELF | `2f340b30099263c604243d56d8dea5b75738a6234d829aefe0d2db952a9d27c5` |
| Production rebuilt ROM image | `79ccd205ca072772f8591667403f3998b3619170928d3b25578fcd186edc74bf` |
| Production map | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Installed owner source | `0d62032830e38601ea0db5bebd798753f70f82ea4399281bde8c0dfc82a748de` |
| Guard table | `22a502a5d003bc0d0b40de30f69e1b9d7425fa27a4099f055fe5152b8bd2b5dd` |
| Retail layout | `67a28e9dfe6bd0dc21e3a386966e69f7507a8e1628dc0f67d46425ac297dadcb` |
| Aggregate progress catalogue | `4f170efa6034414c9a2612153aac6ea69468b99f7523dde4a11370f8b07a2c99` |

## Recount

The fresh production ELF reports:

- Total: **4,139 / 5,512 (75.09%)**, zero address drift, 1,373 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,466 / 4,839 (71.63%)**, zero drift, 1,373 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The converted inventory remains 5,512 / 6,046 functions. The active 80%
threshold is 4,410 exact functions, so **271 more** are needed.

## Graph retention

The standard reduced `graphify update .` extracted eight uncached inputs but
proposed only 24,626 nodes against the retained 58,417-node corpus, so Graphify
correctly refused to overwrite `graph.json`. Its fail-closed report retained
31,816 nodes from 3,754 still-present files outside the reduced scan corpus.
The graph remained byte-identical with SHA-256
`bac5bd4548c0cb427c8ab7aba44ea92de98f05af1ea68ad7aa697ace40714a22`.
No forced refresh or dependency update was used.

An explicit eleven-path incremental rebuild with `force=False` then produced
58,428 nodes, 112,285 links, and 5,124 communities. Against the saved
pre-change snapshot, 58,414 / 58,417 old node IDs were retained, including all
IDs outside the changed-path set. The three replaced IDs are line-number-derived
`DOCS/UPDATE_LOG.md` headings, and each has one uniquely relocated replacement
two lines later. Fourteen IDs were added: those three relocated headings, the
Note 2068 file and its nine indexed headings, and the `ResetActor151218C4` code
node. The eleven-node and nine-link net additions are confined to the owned
changes. The explicit-refresh graph SHA-256 is
`db33e8613ed5d2ad22ef010253e794f88b1db88203f0f6409fe6d2a23c9ba38d`.

## Continuation

The seven smaller rows ahead of the ordinary queue remain the documented
handwritten/custom-ABI/boundary cases: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Rerank the ordinary Game queue from the fresh production ELF.
