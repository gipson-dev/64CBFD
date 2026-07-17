#include <os_internal.h>

extern void *D_8002BDE0;

s32 osPiGetDeviceType(void) {
    return (s32)D_8002BDE0;
}
