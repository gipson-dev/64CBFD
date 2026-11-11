# Ten-entry table initializer direct byte match

Date: 2026-11-11. `func_1500FE30` replaces a zero-return placeholder in
`conker/src/game/generated_3D2E0.c`; its original remains in
`conker/asm/3D2E0.s`. The 91-word body spans VA `0x1500FE30..0x1500FF9C`
and ROM `0x3D2E0..0x3D44C`, with a 0x30-byte frame. All words emit directly
from semantic C with no new guards.

The routine allocates and clears 100 bytes for ten ten-byte entries. It sets
each entry's group, marker and random choice, invokes the existing target
randomizer, then copies each target halfword into the corresponding previous
halfword. Its global table pointer is reloaded around helper calls as in the
original. The original callback `func_1500FFCC` calls it at `0x15010038`.

The bounded guest suite covers 16 cases, including changes to the global
table pointer during modeled helpers, and visits 86 of 91 retail words; the
unvisited instructions are division guard paths. SDK32 native O0/O2/O3 each
pass eight defined cases and nine effective negative controls. Eight cases
exercise the original caller window. Sixteen connected cases execute original
`bzero` and the original target-randomization helper, while allocation, random
values and the randomizer's nested effect remain modeled. A separate null
allocation reaches an unmapped guest store; hardware null behavior and C
behavior for null are not qualified. Arbitrary helper side effects, complete
parent execution, hardware faults, and concurrency are not qualified.

Both object padders agree with the raw object and independently assembled
retail code; 16 rebased GNU links and 210 bounded access-cut quads pass. Actual
Make and an independent strict image comparison account for **261
changed bytes** with zero exclusions. Both neighboring functions, 6,050
function addresses, and 189,088 protected data bytes remain unchanged. The
actual ELF SHA-256 is `b8a63a6a9b1d015913fb756e07d762a5c584406a76e157827aa87e2e4aa351af`. The existing complete-ROM
checksum mismatch remains.

Fresh actual ELF recount: **4,336 / 5,513 (78.65%)** overall and **3,663 /
4,840 (75.68%)** Game, zero drift and 1,177 different. The 80% target needs
75 more exact functions. Tools were committed first as
`97b32e8c2188b542ce1da35ad26ccb23a1aac1ee`; the consumer change is separate.
