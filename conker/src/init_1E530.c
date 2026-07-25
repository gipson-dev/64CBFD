
#include <ultra64.h>

#include "functions.h"
#include "variables.h"
#include "n_abi.h"

#define FIXED_SAMPLE 184
#define N_AL_TEMP_0 0
#define N_AL_TEMP_1 368
#define N_AL_TEMP_2 736
#define N_AL_AUX_L_OUT 1984
#define N_AL_AUX_R_OUT 2352
#define RANGE 2.0f

typedef struct {
    u8 pad0[0x48];
    struct RareN_ALAuxBus_s *auxBus;
    u8 pad4C[8];
    s32 outputRate;
} RareN_ALSynth;

typedef struct {
    s16 fc;
} RareALLowPass;

extern RareN_ALSynth *n_syn;
void init_lpfilter(void *);

s32 func_1001ED6C(void *, s32, void *);

/*
 * The n_audio reverb used by Rare predates the stock SDK ALFx layout in
 * synthInternals.h.  DK64 retained the matching layout and source.
 */
typedef struct {
    u8 pad0[0x14];
    void *state[2];
    f32 ratio;
    s32 upitch;
    f32 delta;
    s32 first;
} RareALResampler;

typedef struct {
    u32 input;
    u32 output;
    s16 ffcoef;
    s16 fbcoef;
    s16 gain;
    u16 padE;
    f32 rsinc;
    f32 rsval;
    s32 rsdelta;
    f32 rsgain;
    RareALLowPass *lp;
    RareALResampler *rs;
} RareALDelay;

typedef struct {
    u32 length;
    RareALDelay *delay;
    u8 section_count;
    u8 pad9[0x17];
    s16 *base[2];
    s16 *input[2];
} RareALFx;

typedef struct RareN_ALAuxBus_s {
    u8 pad0[0x1C];
    RareALFx *fx;
    u8 pad20[0x24];
} RareN_ALAuxBus;

Acmd *func_100210C0(s32, Acmd *, s32, s32 *);
Acmd *func_1001F28C(RareALFx *, RareALDelay *, s32, s32, Acmd *);
Acmd *func_1001F5A4(RareALFx *, s32, s16 *, s32, s32, Acmd *);
Acmd *func_1001F79C(RareALFx *, s32, s16 *, s32, Acmd *);
Gfx *func_1001F978(struct55 *, s32, s32, Gfx *);

