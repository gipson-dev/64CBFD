#include <ultra64.h>
#include "stdlib.h"
#include "string.h"

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_10001AA8();
s16 func_100019F0(s16 *arg0, struct05 *arg1);
/* End generated placeholder declarations. */

void func_10001420(void) {
    u32 base = (u32)&D_80043B40;
    u32 *cursor = (u32 *)base;
    u32 *end = (u32 *)(base + 0xFE0);

    do {
        *cursor++ = 0;
    } while (cursor < end);
}

void func_10001444(void) {
    u32 saveMask = __osDisableInt();
    func_100061F8(2, 31);
    func_10001420();
    func_10005BE0();
    osInvalICache(&D_1002AAD0, 0x80400000 - (u32)&D_1002AAD0);
    __osRestoreInt(saveMask);
}

void func_100014A0(void) {
    osStopThread(&D_80031AE0);
}

void func_100014C4(s32 arg0) {
    u32 saveMask = __osDisableInt();
    func_100061F8(2, 31);

    if (0) {};

    if (D_8003BE74) {
        func_10004074(D_8003BE74 | 0x80000000);
    }
    if (D_8003BE70) {
        func_10004074(D_8003BE70 | 0x80000000);
    }
    func_10005B04(arg0);
    func_10001420();
    func_10005BE0();
    __osRestoreInt(saveMask);
}

void func_10001550(struct246 *arg0, u8 arg1) {
    u8 buf[0x20];
    u8 *ptr;
    f64 val;
    volatile f64 zero2;
    s32 err;
    s16 nsig;
    f32 zero;
    f32 one;

    {
    s16 exp;
    ptr = buf;
    val = arg0->unk0;
    zero = 0;
    one = 1;
    zero2 = zero;
    if (arg0->unk24 < 0) {
        arg0->unk24 = 6;
    } else if (arg0->unk24 == 0 && (arg1 == 'g' || arg1 == 'G')) {
        arg0->unk24 = 1;
    }
    err = func_100019F0(&exp, (struct05 *)arg0);
    if (err > 0) {
        memcpy(arg0->unk8, (err == 2) ? D_8002BF68 : D_8002BF6C,
               arg0->unk14 = 3);
        return;
    }
    if (err == 0) {
        nsig = 0;
        exp = 0;
    } else {
        {
            s32 i;
            s32 n;

            if (val < zero) {
                val = -val;
            }
            exp = exp * 30103 / 0x000186A0 - 4;
            if (exp < 0) {
                n = (3 - exp) & ~3;
                exp = -n;
                for (i = 0; n > 0; n >>= 1, i++) {
                    if ((n & 1) != 0) {
                        val *= D_8002BF20[i];
                    }
                }
            } else if (exp > 0) {
                f64 factor = one;

                exp &= ~3;
                for (n = exp, i = 0; n > 0; n >>= 1, i++) {
                    if ((n & 1) != 0) {
                        factor *= D_8002BF20[i];
                    }
                }
                val /= factor;
            }
        }
        {
            s32 gen;
            s32 j;
            s32 lo;

            gen = ((arg1 == 'f') ? exp + 10 : 6) + arg0->unk24;
            if (gen > 0x13) {
                gen = 0x13;
            }
            *ptr++ = '0';
            if (gen > 0 && zero < val) {
                do {
                    lo = val;
                    if ((gen -= 8) > 0) {
                        val = (val - lo) * D_8002BF78;
                    }
                    ptr = ptr + 8;
                    for (j = 8; lo > 0 && --j >= 0;) {
                        ldiv_t qr = ldiv(lo, 10);

                        *--ptr = qr.rem + '0';
                        lo = qr.quot;
                    }
                    while (--j >= 0) {
                        ptr--;
                        *ptr = '0';
                    }
                    ptr += 8;
                } while (gen > 0 && zero2 < val);
            }

            gen = ptr - &buf[1];
            for (ptr = &buf[1], exp += 7; *ptr == '0'; ptr++) {
                --gen, --exp;
            }

            nsig = ((arg1 == 'f') ? exp + 1 :
                    ((arg1 == 'e' || arg1 == 'E') ? 1 : 0)) + arg0->unk24;
            if (gen < nsig) {
                nsig = gen;
            }
            if (nsig > 0) {
                u8 drop;
                s32 n2;

                if (nsig < gen && ptr[nsig] > '4') {
                    drop = '9';
                } else {
                    drop = '0';
                }

                for (n2 = nsig; ptr[--n2] == drop;) {
                    nsig--;
                }
                if (drop == '9') {
                    ptr[n2]++;
                }
                if (n2 < 0) {
                    --ptr, ++nsig, ++exp;
                }
            }
        }
    }
    func_10001AA8(arg0, arg1, ptr, nsig, exp);
    }
}

s16 func_100019F0(s16 *arg0, struct05 *arg1) {
    s16 temp_v1 = (arg1->unk0 & 0x7FF0) >> 4;

    if (temp_v1 == 0x7FF) {
        s32 ret;
        *arg0 = 0;
        if ((arg1->unk0 & 0xF) || (arg1->unk2) || (arg1->unk4) || (arg1->unk6)) {
            ret = 2;
        }
        else {
            ret = 1;
        }
        return ret;
    }

    if (temp_v1 > 0) {
        arg1->unk0 = (arg1->unk0 & 0x800F) | 0x3FF0;
        *arg0 = temp_v1 - 0x3FE; // 1022
        return -1;
    }

    if (temp_v1 < 0) {
      return 2;
    }

    *arg0 = 0;
    return 0;
}

