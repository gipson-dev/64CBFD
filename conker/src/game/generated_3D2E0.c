#include <ultra64.h>

extern s32 D_800B0E00,D_800B0E04,D_800902DC;
extern u8 *D_80088870;
void *func_15195AA8(s32,s32,s32,s32,s32,s32,s32,s32);
u8 *func_151491F4(s32,s32,s32,s32,s32,s32,s32,s32);
u8 *func_15149130(s32,s32,s32,s32,s32,s32,s32,s32,s32);

extern s32 D_800917B8;

/* Non-matching placeholders for the text-only asm slice asm/3D2E0.s. */

s32 func_1500FE30() {
    return 0;
}

void func_1500FF9C(void) {
    func_1510C4AC(D_800917B8, 0, 0xAD, 0x75);
}

/* Initialize callback state and create two optional records. */
void func_1500FFCC(void) {
    f32 first;
    f32 pair[3];
    u8 *record;
    func_15195AA8(D_800B0E00, D_800902DC, 1, -1, 0, 0, 0, -4);
    func_15195AA8(D_800B0E04, D_800902DC, 1, -1, 0, 1, 0, -4);
    func_1500FE30();
    func_1500FF9C();
    first = 0.0f;
    record = func_151491F4(300, -1, 18, 0, 14, 4, 255, 0);
    if (record != 0) memcpy(record + 0x28, &first, 4);
    pair[0] = 0.0f;
    pair[1] = 0.0f;
    D_80088870 = func_15149130(300, -1, 23, -1, 0, 20, 8, 255, 1);
    if (D_80088870 != 0) memcpy(D_80088870 + 0x28, pair, 8);
}
