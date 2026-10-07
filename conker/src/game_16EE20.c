#include <ultra64.h>

/* The retail checker receives complete words, not the legacy narrow ABI. */
#define func_150A29C8 func_150A29C8_legacy_narrow_signature
#include "functions.h"
#undef func_150A29C8
/* This owner uses the retail pointer, not the legacy inline-array declaration. */
#define D_800D3098 D_800D3098_legacy_array
#include "variables.h"
#undef D_800D3098

typedef struct {
    s32 flags;
    s16 lifetime;
    u8 slot, kind;
    s32 zero8, zeroC;
    u8 random, value11, value12, value13, value14, value15, zero16, seven;
    s32 effect, sourceWord;
    u8 value20, pad21;
    s16 size, count;
} GameRandomDescriptor;

typedef struct {
    s16 value0, value2, value4, value6;
    struct17 point;
    f32 value14, value18, value1C, value20, value24, value28;
    s16 value2C, value2E, value30, value32, value34, value36, value38, value3A;
    u8 slot, pad3D[3];
    f32 value40;
    s16 value44, value46;
    s32 word48;
} GameScaledDescriptor;
extern f32 D_800A5470, D_800A5474;
void func_15153F18(GameScaledDescriptor *, struct17 *, s32, u8, s32);

typedef struct { s32 index; u8 *actor; u8 identity; } GameEffectRefreshRequest;
typedef s32 (*GameEffectClassifier)(s32, u8 *);
typedef void (*GameEffectCallback)(u8 *, s32, s32);
typedef struct { GameEffectCallback callback; s32 count; } GameEffectEntry;
s32 func_15141C0C(u8 *actor);
s32 func_1510F8CC(s32);
s32 func_15141CC0(s32 context);
void func_15141E38(u8 *actor, s32 index);
s32 func_1514ECE0(u8 *, s16, u8 **);
s32 func_1514EC1C(s32, s32, s32);

typedef struct {
    u32 unk0;
    u8 unk4, pad5;
    u16 unk6, unk8;
    u8 unkA, unkB;
} GameTextureSource;
extern s32 D_800DD1B0, D_800DD208, D_800DD20C, D_800DD210;
extern u8 *D_800DD214;
extern s32 D_800BE9F0;
extern u8 D_800BE616;
s32 func_15094FE8(s32, GameTextureSource *, s32, u8 *, s32, s32, s32, s32, s32, s32, s32);

extern s32 D_800915B0, D_80091514;
extern s32 D_80091564[];
extern GameTextureSource D_80090B60[];

extern volatile s32 D_800DCA00;
extern u8 *D_800DCA04;
extern f32 D_800DCA08, D_800DCA0C, D_800DCA10;

typedef struct {
    s16 x, y, z, radius, height, width;
    f32 valueC, value10;
    u8 value14, flags, value16, value17;
    s32 word18, word1C, word20;
    u8 pad24[0x10];
} GameQueryRecord;
extern s32 D_800D3094;
extern GameQueryRecord *D_800D3098;
void func_15143D18(s32 *, s32 *, s32, s32);

typedef struct {
    u8 kind, pad1;
    s16 duration;
    u8 count, mode;
    s8 index;
    u8 pad7;
} GameGatedPacket;
s32 func_150A29C8(s32, s32);
void *func_151D8868(void *, s32, s32, s32);

typedef struct { u8 count; u8 pad1[11]; } GameCursorLimit;
extern GameCursorLimit D_80090B64[];
extern s32 D_800BE9E4;

extern s32 D_800D9D10[];
extern s32 D_800BE628;
extern f32 D_800A56B0, D_800D9B20;
void func_150A7A00(f32 matrix[4][4], f32 x, f32 y, f32 z, f32 *outX, f32 *outY, f32 *outZ, f32 *outW);

/* Generated placeholder declarations. */
void func_15141A7C(u8 *actor, s32 context);
s32 func_15141C0C(u8 *actor);
s32 func_15141CC0(s32 context);
void func_15141E38(u8 *actor, s32 index);
void func_15141F78(u8 slot, u8 *source, f32 scale, u8 tag, f32 *position, u8 mode);
void func_15142180(u8 slot, struct17 *source, s32 word, f32 width, f32 height);
void func_151424F4(Mtx *output, f32 row0, f32 row1, f32 rx, f32 ry, f32 rz,
    f32 cx, f32 cy, f32 cz, f32 tx, f32 ty, f32 tz);
s32 func_15142600();
void func_15142838(Mtx *output, f32 row0, f32 row1, f32 rx, f32 ry, f32 rz,
    f32 tx, f32 ty, f32 tz);
Gfx *func_15142E24(Gfx *output, GameTextureSource *source, s32 packed, s32 width,
    s32 height, s32 value, s32 index, u8 kind, u8 *attachment, u8 *sync, s32 flags);
s32 func_1514306C(GameTextureSource *source, s32 index, s32 subindex, u8 kind);
void func_15143134(f32 *point, f32 *output, u8 *matrix);
s32 func_151432BC();
GameQueryRecord *func_151438D8(s32 start, s32 end, u16 flags, GameQueryRecord *query);
u8 func_15143E94(s32 command, s32 flags);
s32 func_1514401C(u8 index, s32 *velocity, s32 *position, u8 flags);
void func_151441A4(s16 *out0, s16 *out1, s16 *out2, s16 *out3,
    u8 input0, u8 input1, u8 input2, u8 input3,
    u8 direct0, u8 direct1, u8 direct2, u8 direct3, u8 scale, u8 mode);
void func_151442FC(s16 *out0, s16 *out1, s16 *out2, s16 *out3,
    u8 input0, u8 input1, u8 input2, u8 input3,
    u8 direct0, u8 direct1, u8 direct2, u8 direct3, u8 scale, u8 mode);
s32 func_15144CEC(struct17 *arg0, f32 *arg1, f32 *arg2,
    f32 *arg3, f32 *arg4, volatile u8 arg5);
s32 func_15144E80();
s32 func_151451F0(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, f32 arg4, struct17 *arg5, struct17 *arg6, f32 *arg7, f32 *arg8);
s32 func_151452C4(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, struct17 *arg4, struct17 *arg5, f32 *arg6, f32 *arg7);
s32 func_15145740();
void func_1515C1A0(struct127 *, struct17 *, f32 *, f32 *);
s32 func_15145AD8(struct17 *arg0, struct17 *arg1, struct127 *arg2,
    struct17 *arg3, struct17 *arg4, f32 *arg5, f32 *arg6, struct17 *arg7);
s32 func_15145EA4();
s32 func_15146078();
s32 func_151462C8();
s32 func_1514654C();
/* End generated placeholder declarations. */

extern u8 D_800C3E90;
extern s16 D_800DD1C8;
extern s16 D_800DD1CA;
extern s16 D_800DD1CC;
extern s16 D_800DD1CE;
extern s16 D_800DD204;
extern s16 D_800DD206;
extern s16 D_800DD1C0;
extern s16 D_800DD1C2;
extern s16 D_800DD1C4;
extern s16 D_800DD1C6;
extern u32 D_800DD1FC;
extern u32 D_800DD200;

typedef struct {
    s32 words[6];
} SixWordBlock;

extern SixWordBlock D_800A5200;
extern f32 D_800A56A0;

s32 func_150A2AEC(s32 arg0, s32 arg1, s32 *arg2);
s32 func_1514563C(struct17 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 *arg4);
void func_150A7960(f32 mtx[4][4], f32 arg1, f32 arg2, f32 arg3, f32 *arg4, f32 *arg5, f32 *arg6);


void func_15141970(struct37 *arg0) {
    func_1514EDF0(arg0, arg0->unk2C);
}

void func_15141990(void *arg0) {
    func_15141970(arg0);
}

void func_151419B0(void *arg0) {
    func_15141970(arg0);
}

