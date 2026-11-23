#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/10C170.s. */

s32 func_150DECC0() {
    return 0;
}

#include "structs.h"
typedef struct HeightResult71820 {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags, state;
    u16 pad1E;
    s32 value;
} HeightResult71820;
/* Expose the three floats through both helper and struct-copy interfaces. */
typedef union { f32 values[3]; struct17 vector; } GroundVector150DF334;
s32 func_1504697C(f32 *, u16, f32, HeightResult71820 *);
s32 func_150ADA20(void);
void func_150E83AC(struct17 *, s16, u8, s32);
void func_151A9834(f32 *, f32, f32, HeightResult71820 *, s32, u8, u8 *, u8, s32);

/* Resolve contact, submit its timed effect, then scatter ground-tested emissions. */
void func_150DF334(struct260 *owner) {
    HeightResult71820 ground;
    u8 hasContact = 0;
    GroundVector150DF334 contact;
    GroundVector150DF334 probe;
    GroundVector150DF334 burst;
    struct17 *position;
    u32 random;
    struct17 *firstPosition;

    probe.values[0] = *(f32 *)((u8 *)owner + 0x28);
    probe.values[1] = *(f32 *)((u8 *)owner + 0x2C) + 500.0f;
    probe.values[2] = *(f32 *)((u8 *)owner + 0x30);
    if (func_1504697C(probe.values, 0, probe.values[1] - 1000.0f, &ground)) {
        contact.vector.unk0 = *(f32 *)((u8 *)owner + 0x28);
        contact.vector.unk4 = ground.height;
        contact.vector.unk8 = *(f32 *)((u8 *)owner + 0x30);
        hasContact = 1;
    }
    firstPosition = hasContact ? &contact.vector : (struct17 *)((u8 *)owner + 0x28);
    random = (u32)func_150ADA20();
    func_150E83AC(firstPosition, random % 62U + 120U,
                  ((u8 *)owner)[0x0C], ((u8 *)owner)[1]);
    position = (struct17 *)((u8 *)owner + 0x28);
    if (hasContact) position = &contact.vector;
    burst.vector = *position;
    burst.values[1] += 500.0f;
    random = (u32)func_150ADA20();
    func_151A9834(burst.values, burst.values[1] - 1000.0f, 250.0f, &ground,
                  random % 3U + 3U, 1, NULL,
                  ((u8 *)owner)[0x0C], ((u8 *)owner)[1]);
}


s32 func_150DF4B8() {
    return 0;
}
