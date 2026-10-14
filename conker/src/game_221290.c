#include <ultra64.h>

void *func_151F85C4(s32 arg0, s32 arg1, s32 arg2);

s32 func_151F8088(void *arg0, s32 arg1);
s32 func_151F7F60(void *decoder);

#include "functions.h"
#include "variables.h"

extern f32 D_800B0C2C;
extern f32 D_800B0C30;
extern f32 D_800B0C34;
extern f32 D_800B0C38;
extern f32 D_800B0C3C;
extern f32 D_800B0C40;
extern f32 D_800B0C44;
extern f32 D_800B0C48;

extern s32 *D_800E0E20;
extern f32 *D_800E1078;
extern f32 D_800E0E38[];
extern f32 D_800E0EC8[];
extern f32 D_800E0FE8[];
extern s32 D_800E0E28;
extern s32 D_800E0E30;
extern f32 D_800E1080[];
extern f32 D_800E1480[];
extern f32 D_800B067C[];
extern f32 D_800B069C[];
extern s32 D_800E0E00;
extern u8 D_800E1880[];

// Scalefactor band boundary table: 23 long-block edges followed by 14
// short-block edges, one row per (sample rate, MPEG version) pair.
// splat named several interior elements as their own symbols -
// D_800AE99A is .l[1], D_800AE9A8 is .l[8], D_800AE9C6 is .s[0],
// D_800AE9C8 is .s[1] and D_800AE9CE is .s[4] - so those all
// disassemble back out of this one declaration.
typedef struct {
    s16 l[23];
    s16 s[14];
} SfBand;

// The 22-entry pre-emphasis table, copied wholesale onto the stack by
// func_151F42E8 (IDO expands the struct assignment into an inline
// 12-bytes-per-iteration copy loop).
typedef struct {
    s32 v[22];
} PreTab;

extern SfBand D_800AE998[];
extern PreTab D_800B0AB4;

// The MPEG-2 LSF scalefactor-length table: [preflag][region][window][4].
// func_151F578C copies the whole 288-byte table onto its stack (IDO
// expands the struct assignment into an inline copy loop) and then
// bcopy()s one 4-entry row out of the copy.
typedef struct {
    s32 v[2][3][3][4];
} SlenTab;

#define CODEC_SLEN_TABLE (*(SlenTab *)D_800B0B0C)
f32 func_1504A400(f32, f32);



/* Generated placeholder declarations. */
s32 func_151F63C4();
s32 func_151F78B4();
s32 func_151F86B0();
/* End generated placeholder declarations. */

typedef s32 (*func_151F6FD0_ReadFunc)(s32, void *, s32, s32);

s32 func_151F8960(void *arg0, void *arg1, s32 arg2);
s32 func_151F6FD0();

extern s32 D_800B06BC[];
extern s32 D_800B0734[];
extern s32 D_800B0B0C[];
extern u8 D_800AEB54[];
extern u8 D_800AEB5C[];
extern u8 D_800AEB6C[];
extern s16 D_800AEB7C[];

#define S32_AT(base, offset) (*(s32 *)((u8 *)(base) + (offset)))

