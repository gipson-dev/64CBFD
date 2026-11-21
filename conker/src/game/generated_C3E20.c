#include <ultra64.h>
#include "structs.h"

/* Both vectors are floats; the shared SDK still calls the first Z word s32. */
typedef struct {
    u8 retained000[0x2A4];
    struct17 origin;
    u8 retained2B0[0x48];
    struct17 target;
    u8 retained304[0x78];
    f32 value37C;
    u8 retained380[0x10];
    f32 value390;
    u8 retained394[8];
    f32 heading;
    u8 retained3A0[0x600];
} CameraShiftC3E20;
extern CameraShiftC3E20 *D_800DBFF0;
extern s32 D_800D2E30[];
typedef struct {
    s16 x, y, z;
    u8 retained06[0x12];
} CameraQueryPoint;
extern CameraQueryPoint *D_800DC020;
extern s32 D_80082FA0;
extern f32 D_8009DF4C;
struct127 *func_1505EEF4(s32);
f32 func_150AD900(struct17 *, struct17 *);
f32 sqrtf(f32);
f32 sinf(f32);
f32 cosf(f32);

void func_15048F90(struct17 *, struct17 *, struct17 *);
void func_1504917C(struct17 *, struct17 *);


/* Non-matching placeholders for the text-only asm slice asm/C3E20.s. */

extern s32 D_800D2DB4;
extern u8 D_800D2DC0[];
extern u8 D_800C35EA;

s32 func_15096A68(s32);

s32 func_15096970(void) {
    bzero(D_800D2DC0, 0x6C);
    D_800D2DB4 = 0;
}

/* Return whether any preceding 0x24-byte record has an active flag. */
s32 func_150969A0(s32 count) {
    s32 i;
    for (i = 0; i < count; i++) {
        if (D_800D2DC0[i * 0x24] != 0) {
            return 1;
        }
    }
    return 0;
}

s32 func_15096A68(s32 arg0) {
    return 0;
}

void func_15096D08(void) {
    s32 i;
    u8 *entry;

    i = 0;
    if (D_800C35EA != 1) {
        entry = D_800D2DC0;
        while (i != 3) {
            if ((*entry != 0) && (func_15096A68(i) != 0)) {
                break;
            }
            i++;
            entry += 0x24;
        }
    }
}

s32 func_15096D78() {
    return 0;
}

/* Query the active flag, two fixed-point camera values, distance or facing side. */
s32 func_1509759C(s32 view, s32 command, s32 *parameters) {
    CameraShiftC3E20 *camera = &D_800DBFF0[view];
    CameraQueryPoint *point;
    struct17 forward;
    struct17 offset;
    f32 angle;
    struct127 *actor;
    f32 x;
    f32 z;

    if (D_80082FA0 < view) {
        return 0;
    }
    switch (command) {
        case 31:
            return (s32)(camera->value390 * 65536.0f);
        case 30:
            return (s32)(camera->value37C * 65536.0f);
        case 29:
            return D_800D2DC0[parameters[2] * 0x24];
        case 32:
            point = D_800DC020;
            point = &point[parameters[2] & 0xFFF];
            x = camera->target.unk0 - point->x;
            z = camera->target.unk8 - point->z;
            return (s32)sqrtf(x * x + z * z);
        case 33:
            actor = func_1505EEF4(parameters[2] & 0xFFF);
            if (actor == 0) {
                return -1;
            }
            angle = camera->heading + D_8009DF4C;
            forward.unk0 = sinf(angle);
            forward.unk4 = 0.0f;
            forward.unk8 = cosf(angle);
            func_15048F90(&camera->target, (struct17 *)&actor->x_position, &offset);
            offset.unk4 = 0.0f;
            return 0.0f <= func_150AD900(&forward, &offset) ? -1 : 1;
        default: goto no_value;
    }
no_value:
    return 0;
}

/* Move both camera points opposite their normalized separation. */
void func_15097798(s32 view) {
    CameraShiftC3E20 *camera = &D_800DBFF0[view];
    struct17 direction;

    if (D_800D2DB4 != 0) {
        func_15048F90(&camera->origin, &camera->target, &direction);
        func_1504917C(&direction, &direction);
        camera->origin.unk0 += direction.unk0 * -2.5f * D_800D2E30[view];
        camera->origin.unk4 += direction.unk4 * -2.0f * D_800D2E30[view];
        camera->origin.unk8 += direction.unk8 * -2.5f * D_800D2E30[view];
        camera->target.unk0 += direction.unk0 * -2.5f * D_800D2E30[view];
        camera->target.unk4 += direction.unk4 * -2.0f * D_800D2E30[view];
        camera->target.unk8 += direction.unk8 * -2.5f * D_800D2E30[view];
    }
}
