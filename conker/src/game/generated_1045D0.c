#include <ultra64.h>

/* Recovered emitter construction routines from asm/1045D0.s. */

typedef struct { f32 x, y, z; } Position150D7120;
typedef struct {
    s16 f00, f02, f04, f06;
    s32 f08, f0C;
    Position150D7120 position;
    f32 f1C, f20, f24, f28, f2C, f30;
    s32 f34, f38;
    f32 f3C, f40, f44, f48;
    s16 f4C, f4E, f50, f52, f54, f56;
    s8 f58;
    u8 retained59[3];
} EmitterDescriptor150D7120;
extern f32 D_800A0AE0, D_800A0AE4, D_800A0AE8;
void func_151C04F8(Position150D7120 *, u8, s32);
void func_151C05A4(Position150D7120 *, u8, s32);
void func_151C05F0(Position150D7120 *, u8, s32);
void func_1514FCE8(EmitterDescriptor150D7120 *, u8, s32);
/* Prepare a world emitter after submitting its three precursor effects. */
void func_150D7120(Position150D7120 *position, u8 slot, s32 context) {
    EmitterDescriptor150D7120 descriptor;
    func_151C04F8(position, slot, context);
    func_151C05A4(position, slot, context);
    func_151C05F0(position, slot, context);
    descriptor.f00 = 0;
    descriptor.f02 = 255;
    descriptor.f04 = -64;
    descriptor.f06 = 71;
    descriptor.f08 = 6;
    descriptor.f0C = 4;
    descriptor.position = *position;
    descriptor.f1C = 23.0f;
    descriptor.f20 = 30.0f;
    descriptor.f24 = 45.0f;
    descriptor.f28 = 53.0f;
    descriptor.f34 = 7;
    descriptor.f38 = 3;
    descriptor.f4C = 25;
    descriptor.f4E = 15;
    descriptor.f50 = 100;
    descriptor.f52 = 100;
    descriptor.f54 = 12;
    descriptor.f56 = 20;
    descriptor.f58 = 0;
    descriptor.f2C = 203.0f;
    descriptor.f30 = 414.0f;
    descriptor.f3C = 15.0f;
    descriptor.f40 = D_800A0AE0;
    descriptor.f44 = D_800A0AE4;
    descriptor.f48 = D_800A0AE8;
    func_1514FCE8(&descriptor, slot, context);
}

typedef struct { s16 values[9]; } Rotation150D728C;
typedef struct {
    s32 kind, count;
    Position150D7120 position;
    f32 f14, f18, f1C, f20, f24, f28;
    s32 f2C, f30;
    f32 f34, f38, f3C, f40;
    s16 f44, f46, f48, f4A, f4C, f4E;
    s8 f50;
    u8 retained51[3];
} EmitterBody150D728C;
typedef struct {
    Position150D7120 direction;
    f32 radius;
    EmitterBody150D728C body;
} PointEmitter150D728C;
typedef struct {
    Position150D7120 direction;
    Rotation150D728C rotation;
    f32 radius;
    EmitterBody150D728C body;
} OrientedEmitter150D728C;
void func_151BFC40(EmitterBody150D728C *, f32 *);
void func_1514FB98(PointEmitter150D728C *, u8, s32);
void func_1514FBFC(OrientedEmitter150D728C *, u8, s32);

/* Build a point or oriented emitter after the three precursor effects. */
void func_150D728C(Rotation150D728C *rotation, Position150D7120 *position,
                   Position150D7120 *direction, u8 slot, s32 context) {
    func_151C04F8(position, slot, context);
    func_151C05A4(position, slot, context);
    func_151C05F0(position, slot, context);
    if (rotation != NULL) {
        OrientedEmitter150D728C emitter;
        emitter.direction.x = -direction->x;
        emitter.direction.y = -direction->y;
        emitter.direction.z = -direction->z;
        emitter.rotation = *rotation;
        emitter.body.position = *position;
        func_151BFC40(&emitter.body, &emitter.radius);
        func_1514FBFC(&emitter, slot, context);
    } else {
        PointEmitter150D728C emitter;
        emitter.direction.x = -direction->x;
        emitter.direction.y = -direction->y;
        emitter.direction.z = -direction->z;
        func_151BFC40(&emitter.body, &emitter.radius);
        emitter.body.position = *position;
        func_1514FB98(&emitter, slot, context);
    }
}
