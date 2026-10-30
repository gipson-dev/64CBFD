#include <ultra64.h>
#include "structs.h"
void func_15145EA4(struct17 **, struct17 **, u8 *, s32);
/* Assembly consumer: pass the explicitly truncated selector as an ABI word. */
void func_151D4408(struct17 *, struct17 *, void *, u8 *, f32, s32, s32);


void func_151D5514(f32 *, u8, s32);
void func_151D3FF4(f32 *, u8, s32);
f32 func_150ADA68(void);
s32 func_150ADA20(void);
u8 *func_151541B8(f32 *, f32, f32, f32, f32, u8, s32);

typedef struct { f32 x,y,z; } BobVector200930;
typedef struct { s16 remaining; u16 reserved; f32 phase,rate,amplitude; } BobState200930;
typedef struct {
    u8 pad0[0x20]; BobVector200930 position;
    u8 pad2C[0x24]; BobVector200930 base;
    u8 pad5C[0x114]; BobState200930 bob;
} BobActor200930;
extern f32 D_800BE9A4;
extern s32 D_800BE9E4;
f32 func_15144B68(f32);
f32 sinf(f32);


/* Non-matching placeholders for the text-only asm slice asm/200930.s. */

s32 func_15131828();
s32 func_15131958();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3480.s")

/* Advance the vertical oscillation, or restore the base position. */
s32 func_151D3D50(BobActor200930 *actor) {
    BobState200930 *bob = &actor->bob;

    if (bob->remaining > 0) {
        bob->phase += bob->rate * D_800BE9A4;
        bob->phase = func_15144B68(bob->phase);
        actor->position.y = sinf(bob->phase) * bob->amplitude + actor->base.y;
        bob->remaining -= D_800BE9E4;
    } else {
        actor->position = actor->base;
    }
    return 1;
}


#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3E04.s")


#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3E6C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3F14.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D3FF4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D40D4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D42E8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D4408.s")

s32 func_151D4668(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x3C);
}


#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D469C.s")



#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D4794.s")


void func_1516972C(struct102 *);
void func_15149514(s32, u8, s32, s32, s32);

/* Release or deactivate matching owner links, otherwise dispatch the pair event. */
void func_151D4C38(struct260 *owner, s32 eventAddress, u8 command) {
    u8 *link = (u8 *)owner + 0x28;
    u8 *event = (u8 *)eventAddress;

    if (command == 60) {
        if (*(s32 *)link == *(s32 *)event || link[4] == event[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (command == 4) {
        if (*(s32 *)link == *(s32 *)event || link[4] == event[4]) {
            link[0x10] &= ~1;
        }
    } else {
        func_15149514(eventAddress, command, (s32)link, (s32)(link + 4), (s32)owner);
    }
}

s32 func_151D4D04(u8 *arg0, s32 arg1) {
    u8 *temp_a2 = arg0 + 0xA8;

    func_15131828(arg0, arg0 + 0xAC, temp_a2, arg0 + 0xAA);
    func_15131958(arg0 + 0x58, *(s32 *) (temp_a2 + 0xC));
    return 1;
}

void func_151D4D58(u8 *arg0) {
    func_151D469C(arg0, 0, 0x50, 0xFF, 1);
    func_151D469C(arg0, 1, 0x50, 0xFF, 1);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D4DAC.s")

void func_151D5148(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x31C);
    s16 value = *(s16 *) (temp_v0 + 0x24);

    if (value > 0) {
        *(s16 *) (temp_v0 + 0x24) = value - 1;
        temp_v0 = *(u8 **) (arg0 + 0x31C);
    }
    (*(s16 *) (temp_v0 + 0x1AA))++;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5174.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5334.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5404.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5514.s")

/* Submit the paired position effects, then the randomized burst. */
void func_151D5648(f32 *position, u8 kind, s32 mode) {
    u32 randomValue;
    f32 randomScale;

    func_151D5514(position, kind, mode);
    func_151D3FF4(position, kind, mode);
    randomScale = func_150ADA68();
    randomValue = (u32)func_150ADA20();
    func_151541B8(position, randomScale * 4.0f + 12.0f, 1.6409999f,
                 (randomValue % 56U) + 200U, 0.0f, kind, mode);
}

/* Transform both points, then submit their origin and displacement. */
void func_151D5714(struct127 *actor, f32 *first, f32 *second, s32 joint,
                   f32 scale, s32 kind, s32 mode) {
    struct17 origin;
    struct17 direction;
    u8 *matrix;
    struct17 *inputs[2];
    struct17 *outputs[2];

    if (actor->unk1D4 != NULL && (actor->unk74 & 0xF) != 0xF) {
        matrix = (u8 *)actor->unk1D4 + ((u8)joint << 6);
        inputs[0] = (struct17 *)first;
        inputs[1] = (struct17 *)second;
        outputs[0] = &origin;
        outputs[1] = &direction;
        func_15145EA4(inputs, outputs, matrix, 2);
        direction.unk0 -= origin.unk0;
        direction.unk4 -= origin.unk4;
        direction.unk8 -= origin.unk8;
        func_151D4408(&origin, &direction, matrix, (u8 *)actor, scale, (u8)kind, mode);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D57F8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5A18.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5B6C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_200930/func_151D5D60.s")

void func_151D5E30(s32 *arg0) {
    s32 entry;
    u8 i;

    for (i = 0; i < 4; i++) {
        if (entry = arg0[i]) {
            func_100043B4(entry, 3);
        }
    }
}
