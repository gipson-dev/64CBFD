#include <ultra64.h>
#include "structs.h"
extern f32 D_800A0494,D_800A0498,D_800A049C,D_800A04A0,D_800A04A4;
u32 func_150ADA20(void);
f32 func_150ADA68(void);
void *func_151DB5D0(u8,const struct17 *,const struct17 *,f32,f32,f32,f32,s16,u8,s16,s16,u8,u8,s32);


/* Non-matching placeholders for the text-only asm slice asm/F44D0.s. */

s32 func_150C7020() {
    return 0;
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
