# 2030 - Linked-effect event dispatcher matched as guarded C

Verified 2026-11-03. Production is **4,100/5,511 (74.40%)**; Game is
**3,427/4,838 (70.84%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,411 functions remain different. The active 80% target is
**4,409/5,511**, requiring **309 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_151CD3CC` replaces its zero-return placeholder in
`conker/src/game/generated_1FA770.c`. It is the linked-effect event dispatcher
at VA `0x151CD3CC`, ROM `0x1FA87C..0x1FA970`, owned by `generated_1FA770`.
The recovered interface is:

```c
void func_151CD3CC(EffectLinkOwner151CD3CC *owner,
                   s32 *identity, u8 command);
```

The owner embeds a sixteen-byte link record at `+0x28`: source pointer,
identity, current effect pointer and variant byte. Command `0x17` creates the
effect only when the identity matches and no effect is active, passing source,
variant, identity, owner mode `+0x0C` and source kind `+0x01` to
`func_151CD4C0`. It stores the returned effect and clears byte `+0x14` on the
live source pointer. Command `0x18` retires a matching active effect through
`func_151CE47C`. Command `0x23` detaches a matching effect, clears the stored
pointer and sets source byte `+0x14`. Other commands and identity mismatches do
nothing. The source reload after the factory is intentional: a callback may
replace the link's source pointer before the byte clear.

There are no direct JAL callers. The only retail reference is callback-table
entry 30 in `D_8008A8D8`, stored at ROM `0x22F410`. The established generic
dispatcher `func_15149434` loads that entry and calls it as
`(owner, eventIdentityPointer, lowCommandByte)`, proving the narrowed command
ABI. The neighboring factory placeholder's declaration is corrected from an
integer return to `void *`; its unrecovered body remains unchanged and receives
no credit.

## Compiler and image closure

The semantic `-O2 -g3` body naturally emits 60 words with a 48-byte frame and
the two correct J26 bindings. Retail owns 61 words and a 64-byte frame. Ten
checked rows normalize only compiler layout: frame/home offsets, three forward
branch distances, one link-pointer spill/reload, and the closing epilogue.
One row moves the source-byte clear before an unconditional branch and inserts
the independent return-address reload in its delay slot. Both calls move
symbolically: `func_151CD4C0` remains at target offset `+0x05C`, while
`func_151CE47C` moves from natural `+0x0A0` to retail `+0x0A4`.

The guarded result matches all 61 retail words, frame 64 and both relocations.
All 51 other owner functions and normalized pools remain unchanged. Across the
linked image, only `func_151CD3CC` changes; all 6,051 function addresses remain
fixed, and strict comparison uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-masked 60-word payload | `7863f7af254e8fa0cb310b3f72b827ea999bc29b56050868fb61847ac1211902` |
| Retail linked 61-word payload | `ae92b1d194f2d66b8d470f3f726594e3a5c5fddbd963b801b5ee9170c66d32ff` |
| Qualified/production owner | `227a3a3a14f54dbf9f0b02fc9db8bbfe0efff57f7d25df644425a20da5abd115` |
| Predecessor linked ELF | `8998cb5660571804ab3e25b1e35b03b8aa2621a0d4a577f491a56757f8d959a0` |
| Qualified/production linked ELF | `05f576c5a18f61aaf0ce0b703ab593cb1c01923159d971a7b4da37c81c0c8e39` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `20024e16b65bb54d5bd415e126372b1295a8ccfee33dcee6596a871200e71de6` |

## Semantic and production qualification

The big-endian guest oracle executes 336 connected cases across the create,
retire, detach and no-op routes; full-width command values verify low-byte
narrowing. Matching/mismatching identities, active/inactive effects, aliased
identity pointers, both stack phases, two seed sets and factory source-pointer
mutation are covered. Every one of the 61 retail words executes, and all
observable memory and helper calls agree with the reference model.

Native 32-bit O0/O2/O3 profiles each pass 4,096 independent cases, for 12,288
executions, with warnings as errors and UBSan trapping. Twelve compiled
controls independently reject wrong command, identity, empty-effect gate,
source, variant, factory identity, owner mode, source kind, post-create byte,
retire command, detach command and detach byte behavior. All ten stale guard
mutations, the predecessor payload, target-body corruption, target-size
corruption and truncation fail closed.

The installed four-test suite passes in 73.858 seconds. The 19 shared progress,
generated-PC16, guarded-padder and protected-layout tests pass in 11.803
seconds. Protected Game data remains exact at 189,088 bytes across 720 owners,
zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` rebuilt the full corpus because the central guard
table is a dependency of every padded object. Compilation, assembly, linking
and binary generation completed; Make stopped only at the expected whole-ROM
SHA mismatch while the decomp remains incomplete. The production owner and
ELF equal their independently predicted qualified artifacts byte for byte. A
fresh production recount credits exactly this function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `b373b0c`. This is instruction-level and bounded semantic proof,
not natural whole-game or gameplay acceptance. The README changes only its
aggregate byte-exact rows. No Claude call was needed.

## Graph retention

The required bounded Graphify update extracted 24,246 nodes and 43,824 edges
from 2,862 collected files versus the retained 58,384 nodes. It failed closed
without `force=True`, preserving 31,841 nodes from 3,778 still-existing files
outside the reduced scan corpus. The retained graph SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. The
structural pass used zero LLM tokens and repeated the known one-file zero-node
warning for `devcontainer.json`.

## Continuation

The fresh ordinary Game ranking still keeps the six documented boundary cases
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside the direct-C queue. The next
ordinary candidate is `func_15035714` (61 words, 60 current real differences),
followed by the other 60-difference ties. Every candidate still requires
source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
