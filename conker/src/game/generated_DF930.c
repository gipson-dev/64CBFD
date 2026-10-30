#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/DF930.s. */

s32 func_150B2480(s32 arg0, s32 arg1) {
    return 0xA;
}

s32 func_150ADA20(void);
void func_1514C678(f32, f32, f32, f32, s16, s16, s16, u8, s32, f32, void *, u8);
void func_151D5404(f32 *, f32, f32, f32, s32, s32, s32, s32);
void func_151D3FF4(f32 *, u8, s32);

/* Capture the actor position before dispatching the three effects. */
/* Retain both unused words required by the callback table interface. */
void func_150B2494(u8 *actor, s32 unused1, s32 unused2) {
    f32 position[3];

    position[0] = *(f32 *)(actor + 0x14);
    position[1] = *(f32 *)(actor + 0x180);
    position[2] = *(f32 *)(actor + 0x1C);
    func_1514C678(position[0], position[1], position[2], 135.0f,
                 0, 255, (u32)func_150ADA20() % 15 + 27, 7, 0, 0.0f, 0, 255);
    func_151D5404(position, 1502.0f, 3000.0f, 0.00033333333f, 12, 15, 255, 0);
    func_151D3FF4(position, 255, 0);
}

s32 func_150B2570() {
    return 0;
}
