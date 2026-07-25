#include "n_synthInternals.h"

s32 func_10020000();
Acmd *func_10022040(N_PVoice *, s16 *, s32, Acmd *);
s16 _getRate(f32, f32, s32, u16 *);

extern f32 D_8002C814;
extern s16 D_8002BC10[];
extern s16 D_8002BD0E[];

// relies on jump table
/* Non-matching C placeholders for asm/nonmatchings/init_20000/func_10020000.s. */
s32 func_10020000() {
    return 0;
}

s32 n_alEnvmixerParam(N_PVoice *filter, s32 paramID, void *param) {
    N_PVoice  *e = filter;

    switch (paramID) {
      case (AL_FILTER_ADD_UPDATE):
          if (e->em_ctrlTail) {
              e->em_ctrlTail->next = (ALParam *)param;
          } else {
              e->em_ctrlList = (ALParam *)param;
          }
          e->em_ctrlTail = (ALParam *)param;
          break;
      case (AL_FILTER_RESET):
          e->em_first = 1;
          e->em_motion = AL_STOPPED;
          e->em_volume = 1;
          e->em_segEnd = 0;
          e->rs_delta  = 0.0;
          e->rs_first  = 1;
          e->rs_upitch = 0;
          n_alLoadParam(e, AL_FILTER_RESET, param);
          break;
      case (AL_FILTER_START):
          e->em_motion = AL_PLAYING;
          break;
      default:
#if 1
          n_alLoadParam(e, paramID, param);
#else
          n_alResampleParam(e, paramID, param); // TODO
#endif
          break;
  }
  return 0;
}

Acmd *func_10020ABC(N_PVoice *arg0, s16 *arg1, s16 *arg2, s32 arg3,
                    Acmd *arg4) {
    Acmd *sp34;
    N_PVoice *sp30;
    Acmd *sp2C;
    Acmd *sp28;
    Acmd *sp24;
    Acmd *sp20;
    Acmd *sp1C;

    sp34 = arg4;
    sp30 = arg0;
    if (sp30->dc_table != 0) {
        ((u8 *)sp30->dc_table)[0xA] = 1;
    }
    if ((sp30->em_motion != AL_PLAYING) || (arg3 == 0)) {
        return sp34;
    }

    sp34 = func_10022040(sp30, arg1, arg3, arg4);
    if (sp30->em_first) {
        sp30->em_first = 0;
        sp30->em_ltgt =
            (D_8002BC10[(s16)sp30->em_pan] *
             (s16)sp30->em_volume) >> 15;
        sp30->em_lratm =
            _getRate((s16)sp30->em_cvolL, (s16)sp30->em_ltgt,
                     sp30->em_segEnd, &sp30->em_lratl);
        sp30->em_rtgt =
            (D_8002BD0E[-(s16)sp30->em_pan] *
             (s16)sp30->em_volume) >> 15;
        sp30->em_rratm =
            _getRate((s16)sp30->em_cvolR, (s16)sp30->em_rtgt,
                     sp30->em_segEnd, &sp30->em_rratl);

        sp2C = sp34++;
        sp2C->words.w0 = ((s16)sp30->em_cvolL & 0xFFFF) | 0x09060000;
        sp2C->words.w1 =
            (((s16)sp30->em_dryamt & 0xFFFF) << 16) |
            ((s16)sp30->em_wetamt & 0xFFFF);

        sp28 = sp34++;
        sp28->words.w0 = ((s16)sp30->em_rtgt & 0xFFFF) | 0x09040000;
        sp28->words.w1 =
            (((s16)sp30->em_rratm & 0xFFFF) << 16) |
            (sp30->em_rratl & 0xFFFF);

        sp24 = sp34++;
        sp24->words.w0 = ((s16)sp30->em_ltgt & 0xFFFF) | 0x09000000;
        sp24->words.w1 =
            (((s16)sp30->em_lratm & 0xFFFF) << 16) |
            (sp30->em_lratl & 0xFFFF);

        sp20 = sp34++;
        sp20->words.w0 = ((s16)sp30->em_cvolR & 0xFFFF) | 0x03010000;
        sp20->words.w1 = osVirtualToPhysical(sp30->em_state);
        if (1) {
        }
    } else {
        sp1C = sp34++;
        sp1C->words.w0 = 0x03000000;
        sp1C->words.w1 = osVirtualToPhysical(sp30->em_state);
    }

    *arg1 += 0x170;
    sp30->em_delta += 184;
    if (((s16)sp30->em_dryamt & 2) || ((s16)sp30->em_wetamt & 2)) {
        sp30->em_dryamt &= -3;
        sp30->em_wetamt &= -3;
        sp30->em_first = 1;
    }
    return sp34;
}
// NON-MATCHING: pretty close but no cigar
// struct21 *func_10020ABC(struct42 *arg0, struct119 *arg1, s32 arg2, s32 arg3, struct21 *arg4) {
//     struct21 *sp34;
//     struct42 *sp30;
//     struct21 *sp2C;
//     struct21 *sp28;
//     struct21 *sp24;
//     struct21 *sp20;
//     struct21 *sp1C;
//
//     sp34 = arg4;
//     sp30 = arg0;
//     if (sp30->unk28 != 0) {
//         sp30->unk28->unkA = (u8)1;
//     }
//     if ((sp30->unk8C != 1) || (arg3 == 0)) {
//         return sp34;
//     }
//
//     sp34 = func_10022040(sp30, arg1, arg3, arg4);
//     if (sp30->unk80) {
//         sp30->unk80 = 0;
//         sp30->unk70 = (D_8002BC10[(s16)sp30->unk60] * (s16)sp30->unk62) >> 15;
//         sp30->unk6E = _getRate((s16)sp30->unk64, (s16)sp30->unk70, sp30->unk7C, &sp30->unk6C);
//         sp30->unk76 = (D_8002BD0E[-(s16)sp30->unk60] * (s16)sp30->unk62) >> 15;
//         sp30->unk74 = _getRate((s16)sp30->unk66, (s16)sp30->unk76, sp30->unk7C, &sp30->unk72);
//
//         sp2C = sp34 = &sp34->unk8;
//         sp2C->unk0 = ((s16)sp30->unk64 & 0xFFFF) | 0x9060000;
//         sp2C->unk4 = (((s16)sp30->unk68 & 0xFFFF) << 16) | ((s16)sp30->unk6A & 0xFFFF);
//
//         sp28 = sp34 = &sp34->unk8;
//         sp28->unk0 = ((s16)sp30->unk76 & 0xFFFF) | 0x9040000;
//         sp28->unk4 = (((s16)sp30->unk74 & 0xFFFF) << 16) | (sp30->unk72 & 0xFFFF);
//
//         sp24 = sp34 = &sp34->unk8;
//         sp24->unk0 = ((s16)sp30->unk70 & 0xFFFF) | 0x9000000;
//         sp24->unk4 = (((s16)sp30->unk6E & 0xFFFF) << 16) | (sp30->unk6C & 0xFFFF);
//
//         sp20 = sp34 = &sp34->unk8;
//         sp20->unk0 = ((s16)sp30->unk66 & 0xFFFF) | 0x3010000;
//         sp20->unk4 = osVirtualToPhysical(sp30->unk5C);
//     } else {
//         sp1C = sp34 = &sp34->unk8;
//         sp1C->unk0 = 0x3000000;
//         sp1C->unk4 = osVirtualToPhysical(sp30->unk5C);
//         // nop...
//     }
//     // just this line :(
//     arg1 = &arg1->unk170;
//     sp30->unk78 += 0xb8; // 184
//     if ((((s16)sp30->unk68 & 2)) || (((s16)sp30->unk6A & 2))) {
//         sp30->unk68 &= -3; // (s16)sp30->unk68 & -3;
//         sp30->unk6A &= -3;
//         sp30->unk80 = 1;
//     }
//     return sp34;
// }

