# 2005 - Scalar position/velocity smoother matched as guarded C

Verified 2026-11-02. Production **4,072/5,511 (73.89%)**; Game
**3,399/4,838 (70.26%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,439 different; one placeholder is replaced by recovered C and is
newly byte-exact. The active 80% target is **4,409/5,511**, requiring **337
more**. This is progress toward that goal, not completion.

## Semantic recovery and interface

`func_150495B0` is the 216-byte/54-word scalar position/velocity smoother at
VA `0x150495B0` in `conker/src/game/generated_76A60.c`. Its recovered O32
interface is:

```c
void func_150495B0(f32 *position, f32 target, f32 *velocity, f32 strength,
                   f32 damping, f32 deltaTime);
```

The function computes the signed target difference, scales that difference by
the requested strength, damps the current velocity toward it, integrates one
time step and clamps an overshoot to the target while clearing velocity. The
source comment names that behavior without inventing a retail symbol name.
The adjacent `func_15049688` placeholder remains unchanged.

There are 67 aligned direct JAL references across 22 functions in 18 assembly
owners and no function-pointer literals. The caller corpus confirms the six
O32 arguments, including the fifth and sixth floating arguments on the stack,
and preserves the retail pointer mutation and overshoot contract.

## Guarded compiler closure

Fresh IDO emits a 220-byte/55-word raw candidate with a 16-byte frame. Retail
uses a 216-byte/54-word slot and a 24-byte frame. Twenty-three checked rows
close that compiler-layout gap: 22 replace existing scheduling, frame or
register-allocation words and one omits the candidate-only nop at `+0x08C`.
There are no inserted words and no relocations in either slot.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `f513df5a777677b9ecd6da36d1bd009619d1131e8804559530709160d17323c2` |
| Qualified/production owner | `b0e7cb2835913956e5a4cfddf92e6ba5aa2f2fd77717a054d176faae7e5bb802` |
| Qualified/production linked ELF | `dbe6282751fff3f118faed719faa2acaac7e6be94597551bc51e539c0320ad48` |
| Raw candidate slot | `0ab6c7e108330c06f91011f6e58ada22f91b06a5235ab1f1bd4ede4e72ac164f` |
| Retail/guarded slot | `fd407656aa97f156766f9272be44befed09a21737c2595cc9edb107a19735a80` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Guard manifest | `fa105e7075ce37ffb5ef4ac904eae75570de7e4dfcbf06a332f410823117d819` |

## Semantic, caller and image qualification

The permanent suites contain nine tests. Guest differential execution covers
1,072 cases and 2,144 candidate/retail runs, reaching 52 of the 54 retail
words. Native O0, O2 and O3 controls each execute all 536 generated cases plus
eight independent controls. Three caller windows cover five callsites with
3,216 window executions and 5,360 calls plus six controls. These cases include
positive and negative motion, zero and nonzero velocity, exact arrival,
undershoot, overshoot and stack-argument variation.

The real owner preserves its sole adjacent function byte-for-byte. The strict
full-image prediction changes only `func_150495B0`, keeps all 6,051 function
addresses fixed and uses zero exclusions. Actual Make reproduced the qualified
owner and predicted linked ELF byte-for-byte. The full
`make -C conker all -j2` build regenerated every object, linked the development
ELF and ROM, and failed only the expected final retail SHA-1 check because the
wider decomp image is not yet byte-identical.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Converted-C totals do not change because the former placeholder was already in
the generated C inventory. This is instruction-level and bounded semantic
proof, not a claim of natural whole-game effect acceptance.

The permanent experiment and qualification suites were committed first in the
tools submodule as commits `a0df024` and `a6a582d`. The retained qualification
stage is
`conker/build/game-scalar-velocity-smoothing-150495B0-guard-match/`. The root
README changes only its aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,089 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep the
handwritten/custom-ABI `func_150A76F0` and `func_151F8870` tracks separate,
and leave the currently parked `func_1514E920` recovery private. Keep every
new candidate private until its ABI, semantic, caller, owner, actual-Make,
whole-image, protected-data, recount, documentation and graph-retention gates
pass.
