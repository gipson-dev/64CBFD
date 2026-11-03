# 2015 - Actor point selector pair matched as guarded C

Verified 2026-11-02. Production **4,084/5,511 (74.11%)**; Game
**3,411/4,838 (70.50%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,427 different; two zero-return placeholders are replaced by qualified
semantic C and are newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **325 more**. This is progress toward that goal, not completion.

## Recovery and interface

`func_150BE9B0` and `func_150BEC30` are the paired 62-word, frame-`0x38`
actor-point selectors in `conker/src/game/generated_EBE60.c`. Their retail
addresses are `0x150BE9B0` and `0x150BEC30`; their ROM offsets are `0xEBE60`
and `0xEC0E0`.

Both accept an output position, an actor pointer, an optional height-query
result and an unsigned mode byte. The default actor-point index is `0x10`.
Mode 4 selects `0x17` in the first routine and `0x19` in the second; mode 5
selects `0x14` and `0x16`; mode 6 selects `0x0C`; mode 7 retains the default.
The default matters: retail initializes `0x10` in the mode-6 comparison delay
slot, so treating mode 7 as the adjacent `0x0F` point would be a semantic
misrecovery even if later compiler normalization hid the immediate.

Each routine resolves `actor->0x1D4` through `func_15142314`. A null result
pointer returns 1 after that point lookup. Otherwise it creates the local
`(x, y + 10.0f, z)` start point, initializes the result through
`func_1504715C`, and calls `func_15046C80` with a lower bound of
`position[1] - 50.0f`. The actor argument is deliberately volatile so the
incoming home and reload lifetime agree with retail. Direct JALs at ROM
`0xEBFAC` and `0xEC22C` bind the four-argument O32 contracts in
`func_150BEACC` and `func_150BED4C` respectively.

## Guarded compiler closure

IDO emits 61 words for each semantic body. Retail has 62 because its switch
schedule contains one additional branch-delay update. Seventeen checked rows
per routine close the switch/register-allocation cycle and insert that one
word at target offset `0x068`; the remaining code, including all three helper
calls, emits from C. Thus the pair uses 34 fail-closed rows and two insertions,
without changing either function extent, frame, helper binding or neighboring
owner bytes.

Two independent rebases reproduce every linked retail word. Mutating each
expected word and expected-relocation state produces 68 fail-closed cases.
Both guarded functions match all 62 words; the raw and guarded programs also
agree on all reachable instructions. The only statically unreachable retail
word in each function is the duplicate actor-home load at target offset
`0x090`, retained as part of the exact compiler schedule.

| Artifact | SHA-256 |
| --- | --- |
| Raw pair candidate object | `2e916b7f17627d40d209c0662f5d5ac8706ddad3c89c3899af36265838618f16` |
| First isolated guarded object | `4ef158971d788bef5d10a12dbd7c37fdab17e64355a1f77ffad61104e3b0402d` |
| Second isolated guarded object | `79ca3f217e433b49036fefb74b497fb79a599f36f9f7141fd2820ed1a49654cb` |
| Qualified/production owner | `c01b1fe4dae57c7f1692d5622f35f50900c0ebf3586d7a51d0bacd946410577b` |
| Qualified/production linked ELF | `74ef2147f9c4217a5911b758be66c15a734433329d77b54fbf34405367a5858e` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Production guard table | `48c25b8782a0a2c280b70da1826111f4e0167a120379b3b542f78af27fbf91c7` |

## Semantic, owner and image qualification

Four permanent tests pass. A 9,152-case guest corpus runs retail, raw and
guarded programs for 27,456 executions across both functions, including all
mode classes, null/non-null result paths, helper clobbers, actor/result/position
aliases and two independent rebases. Every reachable raw and retail word is
exercised. Native 32-bit O0/O2/O3 controls run 2,048 selected cases per
profile and reject six effective semantic mutants.

The original callers, helper contracts, owner neighbors and pools, symbol
inventory, allocated image and exact qualified/production owner comparison
pass. The actual Make rebuild traversed the full generated, converted and
libultra corpus because the shared guard manifest is a dependency, then linked
successfully. The fresh independent recount credits exactly these two
functions. Protected Game data remains exactly 189,088 bytes across 720
owners with zero different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The permanent experiment and tests were committed first in the tools
submodule as `fd7d4d2`; the installed-comment idempotency correction followed
as `9d53ec1`. The retained qualification stage is
`conker/build/game-actor-point-selector-pair-guard-match/`. This is
instruction-level and bounded semantic proof, not natural whole-game or
gameplay acceptance. The root README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update produced a 58,383-node candidate versus the
retained 58,384 and failed closed without `--force`, preserving 31,816 nodes
from 3,754 still-existing files outside the scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep every
new candidate private until source, ABI/callers, owner, guest/native, actual
Make, complete image, protected-data, production recount and documentation
gates pass.
