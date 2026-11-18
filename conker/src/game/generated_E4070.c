#include <ultra64.h>
typedef struct {
    u8 retained00[0x18];
    s32 progress;
    u8 retained1C[0x10];
    f32 xPosition;
    f32 yPosition;
    u8 retained34[0x11];
    u8 opacity;
} DiagonalMenuRecord150B709C;
extern s32 D_800BE9E8;
extern u8 D_800D98A0[];
void *func_151A4FD0(s32, u32, s32, s32, s32, s32, u8, u32);

extern u8 D_800D98A4[];
extern u8 D_800D9898[];
extern u8 D_800D98C0[];
extern void *D_800D9894;
extern s32 D_800BE9E4;
extern void func_1516972C(void *arg0);

/* Non-matching placeholders for the text-only asm slice asm/E4070.s. */

extern u8 D_800D9890;
void func_150B76BC(s32 x, s32 slot);

void func_150B6C90(void);
void func_150B6D34(void);
void func_150B6D78(void);
void func_150B7484(void);
void func_150B7560(void);
s32 func_150B765C(void);
s32 func_150B768C(void);
void func_150B77A8(void);
void func_150B791C(void);

/* Run one pending menu command; state 3 and out-of-range states are idle. */
void func_150B6BC0(s32 unusedView) {
    switch (D_800D9890) {
    case 1:
        func_150B6C90();
        break;
    case 2:
        func_150B6D34();
        break;
    case 4:
        func_150B6D78();
        break;
    case 5:
        func_150B7484();
        break;
    case 6:
        func_150B7560();
        break;
    case 7:
        func_150B765C();
        break;
    case 8:
        func_150B77A8();
        break;
    case 9:
        func_150B768C();
        break;
    case 10:
        func_150B791C();
        break;
    default: break;
    }
}

/* Replace the color record and reset the ten pointer slots. */
void func_150B6C90(void) {
    void **current;

    if (D_800D9894 != NULL) {
        func_1516972C(D_800D9894);
    }
    D_800D9894 = func_151A4FD0(0, 0, 255, 0, 0, D_800BE9E8, 0, 0);
    D_800D9890 = 3;
    ((void **)D_800D9898)[0] = NULL;
    ((void **)D_800D9898)[1] = NULL;
    current = (void **)D_800D98A0;
    do {
        current[1] = NULL;
        current[2] = NULL;
        current[3] = NULL;
        current[0] = NULL;
        current += 4;
    } while (current != (void **)D_800D98C0);
}

void func_150B6D34(void) {
    u8 *p;
    u8 *ptr = D_800D9898;

    do {
        p = *(u8 **) (ptr + 0x14);
        ptr += 4;
        if (p != 0) {
            *(s32 *) (p + 0x20) = 1;
        }
    } while (ptr != D_800D98A4);
    D_800D9890 = 3;
}

void func_150B6D78(void) {
    void **current;
    void **end;

    if (D_800D9894 != NULL) {
        func_1516972C(D_800D9894);
        D_800D9894 = NULL;
    }

    current = (void **)D_800D9898;
    end = (void **)D_800D98C0;
    do {
        if (*current != NULL) {
            func_1516972C(*current);
            *current = NULL;
        }
        current++;
    } while (current != end);

    D_800D9890 = 3;
}

void func_150B6DFC(u8 *arg0) {
    *(s16 *) (arg0 + 0x34) = *(s16 *) (arg0 + 0x34) + D_800BE9E4 * 48;
    if (*(s16 *) (arg0 + 0x34) >= 0x801) {
        *(s16 *) (arg0 + 0x34) = -0xC00;
    }
}

s32 func_150B6E3C() {
    return 0;
}

/* Advance the diagonal menu entry and pulse its terminal opacity. */
void func_150B709C(DiagonalMenuRecord150B709C *record) {
    s32 progress = record->progress;

    if (progress == 30) {
        s32 opacity = record->opacity;

        opacity += D_800BE9E4 * 8;
        if (opacity >= 256) {
            opacity = 0;
        }
        record->opacity = opacity;
    }
    progress += D_800BE9E4 * 2;
    if (progress >= 31) {
        progress = 30;
    }
    record->progress = progress;
    record->xPosition = (f32)((progress * -84) / 30 + 230);
    record->yPosition = (f32)((progress * -50) / 30 + 170);
}

