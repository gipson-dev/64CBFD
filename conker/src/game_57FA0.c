#include <ultra64.h>
#include "stdarg.h"

#include "functions.h"
#include "variables.h"

#include "macros.h"

/* Generated placeholder declarations. */
void func_1502AB04(s32 count, u32 *pairs, u32 generation, u32 address);
s32 func_1502AC88(u32 arg0, s32 arg1, u32 *arg2);
s32 func_1502AF04();
s32 func_1502B020();
s32 func_1502B110();
s32 func_1502B224();
void *func_1502B350(u32 arg0, u32 arg1, s32 *arg2);
s32 func_1502B4A8(u32 *entries, s32 count);
s32 func_1502B5C8();
void *func_1502B6BC(s32 *size, s32 count, s32 *relocated, s32 depth, ...);
s32 func_1502B8E0();
s32 func_1502B9B4();
/* End generated placeholder declarations. */

extern u8 D_AB1950[];

typedef struct AssetTableCache57FA0 {
    u32 address;
    u32 generation;
    u32 offset;
    u32 descriptor;
} AssetTableCache57FA0;

extern u32 D_800C3D60;
extern AssetTableCache57FA0 D_800C3D68[16];
void *allocate_memory(s32, s32, s32, s32);
s32 func_10006240(void *, void *, u32);

void func_1502AAF0(void) {
}

void func_1502AAF8(s32 arg0) {
}

