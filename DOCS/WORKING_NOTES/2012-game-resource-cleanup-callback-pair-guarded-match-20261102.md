# 2012 - Resource-cleanup callback pair matched as guarded C

Verified 2026-11-02. Production **4,080/5,511 (74.03%)**; Game
**3,407/4,838 (70.42%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,431 different; two zero-return placeholders are replaced by qualified
semantic C and are newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **329 more**. This is progress toward that goal, not completion.

## Recovery and callback contract

`func_151C94D4` and `func_151C95D8` are twin 65-word, frame-24 resource-cleanup
callbacks in `conker/src/game/generated_1F4650.c`:

| Function | VA | ROM | Registration pointer | Finalizer |
| --- | ---: | ---: | ---: | --- |
| `func_151C94D4` | `0x151C94D4` | `0x1F6984` | `0x22E9D0` | `func_1513CA6C` |
| `func_151C95D8` | `0x151C95D8` | `0x1F6A88` | `0x22EA04` | `func_1513CAA0` |

Both callbacks receive the owner pointer in `a0`. If the live slot at owner
offset `0x13C` is non-null, they release that resource and unregister
`func_151C87AC` for the embedded state at owner `+0x110`. They then reload and
conditionally release the eight live resource slots spanning owner offsets
`0x144` through `0x160`, in retail order, before invoking the callback-specific
owner finalizer. The repeated source loads are intentional: they preserve the
retail callback-clobber and alias behavior instead of caching speculative
state.

The retail ROM contains the expected callback pointers at `0x22E9D0` and
`0x22EA04`. The permanent qualification checks those registration locations,
the O32 callback ABI, every null/non-null resource path, release ordering,
unregistration, finalizer selection, and callback side effects.

## Guarded compiler closure

IDO naturally emits all 65 words, every branch and delay slot, the complete
frame and saved-register lifetime, and all call bindings for each callback.
Each candidate differs from retail only at offsets `0x020`, `0x040`, `0x044`,
and `0x048`. Those four words form the same closed `s0`/`t8` owner-reload
register-allocation cycle in both functions.

Eight checked expected-word replacements normalize that compiler allocation:
four rows per callback. No row inserts or omits an instruction, and none has a
relocation transition. Original linking plus two independent rebases reproduce
the expected linked words. Independent mutation of every expected word and
expected-relocation field produces 16 fail-closed cases.

| Artifact | SHA-256 |
| --- | --- |
| Raw candidate owner | `823a9c06aa70fcec73722b76ea099a73d6cea619a93ebd974724b958b492270b` |
| Guard manifest | `8cf18d83b41005e90b9786c5a5c9be7a9cf6a7276e4e69ebbe99874ddbb3491b` |
| Qualified/production owner | `dfe0addfbf14fc35964f6c48833dc297c2b519a55e00a8b8afeb0c63508cabfd` |
| Qualified/production linked ELF | `d27cb68aab00047e05464897b9a1aa00bd9b913243b20f12c43cb1a5c9261b57` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |

## Semantic, owner and image qualification

Six permanent tests pass (latest run: 12.878 seconds). The guest corpus covers
**618 cases per function / 3,708 executions** across retail, raw candidate, and
guarded programs, reaching all 65 words of each callback. Native O0/O2/O3 each
run 2,560 cases over 18 variants, for 138,240 executions total; eight effective
controls per function reject missing releases, stale-slot caching, wrong
ordering, failed unregistration, and wrong-finalizer implementations.

The qualified owner matches the production owner byte-for-byte. At least 40
non-target owner functions remain unchanged. Strict whole-image prediction
permits only the two 260-byte target slots and their symbol extents to change,
keeps every address fixed, and uses zero exclusions. The focused actual Make
build and complete dependency-corpus rebuild reproduce the qualified owner and
linked image. `make -C conker all -j2` compiles and links all Game, Init,
Debugger, generated, converted, and libultra inputs, stopping only at the
expected final retail SHA-1 mismatch because the wider decomp image is not yet
byte-identical.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe611f5be9c941575f87b341a77d808004603ac1cb87c670`.
The permanent experiment and qualification suites were committed first in the
tools submodule as `563f5bc`. The retained qualification stage is
`conker/build/game-cleanup-pair-151C94D4-151C95D8-guard-match/`. This is
instruction-level and bounded semantic proof, not natural whole-game cleanup
or gameplay acceptance. The root README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,134 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep
handwritten/custom-ABI work on its separate track, and keep every new candidate
private until source, ABI/callers, owner, guest/native, actual Make, complete
image, protected-data, production recount and documentation gates pass.
