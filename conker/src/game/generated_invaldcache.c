#include <ultra64.h>
#include "controller.h"

#ifdef osInvalDCache
#undef osInvalDCache
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/os/invaldcache.s. */

#if 0
void osInvalDCache(void *arg0, s32 arg1) {
}
#endif
#pragma GLOBAL_ASM("asm/nonmatchings/generated_invaldcache/osInvalDCache.s")
