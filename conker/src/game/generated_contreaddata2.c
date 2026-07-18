#include <ultra64.h>
#include "controller.h"

#ifdef osContStartReadData2
#undef osContStartReadData2
#endif
#ifdef osContGetReadData2
#undef osContGetReadData2
#endif
#ifdef __osPackReadData2
#undef __osPackReadData2
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/contreaddata2.s. */

s32 osContStartReadData2() {
    return 0;
}

s32 osContGetReadData2() {
    return 0;
}

s32 __osPackReadData2() {
    return 0;
}
