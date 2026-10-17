#include <ultra64.h>
#include "structs.h"
#include <PR/sched.h>

extern u8 D_800BE9C0, D_800BE617, D_800BEBA0;
extern s16 D_800BEAA8;
extern s32 D_80082FA0;
extern Gfx *D_800BE9C8[], *D_800BE9D0, *D_800BE9D8[];
extern OSScTask *D_800BEAD4, D_800BEAD8[];
extern u64 D_100290D0[], D_100291A0[], D_800C1060[], D_800BEBB0[], D_800CBE10[], D_8003A5E8[];
extern u64 *D_800BEAD0, *D_800BEB9C, *D_80038090, *D_80038094;
extern void *D_8002AAE8[];
extern OSMesgQueue D_8003B1E8, D_800BEA10;
extern OSScMsg D_800BEA68[];
void func_1501A39C(void);
/* Each row is text start/end, then data start/end, relative to the ROM base. */
extern s32 D_80084078[];
extern struct104 *D_800B0DF0;
extern s32 D_800BEB98;
extern s8 D_80084070, D_80084074;
extern u8 D_2D4B0[];
s32 func_10004514(s32 devAddr, void *dramAddr, u32 size, s32 block);

void func_1501CC3C(void);

extern u16 *D_800C35C8[];
extern u8 *D_800C35F0[];

extern void (*D_80086014[])();
extern f32 D_800C3594;
extern f32 D_800C35A0;
extern s16 D_800C358C[];
extern s16 D_800C3598[];
extern u8 D_800C3663;
extern u16 *D_800C35D8[];
extern u8 D_800C363A[];
extern u8 *D_800C3960[][30];

/* Non-matching placeholders for the text-only asm slice asm/49D30.s. */

extern struct163 D_800C3CA0[3];
extern struct163 D_800C3D48;
extern void func_1516D2E0(u8 *arg0);
extern void func_1516D328(u8 *arg0);

extern u8 D_800C3510[];
extern u8 D_800C3518[][25];
extern u8 D_800C354A[];
extern u8 D_800C3550[][30];
extern u8 D_800C3670;
extern s64 D_800C3A60[];
extern s32 D_800C3668[];
extern void *func_1502B6BC(s32 *, s32, s32 *, s32, ...);
u8 *func_151149AC(u8);

/* Submit the current graphics task, repairing an out-of-range command cursor. */
void func_1501C880(s32 unused, s32 swapBuffers) {
    s32 capacity;
    Gfx *start;
    s32 used;
    s32 available;

    capacity = (s32)((u32)D_800BE9C8[1] - (u32)D_800BE9C8[0]) >> 3;
    D_800BEAD4 = &D_800BEAD8[D_800BE9C0];
    D_800BEAD4->next = 0;
    start = D_800BE9C8[D_800BE9C0];
    used = (s32)((u32)D_800BE9D0 - (u32)start) >> 3;
    if (used < 0 || capacity < used) {
        func_1501A39C();
        D_800BE9D0 = D_800BE9D8[D_800BE9C0];
        gDPFullSync(D_800BE9D0++);
        gSPEndDisplayList(D_800BE9D0++);
        start = D_800BE9C8[D_800BE9C0];
        used = (s32)((u32)D_800BE9D0 - (u32)start) >> 3;
    }
    available = capacity - 400;
    if (used < 0 || available < used) {
        D_800BE9D0 = (Gfx *)((u32)start + ((u32)available << 3));
        gDPFullSync(D_800BE9D0++);
        gSPEndDisplayList(D_800BE9D0++);
        start = D_800BE9C8[D_800BE9C0];
    }
    D_800BEAD4->list.t.data_ptr = (u64 *)start;
    D_800BEAD4->list.t.data_size = (u32)((s32)((u32)D_800BE9D0 - (u32)D_800BE9C8[D_800BE9C0]) >> 3) << 3;
    func_1501CC3C();
    D_800BEAD4->list.t.type = M_GFXTASK;
    D_800BEAD4->list.t.flags = OS_TASK_LOADABLE;
    D_800BEAD4->list.t.ucode_boot = D_100290D0;
    D_800BEAD4->list.t.ucode_boot_size = (u32)D_100291A0 - (u32)D_100290D0;
    if (D_800BEBA0 != 0) {
        D_800BEAD4->list.t.ucode = D_800C1060;
        D_800BEAD4->list.t.ucode_data = D_800BEB9C;
    } else {
        D_800BEAD4->list.t.ucode = D_800BEBB0;
        D_800BEAD4->list.t.ucode_data = D_800BEAD0;
    }
    D_800BEAD4->list.t.ucode_data_size = SP_UCODE_DATA_SIZE;
    D_800BEAD4->list.t.dram_stack = D_800CBE10;
    D_800BEAD4->list.t.dram_stack_size = 0x400;
    D_800BEAD4->list.t.output_buff = D_80038090;
    D_800BEAD4->list.t.output_buff_size = D_80038094;
    D_800BEAD4->list.t.yield_data_ptr = D_8003A5E8;
    D_800BEAD4->list.t.yield_data_size = OS_YIELD_DATA_SIZE;
    D_800BEAD4->flags = OS_SC_NEEDS_RDP | OS_SC_NEEDS_RSP | OS_SC_LAST_TASK;
    if (swapBuffers != 0) {
        D_800BEAD4->flags |= OS_SC_SWAPBUFFER;
    }
    if (D_800BE617 != 0) {
        D_800BEAD4->flags |= ((u32)D_80082FA0 + 1U) << 16;
        D_800BE617 = 0;
    }
    D_800BEAD4->msgQ = &D_800BEA10;
    D_800BEAD4->msg = &D_800BEA68[D_800BE9C0];
    D_800BEAD4->framebuffer = D_8002AAE8[D_800BE9C0];
    osWritebackDCacheAll();
    osSendMesg(&D_8003B1E8, D_800BEAD4, OS_MESG_BLOCK);
    if (swapBuffers != 0) {
        D_800BE9C0 ^= 1;
    }
    D_800BEAA8++;
}

