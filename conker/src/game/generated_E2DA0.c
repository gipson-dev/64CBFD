#include <ultra64.h>
#include "structs.h"
extern u8 D_8009FC30[];
extern u8 D_800C35EA;
extern u8 D_800CC34A[];

s32 func_150ADA20(void);
void func_15182670(u8 arg0, u8 arg1, u8 arg2, u8 arg3, s16 arg4, u8 arg5,
                   u8 arg6, s32 arg7);

/* Non-matching placeholders for the text-only asm slice asm/E2DA0.s. */

u8 *func_150B58F0(u8 *arg0, s32 arg1) {
    if (D_800C35EA == 1) {
        return arg0;
    }

    *(u16 *) arg0 = 0x1A;
    *(u16 *) (arg0 + 2) = *(u16 *) (D_800CC34A + arg1 * 0x32C);
    return arg0 + 4;
}

typedef struct {
    f32 x, y, z;
} CompositeEffectPosition;
/* Array helpers and the aggregate descriptor share the same three floats. */
typedef union {
    CompositeEffectPosition vector;
    f32 array[3];
} CompositePositionStorage150B5A3C;

extern f32 D_8009FC98, D_8009FC9C;
f32 func_150ADA68(void);
void func_150B5A3C(CompositePositionStorage150B5A3C *,u8,s32);
void func_150B60E0(u8 *actor, f32 *output);
/* Expire a stale attachment or submit the two independently sampled effects. */
void func_150B5950(u8 *record) {
    f32 sample;
    CompositePositionStorage150B5A3C position;
    u8 *actor = *(u8 **)(record + 0x28);
    if (*(s32 *)actor == 0 || record[0x2C] != actor[0x3B]) {
        *(s16 *)(record + 0xE) = -1;
    } else if (*(s32 *)(actor + 0x1D4) != 0) {
        sample = func_150ADA68();
        if (sample < D_8009FC98) {
            position.array[0] = *(f32 *)(actor + 0x14);
            position.array[1] = *(f32 *)(actor + 0x18);
            position.array[2] = *(f32 *)(actor + 0x1C);
            func_150B5A3C(&position, record[0xC], record[1]);
        }
        sample = func_150ADA68();
        if (sample < D_8009FC9C) {
            func_150B60E0(actor, position.array);
            func_150B5A3C(&position, record[0xC], record[1]);
        }
    }
}



typedef struct {
    s32 baseCount;
    s32 countRange;
    CompositeEffectPosition position;
    f32 field14Base;
    f32 field18Range;
    f32 field1CBase;
    f32 field20Range;
    f32 radiusBase;
    f32 radiusRange;
    s16 firstBase;
    s16 firstRange;
    s16 secondBase;
    s16 secondRange;
    s32 headerByteBase;
    s32 headerByteRange;
    s16 headerShortBase;
    s16 headerShortRange;
    u16 field40;
    u8 fixed42;
    u8 fixed43;
    u8 fixed44;
    u8 byteBase45;
    u8 byteBase46;
    u8 byteBase47;
    u8 byteBase48;
    u8 byteRange49;
    u8 byteRange4A;
    u8 byteRange4B;
    u8 byteRange4C;
    u8 byteBase4D;
    u8 byteBase4E;
    u8 byteBase4F;
    u8 byteBase50;
    u8 byteRange51;
    u8 byteRange52;
    u8 byteRange53;
    u8 byteRange54;
    u8 byteBase55;
    u8 byteRange56;
    u8 fixed57;
    u8 fixed58;
    u8 padding59[3];
    s32 field5C;
    s32 field60;
    s16 field64;
    s16 field66;
    s16 field68;
    u8 field6A;
    u8 padding6B;
    f32 field6C;
    s8 field70;
    s8 field71;
    u8 privateTail72[2];
} CompositeEffectInput;
extern f32 D_8009FCA0,D_8009FCA4,D_8009FCA8;
void func_15152B38(CompositeEffectInput *,u8,s32);
void *func_150B5E34(CompositePositionStorage150B5A3C *,u8,s32);
void func_150B6000(f32 *,u8,s32);
/* Submit the fixed composite burst, then both companion effects. */
void func_150B5A3C(CompositePositionStorage150B5A3C *position,u8 mode,s32 extra) {
    CompositeEffectInput packet;
    packet.baseCount=5;
    packet.countRange=5;
    packet.position=position->vector;
    packet.field14Base=20.0f;
    packet.secondBase=-31;
    packet.headerByteRange=2;
    packet.secondRange=80;
    packet.headerByteBase=3;
    packet.headerShortBase=20;
    packet.headerShortRange=30;
    packet.field40=1;
    packet.fixed42=4;
    packet.fixed43=2;
    packet.byteBase46=255;
    packet.byteBase47=255;
    packet.firstRange=255;
    packet.fixed44=3;
    packet.byteBase45=255;
    packet.byteBase48=255;
    packet.byteBase4D=255;
    packet.byteBase4E=255;
    packet.byteBase4F=255;
    packet.byteBase50=255;
    packet.byteBase55=255;
    packet.firstBase=0;
    packet.byteRange49=0;
    packet.byteRange4A=0;
    packet.byteRange4B=0;
    packet.byteRange4C=0;
    packet.byteRange51=0;
    packet.byteRange52=0;
    packet.byteRange53=0;
    packet.byteRange54=0;
    packet.byteRange56=0;
    packet.fixed57=3;
    packet.fixed58=36;
    packet.field5C=0x200005;
    packet.field60=0x60600;
    packet.field64=8;
    packet.field66=31;
    packet.field68=1;
    packet.field6A=0;
    packet.field70=-1;
    packet.field71=0;
    ((s8 *)packet.privateTail72)[0]=-1;
    ((s8 *)packet.privateTail72)[1]=-1;
    packet.field18Range=D_8009FCA0;
    packet.field1CBase=D_8009FCA4;
    packet.field20Range=D_8009FCA8;
    packet.radiusBase=39.0f;
    packet.radiusRange=35.0f;
    packet.field6C=1.0f;
    func_15152B38(&packet,mode,extra);
    func_150B5E34(position,mode,extra);
    func_150B6000(position->array,mode,extra);
}


