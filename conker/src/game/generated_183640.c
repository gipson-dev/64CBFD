#include <ultra64.h>
#include "structs.h"
extern u8 D_800BE9C0;
extern u8 D_80089470[];
extern u8 D_800DCC10[];
extern u8 *D_800BE628;
extern u8 *D_800DC2A0[];
extern s32 D_80082FA0;
void func_100043B4(s32 *, u32);

typedef struct {
    u8 pad0[0x104];
    s32 entries[4];
    s32 trailing;
} ResourceOwner183640;


typedef struct
#ifdef __GNUC__
__attribute__((__may_alias__))
#endif
{
    u8 pad0[0x10];
    u8 flags;
    s8 first, second;
    u8 pad13[3];
    s16 remaining;
    u8 pad18[0x2B];
    u8 alpha;
    u8 pad44[0x20];
    s16 fadeStart, fadeRate;
    u8 *linked;
} ResourceCallback151572D0;
extern s32 (*D_8008AD90[])(u8 *);
extern s32 (*D_8008ADA0[])(u8 *);
void func_1503F4B0(u8 *);


void func_150A8050(f32 matrix[4][4], f32, f32, f32);
typedef struct
#ifdef __GNUC__
__attribute__((__may_alias__))
#endif
{
    u8 pad0[0x54]; f32 position[3]; u8 pad60[0x1c];
    f32 matrix[2][4][4]; u8 padfc[0x24]; f32 params[4];
} ResourceMatrixView;


extern f32 D_800BE9A8;
typedef struct { f32 x, y, z; } ResourceMotionVector;
typedef struct {
    ResourceMotionVector angle; f32 scale;
    ResourceMotionVector velocity; ResourceMotionVector angularVelocity;
    f32 accelerationY, damping; u8 flags;
} ResourceMotionParameters;
typedef struct
#ifdef __GNUC__
__attribute__((__may_alias__))
#endif
{
    u8 pad0[0x54]; ResourceMotionVector position; u8 pad60[0xC0];
    ResourceMotionParameters parameters;
} ResourceMotionView;

/* Non-matching placeholders for the text-only asm slice asm/183640.s. */

s32 func_151D5E30();
void func_15157DEC(u8 *, void *);
void func_15169260(s32, s32, s32, u8);
s32 func_15156190(s32 arg0, u8 arg1, s32 arg2, s32 arg3, s32 arg4);
extern u8 D_800A6060[];

s32 func_15156190(s32 arg0, u8 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return 0;
}

void func_15156388(s32 arg0, u8 arg1, s32 arg2) {
    func_15156190(arg0, arg1, arg2, 0xFF, 0);
}

extern s32 D_800BE9E4;
extern f32 D_800BE9A4;
void func_1516972C(struct102 *);
/* Partial view of the type 44/83 resource initialized by func_15156190. */
typedef struct
#ifdef __GNUC__
__attribute__((__may_alias__))
#endif
{
    u8 prefix[0x10];
    f32 x,y,z,dx,dy,dz;
    f32 u,v,w,du,dv,dw;
    u8 flags,pad41;
    s16 remaining;
    u8 pad44[8];
    u8 alpha,pad4D;
    s16 fadeStart,fadeRate;
} ResourceMotion183640;

/* Update wrapped lifetime, six motion components and optional alpha fade. */
void func_151563B8(struct102 *object) {
    ResourceMotion183640 *state = (ResourceMotion183640 *)object;
    s32 expired = 0;
    if (state->flags & 1) {
        /* Match SUBU and the original signed-halfword store/reload. */
        state->remaining = (s16)((u32)state->remaining - (u32)D_800BE9E4);
        if (state->remaining < 0) expired = 1;
    }
    if (!expired) {
        state->x += state->dx*D_800BE9A4;
        state->y += state->dy*D_800BE9A4;
        state->z += state->dz*D_800BE9A4;
        state->u += state->du*D_800BE9A4;
        state->v += state->dv*D_800BE9A4;
        state->w += state->dw*D_800BE9A4;
        if (state->flags & 8) {
            if (state->remaining < state->fadeStart) {
                /* Narrow before comparing; negative results wrap into the byte. */
                s16 alpha = state->remaining*state->fadeRate;
                if (alpha < state->alpha) state->alpha = (u8)alpha;
            }
        }
    }
    if (expired) func_1516972C(object);
}


s32 func_151564F8() {
    return 0;
}

s32 func_151568F8() {
    return 0;
}

s32 func_15156B54() {
    return 0;
}

s32 func_15156D24() {
    return 0;
}

