#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_151670C0(void);
void func_151671E8(void);
void func_15167310(void);
extern f32 D_800DD1D0[2];
Gfx *func_151674F8(Gfx *output, s32 selector, s16 view, s32 row);
void func_15167B44(u8 *state);
Gfx *func_15167C58();
/* Measured compact sprite view; opaque regions retain unidentified contents. */
typedef struct {
    u8 unidentified00[0x10];
    u8 *texture;
    u32 renderSettings; /* The wrapper also reads this slot as a visibility-owner pointer. */
    s32 orientation;
    s16 phase, speed;
    s16 x, y, z;
    s16 velocityX, velocityZ;
    u8 unidentified2A[2];
    u8 fractionX, fractionZ, fractionY;
    s8 callbackIndex;
    s16 velocityY, accelerationY;
    s16 width, height;
    s16 remaining;
    s8 fadeStep;
    u8 unidentified3B;
    u8 red, green, blue;
    u8 alpha;
    u8 environmentRed, environmentGreen, environmentBlue;
    u8 unidentified43;
    u16 flags;
    u8 unidentified46[2];
    s8 completionIndex;
    u8 unidentified49[3];
} CompactSpriteState;

void func_15167E0C(CompactSpriteState *state);
Gfx *func_15168118(Gfx *output, void *record, s16 view);
typedef struct {
    Vtx vertices[8];
    u32 value80;
    u32 retained84;
    s16 cleared88;
    u16 value8A;
    s16 x, y, z;
    s16 lifetime, remaining;
    s16 initialHeight;
    u16 flags;
    u16 retained9A;
    s16 cleared9C, cleared9E;
    u8 textureIndex, mode;
    s8 tag;
    u8 retainedA3;
    u32 retainedA4;
} SelectedVertexSprite;
extern u8 *D_8008CA4C[];
void func_1516865C(void *, u8, u8, u8, u8);
/* Measured 0xB8-byte sprite-record view; opaque regions are not recovered fields. */
typedef struct {
    u8 unidentified00[0x98];
    s16 phase;
    s16 speed;
    u8 unidentified9C[0xC];
    u16 flags;
    u8 unidentifiedAA[6];
    u8 textureIndex;
    u8 unidentifiedB1;
    s8 callbackIndex;
    u8 unidentifiedB3[5];
} SpriteFrameState;
extern void (*D_8008C9C8[])(SpriteFrameState *);
void func_15168870(SpriteFrameState *state);
s32 func_15168C4C();
void func_15168E54(void *, void *);
/* End generated placeholder declarations. */

void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5);
void func_15168A4C(void *arg0, s32 arg1);
extern void (*D_8008CA20[])(void *);
extern void (*D_8008CB64[])(void);
extern void (*D_8008CB70[])(void);

typedef struct ListNode {
    u8 index;
    u8 row;
    u8 pad2[2];
    struct ListNode *prev;
    struct ListNode *next;
} ListNode;

typedef struct {
    u8 pad0[0x14];
    volatile s32 packed_count;
    u8 pad18[0x20];
    s16 timer;
    u8 pad3A[5];
    u8 available;
} PackedCountState;


void func_15167010(void) {
    void (*func)(void);
    struct115 *cur;
    struct115 *end;

    cur = D_8008B4A8;
    end = (struct115 *) ((u8 *) cur + 0x1484);

    while (cur < end) {
        func = (void (*)(void)) cur->unk18;
        if (func != NULL) {
            func();
        }
        cur++;
    }
}

void func_1516706C(void) {
    void (**func)(void);
    void (**end)(void);

    func = D_8008CB64;
    end = D_8008CB70;
    do {
        if (*func != NULL) {
            (*func)();
        }
        func++;
    } while (func != end);
}

