#include <ultra64.h>
extern OSMesgQueue *D_800E0A20;
extern u8 D_800E0A24;
extern u8 *D_800E0A28;
extern s32 D_800E0A2C;
extern u64 D_8002BD10;
extern OSTimer D_80042A58;
extern OSMesg D_80042A90;
extern OSMesgQueue __osEepromTimerQ;
/* Signed mode argument is qualified against retail; poller remains pending. */
s32 func_151DCFD8();


/* Non-matching placeholders for the text-only asm slice asm/20A3A0.s. */

/* Drain pending EEPROM work, publish the request, then arm its timer. */
s32 func_151DCEF0(OSMesgQueue *queue, s32 address, void *buffer, s32 length) {
    while (func_151DCFD8(1) != 0) {
    }
    D_800E0A20 = queue;
    D_800E0A24 = (u8)address;
    D_800E0A28 = buffer;
    D_800E0A2C = length;
    return osSetTimer(&D_80042A58, (12000ULL * D_8002BD10) / 1000000ULL,
               0, &__osEepromTimerQ, &D_80042A90);
}

s32 func_151DCFD8() {
    return 0;
}
