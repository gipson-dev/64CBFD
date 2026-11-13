#include <ultra64.h>

typedef struct {
    s32 active;
    u8 pad04[0x10];
    f32 x, y, z;
    u8 pad20[0x56];
    u16 unk76;
    u8 pad78[0x5A];
    s16 radius, height, y_offset;
    u8 padD8[0x4C];
    u8 indexPlusOne, immune;
    u8 pad126[0xA4];
    u8 health;
    u8 pad1CB[0x161];
} TrajectoryActor1570;
extern TrajectoryActor1570 D_800CC2D0[26];
extern u8 D_800C3E78;
void func_15047390(f32 [4][4], f32, f32, f32, f32, f32, f32, f32, f32, f32);
s32 func_15049440(f32 [4][4], f32, f32, f32, f32, f32, f32, f32, f32, f32);
s32 func_1505D1C4(f32, f32, f32, s32, s32, u16, s32, s32);
f32 sqrtf(f32);

/* Select the nearest eligible actor along the submitted segment. */
s32 func_150E1570(TrajectoryActor1570 *source, f32 x0, f32 y0, f32 z0,
                  f32 x1, f32 y1, f32 z1, s32 excluded, s32 type) {
    f32 matrix[4][4];
    f32 dx, dy, dz, length;
    s32 best, result, score, sourceIndex, index;
    TrajectoryActor1570 *actor;
    result = 0;
    score = 0;
    func_15047390(matrix, x0, y0, z0, x1, y1, z1, 0.0f, 1.0f, 0.0f);
    dx = x0 - x1;
    dy = y0 - y1;
    dz = z0 - z1;
    length = sqrtf(dx * dx + dy * dy + dz * dz);
    sourceIndex = -1;
    best = -1;
    if (source != NULL) sourceIndex = source->indexPlusOne - 1;
    for (index = 0, actor = D_800CC2D0; index < 25; ++index, ++actor) {
        if (actor->active != 0 && index != excluded && actor->health != 0 &&
            actor->immune == 0 && index != sourceIndex) {
            s32 value = func_15049440(matrix, actor->x, actor->y + (f32)actor->y_offset,
                actor->z, (f32)actor->radius, (f32)actor->height, 0.0f, length, 10.0f, 10.0f);
            if (value != 0 && (best == -1 || value < score)) {
                best = index;
                score = value;
            }
        }
    }
    if (best != -1) {
        actor = &D_800CC2D0[best];
        result = func_1505D1C4(actor->x, actor->y + (f32)actor->y_offset, actor->z,
                              type, D_800C3E78, 0, 0, 0);
        actor->unk76 = source->unk76;
    }
    return result;
}