/* Walk registered update lists, retaining the next node across callbacks. */
void func_151670C0(void) {
    s32 row, column;
    struct115 *descriptor;
    struct102 *node;

    for (row = 0; row < 2; row++) {
        descriptor = D_8008B4A8;
        for (column = 0; column < 101; column++) {
            if (descriptor->unk0 != NULL) {
                node = *(struct102 **)(D_800DCE50 + row * 0x1A0 + column * 4);
                D_800DD190++;
                while (node != NULL) {
                    D_800DD198[D_800DD190] = *(void **)((u8 *)node + 8);
                    descriptor->unk0(node);
                    node = D_800DD198[D_800DD190];
                }
                D_800DD190--;
            }
            descriptor++;
        }
    }
}
/* Walk secondary callbacks, retaining the next node across each call. */
void func_151671E8(void) {
    s32 row, column;
    struct115 *descriptor;
    struct102 *node;

    for (row = 0; row < 2; row++) {
        descriptor = D_8008B4A8;
        for (column = 0; column < 101; column++) {
            if (descriptor->unk4 != NULL) {
                node = *(struct102 **)(D_800DCE50 + row * 0x1A0 + column * 4);
                D_800DD190++;
                while (node != NULL) {
                    D_800DD198[D_800DD190] = *(void **)((u8 *)node + 8);
                    descriptor->unk4((u8 *)node);
                    node = D_800DD198[D_800DD190];
                }
                D_800DD190--;
            }
            descriptor++;
        }
    }
}
/* Cache live view angles, then visit each column's render callbacks in both rows. */
void func_15167310(void) {
    s32 i;
    s32 column;
    /* Measured frame view; the trailing 16 bytes have no recovered use. */
    struct {
        s32 offset;
        u8 unidentified04[16];
    } frame;
    u8 *row;
    struct102 *head;
    struct102 *node;
    struct115 *descriptor;
    f32 angle;

    i = 0;
    if ((s32)((u32)D_80082FA0 + 1) > 0) {
        do {
            angle = D_800DBFF0[i].unk3A0;
            D_800DD1D8[i] = sinf(angle);
            D_800DD1E8[i] = cosf(angle);
            i++;
        } while (i <= D_80082FA0);
    }
    angle = D_800DBFF0->unk3A0;
    D_800DD1D0[0] = sinf(angle);
    D_800DD1D0[1] = cosf(angle);

    column = 0;
    frame.offset = 0;
    do {
        row = D_800DCE50;
        do {
            head = *(struct102 **)(row + frame.offset);
            if (head != NULL) {
                descriptor = &D_8008B4A8[column];
                if (descriptor->unkC != NULL) {
                    node = head;
                    D_800DD190++;
                    while (node != NULL) {
                        D_800DD198[D_800DD190] = (void *)node->unk8;
                        descriptor->unkC(node);
                        node = D_800DD198[D_800DD190];
                    }
                    D_800DD190--;
                }
            }
            row += 0x1A0;
        } while (row != D_800DCE50 + sizeof(D_800DCE50));
        column++;
        frame.offset += 4;
    } while (column != 104);
}
/* Measured 52-byte render view of the registered descriptor table. */
typedef struct {
    u8 unidentified00[8];
    Gfx *(*draw)(Gfx *, void *, s16);
    u8 unidentified0C[4];
    Gfx *beforeList;
    Gfx *(*before)(Gfx *, s32, s32, s16);
    u8 unidentified18[8];
    Gfx *(*after)(Gfx *, s32, s16);
    Gfx *afterList;
    u8 unidentified28[8];
    s8 mode;
    u8 unidentified31[3];
} ListRenderDescriptor;
extern Mtx D_80089470;
extern Gfx *D_800BE9C8[];
extern s32 D_800BEBA4;
/* Image identity is a 32-bit word; all ones invalidates the cache. */
extern u32 D_800DD1B0;
extern s32 D_800DD1B4, D_800DD1B8;
extern s16 D_800DD1BC, D_800DD1BE;
extern s16 D_800DD1C0, D_800DD1C2, D_800DD1C4, D_800DD1C6;
extern s16 D_800DD1C8, D_800DD1CA, D_800DD1CC, D_800DD1CE;
extern s16 D_800DD1F8, D_800DD204, D_800DD206;
extern s32 D_800DD1FC, D_800DD200, D_800DD208, D_800DD20C;
extern s32 D_800DD210, D_800DD214, D_800DD220, D_800DD224, D_800DD228;
void func_15168F84(s32 selector, s32 *first, s32 *last);
/* Render selected descriptor lists with per-node or whole-column rollback. */
/* Render selected descriptor lists with per-node or whole-column rollback. */
Gfx *func_151674F8(Gfx *output, s32 selector, s16 view, s32 row) {
    s32 column, first, last;
    ListRenderDescriptor *descriptor;
    Gfx *(*draw)(Gfx *, void *, s16);
    ListNode *node;
    Gfx *modeZeroStart;
    Gfx *beforeNode;
    Gfx *modeOneStart;
    s32 overflowed;

    gSPMatrix(output++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    func_15168F84(selector, &first, &last);
    if (first < last) {
        descriptor = (ListRenderDescriptor *)(void *)D_8008B4A8 + first;
        column = first;
        do {
            if (descriptor->draw != NULL) {
                if (*(ListNode **)(void *)(D_800DCE50 + row * 0x1A0 + column * 4) != NULL) {
                    D_8003C8E0 = (column & 0xFFFFFF) | 0x07000000;
                    overflowed = 0;
                    if (descriptor->mode == 0) modeZeroStart = output;
                    if (descriptor->mode == 1) modeOneStart = output;

                    /* Reset this column's cached graphics state before its hooks. */
                    D_800D2DAB = 0;
                    D_800DD228 = 0;
                    D_800DD220 = 0;
                    D_800DD224 = 2;
                    D_800DD1B0 = 0xFFFFFFFFU;
                    D_800DD1B4 = -1;
                    D_800DD1B8 = -1;
                    D_800DD1BC = 0;
                    D_800DD1BE = 0;
                    D_800DD1C0 = D_800DD1C2 = D_800DD1C4 = D_800DD1C6 = -1;
                    D_800DD1C8 = D_800DD1CA = D_800DD1CC = D_800DD1CE = -1;
                    D_800DD1F8 = 0;
                    D_800DD1FC = 0;
                    D_800DD200 = 0;
                    D_800DD204 = -1;
                    D_800DD206 = -1;
                    D_800DD208 = -1;
                    D_800DD20C = -1;
                    D_800DD210 = -1;
                    D_800DD214 = 0;
                    D_800DD218 = 0;
                    D_800DD21C = 0;

                    if (descriptor->beforeList != NULL) {
                        gSPDisplayList(output++, descriptor->beforeList);
                    }
                    if (descriptor->before != NULL) {
                        output = descriptor->before(output, column, row, view);
                    }
                    gSPClearGeometryMode(output++, G_LIGHTING);
                    /* The before hook may have replaced the list head. */
                    node = *(ListNode **)(void *)(D_800DCE50 + row * 0x1A0 + column * 4);
                    if (descriptor->mode == 1) {
                        D_800DD190++;
                        while (node != NULL) {
                            /* Retain the callback before publishing the saved next node. */
                            draw = descriptor->draw;
                            D_800DD198[D_800DD190] = node->next;
                            beforeNode = output;
                            output = draw(output, node, view);
                            if (((output - D_800BE9C8[D_800BE9C0]) > D_800BEBA4) ? 1 : 0) {
                                overflowed = 1;
                                output = beforeNode;
                            }
                            node = D_800DD198[D_800DD190];
                        }
                        D_800DD190--;
                    } else {
                        D_800DD190++;
                        while (node != NULL) {
                            /* Retain the callback before publishing the saved next node. */
                            draw = descriptor->draw;
                            D_800DD198[D_800DD190] = node->next;
                            output = draw(output, node, view);
                            node = D_800DD198[D_800DD190];
                        }
                        D_800DD190--;
                    }
                    if (descriptor->afterList != NULL) {
                        gSPDisplayList(output++, descriptor->afterList);
                    }
                    if (descriptor->after != NULL) {
                        output = descriptor->after(output, column, view);
                    }
                    if (overflowed) {
                        if (((output - D_800BE9C8[D_800BE9C0]) > D_800BEBA4) ? 1 : 0) {
                            gSPSetGeometryMode(output, G_ZBUFFER);
                            return modeOneStart;
                        }
                    }
                    if (descriptor->mode == 0) {
                        if (((output - D_800BE9C8[D_800BE9C0]) > D_800BEBA4) ? 1 : 0) {
                            gSPSetGeometryMode(output, G_ZBUFFER);
                            return modeZeroStart;
                        }
                    }
                    D_8003C8E0 = 0;
                }
            }
            column++;
            descriptor++;
        } while (column < last);
    }
    gSPSetGeometryMode(output++, G_ZBUFFER);
    return output;
}
void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5) {
    u8 *ret;

    ret = func_10003C6C(arg2, 1, arg3, 0, arg5);
    if (ret != NULL) {
        ret[1] = arg1;
        func_15168A4C(ret, arg0);
        ret[0xC] = arg4;
    }

    return ret;
}

