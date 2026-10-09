#include <ultra64.h>

typedef struct { s32 words[8]; } RenderRecord15147DA0;
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);

typedef struct { u32 words[3]; } ActorPosition15147EB8;
extern s32 (*D_8008A3E0[])(u8 *);
extern s32 (*D_8008A3F8[])(u8 *);
extern s32 (*D_8008A42C[])(u8 *);

typedef struct {
    f32 x, y, z, velocityY, reserved;
} MotionRecord15148AF4;
extern f32 D_800BE9A4;

typedef struct {
    u32 words[4];
    u16 phase, reserved;
} PhaseRecord15148DE0;

typedef struct {
    f32 x, y, z, velocityY;
    u16 phase, reserved;
} GrowthRecord151488C4;

typedef struct { f32 x, y, z; } RecordPosition15148BA4;
typedef struct HeightResult71820 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} HeightResult71820;
s32 func_15046C80(f32 *, u16, f32, HeightResult71820 *);
extern s32 (*D_8008A430[])(u8 *, f32, f32, f32, f32, void *);
extern s32 (*D_8008A450[])(u8 *, f32, f32, f32, f32, void *);

/* Non-matching placeholders for the text-only asm slice asm/175250.s. */

s32 func_151478F4(s32 arg0);

u8 *func_15147DA0(void *request, void *descriptor, s32 payloadBytes,
    s32 active, s32 first, s32 second, s32 third, s32 fourth, s32 fifth,
    s32 fadeFlag, s32 fadeAlpha, void *render, s32 extraBytes, u8 channel, s32 context) {
    u8 *created;
    u8 *payload;

    *(s32 *)((u8 *)request + 0x10) = 1;
    created = func_15147A80(request, (u32)payloadBytes + 0x48, 0x14, 1, 0, 1,
        fadeFlag, fadeAlpha, (void *)extraBytes, channel, context);
    if (created == NULL) {
        return NULL;
    }
    payload = *(u8 **)(created + 0x98);
    memcpy(payload, descriptor, 32);
    payload[0x20] = active;
    payload[0x21] = first;
    payload[0x22] = second;
    payload[0x23] = third;
    payload[0x24] = fourth;
    payload[0x25] = fifth;
    *(RenderRecord15147DA0 *)(payload + 0x28) = *(RenderRecord15147DA0 *)render;
    return created;
}

