#include <ultra64.h>
extern OSMesgQueue *D_800E0A20;
extern u8 D_800E0A24;
extern u8 *D_800E0A28;
extern s32 D_800E0A2C;
extern u64 D_8002BD10;
extern OSTimer D_80042A58;
extern OSMesg D_80042A90;
extern OSMesgQueue __osEepromTimerQ;
/* Poll a pending EEPROM write using the requested receive mode. */
s32 func_151DCFD8(s32);


/* EEPROM request setup and pending-write polling. */

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

s32 func_151DD4E0(OSMesgQueue *, u8, u8 *);

/* Advance one pending EEPROM write after its timer message is received. */
s32 func_151DCFD8(s32 mode) {
    if (D_800E0A20 == NULL) return 0;
    if (osRecvMesg(&__osEepromTimerQ, NULL, mode) != -1) {
        if (D_800E0A2C <= 0) {
            D_800E0A20 = NULL;
            D_800E0A2C = 0;
            return 0;
        }
        if (func_151DD4E0(D_800E0A20, D_800E0A24, D_800E0A28) != 0) {
            D_800E0A20 = NULL;
            D_800E0A2C = 0;
            return 0;
        }
        D_800E0A2C -= 8;
        D_800E0A24++;
        D_800E0A28 += 8;
        osSetTimer(&D_80042A58, (12000ULL * D_8002BD10) / 1000000ULL,
                   0, &__osEepromTimerQ, &D_80042A90);
        return 1;
    }
    return 0;
}
