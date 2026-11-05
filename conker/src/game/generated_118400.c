#include <ultra64.h>

extern f32 D_800A1470, D_800A1474;
void func_15141F78(u8, u8 *, f32, u8, f32 *, u8);

extern s32 D_800BE9F0;
s32 func_151420F8(s32);

/* Actor point queries, effect classification and callback from asm/118400.s. */

typedef struct HeightResult71820 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} HeightResult71820;
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

/* Emit a point/height-interval effect using the live actor tag and requested scale. */
void func_150EB090(u8 *actor, s32 mode, s32 amount) {
    f32 position[3];
    HeightResult71820 result;

    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_150EAF50(position, actor, &result, mode) != 0) {
        func_15141F78(10, (u8 *)&result, (f32)amount * D_800A1470,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A1474), position, mode);
    }
}
