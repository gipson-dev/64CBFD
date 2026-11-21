#include <ultra64.h>
#include "structs.h"
typedef struct { f32 x, y, z; } GroundEffectPosition1BF090;
typedef struct HeightResult71820 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags, state;
    u16 pad1E;
    s32 value;
} HeightResult71820;
typedef struct HeightActor71820 HeightActor71820;
typedef struct {
    u8 *owner;
    u8 identity;
    GroundEffectPosition1BF090 position;
    s32 channel;
    f32 zero, value1C, value20;
    HeightResult71820 surface;
    f32 value48, value4C;
    s16 value50, value52;
    u8 value54, value55;
    f32 value58, value5C, value60;
    u8 value64;
} OwnerGroundEffect1BF090;
void func_1504715C(HeightResult71820 *, HeightActor71820 *);
struct260 *func_15149130(s16, s8, s8, s8, u8, u8, struct37 *, u8, s32);
void *memcpy(void *, const void *, u32);

void func_15131C84(u8 *, s8 *, f32, f32 *, f32 *, f32 *);

/* Non-matching placeholders for the text-only asm slice asm/1BF090.s. */

/* Build the owner's surface snapshot and create a 104-byte ground effect. */
void *func_15191BE0(u8 *owner, GroundEffectPosition1BF090 *position, u8 channel,
                   f32 value1C, f32 value20, s16 lifetime, f32 value48, f32 value4C,
                   s16 value50, s16 value52, u8 value54, u8 value55,
                   f32 value58, f32 value5C, f32 value60, u8 value64,
                   u8 priority, s32 context) {
    u8 *created;
    OwnerGroundEffect1BF090 packet;

    if (owner == NULL) {
        return NULL;
    }
    packet.owner = owner;
    packet.identity = owner[0x3B];
    packet.position = *position;
    packet.channel = channel << 6;
    packet.value1C = value1C;
    packet.zero = 0.0f;
    packet.value20 = value20;
    func_1504715C(&packet.surface, (HeightActor71820 *)owner);
    packet.value48 = value48;
    packet.value4C = value4C;
    packet.value50 = value50;
    packet.value52 = value52;
    packet.value54 = value54;
    packet.value55 = value55;
    packet.value58 = value58;
    packet.value5C = value5C;
    packet.value60 = value60;
    packet.value64 = value64;
    created = (u8 *)func_15149130(lifetime == -1 ? 300 : lifetime,
                                 -1, 29, -1, lifetime == -1 ? 0 : 1,
                                 29, (struct37 *)sizeof(packet), priority, context);
    if (created != NULL) {
        memcpy(created + 0x28, &packet, sizeof(packet));
    }
    return created;
}

s32 func_15191D54() {
    return 0;
}

s32 func_1519203C() {
    return 0;
}

s32 func_15192308(u8 *arg0, s32 arg1) {
    func_15131C84(arg0 + 0xAC, (s8 *)(arg0 + 0xAE), *(f32 *)(arg0 + 0xA8),
                  (f32 *)(arg0 + 0xB0), (f32 *)(arg0 + 0x38), (f32 *)(arg0 + 0x3C));
    return 1;
}

s32 func_15192358() {
    return 0;
}

s32 func_1519257C(s32 arg0, s32 arg1) {
    s32 call_result = func_15192308(arg0, arg1);
    u8 result = call_result;

    if (call_result != 0) {
        result = func_15192358(arg0, arg1);
    }

    return result;
}

s32 func_151925C4() {
    return 0;
}

void func_1519277C(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, arg0 + 0x28, arg0 + 0x2C, arg0);
}
