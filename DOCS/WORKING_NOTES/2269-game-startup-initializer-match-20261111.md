# Startup initializer byte match

Date: 2026-11-11. `func_1500E470` replaces the zero-return placeholder in
`conker/src/game_3B920.c`. The original remains in
`conker/asm/nonmatchings/game_3B920/func_1500E470.s`. Its 84-word body spans
VA `0x1500E470..0x1500E5C0`, ROM `0x3B920..0x3BA70`, with a 0x18-byte frame.
The semantic C resets startup globals, clears a 24-byte area, invokes the
initialization helpers in order, dispatches an optional category callback,
and submits the inverted `0x80` flag. Five expected-word guards normalize two
closed temporary-register cycles; no volatile accesses were introduced.

Twelve bounded guest cases visit all 84 original words and compare retail,
compiled C and normalized memory, helper calls and preserved registers. SDK32
native O0/O2/O3 each pass 12 cases and eight negative controls. Twelve cases
exercise the original `func_15007B3C` caller window and its special category
path; complete parent execution remains unqualified. Thirty cases connect the
original `bzero` and category helper; the other helpers remain modeled.
An aligned ROM census found one direct JAL at `0x35454` and no aligned entry
address literal. Arbitrary helper side effects, full caller behavior,
hardware faults and concurrency are not qualified.

Both object padders agree with independently assembled retail code after the
five guards. Twelve rebased GNU links, 45 bounded access-cut triples and 137
raw, binding or guard corruption rejections pass. Actual Make and an
independent strict image comparison account for **280 changed bytes**
with zero exclusions; two named metadata symbol-order cycles are recorded in
the manifest. All 6,050 function addresses and 189,088 protected data bytes
remain unchanged. The actual ELF SHA-256 is `acc4c232e70ab19ac3fdd51a2488490d2a416aac72b86de12560a2782868a038`. The
existing complete-ROM checksum mismatch remains.

Fresh actual ELF recount: **4,337 / 5,513 (78.67%)** overall and **3,664 /
4,840 (75.70%)** Game, zero drift and 1,176 different. The 80% target needs
74 more exact functions. Tools were committed first as
`7da8683e6a9d0df0bcb8d401a681c96ce3ec99f6`; the consumer change is separate.

[Note 2268](2268-initializer-declarations-and-startup-audit-20261111.md)
records the separate unresolved cross-translation-unit declaration inconsistency
for `D_800BE4E0` and `func_150ADA20`; this startup match does not resolve it.
