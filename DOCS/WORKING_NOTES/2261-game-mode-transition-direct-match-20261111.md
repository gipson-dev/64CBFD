# Mode transition direct byte match

Date: 2026-11-11. `func_1511172C` replaces a zero-return placeholder in
`conker/src/game/generated_13D350.c`; original assembly remains in
`conker/asm/13D350.s`. Its 75-word body spans VA
`0x1511172C..0x15111858` and ROM `0x13EBDC..0x13ED08`, with a 0x28-byte
frame. The C compiler emits all original words directly, with no new guards.

Mode 1 sets the current state byte to 1, conditionally releases the existing
block, and calls the transition helper. Other modes proceed only when the
requested value differs from the current byte and the state byte is 4. When
`D_80038080` is set, the routine invokes the cleanup helper for 360 successive
indices from the current mode's table entry. It then releases the current
block, stores the requested mode as a byte, and calls the setup helper. Global
pointer and table reloads retain their original timing. The names describe
observed operations; they do not establish the full higher-level subsystem.

Validation covers 256 guest cases reaching all 75 retail words, including
argument truncation and modeled helper mutations, and 256 defined SDK32 native
cases at each of O0/O2/O3 with UBSan and nine effective negative controls. Five
original call sites in `func_151645C4` passed 80 bounded-window cases; the
caller itself matches all 111 retail words. Six connected cases execute the
35-word original cleanup helper 2,160 times; its nested helper and the other
helpers remain modeled. This does not qualify arbitrary helper implementations,
the entire calling context, hardware fault behavior, or concurrent C accesses.

Both object padders match independently assembled retail code and pass 16
rebased GNU links and 128 bounded access-cut comparisons. Actual Make and an
independent strict complete-image comparison account for **229 changed bytes**
with zero exclusions. All 33 neighboring functions, 6,050 function addresses,
and 189,088 protected data bytes remain unchanged. The actual ELF SHA-256 is
`7a4e46277bed22c72d7ee984875dbeaeda150f909f65689eb3459d6d9850e0bb`. The existing full-build checksum mismatch remains;
this function match does not imply a matching complete ROM.

Fresh actual ELF recount: **4,330 / 5,513 (78.54%)** overall and **3,657 /
4,840 (75.56%)** Game, zero drift and 1,183 different. The 80% target needs
81 more exact functions. Tools were committed first as
`30805fc90c72446563b85d0f611cd7a4c0d82d62`; the consumer change is separate.
