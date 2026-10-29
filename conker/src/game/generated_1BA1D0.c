#include <ultra64.h>
#include "structs.h"
typedef struct { u32 words[20]; } Generated1BA1D0Preset;
extern Generated1BA1D0Preset *D_8008D630[];
s32 func_1518FDC4();
void *func_1518F5D0();
f32 func_150ADA68();
s32 func_150ADA20(void);
void func_151429E0(u8, u8 *, u8 *, u8 *);
extern f32 D_800BE9A4;
extern s32 (*D_8008D67C[])(u8 *);
extern void (*D_8008D680[])();
extern void (*D_8008D684[])(u8 *, void *, u8);
typedef struct { s32 a, b, c; } ThreeWord1BA1D0;
void func_15169260(void *, s32, s32, u8);
extern u8 D_800A74D4[];
extern s32 D_800A8010;
typedef struct { s32 val; } OneWord1BA1D0;
typedef struct {
    f32 value;
    f32 pad4[2];
    f32 base;
    f32 scale;
} FloatUpdate1BA1D0;
typedef struct {
    f32 value;
    f32 base;
    f32 scale;
    u8 padC[0x4C];
    s8 callback;
} RandomStep1BA1D0;
typedef struct {
    u8 pad0[0x1C];
    s16 timer;
    u8 pad1E[0x3E];
    u8 value;
    u8 pad5D[0xC7];
    s16 limit;
    s16 scale;
} Generated1BA1D0Record;
typedef struct {
    u8 pad0[0x1C];
    s16 timer;
    u8 pad1E[0x12];
    f32 value30;
    u8 pad34[0x28];
    u8 value5C;
    u8 pad5D[0xF7];
    f32 factor;
    s16 limit;
    s16 scale;
} Generated1BA1D0Record154;
typedef struct {
    u8 pad0;
    u8 selector;
    u8 pad2[0xA];
    u8 owner;
    u8 padD[0xB];
    void *object;
    u8 pad1C[2];
    s16 value;
    u8 pad20;
    s8 state;
} Generated1BA1D0Setup;
extern u8 D_800A7460[];
extern u8 D_800A749C[];

/* Non-matching placeholders for the text-only asm slice asm/1BA1D0.s. */

s32 func_1518F8E0();

s32 func_15191400();
void func_151D33FC(u8 *arg0, void *arg1);

s32 func_1518CD20() {
    return 0;
}

s32 func_1518D1C0(void *arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4,
                  u8 arg5, void *arg6) {
    return 0;
}

s32 func_1518D6E0() {
    return 0;
}

s32 func_1518E298(u8 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    u8 *source = *(u8 **)(arg0 + 0x1C);

    if (source != NULL) {
        if (*(s32 *)source != 0) {
            *(s16 *)(arg0 + 2) = (s16)*(f32 *)(source + 0x14);
            *(s16 *)(arg0 + 4) = (s16)*(f32 *)(source + 0x18);
            *(s16 *)(arg0 + 6) = (s16)*(f32 *)(source + 0x1C);
            return 0;
        }
    }
    return 1;
}

void func_1518E308(u8 *arg0) {
    u8 *record;
    s32 i;

    record = arg0 + 0x48;
    *(s32 *) (arg0 + 0x28) = 0;
    *(f32 *) (arg0 + 0x24) = 0.0f;
    for (i = 0; i < 100; i++, record += 0x18) {
        if (*(void **) record != NULL) {
            func_1516972C(*(void **) record);
        }
    }
    bzero(arg0 + 0x48, 0x960);
}

void func_1518E37C(u8 *arg0, u8 arg1) {
    if (arg1 != *(arg0 + 0x22)) {
        func_1518E308(arg0);
        *(arg0 + 0x22) = arg1;
    }
}

s32 func_1518E3C4() {
    return 0;
}

void func_1518E4A0(u8 *arg0) {
    func_1518E308(arg0);
    func_1514EDF0(arg0, *(s32 *) (arg0 + 0x18));
}

