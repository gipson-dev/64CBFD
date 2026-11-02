# 2006 - Curve/timer callback matched as guarded C

Verified 2026-11-02. Production **4,073/5,511 (73.91%)**; Game
**3,400/4,838 (70.28%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,438 different; one placeholder is replaced by recovered C and is
newly byte-exact. The active 80% target is **4,409/5,511**, requiring **336
more**. This is progress toward that goal, not completion.

## Semantic recovery and callback interface

`func_15131DEC` is the 248-byte/62-word scale, curve-byte and bounded-timer
callback at VA `0x15131DEC` and ROM `0x15F29C` in
`conker/src/game/generated_15D730.c`. Its recovered O32 interface is:

```c
s32 func_15131DEC(u8 *record, s32 event);
```

The function derives a paired scale from the square root of `record+0xA8`
and the multiplier at `record+0xB0`, evaluates an unsigned-byte quadratic
curve from `record+0xB4` and `record+0xB8`, advances the timer by
`D_800BE9A4`, and returns whether the updated timer remains within the limit
at `record+0xAC`. The event argument is part of the callback ABI but is not
consumed by this implementation. The source comment describes the recovered
behavior without inventing a retail symbol name.

The strongest semantic provenance is the already-exact `func_150F3214`, which
has the same square-root scale, unsigned-byte curve and timer/limit sequence
after its own prefix. No aligned direct JAL targets exist. The callback is
installed in the original table in `conker/asm/data/22E220.rodata.s` at ROM
`0x22E2BC` / data address `0x800897FC`, preserving the two-argument dispatcher
contract.

## Guarded compiler closure

Fresh IDO emits the correct 62 words, frame-zero shape and both
`D_800BE9A4` relocations. Only one independent commutative floating multiply
differs: raw C emits `0x46002302` at `+0x024`, while retail emits
`0x46040302`. One checked expected-word replacement preserves the retail
operand order. There are no omissions or insertions, and the HI16/LO16
bindings remain at `+0x0BC` and `+0x0C4`.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `dbe6282751fff3f118faed719faa2acaac7e6be94597551bc51e539c0320ad48` |
| Qualified/production owner | `a69e8f0c816cb9e4860e40a15648f814d075c519f2074436a14385ab34593dbd` |
| Qualified/production linked ELF | `c46e4ee1a389a91913bc5a3a9b8279caabba33aff233e073c91e3317d122e260` |
| Raw candidate object | `e0ec7b930f0399db0b848cdcbd234ff153a3b03cf1160dde404e6984d43cb1b4` |
| Raw candidate linked slot | `aadbeb831f2d7023849238973a0eacc407d6c95fc30f16349bd2dc640c344204` |
| Retail/guarded slot | `c83255773ddb4fd4113dbaa3632e7018ce47ce7dc401b60b358e971112cb3468` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Guard manifest | `f40f594794e6bedfdb6de2f3c3b41bebf96866d28cdddecc660518522c103cbf` |

## Semantic, owner and image qualification

Eight permanent tests pass in 58.550 seconds. The guest corpus exercises
1,080 finite cases plus 128 alias, event and FCSR cases, or 1,208 cases and
2,416 retail/candidate executions, covering at least 60 of 62 retail words.
Native O0, O2 and O3 execute 384 cases each with four effective negative
controls per profile. The callback table word is checked exactly, and a stale
expected-word guard fails closed.

The owner contains 31 functions; all 30 neighbors remain byte-for-byte
unchanged. Strict whole-image closure covers all 6,051 functions, changes only
the target body, keeps every address fixed, uses zero exclusions and accounts
for the symbol-size change from the former 12-byte placeholder to the recovered
248-byte function. Actual Make reproduced the qualified owner and predicted
linked ELF byte-for-byte. The full `make -C conker all -j2` build regenerated
the corpus, linked the development ELF and ROM, and failed only the expected
final retail SHA-1 check because the wider decomp image is not yet
byte-identical.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Converted-C totals do not change because the former placeholder was already in
the generated C inventory. This is instruction-level and bounded semantic
proof, not a claim of natural whole-game effect acceptance.

The permanent experiment and qualification suites were committed first in the
tools submodule as commits `fb1c607` and `ae2bbda`. The retained qualification
stage is `conker/build/game-curve-timer-15131DEC-guard-match/`. The root README
changes only its aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,101 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Do not repeat
the parked `func_15163FEC` or `func_15164134` compiler-exit investigations.
Keep handwritten/custom-ABI `func_150A76F0` and `func_151F8870` on separate
tracks, and leave `func_1514E920` parked. Keep every new candidate private
until its ABI, semantic, caller, owner, actual-Make, whole-image,
protected-data, recount, documentation and graph-retention gates pass.