Acmd *func_1001E530(s32 sampleOffset, Acmd *p, s32 arg2) {
    Acmd *ptr = p;
    RareALFx *r = n_syn->auxBus[arg2].fx;
    s16 i;
    s16 buff1;
    s16 buff2;
    s16 input;
    s16 output;
    s16 *in_ptr;
    s16 *out_ptr;
    s16 *prev_out_ptr = 0;
    RareALDelay *d;
    s32 sp58 = 0;
    u32 j;

    ptr = func_100210C0(sampleOffset, p, arg2, &sp58);

    input = N_AL_AUX_L_OUT;
    output = N_AL_AUX_R_OUT;
    buff1 = N_AL_TEMP_0;
    buff2 = N_AL_TEMP_1;

    if (D_800428C4[arg2] == 0) {
        aMix(ptr++, 0, 0xC000, N_AL_AUX_L_OUT, input);
        aMix(ptr++, 0, 0x4000, N_AL_AUX_R_OUT, input);
    }

    ptr = func_1001F79C(r, 0, r->input[0], input, ptr);

    if (D_800428C4[arg2]) {
        ptr = func_1001F79C(r, 1, r->input[1], N_AL_AUX_R_OUT, ptr);
    }

    for (j = 0; j <= D_800428C4[arg2]; j++) {
        aClearBuffer(ptr++, output, FIXED_SAMPLE << 1);

        for (i = 0; i < r->section_count; i++) {
            d = &r->delay[i];
            in_ptr = &r->input[j][-d->input];
            out_ptr = &r->input[j][-d->output];

            if (D_800428C6[arg2] && D_800428C4[arg2]) {
                d->ffcoef = -d->ffcoef;
                d->fbcoef = -d->fbcoef;
            }

            if (in_ptr == prev_out_ptr) {
                s16 t = buff2;
                buff2 = buff1;
                buff1 = t;
            } else {
                ptr = func_1001F5A4(r, j, in_ptr, buff1, FIXED_SAMPLE, ptr);
            }

            ptr = func_1001F28C(r, d, j, buff2, ptr);

            if (d->ffcoef) {
                aMix(ptr++, 0, (u16)d->ffcoef, buff1, buff2);

                if (!d->rs && !d->lp) {
                    ptr = func_1001F79C(r, j, out_ptr, buff2, ptr);
                }
            }

            if (d->fbcoef) {
                aMix(ptr++, 0, (u16)d->fbcoef, buff2, buff1);
                ptr = func_1001F79C(r, j, in_ptr, buff1, ptr);
            }

            if (d->lp) {
                ptr = (Acmd *)func_1001F978(
                    (struct55 *)d->lp, j, buff2, (Gfx *)ptr);
            }

            if (!d->rs) {
                ptr = func_1001F79C(r, j, out_ptr, buff2, ptr);
            }

            if (d->gain) {
                if (D_800428C4[arg2]) {
                    aMix(ptr++, 0, (u16)d->gain, buff2, output);
                } else {
                    u32 sp34 = d->gain * 1.4141999483109f;

                    if (sp34 > 0x7FFF) {
                        sp34 = 0x7FFF;
                    }

                    aMix(ptr++, 0, (u16)sp34, buff2, output);
                }
            }

            prev_out_ptr = &r->input[j][d->output];
        }

        if (D_800428C4[arg2] && j == 0) {
            ptr = func_1001F5A4(
                r, 1, r->input[1], input, FIXED_SAMPLE, ptr);

            if (D_800428C6[arg2]) {
                aMix(ptr++, 0, 0x5A82, output, N_AL_TEMP_1 + 0x4E0);
            } else {
                aMix(ptr++, 0, 0x5A82, output, N_AL_TEMP_0 + 0x4E0);
            }
        } else {
        }

        aDMEMMove(ptr++, output, N_AL_AUX_L_OUT, FIXED_SAMPLE << 1);

        r->input[j] += FIXED_SAMPLE;

        if (r->input[j] > &r->base[j][r->length]) {
            r->input[j] -= r->length;
        }
    }

    return ptr;
}
s32 func_1001ED6C(void *filter, s32 paramID, void *param) {
    RareALFx *f = (RareALFx *)filter;
    s32 p = paramID & 7;
    s32 s = paramID >> 3;
    s32 val = *(s32 *)param;
    f32 rsgain;

    if (s >= f->section_count) {
        return 0;
    }

    switch (p) {
    case 0:
        f->delay[s].input =
            ((s32)val * n_syn->outputRate / 1000) & 0xfffffff8;
        break;
    case 1:
        f->delay[s].output =
            ((s32)val * n_syn->outputRate / 1000) & 0xfffffff8;
        break;
    case 2:
        f->delay[s].fbcoef = (s16)val;
        break;
    case 3:
        f->delay[s].ffcoef = (s16)val;
        break;
    case 4:
        f->delay[s].gain = (s16)val;
        break;
    case 5:
        f->delay[s].rsinc =
            ((((f32)val) / 1000) * RANGE) / n_syn->outputRate;
        break;
    case 6:
        rsgain = val;
        break;
    case 7:
        if (f->delay[s].lp) {
            f->delay[s].lp->fc = (s16)val;
            init_lpfilter(f->delay[s].lp);
        }
        break;
    }

    if (f->delay[s].input >= f->length - 16) {
        f->delay[s].input = f->length - 16;
    }

    if (f->delay[s].input >= f->length - 8) {
        f->delay[s].input = f->length - 8;
    }

    if (f->delay[s].input >= f->delay[s].output) {
        f->delay[s].output = f->delay[s].input + 8;
    }

    if (f->delay[s].rs) {
        if (p != 6) {
            if (f->delay[s].output - f->delay[s].input != 0) {
                rsgain = (f32)f->delay[s].rsgain /
                         (f->delay[s].output - f->delay[s].input) *
                         173123.404906676f;
            } else {
                rsgain = 0;
            }
        }

        f->delay[s].rsgain =
            (f->delay[s].output - f->delay[s].input) *
            (rsgain / 173123.404906676f);
    }

    return 0;
}
Acmd *func_1001F28C(RareALFx *r, RareALDelay *d, s32 arg2, s32 buff, Acmd *p) {
    Acmd *ptr = p;
    s32 ratio, count, rbuff = N_AL_TEMP_2;
    s16 *out_ptr;
    f32 fincount, fratio, delta;
    s32 ramalign = 0, length;
    s32 incount = FIXED_SAMPLE;
    s16 tmp;

    if (d->rs) {
        length = d->output - d->input;
        delta = func_1001FA78((f32 (*)[4])d, incount);
        delta /= length;
        delta = (s32)(delta * UNITY_PITCH);
        delta = delta / UNITY_PITCH;
        fratio = 1.0f - delta;
        fincount = d->rs->delta + (fratio * (f32)incount);
        count = (s32)fincount;
        d->rs->delta = fincount - (f32)count;
        out_ptr = &r->input[arg2][(s32)-(d->output - d->rsdelta)];
        ramalign = ((s32)out_ptr & 0x7) >> 1;
        ptr = func_1001F5A4(r, arg2, out_ptr - ramalign, rbuff,
                           count + ramalign, ptr);

        ratio = (s32)(fratio * UNITY_PITCH);

        tmp = buff >> 8;
        n_aResample(ptr++, osVirtualToPhysical(d->rs->state[arg2]),
                    d->rs->first, ratio, rbuff + (ramalign << 1), tmp);

        d->rs->first = 0;
        d->rsdelta += count - incount;
    } else {
        out_ptr = &r->input[arg2][(s32)-d->output];
        ptr = func_1001F5A4(r, arg2, out_ptr, buff, FIXED_SAMPLE, ptr);
    }

    return ptr;
}

