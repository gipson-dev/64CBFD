#include <ultra64.h>
#include "structs.h"

/* Both vectors are floats; the shared SDK still calls the first Z word s32. */
typedef struct {
    u8 retained000[0x2A4];
    struct17 origin;
    u8 retained2B0[0x48];
    struct17 target;
    u8 retained304[0x69C];
} CameraShiftC3E20;
extern CameraShiftC3E20 *D_800DBFF0;
extern s32 D_800D2E30[];
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

s32 func_1509759C(s32 arg0, s32 arg1, s32 *arg2) {
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
