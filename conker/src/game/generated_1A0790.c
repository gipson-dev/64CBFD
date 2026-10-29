#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A0790.s. */

typedef struct {
    u8 pad[0x46];
    s8 value;
} Generated1A0790State;

extern Generated1A0790State *D_800B0DF0;

s32 func_151732E0() {
    return 0;
}

s32 func_151733D8(s32 arg0, s32 arg1) {
    return arg0;
}

s32 func_151733E4() {
    return 0;
}

extern u8 *D_800DBFF0;
extern u8 D_800DD2E4[], D_800DBEA8[];
/* Retail consumes five 32-bit arguments; the provider C body remains a placeholder. */
s32 func_151733E4();
/* Publish the selected three-byte state after updating its provider. */
void func_151738C4(s32 context) {
    u8 *state;

    if (D_800B0DF0->value == -1) {
        if (*(u32 *)(D_800DBFF0 + 0x5F0) & 1) {
            func_151733E4(6, 6, context, 0, -1);
            D_800DBEA8[0] = D_800DD2E4[0];
            D_800DBEA8[1] = D_800DD2E4[1];
            D_800DBEA8[2] = D_800DD2E4[2];
        } else {
            func_151733E4(0, 0, context, 0, -1);
            state = (u8 *)D_800B0DF0;
            D_800DBEA8[0] = state[5];
            D_800DBEA8[1] = state[6];
            D_800DBEA8[2] = state[7];
        }
    }
}

s8 func_15173994(s32 arg0) {
    return D_800B0DF0->value;
}
