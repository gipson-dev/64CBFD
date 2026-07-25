#include <ultra64.h>

#include "n_synthInternals.h"
#include "variables.h"

/* Generated placeholder declarations. */
Acmd *func_100214F0(N_PVoice *, s16 *, s32, Acmd *);
/* End generated placeholder declarations. */

// modified n_alResamplePull
Acmd *func_10022460(N_PVoice *arg0, s16 *arg1, Acmd *arg2) {
    Acmd *sp34;
    s16 sp32;
    s32 sp2C;
    s32 sp28;
    f32 sp24;
    Acmd *sp20;
    Acmd *sp1C;

    sp34 = arg2;
    sp32 = 0x170;
    if (arg0->rs_upitch != 0) {
        sp34 = func_100214F0(arg0, &sp32, 0xB8, arg2);
        sp20 = sp34++;
        sp20->words.w0 = (sp32 & 0xFFFFFF) | 0x0A000000;
        sp20->words.w1 = ((*arg1 & 0xFFFF) << 0x10) | 0x170;
        if (1) {
        }
    } else {
        if (arg0->rs_ratio > D_8002C840) {
            arg0->rs_ratio = D_8002C848;
        }
        arg0->rs_ratio = (s32)(arg0->rs_ratio * 32768.0f);
        arg0->rs_ratio /= 32768.0f;
        sp24 = arg0->rs_delta + (arg0->rs_ratio * 184.0f);
        sp2C = (s32)sp24;
        arg0->rs_delta = sp24 - sp2C;
        sp34 = func_100214F0(arg0, &sp32, sp2C, arg2);
        sp28 = arg0->rs_ratio * 32768.0f;
        sp1C = sp34++;
        sp1C->words.w0 =
            (osVirtualToPhysical(arg0->rs_state) & 0xFFFFFF) | 0x05000000;
        sp1C->words.w1 = ((arg0->rs_first & 3) << 0x1E) |
                         ((sp28 & 0xFFFF) << 0xE) |
                         ((sp32 & 0xFFF) * 4);
        arg0->rs_first = 0;
    }
    return sp34;
}
// NON-MATCHING: same issues as the other functions in this range
// struct21 *func_10022460(struct42 *arg0, struct119 *arg1, struct21 *arg2) {
//     struct21 *sp34;
//     s16 sp32;
//     s32 sp2C;
//     s32 sp28;
//     f32 sp24;
//     struct21 *sp20;
//     struct21 *sp1C;
//
//     sp34 = arg2;
//     sp32 = 368; // 0x170;
//     if (arg0->unk50 != 0) {
//         sp34 = func_100214F0(arg0, &sp32, 0xB8, arg2);
//         sp20 = sp34 = &sp34->unk8;
//         sp20->unk0 = (sp32 & 0xFFFFFF) | 0xA000000;
//         sp20->unk4 = ((((s32 )arg1 & 0xFFFF) << 16) | 368);
//     } else {
//         if (D_8002C840 < (f64) arg0->unk4C) {
//             arg0->unk4C = D_8002C848;
//         }
//         arg0->unk4C = (s32) (arg0->unk4C * 32768.0f);
//         arg0->unk4C /= 32768.0f;
//         sp24 = arg0->unk54 + (arg0->unk4C * 184.0f);
//         sp2C = sp24;
//         arg0->unk54 = (sp24 - sp2C);
//         sp34 = func_100214F0(arg0, &sp32, sp2C, arg2);
//         sp28 = arg0->unk4C * 32768.0f;
//
//         sp1C = sp34 = &sp34->unk8;
//         sp1C->unk0 = ((osVirtualToPhysical(arg0->unk48) & 0xFFFFFF) | 0x5000000);
//         sp1C->unk4 = (((arg0->unk58 & 3) << 30) | ((sp28 & 0xFFFF) << 14) | ((sp32 & 0xFFF) * 4));
//         arg0->unk58 = 0;
//     }
//     return sp34;
// }
