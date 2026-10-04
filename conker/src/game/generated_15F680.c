#include <ultra64.h>
extern void (*D_800899D4[])();
extern void (*D_800899B0[])();
extern s32 D_80082FA0;
void func_15169260(void *, s32, s32, u8);
void func_100043B4(s32 *, u32);
extern u8 D_800A3860[];
extern f32 D_800A3868;
extern s32 D_800A3880[];
extern s32 D_800DC63C;
extern s16 D_800DC468[];
extern s32 D_800DC640[];
extern s32 D_800BE9F0;
extern u8 D_800BE616;

typedef struct ExtendedResource15F680 {
    void *data;
} ExtendedResource15F680;

typedef struct ExtendedResourceNode15F680 {
    ExtendedResource15F680 *resource;
    struct ExtendedResourceNode15F680 *next;
    struct ExtendedResourceNode15F680 *previous;
    u16 id;
    u8 retained;
    u8 reserved0F;
} ExtendedResourceNode15F680;

typedef struct ExtendedState15F680 {
    u32 words[9];
} ExtendedState15F680;

extern ExtendedResourceNode15F680 *D_800DC460;
extern ExtendedResourceNode15F680 *D_800DC464;
void *allocate_memory(s32, s32, s32, s32);
void func_10004074(void *);
void *func_15167A68(s32, s32, s32, s32, u8, u8);
void func_15168A9C(void *);
u8 *func_1515D480(s32);
u8 *func_1515D440(void);
void *func_1502B6BC(s32 *, s32, s32 *, s32, ...);
void func_1510CE60(void *, s32, s32, s32, s32 *);
void func_15168E54(void *, void *);
s32 func_151336A8(s32, ExtendedResourceNode15F680 *, void *);
typedef struct { s32 a, b; } TwoWord15F680;
typedef struct {
    u8 pad0[0x154];
    s32 entries[4];
    s32 trailing;
} ResourceOwner15F680;

/* Non-matching placeholders for the text-only asm slice asm/15F680.s. */


s32 func_15133EEC();
s32 func_151424F4(s32, s32, s32, s32, f32, f32, f32, f32, f32, f32, f32, f32);
s32 func_15142838(void *, f32, f32, f32, f32, f32, f32, f32, f32);

s32 func_151321D0() {
    return 0;
}

s32 func_151323AC(u8 *arg0) {
    s32 idx = (*(u32 *) (arg0 + 0x60) & 0x100) ? *(arg0 + 0x68) : 0;

    D_800899B0[idx]();
}

s32 func_151323F8(u8 *arg0) {
    s32 idx = (*(u32 *) (arg0 + 0x60) & 0x100) ? *(arg0 + 0x68) : 0;

    D_800899D4[idx]();
}

s32 func_15132444() {
    return 0;
}

s32 func_15132570(s32 arg0) {
    func_15132444(arg0);
    func_15169804(arg0);
}

s32 func_1513259C(s32 arg0) {
    func_15132444(arg0);
    func_15169824(arg0);
}

void func_151325C8(ResourceOwner15F680 *arg0) {
    s32 i;

    for (i = 0; i <= D_80082FA0; i++) {
        if (arg0->entries[i]) {
            func_100043B4(arg0->entries[i], 4);
        }
    }
    if (arg0->trailing != NULL) {
        func_100043B4(arg0->trailing, 4);
    }
}

