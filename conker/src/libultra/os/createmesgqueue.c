#include <os_internal.h>

extern OSThread D_8002BDF0;

void osCreateMesgQueue(OSMesgQueue *mq, OSMesg *msg, s32 msgCount) {
    mq->mtqueue = &D_8002BDF0;
    mq->fullqueue = &D_8002BDF0;
    mq->validCount = 0;
    mq->first = 0;
    mq->msgCount = msgCount;
    mq->msg = msg;
}
