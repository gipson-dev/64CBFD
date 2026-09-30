#include "PR/ultratypes.h"
#include "string.h"

#if 0
void bzero(void *dst, size_t size) {
    u8 *d;

    d = dst;
    while (size > 0) {
        *d++ = 0;
        size--;
    }
}
#endif
#pragma GLOBAL_ASM("asm/nonmatchings/libultra/libc/bzero/bzero.s")
