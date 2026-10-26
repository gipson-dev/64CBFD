#include <ultra64.h>

extern f32 D_800986EC;
extern f32 D_800C3FD0[];

/* Typed call views retain the recovered ABI while provider bodies remain placeholders. */
typedef s32 (*SentinelPrimaryQuery)(s32, f32 *);
typedef s32 (*SentinelFallbackQuery)(f32 *, s32, s32, s32, f32, s32, f32 *, s32, s32, s32, s32);

extern u8 D_800C3FFA;
extern u8 D_800C3E78;
extern u8 D_800CC2D0[];

/* Non-matching placeholders for the text-only asm slice asm/64120.s. */

extern u8 D_80098068[];
extern f32 D_80098250;

void func_15036C70(u8 *arg0) {
    s32 offset;
    f32 value;

    *(void **) (arg0 + 0x324) = allocate_memory(0x48, 1, 0, 0);
    bzero(*(void **) (arg0 + 0x324), 0x48);
    value = D_80098250;
    for (offset = 0; offset < 0xC; offset += 4) {
        *(f32 *) (*(u8 **) (arg0 + 0x324) + offset) = value;
        *(f32 *) (*(u8 **) (arg0 + 0x324) + offset + 0xC) = value;
    }
}

s32 func_15036CE8() {
    return 0;
}

s32 func_15036F34() {
    return 0;
}

s32 func_15037698() {
    return 0;
}

s32 func_15037880() {
    return 0;
}

s32 func_150379DC() {
    return 0;
}

s32 func_150380C0() {
    return 0;
}

s32 func_15038468() {
    return 0;
}

s32 func_15038620() {
    return 0;
}

u8 *func_15039A54(s32 arg0, s32 arg1) {
    return D_80098068 + (arg1 * 0x18);
}

s32 func_15039A78() {
    return 0;
}

s32 func_15039CC8() {
    return 0;
}

s32 func_15039ED0() {
    return 0;
}

s32 func_1503A08C() {
    return 0;
}

void func_1503A60C(void) {
    u8 *destination = *(u8 **) (D_800CC2D0 + (D_800C3E78 * 0x32C) + 0x1D4) + 0x40;

    *(f32 *) (destination + 0x30) =
        *(f32 *) (D_800CC2D0 + (D_800C3E78 * 0x32C) + 0x174);
    *(f32 *) (destination + 0x34) =
        *(f32 *) (D_800CC2D0 + (D_800C3E78 * 0x32C) + 0x18);
    *(f32 *) (destination + 0x38) =
        *(f32 *) (D_800CC2D0 + (D_800C3E78 * 0x32C) + 0x178);
}

s32 func_1503A678() {
    return 0;
}

void func_1503A7F0(void) {
    s32 saved = D_800C3FFA;

    D_800C3FFA = 0;
    func_15036F34();
    D_800C3FFA = saved;
    func_1503A678();
}

s32 func_1503A830() {
    return 0;
}

/* Initialize both sentinels and use the fallback only if the primary query declines. */
void func_1503B708(f32 *output, s32 arg1, s32 arg2, s32 playerIndex, f32 arg4, s32 arg5, f32 *distance, s32 arg7, s32 arg8, s32 arg9, s32 arg10) {
    f32 sentinel = D_800986EC;

    output[0] = sentinel;
    output[1] = sentinel;
    output[2] = sentinel;
    D_800C3FD0[0] = sentinel;
    D_800C3FD0[1] = sentinel;
    D_800C3FD0[2] = sentinel;
    if (((SentinelPrimaryQuery) func_15037880)(playerIndex, output) == 0) {
        ((SentinelFallbackQuery) func_150380C0)(output, arg1, arg2, playerIndex, arg4, arg5, distance, arg7, arg8, arg9, arg10);
    }
}
