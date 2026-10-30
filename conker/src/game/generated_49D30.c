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
u8 *func_15083E90(u8);
void func_1507E7E4(u8 *, u8, u8, u16, s32);

extern void (*D_80086014[])();
extern f32 D_800C3594;
extern f32 D_800C35A0;
extern s16 D_800C358C[];
extern s16 D_800C3598[];
extern u8 D_800C3663;
extern u16 *D_800C35D8[];
extern u8 D_800C363A[];
extern u8 *D_800C3960[][30];

typedef struct {
    u8 pad00[0xA];
    s16 maximum;
    u8 pad0C[6];
    s16 overrideValue;
} RecordMaximum49D30;
extern s32 D_800C3640[];
extern RecordMaximum49D30 *D_800C3688[][30];
extern u16 *D_800C35D0[];
extern u8 *D_800C3778[][30];

extern s32 D_800C35B8[], D_800C35B0[];
extern u8 D_800C35C0[], D_800C35EA[];
extern u8 D_800C3654[], D_800C3656[], D_800C3658[], D_800C365A[];
extern u8 D_800C365C[], D_800C365E[], D_800C3660[];
extern u8 D_800C35F8, D_800C3638, D_800C3662, D_800C3C8C, D_800C3C8D;
extern u8 D_800C35C2, D_800C3A58, D_800C3C8B, D_800C3680, D_800C3672, D_800C3C9D, D_8008FD84;
extern s8 D_800C3C8A;
extern s16 D_800C3C8E, D_800C3C9E;
extern s32 D_800C367C;
extern void *D_800C3D50;
extern f32 D_800C3648, D_800C364C, D_800C3650, D_800C35A4, D_800C3674, D_800C3678;
extern f32 D_800969C0;
void func_150233BC(void);

typedef struct {
    u16 activeCount;
    u16 fallbackCount;
    u16 preferredCount;
    u16 auxiliaryCount;
} SequenceHeader49D30;
typedef struct {
    u8 *data;
    u32 bytes;
} SequenceDescriptor49D30;
typedef struct {
    u8 pad00[4];
    u32 *items;
    u8 pad08[0x30];
    u8 *scratch;
    u8 pad3C[4];
} SequenceRuntime49D30;
extern u8 D_800C35C4, D_800C35C5, D_800C35E8[], D_800C3C90, D_800C3C98;
extern s8 D_800C35A8;
extern s32 D_800BE9F0, D_800C3C94;
extern u8 **D_800C35E0[];
extern SequenceRuntime49D30 *D_800C3A50[];
extern u8 *D_800C3958[], *D_800C3868[][30];
extern s16 D_800C3C9A;
extern u8 D_800DBFF4;
extern void (*D_800840FC[])(s32, s32, s32, s32);
s32 allocate_memory(s32, s32, s32, s32);
void func_1501C730(s32, s32, s32, s32, s32);
s32 func_15022BA4();
s32 func_15020388();
s32 func_150238D0();
void func_15022234(s32);
void func_15022248(s32);
s32 func_1501E81C();
s32 func_150242F8();
s32 func_1501EC38();
void func_15022848(s32 index);
void func_15022754(s32);
s32 func_15022528();
s32 func_15020EC4();
void func_1501DAAC(s32 slot);
typedef struct {
    u8 pad00[5];
    s8 colorIndex;
    s16 mode;
} SequenceEvent49D30;
extern u8 D_800C3C99, D_800C3C9C, D_800C35A9, D_800C35AA;
extern u8 D_80084110[][3];
s32 func_15023BB0(u8 *, s32, s32, SequenceEvent49D30 **,
    s32, s32, s32, s32, s32, s32, s32);
void func_1517EE40(s32, s32, s32, s32, s8, s32);





/* Non-matching placeholders for the text-only asm slice asm/49D30.s. */

extern struct163 D_800C3CA0[3];
extern struct163 D_800C3D48;
extern void func_1516D2E0(u8 *arg0);
extern void func_1516D328(u8 *arg0);

extern u8 D_800C3510[];
extern u8 D_800C3518[][25];
extern struct127 D_800CC2D0[];
void func_15060F28(struct127 *, s32);
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