s32 func_15147EB8(u8 *actor) {
    u8 *payload = *(u8 **)(actor + 0x98);
    s8 failed = 0;
    s32 success;
    s32 selector;
    s32 value;
    u8 *records;

    selector = payload[0x20];
    if (selector != 0) {
        if (D_8008A3E0[selector](actor) == 0) {
            failed = 1;
        }
    }
    selector = payload[0x21];
    if (selector != 0 && !failed) {
        if (D_8008A3F8[selector](actor) == 0) {
            failed = 1;
        }
    }
    if ((payload[0x18] & 0x40) && !failed) {
        value = *(s16 *)(actor + 0x1C);
        if (value < *(s16 *)(payload + 0x1C)) {
            s32 product;
            product = (u32)value * (u32)*(s16 *)(payload + 0x1E);
            if (product < payload[0x1B]) {
                payload[0x1B] = product;
            }
        }
    }
    success = !failed;
    if (failed) {
        selector = payload[0x22];
        if (selector != 0) {
            D_8008A42C[selector](actor);
        }
    }
    records = *(u8 **)(actor + 0x94);
    if (*(s8 *)(actor + 0x2C) > 0) {
        *(ActorPosition15147EB8 *)(actor + 0x54) = *(ActorPosition15147EB8 *)(
            records + *(s8 *)(actor + 0x2D) * 20);
    } else {
        *(f32 *)(actor + 0x54) = 0.0f;
        *(f32 *)(actor + 0x58) = 0.0f;
        *(f32 *)(actor + 0x5C) = 0.0f;
    }
    return (s8)success;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_175250/func_1514803C.s")

s32 func_151488C4(u8 *actor) {
    s32 index;
    u8 *payload;
    GrowthRecord151488C4 *records;
    u16 phase;
    u16 step;
    s32 active;

    records = *(GrowthRecord151488C4 **)(actor + 0x94);
    payload = *(u8 **)(actor + 0x98);
    index = *(s8 *)(actor + 0x2D);
    while (index != *(s8 *)(actor + 0x2E)) {
        records[index].velocityY -= *(f32 *)(payload + 0x10) * D_800BE9A4;
        records[index].x += *(f32 *)(payload + 0x04) * D_800BE9A4;
        records[index].y += records[index].velocityY * D_800BE9A4;
        records[index].z += *(f32 *)(payload + 0x0C) * D_800BE9A4;
        if (++index == actor[0x25]) {
            index = 0;
        }
    }
    active = *(s8 *)(actor + 0x2C);
    if (active < actor[0x25] - 1) {
        phase = (payload[0x18] & 0x20) ? 0x1000 : 0;
        /* Retail leaves the stack step untouched when active is zero. */
        if (active != 0) {
            step = 0x1000 / active;
        }
        actor[0x2C] = active + 1;
        *(ActorPosition15147EB8 *)(records + *(s8 *)(actor + 0x2E)) = *(ActorPosition15147EB8 *)(actor + 0x10);
        records[*(s8 *)(actor + 0x2E)].velocityY = *(f32 *)(payload + 0x08);
        if (actor[0x25] == ++(*(s8 *)(actor + 0x2E))) {
            actor[0x2E] = 0;
        }
        index = *(s8 *)(actor + 0x2D);
        while (index != *(s8 *)(actor + 0x2E)) {
            records[index].phase = phase;
            if (payload[0x18] & 0x20) {
                phase -= step;
            } else {
                phase += step;
            }
            if (++index == actor[0x25]) {
                index = 0;
            }
        }
    } else {
        if (payload[0x18] & 0x17) {
            payload[0x20] = 3;
        } else {
            payload[0x20] = 2;
        }
    }
    return 1;
}

s32 func_15148AF4(u8 *actor) {
    MotionRecord15148AF4 *records = *(MotionRecord15148AF4 **)(actor + 0x94);
    u8 *payload = *(u8 **)(actor + 0x98);
    s32 index = *(s8 *)(actor + 0x2E);
    MotionRecord15148AF4 *record;

    do {
        index--;
        if (index < 0) {
            index = actor[0x25] - 1;
        }
        record = records + index;
        record->velocityY -= *(f32 *)(payload + 0x10) * D_800BE9A4;
        record->x += *(f32 *)(payload + 0x04) * D_800BE9A4;
        record->y += record->velocityY * D_800BE9A4;
        record->z += *(f32 *)(payload + 0x0C) * D_800BE9A4;
    } while (index != *(s8 *)(actor + 0x2D));
    return 1;
}

s32 func_15148BA4(u8 *actor) {
    u8 *payload = *(u8 **)(actor + 0x98);
    MotionRecord15148AF4 *records = *(MotionRecord15148AF4 **)(actor + 0x94);
    s32 index = *(s8 *)(actor + 0x2E);
    RecordPosition15148BA4 previous;
    f32 position[3];
    s32 selector;

    /* Retail's snapshot gate is narrower than the later response gate. */
    if (payload[0x18] & 7) {
        previous = *(RecordPosition15148BA4 *)(records + *(s8 *)(actor + 0x2D));
    }
    do {
        index--;
        if (index < 0) {
            index = actor[0x25] - 1;
        }
        records[index].velocityY -= *(f32 *)(payload + 0x10) * D_800BE9A4;
        records[index].x += *(f32 *)(payload + 0x04) * D_800BE9A4;
        records[index].y += records[index].velocityY * D_800BE9A4;
        records[index].z += *(f32 *)(payload + 0x0C) * D_800BE9A4;
    } while (index != *(s8 *)(actor + 0x2D));
    if (payload[0x18] & 0x17) {
        if (records[*(s8 *)(actor + 0x2D)].y < previous.y) {
            position[0] = records[*(s8 *)(actor + 0x2D)].x;
            position[1] = previous.y;
            position[2] = records[*(s8 *)(actor + 0x2D)].z;
            if (func_15046C80(position, 0, records[*(s8 *)(actor + 0x2D)].y,
                    (HeightResult71820 *)(actor + 0x60))) {
                if (actor[0x7D] == 3) {
                    selector = payload[0x24];
                    if (selector != 0) {
                        if (D_8008A450[selector](actor, previous.x, previous.y,
                                previous.z, *(f32 *)(actor + 0x60), actor + 0x64) == 0) {
                            return 0;
                        }
                    }
                } else {
                    selector = payload[0x23];
                    if (selector != 0) {
                        if (D_8008A430[selector](actor, previous.x, previous.y,
                                previous.z, *(f32 *)(actor + 0x60), actor + 0x64) == 0) {
                            return 0;
                        }
                    }
                }
            }
        }
    }
    return 1;
}

s32 func_15148DE0(u8 *actor) {
    u8 *payload;
    PhaseRecord15148DE0 *records;
    s32 index;
    u16 step;
    u16 phase;

    if (*(s8 *)(actor + 0x2C) >= 3) {
        (*(s8 *)(actor + 0x2C))--;
        records = *(PhaseRecord15148DE0 **)(actor + 0x94);
        payload = *(u8 **)(actor + 0x98);
        index = *(s8 *)(actor + 0x2D);
        step = 0x1000 / *(s8 *)(actor + 0x2C);
        phase = (payload[0x18] & 0x20) ? 0x1000 : 0;
        (*(s8 *)(actor + 0x2E))--;
        if (*(s8 *)(actor + 0x2E) < 0) {
            actor[0x2E] = actor[0x25] - 1;
        }
        while (index != *(s8 *)(actor + 0x2E)) {
            records[index].phase = phase;
            if (payload[0x18] & 0x20) {
                phase -= step;
            } else {
                phase += step;
            }
            if (++index == actor[0x25]) {
                index = 0;
            }
        }
        return 1;
    }
    return 0;
}

s32 func_15148EF8(u8 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    u8 *temp_v1 = *(u8 **) (arg0 + 0x98);

    temp_v1[0x20] = 4;
    return 1;
}

s32 func_15148F1C() {
    return 0;
}

s32 func_151490C8(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    *(temp_v0 + 0x1B) = temp_v1;
    if ((temp_v1 & 0xFF) < 0) {
        return 0;
    }
    return 1;
}

void func_15149104(s32 arg0) {
    func_151478F4(arg0);
}
