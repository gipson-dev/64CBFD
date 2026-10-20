#include <ultra64.h>
#include "structs.h"
void func_15048F90(struct17 *, struct17 *, struct17 *);
f32 func_15048FC8(struct17 *);
void func_15122980(struct108 *);
extern f32 D_800A3460;


/* Remaining non-matching placeholder for the text-only asm slice asm/14F580.s. */

/* Refresh the camera heading when descriptor mask 0x4 is clear. */
void func_151220D0(struct108 *camera) {
    struct17 direction;

    if (!(camera->unk36C[0] & 4)) {
        func_15048F90((struct17 *)&camera->unk2F8,
            (struct17 *)&camera->unk2BC, &direction);
        direction.unk0 += *(f32 *)&camera->unk2C8 - camera->unk2BC;
        direction.unk8 += *(f32 *)&camera->unk2D0 - camera->unk2C4;
        camera->unk37C = func_15048FC8(&direction);
        camera->unk39C = camera->unk37C * D_800A3460;
    }
    func_15122980(camera);
}

s32 func_15122170() {
    return 0;
}
