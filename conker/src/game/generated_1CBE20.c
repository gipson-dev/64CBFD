#include <ultra64.h>

extern f32 D_800A8CD8;
extern s32 D_800BE9E4;
void func_1516972C(void *);
void *func_15167A68(s32, s32, s32, s32, u8, u8);

typedef struct {
    u8 header[0x10];
    u32 flags;
    s32 state;
    u8 *first;
    u8 *second;
    s16 lifetime;
    u8 pad22[2];
    u8 *owner;
    u8 mode;
    u8 pad29[3];
} AddressRecord1CBE20;

typedef struct { f32 x, y, z; } Position1CBE20;
typedef struct {
    s32 count;
    s32 countRange;
    Position1CBE20 position;
    s16 angle;
    s16 angleRange;
    s16 pitch;
    s16 pitchRange;
    f32 speed;
    f32 speedRange;
    f32 vertical;
    f32 verticalRange;
    s16 lifetime;
    s16 lifetimeRange;
    f32 scale;
    f32 scaleRange;
    f32 spread;
} Configuration1CBE20;

extern f32 D_800A8CC0, D_800A8CC4, D_800A8CC8, D_800A8CCC, D_800A8CD0;
void func_15152190(Configuration1CBE20 *, s32 *, f32 *, s32, f32, u8, u8, s32);

typedef struct {
    Position1CBE20 position;
    Position1CBE20 vector;
    f32 width;
    f32 height;
} Source1CBE20;
typedef struct {
    f32 field00;
    f32 field04;
    f32 field08;
    f32 field0C;
    Position1CBE20 vector;
    f32 field1C;
    f32 field20;
    f32 field24;
    Position1CBE20 position;
    Position1CBE20 first;
    Position1CBE20 second;
    f32 field4C;
    u32 flags;
    s16 lifetime;
    u16 resource;
    u8 field58;
    u8 pad59[3];
    u32 field5C;
    u8 field60;
    u8 field61;
    u8 field62;
    u8 field63;
    u8 field64;
    u8 field65;
    u8 field66;
    u8 field67;
    u8 field68;
    u8 pad69;
    u8 field6A;
    u8 pad6B;
    u32 field6C;
    u8 field70;
    u8 pad71;
    s16 field72;
    s16 field74;
    u8 pad76[2];
    u32 field78;
} ActorDescriptor1CBE20;

