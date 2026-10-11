#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/6A3D0.s. */

typedef struct {
    u8 pad0[0x30];
    u8 *data;
    u32 count;
} RecordByteBuffer;

extern u8 *D_800D19A0[];
extern u8 D_80098888[];
extern u8 *D_80084410[];
extern s16 D_800C5A90[];
extern struct124 *D_800D1C90[];
extern void *func_1502B6BC(s32 *, s32, s32 *, s32, ...);

extern u32 D_800C4020[];
extern u32 *D_800C4488[];
extern u32 *D_800C48F0[];
extern u32 D_800C4BE0[];
extern u32 *D_800C5338[];
extern u32 D_800C5048[];
extern u16 D_800C4310[];
extern u16 D_800C57A0[];
extern u16 D_800C4778[];
extern u16 D_800C5628[];
extern u16 D_800C4ED0[];
extern u8 *D_800C6360[];
extern u8 *D_800C5C08[];
extern u8 *D_800C6070[];
void *func_1502B6BC(s32 *, s32, s32 *, s32, ...);
void func_1503D438(u32 *, u32);
s32 func_1503D368();
s32 func_1503DC3C(s32);
void func_1510CE60(u32, s32, s32, s32, s32);
s32 func_1503D984();
s32 func_1503D804();
s32 func_150028BC(s32);
s32 func_1503D774(s32, s32);
s32 func_1503D660();
s32 func_1503DD1C();
void func_10004074(void *);

s32 func_1503CF20(s32 identity, s32 unused, u8 *config, s32 extras, s32 flags) {
    s32 output;
    u32 *block;
    u8 **mainSlot;
    u32 *first;
    u32 **primary;
    u32 **secondary;
    u16 *count;
    s32 failed;
    s32 index;
    s32 offset;
    u32 boundary;
    u8 **cleanupSlot;

    if (identity == 0xFF) {
        return 0;
    }
    if (identity >= 0xBB) {
        return 0;
    }
    mainSlot = &D_800D19A0[identity];
    if (*mainSlot != NULL) {
        return 0;
    }
    block = func_1502B6BC(&output, 7, 0, 2, 1, identity);
    if (block == NULL) {
        return 1;
    }
    *mainSlot = (u8 *)block + 0x38;
    first = &D_800C4020[identity];
    *first = block[0];
    primary = &D_800C4488[identity];
    *primary = (u32 *)block[2];
    secondary = &D_800C48F0[identity];
    *secondary = (u32 *)block[10];
    D_800C4BE0[identity] = block[4];
    D_800C5338[identity] = (u32 *)block[6];
    D_800C5048[identity] = block[8];
    D_800C4310[identity] = block[1] >> 2;
    if (*first != 0) {
        boundary = *first;
    } else {
        boundary = (u32)*primary;
    }
    D_800C57A0[identity] = (boundary - (u32)block - 0x38) >> 4;
    count = &D_800C4778[identity];
    index = 0;
    if ((*count = block[3] >> 2) > 0) {
        offset = 0;
        do {
            func_1503D438((u32 *)((u8 *)*primary + offset), (u32)block);
            func_1503D368(*(u32 *)((u8 *)*primary + offset), (u32)block);
            index++;
            offset += 4;
        } while (index < *count);
    }
    boundary = block[11] >> 2;
    index = 0;
    offset = 0;
    if (boundary != 0) {
        do {
            func_1503D438((u32 *)((u8 *)*secondary + offset), (u32)block);
            func_1503D368(*(u32 *)((u8 *)*secondary + offset), (u32)block);
            index++;
            offset += 4;
        } while ((u32)index < boundary);
    }
    D_800C5628[identity] = block[7] / 12;
    D_800C4ED0[identity] = block[5] >> 4;
    failed = 0;
    if (extras != 0) {
        failed = func_1503DC3C(identity);
        if (failed == 0) {
            offset = 0;
            for (index = 0; index < *count; index++) {
                func_1510CE60(*(u32 *)((u8 *)*primary + offset), 0, 0, 0x3E, 0);
                offset += 4;
            }
        }
    }
    if (failed == 0) {
        func_1503D984(identity);
        failed |= func_1503D804(identity);
    }
    if (failed == 0) {
        if (((config != NULL) && (*(u32 *)(config + 0x18) & 0x4000)) ||
            (flags & 1)) {
            if (func_150028BC(identity) != 0) {
                failed |= 8;
            }
        }
    }
    if (failed == 0) {
        failed |= func_1503D774(identity, 0);
        if (failed == 0) {
            failed |= func_1503D660(identity, 0);
        }
    }
    if (failed != 0) {
        if (D_800C6360[identity] != NULL) {
            func_10004074(D_800C6360[identity]);
        }
        func_1503DD1C(identity);
        cleanupSlot = &D_800C5C08[identity];
        if (*cleanupSlot != NULL) {
            func_10004074(*cleanupSlot);
            *cleanupSlot = NULL;
        }
        cleanupSlot = &D_800C6070[identity];
        if (*cleanupSlot != NULL) {
            func_10004074(*cleanupSlot);
            *cleanupSlot = NULL;
        }
        if (*mainSlot != NULL) {
            func_10004074(*mainSlot - 0x38);
            *mainSlot = NULL;
        }
    }
    return failed;
}

