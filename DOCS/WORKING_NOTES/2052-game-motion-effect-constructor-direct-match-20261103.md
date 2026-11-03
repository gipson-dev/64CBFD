# Game Motion-Effect Constructor Direct Match (2026-11-03)

## Outcome

`func_15189900` is restored from a zero-return placeholder as semantic C and
matches its complete 64-word retail slot with the original 40-byte frame. The
typed implementation emits directly under the owner's retail `-O2 -g3`
profile: there are zero natural positional differences and no expected-word
guards.

This is a source, ABI, guest/native execution, owner, complete-image,
protected-data, production-build, and recount result. It does not claim live
gameplay or hardware acceptance.

## Recovered contract

The function takes a pointer to a 0x50-byte motion descriptor and an unsigned
byte enable flag, and returns `void`. It:

- requests a 0x78-byte category-0x1A object from `func_15167A68`;
- leaves all object memory untouched when allocation fails;
- copies the complete descriptor into the object at offset 0x10;
- calls `func_1510F800(0)`;
- registers the truncated X/Z midpoint through `func_1510FD20`, using
  `position + velocity * 0.5f`, and stores the returned handle at 0x6C;
- normalizes the low byte of the enable argument to zero or one at 0x70;
- clears the signed age at 0x60 and elapsed float at 0x64; and
- stores position Y plus velocity Y when the velocity is negative, otherwise
  position Y, as the baseline at 0x68.

The explicit local `enabledValue` and two-arm assignment are retained because
that is the source shape selected by the retail schedule. The structure names
describe only the fields established by this routine; unknown retained bytes
remain deliberately unnamed.

## ABI and caller evidence

The retail image contains eleven direct calls and no aligned pointer literal:

- one call from `func_15008BF0`;
- one call from `func_1500E8C0`; and
- nine calls from `func_1500F40C`.

The complete call-site list is at ROM offsets `0x36254`, `0x3BEC8`, `0x3CA80`,
`0x3CAFC`, `0x3CB78`, `0x3CBF4`, `0x3CC70`, `0x3CCE4`, `0x3CD60`, `0x3CDDC`,
and `0x3CE58`. Four relocations remain bound to `func_15167A68`, `memcpy`,
`func_1510F800`, and `func_1510FD20`.

## Exact compiler and image proof

The selected body is 64 words with frame 0x28 under `-O2 -g3`; `-O2` without
debug scheduling differs by seven words. No guard table row is added. The
strict pre-install reconstruction compares all 6,051 linked functions and
finds only `func_15189900` changed, with every symbol address fixed, zero
exclusions, all three owner neighbors unchanged, and all callers unchanged.

The independent predicted hashes were:

- owner object: `ad5b5bbfae6d149094862c3a3d8541a0b97410b393e3fa79bbd2dcb0ae9578e9`;
- linked ELF: `1613a6c709d4b73b14ef064b853822a3784e1839a844600c16032226bd4eeb24`.

The actual production Make reproduced both hashes exactly. It compiled the
owner, padded the generated slice, linked `conker.us.elf`, and emitted
`conker.us.bin`; it stopped only at the expected final whole-ROM SHA mismatch
while the decomp remains incomplete. The pre-existing duplicate
`generated_12D630.c.o` recipe warning remains unchanged. There were no compile,
assembly, padding, or link errors.

The protected Game-data audit remains exact at address `0x80082760`: 189,088
bytes across 720 owners, zero different bytes, zero different owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

## Execution and negative controls

The permanent qualification tools were committed first in tools commit
`070f2af` (`test(game): qualify motion effect constructor`):

- `tools/experiments/game_effect_motion_constructor_candidates.py`;
- `tools/experiments/game_effect_motion_constructor_match.py`; and
- `tools/tests/test_game_effect_motion_constructor_match.py`.

The installed suite passes all three tests in 49.309 seconds. Its 240 guest
executions cover 120 semantic cases at entry phases zero and eight, including
allocation success/failure, exact descriptor copying, call clobbers, midpoint
rounding, enable normalization, signed-zero behavior, and both Y-baseline
branches. They visit all 63 architecturally reachable retail words. The
remaining word at `+0xE4` is a duplicate `lwc1` in retail dead code: the
preceding branch-likely jumps over it, while the other arm branches directly
to the epilogue. Static exact-body comparison still covers all 64 words.

Native execution passes under O0, O2, and O3. Eight deliberately broken
controls are rejected: wrong allocation kind, wrong allocation size, short
copy, skipped initialization, full rather than half velocity, raw enable byte,
retained age, and omitted negative-Y adjustment. The shared match-progress,
generated-word-patch, PC16, and protected-data suite passes all 19 tests in
11.333 seconds.

## Frozen evidence

| Artifact | SHA-256 |
| --- | --- |
| Natural compact body with relocation fields normalized | `fe12ba0e5f5a5e45029c249c9ae69437502fcfc57ae88df1ac81f61ff6721526` |
| Retail linked body | `00f32282482f3dd37d312d61773449c380709d67a1028fc232ead73172b6be4c` |
| Installed owner source | `3de1e31350e25a6408841f033cf40f58cae54fa2a1104cb5c9d3c9efba5439a5` |
| Qualified/production owner object | `ad5b5bbfae6d149094862c3a3d8541a0b97410b393e3fa79bbd2dcb0ae9578e9` |
| Qualified/production linked ELF | `1613a6c709d4b73b14ef064b853822a3784e1839a844600c16032226bd4eeb24` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Installed guard table | `df161f3541627ea3f6f5fbdfd888d2122e7b6c9ce314e6230f1b4a918cfb309b` |
| Generated aggregate progress catalogue | `96a7f15ab5207027a204f795e91b8f9f3453482ce4ec4d47bd8bcb4b5a305502` |

## Recount

The fresh production ELF reports:

- Total: **4,122 / 5,511 (74.80%)**, zero address drift, 1,389 different.
- Init: **492 / 492 (100.00%)**, zero drift.
- Game: **3,449 / 4,838 (71.29%)**, zero drift, 1,389 different.
- Debugger: **181 / 181 (100.00%)**, zero drift.

The active 80% threshold is 4,409 exact functions, so **287 more** are needed.

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,257-node
graph with 112,206 edges and 5,059 communities; visualization was skipped at
the configured 5,000-node limit. An independent in-memory comparison retained
58,243 of 58,246 prior node IDs, removed three changed-corpus IDs, and added
fourteen changed-corpus IDs.

The retained/refreshed `graphify-out/graph.json` is 75,529,688 bytes with
SHA-256 `326adde21f9d09957f461ad83bb377bba32b4c454bc17d2ce0422b91d8c848e6`.
The update used Graphify's incremental nine-path mechanism, deterministic hash
seeding, one worker, and `force=False`. This is bounded old-node retention
evidence, not a full-corpus extraction claim.

## Continuation

The seven smaller entries remain in their documented handwritten/custom-ABI
lane: `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68`, `func_151AE2BC`, and `func_150A6760`. The fresh ordinary
queue now starts at `func_1518A914` (63 words, 61 real differences), followed
by `func_151AB1C4`, `func_151AF5C0`, `func_151DA6F8`, and `func_1504A620`.
Every candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
