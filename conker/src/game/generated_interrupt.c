#include <ultra64.h>
#include "controller.h"

#ifdef __osDisableInt
#undef __osDisableInt
#endif
#ifdef __osRestoreInt
#undef __osRestoreInt
#endif

/* Original handwritten CP0 interrupt-mask wrappers. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_interrupt/__osDisableInt.s")
#pragma GLOBAL_ASM("asm/nonmatchings/generated_interrupt/__osRestoreInt.s")
