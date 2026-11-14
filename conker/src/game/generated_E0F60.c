#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/E0F60.s. */

typedef struct { f32 x, y, z; u8 pad[2]; s16 angle; } EffectPosition150B3AB0;
typedef struct { u8 kind, pad01; s16 size; u8 mode, enabled; s8 value; u8 pad07; } EffectPacket150B3AB0;
extern s32 D_800BE9E8;
extern u8 *D_800DBFF0;
extern f32 D_8009FBC0[];
void func_1512D748(void *, s32, s32);
void func_15143134(f32 *, f32 *, u8 *);
s32 func_150ADA20(void);
void func_1514C858(f32, f32, f32, f32, s32, s32, s32, s32, s32, s32, f32, s32, s32);
u8 *func_151D8868(u8 *, s32, u8, s32);
void func_151D3FF4(f32 *, u8, s32);
/* Dispatch actor-linked effects; retain the retail slot-byte reloads. */
void func_150B3AB0(u8 *actor, volatile u8 slot) {
    EffectPosition150B3AB0 position;
    EffectPacket150B3AB0 packet;
    if (actor != NULL && *(u8 **)(actor + 0x1D4) != NULL) {
        func_1512D748(D_800DBFF0 + D_800BE9E8 * 0x9A0, 6, 1);
        position.angle = (*(u16 *)(actor + 0x7A) >> 8) + 0x40;
        func_15143134(D_8009FBC0, (f32 *)&position, *(u8 **)(actor + 0x1D4) + 0x640);
        func_1514C858(position.x, position.y, position.z, 10.0f, position.angle, 0, 255, (u32)func_150ADA20() % 31 + 40, 8, 0, 0.0f, 0, slot);
        packet.kind = 1;
        packet.size = (func_150ADA20() & 15) + 12;
        packet.mode = (func_150ADA20() & 3) + 5;
        packet.value = -1;
        packet.enabled = 1;
        func_151D8868((u8 *)&packet, 0, slot, 0);
        func_151D3FF4((f32 *)&position, slot, 0);
    }
}

s32 func_150B3C0C() {
    return 0;
}
