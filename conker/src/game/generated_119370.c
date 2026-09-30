#include <ultra64.h>

void func_151C3B0C(void *arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   s32 arg5, s32 arg6, s32 arg7);

/* Non-matching placeholders for the text-only asm slice asm/119370.s. */

typedef struct {
    void *data;
    u8 type;
} Generated119370Record;

s32 func_150EBEC0() {
    return 0;
}

// Matches retail directly when the type byte is promoted to a signed word.
s32 func_150EC3D4(Generated119370Record *arg0, Generated119370Record *arg1) {
    s32 type;

    if (arg0 == arg1) {
        return 0;
    }
    if (arg0->data == NULL) {
        return 0;
    }
    type = arg0->type;
    if (type == 0xFF) {
        return 0;
    }
    if (type == 0 || type == 1 || type == 2 || type == 3 || type == 4 ||
        type == 0x28 || type == 0x77) {
        return 1;
    }
    return 0;
}

void func_150EC45C(void *arg0) {
    func_151C3B0C(arg0, 1.0f, 1.0f, 1.0f, 0.0f, 0xFF, 0xFF, 0xFF);
}
