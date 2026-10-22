#include <ultra64.h>
#include "structs.h"
typedef void (*FrameLayerCallback)(s32);
extern FrameLayerCallback D_8008CD04[];
extern s32 D_800B0E00[2];
extern u8 D_800BE616;
extern u16 D_800CBD4E;
void func_15165F70(void);
void func_15195FF0(s32, s32);
void func_1510C8A8(void);
void func_1517DE5C(void);
void func_151880C0(void);


extern struct104 *D_800B0DF0;
extern Mtx D_80089470;
typedef Gfx *(*MatrixWrapperCallback)(Gfx *, s32);
extern MatrixWrapperCallback D_8008CD74[], D_8008CD7C[];


/* Non-matching placeholders for the text-only asm slice asm/1A1E50.s. */

extern s32 D_800BE9E4;
extern u8 D_800DD405;
extern u8 D_800DD406;

void func_151749A0(s32 timerLimit, s32 counterLimit) {
    D_800DD406 += D_800BE9E4;
    if (timerLimit < D_800DD406) {
        D_800DD405++;
        if (D_800DD405 >= counterLimit) {
            D_800DD405 = 0;
        }
        D_800DD406 = 0;
    }
}

/* Run frame-layer callbacks and advance the wrapping phase accumulator. */
void func_151749F8(s32 unused, s32 view) {
    func_15165F70();
    func_15195FF0(D_800B0E00[0], D_800B0E00[1]);
    func_1510C8A8();
    if (((u8 *)D_800B0DF0)[0xB] != 0) {
        D_8008CD04[((u8 *)D_800B0DF0)[0xB]](view);
    }
    if (D_800BE616 == 0) {
        func_1517DE5C();
        func_151880C0();
    }
    D_800CBD4E += (u32)D_800BE9E4 << 6;
}

/* Wrap the selected layer in pipe synchronization and model-view loads. */
Gfx *func_15174AA4(Gfx *commands, s32 unused, s32 view) {
    gDPPipeSync(commands++);
    gSPMatrix(commands++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    if (((u8 *)D_800B0DF0)[0xC] != 0) {
        commands = D_8008CD74[((u8 *)D_800B0DF0)[0xC]](commands, view);
    }
    gSPMatrix(commands++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    return commands;
}

/* Wrap the selected layer in pipe synchronization and model-view loads. */
Gfx *func_15174B48(Gfx *commands, s32 unused, s32 view) {
    gDPPipeSync(commands++);
    gSPMatrix(commands++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    if (((u8 *)D_800B0DF0)[0xD] != 0) {
        commands = D_8008CD7C[((u8 *)D_800B0DF0)[0xD]](commands, view);
    }
    gSPMatrix(commands++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    return commands;
}
