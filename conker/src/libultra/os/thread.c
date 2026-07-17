#include <os_internal.h>

void __osDequeueThread(OSThread **queue, OSThread *thread) {
    OSThread *pred;
    OSThread *succ;

    pred = (OSThread *)queue;
    succ = pred->next;
    while (succ != 0) {
        if (succ == thread) {
            pred->next = thread->next;
            return;
        }
        pred = succ;
        succ = pred->next;
    }
}
