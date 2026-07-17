#include <os_internal.h>
#include <rcp.h>

s32 __osSiDeviceBusy(void);

s32 __osSpRawWriteIo(u32 devAddr, u32 data) {
    if (__osSiDeviceBusy()) {
        return -1;
    }
    IO_WRITE(devAddr, data);
    return 0;
}
