#include <ultra64.h>

#include "n_synthInternals.h"
#include "variables.h"

typedef struct {
    u8 pad0[0x14];
    void *dc_state;
    void *dc_lstate;
    u8 pad1C[0x14];
    void *(*dc_dma)(s32, s32, void *);
    void *dc_dmaState;
    u8 pad38[8];
    s32 dc_first;
    s32 dc_memin;
    u8 pad48[0x1A];
    s16 em_volume;
    u8 pad64[0x1C];
    s32 em_first;
} RareDecoderVoice;

/* Generated placeholder declarations. */
s32 func_100214F0(s32 arg0, s32 arg1, s32 arg2, s32 arg3);
s32 func_10021C40(N_PVoice *, s32, void *);
Acmd *func_10021E4C(Acmd *, RareDecoderVoice *, s32, s32, s16, s16, s32);
/* End generated placeholder declarations. */

// struct21 *func_100214F0(struct42 *arg0, void *arg1, s32 arg2, void *struct21);
/* Non-matching C placeholders for asm/nonmatchings/init_214F0/func_100214F0.s. */
s32 func_100214F0(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return 0;
}
// modified n_alLoadParam
s32 func_10021C40(N_PVoice *filter, s32 paramID, void *param) {
    switch (paramID) {
        case AL_FILTER_SET_WAVETABLE:
            filter->dc_table = (ALWaveTable *)param;
            filter->dc_memin = (s32)filter->dc_table->base;
            filter->dc_sample = 0;
            filter->dc_table->len = 9 * (filter->dc_table->len / 9);

            if (((u32)filter->dc_table->waveInfo.adpcmWave.book &
                 0xFF000003) != 0x80000000) {
                filter->dc_loop.start =
                    filter->dc_loop.end = filter->dc_loop.count = 0;
                break;
            } else {
                filter->dc_bookSize =
                    2 * filter->dc_table->waveInfo.adpcmWave.book->order *
                    filter->dc_table->waveInfo.adpcmWave.book->npredictors *
                    ADPCMVSIZE;
            }

            if (filter->dc_table->waveInfo.adpcmWave.loop) {
                filter->dc_loop.start =
                    filter->dc_table->waveInfo.adpcmWave.loop->start;
                filter->dc_loop.end =
                    filter->dc_table->waveInfo.adpcmWave.loop->end;
                filter->dc_loop.count =
                    filter->dc_table->waveInfo.adpcmWave.loop->count;

                bcopy(filter->dc_table->waveInfo.adpcmWave.loop->state,
                      filter->dc_lstate, sizeof(ADPCM_STATE));
            } else {
                filter->dc_loop.start =
                    filter->dc_loop.end = filter->dc_loop.count = 0;
            }
            break;
        case AL_FILTER_RESET:
            filter->dc_lastsam = 0;
            filter->dc_first = 1;
            filter->dc_sample = 0;

            if (filter->dc_table) {
                filter->dc_memin = (s32)filter->dc_table->base;
                filter->dc_loop.count = 0;
            }
            break;
        default:
            break;
    }

    return 0;
}
// ? func_10021C40(void *arg0, s32 arg1, s32 arg2) {
//     s32 temp_s0;
//     s32 temp_s0_2;
//     void *temp_t3;
//     void *temp_t3_2;
//
//     if (arg1 != 4) {
//         if (arg1 != 5) {
//
//         } else {
//             arg0->unk28 = arg2;
//             arg0->unk44 = (s32) *arg0->unk28;
//             arg0->unk38 = 0;
//             temp_t3 = arg0->unk28;
//             temp_t3->unk4 = (s32) (((s32) temp_t3->unk4 / 9) * 9);
//             if ((arg0->unk28->unk10 & 0xFF000003) != 0x80000000) {
//                 arg0->unk24 = 0;
//                 temp_s0 = arg0->unk24;
//                 arg0->unk20 = temp_s0;
//                 arg0->unk1C = temp_s0;
//             } else {
//                 temp_t3_2 = arg0->unk28->unk10;
//                 arg0->unk2C = (s32) (temp_t3_2->unk0 * 2 * temp_t3_2->unk4 * 8);
//                 if (arg0->unk28->unkC != 0) {
//                     arg0->unk1C = (s32) *arg0->unk28->unkC;
//                     arg0->unk20 = (s32) arg0->unk28->unkC->unk4;
//                     arg0->unk24 = (s32) arg0->unk28->unkC->unk8;
//                     bcopy(arg0->unk28->unkC + 0xC, arg0->unk18, 0x20);
//                 } else {
//                     arg0->unk24 = 0;
//                     temp_s0_2 = arg0->unk24;
//                     arg0->unk20 = temp_s0_2;
//                     arg0->unk1C = temp_s0_2;
//                 }
//             }
//         }
//     } else {
//         arg0->unk3C = 0;
//         arg0->unk40 = 1;
//         arg0->unk38 = 0;
//         if (arg0->unk28 != 0) {
//             arg0->unk44 = (s32) *arg0->unk28;
//             arg0->unk24 = 0;
//         }
//     }
//     return 0;
// }

Acmd *func_10021E4C(Acmd *arg0, RareDecoderVoice *arg1, s32 arg2, s32 arg3,
                    s16 arg4, s16 arg5, s32 arg6) {
    s32 sp2C;
    s32 sp28;
    Acmd *sp24;
    Acmd *sp20;
    Acmd *sp1C;

    if (arg3 > 0) {
        sp28 = (s32)arg1->dc_dma(arg1->dc_memin, arg3, arg1->dc_dmaState);
        if (sp28 == 0) {
            arg1->em_first = 1;
            arg1->em_volume = 0;
            arg1->dc_first = 0;
            return arg0;
        }
        sp2C = sp28 & 7;
        arg3 += sp2C;
        sp24 = arg0++;
        sp24->words.w0 =
            ((((arg3 - (arg3 & 7)) + 8) & 0xFFF) << 0xC) |
            0x04000000 | (arg5 & 0xFFF);
        sp24->words.w1 = sp28 - sp2C;
        if (1) {
        }
    } else {
        sp2C = 0;
    }
    if (arg6 & 2) {
        sp20 = arg0++;
        sp20->words.w0 = 0x0F000000;
        sp20->words.w1 = (s32)arg1->dc_lstate & 0x1FFFFFFF;
    }
    sp1C = arg0++;
    sp1C->words.w0 =
        ((s32)arg1->dc_state & 0x1FFFFFFF & 0xFFFFFF) | 0x01000000;
    sp1C->words.w1 =
        ((arg6 & 0xF) << 0x1C) |
        (((arg2 * 2) & 0xFFF) << 0x10) |
        ((sp2C & 0xF) << 0xC) |
        (arg4 & 0xFFF);
    arg1->dc_first = 0;
    return arg0;
}
