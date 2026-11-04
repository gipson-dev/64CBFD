#include <ultra64.h>
#include <string.h>
typedef struct {
    f32 x;
    f32 y;
    f32 z;
} PayloadVector1515AA84;

typedef struct {
    u32 words[10];
} OwnerState1515AA84;

typedef struct {
    f32 zero;
    PayloadVector1515AA84 position;
    f32 scalar;
    OwnerState1515AA84 ownerState;
} ExtendedRandomPayload1515AA84;

typedef struct {
    s16 minimum;
    s16 rangeMinusOne;
} LifetimeRange1515AA84;
s32 func_150ADA20(void);
u8 *func_15149130(s16, s8, s8, s8, u8, u8, void *, u8, s32);

typedef struct {
    u8 retained00[0x48];
    f32 xPosition;
    f32 yPosition;
    f32 zPosition;
    u8 retained54[0xA4];
    f32 scaleByte;
} TranslationScaleState15158920;
typedef struct {
    f32 values[4][4];
} MatrixOnlyWorkspace15158920;
extern f32 D_800A6070;
extern MatrixOnlyWorkspace15158920 D_8008AE18;

typedef struct {
    u8 retained00[0x48];
    f32 xPosition;
    f32 yPosition;
    f32 zPosition;
    u8 retained54[0xA4];
    f32 xRotation;
    f32 yRotation;
    f32 zRotation;
    f32 uniformScale;
} UniformMatrixState1515858C;
void func_150A8050(f32 matrix[4][4], f32, f32, f32);


extern u16 D_8008B040;

extern s32 D_80082FA0;
extern f32 D_800A63A0;
extern s32 D_800BE9E4;
extern s32 (*D_8008AE00[])();
void func_1516972C(u8 *arg0);
void func_100043B4(s32 *, u32);

typedef struct {
    u8 pad0[0xE0];
    s32 entries[4];
    s32 trailing;
} ResourceOwner185560;

typedef struct {
    u8 pad0[0x14];
    s16 timer;
    u8 pad16[0x25];
    u8 value;
    u8 pad3C[0xBC];
    s16 limit;
    u8 padFA[2];
    u32 scale;
} Generated185560Record;

typedef struct {
    u8 pad0[0x40];
    s32 current;
    u8 selector;
} Generated185560Selection;

typedef struct {
    s32 first;
    s32 second;
    u8 first_selector;
    u8 second_selector;
} Generated185560SelectionPair;

/* Non-matching placeholders for the text-only asm slice asm/185560.s. */

s32 func_151580B0() {
    return 0;
}

void func_151581D8(s32 arg0, u8 arg1, s32 arg2, u8 arg3, s32 arg4) {
    func_151580B0(arg0, 0, 0, arg1, arg2, arg3, arg4);
}

void func_15158224(u8 *arg0) {
    s32 remove = 0;
    s8 callbackIndex;

    if ((arg0[0x10] & 1) != 0) {
        *(s16 *)(arg0 + 0x14) -= D_800BE9E4;
        if (*(s16 *)(arg0 + 0x14) < 0) {
            remove = 1;
        }
    }
    if (remove == 0) {
        callbackIndex = *(s8 *)(arg0 + 0x12);
        if ((callbackIndex != -1) && (D_8008AE00[callbackIndex]() == 0)) {
            remove = 1;
        }
    }
    if (remove != 0) {
        func_1516972C(arg0);
    }
}

s32 func_151582C8() {
    return 0;
}

/* Build and submit the state's translated, uniformly scaled matrix. */
s32 func_1515858C(Mtx *output, UniformMatrixState1515858C *state) {
    f32 *rotation = &state->xRotation;
    f32 matrix[4][4];

    func_150A8050(matrix, rotation[0], rotation[1], rotation[2]);
    matrix[3][0] = state->xPosition;
    matrix[3][1] = state->yPosition;
    matrix[3][2] = state->zPosition;
    matrix[0][0] *= rotation[3];
    matrix[0][1] *= rotation[3];
    matrix[0][2] *= rotation[3];
    matrix[1][0] *= rotation[3];
    matrix[1][1] *= rotation[3];
    matrix[1][2] *= rotation[3];
    matrix[2][0] *= rotation[3];
    matrix[2][1] *= rotation[3];
    matrix[2][2] *= rotation[3];
    guMtxF2L(matrix, output);
    return 1;
}