void func_15156F94(u8 *arg0) {
    func_151D5E30(arg0 + 0x88, arg0);
}

s32 func_15156FB8(s32 arg0) {
    func_15156F94(arg0);
    func_15169804(arg0);
}

s32 func_15156FE4(s32 arg0) {
    func_15156F94(arg0);
    func_15169824(arg0);
}

s32 func_15157010(s32 arg0, s32 arg1, f32 arg2, s32 arg3, s32 arg4,
                   s32 arg5, u8 arg6, s32 arg7) {
    return 0;
}

void func_151571C4(ResourceOwner183640 *arg0) {
    s32 i;

    for (i = 0; i <= D_80082FA0; i++) {
        if (arg0->entries[i]) {
            func_100043B4(arg0->entries[i], 4);
        }
    }
    if (arg0->trailing != NULL) {
        func_100043B4(arg0->trailing, 4);
    }
}

void func_15157248(u8 *arg0) {
    func_151571C4(arg0);
    func_1518CA04(*(s32 *) (arg0 + 0x18));
    func_1503F7B8(*(s32 *) (arg0 + 0x68));
    func_15169804(arg0);
}

void func_1515728C(u8 *arg0) {
    func_151571C4(arg0);
    func_1518CA04(*(s32 *) (arg0 + 0x18));
    func_1503F7B8(*(s32 *) (arg0 + 0x68));
    func_15169824(arg0);
}

/* Update resource lifetime and callbacks; release expired records. */
void func_151572D0(struct102 *object) {
    ResourceCallback151572D0 *state = (ResourceCallback151572D0 *)object;
    u8 expired = 0;
    if (state->flags & 1) {
        state->remaining = (s16)((u32)state->remaining - (u32)D_800BE9E4);
        if (state->remaining < 0) expired = 1;
    }
    if (!expired) {
        if (state->first != -1) {
            if (!D_8008AD90[state->first]((u8 *)object)) expired = 1;
        }
        if (state->second != -1) {
            if (!D_8008ADA0[state->second]((u8 *)object)) expired = 1;
        }
    }
    if (!expired) func_1503F4B0(state->linked);
    if (!expired && (state->flags & 0x20)) {
        if (state->remaining < state->fadeStart) {
            s32 alpha = state->remaining * state->fadeRate;
            if (alpha < state->alpha) state->alpha = (u8)alpha;
        }
    }
    if (expired) func_1516972C(object);
}

s32 func_15157420() {
    return 0;
}

s32 func_15157860(u8 *arg0) {
    struct {
        u8 pad[0x7C];
        f32 matrices[1][4][4];
    } *ptr = (void *) arg0;

    guMtxIdentF(ptr->matrices[D_800BE9C0]);
    return 1;
}

/* Note 533: descriptor-copy allocation wrapper. */
s32 func_15157898(s32 arg0, void *arg1, s32 arg2, f32 arg3, s32 arg4,
                   s32 arg5, u8 *arg6, u8 arg7, s32 arg8) {
    s32 result;

    result = func_15157010(arg0, arg2, arg3, arg4, arg5,
                           (s32) (arg6 + 0x38), arg7, arg8);
    if (result == 0) {
        return 0;
    }
    memcpy((void *) (result + 0x120), arg1, 0x38);
    return result;
}

/* Build the selected resource matrix and apply position and scale. */
s32 func_15157918(u8 *object) {
    ResourceMatrixView *view = (void *)object;
    f32 *params = view->params;
    func_150A8050(view->matrix[D_800BE9C0], view->params[0], view->params[1], view->params[2]);
    view->matrix[D_800BE9C0][3][0] = view->position[0];
    view->matrix[D_800BE9C0][3][1] = view->position[1];
    view->matrix[D_800BE9C0][3][2] = view->position[2];
    view->matrix[D_800BE9C0][0][0] *= params[3];
    view->matrix[D_800BE9C0][0][1] *= params[3];
    view->matrix[D_800BE9C0][0][2] *= params[3];
    view->matrix[D_800BE9C0][1][0] *= params[3];
    view->matrix[D_800BE9C0][1][1] *= params[3];
    view->matrix[D_800BE9C0][1][2] *= params[3];
    view->matrix[D_800BE9C0][2][0] *= params[3];
    view->matrix[D_800BE9C0][2][1] *= params[3];
    view->matrix[D_800BE9C0][2][2] *= params[3];
    return 1;
}

