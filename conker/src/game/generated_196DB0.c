#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/196DB0.s. */

void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5);

void *func_15169900(void *arg0, s32 arg1) {
    void *ret;

    ret = func_15167A68(0x5E, 0, 0x4C, 0, arg1, 1);
    if (ret != NULL) {
        bcopy(arg0, (u8 *) ret + 0x10, 0x3C);
    }

    return ret;
}

void func_15169968(register void *arg0) {
    func_15169900(arg0, 0xFF);
}

#include "structs.h"
typedef void (*RecordPhaseCallback)(void *);
extern RecordPhaseCallback D_8008CA20[];
extern s32 D_800BE9E4;
void func_1516972C(struct102 *);

/* Run the optional record callback, advance its phase once, and expire its lifetime. */
void func_15169988(u8 *record) {
    s32 selector = *(s8 *)(record + 0x40);
    u32 value;
    s32 period;
    s32 lifetime;

    if (selector != 0) {
        D_8008CA20[selector](record);
    }
    value = *(s16 *)(record + 0x26);
    value += (u32)*(s16 *)(record + 0x28) * (u32)D_800BE9E4;
    period = record[0x41] << 8;
    if ((s32)value >= period) {
        value = (s32)((u32)value - (u32)period);
    } else if ((s32)value < 0) {
        value = (s32)((u32)value + (u32)period);
    }
    lifetime = *(s16 *)(record + 0x24);
    *(s16 *)(record + 0x26) = value;
    if (lifetime != 0) {
        lifetime = (s32)((u32)lifetime - (u32)D_800BE9E4);
        if (lifetime <= 0) {
            func_1516972C((struct102 *)record);
        } else {
            *(s16 *)(record + 0x24) = lifetime;
        }
    }
}

s32 func_15169A48() {
    return 0;
}
