#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_100046E4(s32 devAddr, void *dramAddr, u32 size);
/* End generated placeholder declarations. */

void func_10004470(void) {
    int i;
    osCreatePiManager(150, &D_800388B0, &D_800380E0, 0xC8);

    for (i = 0; i < 3; i++)
    {
        osCreateMesgQueue(&gMessageQueue[i], &gMessages[i], 1);
    }

    osCreateMesgQueue(&gMessageQueue0, &gMessage0, 300);
    D_8003A570 = 0;
    D_8003A571 = 0;
}

s32 func_10004514(s32 devAddr, void *dramAddr, u32 size, s32 arg3) {
    OSMesgQueue *msgQueue;
    OSIoMesg tmpIoMsg;
    OSIoMesg *ioMsg;
    s32 sp3c;

    sp3c = __osRunningThread->id - 3;
    if ((size < 0xC8U) && (sp3c == 0)) {
        func_1000480C(devAddr, dramAddr, size);
        return;
    }
    if ((sp3c >= 4) || ( sp3c < 0)) {
        sp3c = 0;
    }
    if (arg3 == 0) {
        if (D_8003A571 != 300) { // messages waiting?
            ioMsg = &D_80038950[D_8003A570];
            msgQueue = &gMessageQueue0;
            if (D_8003A570 == 299) { // number of message queues used?
                D_8003A570 = 0;
            } else {
                D_8003A570 += 1U;
            }
            D_8003A571 += 1U;
        } else {
            return;
        }
    } else {
        ioMsg = &tmpIoMsg;
        msgQueue = &gMessageQueue[sp3c];
    }
    osInvalDCache(dramAddr, size);
    osPiStartDma(ioMsg, 0, 0, devAddr, dramAddr, size, msgQueue);

    if (arg3 != 0) {
        osRecvMesg(msgQueue, 0, OS_MESG_BLOCK);
    }
}

void func_10004674(void) {
    int i;
    for (i = 0; i < D_8003A571; i++)
    {
        osRecvMesg(&gMessageQueue0, 0, OS_MESG_BLOCK);
    }

    D_8003A571 = 0;
}

void func_100046E4(s32 devAddr, void *dramAddr, u32 size) {
    OSMesgQueue *mesgQueue;
    struct {
        OSMesg mesg;
        OSIoMesg ioMesg;
    } messages;
    u32 chunkSize;
    u32 sent;
    s32 threadId;

    threadId = __osRunningThread->id - 3;
    if ((threadId >= 4) || (threadId < 0)) {
        threadId = 0;
    }
    sent = 0;
    osInvalDCache(dramAddr, size);
    if (size != 0) {
        mesgQueue = &gMessageQueue[threadId];
        do {
            if ((size - sent) < 0x14000U) {
                chunkSize = size - sent;
            } else {
                chunkSize = 0x14000;
            }
            osPiStartDma(&messages.ioMesg, 0, 0, devAddr, dramAddr, chunkSize, mesgQueue);
            osRecvMesg(mesgQueue, &messages.mesg, OS_MESG_BLOCK);
            sent += chunkSize;
            devAddr += chunkSize;
            dramAddr = (u8 *)dramAddr + chunkSize;
        } while (sent < size);
    }
}

void func_1000480C(s32 devAddr, void *dramAddr, u32 size) {
    u32 word;
    u32 offset;
    u32 copyLimit;
    u16 *halves;

    D_8003A572 = 1;
    size = (size + 1) & ~1;
    while (D_8003A573 != 0) {}
    while ((IO_READ(PI_STATUS_REG) & (PI_STATUS_DMA_BUSY | PI_STATUS_IO_BUSY)) != 0) {}

    devAddr |= D_80000308;
    copyLimit = size - 2;
    offset = 0;
    halves = (u16 *)&word;
    if (devAddr & 2) {
        size -= 2;
        word = IO_READ(devAddr - 2);
        *(u16 *)dramAddr = halves[1];
        copyLimit = size - 2;

        if (copyLimit != 0) {
            do {
                word = IO_READ(devAddr + offset + 2);
                offset += 4;
                *(u16 *)((u8 *)dramAddr + offset - 2) = word >> 16;
                *(u16 *)((u8 *)dramAddr + offset) = word;
            } while (offset < copyLimit);
        }

        if (size & 2) {
            word = IO_READ(devAddr + offset + 2);
            *(u16 *)((u8 *)dramAddr + offset + 2) = halves[0];
        }
    } else {
        if (copyLimit != 0) {
            do {
                *(u32 *)((u8 *)dramAddr + offset) = IO_READ(devAddr + offset);
                offset += 4;
            } while (offset < copyLimit);
        }

        if (size & 2) {
            word = IO_READ(devAddr + offset);
            *(u16 *)((u8 *)dramAddr + offset) = halves[0];
        }
    }

    D_8003A572 = 0;
    if (D_8003A575 != 0) {
        osStartThread((OSThread *)&D_80035910);
    }
}