void func_1502AB04(s32 count, u32 *pairs, u32 generation, u32 address) {
    u32 i;

    if (count != 0) {
        bcopy(&D_800C3D68[count], D_800C3D68, (16 - count) * 16);
    }
    for (i = 16 - (u32)count; i < 16; i++) {
        D_800C3D68[i].offset = pairs[0];
        D_800C3D68[i].descriptor = pairs[1];
        D_800C3D68[i].address = address;
        D_800C3D68[i].generation = generation;
        pairs += 2;
        address += 8;
    }
}
s32 func_1502AC88(u32 arg0, s32 arg1, u32 *arg2) {
    AssetTableCache57FA0 saved;
    u8 storage[0x40];
    u8 *aligned;
    u32 *pairs;
    u32 address;
    u32 offset;
    u32 i;
    u32 j;

    address = (arg0 + (u32)arg1 * 8) | 0x80000000;
    for (i = 0; i < 16; i++) {
        if (D_800C3D68[i].address == address) {
            saved = D_800C3D68[i];
            for (j = i; j < 15; j++) {
                D_800C3D68[j] = D_800C3D68[j + 1];
            }
            D_800C3D68[15] = saved;
            D_800C3D68[15].generation = D_800C3D60;
            *arg2 = D_800C3D68[15].descriptor;
            return D_800C3D68[15].offset;
        }
    }
    D_800C3D60++;
    aligned = (u8 *)(((u32)storage + 15) & ~0xF);
    func_10004514(address & 0x7FFFFFF0, aligned, ((address & 0xE) + 0x1F) & ~0xF, 1);
    pairs = (u32 *)(aligned + (address & 0xF));
    offset = pairs[0];
    *arg2 = pairs[1];
    func_1502AB04(2, pairs, D_800C3D60, address);
    return offset;
}
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502AF04.s. */
s32 func_1502AF04() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B020.s. */
s32 func_1502B020() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B110.s. */
s32 func_1502B110() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B224.s. */
s32 func_1502B224() {
    return 0;
}
void *func_1502B350(u32 arg0, u32 arg1, s32 *arg2) {
    u32 amount;
    u32 expanded;
    void *compressed;
    void *result;

    amount = ((arg1 & 0x0FFFFFFF) + 1) & ~1;
    compressed = allocate_memory(amount, 1, 2, 2);
    result = compressed;
    if (compressed == NULL) {
        return NULL;
    }
    func_10004514(arg0, compressed, (amount + 15) & ~0xF, 1);
    if ((arg1 & 0x70000000) == 0x10000000) {
        expanded = *(u32 *)compressed & 0x7FFFFFFF;
        *arg2 = expanded;
        result = NULL;
        amount = 0;
        if (expanded != 0 && expanded < 1000000) {
            result = allocate_memory(expanded, 1, 2, 2);
            if (result != NULL) {
                amount = func_10006240(compressed, result, D_8003809C);
            }
        }
        func_10004074(compressed);
    }
    *arg2 = amount;
    return result;
}
s32 func_1502B4A8(u32 *entries, s32 count) {
    u32 *cursor;
    u32 base;
    s32 i;

    if (count == 0) {
        cursor = entries;
        do {
            count++;
            if (cursor[1] & 0x80000000) {
                break;
            }
            cursor += 2;
        } while (1);
    }
    base = (u32)entries;
    for (i = 0; i < count; i++) {
        entries[i * 2 + 1] &= 0x0FFFFFFF;
        if (entries[i * 2] == 0xFFFFFFFF || entries[i * 2 + 1] == 0) {
            entries[i * 2] = 0;
        } else {
            entries[i * 2] += base;
        }
    }
    return count;
}
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B5C8.s. */
s32 func_1502B5C8() {
    return 0;
}
void *func_1502B6BC(s32 *size, s32 count, s32 *relocated, s32 depth, ...) {
    s32 *target;
    va_list path;
    s32 fallbackSize;
    s32 component;
    u32 offset;
    /* Retail leaves this undefined for zero depth or an unwritten lookup result. */
    u32 descriptor;
    void *result;

    target = &fallbackSize;
    if (size != NULL) {
        target = size;
    }
    *target = 1;
    offset = (u32)D_AB1950;
    va_start(path, depth);
    if (depth != 0) {
        do {
            component = va_arg(path, s32);
            if (*target != 0) {
                offset += func_1502AC88(offset, component, &descriptor);
            }
            *target = descriptor & 0x0FFFFFFF;
        } while (--depth != 0);
    }
    va_end(path);
    if (*target != 0) {
        result = func_1502B350(offset, descriptor, target);
        if (*target != 0 && result != NULL) {
            count = func_1502B4A8(result, count);
        } else {
            count = 0;
        }
        if (relocated != NULL) {
            *relocated = count;
        }
    } else {
        result = NULL;
    }
    return result;
}
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B7F0.s. */
s32 func_1502B7F0(s32*arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return 0;
}
// void func_1502B7F0(s32 *arg0, s32 arg1, s32 arg2, s32 arg3) {
//     s32 sp38;
//     s32 sp34;
//     s32 temp_s1;
//     s32 offset;
//     s32 i;
//
//     sp38 = 1;
//     offset = &D_00AB1950; // 0xAB1950 - assets offsets table
//     temp_s1 = &arg2;
//
//     i = arg1;
//     if (i != 0) {
//         do {
//             temp_s1 = ALIGN4(temp_s1);
//             if (sp38 != 0) {
//                 offset += func_1502AC88(offset, temp_s1, &sp34);
//             }
//             sp38 = sp34 & 0xFFFFFFF;
//             temp_s1 += 1;
//         } while (i-- != 0);
//     }
//
//     if (sp38 != 0) {
//         *arg0 = func_1502B350(offset, sp34, &sp38);
//     } else {
//         *arg0 = 0;
//     }
// }

/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B8E0.s. */
s32 func_1502B8E0() {
    return 0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B9B4.s. */
s32 func_1502B9B4() {
    return 0;
}
// NON-MATCHING: maybe 50% there?
// s32 func_1502B9B4(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
//
//     s32 stack2[2];
//     s32 stack1[2];
//     s32 stack0[5];
//
//     s32 more;
//     s32 offset;
//     s32 *tmp;
//     s32 i;
//
//     more = 1;
//     offset = &D_00AB1950;
//     tmp = &arg1;
//
//     for (i = arg0; i != 0; i--) {
//         tmp = ALIGN4(tmp) + 4;
//         if (more != 0) {
//             offset += func_1502AC88(offset, tmp - 4, &stack0);
//         }
//         more = *stack0 & 0xFFFFFFF;
//     }
//
//     if (more != 0) {
//         more = ALIGN2(stack0[0] & 0xFFFFFFF);
//         if ((*stack0 & 0x70000000) == 0x10000000) {
//             if (((s32) &stack1 & 8) != 0) {
//                 *stack1 = &stack2;
//             }
//             func_10004514(offset, stack1, 0x10, 1); // decompress?
//             more = *stack1;
//         }
//     }
//
//     return more;
// }