void *func_1513264C(u8 *descriptor, s32 resource, s32 value,
                    ExtendedState15F680 *state, s32 payloadBytes, u8 slot, s32 context) {
    u8 *result;
    ExtendedResourceNode15F680 *node;
    s32 kind;
    s32 pool;
    s32 remaining;
    s32 i;
    f32 x;
    f32 y;
    f32 z;

    if (D_800DC63C > 300) {
        return NULL;
    }
    kind = (*(u32 *)(descriptor + 0x50) & 0x4000) ? 0x48 : 0x19;
    pool = (*(u32 *)(descriptor + 0x50) & 0x400000) ? 2 : 1;
    result = func_15167A68(kind, context, payloadBytes + 0x170, 1, slot, pool);
    if (result == NULL) {
        return NULL;
    }

    if (D_800DC468[*(u16 *)(descriptor + 0x56)] == 0) {
        pool = (*(u32 *)(descriptor + 0x50) & 0x400000) ? 2 : 1;
        node = allocate_memory(0x10, 1, 2, pool);
        if (node == NULL) {
            func_15168A9C(result);
            func_10004074(result);
            return NULL;
        }
        if (!func_151336A8(*(u16 *)(descriptor + 0x56), node, result)) {
            func_15168A9C(result);
            func_10004074(result);
            func_10004074(node);
            return NULL;
        }
        node->next = D_800DC460;
        if (D_800DC460 != NULL) {
            D_800DC460->previous = node;
        } else {
            D_800DC464 = node;
        }
        D_800DC460 = node;
        node->previous = NULL;
        node->id = *(u16 *)(descriptor + 0x56);
        node->retained = 0;
        if ((*(u32 *)(descriptor + 0x50) & 0x100000) &&
            D_800BE9F0 != 0x3B && D_800BE9F0 != 6 && D_800BE9F0 != 0x13 &&
            D_800BE616 == 0 && D_800BE9F0 != 2) {
            node->retained = 1;
        }
    } else {
        node = D_800DC460;
        remaining = 100;
        if (node->id != *(u16 *)(descriptor + 0x56)) {
            do {
                remaining--;
                node = node->next;
                if (remaining <= 0) {
                    break;
                }
            } while (node->id != *(u16 *)(descriptor + 0x56));
        }
        if (remaining <= 0) {
            func_15168A9C(result);
            func_10004074(result);
            return NULL;
        }
    }

    D_800DC468[*(u16 *)(descriptor + 0x56)]++;
    *(ExtendedResourceNode15F680 **)(result + 0x8C) = node;
    memcpy(result + 0x10, descriptor, 0x7C);
    result[0x149] = 0;
    *(f32 *)(result + 0x134) = 0.0f;
    *(f32 *)(result + 0x138) = 0.0f;
    *(f32 *)(result + 0x13C) = 0.0f;
    x = *(f32 *)(descriptor + 0x34);
    y = *(f32 *)(descriptor + 0x38);
    z = *(f32 *)(descriptor + 0x3C);
    result[0x148] = 0;
    *(f32 *)(result + 0x144) = 1.0f;
    *(f32 *)(result + 0x140) = sqrtf((x * x + y * y) + z * z);
    if (state != NULL) {
        *(ExtendedState15F680 *)(result + 0x110) = *state;
    } else {
        /* Retail initializes only these default-state fields. */
        *(u32 *)(result + 0x130) = 0;
        result[0x12D] = 0;
        result[0x12C] = 0;
        *(u32 *)(result + 0x128) = 0;
        *(f32 *)(result + 0x110) = D_800A3868;
    }
    D_800DC63C++;
    result[0x150] = 0;
    *(s32 *)(result + 0x14C) = resource;
    *(s32 *)(result + 0x168) = value;
    for (i = 0; i < 4; i++) {
        *(void **)(result + 0x154 + i * 4) = NULL;
    }
    *(void **)(result + 0x164) = NULL;
    if (resource != 0) {
        for (i = 0; i <= D_80082FA0; i++) {
            *(void **)(result + 0x154 + i * 4) = func_1515D480(resource);
        }
        *(void **)(result + 0x164) = func_1515D440();
    }
    *(u32 *)(result + 0x60) &= ~0x200000;
    return result;
}

void *func_15132A4C(void *arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, s32 arg5) {
    return func_1513264C(arg0, arg1, arg2, 0, arg3, arg4, arg5);
}

s32 func_15132A88() {
    return 0;
}

s32 func_15132B80() {
    return 0;
}

s32 func_15132DDC() {
    return 0;
}

s32 func_151332DC() {
    return 0;
}

s32 func_15133510(s32 arg0, u8 *arg1) {
    func_151424F4(arg0,
                  *(s32 *)(arg1 + 0x18),
                  *(s32 *)(arg1 + 0x1C),
                  *(s32 *)(arg1 + 0x20),
                  *(f32 *)(arg1 + 0x24),
                  *(f32 *)(arg1 + 0x28),
                  *(f32 *)(arg1 + 0x2C),
                  *(f32 *)(arg1 + 0x30),
                  *(f32 *)(arg1 + 0x34),
                  *(f32 *)(arg1 + 0x38),
                  *(f32 *)(arg1 + 0x3C),
                  *(f32 *)(arg1 + 0x40));
    return 1;
}

