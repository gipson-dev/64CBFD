
#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_10002718();
/* End generated placeholder declarations. */

extern u8 D_8002AAF0[];
extern u8 D_8002AB14[];
extern u8 D_8002BF80[];
extern u8 D_8002BF84[];
extern s32 D_8002BF8C[];

typedef struct {
    s32 unk0;
    s32 unk4;
    u8 *text;
    s32 prefixLength;
    s32 leadingZeroes;
    s32 textLength;
    s32 middleZeroes;
    s32 suffixLength;
    s32 trailingZeroes;
    s32 unk24;
    s32 unk28;
    s32 unk2C;
    s32 flags;
    u8 length;
    u8 pad35[3];
} PrintConversion;

s32 func_10002070(s32 arg0, s32 arg1, s32 arg2) {
    return 1;
}
s32 func_100020D0(s32 (*arg0)(s32, u8 *, s32), s32 arg1, u8 *arg2,
                   s32 *arg3);

void func_10002088(s32 arg0, ...) {
    D_80035500 = 0;
    func_100020D0(func_10002070, 0, arg0, &arg0 + 1);
}

s32 func_100020D0(s32 (*write)(s32, u8 *, s32), s32 state, u8 *format,
                   s32 *args) {
    u8 buffer[0x2C];
    PrintConversion conversion;
    s32 total;
    s32 flags;
    s32 chunk;
    s32 written;
    u8 *cursor;
    u8 *start;
    u8 *flag;

    total = 0;
    for (;;) {
        start = format;
        while ((*format != 0) && (*format != '%')) {
            format++;
        }
        written = format - start;
        if (written > 0) {
            state = write(state, start, written);
            if (state == 0) {
                return total;
            }
            total += written;
        }
        if (*format == 0) {
            return total;
        }

        cursor = format + 1;
        flags = 0;
        while ((flag = (u8 *)strchr((char *)D_8002BF84, *cursor)) != NULL) {
            flags |= D_8002BF8C[flag - D_8002BF84];
            cursor++;
        }

        if (*cursor == '*') {
            args = (s32 *)(((u32)args + 3) & ~3);
            conversion.unk28 = *args++;
            cursor++;
            if (conversion.unk28 < 0) {
                conversion.unk28 = -conversion.unk28;
                flags |= 4;
            }
        } else {
            conversion.unk28 = 0;
            while ((*cursor >= '0') && (*cursor <= '9')) {
                if (conversion.unk28 < 999) {
                    conversion.unk28 = (*cursor - '0') +
                                       (conversion.unk28 * 10);
                }
                cursor++;
            }
        }

        if (*cursor != '.') {
            conversion.unk24 = -1;
        } else {
            cursor++;
            if (*cursor == '*') {
                args = (s32 *)(((u32)args + 3) & ~3);
                conversion.unk24 = *args++;
                cursor++;
            } else {
                conversion.unk24 = 0;
                while ((*cursor >= '0') && (*cursor <= '9')) {
                    if (conversion.unk24 < 999) {
                        conversion.unk24 = (*cursor - '0') +
                                           (conversion.unk24 * 10);
                    }
                    cursor++;
                }
            }
        }

        if (strchr((char *)D_8002BF80, *cursor) != NULL) {
            conversion.length = *cursor++;
        } else {
            conversion.length = 0;
        }
        if ((conversion.length == 'l') && (*cursor == 'l')) {
            conversion.length = 'L';
            cursor++;
        }

        conversion.flags = flags;
        func_10002718(&conversion, &args, *cursor, buffer);

        conversion.unk28 -= conversion.prefixLength +
                            conversion.leadingZeroes + conversion.textLength +
                            conversion.middleZeroes + conversion.suffixLength +
                            conversion.trailingZeroes;

        if ((flags & 4) == 0) {
            while (conversion.unk28 > 0) {
                chunk = (conversion.unk28 < 0x21) ? conversion.unk28 : 0x20;
                if (chunk > 0) {
                    state = write(state, D_8002AAF0, chunk);
                    if (state == 0) {
                        return total;
                    }
                    total += chunk;
                }
                conversion.unk28 -= chunk;
            }
        }

        if (conversion.prefixLength > 0) {
            state = write(state, buffer, conversion.prefixLength);
            if (state == 0) {
                return total;
            }
            total += conversion.prefixLength;
        }

        for (written = conversion.leadingZeroes; written > 0;
             written -= chunk) {
            chunk = (written < 0x21) ? written : 0x20;
            if (chunk > 0) {
                state = write(state, D_8002AB14, chunk);
                if (state == 0) {
                    return total;
                }
                total += chunk;
            }
        }

        if (conversion.textLength > 0) {
            state = write(state, conversion.text, conversion.textLength);
            if (state == 0) {
                return total;
            }
            total += conversion.textLength;
        }

        for (written = conversion.middleZeroes; written > 0;
             written -= chunk) {
            chunk = (written < 0x21) ? written : 0x20;
            if (chunk > 0) {
                state = write(state, D_8002AB14, chunk);
                if (state == 0) {
                    return total;
                }
                total += chunk;
            }
        }

        if (conversion.suffixLength > 0) {
            state = write(state, conversion.text + conversion.textLength,
                          conversion.suffixLength);
            if (state == 0) {
                return total;
            }
            total += conversion.suffixLength;
        }

        for (written = conversion.trailingZeroes; written > 0;
             written -= chunk) {
            chunk = (written < 0x21) ? written : 0x20;
            if (chunk > 0) {
                state = write(state, D_8002AB14, chunk);
                if (state == 0) {
                    return total;
                }
                total += chunk;
            }
        }

        if ((flags & 4) != 0) {
            while (conversion.unk28 > 0) {
                chunk = (conversion.unk28 < 0x21) ? conversion.unk28 : 0x20;
                if (chunk > 0) {
                    state = write(state, D_8002AAF0, chunk);
                    if (state == 0) {
                        return total;
                    }
                    total += chunk;
                }
                conversion.unk28 -= chunk;
            }
        }
        format = cursor + 1;
    }
}

// contains a jump table
/* Non-matching C placeholders for asm/nonmatchings/init_2070/func_10002718.s. */
s32 func_10002718() {
    return 0;
}