s32 func_1518E4CC(s32 arg0) {
    func_1518E4A0(arg0);
    func_15169804(arg0);
}

s32 func_1518E4F8(s32 arg0) {
    func_1518E4A0(arg0);
    func_15169824(arg0);
}

/* Initialize flags, choose the kind, and set opaque black RGBA defaults. */
void func_1518E524(u8 *kind, u8 *flags, u8 *red, u8 *green, u8 *blue,
                  u8 *alpha, s16 *mode) {
    *flags = 2;
    if (func_150ADA20() & 1) {
        *flags |= 1;
    }
    switch (func_150ADA20() & 1) {
        case 0:
            *kind = 0x13;
            break;
        case 1:
            *kind = 0x14;
            break;
    }
    *red = 0;
    *green = 0;
    *blue = 0;
    *alpha = 0xFF;
    *mode = 0x301;
}

void func_1518E5D8(u8 *arg0, u8 *arg1, u8 *arg2, u8 *arg3, u8 *arg4, u8 *arg5, s16 *arg6) {
    s32 selector;

    if (func_150ADA20() & 1) {
        *arg1 |= 1;
    }
    *arg0 = 0x16;
    if (func_150ADA20() & 1) {
        selector = 3;
    } else {
        selector = 4;
    }
    func_151429E0(selector, arg2, arg3, arg4);
    *arg5 = 0xC8;
    *arg6 = 0x401;
}

s32 func_1518E66C(Generated1BA1D0Setup *arg0) {
    func_1518D1C0(arg0->object, 3, 0, 0, arg0->owner, arg0->selector,
                  D_800A7460);
    arg0->value = 0x80;
    arg0->state = -1;
    return 0;
}

s32 func_1518E6D4(Generated1BA1D0Setup *arg0) {
    func_1518D1C0(arg0->object, 4, 0, 0, arg0->owner, arg0->selector,
                  D_800A749C);
    arg0->value = 0x80;
    arg0->state = -1;
    return 0;
}

s32 func_1518E73C() {
    return 0;
}

s32 func_1518EB10() {
    return 0;
}

s32 func_1518EF54() {
    return 0;
}

typedef struct {
    u8 reserved[0x34];
    f32 position[3];
    f32 endPoint[3];
    u8 reserved4C[0xF4];
    f32 velocity[3];
    f32 verticalAcceleration;
    f32 damping;
} DualPointMotion1BA1D0;

/* Damp planar velocity and advance both points by the same displacement. */
s32 func_1518F058(DualPointMotion1BA1D0 *motion) {
    f32 damping = motion->damping;
    f32 step;
    f32 dx, dy, dz;

    motion->velocity[0] *= damping;
    motion->velocity[1] += motion->verticalAcceleration * D_800BE9A4;
    motion->velocity[2] *= damping;
    step = D_800BE9A4;
    dx = motion->velocity[0] * step;
    dy = motion->velocity[1] * step;
    dz = motion->velocity[2] * step;
    motion->position[0] += dx;
    motion->position[1] += dy;
    motion->position[2] += dz;
    motion->endPoint[0] += dx;
    motion->endPoint[1] += dy;
    motion->endPoint[2] += dz;
    return 1;
}

s32 func_1518F108(u8 *arg0) {
    f32 value0 = *(f32 *)(arg0 + 0x30);
    f32 factor = *(f32 *)(arg0 + 0x154);
    f32 value1 = *(f32 *)(arg0 + 0x2C);
    s32 timer = *(s16 *)(arg0 + 0x1C);

    *(f32 *)(arg0 + 0x30) = value0 - (value0 * factor);
    *(f32 *)(arg0 + 0x2C) = value1 - (value1 * factor);
    if (timer < *(s16 *)(arg0 + 0x158)) {
        arg0[0x5C] = (u32) timer * (u32)*(s16 *)(arg0 + 0x15A);
    }
    return 1;
}

s32 func_1518F15C(u8 *arg0) {
    Generated1BA1D0Record154 *self = (void *) arg0;
    s32 temp_v0 = self->timer;

    self->value30 = self->value30 - self->value30 * self->factor;
    if (temp_v0 < self->limit) {
        self->value5C = temp_v0 * (u32) self->scale;
    }
    return 1;
}

