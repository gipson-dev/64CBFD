#include <ultra64.h>
typedef struct { u32 address; u32 reserved[2]; } ActorSegmentRow58F80;
extern u8 *D_800D1C90[];
extern ActorSegmentRow58F80 *D_800C5338[];
u8 *func_1507E908(u8 *, s32);
void func_1507E3C0(u8 *);
extern s32 D_800BE9E4;
extern f32 D_80096F38, D_80096F3C;
f32 cosf(f32);

extern u8 D_800CC406[];
extern s32 D_800C3E80[];
extern u8 D_800BE9C0;
extern s32 D_800C3E88;
extern s32 D_800C3E8C;
extern u16 D_800C3E7A;
extern u8 D_800C3E90;
extern u16 D_800C4ED0[];
extern u8 D_800CC33A[];
extern u8 D_80038080;
extern s32 D_800BE9F0;
extern u8 D_800D2040[];

typedef struct ActorDisplay58F80 {
    s32 active;
    u8 id;
    u8 state;
    u8 pad6[0x17E];
    u32 flags;
    u8 pad188[0x1A4];
} ActorDisplay58F80;

extern ActorDisplay58F80 D_800CC2D0[26];
extern Gfx D_80084160[], D_80084190[];
extern s32 D_8003C8E0;
s32 func_1506196C(ActorDisplay58F80 *actor, s32 view);
Gfx *func_1502C408();
Gfx *func_1502C974();
Gfx *func_150368C4(Gfx *commands, s32 slot, s32 view);
Gfx *func_15030E08(Gfx *commands, s32 view, s32 mode);

Gfx *func_1502BAD0(Gfx *commands, s32 mode, s16 view) {
    ActorDisplay58F80 *actor;
    s32 slot;
    s32 state;

    gSPDisplayList(commands++, D_80084160);
    actor = D_800CC2D0;
    for (slot = 0; slot != 25; slot++, actor++) {
        D_8003C8E0 = (slot & 0xFFFFFF) | 0x1000000;
        state = actor->active;
        if (state == 0) {
            continue;
        }
        state = actor->state;
        if (state == 3 || state == 5) {
            continue;
        }
        if (state == 2) {
            if (mode != 2) {
                continue;
            }
        } else if (actor->id == 255) {
            continue;
        }
        if (mode == 6) {
            if (state != 7) {
                continue;
            }
        } else if (mode == 0) {
            if (((actor->flags >> 9) & 1) == 0) {
                continue;
            }
        } else if (mode == 1) {
            if (state == 7 || state == 1) {
                continue;
            }
            if (state == 0 && func_1506196C(actor, view) < 255) {
                continue;
            }
        } else if (mode == 2) {
            if (state != 2) {
                if (state == 7 || (state != 0 && state != 1)) {
                    continue;
                }
                if (state == 0 && func_1506196C(actor, view) == 255) {
                    continue;
                }
            }
        }
        /* The filter callback can change the state used to select a renderer. */
        if (actor->state == 2) {
            commands = func_1502C408(commands, slot);
        } else {
            commands = func_1502C974(commands, slot, view, mode, 0);
            if (slot == 0) {
                commands = func_150368C4(commands, slot, view);
            }
        }
    }
    D_8003C8E0 = 0x1FFFFFF;
    if (mode == 1) {
        commands = func_15030E08(commands, view, 0);
    } else if (mode == 2) {
        commands = func_15030E08(commands, view, 1);
    } else if (mode == 6) {
        commands = func_15030E08(commands, view, 2);
    }
    gSPDisplayList(commands++, D_80084190);
    D_8003C8E0 = 0;
    return commands;
}

typedef struct ActorUpdate58F80 {
    s32 active;
    u8 id;
    u8 state;
    u8 pad6[0x5F];
    u8 predecessor;
    u8 pad66[0x3E];
    u8 signal;
    u8 padA5[0x53];
    u32 flags;
    u8 padFC[0x38];
    u8 eventA;
    u8 eventB;
    u8 pad136[0x93];
    u8 prepare;
    u8 pad1CA[0xA];
    s32 work;
    u8 pad1D8[0x24];
    u8 status;
    u8 pad1FD[0x63];
    u32 optional;
    u8 pad264[0x10];
    u8 maskId;
    u8 pad275[0xB7];
} ActorUpdate58F80;

