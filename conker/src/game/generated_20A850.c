#include <ultra64.h>

/* EEPROM block reader recovered from asm/20A850.s. */

s32 func_151DCFD8(s32);
s32 func_151DD140(OSMesgQueue *, u8, u8 *);

/* Drain pending EEPROM work, then read successive complete eight-byte blocks. */
s32 func_151DD3A0(OSMesgQueue *queue, u8 address, u8 *buffer, s32 remaining) {
    s32 result = 0;

    while (func_151DCFD8(1) != 0) {
    }
    while (remaining > 0) {
        result = func_151DD140(queue, address, buffer);
        if (result != 0) {
            return result;
        }
        remaining -= 8;
        address++;
        buffer += 8;
    }
    return result;
}