s32 func_1518F1A0() {
    return 0;
}

extern f32 D_800A7B74;
extern f32 D_800A7B78;

typedef struct {
    f32 firstUpper;
    f32 firstLower;
    f32 firstTarget;
    f32 secondUpper;
    f32 secondLower;
    f32 reserved14;
    f32 secondTarget;
    s16 firstReady;
    s16 secondReady;
} RandomTargets1BA1D0;

/* Initialize missing random targets, then interpolate the two live coordinates. */
s32 func_1518F384(u8 *object) {
    RandomTargets1BA1D0 *targets = (RandomTargets1BA1D0 *)(object + 0x110);

    if (targets->firstReady == 0) {
        targets->firstTarget = func_150ADA68() *
            (targets->firstUpper - targets->firstLower) + targets->firstLower;
        targets->firstReady = 1;
    }
    if (targets->secondReady == 0) {
        targets->secondTarget = func_150ADA68() *
            (targets->secondUpper - targets->secondLower) + targets->secondLower;
        targets->secondReady = 1;
    }
    *(f32 *)(object + 0x30) +=
        (targets->secondTarget - *(f32 *)(object + 0x30)) * D_800A7B74;
    *(f32 *)(object + 0x2C) +=
        (targets->firstTarget - *(f32 *)(object + 0x2C)) * D_800A7B78;
    return 1;
}

void func_1518F45C(s32 arg0, u8 arg1) {
    OneWord1BA1D0 tmp;

    tmp = *(OneWord1BA1D0 *) D_800A74D4;
    func_15169260(&tmp, 1, arg0, arg1);
}

void func_1518F49C(u8 *arg0, u8 *arg1, s32 arg2) {
    s32 temp_v0;
    s32 temp_v1;
    u8 temp_a0;
    u8 temp_a1;

    func_15169850((s32)arg1, ((u8 *)&arg2)[3], (s32)(arg0 + 0x18),
                  (s32)(arg0 + 0x1C), (s32)arg0);

    if (((u8 *)&arg2)[3] != 0x49) {
        return;
    }
    temp_v0 = *(s32 *)(arg0 + 0x18);
    temp_v1 = *(s32 *)arg1;
    temp_a0 = arg0[0x1C];
    temp_a1 = arg1[4];
    if ((temp_v0 != temp_v1) && (temp_a0 != temp_a1)) {
        return;
    }
    func_1516972C(arg0);
}

/* Select the object's preset, then forward the payload arguments. */
void *func_1518F51C(void *object, u8 variant, s16 mode, s8 first,
                  s8 second, s8 third, u8 value, s32 extraBytes,
                  u8 channel, s32 context) {
    u32 reserved; /* Retail keeps this word unwritten above the byte output. */
    u8 preset;

    if (object == NULL) {
        return NULL;
    }
    if (!func_1518FDC4(object, &preset, variant)) {
        return NULL;
    }
    return func_1518F5D0(object, &D_8008D630[preset][variant], mode, first,
                       second, third, value, extraBytes, channel, context);
}

void *func_1518F5D0() {
    return NULL;
}

s32 func_1518F7C4(u8 *arg0) {
    RandomStep1BA1D0 *step;
    f32 random;

    random = func_150ADA68();
    step = (RandomStep1BA1D0 *) (arg0 + 0x30);
    step->value += (step->base + random * step->scale) * D_800BE9A4;
    func_1518F8E0(arg0);

    if (step->callback == -1) {
        return 1;
    }
    return D_8008D67C[step->callback](arg0);
}

void func_1518F858(u8 *arg0) {
    volatile s8 *index = (s8 *) (arg0 + 0x89);

    if (*index == -1) {
        return;
    }

    D_8008D680[*index]();
}

