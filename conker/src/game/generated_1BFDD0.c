#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1BFDD0.s. */

void *func_151491F4(s16 arg0, s8 arg1, s8 arg2, u8 arg3, u8 arg4, s32 arg5, u8 arg6, s32 arg7);

typedef struct {
    void *owner;
    u8 selector;
    u8 pad5[3];
    f32 value;
} Generated1BFDD0Payload;

void func_15192920(u8 * volatile arg0) {
    u8 *record;
    Generated1BFDD0Payload payload;

    if (arg0 != NULL) {
        payload.owner = arg0;
        payload.selector = ((u8 *)payload.owner)[0x3B];
        payload.value = 0.0f;
        record = func_151491F4(0x23, -1, 0x14, 1, 0x10, 0xC, 0xFF, 1);
        if (record != NULL) {
            memcpy(record + 0x28, &payload, sizeof(payload));
        }
    }
}

s32 func_151929A4() {
    return 0;
}

s32 func_15192D48() {
    return 0;
}

s32 func_15192DF0() {
    return 0;
}

s32 func_15193234() {
    return 0;
}

s32 func_151932E0() {
    return 0;
}
