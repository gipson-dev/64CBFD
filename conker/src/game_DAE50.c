#include <ultra64.h>

#include "functions.h"
#include "variables.h"


// some mips3/64bit stuff going on here

#pragma GLOBAL_ASM("asm/nonmatchings/game_DAE50/func_150AD9A0.s")
// NON-MATCHING: I am nothing without mip2c.
// s32 func_150AD9A0(s32 arg0, s32 arg1, s32 arg2) {
//     s32 v0;
//     s32 tmp0 = (s32)arg0; // = arg0;
//     s32 tmp1 = (s32)arg1;
//     s32 tmp2 = (s32)arg2;
//
//     // /* AD9A0 850AD9A0 000417C3 */  sra        $v0, $a0, 0x1f
//     // /* AD9A4 850AD9A4 00822026 */  xor        $a0, $a0, $v0
//     // /* AD9A8 850AD9A8 00822022 */  sub        $a0, $a0, $v0
//     v0 = (tmp0 >> 31);
//     tmp0 = (tmp0 ^ v0) - v0;
//     // tmp0 =   tmp0 - v0;
//     // tmp0 = tmp0 - v0;
//     // /* AD9AC 850AD9AC 000517C3 */  sra        $v0, $a1, 0x1f
//     // /* AD9B0 850AD9B0 00A22826 */  xor        $a1, $a1, $v0
//     // /* AD9B4 850AD9B4 00A22822 */  sub        $a1, $a1, $v0
//     v0 = arg1 >> 31;
//     tmp1 = tmp1 ^ v0;
//     tmp1 = tmp1 - v0;
//
//     // /* AD9B8 850AD9B8 000617C3 */  sra        $v0, $a2, 0x1f
//     // /* AD9BC 850AD9BC 00C23026 */  xor        $a2, $a2, $v0
//     // /* AD9C8 850AD9C8 00C23022 */   sub       $a2, $a2, $v0
//     v0 = tmp2 >> 31;
//     tmp2 = tmp2 ^ v0;
//     // tmp2 = tmp2 - v0;
//
//     // /* AD9C0 850AD9C0 0085082A */  slt        $at, $a0, $a1
//     // /* AD9C4 850AD9C4 10200004 */  beqz       $at, .L850AD9D8
//     if (tmp0 < tmp1)
//     {
//         // .L850AD9D8:
//         // /* AD9CC 850AD9CC 00A42826 */  xor        $a1, $a1, $a0
//         // /* AD9D0 850AD9D0 00852026 */  xor        $a0, $a0, $a1
//         // /* AD9D4 850AD9D4 00A42826 */  xor        $a1, $a1, $a0
//         v0 = tmp1 ^ tmp0;
//         tmp0 = tmp0 ^ v0;
//         tmp1 = tmp1 ^ tmp0;
//     }
//     // /* AD9E0 850AD9E0 00C41026 */   xor       $v0, $a2, $a0
//     // /* AD9E4 850AD9E4 00822026 */  xor        $a0, $a0, $v0
//     // /* AD9E8 850AD9E8 00443026 */  xor        $a2, $v0, $a0
//     v0 = tmp2 ^ tmp0;
//     tmp0 = tmp0 ^ v0;
//     tmp2 = v0 ^ tmp0;
//     // /* AD9D8 850AD9D8 0086082A */  slt        $at, $a0, $a2
//     // /* AD9DC 850AD9DC 10200003 */  beqz       $at, .L850AD9EC
//     if (tmp0 < tmp2)
//     {
//         // .L850AD9EC:
//         // /* AD9EC 850AD9EC 00A6082A */  slt        $at, $a1, $a2
//         // /* AD9F0 850AD9F0 10200004 */  beqz       $at, .L850ADA04
//         if (tmp1 - tmp2 != 0)
//         {
//             v0 = 0xb; // ??
//             tmp2 = tmp2 ^ tmp1;
//             tmp1 = tmp1 ^ tmp2;
//             tmp2 = tmp2 ^ tmp1;
//         }
//
//         // /* AD9F4 850AD9F4 2402000B */   addiu     $v0, $zero, 0xb
//         // /* AD9F8 850AD9F8 00C53026 */  xor        $a2, $a2, $a1
//         // /* AD9FC 850AD9FC 00A62826 */  xor        $a1, $a1, $a2
//         // /* ADA00 850ADA00 00C53026 */  xor        $a2, $a2, $a1
//
//     }
//     // .L850ADA04:
//     // /* ADA04 850ADA04 00A20018 */  mult       $a1, $v0
//     tmp1 = tmp1 * v0;
//     // /* ADA08 850ADA08 00063082 */  srl        $a2, $a2, 2
//     tmp2 = tmp2 >> 2;
//     // /* ADA0C 850ADA0C 00C43020 */  add        $a2, $a2, $a0
//     tmp2 = tmp2 + tmp0;
//     // /* ADA10 850ADA10 00001012 */  mflo       $v0
//     // /* ADA14 850ADA14 00021142 */  srl        $v0, $v0, 5
//     v0 = v0 << 5;
//     // /* ADA18 850ADA18 03E00008 */  jr         $ra
//     // /* ADA1C 850ADA1C 00461020 */   add       $v0, $v0, $a2
//     v0 = v0 + tmp2;
//     return v0;
// }

// Hand-written assembly in the original game (like func_16003650) - do not
// try to match from C. Evidence: strictly source-order instruction sequence
// (IDO -O2 reschedules), minimal a0/a1/a2 register reuse, `lui at`/`lui a0`
// self-base forms that are exactly the assembler's `ld/sd reg, symbol` macro
// expansions, a filled jr-ra delay slot, and (in func_150ADACC) a dead
// `li a0,0` that is unique in the entire ROM. Verified-correct C equivalents
// kept below for documentation.
//
// xorshift-style PRNG step, operating on the 64-bit seed D_800885B0.
s32 func_150ADA20(void) {
    u64 seed = D_800885B0;
    u64 mixed = ((seed << 63) >> 31) | ((seed << 31) >> 32);

    mixed ^= (seed << 44) >> 32;
    seed = ((mixed >> 20) & 0xFFF) ^ mixed;
    D_800885B0 = seed;
    return (s32) seed;
}

f32 func_150ADA68(void) {
    u64 seed = D_800885B0;
    u64 mixed = ((seed << 63) >> 31) | ((seed << 31) >> 32);

    mixed ^= (seed << 44) >> 32;
    seed = ((mixed >> 20) & 0xFFF) ^ mixed;
    D_800885B0 = seed;
    return (f32)((s32)seed & 0xFFFF) * D_8009F740;
}

// PRNG seed setter (see handwritten-assembly note above func_150ADA20):
void func_150ADACC(u32 arg0) {
    D_800885B0 = arg0 + 1;
}
