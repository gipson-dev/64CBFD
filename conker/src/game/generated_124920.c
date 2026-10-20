#include <ultra64.h>
#include "structs.h"
f32 func_150ADA68(void);
void *func_151541B8(struct17 *, f32, f32, f32, f32, u8, s32);
void func_151D3F14(struct17 *, u8, s32);


extern u8 D_800A1C40[][2];

/* Non-matching placeholders for the text-only asm slice asm/124920.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/game_124920/func_150F7470.s")

s32 func_150F78B4() {
    return 0;
}

s32 func_150F7E20() {
    return 0;
}

void func_150F7F58(u8 *arg0, s16 arg1) {
    func_15140410(arg0, arg0 + 0x110, arg0 + 0x11C, arg1);
}

/* Submit the randomized point effect, then the secondary point event. */
void func_150F7F8C(struct17 *point, u8 selector, s32 parameter) {
    f32 second;
    f32 first = func_150ADA68();

    second = func_150ADA68();

    func_151541B8(point, first * 3.0f + 9.0f, 0.5119050145149231f,
        second * 70.0f + 70.0f, 0.0f, selector, parameter);
    func_151D3F14(point, selector, parameter);
}

s32 func_150F802C() {
    return 0;
}

s32 func_150F81BC() {
    return 0;
}

s32 func_150F85A0() {
    return 0;
}

void func_150F884C(u8 arg0, s32 arg1) {
    s32 value[2];

    value[0] = arg1;
    func_151494E0(value, 0x3F);
}

s32 func_150F887C() {
    return 0;
}

s32 func_150F892C() {
    return 0;
}

void func_150F9720(u8 arg0) {
    s64 value;
    u8 *pair;

    pair = D_800A1C40[arg0];
    *(s32 *)&value = 0;
    ((u8 *)&value)[4] = pair[0];
    func_151494E0((s32)&value, 0x42);
    ((u8 *)&value)[4] = pair[1];
    func_151494E0((s32)&value, 0x42);
}

void func_150F9788(s32 arg0) {
}

s32 func_150F9794(s32 arg0) {
    func_150F9788(arg0);
    func_1514933C(arg0);
}

s32 func_150F97C0(s32 arg0) {
    func_150F9788(arg0);
    func_15149368(arg0);
}

s32 func_150F97EC() {
    return 0;
}

s32 func_150F9950() {
    return 0;
}
