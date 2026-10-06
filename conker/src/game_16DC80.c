#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
u8 *func_151407D0(void *source, s32 size, u8 *descriptor, u8 kind, u8 mode,
                 u8 first, u8 variant, s8 selector, u8 channel, s32 context);
s32 func_151408A4();
void func_151412BC(void);
s32 func_15141478(u8 *actor);
s32 func_151415D4(u8 *actor);
void func_151416E8(u8 *actor, u8 *event, u8 command);
/* End generated placeholder declarations. */

void func_1514182C(u8 *actor, f32 *origin, f32 height, f32 scale, f32 angleX, f32 angleZ);
void func_150A7960(f32 *, f32, f32, f32, f32 *, f32 *, f32 *);

typedef struct {
    s32 first;
    s32 second;
} TwoWord16DC80;

typedef void (*ActorEventCallback16DC80)(u8 *, u8 *, u8);
extern ActorEventCallback16DC80 D_8008A02C[];

u8 *func_151407D0(void *source, s32 size, u8 *descriptor, u8 kind, u8 mode,
                       u8 first, u8 variant, s8 selector, u8 channel, s32 context) {
    u8 *result;
    u8 *payload;
    descriptor[1] = 3;
    *(u32 *)(descriptor + 0x40) |= 0x40400000;
    result = func_1513D524(descriptor, kind, mode, first, 1, variant, size, channel, context);
    if (result != NULL) {
        payload = result + 0x110;
        memcpy(payload, source, size);
        *(s32 *)(payload + 0x44) = 0;
        payload[0x59] = selector;
        goto finalize;
    }
    return NULL;
finalize:
    if (result != NULL) {
        *(u32 *)&D_800DC9F0 += 1;
    }
    return result;
}

/* Non-matching C placeholders for asm/nonmatchings/game_16DC80/func_151408A4.s. */
s32 func_151408A4() {
    return 0;
}

void func_151411A4(struct210 *arg0) {
    func_1513CA6C(arg0);
}

void func_151411C4(struct210 *arg0) {
    func_1513CAA0(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/game_16DC80/func_151411E4.s")

void func_15141250(struct210 *arg0) {
    if (*(vertex *volatile *)((u8 *)arg0 + 0x154) != NULL) {
        func_1517E134(*(vertex *volatile *)((u8 *)arg0 + 0x154), arg0);
    }
    D_800DC9F0--;
    D_80089FE4[*(u8 *)((u8 *)arg0 + 0x168)](arg0);
}

void func_151412BC(void) {
    u8 *row;
    u8 *node;
    u8 *payload;
    u8 bucket;
    s32 channel;
    s32 x;
    s32 y;
    u32 flags;
    row = D_800DCE50;
    do {
        bucket = 0;
        do {
            node = ((u8 **)row)[((s32 *)&D_800A5168)[bucket]];
            if (node != NULL) {
                do {
                    flags = *(u32 *)(node + 0x58);
                    if (flags & 0x2000) {
                        *(s16 *)(node + 0x162) = 0;
                        *(s16 *)(node + 0x160) = 0;
                        *(s16 *)(node + 0x15E) = 0;
                        *(s16 *)(node + 0x15C) = 0;
                        if (flags & 0x10) {
                            channel = 0;
                            payload = node + 0x110;
                            if (D_80082FA0 >= 0) {
                                do {
                                    x = *(s32 *)(payload + 0x24 + channel * 4);
                                    if (x >= 0 && x < D_800BE620 &&
                                        (y = *(s32 *)(payload + 0x34 + channel * 4)) >= 0 && y < D_800BE624) {
                                        *(u16 *)(payload + 0x4C + channel * 2) = (*(u16 **)&D_800BE9C4)[y * D_800BE620 + x];
                                    } else {
                                        *(u16 *)(payload + 0x4C + channel * 2) = 0x7FFF;
                                    }
                                    channel = (u8)(channel + 1);
                                } while (channel <= D_80082FA0);
                            }
                        }
                    }
                    node = *(u8 **)(node + 8);
                } while (node != NULL);
            }
            bucket++;
        } while (bucket < 4);
        row += 0x1A0;
    } while (row != (u8 *)&D_800DD190);
}

void func_1514143C(struct210 *arg0) {
    if (arg0->unk154 != NULL) {
        arg0->unk154->x = arg0->unk34;
        arg0->unk154->y = arg0->unk38;
        arg0->unk154->z = arg0->unk3C;
    }
}

s32 func_15141478(u8 *actor) {
    f32 sample;
    u8 *runtime;
    u8 *payload;
    payload = actor + 0x110;
    runtime = actor + 0x170;
    *(f32 *)(actor + 0x180) -= D_800BE9A4;
    if (*(f32 *)(actor + 0x180) < 0.0f) {
        sample = func_150ADA68();
        *(f32 *)(runtime + 0x10) = sample * *(f32 *)(runtime + 0x14);
        if (func_150ADA20() & 3) {
            sample = func_150ADA68();
            *(f32 *)(runtime + 0xC) = sample * (*(f32 *)(runtime + 0) - *(f32 *)(runtime + 4)) + *(f32 *)(runtime + 4);
        } else {
            sample = func_150ADA68();
            *(f32 *)(runtime + 0xC) = sample * (*(f32 *)(runtime + 8) - *(f32 *)(runtime + 0)) + *(f32 *)(runtime + 0);
        }
    }
    *(f32 *)(payload + 0x48) += (*(f32 *)(runtime + 0xC) - *(f32 *)(payload + 0x48)) * *(f32 *)(runtime + 0x18);
    return 1;
}

s32 func_15141564(u8 *arg0) {
    u8 *base = arg0 + 0x170;

    *(f32 *)(arg0 + 0x158) = (*(f32 *)(base + 4) * sinf(*(f32 *)(arg0 + 0x178))) + *(f32 *)(base + 0);
    *(f32 *)(base + 8) += *(f32 *)(base + 0xC) * D_800BE9A4;
    *(f32 *)(base + 8) = func_15144B68(*(f32 *)(base + 8));
    return 1;
}

s32 func_151415D4(u8 *actor) {
    u8 *runtime;
    f32 period;
    runtime = actor + 0x170;
    if (*(f32 *)(actor + 0x17C) < *(f32 *)(actor + 0x180)) {
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 4);
    } else if (*(f32 *)(runtime + 0xC) < *(f32 *)(runtime + 0x14)) {
        f32 factor;
        factor = (*(f32 *)(runtime + 0xC) - *(f32 *)(runtime + 0x10)) * *(f32 *)(runtime + 0x20);
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 8) * factor + *(f32 *)(runtime + 4);
    } else if (*(f32 *)(runtime + 0xC) < *(f32 *)(runtime + 0x18)) {
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 0);
    } else {
        f32 factor;
        factor = 1.0f - (*(f32 *)(runtime + 0xC) - *(f32 *)(runtime + 0x18)) * *(f32 *)(runtime + 0x20);
        *(f32 *)(actor + 0x158) = *(f32 *)(runtime + 4) + *(f32 *)(runtime + 8) * factor;
    }
    period = *(f32 *)(runtime + 0x1C);
    *(f32 *)(runtime + 0xC) += D_800BE9A4;
    while (period < *(f32 *)(runtime + 0xC)) {
        *(f32 *)(runtime + 0xC) -= period;
    }
    return 1;
}

