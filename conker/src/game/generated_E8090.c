#include <ultra64.h>

typedef struct {
    u8 pad0[0x1C];
    s16 timer;
    u8 pad1E[0xA];
    u8 value;
    u8 pad29[0x87];
    s16 limit;
    s16 scale;
} GeneratedE8090Record;

/* Non-matching placeholders for the text-only asm slice asm/E8090.s. */

s32 func_150BABE0() {
    return 0;
}

s32 func_150BAFEC() {
    return 0;
}

s32 func_150BB260() {
    return 0;
}

void func_150BB408(u8 *arg0) {
    *(u32 *) (arg0 + 0x18) |= 1;
    *(s16 *) (arg0 + 0x1C) = 0x32;
    *(s16 *) (arg0 + 0xB0) = *(s16 *) (arg0 + 0x1C);
    *(s16 *) (arg0 + 0xB2) = 5;
    func_1513F6C0(arg0, 6, *(arg0 + 0x81));
}

s32 func_150BB450(u8 *arg0) {
    GeneratedE8090Record *self = (void *) arg0;
    s32 temp_v0 = self->timer;

    if (temp_v0 < self->limit) {
        s32 temp_v1 = (s16) (temp_v0 * (u32) self->scale);

        if (temp_v1 < self->value) {
            self->value = temp_v1;
        }
    }
    return 1;
}

s32 func_150BB498() {
    return 0;
}
