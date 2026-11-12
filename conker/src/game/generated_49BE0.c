#include <ultra64.h>
#include "structs.h"
extern u16 D_800D2132;
extern struct127 D_800CC2D0[26];
extern u8 D_800BE615, D_800BE616, D_800DD2C0;
extern u16 *D_800BE9F4;
extern s32 D_800BEA00[], D_800BEA04[];
void func_1501C53C(void);
void func_15016680(void);
/* Dispatch a scene transition using the original seven-entry table. */
void func_1501C730(s32 command, s32 scene, s32 channel, s32 arg3, s32 arg4) {
    func_1501C53C();
    D_800D2132 = 0;
    switch (command) {
        case 0:
            /* Retains the retail switch range; IDO folds this repeated store. */
            D_800D2132 = 0;
            break;
        case 4:
        case 6:
            D_800BEA00[0] = arg4;
            D_800BEA04[0] = arg3;
            D_800BE9F4 = (u16 *)scene;
            D_800DD2C0 = channel;
            D_800BE615 = 2;
            break;
        case 1:
            D_800BE615 = 3;
            D_800BE9F4 = (u16 *)scene;
            D_800D2132 = D_800CC2D0[0].unkB2;
            break;
        case 2:
            D_800BE615 = 3;
            D_800BE9F4 = (u16 *)scene;
            D_800DD2C0 = channel;
            D_800D2132 = D_800CC2D0[0].unkB2;
            break;
        case 3:
            if (D_800BE616 == 0) {
                D_800BE615 = 4;
                func_15016680();
            }
            break;
        case 5:
            D_800BE9F4 = (u16 *)5;
            D_800BE615 = 1;
            break;
    }
}