s32 func_15133588() {
    return 0;
}

s32 func_151336A8(s32 index, ExtendedResourceNode15F680 *node, void *record) {
    s32 output0;
    s32 output1;

    (void)record;
    node->resource = func_1502B6BC(&output0, 0, &output1, 2, 9, D_800A3880[index]);
    if (node->resource == NULL) {
        return 0;
    }
    func_1510CE60(node->resource->data, 0, 1, 0x3E, &D_800DC640[index]);
    func_15168E54(node->resource->data, node->resource);
    return 1;
}

s32 func_15133760(u8 *arg0, u8 *arg1) {
    func_15142838(
        arg0,
        *(f32 *)(arg1 + 0x18),
        *(f32 *)(arg1 + 0x1C),
        *(f32 *)(arg1 + 0x20),
        *(f32 *)(arg1 + 0x24),
        *(f32 *)(arg1 + 0x28),
        *(f32 *)(arg1 + 0x38),
        *(f32 *)(arg1 + 0x3C),
        *(f32 *)(arg1 + 0x40)
    );
    return 1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_15F680/func_151337C0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_15F680/func_15133894.s")

s32 func_151339D4(u8 *arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4) {
    f32 scale;

    *(f32 *)(arg0 + 0x3C) = *(f32 *)(arg0 + 0x10) + arg4;
    scale = *(f32 *)(arg0 + 0x14);
    *(f32 *)(arg0 + 0x44) *= scale;
    *(f32 *)(arg0 + 0x48) *= -scale;
    *(f32 *)(arg0 + 0x4C) *= scale;
    *(f32 *)(arg0 + 0x50) *= scale;
    *(f32 *)(arg0 + 0x54) *= scale;
    *(f32 *)(arg0 + 0x58) *= scale;
    return 1;
}

s32 func_15133A50(u8 *arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4) {
    f32 value = *(f32 *) (arg0 + 0x10) + arg4;

    *(f32 *) (arg0 + 0x44) = 0.0f;
    *(f32 *) (arg0 + 0x48) = 0.0f;
    *(f32 *) (arg0 + 0x4C) = 0.0f;
    *(f32 *) (arg0 + 0x50) = 0.0f;
    *(f32 *) (arg0 + 0x54) = 0.0f;
    *(f32 *) (arg0 + 0x3C) = value;
    *(f32 *) (arg0 + 0x58) = 0.0f;
    return 1;
}

s32 func_15133A94() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_15F680/func_15133B98.s")

s32 func_15133C58() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_15F680/func_15133D20.s")

void func_15133DE8(u8 *arg0, u8 *arg1, u8 arg2) {
    u32 id;

    if (arg2 == 0) {
        id = *(u32 *)arg1;
        if ((id == *(u32 *)(arg0 + 0x7C)) ||
            (*(arg1 + 4) == *(arg0 + 0x80))) {
            func_1516972C(arg0);
        }
    }
}

void func_15133E3C(s32 arg0, u8 arg1) {
    TwoWord15F680 tmp = *(TwoWord15F680 *)D_800A3860;

    func_15169260(&tmp, 2, arg0, arg1);
}

s32 func_15133E84(s32 arg0, u8 *arg1, s32 arg2) {
    func_15133EEC(arg0, *(u16 *)(arg1 + 0x170), *(u8 *)(arg1 + 0x172), *(s32 *)(arg1 + 0x174));
}

s32 func_15133EB8(s32 arg0, u8 *arg1, s32 arg2) {
    func_15133EEC(arg0, *(u16 *)(arg1 + 0x174), *(u8 *)(arg1 + 0x176), *(s32 *)(arg1 + 0x178));
}

s32 func_15133EEC() {
    return 0;
}

s32 func_15133FD8(s32 arg0, u8 *arg1, s32 arg2) {
    u8 *entries = arg1 + 0x170;
    s32 i;

    i = 0;
    while (i < entries[0]) {
        arg0 = func_15133EEC(arg0, *(u16 *)(entries + i * 8 + 4),
                             entries[i * 8 + 6],
                             *(s32 *)(entries + i * 8 + 8));
        i = (i + 1) & 0xFF;
    }

    return arg0;
}