Acmd *func_1001F5A4(RareALFx *r, s32 arg1, s16 *curr_ptr, s32 buff,
                    s32 count, Acmd *p) {
    Acmd *ptr = p;
    s32 after_end, before_end;
    s16 *updated_ptr, *delay_end;

    delay_end = &r->base[arg1][r->length];

    if (curr_ptr < r->base[arg1]) {
        curr_ptr += r->length;
    }

    updated_ptr = curr_ptr + count;

    if (updated_ptr > delay_end) {
        after_end = updated_ptr - delay_end;
        before_end = delay_end - curr_ptr;

        n_aLoadBuffer(ptr++, before_end << 1, buff,
                      osVirtualToPhysical(curr_ptr));
        n_aLoadBuffer(ptr++, after_end << 1, buff + (before_end << 1),
                      osVirtualToPhysical(r->base[arg1]));
    } else {
        n_aLoadBuffer(ptr++, count << 1, buff,
                      osVirtualToPhysical(curr_ptr));
    }

    return ptr;
}
// void *func_1001F5A4(void *arg0, s32 arg1, u32 arg2, s32 arg3, s32 arg4, void *arg5) {
//     void *sp34;
//     s32 sp30;
//     s32 sp2C;
//     u32 sp28;
//     u32 sp24;
//     void *sp20;
//     void *sp1C;
//     void *sp18;
//     void *temp_t3;
//     void *temp_t3_2;
//     void *temp_t7;
//
//     sp34 = arg5;
//     sp24 = (arg0 + (arg1 * 4))->unk20 + (*arg0 * 2);
//     if (arg2 < (u32) (arg0 + (arg1 * 4))->unk20) {
//         arg2 = arg2 + (*arg0 * 2);
//     }
//     sp28 = (arg4 * 2) + arg2;
//     if (sp24 < sp28) {
//         sp30 = (s32) (sp28 - sp24) >> 1;
//         sp2C = (s32) (sp24 - arg2) >> 1;
//         temp_t7 = sp34;
//         sp34 = temp_t7 + 8;
//         sp20 = temp_t7;
//         *temp_t7 = (s32) ((((sp2C * 2) & 0xFFF) << 0xC) | 0x4000000 | (arg3 & 0xFFF));
//         sp20->unk4 = osVirtualToPhysical(arg2);
//         temp_t3 = sp34;
//         sp34 = temp_t3 + 8;
//         sp1C = temp_t3;
//         sp1C->unk0 = (s32) ((((sp30 * 2) & 0xFFF) << 0xC) | 0x4000000 | ((arg3 + (sp2C * 2)) & 0xFFF));
//         sp1C->unk4 = osVirtualToPhysical((arg0 + (arg1 * 4))->unk20);
//     } else {
//         temp_t3_2 = sp34;
//         sp34 = temp_t3_2 + 8;
//         sp18 = temp_t3_2;
//         *temp_t3_2 = (s32) ((((arg4 * 2) & 0xFFF) << 0xC) | 0x4000000 | (arg3 & 0xFFF));
//         sp18->unk4 = osVirtualToPhysical(arg2);
//     }
//     return sp34;
// }