void func_150B71A8(u8 *arg0) {
    if (*(s16 *) (arg0 + 0x38) != 0x1000) {
        *(s16 *) (arg0 + 0x38) += D_800BE9E4 << 8;
        if (*(s16 *) (arg0 + 0x38) > 0x1000) {
            *(s16 *) (arg0 + 0x38) = 0x1000;
        }
    } else if (*(s16 *) (arg0 + 0x3A) != 0x1000) {
        *(s16 *) (arg0 + 0x3A) += D_800BE9E4 << 8;
        if (*(s16 *) (arg0 + 0x3A) > 0x1000) {
            *(s16 *) (arg0 + 0x3A) = 0x1000;
        }
    }
}

s32 func_150B7220() {
    return 0;
}

void func_150B73F0(u8 *arg0) {
    s32 scale;
    s32 x;
    s32 y;

    scale = (*(s16 *)(arg0 + 0x24) << 16) / *(s32 *)(arg0 + 0x1C);
    x = (((*(s16 *)(arg0 + 0x20) - *(s16 *)(arg0 + 0x18)) * scale) >> 16) +
        *(s16 *)(arg0 + 0x18);
    y = (((*(s16 *)(arg0 + 0x22) - *(s16 *)(arg0 + 0x1A)) * scale) >> 16) +
        *(s16 *)(arg0 + 0x1A);
    *(f32 *)(arg0 + 0x2C) = (f32)x;
    *(f32 *)(arg0 + 0x30) = (f32)y;
}

extern u8 D_800918DC[];
void *func_15169968(void *);

typedef struct {
    u8 *asset;
    u8 *secondaryAsset;
    s32 field08;
    s32 field0C;
    s32 field10;
    s16 field14;
    s16 field16;
    s16 field18;
    u8 reserved1A[2];
    f32 field1C;
    f32 field20;
    s16 field24;
    s16 field26;
    s16 field28;
    s16 field2A;
    s16 field2C;
    s16 field2E;
    u8 field30;
    u8 field31;
    u8 field32;
    u8 field33;
    u8 field34;
    u8 field35;
    u8 field36;
    u8 field37;
    u8 field38;
    u8 field39;
    u8 reserved3A[2];
} MenuRecordDescriptorE4070;

/* Replace the menu record from its fixed descriptor, then select state 3. */
void func_150B7484(void) {
    MenuRecordDescriptorE4070 descriptor;

    descriptor.field31 = 1;
    descriptor.field2C = 88;
    descriptor.field1C = 60.0f;
    descriptor.field20 = 60.0f;
    descriptor.field14 = 0;
    descriptor.field16 = 0;
    descriptor.field18 = 0;
    descriptor.field2E = 88;
    descriptor.field30 = 6;
    descriptor.asset = D_800918DC;
    descriptor.field32 = 255;
    descriptor.field33 = 0;
    descriptor.field34 = 0;
    descriptor.field35 = 255;
    descriptor.field24 = 0;
    descriptor.field26 = 0;
    descriptor.field39 = 0;
    descriptor.field36 = 7;
    descriptor.field37 = 21;
    descriptor.field38 = 1;
    descriptor.field28 = 81;
    descriptor.field2A = 81;
    if (*(void **)D_800D9898 != NULL) {
        func_1516972C(*(void **)D_800D9898);
    }
    *(void **)D_800D9898 = func_15169968(&descriptor);
    D_800D9890 = 3;
}

/* Replace both fixed menu records, then select state 3. */
void func_150B7560(void) {
    MenuRecordDescriptorE4070 descriptor;

    if (*(void **)D_800D9898 != NULL) {
        func_1516972C(*(void **)D_800D9898);
        *(void **)D_800D9898 = NULL;
    }
    descriptor.field18 = 77;
    descriptor.field31 = 15;
    descriptor.field14 = 0;
    descriptor.field16 = 0;
    descriptor.field2C = 88;
    descriptor.field2E = 88;
    descriptor.field30 = 0;
    descriptor.asset = D_800918DC;
    descriptor.field24 = 0;
    descriptor.field26 = 0;
    descriptor.field32 = 255;
    descriptor.field33 = 0;
    descriptor.field34 = 0;
    descriptor.field35 = 255;
    descriptor.field36 = 7;
    descriptor.field37 = 17;
    descriptor.field38 = 1;
    descriptor.field39 = 0;
    descriptor.field28 = 4096;
    descriptor.field2A = 4096;
    descriptor.field1C = 60.0f;
    descriptor.field20 = 60.0f;
    if (*(void **)D_800D98A4 != NULL) {
        func_1516972C(*(void **)D_800D98A4);
    }
    *(void **)D_800D98A4 = func_15169968(&descriptor);
    D_800D9890 = 3;
}