s32 func_15158684() {
    return 0;
}

/* Build and submit the state's translated, byte-scaled matrix. */
s32 func_15158920(Mtx *output, TranslationScaleState15158920 *state) {
    MatrixOnlyWorkspace15158920 workspace = D_8008AE18;
    f32 scale;

    scale = state->scaleByte * D_800A6070;
    workspace.values[3][0] = state->xPosition;
    workspace.values[3][1] = state->yPosition;
    workspace.values[3][2] = state->zPosition;

    workspace.values[0][0] *= scale;
    workspace.values[0][1] *= scale;
    workspace.values[0][2] *= scale;
    workspace.values[1][0] *= scale;
    workspace.values[1][1] *= scale;
    workspace.values[1][2] *= scale;
    workspace.values[2][0] *= scale;
    workspace.values[2][1] *= scale;
    workspace.values[2][2] *= scale;
    guMtxF2L(workspace.values, output);
    return 1;
}

void func_15158A20(ResourceOwner185560 *arg0) {
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

s32 func_15158AA4(s32 arg0) {
    func_15158A20(arg0);
    func_15169804(arg0);
}

s32 func_15158AD0(s32 arg0) {
    func_15158A20(arg0);
    func_15169824(arg0);
}

s32 func_15158AFC(u8 *arg0) {
    Generated185560Record *self = (void *) arg0;
    s32 temp_v0 = self->timer;

    if (temp_v0 < self->limit) {
        s32 temp_v1 = temp_v0 * self->scale;

        if (temp_v1 < self->value) {
            self->value = temp_v1;
        }
    }
    return 1;
}

void func_15158B3C(Generated185560Selection *selection,
                   Generated185560SelectionPair *pair, u8 operation) {
    if (operation == 0x2D) {
        if (selection->current == pair->first) {
            selection->current = pair->second;
            selection->selector = pair->second_selector;
            return;
        }
        if (selection->current == pair->second) {
            selection->current = pair->first;
            selection->selector = pair->first_selector;
        }
        return;
    }
    if (operation != 0) {
        return;
    }
    if (selection->current != pair->first) {
        if (selection->selector != ((u8 *) pair)[4]) {
            return;
        }
    }
    selection->current = 0;
    selection->selector = 0;
}

s32 func_15158BD0() {
    return 0;
}

s32 func_15158CD4(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x18));
    func_15169804(arg0);
}

s32 func_15158D00(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x18));
    func_15169824(arg0);
}

s32 func_15158D2C() {
    return 0;
}

void func_1519F400(u8 *selection);

/* Apply a matching selection event or exchange the two indexed choices. */
void func_15158FA4(u8 *selection, u8 *event, u8 opcode) {
    s32 first;
    s32 current;

    if (opcode == 0) {
        if ((*(s32 *)(selection + 0x18) == *(s32 *)(event + 0)) ||
            (selection[0x1C] == event[4])) {
            func_1516972C(selection);
        }
    } else if (opcode == 0x2D) {
        first = *(s32 *)(event + 0);
        current = *(s32 *)(selection + 0x18);
        if (first == current) {
            *(s32 *)(selection + 0x18) = *(s32 *)(event + 4);
            selection[0x1C] = event[9];
        } else {
            s32 second = *(s32 *)(event + 4);
            if (second != current) {
                return;
            }
            *(s32 *)(selection + 0x18) = first;
            selection[0x1C] = event[8];
        }
    } else if (opcode == 4) {
        if ((*(s32 *)(selection + 0x18) == *(s32 *)(event + 0)) ||
            (selection[0x1C] == event[4])) {
            func_1519F400(selection);
        }
    }
}

