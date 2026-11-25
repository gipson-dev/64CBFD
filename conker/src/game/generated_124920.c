#include <ultra64.h>
#include "structs.h"
f32 func_150ADA68(void);
void *func_151541B8(struct17 *, f32, f32, f32, f32, u8, s32);
void func_151D3F14(struct17 *, u8, s32);


extern u8 D_800A1C40[][2];

/* Non-matching placeholders for the text-only asm slice asm/124920.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/game_124920/func_150F7470.s")

s32 func_150F78B4() {
    return 0;
}

#include <math.h>

extern f32 D_800A1BD8, D_800BE9A4;
f32 func_15144B68(f32 angle);

typedef struct {
    u8 reserved[0x18];
    f32 remaining;
    f32 phase;
    f32 rate;
    f32 center;
    f32 amplitude;
} SineEffectState124920;

/* Update the intensity, sine-driven value, wrapped phase and remaining time. */
s32 func_150F7E20(u8 *effect) {
    f32 sine;
    f32 value;
    SineEffectState124920 *state;

    state = (SineEffectState124920 *)(effect + 0x110);
    effect[0x5C] = (u32)(*(f32 *)(effect + 0x128) * D_800A1BD8);
    sine = sinf(*(f32 *)(effect + 0x12C));
    value = sine * state->amplitude + state->center;
    *(f32 *)(effect + 0x30) = value;
    *(f32 *)(effect + 0x2C) = value;
    state->phase = func_15144B68(state->phase + state->rate * D_800BE9A4);
    state->remaining -= D_800BE9A4;
    if (state->remaining < 0.0f) {
        return 0;
    }
    return 1;
}

void func_150F7F58(u8 *arg0, s16 arg1) {
    func_15140410(arg0, arg0 + 0x110, arg0 + 0x11C, arg1);
}

/* Submit the randomized point effect, then the secondary point event. */
void func_150F7F8C(struct17 *point, u8 selector, s32 parameter) {
    f32 second;
    f32 first = func_150ADA68();

    second = func_150ADA68();

    func_151541B8(point, first * 3.0f + 9.0f, 0.5119050145149231f,
        second * 70.0f + 70.0f, 0.0f, selector, parameter);
    func_151D3F14(point, selector, parameter);
}

#include "libc/string.h"
typedef struct { f32 x, y, z; } OwnerEffectVector150F802C;
typedef struct {
    f32 position[3];
    f32 direction[3];
    u8 retained18[0x2C];
} OwnerEffectRecord150F802C;
typedef struct {
    OwnerEffectRecord150F802C *owner;
    f32 position[3];
    f32 zero10;
} OwnerEffectTail150F802C;
typedef struct {
    f32 scale[2];
    f32 extent[2];
    f32 direction[3];
    f32 unitScale[3];
    f32 position[3];
    f32 zeroVelocity[3];
    OwnerEffectVector150F802C reference;
    f32 zero4C;
    u32 flags;
    s16 parameter;
    u16 resourceId;
    u8 zero58, padding59[3];
    u32 zero5C;
    u8 value60, value61, zero62, zero63, zero64, zero65, zero66, zero67, zero68;
    u8 padding69, zero6A, padding6B;
    u32 zero6C;
    u8 zero70, padding71;
    u16 value72, value74;
    u8 padding76[2];
    u32 zero78;
} OwnerEffectDescriptor150F802C;
typedef struct ExtendedState15F680 ExtendedState15F680;
extern f32 D_800A1BDC;
extern OwnerEffectVector150F802C D_800A5480;
void *func_1513264C(u8 *,s32,s32,ExtendedState15F680 *,s32,u8,s32);
/* Capture a source record, submit its descriptor, then retain its owner/position. */
void func_150F802C(OwnerEffectRecord150F802C *source,s16 parameter,u8 slot,s32 context) {
    OwnerEffectTail150F802C tail;
    OwnerEffectDescriptor150F802C descriptor;
    void *result;
    descriptor.extent[0]=D_800A1BDC;
    descriptor.extent[1]=D_800A1BDC;
    tail.owner=source;
    tail.position[0]=source->position[0];
    tail.position[1]=source->position[1];
    tail.position[2]=source->position[2];
    tail.zero10=0.0f;
    descriptor.scale[0]=1.0f;
    descriptor.scale[1]=1.0f;
    descriptor.direction[0]=source->direction[0];
    descriptor.direction[1]=source->direction[1];
    descriptor.direction[2]=source->direction[2];
    descriptor.unitScale[0]=1.0f;
    descriptor.unitScale[1]=1.0f;
    descriptor.unitScale[2]=1.0f;
    descriptor.position[0]=source->position[0];
    descriptor.position[1]=source->position[1];
    descriptor.position[2]=source->position[2];
    descriptor.zeroVelocity[0]=0.0f;
    descriptor.zeroVelocity[1]=0.0f;
    descriptor.zeroVelocity[2]=0.0f;
    descriptor.reference=D_800A5480;
    descriptor.zero4C=0.0f;
    descriptor.flags=0x980;
    descriptor.parameter=parameter;
    descriptor.resourceId=47;
    descriptor.zero58=0;
    descriptor.zero5C=0;
    descriptor.value60=255;
    descriptor.value61=20;
    descriptor.zero62=0;
    descriptor.zero63=0;
    descriptor.zero64=0;
    descriptor.zero65=0;
    descriptor.zero66=0;
    descriptor.zero67=0;
    descriptor.zero68=0;
    descriptor.zero6A=0;
    descriptor.zero6C=0;
    descriptor.zero70=0;
    descriptor.value72=1;
    descriptor.value74=255;
    descriptor.zero78=0;
    result=func_1513264C((u8 *)&descriptor,3,255,0,180,slot,context);
    if (result != 0) {
        memcpy((u8 *)result+0x170,&tail,20);
    }
}

