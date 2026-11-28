#include <ultra64.h>

#include "structs.h"

typedef struct {
    void *descriptor;
    f32 baseRate;
    f32 rateRange;
    f32 baseScale;
    f32 scaleRange;
    f32 accumulator;
} EmitterState116D40;
typedef struct {
    struct260 header;
    u8 reserved24[4];
    EmitterState116D40 emitter;
} EmitterOwner116D40;
extern f32 D_800BE9A4;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_1514470C(void *, void *);
void func_15143794(s16, s16, f32, vertex *);
s32 func_150E9890(vertex *, vertex *, f32, u32, u32);


/* The particle provider remains unfinished; its typed interface is recovered. */

s32 func_150E9890(vertex *position, vertex *velocity, f32 scale, u32 mode, u32 identity) {
    return 0;
}

/* Accumulate the emission rate and submit each completed particle. */
void func_150E9E34(struct260 *owner) {
    EmitterState116D40 *state;
    vertex position;
    vertex velocity;
    f32 scale;
    u32 first;
    u32 second;

    state = &((EmitterOwner116D40 *)owner)->emitter;
    state->accumulator += (state->baseRate + func_150ADA68() * state->rateRange) * D_800BE9A4;
    if (state->accumulator > 1.0f) {
        do {
            scale = func_150ADA68() * state->scaleRange + state->baseScale;
            func_1514470C(state->descriptor, &position);
            first = (u32)func_150ADA20();
            second = (u32)func_150ADA20();
            func_15143794((s16)(first & 255), (s16)(64 - second % 129),
                         func_150ADA68() * 600.0f * 0.01f, &velocity);
            func_150E9890(&position, &velocity, scale, owner->pad0[12], owner->pad0[1]);
            state->accumulator -= 1.0f;
        } while (state->accumulator > 1.0f);
    }
}