extern u8 D_800C666F[];
s32 func_1502DF38();
s32 func_1502C608();
s32 func_1502FBE8();
s32 func_1502E4C4();
s32 func_1503A08C();
s32 func_150345E4();
s32 func_1503A830();
s32 func_1503DF48();
void func_1502EEF4(s32 slot);
s32 func_1502F264();
void func_1502EAFC(u8 *object);
s32 func_150A4B04();
s32 func_1517AD00();

void func_1502BD84(ActorUpdate58F80 *actor, s32 slot) {
    s32 state;

    state = actor->state;
    actor->work = 0;
    if (state == 5) {
        func_1502DF38(slot, 1);
        return;
    }
    if (actor->id == 255 || state == 3) {
        return;
    }
    if (state == 2) {
        func_1502C608(slot);
        return;
    }
    if (actor->prepare != 0) {
        func_1502FBE8(actor);
    }
    func_1502E4C4(slot);
    func_1502DF38(slot, 0);
    func_1503A08C(actor);
    if (actor->work == 0) {
        actor->status = 2;
    } else {
        func_150345E4(slot);
        func_1503A830(actor);
    }
    if (D_800C666F[slot * 16] != 0) {
        func_1503DF48(slot);
    }
    if (actor->active != 0) {
        func_1502EEF4(slot);
        func_1502F264(slot);
        if (actor->signal != 0) {
            func_1502EAFC((u8 *)actor);
        }
        if ((actor->flags & 0x4000) != 0) {
            func_150A4B04(actor);
        }
        if (actor->optional != 0) {
            func_1517AD00(actor->eventA, actor->eventB, slot);
        }
    }
}

typedef struct ActorCopy58F80 {
    u8 pad0[4];
    u8 id;
    u8 pad5[0xF3];
    u32 flags;
    u8 padFC[0xD8];
    void *source;
    void *buffer;
    u8 pad1DC[0x88];
    u32 copyState;
    u8 pad268[0xC4];
} ActorCopy58F80;

extern u32 D_800C3E74;
extern u8 D_800C3E70, D_800BEAC0;
extern ActorUpdate58F80 D_800D121C[];
void func_1503F964(void);
void func_1502F3C8(void);
void func_1502F948(ActorCopy58F80 *actor);
s32 func_15030468();
s32 func_1507C22C();

void func_1502BEE4(void) {
    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot;
    s32 maxDepth;
    s32 index;
    u8 ordered[25];
    u8 depths[25];
    s32 count;

    func_1503F964();
    D_800C3E90 = 0;
    D_800C3E74 = 0;
    maxDepth = 0;
    actor = ((ActorUpdate58F80 *)D_800CC2D0);
    do {
        if (actor->maskId != 0) {
            D_800C3E74 |= 1u << ((actor->maskId + 31) & 31);
        }
        actor++;
    } while (actor < (((ActorUpdate58F80 *)D_800CC2D0) + 25));
    bzero(depths, 25);
    slot = 0;
    actor = ((ActorUpdate58F80 *)D_800CC2D0);
    do {
        if (actor->active != 0) {
            if (actor->predecessor != 0) {
                cursor = actor;
                depths[slot] = 0;
                while (cursor->predecessor != 0) {
                    cursor = ((ActorUpdate58F80 *)D_800CC2D0) + (cursor->predecessor - 1);
                    depths[slot]++;
                }
                if (maxDepth < depths[slot]) {
                    maxDepth = depths[slot];
                }
            } else {
                func_1502BD84(actor, slot);
            }
        }
        slot++;
        actor++;
    } while (slot < 25);
    count = 0;
    if (maxDepth != 0) {
        for (slot = 1; slot <= maxDepth; slot++) {
            for (index = 0; index < 25; index++) {
                if (depths[index] == slot) {
                    ordered[count++] = index;
                }
            }
        }
        for (slot = 0; slot < count; slot++) {
            func_1502BD84(((ActorUpdate58F80 *)D_800CC2D0) + ordered[slot], ordered[slot]);
        }
    }
    func_1502F3C8();
    actor = ((ActorUpdate58F80 *)D_800CC2D0);
    do {
        if (actor->active != 0) {
            func_1502F948((ActorCopy58F80 *)actor);
        }
        actor++;
    } while (actor != D_800D121C);
    func_15030468();
    if (D_800BEAC0 == 0) {
        func_1507C22C(0);
    }
    D_800C3E70 = 0;
}