s32 func_150B765C(void) {
    func_150B76BC(0x3C, 1);
    D_800D9890 = 3;
}

s32 func_150B768C(void) {
    func_150B76BC(0xE6, 2);
    D_800D9890 = 3;
}

extern u8 D_800918E8[];

/* Replace the selected menu record using its screen-position descriptor. */
void func_150B76BC(s32 x, s32 slot) {
    MenuRecordDescriptorE4070 descriptor;

    descriptor.field31 = 1;
    descriptor.field2C = 88;
    descriptor.field1C = (f32)x;
    descriptor.field2E = 64;
    descriptor.field20 = 170.0f;
    descriptor.field30 = 6;
    descriptor.field14 = 0;
    descriptor.field16 = 0;
    descriptor.field18 = 0;
    descriptor.asset = D_800918E8;
    descriptor.field32 = 255;
    descriptor.field33 = 0;
    descriptor.field34 = 0;
    descriptor.field35 = 255;
    descriptor.field24 = 0;
    descriptor.field26 = 0;
    descriptor.field39 = 0;
    descriptor.field36 = 7;
    descriptor.field37 = 21;
    descriptor.field38 = 1;
    descriptor.field28 = 81;
    descriptor.field2A = 81;
    if (((void **)D_800D9898)[slot] != NULL) {
        func_1516972C(((void **)D_800D9898)[slot]);
    }
    ((void **)D_800D9898)[slot] = func_15169968(&descriptor);
}

extern u8 D_800918F4[], D_80091900[];

/* Replace both menu layers using the shared, partially initialized descriptor. */
void func_150B77A8(void) {
    MenuRecordDescriptorE4070 descriptor;

    if (((void **)D_800D9898)[1] != NULL) {
        func_1516972C(((void **)D_800D9898)[1]);
        ((void **)D_800D9898)[1] = NULL;
    }
    descriptor.field2C = 64;
    descriptor.field2E = 64;
    descriptor.field30 = 4;
    descriptor.asset = D_800918F4;
    descriptor.secondaryAsset = D_80091900;
    descriptor.field14 = 0;
    descriptor.field16 = 0;
    descriptor.field18 = 0;
    descriptor.field31 = 0;
    descriptor.field24 = -2048;
    descriptor.field26 = 9;
    descriptor.field32 = 255;
    descriptor.field33 = 0;
    descriptor.field34 = 0;
    descriptor.field35 = 255;
    descriptor.field36 = 13;
    descriptor.field37 = 18;
    descriptor.field38 = 2;
    descriptor.field39 = 3;
    descriptor.field28 = 4096;
    descriptor.field2A = 4096;
    descriptor.field1C = 60.0f;
    descriptor.field20 = 170.0f;
    if (((void **)D_800D9898)[4] != NULL) {
        func_1516972C(((void **)D_800D9898)[4]);
    }
    ((void **)D_800D9898)[4] = func_15169968(&descriptor);
    descriptor.field24 = 0;
    descriptor.field26 = 0;
    descriptor.field2C = 88;
    descriptor.field2E = 64;
    descriptor.field30 = 0;
    descriptor.field36 = 7;
    descriptor.field37 = 17;
    descriptor.asset = D_800918E8;
    descriptor.field38 = 1;
    if (((void **)D_800D9898)[8] != NULL) {
        func_1516972C(((void **)D_800D9898)[8]);
    }
    ((void **)D_800D9898)[8] = func_15169968(&descriptor);
    D_800D9890 = 3;
}


extern u8 D_8009190C[];

