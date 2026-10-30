#include <ultra64.h>

/* Partially recovered text-only slice asm/173D40.s. */

s32 func_15146BF8();

typedef struct HeightResult71820 HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
void func_15142314(u8 *, s32, f32 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);

/* Resolve the selected actor point and optionally query its vertical interval. */
s32 func_15146890(position, actor, result, mode)
f32 *position;
u8 *actor;
HeightResult71820 *result;
u8 mode;
{
    f32 start[3];
    s32 index;

    if (mode != 1 && mode != 2) {
        return 0;
    }
    if (mode == 1) {
        index = 0x13;
    } else {
        index = 0x17;
    }
    func_15142314(*(u8 **)(actor + 0x1D4), index, position);
    if (result == 0) {
        return 1;
    }
    start[0] = position[0];
    start[1] = position[1] + 10.0f;
    start[2] = position[2];
    func_1504715C(result, (HeightActor71820 *)actor);
    return func_15046C80(start, 0, position[1] - 50.0f, result);
}

s32 func_15146970() {
    return 0;
}

s32 func_15146A98() {
    return 0;
}

void func_15146BB8(register s32 arg0, register s32 arg1, register s32 arg2) {
    func_15146BF8(arg0, arg1, arg2, 0);
}

void func_15146BD8(register s32 arg0, register s32 arg1, register s32 arg2) {
    func_15146BF8(arg0, arg1, arg2, 1);
}

s32 func_15146BF8() {
    return 0;
}

s32 func_15146D60() {
    return 0;
}

s32 func_15146E84() {
    return 0;
}

s32 func_15146890();
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);

/* Submit a randomized type-22 burst at the attached object's selected point. */
void func_15147040(u8 *actor, u8 context, s32 unused) {
    f32 position[3];
    s16 count;

    if (*(void **)(actor + 0x1D4) == NULL) {
        return;
    }
    func_15146890(position, actor, (HeightResult71820 *)0, context);
    count = (u32)func_150ADA20() % 11U + 5;
    func_1514C678(position[0], position[1], position[2], func_150ADA68() * 11.0f,
        0, 255, count, 0x16, 0, 0.0f, NULL, 255);
}

s32 func_151470FC() {
    return 0;
}

s32 func_15147318() {
    return 0;
}

s32 func_15147478() {
    return 0;
}

s32 func_151475D8() {
    return 0;
}
