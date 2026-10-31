#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/10E240.s. */

s32 func_150E0D90() {
    return 0;
}

typedef struct {u8 pad0[0x10];s16 x;u8 pad12[2];s16 y;} PresetHeader;
typedef struct {u8 index;u8 retained[3];PresetHeader *resource;s32 handle;f32 zero;} PresetPayload;
extern u8 D_800A0FE0[2];
PresetHeader *func_151149AC(u32);
void func_1510F800(s32);
s32 func_1510FD20(s32,s32);
void *func_15149130(s16,s8,s8,s8,u8,u8,s32,u8,s32);
void *memcpy(void *,const void *,u32);
/* Build the selected preset's sixteen-byte effect payload. */
void *func_150E1060(u8 index, u8 variant, s32 flags) {
    void *created;
    PresetPayload packet;
    if (index < 0) {
        return NULL;
    }
    if (index >= 2) {
        return NULL;
    }
    packet.index = index;
    packet.resource = func_151149AC(D_800A0FE0[index]);
    if (packet.resource == NULL) {
        return NULL;
    }
    func_1510F800(0);
    packet.handle = func_1510FD20(packet.resource->x, packet.resource->y);
    packet.zero = 0.0f;
    created = func_15149130(300,-1,31,-1,0,31,16,variant,flags);
    if (created != NULL) {
        memcpy((u8 *)created + 0x28, &packet, 16);
    }
    return created;
}

s32 func_150E114C() {
    return 0;
}