/* Replace the four menu records, preserving retail's conditional release targets. */
void func_150B791C(void) {
    MenuRecordDescriptorE4070 descriptor;

    if (((void **)D_800D9898)[2] != NULL) {
        func_1516972C(((void **)D_800D9898)[2]);
        ((void **)D_800D9898)[2] = NULL;
    }
    descriptor.field31 = 3;
    descriptor.field2C = 64;
    descriptor.field2E = 16;
    descriptor.field30 = 5;
    descriptor.field20 = 150.0f;
    descriptor.field1C = 230.0f;
    descriptor.field0C = (s32)descriptor.field20;
    descriptor.field24 = 0;
    descriptor.field26 = 0;
    descriptor.field14 = 0;
    descriptor.field16 = 0;
    descriptor.field18 = 0;
    descriptor.asset = D_8009190C;
    descriptor.secondaryAsset = NULL;
    descriptor.field08 = 0;
    descriptor.field10 = 0;
    descriptor.field32 = 255;
    descriptor.field33 = 0;
    descriptor.field34 = 0;
    descriptor.field35 = 128;
    descriptor.field36 = 7;
    descriptor.field37 = 17;
    descriptor.field38 = 1;
    descriptor.field39 = 0;
    descriptor.field28 = 4096;
    descriptor.field2A = 4096;
    if (((void **)D_800D9898)[5] != NULL) {
        func_1516972C(((void **)D_800D9898)[5]);
    }
    ((void **)D_800D9898)[5] = func_15169968(&descriptor);
    descriptor.field16 = 256;
    descriptor.field08 = 256;
    descriptor.field35 = 255;
    descriptor.field20 = 170.0f;
    descriptor.field0C = (s32)descriptor.field20;
    /* The gate is slot6, but the original release argument is the first result. */
    if (((void **)D_800D9898)[6] != NULL) func_1516972C(((void **)D_800D9898)[5]);
    ((void **)D_800D9898)[6] = func_15169968(&descriptor);
    descriptor.field16 = 512;
    descriptor.field08 = 512;
    descriptor.field35 = 128;
    descriptor.field20 = 190.0f;
    descriptor.field0C = (s32)descriptor.field20;
    /* Likewise, slot7 gates a release of the then-current slot5 pointer. */
    if (((void **)D_800D9898)[7] != NULL) {
        func_1516972C(((void **)D_800D9898)[5]);
    }
    ((void **)D_800D9898)[7] = func_15169968(&descriptor);
    descriptor.field14 = 0;
    descriptor.field16 = 0;
    descriptor.field18 = 0;
    descriptor.field31 = 0;
    descriptor.field2C = 88;
    descriptor.field2E = 64;
    descriptor.field35 = 255;
    descriptor.field30 = 0;
    descriptor.asset = D_800918E8;
    descriptor.field1C = 230.0f;
    descriptor.field20 = 170.0f;
    if (((void **)D_800D9898)[9] != NULL) func_1516972C(((void **)D_800D9898)[9]);
    ((void **)D_800D9898)[9] = func_15169968(&descriptor);
    D_800D9890 = 3;
}


typedef struct { f32 x, y, z; } MenuBurstPointE4070;

