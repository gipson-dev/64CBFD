#include <os_internal.h>
#include <rcp.h>

s32 __osSiDeviceBusy(void);

s32 __osSiRawStartDma(s32 direction, void *dramAddr) {
    if (__osSiDeviceBusy()) {
        return -1;
    }

    if (direction == OS_WRITE) {
        osWritebackDCache(dramAddr, 0x40);
    }

    IO_WRITE(SI_DRAM_ADDR_REG, osVirtualToPhysical(dramAddr));

    if (direction == OS_READ) {
        IO_WRITE(SI_PIF_ADDR_RD64B_REG, PIF_RAM_START);
    } else {
        IO_WRITE(SI_PIF_ADDR_WR64B_REG, PIF_RAM_START);
    }

    if (direction == OS_READ) {
        osInvalDCache(dramAddr, 0x40);
    }

    return 0;
}