void func_15167AD8(void *arg0, u8 arg1, s32 arg2) {
    u8 *tmp;

    tmp = func_15167A68(3, arg2, 0x28, 0, arg1, 1);
    if (tmp != NULL) {
        bcopy(arg0, tmp + 0x10, 0x18);
        tmp[0x23] = 0xFF;
    }
}
/* Apply the optional update callback, rate countdown and wrapped animation phase. */
void func_15167B44(u8 *state) {
    s32 rate;
    s32 remaining;
    s32 cost;

    if (state[0x24] != 0) {
        D_8008CA20[state[0x24]](state);
    }
    rate = *(s8 *)(state + 0x22);
    if (rate > 0) {
        remaining = state[0x23];
        if (rate < remaining) {
            state[0x23] = remaining - rate;
        } else {
            *(s16 *)(state + 0x14) = (*(u8 **)(state + 0x10))[4] << 8;
        }
    } else if (rate < 0) {
        cost = -rate;
        if (*(s16 *)(state + 0x14) / 256 >= (*(u8 **)(state + 0x10))[4] - 1) {
            remaining = state[0x23];
            if (cost < remaining) {
                state[0x23] = remaining - cost;
                *(s16 *)(state + 0x14) -= *(s16 *)(state + 0x16);
            }
        }
    }
    *(s16 *)(state + 0x14) += *(s16 *)(state + 0x16);
    if (*(s16 *)(state + 0x14) / 256 >= (*(u8 **)(state + 0x10))[4]) {
        func_1516972C((struct102 *)state);
    }
}
/* Animation texture and screen-packet callback. */
typedef struct { u32 *frames; } AnimatedTexture15167;
typedef struct {
    u8 pad0[0x10]; AnimatedTexture15167 *texture;
    s16 phase, rate, x, y, z, width, height;
    s8 mode; u8 alpha;
} AnimatedState15167;
typedef struct { s16 x,y,z,width,height; u8 alpha, padB[2], zero, padE[6]; } AnimatedPacket15167;
typedef struct { u8 before[4]; s32 value; u8 pad[8]; } AnimatedSync15167;
extern u32 D_800A4AC8[];
Gfx *func_15142E24(Gfx *, void *, s32, s32, s32, s32, s32, u8, u8 *, u8 *, s32);
Gfx *func_15142FBC(Gfx *, u32, u32, u8 *);
Gfx *func_15095760(Gfx *, s16 *);
/* Emit the current animated texture and its projected screen packet. */
Gfx *func_15167C58(Gfx *output, AnimatedState15167 *state, volatile s32 unused) {
    AnimatedPacket15167 packet;
    AnimatedSync15167 sync;
    s32 mode;
    sync.value = 1;
    output = func_15142E24(output, state->texture, (s32)((u32)(s32)state->phase << 8), 2,
        256, 256, state->texture->frames[state->phase >> 8], 5, (u8 *)&packet, (u8 *)&sync.value, 3);
    packet.x = state->x; packet.y = state->y; packet.z = state->z;
    packet.width = state->width; packet.height = state->height;
    packet.alpha = state->alpha; packet.zero = 0;
    if (state->mode != 255) mode = 3;
    else if (state->mode == 255) mode = 9;
    output = func_15142FBC(output, 0x2C00, D_800A4AC8[mode * 2 + 1] | D_800A4AC8[mode * 2] | 4, (u8 *)&sync.value);
    return func_15095760(output, (s16 *)&packet);
}
/* Return the allocated particle so callers can append their extra payload. */
u8 *func_15167D84(void *packet, s32 alternate, s32 extraBytes, s8 marker, u8 mode, s32 owner) {
    u8 *particle;
    s32 kind;

    if (alternate == 0) {
        kind = 5;
    } else {
        kind = 0x42;
    }

    particle = func_15167A68(kind, owner, extraBytes + 0x50, 0, mode, 1);
    if (particle == NULL) return particle;
    bcopy(packet, particle + 0x10, 0x38);
    particle[0x48] = marker;
    return particle;
}
/* Advance lifetime, fade, fixed-point motion and animation before completion. */
void func_15167E0C(CompactSpriteState *state) {
    u8 finished;
    s32 packed;
    s32 delta;
    s32 speed;
    s32 upper;

    finished = 0;
    if (state->remaining != 0x7FFF) {
        state->remaining = (u32)state->remaining - (u32)D_800BE9E4;
        if (state->remaining < 0) {
            state->remaining = 0;
            finished = 1;
        }
    }
    if (state->fadeStep > 0) {
        if (state->fadeStep < state->alpha) {
            state->alpha -= state->fadeStep;
        } else {
            state->remaining = 0;
            finished = 1;
        }
    }
    if (state->callbackIndex != -1 && D_8008C9C8[state->callbackIndex] != NULL) {
        D_8008C9C8[state->callbackIndex]((SpriteFrameState *)(void *)state);
    }
    if (state->remaining != 0) {
        state->velocityY += state->accelerationY;
        packed = ((u32)(s32)state->y << 8) | state->fractionY;
        delta = (u32)(s32)state->velocityY * (u32)D_800BE9E4;
        state->y = (s32)((u32)packed + (u32)delta) >> 8;
        state->fractionY = (u32)packed + (u32)delta;
        packed = ((u32)(s32)state->x << 8) | state->fractionX;
        delta = (u32)(s32)state->velocityX * (u32)D_800BE9E4;
        state->x = (s32)((u32)packed + (u32)delta) >> 8;
        state->fractionX = (u32)packed + (u32)delta;
        packed = ((u32)(s32)state->z << 8) | state->fractionZ;
        delta = (u32)(s32)state->velocityZ * (u32)D_800BE9E4;
        state->z = (s32)((u32)packed + (u32)delta) >> 8;
        state->fractionZ = (u32)packed + (u32)delta;

        speed = state->speed;
        if (speed != 0) {
            upper = (state->texture[4] << 8) - 1;
            state->phase = (u32)state->phase + (u32)speed * (u32)D_800BE9E4;
            if (state->phase > upper) {
                if (state->flags & 0x20) {
                    state->remaining = 0;
                    finished = 1;
                } else {
                    state->flags |= 0x80;
                    if (state->flags & 2) {
                        state->phase = upper - state->phase % upper;
                        state->speed = -state->speed;
                    } else {
                        do {
                            state->phase -= upper;
                        } while (state->phase > upper);
                    }
                }
            } else if (state->phase < 0) {
                if (state->flags & 0x40) {
                    state->remaining = 0;
                    finished = 1;
                } else if (state->flags & 2) {
                    state->phase = -state->phase % upper;
                    state->speed = -speed;
                } else {
                    do {
                        state->phase += upper;
                    } while (state->phase < 0);
                }
            }
        }
    } else {
        finished = 1;
    }
    if (finished != 0) {
        if (state->completionIndex != -1) {
            D_8008CA20[state->completionIndex](state);
        }
        func_1516972C((struct102 *)(void *)state);
    }
}
extern f32 D_800A6CA0, D_800A6CA4;
extern u32 D_800D2C9C;
extern u8 D_800907FC[], D_8009053C[];
/* Same measured 20-byte packet consumed by 15095760/15095B08. */
typedef struct {
    s16 x, y, z, width, height;
    u8 alpha, animationStep, animationFrame, flipFlags;
    u8 unidentified0E[2];
    void *descriptor;
} CompactSpriteDrawPacket;
Gfx *func_15142E24(Gfx *, void *, s32, s32, s32, s32, s32, u8, u8 *, u8 *, s32);
Gfx *func_15142B7C(Gfx *, u32, u32);
Gfx *func_1513F4E4(Gfx *, u8, u8 *);
Gfx *func_15142CF0(Gfx *, s32, s32, s32, s32, s32, s32, u8 *);
Gfx *func_15142C10(Gfx *, s32, s32, s32, s32, u8 *);
/* Build compact sprite texture, dimensions, render state and colors. */
Gfx *func_15168118(Gfx *output, void *record, s16 view) {
    CompactSpriteState *state = record;
    CompactSpriteDrawPacket packet;
    u8 sync;
    u8 combiner, renderMode;
    u8 *texture;
    u32 image;
    s32 dimension, baseWidth;
    f32 angle;
    s32 positiveWidth;
    u32 extraMode;
    u32 renderWord0, renderWord1;
    s32 type;
    s32 red, green, blue;
    s32 primaryRed, primaryGreen, primaryBlue, primaryAlpha;

    packet.flipFlags = 0;
    if (state->flags & 4) packet.flipFlags = 1;
    if (state->flags & 8) packet.flipFlags |= 2;
    sync = 1;
    texture = state->texture;
    if (*(u32 *)texture < 0x10000000U) {
        image = *(u32 *)texture;
    } else {
        image = ((u32 *)*(u32 *)texture)[state->phase >> 8];
    }
    output = func_15142E24(output, texture, (u32)(s32)state->phase << 8,
                         2, 0x100, 0x100, image, 5, (u8 *)&packet, &sync, 3);
    packet.x = state->x;
    packet.y = state->y;
    packet.z = state->z;
    dimension = state->width;
    if (dimension < 0) {
        angle = fabsf(D_800DBFF0[view].unk380 + (s32)(state->orientation & 0xFF) * 1.40625f);
        while (angle >= 360.0f) angle -= 360.0f;
        if (angle >= 180.0f) angle -= 180.0f;
        if (angle >= 90.0f) angle = 180.0f - angle;
        dimension = (s32)((f32)dimension * angle * D_800A6CA0);
        if (dimension < 0x400) dimension = 0x400;
    }
    packet.width = dimension;
    dimension = state->height;
    if (dimension < 0) {
        baseWidth = state->width;
        if (baseWidth < 0) positiveWidth = 0;
        else positiveWidth = baseWidth;
        angle = fabsf(D_800DBFF0[view].unk388);
        dimension = (s32)(angle * (positiveWidth + dimension) * D_800A6CA4 - (f32)dimension);
    }
    packet.height = dimension;
    if (state->flags & 0x100) {
        combiner = (state->renderSettings & 0xFFFF0000) >> 16;
        renderMode = state->renderSettings;
        output = func_15142B7C(output, 5, 0);
        output = func_1513F4E4(output, combiner, &sync);
        if (state->flags & 0x200) extraMode = 0x100000;
        else extraMode = 0;
        renderWord1 = D_800A4AC8[renderMode * 2 + 1];
        renderWord0 = D_800A4AC8[renderMode * 2];
        output = func_15142FBC(output, extraMode | D_800D2C9C | 0x2CA0, renderWord1 | renderWord0 | 4, &sync);
        primaryGreen = state->green;
    } else {
        type = (state->texture)[0xA];
        if (type != 5) {
            output = func_1513F4E4(output, 13, &sync);
            renderWord1 = D_800A4AC8[7];
            renderWord0 = D_800A4AC8[6];
            output = func_15142FBC(output, D_800D2C9C | 0x2CA0, renderWord1 | renderWord0 | 4, &sync);
        } else if (type == 3) { /* Retail retains this test after the type-5 gate. */
            output = func_1513F4E4(output, 14, &sync);
            renderWord1 = D_800A4AC8[7];
            renderWord0 = D_800A4AC8[6];
            output = func_15142FBC(output, D_800D2C9C | 0x2CA0, renderWord1 | renderWord0 | 4, &sync);
        } else if (state->flags & 0x10) {
            output = func_1513F4E4(output, 13, &sync);
            renderWord1 = D_800A4AC8[37];
            renderWord0 = D_800A4AC8[36];
            output = func_15142FBC(output, D_800D2C9C | 0x2CA0, renderWord1 | renderWord0 | 4, &sync);
        } else {
            output = func_1513F4E4(output, 15, &sync);
            renderWord1 = D_800A4AC8[35];
            renderWord0 = D_800A4AC8[34];
            output = func_15142FBC(output, D_800D2C9C | 0x100000 | 0x2CA0, renderWord1 | renderWord0 | 4, &sync);
        }
        primaryGreen = state->green;
    }
    primaryBlue = state->blue;
    primaryAlpha = state->alpha;
    primaryRed = state->red;
    output = func_15142CF0(output, 1, 0, primaryRed, primaryGreen, primaryBlue, primaryAlpha, &sync);
    if (state->flags & 1) {
        red = state->environmentRed; green = state->environmentGreen; blue = state->environmentBlue;
    } else if (state->texture == D_800907FC) {
        red = green = 128; blue = 255;
    } else if (state->texture == D_8009053C) {
        red = green = blue = 255;
    } else {
        red = green = blue = 0;
    }
    output = func_15142C10(output, red, green, blue, 0, &sync);
    return func_15095760(output, (s16 *)&packet);
}
/* Initialize eight vertex colors and the two texture quads, preserving positions. */
void func_1516865C(void *input, u8 red, u8 green, u8 blue, u8 alpha) {
    SelectedVertexSprite *sprite = input;
    s16 lowV = 8192;
    s16 highV = (*(u16 *)(D_8008CA4C[sprite->textureIndex] + 8) + 256) << 5;
    s16 lowU = 8192;
    s16 highU = (*(u16 *)(D_8008CA4C[sprite->textureIndex] + 6) + 256) << 5;
    s32 i = 0;
    Vtx *vertices = sprite->vertices;
    do {
        i++;
        vertices += 4;
        vertices[-3].v.flag = 0;
        vertices[-3].v.cn[0] = red;
        vertices[-3].v.cn[1] = green;
        vertices[-3].v.cn[2] = blue;
        vertices[-3].v.cn[3] = alpha;
        vertices[-2].v.flag = 0;
        vertices[-2].v.cn[0] = red;
        vertices[-2].v.cn[1] = green;
        vertices[-2].v.cn[2] = blue;
        vertices[-2].v.cn[3] = alpha;
        vertices[-1].v.flag = 0;
        vertices[-1].v.cn[0] = red;
        vertices[-1].v.cn[1] = green;
        vertices[-1].v.cn[2] = blue;
        vertices[-1].v.cn[3] = alpha;
        vertices[-4].v.flag = 0;
        vertices[-4].v.cn[0] = red;
        vertices[-4].v.cn[1] = green;
        vertices[-4].v.cn[2] = blue;
        vertices[-4].v.cn[3] = alpha;
    } while (i != 2);
    if (sprite->flags & 0x80) {
        highV = 8192;
        lowV = (*(u16 *)(D_8008CA4C[sprite->textureIndex] + 8) + 256) << 5;
    }
    if (sprite->flags & 0x100) {
        highU = 8192;
        lowU = (*(u16 *)(D_8008CA4C[sprite->textureIndex] + 6) + 256) << 5;
    }
    sprite->vertices[6].v.tc[0] = lowU;
    sprite->vertices[7].v.tc[1] = lowV;
    sprite->vertices[7].v.tc[0] = highU;
    sprite->vertices[1].v.tc[0] = sprite->vertices[5].v.tc[0] = sprite->vertices[2].v.tc[0] = sprite->vertices[6].v.tc[0];
    sprite->vertices[5].v.tc[1] = highV;
    sprite->cleared88 = 0;
    sprite->vertices[2].v.tc[1] = sprite->vertices[6].v.tc[1] = sprite->vertices[3].v.tc[1] = sprite->vertices[7].v.tc[1];
    sprite->cleared9C = 0;
    sprite->cleared9E = 0;
    sprite->vertices[0].v.tc[0] = sprite->vertices[4].v.tc[0] = sprite->vertices[3].v.tc[0] = sprite->vertices[7].v.tc[0];
    sprite->vertices[0].v.tc[1] = sprite->vertices[4].v.tc[1] = sprite->vertices[1].v.tc[1] = sprite->vertices[5].v.tc[1];
}
void *func_15168800(void *arg0, u8 arg1, s32 arg2) {
    u8 *tmp;

    tmp = func_15167A68(0xE, arg2, 0xB8, 1, arg1, 1);
    if (tmp == NULL) {
        return NULL;
    }
    bcopy(arg0, tmp + 0x10, 0xA8);
    return tmp;
}
/* Advance the signed sprite phase, then honor callback changes before cleanup. */
void func_15168870(SpriteFrameState *state) {
    s32 upper;
    s32 frames;
    s32 speed;
    void (*callback)(SpriteFrameState *);

    speed = state->speed;
    if (speed != 0) {
        frames = D_8008CA4C[state->textureIndex][4];
        state->phase = (u32)state->phase + (u32)speed * (u32)D_800BE9E4;
        upper = (frames << 8) - 1;
        if (state->phase > upper) {
            if (state->flags & 0x40) {
                state->phase = upper - state->phase % upper;
                state->speed = -speed;
            } else if (state->flags & 4) {
                state->phase = -1;
            } else {
                do {
                    state->phase -= upper;
                } while (state->phase > upper);
            }
        } else if (state->phase < 0) {
            if (state->flags & 0x40) {
                state->phase = -state->phase % upper;
                state->speed = -speed;
            } else if (state->flags & 4) {
                state->phase = -1;
            } else {
                do {
                    state->phase += upper;
                } while (state->phase < 0);
            }
        }
    }
    if (state->callbackIndex != -1) {
        callback = D_8008C9C8[state->callbackIndex];
        if (callback != NULL) {
            callback(state);
        }
    }
    if (state->phase == -1) {
        func_1516972C((struct102 *)state);
    }
}
// NON-MATCHING: only differs from us by the jal target address of func_15168B10
// (not yet confirmed byte-matching itself) - this function's own code is verified
// byte-identical otherwise.
void func_15168A2C(s32 arg0) {
    func_15168B10(arg0, 0);
}
void func_15168A4C(void *arg0, s32 arg1) {
    ListNode *node;
    ListNode **slot;
    u8 row;
    s32 column;

    node = arg0;
    row = node->row;
    column = arg1 * 4;
    slot = (ListNode **) (D_800DCE50 + (row * 0x1A0) + column);
    if ((node->next = *slot) != NULL) {
        node->next->prev = node;
    }
    node->index = arg1;
    node->prev = NULL;
    *slot = node;
}