Acmd *func_1001F79C(RareALFx *arg0, s32 arg1, s16 *arg2, s32 arg3,
                    Acmd *arg4) {
    Acmd *sp34;
    s32 sp30;
    s32 sp2C;
    u32 sp28;
    u32 sp24;
    Acmd *sp20;
    Acmd *sp1C;
    Acmd *sp18;

    sp34 = arg4;
    sp24 = &arg0->base[arg1][arg0->length];
    if ((u32)arg2 < (u32)arg0->base[arg1]) {
        arg2 += arg0->length;
    }
    sp28 = &arg2[184];
    if (sp28 > sp24) {
        sp30 = (s32)(sp28 - sp24) >> 1;
        sp2C = (s32)(sp24 - (s32)arg2) >> 1;
        sp20 = sp34++;
        sp20->words.w0 = (((sp2C * 2) & 0xFFF) << 0xC) |
                          0x06000000 | (arg3 & 0xFFF);
        sp20->words.w1 = osVirtualToPhysical((void *)arg2);
        sp1C = sp34++;
        sp1C->words.w0 = (((sp30 * 2) & 0xFFF) << 0xC) |
                          0x06000000 |
                          ((arg3 + (sp2C * 2)) & 0xFFF);
        sp1C->words.w1 = osVirtualToPhysical(arg0->base[arg1]);
        if (1) {
        }
    } else {
        sp18 = sp34++;
        sp18->words.w0 = (arg3 & 0xFFF) | 0x06170000;
        sp18->words.w1 = osVirtualToPhysical((void *)arg2);
    }
    return sp34;
}
// void *func_1001F79C(void *arg0, s32 arg1, u32 arg2, s32 arg3, void *arg4) {
//     void *sp34;
//     s32 sp30;
//     s32 sp2C;
//     u32 sp28;
//     u32 sp24;
//     void *sp20;
//     void *sp1C;
//     void *sp18;
//     void *temp_t0;
//     void *temp_t7;
//     void *temp_t7_2;
//
//     sp34 = arg4;
//     sp24 = (arg0 + (arg1 * 4))->unk20 + (*arg0 * 2);
//     if (arg2 < (u32) (arg0 + (arg1 * 4))->unk20) {
//         arg2 = arg2 + (*arg0 * 2);
//     }
//     sp28 = arg2 + 0x170;
//     if (sp24 < sp28) {
//         sp30 = (s32) (sp28 - sp24) >> 1;
//         sp2C = (s32) (sp24 - arg2) >> 1;
//         temp_t0 = sp34;
//         sp34 = temp_t0 + 8;
//         sp20 = temp_t0;
//         *temp_t0 = (s32) ((((sp2C * 2) & 0xFFF) << 0xC) | 0x6000000 | (arg3 & 0xFFF));
//         sp20->unk4 = osVirtualToPhysical(arg2);
//         temp_t7 = sp34;
//         sp34 = temp_t7 + 8;
//         sp1C = temp_t7;
//         sp1C->unk0 = (s32) ((((sp30 * 2) & 0xFFF) << 0xC) | 0x6000000 | ((arg3 + (sp2C * 2)) & 0xFFF));
//         sp1C->unk4 = osVirtualToPhysical((arg0 + (arg1 * 4))->unk20);
//     } else {
//         temp_t7_2 = sp34;
//         sp34 = temp_t7_2 + 8;
//         sp18 = temp_t7_2;
//         sp18->unk0 = (s32) ((arg3 & 0xFFF) | 0x6170000);
//         sp18->unk4 = osVirtualToPhysical(arg2);
//     }
//     return sp34;
// }

