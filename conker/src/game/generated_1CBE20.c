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

s32 func_1519EB8C() {
    return 0;
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
