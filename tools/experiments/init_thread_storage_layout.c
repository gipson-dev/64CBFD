#include <PR/os_thread.h>
#include <stddef.h>

const unsigned int init_thread_storage_layout[] = {
    sizeof(OSThread),
    offsetof(OSThread, context),
    offsetof(OSThread, context.fp0),
    offsetof(OSThread, context.fp30)
};
