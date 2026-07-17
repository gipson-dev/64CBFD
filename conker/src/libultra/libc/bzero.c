#include "PR/ultratypes.h"
#include "string.h"

void bzero(void *dst, size_t size) {
    u8 *d;

    d = dst;
    while (size > 0) {
        *d++ = 0;
        size--;
    }
}
