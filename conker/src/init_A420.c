#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1000A420(s32 arg0, s32 arg1, s32 arg2, f32 arg3, s32 arg4,
                  s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 *arg9,
                  s32 *argA, s32 *argB);
s32 func_1000A750();
s32 func_1000B060(f32 arg0, f32 arg1, s32 arg2);
/* End generated placeholder declarations. */

void func_1000E40C(s32, s32);
s32 func_150AD960(s32, s32, s32, s32);
s32 func_150AD9A0(s32, s32, s32);

s32 func_1000A420(s32 arg0, s32 arg1, s32 arg2, f32 arg3, s32 arg4,
                  s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 *arg9,
                  s32 *argA, s32 *argB) {
    f64 angle;
    s32 attenuation;
    f32 direction;
    s32 panFlags;
    s16 pan;
    s8 rotatedPan;
    s32 distance;

    panFlags = 128;
    if ((arg7 & 0x8000) != 0) {
        arg7 &= 0x7FFF;
        distance = func_150AD960(arg4, arg6, 0, 0);
    } else {
        distance = func_150AD9A0(arg4, arg5, arg6);
    }

    attenuation = 0x7FFF - (((arg8 - distance) << 15) / (arg8 - arg7));
    if (attenuation >= 401) {
        if (arg9 != NULL) {
            if (func_150AD960(arg0, arg2, 0, 0) >= 31) {
                direction = sqrtf((f32)((arg0 * arg0) + (arg2 * arg2)));
                if (D_8002C200 < direction) {
                    direction = arg0 / direction;
                }
                angle = func_150487E0(direction) * D_8002C208;
                pan = angle;
                if (arg2 > 0) {
                    if (pan < 0) {
                        pan = -128 - pan;
                    } else {
                        pan = 128 - pan;
                    }
                }
                rotatedPan = pan + (arg3 * D_8002C210);
                if ((rotatedPan >= 96) || (rotatedPan < -96)) {
                    pan = 0;
                } else if (rotatedPan >= 32) {
                    pan = 95 - rotatedPan;
                } else if (rotatedPan < -32) {
                    pan = -95 - rotatedPan;
                } else {
                    panFlags = 0;
                    pan = rotatedPan + rotatedPan;
                }
                *arg9 = (pan + 64) | panFlags;
            } else {
                *arg9 = 64;
            }
        }

        if ((0x7FFF - (((arg8 - distance) << 15) / (arg8 - arg7))) < 0) {
            attenuation = 0;
        }
        if (attenuation >= 0x8000) {
            attenuation = 0x7FFF;
        }
        *argA = attenuation;
    } else {
        *argA = 0;
    }

    if (argB != NULL) {
        *argB = distance;
    }
    return distance;
}

/* Non-matching C placeholders for asm/nonmatchings/init_A420/func_1000A750.s. */
s32 func_1000A750() {
    return 0;
}
s32 func_1000B060(f32 arg0, f32 arg1, s32 arg2) {
    s16 phi_a1;
    f32 sp18;
    s16 temp_t8;
    f64 temp_f6;
    s8 temp_t9;
    s16 phi_v1_2;

    sp18 = sqrtf((arg0 * arg0) + (arg1 * arg1));
    if (D_8002C214 < sp18) {
        sp18 = arg0 / sp18;
    }
    phi_a1 = 128;
    temp_f6 = func_150487E0(sp18) * D_8002C218;
    phi_v1_2 = temp_f6;
    if (0.0f < arg1) {
        temp_t8 = temp_f6;
        if ((s32)temp_t8 < 0) {
            phi_v1_2 = (s16)(-128 - temp_t8);
        } else {
            phi_v1_2 = (s16)(128 - temp_t8);
        }
    }
    temp_t9 = phi_v1_2 + arg2;
    phi_v1_2 = temp_t9;
    if ((phi_v1_2 >= 96) || (phi_v1_2 < -96)) {
        phi_v1_2 = 0;
    } else if ((s32)phi_v1_2 >= 32) {
        phi_v1_2 = (s16)(0x5F - phi_v1_2);
    } else if ((s32)phi_v1_2 < -32) {
        phi_v1_2 = (s16)(-0x5F - phi_v1_2);
    } else {
        phi_v1_2 += phi_v1_2;
        phi_a1 = 0;
    }
    return (phi_v1_2 + 64) | phi_a1;
}
