#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1515C388();
s32 func_1515C534();
s32 func_1515C6F4();
s32 func_1515D130();
/* End generated placeholder declarations. */

void *func_15147A80(void *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, s32 arg7, u8 arg8, s32 arg9);

void *func_1515C2F0(u8 *arg0, u8 *arg1, void *arg2, s32 arg3, u8 arg4, s32 arg5) {
    u8 *temp_v0;

    *(s32 *)(arg0 + 0x10) = 0xA;
    temp_v0 = func_15147A80(arg1 + 0x40, 0x10, 8, 8, 8, 0, 0, arg3, arg4, arg5);
    if (temp_v0 == NULL) {
        return NULL;
    }
    memcpy(*(void **)(temp_v0 + 0x98), arg2, 0x3C);
    return temp_v0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_1897A0/func_1515C388.s. */
s32 func_1515C388() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1897A0/func_1515C534.s. */
s32 func_1515C534() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1897A0/func_1515C6F4.s. */
s32 func_1515C6F4() {
    return 0;
}
s32 func_1515CF9C(u8 *arg0, u8 *arg1) {
    u8 *base;
    u8 *slot;

    if ((s8)arg0[0x2C] < (arg0[0x25] - 1)) {
        base = *(u8 **)(arg0 + 0x94);
        arg0[0x2C] = (s8)arg0[0x2C] + 1;
        slot = base + ((s8)arg0[0x2E] * 0x10);
        *(s32 *)(slot + 0) = *(s32 *)(arg0 + 0x10);
        *(s32 *)(slot + 4) = *(s32 *)(arg0 + 0x14);
        *(s32 *)(slot + 8) = *(s32 *)(arg0 + 0x18);
        *(f32 *)(slot + 0xC) = *(f32 *)(arg1 + 8);
        arg0[0x2E] = (s8)arg0[0x2E] + 1;
        if (arg0[0x25] == (s8)arg0[0x2E]) {
            arg0[0x2E] = 0;
        }
    } else {
        arg1[0x39] = -1;
    }
    return 1;
}

s32 func_1515D030(u8 *arg0, s32 arg1) {
    s8 count = arg0[0x2C];

    if (count >= 3) {
        arg0[0x2C] = count - 1;
        arg0[0x2E]--;
        if ((s8)arg0[0x2E] < 0) {
            arg0[0x2E] = arg0[0x25] - 1;
        }
        return 1;
    }
    return 0;
}

void *func_1515D088(u8 *arg0) {
    struct {
        void *unk0;
        f32 unk4;
        s8 unk8;
        u8 pad[3];
    } data;
    u8 *temp_v0;
    s32 value = *(s32 *)(arg0 + 0x18);

    data.unk8 = value;
    if ((value & 0xFF) >= 2) {
        return NULL;
    }

    data.unk0 = arg0;
    data.unk4 = 0.0f;
    temp_v0 = (u8 *)func_151491F4(0x12C, -1, 0x11, 0, 0xD, 0xC, 0xFF, 1);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, &data, 0xC);
    }
    return temp_v0;
}

// fat struct
/* Non-matching C placeholders for asm/nonmatchings/game_1897A0/func_1515D130.s. */
s32 func_1515D130() {
    return 0;
}
