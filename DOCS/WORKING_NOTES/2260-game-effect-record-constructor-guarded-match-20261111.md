# Effect-record constructor guarded byte match

Date: 2026-11-11. `func_151580B0` restores an effect-record constructor in
`conker/src/game/generated_185560.c`; original assembly remains in
`conker/asm/185560.s`. Its 74-word body occupies VA
`0x151580B0..0x151581D8` and ROM `0x185560..0x185688`, with a retail 0x38-byte
frame. Two expected-word guards move the loop pointer increment and zero store
into their retail positions. This is a guarded match, not a direct C match.

The constructor allocates a record, copies 0x44 source bytes, initializes its
fields and four slots, and conditionally allocates slot entries using the live
`D_80082FA0` bound, followed by a trailing object. The second argument is an
entry count: the connected allocation helper multiplies it by 96. An old-style
C definition preserves default argument promotions at an existing unprototyped
caller; changing to narrow prototyped parameters changes that caller's code
and invalidates its existing guards. Names reflect observed behavior and do not
claim a complete higher-level object identity.

Validation covers 896 guest cases (2,688 original/raw/normalized executions),
all 74 retail words, and 896 defined SDK32 cases per O0/O2/O3 with UBSan and
ten effective negative controls. Both original callers have 448 bounded-window
cases each. Another 128 cases connect original `memcpy`, entry-allocation, and
trailing-object helper instructions; allocators and zeroing remain modeled.
Tests use bounded table sizes and exclude overlapping copies. The complete
second caller, arbitrary allocator behavior, callback aliases, raw private-stack
fault state, and portable fault equivalence are not qualified.

Both padders match independently assembled retail code. Qualification rejects
308 corrupt byte/binding inputs and two individually corrupted guards, and
passes 16 rebased links and 168 access-cut quads. Actual Make and independent
complete-image comparison account for **221 changed bytes** with zero
exclusions; 36 neighboring functions, all 6,050 function addresses, and
189,088 protected data bytes remain unchanged. The actual ELF SHA-256 is
`f194c1fbed535a6f56a781a13c0c958e923f83fb8571c4600c2e538ec0e99d19`. Existing full-build checksum mismatch remains; this
function match does not imply a matching complete ROM.

Fresh actual ELF recount: **4,329 / 5,513 (78.52%)** overall and **3,656 /
4,840 (75.54%)** Game, zero drift and 1,184 different. The 80% target needs
82 more exact functions. Tools were committed first as
`05a0232516006812f7a6314514a3e7cfb7280dc4`; the consumer change is separate.