/* Integrate resource motion, damping, and angular velocity. */
s32 func_15157AA8(u8 *object) {
    ResourceMotionView *view = (void *)object;
    ResourceMotionParameters *state = (void *)(object + 0x120);
    u32 ticks;
    ResourceMotionVector previous;
    f32 accelerationX, accelerationY, accelerationZ;
    if (state->flags & 1) {
        previous = state->velocity;
        if (state->flags & 8) {
            ticks = (u32)D_800BE9E4;
            while (ticks != 0) {
                state->velocity.x *= state->damping;
                state->velocity.z *= state->damping;
                ticks--;
            }
        }
        if (state->flags & 4) {
            accelerationY = state->accelerationY;
            state->velocity.y += accelerationY * D_800BE9A4;
        } else {
            accelerationY = 0.0f;
        }
        accelerationX = (state->velocity.x - previous.x) * D_800BE9A8;
        accelerationZ = (state->velocity.z - previous.z) * D_800BE9A8;
        view->position.x += (previous.x + (0.5f * accelerationX) * D_800BE9A4) * D_800BE9A4;
        view->position.y += (previous.y + (0.5f * accelerationY) * D_800BE9A4) * D_800BE9A4;
        view->position.z += (previous.z + (0.5f * accelerationZ) * D_800BE9A4) * D_800BE9A4;
    }
    if (state->flags & 2) {
        state->angle.x += state->angularVelocity.x * D_800BE9A4;
        state->angle.y += state->angularVelocity.y * D_800BE9A4;
        state->angle.z += state->angularVelocity.z * D_800BE9A4;
    }
    return 1;
}

void func_15157D88(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x4C), (s32) (arg0 + 0x50), (s32) arg0);
}

s32 func_15157DC8(u8 *arg0) {
    func_15157DEC(arg0, arg0 + 0x120);
    return 1;
}

void func_150A8050(f32 [4][4], f32, f32, f32);
/* Five scalar parameters: both a caller-local structure and embedded storage. */
typedef struct
#ifdef __GNUC__
__attribute__((__may_alias__))
#endif
{
    f32 angleX, angleY, angleZ;
    f32 scaleXZ, scaleY;
} ResourceTransform183640;

/* Partial resource view with its two 64-byte matrix pages. */
typedef struct
#ifdef __GNUC__
__attribute__((__may_alias__))
#endif
{
    u8 prefix[0x54];
    f32 x, y, z;
    u8 pad60[0x1C];
    f32 matrices[2][4][4];
} ResourceMatrix183640;

/* Rebuild the selected page; keep page and scale reloads after each store. */
void func_15157DEC(u8 *object, void *parameters) {
    ResourceMatrix183640 *state = (ResourceMatrix183640 *)object;
    ResourceTransform183640 *transform = (ResourceTransform183640 *)parameters;
    func_150A8050(state->matrices[D_800BE9C0], transform->angleX, transform->angleY, transform->angleZ);
    state->matrices[D_800BE9C0][3][0] = state->x;
    state->matrices[D_800BE9C0][3][1] = state->y;
    state->matrices[D_800BE9C0][3][2] = state->z;
    state->matrices[D_800BE9C0][0][0] *= transform->scaleXZ;
    state->matrices[D_800BE9C0][0][1] *= transform->scaleXZ;
    state->matrices[D_800BE9C0][0][2] *= transform->scaleXZ;
    state->matrices[D_800BE9C0][1][0] *= transform->scaleY;
    state->matrices[D_800BE9C0][1][1] *= transform->scaleY;
    state->matrices[D_800BE9C0][1][2] *= transform->scaleY;
    state->matrices[D_800BE9C0][2][0] *= transform->scaleXZ;
    state->matrices[D_800BE9C0][2][1] *= transform->scaleXZ;
    state->matrices[D_800BE9C0][2][2] *= transform->scaleXZ;
}


Gfx *func_15157F80(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, u8 *arg4) {
    gSPMatrix(arg0++, D_80089470, 2);
    gSPMatrix(arg0++, D_800DCC10 + arg2 * 0x40, 6);
    *arg4 = 1;
    return arg0;
}

Gfx *func_15157FE8(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3) {
    gSPMatrix(arg0++, (u32)D_800BE628 + arg2 * 0x180 + D_800BE9C0 * 0x40 + 0x100,
              G_MTX_PROJECTION | G_MTX_LOAD | G_MTX_NOPUSH);
    gSPMatrix(arg0++, D_800DC2A0[D_800BE9C0] + arg2 * 0x40,
              G_MTX_PROJECTION | G_MTX_MUL | G_MTX_NOPUSH);
    return arg0;
}

void func_15158078(s32 arg0, u8 arg1) {
    func_15169260((s32) D_800A6060, 3, arg0, arg1);
}
