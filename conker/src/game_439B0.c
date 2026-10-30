#include <ultra64.h>
extern u8 D_800BE580[];
extern u8 D_800BEAAB;
u32 func_1502B020(u32 *, u32, ...);


#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_15016588(void);
/* End generated placeholder declarations. */

void func_15016500(void) {
    D_800D1940 = (u8)0;
    D_800D1941 = (u8)0;
    D_800D1944 = 0;
    D_800D1948 = 0;
    D_800D194C = 0;
    D_800D1950 = 0;
    bzero(D_800D1958, 48); // bzero
    D_800D1988 = 0.0f;
    D_800D198C = 0.0f;
    D_800D1990 = 0.0f;
    D_800D1994 = (u8)0;
    D_800D1995 = (u8)0;
    D_800D1998 = 0;
}

/* Rebuild the resource-presence bits using each query's returned size. */
void func_15016588(void) {
    s32 index;
    s32 byteIndex;
    s32 mask;
    u32 size;

    bzero(D_800BE580, 8);
    byteIndex = -1;
    index = 0;
    do {
        if ((index & 7) == 0) {
            mask = 1;
            byteIndex++;
        } else {
            mask <<= 1;
        }
        func_1502B020(&size, 3, 0x1A, D_800BEAAB, index);
        index++;
        if (size != 0) {
            D_800BE580[byteIndex] |= mask;
        }
    } while (index != 67);
}
