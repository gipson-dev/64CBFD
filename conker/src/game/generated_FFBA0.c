#include <ultra64.h>
#include "structs.h"

extern f32 D_800BE9A4;
f32 func_15144B68(f32);
f32 sinf(f32);
typedef struct {
    f32 x;
    f32 y;
    f32 baseX;
    f32 baseY;
    f32 amplitudeX;
    f32 amplitudeY;
    f32 phaseX;
    f32 phaseY;
    f32 speedX;
    f32 speedY;
    f32 timer;
    f32 opacityRate;
} OscillationFFBA0;
typedef struct {
    u8 pad00[0x5C];
    u8 opacity;
    u8 pad5D[0xB3];
    OscillationFFBA0 motion;
} OscillatingRecordFFBA0;


typedef struct ReloadRecord {
    u32 command;
    u32 base;
    u32 range;
    u32 timer;
    u8 parameters[1];
} ReloadRecord;

extern s32 D_800BE9E4;
void func_150D278C(u32, const void *, u8, s32);
s32 func_150ADA20(void);

/* Non-matching placeholders for the text-only asm slice asm/FFBA0.s. */

void func_150D26F0(u8 *object) {
    ReloadRecord *record = (ReloadRecord *) (object + 0x28);

    if (object[0x78] & 1) {
        record->timer -= (u32) D_800BE9E4;
        if ((s32) record->timer < 0) {
            func_150D278C(record->command, record->parameters, object[0xC], object[1]);
            record->timer = (u32) func_150ADA20() % (record->range + 1) + record->base;
        }
    }
}

typedef struct { u8 rgb[3][3]; } EffectPalette150D278C;
typedef struct {
    u32 command;
    f32 randomPhase, rate, inverseRate, signedSpeed;
    f32 zero14, zero18;
    u8 parameters[64];
    u8 colour[3];
    u8 retained5F;
} RandomEffectPayload150D278C;
extern EffectPalette150D278C D_800A0990;
extern f32 D_800A099C, D_800A09A0, D_800A09A4, D_800A09A8, D_800A09AC;
f32 func_150ADA68(void);
void *memcpy(void *, const void *, u32);
struct260 *func_15149130(s16, s8, s8, s8, u8, u8, struct37 *, u8, s32);

/* Build randomized motion and palette data, retaining the original unwritten tail byte. */
void func_150D278C(u32 command, const void *parameters, u8 priority, s32 context) {
    RandomEffectPayload150D278C packet;
    struct260 *created;
    s16 lifetime;

    packet.command = command;
    packet.randomPhase = func_150ADA68();
    packet.randomPhase = (packet.randomPhase + packet.randomPhase) * D_800A099C;
    packet.rate = func_150ADA68() * D_800A09A0 + D_800A09A4;
    packet.inverseRate = 1.0f / packet.rate;
    packet.signedSpeed = func_150ADA68() * D_800A09A8 + D_800A09AC;
    if ((u32)func_150ADA20() & 1) {
        packet.signedSpeed = -packet.signedSpeed;
    }
    packet.zero14 = 0.0f;
    packet.zero18 = 0.0f;
    memcpy(packet.parameters, parameters, 0x40);
    {
        EffectPalette150D278C palette;
        u8 colour;
        palette = D_800A0990;
        colour = (u8)((u32)func_150ADA20() % 3);
        packet.colour[0] = palette.rgb[colour][0];
        packet.colour[1] = palette.rgb[colour][1];
        packet.colour[2] = palette.rgb[colour][2];
    }
    lifetime = (s16)((u32)func_150ADA20() % 101 + 100);
    created = func_15149130(lifetime,
                           -1, 50, -1, 1, 0, (struct37 *)0x60, (u8)priority, context);
    if (created != NULL) {
        memcpy((u8 *)created + 0x28, &packet, 0x60);
    }
}

s32 func_150D2924() {
    return 0;
}

s32 func_150D2D6C() {
    return 0;
}

/* Update the record oscillation and report whether its timer remains positive. */
s32 func_150D317C(OscillatingRecordFFBA0 *record) {
    OscillationFFBA0 *motion;

    record->motion.phaseX += record->motion.speedX * D_800BE9A4;
    record->motion.phaseY += record->motion.speedY * D_800BE9A4;
    motion = &record->motion;
    motion->phaseX = func_15144B68(motion->phaseX);
    motion->phaseY = func_15144B68(motion->phaseY);
    motion->x = sinf(motion->phaseX) * motion->amplitudeX + motion->baseX;
    motion->y = sinf(motion->phaseY) * motion->amplitudeY + motion->baseY;
    motion->timer -= D_800BE9A4;
    record->opacity = (u32)(motion->opacityRate * motion->timer);
    if (motion->timer > 0.0f) return 1;
    return 0;
}

void func_150D32FC(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *record = arg0 + 0x28;

    if (arg2 == 0x34 && *arg1 == record[0x51]) {
        func_150D278C(*(s32 *) record, record + 0x10, arg0[0xC], arg0[1]);
    }
}
