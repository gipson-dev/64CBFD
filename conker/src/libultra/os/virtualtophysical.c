#include <os_internal.h>
#include <R4300.h>

u32 osVirtualToPhysical(void *addr) {
    u32 value;

    value = (u32)addr;
    if ((value >= 0x80000000) && (value < 0xA0000000)) {
        return value & 0x1FFFFFFF;
    }

    if ((value >= 0xA0000000) && (value < 0xC0000000)) {
        return value & 0x1FFFFFFF;
    }

    return __osProbeTLB(addr);
}
