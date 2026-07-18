#include <ultra64.h>
#include "controller.h"

#ifdef __osSumcalc
#undef __osSumcalc
#endif
#ifdef __osIdCheckSum
#undef __osIdCheckSum
#endif
#ifdef __osRepairPackId
#undef __osRepairPackId
#endif
#ifdef __osCheckPackId
#undef __osCheckPackId
#endif
#ifdef __osGetId
#undef __osGetId
#endif
#ifdef __osCheckId
#undef __osCheckId
#endif
#ifdef __osPfsRWInode
#undef __osPfsRWInode
#endif
#ifdef __osPfsSelectBank
#undef __osPfsSelectBank
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/contpfs.s. */

u16 __osSumcalc(u8 *ptr, int length) {
    return 0;
}

s32 __osIdCheckSum(u16 *ptr, u16 *csum, u16 *icsum) {
    return 0;
}

s32 __osRepairPackId(OSPfs *pfs, __OSPackId *badid, __OSPackId *newid) {
    return 0;
}

s32 __osCheckPackId(OSPfs *pfs, __OSPackId *temp) {
    return 0;
}

s32 __osGetId(OSPfs *pfs) {
    return 0;
}

s32 __osCheckId(OSPfs *pfs) {
    return 0;
}

s32 __osPfsRWInode(OSPfs *pfs, __OSInode *inode, u8 flag, u8 bank) {
    return 0;
}

s32 __osPfsSelectBank(OSPfs *pfs) {
    return 0;
}