/* Initialize codec windows, the x^(4/3) lookup, and geometric gain tables. */
s32 func_151F3DE0(void) {
    s32 i;
    f32 x;
    f32 xx;
    f32 delta;
    f32 t;
    f32 eps;
    f32 c;
    f32 d;

    i = 0;
    do {
        D_800E0E38[i] = sinf(((f32) i + 0.5f) * D_800B0C2C);
    } while (++i < 0x24);

    i = 0;
    do {
        D_800E0EC8[i] = sinf(((f32) i + 0.5f) * D_800B0C30);
    } while (++i < 0x12);

    i = 0x12;
    do {
        D_800E0EC8[i] = 1.0f;
    } while (++i < 0x18);

    i = 0x18;
    do {
        D_800E0EC8[i] = sinf((((f32) i + 0.5f) - 18.0f) * D_800B0C34);
    } while (++i < 0x1E);

    i = 0x1E;
    do {
        D_800E0EC8[i] = 0.0f;
    } while (++i < 0x24);

    i = 0;
    do {
        D_800E0FE8[i] = 0.0f;
    } while (++i < 6);

    i = 6;
    do {
        D_800E0FE8[i] = sinf((((f32) i + 0.5f) - 6.0f) * D_800B0C38);
    } while (++i < 0xC);

    i = 0xC;
    do {
        D_800E0FE8[i] = 1.0f;
    } while (++i < 0x12);

    i = 0x12;
    do {
        D_800E0FE8[i] = sinf(((f32) i + 0.5f) * D_800B0C3C);
    } while (++i < 0x24);

    i = 1;
    do {
        D_800E0E20[i] += D_800E0E28;
    } while (++i < 0x22);

    D_800E1078 = (f32 *) D_800E0E30;
    if (D_800E1078 == 0) {
        return 0;
    }

    x = 1.0f;
    D_800E1078[0] = 0.0f;

    i = 1;
    do {
        t = (f32) i;
        t = t * t;
        eps = t * D_800B0C40;
        t = t * t;
        do {
            xx = x * x;
            delta = (xx * x - t) / (2.0f * xx);
            x = x - delta;
        } while (delta > eps || delta < -eps);
        D_800E1078[i] = x;
    } while (++i < 0x2000);

    c = D_800B0C44;
    d = 0.25f;
    D_800E1080[0] = 1.0f;
    D_800E1480[0] = 1.0f;

    i = 1;
    do {
        D_800E1080[i] = c;
        D_800E1480[i] = d;
        d = d * 0.25f;
        c = c * D_800B0C48;
    } while (++i < 0x100);

    return 1;
}
/* Requantize one granule/channel spectrum using its gain and scalefactors. */
s32 func_151F42E8(void *arg0, s32 arg1, s32 arg2) {
    s32 idx;
    s32 next;
    s32 bandStart;
    s32 bandWidth;
    PreTab tbl;
    f32 lval[22];
    f32 sval[3][13];
    f32 gain;
    s32 sb;
    s32 win;
    s32 pre;
    s32 sfs;
    s32 sfi;
    s32 i;
    s32 cnt;
    f32 *out;
    s16 *isp;
    u8 *sgn;
    s32 flagA;
    s32 flagB;
    s32 mixed;
    s32 nextEdge;
    f32 *srow;

    tbl = D_800B0AB4;
    idx = *(s32 *) ((char *) arg0 + 0x3BA4) * 3 + *(s32 *) ((char *) arg0 + 0x3BB4);

    if (*(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3C98) != 0 &&
        *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA0) == 2) {
        if (*(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA8) != 0) {
            next = D_800AE998[idx].l[1];
        } else {
            next = D_800AE998[idx].s[1] * 3;
            bandWidth = D_800AE998[idx].s[1];
            bandStart = 0;
        }
    } else {
        next = D_800AE998[idx].l[1];
    }

    gain = func_1504A400(2.0f,
        ((f32) *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3C88) - 210.0f) * 0.25f);
    pre = *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CF8);

    for (sb = 0; sb < 0x16; sb++) {
        sfi = (((s32 *) ((char *) arg0 + arg1 * 248 + arg2 * 248 + 0x3D08))[sb]
               + *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CF0) * tbl.v[sb])
              * (pre + 1);
        lval[sb] = D_800E1080[sfi] * gain;
    }

    for (win = 0; win < 3; win++) {
        for (sb = 0; sb < 0xD; sb++) {
            sfs = *(s32 *) ((char *) arg0 + arg1 * 12 + arg2 * 12 + win * 4 + 0x3CC8);
            sfi = *(s32 *) ((char *) arg0 + arg1 * 248 + arg2 * 248 + win * 52 + sb * 4 + 0x3D64)
                  * (pre + 1);
            sval[win][sb] = (gain * D_800E1480[sfs]) * D_800E1080[sfi];
        }
    }

    sb = 0;
    i = 0;
    cnt = *(s32 *) ((char *) arg0 + arg2 * 4 + 0x465C);
    out = (f32 *) ((char *) arg0 + arg2 * 2304 + 0x4664);
    isp = (s16 *) ((char *) arg0 + arg2 * 1156 + 0x3F94);
    sgn = (u8 *) ((char *) arg0 + arg2 * 578 + 0x4418);

    flagA = *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA0) == 2 &&
            *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA8) == 0;
    flagB = *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA0) == 2 &&
            *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA8) != 0;
    mixed = *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3C98);

    while (i < cnt) {
        if (next > cnt) {
            next = cnt;
        }
        if (mixed != 0 && (flagA != 0 || (flagB != 0 && i >= 0x24))) {
            win = (i - bandStart) / bandWidth;
            nextEdge = bandStart + bandWidth;
        }
        while (i < next) {
            if (mixed != 0 && (flagA != 0 || (flagB != 0 && i >= 0x24))) {
                if (i >= nextEdge) {
                    nextEdge += bandWidth;
                    win++;
                }
                srow = sval[win];
                if (*sgn++) {
                    *out++ = -(D_800E1078[*isp++] * srow[sb]);
                } else {
                    *out++ = D_800E1078[*isp++] * srow[sb];
                }
            } else {
                if (*sgn++) {
                    *out++ = -(D_800E1078[*isp++] * lval[sb]);
                } else {
                    *out++ = D_800E1078[*isp++] * lval[sb];
                }
            }
            i++;
        }
        if (*(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3C98) != 0 &&
            *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA0) == 2) {
            if (*(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA8) != 0) {
                if (D_800AE998[idx].l[8] == i) {
                    next = D_800AE998[idx].s[4] * 3;
                    sb = 3;
                    bandWidth = D_800AE998[idx].s[sb + 1] - D_800AE998[idx].s[sb];
                    bandStart = D_800AE998[idx].s[sb] * 3;
                } else {
                    if (i < D_800AE998[idx].l[8]) {
                        next = D_800AE998[idx].l[++sb + 1];
                    } else {
                        next = D_800AE998[idx].s[++sb + 1] * 3;
                        bandWidth = D_800AE998[idx].s[sb + 1] - D_800AE998[idx].s[sb];
                        bandStart = D_800AE998[idx].s[sb] * 3;
                    }
                }
            } else {
                next = D_800AE998[idx].s[++sb + 1] * 3;
                bandWidth = D_800AE998[idx].s[sb + 1] - D_800AE998[idx].s[sb];
                bandStart = D_800AE998[idx].s[sb] * 3;
            }
        } else {
            next = D_800AE998[idx].l[++sb + 1];
        }
    }

    if (i < 0x240) {
        bzero(out, *(s32 *) ((char *) arg0 + arg2 * 4 + 0x4660) * 4);
        return 1;
    }
    return 1;
}
// NON-MATCHING: bitstream table fill lifted with raw decoder offsets
s32 func_151F4F38(void *arg0, s32 arg1, s32 arg2) {
    u8 *base;
    s32 table_offset;
    s32 sample_base;
    s32 code;
    s32 i;
    s32 j;
    s32 k;
    s32 bit_count;
    s32 group;

    base = arg0;
    table_offset = (arg1 * 4) + (arg2 * 4);
    sample_base = (arg1 * 0xF8) + (arg2 * 0xF8);
    code = S32_AT(base, 0x3C90 + table_offset);

    if ((S32_AT(base, 0x3C98 + table_offset) != 0) && (S32_AT(base, 0x3CA0 + table_offset) == 2)) {
        if (S32_AT(base, 0x3CA8 + table_offset) != 0) {
            for (i = 0; i < 8; i++) {
                bit_count = D_800AEB5C[code];
                if (bit_count != 0) {
                    S32_AT(base, 0x3D08 + sample_base + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                } else {
                    S32_AT(base, 0x3D08 + sample_base + (i * 4)) = 0;
                }
            }

            for (i = 3; i < 6; i++) {
                for (j = 0; j < 3; j++) {
                    bit_count = D_800AEB5C[code];
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = 0;
                    }
                }
            }

            for (i = 6; i < 0xC; i++) {
                for (j = 0; j < 3; j++) {
                    bit_count = D_800AEB6C[code];
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = 0;
                    }
                }
            }
        } else {
            for (k = 0; k < 2; k++) {
                for (i = D_800AEB54[k + 5]; i < D_800AEB54[k + 6]; i++) {
                    for (j = 0; j < 3; j++) {
                        bit_count = D_800AEB5C[(k * 0x10) + code];
                        if (bit_count != 0) {
                            S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                        } else {
                            S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = 0;
                        }
                    }
                }
            }
        }

        for (j = 0; j < 3; j++) {
            S32_AT(base, 0x3D94 + sample_base + (j * 0x34)) = 0;
        }
    } else {
        for (k = 0; k < 4; k++) {
            if ((S32_AT(base, 0x3BF8 + (arg2 * 0x80) + (k * 4)) == 0) || (arg1 == 0)) {
                for (i = D_800AEB54[k]; i < D_800AEB54[k + 1]; i++) {
                    if (k < 2) {
                        group = 0;
                    } else {
                        group = 1;
                    }
                    bit_count = D_800AEB5C[(group * 0x10) + code];
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D08 + sample_base + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D08 + sample_base + (i * 4)) = 0;
                    }
                }
            } else {
                for (i = D_800AEB54[k]; i < D_800AEB54[k + 1]; i++) {
                    S32_AT(base, 0x3E00 + (arg2 * 0xF8) + (i * 4)) = S32_AT(base, 0x3D08 + (arg2 * 0xF8) + (i * 4));
                }
            }
        }
        S32_AT(base, 0x3D60 + sample_base) = 0;
    }

    return 1;
}
/* Decode MPEG-2 low-sampling-frequency scalefactors and intensity-stereo masks. */
s32 func_151F578C(void *arg0, s32 arg1, s32 arg2) {
    SlenTab tbl;
    s32 slen[4];
    s32 sfc;
    s32 *pre;
    s32 mixedFlag;
    s32 blockType;
    s32 winSwitch;
    s32 a;
    s32 b;
    s32 i;
    s32 j;
    s32 half;
    s32 nr[4];
    s32 k;
    s32 sl;
    s32 mask;

    tbl = CODEC_SLEN_TABLE;
    sfc = *(s32 *) ((char *) arg0 + arg2 * 4 + 0x3C90);
    pre = (s32 *) ((char *) arg0 + arg2 * 4 + 0x3CF0);
    mixedFlag = *(s32 *) ((char *) arg0 + arg2 * 4 + 0x3CA8);
    blockType = *(s32 *) ((char *) arg0 + arg2 * 4 + 0x3CA0);
    winSwitch = *(s32 *) ((char *) arg0 + arg2 * 4 + 0x3C98);

    if ((*(s32 *) ((char *) arg0 + 0x3BC4) != 1 && *(s32 *) ((char *) arg0 + 0x3BC4) != 3) ||
        arg2 != 1) {
        a = 0;
        if (sfc < 0x190) {
            slen[0] = (sfc >> 4) / 5;
            slen[1] = (sfc >> 4) % 5;
            slen[2] = (sfc % 16) >> 2;
            slen[3] = sfc % 4;
            *pre = 0;
            b = 0;
        } else if (sfc >= 0x190 && sfc < 0x1F4) {
            slen[0] = ((sfc - 0x190) >> 2) / 5;
            slen[1] = ((sfc - 0x190) >> 2) % 5;
            slen[2] = (sfc - 0x190) % 4;
            slen[3] = 0;
            *pre = 0;
            b = 1;
        } else if (sfc >= 0x1F4 && sfc < 0x200) {
            slen[0] = (sfc - 0x1F4) / 3;
            slen[1] = (sfc - 0x1F4) % 3;
            slen[2] = 0;
            slen[3] = 0;
            *pre = 1;
            b = 2;
        }
    }

    if ((*(s32 *) ((char *) arg0 + 0x3BC4) == 1 || *(s32 *) ((char *) arg0 + 0x3BC4) == 3) &&
        arg2 == 1) {
        *(s32 *) ((char *) arg0 + 0x3EF8) = sfc % 2;
        half = sfc >> 1;
        a = 1;
        if (half < 0xB4) {
            slen[0] = half / 0x24;
            slen[1] = (half % 0x24) / 6;
            slen[2] = (half % 0x24) % 6;
            slen[3] = 0;
            *pre = 0;
            b = 0;
        } else if (half >= 0xB4 && half < 0xF4) {
            slen[0] = ((half - 0xB4) % 0x40) >> 4;
            slen[1] = ((half - 0xB4) % 16) >> 2;
            slen[2] = (half - 0xB4) % 4;
            slen[3] = 0;
            *pre = 0;
            b = 1;
        } else if (half >= 0xF4 && half < 0xFF) {
            slen[0] = (half - 0xF4) / 3;
            slen[1] = (half - 0xF4) % 3;
            slen[2] = 0;
            slen[3] = 0;
            *pre = 0;
            b = 2;
        }
    }

    if (winSwitch != 0 && blockType == 2) {
        bcopy(tbl.v[a][b][mixedFlag + 1], nr, 0x10);
    } else {
        bcopy(tbl.v[a][b][0], nr, 0x10);
    }

    k = 0;
    if (winSwitch == 0 || (winSwitch != 0 && blockType != 2)) {
        for (i = 0; i < 4; i++) {
            sl = slen[i];
            mask = (1 << sl) - 1;
            for (j = 0; j < nr[i]; j++) {
                *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3D08) =
                    sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                if (arg2 != 0) {
                    *(s32 *) ((char *) arg0 + k * 4 + 0x3EFC) = mask;
                }
                k++;
            }
        }
    } else {
        if (blockType == 2) {
            if (mixedFlag == 0) {
                for (i = 0; i < 4; i++) {
                    sl = slen[i];
                    mask = (1 << sl) - 1;
                    for (j = 0; j < nr[i]; j += 3) {
                        *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3D64) =
                            sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                        *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3D98) =
                            sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                        *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3DCC) =
                            sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                        if (arg2 != 0) {
                            *(s32 *) ((char *) arg0 + k * 4 + 0x3F14) = mask;
                        }
                        k++;
                    }
                }
            } else {
                sl = slen[0];
                mask = (1 << sl) - 1;
                for (j = 0; j < 6; j++) {
                    *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3D08) =
                        sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                    if (arg2 != 0) {
                        *(s32 *) ((char *) arg0 + k * 4 + 0x3EFC) = mask;
                    }
                    k++;
                }
                nr[0] -= 6;
                k = 3;
                for (i = 0; i < 4; i++) {
                    sl = slen[i];
                    mask = (1 << sl) - 1;
                    for (j = 0; j < nr[i]; j += 3) {
                        *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3D64) =
                            sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                        *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3D98) =
                            sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                        *(s32 *) ((char *) arg0 + arg2 * 248 + k * 4 + 0x3DCC) =
                            sl ? func_151F8960((char *) arg0 + 0x1C, (char *) arg0 + 0x2020, sl) : 0;
                        if (arg2 != 0) {
                            *(s32 *) ((char *) arg0 + k * 4 + 0x3F14) = mask;
                        }
                        k++;
                    }
                }
            }
        }
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F63C4.s. */
s32 func_151F63C4() {
    return 0;
}
/* Reorder short-block spectral samples, or copy the long-block spectrum. */
s32 func_151F6970(void *arg0, s32 arg1) {
    s16 *tbl;
    f32 *dst;
    f32 *src;
    s32 i;

    tbl = (s16 *) ((char *) D_800AEB7C
                   + *(s32 *) ((char *) arg0 + 0x3BA4) * 3456
                   + *(s32 *) ((char *) arg0 + 0x3BB4) * 1152);
    dst = (f32 *) ((char *) arg0 + 0x4F64);
    src = (f32 *) ((char *) arg0 + 0x4664);
    i = 0;

    if (*(s32 *) ((char *) arg0 + arg1 * 4 + 0x3C98) != 0 &&
        *(s32 *) ((char *) arg0 + arg1 * 4 + 0x3CA0) == 2) {
        if (*(s32 *) ((char *) arg0 + arg1 * 4 + 0x3CA8) != 0) {
            while (i++ < 0x24) {
                *dst++ = *src++;
            }
        }
        while (i < 0x240) {
            dst[tbl[i++]] = *src++;
        }
    } else {
        while (i++ < 0x240) {
            *dst++ = *src++;
        }
    }

    return 1;
}
/* Apply the eight butterfly rotations between adjacent long-block subbands. */
s32 func_151F6B28(void *arg0, s32 arg1, s32 arg2) {
    s32 k;
    f32 *p;
    f32 a;
    f32 b;

    if (*(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3C98) != 0 &&
        *(s32 *) ((char *) arg0 + arg1 * 4 + arg2 * 4 + 0x3CA0) == 2) {
        return 1;
    }

    k = 1;
    do {
        p = (f32 *) ((char *) arg0 + arg2 * 2304 + k * 72 + 0x4F64);

        a = p[0];
        b = p[-1];
        p[-1] = b * D_800B069C[0] - D_800B067C[0] * a;
        p[0] = a * D_800B069C[0] + D_800B067C[0] * b;

        a = p[1];
        b = p[-2];
        p[-2] = b * D_800B069C[1] - D_800B067C[1] * a;
        p[1] = a * D_800B069C[1] + D_800B067C[1] * b;

        a = p[2];
        b = p[-3];
        p[-3] = b * D_800B069C[2] - D_800B067C[2] * a;
        p[2] = a * D_800B069C[2] + D_800B067C[2] * b;

        a = p[3];
        b = p[-4];
        p[-4] = b * D_800B069C[3] - D_800B067C[3] * a;
        p[3] = a * D_800B069C[3] + D_800B067C[3] * b;

        a = p[4];
        b = p[-5];
        p[-5] = b * D_800B069C[4] - D_800B067C[4] * a;
        p[4] = a * D_800B069C[4] + D_800B067C[4] * b;

        a = p[5];
        b = p[-6];
        p[-6] = b * D_800B069C[5] - D_800B067C[5] * a;
        p[5] = a * D_800B069C[5] + D_800B067C[5] * b;

        a = p[6];
        b = p[-7];
        p[-7] = b * D_800B069C[6] - D_800B067C[6] * a;
        p[6] = a * D_800B069C[6] + D_800B067C[6] * b;

        a = p[7];
        b = p[-8];
        p[-8] = b * D_800B069C[7] - D_800B067C[7] * a;
        p[7] = a * D_800B069C[7] + D_800B067C[7] * b;
    } while (++k < 0x20);

    return 1;
}

