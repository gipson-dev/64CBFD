#include <ultra64.h>
#include "stdarg.h"

#include "functions.h"
#include "variables.h"

#include "macros.h"

/* Generated placeholder declarations. */
s32 func_1502AB04();
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

void func_1502AAF0(void) {
}

void func_1502AAF8(s32 arg0) {
}

/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502AB04.s. */
s32 func_1502AB04() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502AC88.s. */
s32 func_1502AC88(u32 arg0, s32 arg1, u32 *arg2) {
    return 0;
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
/* Non-matching C placeholders for asm/nonmatchings/game_57FA0/func_1502B350.s. */
void *func_1502B350(u32 arg0, u32 arg1, s32 *arg2) {
    return NULL;
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
    va_list path;
    s32 fallbackSize;
    /* Retail leaves this undefined for zero depth or an unwritten lookup result. */
    u32 descriptor;
    u32 offset;
    s32 component;
    void *result;

    if (size == NULL) {
        size = &fallbackSize;
    }
    *size = 1;
    offset = (u32)D_AB1950;
    va_start(path, depth);
    if (depth != 0) {
        do {
            component = va_arg(path, s32);
            if (*size != 0) {
                offset += func_1502AC88(offset, component, &descriptor);
            }
            *size = descriptor & 0x0FFFFFFF;
        } while (--depth != 0);
    }
    va_end(path);
    if (*size != 0) {
        result = func_1502B350(offset, descriptor, size);
        if (*size != 0 && result != NULL) {
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
