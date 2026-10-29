#include <ultra64.h>
extern u8 D_80088980;
extern f32 D_800A0FB0;
typedef struct {
    u8 unk0[0x14];
    u8 active;
    u8 unk15[0x1F];
} struct_150DF8C0_record;
typedef struct {
    u8 values[3];
} struct_150DF8C0_indices;
extern struct_150DF8C0_record *D_800D3098;
extern struct_150DF8C0_indices D_80088984;

/* Non-matching placeholders for the text-only asm slice asm/10CD70.s. */

s32 func_150DF8C0(s32 arg0) {
    struct_150DF8C0_indices indices = D_80088984;

    if (D_800D3098[indices.values[arg0]].active != 0) {
        return 1;
    }
    return 0;
}

s32 func_150DF920() {
    return 0;
}

extern u8 D_800DD405;
extern s32 D_80090324[];
u32 func_1510D0EC(s32, s32 *, s32, s32);

/* Load the three resource segments selected by the live activity and variant. */
Gfx *func_150DFBD0(Gfx *cursor) {
    s32 index;
    /* The loader writes one word; preserve the retail aligned output cell. */
    union {
        s64 alignment;
        s32 value;
    } extent;
    s32 resource;
    u32 address;

    for (index = 0; index < 3; index++) {
        address = func_150DF8C0(index);
        if (address) {
            address = D_800DD405;
            resource = D_80090324[address + 9];
        } else {
            resource = D_80090324[8];
        }
        address = func_1510D0EC(resource, &extent.value, 3, 0);
        gSPSegment(cursor++, index + 2, address);
    }
    return cursor;
}

s32 func_150DFCA8() {
    return 0;
}

void func_150DFDA4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x1D4) + 0x40;

    *(f32 *) (temp_v0 + 0x30) = *(f32 *) (arg0 + 0x14);
    *(f32 *) (temp_v0 + 0x34) = D_800A0FB0;
    *(f32 *) (temp_v0 + 0x38) = *(f32 *) (arg0 + 0x1C);
}

s32 func_150DFDD0() {
    return 0;
}

s32 func_150DFEFC() {
    return 0;
}

void func_150E02C0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15149514(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150E0300(void) {
    if (D_80088980 == 0) {
        func_1515F170(6, 0);
        func_1513BAE8();
        D_80088980 = 1;
    }
}

typedef struct {
    f32 x, y, z;
} OwnerVector10CD70;

typedef struct {
    u32 zero0, zero4;
    u8 ownerIdentity, reserved09[3];
    u8 *owner;
    u8 attachment, reserved11[3];
    OwnerVector10CD70 vector;
    f32 value20, value24;
    s16 duration;
    u8 flags, kind;
    s8 callback;
    u8 mode;
} OwnerVectorDescriptor10CD70;

/* Retail reads the complete 12-byte vector preset at this symbol. */
extern OwnerVector10CD70 D_800A5480;
extern f32 D_800A0FB4, D_800A0FB8;
void *func_1513418C(void *, s32, u8, s32);

/* Submit the owner-linked descriptor with the shared vector preset. */
void *func_150E0348(u8 *owner, u8 selector, s32 category) {
    OwnerVectorDescriptor10CD70 descriptor;

    descriptor.zero0 = 0;
    descriptor.zero4 = 0;
    descriptor.ownerIdentity = owner[0x3B];
    descriptor.owner = owner;
    descriptor.attachment = 0;
    descriptor.vector = D_800A5480;
    descriptor.value20 = D_800A0FB4;
    descriptor.value24 = D_800A0FB8;
    descriptor.duration = 300;
    descriptor.flags = 0x1B;
    descriptor.kind = 0x0B;
    descriptor.callback = -1;
    descriptor.mode = 0;
    return func_1513418C(&descriptor, 0, selector, category);
}

s32 func_150E03F8() {
    return 0;
}

s32 func_150E05F8() {
    return 0;
}

s32 func_150E06D8() {
    return 0;
}
