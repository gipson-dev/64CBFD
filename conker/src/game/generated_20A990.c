#include <ultra64.h>
#include "controller.h"

extern OSPifRam D_800E0A30;
void __osSiGetAccess(void);
void __osSiRelAccess(void);
s32 __osSiRawStartDma(s32, void *);
void func_151DD65C(u8, u8 *);
s32 func_151DD710(OSMesgQueue *, OSContStatus *);

s32 func_151DD4E0(OSMesgQueue *mq, u8 address, u8 *buffer) {
    s32 ret = 0;
    u16 type;
    u8 *ptr = (u8 *)&D_800E0A30.ramarray;
    __OSContEepromFormat eepromformat;
    OSContStatus sdata;
    u8 temp[4];

    __osSiGetAccess();
    ret = func_151DD710(mq, &sdata);
    type = sdata.type & (CONT_EEPROM | CONT_EEP16K);

    if (ret == 0) {
        switch (type) {
        case CONT_EEPROM:
            if (address >= EEPROM_MAXBLOCKS) {
                ret = -1;
            }
            break;
        case CONT_EEPROM | CONT_EEP16K:
            if (address >= EEP16K_MAXBLOCKS) {
                ret = -1;
            }
            break;
        default:
            ret = CONT_NO_RESPONSE_ERROR;
        }
    }

    if (ret != 0) {
        __osSiRelAccess();
        return ret;
    }

    while (sdata.status & CONT_EEPROM_BUSY) {
        func_151DD710(mq, &sdata);
    }

    func_151DD65C(address, buffer);
    ret = __osSiRawStartDma(OS_WRITE, &D_800E0A30);
    osRecvMesg(mq, NULL, OS_MESG_BLOCK);
    ret = __osSiRawStartDma(OS_READ, &D_800E0A30);
    __osContLastCmd = CONT_CMD_WRITE_EEPROM;
    osRecvMesg(mq, NULL, OS_MESG_BLOCK);
    ptr += MAXCONTROLLERS;
    eepromformat = *(__OSContEepromFormat *)ptr;
    ret = CHNL_ERR(eepromformat);

    __osSiRelAccess();
    return ret;
}

void func_151DD65C(u8 address, u8 *buffer) {
    u8 *ptr = (u8 *)&D_800E0A30.ramarray;
    __OSContEepromFormat eepromformat;
    s32 i;

    D_800E0A30.pifstatus = CONT_CMD_EXE;

    eepromformat.txsize = CONT_CMD_WRITE_EEPROM_TX;
    eepromformat.rxsize = CONT_CMD_WRITE_EEPROM_RX;
    eepromformat.cmd = CONT_CMD_WRITE_EEPROM;
    eepromformat.address = address;

    for (i = 0; i < ARRLEN(eepromformat.data); i++) {
        eepromformat.data[i] = *buffer++;
    }

    for (i = 0; i < MAXCONTROLLERS; i++) {
        *ptr++ = 0;
    }

    *(__OSContEepromFormat *)ptr = eepromformat;
    ptr += sizeof(__OSContEepromFormat);
    ptr[0] = CONT_CMD_END;
}

s32 func_151DD710(OSMesgQueue *mq, OSContStatus *data) {
    s32 ret = 0;
    s32 i;
    u8 *ptr = (u8 *)D_800E0A30.ramarray;
    __OSContRequesFormat requestformat;

    for (i = 0; i < ARRLEN(D_800E0A30.ramarray) + 1; i++) {
        D_800E0A30.ramarray[i] = 0;
    }

    D_800E0A30.pifstatus = CONT_CMD_EXE;
    ptr = (u8 *)D_800E0A30.ramarray;

    for (i = 0; i < MAXCONTROLLERS; i++) {
        *ptr++ = CONT_CMD_REQUEST_STATUS;
    }

    requestformat.dummy = CONT_CMD_NOP;
    requestformat.txsize = CONT_CMD_REQUEST_STATUS_TX;
    requestformat.rxsize = CONT_CMD_REQUEST_STATUS_RX;
    requestformat.cmd = CONT_CMD_REQUEST_STATUS;
    requestformat.typeh = CONT_CMD_NOP;
    requestformat.typel = CONT_CMD_NOP;
    requestformat.status = CONT_CMD_NOP;
    requestformat.dummy1 = CONT_CMD_NOP;
    *(__OSContRequesFormat *)ptr = requestformat;
    ptr += sizeof(__OSContRequesFormat);
    *ptr = CONT_CMD_END;

    ret = __osSiRawStartDma(OS_WRITE, &D_800E0A30);
    osRecvMesg(mq, NULL, OS_MESG_BLOCK);
    __osContLastCmd = CONT_CMD_END;
    if (ret != 0) {
        return ret;
    }

    ret = __osSiRawStartDma(OS_READ, &D_800E0A30);
    osRecvMesg(mq, NULL, OS_MESG_BLOCK);
    if (ret != 0) {
        return ret;
    }

    ptr = (u8 *)&D_800E0A30;

    for (i = 0; i < MAXCONTROLLERS; i++) {
        *ptr++ = 0;
    }

    requestformat = *(__OSContRequesFormat *)ptr;
    data->errno = CHNL_ERR(requestformat);
    data->type = (requestformat.typel << 8) | requestformat.typeh;
    data->status = requestformat.status;
    return data->errno;
}

s32 func_151DD8C0() {
    return 0;
}