/* Load both selected microcode pairs when their signed cache bytes differ. */
void func_1501CC3C(void) {
    s32 variant;
    s32 pairedOffset;
    s32 *range;

    variant = D_800B0DF0->pad2B[0];
    if ((s32)variant >= 2) {
        variant -= 2;
        pairedOffset = 0;
    } else {
        pairedOffset = 4;
    }
    if (D_800BEB98 == 1) {
        variant += 2;
    }
    range = &D_80084078[variant * 4];
    if (variant != D_80084070 || pairedOffset != D_80084074) {
        func_10004514((s32)(range[0] + (u32)D_2D4B0), D_800C1060, range[1] - range[0], 1);
        D_800BEB9C = (u64 *)((u32)D_800C1060 + (s32)(range[1] - range[0]));
        func_10004514((s32)(range[2] + (u32)D_2D4B0), D_800BEB9C, range[3] - range[2], 1);
        D_80084070 = variant;
        range = &D_80084078[(variant + pairedOffset) * 4];
        D_80084074 = pairedOffset;
        func_10004514((s32)(range[0] + (u32)D_2D4B0), D_800BEBB0, range[1] - range[0], 1);
        D_800BEAD0 = (u64 *)((u32)D_800BEBB0 + (s32)(range[1] - range[0]));
        func_10004514((s32)(range[2] + (u32)D_2D4B0), D_800BEAD0, range[3] - range[2], 1);
    }
}

void func_1501CDC0(s32 index) {
    s32 count = 0;
    s32 offset;
    u8 **slot;

    if (D_800C363A[index] > 0) {
        slot = D_800C3960[index];
        do {
            offset = 0;
            do {
                (*slot)[offset] = 0xFF;
                (*slot)[offset + 1] = 0xFF;
                (*slot)[offset + 2] = 0xFF;
                (*slot)[offset + 3] = 0xFF;
                offset += 4;
            } while (offset != 16);
            count++;
            slot++;
        } while (count < D_800C363A[index]);
    }
}

s32 func_1501CE54() {
    return 0;
}

s32 func_1501CFF8(s32 arg0) {
    s32 sum = 0;
    s32 i = 0;

    if (D_800C363A[arg0] > 0) {
        u16 *ptr = D_800C35D8[arg0];

        do {
            sum += *ptr;
            i += 1;
            ptr += 1;
        } while (i < D_800C363A[arg0]);
    }
    return sum;
}

s32 func_1501D044() {
    return 0;
}

s32 func_1501D1D4(s32 arg0, s32 arg1, s32 index) {
    s32 result1;
    s32 result0;
    s32 result;

    result = (s32)func_1502B6BC(&result0, 0, &result1, 3, 6, arg0, arg1);
    if (result != 0) {
        D_800C3668[index] = result;
    } else {
        D_800C3668[index] = 0;
    }
    return result;
}

void func_1501D258(s32 index, s32 bit) {
    if (D_800C3670 == 0) {
        D_800C3A60[index] |= 1LL << bit;
    }
}

s32 func_1501D2C4(s32 index, s32 bit) {
    if (D_800C3670 != 0) {
        return 1;
    }
    if (D_800C3A60[index] & (1LL << bit)) {
        return 1;
    }
    return 0;
}

s32 func_1501D348() {
    return 0;
}

s32 func_1501DAAC() {
    return 0;
}

s32 func_1501DE18() {
    return 0;
}

s32 func_1501DF04() {
    return 0;
}

s32 func_1501E05C() {
    return 0;
}

s32 func_1501E1B4() {
    return 0;
}

s32 func_1501E2F8() {
    return 0;
}

s32 func_1501E400() {
    return 0;
}

s32 func_1501E540() {
    return 0;
}

s32 func_1501E73C() {
    return 0;
}

s32 func_1501E81C() {
    return 0;
}

