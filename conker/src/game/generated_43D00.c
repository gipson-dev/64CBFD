#include <ultra64.h>

/* Category records, resource caching, and per-record payload tables. */

#include "structs.h"
extern u8 D_800BE590, D_800D2100;
extern struct258 *D_800D20FC;
extern u16 D_800BE598[];
extern void *D_800BE5A8[];
u32 func_1502B7F0(void **output, u32 depth, ...);

/* Cache each distinct record resource, retaining the loader's live output. */
void func_15016850(void) {
    s32 offset, index, found;
    void *handle;
    s32 resource, limit;

    handle = 0;
    D_800BE590 = 0;
    offset = 0;
    if (D_800D2100 > 0) {
      do {
        resource = ((u8 *)D_800D20FC)[offset + 4];
        found = 0;
        for (index = 0; index < D_800BE590; index++) {
            if (resource == D_800BE598[index]) {
                found = 1;
                break;
            }
        }
        if (!found) {
            if (resource < 187) func_1502B7F0(&handle, 2, 18, resource);
            if (handle != 0) {
                D_800BE5A8[D_800BE590] = handle;
                D_800BE598[D_800BE590] = resource;
                D_800BE590++;
            }
        }
        limit = D_800D2100 << 2;
        limit -= D_800D2100;
        limit <<= 4;
        offset += 48;
      } while (offset < limit);
    }
}

typedef struct Record150169A0 {
    u16 field0;
    u8 disabled, kind, resource, field5;
    s16 x, y, z;
    u8 heading, fieldD, fieldE, fieldF, field10;
    u8 pad11[7];
    u32 flags, field1C;
    f32 scale20, scale24;
    u8 identity, pad29[7];
} Record150169A0;
typedef char Record150169A0Size[sizeof(Record150169A0) == 0x30 ? 1 : -1];
extern u8 D_1A33F0[], D_1A34E0[], D_1A37E0[];
extern u8 D_800D2101;
extern u8 *D_800D210C;
extern s16 *D_800D2110;
extern s32 D_800D1548, D_800BE9F0;
extern s8 D_8008FD8C, D_8008FD90;
extern u16 D_800D2340;
extern struct127 D_800CC2D0[26];
void func_15004F30(void);
u32 func_1502B9B4(u32 depth, ...);
void *allocate_memory(s32 size, s32 mode, s32 pool, s32 flags);
s32 func_10004514(s32 address, void *destination, u32 size, s32 mode);
u32 func_1502B8E0(void *buffer, u32 capacity, u32 depth, ...);
s32 func_150859AC(s16 slot, s16 field);
s32 func_15083DA0(void);
s32 func_1508295C(s32 category, u8 *mode, s32 enabled);
void func_15172CA8(s32 mode);
void func_15017114(s32 category);
#define RECORD150169A0(o) (*(Record150169A0 *)((u8 *)D_800D20FC + (o)))

