#include <ultra64.h>
typedef struct HeightResult71820 HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
struct HeightResult71820 { f32 height; s16 vertices[9]; s16 pad16; u32 metadata; u8 flags; u8 state; u16 pad1e; s32 value; };
extern f32 D_800A00C0,D_800A00C4,D_800A00C8,D_800A00CC;
extern f32 D_800A00D0,D_800A00D4,D_800A00D8;
void func_15141F78(u8,u8 *,f32,u8,f32 *,u8);
void func_15142180(u8,f32 *,s32,f32,f32);
void func_15142314(u8 *, s32, f32 *);
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);

s32 func_1509BE40(s32, ...);

/* Non-matching placeholders for the text-only asm slice asm/EBE60.s. */

/* Resolve the mode-selected actor point and optionally query its vertical interval. */
s32 func_150BE9B0(f32 *position, u8 * volatile actor,
        HeightResult71820 *result, u8 mode) {
    f32 start[3];
    register s32 index = 0x10;

    switch (mode) {
        case 4:
            index = 0x17;
            break;
        case 5:
            index = 0x14;
            break;
        case 6:
            index = 0xC;
            break;
        case 7:
            break;
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

s32 func_150BEAA8(s32 arg0, s32 arg1) {
    if ((arg0 == 0) || (arg0 == 1)) {
        return 0x11;
    }
    return -1;
}

/* Emit a point effect and its additional high-intensity effect. */
void func_150BEACC(u8 *actor, s32 mode, s32 amount) {
    f32 position[3];
    HeightResult71820 result;
    s32 selected = (u8)mode;
    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_150BE9B0(position, actor, &result, selected) != 0) {
        func_15141F78(11, (u8 *)&result, ((f32)amount * D_800A00C0) * D_800A00C4,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A00C8), position, selected);
        if (amount >= 76) {
            func_15142180(2, position, result.metadata, 3.232f, D_800A00CC);
        }
    }
}

/* Resolve the mode-selected actor point and optionally query its vertical interval. */
s32 func_150BEC30(f32 *position, u8 * volatile actor,
        HeightResult71820 *result, u8 mode) {
    f32 start[3];
    register s32 index = 0x10;

    switch (mode) {
        case 4:
            index = 0x19;
            break;
        case 5:
            index = 0x16;
            break;
        case 6:
            index = 0xC;
            break;
        case 7:
            break;
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

s32 func_150BED28(s32 arg0, s32 arg1) {
    if ((arg0 == 0) || (arg0 == 1)) {
        return 0x12;
    }
    return -1;
}

/* Emit the alternate point effect and its additional high-intensity effect. */
void func_150BED4C(u8 *actor, s32 mode, s32 amount) {
    f32 position[3];
    HeightResult71820 result;
    s32 selected = (u8)mode;
    f32 multiplier = 2.0f;
    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_150BEC30(position, actor, &result, selected) != 0) {
        func_15141F78(11, (u8 *)&result, ((f32)amount * D_800A00D0) * multiplier,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A00D4), position, selected);
        if (amount >= 76) {
            func_15142180(2, position, result.metadata, 3.232f, D_800A00D8);
        }
    }
}

/* Update actor bits 0x1010 and 0x01000000 from event queries. */
void func_150BEEB0(void *actor) {
    if ((func_1509BE40(1, 0x4063, 6, 0x2000) != 0) || (func_1509BE40(1, 0x4001, 6, 0x9000) != 0)) {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) | 0x1010);
    } else {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) & ~0x1010);
    }
    if (func_1509BE40(1, 0x4069, 6, 0x2000) != 0) {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) | 0x01000000);
        return;
    }
    (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) & 0xFEFFFFFF);
}
