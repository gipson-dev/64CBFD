#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_10003ACC(s32 arg0, s32 arg1, s32 arg2);
/* End generated placeholder declarations. */

void func_100039C0(void) {
    OSViMode *mode;

    D_800BE620 = 292; // screen width px
    D_800BE624 = 216; // screen height px
    D_800380A0 = (f32) D_800BE620 / 292.0f;
    D_800380A4 = (f32) D_800BE624 / 216.0f;
    D_800BE9C4 = allocate_memory(D_800BE620 * D_800BE624 * 2, 255, 3, 0);
    func_10003ACC(0, 0, 0);
    func_15015FBC(D_800BE620, D_800BE624);
    if (D_80000300 == 2) {
        mode = &D_8002ABE0;
    } else {
        mode = &D_8002AB90;
    }
    osViSetMode(mode);
    osViSwapBuffer((void *)D_8002AAE8[D_800BE9C0 ^ 1]);
}

void func_10003ACC(s32 arg0, s32 arg1, s32 arg2) {
    s16 *framebuffer;
    s16 *remainderCursor;
    s16 *bulkCursor;
    s32 count;
    s32 index;
    s32 remainder;

    framebuffer = (s16 *)D_8002AAE8[0];
    index = 0;
    count = (D_800BE620 * D_800BE624 * 2) >> 1;
    if (framebuffer != NULL) {
        if (count > 0) {
            do {
                index++;
                framebuffer++;
                framebuffer[-1] = ((arg0 << 8) & 0xF800) |
                                  ((arg1 << 3) & 0x07C0) |
                                  ((arg2 >> 2) & 0x003E) | 1;
            } while (index < count);
            index = 0;
        }

        if (count > 0) {
            arg0 = ((arg0 << 8) & 0xF800) |
                   ((arg1 << 3) & 0x07C0) |
                   ((arg2 >> 2) & 0x003E) | 1;
            remainder = count & 3;
            if (remainder != 0) {
                remainderCursor = (s16 *)D_8002AAE8[1] + index;
                do {
                    index++;
                    *remainderCursor++ = arg0;
                } while (remainder != index);
            }
            if (index != count) {
                bulkCursor = (s16 *)D_8002AAE8[1] + index;
                do {
                    index += 4;
                    bulkCursor[1] = arg0;
                    bulkCursor[2] = arg0;
                    bulkCursor[3] = arg0;
                    bulkCursor += 4;
                    bulkCursor[-4] = arg0;
                } while (index != count);
            }
        }
    }
}
