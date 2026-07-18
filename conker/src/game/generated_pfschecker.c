#include <ultra64.h>
#include "controller.h"

#ifdef osPfsChecker
#undef osPfsChecker
#endif
#ifdef corrupted_init
#undef corrupted_init
#endif
#ifdef corrupted
#undef corrupted
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/pfschecker.s. */

s32 osPfsChecker(OSPfs *arg0) {
    return 0;
}

s32 corrupted_init() {
    return 0;
}

s32 corrupted() {
    return 0;
}
