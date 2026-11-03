# Working Note 2051: Game record-to-actor distance guarded match

Date: 2026-11-03

## Result

`func_15178C9C`, owner `conker/src/game/generated_1A5440.c`, retail VA
`0x15178C9C..0x15178DA4`, ROM `0x1A614C..0x1A6254`, is restored from its
zero-return placeholder as semantic C. The retail `-O2 -g3` body now matches
all 66 words and its original `0x18` frame.

The recovered query:

1. resolves the selected record with `func_15178B98(recordId)`;
2. returns the retail fallback value 1 when that record does not exist;
3. indexes the actor table `D_800CC2D0` by its exact `0x32C`-byte stride;
4. subtracts the record's signed integer XYZ coordinates at `+0x18`, `+0x1C`,
   and `+0x20` from the actor's floating XYZ coordinates at `+0x14`, `+0x18`,
   and `+0x1C`;
5. truncates each floating delta to signed integer, squares and sums the three
   deltas, converts that sum to float, and computes its square root; and
6. truncates the resulting distance to the returned signed integer.

Sixteen checked word guards normalize one closed compiler register-allocation
rotation covering the actor pointer and the X/Y/Z delta, square, and
accumulator lifetimes. They do not replace a condition, call, table binding,
field offset, conversion, multiply, sum, square root, fallback, or return.
The three original relocations remain bound to the record lookup call and the
two halves of `D_800CC2D0`.

The installed source names the recovered layouts `DistanceRecord15178C9C` and
`DistanceActor15178C9C`; its comment identifies the routine as the integer
distance from a selected record to an actor position.

## ABI, caller, and ownership

The recovered ABI is `s32 func_15178C9C(u8 recordId, s32 actorIndex)`. Its
sole direct caller is at ROM `0xCB3A4` in `func_1509DEC4`; there are no aligned
function-pointer literals. The selected owner preserves ten neighboring
bodies and its original object boundaries.

The strict linked-image comparison contains 6,051 functions, changes only
`func_15178C9C`, keeps every function address fixed, and uses zero exclusions.
Protected Game data remains exact across 189,088 bytes and 720 owners with
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Permanent qualification

The tools were committed before source installation as `8406a39`
(`test(game): qualify record actor distance`) and `f33ae36`
(`test(game): support installed distance source`). The permanent harness is:

- `tools/experiments/game_record_actor_distance_candidates.py`;
- `tools/experiments/game_record_actor_distance_match.py`; and
- `tools/tests/test_game_record_actor_distance_match.py`.

The installed three-test suite proves:

- 240 guest executions from 120 cases at entry phases zero and eight;
- all 66 retail words visited;
- missing-record fallback, actor indexing, all six coordinate fields, all
  three truncations and squares, the XYZ sum, square root, return conversion,
  caller binding, and call clobbers;
- native O0/O2/O3 execution; and
- eight effective semantic controls: missing-record fallback, next actor,
  wrong actor X field, X addition instead of subtraction, wrong record Y
  field, omitted Y square, omitted Z square, and a distance bias.

The installed suite passes all three tests in 28.865 seconds. The current
shared match-progress, generated-word-patch, PC16, and protected-data suite
passes all 19 tests in 9.624 seconds. Every checked row is stale-word guarded
by the complete owner/image gate.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Natural compact body with relocation fields normalized | `ef7014d423dcd00e31dbdcc94fbfee9d8fc3840ca6395d68192348911656b487` |
| Retail/guarded linked body | `18473fd35f3252a6b98c70ba4859665f62aeeccc167104c6c3980ac1d09b0e7d` |
| Installed source | `20e19527893fe5af5e1cffa562d81766e60569694741a05858d7701a4c38a207` |
| Qualified/production owner object | `69db84bac3dc9a94146701892c2da25571974691914061117e28085b838579c3` |
| Qualified/production linked ELF | `078d0fe77276a5cf7a1f3319bf67e511b4247c5f83261a92b42dbd4a2bf9106e` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `df161f3541627ea3f6f5fbdfd888d2122e7b6c9ce314e6230f1b4a918cfb309b` |
| Generated aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

The actual production Make rebuilt the complete Game and libultra object set,
padded every generated owner, linked `conker.us.elf`, and emitted
`conker.us.bin`. It stopped only at the expected final whole-ROM SHA mismatch
while the decomp remains incomplete; there were no compile, assembly, padding,
or link errors. The production owner and ELF reproduce the independently
predicted hashes above exactly.

## Recount

The fresh production ELF reports:

- Total: **4,121 / 5,511 (74.78%)**, zero address drift, 1,390 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,448 / 4,838 (71.27%)**, zero drift, 1,390 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **288 more** are needed.

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,246-node
graph with 112,196 edges and 5,093 communities; visualization was skipped at
the configured 5,000-node limit. An independent in-memory comparison retained
58,234 of 58,237 prior node IDs, removed three changed-corpus IDs, and added
twelve changed-corpus IDs.

The retained/refreshed `graphify-out/graph.json` is 75,516,353 bytes with
SHA-256 `d90682e3fd4a7301965a4858eab5a3cba1e1de6b8c177448f6f0025eb6b10674`.
The update used Graphify's incremental ten-path mechanism, deterministic hash
seeding, one worker, and `force=False`. This is bounded old-node retention
evidence, not a full-corpus extraction claim.

## Continuation

The seven smaller entries remain in their documented handwritten/custom-ABI
lane: `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. The fresh ordinary
queue now starts at `func_15189900` (64 words, 61 real differences), followed
by `func_1518A914`, `func_151AB1C4`, `func_151AF5C0`, and `func_151DA6F8`.
Every candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit. This static qualification does not claim
gameplay or hardware acceptance.
