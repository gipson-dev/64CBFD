#include <ultra64.h>
#include "controller.h"

#ifdef __osContRamWrite
#undef __osContRamWrite
#endif
#ifdef __osPackRamWriteData
#undef __osPackRamWriteData
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/contramwrite.s. */

s32 __osContRamWrite(OSMesgQueue *mq, int channel, u16 address, u8 *buffer, int force) {
    return 0;
}

s32 __osPackRamWriteData() {
    return 0;
}