/* Prefer an explicit override or primary maximum before scanning fallback tails. */
void func_1501CE54(s32 slot) {
    s32 *maximum;
    s32 count;
    u16 *primary;
    s32 i;
    s32 offset;
    u16 *enabled;
    s32 primaryValue;
    s32 value;
    u16 active;
    u16 entries;

    maximum = &D_800C3640[slot];
    *maximum = 0;
    count = D_800C363A[slot];
    if (count != 0) {
        primary = D_800C35D8[slot];
        if (primary[0] >= 4) {
            value = D_800C3688[slot][0]->overrideValue;
            if (value != -9999) {
                *maximum = value;
                return;
            }
        }
        /* In the preferred pass, value records whether the output was updated. */
        value = 0;
        i = 0;
        if (count > 0) {
            enabled = D_800C35C8[slot];
            offset = 0;
            do {
                active = *enabled++;
                if (active != 0 && *(u16 *)((u8 *)primary + offset) != 0) {
                    primaryValue = D_800C3688[slot][i]->maximum;
                    if (*maximum < primaryValue) {
                        *maximum = primaryValue;
                        value = 1;
                    }
                }
                i++;
                offset += 2;
            } while ((s32)(i < count) != 0);
        }
        if (!value) {
            i = 0;
            if (count > 0) {
                enabled = D_800C35C8[slot];
                offset = 0;
                do {
                    active = *enabled++;
                    if (active != 0) {
                        entries = *(u16 *)((u8 *)D_800C35D0[slot] + offset);
                        if (entries != 0) {
                            value = *(s16 *)(D_800C3778[slot][i] + entries * 8 - 2);
                            if (*maximum < value) {
                                *maximum = value;
                            }
                        }
                    }
                    i++;
                    offset += 2;
                } while ((s32)(i < count) != 0);
            }
        }
    }
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

/* Reset the selected slot and shared sequence state before clearing actor records. */
void func_1501D044(s32 slot) {
    /* Capture the shared limit before resetting indexed state. */
    f32 limit = D_800969C0;

    D_800C35B8[slot] = -100;
    D_800C35B0[slot] = 0;
    D_800C35C0[slot] = 0;
    D_800C3C8E = 0;
    D_800C363A[slot] = 0;
    D_800C35EA[slot] = 0;
    D_800C3D50 = NULL;
    D_800C35F8 = 255;
    D_800C3648 = 0.0f;
    D_800C364C = 0.0f;
    D_800C3650 = 0.0f;
    D_800C3654[slot] = 0;
    D_800C3656[slot] = 0;
    D_800C3658[slot] = 1;
    D_800C365A[slot] = 0;
    D_800C365C[slot] = 0;
    D_800C365E[slot] = 0;
    D_800C3660[slot] = 0;
    D_800C3638 = 0;
    D_800C3662 = 0;
    D_800C3C8C = 0;
    D_800C3C8D = 0;
    D_800C35C2 = 0;
    D_800C3A58 = 0;
    D_800C35A4 = 0.0f;
    D_800C3C8A = -1;
    D_800C3C8B = 0;
    D_800C3674 = limit;
    D_800C3678 = limit;
    D_800C367C = 0;
    D_800C3680 = 0;
    D_800C3672 = 0;
    D_800C3C9D = 100;
    D_800C3C9E = -1;
    func_150233BC();
    /* These flags are cleared only after the actor-table helper returns. */
    D_8008FD84 = 0;
    D_800C3670 = 0;
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

/* Allocate and publish a slot's record groups, then run its setup providers. */
void func_1501D348(s32 scene, s32 sequence, s32 slot, s32 hook, s32 parameter) {
    s32 value;
    SequenceDescriptor49D30 *bundle;
    SequenceHeader49D30 *header;
    s32 i;
    s32 cursor;
    s32 bytes;

    /* Retail reuses this word for status, sizes, allocation results and flags. */
    value = D_800C35EA[slot];
    if (value == 1 || D_800C35C4 != 0) return;
    D_800C3C90 = hook;
    D_800C3C94 = parameter;
    if (scene != D_800BE9F0) {
        D_800C35C4 = (u32)sequence + 1U;
        func_1501C730(1, scene, 0, 0, 0);
        value = 1;
        if (D_800C35EA[slot] != 0) D_800C35C5 = 0;
        else D_800C35C5 = value;
        return;
    }
    D_800C35E8[slot] = sequence;
    if (value != 2) {
        D_800C35A8 = D_800BE9F0;
        D_800C3C98 = sequence;
    }
    func_1501D044(slot);
    if (func_1501D1D4(scene, sequence, slot) == 0) return;
    bundle = (SequenceDescriptor49D30 *)D_800C3668[slot];
    header = (SequenceHeader49D30 *)bundle[0].data;
    D_800C35C8[slot] = (void *)allocate_memory(header->activeCount * 2, 1, 0, 0);
    cursor = 1;
    for (i = 0; i < header->activeCount; i++, cursor++) {
            (D_800C35C8[slot])[i] = bundle[cursor].bytes >> 3;
    }
    cursor = 1;
    value = header->fallbackCount;
    if (value < header->activeCount) value = header->activeCount;
    bytes = value * 2;
    D_800C35D0[slot] = (void *)allocate_memory(bytes, 1, 0, 0);
    bzero(D_800C35D0[slot], bytes);
    value = header->preferredCount;
    if (value < header->activeCount) value = header->activeCount;
    bytes = value * 2;
    D_800C35D8[slot] = (void *)allocate_memory(bytes, 1, 0, 0);
    bzero(D_800C35D8[slot], bytes);
    D_800C35E0[slot] = (void *)allocate_memory(header->auxiliaryCount * 4, 1, 0, 0);
    D_800C3A50[slot] = (void *)allocate_memory(header->activeCount * 0x40, 1, 0, 0);
    for (i = 0; i < header->activeCount; i++) {
            if ((D_800C35C8[slot])[i] != 0) {
                value = allocate_memory((D_800C35C8[slot])[i] * 4, 1, 0, 0);
                (D_800C3A50[slot])[i].items = (void *)value;
                value = allocate_memory(0x194, 1, 0, 0);
                (D_800C3A50[slot])[i].scratch = (void *)value;
            }
    }
    D_800C3958[slot] = (void *)allocate_memory(header->activeCount * 0x44, 1, 0, 0);
    for (i = 0; i < header->activeCount; i++) {
            D_800C3960[slot][i] = (void *)allocate_memory(0x10, 1, 0, 0);
    }
    for (i = 0; i < header->activeCount; i++) {
            (D_800C35D8[slot])[i] = 0;
            (D_800C35D0[slot])[i] = 0;
            (D_800C35C8[slot])[i] = 0;
    }
    D_800C363A[slot] = header->activeCount;
    for (i = 0; i < header->activeCount; i++) {
            (D_800C35C8[slot])[i] = bundle[cursor].bytes >> 3;
            D_800C3868[slot][i] = bundle[cursor].data;
            cursor++;
    }
    D_800C35F0[slot] = bundle[cursor].data;
    /* Retail skips another activeCount descriptors before the fallback group. */
    cursor += header->activeCount;
    for (i = 0; i < header->fallbackCount; i++) {
            (D_800C35D0[slot])[i] = bundle[cursor].bytes >> 3;
            D_800C3778[slot][i] = bundle[cursor].data;
            cursor++;
    }
    for (i = 0; i < header->preferredCount; i++) {
            (D_800C35D8[slot])[i] = bundle[cursor].bytes >> 3;
            D_800C3688[slot][i] = (RecordMaximum49D30 *)bundle[cursor].data;
            cursor++;
    }
    for (i = 0; i < header->auxiliaryCount; i++) {
            (D_800C35E0[slot])[i] = bundle[cursor + i].data;
    }
    if (hook != 0) D_800840FC[hook](scene, sequence, slot, parameter);
    D_800C3C9A = func_1501CFF8(slot);
    D_800C3D50 = (void *)allocate_memory((u16)D_800C3C9A * 12, 1, 0, 0);
    D_800C35B0[slot] = 0;
    func_1501CDC0(slot);
    func_1501CE54(slot);
    func_15022BA4(slot);
    for (i = 0; i < D_800C363A[slot]; i++) {
        func_15020388(i, slot);
    }
    func_150238D0();
    value = 1;
    D_800C35EA[slot] = value;
    D_800C3638 = value;
    func_15022234(slot);
    func_15022248(slot);
    if (D_800C363A[slot] == 0) func_1501E81C(0, slot);
    func_150242F8(1, slot);
    func_1501EC38(slot);
    func_15022848(slot);
    func_15022754(slot);
    func_15022528(slot);
    func_15020EC4(slot);
    D_800DBFF4 = 4;
    func_1501DAAC(slot);
}

/* Collect live sequence flags and submit each improving color selection. */
void func_1501DAAC(s32 slot) {
    s32 best;
    s32 value;
    SequenceEvent49D30 *event;
    RecordMaximum49D30 **record;
    u8 *commands;
    u8 *count;
    s32 index;

    D_800C3C99 = 0;
    D_800C35A9 = 0;
    D_800C3C9C = 0;
    D_800C35AA = 0;
    count = &D_800C363A[slot];
    D_800C3C8E = 0;
    best = -1;
    index = 0;
    if (*count > 0) {
        record = D_800C3688[slot];
        do {
            commands = (u8 *)*record + 0x18;
            if (*record != NULL) {
                event = NULL;
                func_15023BB0(commands, 5, index, &event, 1, 0x1E, 0, 0, 0, 0, slot);
                if (event != NULL) D_800C3C99 = 1;
                event = NULL;
                func_15023BB0(commands, 5, index, &event, 1, 0x0E, 0, 0, 0, 0, slot);
                if (event != NULL) D_800C3C9C = 1;
                event = NULL;
                func_15023BB0(commands, 5, index, &event, 1, 0x68, 0, 0, 0, 0, slot);
                if (event != NULL) D_800C35AA = 1;
                event = NULL;
                func_15023BB0(commands, 5, index, &event, 1, 0x44, 0, 0, 0, 0, slot);
                if (event != NULL) D_800C35A9 = 1;
                event = NULL;
                value = func_15023BB0(commands, 5, index, &event, 1, 0x77, 0, 0, 0, 0, slot);
                if (event != NULL) D_800C3C8E = value;
                event = NULL;
                value = func_15023BB0(commands, 5, index, &event, 1, 1, 1, 0, 0, 0, slot);
                if (event != NULL && (best == -1 || value < best)) {
                    best = value;
                    if (event->mode == 1) {
                        func_1517EE40(D_80084110[event->colorIndex][0], D_80084110[event->colorIndex][1], D_80084110[event->colorIndex][2], 0, 1, 0);
                    } else {
                        func_1517EE40(D_80084110[event->colorIndex][0], D_80084110[event->colorIndex][1], D_80084110[event->colorIndex][2], 0, 0, 0);
                    }
                }
            }
            index++;
            record++;
        } while (index < *count);
    }
    D_800C35B0[slot] = (u16)D_800C3C8E;
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

void func_1507EABC(u8 *);

/* Normalize channel values of at least 10 on type-2 group actors. */
void func_1501E73C(s32 group) {
    s32 offset;
    u8 **records;
    u8 *actor;
    u8 *record;

    if (D_800C363A[group] > 0) {
        records = &D_800C35F0[group];
        offset = 0;
        do {
            record = *records + offset;
            if (*(u16 *)record == 2) {
                actor = func_15083E90(record[2]);
                if (actor == NULL) goto advance;
                {
                    if (actor[0x6C] >= 10) {
                        actor[0x6C] = 0;
                        actor[0x6A] = 0;
                    }
                    if (actor[0x6D] >= 10) {
                        actor[0x6D] = 0;
                        actor[0x6B] = 0;
                    }
                    func_1507EABC(actor);
                }
            }
advance:
            offset += 8;
        } while (offset < D_800C363A[group] * 8);
    }
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

/* Reset the actor referenced by a live type-2 group record. */
void func_150222E0(s32 index, s32 group) {
    u8 *actor;
    u8 *record;
    if (D_800C35C8[group][index] == 0) {
        return;
    }
    record = D_800C35F0[group] + (u32)index * 8;
    if (*(u16 *)record != 2) {
        return;
    }
    actor = func_15083E90(record[2]);
    if (actor != NULL) {
        actor[0x6C] = 0;
        actor[0x6D] = 0;
        actor[0x6A] = 0;
        actor[0x6B] = 0;
        *(u16 *)(actor + 0x282) = 0;
        *(u16 *)(actor + 0x27A) = 0;
        *(u16 *)(actor + 0x27C) = 0;
        *(u16 *)(actor + 0x27E) = 0;
        *(u16 *)(actor + 0x280) = 0;
        func_1507E7E4(actor, 0, 3, 0xFFFF, 10);
        actor[0x71] = 0;
    }
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

/* Run both callbacks per active entry, reloading the count after each pair. */
void func_15022848(s32 index) {
    s32 i;
    u8 *count;

    if (D_800C35EA[index] == 1) {
        D_800C3638 = 0;
        count = &D_800C363A[index];
        for (i = 0; i < *count; i++) {
            func_15022398(i, index);
            func_150222E0(i, index);
        }
        D_800C3638 = 1;
    }
}

/* Process live group actors; the helper may change the remaining entries. */
void func_150228E4(s32 group) {
    s32 index;
    u8 *cursor;

    index = 0;
    if (D_800C3510[group] > 0) {
        cursor = D_800C3518[group];
        do {
            if (D_800CC2D0[*cursor].interaction_state != 0) {
                func_15060F28(&D_800CC2D0[*cursor], 0);
            }
            index++;
            cursor++;
        } while (index < D_800C3510[group]);
    }
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

/* Find an enabled descriptor whose tag matches the selected record. */
s32 func_15022B08(s32 recordIndex, s32 category) {
    extern u8 *D_800DBEF4;
    s32 i = 0;
    u16 *enabled;

    if (D_800C363A[category] > 0) {
        enabled = D_800C35C8[category];
        do {
            if (*enabled != 0) {
                if (D_800C35F0[category][i * 8 + 2] ==
                    ((u8 (*)[0xA0])D_800DBEF4)[recordIndex][0x72]) {
                    return 1;
                }
            }
            i++;
            enabled++;
        } while (i < D_800C363A[category]);
    }
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
