#include <os_internal.h>
#include <rcp.h>
#include "../os/osint.h"

extern u8 hdwrBugFlag;
extern u8 D_8002AB40;
extern u8 D_8002AB40_2;

s32 osAiSetNextBuffer(void *bufPtr, u32 size) {
    char *bptr = bufPtr;

    if (hdwrBugFlag != 0) {
        bptr -= 0x2000;
    }

    if ((((u32)bufPtr + size) & 0x3FFF) == 0x2000) {
        D_8002AB40 = 1;
    } else {
        D_8002AB40_2 = 0;
    }

    if (__osAiDeviceBusy()) {
        return -1;
    }

    IO_WRITE(AI_DRAM_ADDR_REG, osVirtualToPhysical(bptr));
    IO_WRITE(AI_LEN_REG, size);
    return 0;
}
