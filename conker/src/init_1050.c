#include <ultra64.h>

#include "functions.h"
#include "variables.h"
#include "macros.h"

extern u8 D_151FA130;

void func_10001050(void) {
    bzero(&D_8002D4B0, (s32) &D_80043B40 - (s32) &D_8002D4B0); // zero out bss
    func_100061F8(1, 31);
    osInitialize();
    __osSetSR(__osGetSR() | SR_CU1 | SR_FR);
    __osSetFpcCsr(FPCSR_FS);
    osCreateThread(&D_800318B0, 1, (void*) func_100010F8, 0, &D_8002D8B0, 5);
    osStartThread(&D_800318B0);
}

void func_100010F8(s32 arg0) {
    func_10004470(); // create message queues
    osCreateThread(&D_80031AE0, 3, (void*) func_10001194, (void *) arg0, &D_800318B0, 10);
    if ((D_8002AC5C == 0) && (D_80000310 == 0x17D9)) {
        osStartThread(&D_80031AE0);
    }
    osSetThreadPri(&D_800318B0, NULL);
    do {} while(1);
}

void func_10001194(s32 arg0) {
    u32 blockCount;
    s32 sourceAddress;
    s32 allocation;
    s32 transferSize;
    s32 clearSize;
    s32 offset;
    s32 i;
    s32 *framebuffers;

    func_10005218();
    if (D_8000030C == 0) {
        clearSize = 0x80400000 - (s32)&D_80043B40;
        bzero(&D_80043B40, clearSize);
    } else {
        bzero(&D_800E9D10, 0x80400000 - (s32)&D_800E9D10);
        clearSize = 0x80400000 - (s32)&D_80043B40;
    }

    osInvalICache(&D_80043B40, clearSize);
    osInvalDCache(&D_80043B40, clearSize);
    func_10003920();
    func_10003930();
    func_10003BD0();
    func_1000709C();

    framebuffers = D_8002AAE8;
    framebuffers[0] = func_10003C6C(0x1ECC0, 0xFF, 3, 1, 0);
    framebuffers[1] = func_10003C6C(0x1ECC0, 0xFF, 3, 1, 0);
    osCreateViManager(OS_PRIORITY_VIMGR);

    offset = 0x42450;
    func_10004514(offset, &D_80082B20, 0x10, 1);
    sourceAddress = D_80082B20 + offset;
    transferSize = 0x19EA88 - sourceAddress;
    allocation = allocate_memory(transferSize, 1, 2, 0);
    func_10004514(sourceAddress, (void *)allocation, transferSize, 1);
    func_10006240((void *)allocation, &D_80082B20, D_8003809C);
    func_10004074((void *)allocation);

    blockCount = (u32)((s32)&D_151FA130 - (s32)func_15000000 + 0xFFF) >> 12;
    D_800354F8 = ALIGN16(&D_80033330);
    D_800354FC = (s32 *)ALIGNU16(&D_80032B30);
    func_10004514(offset + 4, D_800354FC,
                  (((((blockCount + 2) << 2) + 0xF) | 0xF) ^ 0xF), 1);

    blockCount++;
    for (i = 0; i < blockCount; i++) {
        D_800354FC[i] = (D_800354FC[i] ^ 0x8039CCCA) + offset;
    }

    D_8003BE74 = 0;
    func_10005B04(0xEB);
    func_10001420();
    func_10005BE0();
    func_15007830();
}