typedef struct {
    u8 reserved00[0x14];
    MenuBurstPointE4070 position;
    u8 reserved20[0x1C];
    f32 radialOffset, field40;
    u8 reserved44[0x32];
    u16 heading;
    u8 reserved78[0x40];
    f32 fieldB8;
    u8 reservedBC[8];
    f32 fieldC4;
    u8 reservedC8[0x84];
    f32 factorX, factorY;
    u8 reserved154[0x30];
    u32 field184;
    u8 reserved188[0x4C];
    void *model;
} ActorBurstE4070;
typedef struct {
    f32 field00, field04, field08, field0C;
    f32 field10, field14, field18, field1C, field20, field24;
    MenuBurstPointE4070 position;
    MenuBurstPointE4070 velocity;
    f32 field40, field44, field48, field4C;
    u32 flags;
    s16 field54;
    u16 resource;
    u8 field58, reserved59[3];
    u32 field5C;
    u8 field60, field61, field62, field63, field64, field65;
    u8 field66, field67, field68, reserved69, field6A, reserved6B;
    u32 field6C;
    u8 field70, reserved71;
    s16 field72, field74;
    u8 reserved76[6];
} ActorChildDescriptorE4070;
typedef struct {
    MenuBurstPointE4070 position;
    f32 field0C, field10, field14, field18, field1C, field20;
    s16 field24, field26, field28, field2A, field2C, field2E;
    s16 field30, field32, field34, field36;
    u8 field38, field39, field3A, reserved3B;
    u32 field3C, field40, field44, field48, field4C, field50;
    u8 field54, field55, field56, reserved57;
    u32 field58, field5C, field60, field64, field68;
    u32 field6C, field70, field74, field78;
    u8 field7C, field7D, reserved7E[2];
    s16 field80, field82;
    u32 field84;
} ActorSprayDescriptorE4070;
typedef struct { f32 height; u8 retained04[0x20]; } ActorHeightResultE4070;
extern MenuBurstPointE4070 D_8009FD30, D_8009FD3C, D_8009FD48;
extern f32 D_8009FD54, D_8009FD58, D_8009FD5C, D_8009FD60, D_8009FD64;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
f32 func_151423D8(u8);
f32 sqrtf(f32);
f32 fabsf(f32);
#pragma intrinsic (fabsf)
void func_15142314(void *, s32, MenuBurstPointE4070 *);
void func_15143134(MenuBurstPointE4070 *, MenuBurstPointE4070 *, void *);
void func_1515C244(ActorBurstE4070 *, MenuBurstPointE4070 *, f32 *, f32 *);
void func_150B82D0(MenuBurstPointE4070 *, f32 *, f32 *, f32 *, u8, s32);
void *func_150B85C0(MenuBurstPointE4070 *, f32 *, f32 *, u8, s32);
void func_1504715C(ActorHeightResultE4070 *, ActorBurstE4070 *);
s32 func_15046C80(MenuBurstPointE4070 *, u16, f32, ActorHeightResultE4070 *);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);
void *func_15132A4C(void *, s32, s32, s32, u8, s32);
void func_15151A38(void *, u8, s32);


