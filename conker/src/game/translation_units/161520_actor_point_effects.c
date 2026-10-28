#include <ultra64.h>
#include "structs.h"

typedef struct ActorEffectSurface {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} ActorEffectSurface;

s32 func_15134070(struct102 *);
s32 func_151380B4(struct102 *, s32, vertex *);
s32 func_15138120(struct102 *, s32, u8);
void func_1504715C(ActorEffectSurface *, struct102 *);
s32 func_151382E0(vertex *position, s32 type, ActorEffectSurface *surface, u8 group, s32 context);
s32 func_15138424(struct102 *actor, vertex *position, s32 type, ActorEffectSurface *surface, u8 group, s32 context);

/* Dispatch the selected actor effect, adding point-based effects when a point is available. */
void func_15138BC0(struct102 *actor, u8 group, s32 context) {
    s32 type;
    vertex position;
    u8 available;
    ActorEffectSurface surface;

    type = func_15134070(actor);
    if (type != 99) {
        available = func_151380B4(actor, type, &position);
        func_15138120(actor, type, 1);
        if (available) {
            func_1504715C(&surface, actor);
            func_151382E0(&position, type, &surface, group, context);
            func_15138424(actor, &position, type, &surface, group, context);
        }
    }
}
