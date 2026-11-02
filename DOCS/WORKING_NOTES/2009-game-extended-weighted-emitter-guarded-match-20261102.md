# 2009 - Extended weighted emitter matched as guarded C

Verified 2026-11-02. Production **4,076/5,511 (73.96%)**; Game
**3,403/4,838 (70.34%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,435 different; one existing semantic C routine is newly byte-exact.
The active 80% target is **4,409/5,511**, requiring **333 more**. This is
progress toward that goal, not completion.

## Existing semantic recovery and callback contract

`func_150E9178` is the code-0x36 extended weighted emitter at VA
`0x150E9178` and ROM `0x116628` in
`conker/src/game/generated_113D60.c`. Its recovered O32 interface remains:

```c
void func_150E9178(u8 *record);
```

The semantic body was recovered and qualified in
[Note 957](957-game-extended-weighted-emitter-semantic-recovery-20261004.md).
It obtains the current-player origin, advances the rate/variation accumulator,
selects a descriptor from the weighted linked list, asks `func_1514470C` for
the selected world position, and applies the strict squared-distance limit.
Each in-range attempt creates a code-0x37 child through `func_15149130` and
copies the complete 60-byte extended position payload when allocation succeeds.

The callback table still maps code `0x36` to `func_150E9178` and code `0x37`
to the connected child callback `func_150E93DC`. The contract deliberately
preserves strict accumulator, selection and distance comparisons; callback-
sensitive reloads; unsigned duration residues; allocation-failure progress;
and the retail payload's 22 unspecified bytes. No null-list guard, clamp,
normalization, payload clearing or invented retail name was added.

## Guarded compiler closure

Fresh IDO emits the complete 153-word body with a `0xF8` frame. Retail uses a
`0xF0` frame. The raw semantic body has 54 linked word differences caused by
the frame displacement, saved-register allocation, local placement and the
resulting instruction schedule. Exactly 54 checked expected-word replacements
close that compiler-layout cycle; there are no omissions or insertions.

Fourteen guard rows cross relocation-bearing compiler positions. Their
expected and replacement relocation metadata is checked explicitly, so the
normalization remains valid after three independent links with different code
and data addresses. Every expected-word and expected-relocation field was
mutated independently: all 108 stale forms fail closed.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `b8717679215b85d1a3cb5cad066dd5db772d3fa1b4a0747590f8b74eb343a969` |
| Qualified/production owner | `193650d008d5dbe80b91538f0490b1b7c32820577ee3a170056c145740e8280f` |
| Qualified/production linked ELF | `5c704119b6044bdd78458bc9350a0225369d75bc3b7c52502f50cea597cc68d4` |
| Raw candidate object | `2091339b11e2df24a14f60649f9390b6388b0940daabad7e2e492967f33a7a86` |
| Raw linked 153-word body | `ef319998a5e6c55e5fa3e2808e82e710c7c49d01dfaef2bb0fd50ff886ec8b24` |
| Retail/guarded 153-word slot | `45ace35c4425986241dcc0f016d7654248990ee2a5e014c04fd47ca1447475ae` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Guard manifest | `ba8282b999174adbc2c6ceece203eead34978e6d1a9d4531f3c73e0cd2a23bc5` |

## Semantic, owner and image qualification

Thirty permanent tests across the emitter, guarded closure and connected child
suite pass in 10.954 seconds. They retain the semantic boundary cases from the
earlier recovery, prove complete 153-word retail closure, verify the original
link plus three independent rebases, and exercise all 108 fail-closed guard
mutations. The connected child suite remains bounded independently; this match
does not credit its still-different 208-word slot.

The owner contains 29 functions; all 28 neighbors and their relocations remain
byte-for-byte unchanged. Strict whole-image prediction changes only this
612-byte target slot, keeps every address fixed and uses zero exclusions.
Actual Make reproduced the qualified owner and predicted linked ELF
byte-for-byte. The global guard dependency rebuild recompiled the complete
generated corpus, audited every existing row without a stale-guard failure and
linked successfully. The full `make -C conker all -j2` pipeline regenerated the
development ROM and stopped only at the expected final retail SHA-1 mismatch
because the wider decomp image is not yet byte-identical.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe611f5be9c941575f87b341a77d808004603ac1cb87c670`.
Converted-C totals do not change because this function already had semantic C.
This is instruction-level and bounded semantic proof, not natural whole-game
effect, rendering or gameplay acceptance.

The permanent experiment and qualification suites were committed first in the
tools submodule as commit `5576e95`. The retained qualification stage is
`conker/build/game-extended-weighted-emitter-150E9178-match/`. The root README
changes only its aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,114 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep the
connected code-0x37 child callback in the unmatched queue until its own
compiler closure passes, keep parked handwritten/custom-ABI work on its
separate track, and keep every new candidate private until all qualification
gates pass.
