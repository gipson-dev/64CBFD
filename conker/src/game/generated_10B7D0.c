#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/10B7D0.s. */

extern u8 D_800A0D0B[];
extern u8 D_800A0D2B[];
extern s32 D_80082FA0;

typedef struct {
    u8 pad0[0x388];
    f32 threshold;
    u8 pad38C[0x614];
} Generated10B7D0PlayerRecord;

extern Generated10B7D0PlayerRecord *D_800DBFF0;

s32 func_150DEC28();
s32 func_15140410();

void func_150DE320(s32 arg0) {
}

s32 func_150DE32C() {
    return 0;
}

s32 func_150DE458() {
    return 0;
}

s32 func_150DE6D8() {
    return 0;
}

s32 func_150DE7C0() {
    return 0;
}

s32 func_150DEACC() {
    return 0;
}

/* Note 529: current-player threshold gate and embedded-record dispatch. */
s32 func_150DEB58(u8 *arg0, s16 arg1) {
    if (D_800DBFF0[D_80082FA0].threshold < 5.0f) {
        return 0;
    }
    return func_15140410(arg0, arg0 + 0x120, arg0 + 0x12C, arg1);
}

void func_150DEBE0(s32 arg0) {
    s32 i = 0;

    do {
        func_150DEC28(i & 0xFF, 1);
        i += 1;
        i = i & 0xFF;
    } while (i < 4);
}

s32 func_150DEC28(arg0, arg1)
u8 arg0;
u8 arg1;
{
    s32 offset = arg0 * 4;

    func_151616D0(D_800A0D0B[offset], 0x22, 0);
    func_151417C4(D_800A0D2B[offset], 0x22);
}
