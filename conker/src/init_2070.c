
#include <ultra64.h>
#include "string.h"

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

void _Litob(PrintConversion *arg0, s32 arg1);

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

s32 func_10002718(arg0, arg1, arg2, arg3)
PrintConversion *arg0;
s32 **arg1;
u8 arg2;
u8 *arg3;
{
    s32 *cursor;
    s64 value;
    void *pointer;

    arg0->prefixLength = 0;
    arg0->leadingZeroes = 0;
    arg0->textLength = 0;
    arg0->middleZeroes = 0;
    arg0->suffixLength = 0;
    arg0->trailingZeroes = 0;

    switch (arg2) {
        case 'c':
            cursor = (s32 *)(((u32)*arg1 + 3) & ~3);
            *arg1 = cursor + 1;
            arg3[arg0->prefixLength++] = *cursor;
            break;

        case 'd':
        case 'i':
            if (arg0->length == 'L') {
                cursor = (s32 *)(((u32)*arg1 + 7) & ~7);
                value = *(s64 *)cursor;
                *arg1 = cursor + 2;
            } else {
                cursor = (s32 *)(((u32)*arg1 + 3) & ~3);
                value = *cursor;
                *arg1 = cursor + 1;
            }
            if (arg0->length == 'h') {
                value = (s16)value;
            }
            *(s64 *)&arg0->unk0 = value;
            if (value < 0) {
                arg3[arg0->prefixLength++] = '-';
            } else if ((arg0->flags & 2) != 0) {
                arg3[arg0->prefixLength++] = '+';
            } else if ((arg0->flags & 1) != 0) {
                arg3[arg0->prefixLength++] = ' ';
            }
            arg0->text = arg3 + arg0->prefixLength;
            _Litob(arg0, arg2);
            break;

        case 'x':
        case 'X':
        case 'u':
        case 'o':
            if (arg0->length == 'L') {
                cursor = (s32 *)(((u32)*arg1 + 7) & ~7);
                value = *(s64 *)cursor;
                *arg1 = cursor + 2;
            } else {
                cursor = (s32 *)(((u32)*arg1 + 3) & ~3);
                value = *cursor;
                *arg1 = cursor + 1;
            }
            if (arg0->length == 'h') {
                value = (u16)value;
            } else if (arg0->length == 0) {
                value = (u32)value;
            }
            *(s64 *)&arg0->unk0 = value;
            if ((arg0->flags & 8) != 0) {
                arg3[arg0->prefixLength++] = '0';
                if ((arg2 == 'x') || (arg2 == 'X')) {
                    arg3[arg0->prefixLength++] = arg2;
                }
            }
            arg0->text = arg3 + arg0->prefixLength;
            _Litob(arg0, arg2);
            break;

        case 'e':
        case 'f':
        case 'g':
        case 'E':
        case 'G':
            cursor = (s32 *)(((u32)*arg1 + 7) & ~7);
            *(f64 *)&arg0->unk0 = *(f64 *)cursor;
            *arg1 = cursor + 2;
            if ((*(u16 *)&arg0->unk0 & 0x8000) != 0) {
                arg3[arg0->prefixLength++] = '-';
            } else if ((arg0->flags & 2) != 0) {
                arg3[arg0->prefixLength++] = '+';
            } else if ((arg0->flags & 1) != 0) {
                arg3[arg0->prefixLength++] = ' ';
            }
            arg0->text = arg3 + arg0->prefixLength;
            func_10001550((struct246 *)arg0, arg2);
            break;

        case 'n':
            cursor = (s32 *)(((u32)*arg1 + 3) & ~3);
            pointer = (void *)*cursor;
            *arg1 = cursor + 1;
            if (arg0->length == 'h') {
                *(u16 *)pointer = arg0->unk2C;
            } else if (arg0->length == 'L') {
                *(u64 *)pointer = (u32)arg0->unk2C;
            } else {
                *(u32 *)pointer = arg0->unk2C;
            }
            break;

        case 'p':
            cursor = (s32 *)(((u32)*arg1 + 3) & ~3);
            value = *cursor;
            *arg1 = cursor + 1;
            *(s64 *)&arg0->unk0 = value;
            arg0->text = arg3 + arg0->prefixLength;
            _Litob(arg0, 'x');
            break;

        case 's':
            cursor = (s32 *)(((u32)*arg1 + 3) & ~3);
            arg0->text = (u8 *)*cursor;
            *arg1 = cursor + 1;
            arg0->textLength = strlen((char *)arg0->text);
            if ((arg0->unk24 >= 0) && (arg0->unk24 < arg0->textLength)) {
                arg0->textLength = arg0->unk24;
            }
            break;

        case '%':
            arg3[arg0->prefixLength++] = '%';
            break;

        default:
            arg3[arg0->prefixLength++] = arg2;
            break;
    }
}
