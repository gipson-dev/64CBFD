#include <ultra64.h>

/* Camera-condition callback for the script-selected view. */

#include "structs.h"
extern f32 D_800A00B0, D_800A00B4;
extern u8 D_800CC335;
s32 func_1509BE40(s32, ...);
void func_1509BFB0(s32, s32, s32, ...);
void func_1512868C(struct108 *);
s32 func_15123934(struct108 *, s32, s32, s32, s32);
void func_151254F4(struct108 *, s32);
void func_15123070(struct108 *);
s32 func_151239CC(struct108 *, s32);

/* Update camera state from the current script conditions. */
void func_150BE850(s32 cameraAddress) {
    s32 value;
    s32 condition;
    f32 width;
    f32 height;
    condition = func_1509BE40(0, 0x2006, 0xB7);
    condition = func_1509BE40(0, condition | 0x2000, 0xBC);
    value = func_1509BE40(0, 0x2000, 0xBB);
    if (condition != 0 && value != -1) {
        func_1509BFB0(0, 0x400E, 1);
        if (*(s32 *)((u8 *)(struct108 *)cameraAddress + 0x2C) != 8) {
            func_1512868C((struct108 *)cameraAddress);
        }
        if (func_15123934((struct108 *)cameraAddress, 8, 0, *(s32 *)((u8 *)(struct108 *)cameraAddress + 0x134), 3)) {
            func_151254F4((struct108 *)cameraAddress, D_800CC335 - 1);
            *(u32 *)((u8 *)(struct108 *)cameraAddress + 0x84) |= 0x1000200;
            *(s16 *)((u8 *)(struct108 *)cameraAddress + 0x73C) = 0;
            *(u32 *)((u8 *)(struct108 *)cameraAddress + 0x84) &= ~4;
            *(f32 *)((u8 *)(struct108 *)cameraAddress + 0x674) = 0.0f;
        }
        width = D_800A00B0;
        height = D_800A00B4;
        *(f32 *)((u8 *)(struct108 *)cameraAddress + 0x348) = width;
        *(f32 *)((u8 *)(struct108 *)cameraAddress + 0x34C) = width;
        *(f32 *)((u8 *)(struct108 *)cameraAddress + 0x374) = height;
        *(f32 *)((u8 *)(struct108 *)cameraAddress + 0x190) = 0.0f;
        func_15123070((struct108 *)cameraAddress);
    } else if (func_151239CC((struct108 *)cameraAddress, 3)) {
        func_151254F4((struct108 *)cameraAddress, 0);
        *(f32 *)((u8 *)(struct108 *)cameraAddress + 0x674) = 0.0f;
        func_1509BFB0(0, 0x400E, 0);
    }
}
