# 2023 - Actor child-state finisher matched as guarded C

Verified 2026-11-02. Production is **4,093/5,511 (74.27%)**; Game is
**3,420/4,838 (70.69%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,418 functions remain different. The active 80% target is
**4,409/5,511**, requiring **316 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_1507FEA0` replaces its zero-return placeholder in
`conker/src/game/generated_AC030.c`. It is the actor child-state finisher at
`0x1507FEA0`, ROM `0xAD350..0xAD444`, owned by `generated_AC030`. Its recovered
interface is:

```c
void func_1507FEA0(u8 *actor);
```

The routine returns immediately when `actor + 0x31C` has no child or when the
actor marker at `+0x127` is `0xFF`. Otherwise it decrements the nonzero byte at
`+0x13A`, then operates on the child's state record at `+0x58`.

When state byte zero is one and `D_800C35EA` is not one, the unsigned count at
state `+2` advances by signed tick `D_800BE9E4` only while it remains below
retail's signed `0xFFFF - tick` bound. Every other state/player combination
clears the count and bytes `+4`, `+5`, `+0xC` and `+0xD`. This combined reset
condition is important: the original assembly clears the complete state both
for a non-one state and for player mode one.

The signed child timer at `+0x66` then counts down by the tick. Expiry calls
`func_1507FF94(actor)`, reloads the child pointer because that callback may
replace it, and clears the new child's timer. Every non-early path finally
calls `func_1507FC2C(actor)`.

There are two direct retail callers. The recovered `func_1502378C` call is at
ROM `0x50CD4`, with the actor move in its delay slot and the post-call
`actor->unk2FF = 1` store unchanged. The second call is at ROM `0x7A50C`
inside still-unconverted `func_1504CB98`; its actor move and following call
remain fixed. There are no aligned literal pointers equal to the function
entry.

## Guarded compiler and image closure

Retail-profile IDO emits the complete **61 words/frame24**, with the same
branches, calls and eight relocations. Fifteen natural word differences form
closed compiler allocation/scheduling cycles:

- six words reorder the countdown load, state-base setup and
  `D_800C35EA` HI16 load, moving that relocation from `+0x2C` to retail
  `+0x30` symbolically;
- five words normalize the unsigned count temporary registers;
- two words normalize the signed timer subtraction result; and
- two words normalize the reloaded child pointer used by the expiry clear.

Fifteen checked retail-word rows normalize only those cycles. There are no
insertions, omissions, assembly blocks, compiler-profile changes or Makefile
changes. The remaining relocations stay attached to `D_800C35EA`, both
`D_800BE9E4` accesses, `func_1507FF94` and `func_1507FC2C`.

All 15 other functions in `generated_AC030`, normalized owner pools, all
6,051 function addresses and the complete allocated image outside this
function remain fixed. Strict full-image prediction uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 61-word object payload | `02e668794fb1544bd1de43b0f509c7a19dc6e00b20a3d07c883e16235a6a6c20` |
| Retail linked 61-word payload | `5dbd06b4cd858bf4b29bf073a48425e792f2b3f0e5fcb38b8f3871e1b028db1b` |
| Qualified/production owner | `b96a75faaf8ae75a6bc5c84cedc963724f73ca2809322ab2a485f4b805ac498f` |
| Predecessor linked ELF | `07ad10cd6c8628054831ce3929ebb3ddd83f581853d415cef27953315c910a01` |
| Qualified/production linked ELF | `9b28d118b6f5e312f002dca0c717f2f6672772e676c85f934be7e97ce6fc9103` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `638b2495aea5f5259ae75aa57e07111ec7a3dd3d210602d9a0683e2c48c89dca` |

The natural object hash masks relocation immediates, while the retail body
hash is taken from the linked ROM, so those two hashes are intentionally not
equal.

## Semantic and production qualification

The raw big-endian guest oracle executes **2,308 cases** across both stack
phases, both early exits, zero/nonzero countdowns, all state/player gates,
count boundaries, signed timer and tick boundaries, and callback-driven child
replacement. It compares every external memory byte and both call sequences
against an independent reference while clobbering caller-saved integer and
floating registers at each helper. Every retail body word is reached.

Native 32-bit O0/O2/O3 profiles pass the bounded Cartesian corpus. Eleven
effective controls cover countdown, marker, state/player gates, count bound
and update, complete reset, timer comparison/update, child reload and final
helper; all fail as intended. The permanent four-test suite additionally
verifies both callers, all 15 stale-guard mutations, 15 owner neighbors,
literal full-image prediction, protected data and installed
source/object/image coherence. Together with the 19 shared progress, PC16,
padder and protected-layout tests, all **23 tests pass in 39.157 seconds**.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the complete guard-table dependency set,
linked `conker.us.elf` and produced `conker.us.bin`; it stopped only at the
expected whole-ROM SHA mismatch because the overall decomp is incomplete. A
fresh independent recount credits exactly this function.

The candidate screen, qualification module and tests were committed first in
the tools submodule as `49afb8c`. Retained stage:
`conker/build/game-actor-child-state-finish-1507FEA0-guard-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,220 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

Continue from the fresh ordinary Game ranking at `func_1514E920` in
`conker/src/game/generated_179F30.c`. Keep `func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68` and
`func_151AE2BC` outside an ordinary direct-C screen until their existing
boundaries are resolved. Every candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount and documentation gates before credit.
