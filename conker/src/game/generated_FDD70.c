#include <ultra64.h>
extern f32 D_800A0894;
f32 func_150ADA68();

/* Non-matching placeholders for the text-only asm slice asm/FDD70.s. */

s32 func_150D08C0() {
    return 0;
}

s32 func_150D0E90() {
    return 0;
}

extern f32 D_800A0890;
void *func_15134DAC(s32, s32);
typedef struct {
    u8 owner_id;
    u8 pad1[3];
    u8 *owner;
    u8 attachmentIndex;
    u8 pad9[3];
    f32 zero0;
    f32 zero1;
    f32 zero2;
    f32 zero3;
    f32 value1C;
    f32 value20;
    u8 mode;
    u8 pad25;
    s16 activeFrames;
    s16 restartDelay;
    s16 lifetime;
    s16 value2C;
    s8 startCallback;
    s8 transformCallback;
    s8 updateCallback;
    u8 pad31[3];
    f32 rate;
    u8 flags;
    s8 finishCallback;
} OwnerVariantDescriptorFDD70;

/* Construct an owner-attached effect with a variant-dependent signed offset. */
void *func_150D10E4(u8 *owner, u8 variant) {
    OwnerVariantDescriptorFDD70 packet;
    packet.owner_id = owner[0x3B];
    packet.owner = owner;
    packet.attachmentIndex = 0;
    packet.zero0 = 0.0f;
    packet.zero1 = 0.0f;
    packet.zero2 = 0.0f;
    packet.zero3 = 0.0f;
    packet.value1C = variant != 0 ? -30.0f : 30.0f;
    packet.value20 = 0.0f;
    packet.mode = 2;
    packet.activeFrames = 50;
    packet.restartDelay = 22;
    packet.lifetime = 2000;
    packet.value2C = 0;
    packet.startCallback = 6;
    packet.transformCallback = 7;
    packet.updateCallback = -1;
    packet.rate = D_800A0890;
    packet.flags = 0;
    packet.finishCallback = -1;
    return func_15134DAC((s32)&packet, 0);
}

s32 func_150D11B4(u8 *arg0) {
    *(f32 *) (arg0 + 0x74) = (func_150ADA68() * 150.0f + 350.0f) * D_800A0894;
    return 1;
}

s32 func_150D1204() {
    return 0;
}
