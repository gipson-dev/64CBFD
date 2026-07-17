#include "PR/ultratypes.h"
#include "string.h"

void *bcopy(const void *src, void *dst, size_t size) {
    const u8 *s;
    u8 *d;
    void *ret;

    ret = dst;
    s = src;
    d = dst;

    if ((d > s) && (d < s + size)) {
        s += size;
        d += size;
        while (size > 0) {
            *--d = *--s;
            size--;
        }
    } else {
        while (size > 0) {
            *d++ = *s++;
            size--;
        }
    }

    return ret;
}
