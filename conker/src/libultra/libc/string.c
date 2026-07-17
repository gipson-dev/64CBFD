#include "PR/ultratypes.h"
#include "string.h"

void *memcpy(void *dst, const void *src, size_t size) {
    u8 *d = dst;
    const u8 *s = src;

    while (size > 0) {
        *d++ = *s++;
        size--;
    }
    return dst;
}

size_t strlen(const char *str) {
    const char *end = str;

    while (*end != 0) {
        end++;
    }
    return end - str;
}

char *strchr(const char *str, s32 ch) {
    u8 c = ch;

    do {
        if (*str == c) {
            return (char *)str;
        }
    } while (*str++ != 0);

    return 0;
}