/* Emit the actor's bound burst, ground effect, and two endpoint sprays. */
void func_150B7B40(ActorBurstE4070 *actor, u8 slot, s32 context) {
    MenuBurstPointE4070 endpoints[2];
    MenuBurstPointE4070 origin;
    f32 sine, cosine, factorX, factorY, magnitude;
    ActorChildDescriptorE4070 child;
    f32 headingSine, headingCosine, pitchSine, pitchCosine;
    f32 offsetX, offsetZ;
    MenuBurstPointE4070 center;
    f32 height, radius, ratio;
    MenuBurstPointE4070 boundA, boundB;
    f32 dx, dz;
    void *matrix;
    ActorHeightResultE4070 floor;
    MenuBurstPointE4070 probe;
    s16 heading, pitch;
    s16 duration;
    s8 index;
    f32 averageScale;
    f32 componentScale;
    f32 magnitudeSample;
    f32 rotationSampleX;
    f32 rotationSampleY;
    ActorSprayDescriptorE4070 spray;

    if (actor == NULL) return;
    if (actor->model != NULL) {
        func_15142314(actor->model, 4, &endpoints[0]);
        func_15142314(actor->model, 5, &endpoints[1]);
        func_15142314(actor->model, 0, &origin);
    } else {
        origin.x = actor->position.x;
        origin.y = actor->position.y;
        origin.z = actor->position.z;
        endpoints[0].x = origin.x + 20.0f;
        endpoints[1].x = origin.x - 20.0f;
        endpoints[0].y = endpoints[1].y = origin.y + 130.0f;
        endpoints[0].z = endpoints[1].z = origin.z;
    }
    sine = func_151423D8((actor->heading >> 8) & 255);
    cosine = func_151423D8(((actor->heading >> 8) + 64) & 255);
    offsetX = actor->radialOffset * sine;
    offsetZ = actor->radialOffset * cosine;
    matrix = actor->model;
    if (matrix != NULL) {
        matrix = (u8 *)matrix + 0x80;
        func_15143134(&D_8009FD30, &center, matrix);
        func_15143134(&D_8009FD3C, &boundA, matrix);
        func_15143134(&D_8009FD48, &boundB, matrix);
        height = fabsf(center.y - boundA.y);
        dx = boundB.x - boundA.x;
        dz = boundB.z - boundA.z;
        radius = sqrtf(dx * dx + dz * dz);
    } else {
        func_1515C244(actor, &center, &radius, &height);
    }
    ratio = radius != 0.0f ? height / radius : 1.0f;
    func_150B82D0(&center, &height, &radius, &ratio, slot, context);
    func_150B85C0(&center, &height, &radius, slot, context);
    probe.x = center.x;
    probe.y = center.y + 100.0f;
    probe.z = center.z;
    func_1504715C(&floor, actor);
    if (func_15046C80(&probe, 0, center.y - 2000.0f, &floor)) {
        probe.y = floor.height;
        duration = (u32)func_150ADA20() % 11U + 30;
        func_1514C678(probe.x, probe.y + 31.0f, probe.z, radius,
            0, 255, duration, 25, 0, 0.0f, NULL, slot);
    }
    child.field04 = D_8009FD54;
    child.field54 = 300;
    child.resource = 0;
    child.field10 = actor->fieldB8;
    child.field14 = actor->field40;
    child.field18 = actor->fieldC4;
    child.field1C = child.field20 = child.field24 = 1.0f;
    child.flags = 0x197D;
    child.field58 = 0;
    child.field5C = 0;
    child.field60 = 255;
    child.field61 = 1;
    child.field62 = 0;
    child.field63 = 1;
    child.field64 = 0;
    child.field65 = 1;
    child.field66 = 0;
    child.field67 = 0;
    child.field68 = 0;
    child.field6A = 0;
    child.field6C = 0;
    child.field70 = 0;
    child.field72 = 1;
    child.field74 = 255;
    child.field48 = 0.0f;
    child.field4C = D_8009FD58;
    factorX = actor->factorX;
    if (factorX > 1.0f) factorX = 1.0f;
    if (factorX < 0.5f) factorX = 0.5f;
    factorY = actor->factorY;
    if (factorY > 1.0f) factorY = 1.0f;
    if (factorY < 0.5f) factorY = 0.5f;
    child.field00 = (28.0f * factorY + 28.0f * factorX) * 0.5f;
    child.field08 = 3.0f * factorX;
    child.field0C = 3.0f * factorY;
    index = 0;
    do {
        magnitudeSample = func_150ADA68();
        magnitude = (magnitudeSample * 30.0f) * actor->factorY + 10.0f;
        heading = (u32)func_150ADA20() & 127;
        pitch = -32 - ((u32)func_150ADA20() & 31);
        headingSine = func_151423D8(heading);
        headingCosine = func_151423D8(heading - 64);
        pitchSine = func_151423D8(pitch);
        pitchCosine = func_151423D8(pitch - 64);
        child.position = endpoints[index];
        child.velocity.x = (magnitude * pitchSine) * headingCosine + offsetX;
        child.velocity.y = -magnitude * pitchCosine;
        child.velocity.z = (magnitude * pitchSine) * headingSine + offsetZ;
        rotationSampleX = func_150ADA68();
        child.field40 = 30.0f - rotationSampleX * 60.0f;
        rotationSampleY = func_150ADA68();
        child.field44 = 30.0f - rotationSampleY * 60.0f;
        func_15132A4C(&child, 3, 2, 0, slot, 0);
        averageScale = ((actor->factorX + actor->factorY) * 0.5f) / D_8009FD5C;
        spray.position = endpoints[index];
        spray.field24 = 4;
        spray.field26 = 4;
        spray.field2A = 255;
        spray.field2C = -63;
        spray.field2E = 75;
        spray.field34 = 50;
        spray.field36 = 20;
        spray.field30 = 3;
        spray.field32 = 3;
        spray.field39 = 33;
        spray.field3A = 72;
        spray.field3C = 1;
        spray.field55 = 155;
        spray.field56 = 100;
        spray.field58 = 3;
        componentScale = 3.0f * averageScale;
        spray.field0C = componentScale;
        spray.field10 = componentScale;
        spray.field1C = 15.0f * averageScale;
        spray.field20 = 10.0f * averageScale;
        spray.field28 = 0;
        spray.field38 = 1;
        spray.field40 = 0;
        spray.field44 = 0;
        spray.field48 = 0;
        spray.field4C = 0;
        spray.field50 = 0;
        spray.field54 = 0;
        spray.field5C = 255;
        spray.field60 = 0;
        spray.field64 = 0x220005;
        spray.field68 = 0x1D0600;
        spray.field6C = 1;
        spray.field70 = 0x3B;
        spray.field74 = 0x80;
        spray.field78 = 0x20;
        spray.field7C = 0;
        spray.field7D = 7;
        spray.field80 = 10;
        spray.field82 = 25;
        spray.field14 = D_8009FD60;
        spray.field18 = D_8009FD64;
        spray.field84 = actor->field184;
        func_15151A38(&spray, slot, context);
        index++;
    } while (index < 2);
}