/* Load category records, apply player settings, then fill cache and identities. */
void func_150169A0(s32 category) {
    s32 identityIndex;
    u8 *end;
    u8 *bank;
    u32 bytes, extra;
    s32 count, slot;

    func_15004F30();
    switch (category) {
    case 0x1A: case 0x24: case 0x2B: case 0x2D:
    case 0x30: case 0x33: case 0x34: case 0x3F:
        bank = D_1A34E0;
        end = D_1A37E0;
        break;
    default:
        bank = D_1A33F0;
        end = D_1A34E0;
        break;
    }
    extra = func_1502B9B4(2, 14);
    bytes = end - bank;
    D_800D20FC = allocate_memory(extra + bytes, 1, 2, 0);
    func_10004514((s32)bank, D_800D20FC, bytes, 1);
    D_800D2100 = bytes / 48;
    D_800D2101 = D_800D2100;
    D_800D2100 += func_1502B8E0((Record150169A0 *)D_800D20FC + D_800D2100,
                               0, 2, 14, category) / 48;
    func_15017114(category);
    count = D_800D2100;
    D_800D210C = allocate_memory(count, 1, 0, 0);
    bytes = count * 2;
    D_800D2110 = allocate_memory(bytes, 1, 0, 0);
    bzero(D_800D210C, count);
    bzero(D_800D2110, bytes);
    D_800D1548 = 0;
    slot = 0;
    if (D_8008FD8C > 0) {
      do {
        if ((1 << slot) & D_800D2340) {
            s32 selected = func_150859AC((s16)slot, 1);
            RECORD150169A0(slot * 48).disabled = 0;
            switch (selected) {
            case 0:
                if (D_800BE9F0 == 0x36 || D_800BE9F0 == 0x3A || D_800BE9F0 == 0x40)
                    RECORD150169A0(slot * 48).resource = 150;
                else
                    RECORD150169A0(slot * 48).resource = 0;
                break;
            case 16: RECORD150169A0(slot * 48).resource = 150; break;
            case 1: RECORD150169A0(slot * 48).resource = 59; break;
            case 2: RECORD150169A0(slot * 48).resource = 152; break;
            case 3: RECORD150169A0(slot * 48).resource = 117; break;
            case 4: RECORD150169A0(slot * 48).resource = 128; break;
            case 37:
                RECORD150169A0(slot * 48).resource = 176;
                RECORD150169A0(slot * 48).scale24 = 0.6f;
                RECORD150169A0(slot * 48).scale20 = RECORD150169A0(slot * 48).scale24;
                break;
            case 38:
                RECORD150169A0(slot * 48).resource = 177;
                RECORD150169A0(slot * 48).scale24 = 0.6f;
                RECORD150169A0(slot * 48).scale20 = RECORD150169A0(slot * 48).scale24;
                break;
            case 39: RECORD150169A0(slot * 48).resource = 178; break;
            case 40: RECORD150169A0(slot * 48).resource = 180; break;
            case 33: RECORD150169A0(slot * 48).resource = 159; break;
            case 34: RECORD150169A0(slot * 48).resource = 160; break;
            case 11: RECORD150169A0(slot * 48).resource = 136; break;
            case 35:
                RECORD150169A0(slot * 48).resource = 155;
                RECORD150169A0(slot * 48).kind = 21; break;
            case 36:
                RECORD150169A0(slot * 48).resource = 154;
                RECORD150169A0(slot * 48).kind = 21; break;
            case 17: case 18: case 19: case 20: case 21: case 22:
            case 23: case 24: case 25: case 26: case 27: case 28:
                RECORD150169A0(slot * 48).resource = 156; break;
            case 29: case 30: case 31: case 32:
                RECORD150169A0(slot * 48).resource = 157; break;
            case 12: case 13: case 14: case 15:
                RECORD150169A0(slot * 48).resource = 144;
                if (slot < D_8008FD90) RECORD150169A0(slot * 48).kind = 1;
                else RECORD150169A0(slot * 48).kind = 12;
                RECORD150169A0(slot * 48).flags |= 4;
                RECORD150169A0(slot * 48).fieldD = 13;
                break;
            case 8:
                RECORD150169A0(slot * 48).resource = 119;
                RECORD150169A0(slot * 48).kind = 30;
                RECORD150169A0(slot * 48).field10 = 170;
                if (slot >= D_8008FD90) RECORD150169A0(slot * 48).fieldD = 3;
                else RECORD150169A0(slot * 48).fieldD = 1;
                RECORD150169A0(slot * 48).flags |= 0x180000;
                RECORD150169A0(slot * 48).fieldE |= 0x80;
                break;
            case 10:
                RECORD150169A0(slot * 48).resource = 119;
                RECORD150169A0(slot * 48).kind = 37;
                RECORD150169A0(slot * 48).field10 = 168;
                RECORD150169A0(slot * 48).fieldD = 3;
                RECORD150169A0(slot * 48).flags |= 0x100000;
                break;
            case 9:
                RECORD150169A0(slot * 48).resource = 83;
                RECORD150169A0(slot * 48).kind = 31;
                RECORD150169A0(slot * 48).field10 = 168;
                RECORD150169A0(slot * 48).fieldD = 2;
                RECORD150169A0(slot * 48).scale20 = 0.7f;
                RECORD150169A0(slot * 48).scale24 = 0.7f;
                RECORD150169A0(slot * 48).flags |= 1;
                break;
            }
            if (D_800BE9F0 == 0x33 || D_800BE9F0 == 0x32)
                RECORD150169A0(slot * 48).flags |= 0x4000000;
            RECORD150169A0(slot * 48).x = (s16)(s32)D_800CC2D0[slot].x_position;
            RECORD150169A0(slot * 48).y = (s16)(s32)D_800CC2D0[slot].y_position;
            RECORD150169A0(slot * 48).z = (s16)(s32)D_800CC2D0[slot].z_position;
            RECORD150169A0(slot * 48).heading = D_800CC2D0[slot].unk76 >> 8;
        } else {
            RECORD150169A0(slot * 48).disabled = 1;
        }
        slot++;
      } while (slot < D_8008FD8C);
    }
    func_15016850();
    for (identityIndex = 0; identityIndex < D_800D2100; identityIndex++) {
        if (RECORD150169A0(identityIndex * 48).identity == 0)
            RECORD150169A0(identityIndex * 48).identity = func_15083DA0();
    }
    func_1508295C(category, (u8 *)1, 1);
    func_15172CA8(0);
    func_1508295C(category, (u8 *)1, 0);
}


typedef struct RecordPayloadMetadata15017114 {
    u32 offset, status;
} RecordPayloadMetadata15017114;
extern u8 **D_800D2104;
extern u8 *D_800D2108;

/* Initialize player payloads and resolve appended records' relative metadata. */
void func_15017114(s32 category) {
    u8 count;
    u8 *metadata;
    s32 index;
    u8 *playerPayload;

    metadata = 0;
    count = D_800D2100;
    D_800D2104 = allocate_memory(count * 4, 1, 0, 0);
    D_800D2108 = allocate_memory(count, 1, 0, 0);
    bzero(D_800D2104, count * 4);
    bzero(D_800D2108, count);
    for (index = 0; index < D_8008FD8C; index++) {
        playerPayload = allocate_memory(16, 1, 2, 0);
        D_800D2104[index] = playerPayload;
        bzero(D_800D2104[index], 16);
        D_800D2108[index] = 2;
    }
    if (func_1502B7F0((void **)&metadata, 2, 16, category)) {
        for (index = D_800D2101; index < D_800D2100; index++) {
            if (((RecordPayloadMetadata15017114 *)metadata)[index - D_800D2101].offset != 0) {
                D_800D2108[index] = ((RecordPayloadMetadata15017114 *)metadata)[index - D_800D2101].status;
                D_800D2104[index] = metadata + ((RecordPayloadMetadata15017114 *)metadata)[index - D_800D2101].offset;
            }
        }
    }
}
