#include <ultra64.h>
#include "structs.h"
extern f32 D_800AAABC, D_800AAAC0, D_800AAAC4, D_800AAAC8;
extern f32 D_800AAA90[3], D_800AAA9C[3];
f32 func_150ADA68(void);
s32 func_150ADA20(void);
u8 *func_15102B38(u8 *, u8, f32 *, f32 *, f32 *, s16, u8, f32, f32 *, u8, s32, s16, u8, s32);

/* Non-matching placeholders for the text-only asm slice asm/1F2730.s. */

s32 func_151C5280() {
    return 0;
}

/* Submit an effect with randomized scale, type and angular parameters. */
u8 *func_151C5588(u8 *owner, f32 *position, s16 duration, u8 priority, s32 parameter) {
    f32 scale[2];
    s32 random[2];

    scale[1] = (func_150ADA68() * D_800AAABC + 604.0f) * D_800AAAC0;
    scale[0] = (func_150ADA68() * 59.0f + 141.0f) * D_800AAAC4;
    random[0] = func_150ADA20();
    random[1] = func_150ADA20();
    return func_15102B38(owner, 0, D_800AAA90, D_800AAA9C, scale,
                         (random[0] & 3) + 6, 255,
                         func_150ADA68() * 270.0f + D_800AAAC8,
                         position, 255, 0, duration, priority, parameter);
}

s32 func_150ADA20(void);
struct225 *func_151602C0(Header *, Header2 *, s32, s32, s32, s32, u8, u8, s32, u8, s32);

typedef struct {
    s16 countBase;
    s16 countRange;
    void *providerType;
    s16 reserved8;
    s16 secondAngleBase;
    s16 reservedC;
    s16 secondAngleRange;
    f32 radiusBase;
    f32 radiusRange;
    f32 scaleBase;
    f32 scaleRange;
    /* Raw mode/pointer word; its floating load preserves the retail caller. */
    f32 modeWord;
    u8 selectorBase;
    u8 selectorRange;
    s16 durationBase;
    s16 durationRange;
    u8 reserved2A[2];
    f32 timeBase;
    f32 timeRange;
    f32 opaqueChance;
    s32 requestValue;
} DirectionEffectInput;

extern f32 D_800AAAF4;
extern f32 D_800AAAF8;
extern f32 D_800AAAFC;
void func_15154684(DirectionEffectInput *, s32, s32);

/* Submit a randomized effect at the position's truncated integer coordinates. */
void func_151C56A4(f32 *position, u8 kind, s32 mode) {
    Header header;
    Header2 coordinates;

    header.unk0 = 3;
    header.unk1 = -1;
    header.unk2 = (u32)func_150ADA20() % 3U + 3;
    header.unk4 = 0;
    coordinates.unk0 = position[0];
    coordinates.unk4 = position[1];
    coordinates.unk8 = position[2];
    func_151602C0(&header, &coordinates, ((u32)func_150ADA20() & 1) + 6,
                 0xFF, 0xE8, 0xAB, 0xFF, 0, 0, kind, mode);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1F2730/func_151C577C.s")


#pragma GLOBAL_ASM("asm/nonmatchings/generated_1F2730/func_151C5E74.s")


s32 func_151C5F44() {
    return 0;
}

/* Submit one fixed input descriptor to the directional-effect factory. */
void func_151C61A0(void *providerType, s32 requestValue, u8 channel, s32 owner) {
    DirectionEffectInput input;

    input.countBase = 10;
    input.countRange = 4;
    input.providerType = providerType;
    input.reserved8 = 0;
    input.reservedC = 255;
    input.secondAngleBase = -24;
    input.secondAngleRange = 25;
    input.radiusBase = 5.0f;
    input.radiusRange = 7.0f;
    input.scaleBase = D_800AAAF4;
    input.scaleRange = D_800AAAF8;
    input.modeWord = D_800AAAFC;
    input.selectorBase = 190;
    input.selectorRange = 65;
    input.durationBase = 200;
    input.durationRange = 150;
    input.timeBase = 96.0f;
    input.timeRange = 109.0f;
    input.opaqueChance = 1.0f;
    input.requestValue = requestValue;
    func_15154684(&input, channel, owner);
}

s32 func_151C6290(u8 *arg0, u8 arg1, u8 arg2) {
    u8 temp_v0 = *(arg0 + 4);

    if ((temp_v0 == 0x5A) || (temp_v0 == 0x74) || (temp_v0 == 0x7A)) {
        return 0;
    }
    return 1;
}
