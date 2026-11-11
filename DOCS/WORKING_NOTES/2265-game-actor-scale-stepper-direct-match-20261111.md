# Actor scale stepper direct byte match

Date: 2026-11-11. `func_15053750` replaces a zero-return placeholder in
`conker/src/game_77AD0.c`; original instructions remain in
`conker/asm/nonmatchings/game_77AD0/func_15053750.s`. Its 81-word body spans
VA `0x15053750..0x15053894` and ROM `0x80C00..0x80D44`, with a 0x18-byte
frame. All words emit directly from semantic C with no new guards.

With a nonnegative configured step, the function moves an actor's horizontal
and vertical scales toward their respective target values. If a nonzero
difference is smaller than the step, it passes the target to the existing
scale helper; otherwise it moves by a signed step. It reloads actor state
after the first helper call. The C keeps
the original order of the floating additions. The original caller at
`0x15052634` supplies the actor in the delay slot and does not use a return
value; the prior placeholder declaration was corrected to `void`.

The bounded guest suite covers 36 finite-value cases and 79 executed words;
two duplicate instructions at `0x150537A8` and `0x15053844` were unvisited.
SDK32 native O0/O2/O3 each pass 28 finite cases with UBSan and eight effective
negative controls. Eighteen bounded cases exercise the original caller window.
Eighteen more connect the complete 77-word original `func_15062BDC` helper
across actor IDs 255 and 3; its two nested helpers remain modeled. Special
floating values, nondefault FCSR, arbitrary helper side effects, complete
parent functions, hardware faults, and concurrent access are not qualified.

Both object padders and an independent assembly agree with the raw C object;
16 rebased GNU links and 42 bounded access-cut quads pass. Actual Make and
the independent strict image comparison account for **232 changed
bytes** with zero exclusions. All 57 neighboring functions, 6,050 function
addresses, and 189,088 protected data bytes remain unchanged. The actual ELF
SHA-256 is `ebc101e712dd71da2cb47ac8514d37e6e79ea20ef492e692d8eb9a3ca62f320e`. The existing complete-ROM checksum
mismatch remains.

Fresh actual ELF recount: **4,334 / 5,513 (78.61%)** overall and **3,661 /
4,840 (75.64%)** Game, zero drift and 1,179 different. The 80% target needs
77 more exact functions. Tools were committed first as
`0ab1db5648252ecd13c895b51dad7b25a4368203`; the consumer change is separate.
