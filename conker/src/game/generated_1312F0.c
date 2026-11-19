#include <ultra64.h>
#include "structs.h"
f32 func_150ADA68(void);
s32 func_150ADA20(void);

typedef struct {
    f32 height;
    s16 vertices[9];
    s16 pad16;
    u32 metadata;
    u8 flags;
    u8 state;
    u16 pad1E;
    s32 value;
} ExplosionGround1312F0;

void func_151D3FF4(struct17 *, u8, s32);
void func_1504715C(ExplosionGround1312F0 *, void *);
s32 func_15046C80(struct17 *, u16, f32, ExplosionGround1312F0 *);
/* The bounded lifetime is passed as an o32 word to this assembly consumer. */
void func_150E7FEC(f32, u8, s16 *, struct17 *, u32, s32, s32, s32, s32, s32, u8, s32);
void func_150E83AC(struct17 *, s16, u8, s32);
void func_151D5404(struct17 *, f32, f32, f32, s16, s16, u8, s32);
void func_151D5334(struct17 *, f32, f32, f32, u8, u8, s32);
void func_151D5514(struct17 *, u8, s32);
void func_151D40D4(struct17 *, struct17 *, void *, void *, s32, s32, s32, s32);
void func_15055A2C(s32, f32, f32, f32, s32);
u8 *func_151541B8(struct17 *, f32, f32, f32, f32, u8, s32);

/* Submit the explosion's ground contact, particles, actor effects and sound. */
void func_15103E40(void *source, void *groundContext, struct17 *position, u8 mode, s32 detail, u8 slot, s32 context) {
    struct17 contact;
    u8 hasContact;
    struct17 probe;
    ExplosionGround1312F0 ground;
    f32 sample;

    if (source != NULL) {
        hasContact = 0;
        func_151D3FF4(position, slot, context);
        probe.unk0 = position->unk0;
        probe.unk4 = position->unk4 + 100.0f;
        probe.unk8 = position->unk8;
        func_1504715C(&ground, groundContext);
        if (func_15046C80(&probe, 0, position->unk4 - 100.0f, &ground) != 0) {
            if (ground.flags & 1) {
                contact.unk0 = probe.unk0;
                contact.unk4 = ground.height;
                contact.unk8 = probe.unk8;
                hasContact = 1;
                sample = func_150ADA68();
                func_150E7FEC(sample * 125.0f + 204.0f, (u32)func_150ADA20() % 101U + 155U,
                              ground.vertices, &contact, (u32)func_150ADA20() % 302U + 500U,
                              0, 1, 0, 0, 0, slot, 0);
            }
        }
        func_150E83AC(hasContact ? &contact : position, (u32)func_150ADA20() % 62U + 120U, slot, context);
        func_151D5404(position, 506.0f, 1013.0f, 0.000987166888f, 15, 20, slot, context);
        func_151D5334(position, 506.0f, 1013.0f, 0.000987166888f, 5, slot, context);
        func_151D5514(position, slot, context);
        if (mode != 0) {
            u8 firstEffect;
            u8 secondEffect;
            if (mode == 2) {
                firstEffect = 0x42;
                secondEffect = 0x41;
            } else {
                firstEffect = 0x2B;
                secondEffect = 0x2A;
            }
            func_151D40D4(position, 0, source, groundContext, 0, firstEffect, secondEffect, detail);
        }
        func_15055A2C(0, position->unk0, position->unk4, position->unk8, 1);
        sample = func_150ADA68();
        func_151541B8(position, sample * 4.0f + 12.0f, 1.64099991f, (u32)func_150ADA20() % 56U + 200U, 0.0f, slot, context);
    }
}
