#include "n_synthInternals.h"

extern f32 D_8002C830;
extern f32 D_8002C834;
extern f32 D_8002C838;
f32 sqrtf(f32);

Acmd *func_10022460(N_PVoice *, s16 *, Acmd *);
void func_1001CF38(void *, f32);

Acmd *func_10022040(N_PVoice *arg0, s16 *arg1, s32 arg2, Acmd *arg3) {
    Acmd *sp2C;
    f32 sp28;
    Acmd *sp24;
    Acmd *sp20;
    Acmd *sp1C;

    sp2C = arg3;
    sp2C = func_10022460(arg0, arg1, arg3);
    if ((arg0->unk99 != 0) && (arg0->unk99 < 0x40)) {
        if (arg0->unk99 >= 6) {
            sp28 = D_8002C830 / sqrtf(arg0->unk99 + 1.0f);
        } else {
            sp28 = 65536.0f / ((f32)arg0->unk99 + 1.0f);
        }
        if (sp28 < D_8002C834) {
            sp28 = D_8002C838;
        }
        sp24 = sp2C++;
        sp24->words.w0 = *arg1 & 0xFFFF;
        sp24->words.w1 =
            (((u32)sp28 & 0xFFFF) << 16) | ((arg0->unk99 + 1) & 0xFFFF);
    }
    if (arg0->unkA2 > 0) {
        if (arg0->unkC8 != 0) {
            func_1001CF38(&arg0->unkA0, 22050.0f);
        }
        sp20 = sp2C++;
        sp20->words.w0 = 0x0B000020;
        sp20->words.w1 = osVirtualToPhysical(&arg0->padA4[4]);
        if (arg0->unkC8 == 2) {
            arg0->unkC8 = 0;
        }
        sp1C = sp2C++;
        sp1C->words.w0 =
            (*arg1 & 0xFFFF) |
            (((arg0->unkC8 & 0xFF) << 16) | 0x0E000000);
        sp1C->words.w1 =
            osVirtualToPhysical(arg0->unkCC) & 0xFFFFFF & 0xFFFFFF;
        arg0->unkC8 = 0;
    }
    return sp2C;
}
// NON-MATCHING: 80% matching
// struct21 *func_10022040(struct42 *arg0, struct119 *arg1, s32 arg2, struct21 *arg3) {
//     struct21 *sp2C;
//     f32 sp28;
//     struct21 *sp24;
//     struct21 *sp20;
//     struct21 *sp1C;
//
//     sp2C = arg3;
//     sp2C = func_10022460(arg0, arg1, arg3);
//
//     if ((arg0->unk99 != 0) && (arg0->unk99 < 64)) {
//         if (arg0->unk99 >= 6) {
//             sp28 = D_8002C820 / sqrtf(arg0->unk99 + 1.0f);
//         } else {
//             sp28 = 65536.0f / (arg0->unk99 + 1.0f);
//         }
//         if (sp28 < D_8002C834) {
//             sp28 = D_8002C838;
//         }
//         sp24 = sp2C = &sp2C->unk8;
//         sp24->unk0 = ((s32)arg1 & 0xFFFF);
//         sp24->unk4 =  (((u32) sp28 & 0xFFFF) << 16) | (arg0->unk99 + 1);
//     }
//     if ((s16)arg0->unkA2 > 0) {
//         if (arg0->unkC8 != 0) {
//             func_1001CF38(&arg0->unkA0, 22050.0f);
//         }
//         sp20 = sp2C = &sp2C->unk8;
//         sp20->unk0 = 0xB000020;
//         sp20->unk4 = osVirtualToPhysical(&arg0->unkA8);
//         if (arg0->unkC8 == 2) {
//             arg0->unkC8 = 0;
//         }
//         sp1C = sp2C = &sp2C->unk8;
//         sp1C->unk0 = (((s32)arg1 & 0xFFFF) | (((arg0->unkC8 & 0xFF) << 0x10) | 0xE000000));
//         sp1C->unk4 = (osVirtualToPhysical(arg0->unkCC) & 0xFFFFFF & 0xFFFFFF);
//         arg0->unkC8 = 0;
//     }
//     return sp2C;
// }

s32 n_alLoadParam(N_PVoice *filter, s32 paramID, void *param) {
    f32 *sp24 = &param;

    switch (paramID) {
        case 4:
            filter->unkA2 = 0;
            func_10021C40(filter, 4, param);
            break;
        case 18:
            filter->unkA2 = param;
            filter->unkC8 |= 2;
            break;
        case 19:
            filter->unkA0 = *sp24;
            filter->unkC8 |= 2;
            break;
        case 17:
            filter->unk99 = param;
            break;
        default:
            func_10021C40(filter, paramID, param);
            break;
    }

    return 0;
}
