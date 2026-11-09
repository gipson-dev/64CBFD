#include <ultra64.h>
#include "structs.h"
#include <math.h>
extern struct127 D_800CC2D0[26];
extern f32 D_800A3730;
/* Read the first signed halfword of the unresolved actor word field. */
typedef s16
#ifdef __GNUC__
__attribute__((__may_alias__))
#endif
ActorHeadingHalfword15B960;

/* Position the secondary camera from its selected actor and adjusted heading. */
void func_1512E4B0(struct108 *camera) {
    s32 slot;
    s32 heading;
    f32 offset;
    f32 angle;
    struct127 *actor;
    slot = 0;
    if (camera->unk23D == 3) slot = 1;
    actor = &D_800CC2D0[slot];
    camera->unk2BC = actor->x_position;
    camera->unk2C0 = actor->y_position + 150.0f;
    camera->unk2C4 = actor->z_position;
    heading = (s16)-*(ActorHeadingHalfword15B960 *)((u8 *)actor + 0x2E4);
    /* Truncate to a full word before the original signed-halfword wrap. */
    heading += actor->unk40*10.0f;
    heading = (s16)heading;
    angle = ((f32)heading*D_800A3730)/1800.0f;
    offset = sinf(angle)*60.0f;
    camera->unk2F8 = camera->unk2BC - offset;
    camera->unk2FC = camera->unk2C0;
    offset = cosf(angle)*60.0f;
    camera->unk300 = camera->unk2C4 - offset;
}
