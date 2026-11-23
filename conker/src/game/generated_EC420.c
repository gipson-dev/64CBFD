#include <ultra64.h>

extern s32 D_800BE9E4;

/* Non-matching placeholders for the text-only asm slice asm/EC420.s. */

void func_150BEF70(s32 arg0) {
}

void func_1516D99C(
    s16 arg0, s16 arg1, s16 arg2, u8 arg3, u8 arg4, u8 arg5,
    u8 arg6, u8 arg7, u8 arg8, u8 arg9, u8 arg10, u8 arg11,
    u8 arg12, u8 arg13, u8 arg14, u8 arg15, u8 arg16, u8 arg17,
    u8 arg18, u8 arg19, u8 arg20, u8 arg21, u8 arg22, u8 arg23,
    u8 arg24, u8 arg25, u8 arg26, s16 arg27, s16 arg28, s16 arg29,
    s16 arg30, u16 arg31, u8 arg32, u8 arg33, u8 arg34, u8 arg35,
    s16 arg36, u16 arg37, u16 arg38, u8 arg39, u8 arg40, u8 arg41,
    u8 arg42, u8 arg43, s32 arg44, u8 arg45, u8 arg46, s32 arg47,
    s32 arg48);

/* Submit the same factory request at two opposite signed positions. */
void func_150BEF7C(s32 parameter) {
    s32 position;
    s32 count;

    position = 380;
    count = 0;
    do {
        func_1516D99C(0x1FDB, 0x25, (s16)position, 0xD, 0, 0x50, 0x8F,
            0, 0, 0, 0, 0, 8, 200,
            10, 0, 0, 0, 0, 0, 40,
            40, 4, 0, 0, 0, 0, 0x555,
            0x555, 0x555, 0x555, parameter, 50, 0, 255,
            20, 4000, 2000, 1, 6, 0, 1,
            0, 0, 0, 0, 3, 255, 0);
        count++;
        position = -position;
    } while (count != 2);
}

/* Advance effect intensity and two signed accumulators; return 1 when finished. */
s32 func_150BF0F4(u8 *record) {
    s32 value = record[0x1F];
    s32 target = record[0x26];
    s32 phase;
    if (record[0x24] != 0) {
        if (value != target) {
            value = (s32)((u32)value + (u32)D_800BE9E4 * record[0x27]);
            if (value > target) value = target;
            record[0x1F] = value;
        }
    } else if (value != 0) {
        value = (s32)((u32)value - (u32)D_800BE9E4 * record[0x2F]);
        if (value < 0) value = 0;
        record[0x1F] = value;
    }
    if (record[0x24] == 0 && value == 0) return 1;
    *(s16 *)(record + 0x14) = (s32)((u32)*(s16 *)(record + 0x14) + (u32)(s32)*(s8 *)(record + 0x2D) * (u32)D_800BE9E4);
    *(s16 *)(record + 0x16) = (s32)((u32)*(s16 *)(record + 0x16) + (u32)(s32)*(s8 *)(record + 0x2E) * (u32)D_800BE9E4);
    if (*(s16 *)(record + 0x14) <= 0) {
        *(s16 *)(record + 0x16) = 0;
        *(s16 *)(record + 0x14) = *(s16 *)(record + 0x16);
        return 1;
    }
    phase = (s32)((u32)record[0x2C] + (u32)D_800BE9E4);
    if (phase >= 128) phase = 127;
    record[0x2C] = phase;
    return 0;
}

s32 func_150BF21C() {
    return 0;
}

s32 func_150BF760() {
    return 0;
}

s32 func_150BFA7C() {
    return 0;
}

typedef struct { f32 x, y, z; } EmissionPositionEC420;
typedef struct {
    s16 count, countRange;
    u8 kind, reserved05;
    u16 field06;
    u32 header, field0C;
    s16 field10, field12;
    u32 field14, field18;
    u8 field1C, field1D, field1E, field1F;
    u8 field20, field21, field22, field23, field24, field25;
    s16 field26, field28, field2A;
    f32 field2C, field30, field34;
    EmissionPositionEC420 position;
    s16 field44, field46, field48, field4A;
    f32 field4C, field50, field54, field58;
    u32 flags;
    s8 field60, field61;
    u8 field62, field63, field64;
    u8 reserved65[3];
    f32 payloadValue;
} EmissionPresetEC420;
extern f32 D_800A0134,D_800A0138,D_800A013C,D_800A0140,D_800A0144,D_800A0148;
void func_15136C3C(void *,u8,u8,u8,u8,u8,u8,s32);
void func_15153634(void *,u8,u8,s32);