void func_151416E8(u8 *actor, u8 *event, u8 command) {
    u8 *payload;
    if (D_8008A02C[*(volatile u8 *)(actor + 0x168)] != NULL) {
        D_8008A02C[*(volatile u8 *)(actor + 0x168)](actor, event, command);
    }
    if (command == 0x22 || command == 0x24 || command == 0x25) {
        /* Retain the retail payload base using unsigned N64 address arithmetic. */
        payload = (u8 *)((u32)actor - (u32)-0x110);
        if (event[0] == payload[0x58]) {
            switch (command) {
                case 0x22: func_1516972C((struct102 *)actor); break;
                case 0x24: *(s8 *)(payload + 0x59) = -1; break;
                case 0x25: *(s8 *)(payload + 0x59) = 2; break;
            }
        }
    }
}

void func_151417C4(u8 arg0, u8 arg1) {
    u8 byte[1];
    TwoWord16DC80 tmp;

    tmp = *(TwoWord16DC80 *) D_8008A074;
    byte[0] = arg0;
    func_15169260(&tmp, 2, (s32) byte, arg1);
}

s32 func_15141818(s32 arg0, s32 arg1) {
    return 0;
}

void func_1514182C(u8 *actor, f32 *origin, f32 height, f32 scale, f32 angleX, f32 angleZ) {
    f32 dx, dy, dz;
    f32 matrix[4][4];
    func_150A8050(matrix, angleX, 0.0f, angleZ);
    matrix[3][0] = origin[0];
    matrix[3][1] = origin[1];
    matrix[3][2] = origin[2];
    func_150A7960((f32 *)matrix, 0.0f, height, 0.0f,
        (f32 *)(actor + 0x34), (f32 *)(actor + 0x38), (f32 *)(actor + 0x3C));
    dx = (*(f32 *)(actor + 0x34) - origin[0]) * scale;
    dy = (*(f32 *)(actor + 0x38) - origin[1]) * scale;
    dz = (*(f32 *)(actor + 0x3C) - origin[2]) * scale;
    *(f32 *)(actor + 0x40) = *(f32 *)(actor + 0x34) + dx * 500.0f;
    *(f32 *)(actor + 0x44) = *(f32 *)(actor + 0x38) + dy * 500.0f;
    *(f32 *)(actor + 0x48) = *(f32 *)(actor + 0x3C) + dz * 500.0f;
}

s32 func_15141928(void *arg0) {
    void *temp_v0 = *(void **)((u8 *)arg0 + 0x178);
    func_1514182C((u8 *)arg0, (f32 *)((u8 *)arg0 + 0x17C),
        *(f32 *)((u8 *)arg0 + 0x170), *(f32 *)((u8 *)arg0 + 0x174),
        *(f32 *)temp_v0, *(f32 *)((u8 *)temp_v0 + 8));
    return 1;
}