s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_15143794(s16, s16, f32, MenuBurstPointE4070 *);
void *func_1518A3C0(MenuBurstPointE4070 *, MenuBurstPointE4070 *, f32,
    MenuBurstPointE4070 *, MenuBurstPointE4070 *, f32, f32, u8, s16, u8,
    s32, u8, s32);

/* Emit a randomized burst around the caller's position and scaled dimensions. */
void func_150B82D0(MenuBurstPointE4070 *center, f32 *unusedHeight, f32 *radius,
                    f32 *ratio, u8 unusedSlot, s32 unusedContext) {
    MenuBurstPointE4070 position;
    MenuBurstPointE4070 rotation;
    MenuBurstPointE4070 velocity;
    MenuBurstPointE4070 acceleration;
    s32 remaining;
    s16 heading;
    s16 pitch;
    f32 firstSample, secondSample;

    remaining = (u32)func_150ADA20() % 26U + 35;
    if (remaining > 0) {
        do {
            heading = (u32)func_150ADA20() & 255;
            pitch = (u32)func_150ADA20() % 61U - 63;
            func_15143794(heading, pitch, *radius, &position);
            position.y *= *ratio;
            position.x += center->x;
            position.y += center->y;
            position.z += center->z;
            rotation.x = func_150ADA68() * 360.0f;
            rotation.y = func_150ADA68() * 360.0f;
            rotation.z = func_150ADA68() * 360.0f;
            func_15143794(heading, pitch,
                (func_150ADA68() * 1221.0f + 1806.0f) * 0.01f,
                &velocity);
            acceleration.x = (func_150ADA68() * 3140.0f + -1570.0f) * 0.01f;
            acceleration.y = 0.0f;
            acceleration.z = (func_150ADA68() * 3140.0f + -1570.0f) * 0.01f;
            firstSample = func_150ADA68();
            secondSample = func_150ADA68();
            func_1518A3C0(&position, &rotation,
                (firstSample * 104.0f + 78.0f) * 0.001f, &velocity,
                &acceleration, (secondSample * 633.0f + -1064.0f) * 0.001f,
                0.9425339698791504f, 1, (u32)func_150ADA20() % 51U + 75, 0, 0, 255, 1);
            remaining--;
        } while (remaining != 0);
    }
}


typedef struct {
    u32 field00, field04;
    s16 field08, field0A;
    u32 field0C, field10;
    u8 field14, field15, field16, field17;
    u8 field18, field19, field1A, field1B;
    u8 field1C, field1D;
    s16 field1E, field20, field22;
    f32 field24, field28, field2C;
    MenuBurstPointE4070 position;
    f32 field3C, field40, field44;
    MenuBurstPointE4070 direction;
    f32 field54;
    u32 flags;
    u8 reserved5C[4];
    u8 field60, field61;
    s8 field62;
    s8 field63, field64;
    u8 field65, reserved66[10];
} MenuRadialPacketE4070;
extern f32 D_8009FD88;
s32 func_150ADA20(void);
void *func_15130374(void *, u8, s32, u8, s32);


