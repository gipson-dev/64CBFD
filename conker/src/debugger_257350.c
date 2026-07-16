#include <ultra64.h>
#include "stdarg.h"
#include "stdlib.h"
#include "string.h"

#include "functions.h"
#include "variables.h"

s32 func_16001BB4(s32 (*arg0)(u8 *, u8 *, u32), u8 *dst, u8 *fmt, va_list arg3);
s32 func_16002D2C(s16 *arg0, u16 *arg1);
void func_16002DE4(struct262 *arg0, u8 arg1, u8 *arg2, s16 arg3, s16 arg4);

// whats wrong with bcopy?
u8* func_16001AD0(u8 *arg0, u8 *arg1, u32 arg2) {
    u8 *tmp0 = arg0;
    u8 *tmp1 = arg1;

    while (arg2 > 0) {
        *tmp0++ = *tmp1++;
        arg2 -= 1;
    }

    return arg0;
}

s32 func_16001B00(u8 *arg0) { // strlen
    s32 count;
    u8 *p;

    p = arg0;
    count = 0;
    if (*arg0 != 0) {
        do {
            count += 1;
            p += 1;
        } while (p[0] != 0);
    }
    return count;
}
// sprintf-style: format arg1 into arg0 via the %-parser func_16001BB4;
// a true varargs function (retail homes all four register args at entry,
// which is IDO's varargs codegen - K&R or address-taken params don't
// reproduce it). va_start(ap, arg1) = &arg2's home slot, so the va_list
// hand-off to func_16001BB4 and callers passing extra args (including
// func_16001044's f64 for "%f") all just work.
s32 func_16001B34(u8 *arg0, u8 *arg1, ...) {
    s32 idx;
    va_list ap;

    va_start(ap, arg1);
    idx = func_16001BB4(func_16001B8C, arg0, arg1, ap);
    va_end(ap);
    if (idx >= 0) {
        arg0[idx] = 0;
    }
    return idx;
}
s32 func_16001B8C(u8 *arg0, u8 *arg1, u32 arg2) {
    return func_16001AD0(arg0, arg1, arg2) + arg2;
}

// Plauger/N64-SDK _Printf (see the _Litob note below). The pad emission
// blocks are the SDK's _PROUT/_PAD macros with a distinct i/c local pair
// per instance, and the running total is the struct's pad2C ("size")
// field - which is why retail keeps it memory-resident across callbacks.
#define ATOI(i, a)                           \
    for (i = 0; *a >= '0' && *a <= '9'; a++) \
        if (i < 999)                         \
            i = *a + i * 10 - '0';
#define _PROUT(dst, fmt, _size)                      \
    if (_size > 0) {                                 \
        dst = (u8 *) arg0(dst, (u8 *) (fmt), _size); \
        if (dst != 0)                                \
            st.pad2C += _size;                       \
        else                                         \
            return st.pad2C;                         \
    }
#define _PAD(i, m, c, src, extracond) \
    if (extracond && m > 0)           \
        for (i = m; i > 0; i -= c) {  \
            if ((u32) i > 32)         \
                c = 32;               \
            else                      \
                c = i;                \
            _PROUT(dst, src, c);      \
        }

