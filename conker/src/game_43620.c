#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_15016170(s32);
void func_151F3C34(s32);
/* End generated placeholder declarations. */

/* Non-matching C placeholders for asm/nonmatchings/game_43620/func_15016170.s. */
/* Initialize stream buffers, pan/gain state and the DMA callback address. */
void func_15016170(s32 heapAddress) {
    s32 index;
    s16 gain;
    bzero(&D_800E0D80, sizeof(D_800E0D80));
    D_800E0D80.unk8 = (s32)alHeapDBAlloc(0, 0, (ALHeap *)heapAddress, 1, 80);
    D_800E0D80.unk74 = (s32)alHeapDBAlloc(0, 0, (ALHeap *)heapAddress, 1, 1088);
    D_800E0D80.unk5C = (s32)alHeapDBAlloc(0, 0, (ALHeap *)heapAddress, 1, 8);
    D_800E0D80.unkC = 64;
    D_800E0D80.unk96 = 64;
    D_800E0D80.unk84 = 0;
    D_800E0D80.unkE = 0x7FFF;
    /* Keep the signed gain and unsigned word limit distinct. */
    *(u32 *)((u8 *)&D_800E0D80 + 0x88) = 0x7FFFU;
    D_800E0D80.unk9A = 0;
    D_800E0D80.unk32 = 0;
    D_800E0D80.unk30 = 0;
    D_800E0D80.unk94 = D_800E0D80.unk96;
    /* The endpoint is one-past the 127-sample array; pan64 reads entries64/63. */
    index = D_800E0D80.unkC * 2;
    D_800E0D80.unk10 = (*(s16 *)((u8 *)&D_8002BC10 + index) * (gain = D_800E0D80.unkE)) >> 15;
    D_800E0D80.unk12 = (*(s16 *)((u32)(D_8002BC10 + 127) - (u32)index) * gain) >> 15;
    D_800E0D80.unk24 = 1;
    D_800E0D80.unk14 = 0x7FFC;
    D_800E0D80.unk16 = 0;
    func_151F3C34((s32)func_151F3C4C);
}
// looks straightforward.. but... isnt
// void func_15016170(s32 arg0) {
//     s32 idx;
//     s16 tmp;
//     bzero(&D_800E0D80, 160);
//     D_800E0D80.unk8 = alHeapDBAlloc(0, 0, arg0, 1, 80);
//     D_800E0D80.unk74 = alHeapDBAlloc(0, 0, arg0, 1, 1088);
//     D_800E0D80.unk5C = alHeapDBAlloc(0, 0, arg0, 1, 8);
//     D_800E0D80.unk96 = 64;
//     D_800E0D80.unkC = 64;
//     D_800E0D80.unk84 = 0;
//     D_800E0D80.unkE = 0x7FFF;
//     D_800E0D80.unk88 = 0x7FFF;
//     D_800E0D80.unk9A = 0;
//     D_800E0D80.unk32 = 0;
//     D_800E0D80.unk30 = 0;
//     D_800E0D80.unk94 = D_800E0D80.unk96;
//     idx = D_800E0D80.unkC;
//     tmp = D_800E0D80.unkE;
//     D_800E0D80.unk10 = (D_8002BC10[idx] * tmp) >> 15;
//     D_800E0D80.unk12 = (D_8002BD0E[-idx] * tmp) >> 15;
//     D_800E0D80.unk24 = 1;
//     D_800E0D80.unk14 = 0x7FFC;
//     D_800E0D80.unk16 = 0;
//     func_151F3C34(func_151F3C4C, tmp, 64);
// }