/* Snapshot the actor position before the effect helper, then emit this preset. */
void func_150BFFE0(u8 *actor) {
    EmissionPositionEC420 position;
    EmissionPresetEC420 packet;
    position.x = *(f32 *)(actor + 0x14);
    position.y = *(f32 *)(actor + 0x180) + 70.0f;
    position.z = *(f32 *)(actor + 0x1C);
    func_15136C3C(actor,0,0,1,0,0,255,1);
    packet.field2C = D_800A0134;
    packet.field34 = D_800A013C;
    packet.position.x = position.x;
    packet.position.y = position.y + 35.0f;
    packet.field4C = 15.0f;
    packet.field50 = 39.0f;
    packet.field54 = D_800A0140;
    packet.count = 17;
    packet.countRange = 7;
    packet.kind = 108;
    packet.field06 = 0x5103;
    packet.header = 0x200005;
    packet.field10 = 40;
    packet.field12 = 20;
    packet.field1F = 255;
    packet.field1C = 78;
    packet.field58 = D_800A0144;
    packet.field22 = 200;
    packet.field1D = 84;
    packet.field1E = 123;
    packet.field20 = 164;
    packet.field21 = 161;
    packet.field23 = 155;
    packet.field24 = 100;
    packet.field25 = 255;
    packet.field26 = 30;
    packet.field28 = 8;
    packet.field30 = D_800A0138;
    packet.payloadValue = D_800A0148;
    packet.field0C = 0;
    packet.field14 = 0;
    packet.field18 = 0;
    packet.field2A = 30;
    packet.field44 = 0;
    packet.field46 = -20;
    packet.field48 = 255;
    packet.field4A = 30;
    packet.flags = 0x40040E07;
    packet.field60 = 16;
    packet.field61 = -1;
    packet.field62 = 8;
    packet.field63 = 6;
    packet.field64 = 1;
    packet.position.z = position.z;
    func_15153634(&packet,255,255,1);
}


typedef struct {
    s32 count, countRange;
    EmissionPositionEC420 position;
    s16 angle, angleRange, pitch, pitchRange;
    f32 speed, speedRange, vertical, verticalRange;
    s16 lifetime, lifetimeRange;
    f32 scale, scaleRange, spread;
} BurstConfigurationEC420;
typedef struct { s32 value; } ResourceOneEC420;
typedef struct { f32 value; } ScaleOneEC420;
extern ResourceOneEC420 D_800A0100;
extern ScaleOneEC420 D_800A0104;
extern f32 D_800A014C, D_800A0150, D_800A0154, D_800A0158, D_800A015C;
extern f32 D_800A0160, D_800A0164, D_800A0168, D_800A016C;
void func_15152190(BurstConfigurationEC420 *, s32 *, f32 *, s32, f32, u8, u8, s32);

/* Impact callback: capture the owner position, then submit both effect presets.
 * The callback position arguments and contact pointer are unused by this preset. */
