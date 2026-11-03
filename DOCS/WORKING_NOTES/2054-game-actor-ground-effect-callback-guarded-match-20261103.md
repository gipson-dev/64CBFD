# Game Actor Ground-Effect Callback Guarded Match (2026-11-03)

## Outcome

`func_151AB1C4` is restored from a zero-return placeholder as semantic C. The
complete 64-word retail slot and 0x40-byte frame are byte-exact after nine
relocation-aware expected-word guards normalize two independent IDO layout
choices. Six rows move an independent opening load/constant setup schedule;
three rows move the same temporary pointer spill from stack home 0x2C to
retail's 0x28 home. The function's control flow, helper calls, data accesses,
and side effects remain expressed in C.

This is a source, callback-ABI, guest/native execution, owner, complete-image,
protected-data, production-build, and recount result. It does not claim live
gameplay, renderer, audio-output, or hardware acceptance.

## Recovered contract

The callback takes one owner pointer and always finalizes an attached actor:

- loads the attached actor from owner offset 0x18;
- copies actor X and Z from offsets 0x14 and 0x1C;
- chooses probe Y from actor offset 0x118 plus 100 when it exceeds global
  `D_800A8FEC`, otherwise actor offset 0x18 plus 150;
- probes 300 units below that point with `func_15045800`, writing the result
  to owner offset 0x34;
- on a hit, replaces the local Y with that result, submits effect kind 3 via
  `func_151ABE40`, and starts sound 0x5208 through `func_10010FFC`;
- passes the live owner category byte at 0x0C and identity byte at 0x01 to the
  effect helper; and
- unconditionally calls `func_151AA264` with the originally captured actor and
  owner result field.

The actor capture intentionally survives helper mutations. The category and
identity bytes are read after the ground query, while the actor argument used
by the sound and finalizer remains the entry-time pointer. The recovered
function is therefore declared `void func_151AB1C4(u8 *owner)`.

## Callback, owner, and guard evidence

There are no direct `jal` calls to the target. Its only aligned retail pointer
is at ROM `0x22FACC`, entry 15 of callback table `D_8008AFD0`, fixing the
one-owner-pointer side-effect callback ABI and unconditional finalizer tail.

The natural IDO body already has all 64 words, the retail 0x40 frame, and six
correct bindings. Its nine positional differences are exactly the nine guard
rows: offsets 0x18 through 0x2C form one closed six-word scheduling
permutation, and offsets 0x84, 0xA8, and 0xE8 form one closed spill-home
change. The first two rows carry the `D_800A8FEC` HI16/LO16 relocations to
their retail positions; all four `jal` relocations remain naturally fixed.

The strict reconstruction compares all 6,051 linked functions and finds only
`func_151AB1C4` changed, every symbol address fixed, zero exclusions, all 40
owner neighbors unchanged, and all protected Game data unchanged.

## Execution and negative controls

The permanent qualification tools were committed before source installation:

- tools commit `287afa4` (`test(game): qualify actor ground effect callback`);
- tools commit `7f91161` (`test(game): support installed ground callback source`);
- `tools/experiments/game_actor_ground_effect_callback_candidates.py`;
- `tools/experiments/game_actor_ground_effect_callback_match.py`; and
- `tools/tests/test_game_actor_ground_effect_callback_match.py`.

The installed suite passes all three tests in 33.973 seconds. Its 256 guest
executions cover 128 fixtures at entry phases zero and eight, both threshold
branches, hit and miss exits, helper mutations, owner/actor aliases, and
caller-saved register clobbering. It visits 63 of 64 words. Retail word
`0xC6100018` at offset 0x58 is unreachable: the branch-likely delay slot is at
0x3C, the false target is 0x5C, and the true path's unconditional branch skips
the duplicate load.

Native execution passes under O0, O2, and O3. Eleven deliberately broken
controls are rejected: wrong X, top, high offset, low offset, Z, probe depth,
effect kind, stale category, missing sound, missing finalizer, and wrong final
result pointer. The shared match-progress, generated-word-patch, PC16, and
protected-data suite passes all 19 tests in 6.388 seconds.

## Production and protected data

The independent predicted hashes were:

- owner object: `f4eab99f7f7e7d76eef7757b96ad6cdbacea813d21ab708313b394036ef082ae`;
- linked ELF: `c1609b5795c7be856dea52e03b7870054b3feb35fd672a65ef7f8a588341dacb`.

The actual production Make reproduced both hashes exactly. It rebuilt the
complete tree after the old build cleanup, padded the generated owner, linked
`conker.us.elf`, and emitted `build/conker.us.bin`. Verification stopped only
at the expected final whole-ROM SHA mismatch while the decomp remains
incomplete. The pre-existing duplicate `generated_12D630.c.o` recipe warning
remains unchanged; there were no compile, assembly, padding, or link errors.

The protected Game-data audit remains exact at address `0x80082760`: 189,088
bytes across 720 owners, zero different bytes, zero different owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Natural compact body with relocation fields normalized | `d212aaf861483e1351b07c539591dbd3e2347305f496b4dde16b6fb143c702b8` |
| Complete guarded retail body | `4012796eaf4f223f8f069fe2f388dcc8ed44ca607b36533feec7242bef07f00c` |
| Installed owner source | `4f51d828b88952126132bbb60fc5bdcb6e3a6410effaa1c106ecd6fa9e96575f` |
| Qualified/production owner object | `f4eab99f7f7e7d76eef7757b96ad6cdbacea813d21ab708313b394036ef082ae` |
| Predecessor linked ELF | `009150c2c9e451efb1f04db1fd988c3968344268ca3f93aca25c3960dc231206` |
| Qualified/production linked ELF | `c1609b5795c7be856dea52e03b7870054b3feb35fd672a65ef7f8a588341dacb` |
| Production rebuilt ROM image | `fe877dae9a68e5c59f688e465b76f4dacf8b7b356d9ea21cc6006d6ef973ad24` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `5dca6cbb64815f8cfbb474e08fa06488691252ad0bc25ae7beaf4af0449ec59c` |
| Generated aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,124 / 5,511 (74.83%)**, zero address drift, 1,387 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,451 / 4,838 (71.33%)**, zero drift, 1,387 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **285 more** are needed.

## Graph retention

The standard reduced-corpus Graphify update proposed 24,475 nodes versus the
retained 58,270 and failed closed without `--force`. It reported preservation
of 31,816 nodes from 3,754 still-existing files outside that scan corpus.

The established explicit changed-path rebuild then retained 58,267 of 58,270
prior node IDs, removed the three superseded changed-document IDs, and added
fourteen current IDs. The resulting graph has 58,281 nodes, 112,224 edges, and
5,032 communities; visualization was skipped at the configured 5,000-node
limit. `graphify-out/graph.json` is 75,496,832 bytes with SHA-256
`f863efb7a7c79e3aed6fed3e7af97c2d18add8d1c466a67ba6610364228a2f56`.

The accepted update used the explicit ten-path change set, deterministic hash
seeding, one extraction worker, and `force=False`. The guard CSV and submodule
pointer are outside AST ownership; the source and documentation paths were
reconciled against the retained graph. This is bounded old-node retention
evidence, not a full-corpus extraction claim.

## Continuation

The seven smaller entries remain in their documented handwritten/custom-ABI
lane: `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. Continue with ordinary
candidate `func_151AF5C0`, followed by `func_151DA6F8`, `func_1504A620`, and
`func_15172D80`. Every candidate still requires source, ABI/caller, owner,
guest/native, actual Make, complete-image, protected-data, production recount,
documentation, and graph-retention gates before credit.