void func_151419D0(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *dst = arg0 + 0x28;
    s32 current;
    s32 source;

    if (arg2 == 0) {
        source = *(s32 *)arg1;
        if ((source == *(s32 *)(dst + 4)) || (dst[8] == arg1[4])) {
            func_1516972C(arg0);
        }
    } else if (arg2 == 0x2D) {
        current = *(s32 *)(dst + 4);
        source = *(s32 *)arg1;
        if (source == current) {
            *(s32 *)(dst + 4) = *(s32 *)(arg1 + 4);
            dst[8] = arg1[9];
        } else if (*(s32 *)(arg1 + 4) == current) {
            *(s32 *)(dst + 4) = source;
            dst[8] = arg1[8];
        }
    }
}
/* Matched with closed register, scheduling and private cursor guards. */
void func_15141A7C(u8 *actor, s32 context) {
    s32 category;
    s32 selected;
    u8 *node;
    u8 *record;
    if (D_800BE616 == 0) {
        category = func_15141C0C(actor);
        if (((GameEffectClassifier *)D_8008A084)[category] != NULL) {
            {
                s32 classified = func_15141CC0(func_1510F8CC(*(s32 *)(actor + 0x184)));
                selected = ((GameEffectClassifier *)D_8008A084)[category](classified, actor);
            }
            if ((selected != -1) && (((GameEffectEntry *)D_8008A0B4)[selected].callback != NULL)) {
                if (((GameEffectEntry *)D_8008A0B4)[selected].count > 0) {
                    func_15141E38(actor, selected);
                } else {
                    ((GameEffectEntry *)D_8008A0B4)[selected].callback(actor, context, 0);
                }
            }
        }
        node = *(u8 **)(actor + 0x2F4);
        while (func_1514ECE0(node, 0x1A, &node)) {
            record = *(u8 **)(node + 0x10);
            if (((GameEffectEntry *)D_8008A0B4)[*(volatile s32 *)(record + 0x28)].callback != NULL) {
                ((GameEffectEntry *)D_8008A0B4)[*(volatile s32 *)(record + 0x28)].callback(actor, context, *(s16 *)(record + 0xE));
            }
            *(u8 *volatile *)&node = *(u8 **)(node + 0x14);
        }
    }
}
/* Direct C; the owner rodata anchor retains the original switch pool. */
s32 func_15141C0C(u8 *actor) {
    s32 identity = actor[4];
    switch (identity) {
        case 0x79:
            return 10;
        case 0x21:
            return 9;
        case 0x7B:
            return 8;
        case 0x0:
        case 0x1:
        case 0x2:
        case 0x3:
        case 0x4:
        case 0x96:
            return 0;
        case 0x10:
        case 0x91:
            return 1;
        case 0x2B:
            return 2;
        case 0x54:
            return 5;
        case 0x36:
        case 0x53:
        case 0xA5:
            return 6;
        case 0x58:
            return 7;
        case 0x45:
            return 3;
        case 0x4B:
            return 4;
    }
    return 11;
}
/* Direct C; its switch follows the actor tables in the same anchored pool. */
s32 func_15141CC0(s32 context) {
    s32 world = D_800BE9F0;
    if (world == 47) {
        return 6;
    }
    if (world == 66) {
        return 7;
    }
    if (world == 39) {
        return 8;
    }
    if (world == 25) {
        return 5;
    }
    switch (context) {
        case 10:
            return 0;
        case 7:
            return 2;
        case 11:
            return 1;
        case 15:
            return 3;
        case 2:
        case 8:
        case 12:
            if (world == 2) {
                return 7;
            }
            return 4;
        case 5:
            if (world == 20) {
                return 5;
            }
            return 9;
        case 0:
            return 9;
    }
    return 9;
}
void func_15141DA4(void *arg0, s32 arg1, s32 arg2) {
    if ((arg1 < 12) && (arg1 >= 0) &&
        (arg2 < 20) && (arg2 >= 0) &&
        (D_800BE616 == 0) &&
        (D_8008A084[arg1] != 0) && (arg2 != -1)) {
        if ((D_8008A0B4[arg2].unk0 != 0) && (D_8008A0B4[arg2].unk4 > 0)) {
            func_15141E38(arg0, arg2);
        }
    }
}
/* Matched with closed register/scheduling and private request/cursor guards. */
void func_15141E38(u8 *actor, s32 index) {
    u8 *created;
    u8 *node;
    u8 *matched = NULL;
    u8 *record;
    GameEffectRefreshRequest request;
    node = *(u8 **)(actor + 0x2F4);
    while (func_1514ECE0(node, 0x1A, &node)) {
        record = *(u8 **)(node + 0x10);
        if (*(s32 *)(record + 0x28) == index) {
            matched = node;
            *(s16 *)(record + 0xE) = D_8008A0B4[index].unk4;
        }
        *(u8 *volatile *)&node = *(u8 **)(node + 0x14);
    }
    if (matched == NULL) {
        request.index = index;
        request.actor = actor;
        request.identity = actor[0x3B];
        created = (u8 *)func_15149130((s16)D_8008A0B4[index].unk4,
            -1, -1, -1, 1, 50, (struct37 *)12, 255, 1);
        if (created != NULL) {
            memcpy(created + 0x28, &request, 12);
            func_1514EC1C((s32)created, (s32)actor, 0x1A);
        }
    }
}
void func_15141F78(u8 slot, u8 *source, f32 scale, u8 tag, f32 *position, u8 mode) {
    GameRandomDescriptor descriptor;
    f32 range;
    s32 enabled;
    descriptor.slot = slot;
    descriptor.kind = 0;
    descriptor.flags = 0x6F701;
    descriptor.lifetime = (u32)func_150ADA20() % 61U + 100;
    descriptor.zero8 = 0;
    descriptor.zeroC = 0;
    descriptor.random = (func_150ADA20() & 0x7F) + 128;
    descriptor.value11 = 0xFF;
    descriptor.value12 = 0xFF;
    descriptor.value13 = 0xFF;
    descriptor.value14 = 0xFF;
    descriptor.value15 = 0xFF;
    descriptor.effect = 0x3B0002;
    descriptor.zero16 = 0;
    descriptor.seven = 7;
    descriptor.value20 = 0xFF;
    descriptor.sourceWord = *(s32 *)(source + 0x18);
    descriptor.size = 0x28;
    descriptor.count = 6;
    range = (func_150ADA68() * 5.0f + 10.0f) * scale;
    if (mode == 2) {
        enabled = 1;
    } else {
        enabled = 0;
    }
    func_1513C650((s32)&descriptor, 0, 0, (s32)(source + 4),
        position[0], *(f32 *)source, position[2], range, range,
        tag, enabled, 3, 1, 0, 255, 1);
}

s32 func_151420F8(struct127 *arg0) {
    SixWordBlock tmp;

    tmp = D_800A5200;
    if (func_150A2AEC(((s32)arg0 - (s32)D_800CC2D0) /
                      (s32)sizeof(struct127), 6, tmp.words) == -1) {
        return 0;
    }
    return 1;
}
void func_15142180(u8 slot, struct17 *source, s32 word, f32 width, f32 height) {
    GameScaledDescriptor descriptor;
    descriptor.point = *source;
    descriptor.value14 = 2.5f * width;
    descriptor.value18 = 2 * width;
    descriptor.value1C = D_800A5470;
    descriptor.value20 = D_800A5474;
    descriptor.value2C = 3;
    descriptor.value2E = 3;
    descriptor.value2 = 255;
    descriptor.value4 = -25;
    descriptor.value6 = 10;
    descriptor.value30 = 3;
    descriptor.value24 = 3.0f * height;
    descriptor.value28 = 3.5f * height;
    descriptor.value0 = 0;
    descriptor.value32 = 1;
    descriptor.value34 = 9;
    descriptor.value36 = 15;
    descriptor.value38 = 180;
    descriptor.value3A = 75;
    descriptor.value44 = 12;
    descriptor.value46 = 21;
    descriptor.value40 = 0.0f;
    descriptor.word48 = word;
    descriptor.slot = slot;
    func_15153F18(&descriptor, &descriptor.point, 0, 255, 1);
}
s32 func_151422C0(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return (arg3 + arg2) >> 1;
}

s32 func_151422DC(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6) {
    return arg4;
}

s32 func_151422F8(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return arg4;
}

