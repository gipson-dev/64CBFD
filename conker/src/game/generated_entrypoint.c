#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/entrypoint.s. */

// Handwritten startup clear-and-jump routine. It deliberately uses addi and
// installs the stack immediately before its indirect jump into initialization.
#if 0
s32 func_10001000() {
    return 0;
}
#endif
#pragma GLOBAL_ASM("asm/nonmatchings/generated_entrypoint/func_10001000.s")
