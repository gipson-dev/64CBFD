#include <ultra64.h>
#include "controller.h"

#ifdef osMapTLB
#undef osMapTLB
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/os/maptlb.s. */

#if 0
void osMapTLB(s32 arg0, OSPageMask arg1, void *arg2, u32 arg3, u32 arg4, s32 arg5) {
}
#endif
#pragma GLOBAL_ASM("asm/nonmatchings/generated_maptlb/osMapTLB.s")
