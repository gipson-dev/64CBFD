# Working Note 2050: Game environment snapshot setup guarded match

Date: 2026-11-03

## Result

`func_151732E0`, owner `conker/src/game/generated_1A0790.c`, retail VA
`0x151732E0..0x151733D8`, ROM `0x1A0790..0x1A0888`, is restored from its
zero-return placeholder as semantic C. The retail `-O2 -g3` body now matches
all 62 words and its original `0x20` frame. One checked word guard normalizes
only a commutative equality operand order:

- `+0x028`: natural `bnel v0,t6` becomes retail `bnel t6,v0`.

The guard preserves the same equality test and delay-slot behavior. It does
not replace a branch condition, call, global binding, field access, snapshot
store, or provider selection.

The recovered setup:

1. reads signed `secondRange` from the live environment record at `+0x3C`;
2. when signed `fourthRange` at `+0x40` equals it and both are zero, repairs
   `fourthRange` to 100;
3. snapshots RGBA bytes `+0x42..+0x45`, four signed range halfwords
   `+0x3A..+0x40`, and the unsigned selected/fallback halfwords at `+0x02` and
   `+0x00` into the 16-byte `D_8008CC70` environment snapshot;
4. reads the signed provider selector at `+0x46`;
5. for a non-`-1` selector, sets `D_800DD2E0` active and calls
   `func_151733E4(selector, selector, context, 0, -1)`; and
6. for the `-1` sentinel, clears the active flag and calls
   `func_151733E4(0, 0, context, 0, -1)`.

The installed source uses typed signed and unsigned fields for the recovered
record and an explicitly sized snapshot structure. The comment identifies the
routine as the live-environment snapshot and initial-provider selection step.

## ABI, callers, and ownership

The recovered function takes one 32-bit context value and returns `void`.
There are two direct callers and no aligned function-pointer literals:

- ROM `0x352A4`, in `func_15007B3C`; its delay slot loads `D_800BE9F0` into
  `a0`;
- ROM `0x3B9B4`, in `func_1500E470`; its delay slot reloads the original
  context from the stack.

The twelve function/global relocations cover four references to `D_800B0DF0`,
two to `D_8008CC70`, four to `D_800DD2E0`, and two calls to
`func_151733E4`. The owner retains its mixed retail profile: its main object is
compiled with `-O2 -g3`, while `func_151733D8` is selected from the companion
`-O2` no-debug object. The selected owner comparison preserves every
neighboring body.

The strict linked-image comparison contains 6,051 functions, changes only
`func_151732E0`, keeps every function address fixed, and uses zero exclusions.
Protected Game data remains exact across 189,088 bytes and 720 owners with
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Permanent qualification

The tools were committed before source installation as `e554b49`
(`test(game): qualify environment snapshot setup`). The permanent harness is:

- `tools/experiments/game_environment_snapshot_candidates.py`;
- `tools/experiments/game_environment_snapshot_match.py`; and
- `tools/tests/test_game_environment_snapshot_match.py`.

The installed three-test suite proves:

- 280 guest executions from 140 cases at entry phases zero and eight;
- all 62 retail words visited;
- the zero-range repair, complete 16-byte snapshot, signed selector sentinel,
  active flag, provider arguments, caller bindings, and call clobbers;
- native O0/O2/O3 execution; and
- eight effective semantic controls: missing repair, wrong repair value, wrong
  second-range snapshot, swapped selected/fallback values, wrong sentinel,
  inverted active flag, missing duplicate selector argument, and forced default
  provider.

The installed suite passes all three tests in 27.313 seconds. The current
shared match-progress, generated-word-patch, PC16, and protected-data suite
passes all 19 tests in 9.953 seconds. The sole guard row is checked for a stale
expected word by the complete owner/image gate.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Natural compact body with relocation fields normalized | `a0b439002fae7517273c67a54579e28038e6c662dbebbf121f91c83b61114ddf` |
| Retail/guarded linked body | `b851f41c56fa0253132495248588db0227794f2a624efe5e29ca642db21d492b` |
| Installed source | `498f81e1cf74eb0f096d31cb0f71a521552683800ffcafdfc9843c30380499c3` |
| Qualified/production owner object | `9956f609092822400b0a9db1db31a0d5747a198115961a2a998c3895d0940971` |
| Qualified/production linked ELF | `21462505518ee6b17213cd6434b65b4c0409c8065b5159507a0afa528a536804` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `effd48acffc0ad66a5fa81ec6255e85a4d7c6db410bfac03c2834dcb82aa1fd3` |
| Generated aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

The actual production Make rebuilt the complete Game and libultra object set,
padded every generated owner, linked `conker.us.elf`, and emitted
`conker.us.bin`. It stopped only at the expected final whole-ROM SHA mismatch
while the decomp remains incomplete; there were no compile, assembly, padding,
or link errors. The production owner and ELF reproduce the independently
predicted hashes above exactly.

## Recount

The fresh production ELF reports:

- Total: **4,120 / 5,511 (74.76%)**, zero address drift, 1,391 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,447 / 4,838 (71.25%)**, zero drift, 1,391 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **289 more** are needed.

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,237-node
graph with 112,190 edges and 5,040 communities; visualization was skipped at
the configured 5,000-node limit. An independent in-memory comparison retained
58,225 of 58,228 prior node IDs, removed three changed-corpus IDs, and added
twelve changed-corpus IDs.

The retained/refreshed `graphify-out/graph.json` is 75,506,985 bytes with
SHA-256 `9f2871e566878d709a912809c048ce0fdfc1d3f5ee0ba575f6d7f4d4905a7e27`.
The update used Graphify's incremental ten-path mechanism, deterministic hash
seeding, one worker, and `force=False`. This is bounded old-node retention
evidence, not a full-corpus extraction claim.

## Continuation

The seven smaller entries remain in their documented handwritten/custom-ABI
lane: `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. The fresh ordinary
queue starts at `func_15178C9C` (66 words, 61 real differences), followed by
the tied `func_15189900`, `func_1518A914`, `func_151AB1C4`, and
`func_151AF5C0` group. Every candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount, documentation, and graph-retention gates before credit. This static
qualification does not claim gameplay or hardware acceptance.
