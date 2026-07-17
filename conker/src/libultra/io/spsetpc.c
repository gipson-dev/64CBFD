#include <os_internal.h>
#include <rcp.h>

s32 __osSpSetPc(u32 pc) {
    u32 status;

    status = IO_READ(SP_STATUS_REG);
    if (!(status & SP_STATUS_HALT)) {
        return -1;
    }
    IO_WRITE(SP_PC_REG, pc);
    return 0;
}
