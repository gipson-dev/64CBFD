#include "piint.h"

extern u32 D_80000308;

s32 osPiRawReadIo(u32 devAddr, u32 *data) {
    u32 stat;

    WAIT_ON_IOBUSY(stat);
    *data = IO_READ(D_80000308 | devAddr);
    return 0;
}
