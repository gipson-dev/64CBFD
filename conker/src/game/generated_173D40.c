#include <ultra64.h>
typedef struct { f32 x, y, z; } EffectPoint173D40;
typedef struct {
    s32 countBase;
    s32 countRange;
    EffectPoint173D40 position;
    f32 field14;
    f32 field18;
    s16 minimum1C;
    s16 range1E;
    s16 minimum20;
    s16 range22;
    f32 field24;
    f32 field28;
    f32 field2C;
    f32 field30;
    f32 field34;
    f32 field38;
    u8 mode;
    u8 reserved3D;
    s16 value3E;
    s16 value40;
    u8 reserved42[2];
} PointEffectDescriptor173D40;
extern f32 D_800A5708, D_800A570C, D_800A5710, D_800A5714, D_800A5718, D_800A571C;
void func_15150F90(PointEffectDescriptor173D40 *, u8, u8, s32);


extern f32 D_800A5728, D_800A572C;
extern f32 D_800A5720, D_800A5724;
void func_15141F78(u8, u8 *, f32, u8, f32 *, u8);
extern f32 D_800A573C,D_800A5740,D_800A5744,D_800A5748,D_800A574C,D_800A5750;
extern s32 (*D_8008FD04)(void);
extern s32 (*D_8008FD1C)(void);
extern s32 (*D_8008FD30)(void);
void func_15142180(u8, f32 *, s32, f32, f32);

/* Partially recovered text-only slice asm/173D40.s. */

void func_15146BF8();

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

/* Select the actor effect, consulting state or the five-ID list when needed. */
s32 func_15146970(s32 kind, u8 *actor) {
    extern s32 D_800BE9F0;
    extern u8 D_800CC2D0[];
    extern s32 func_151420F8(u8 *);
    extern s32 func_150A2AEC(s32, s32, s32 *);
    switch (kind) {
        case 8: return 16;
        case 7: return 15;
        case 5: return 5;
        case 2: return 2;
        case 0: return 0;
        case 1:
            if (D_800BE9F0 == 4) {
                if (func_151420F8(actor)) {
                    return 6;
                } else {
                    return 3;
                }
            } else {
                return 1;
            }
        case 4: return 4;
        case 3: return 3;
        case 6: {
            s32 choices[5] = {0x401D, 0x401E, 0x401F, 0x4020, 0x4021};
            if (func_150A2AEC((s32)((u32)actor - (u32)D_800CC2D0) / 0x32C,
                              5, choices) == -1) {
                return -1;
            } else {
                return 6;
            }
        }
    }
    return -1;
}

/* Submit the point effect using the attached actor's selected position. */
void func_15146A98(u8 *actor, s32 context, s32 unused) {
    EffectPoint173D40 position;
    PointEffectDescriptor173D40 descriptor;

    if (*(u32 *)(actor + 0x1D4) == 0) return;
    func_15146890(&position.x, actor, (HeightResult71820 *)0, (u8)context);
    descriptor.countBase = 5;
    descriptor.countRange = 22;
    descriptor.position = position;
    descriptor.field14 = D_800A5708;
    descriptor.field18 = D_800A570C;
    descriptor.minimum1C = 0;
    descriptor.range1E = 255;
    descriptor.minimum20 = -20;
    descriptor.range22 = 14;
    descriptor.field24 = 6.0f;
    descriptor.field28 = 3.0f;
    descriptor.field2C = D_800A5710;
    descriptor.field30 = D_800A5714;
    descriptor.field34 = D_800A5718;
    descriptor.field38 = D_800A571C;
    descriptor.mode = 3;
    descriptor.value3E = 25;
    descriptor.value40 = 25;
    func_15150F90(&descriptor, 0, 255, 1);
}

void func_15146BB8(register s32 arg0, register s32 arg1, register s32 arg2) {
    func_15146BF8(arg0, arg1, arg2, 0);
}

void func_15146BD8(register s32 arg0, register s32 arg1, register s32 arg2) {
    func_15146BF8(arg0, arg1, arg2, 1);
}

/* Emit the flagged point effect and its additional high-intensity effect. */
void func_15146BF8(u8 *actor, s32 mode, s32 amount, s32 flag) {
    f32 position[3];
    HeightResult71820 result;
    s32 selected = (u8)mode;
    s32 slot;
    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_15146890(position, actor, &result, selected) != 0) {
        if ((u8)flag) slot = 12; else slot = 11;
        func_15141F78((u8)slot, (u8 *)&result, (f32)amount * D_800A5720,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A5724), position, selected);
        if (amount >= 115) func_15142180(2, position, result.metadata, 1.0f, 1.0f);
    }
}

/* Emit a point/height-interval effect using the live actor tag and requested scale. */
void func_15146D60(u8 *actor, s32 mode, s32 amount) {
    f32 position[3];
    HeightResult71820 result;
    s32 selected = (u8)mode;

    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_15146890(position, actor, &result, selected) != 0) {
        func_15141F78(10, (u8 *)&result, (f32)amount * D_800A5728,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A572C), position, selected);
    }
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

/* Submit the optional point effect before choosing the main effect. */
void func_15147318(u8 *actor, s32 mode, s32 amount) {
    f32 position[3];
    HeightResult71820 result;
    s32 selected = (u8)mode;
    s32 slot;
    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_15146890(position, actor, &result, selected) != 0) {
        if (amount >= 115) func_15142180(0, position, result.metadata, 1.0f, 1.0f);
        slot = D_8008FD04();
        func_15141F78((u8)slot, (u8 *)&result, (f32)amount * D_800A573C,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A5740), position, selected);

    }
}

/* Submit the optional slot-6 point effect after the main effect. */
void func_15147478(u8 *actor, s32 mode, s32 amount) {
    f32 position[3];
    HeightResult71820 result;
    s32 selected = (u8)mode;
    s32 slot;
    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_15146890(position, actor, &result, selected) != 0) {

        slot = D_8008FD1C();
        func_15141F78((u8)slot, (u8 *)&result, (f32)amount * D_800A5744,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A5748), position, selected);
        if (amount >= 115) func_15142180(6, position, result.metadata, 1.0f, 1.0f);
    }
}

/* Submit the optional slot-11 point effect after the main effect. */
void func_151475D8(u8 *actor, s32 mode, s32 amount) {
    f32 position[3];
    HeightResult71820 result;
    s32 selected = (u8)mode;
    s32 slot;
    if (*(s32 *)(actor + 0x1D4) == 0) return;
    if (func_15146890(position, actor, &result, selected) != 0) {

        slot = D_8008FD30();
        func_15141F78((u8)slot, (u8 *)&result, (f32)amount * D_800A574C,
                      (u8)(u32)(*(f32 *)(actor + 0x40) * D_800A5750), position, selected);
        if (amount >= 115) func_15142180(11, position, result.metadata, 1.0f, 1.0f);
    }
}
