# Descriptor-record constructor byte match

Date: 2026-11-11. `func_151A7950` replaces a zero-return placeholder in
`conker/src/game/generated_1D4E00.c`; the original remains in
`conker/asm/1D4E00.s`. Its 80-word body spans VA `0x151A7950..0x151A7A90`
and ROM `0x1D4E00..0x1D4F40`, with a 0x30-byte stack frame. Semantic C emits
79 retail words directly; one expected-word guard swaps the operands of a
non-trapping, commutative `addu` at offset `0xB0`.

The function requests a variable-sized record using the signed descriptor
count and caller-supplied byte count. On success it copies 0x50 descriptor
bytes, initializes the start and end vector fields, clears 0x10 bytes, and
derives a field from the copied count. It returns zero on allocation failure.
The descriptor count is reloaded after helpers as in retail; the copied count
used for the final field can therefore differ from the later source count.
Names describe observed behavior without assigning an unverified higher-level
purpose.

Validation covers 120 bounded guest cases reaching all 80 retail words,
including allocation success/failure, counts -1 through 3, and modeled
changes to the descriptor at helper boundaries. SDK32 native O0/O2/O3 each
pass 60 cases with UBSan and nine effective negative controls. Both original
call sites pass 12 bounded cases each, including their delay slots and the
second caller's result branch and nine-element descriptor. Original `memcpy`
and `bzero` execute in 40 connected cases; the outer allocator remains
modeled. Copy overlap, arbitrary out-of-bounds counts, complete caller
functions, hardware fault behavior, and concurrency are not qualified.

Both object padders agree with independently assembled retail code. The
checks reject 326 raw-byte or relocation corruptions and an altered guard,
and pass 16 rebased links and 193 bounded access-cut comparisons. Actual
Make and an independent strict full-image comparison account for **243
changed bytes** with zero exclusions. All 22 neighboring functions, 6,050
function addresses, and 189,088 protected data bytes remain unchanged. The
actual ELF SHA-256 is `a0544627ef17d69a35a8becf23da5f08d32ec461d2de2e3c0e437687d860806b`. The pre-existing full-build
ROM checksum mismatch remains.

Fresh actual ELF recount: **4,333 / 5,513 (78.60%)** overall and **3,660 /
4,840 (75.62%)** Game, zero drift and 1,180 different. The 80% target needs
78 more exact functions. Tools were committed first as
`473e73811d05eee5caf12a5ca823de1475292c59`; the consumer change is separate.
