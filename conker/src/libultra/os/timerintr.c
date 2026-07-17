#include <os_internal.h>
#include "osint.h"

extern OSTimer *D_8002BD70;
extern OSTime D_800429B0;
extern u32 D_800429B8;
extern u32 D_800429BC;
extern u32 D_800429C0;

void __osTimerServicesInit(void) {
    D_800429B0 = 0;
    D_800429B8 = 0;
    D_800429BC = 0;
    D_8002BD70->next = D_8002BD70->prev = D_8002BD70;
    D_8002BD70->interval = D_8002BD70->value = 0;
    D_8002BD70->mq = 0;
    D_8002BD70->msg = 0;
}

void __osTimerInterrupt(void) {
    OSTimer *t;
    u32 count;
    u32 elapsedCycles;

    if (D_8002BD70->next == D_8002BD70) {
        return;
    }

    for (;;) {
        t = D_8002BD70->next;

        if (t == D_8002BD70) {
            __osSetCompare(0);
            D_800429C0 = 0;
            break;
        }

        count = osGetCount();
        elapsedCycles = count - D_800429C0;
        D_800429C0 = count;

        if (elapsedCycles < t->value) {
            t->value -= elapsedCycles;
            __osSetTimerIntr(t->value);
            break;
        }

        t->prev->next = t->next;
        t->next->prev = t->prev;
        t->next = 0;
        t->prev = 0;

        if (t->mq != 0) {
            osSendMesg(t->mq, t->msg, OS_MESG_NOBLOCK);
        }

        if (t->interval != 0) {
            t->value = t->interval;
            __osInsertTimer(t);
        }
    }
}

void __osSetTimerIntr(OSTime tim) {
    OSTime newTime;
    u32 savedMask;

    savedMask = __osDisableInt();
    D_800429C0 = osGetCount();
    newTime = D_800429C0 + tim;
    __osSetCompare(newTime);
    __osRestoreInt(savedMask);
}

OSTime __osInsertTimer(OSTimer *t) {
    OSTimer *timep;
    OSTime tim;
    u32 savedMask;

    savedMask = __osDisableInt();
    timep = D_8002BD70->next;
    tim = t->value;

    while ((timep != D_8002BD70) && (tim > timep->value)) {
        tim -= timep->value;
        timep = timep->next;
    }

    t->value = tim;

    if (timep != D_8002BD70) {
        timep->value -= tim;
    }

    t->next = timep;
    t->prev = timep->prev;
    timep->prev->next = t;
    timep->prev = t;
    __osRestoreInt(savedMask);
    return tim;
}