s32 func_10001AA8(arg0, arg1, arg2, arg3, arg4)
struct246 *arg0;
u8 arg1;
u8 *arg2;
s16 arg3;
s16 arg4;
{
    s32 value;
    s32 total;
    s32 precision;
    s32 leading;
    s32 exponent;
    u8 *output;

    if (arg3 <= 0) {
        arg2 = D_8002BF70;
        arg3 = 1;
    }

    if (arg1 == 'f') {
        goto fixed_format;
    }
    if ((arg1 == 'g') || (arg1 == 'G')) {
        if ((arg4 >= -4) && (arg4 < arg0->unk24)) {
fixed_format:
            arg4++;
            if (arg1 != 'f') {
                precision = arg0->unk24;
                if (((arg0->unk30 & 8) == 0) && (arg3 < arg0->unk24)) {
                    arg0->unk24 = arg3;
                    precision = arg3;
                }
                arg0->unk24 = precision - arg4;
                if (arg0->unk24 < 0) {
                    arg0->unk24 = 0;
                }
            }

            if (arg4 <= 0) {
                arg0->unk8[arg0->unk14++] = '0';
                if ((arg0->unk24 > 0) || ((arg0->unk30 & 8) != 0)) {
                    arg0->unk8[arg0->unk14++] = '.';
                }
                leading = -arg4;
                if (arg0->unk24 < leading) {
                    leading = arg0->unk24;
                    arg4 = -arg0->unk24;
                }
                arg0->unk18 = leading;
                arg0->unk24 += arg4;
                if (arg0->unk24 < arg3) {
                    arg3 = arg0->unk24;
                }
                arg0->unk1C = arg3;
                memcpy(arg0->unk8 + arg0->unk14, arg2, arg3);
                arg0->unk20 = arg0->unk24 - arg3;
            } else if (arg3 < arg4) {
                memcpy(arg0->unk8 + arg0->unk14, arg2, arg3);
                arg0->unk14 += arg3;
                arg0->unk18 = arg4 - arg3;
                if ((arg0->unk24 > 0) || ((arg0->unk30 & 8) != 0)) {
                    arg0->unk8[arg0->unk14] = '.';
                    arg0->unk1C++;
                }
                arg0->unk20 = arg0->unk24;
            } else {
                memcpy(arg0->unk8 + arg0->unk14, arg2, arg4);
                arg0->unk14 += arg4;
                if ((arg0->unk24 > 0) || ((arg0->unk30 & 8) != 0)) {
                    arg0->unk8[arg0->unk14++] = '.';
                }
                arg3 -= arg4;
                if (arg0->unk24 < arg3) {
                    arg3 = arg0->unk24;
                }
                memcpy(arg0->unk8 + arg0->unk14, arg2 + arg4, arg3);
                arg0->unk14 += arg3;
                arg0->unk18 = arg0->unk24 - arg3;
            }
            goto finish;
        }
    }

scientific_format:
    if ((arg1 == 'g') || (arg1 == 'G')) {
        precision = arg0->unk24;
        if (arg3 < precision) {
            arg0->unk24 = arg3;
            precision = arg3;
        }
        arg0->unk24 = precision - 1;
        if (arg0->unk24 < 0) {
            arg0->unk24 = 0;
        }
        arg1 = (arg1 == 'g') ? 'e' : 'E';
    }

    arg0->unk8[arg0->unk14++] = *arg2++;
    if ((arg0->unk24 > 0) || ((arg0->unk30 & 8) != 0)) {
        arg0->unk8[arg0->unk14++] = '.';
    }
    if (arg0->unk24 > 0) {
        arg3--;
        if (arg0->unk24 < arg3) {
            arg3 = arg0->unk24;
        }
        memcpy(arg0->unk8 + arg0->unk14, arg2, arg3);
        arg0->unk14 += arg3;
        arg0->unk18 = arg0->unk24 - arg3;
    }

    output = arg0->unk8 + arg0->unk14;
    *output++ = arg1;
    if (arg4 >= 0) {
        *output++ = '+';
        exponent = arg4;
    } else {
        *output++ = '-';
        exponent = -arg4;
    }
    if (exponent >= 100) {
        if (exponent >= 1000) {
            *output++ = (exponent / 1000) + '0';
            exponent %= 1000;
        }
        *output++ = (exponent / 100) + '0';
        exponent %= 100;
    }
    output[0] = (exponent / 10) + '0';
    output[1] = (exponent % 10) + '0';
    output += 2;
    arg0->unk1C = (output - arg0->unk8) - arg0->unk14;

finish:
    if ((arg0->unk30 & 0x14) == 0x10) {
        value = arg0->unk28;
        total = arg0->unkC + arg0->unk14 + arg0->unk18 + arg0->unk1C +
                arg0->unk20;
        if (total < value) {
            arg0->unk10 = value - total;
        }
    }
}
