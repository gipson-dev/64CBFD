#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/B21B0.s. */

typedef struct {
    u8 pad[0x11B];
    u8 value;
} GeneratedB21B0Target;

typedef struct {
    u8 pad[0x31C];
    GeneratedB21B0Target *target;
} GeneratedB21B0Owner;

s32 func_15084D00() {
    return 0;
}

s32 func_15084D70() {
    return 0;
}

void func_15085410(GeneratedB21B0Owner *arg0, s32 arg1) {
    arg0->target->value = arg1;
}

u8 func_15085420(GeneratedB21B0Owner *arg0) {
    return arg0->target->value;
}

s32 func_15085430() {
    return 0;
}

s32 func_15085710() {
    return 0;
}

s32 func_150859AC() {
    return 0;
}

s32 func_15085ABC() {
    return 0;
}
