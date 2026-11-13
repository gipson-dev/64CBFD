#include <ultra64.h>
#include <string.h>

/* The allocator takes a byte count in its seventh argument. */
#define func_15149130 func_15149130_legacy_signature
#include "functions.h"
#undef func_15149130
/* This resource table is a pointer, not the legacy inline array. */
#define D_800D3098 D_800D3098_legacy_array
#include "variables.h"
#undef D_800D3098

extern u8 *D_800D3098;
extern struct260 *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);

/* Generated placeholder declarations. */
void func_15010880(void);
/* End generated placeholder declarations. */

void func_15010780(void) {
    func_15177410(1, 255,    0, 108, 0, 0.0f, 15000, 80.0f, 77, 15, 127, 127, 127, 127, 127, 127);
    func_15177410(0, 255, 6628, 108, 0, 0.0f, 15000, 80.0f, 77, 15, 127, 127, 127, 127, 127, 127);
}

/* Initialize the scene callback and its optional records. */
void func_15010880(void) {
    struct177 tmp;
    struct260 *record;
    u32 base;
    func_15177410(16, 233, -437, 1123, -3263, 90.0f, 15000, 36.0f, 77, 15, 127, 127, 127, 127, 127, 127);
    D_800E0934 = (s32)func_150DE32C;
    tmp.unk0 = 0;
    base = (u32)D_800D3098;
    tmp.unk4 = base + 0xEA0U;
    tmp.unk8 = base + 0xED4U;
    record = func_15149130(300, -1, 94, -1, 0, 0, 12, 255, 1);
    if (record != NULL) {
        memcpy((u8 *)record + 0x28, &tmp, 12);
    }
    if ((D_800D2E4C->unk12 & 0x40) != 0) {
        func_15149130(5, 9, -1, -1, 1, 0, 0, 255, 1);
    }
}
void func_150109D0(void) {
    struct179 tmp;

    tmp.unk20 = 0;  
    //D_80096430 listed as (struct180*), but used as (struct180) here;
    tmp.unk4 = *((struct180*) &D_80096430); 

    tmp.unk0 = 1;
    tmp.unk1C = fabsf(tmp.unk4.unk4 - tmp.unk4.unk10); 
    func_151ACBD4(&tmp, 0);
    func_150E8854();
}
