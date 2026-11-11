# Actor position pair direct byte match

Date: 2026-11-11. `func_15195528` replaces a zero-return placeholder in
`conker/src/game/generated_1C1150.c`; original assembly remains in
`conker/asm/1C1150.s`. Its 74-word body spans VA
`0x15195528..0x15195650` and ROM `0x1C29D8..0x1C2B00`, with a 0x58-byte
frame. The C compiler emits all original words directly, with no new guards.

The callback obtains an angle from the optional source object or the actor,
converts it with the global scale, and uses a direction helper to build two
positions around the actor before calling a submission helper. Entry 27 of
`D_80086694` points to this function; two original dispatchers call through the
same table. The actor is dereferenced later even on the original both-null
branch, so normal C execution is qualified only with a non-null actor. The
existing compiler warning elsewhere in the same owner is unchanged.

Validation covers 108 finite guest cases and one bounded null-actor unmapped
read, reaching all 74 retail words, plus 108 defined SDK32 native cases per
O0/O2/O3 with UBSan and ten effective negative controls. Twenty-four cases
cover the two original dispatcher windows. Twelve connected cases execute the
22-word original direction helper; sine, cosine, and final submission remain
modeled. Tests include identical source and actor pointers. Results cover
finite values under nearest rounding, not all hardware FCSR modes, NaNs,
infinities, full parent dispatchers, arbitrary helper
behavior, or portable fault behavior.

Both object padders match independently assembled retail code and pass 16
rebased GNU links and 72 bounded access-cut comparisons. Actual Make and a
strict complete-image comparison account for **242 changed bytes**, including
one explicitly modeled two-symbol ordering swap, with zero exclusions. All
28 neighboring functions, 6,050 function addresses, and 189,088 protected data
bytes remain unchanged. The actual ELF SHA-256 is `7ae9fc30c944baa7781ba9d8cdae9227a65a7ad5d54d3e81123cf7a293c00896`.
The existing full-build checksum mismatch remains; this function match does
not imply a matching complete ROM.

Fresh actual ELF recount: **4,331 / 5,513 (78.56%)** overall and **3,658 /
4,840 (75.58%)** Game, zero drift and 1,182 different. The 80% target needs
80 more exact functions. Tools were committed first as
`965fdb07f544bb0762fd6bf280dee1b72b4a764c`; the consumer change is separate.
