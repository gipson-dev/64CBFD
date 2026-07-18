#include <ultra64.h>
#include "controller.h"

#ifdef osCreateViManager
#undef osCreateViManager
#endif
#ifdef viMgrMain
#undef viMgrMain
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/vimgr.s. */

void osCreateViManager(OSPri arg0) {
}

s32 viMgrMain() {
    return 0;
}
