#include <os_internal.h>
#include <rcp.h>

s32 __osSiDeviceBusy(void) {
    u32 status;

    status = IO_READ(SI_STATUS_REG);
    if (status & (SI_STATUS_DMA_BUSY | SI_STATUS_RD_BUSY)) {
        return 1;
    }
    return 0;
}
