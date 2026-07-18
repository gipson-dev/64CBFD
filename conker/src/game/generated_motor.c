#define osMotorInit osMotorInit_api
#include <ultra64.h>
#include "controller.h"
#include "siint.h"

#undef osMotorInit

#ifdef osMotorStop
#undef osMotorStop
#endif
#ifdef osMotorStart
#undef osMotorStart
#endif

extern OSPifRam D_8003BC30[4];
extern OSPifRam D_8003BD30[4];
extern u8 D_8003BE30[32];
extern u8 D_8003BE50[32];

void osMotorInit(s32 channel, u16 address, u8 *buffer, OSPifRam *mdata);

s32 osMotorStop(OSPfs *pfs) {
    s32 i;
    s32 ret;
    u8 *ptr;
    __OSContRamReadFormat ramreadformat;

    __osSiGetAccess();
    __osContLastCmd = CONT_CMD_WRITE_MEMPACK;
    __osSiRawStartDma(OS_WRITE, &D_8003BC30[pfs->channel]);
    osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);
    __osSiRawStartDma(OS_READ, &__osPfsPifRam);
    osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);

    ptr = (u8 *)&__osPfsPifRam;
    if (pfs->channel != 0) {
        for (i = 0; i < pfs->channel; i++) {
            ptr++;
        }
    }

    ramreadformat = *(__OSContRamReadFormat *)ptr;
    ret = CHNL_ERR(ramreadformat);
    if ((ret == 0) && (ramreadformat.datacrc != 0)) {
        ret = PFS_ERR_CONTRFAIL;
    }
    __osSiRelAccess();
    return ret;
}

s32 osMotorStart(OSPfs *pfs) {
    s32 i;
    s32 ret;
    u8 *ptr;
    __OSContRamReadFormat ramreadformat;

    __osSiGetAccess();
    __osContLastCmd = CONT_CMD_WRITE_MEMPACK;
    __osSiRawStartDma(OS_WRITE, &D_8003BD30[pfs->channel]);
    osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);
    __osSiRawStartDma(OS_READ, &__osPfsPifRam);
    osRecvMesg(pfs->queue, NULL, OS_MESG_BLOCK);

    ptr = (u8 *)&__osPfsPifRam;
    if (pfs->channel != 0) {
        for (i = 0; i < pfs->channel; i++) {
            ptr++;
        }
    }

    ramreadformat = *(__OSContRamReadFormat *)ptr;
    ret = CHNL_ERR(ramreadformat);
    if ((ret == 0) && (ramreadformat.datacrc != 0xEB)) {
        ret = PFS_ERR_CONTRFAIL;
    }
    __osSiRelAccess();
    return ret;
}

s32 _MakeMotorData(OSMesgQueue *mq, OSPfs *pfs, s32 channel) {
    s32 i;
    s32 ret;
    u8 temp[32];

    pfs->queue = mq;
    pfs->channel = channel;
    pfs->status = 0;
    pfs->activebank = 0x80;

    for (i = 0; i < 32; i++) {
        temp[i] = 0x80;
    }

    ret = __osContRamWrite(mq, channel, 0x400, temp, FALSE);
    if (ret == PFS_ERR_NEW_PACK) {
        ret = __osContRamWrite(mq, channel, 0x400, temp, FALSE);
    }
    if (ret != 0) {
        return ret;
    }

    ret = __osContRamRead(mq, channel, 0x400, temp);
    if (ret != 0) {
        return ret;
    }
    if (temp[31] != 0x80) {
        return PFS_ERR_DEVICE;
    }

    for (i = 0; i < 32; i++) {
        D_8003BE50[i] = 1;
        D_8003BE30[i] = 0;
    }

    osMotorInit(channel, 0x600, D_8003BE50, &D_8003BD30[channel]);
    osMotorInit(channel, 0x600, D_8003BE30, &D_8003BC30[channel]);
    return 0;
}

void osMotorInit(s32 channel, u16 address, u8 *buffer, OSPifRam *mdata) {
    u8 *ptr;
    __OSContRamReadFormat ramreadformat;
    s32 i;

    ptr = (u8 *)mdata->ramarray;
    for (i = 0; i < 15; i++) {
        mdata->ramarray[i] = 0;
    }
    mdata->pifstatus = CONT_CMD_EXE;

    ramreadformat.dummy = CONT_CMD_NOP;
    ramreadformat.txsize = CONT_CMD_WRITE_MEMPACK_TX;
    ramreadformat.rxsize = CONT_CMD_WRITE_MEMPACK_RX;
    ramreadformat.cmd = CONT_CMD_WRITE_MEMPACK;
    ramreadformat.address = (address << 5) | __osContAddressCrc(address);
    ramreadformat.datacrc = CONT_CMD_NOP;

    for (i = 0; i < 32; i++) {
        ramreadformat.data[i] = *buffer++;
    }

    if (channel != 0) {
        for (i = 0; i < channel; i++) {
            *ptr++ = 0;
        }
    }

    *(__OSContRamReadFormat *)ptr = ramreadformat;
    ptr += sizeof(__OSContRamReadFormat);
    ptr[0] = CONT_CMD_END;
}
