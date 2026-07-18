#include <ultra64.h>
#include "controller.h"

#ifdef osContStartReadData
#undef osContStartReadData
#endif
#ifdef osContGetReadData
#undef osContGetReadData
#endif
#ifdef __osPackReadData
#undef __osPackReadData
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/contreaddata.s. */

s32 osContStartReadData(OSMesgQueue *arg0) {
    return 0;
}

void osContGetReadData(OSContPad *arg0) {
}

s32 __osPackReadData() {
    return 0;
}