void func_15168A9C(ListNode *arg0) {
    ListNode **slot;
    ListNode *next;
    ListNode *prev;
    u8 row;
    u8 index;

    row = arg0->row;
    index = arg0->index;
    slot = (ListNode **) (D_800DCE50 + (row * 0x1A0) + (index * 4));
    if (arg0 == *slot) {
        *slot = arg0->next;
    }
    next = arg0->next;
    if (next != NULL) {
        next->prev = arg0->prev;
    }
    prev = arg0->prev;
    if (prev != NULL) {
        prev->next = arg0->next;
    }
}


void func_15168B10(s32 arg0, s32 arg1) {
    func_15168A9C(arg0);
    func_15168A4C(arg0, arg1);
}

/* Note 388: guards preserve one closed IDO register-allocation cycle. */
void func_15168B44(PackedCountState *arg0) {
    s32 value = arg0->packed_count;
    u16 count = value;
    s32 upper;

    if (count != 0) {
        count--;
        upper = value & 0xFFFF0000;
        arg0->packed_count = upper;
        arg0->timer = 0x1E;
        arg0->packed_count = upper | count;
        return;
    }

    count = value >> 16;
    if (count < arg0->available) {
        arg0->available -= count;
        arg0->timer = 0x1E;
    } else {
        arg0->timer = 0;
    }
}

