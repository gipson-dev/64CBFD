#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/CDE80.s. */

typedef struct {
    s16 field0;
    s16 field2;
    s16 field4;
    u8 pad6[0x11];
    u8 field17;
    s32 field18;
    s32 field1C;
    s32 field20;
    u8 pad24[0x10];
} GeneratedCDE80Record;

extern GeneratedCDE80Record *D_800D3098;
extern f32 D_8009F5A0;
extern f32 D_8009F5A4;

typedef struct {
    u8 pad0[0xC];
    f32 angle0;
    f32 angle1;
    u8 pad14[0x10];
    f32 cosine0;
    f32 sine0;
    f32 cosine1;
    f32 sine1;
} GeneratedCDE80TrigRecord;

typedef struct {
    s16 origin0;
    s16 origin1;
    s16 origin2;
    u8 pad6[0x1E];
    f32 coefficient0;
    f32 scale;
    f32 coefficient1;
    f32 coefficient2;
} GeneratedCDE80Plane;

f32 func_150AD780(f32);
f32 func_150AD78C(f32);

s32 func_150A09D0() {
    return 0;
}

void func_150A0D14(GeneratedCDE80TrigRecord *record) {
    f32 angle;

    angle = record->angle0 * D_8009F5A0;
    record->cosine0 = func_150AD78C(angle);
    record->sine0 = func_150AD780(angle);

    angle = record->angle1 * D_8009F5A4;
    record->cosine1 = func_150AD78C(angle);
    record->sine1 = func_150AD780(angle);
}

s32 func_150A0D8C() {
    return 0;
}

s32 func_150A1040(register s32 arg0) {
    return arg0 + 0x400;
}

s32 func_150A104C() {
    return 0;
}

s32 func_150A11C4() {
    return 0;
}

s32 func_150A1DA0(struct127 *arg0, s32 arg1, s32 arg2) {
    return 0;
}

s32 func_150A23E4() {
    return 0;
}

s32 func_150A24C0() {
    return 0;
}

s32 func_150A25D4() {
    return 0;
}

s32 func_150A278C() {
    return 0;
}

s32 func_150A2864() {
    return 0;
}

s32 func_150A2940() {
    return 0;
}

s32 func_150A29C8() {
    return 0;
}

s32 func_150A2AEC() {
    return 0;
}

/* Original active-actor volume occupancy; OGL Note 640. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_CDE80/func_150A2CA4.s")

/* Original view-volume query; OGL Note 545. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_CDE80/func_150A2D84.s")

// Matched with guarded floating-point allocation and scheduling normalization.
s32 func_150A2E4C(GeneratedCDE80Plane *plane, f32 value0, f32 value1,
                   f32 value2) {
    volatile s16 *origin;
    f32 factor0;
    f32 factor2;
    f32 result;

    origin = &plane->origin0;
    value0 = value0 - origin[0];
    value1 = value1 - origin[1];
    value2 = value1 - origin[2];

    factor2 = plane->coefficient2;
    factor0 = plane->coefficient1;
    result = value2 * factor2 + value0 * factor0;
    factor2 = plane->scale;
    factor0 = plane->coefficient0;
    result = result * factor2 - value1 * factor0;
    if (result <= 0.0f) {
        return 1;
    }
    return 0;
}

s32 func_150A2EE4() {
    return 0;
}

s32 func_150A2FA4() {
    return 0;
}

s32 func_150A3058() {
    return 0;
}

s32 func_150A3194() {
    return 0;
}

s32 func_150A32B4(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct127 query;

    query.x_position = arg1;
    query.y_position = arg2;
    query.z_position = arg3;
    query.old_x_position = arg1;
    query.unk180 = arg2;
    query.old_y_position = arg2;
    query.old_z_position = arg3;

    if (func_150A1DA0(&query, arg0, 0) == 0) {
        return 1;
    }
    return 0;
}

void func_150A3330(s32 arg0, s32 *arg1, s32 *arg2, s32 *arg3, s32 *arg4) {
    *arg1 = D_800D3098[arg0].field17;
    *arg2 = D_800D3098[arg0].field18;
    *arg3 = D_800D3098[arg0].field1C;
    *arg4 = D_800D3098[arg0].field20;
}

s32 func_150A3398() {
    return 0;
}

void func_150A3444(s32 index, s16 arg1, s16 arg2, s16 arg3) {
    D_800D3098[index].field0 = arg1;
    D_800D3098[index].field2 = arg2;
    D_800D3098[index].field4 = arg3;
}

s32 func_150A3504();

s32 func_150A34B0(u8 *arg0) {
    if (arg0[0x14] == 1) {
        return 0;
    }
    if ((arg0[0x15] & 3) == 0) {
        return func_150A3504(arg0);
    }
    return 0;
}

s32 func_150A3504() {
    return 0;
}
