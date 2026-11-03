# 2031 - Reflected projection probe matched as guarded C

Verified 2026-11-03. Production is **4,101/5,511 (74.41%)**; Game is
**3,428/4,838 (70.86%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,410 functions remain different. The active 80% target is
**4,409/5,511**, requiring **308 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_15035714` replaces its zero-return placeholder in
`conker/src/game/generated_61D10.c`. It is the reflected projection probe at
VA `0x15035714`, ROM `0x62BC4..0x62CB8`, owned by `generated_61D10`. The
recovered interface is:

```c
s32 func_15035714(s32 mode, u8 *actor, u8 *projection, f32 reflectionY);
```

The routine selects the current view through `D_800BE628` and the actor's
descriptor through `D_800D1C90[actor[4]]`. It scales actor extents `+0x14C`
and `+0x150` by the descriptor's unsigned width at `+0x0E`, while the signed
descriptor height at `+0x10` supplies the vertical radius. Modes zero and one
reflect actor Y about `reflectionY`; other modes use the direct actor Y plus
vertical radius. The resulting X/Y/Z and half extents are submitted to
`func_150A6360` with `D_800D9C10` and `D_80097D70`. The function returns one
exactly when that helper returns zero.

Retail contains one direct JAL from `func_15035808` at ROM `0x62FBC` and no
aligned pointer literals. Its caller passes the actor, provisional projection
record, mode and floating reflection plane, then retires the provisional
record when this probe returns nonzero. The Alternate Source donor was used
only as comparison evidence: its inferred types and argument order did not
match the retail ABI, so no donor body was copied.

## Compiler and image closure

The semantic `-O2 -g3` body naturally emits all 61 words with a 48-byte frame
and the correct nine relocations. Retail also owns 61 words but uses a 64-byte
frame. Seventeen checked rows normalize only compiler frame, register and
floating-point scheduling choices; there are no inserted or omitted words.
The nine symbolic bindings remain the two HI16/LO16 pairs for `D_800BE628`,
`D_800D1C90`, `D_80097D70` and `D_800D9C10`, plus the J26 binding for
`func_150A6360`.

The guarded result matches all 61 retail words. All nine other owner functions
and normalized pools remain unchanged. Across the linked image, only
`func_15035714` changes; all 6,051 function addresses remain fixed, and strict
comparison uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-masked 61-word payload | `7737dcd1956bd0849c341aa7652325e9123d1d60fa0de4877d19baa689be868a` |
| Retail linked 61-word payload | `d21bbfe78a3f986521fae1730e3d828ad77e65e5bda98f6716bf6fddf4aeb760` |
| Qualified/production owner | `3ce3749fe9ce436c166a9882e7c13ecb4ccddf97ba6d48c7d7fe1aabfbb71b27` |
| Predecessor linked ELF | `05f576c5a18f61aaf0ce0b703ab593cb1c01923159d971a7b4da37c81c0c8e39` |
| Qualified/production linked ELF | `d40a3b3f73d4802ac72ca9a990b6222bed99d88931911ca1b3dd5861af9d94e1` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `dd2518e2b31669cd85237eb72b3fc24d79f59789301cd63d39b28551a2ae470f` |

## Semantic and production qualification

The big-endian guest oracle executes 23,040 connected cases across all modes,
descriptor width/height boundaries, signed heights, reflected/direct Y paths,
both helper outcomes and both stack phases. It reaches every semantically
executable retail word. Four words are statically unreachable: three dead
unsigned-halfword correction instructions and one branch-likely-annulled
duplicate load.

Native 32-bit O0/O2/O3 profiles each pass 5,760 independent cases, for 17,280
executions, with warnings as errors and UBSan trapping. Six compiled controls
independently reject wrong identity, width, height, reflection-mode,
projection-X and return behavior. All seventeen stale guard mutations, the
predecessor payload, target-body corruption and target-size corruption fail
closed.

The installed four-test suite passes in 65.222 seconds. Thirteen shared
progress, generated-PC16 and protected-layout tests pass in 12.363 seconds;
the six guarded-padder tests pass in 0.058 seconds. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` rebuilt the full corpus because the central guard
table is a dependency of every padded object. Compilation, assembly, linking
and binary generation completed; Make stopped only at the expected whole-ROM
SHA mismatch while the decomp remains incomplete. The production owner and
ELF equal their independently predicted qualified artifacts byte for byte. A
fresh production recount credits exactly this function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `8de60f1`. This is instruction-level and bounded semantic proof,
not natural whole-game or gameplay acceptance. The README changes only its
aggregate byte-exact rows. No Claude call was needed.

## Graph retention

The required bounded Graphify update produced a candidate graph with 58,383
nodes versus the retained 58,384. It failed closed without `force=True`,
preserving 31,816 nodes from 3,754 still-existing files outside the scan
corpus. The retained graph SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

The fresh ordinary Game ranking still keeps the six documented boundary cases
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside the direct-C queue. The next
ordinary candidate is `func_1507F54C` (61 words, 60 current real differences),
followed by the other 60-difference ties. Every candidate still requires
source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
