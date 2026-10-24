#include <ultra64.h>

/* Animated quad records and remaining functions from asm/19F150.s. */

typedef struct {
    u8 opaque0[0x10];
    Vtx vertices[4];
    s16 lifetime;
    s16 frame;
    s16 frameStep;
    u16 color;
    u8 imageIndex;
    u8 flags;
    u8 opaque5A[6];
} QuadEffect19F150;

void *func_15167A68(s32, s32, s32, s32, u8, u8);

/* Allocate an animated quad and initialize its metadata and vertex flags. */
void *func_15171CA0(s16 lifetime, u16 color, u8 imageIndex, s32 flags,
                    s32 frameStep, s32 alternate, u8 slot, s32 context) {
    QuadEffect19F150 *record;

    record = func_15167A68(alternate == 0 ? 0xF : 0x43, context,
                          sizeof(QuadEffect19F150), 1, slot, 1);
    if (record == NULL) {
        return NULL;
    }
    record->lifetime = lifetime;
    record->frame = 0;
    record->frameStep = frameStep;
    record->color = color;
    record->imageIndex = imageIndex;
    record->flags = flags;
    record->vertices[0].v.flag = 0;
    record->vertices[1].v.flag = 0;
    record->vertices[2].v.flag = 0;
    record->vertices[3].v.flag = 0;
    return record;
}

s32 func_15171D4C() {
    return 0;
}

s32 func_15171F04() {
    return 0;
}

s32 func_15171FC0() {
    return 0;
}

s32 func_151720C4() {
    return 0;
}

s32 func_151725FC() {
    return 0;
}

s32 func_15172B20() {
    return 0;
}
