#include <os_internal.h>

void __osDequeueThread(register OSThread **queue, register OSThread *thread) {
    register OSThread *pred;
    register OSThread *succ;

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
