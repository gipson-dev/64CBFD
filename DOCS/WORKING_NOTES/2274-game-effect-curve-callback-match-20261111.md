# Effect-curve callback byte match

Date: 2026-11-11. `func_151A175C` replaces the zero-return placeholder in
`conker/src/game/generated_1CC440.c`; original assembly is in
`conker/asm/1CC440.s`. Its 96-word body spans VA `0x151A175C..0x151A18DC`,
ROM `0x1CEC0C..0x1CED8C`.

The C callback applies age-dependent intensity and size curves and advances
three packed 24.8-style fixed-point coordinates using the global tick. The
curve's low halfwords are signed when forming velocity, and the arithmetic
uses unsigned low-word operations to preserve retail wrapping. The callback
has a void interface; both qualified dispatcher windows ignore its incidental
register result.

The compiler emits 96 raw words with 75 expected-word guards normalizing
register allocation and instruction scheduling. The complete guarded body
and its relocation bindings match retail. This is not an unguarded C match;
the raw C and guarded output are checked separately.

A bounded oracle compared retail, raw C and guarded output in 392 cases,
including signed and 32-bit wrapping boundaries, and visited all 96 retail
words. Native SDK32 O0/O2/O3 each passed those 392 cases and 13 negative
controls with undefined-behavior sanitization. Both original dispatch windows
(`func_15167E0C` and `func_15168870`) passed 784 cases combined through
`D_8008C9C8[16]`; the complete parent functions are not qualified. Inputs use
valid aligned, disjoint record and tick storage. Arbitrary aliasing, concurrent
mutation, hardware faults and broader dispatcher behavior are not qualified.
A read-only external advisory request timed out and provided no review result.

Both padders agree with independently assembled retail code and bindings;
12 rebased GNU links, 46 bounded access-cut triples and 175 corruption
rejections pass. Actual Make and strict independent image comparison account
for **270 changed bytes** with zero exclusions. All 6,050 function
addresses and 189,088 protected data bytes remain unchanged. Actual ELF
SHA-256: `6f8b37d69c632b718eafb85441b1ee07a5c452c6ea74f34d8a918590a9ce26d0`. The existing complete-ROM checksum mismatch
remains.

Fresh actual ELF recount: **4,342 / 5,513 (78.76%)** overall and **3,669 /
4,840 (75.81%)** Game, zero drift and 1,171 different. The 80% target needs
69 more exact functions. The tools commit `35ed67a8ad3693632b9ab7d2f9b269bb3380d888`
precedes the consumer change.
