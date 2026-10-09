#include <ultra64.h>
extern void (*D_8008A340[])();
extern void (*D_8008A2F0[])();
extern void (*D_8008A390[])();
extern s32 D_80082FA0;
void func_100043B4(s32 *, u32);

typedef struct {
    u8 pad0[0x3C];
    s32 entries[4];
    s32 trailing;
} ResourceOwner174BF0;

typedef struct { s32 words[9]; } EffectOptional15147A80;
typedef struct {
    u8 prefix[0x10], request[0x1C];
    u8 flags[6], padding32[2];
    s32 resourceBytes;
    u8 state, padding39[3];
    u8 *entries[4], *trailing;
    s32 value;
    f32 position[3];
    EffectOptional15147A80 optional;
    u8 cleared[0x10];
    u8 *end, *payload;
    s32 padding9C;
} EffectCore15147A80;

void *func_15167A68(s32, s32, s32, s32, u8, u8);
u8 *func_1515D480(s32);
u8 *func_1515D440(void);

u8 *func_151462C8(u8 *, void *, u8, u8 *, u8, s16, void *, u8, s32);
void func_1516972C(u8 *);
extern u8 *(*D_8008A2A4[])(u8 *, u8 *, s16);

/* Non-matching placeholders for the text-only asm slice asm/174BF0.s. */

s32 func_151D5E30();
void func_1514795C(ResourceOwner174BF0 *);
void func_15169260(s32, s32, s32, u8);
extern u8 D_800A5760[];

s32 func_15147740() {
    return 0;
}

void func_151478D0(u8 *arg0) {
    func_151D5E30(arg0 + 0x84, arg0);
}

s32 func_151478F4(s32 arg0) {
    func_151478D0(arg0);
    func_1514795C(arg0);
    func_15169804(arg0);
}

s32 func_15147928(s32 arg0) {
    func_151478D0(arg0);
    func_1514795C(arg0);
    func_15169824(arg0);
}

void func_1514795C(ResourceOwner174BF0 *arg0) {
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

void func_151479E0(u8 *arg0) {
    s32 idx = *(s32 *) (arg0 + 0x20);

    if (idx < 0) {
        idx = 0;
    } else if (idx >= 0x14) {
        idx = 0;
    }
    D_8008A2F0[idx]();
}

void func_15147A30(u8 *arg0) {
    s32 idx = *(s32 *) (arg0 + 0x20);

    if (idx < 0) {
        idx = 0;
    } else if (idx >= 0x14) {
        idx = 0;
    }
    D_8008A340[idx]();
}

u8 *func_15147A80(void *request, s32 payloadBytes, s32 entryBytes,
    s32 active, s32 first, s32 second, s32 resourceBytes, s32 value,
    void *optional, u8 channel, s32 context) {
    EffectCore15147A80 *created;
    u8 *payload;
    u8 kind;
    s32 i;
    u32 extra;

    extra = (u32)((u8 *)request)[0x15] * (u32)entryBytes;
    kind = 0x22;
    if (*(u16 *)((u8 *)request + 0xE) & 0x40) {
        kind = 0x4D;
    } else {
        kind = 0x22;
    }
    created = (EffectCore15147A80 *)func_15167A68(kind, context,
        (u32)payloadBytes + extra + 0xA0,
        1, channel, 1);
    if (created == NULL) {
        return NULL;
    }
    payload = (u8 *)(created + 1);
    created->payload = payload;
    created->end = created->payload + payloadBytes;
    memcpy(created->request, request, 28);
    created->flags[0] = 0;
    created->flags[1] = 0;
    created->flags[2] = 0;
    created->flags[3] = active;
    created->flags[4] = first;
    created->flags[5] = second;
    if (optional != NULL) {
        created->optional = *(EffectOptional15147A80 *)optional;
    } else {
        ((u8 *)&created->optional)[0x1C] = 0;
    }
    created->resourceBytes = resourceBytes;
    created->value = value;
    created->state = 0;
    for (i = 0; i < 4; i++) {
        created->entries[i] = 0;
    }
    created->trailing = 0;
    if (resourceBytes != 0) {
        for (i = 0; i <= D_80082FA0; i++) {
            created->entries[i] = func_1515D480(resourceBytes);
        }
        created->trailing = func_1515D440();
    }
    created->position[0] = 0.0f;
    created->position[1] = 0.0f;
    created->position[2] = 0.0f;
    bzero(created->cleared, 0x10);
    return (u8 *)created;
}

u8 *func_15147C4C(u8 *commands, u8 *actor, s16 index) {
    s32 optional;
    u8 selector;

    if (*(u16 *)(actor + 0x1E) & 0x20) {
        optional = *(s32 *)(actor + 0x28);
    } else {
        optional = 0;
    }
    commands = func_151462C8(commands, actor + 0x34, 0, NULL, 0,
        index, actor + 0x54, 2, optional);
    selector = actor[0x31];
    if (selector >= 0x13) {
        func_1516972C(actor);
        return commands;
    }
    if (selector != 0) {
        return D_8008A2A4[selector](actor, commands, index);
    }
    return commands;
}

void func_15147D1C(u8 *arg0, s32 arg1, u8 arg2) {
    void (*temp_v0)(u8 *, s32, u8) = D_8008A390[*(s32 *) (arg0 + 0x20)];

    if (temp_v0 != 0) {
        temp_v0(arg0, arg1, arg2);
    }
}

void func_15147D64(s32 arg0, u8 arg1) {
    func_15169260((s32) D_800A5760, 2, arg0, arg1);
}