// NON-MATCHING: opaque asset-loader struct, offset overlay for first C pass
s32 func_151F6FD0(void *arg0) {
    u8 *base;
    void *read_base;
    void *read_state;
    func_151F6FD0_ReadFunc read_func;
    s32 count;
    s32 i;
    s32 j;
    s32 k;
    s32 field_size;
    s32 table_offset;
    s32 table_stride;

    base = arg0;
    if (S32_AT(base, 0x3BA4) != 0) {
        if (S32_AT(base, 0x3BC0) == 3) {
            S32_AT(base, 0x206C) = 0x11;
        } else {
            S32_AT(base, 0x206C) = 0x20;
        }
    } else if (S32_AT(base, 0x3BC0) == 3) {
        S32_AT(base, 0x206C) = 9;
    } else {
        S32_AT(base, 0x206C) = 0x11;
    }

    read_func = (func_151F6FD0_ReadFunc)S32_AT(base, 4);
    count = read_func(S32_AT(base, 0), base + S32_AT(base, 0x2068) + 0x2024, S32_AT(base, 0x206C), -1);
    if (S32_AT(base, 0x206C) != count) {
        return 0;
    }
    S32_AT(base, 0x18) += S32_AT(base, 0x206C);

    if (S32_AT(base, 0x3BC0) == 3) {
        S32_AT(base, 0x3F8C) = 1;
    } else {
        S32_AT(base, 0x3F8C) = 2;
    }
    if (S32_AT(base, 0x3BA4) != 0) {
        S32_AT(base, 0x3F90) = 2;
    } else {
        S32_AT(base, 0x3F90) = 1;
    }

    read_base = base + 0x2024;
    read_state = base + 0x2064;
    if (S32_AT(base, 0x3BA4) != 0) {
        S32_AT(base, 0x3BF4) = func_151F8960(read_base, read_state, 9);
        if (S32_AT(base, 0x3F8C) == 1) {
            func_151F8960(read_base, read_state, 5);
        } else {
            func_151F8960(read_base, read_state, 3);
        }
    } else {
        S32_AT(base, 0x3BF4) = func_151F8960(read_base, read_state, 8);
        if (S32_AT(base, 0x3F8C) == 1) {
            func_151F8960(read_base, read_state, 1);
        } else {
            func_151F8960(read_base, read_state, 2);
        }
    }

    if (S32_AT(base, 0x3BA4) != 0) {
        for (i = 0; i < S32_AT(base, 0x3F8C); i++) {
            for (j = 0; j < 4; j++) {
                S32_AT(base, 0x3BF8 + (i * 0x80) + (j * 4)) = func_151F8960(read_base, read_state, 1);
            }
        }
    }

    if (S32_AT(base, 0x3BA4) != 0) {
        field_size = 4;
    } else {
        field_size = 9;
    }

    for (i = 0; i < S32_AT(base, 0x3F90); i++) {
        for (j = 0; j < S32_AT(base, 0x3F8C); j++) {
            table_offset = (i * 4) + (j * 4);
            S32_AT(base, 0x3C78 + table_offset) = func_151F8960(read_base, read_state, 0xC);
            S32_AT(base, 0x3C80 + table_offset) = func_151F8960(read_base, read_state, 9);
            S32_AT(base, 0x3C88 + table_offset) = func_151F8960(read_base, read_state, 8);
            if (field_size != 0) {
                S32_AT(base, 0x3C90 + table_offset) = func_151F8960(read_base, read_state, field_size);
            } else {
                S32_AT(base, 0x3C90 + table_offset) = 0;
            }
            S32_AT(base, 0x3C98 + table_offset) = func_151F8960(read_base, read_state, 1);
            table_stride = (i * 0xC) + (j * 0xC);
            if (S32_AT(base, 0x3C98 + table_offset) != 0) {
                S32_AT(base, 0x3CA0 + table_offset) = func_151F8960(read_base, read_state, 2);
                S32_AT(base, 0x3CA8 + table_offset) = func_151F8960(read_base, read_state, 1);
                for (k = 0; k < 2; k++) {
                    S32_AT(base, 0x3CB0 + table_stride + (k * 4)) = func_151F8960(read_base, read_state, 5);
                }
                S32_AT(base, 0x3CB8 + table_stride) = 0;
                for (k = 0; k < 3; k++) {
                    S32_AT(base, 0x3CC8 + table_stride + (k * 4)) = func_151F8960(read_base, read_state, 3);
                }
            } else {
                S32_AT(base, 0x3CA0 + table_offset) = 0;
                S32_AT(base, 0x3CA8 + table_offset) = 0;
                for (k = 0; k < 3; k++) {
                    S32_AT(base, 0x3CB0 + table_stride + (k * 4)) = func_151F8960(read_base, read_state, 5);
                }
                S32_AT(base, 0x3CE0 + table_offset) = func_151F8960(read_base, read_state, 4);
                S32_AT(base, 0x3CE8 + table_offset) = func_151F8960(read_base, read_state, 3);
            }
            if (S32_AT(base, 0x3BA4) != 0) {
                S32_AT(base, 0x3CF0 + table_offset) = func_151F8960(read_base, read_state, 1);
            }
            S32_AT(base, 0x3CF8 + table_offset) = func_151F8960(read_base, read_state, 1);
            S32_AT(base, 0x3D00 + table_offset) = func_151F8960(read_base, read_state, 1);
        }
    }

    S32_AT(base, 0x3F7C) = D_800B06BC[(S32_AT(base, 0x3BA4) * 15) + S32_AT(base, 0x3BB0)];
    S32_AT(base, 0x3F80) = D_800B0734[(S32_AT(base, 0x3BA4) * 4) + S32_AT(base, 0x3BB4)];
    if (S32_AT(base, 0x3BA4) != 0) {
        S32_AT(base, 0x3F84) = (S32_AT(base, 0x3F7C) * 0x90) / S32_AT(base, 0x3F80);
    } else {
        S32_AT(base, 0x3F84) = (S32_AT(base, 0x3F7C) * 0x48) / S32_AT(base, 0x3F80);
    }
    S32_AT(base, 0x3F88) = (S32_AT(base, 0x3F84) + S32_AT(base, 0x3BB8)) - (S32_AT(base, 0x2068) + S32_AT(base, 0x206C));
    return 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F78B4.s. */
s32 func_151F78B4() {
    return 0;
}
/* Refill the codec input window, compacting bytes and padding a short read. */
s32 func_151F7F60(void *decoder) {
    s32 shiftBytes = 0x1000;
    s32 bytesRead;

    if (*(s32 *)((char *)decoder + 0x3F88) + *(s32 *)((char *)decoder + 0x201C) >= 0x1FFC) {
        bcopy((char *)decoder + shiftBytes + 0x1C, (char *)decoder + 0x1C, shiftBytes);
        *(s32 *)((char *)decoder + 0x201C) -= shiftBytes;
        *(s32 *)((char *)decoder + 0x2020) -= shiftBytes << 3;
    }

    bytesRead = ((func_151F6FD0_ReadFunc)(*(s32 *)((char *)decoder + 4)))(
        *(s32 *)decoder,
        (char *)decoder + *(s32 *)((char *)decoder + 0x201C) + 0x1C,
        *(s32 *)((char *)decoder + 0x3F88),
        -1);

    if (bytesRead < *(s32 *)((char *)decoder + 0x3F88)) {
        bzero((char *)decoder + bytesRead + 0x1C, *(s32 *)((char *)decoder + 0x3F88) - bytesRead);
    }

    *(s32 *)((char *)decoder + 0x18) += *(s32 *)((char *)decoder + 0x3F88);
    *(s32 *)((char *)decoder + 0x201C) += *(s32 *)((char *)decoder + 0x3F88);

    return *(s32 *)((char *)decoder + 0x201C) - *(s32 *)((char *)decoder + 0x3F88);
}
/* Synchronize and validate a frame header, then dispatch its side-info parser. */
s32 func_151F8088(void *arg0, s32 arg1) {
    s32 sync;
    s32 n;
    s32 r;
    u8 mask;

    if (arg1 != -1) {
        *(s32 *) ((char *) arg0 + 0x18) = arg1;
    }

    sync = arg1;
    n = 0;
    mask = 0xFF;

    for (;;) {
        r = ((s32 (*)(void *, void *, s32, s32)) *(void **) ((char *) arg0 + 4))(
                *(void **) arg0, (char *) arg0 + n + 0x2024, 1, sync);
        if (r <= 0) {
            return 0;
        }
        sync = -1;
        *(s32 *) ((char *) arg0 + 0x18) += 1;

        if (*(u8 *) ((char *) arg0 + n + 0x2024) != 0xFF &&
            *(u8 *) ((char *) arg0 + n + 0x2024) != 0xF3) {
            return 0;
        }

        if ((*(u8 *) ((char *) arg0 + n + 0x2024) & mask) != mask) {
            mask = 0xFF;
            n = 0;
            continue;
        }
        n++;
        if (mask == 0xF0) {
            break;
        }
        mask = 0xF0;
    }

    r = ((s32 (*)(void *, void *, s32, s32)) *(void **) ((char *) arg0 + 4))(
            *(void **) arg0, (char *) arg0 + 0x2026, 2, -1);
    if (r <= 0) {
        return 0;
    }
    *(s32 *) ((char *) arg0 + 0x18) += 2;
    *(s32 *) ((char *) arg0 + 0x2064) = 0xC;

    *(s32 *) ((char *) arg0 + 0x3BA4) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 1);
    *(s32 *) ((char *) arg0 + 0x3BA8) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 2);
    *(s32 *) ((char *) arg0 + 0x3BAC) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 1);
    *(s32 *) ((char *) arg0 + 0x3BB0) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 4);
    *(s32 *) ((char *) arg0 + 0x3BB4) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 2);
    *(s32 *) ((char *) arg0 + 0x3BB8) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 1);
    *(s32 *) ((char *) arg0 + 0x3BBC) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 1);
    *(s32 *) ((char *) arg0 + 0x3BC0) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 2);
    *(s32 *) ((char *) arg0 + 0x3BC4) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 2);
    *(s32 *) ((char *) arg0 + 0x3BC8) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 1);
    *(s32 *) ((char *) arg0 + 0x3BCC) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 1);
    *(s32 *) ((char *) arg0 + 0x3BD0) = func_151F8960((char *) arg0 + 0x2024, (char *) arg0 + 0x2064, 2);

    if (*(s32 *) ((char *) arg0 + 0x3BB0) == 0xF ||
        *(s32 *) ((char *) arg0 + 0x3BB4) == 3) {
        return func_151F8088(arg0, -1);
    }

    if (*(s32 *) ((char *) arg0 + 0x3BD4) == 0) {
        *(s32 *) ((char *) arg0 + 0x3BD4) = 1;
        *(s32 *) ((char *) arg0 + 0x3BD8) = *(s32 *) ((char *) arg0 + 0x3BA4);
        *(s32 *) ((char *) arg0 + 0x3BDC) = *(s32 *) ((char *) arg0 + 0x3BA8);
        *(s32 *) ((char *) arg0 + 0x3BE0) = *(s32 *) ((char *) arg0 + 0x3BAC);
        *(s32 *) ((char *) arg0 + 0x3BE4) = *(s32 *) ((char *) arg0 + 0x3BB4);
        *(s32 *) ((char *) arg0 + 0x3BE8) = *(s32 *) ((char *) arg0 + 0x3BC0);
        *(s32 *) ((char *) arg0 + 0x3BEC) = *(s32 *) ((char *) arg0 + 0x3BC8);
        *(s32 *) ((char *) arg0 + 0x3BF0) = *(s32 *) ((char *) arg0 + 0x3BCC);
    } else if (*(s32 *) ((char *) arg0 + 0x3BD8) != *(s32 *) ((char *) arg0 + 0x3BA4) ||
               *(s32 *) ((char *) arg0 + 0x3BDC) != *(s32 *) ((char *) arg0 + 0x3BA8) ||
               *(s32 *) ((char *) arg0 + 0x3BE0) != *(s32 *) ((char *) arg0 + 0x3BAC) ||
               *(s32 *) ((char *) arg0 + 0x3BE4) != *(s32 *) ((char *) arg0 + 0x3BB4) ||
               *(s32 *) ((char *) arg0 + 0x3BE8) != *(s32 *) ((char *) arg0 + 0x3BC0) ||
               *(s32 *) ((char *) arg0 + 0x3BF0) != *(s32 *) ((char *) arg0 + 0x3BCC)) {
        return func_151F8088(arg0, -1);
    }

    *(s32 *) ((char *) arg0 + 0x2068) = 4;

    if (*(s32 *) ((char *) arg0 + 0x3BAC) == 0) {
        r = ((s32 (*)(void *, void *, s32, s32)) *(void **) ((char *) arg0 + 4))(
                *(void **) arg0, (char *) arg0 + 0x2028, 2, -1);
        if (r <= 0) {
            return 0;
        }
        *(s32 *) ((char *) arg0 + 0x18) += 2;
        *(s32 *) ((char *) arg0 + 0x2064) += 0x10;
        *(s32 *) ((char *) arg0 + 0x2068) = 6;
    }

    if (*(s32 *) ((char *) arg0 + 0x3BA8) == 1) {
        *(s32 *) ((char *) arg0 + 0x8478) = (s32) func_151F78B4;
        *(s32 *) ((char *) arg0 + 0x847C) = (s32) func_151F6FD0;
    } else if (*(s32 *) ((char *) arg0 + 0x3BA8) == 2) {
        return 0;
    } else if (*(s32 *) ((char *) arg0 + 0x3BA8) == 3) {
        return 0;
    }

    if (((s32 (*)(void *)) *(void **) ((char *) arg0 + 0x847C))(arg0) == 0) {
        return 0;
    }

    return 1;
}
/* Initialize the fixed codec buffer and reject an invalid opening frame. */
void *func_151F85C4(s32 arg0, s32 arg1, s32 arg2) {
    void *obj = D_800E1880;

    if (obj == 0) {
        return 0;
    }

    *(s32 *) ((char *) obj + 0xC) = -1;
    *(s32 *) ((char *) obj + 0x10) = -1;
    *(s32 *) ((char *) obj + 0x14) = -1;
    *(s32 *) ((char *) obj + 0x0) = arg0;
    *(s32 *) ((char *) obj + 0x4) = arg1;
    *(s32 *) ((char *) obj + 0x8) = arg2;
    *(s32 *) ((char *) obj + 0x201C) = 0;
    *(s32 *) ((char *) obj + 0x2020) = 0;
    *(s32 *) ((char *) obj + 0x3BA0) = 0;

    if (func_151F8088(obj, 0) == 0) {
        return 0;
    }

    *(s32 *) ((char *) obj + 0x8474) = 0;
    bzero((char *) obj + 0x6A64, 0x900);

    return obj;
}
// void *func_151F85C4(s32 arg0, s32 arg1, s32 arg2) {
//     void *sp1C;
//
//     sp1C = (void *)0x800E1880;
//     if (sp1C == 0) {
//         return NULL;
//     }
//     sp1C->unkC = -1;
//     sp1C->unk10 = -1;
//     sp1C->unk14 = -1;
//     sp1C->unk0 = arg0;
//     sp1C->unk4 = arg1;
//     sp1C->unk8 = arg2;
//     sp1C->unk201C = 0;
//     sp1C->unk2020 = 0;
//     sp1C->unk3BA0 = 0;
//     if (func_151F8088(sp1C, 0) == 0) {
//         return NULL;
//     }
//     sp1C->unk8474 = 0;
//     bzero(sp1C + 0x6A64, 0x900);
//     return sp1C;
// }

/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F86B0.s. */
s32 func_151F86B0() {
    return 0;
}

#undef S32_AT
