#include <ultra64.h>

typedef struct GroundResult150CDBB0 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} GroundResult150CDBB0;

extern f32 D_800A07B0;
void func_1504715C(GroundResult150CDBB0 *, void *);
s32 func_15046C80(f32 *, u16, f32, GroundResult150CDBB0 *);
u32 func_150ADA20(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);

/* Query the ground height and submit two randomized effects on success. */
void func_150CDBB0(u8 *actor, u8 flags, s32 unused) {
    f32 point[3];
    GroundResult150CDBB0 result;
    u32 random;

    if (actor != NULL) {
        func_1504715C(&result, actor);
        point[0] = *(f32 *)(actor + 0x14);
        point[1] = *(f32 *)(actor + 0x18) + 1000.0f;
        point[2] = *(f32 *)(actor + 0x1C);
        if (func_15046C80(point, 0, *(f32 *)(actor + 0x18) - D_800A07B0, &result)) {
            point[1] = result.height;
            random = func_150ADA20();
            func_1514C678(point[0], point[1], point[2], 251.0f, 0, 255,
                          (random & 15U) + 35, 0x17, 0, 0.0f, NULL, flags);
            random = func_150ADA20();
            func_1514C678(point[0], point[1], point[2], 290.0f, 0, 255,
                          (random % 21U) + 30, 0x18, 0, 0.0f, NULL, flags);
        }
    }
}

/* Non-matching placeholders for the remaining asm slice. */
s32 func_150CDCF4() {
    return 0;
}

s32 func_150CDF10() {
    return 0;
}
