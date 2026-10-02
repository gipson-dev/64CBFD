#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/6A3D0.s. */

typedef struct {
    u8 pad0[0x30];
    u8 *data;
    u32 count;
} RecordByteBuffer;

extern u8 *D_800D19A0[];
extern u8 D_80098888[];
extern u8 *D_80084410[];
extern s16 D_800C5A90[];
extern struct124 *D_800D1C90[];
extern s32 func_1502B6BC(s32 *, s32, s32, s32, s32, s32);

s32 func_1503CF20() {
    return 0;
}

s32 func_1503D368() {
    return 0;
}

void func_1503D438(u32 *arg0, u32 arg1) {
    u32 temp_v0 = *arg0;

    if ((temp_v0 != 0) && ((temp_v0 & 0x0F000000) == 0)) {
        *arg0 = temp_v0 + arg1;
    }
}

void func_1503D45C(s32 *arg0, s32 arg1) {
    while (*arg0 != 0) {
        *arg0 = *arg0 + arg1;
        arg0 = arg0 + 2;
    }
}

void func_1503D484(u8 *arg0, s32 arg1) {
    u8 *start = arg0;

    while (*(u16 *)arg0 != 999) {
        if (*(u32 *)(arg0 + 4) != 0) {
            func_1503D438((u32 *)(arg0 + 4), (u32)start);
        }
        arg0 += 8;
    }

    D_800C5A90[arg1] = (s32)(arg0 - start) >> 3;
}

s32 func_1503D510() {
    return 0;
}

s32 func_1503D5F0(s32 value) {
    s32 group;
    s32 i;

    for (group = 0; group < 5; group++) {
        for (i = 0; i < D_80098888[group]; i++) {
            if (value == D_80084410[group][i]) {
                return D_80084410[group][0];
            }
        }
    }

    return value;
}

s32 func_1503D660() {
    return 0;
}

s32 func_1503D774(s32 arg0, s32 arg1) {
    s32 output;
    struct124 **slot = &D_800D1C90[arg0];
    s32 loaded;

    if (*slot != NULL) {
        return 0;
    }

    loaded = func_1502B6BC(&output, 2, 0, 2, 0x11, arg0);
    if (loaded == 0) {
        *slot = NULL;
        return 2;
    }

    *slot = (struct124 *)loaded;
    *slot = *(struct124 **)loaded;
    return 0;
}

s32 func_1503D804() {
    return 0;
}

s32 func_1503D984() {
    return 0;
}

s32 func_1503DA3C(s32 arg0, u32 arg1) {
    u8 *entry = D_800D19A0[arg0];
    RecordByteBuffer *buffer = (RecordByteBuffer *)(entry - sizeof(RecordByteBuffer));
    u8 *data;
    s32 result;

    if (entry == NULL) {
        return 0xFF;
    }
    if (buffer->count < arg1 + 1) {
        return 0xFF;
    }
    data = buffer->data;
    result = (data != NULL) ? data[arg1] : 0xFF;
    return result;
}

s32 func_1503DA9C() {
    return 0;
}

s32 func_1503DC3C() {
    return 0;
}

s32 func_1503DD1C() {
    return 0;
}
