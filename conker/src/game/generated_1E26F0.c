#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1E26F0.s. */

typedef struct {u8 *resource;u8 id;u8 pad5[3];} ResourcePairEntry;
typedef struct {
    /* Opaque retail storage retains its N64 eight-byte alignment. */
    u64 retained[0xB0];
    ResourcePairEntry entries[2];
    f32 height, zero, extent, inverseExtent, factor;
    u8 tail[4];
} ResourcePairPayload;
u8 *func_15083E90(u8);
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
extern f32 D_800AA418;
/* Initialize the resource-pair fields and copy the original payload on success. */
void *func_151B5240(s16 effect, u8 variant, s32 flags) {
    void *record;
    ResourcePairPayload payload;
    payload.entries[0].id = 23;
    payload.entries[1].id = 22;
    payload.entries[0].resource = func_15083E90(23);
    payload.entries[1].resource = func_15083E90(payload.entries[1].id);
    payload.extent = 250.0f;
    payload.height = 18.0f;
    payload.zero = 0.0f;
    payload.factor = D_800AA418;
    payload.inverseExtent = 1.0f / payload.extent;
    record = func_15149130(effect, -1, -1, 1, 1, 21, 0x5A8, variant, flags);
    if (record != NULL) {
        memcpy((u8 *)record + 0x28, &payload, 0x5A8);
    }
    return record;
}

s32 func_151B5328() {
    return 0;
}

s32 func_151B5A9C() {
    return 0;
}
