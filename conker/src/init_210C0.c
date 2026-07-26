#include "n_synthInternals.h"

extern f32 D_8002C820;

f32 sqrtf(f32);
Acmd *func_10020000(N_PVoice *, s32, Acmd *);

// modified n_alAuxBusPull
Acmd *func_100210C0(s32 arg0, Acmd *arg1, s32 arg2, s32 *arg3) {
    Acmd *sp3C;
    N_ALAuxBus *sp38;
    N_PVoice *sp34;
    s32 sp30;
    u32 sp2C;
    u32 sp28;
    Acmd *sp24;
    Acmd *sp20;
    Acmd *sp1C;

    sp3C = arg1;
    sp38 = &n_syn->auxBus[arg2];
    sp30 = 0;
    sp2C = 1;
    *arg3 = 0;
    sp34 = (N_PVoice *)sp38->sourceCount;

    if (sp34) {
        do {
            sp34 = (N_PVoice *)((u8 *)sp34 - sizeof(ALLink));
            if ((sp34->vvoice != NULL) &&
                (sp34->vvoice->pvoice != NULL) &&
                (sp34->vvoice->pvoice->unk99 >= 0x40)) {
                sp3C = func_10020000(sp34, arg0, sp3C);
                *arg3 += 1;
                sp30++;
                if (sp34->vvoice->pvoice->unk99 > sp2C) {
                    sp2C = sp34->vvoice->pvoice->unk99;
                }
            }
            sp34 = (N_PVoice *)sp34->voiceLink.next;
        } while (sp34);
    }

    if (sp30) {
        sp2C -= 0x3E;
        if (sp2C >= 7U) {
            sp28 = D_8002C820 / sqrtf(sp2C);
        } else {
            sp28 = 65536.0f / sp2C;
        }

        sp24 = sp3C++;
        sp24->words.w0 = 0x4E0;
        sp24->words.w1 =
            ((sp28 & 0xFFFF) << 16) | (sp2C & 0xFFFF);

        sp20 = sp3C++;
        sp20->words.w0 = 0x650;
        sp20->words.w1 =
            ((sp28 & 0xFFFF) << 16) | (sp2C & 0xFFFF);
    }

    sp34 = (N_PVoice *)sp38->sourceCount;
    if (sp34) {
        do {
            sp34 = (N_PVoice *)((u8 *)sp34 - sizeof(ALLink));
            if (((sp34->vvoice != NULL) &&
                 ((sp34->vvoice->pvoice == NULL) ||
                  (sp34->vvoice->pvoice->unk99 < 0x40))) ||
                ((sp34->vvoice == NULL) && (arg2 == 0))) {
                sp1C = sp3C;
                sp3C = func_10020000(sp34, arg0, sp3C);
                if (sp3C != sp1C) {
                    *arg3 += 1;
                }
            }
            sp34 = (N_PVoice *)sp34->voiceLink.next;
        } while (sp34);
    }

    return sp3C;
}