s32 func_150C01DC(u8 *owner, f32 unusedX, f32 unusedY, f32 unusedZ,
    f32 height, void *contact) {
    EmissionPositionEC420 position;
    BurstConfigurationEC420 burst;
    ResourceOneEC420 resource;
    ScaleOneEC420 scale;
    EmissionPresetEC420 emission;
    f32 sharedScale;

    position.x = *(f32 *)(owner + 0x38);
    position.y = height + 20.0f;
    position.z = *(f32 *)(owner + 0x40);
    resource = D_800A0100;
    scale = D_800A0104;
    burst.count = 5;
    burst.countRange = 4;
    burst.position = position;
    burst.angle = 0;
    burst.angleRange = 255;
    burst.pitch = -64;
    burst.pitchRange = 34;
    burst.speed = 12.0f;
    burst.speedRange = 8.0f;
    burst.vertical = D_800A014C;
    burst.verticalRange = D_800A0150;
    burst.lifetime = 30;
    burst.lifetimeRange = 15;
    burst.scale = D_800A0154;
    burst.scaleRange = D_800A0158;
    burst.spread = D_800A015C;
    func_15152190(&burst, &resource.value, &scale.value, 1, 0.0f, 1,
        owner[0xC], owner[1]);

    sharedScale = D_800A0160;
    emission.field2C = D_800A0164;
    emission.field30 = 218.0f;
    emission.field34 = D_800A0168;
    emission.count = 5;
    emission.countRange = 8;
    emission.kind = 108;
    emission.field06 = 0x5103;
    emission.header = 0x200005;
    emission.field10 = 30;
    emission.field12 = 15;
    emission.field1F = 255;
    emission.field1C = 78;
    emission.field1D = 84;
    emission.field0C = 0;
    emission.field14 = 0;
    emission.field18 = 0;
    emission.field1E = 123;
    emission.field20 = 164;
    emission.field21 = 161;
    emission.field22 = 200;
    emission.field23 = 100;
    emission.field24 = 155;
    emission.field25 = 255;
    emission.field26 = 14;
    emission.field28 = 18;
    emission.field2A = 14;
    emission.position = position;
    emission.field44 = 0;
    emission.field46 = -40;
    emission.field48 = 255;
    emission.field4A = 40;
    emission.field54 = sharedScale;
    emission.field58 = sharedScale;
    emission.flags = 0x840E07;
    emission.field60 = 16;
    emission.field61 = -1;
    emission.field62 = 8;
    emission.field63 = 6;
    emission.field64 = 1;
    emission.field4C = 19.0f;
    emission.field50 = 8.0f;
    emission.payloadValue = D_800A016C;
    func_15153634(&emission, 255, owner[0xC], owner[1]);
    return 0;
}


typedef struct { f32 x, y, z; } EffectPositionEC420;
struct ExtendedState15F680;
typedef struct EffectPresetEC420 {
    s32 countBase;
    s32 countRange;
    EffectPositionEC420 position;
    f32 speedBase;
    f32 speedRange;
    f32 verticalBase;
    f32 verticalRange;
    s16 lifetimeBase;
    s16 lifetimeRange;
    f32 sizeBase;
    f32 sizeRange;
    f32 jitter;
    struct ExtendedState15F680 *state;
    f32 chance;
    f32 offsetBase;
    f32 offsetRange;
    f32 aspect;
    s32 *resources;
    f32 *sizes;
    s32 resourceCount;
    f32 radius;
    u8 flags;
    u8 kind;
    u16 padding;
    s32 extraSize;
    void *extraData;
} EffectPresetEC420;
typedef struct { s16 first, firstRange, second, secondRange; } EffectAnglesEC420;
typedef struct { f32 value; } EffectSizeEC420;
extern EffectSizeEC420 D_800A0108;
extern f32 D_800A0170, D_800A0174, D_800A0178, D_800A017C;
extern f32 D_800A0180, D_800A0184, D_800A0188, D_800A018C, D_800A0190;
void func_15150400(EffectPresetEC420 *, EffectAnglesEC420 *, u8, s32);

void func_150C04C0(EffectPositionEC420 *position, struct ExtendedState15F680 *state, s32 variant,
    u8 enabled, u8 channel, s32 context) {
    EffectPresetEC420 preset;
    EffectAnglesEC420 angles;
    s32 localResource;
    EffectSizeEC420 sizes;
    f32 extra;
    s32 flag;

    sizes = D_800A0108;
    extra = D_800A0170;
    localResource = variant;
    preset.countBase = 9;
    preset.countRange = 4;
    preset.position = *position;
    preset.speedBase = 4.0f;
    preset.speedRange = 7.0f;
    preset.verticalBase = D_800A0174;
    preset.verticalRange = D_800A0178;
    preset.lifetimeBase = 80;
    preset.lifetimeRange = 60;
    preset.sizeBase = D_800A017C;
    preset.sizeRange = D_800A0180;
    preset.jitter = D_800A0184;
    preset.state = state;
    preset.chance = D_800A0188;
    preset.offsetBase = D_800A018C;
    preset.offsetRange = D_800A0190;
    preset.aspect = 10.0f;
    preset.resources = &localResource;
    preset.sizes = &sizes.value;
    preset.resourceCount = 1;
    preset.radius = 78.0f;
    if (enabled) {
        flag = 1;
    } else {
        flag = 0;
    }
    preset.flags = flag;
    preset.kind = 14;
    preset.extraSize = 4;
    preset.extraData = &extra;
    angles.first = 0;
    angles.firstRange = 255;
    angles.second = -50;
    angles.secondRange = 35;
    func_15150400(&preset, &angles, channel, context);
}


s32 func_150C0648() {
    return 0;
}
