# 2013 - Dependency record status query matched as guarded C

Verified 2026-11-02. Production **4,081/5,511 (74.05%)**; Game
**3,408/4,838 (70.44%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,430 different; one zero-return placeholder is replaced by qualified
semantic C and is newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **328 more**. This is progress toward that goal, not completion.

## Recovery and interface

`func_1509D08C` is the 61-word, frame-zero dependency-record status query in
`conker/src/game/generated_C9EC0.c`. Its retail address is `0x1509D08C` and
its ROM offset is `0xCA53C`.

The recovered routine indexes the live `D_800D2FB0` record table with the
retail eight-byte stride and reads the record pointer at entry offset `+8`.
Missing table or record pointers return false while writing the retail
defaults `0xBF` and zero to non-null output pointers. A live record optionally
returns its signed primary and secondary values, then scans every dependency
halfword against the packed `D_800D2E4C` availability bitmap. It returns true
only when every dependency bit is active.

The record pointer is deliberately reloaded after each optional output store.
That preserves retail behavior when either output aliases the table or record
storage and the store changes the next live read. The first ABI argument is
retained even though this routine does not consume it. Two original callers at
ROM offsets `0x20CC30` and `0x2105C0` validate the four-argument O32 interface,
optional outputs, and boolean result use.

## Guarded compiler closure

The owner's actual Make profile is IDO `-O2 -g3 -Wo,-loopunroll,0`. Using a
generic O2 profile is not equivalent: it can overflow the neighboring
`func_1509CA98` slot, so both qualification and production use the owner profile.

IDO naturally emits the complete 61-word extent, frame-zero interface, output
reloads, dependency scan, branches and delay slots. Twelve words differ from
retail at offsets `0x014`, `0x094`, `0x098`, `0x09C`, `0x0B0`, `0x0B4`,
`0x0B8`, `0x0BC`, `0x0C0`, `0x0C4`, `0x0C8`, and `0x0D4`. The first is an
equivalent address-add operand order; the remaining eleven form one closed
loop register-allocation and scheduling cycle.

Twelve checked expected-word replacements normalize that compiler output.
No row inserts or omits an instruction, and none has a relocation transition.
Original linking plus two independent rebases reproduce all expected linked
words. Independent expected-word and expected-relocation mutations produce 24
fail-closed cases.

| Artifact | SHA-256 |
| --- | --- |
| Raw candidate object | `1080d67de99f2cd2ef2963b299763b6715d462d56962fffd6604be40fba2b95b` |
| Isolated guarded object | `c0cee784ada086dba9ec6d0c7ee8f4e96f6ad938ab6bdf547d97a1c137114c3f` |
| Qualified guard manifest | `e211cce12f3b3575cc5536716bba257a34a131bf3736a10ef3d5e670b2628e93` |
| Qualified/production owner | `3214e08d0f2e6e92776d6e41b0c4ea26ff34cd73c461055e2e66e8fc97d50953` |
| Qualified/production linked ELF | `0b497dd3c564ccb9f49634ad86e30c448ab40446f34d1292a5e9f85b95b172b0` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |

## Semantic, owner and image qualification

Six permanent tests pass. Thirty-four guest cases execute retail, raw
candidate and guarded programs for 102 executions, covering all 61 words.
They include null table/record paths, optional outputs, empty and multi-entry
dependency lists, active and missing bits, boundary resource IDs, and two
output-alias cases that require the live record reloads. Native O0/O2/O3 and
UBSan controls pass; eight effective negative implementations are rejected.

The qualified owner is byte-identical to the production
`generated_C9EC0.c.o`, and every non-target owner function remains unchanged.
Both original caller windows pass. Strict whole-image prediction permits only
the 244-byte target slot and its symbol extent to change, keeps every address
fixed, and uses zero exclusions. The production dependency-corpus rebuild and
link reproduce the predicted owner and ELF.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The permanent experiment and qualification suites were committed first in the
tools submodule as `701c853`. The retained qualification stage is
`conker/build/game-dependency-record-status-1509D08C-guard-match/`. This is
instruction-level and bounded semantic proof, not natural whole-game or
gameplay acceptance. The root README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,140 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep every
new candidate private until source, ABI/callers, owner, guest/native, actual
Make, complete image, protected-data, production recount and documentation
gates pass.