// NEARLY MATCHING (400/402 words, ~6 real diff instructions) - kept as
// GLOBAL_ASM below so the function occupies its exact retail size, which
// heals the debugger overlay's data displacement. Two 1-word uopt
// scheduling idioms remain unsolved in C (see WORKING_NOTES eighteenth
// session part 3): (1) retail computes the first chunk via
// `subu v0` + `move s1,v0` (a web-split across the callback call that
// our uopt always coalesces), and (2) retail likely-converts the last
// _PAD's skip branch (beqzl + duplicated addiu in its delay) and fills
// the loop-back `b` delay with an `lbu` preload of the loop top, where
// ours fills it with the fmt update instead. Both double-branch
// structures exist in our build too - only the delay-fill choices
// differ. Re-enable this C (and delete the pragma) to keep hunting.
// s32 func_16001BB4(s32 (*arg0)(u8 *, u8 *, u32), u8 *dst, u8 *fmt, va_list arg3) {
//     struct262 st;
//     u8 *fmt_ptr;
//     u8 c;
//     u8 *flag_index;
//     u8 buf[0x20];
//     s32 c1, i1, c2, i2, c3, i3, c4, i4, c5, i5;
//     s32 n;
//     s32 pad1;
//
//     st.pad2C = 0;
//     for (;; fmt = fmt_ptr + 1) {
//     c = *fmt;
//     fmt_ptr = fmt + 1;
//     if ((s32) c > 0) {
//         while (1) {
//             if (c == '%') {
//                 fmt_ptr -= 1;
//                 break;
//             }
//             c = *fmt_ptr;
//             fmt_ptr += 1;
//             if ((s32) c <= 0) {
//                 break;
//             }
//         }
//     }
//     if (fmt_ptr - fmt > 0) {
//         i1 = fmt_ptr - fmt;
//         dst = (u8 *) arg0(dst, fmt, fmt_ptr - fmt);
//         if (dst != 0)
//             st.pad2C += i1;
//         else
//             return st.pad2C;
//     }
//     fmt_ptr += 1;
//     if (c == 0) {
//         return st.pad2C;
//     }
//     st.flags = 0;
//     for (; (flag_index = (u8 *) strchr((char *) D_16004804, *fmt_ptr)) != NULL; fmt_ptr++) {
//         st.flags |= D_1600480C[flag_index - D_16004804];
//     }
//     if (*fmt_ptr == '*') {
//         st.unk28 = va_arg(arg3, s32);
//         if (st.unk28 < 0) {
//             st.unk28 = -st.unk28;
//             st.flags |= 4;
//         }
//         fmt_ptr++;
//     } else {
//         ATOI(st.unk28, fmt_ptr);
//     }
//     if (*fmt_ptr != '.') {
//         st.width = -1;
//     } else {
//         fmt_ptr++;
//         if (*fmt_ptr == '*') {
//             st.width = va_arg(arg3, s32);
//             fmt_ptr++;
//         } else {
//             ATOI(st.width, fmt_ptr);
//         }
//     }
//     if (strchr((char *) D_16004800, *fmt_ptr) != NULL) {
//         st.length = *fmt_ptr++;
//     } else {
//         st.length = 0;
//     }
//     if (st.length == 'l' && *fmt_ptr == 'l') {
//         st.length = 'L';
//         fmt_ptr++;
//     }
//     func_160021FC(&st, &arg3, *fmt_ptr, buf);
//     st.unk28 -= st.unkC + st.padWidth + st.len + st.unk18 + st.unk1C + st.unk20;
//     _PAD(i1, st.unk28, c1, D_16003C70, !(st.flags & 4));
//     _PROUT(dst, buf, st.unkC);
//     _PAD(i1, st.padWidth, c1, D_16003C94, 1);
//     _PROUT(dst, st.dest, st.len);
//     _PAD(i1, st.unk18, c1, D_16003C94, 1);
//     _PROUT(dst, &st.dest[st.len], st.unk1C);
//     _PAD(i1, st.unk20, c1, D_16003C94, 1);
//     _PAD(i1, st.unk28, c1, D_16003C70, st.flags & 4);
//     }
// }
#pragma GLOBAL_ASM("asm/nonmatchings/debugger_257350/func_16001BB4.s")

#undef ATOI
#undef _PROUT
#undef _PAD