void func_15142314(u8 *arg0, s32 arg1, f32 *arg2) {
    u8 *ptr = arg0 + (arg1 << 6);
    f32 scale = 1.0f / 65536.0f;

    if (D_800C3E90 != 0) {
        arg2[0] = (f32)(((*(s16 *)(ptr + 0x18)) << 16) + *(s16 *)(ptr + 0x38)) * scale;
        arg2[1] = (f32)(((*(s16 *)(ptr + 0x1A)) << 16) + *(s16 *)(ptr + 0x3A)) * scale;
        arg2[2] = (f32)(((*(s16 *)(ptr + 0x1C)) << 16) + *(s16 *)(ptr + 0x3C)) * scale;
    } else {
        arg2[0] = *(f32 *)(ptr + 0x30);
        arg2[1] = *(f32 *)(ptr + 0x34);
        arg2[2] = *(f32 *)(ptr + 0x38);
    }
}
f32 func_151423D8(u8 arg0) {
    s32 idx;
    s32 quadrant;

    if (arg0 & 0x40) {
        idx = 0x40 - (arg0 & 0x3F);
    } else {
        idx = arg0 & 0x3F;
    }

    quadrant = arg0 & 0xC0;
    if ((quadrant == 0) || (quadrant == 0xC0)) {
        return D_8009A220[idx];
    }
    return -D_8009A220[idx];
}
void *func_15142444(u8 arg0, u8 *arg1) {
    u8 *found;

    if (arg0 == 0xFF) {
        if (*(s32 *)(arg1 + 0x1D4) != 0) {
            return arg1;
        }
        return NULL;
    }

    if ((arg1 != NULL) && (*(s32 *)arg1 != 0) && (arg0 == arg1[0x3B])) {
        if (*(s32 *)(arg1 + 0x1D4) != 0) {
            return arg1;
        }
        return NULL;
    }

    found = (u8 *)func_15083E90(arg0);
    if (found == NULL) {
        return NULL;
    }
    if (*(s32 *)(found + 0x1D4) == 0) {
        return NULL;
    }
    return found;
}
void func_151424F4(Mtx *output, f32 row0, f32 row1, f32 rx, f32 ry, f32 rz,
    f32 cx, f32 cy, f32 cz, f32 tx, f32 ty, f32 tz) {
    f32 matrix[4][4];
    func_150A8050(matrix, rx, ry, rz);
    matrix[3][0] = tx;
    matrix[3][1] = ty;
    matrix[3][2] = tz;
    matrix[0][0] *= cx * row0;
    matrix[0][1] *= cy * row0;
    matrix[0][2] *= cz * row0;
    matrix[1][0] *= cx * row1;
    matrix[1][1] *= cy * row1;
    matrix[1][2] *= cz * row1;
    matrix[2][0] *= cx * row0;
    matrix[2][1] *= cy * row0;
    matrix[2][2] *= cz * row0;
    guMtxF2L(matrix, output);
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15142600.s. */
s32 func_15142600() {
    return 0;
}
void func_15142838(Mtx *output, f32 row0, f32 row1, f32 rx, f32 ry, f32 rz,
    f32 tx, f32 ty, f32 tz) {
    f32 matrix[4][4];
    func_150A8050(matrix, rx, ry, rz);
    matrix[3][0] = tx;
    matrix[3][1] = ty;
    matrix[3][2] = tz;
    matrix[0][0] *= row0;
    matrix[0][1] *= row0;
    matrix[0][2] *= row0;
    matrix[1][0] *= row1;
    matrix[1][1] *= row1;
    matrix[1][2] *= row1;
    matrix[2][0] *= row0;
    matrix[2][1] *= row0;
    matrix[2][2] *= row0;
    guMtxF2L(matrix, output);
}
void func_15142914(f32 *arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 arg7, f32 arg8) {
    func_150A8050((f32 (*)[4])arg0, arg3, arg4, arg5);

    arg0[12] = arg6;
    arg0[13] = arg7;
    arg0[14] = arg8;

    arg0[0] *= arg1;
    arg0[1] *= arg1;
    arg0[2] *= arg1;
    arg0[4] *= arg2;
    arg0[5] *= arg2;
    arg0[6] *= arg2;
    arg0[8] *= arg1;
    arg0[9] *= arg1;
    arg0[10] *= arg1;
}

void func_151429E0(u8 arg0, u8 *arg1, u8 *arg2, u8 *arg3) {
    u8 *tmp = &D_8008A160[((func_150ADA20() & 3) * 3) + (arg0 * 12)];

    *arg1 = tmp[0];
    *arg2 = tmp[1];
    *arg3 = tmp[2];
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_15142A5C(s32 *arg0) {
    s32 *p = *(s32**)((u8*)arg0 + 0x2D0);
    s32 v0 = 0;
    if (*(s16*)((u8*)p + 0x3C) > 0) {
        return 1;
    }
    return v0;
}
f32 func_15142A80(f32 arg0) {
    return (1.0f - arg0) * (arg0 - 2.0f) * arg0 * D_800A5624;
}
f32 func_15142AC0(f32 arg0) {
    return (arg0 + 1.0f) * (arg0 - 1.0f) * (arg0 - 2.0f) * 0.5f;
}
f32 func_15142B04(f32 arg0) {
    return (2.0f - arg0) * (arg0 + 1.0f) * arg0 * 0.5f;
}
f32 func_15142B44(f32 arg0) {
    return (arg0 + 1.0f) * (arg0 - 1.0f) * arg0 * D_800A5628;
}
Gfx *func_15142B7C(Gfx *arg0, u32 arg1, u32 arg2) {
    if (((~D_800DD200) & arg2) != 0) {
        gSPClearGeometryMode(arg0++, arg2);
        D_800DD200 |= arg2;
    }

    if (((~D_800DD1FC) & arg1) != 0) {
        gSPSetGeometryMode(arg0++, arg1);
        D_800DD1FC |= arg1;
    }
    return arg0;
}

Gfx *func_15142C10(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, u8 *arg5) {
    if ((arg1 == D_800DD1C8) && (arg2 == D_800DD1CA) && (arg3 == D_800DD1CC) && (arg4 == D_800DD1CE)) {
        return arg0;
    }

    if (*arg5 == 1) {
        gDPPipeSync(arg0++);
        *arg5 = 0;
    }

    arg0->words.w0 = 0xFB000000;
    arg0->words.w1 = ((arg1 & 0xFF) << 24) | ((arg2 & 0xFF) << 16) | ((arg3 & 0xFF) << 8) | (arg4 & 0xFF);
    arg0++;

    D_800DD1C8 = arg1;
    D_800DD1CA = arg2;
    D_800DD1CC = arg3;
    D_800DD1CE = arg4;
    return arg0;
}

Gfx *func_15142CF0(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6, u8 *arg7) {
    if ((arg1 == D_800DD204) && (arg2 == D_800DD206) && (arg3 == D_800DD1C0) &&
        (arg4 == D_800DD1C2) && (arg5 == D_800DD1C4) && (arg6 == D_800DD1C6)) {
        return arg0;
    }

    if (*arg7 == 1) {
        gDPPipeSync(arg0++);
        *arg7 = 0;
    }

    arg0->words.w0 = 0xFA000000 | ((arg1 & 0xFF) << 8) | (arg2 & 0xFF);
    arg0->words.w1 = ((arg3 & 0xFF) << 24) | ((arg4 & 0xFF) << 16) | ((arg5 & 0xFF) << 8) | (arg6 & 0xFF);
    arg0++;

    D_800DD204 = arg1;
    D_800DD206 = arg2;
    D_800DD1C0 = arg3;
    D_800DD1C2 = arg4;
    D_800DD1C4 = arg5;
    D_800DD1C6 = arg6;
    return arg0;
}
Gfx *func_15142E24(Gfx *output, GameTextureSource *source, s32 packed, s32 width,
    s32 height, s32 value, s32 index, u8 kind, u8 *attachment, u8 *sync, s32 flags) {
    s32 image = func_1514306C(source, index, packed >> 16, kind);
    if (image != D_800DD1B0 || width != D_800DD208 ||
        height != D_800DD20C || value != D_800DD210 || attachment != D_800DD214) {
        if (*sync == 1) {
            *sync = 0;
        }
        if (D_800BE9F0 == 0x18 || D_800BE9F0 == 0x13 || D_800BE9F0 == 6 ||
            D_800BE9F0 == 0x3B || D_800BE9F0 == 2 || D_800BE616 != 0) {
            flags = 3;
        }
        output = (Gfx *)func_15094FE8((s32)output, source, packed >> 8, attachment, 0, 0, 0,
            width, height, value, flags);
        D_800DD1B0 = image;
        D_800DD208 = width;
        D_800DD20C = height;
        D_800DD210 = value;
        *(u8 *volatile *)&D_800DD214 = *(u8 *volatile *)&D_800DD214;
    }
    return output;
}
Gfx *func_15142FBC(Gfx *arg0, u32 arg1, u32 arg2, u8 *arg3) {
    Gfx *cmd;

    if ((arg1 != D_800DD218) || (arg2 != D_800DD21C)) {
        if (*arg3 == 1) {
            gDPPipeSync(arg0++);
            *arg3 = 0;
        }

        cmd = arg0++;
        cmd->words.w0 = 0xEF000000 | ((arg1 | 0xF) & 0xFFFFFF);
        cmd->words.w1 = arg2;
        D_800DD218 = arg1;
        D_800DD21C = arg2;
    }
    return arg0;
}
s16 func_15143044(u8 arg0, s32 arg1) {
    return (s16)(0x7FFF - arg0);
}
s32 func_1514306C(GameTextureSource *source, s32 index, s32 subindex, u8 kind) {
    s32 result;
    switch (kind) {
        case 4:
            result = D_800915B0;
            break;
        case 3:
            result = D_80091514;
            break;
        case 1:
            result = 0;
            break;
        case 2:
            result = D_80091564[index];
            break;
        case 5:
            result = index;
            break;
        case 6:
            index = source->unk0;
            if ((u32)index >= 0x10000000U) {
                result = ((s32 *)source->unk0)[subindex];
            } else {
                result = index;
            }
            break;
        default:
            result = ((s32 *)D_80090B60[index].unk0)[subindex];
            break;
    }
    return result;
}
void func_15143134(f32 *point, f32 *output, u8 *matrix) {
    f32 converted[4][4];
    D_800DCA00 = 1;
    if (point != NULL && (point[0] != 0.0f || point[1] != 0.0f || point[2] != 0.0f)) {
        D_800DCA00 = 2;
        D_800DCA08 = point[0];
        D_800DCA0C = point[1];
        D_800DCA10 = point[2];
        if (D_800C3E90 != 0) {
            D_800DCA00 = 3;
            D_800DCA04 = matrix;
            guMtxL2F(converted, (Mtx *)matrix);
            func_150A7960(converted, point[0], point[1], point[2],
                &output[0], &output[1], &output[2]);
            D_800DCA00 = 4;
            D_800DCA00 = 0;
            return;
        } else {
            D_800DCA00 = 5;
            D_800DCA04 = matrix;
            func_150A7960((f32 (*)[4])matrix, point[0], point[1], point[2],
                &output[0], &output[1], &output[2]);
            D_800DCA00 = 6;
        }
    } else {
        D_800DCA00 = 7;
        func_15142314(matrix, 0, output);
        D_800DCA00 = 8;
    }
    D_800DCA00 = 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151432BC.s. */
s32 func_151432BC() {
    return 0;
}
// void func_151432BC(struct208 *arg0, f32 *arg1, f32 *arg2, f32 *arg3, f32 *arg4) {
//     struct209 tmp;
//     f32 temp_f2;
//     f32 temp_f6;
//     f32 temp_ret;
//     s32 temp_t6;
//     u8 temp_a0;
//
//     temp_t6 = (arg0->unk15) & 3;
//     if (temp_t6 == 0) {
//         tmp.unk1B = func_150ADA20();
//         tmp.unk14 = func_151423D8((tmp.unk1B - 64) & 0xFF);
//         tmp.unk10 = func_151423D8(tmp.unk1B);
//         temp_ret = func_150ADA68();
//         temp_f2 = temp_ret * arg0->unk6;
//         *arg1 = (arg0->unk0 + (temp_f2 * tmp.unk10));
//         *arg2 = (arg0->unk4 - (temp_f2 * tmp.unk14));
//         *arg3 = (arg0->unk2 + arg0->unk8);
//         *arg4 = arg0->unk2;
//     } else if (temp_t6 != 1) {
//         if (temp_t6 == 2) {
//             tmp.unk2F = (u32) (arg0->unk10 * D_800A5644); // 0.7111111283302307
//             tmp.unk28 = func_151423D8((tmp.unk2F - 64));
//             tmp.unk24 = func_151423D8(tmp.unk2F);
//             tmp.unk20 = (func_150ADA68() * (2.0f * (f32) arg0->unk6)) + (f32) -(s32) arg0->unk6;
//             temp_f2 = (func_150ADA68() * (2.0f * (f32) arg0->unkA)) + (f32) -(s32) arg0->unkA;
//             temp_f6 = temp_f2 * tmp.unk24;
//             *arg1 = (arg0->unk0 + ((tmp.unk20 * tmp.unk24) + (temp_f2 * tmp.unk28)));
//             *arg2 = (arg0->unk4 + (temp_f6 - (tmp.unk20 * tmp.unk28)));
//             *arg3 = (arg0->unk2 + arg0->unk8);
//             *arg4 = arg0->unk2;
//         } else {
//             *arg1 = arg0->unk0;
//             *arg2 = arg0->unk4;
//             *arg3 = (arg0->unk2 + arg0->unk8);
//             *arg4 = (arg0->unk2 - arg0->unk8);
//         }
//     } else {
//         tmp.unkB = func_150ADA20();
//         tmp.unk4 = func_151423D8((tmp.unkB - 64));
//         tmp.unk0 = func_151423D8(tmp.unkB);
//         temp_ret = func_150ADA68();
//         temp_f2 = temp_ret * (f32) arg0->unk6;
//         *arg1 = (arg0->unk0 + (temp_f2 * tmp.unk0));
//         *arg2 = (arg0->unk4 - (temp_f2 * tmp.unk4));
//         *arg3 = (arg0->unk2 + arg0->unk8);
//         *arg4 = (arg0->unk2 - arg0->unk8);
//     }
// }


void func_151436B4(f32 arg0, f32 arg1, f32 arg2, vertex *arg3) {
    f32 cos0 = cosf(arg0);
    f32 sin0 = sinf(arg0);
    f32 cos1 = cosf(arg1);
    f32 sin1 = sinf(arg1);
    f32 temp = arg2 * cos1;

    arg3->x = temp * sin0;
    arg3->y = -arg2 * sin1;
    arg3->z = temp * cos0;
}
void func_1514373C(f32 arg0, f32 arg1, f32 *arg2, f32 *arg3) {
    f32 tmp = cosf(arg0);
    f32 sin0 = sinf(arg0);

    *arg2 = arg1 * sin0;
    *arg3 = arg1 * tmp;
}
// NON-MATCHING: only differs from us by the jal target address of the still-unmatched
// func_151423D8 (called 4 times here) - this function's own code is verified
// byte-identical otherwise.
void func_15143794(s16 arg0, s16 arg1, f32 arg2, vertex *arg3) {
    f32 sinArg0 = func_151423D8((u8) arg0);
    f32 sinArg0m = func_151423D8((u8) (arg0 - 0x40));
    f32 sinArg1 = func_151423D8((u8) arg1);
    f32 sinArg1m = func_151423D8((u8) (arg1 - 0x40));
    f32 temp = arg2 * sinArg1;

    arg3->x = temp * sinArg0m;
    arg3->y = -arg2 * sinArg1m;
    arg3->z = temp * sinArg0;
}
// NON-MATCHING: only differs from us by the jal target address of func_15143794
// (verified byte-identical above except for its own dependency on func_151423D8) -
// this function's own code is verified byte-identical otherwise.
void func_15143834(s16 arg0, s16 arg1, f32 arg2, vertex *arg3) {
    func_15143794(arg0, arg1, arg2, arg3);
}
void func_15143874(s16 arg0, f32 arg1, f32 *arg2, f32 *arg3) {
    f32 tmp = func_151423D8(arg0);
    u8 angle = arg0 - 0x40;
    f32 angleValue = func_151423D8(angle);

    *arg2 = arg1 * angleValue;
    *arg3 = arg1 * tmp;
}
GameQueryRecord *func_151438D8(s32 start, s32 end, u16 flags, GameQueryRecord *query) {
    s32 index;
    GameQueryRecord *result = NULL;
    u16 pass;
    u16 match;

    if (query == NULL) {
        return NULL;
    }
    func_15143D18(&start, &end, 0, D_800D3094);
    for (index = start; index < end; index++) {
        pass = 0;
        match = 0;
        if (flags & 0x1) {
            if (query->x == D_800D3098[index].x &&
                query->y == D_800D3098[index].y &&
                query->z == D_800D3098[index].z) {
                pass |= 0x1;
                match |= 0x1;
            }
        } else {
            pass |= 0x1;
        }
        if (flags & 0x2) {
            if (query->radius == D_800D3098[index].radius &&
                query->height == D_800D3098[index].height &&
                query->width == D_800D3098[index].width) {
                pass |= 0x2;
                match |= 0x2;
            }
        } else {
            pass |= 0x2;
        }
        if (flags & 0x4) {
            if (query->valueC == D_800D3098[index].valueC) {
                pass |= 0x4;
                match |= 0x4;
            }
        } else {
            pass |= 0x4;
        }
        if (flags & 0x8) {
            if (query->value10 == D_800D3098[index].value10) {
                pass |= 0x8;
                match |= 0x8;
            }
        } else {
            pass |= 0x8;
        }
        if (flags & 0x10) {
            if (query->value14 == D_800D3098[index].value14) {
                pass |= 0x10;
                match |= 0x10;
            }
        } else {
            pass |= 0x10;
        }
        if (flags & 0x20) {
            if (query->flags == (D_800D3098[index].flags >> 2)) {
                pass |= 0x20;
                match |= 0x20;
            }
        } else {
            pass |= 0x20;
        }
        if (flags & 0x40) {
            if (query->value16 == D_800D3098[index].value16) {
                pass |= 0x40;
                match |= 0x40;
            }
        } else {
            pass |= 0x40;
        }
        if (flags & 0x80) {
            if (query->value17 == D_800D3098[index].value17) {
                pass |= 0x80;
                match |= 0x80;
            }
        } else {
            pass |= 0x80;
        }
        if (flags & 0x100) {
            if (query->word18 == D_800D3098[index].word18) {
                pass |= 0x100;
                match |= 0x100;
            }
        } else {
            pass |= 0x100;
        }
        if (flags & 0x200) {
            if (query->word1C == D_800D3098[index].word1C) {
                pass |= 0x200;
                match |= 0x200;
            }
        } else {
            pass |= 0x200;
        }
        if (flags & 0x400) {
            if (query->word20 == D_800D3098[index].word20) {
                pass |= 0x400;
                match |= 0x400;
            }
        } else {
            pass |= 0x400;
        }
        if (flags & 0x1000) {
            if (pass == 0x7FF) {
                result = &D_800D3098[index];
            }
        } else if (match != 0) {
            result = &D_800D3098[index];
        }
    }
    return result;
}
void func_15143D18(s32 *arg0, s32 *arg1, s32 arg2, s32 arg3) {
    s32 value1;
    s32 value0;

    if (arg3 < arg2) {
        s32 tmp;
        s32 newArg3;

        tmp = arg2 ^ arg3;
        newArg3 = arg3 ^ tmp;
        arg3 = newArg3;
        arg2 = tmp ^ newArg3;
    }

    value1 = *arg1;
    value0 = *arg0;
    if (value1 < value0) {
        s32 tmp;

        tmp = value0 ^ value1;
        *arg0 = tmp;
        value1 = *arg1 ^ tmp;
        *arg1 = value1;
        value0 = *arg0 ^ value1;
        *arg0 = value0;
    }

    if (value0 < arg2) {
        *arg0 = arg2;
    }
    if (arg3 < *arg1) {
        *arg1 = arg3;
    }
}
s32 func_15143DA8(s32 *volatile arg0, s32 arg1, s32 arg2) {
    s32 *ptr;
    s32 value;

    ptr = arg0;
    if (arg2 < arg1) {
        s32 tmp;
        s32 newArg2;

        tmp = arg1 ^ arg2;
        newArg2 = arg2 ^ tmp;
        arg2 = newArg2;
        arg1 = tmp ^ newArg2;
    }

    value = *ptr;
    if (value < arg1) {
        *ptr = arg1;
        return 1;
    }

    if (arg2 < value) {
        *arg0 = arg2;
        return 2;
    }

    return 0;
}

s32 func_15143E08(struct127 *arg0) {
    return (((s32) arg0->unk7A >> 8) + 64) & 0xFF;
}

s16 func_15143E24(struct127 *arg0) {
    struct126 *temp = arg0->unk31C;

    if (temp != NULL) {
        return (arg0->unk7A - temp->unk12) >> 8;
    }
    return arg0->unk7A >> 8;
}
f32 func_15143E64(f32 *arg0) {
    f32 x = arg0[0];
    f32 y = arg0[1];
    f32 z = arg0[2];
    return sqrtf(x * x + y * y + z * z);
}
/* Submission copies all eight bytes; preserve the untouched packet padding. */
u8 func_15143E94(s32 command, s32 flags) {
    u8 result = 0;
    s8 count;
    s8 index;
    s16 active;
    s16 ready;
    GameGatedPacket packet;

    count = (u32)D_80082FA0 + 1;
    index = 0;
    active = 0;
    while (active == 0 && index < count) {
        if (D_800CC2D0[index].health != 0) {
            active = 1;
        } else {
            index++;
        }
    }
    if (active != 0) {
        index = 0;
        ready = 0;
        while (ready == 0 && index < count) {
            if (func_150A29C8(index, flags) == 0) {
                ready = 1;
            } else {
                index++;
            }
        }
        if (ready != 0) {
            func_1512D748(&D_800DBFF0[D_800BE9E8], command, 1);
            packet.kind = 1;
            packet.duration = (func_150ADA20() & 0xF) + 20;
            packet.count = (func_150ADA20() & 3) + 4;
            packet.index = -1;
            packet.mode = 1;
            func_151D8868(&packet, 0, 255, 0);
            result = 1;
        }
    }
    return result;
}
s32 func_1514401C(u8 index, s32 *velocity, s32 *position, u8 flags) {
    s32 result = 0;
    s32 limit;
    s32 value;

    limit = (D_80090B64[index].count << 16) - 1;
    *position = (u32)*position + (u32)*velocity * (u32)D_800BE9E4;
    value = *position;
    if (value > limit) {
        if (flags & 1) {
            result = 1;
        } else if (flags & 2) {
            *velocity = 0;
            *position = limit;
        } else if (flags & 4) {
            *position = limit - value % limit;
            *velocity = 0U - (u32)*velocity;
        } else {
            do {
                *position = (u32)value - (u32)limit;
                value = *position;
            } while (value > limit);
        }
    } else if (value < 0) {
        if (!(flags & 8)) {
            if (flags & 16) {
                *velocity = 0;
                *position = 0;
            } else if (flags & 4) {
                *position = (s32)(0U - (u32)value) % limit;
                *velocity = 0U - (u32)*velocity;
            } else {
                do {
                    *position = (u32)value + (u32)limit;
                    value = *position;
                } while (value < 0);
            }
        }
    }
    return result;
}
void func_151441A4(s16 *out0, s16 *out1, s16 *out2, s16 *out3,
    u8 input0, u8 input1, u8 input2, u8 input3,
    u8 direct0, u8 direct1, u8 direct2, u8 direct3, u8 scale, u8 mode) {
    switch (mode) {
    case 2:
        *out0 = direct0;
        *out1 = direct1;
        *out2 = direct2;
        *out3 = direct3;
        break;
    case 0:
        *out3 = 0;
        *out0 = *out1 = *out2 = *out3;
        break;
    case 1:
        *out2 = 0;
        *out0 = *out1 = *out2;
        *out3 = direct3;
        break;
    case 3:
        *out0 = (input0 * scale) >> 8;
        *out1 = (input1 * scale) >> 8;
        *out2 = (input2 * scale) >> 8;
        *out3 = 0;
        break;
    case 4:
        *out0 = (input0 * scale) >> 8;
        *out1 = (input1 * scale) >> 8;
        *out2 = (input2 * scale) >> 8;
        *out3 = 0;
        break;
    default:
        *out0 = (input0 * scale) >> 8;
        *out1 = (input1 * scale) >> 8;
        *out2 = (input2 * scale) >> 8;
        *out3 = 0;
        break;
    }
}
void func_151442FC(s16 *out0, s16 *out1, s16 *out2, s16 *out3,
    u8 input0, u8 input1, u8 input2, u8 input3,
    u8 direct0, u8 direct1, u8 direct2, u8 direct3, u8 scale, u8 mode) {
    switch (mode) {
    case 2:
    case 3:
        *out0 = input0;
        *out1 = input1;
        *out2 = input2;
        *out3 = input3;
        break;
    case 13:
        *out0 = input0;
        *out1 = input1;
        *out2 = input2;
        *out3 = 0;
        break;
    case 0:
        *out3 = 0;
        *out0 = *out1 = *out2 = *out3;
        break;
    case 1:
        *out0 = *out1 = *out2 = scale;
        *out3 = 0;
        break;
    case 7:
    case 12:
        *out2 = 0;
        *out0 = *out1 = *out2;
        *out3 = direct3;
        break;
    case 8:
        *out2 = 0;
        *out0 = *out1 = *out2;
        *out3 = input3;
        break;
    case 4:
        *out0 = *out1 = *out2 = scale;
        *out3 = (input3 * direct3) >> 8;
        break;
    case 5:
        *out0 = *out1 = *out2 = scale;
        *out3 = (input3 * direct3) >> 8;
        break;
    case 6:
        *out0 = input0;
        *out1 = input1;
        *out2 = input2;
        *out3 = direct3;
        break;
    case 10:
        *out0 = direct0;
        *out1 = direct1;
        *out2 = direct2;
        *out3 = direct3;
        break;
    case 11:
        *out0 = direct0;
        *out1 = direct1;
        *out2 = direct2;
        *out3 = input3;
        break;
    case 9:
        *out0 = *out1 = *out2 = scale;
        *out3 = direct3;
        break;
    default:
        *out0 = *out1 = *out2 = scale;
        *out3 = (input3 * direct3) >> 8;
        break;
    }
}
u32 func_151444DC(s32 arg0, s32 arg1, s32 arg2) {
    s32 step;

    if (arg1 < arg0) {
        step = arg1 - arg2 + 1;
        do {
            arg0 -= step;
        } while (arg1 < arg0);
    }

    if (arg0 < arg2) {
        step = arg1 - arg2 + 1;
        do {
            arg0 += step;
        } while (arg0 < arg2);
    }

    return arg0;
}
f32 func_15144528(f32 arg0, f32 arg1, f32 arg2) {
    f32 step = arg1 - arg2;

    while (arg1 < arg0) {
        arg0 -= step;
    }

    while (arg0 < arg2) {
        arg0 += step;
    }

    return arg0;
}
f32 func_15144598(struct134 *arg0) {
    f32 ret;
    u8 *record = (u8 *)arg0;

    switch (record[0x15] & 3) {
        case 2:
            ret = *(s16 *)(record + 0xA) * *(s16 *)(record + 6) * 4.0f;
            break;
        case 0:
        case 1:
            ret = *(s16 *)(record + 6) * *(s16 *)(record + 6) * D_800A5694;
            break;
        default:
            ret = 1.0f;
            break;
    }

    return ret;
}
f32 func_1514462C(struct134 *arg0) {
    f32 ret;
    u8 *record = (u8 *)arg0;

    switch (record[0x15] & 3) {
        case 2:
            /* Wrap the integer product before converting it to float. */
            ret = (s32)((u32)*(s16 *)(record + 8) * (u32)*(s16 *)(record + 0xA) * (u32)*(s16 *)(record + 6));
            break;
        case 0:
            ret = *(s16 *)(record + 8) * (*(s16 *)(record + 6) * *(s16 *)(record + 6) * D_800A5698);
            break;
        case 1: {
            f32 radius = *(s16 *)(record + 6);
            ret = radius * D_800A569C * radius * radius;
            break;
        }
        default:
            ret = 1.0f;
            break;
    }

    return ret;
}
void func_1514470C(void *descriptor, void *output) {
    u8 *record = descriptor;
    f32 *position = output;
    f32 width = *(s16 *)(record + 6);
    f32 height = *(s16 *)(record + 8);
    f32 depth = *(s16 *)(record + 0xA);
    f32 coefficient24 = *(f32 *)(record + 0x24);
    f32 coefficient28 = *(f32 *)(record + 0x28);
    f32 coefficient2C = *(f32 *)(record + 0x2C);
    f32 coefficient30 = *(f32 *)(record + 0x30);
    f32 radius;
    f32 x;
    f32 y;
    f32 z;
    f32 transformed;
    f32 angle0;
    f32 angle1;
    f32 period;
    u8 angle;
    vertex point;

    switch (record[0x15] & 3) {
        case 0:
            radius = func_150ADA68() * width;
            angle = func_150ADA20();
            x = func_151423D8((u8)(angle - 0x40)) * radius;
            y = func_150ADA68() * height;
            z = func_151423D8(angle) * radius;
            break;
        case 2:
            x = func_150ADA68() * (width + width) - width;
            y = func_150ADA68() * height;
            z = func_150ADA68() * (depth + depth) - depth;
            break;
        case 1:
            angle0 = func_150ADA68();
            angle1 = func_150ADA68();
            radius = func_150ADA68();
            period = D_800A56A0;
            func_151436B4(angle0 * period, angle1 * period, radius * width, &point);
            position[0] = *(s16 *)(record + 0) + point.x;
            position[1] = *(s16 *)(record + 2) + point.y;
            position[2] = *(s16 *)(record + 4) + point.z;
            return;
        default:
            position[0] = *(s16 *)(record + 0);
            position[1] = *(s16 *)(record + 2);
            position[2] = *(s16 *)(record + 4);
            return;
    }

    transformed = y * coefficient24 + z * coefficient28;
    position[0] = *(s16 *)(record + 0) + (x * coefficient30 + transformed * coefficient2C);
    position[1] = *(s16 *)(record + 2) + (y * coefficient28 - z * coefficient24);
    position[2] = *(s16 *)(record + 4) + (transformed * coefficient30 - x * coefficient2C);
}
// Matched with guarded commutative-add normalization.
f32 func_15144A74(f32 *arg0, f32 *arg1) {
    return arg0[0] * arg1[0] + arg0[1] * arg1[1] + arg1[2] * arg0[2];
}
f32 func_15144AA8(s32 arg0) {
    f32 ret = D_800DBFF0[arg0].unk380;

    while (ret > 360.0f) {
        ret -= 360.0f;
    }

    while (ret < 0.0f) {
        ret += 360.0f;
    }

    return ret;
}
f32 *func_15144B34(s32 arg0) {
    return &D_800DBFF0[arg0].unk2F8;
}
f32 func_15144B68(f32 arg0) {
    f32 ret = arg0;

    while (D_800A56A4 < ret) {
        ret -= D_800A56A4;
    }

    while (ret < 0.0f) {
        ret += D_800A56A4;
    }

    return ret;
}

f32 func_15144BC8(f32 arg0) {
    f32 ret = arg0;

    while (360.0f < ret) {
        ret -= 360.0f;
    }

    while (ret < 0.0f) {
        ret += 360.0f;
    }

    return ret;
}

s32 func_15144C2C(s16 arg0) {
    s16 tmp1 = arg0;

    while (tmp1 >= 256)
    {
        tmp1 -= 255;
    }
    while (tmp1 < 0)
    {
        tmp1 += 255;
    }

    return tmp1;
}

f32 func_15144C8C(f32 arg0, f32 arg1) {
    f32 tmp;

    arg0 = func_15144B68(arg0);
    tmp = fabsf(arg0 - func_15144B68(arg1));
    if (D_800A56A8 < tmp) {
        tmp = D_800A56AC - tmp;
    }
    return tmp;
}
/* Note 1082: projection with optional outputs and live view/reciprocal reads. */
s32 func_15144CEC(struct17 *arg0, f32 *arg1, f32 *arg2, f32 *arg3, f32 *arg4, volatile u8 arg5) {
    f32 localZ;
    f32 localW;
    f32 localReciprocal;
    f32 value;
    f32 yProduct;
    s32 offset;

    if (arg2 == NULL) {
        arg2 = &localZ;
    }
    if (arg3 == NULL) {
        arg3 = &localW;
    }
    offset = arg5;
    if (arg4 == NULL) {
        arg4 = &localReciprocal;
    }
    func_150A7A00((f32 (*)[4])((u8 *)D_800D9D10 + (offset << 6)),
                 arg0->unk0, arg0->unk4, arg0->unk8, arg1, arg1 + 1, arg2, arg3);
    value = *arg3;
    if (D_800A56B0 <= value || value <= D_800D9B20) {
        return 0;
    }
    if (value != 0.0f) {
        *arg4 = 1.0f / value;
    } else {
        return 0;
    }
    offset = arg5 * 0x180;
    value = *arg4 * (arg1[0] * (((struct140 *)((u8 *)D_800BE628 + offset))->unkC + 5.0f))
        + ((struct140 *)((u8 *)D_800BE628 + offset))->unk34;
    yProduct = arg1[1] * (((struct140 *)((u8 *)D_800BE628 + offset))->unk10 + 5.0f);
    arg1[0] = value;
    arg1[1] = ((struct140 *)((u8 *)D_800BE628 + offset))->unk38 - *arg4 * yProduct;
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15144E80.s. */
/* Note 374: original surface splash construction and triangle basis. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_16EE20/func_15144E80.s")

void func_151450B4(struct17 *arg0, struct17 *arg1, struct17 *arg2) {
    arg2->unk0 = arg0->unk4 * arg1->unk8 - arg0->unk8 * arg1->unk4;
    arg2->unk4 = arg0->unk8 * arg1->unk0 - arg0->unk0 * arg1->unk8;
    arg2->unk8 = arg0->unk0 * arg1->unk4 - arg0->unk4 * arg1->unk0;
}

s32 func_15145128(struct17 *arg0, struct17 *arg1, f32 *arg2, f32 *arg3) {
    f32 local;
    f32 len;

    if (arg3 == NULL) {
        arg3 = &local;
    }

    len = (arg0->unk0 * arg0->unk0) + (arg0->unk4 * arg0->unk4) + (arg0->unk8 * arg0->unk8);
    if (len == 0.0f) {
        return 0;
    }

    if (arg2 != NULL) {
        *arg3 = 1.0f / (*arg2 = sqrtf(len));
    } else {
        *arg3 = 1.0f / sqrtf(len);
    }

    arg1->unk0 = *arg3 * arg0->unk0;
    arg1->unk4 = *arg3 * arg0->unk4;
    arg1->unk8 = *arg3 * arg0->unk8;
    return 1;
}
/* Note 1083: eight-argument forwarding with live sign/threshold acceptance. */
s32 func_151451F0(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, f32 arg4, struct17 *arg5, struct17 *arg6, f32 *arg7, f32 *arg8) {
    if (func_151452C4(arg0, arg1, arg2, arg3, arg5, arg6, arg7, arg8)) {
        if (*arg7 < 0.0f && *arg8 < 0.0f) {
            return 0;
        }
        if (*arg7 >= 0.0f && *arg8 < 0.0f) {
            return 1;
        }
        if (*arg7 < arg4) {
            return 1;
        } else {
            return 0;
        }
    } else {
        return 0;
    }
}
/* Note 1086: original private layout; checked FP/schedule guards only. */
s32 func_151452C4(struct17 *arg0, struct17 *arg1, struct17 *arg2,
    f32 arg3, struct17 *arg4, struct17 *arg5, f32 *arg6, f32 *arg7) {
    f32 x;
    f32 y;
    f32 z;
    union {struct17 point; f32 values[3];} direction;
    struct17 origin;
    f32 projection;
    f32 radiusSquared;
    f32 perpendicularSquared;
    f32 root;
    f32 first;
    f32 second;
    struct17 relative;

    x = arg2->unk0 - arg0->unk0;
    y = arg2->unk4 - arg0->unk4;
    z = arg2->unk8 - arg0->unk8;
    direction.point = *arg1;
    origin = *arg0;
    projection = x * direction.values[0] + y * direction.values[1] + z * direction.values[2];
    radiusSquared = arg3 * arg3;
    perpendicularSquared = x * x + y * y + z * z - projection * projection;
    if (radiusSquared < perpendicularSquared) {
        return 0;
    }
    root = sqrtf(radiusSquared - perpendicularSquared);
    if (projection < root) {
        root = -root;
    }
    first = projection - root;
    second = projection + root;
    arg4->unk0 = first * direction.values[0] + origin.unk0;
    arg4->unk4 = first * direction.values[1] + origin.unk4;
    arg4->unk8 = first * direction.values[2] + origin.unk8;
    *arg6 = first;
    arg5->unk0 = second * direction.values[0] + origin.unk0;
    arg5->unk4 = second * direction.values[1] + origin.unk4;
    arg5->unk8 = second * direction.values[2] + origin.unk8;
    *arg7 = second;
    relative.unk0 = arg4->unk0 - arg0->unk0;
    relative.unk4 = arg4->unk4 - arg0->unk4;
    relative.unk8 = arg4->unk8 - arg0->unk8;
    if (func_15144A74((f32 *)&relative, (f32 *)arg1) < 0.0f) {
        return 0;
    }
    return 1;
}
s32 func_151454BC(u8 arg0, f32 arg1, struct17 *arg2) {
    f32 tmp1;
    f32 tmp2;
    f32 tmp3;
    struct17 *temp_v0;

    temp_v0 = func_15144B34(arg0);
    tmp1 = arg2->unk0 - temp_v0->unk0;
    tmp2 = arg2->unk4 - temp_v0->unk4;
    tmp3 = arg2->unk8 - temp_v0->unk8;

    if ((arg1 * arg1) < ((tmp1 * tmp1) + (tmp2 * tmp2) + (tmp3 * tmp3))) {
        return 0;
    }
    return 1;
}

void func_15145548(struct17 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 *arg4) {
    f32 local;

    if (arg4 == NULL) {
        arg4 = &local;
    }

    if (func_1514563C(arg0, arg1, arg2, arg3, arg4) != 0) {
        if (*arg4 < 0.0f) {
            *arg3 = *arg0;
        } else if (*arg4 > 1.0f) {
            arg3->unk0 = arg0->unk0 + arg1->unk0;
            arg3->unk4 = arg0->unk4 + arg1->unk4;
            arg3->unk8 = arg0->unk8 + arg1->unk8;
        }
    } else {
        *arg3 = *arg0;
    }
}

s32 func_1514563C(struct17 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 *arg4) {
    f32 local;
    f32 mag_sq;
    f32 dot0;
    f32 dot1;
    f32 amount;

    if (arg4 == NULL) {
        arg4 = &local;
    }

    mag_sq = (arg1->unk0 * arg1->unk0) + (arg1->unk4 * arg1->unk4) + (arg1->unk8 * arg1->unk8);
    if (mag_sq == 0.0f) {
        return 0;
    }

    dot0 = (arg1->unk0 * arg0->unk0) + (arg1->unk4 * arg0->unk4) + (arg1->unk8 * arg0->unk8);
    dot1 = (arg1->unk0 * arg2->unk0) + (arg1->unk4 * arg2->unk4) + (arg1->unk8 * arg2->unk8);
    amount = (dot1 - dot0) / mag_sq;
    *arg4 = amount;

    arg3->unk0 = arg0->unk0 + (amount * arg1->unk0);
    arg3->unk4 = arg0->unk4 + (*arg4 * arg1->unk4);
    arg3->unk8 = arg0->unk8 + (*arg4 * arg1->unk8);
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15145740.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_16EE20/func_15145740.s")
// NON-MATCHING: 90% there
// void func_15145740(struct127 *arg0, struct17 *arg1, struct17 *arg2, struct17 *arg3, f32 arg4) {
//     struct194 tmp;
//     f32 temp_f6;
//     s16 phi_v1;
//     s16 phi_t0;
//
//     if ((arg0->unk4 == 0x96) && ((arg0->unk31C->unk7D != 0))) {
//         phi_t0 = arg0->unk7A + arg0->unk31C->unk80;
//     } else {
//         if (arg0->unk31C != 0) {
//             phi_t0 = arg0->unk7A - arg0->unk31C->unk12;
//         } else {
//             phi_t0 = arg0->unk7A;
//         }
//     }
//     if ((arg0->unk4 == 0x96) && (arg0->unk31C->unk7D != 0)) {
//         phi_v1 = arg0->unk31C->unk82 + 1024;
//     } else {
//         phi_v1 = arg0->unk1D1 * 200;
//     }
//     tmp.unk14 = phi_t0;
//     tmp.unk10 = phi_v1 * 0.005493164f;
//     tmp.unk0 = tmp.unk10 * D_800A56B4;
//     func_1505A184(phi_t0, 2000.0f, tmp.unk10, &arg1->unk0, &arg1->unk8, &arg1->unk4);
//     if (arg2 != 0) {
//         arg2->unk4 = cosf(tmp.unk0) * 1000.0f;
//         temp_f6 = sinf(tmp.unk0) * 1000.0f;
//         tmp.unk8 = temp_f6;
//         tmp.unk4 = phi_t0 * D_800A56B8;
//         arg2->unk0 = cosf(tmp.unk4) * tmp.unk8;
//         arg2->unk8 = sinf(tmp.unk4) * -temp_f6;
//         if (arg3 != 0) {
//             tmp.unkC = tmp.unk0 + arg4;
//             arg3->unk4 = cosf(tmp.unkC) * 1000.0f;
//             tmp.unk8 = sinf(tmp.unkC) * 1000.0f;
//             arg3->unk0 = cosf(tmp.unk4) * tmp.unk8;
//             arg3->unk8 = sinf(tmp.unk4) * -tmp.unk8;
//         }
//     }
// }

void func_15145974(struct17 *arg0, f32 *arg1, f32 *arg2) {
    *arg1 = func_150484A0(arg0->unk0, arg0->unk8) * D_800A56BC;
    if (arg2 != NULL) {
        *arg2 = (func_150484A0(sqrtf(arg0->unk0 * arg0->unk0 + arg0->unk8 * arg0->unk8), arg0->unk4) * D_800A56C0) - 90.0f;
    }
}

f32 func_15145A0C(f32 arg0, f32 arg1, f32 arg2) {
    return D_800A548C[(s32)(arg0 * arg2 * 100.0f)] * arg1;
}


void func_15145A50(struct127 *arg0) {
    arg0->unk5 = 3;
    if (D_800BE9F0 != 51) {
        if ((D_800BE616 != 0) || (arg0->interaction_state == 5) || (arg0->interaction_state == 1) || (arg0->interaction_state == 21)) {
            arg0->interaction_state = 5;
            if (arg0->unk31C != NULL) {
                arg0->unk31C->unk78 = 0;
            }
        } else {
            func_15053694(arg0);
        }
    }
}
/* Note 1090: scoped scale/reciprocal lifetimes preserve the direct retail schedule. */
s32 func_15145AD8(struct17 *arg0, struct17 *arg1, struct127 *arg2,
    struct17 *arg3, struct17 *arg4, f32 *arg5, f32 *arg6, struct17 *arg7) {
    struct17 center;
    f32 radius;
    f32 height;
    struct17 origin;
    struct17 direction;
    struct17 scaledCenter;
    f32 length;
    f32 first;
    f32 second;

    if (arg5 != NULL) {
        arg5 = &radius;
    }
    if (arg6 != NULL) {
        arg6 = &height;
    }
    if (arg7 != NULL) {
        arg7 = &center;
    }
    func_1515C1A0(arg2, arg7, arg5, arg6);
    if (*arg6 == 0.0f) {
        return 0;
    }
    if (*arg5 == 0.0f) {
        return 0;
    }
    {
        f32 scale;
        f32 inverse;

        scale = arg2->unkDC;
        inverse = arg2->unkE0;
        origin.unk0 = arg0->unk0;
        origin.unk4 = arg0->unk4 * scale;
        origin.unk8 = arg0->unk8;
        direction.unk0 = arg1->unk0;
        direction.unk4 = arg1->unk4 * scale;
        direction.unk8 = arg1->unk8;
        {
            f32 reciprocal;

            if (!func_15145128(&direction, &direction, &length, &reciprocal)) {
                return 0;
            }
            scaledCenter.unk0 = arg7->unk0;
            scaledCenter.unk4 = arg7->unk4 * scale;
            scaledCenter.unk8 = arg7->unk8;
            if (!func_151451F0(&origin, &direction, &scaledCenter, *arg5, length,
                    arg3, arg4, &first, &second)) {
                return 0;
            }
            arg3->unk4 *= inverse;
            arg4->unk4 *= inverse;
            return 1;
        }
    }
}
u8 func_15145C90(s32 arg0) {
    if (arg0 < 0) {
        return 1;
    } else {
        return (D_800DBEF4[arg0].unk6F & 0x80) == 0x80;
    }
}

void func_15145CD0(u8 *arg0, struct17 **arg1, struct17 **arg2, s32 arg3) {
    f32 mtx[4][4];
    struct17 *src;
    struct17 *dst;

    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));
    mtx[3][0] = *(s16 *)(arg0 + 0x10);
    mtx[3][1] = *(s16 *)(arg0 + 0x12);
    mtx[3][2] = *(s16 *)(arg0 + 0x14);

    while (arg3 > 0) {
        src = *arg1;
        dst = *arg2;
        func_150A7960(mtx, src->unk0, src->unk4, src->unk8, &dst->unk0, &dst->unk4, &dst->unk8);
        arg3--;
        arg1++;
        arg2++;
    }
}

void func_15145DB4(u8 *arg0, struct17 *arg1, struct17 *arg2, s32 arg3) {
    f32 mtx[4][4];

    func_150A8050(mtx, *(f32 *)(arg0 + 0), *(f32 *)(arg0 + 4), *(f32 *)(arg0 + 8));
    mtx[3][0] = *(s16 *)(arg0 + 0x10);
    mtx[3][1] = *(s16 *)(arg0 + 0x12);
    mtx[3][2] = *(s16 *)(arg0 + 0x14);

    while (arg3 > 0) {
        func_150A7960(mtx, arg1->unk0, arg1->unk4, arg1->unk8, &arg2->unk0, &arg2->unk4, &arg2->unk8);
        arg3--;
        arg1++;
        arg2++;
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15145EA4.s. */
s32 func_15145EA4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_15146078.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_16EE20/func_15146078.s")
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_151462C8.s. */
s32 func_151462C8() {
    return 0;
}
u8 func_151464B8(s16 *arg0) {
    s16 mask;
    s32 i;
    s32 masked;

    i = 0;
    mask = 0;
    for (; i <= D_80082FA0; i++) {
        mask |= 1 << i;
    }

    masked = (arg0[1] & mask) ^ 0;
    return (masked == 0) & 0xFFFFFFFFFFFFFFFF;
}

void func_15146508(struct127 *arg0, struct127 *arg1) {
    struct193 tmp;

    tmp.unk0 = arg0;
    tmp.unk4 = arg1;
    tmp.unk8 = arg0->unique_id;
    tmp.unk9 = arg1->unique_id;
    func_15169040(&tmp, 45, arg0, arg1);
}
/* Non-matching C placeholders for asm/nonmatchings/game_16EE20/func_1514654C.s. */
s32 func_1514654C() {
    return 0;
}
// Matched with guarded opening-load scheduling normalization.
s32 func_1514672C(struct17 *arg0) {
    if ((D_800A56C4 < fabsf(arg0->unk0)) || (D_800A56C4 < fabsf(arg0->unk8)) || (D_800A56C4 < arg0->unk4) || (arg0->unk4 < D_800A56C8)) {
        return 0;
    } else {
        return 1;
    }
}

void func_151467A4(f32 *arg0, f32 arg1, f32 *arg2, f32 arg3, f32 arg4, f32 arg5, f32 arg6, f32 *arg7) {
    *arg0 = *arg0 - D_800BE9A4;
    if (*arg0 < 0.0f) {
        *arg0 = func_150ADA68() * arg1;
        if ((func_150ADA20() & 3) != 0) {
            *arg2 = (func_150ADA68() * (arg4 - arg3)) + arg3;
        } else {
            *arg2 = (func_150ADA68() * (arg5 - arg4)) + arg4;
        }
    }
    *arg7 = ((*arg2 - *arg7) * arg6) + *arg7;
}
