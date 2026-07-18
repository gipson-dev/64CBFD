#include <ultra64.h>
#include "controller.h"

#ifdef __osContRamWrite2
#undef __osContRamWrite2
#endif
#ifdef __osPackRamWriteData2
#undef __osPackRamWriteData2
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/contramwrite2.s. */

s32 __osContRamWrite2() {
    return 0;
}

s32 __osPackRamWriteData2() {
    return 0;
}
