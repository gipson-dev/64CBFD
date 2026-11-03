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
typedef struct {
    u8 pad0[0x580];
    s32 key0;
    u8 tag0;
    u8 pad585[3];
    s32 key1;
    u8 tag1;
} DualIdentityState151B5A9C;
typedef struct {
    u8 pad0[0x28];
    DualIdentityState151B5A9C identity;
} DualIdentityOwner151B5A9C;
typedef struct {
    s32 key0;
    s32 key1;
    u8 tag0;
    u8 tag1;
} DualIdentityEvent151B5A9C;
void func_1516972C(DualIdentityOwner151B5A9C *);

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

/* Replace matching identity pairs or release an owner on command zero. */
void func_151B5A9C(DualIdentityOwner151B5A9C *owner,
                       DualIdentityEvent151B5A9C *event, u8 command) {
    DualIdentityState151B5A9C *state = &owner->identity;
    s32 key;

    if (command == 0x2D) {
        if (state->key0 == event->key0) {
            state->key0 = event->key1;
            state->tag0 = event->tag1;
        } else if (state->key0 == event->key1) {
            state->key0 = event->key0;
            state->tag0 = event->tag0;
        }
        if (state->key1 == event->key0) {
            state->key1 = event->key1;
            state->tag1 = event->tag1;
        } else if (state->key1 == event->key1) {
            state->key1 = event->key0;
            state->tag1 = event->tag0;
        }
    } else if (command == 0) {
        key = event->key0;
        if (state->key0 == key || state->key1 == key ||
            ((u8 *)event)[4] == state->tag0 ||
            ((u8 *)event)[4] == state->tag1) {
            func_1516972C(owner);
        }
    }
}
