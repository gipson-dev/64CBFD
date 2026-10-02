#include <ultra64.h>
#include "controller.h"
#include "piint.h"
#include "osint.h"

extern OSPiHandle *D_80043B34;
extern OSIntMask D_8002BD1C;
extern s32 D_8002BD20;
extern __OSEventState D_80042910[OS_NUM_EVENTS];
extern OSThread *D_8002BDF8;
extern OSThread *func_10007A24(OSThread **queue);
extern void func_100079D8(OSThread **queue, OSThread *thread);

#ifdef __osLeoInterrupt
#undef __osLeoInterrupt
#endif
#ifdef __osLeoAbnormalResume
#undef __osLeoAbnormalResume
#endif
#ifdef __osLeoResume
#undef __osLeoResume
#endif

void __osLeoResume(void);
void __osLeoAbnormalResume(void);

enum {
    LEO_INTERRUPT_ERROR_BUFFER_MANAGER = 3,
    LEO_INTERRUPT_ERROR_DATA_PHASE = 6,
    LEO_INTERRUPT_ERROR_C1 = 17
};

s32 __osLeoInterrupt(void) {
    u32 stat;
    volatile u32 pi_stat;
    u32 bm_stat;
    __OSTranxInfo *info;
    __OSBlockInfo *blockInfo;

    if (D_8002BD20 == 0) {
        return 0;
    }

    info = &D_80043B34->transferInfo;
    blockInfo = &info->block[info->blockNum];

    pi_stat = IO_READ(PI_STATUS_REG);
    if (pi_stat & PI_STATUS_DMA_BUSY) {
        IO_WRITE(PI_STATUS_REG, PI_STATUS_RESET | PI_STATUS_CLR_INTR);
        pi_stat = IO_READ(PI_STATUS_REG);
        while (pi_stat & PI_STATUS_IO_BUSY) {
            pi_stat = IO_READ(PI_STATUS_REG);
        }

        stat = IO_READ(LEO_STATUS);
        if (stat & LEO_STATUS_MECHANIC_INTERRUPT) {
            pi_stat = IO_READ(PI_STATUS_REG);
            while (pi_stat & PI_STATUS_IO_BUSY) {
                pi_stat = IO_READ(PI_STATUS_REG);
            }
            IO_WRITE(LEO_BM_CTL, info->bmCtlShadow | LEO_BM_CTL_CLR_MECHANIC_INTR);
        }

        blockInfo->errStatus = 0x4B;
        __osLeoAbnormalResume();
        return 1;
    }

    pi_stat = IO_READ(PI_STATUS_REG);
    while (pi_stat & PI_STATUS_IO_BUSY) {
        pi_stat = IO_READ(PI_STATUS_REG);
    }
    stat = IO_READ(LEO_STATUS);
    if (stat & LEO_STATUS_MECHANIC_INTERRUPT) {
        pi_stat = IO_READ(PI_STATUS_REG);
        while (pi_stat & PI_STATUS_IO_BUSY) {
            pi_stat = IO_READ(PI_STATUS_REG);
        }
        IO_WRITE(LEO_BM_CTL, info->bmCtlShadow | LEO_BM_CTL_CLR_MECHANIC_INTR);
        blockInfo->errStatus = LEO_ERROR_GOOD;
        return 0;
    }

    if (stat & LEO_STATUS_BUFFER_MANAGER_ERROR) {
        blockInfo->errStatus = LEO_INTERRUPT_ERROR_BUFFER_MANAGER;
        __osLeoResume();
        IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
        D_8002BD1C |= OS_IM_PI;
        return 1;
    }

    if (info->cmdType == LEO_CMD_TYPE_1) {
        if ((stat & LEO_STATUS_DATA_REQUEST) == 0) {
            if (info->sectorNum + 1 != info->transferMode * 85) {
                blockInfo->errStatus = LEO_INTERRUPT_ERROR_DATA_PHASE;
                __osLeoAbnormalResume();
                return 1;
            }

            IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
            D_8002BD1C |= OS_IM_PI;
            blockInfo->errStatus = LEO_ERROR_GOOD;
            __osLeoResume();
            return 1;
        } else {
            blockInfo->dramAddr = (void *)((u32)blockInfo->dramAddr + blockInfo->sectorSize);
            info->sectorNum++;
            osEPiRawStartDma(D_80043B34, OS_WRITE, LEO_SECTOR_BUFF, blockInfo->dramAddr,
                            blockInfo->sectorSize);
            return 1;
        }
    } else if (info->cmdType == LEO_CMD_TYPE_0) {
        if (info->transferMode == LEO_SECTOR_MODE) {
            if (info->sectorNum > (s32)blockInfo->C1ErrNum + 17) {
                blockInfo->errStatus = LEO_ERROR_GOOD;
                __osLeoAbnormalResume();
                return 1;
            }

            if ((stat & LEO_STATUS_DATA_REQUEST) == 0) {
                blockInfo->errStatus = LEO_INTERRUPT_ERROR_C1;
                __osLeoAbnormalResume();
                return 1;
            }
        } else {
            blockInfo->dramAddr = (void *)((u32)blockInfo->dramAddr + blockInfo->sectorSize);
        }

        bm_stat = IO_READ(LEO_BM_STATUS);
        if (((bm_stat & LEO_BM_STATUS_C1SINGLE) && (bm_stat & LEO_BM_STATUS_C1DOUBLE)) ||
            (bm_stat & LEO_BM_STATUS_MICRO)) {
            if (blockInfo->C1ErrNum > 3) {
                if ((info->transferMode != LEO_SECTOR_MODE) || (info->sectorNum > 0x52)) {
                    blockInfo->errStatus = LEO_INTERRUPT_ERROR_C1;
                    __osLeoAbnormalResume();
                    return 1;
                }
            } else {
                s32 errNum = blockInfo->C1ErrNum;
                blockInfo->C1ErrSector[errNum] = info->sectorNum + 1;
            }
            blockInfo->C1ErrNum++;
        }

        if (stat & LEO_STATUS_C2_TRANSFER) {
            if (info->sectorNum + 1 != 88) {
                blockInfo->errStatus = LEO_INTERRUPT_ERROR_DATA_PHASE;
                __osLeoAbnormalResume();
            }

            if ((info->transferMode == LEO_TRACK_MODE) && (info->blockNum == 0)) {
                info->blockNum = 1;
                info->sectorNum = -1;
                info->block[1].dramAddr =
                    (void *)((u32)info->block[1].dramAddr - info->block[1].sectorSize);
            } else {
                IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
                D_8002BD1C |= OS_IM_PI;
            }

            osEPiRawStartDma(D_80043B34, OS_READ, LEO_C2_BUFF, blockInfo->C2Addr,
                            blockInfo->sectorSize * 4);
            blockInfo->errStatus = LEO_ERROR_GOOD;
            return 1;
        }

        if ((info->sectorNum == -1) && (info->transferMode == LEO_TRACK_MODE) &&
            (info->blockNum == 1)) {
            __OSBlockInfo *bptr = &info->block[0];

            if (bptr->C1ErrNum == 0) {
                if (((u32 *)bptr->C2Addr)[0] | ((u32 *)bptr->C2Addr)[1] |
                    ((u32 *)bptr->C2Addr)[2] | ((u32 *)bptr->C2Addr)[3]) {
                    bptr->errStatus = LEO_INTERRUPT_ERROR_DATA_PHASE;
                    __osLeoAbnormalResume();
                    return 1;
                }
            }

            bptr->errStatus = LEO_ERROR_GOOD;
            __osLeoResume();
        }

        info->sectorNum++;
        if (stat & LEO_STATUS_DATA_REQUEST) {
            if (info->sectorNum > 0x54) {
                blockInfo->errStatus = LEO_INTERRUPT_ERROR_DATA_PHASE;
                __osLeoAbnormalResume();
                return 1;
            }

            osEPiRawStartDma(D_80043B34, OS_READ, LEO_SECTOR_BUFF, blockInfo->dramAddr,
                            blockInfo->sectorSize);
            blockInfo->errStatus = LEO_ERROR_GOOD;
            return 1;
        } else if (info->sectorNum <= 0x54) {
            blockInfo->errStatus = LEO_INTERRUPT_ERROR_DATA_PHASE;
            __osLeoAbnormalResume();
            return 1;
        }

        return 1;
    } else {
        blockInfo->errStatus = 0x4B;
        __osLeoAbnormalResume();
        return 1;
    }
}