void func_1518F89C(u8 *arg0) {
    FloatUpdate1BA1D0 *temp_v0;
    f32 r;

    r = func_150ADA68();
    temp_v0 = (FloatUpdate1BA1D0 *) (arg0 + 0x30);
    temp_v0->value = r * temp_v0->scale + temp_v0->base;
    func_1518F8E0(arg0);
}

s32 func_1518F8E0() {
    return 0;
}

s32 func_1518FC04(u8 *arg0, ThreeWord1BA1D0 *arg1) {
    u8 *temp = *(u8 **) (arg0 + 0x2C);

    *(ThreeWord1BA1D0 *) (temp + 0x34) = *arg1;
    func_1514BE20(temp);
    return 1;
}

s32 func_1518FC44(u8 *arg0, ThreeWord1BA1D0 *arg1) {
    u8 *temp = *(u8 **) (arg0 + 0x2C);

    *(ThreeWord1BA1D0 *) (temp + 0x34) = *arg1;
    func_1514BF50(temp);
    return 1;
}

s32 func_1518FC84() {
    return 0;
}

s32 func_1518FDC4() {
    return 0;
}

s32 func_1519003C() {
    return 0;
}

s32 func_1519021C() {
    return 0;
}

void func_151903D0(u8 *arg0) {
    func_15163DEC(arg0, arg0 + 0x20);
    func_15163F50(arg0, arg0 + 0x18);
}

void func_15190400(u8 *arg0, u8 *arg1, u8 arg2) {
    s32 temp_v0;
    s32 temp_v1;
    u8 temp_a2;
    u8 temp_a3;

    if (arg2 == 0) {
        temp_v0 = *(s32 *)(arg0 + 0x18);
        temp_v1 = *(s32 *)arg1;
        temp_a2 = arg0[0x1C];
        temp_a3 = arg1[4];
        if (temp_v0 != temp_v1) {
            if (temp_a2 != temp_a3) {
                return;
            }
        }
        func_1516972C(arg0);
    }
}

void func_15190454(u8 *arg0) {
    u8 *temp_v0;

    temp_v0 = *(u8 **)(arg0 + 0x40);
    *(s32 *)(temp_v0 + 0x84) = 0;
}

s32 func_15190464(s32 arg0) {
    func_15190454(arg0);
    func_151617C4(arg0);
}

s32 func_15190490(s32 arg0) {
    func_15190454(arg0);
    func_151617E4(arg0);
}

// Matched with guarded branch and call-setup scheduling normalization.
void func_151904BC(u8 *arg0) {
    s32 owner;
    u8 *volatile resource;

    if (*(u8 *volatile *)(arg0 + 0x84) != NULL) {
        func_1516972C(*(u8 *volatile *)(arg0 + 0x84));
    }
    owner = *(s32 *)(arg0 + 0x10);
    resource = arg0 + 0x30;
    func_1000FD38(func_1518E298, arg0, owner);
    func_151D2B4C(*(s32 *)(resource + 0x48));
}

void func_15190518(u8 *arg0) {
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    func_1516944C(0x3E, &rec, 0x2A);
}

void func_15190550(u8 *arg0, void *arg1, u8 arg2) {
    void (*callback)(u8 *, void *, u8);

    if (arg2 == 0x2A) {
        func_151D33FC(arg0, arg1);
    }

    callback = D_8008D684[arg0[0x8A]];
    if (callback != NULL) {
        callback(arg0, arg1, arg2);
    }
}

s32 func_151905BC() {
    return 0;
}

void func_151906C4(u8 *arg0) {
    u8 *target = *(u8 **)(*(u8 **)(arg0 + 0x10) + 0x31C);

    if (target != NULL) {
        target[0x1AC] = 0;
    }
}

void func_151906E0(u8 *arg0, s32 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x90;

    if (arg2 == 0x2D) {
        s32 temp_v1 = arg1[0];
        s32 temp_a2 = *(s32 *) (temp_v0 + 8);

        if (temp_v1 == temp_a2) {
            *(s32 *) (temp_v0 + 8) = arg1[1];
        } else if ((u32) arg1[1] - (u32) temp_a2 == 0) {
            *(s32 *) (temp_v0 + 8) = temp_v1;
        }
    }
}