void func_15168BAC(void *arg0) {
    u8 idx = *((u8 *) arg0 + 0xE4);

    if (idx != 0) {
        D_8008CA20[idx](arg0);
    }
}

void func_15168BE4(void *arg0, u8 arg1, s32 arg2) {
    void *tmp;

    if (*(s32 *) ((u8 *) arg0 + 0x40) != 0) {
        tmp = func_15167A68(0x10, arg2, 0xF0, 1, arg1, 1);
        if (tmp != NULL) {
            bcopy(arg0, (u8 *) tmp + 0x90, 0x60);
        }
    }
}

/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15168C4C.s. */
s32 func_15168C4C() {
    return 0;
}
void func_15168E34(s32 *arg0, s32 arg1) {
    s32 temp_v0;

    temp_v0 = *arg0;
    if (!(temp_v0 & 0x0F000000)) {
        *arg0 = temp_v0 + arg1;
    }
}
void func_15168E54(void *arg0, void *arg1) {
    s8 *cur;
    s32 i = 0;
    s8 opcode;

    cur = arg0;
    if (*(volatile s8 *)cur != -0x21) {
        opcode = *(volatile s8 *)cur;
        do {
            if ((1 == opcode) || ((-0x24 == opcode) && (0xE == ((u8 *)cur)[3]))) {
                func_15168E34((s32 *)(cur + 4), (s32)arg1);
            }
            i++;
            cur = (s8 *)((i << 3) + (s32)arg0);
            opcode = *(volatile s8 *)cur;
        } while (-0x21 != opcode);
    }
}
void func_15168F08(s8 *arg0, s32 arg1) {
    s8 *cur;
    s32 i = 0;
    s8 opcode;

    cur = arg0;
    if (*(volatile s8 *)cur != -0x21) {
        opcode = *(volatile s8 *)cur;
        do {
            i++;
            if ((1 == opcode) || ((-0x24 == opcode) && (0xE == ((u8 *)cur)[3]))) {
                *(s32 *)(cur + 4) &= 0xFFFFFF;
                *(s32 *)(cur + 4) += arg1;
            }
            cur = arg0 + (i << 3);
            opcode = *(volatile s8 *)cur;
        } while (opcode != -0x21);
    }
}
/* Return the inclusive index range for the selected group. */
void func_15168F84(s32 group, s32 *first, s32 *last) {
    if (group == 0) {
        *first = 1;
        *last = 0x41;
    } else if (group == 1) {
        *first = 0x42;
        *last = 0x4F;
    } else if (group == 2) {
        *first = 0x50;
        *last = 0x58;
    } else if (group == 3) {
        *first = 0x59;
        *last = 0x5C;
    } else if (group == 5) {
        *first = 0x61;
        *last = 0x63;
    } else if (group == 6) {
        *first = 0x64;
        *last = 0x65;
    } else {
        *first = 0x5D;
        *last = 0x60;
    }
}
/* Forward an event across the complete node-column range. */
void func_15169040(s32 arg0, u8 arg1) {
    func_15169070(0, 0x68, arg0, arg1);
}
/* Walk both node rows in the clamped range, preserving callback-safe next links. */
void func_15169070(s32 first, s32 last, s32 payload, u8 opcode) {
    u8 pad[20]; /* Retain the observed frame and column home; original use is unknown. */
    s32 column;
    u8 *row;
    u8 *head;
    struct115 *descriptor;
    void *node;

    func_15143D18(&first, &last, 2, 0x68);
    if (first < last) {
        descriptor = &D_8008B4A8[first];
        column = first * 4;
        do {
            row = D_800DCE50;
            head = D_800DCE50 + column;
            do {
                if (descriptor->unk1C != NULL) {
                    node = *(void **) head;
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = *(void **) ((u8 *) node + 8);
                            func_1516968C(node, (u8 *)payload, opcode);
                            descriptor->unk1C(node, payload, opcode);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                } else {
                    node = *(void **) head;
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = *(void **) ((u8 *) node + 8);
                            func_1516968C(node, (u8 *)payload, opcode);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                }
                row += 0x1A0;
                head += 0x1A0;
            } while (row != D_800DCE50 + sizeof(D_800DCE50));
            column += 4;
            descriptor += 1;
        } while (column < last * 4);
    }
}
/* Dispatch indexed descriptor columns, retaining live entries and continuation slots. */
void func_15169260(void *indices, s32 count, s32 payload, u8 opcode) {
    struct102 *node;
    /* Measured retail local-frame view; the 12-byte gap has no recovered use. */
    struct {
        u8 *row;
        u8 unidentified04[12];
        s32 index;
    } state;

    state.index = 0;
    if (count > 0) {
        do {
            state.row = D_800DCE50;
            do {
                if (D_8008B4A8[*(s32 *)indices].unk1C != NULL) {
                    node = *(struct102 **)(state.row + *(s32 *)indices * 4);
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = (void *)node->unk8;
                            func_1516968C(node, (u8 *)payload, opcode);
                            D_8008B4A8[*(s32 *)indices].unk1C(node, payload, opcode);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                } else {
                    node = *(struct102 **)(state.row + *(s32 *)indices * 4);
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = (void *)node->unk8;
                            func_1516968C(node, (u8 *)payload, opcode);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                }
                state.row += 0x1A0;
            } while (state.row != D_800DCE50 + sizeof(D_800DCE50));
            indices = (u8 *)indices + 4;
            state.index++;
        } while (state.index != count);
    }
}
/* Dispatch one descriptor column in both rows, preserving callback-safe next links. */
void func_1516944C(s32 column, s32 payload, u8 opcode) {
    u8 *row;
    u8 *head;
    struct115 *descriptor;
    void *node;

    if (column >= 0x68) {
        column = 0x67;
    }
    descriptor = &D_8008B4A8[column];
    head = D_800DCE50 + column * 4;
    row = D_800DCE50;
    do {
        if (descriptor->unk1C != NULL) {
            node = *(void **)head;
            D_800DD190++;
            if (node != NULL) {
                do {
                    D_800DD198[D_800DD190] = *(void **)((u8 *)node + 8);
                    func_1516968C(node, (u8 *)payload, opcode);
                    descriptor->unk1C(node, payload, opcode);
                    node = D_800DD198[D_800DD190];
                } while (node != NULL);
            }
            D_800DD190--;
        } else {
            node = *(void **)head;
            D_800DD190++;
            if (node != NULL) {
                do {
                    D_800DD198[D_800DD190] = *(void **)((u8 *)node + 8);
                    func_1516968C(node, (u8 *)payload, opcode);
                    node = D_800DD198[D_800DD190];
                } while (node != NULL);
            }
            D_800DD190--;
        }
        row += 0x1A0;
        head += 0x1A0;
    } while (row != D_800DCE50 + sizeof(D_800DCE50));
}