s32 func_1502C1A4() {
    return 0;
}

void func_1502C380(void) {
    D_800C3E88 = D_800C3E80[D_800BE9C0];
    D_800C3E8C = D_800C3E88;
    D_800C3E7A = 0;
}

s32 func_1502C3BC(s32 arg0) {
    s32 temp_v1 = *(D_800CC406 + arg0 * 0x32C);

    if (temp_v1 >= 0x46) {
        temp_v1 = 0xB;
    }
    return temp_v1;
}

Gfx *func_1502C408() {
    return 0;
}

s32 func_1502C608() {
    return 0;
}

s32 func_1502C6E8() {
    return 0;
}

Gfx *func_1502C974() {
    return 0;
}

s32 func_1502CC34() {
    return 0;
}

s32 func_1502CCFC() {
    return 0;
}

s32 func_1502D54C() {
    return 0;
}

s32 func_1502D630() {
    return 0;
}

s32 func_1502D824() {
    return 0;
}

s32 func_1502DB20(s32 arg0) {
    switch (arg0) {
        case 59:
        case 117:
        case 130:
        case 136:
        case 144:
        case 150:
        case 152:
        case 156:
        case 157:
        case 159:
        case 160:
        case 177:
        case 178:
        case 180:
            return D_800C4ED0[arg0] - 4;
        default:
            return D_800C4ED0[arg0];
    }
}

s32 func_1502DB84() {
    return 0;
}

s32 func_1502DF38() {
    return 0;
}

void func_1502E474(void) {
    if (D_800C3E7A != 0) {
        func_150A9984(D_800C3E80[D_800BE9C0], D_800C3E7A);
    }
    D_800C3E90 = 1;
}

s32 func_1502E4C4() {
    return 0;
}

void func_1502E9FC(s32 arg0, s32 arg1) {
}

void func_1502EA0C(u8 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    arg0[0xA4] = 4;
    arg0[0xA5] = 0;
    arg0[0xA6] = arg5;
    arg0[0xA7] = 0xFF;
    *(u32 *) (arg0 + 0xA0) = (arg4 << 24) | (arg1 << 16) | (arg2 << 8) | arg3;
}

void func_1502EA50(u8 *arg0) {
    arg0[0xA4] = 5;
}

void func_1502EA60(u8 *arg0, s32 arg1) {
    arg0[0xA4] = 2;
    arg0[0xA5] = 0xFF;
    arg0[0xA6] = arg1;
}

