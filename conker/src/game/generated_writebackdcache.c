#include <ultra64.h>

#ifdef osWritebackDCache
#undef osWritebackDCache
#endif

/* Original handwritten primary data-cache writeback routine. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_writebackdcache/osWritebackDCache.s")