void func_151695F0(void *arg0, u8 arg1) {
    struct {
        void *ptr;
        u8 tag;
    } tmp;

    tmp.ptr = arg0;
    tmp.tag = ((u8 *) arg0)[0x3B];
    func_15169040((s32) &tmp, arg1);
}

void func_1516962C(s32 arg0, void *arg1, u8 arg2) {
    struct {
        void *ptr;
        u8 tag;
    } tmp;

    tmp.ptr = arg1;
    tmp.tag = ((u8 *) arg1)[0x3B];
    func_1516944C(arg0, (s32) &tmp, arg2);
}

s32 func_15169668(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    D_800D2DAB = 1;
    return arg0;
}
// Matched with guarded byte-load scheduling normalization.
void func_1516968C(struct102 *arg0, u8 *arg1, u8 arg2) {
    if (((arg2 == 0xF) || (arg2 == 0x10)) && (*arg1 == arg0->unkC)) {
        func_1516972C(arg0);
    }
}
// Matched with guarded loop-setup scheduling normalization.
void func_151696DC(void *arg0) {
    s8 i;
    s8 count;
    void **slots;

    i = 0;
    count = D_800DD190;
    slots = D_800DD198;
    if (count > 0) {
        do {
            if (arg0 == slots[i]) {
                slots[i] = *(void **) ((u8 *) arg0 + 8);
            }
            i++;
        } while (i < count);
    }
}