s32 func_15159084(u8 *arg0, u8 arg1) {
    s32 flags = *(s32 *)(arg0 + 0x184) & 0x1F;
    f32 height;
    s32 result;

    if ((arg1 == 2) || (arg1 == 3)) {
        result = 0;
    } else {
        if ((D_800A63A0 == (height = *(f32 *)(arg0 + 0x118))) &&
            ((flags & 0xA) == 0)) {
            result = 1;
        } else if ((height < *(f32 *)(arg0 + 0x18)) ||
                   (*(u8 *)(arg0 + 0x137) != 0)) {
            result = 1;
        } else {
            result = 0;
        }
    }
    return result;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_185560/func_15159120.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_185560/func_15159184.s")

s32 func_15159230(u8 *arg0, f32 *arg1, u8 arg2) {
    s32 result;

    if (arg1[0] == *(f32 *) (arg0 + 0x14)) {
        if (arg1[1] == *(f32 *) (arg0 + 0x18)) {
            result = 0;
            if (arg1[2] == *(f32 *) (arg0 + 0x1C)) {
                goto done;
            }
        }
    }
    if (arg2 != 1) {
        if (arg2 == 2) {
            goto set_two;
        }
        result = 1;
        goto done;
    }
set_two:
    result = 2;
done:
    return result;
}

/* Prioritize the two special actor types, then flag and motion states. */
s32 func_151592B8(u8 *actor, u8 mode) {
    u16 keys[1];
    u32 cursor;
    s32 actorType;
    s32 matched;
    s32 result;

    if (mode == 0) {
        keys[0] = D_8008B040;
        matched = 0;
        actorType = *(u16 *)(actor + 0x84);
        cursor = (u32)((u8 *)keys + 1);
        do {
            if (actorType == *(u8 *)cursor--) {
                matched = 1;
            }
        } while (!matched && cursor >= (u32)(u8 *)keys);
    } else {
        matched = 0;
    }
    if (matched) {
        result = 3;
    } else if (actor[0xAD] != 0) {
        result = 2;
    } else if (0.0f != *(f32 *)(actor + 0x28)) {
        result = 1;
    } else {
        result = 4;
    }
    return result;
}

extern u8 D_800BE616;

/* Apply each classification rule in order; later matching rules replace the output byte. */
s32 func_15159370(u8 *record, u8 *classification) {
    s32 matched = 0;

    if (D_800BE616 != 0) {
        *classification = 0;
        matched = 1;
    }
    if (record[0x3B] == 1) {
        *classification = 0;
        matched = 1;
    }
    if ((record[5] == 5) || (record[5] == 2)) {
        *classification = 1;
        matched = 1;
    }
    switch (record[4]) {
        case 8:
            *classification = 2;
            matched = 1;
            break;
        case 10:
            *classification = 3;
            matched = 1;
            break;
        case 0x29:
        case 0x2A:
            *classification = 4;
            matched = 1;
            break;
    }
    return matched;
}

s32 func_1515942C() {
    return 0;
}


#pragma GLOBAL_ASM("asm/nonmatchings/generated_185560/func_15159594.s")


s32 func_151596BC() {
    return 0;
}

s32 func_15159890() {
    return 0;
}

s32 func_15159BB0(f32 arg0, f32 arg1, f32 arg2, s32 arg3, s32 arg4, s32 arg5, u8 *arg6) {
    f32 position[3];
    f32 velocity[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    velocity[0] = 0.0f;
    velocity[1] = 0.0f;
    velocity[2] = 0.0f;

    return func_15159890(position, velocity, arg6[0xC], arg6[1]);
}

s32 func_15159C08() {
    return 0;
}

s32 func_1515A11C() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_185560/func_1515A238.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_185560/func_1515A60C.s")

s32 func_1515A78C() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_185560/func_1515A920.s")

s32 func_1515A974() {
    return 0;
}

/* Submit the position and retained owner state with a randomized lifetime. */
void func_1515AA84(u8 * volatile owner,
        PayloadVector1515AA84 *position, f32 scalar, s32 unused3) {
    ExtendedRandomPayload1515AA84 payload;
    u8 *ownerAfter;
    LifetimeRange1515AA84 *range;
    u32 random;
    u8 * record;
    u16 lifetime;

    payload.zero = 0.0f;
    payload.position = *position;
    payload.scalar = scalar;
    payload.ownerState = *(OwnerState1515AA84 *)(owner + 0x84);
    random = func_150ADA20();
    ownerAfter = owner;
    range = (LifetimeRange1515AA84 *)(ownerAfter + 0x80);
    lifetime = random % (range->rangeMinusOne + 1U) + range->minimum;
    record = (u8 *)func_15149130((s16)lifetime,
        -1, 0x3F, -1, 1, 0, (void *)0x3C,
        ownerAfter[0xC], ownerAfter[1]);
    if (record != NULL) {
        memcpy((u8 *)record + 0x28, &payload, sizeof(payload));
    }
}

s32 func_1515AB88() {
    return 0;
}
