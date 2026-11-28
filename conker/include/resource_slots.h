#ifndef RESOURCE_SLOTS_H
#define RESOURCE_SLOTS_H
#include <ultra64.h>
/* Fifteen resource slots: ROM address, aligned byte count and pending buffer. */
typedef struct {
    u32 address;
    u32 alignedSize;
    void *pending;
    u8 state;
    u8 retained0D[3];
} ResourceSlot;
typedef struct { u16 id, retained; } ResourcePreset;
extern ResourceSlot D_800DDA90[15];
extern ResourcePreset D_800BE4A0[15];
#endif
