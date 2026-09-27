#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/6A3D0.s. */

typedef struct {
    u8 pad0[0x30];
    u8 *data;
    u32 count;
} RecordByteBuffer;

extern u8 *D_800D19A0[];

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

s32 func_1503D484() {
    return 0;
}

s32 func_1503D510() {
    return 0;
}

s32 func_1503D5F0() {
    return 0;
}

s32 func_1503D660() {
    return 0;
}

s32 func_1503D774() {
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
