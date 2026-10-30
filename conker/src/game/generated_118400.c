#include <ultra64.h>

extern s32 D_800BE9F0;
s32 func_151420F8(s32);

/* Non-matching placeholders for the text-only asm slice asm/118400.s. */

typedef struct HeightResult71820 HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
void func_15142314(u8 *, s32, f32 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);

/* Resolve the selected actor point and optionally query its vertical interval. */
s32 func_150EAF50(f32 *position, u8 *actor, HeightResult71820 *result, u8 mode) {
    f32 start[3];
    s32 index;

    if (mode != 1 && mode != 2) {
        return 0;
    }
    if (mode == 1) {
        index = 0x21;
    } else {
        index = 0x1D;
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

s32 func_150EB030(s32 arg0, s32 arg1) {
    switch (arg0) {
        case 1:
            switch (D_800BE9F0) {
                case 4:
                    if (func_151420F8(arg1) != 0) {
                        return 6;
                    }
                    return 3;
                default:
                    return -1;
            }
        default:
            return -1;
    }
}

s32 func_150EB090() {
    return 0;
}
