# Game Late Uniform-Matrix Submit Direct Match (2026-11-03)

## Outcome

`func_1518A914` is restored from a zero-return placeholder as semantic C. Its
62-word compiler body is byte-exact under the owner's retail `-O2 -g3`
profile, and the generated-object padder retains the original zero word at the
owner boundary for a complete 63-word linked retail slot. The frame remains
0x68, both relocations remain correctly bound, and no expected-word guard is
needed.

This is a source, callback-ABI, guest/native execution, owner, complete-image,
protected-data, production-build, and recount result. It does not claim live
gameplay or hardware acceptance.

## Recovered contract

The callback takes a fixed-point matrix output pointer and a state pointer,
then returns one after conversion. The recovered C:

- passes state rotations at 0x100, 0x104, and 0x108 to `func_150A8050`;
- copies state positions at 0x48, 0x4C, and 0x50 into matrix row 3;
- multiplies all nine 3x3 basis elements by the uniform scale at 0x10C;
- leaves the homogeneous and translation terms otherwise intact;
- converts the float matrix through `guMtxF2L`; and
- returns one.

The source keeps the rotation pointer declared before the 4x4 matrix and
assigned afterward because that shape reproduces retail's saved-register and
load schedule. `-O2` without `-g3` emits 61 words and differs at 13 positions,
confirming the retail profile.

## Callback and owner evidence

There are no direct `jal` calls to this function. The sole aligned retail
pointer is at ROM `0x22F8D0`, the middle entry of callback table
`D_8008AE0C`. Its neighbors are the already-restored uniform-matrix callback
`func_1515858C` and `func_15158920`, which fixes the two-pointer callback ABI
and return contract. The two target relocations remain bound to
`func_150A8050` and `guMtxF2L`.

The strict pre-install reconstruction compares all 6,051 linked functions and
finds only `func_1518A914` changed, every symbol address fixed, zero
exclusions, both owner neighbors unchanged, and the callback table unchanged.
The 248-byte compiler body matches retail directly; the full linked 252-byte
slot additionally proves the original trailing zero pad.

## Execution and negative controls

The permanent qualification tools were committed before source installation:

- tools commit `f8e8c86` (`test(game): qualify late uniform matrix submit`);
- tools commit `f92ab3b` (`test(game): support installed late matrix source`);
- `tools/experiments/game_late_uniform_matrix_submit_candidates.py`;
- `tools/experiments/game_late_uniform_matrix_submit_match.py`; and
- `tools/tests/test_game_late_uniform_matrix_submit_match.py`.

The installed suite passes all three tests in 30.925 seconds. Its 512 guest
executions cover 32 seeds, eight post-helper mutation modes, and entry phases
zero and eight. Every executable compiler word is visited; the final retail
word is owner-boundary padding after the return and is checked statically in
the linked slot. The helper hook deliberately clobbers caller-saved registers
and mutates the state, proving that rotation arguments are captured before the
call while position and scale are read afterward.

Native execution passes under O0, O2, and O3. Eleven deliberately broken
controls are rejected: each wrong rotation, each wrong position, wrong scale,
one missing basis multiply, scaled translation, wrong conversion output, and
wrong return value. The shared match-progress, generated-word-patch, PC16, and
protected-data suite passes all 19 tests in 7.033 seconds.

## Production and protected data

The independent predicted hashes were:

- owner object: `ae0f077dc1baeb8be0b8ae1bcfe0a5bebba852d8089f13879c6252fb84cc23fd`;
- linked ELF: `009150c2c9e451efb1f04db1fd988c3968344268ca3f93aca25c3960dc231206`.

The actual production Make reproduced both hashes exactly. It compiled the
owner, padded the generated slice, linked `conker.us.elf`, and emitted
`conker.us.bin`; it stopped only at the expected final whole-ROM SHA mismatch
while the decomp remains incomplete. The pre-existing duplicate
`generated_12D630.c.o` recipe warning remains unchanged. There were no compile,
assembly, padding, or link errors.

The protected Game-data audit remains exact at address `0x80082760`: 189,088
bytes across 720 owners, zero different bytes, zero different owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Natural compact object body with relocation fields normalized | `e748b3ac61b5c1a2604161bc7a47119fc1f502c5348823c6ac6f1a46ac31cf5d` |
| Linked 62-word compiler body | `a9a4eeb3733fa67f590e0598d471d24d2db449b91f6477888fbe2c6c35a76731` |
| Complete 63-word retail slot including boundary pad | `7484f27bae35efb02afac8e7e95f175253579746834a652ae93d957aa3380169` |
| Installed owner source | `fb3b8d6ae333568db6cb3d18cbbd624e3795dc6bfb978f8c16ec0cef2b50861f` |
| Qualified/production owner object | `ae0f077dc1baeb8be0b8ae1bcfe0a5bebba852d8089f13879c6252fb84cc23fd` |
| Qualified/production linked ELF | `009150c2c9e451efb1f04db1fd988c3968344268ca3f93aca25c3960dc231206` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `df161f3541627ea3f6f5fbdfd888d2122e7b6c9ce314e6230f1b4a918cfb309b` |
| Generated aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,123 / 5,511 (74.81%)**, zero address drift, 1,388 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,450 / 4,838 (71.31%)**, zero drift, 1,388 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **286 more** are needed.

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,269-node
graph with 112,218 edges and 5,062 communities; visualization was skipped at
the configured 5,000-node limit. An independent in-memory comparison retained
58,255 of 58,258 prior node IDs, removed three changed-corpus IDs, and added
fourteen changed-corpus IDs.

The retained/refreshed `graphify-out/graph.json` is 75,541,068 bytes with
SHA-256 `9499fdc2d8ca99aacd806dd5f9a4bf15d13e3588fa5163685b9772e7cd9775a7`.
The update used Graphify's incremental nine-path mechanism, deterministic hash
seeding, one worker, and `force=False`. This is bounded old-node retention
evidence, not a full-corpus extraction claim.

## Continuation

The seven smaller entries remain in their documented handwritten/custom-ABI
lane: `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. The fresh ordinary
queue now starts at `func_151AB1C4` (64 words, 61 real differences), followed
by `func_151AF5C0`, `func_151DA6F8`, `func_1504A620`, and `func_15172D80`.
Every candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