// uses jump table
#pragma GLOBAL_ASM("asm/nonmatchings/debugger_257350/func_160021FC.s")
// contains delay slot
// Plauger/N64-SDK _Ldtob (see the _Litob note below; func_16002D2C is
// _Ldunscale, D_16004870/D_16004874 are "NaN"/"Inf", D_16004828 is the
// 10^(2^n) powers table, D_16004950 is 1.0e8).
void func_1600288C(struct262 *arg0, u8 arg1) {
    u8 buf[0x20];
    u8 *ptr;
    f64 val;
    volatile f64 zero2;
    s32 err;
    s16 nsig;
    s16 exp;
    f64 factor;
    u8 drop;
    s32 n2;
    f64 zero;
    f32 fzero;
    f32 one;

    ptr = buf;
    val = arg0->num.fvalue;
    fzero = 0;
    one = 1;
    zero = fzero;
    zero2 = zero;
    if (arg0->width < 0) {
        arg0->width = 6;
    } else if (arg0->width == 0 && (arg1 == 'g' || arg1 == 'G')) {
        arg0->width = 1;
    }
    err = func_16002D2C(&exp, (u16 *) arg0);
    if (err > 0) {
        func_16001AD0(arg0->dest, (err == 2) ? D_16004870 : D_16004874, arg0->len = 3);
        return;
    }
    if (err == 0) {
        nsig = 0;
        exp = 0;
    } else {
        s32 i;
        s32 n;
        s32 gen;
        s32 j;
        s32 lo;

        if (val < zero) {
            val = -val;
        }
        exp = exp * 30103 / 0x000186A0 - 4;
        if (exp < 0) {
            n = (3 - exp) & ~3;
            exp = -n;
            for (i = 0; n > 0; n >>= 1, i++) {
                if ((n & 1) != 0) {
                    val *= D_16004828[i];
                }
            }
        } else if (exp > 0) {
            factor = one;
            exp &= ~3;
            for (n = exp, i = 0; n > 0; n >>= 1, i++) {
                if ((n & 1) != 0) {
                    factor *= D_16004828[i];
                }
            }
            val /= factor;
        }
        gen = ((arg1 == 'f') ? exp + 10 : 6) + arg0->width;
        if (gen > 0x13) {
            gen = 0x13;
        }
        *ptr++ = '0';
        if (gen > 0 && zero < val) {
            do {
                lo = val;
                if ((gen -= 8) > 0) {
                    val = (val - lo) * D_16004950;
                }
                ptr = ptr + 8;
                for (j = 8; lo > 0 && --j >= 0;) {
                    ldiv_t qr = ldiv(lo, 10);

                    *--ptr = qr.rem + '0';
                    lo = qr.quot;
                }
                while (--j >= 0) {
                    ptr--;
                    *ptr = '0';
                }
                ptr += 8;
            } while (gen > 0 && zero2 < val);
        }

        gen = ptr - &buf[1];
        for (ptr = &buf[1], exp += 7; *ptr == '0'; ptr++) {
            --gen, --exp;
        }

        nsig = ((arg1 == 'f') ? exp + 1 : ((arg1 == 'e' || arg1 == 'E') ? 1 : 0)) + arg0->width;
        if (gen < nsig) {
            nsig = gen;
        }
        if (nsig > 0) {
            if (nsig < gen && ptr[nsig] > '4') {
                drop = '9';
            } else {
                drop = '0';
            }

            for (n2 = nsig; ptr[--n2] == drop;) {
                nsig--;
            }
            if (drop == '9') {
                ptr[n2]++;
            }
            if (n2 < 0) {
                --ptr, ++nsig, ++exp;
            }
        }
    }
    func_16002DE4(arg0, arg1, ptr, nsig, exp);
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
// classify an IEEE double via its first u16: >0 normal (exponent extracted
// to *arg0, mantissa top rebased to 1.0-2.0), 0 zero, 1 Inf, 2 NaN/denormal.
// The (s16)(ternary) return is load-bearing: cfe converts each ternary arm
// to s16 at its own definition site and uopt never folds those conversions,
// which is the only source shape that reproduces retail's li/sll/sra pairs
// (a plain variable or two returns gets constant-folded to li v0,2/1).
// Reading arg1[0] directly everywhere (no local copy) is also load-bearing:
// CSE supplies the single lhu in a2; a named local flips the a2/v1 register
// assignment or materializes an extra andi 0xFFFF.
s32 func_16002D2C(s16 *arg0, u16 *arg1) {
    s16 exp;

    exp = (arg1[0] & 0x7FF0) >> 4;
    if (exp == 0x7FF) {
        *arg0 = 0;
        return (s16) (((arg1[0] & 0xF) || (arg1[1] != 0) || (arg1[2] != 0) || (arg1[3] != 0)) ? 2 : 1);
    }
    if (exp > 0) {
        arg1[0] = (arg1[0] & 0x800F) | 0x3FF0;
        *arg0 = exp - 0x3FE;
        return -1;
    }
    if (exp < 0) {
        return 2;
    }
    *arg0 = 0;
    return 0;
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
// %f/%e/%g digit placement: lays out the converted digit string (arg2,
// arg3 digits) and exponent (arg4) into the output record.
// Plauger/N64-SDK _Genld (see the _Litob note below; field mapping:
// width=precision, len=part2_len, dest=buff, unkC=part1_len,
// unk18=num_mid_zeros, unk1C=part3_len, unk20=num_trailing_zeros,
// unk28=width, padWidth=num_leading_zeros; func_16001AD0=memcpy).
void func_16002DE4(struct262 *arg0, u8 arg1, u8 *arg2, s16 arg3, s16 arg4) {
    u8 point = '.';

    if (arg3 <= 0) {
        arg2 = D_16004878;
        arg3 = 1;
    }
    if (arg1 == 'f' || ((arg1 == 'g' || arg1 == 'G') && (-4 <= arg4) && (arg4 < arg0->width))) {
        ++arg4;
        if (arg1 != 'f') {
            if (!(arg0->flags & 8) && (arg3 < arg0->width)) {
                arg0->width = arg3;
            }
            if ((arg0->width -= arg4) < 0) {
                arg0->width = 0;
            }
        }
        if (arg4 <= 0) {
            arg0->dest[arg0->len++] = '0';
            if ((0 < arg0->width) || (arg0->flags & 8)) {
                arg0->dest[arg0->len++] = point;
            }
            if (arg0->width < -arg4) {
                arg4 = -arg0->width;
            }
            arg0->unk18 = -arg4;
            arg0->width += arg4;
            if (arg0->width < arg3) {
                arg3 = arg0->width;
            }
            func_16001AD0(&arg0->dest[arg0->len], arg2, arg0->unk1C = arg3);
            arg0->unk20 = arg0->width - arg3;
        } else if (arg3 < arg4) {
            func_16001AD0(&arg0->dest[arg0->len], arg2, arg3);
            arg0->len += arg3;
            arg0->unk18 = arg4 - arg3;
            if ((0 < arg0->width) || (arg0->flags & 8)) {
                arg0->dest[arg0->len] = point, ++arg0->unk1C;
            }
            arg0->unk20 = arg0->width;
        } else {
            func_16001AD0(&arg0->dest[arg0->len], arg2, arg4);
            arg0->len += arg4;
            arg3 -= arg4;
            if ((0 < arg0->width) || (arg0->flags & 8)) {
                arg0->dest[arg0->len++] = point;
            }
            if (arg0->width < arg3) {
                arg3 = arg0->width;
            }
            func_16001AD0(&arg0->dest[arg0->len], arg2 + arg4, arg3);
            arg0->len += arg3;
            arg0->unk18 = arg0->width - arg3;
        }
    } else {
        if (arg1 == 'g' || arg1 == 'G') {
            if (arg3 < arg0->width) {
                arg0->width = arg3;
            }
            if (--arg0->width < 0) {
                arg0->width = 0;
            }
            arg1 = (arg1 == 'g') ? 'e' : 'E';
        }
        arg0->dest[arg0->len++] = *arg2++;
        if ((0 < arg0->width) || (arg0->flags & 8)) {
            arg0->dest[arg0->len++] = point;
        }
        if (0 < arg0->width) {
            if (arg0->width < --arg3) {
                arg3 = arg0->width;
            }
            func_16001AD0(&arg0->dest[arg0->len], arg2, arg3);
            arg0->len += arg3;
            arg0->unk18 = arg0->width - arg3;
        }
        arg2 = &arg0->dest[arg0->len];
        *arg2++ = arg1;
        if (0 <= arg4) {
            *arg2++ = '+';
        } else {
            *arg2++ = '-';
            arg4 = -arg4;
        }
        if (100 <= arg4) {
            if (1000 <= arg4) {
                *arg2++ = arg4 / 1000 + '0', arg4 %= 1000;
            }
            *arg2++ = arg4 / 100 + '0', arg4 %= 100;
        }
        *arg2++ = arg4 / 10 + '0', arg4 %= 10;
        *arg2++ = arg4 + '0';
        arg0->unk1C = arg2 - &arg0->dest[arg0->len];
    }
    if ((arg0->flags & 0x14) == 0x10) {
        s32 total = arg0->unkC + arg0->len + arg0->unk18 + arg0->unk1C + arg0->unk20;

        if (total < arg0->unk28) {
            arg0->padWidth = arg0->unk28 - total;
        }
    }
}
// %d/%i/%o/%x/%X: 64-bit integer to string via repeated division.
// This is P.J. Plauger's _Litob ("The Standard C Library" printf engine,
// which this whole debugger formatter file is Rare's 64-bit adaptation of:
// func_16001BB4 = _Printf, func_1600288C = _Ldtob, this = _Litob).
// Shape notes confirmed against retail: radix/table are nested-ternary
// declaration initializers, uvalue initializes straight from the struct
// (no s64 local - the value slot pair in retail is cfe's 64-bit staging
// temp), the negate is uvalue = -uvalue, buf[--pos] indexing (the
// pre-decrement temp is what stops uopt inventing a moving pointer), qr is
// block-scoped in the loop, the loop condition reads arg0->num.value
// directly, and the final width fixup reuses pos (Plauger reuses i).
void func_160033A8(struct262 *arg0, u8 arg1) {
    u8 buf[24];
    u8 *table = (arg1 == 'X') ? &D_16003CCC : &D_16003CB8;
    s32 radix = (arg1 == 'o') ? 8 : (arg1 != 'x' && arg1 != 'X') ? 10 : 16;
    s32 pos = 24;
    u64 uvalue = arg0->num.value;

    if ((arg1 == 'd' || arg1 == 'i') && (arg0->num.value < 0)) {
        uvalue = -uvalue;
    }
    if ((uvalue != 0) || (arg0->width != 0)) {
        buf[--pos] = table[uvalue % radix];
    }
    arg0->num.value = uvalue / radix;
    while ((arg0->num.value > 0) && (pos > 0)) {
        lldiv_t qr = lldiv(arg0->num.value, radix);

        arg0->num.value = qr.quot;
        buf[--pos] = table[qr.rem];
    }
    arg0->len = 24 - pos;
    func_16001AD0(arg0->dest, &buf[pos], arg0->len);
    if (arg0->len < arg0->width) {
        arg0->padWidth = arg0->width - arg0->len;
    }
    if ((arg0->width < 0) && ((arg0->flags & 0x14) == 0x10)) {
        pos = ((arg0->unk28 - arg0->unkC) - arg0->padWidth) - arg0->len;
        if (pos > 0) {
            arg0->padWidth = arg0->padWidth + pos;
        }
    }
}