s32 func_150B5C38() {
    return 0;
}

typedef struct {
    u32 flags00, field04;
    s16 code08, lifetime;
    u32 zero0C, zero10;
    u8 rgba14[4], rgba18[4];
    u8 value1C, paletteIndex;
    s16 value1E, value20, value22;
    f32 scale, extentX, extentY;
    CompositeEffectPosition position, velocity, acceleration;
    f32 parameter;
    u32 flags58, reserved5C;
    u8 value60, value61;
    s8 value62, value63, value64, value65;
    u8 reserved66[2];
    s16 reserved68;
    u8 reserved6A[2];
    f32 reserved6C;
} RandomParticleDefinition150B5E34;
void *func_15130280(RandomParticleDefinition150B5E34 *,u8,void *,s32,u8,s32);
/* Build the randomized companion particle and return its allocation result. */
void *func_150B5E34(CompositePositionStorage150B5A3C *position,u8 mode,s32 extra) {
    RandomParticleDefinition150B5E34 packet;
    u32 firstFlag;
    packet.paletteIndex=43;
    packet.code08=0x4403;
    packet.flags00=0x200005;
    packet.field04=0x20000;
    packet.lifetime=(u32)func_150ADA20()%7U+4;
    packet.zero0C=0;
    packet.zero10=0;
    packet.rgba14[0]=255;
    packet.rgba14[1]=255;
    packet.rgba14[2]=255;
    packet.rgba14[3]=255;
    packet.rgba18[0]=255;
    packet.rgba18[1]=255;
    packet.rgba18[2]=255;
    packet.rgba18[3]=255;
    packet.value1C=255;
    packet.extentX=packet.extentY=func_150ADA68()*500.0f+500.0f;
    packet.position=position->vector;
    packet.value1E=3;
    packet.value20=85;
    packet.value22=1;
    packet.velocity.x=0.0f;
    packet.velocity.y=0.0f;
    packet.velocity.z=0.0f;
    packet.acceleration.x=0.0f;
    packet.acceleration.y=0.0f;
    packet.acceleration.z=0.0f;
    packet.parameter=0.0f;
    packet.scale=1.0f;
    firstFlag=(func_150ADA20()&1)?0x40:0;
    packet.flags58=((func_150ADA20()&1)?0x80:0)|1|firstFlag|0xC200;
    packet.value60=6;
    packet.value61=6;
    packet.value62=-1;
    packet.value63=-1;
    packet.value64=-1;
    packet.value65=4;
    return func_15130280(&packet,1,0,0,mode,extra);
}


struct225 *func_151602C0(Header *, Header2 *, s32, s32, s32, s32, u8, u8, s32, u8, s32);

/* Submit a randomized effect at the position's truncated integer coordinates. */
void func_150B6000(f32 *position, u8 kind, s32 mode) {
    Header header;
    Header2 coordinates;

    header.unk0 = 3;
    header.unk1 = -1;
    header.unk2 = (u32)func_150ADA20() % 9U + 3;
    header.unk4 = 0;
    coordinates.unk0 = position[0];
    coordinates.unk4 = position[1];
    coordinates.unk8 = position[2];
    func_151602C0(&header, &coordinates, ((u32)func_150ADA20() % 201U) + 55,
                 0xFF, 0xFF, 0xFF, 0xFF, 0, 0, kind, mode);
}

void func_150B60E0(u8 *arg0, f32 *arg1) {
    func_15143134(&D_8009FC30, arg1, *(s32 *) (arg0 + 0x1D4) + 0x140);
}

s32 func_150B6110() {
    return 0;
}

void func_150B6450(u8 *arg0, u8 arg1, u8 arg2) {
    if (arg2 == 0x4A) {
        func_1516972C(arg0);
    }
}

s32 func_150B648C() {
    return 0;
}

s32 func_150B66DC(u8 *arg0) {
    u8 *source;
    s32 result;
    s32 selector;

    source = *(u8 **)(arg0 + 0x18);
    selector = source[0x68];
    result = 1;
    selector -= 15;

    switch (selector) {
        case 0:
            *(*(u8 **)(arg0 + 0x14) + 9) = 1;
            break;
        case 1:
            *(*(u8 **)(arg0 + 0x14) + 9) = 0;
            *(*(u8 **)(arg0 + 0x14) + 0x2F) = 20;
            break;
        case 2:
        default:
            *(*(u8 **)(arg0 + 0x14) + 9) = 0;
            *(*(u8 **)(arg0 + 0x14) + 0x2F) = 40;
            break;
    }
    return result;
}

void func_150B6754(u8 arg0, s32 arg1) {
    func_15182670(0xCC, 0xCC, 0xFF, (func_150ADA20() % 56U) + 200,
                  (func_150ADA20() % 11U) + 15, 0, arg0, arg1);
}
