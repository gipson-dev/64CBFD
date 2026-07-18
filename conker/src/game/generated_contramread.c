#include <ultra64.h>
#include "controller.h"

#ifdef __osContRamRead
#undef __osContRamRead
#endif
#ifdef __osPackRamReadData
#undef __osPackRamReadData
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/contramread.s. */

s32 __osContRamRead(OSMesgQueue *mq, int channel, u16 address, u8 *buffer) {
    return 0;
}

s32 __osPackRamReadData() {
    return 0;
}
