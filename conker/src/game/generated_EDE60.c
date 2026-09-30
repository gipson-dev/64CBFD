#include <ultra64.h>

extern void func_1516972C(void *arg0);

/* Non-matching placeholders for the text-only asm slice asm/EDE60.s. */

void func_150C0A48(u8 *arg0);

void func_150C09B0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x20), (s32) (arg0 + 0x24), (s32) arg0);
}

s32 func_150C09F0(s32 arg0) {
    func_150C0A48(arg0);
    func_15169804(arg0);
}

s32 func_150C0A1C(s32 arg0) {
    func_150C0A48(arg0);
    func_15169824(arg0);
}

void func_150C0A48(u8 *arg0) {
    s16 index = *(s16 *)(arg0 + 0x44);

    while (index != -1) {
        u8 *entries = *(u8 **)(arg0 + 0x40);

        func_1516972C(*(void **)((s32)entries + index * 8));
        entries = *(u8 **)(arg0 + 0x40);
        index = *(s16 *)((s32)entries + index * 8 + 4);
    }
}

s32 func_150C0AC0() {
    return 0;
}

s32 func_150C0C38() {
    return 0;
}

s32 func_150C1198() {
    return 0;
}