void func_1516972C(struct102 *arg0) {
    void (*func)(struct102 *arg0);
    func_151696DC(arg0);

    if (arg0->unk0 >= 2) {
        func = D_8008B4D0[arg0->unk0].unk0;
        if (func != NULL) {
            func(arg0);
            return;
        }
        func_15169804(arg0);
    }
}

void func_1516979C(struct102 *arg0) {
    void (*func)(struct102 *arg0);

    func_151696DC(arg0);
    func = D_8008B4D4[arg0->unk0].unk0;
    if (func != NULL) {
        func(arg0);
        return;
    }
    func_15169824(arg0);
}

void func_15169804(struct102 *arg0) {
    func_15168B10(arg0, 1);
}

void func_15169824(struct102 *arg0) {
    func_15168A9C(arg0);
    func_10004074(arg0);
}

/* Release a matching owner, or exchange a paired reference and its identity tag. */
void func_15169850(s32 pairAddress, u8 command, s32 valueAddress, s32 tagAddress, s32 owner) {
    s32 *pair = (s32 *)pairAddress;
    s32 *value = (s32 *)valueAddress;
    u8 *tag = (u8 *)tagAddress;

    if (command == 0) {
        if ((pair[0] == *value) || (((u8 *)pair)[4] == *tag)) {
            func_1516972C((struct102 *)owner);
        }
    } else if (command == 0x2D) {
        if (pair[0] == *value) {
            *value = pair[1];
            *tag = ((u8 *)pair)[9];
        } else if (pair[1] == *value) {
            *value = pair[0];
            *tag = ((u8 *)pair)[8];
        }
    }
}