extern Position1CBE20 D_800A5480;
extern f32 D_800A8CD4;
struct ExtendedState15F680;
void *func_1513264C(u8 *, s32, s32, struct ExtendedState15F680 *, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Non-matching placeholders for the text-only asm slice asm/1CBE20.s. */

AddressRecord1CBE20 *func_1519E970(s16 lifetime, u8 *owner, u8 mode, u8 *first,
                                       u8 *second, u8 channel, s32 context) {
    AddressRecord1CBE20 *record;

    record = func_15167A68(0x26, context, sizeof(AddressRecord1CBE20), 1, channel, 1);
    if (record == NULL) {
        return NULL;
    }
    record->first = first;
    record->second = second;
    record->lifetime = lifetime;
    record->mode = mode;
    record->owner = owner;
    record->flags = 1;
    record->state = 0;
    return record;
}

void func_1519EA04(u8 *arg0) {
    s32 expired;

    if ((*(s32 *)(arg0 + 0x10) & 1) == 0) {
        return;
    }
    *(s16 *)(arg0 + 0x20) -= D_800BE9E4;
    expired = 0;
    if (*(s16 *)(arg0 + 0x20) < 0) {
        expired = 1;
    }
    if (expired == 0) {
        return;
    }
    if (arg0[0x28] == 0) {
        expired = *(s32 *)(arg0 + 0x24);
        *(s32 *)(expired + 0x30) = 0;
    }
    func_1516972C(arg0);
}

void func_1519EA78(Position1CBE20 *position, u16 selector, f32 scale, u8 channel, s32 context) {
    Configuration1CBE20 packet;
    s32 selected;
    f32 selectedScale;

    packet.count = 10;
    packet.countRange = 7;
    packet.position = *position;
    packet.angle = 0;
    packet.angleRange = 255;
    packet.pitch = -53;
    packet.pitchRange = 24;
    packet.speed = 10.0f;
    packet.speedRange = 8.0f;
    packet.vertical = D_800A8CC0;
    packet.verticalRange = D_800A8CC4;
    packet.lifetime = 50;
    packet.lifetimeRange = 20;
    packet.scale = D_800A8CC8;
    packet.scaleRange = D_800A8CCC;
    packet.spread = D_800A8CD0;
    selected = selector;
    selectedScale = scale;
    func_15152190(&packet, &selected, &selectedScale, 1, 0.0f, 0, channel, context);
}

void func_1519EB8C(Source1CBE20 *source, u16 resource, s16 lifetime, u8 channel, s32 context) {
    ActorDescriptor1CBE20 packet;
    Source1CBE20 *savedSource;
    u8 *actor;

    savedSource = source;
    packet.field00 = 1.0f;
    packet.field04 = 1.0f;
    packet.field08 = source->width * D_800A8CD4;
    packet.field0C = source->height * D_800A8CD4;
    packet.vector.x = source->vector.x;
    packet.vector.y = source->vector.y;
    packet.vector.z = source->vector.z;
    packet.field1C = 1.0f;
    packet.field20 = 1.0f;
    packet.field24 = 1.0f;
    packet.position.x = source->position.x;
    packet.position.y = source->position.y;
    packet.position.z = source->position.z;
    packet.first = D_800A5480;
    packet.second = D_800A5480;
    packet.field4C = 0.0f;
    packet.flags = 0x980;
    packet.lifetime = lifetime;
    packet.resource = resource;
    packet.field58 = 0;
    packet.field5C = 0;
    packet.field60 = 255;
    packet.field61 = 21;
    packet.field62 = 0;
    packet.field63 = 0;
    packet.field64 = 0;
    packet.field65 = 0;
    packet.field66 = 0;
    packet.field67 = 0;
    packet.field68 = 2;
    packet.field6A = 0;
    packet.field6C = 0;
    packet.field70 = 0;
    packet.field72 = 1;
    packet.field74 = 255;
    packet.field78 = 0;
    actor = func_1513264C((u8 *)&packet, 3, 255, NULL, 4, channel, context);
    if (actor != NULL) {
        memcpy(actor + 0x170, &savedSource, sizeof(savedSource));
    }
}

s32 func_1519ED24(u8 *arg0) {
    f32 scale = D_800A8CD8;
    u8 *source = *(u8 **)(arg0 + 0x170);

    *(f32 *)(arg0 + 0x18) = *(f32 *)(source + 0x18) * scale;
    *(f32 *)(arg0 + 0x1C) = *(f32 *)(source + 0x1C) * scale;
    *(f32 *)(arg0 + 0x20) = *(f32 *)(source + 0x0C);
    *(f32 *)(arg0 + 0x24) = *(f32 *)(source + 0x10);
    *(f32 *)(arg0 + 0x28) = *(f32 *)(source + 0x14);
    *(f32 *)(arg0 + 0x38) = *(f32 *)(source + 0x00);
    *(f32 *)(arg0 + 0x3C) = *(f32 *)(source + 0x04);
    *(f32 *)(arg0 + 0x40) = *(f32 *)(source + 0x08);
    return 1;
}

s32 func_1519ED84() {
    return 0;
}

s32 func_1519EF04(u8 *arg0) {
    u8 *source = *(u8 **)(arg0 + 0x110);

    *(f32 *)(arg0 + 0x2C) = *(f32 *)(source + 0x18) * 10.0f;
    *(f32 *)(arg0 + 0x30) = *(f32 *)(source + 0x1C) * 10.0f;
    *(f32 *)(arg0 + 0x40) = *(f32 *)(source + 0x0C);
    *(f32 *)(arg0 + 0x44) = *(f32 *)(source + 0x10);
    *(f32 *)(arg0 + 0x48) = *(f32 *)(source + 0x14);
    *(f32 *)(arg0 + 0x34) = *(f32 *)(source + 0x00);
    *(f32 *)(arg0 + 0x38) = *(f32 *)(source + 0x04);
    *(f32 *)(arg0 + 0x3C) = *(f32 *)(source + 0x08);
    return 1;
}