s32 func_1503D368() {
    return 0;
}

void func_1503D438(u32 *arg0, u32 arg1) {
    u32 temp_v0 = *arg0;

    if ((temp_v0 != 0) && ((temp_v0 & 0x0F000000) == 0)) {
        *arg0 = temp_v0 + arg1;
    }
}

void func_1503D45C(s32 *arg0, s32 arg1) {
    while (*arg0 != 0) {
        *arg0 = *arg0 + arg1;
        arg0 = arg0 + 2;
    }
}

void func_1503D484(u8 *arg0, s32 arg1) {
    u8 *start = arg0;

    while (*(u16 *)arg0 != 999) {
        if (*(u32 *)(arg0 + 4) != 0) {
            func_1503D438((u32 *)(arg0 + 4), (u32)start);
        }
        arg0 += 8;
    }

    D_800C5A90[arg1] = (s32)(arg0 - start) >> 3;
}

s32 func_1503D510() {
    return 0;
}

s32 func_1503D5F0(s32 value) {
    s32 group;
    s32 i;

    for (group = 0; group < 5; group++) {
        for (i = 0; i < D_80098888[group]; i++) {
            if (value == D_80084410[group][i]) {
                return D_80084410[group][0];
            }
        }
    }

    return value;
}

s32 func_1503D660() {
    return 0;
}

s32 func_1503D774(s32 arg0, s32 arg1) {
    s32 output;
    struct124 **slot = &D_800D1C90[arg0];
    void *loaded;

    if (*slot != NULL) {
        return 0;
    }

    loaded = func_1502B6BC(&output, 2, 0, 2, 0x11, arg0);
    if (loaded == 0) {
        *slot = NULL;
        return 2;
    }

    *slot = (struct124 *)loaded;
    *slot = *(struct124 **)loaded;
    return 0;
}

s32 func_1503D804() {
    return 0;
}

s32 func_1503D984() {
    return 0;
}

s32 func_1503DA3C(s32 arg0, u32 arg1) {
    u8 *entry = D_800D19A0[arg0];
    RecordByteBuffer *buffer = (RecordByteBuffer *)(entry - sizeof(RecordByteBuffer));
    u8 *data;
    s32 result;

    if (entry == NULL) {
        return 0xFF;
    }
    if (buffer->count < arg1 + 1) {
        return 0xFF;
    }
    data = buffer->data;
    result = (data != NULL) ? data[arg1] : 0xFF;
    return result;
}

extern u8 *D_800C5C08[];
extern u16 D_800C5628[];
extern u32 *D_800C5338[];
extern u16 D_800C4778[];
extern u32 *D_800C4488[];
s32 func_1503CF20(s32, s32, u8 *, s32, s32);
s32 func_1503DC3C(s32);
s32 func_150028BC(s32);
void func_1510CE60(u32, s32, s32, s32, s32);
s32 func_15084044(u8 *, s32);

s32 func_1503DA9C(u8 *actor, s32 identity, s32 channel, s32 extras) {
    u8 *config;
    s32 index;
    s32 result;
    s32 tableOffset;

    tableOffset = identity * 4;
    config = *(u8 **)(actor + 0x144);
    if ((*(u8 **)((u8 *)D_800D19A0 + tableOffset)) == NULL) {
        result = func_1503CF20(identity, 0, config, extras, actor[0xAC]);
    } else {
        result = 0;
        if (((config != NULL) && (*(u32 *)(config + 0x18) & 0x4000)) ||
            (actor[0xAC] & 1)) {
            if ((*(u8 **)((u8 *)D_800C5C08 + tableOffset)) == NULL) {
                func_150028BC(identity);
            }
        }
        if ((extras != 0) && (D_800C5628[identity] != 0)) {
            if (*(*(u32 **)((u8 *)D_800C5338 + tableOffset)) < 0x10000000U) {
                result = func_1503DC3C(identity);
                for (index = 0; index < D_800C4778[identity]; index++) {
                    func_1510CE60((*(u32 **)((u8 *)D_800C4488 + tableOffset))[index], 0, 0, 0x3E, 0);
                }
            }
        }
    }
    if (result == 0) {
        result = func_15084044(actor, channel);
    }
    return result;
}

u32 func_1510D0EC(u32, s32, s32, s32);

s32 func_1503DC3C(s32 identity) {
    u16 *count;
    s32 failed;
    s32 index;
    u32 **slot;
    u32 *cursor;
    s32 offset;
    u32 loaded;

    count = &D_800C5628[identity];
    failed = 0;
    index = 0;
    if (*count > 0) {
        slot = &D_800C5338[identity];
        cursor = *slot;
        offset = 0;
        do {
            loaded = func_1510D0EC(cursor[1], 0, 0x3E, 1);
            *(u32 *)((u8 *)*slot + offset) = loaded;
            cursor = (u32 *)((u8 *)*slot + offset);
            if (*cursor == 0x80000000U) {
                failed |= 0x10;
            }
            index++;
            offset += 12;
            cursor += 3;
        } while (index < *count);
    }
    return failed;
}

s32 func_1503DD1C() {
    return 0;
}
