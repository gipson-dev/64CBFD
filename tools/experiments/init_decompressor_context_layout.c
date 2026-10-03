#include <ultra64.h>
#include <stddef.h>

typedef struct {
    char pad;
    OSThread thread;
} InitContextAlignment;

/* Retail FR=1 stores 32 FPRs instead of the SDK header's 16 paired slots. */
typedef struct {
    unsigned char prefix[offsetof(OSThread, context.fp0)];
    u64 fpr[32];
} InitRetailThreadStorage;

const unsigned int init_decode_context_layout[] = {
    sizeof(void *),
    sizeof(long),
    sizeof(__OSThreadContext),
    sizeof(OSThread),
    offsetof(OSThread, context),
    offsetof(OSThread, context.sp),
    offsetof(OSThread, context.fp0),
    offsetof(InitContextAlignment, thread),
    sizeof(InitRetailThreadStorage),
    offsetof(InitRetailThreadStorage, fpr)
};