s16 _getRate(f32 arg0, f32 arg1, s32 arg2, u16 *arg3) {
    s16 spE;
    s16 spC;
    f32 sp8;
    f32 sp4;
    f32 sp0;

    if (arg2 == 0) {
        if (arg0 <= arg1) {
            *arg3 = 0xFFFF;
            return 0x7FFF;
        } else {
            *arg3 = 0;
            return -0x8000;
        }
    }
    sp8 = 1.0f / (f32) arg2;

    if (arg1 < 1.0f) {
        arg1 = 1.0f;
    }
    if (arg0 <= 0.0f) {
        arg0 = 1.0f;
    }
    sp4 = (arg1 - arg0) * sp8 * 8.0f;
    spE = (s16) (s32) sp4;
    sp0 = sp4 - (f32) spE;
    spE = spE - 1;
    sp0 = sp0 + 1.0f;
    spC = (s16) (s32) sp0;
    spE = spE + spC;
    sp0 = sp0 - (f32) spC;
    *arg3 = (u32) (D_8002C814 * sp0); // 65535.0f
    return spE;
}

s16 _getVol(s16 ivol, s32 samples, s16 ratem, u16 ratel)
{
    s32 tmp1;
#ifdef AUD_PROFILE
    lastCnt[++cnt_index] = osGetCount();
#endif

    samples >>= 3;
    if (samples == 0){
        return ivol;
    }

    tmp1 = ratel * samples;
    tmp1 >>= 16;
    tmp1 += ratem * samples;
    ivol += tmp1;

#ifdef AUD_PROFILE
    PROFILE_AUD(vol_num, vol_cnt, vol_max, vol_min);
#endif
    return ivol;
}