s32 func_150F81BC() {
    return 0;
}

s32 func_150F85A0() {
    return 0;
}

void func_150F884C(u8 arg0, s32 arg1) {
    s32 value[2];

    value[0] = arg1;
    func_151494E0(value, 0x3F);
}

typedef struct {
    s32 reference;
    u8 tag, reserved05[3];
    u8 selected, reserved09[3];
    u8 *records[8];
} LinkedRecordGroup124920;

s32 func_150F892C();

/* Select the final linked record or forward a matching reference event. */
void func_150F887C(struct260 *owner, s32 packetAddress, u8 command) {
    LinkedRecordGroup124920 *group;
    u8 i;

    if (command == 0x42) {
        group = (LinkedRecordGroup124920 *)((u8 *)owner + 0x28);
        if (((u8 *)packetAddress)[4] == group->tag) {
            for (i = 0; i < 7; i++) {
                group->records[i][0x6E] = 1;
            }
            group->records[7][0x6E] = 0;
            group->selected = 7;
        }
    } else if (command == 0x3F) {
        if (*(s32 *)packetAddress == *(s32 *)((u8 *)owner + 0x28)) {
            func_150F892C(owner);
        }
    }
}

s32 func_150F892C() {
    return 0;
}

void func_150F9720(u8 arg0) {
    s64 value;
    u8 *pair;

    pair = D_800A1C40[arg0];
    *(s32 *)&value = 0;
    ((u8 *)&value)[4] = pair[0];
    func_151494E0((s32)&value, 0x42);
    ((u8 *)&value)[4] = pair[1];
    func_151494E0((s32)&value, 0x42);
}

void func_150F9788(s32 arg0) {
}

s32 func_150F9794(s32 arg0) {
    func_150F9788(arg0);
    func_1514933C(arg0);
}

s32 func_150F97C0(s32 arg0) {
    func_150F9788(arg0);
    func_15149368(arg0);
}

extern u8 D_80088B50;
extern f32 D_800A1C48[3], D_800A1C54[3];
s32 func_150ADA20(void);
void func_15145EA4(struct17 **, struct17 **, u8 *, s32);
u8 *func_15102B38(u8 *, u8, f32 *, f32 *, f32 *, s16, u8, f32, f32 *, u8, s32, s16, u8, s32);

/* Transform the actor's emitter point and submit an effect with randomized parameters. */
void func_150F97EC(struct127 *actor, u8 priority, s32 parameter) {
    struct17 position;
    f32 sample;
    f32 scale[2];
    struct17 *input;
    struct17 *output;
    f32 span;
    u32 random[2];

    if (actor->unk1D4 != NULL) {
        input = (struct17 *)D_800A1C48;
        output = &position;
        func_15145EA4(&input, &output, (u8 *)actor->unk1D4 + D_80088B50 * 64, 1);
        span = 1.0f;
        sample = func_150ADA68();
        scale[1] = sample * span + 2.0f;
        scale[0] = func_150ADA68() * 14.0f + 28.0f;
        random[0] = func_150ADA20();
        random[1] = func_150ADA20();
        func_15102B38((u8 *)actor, D_80088B50, D_800A1C48, D_800A1C54, scale,
            random[0] % 3U + 4, random[1] % 156U + 100,
            func_150ADA68() * 300.0f + 400.0f, (f32 *)&position,
            255, 0, -1, priority, parameter);
    }
}



u8 *func_150FF288(u8 *);
s32 func_150FF6E0(struct17 *, struct17 *, struct17 *, struct17 *, struct17 *, u8 *, u8 *);
void func_151D3F14(struct17 *, u8, s32);
void func_151D4408(struct17 *, struct17 *, void *, u8 *, f32, u8, s32);
void func_150FF474(struct17 *, struct17 *, u8, s32);
/* Recover descriptor geometry and submit the actor's paired effects. */
void func_150F9950(u8 *actor, u8 selector, s32 parameter) {
    struct17 points[6];
    struct17 origin;
    struct17 direction;
    struct17 velocity;
    struct17 other;
    u8 *descriptor;

    descriptor = func_150FF288(actor);
    if (descriptor != 0) {
        if (func_150FF6E0(points, &origin, &direction, &velocity, &other, actor, descriptor)) {
            func_151D3F14(&origin, selector, parameter);
            func_151D4408(&direction, &velocity,
                *(u8 **)(actor + 0x1D4) + descriptor[2] * 64,
                actor, 1.0f, selector, parameter);
            func_150FF474(&origin, points, selector, parameter);
        }
    }
}
