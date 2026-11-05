#include <ultra64.h>

#include "structs.h"

extern struct108 *D_800DBFF0;
struct127 *func_1505EEF4(s32);
void func_15022190(s16, s16, s16, f32);
void func_150221E8(s16, s16, s16, f32);

/* Non-matching placeholders for the text-only asm slice asm/C98F0.s. */

s32 func_1509C440() {
    return 0;
}

s32 func_1509C7C8() {
    return 0;
}

/* Forward an actor's position with the selected camera heading plus 180 degrees. */
void func_1509C8FC(s32 key, s32 alternate) {
    struct127 *actor = func_1505EEF4(key & 0xFFF);
    f32 heading;

    if (actor != NULL) {
        if (D_800DBFF0->unk2C & 0x100) {
            heading = *(f32 *)((u8 *)D_800DBFF0 + 0x760);
        } else {
            heading = D_800DBFF0->unk37C;
        }
        if (alternate) {
            func_150221E8((s16)(s32)actor->x_position, (s16)(s32)actor->y_position,
                          (s16)(s32)actor->z_position, heading + 180.0f);
        } else {
            func_15022190((s16)(s32)actor->x_position, (s16)(s32)actor->y_position,
                          (s16)(s32)actor->z_position, heading + 180.0f);
        }
    }
}