void func_1519072C(u8 *arg0) {
    struct {
        s32 pad;
        s32 rec_ptr;
        struct {
            u8 *target;
            u8 code;
        } rec;
    } locals;

    locals.rec.target = arg0;
    locals.rec.code = *(arg0 + 0x3B);
    locals.rec_ptr = (s32)&locals.rec;
    func_151D343C(locals.rec_ptr, 0x2A);
    func_1518F45C(locals.rec_ptr, 0x49);
}

void func_15191B8C(s32, u8);
void *func_15167A68(s32, s32, s32, s32, u8, u8);
void *memcpy(void *, const void *, u32);
u8 func_151D8E20(void);
typedef struct {
    u8 *owner;
    u8 owner_id;
    u8 padding[7];
} OwnerBufferNotice1BA1D0;
/* Notify the owner, then allocate and initialize its payload buffer. */
void *func_15190770(struct185 *payload, s32 extraBytes, u8 priority, s32 context) {
    OwnerBufferNotice1BA1D0 notice;
    u8 *created;

    notice.owner = (u8 *)payload->unk0;
    notice.owner_id = ((u8 *)payload->unk0)[0x3B];
    func_15191B8C((s32)&notice, 14);
    created = func_15167A68(0x20, context, extraBytes + 0x300, 1, priority, 1);
    if (created == NULL) {
        return NULL;
    }
    memcpy(created + 0x10, payload, 12);
    *(u8 **)(created + 0x24) = created + 0x30;
    *(u8 **)(created + 0x28) = created + 0x300;
    *(s32 *)(created + 0x20) = 0;
    *(f32 *)(created + 0x1C) = 0.0f;
    bzero(created + 0x30, 0x2D0);
    created[0x2C] = func_151D8E20();
    return created;
}

s32 func_15190840(s32 arg0) {
    func_15191400(arg0);
    func_15169804(arg0);
}

s32 func_1519086C(s32 arg0) {
    func_15191400(arg0);
    func_15169824(arg0);
}

s32 func_15190898() {
    return 0;
}

s32 func_15190F9C() {
    return 0;
}

s32 func_1519108C() {
    return 0;
}

s32 func_15191400() {
    return 0;
}

s32 func_15191520() {
    return 0;
}

s32 func_1519187C(u8 *arg0) {
    Generated1BA1D0Record *self = (void *) arg0;
    s32 temp_v0 = self->timer;

    if (temp_v0 < self->limit) {
        s32 temp_v1 = temp_v0 * (u32) self->scale;

        if (temp_v1 < self->value) {
            self->value = temp_v1;
        }
    }
    return 1;
}

/* Release invalid owner links, or emit the owner payload before releasing the record. */
void func_151918BC(u8 *record) {
    /* Preserve the retail frame and the release flag spill at incoming SP - 9. */
    s32 unused[2];
    u8 release = 0;
    u8 *owner = *(u8 **)(record + 0x28);
    u8 *payload;

    (void)unused;
    if (*(s32 *)owner == 0) {
        release = 1;
    } else if (record[0x2C] != owner[0x3B]) {
        release = 1;
    }
    if (!release && *(s32 *)(owner + 0x1D4) != 0) {
        payload = record + 0x28;
        release = 1;
        if (record[0xD] & 1) {
            payload[8] |= 1;
            *(s16 *)(payload + 6) = *(s16 *)(record + 0xE);
        } else {
            *(s16 *)(payload + 6) = 300;
        }
        func_15190770((struct185 *)payload, 0, record[0xC], record[1]);
    }
    if (release) {
        func_1516972C(record);
    }
}

s32 func_15191980() {
    return 0;
}

s32 func_15191A84() {
    return 0;
}

void func_15191B8C(s32 arg0, u8 arg1) {
    OneWord1BA1D0 tmp;

    tmp.val = D_800A8010;
    func_151494E0(arg0, arg1);
    func_15169260(&tmp, 1, arg0, arg1);
}
