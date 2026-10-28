#include <ultra64.h>
#include "structs.h"
#include <string.h>

/* Non-matching placeholders for the text-only asm slice asm/209B50.s. */

s32 func_151DC6A0() {
    return 0;
}

typedef struct {
    vertex position;
    f32 accumulator;
    u8 flag;
    u8 reserved[3];
} Type91PointPayload;

s32 func_151DC6A0();
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);

/* Optionally run companion effects, then attach the point and flag to a type-0x5B effect. */
void func_151DC8BC(vertex *position, s16 lifetime, u8 companions, u8 flag, u8 group, s32 context) {
    Type91PointPayload payload;
    u8 *effect;

    if (companions) {
        func_151DC6A0(position, group, context);
    }
    payload.position = *position;
    payload.accumulator = 0.0f;
    payload.flag = flag;
    effect = func_15149130(lifetime, -1, 0x5B, -1, 1, 0, sizeof(payload), group, context);
    if (effect != NULL) {
        memcpy(effect + 0x28, &payload, sizeof(payload));
    }
}

s32 func_151DC97C() {
    return 0;
}
