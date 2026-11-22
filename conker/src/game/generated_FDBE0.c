#include <ultra64.h>

/* Recovered routine from the text-only asm slice asm/FDBE0.s. */

typedef struct { s16 x,y,z; u8 rest[0x2E]; } AmbientSoundRecord;
extern AmbientSoundRecord *D_800D3098;
extern u8 D_800D98F0;
extern s32 D_800BE9E4;
void func_151827D0(void);
s32 func_150A29C8(u32,u32);
u32 func_150ADA20(void);
u16 func_10010F88(s32,u16,s16,u8,s32,s16,s16,s16,s16,s16);

/* Update the cooldown and play a sound at the first available record. */
void func_150D0730(s32 unused) {
    s32 selected=0;
    u32 soundId;
    func_151827D0();
    if (D_800D98F0 != 0) {
        if (D_800BE9E4 < D_800D98F0) {
            D_800D98F0 -= (u32)D_800BE9E4;
        } else {
            D_800D98F0=0;
        }
    } else {
        if (!func_150A29C8(0,0x15)) selected=0x15;
        else if (!func_150A29C8(0,0x1A)) selected=0x1A;
        else if (!func_150A29C8(0,0x1B)) selected=0x1B;
        else if (!func_150A29C8(0,0x1C)) selected=0x1C;
        else if (!func_150A29C8(0,0x1D)) selected=0x1D;
        else if (!func_150A29C8(0,0x20)) selected=0x20;
        if (selected != 0) {
            D_800D98F0=(func_150ADA20()&127)+128;
            soundId=func_150ADA20()%3+108;
            func_10010F88(soundId,24000,0,0,0,
                         D_800D3098[selected].x,D_800D3098[selected].y,
                         D_800D3098[selected].z,800,1500);
        }
    }
}
