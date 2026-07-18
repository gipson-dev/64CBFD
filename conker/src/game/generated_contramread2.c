#include <ultra64.h>
#include "controller.h"

#ifdef __osContRamRead2
#undef __osContRamRead2
#endif
#ifdef __osPackRamReadData2
#undef __osPackRamReadData2
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/contramread2.s. */

s32 __osContRamRead2() {
    return 0;
}

s32 __osPackRamReadData2() {
    return 0;
}
