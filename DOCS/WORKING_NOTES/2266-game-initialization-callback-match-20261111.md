# Initialization callback byte match

Date: 2026-11-11. `func_1500FFCC` replaces a zero-return placeholder in
`conker/src/game/generated_3D2E0.c`; original instructions remain in
`conker/asm/3D2E0.s`. The routine has a 79-word body at VA
`0x1500FFCC..0x15010108` and ROM `0x3D47C..0x3D5B8`, followed by two retail
alignment words. Its frame is 0x48 bytes. Semantic C emits the routine; 15
expected-word guards normalize a closed call-preparation schedule.

The callback makes two setup calls, invokes the existing initialization and
sound routines, and requests two optional records. It copies a zero-valued
word into the first successful record and a zero-valued pair into the second,
whose pointer is stored globally. It is index 12 of `D_80082D90`, reached by
the original `func_1500E470` dispatcher at `0x1500E55C`; the dispatcher does
not use its return value. The two alignment words remain intact. Local
allocator declarations describe the 32-bit argument slots used here; shared
headers use narrower parameters and have an unresolved type for the size-like
argument. The caller checks cover the concrete values used by this routine.
At this checkpoint, its `func_1500FE30` dependency is still a zero-return
placeholder and is being qualified separately.

The 15 guarded words reorder independent stack stores and argument-register
preparation before the same second allocation call. Both instruction streams
produce the same registers and stack slots when the call begins. The bounded
guest test covers 16 cases and all 79 retail words; the corresponding SDK32
native O0/O2/O3 tests each cover 16 cases with nine effective negative
controls. Eight cases exercise the original callback-table window. Sixteen
connected cases execute the original 12-word sound wrapper and 11-word copy
helper. An additional 16 connected cases execute both original allocator
wrappers; their inner allocator, zeroing and other helpers remain modeled.
Arbitrary helper effects,
complete parent execution, partial-fault register or stack state, hardware
fault behavior, and concurrency are not qualified.

Both padders agree with independently assembled retail code. Validation rejects
352 raw-byte or relocation corruptions and all 15 altered guards, and passes
16 rebased GNU links and 108 bounded access-cut comparisons. Actual Make and
the independent strict image comparison account for **252 changed
bytes** with zero exclusions. Both neighboring functions, 6,050 function
addresses, and 189,088 protected data bytes remain unchanged. The actual ELF
SHA-256 is `30b7fe0ab409914b3af920c44189511164c097e8a14b481fd89aeea7c470e9ed`. The existing complete-ROM checksum
mismatch remains.

Fresh actual ELF recount: **4,335 / 5,513 (78.63%)** overall and **3,662 /
4,840 (75.66%)** Game, zero drift and 1,178 different. The 80% target needs
76 more exact functions. Tools were committed first as
`e49fe5443984a48e2fb7b1ae57a8e720ab294172`; the consumer change is separate.