void func_1502EA7C(u8 *arg0, s32 arg1) {
    arg0[0xA4] = 3;
    arg0[0xA5] = 0xFF;
    arg0[0xA6] = arg1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_58F80/func_1502EA98.s")

void func_1502EAFC(u8 *object) {
    s32 delta, phase;

    switch (object[0xA4]) {
    case 2:
    case 3:
        delta = (u32)object[0xA6] * (u32)D_800BE9E4;
        phase = object[0xA5];
        if (delta < phase) {
            object[0xA5] = (u32)phase - (u32)delta;
        } else {
            object[0xA5] = 0;
        }
        break;
    case 5:
        delta = (u32)D_800BE9E4 * 10;
        phase = object[0xA7];
        if (delta < phase) {
            object[0xA7] = (u32)phase - (u32)delta;
        } else {
            object[0xA4] = 0;
        }
        /* Fall through. */
    case 4:
        object[0xA5] += (u32)object[0xA6] * (u32)D_800BE9E4;
        break;
    case 6:
        delta = (u32)object[0xA6] * (u32)D_800BE9E4;
        phase = object[0xA5];
        if (phase < (s32)(255u - (u32)delta)) {
            object[0xA5] = (u32)phase + (u32)delta;
        } else {
            object[0xA5] = 255;
        }
        object[0xA4] = 7;
        break;
    case 7:
        delta = (u32)object[0xA6] * (u32)D_800BE9E4;
        phase = object[0xA5];
        if (delta < phase) {
            object[0xA5] = (u32)phase - (u32)delta;
        } else {
            object[0xA4] = 0;
        }
        break;
    }
}

void func_1502EC34(u8 *object, s32 *red, s32 *green, s32 *blue, s32 *opacity) {
    /* Retain retail scratch extent; these reserved words are not accessed. */
    s32 reserved0, reserved1;
    s32 high, value;
    f32 amount;

    switch (object[0xA4]) {
    case 1:
        *red = object[0xA5];
        *green = object[0xA6];
        *blue = object[0xA7];
        value = *(s32 *)(object + 0xA0);
        if ((u32)value >= 256) {
            amount = *(f32 *)value;
            amount = amount < 0.0f ? 0.0f : (amount > 255.0f ? 255.0f : amount);
            *opacity = (s32)(amount * D_80096F38);
        } else {
            *opacity = value;
        }
        break;
    case 2:
    case 3:
        *red = 0;
        *green = 0;
        *blue = 0;
        value = object[0xA5];
        *opacity = value;
        if (object[0xA4] == 3) {
            *opacity = 255 - value;
        }
        break;
    case 4:
    case 5:
        value = *(s32 *)(object + 0xA0);
        high = (value >> 24) & 255;
        *red = (value >> 16) & 255;
        *green = (*(s32 *)(object + 0xA0) >> 8) & 255;
        *blue = *(s32 *)(object + 0xA0) & 255;
        amount = cosf((u32)object[0xA5] * D_80096F3C);
        value = (s32)(high + 64.0f * ((amount + 1.0f) * 0.5f));
        *opacity = value;
        *opacity = value + (((255 - value) * (255 - object[0xA7])) >> 8);
        break;
    case 6:
    case 7:
        value = *(s32 *)(object + 0xA0);
        *red = (value >> 16) & 255;
        high = (value >> 24) & 255;
        *green = (*(s32 *)(object + 0xA0) >> 8) & 255;
        *blue = *(s32 *)(object + 0xA0) & 255;
        *opacity = 255 - ((object[0xA5] * high) >> 8);
        break;
    }
}

s32 func_1502EE8C(s32 arg0, s32 arg1) {
    s32 value = D_800CC33A[arg0 * 0x32C + arg1];
    s32 result;

    if (value < 2) {
        result = value;
    } else if (value < 4) {
        result = value - 2;
    } else {
        result = 2;
    }
    return result;
}

void func_1502EEF4(s32 slot) {
    u8 *actor;
    s32 index;
    u8 state;

    actor = (u8 *)D_800CC2D0 + (u32)slot * 0x32C;
    for (index = 0; index != 2; index++, actor++) {
        if (actor[0x6C] < 10) {
            state = func_1502EE8C(slot, index);
            if (state == 0) {
                if (actor[0x6C] > 0) {
                    actor[0x6C]--;
                }
            } else if (state == 1) {
                if (actor[0x6C] < 2) {
                    actor[0x6C]++;
                }
            } else {
                actor[0x6C] = 1;
            }
        }
    }
    /* Keep the final slot lookup separate from the advanced byte cursor. */
    func_1507E3C0((u8 *)D_800CC2D0 + ((u32)slot * 0xCB << 2));
}

Gfx *func_1502F01C(Gfx *commands, s32 slot) {
    u8 *actor;
    u8 *cursor;
    u8 *pair;
    s32 index;
    u8 identity;
    u8 selected[2];
    ActorSegmentRow58F80 *rows;

    actor = (u8 *)D_800CC2D0 + (u32)slot * 0x32C;
    identity = actor[4];
    pair = NULL;
    cursor = actor;
    for (index = 0; index != 2; index++, cursor++) {
        if (cursor[0x6C] >= 10) {
            selected[index] = cursor[0x6C] - 10;
        } else {
            selected[index] = D_800D1C90[identity][((u32)index << 2) - index + cursor[0x6C] + 8];
            if (actor[0x6F] != 0 && pair == NULL) {
                pair = func_1507E908(actor, actor[0x6F]);
            }
            if (pair != NULL) {
                s32 pairValues[2];
                pairValues[0] = pair[0];
                pairValues[1] = pair[1];
                if (pair != NULL) {
                    if (pairValues[index] == (D_800D1C90[identity] + (u32)index * 4 - index)[10]) {
                        selected[index] = pairValues[index];
                    } else if (cursor[0x6C] == 0) {
                        selected[index] = pairValues[index];
                    }
                }
            }
        }
    }
    rows = D_800C5338[actor[4]];
    if (rows != NULL) {
        gSPSegment(commands++, 6, rows[selected[0]].address);
        gSPSegment(commands++, 7, rows[selected[1]].address);
        gSPSegment(commands++, 10, rows[actor[0x68]].address);
        gSPSegment(commands++, 11, rows[actor[0x69]].address);
    }
    return commands;
}

s32 func_1502F264() {
    return 0;
}

typedef struct ActorAttachment58F80 {
    s32 active;
    u8 pad4[0x10];
    f32 x, y, z;
    u8 pad20[0x160];
    f32 boundY;
    u8 pad184[0x1A];
    u16 joint;
    u8 pad1A0[0xD4];
    u8 reference;
    u8 pad275[0xB7];
} ActorAttachment58F80;

typedef struct ActorVertex58F80 {
    s16 x, y, z;
    u8 pad6[10];
} ActorVertex58F80;

typedef struct ActorRange58F80 {
    u32 start, count, matrix;
} ActorRange58F80;

extern u32 *D_800C6070[];
extern u8 *D_800D19A0[];
extern u16 D_800C5EF8[];
extern ActorRange58F80 *D_800C5C08[];
void func_150A7960(f32 *, f32, f32, f32, f32 *, f32 *, f32 *);
void func_1502F490(ActorCopy58F80 *, f32 *, f32 *, f32 *, s32);

void func_1502F3C8(void) {
    ActorAttachment58F80 *actor;

    for (actor = ((ActorAttachment58F80 *)D_800CC2D0); actor != ((ActorAttachment58F80 *)D_800D121C); actor++) {
        if (actor->active != 0 && actor->reference != 0) {
            actor->y = actor->boundY;
            func_1502F490((ActorCopy58F80 *)(((ActorAttachment58F80 *)D_800CC2D0) + actor->reference - 1),
                         &actor->x, &actor->y, &actor->z, actor->joint);
            if (actor->y < actor->boundY) {
                actor->y = actor->boundY;
            } else {
                actor->boundY = actor->y;
            }
        }
    }
}

void func_1502F490(ActorCopy58F80 *actor, f32 *x, f32 *y, f32 *z, s32 joint) {
    ActorRange58F80 *range;
    s32 i;
    f32 relative[3];
    f32 blend[3];
    u32 matrices[3];
    ActorVertex58F80 **vertex;
    u32 *matrix;
    f32 (*point)[3];
    f32 (*triangle)[3];
    u8 *base;
    ActorVertex58F80 *vertices[3];
    f32 points[6][3];
    f32 edgeA[2][3];
    f32 edgeB[2][3];
    s32 j;
    u32 mask;
    f32 weightA;
    f32 weightB;

    matrix = D_800C6070[actor->id];
    if (matrix == NULL) {
        return;
    }
    base = D_800D19A0[actor->id];
    for (i = 0; i != 3; i++) {
        vertices[i] = (ActorVertex58F80 *)(base + matrix[joint * 3 + i]);
    }
    mask = 0;
    for (i = 0; ; i++) {
        if (i == D_800C5EF8[actor->id]) {
            return;
        }
        for (j = 0; j != 3; j++) {
            if ((mask & (1u << j)) == 0) {
                range = D_800C5C08[actor->id] + i;
                if ((u32)vertices[j] >= range->start &&
                    (u32)vertices[j] < range->start + (range->count << 4)) {
                    matrices[j] = range->matrix;
                    mask |= 1u << j;
                }
            }
        }
        if (mask == 7) {
            break;
        }
    }
    base = actor->buffer;
    if (base == NULL || actor->source == NULL) {
        return;
    }
    triangle = points;
    do {
        if (triangle == points + 3) {
            base = actor->source;
        }
        vertex = vertices;
        matrix = matrices;
        point = triangle;
        do {
            func_150A7960((f32 *)(base + (*matrix << 6)),
                         (f32)(*vertex)->x, (f32)(*vertex)->y, (f32)(*vertex)->z,
                         &(*point)[0], &(*point)[1], &(*point)[2]);
            vertex++;
            matrix++;
            point++;
        } while (matrix != matrices + 3);
        triangle += 3;
    } while (triangle < points + 6);
    for (i = 0; i != 2; i++) {
        for (j = 0; j != 3; j++) {
            edgeA[i][j] = points[i * 3 + 1][j] - points[i * 3][j];
            edgeB[i][j] = points[i * 3 + 2][j] - points[i * 3][j];
        }
    }
    relative[0] = *x - points[0][0];
    relative[1] = *y - points[0][1];
    relative[2] = *z - points[0][2];
    weightB = edgeA[0][0] * edgeB[0][2] - edgeB[0][0] * edgeA[0][2];
    if (weightB == 0.0f) {
        weightA = -100.0f;
    } else {
        weightA = (relative[0] * edgeB[0][2] - edgeB[0][0] * relative[2]) / weightB;
    }
    if (weightA < 0.0f || 1.0f < weightA) {
        return;
    }
    if (edgeB[0][2] == 0.0f) {
        weightB = -100.0f;
    } else {
        weightB = (relative[2] - weightA * edgeA[0][2]) / edgeB[0][2];
    }
    if (weightB < 0.0f || 1.0f < weightB) {
        return;
    }
    for (j = 0; j != 3; j++) {
        blend[j] = edgeB[1][j] * weightB + weightA * edgeA[1][j];
    }
    relative[1] = edgeB[0][1] * weightB + weightA * edgeA[0][1];
    *x += ((blend[0] + points[3][0]) - relative[0]) - points[0][0];
    *y += ((blend[1] + points[3][1]) - relative[1]) - points[0][1];
    *z += ((blend[2] + points[3][2]) - relative[2]) - points[0][2];
}

s32 allocate_memory(s32, s32, s32, s32);

void func_1502F948(ActorCopy58F80 *actor) {
    s32 id;

    if ((actor->flags & 0x4000) != 0 && actor->copyState != 0 && actor->source != NULL) {
        id = actor->id;
        if (actor->buffer == NULL) {
            actor->buffer = (void *)allocate_memory(D_800C4ED0[id] << 6, 1, 1, 2);
            if (actor->buffer == NULL) {
                return;
            }
        }
        bcopy(actor->source, actor->buffer, D_800C4ED0[id] << 6);
    }
}

s32 func_1502F9FC() {
    return 0;
}

s32 func_1502FBE8() {
    return 0;
}

// Matched with guarded sentinel allocation and fallback scheduling.
void func_1502FD70(u8 *arg0) {
    u8 index = arg0[4];
    u8 *state;
    s32 state_value;
    u8 *object;
    s32 object_value;
    s32 sentinel;
    s32 scaled;

    if ((D_80038080 == 0) && (D_800BE9F0 == 0x1D)) {
        D_800D2040[index] = 2;
        return;
    }

    state = &D_800D2040[index];
    state_value = *state;
    sentinel = 0xFF;
    if (state_value != sentinel) {
        object = *(u8 **)(arg0 + 0x144);
        if (object == NULL) {
            scaled = 3;
        } else {
            object_value = object[0x2E];
            if (object_value == sentinel) {
                return;
            }
            if (object_value == 0) {
                scaled = 3;
            } else {
                scaled = object_value * 30;
                if (state_value < scaled) {
                    *state = scaled;
                    return;
                }
                return;
            }
        }
        *state = scaled;
    }
}
