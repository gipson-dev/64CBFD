#include <ultra64.h>


typedef struct { void *allocation; u8 age; u8 unused[3]; } CacheEntry1517;
typedef struct { u8 countIndex; u8 slots; u8 unused[6]; } CacheDescriptor1517;
extern s32 D_800DD460[2];
extern CacheDescriptor1517 D_800A7230[2];
extern u16 D_800C4310[];
void func_10004074(void *allocation);

/* Age or release cached allocations in both active groups. */
void func_1517ABB0(void) {
    s32 group, row, col;
    s32 slots, byteOffset;
    u16 count;
    CacheDescriptor1517 *descriptor;
    CacheEntry1517 *entry;
    for (group = 0; group < 2; group++) {
        descriptor = &D_800A7230[group];
        if (D_800DD460[group] != 0) {
            row = 0;
            count = D_800C4310[descriptor->countIndex];
            while (row < count) {
                slots = descriptor->slots;
                if (slots > 0) {
                    col = 0;
                    byteOffset = 0;
                    do {
                        entry = (CacheEntry1517 *)((u8 *)((CacheEntry1517 **)(u32)D_800DD460[group])[row] + byteOffset);
                        if (entry->allocation != NULL) {
                            if (entry->age != 0) {
                                entry->age--;
                                slots = descriptor->slots;
                                goto next_slot;
                            }
                            func_10004074(entry->allocation);
                            ((CacheEntry1517 *)((u8 *)((CacheEntry1517 **)(u32)D_800DD460[group])[row] + byteOffset))->allocation = NULL;
                            slots = descriptor->slots;
                        }
next_slot:
                        col++;
                        byteOffset += 8;
                    } while (col < slots);
                    count = D_800C4310[descriptor->countIndex];
                }
                row++;
            }
        }
    }
}

/* Non-matching placeholder for asm/1A8060.s. */
s32 func_1517AD00() {
    return 0;
}