s32 func_1501EA18() {
    return 0;
}

s32 func_1501EC38() {
    return 0;
}

s32 func_1501F72C() {
    return 0;
}

s32 func_1501FC8C() {
    return 0;
}

s32 func_1501FE68() {
    return 0;
}

s32 func_1501FFE8() {
    return 0;
}

s32 func_15020388() {
    return 0;
}

s32 func_15020878() {
    return 0;
}

s32 func_15020EC4() {
    return 0;
}

s32 func_1502178C() {
    return 0;
}

s32 func_15021DB8() {
    return 0;
}

s32 func_15022024() {
    return 0;
}

void func_15022190(s16 arg0, s16 arg1, s16 arg2, f32 arg3) {
    D_800C3594 = arg3;
    D_800C358C[0] = arg0;
    D_800C358C[1] = arg1;
    D_800C358C[2] = arg2;
    D_800C3663 = 1;
}

void func_150221E8(s16 arg0, s16 arg1, s16 arg2, f32 arg3) {
    D_800C35A0 = arg3;
    D_800C3598[0] = arg0;
    D_800C3598[1] = arg1;
    D_800C3598[2] = arg2;
}

void func_15022234(s32 arg0) {
    D_800C3510[arg0] = 0;
}

void func_15022248(s32 arg0) {
    D_800C354A[arg0] = 0;
}

void func_1502225C(s32 value, s32 group) {
    s32 i = 0;
    u8 *count = &D_800C3510[group];
    s32 count_value = *count;
    s32 limit = count_value;

    if (count_value > 0) {
        do {
            if (value == D_800C3518[group][i]) {
                return;
            }
            i++;
        } while (i < limit);
    }

    D_800C3518[group][count_value] = value;
    *count = count_value + 1;
}

s32 func_150222E0() {
    return 0;
}

s32 func_15022398() {
    return 0;
}

s32 func_15022528() {
    return 0;
}

void func_15022640(s32 value, s32 group) {
    s32 i = 0;
    u8 *count = &D_800C354A[group];
    s32 count_value = *count;
    s32 limit = count_value;

    if (count_value > 0) {
        do {
            if (value == D_800C3550[group][i]) {
                return;
            }
            i++;
        } while (i < limit);
    }

    D_800C3550[group][count_value] = value;
    *count = count_value + 1;
}

void func_150226BC(s32 index, s32 group) {
    u8 *actor;
    u8 *record;

    if (D_800C35C8[group][index] == 0) {
        return;
    }
    record = D_800C35F0[group] + (u32)index * 8;
    if (*(u16 *)record != 3) {
        return;
    }
    actor = func_151149AC(record[2]);
    if (actor != NULL) {
        if (actor[0x6E] == 1) {
            func_15022640(actor[0x72], group);
            actor[0x6E] = 0;
        }
    }
}

void func_15022754(s32 index) {
    s32 i = 0;
    u8 *count = &D_800C363A[index];

    if (*count > 0) {
        do {
            func_150226BC(i, index);
            i++;
        } while (i < *count);
    }
}

void func_150227BC(s32 group) {
    s32 i = 0;
    u8 *count = &D_800C354A[group];
    s32 row_offset = group * 30;

    if (*count > 0) {
        u8 *entry = (u8 *)D_800C3550 + row_offset;

        do {
            func_151149AC(*entry)[0x6E] = 1;
            i++;
            entry++;
        } while (i < *count);
    }
}

s32 func_15022848() {
    return 0;
}

s32 func_150228E4() {
    return 0;
}

void func_15022998(s32 *arg0) {
    s32 temp_v0 = *arg0;

    if ((temp_v0 == 0x1B) || (temp_v0 == 4)) {
        void (*temp_v1)() = D_80086014[temp_v0];

        if (temp_v1 != 0) {
            temp_v1();
        }
    }
}

s32 func_150229E4() {
    return 0;
}

s32 func_15022B08() {
    return 0;
}

s32 func_15022BA4() {
    return 0;
}

s32 func_15023264() {
    return 0;
}

void func_150233BC(void) {
    bzero(D_800C3CA0, 0xA8);
}

void func_150233E4(void) {
    struct163 *entry = D_800C3CA0;

    do {
        if (entry->unk0 != 0) {
            func_1516D2E0(entry->unk34);
            entry->unk34 = NULL;
            entry->unk0 = 0;
        }
        entry++;
    } while (entry != &D_800C3D48);
}

void func_15023440(struct163 *arg0, s32 arg1) {
    if (arg1 != 0) {
        func_1516D2E0(arg0->unk34);
        arg0->unk34 = NULL;
    } else if (arg0->unkC != 0) {
        func_1516D328(arg0->unk34);
    } else {
        arg0->unk34 = NULL;
    }
    arg0->unk0 = 0;
}

s32 func_150234A4() {
    return 0;
}

s32 func_150235DC() {
    return 0;
}

s32 func_1502378C() {
    return 0;
}
