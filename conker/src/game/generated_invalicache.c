#include <ultra64.h>

#ifdef osInvalICache
#undef osInvalICache
#endif

/* Original handwritten primary instruction-cache invalidation routine. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_invalicache/osInvalICache.s")
