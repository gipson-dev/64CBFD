#include <ultra64.h>
#include "structs.h"
extern f32 D_800A0494,D_800A0498,D_800A049C,D_800A04A0,D_800A04A4;
u32 func_150ADA20(void);
f32 func_150ADA68(void);
void *func_151DB5D0(u8,const struct17 *,const struct17 *,f32,f32,f32,f32,s16,u8,s16,s16,u8,u8,s32);


typedef struct {
    u8 ownerTag; u8 padding1[3]; u8 *owner;
    u8 eventCode; u8 padding9[3]; f32 parameters[6];
    u8 mode; u8 padding25; s16 size; s16 spread; s16 lifetime;
    u8 padding2C[2]; s8 field2E; u8 field2F; s8 field30;
    u8 padding31[3]; f32 coefficient; u8 field38; s8 field39;
    u8 padding3A[2];
} AttachedSprayPacket;
void func_1516962C(s32,void *,u8);
void *func_15134DAC(AttachedSprayPacket *,s32);
extern f32 D_800A0490;


/* Submit two attached sprays, retaining fields changed by the first submission. */
void func_150C7020(u8 *owner,s16 lifetime,u8 unusedOpacity,s32 unusedMode) {
    AttachedSprayPacket packet;
    if (owner != 0) {
        func_1516962C(0x29,owner,0x12);
        packet.ownerTag = owner[0x3B];
        packet.owner = owner;
        packet.eventCode = 13;
        packet.parameters[0] = 2.0f;
        packet.parameters[1] = 0.0f;
        packet.parameters[2] = 34.0f;
        packet.parameters[3] = -15.0f;
        packet.parameters[4] = 0.0f;
        packet.parameters[5] = 34.0f;
        packet.mode = 0;
        packet.field2E = -1;
        packet.field2F = 1;
        packet.field30 = -1;
        packet.field38 = 2;
        packet.field39 = -1;
        packet.coefficient = D_800A0490;
        if (lifetime != 0) {
            packet.lifetime = lifetime;
            packet.mode = 2;
        } else {
            packet.lifetime = 300;
        }
        packet.size = func_150ADA20() % 66U + 35;
        packet.spread = func_150ADA20() % 26U + 25;
        func_15134DAC(&packet,0);
        packet.eventCode = 12;
        packet.parameters[0] = -2.0f;
        packet.parameters[1] = 0.0f;
        packet.parameters[2] = 34.0f;
        packet.parameters[3] = 15.0f;
        packet.parameters[4] = 0.0f;
        packet.parameters[5] = 34.0f;
        packet.size = func_150ADA20() % 66U + 35;
        packet.spread = func_150ADA20() % 26U + 25;
        func_15134DAC(&packet,0);
    }
}

/* Submit a scaled point-difference velocity with five ordered random draws. */
void func_150C71C0(f32 *first,f32 *second,f32 *unusedFirstStep,
                    f32 *unusedSecondStep,f32 unusedFraction,struct102 *emitter) {
    struct17 velocity;
    s16 lifetime;
    u32 opacityRandom;
    f32 thirdRandom;
    f32 secondRandom;
    f32 firstRandom;

    velocity.unk0 = (second[0] - first[0]) * 0.4070000052f;
    velocity.unk4 = (second[1] - first[1]) * 0.4070000052f;
    velocity.unk8 = (second[2] - first[2]) * 0.4070000052f;
    lifetime = func_150ADA20() % 31U + 42;
    firstRandom = func_150ADA68();
    secondRandom = func_150ADA68();
    thirdRandom = func_150ADA68();
    opacityRandom = func_150ADA20();
    func_151DB5D0(0,(const struct17 *)first,&velocity,
        firstRandom * 70.0f + 30.0f,
        secondRandom * D_800A0498 + D_800A049C,1.0f,
        thirdRandom * D_800A04A0 + D_800A04A4,
        lifetime,opacityRandom % 101U + 155,lifetime,255 / lifetime,1,
        ((u8 *)emitter)[0xC],((u8 *)emitter)[1]);
}
