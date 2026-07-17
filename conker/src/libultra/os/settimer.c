#include <os_internal.h>
#include "osint.h"

extern OSTimer *D_8002BD70;

int osSetTimer(OSTimer *t, OSTime countdown, OSTime interval, OSMesgQueue *mq, OSMesg msg) {
    OSTime time;

    t->next = 0;
    t->prev = 0;
    t->interval = interval;
    t->value = (countdown != 0) ? countdown : interval;
    t->mq = mq;
    t->msg = msg;

    time = __osInsertTimer(t);
    if (D_8002BD70->next == t) {
        __osSetTimerIntr(time);
    }

    return 0;
}