/* Non-matching C placeholders for asm/nonmatchings/init_1E530/func_1001F978.s. */
Gfx *func_1001F978(struct55 *arg0, s32 arg1, s32 arg2, Gfx *arg3) {
    Gfx *sp24;
    s16 sp22;
    Gfx *sp1C;
    Gfx *sp18;

    sp24 = arg3;
    sp22 = arg2 >> 8;
    sp1C = sp24++;
    sp1C->words.w0 = 0x0B000020;
    sp1C->words.w1 = osVirtualToPhysical((s32)arg0 + 8);
    sp18 = sp24++;
    sp18->words.w0 = ((arg0->unk28 & 0xFF) << 0x10) | 0x0E000000 | (arg0->unk2 & 0xFFFF);
    sp18->words.w1 = (osVirtualToPhysical(*(s32 *)((s32)arg0 + (arg1 * 4) + 0x2C)) & 0x00FFFFFF) | ((sp22 & 0xFF) << 0x18);
    arg0->unk28 = 0;
    return sp24;
}
// NON-MATCHING: lots of work still to do
// struct56 *func_1001F978(struct55 *arg0, s32 arg1, s32 arg2, struct56 *arg3) {
//     struct56 *sp24;
//     s16 sp22;
//     struct56 *temp_t9;
//
//     sp24 = arg3;
//     sp22 = arg2 >> 8;
//     temp_t9 = sp24;
//     sp24 = temp_t9->unk8;
//     temp_t9->unk0 = 0xB000020;
//     temp_t9->unk4 = osVirtualToPhysical(&arg0->unk8);
//     temp_t9 = sp24;
//     sp24 = temp_t9->unk8;
//     temp_t9->unk0 = (s32) (((arg0->unk28 & 0xFF) << 0x10) | 0xE000000 | (arg0->unk2 & 0xFFFF));
//     temp_t9->unk4 = (s32) ((osVirtualToPhysical(arg0->unk2C[arg1]) & 0xFFFFFF) | ((sp22 & 0xFF) << 0x18));
//     arg0->unk28 = 0;
//     return sp24;
// }

f32 func_1001FA78(f32 arg0[4][4], s32 arg1) {
    f32 tmp;

    ((RareALDelay *)arg0)->rsval += ((RareALDelay *)arg0)->rsinc * arg1;
    if (((RareALDelay *)arg0)->rsval > 2.0f) {
        ((RareALDelay *)arg0)->rsval -= 4.0f;
    }
    else {
        ((RareALDelay *)arg0)->rsval = ((RareALDelay *)arg0)->rsval;
    }

    tmp = ((RareALDelay *)arg0)->rsval;
    tmp = tmp < 0.0f ? -tmp : tmp;
    tmp = tmp - 1.0f;

    return tmp * ((RareALDelay *)arg0)->rsgain;
}