/* Submit the scaled radial packet and return the factory's allocation result. */
void *func_150B85C0(MenuBurstPointE4070 *position, f32 *height, f32 *radius,
                    u8 slot, s32 context) {
    MenuRadialPacketE4070 packet;
    s32 secondFlag;
    s32 firstFlag;

    packet.field1D = 41;
    packet.field08 = 0xE03;
    packet.field00 = 0x200005;
    packet.field04 = 0;
    packet.field0A = (u32)func_150ADA20() % 11U + 35;
    packet.field0C = 0;
    packet.field10 = 0;
    packet.field18 = 176;
    packet.field19 = 160;
    packet.field1A = 42;
    packet.field14 = 64;
    packet.field15 = 11;
    packet.field16 = 106;
    packet.field17 = 255;
    packet.field1B = (u32)func_150ADA20() % 51U + 100;
    packet.field1C = 255;
    packet.field60 = 3;
    packet.field61 = 3;
    packet.field28 = *radius * 20.0f;
    packet.field2C = *height * 20.0f;
    packet.position = *position;
    packet.field3C = 0.0f;
    packet.field40 = 0.0f;
    packet.field44 = 0.0f;
    packet.direction.x = 0.0f;
    packet.direction.y = 0.0f;
    packet.direction.z = 0.0f;
    packet.field54 = 0.0f;
    firstFlag = (func_150ADA20() & 1) ? 0x40 : 0;
    secondFlag = (func_150ADA20() & 1) ? 0x80 : 0;
    packet.flags = secondFlag | 0xE01 | firstFlag | 0xC000;
    packet.field62 = -1;
    packet.field63 = -1;
    packet.field1E = 25;
    packet.field20 = 10;
    packet.field22 = 40;
    packet.field64 = -1;
    packet.field65 = 0;
    packet.field24 = D_8009FD88;
    return func_15130374(&packet, 1, 0, slot, context);
}


extern f32 D_8009FD8C, D_8009FD90, D_8009FD94, D_8009FD98, D_8009FD9C, D_8009FDA0;
void func_15143874(s16, f32, f32 *, f32 *);
void *memcpy(void *, const void *, size_t);


/* Submit the menu radial descriptor and retain its pre-sampled object value. */
s32 func_150B879C(s32 kind, s16 index, f32 x, f32 y, f32 z,
                    f32 unused5, f32 unused6, f32 unused7, s16 heading, u8 unused9,
                    f32 unused10, s32 unused11, f32 unused12, s32 unused13, u8 slot) {
    f32 bonus;
    MenuRadialPacketE4070 packet;
    f32 sample;
    s32 secondFlag;
    s32 firstFlag;
    void *allocated;

    bonus = D_8009FD8C;
    packet.field1D = 41;
    packet.field08 = 0xE03;
    packet.field00 = 0x200005;
    packet.field04 = 0;
    packet.field0A = ((u32)func_150ADA20() & 15) + 25;
    packet.field0C = 0;
    packet.field10 = 0;
    packet.field18 = 176;
    packet.field19 = 160;
    packet.field1A = 42;
    packet.field14 = 64;
    packet.field15 = 11;
    packet.field16 = 106;
    packet.field17 = 255;
    packet.field1B = (u32)func_150ADA20() % 71U + 60;
    packet.field1C = 255;
    packet.field60 = 3;
    packet.field61 = 3;
    sample = func_150ADA68();
    packet.field28 = packet.field2C = (sample * D_8009FD90 + D_8009FD94) * D_8009FD98;
    packet.position.x = x;
    packet.position.y = y;
    packet.position.z = z;
    packet.field3C = 0.0f;
    packet.field40 = 0.0f;
    packet.field44 = 0.0f;
    sample = func_150ADA68();
    func_15143874(heading, (sample * 154.0f + 205.0f) * D_8009FD9C,
        &packet.direction.x, &packet.direction.z);
    packet.direction.y = 0.0f;
    packet.field54 = 0.0f;
    firstFlag = (func_150ADA20() & 1) ? 0x40 : 0;
    secondFlag = (func_150ADA20() & 1) ? 0x80 : 0;
    packet.flags = secondFlag | 0xE05 | firstFlag | 0xC000;
    packet.field62 = 10;
    packet.field63 = -1;
    packet.field1E = 28;
    packet.field20 = 9;
    packet.field22 = 25;
    packet.field64 = -1;
    packet.field65 = 0;
    packet.field24 = D_8009FDA0;
    allocated = func_15130374(&packet, 1, 4, slot, 1);
    if (allocated != NULL) memcpy((u8 *)allocated + 0xA8, &bonus, 4);
    return 1;
}
