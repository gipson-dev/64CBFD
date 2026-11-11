#include <ultra64.h>

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
s32 func_150D278C();
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

s32 func_150D278C() {
    return 0;
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
