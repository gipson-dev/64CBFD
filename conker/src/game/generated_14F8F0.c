#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/14F8F0.s. */

s32 func_15122440() {
    return 0;
}

#include "structs.h"
extern f32 D_800A34A0;
void func_15048F90(struct17 *, struct17 *, struct17 *);
f32 func_15048FC8(struct17 *);
f32 func_15048A70(f32, f32);
void func_150495B0(f32 *, f32, f32 *, f32, f32, f32);
void func_15123A54(void *);
void func_1512E140(void *);
void func_1512A390(void *);

/* Update the camera heading and always run its trailing state helpers. */
void func_15122980(u8 *camera) {
    struct17 first;
    struct17 second;
    f32 current;
    f32 target;
    f32 angle;
    if (*(s32 *)(camera + 0xDC) != 4) {
        func_15048F90((struct17 *)(camera + 0x2F8), (struct17 *)(camera + 0x2C8), &first);
        func_15048F90((struct17 *)(camera + 0x2F8), (struct17 *)(camera + 0x2BC), &second);
        current = func_15048FC8(&first);
        target = func_15048FC8(&second);
        if (*(s16 *)(camera + 0x298) == 0) {
            *(f32 *)(camera + 0x8D4) = 0.0f;
        } else if ((*(u32 *)(camera + 0x84) & 0x100000) ||
                   ((angle = *(f32 *)(camera + 0x390)) > 180.0f && angle < 270.0f)) {
            *(f32 *)(camera + 0x8D4) = 0.75f;
        } else {
            *(f32 *)(camera + 0x8D4) = 0.5f;
        }
        func_150495B0((f32 *)(camera + 0x8DC), *(f32 *)(camera + 0x8D4),
                      (f32 *)(camera + 0x8D8), 1.0f, 2.0f, *(f32 *)(camera + 0x7B4));
        *(f32 *)(camera + 0x37C) += func_15048A70(current, target) * *(f32 *)(camera + 0x8DC);
        *(f32 *)(camera + 0x39C) = *(f32 *)(camera + 0x37C) * D_800A34A0;
    }
    func_15123A54(camera);
    func_1512E140(camera);
    func_1512A390(camera);
}