void __osLeoAbnormalResume(void) {
    __OSTranxInfo *info = &D_80043B34->transferInfo;
    u32 pi_stat;

    pi_stat = IO_READ(PI_STATUS_REG);
    while (pi_stat & PI_STATUS_IO_BUSY) {
        pi_stat = IO_READ(PI_STATUS_REG);
    }
    IO_WRITE(LEO_BM_CTL, info->bmCtlShadow | LEO_BM_CTL_RESET);
    pi_stat = IO_READ(PI_STATUS_REG);
    while (pi_stat & PI_STATUS_IO_BUSY) {
        pi_stat = IO_READ(PI_STATUS_REG);
    }
    IO_WRITE(LEO_BM_CTL, info->bmCtlShadow);
    __osLeoResume();
    IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
    D_8002BD1C |= OS_IM_PI;
}

void __osLeoResume(void) {
    __OSEventState *es = &D_80042910[OS_EVENT_PI];
    OSMesgQueue *mq = es->messageQueue;
    s32 last;

    if ((mq == NULL) || MQ_IS_FULL(mq)) {
        return;
    }

    last = (mq->first + mq->validCount) % mq->msgCount;
    mq->msg[last] = es->message;
    mq->validCount++;

    if (mq->mtqueue->next != NULL) {
        func_100079D8(&D_8002BDF8, func_10007A24(&mq->mtqueue));
    }
}
