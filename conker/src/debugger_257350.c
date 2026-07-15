#include <ultra64.h>
#include "stdarg.h"
#include "stdlib.h"
#include "string.h"

#include "functions.h"
#include "variables.h"

s32 func_16001BB4(s32 (*arg0)(u8 *, u8 *, u32), u8 *arg1, u8 *arg2, s32 *arg3);
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
    idx = func_16001BB4(func_16001B8C, arg0, arg1, (s32 *) ap);
    va_end(ap);
    if (idx >= 0) {
        arg0[idx] = 0;
    }
    return idx;
}
s32 func_16001B8C(u8 *arg0, u8 *arg1, u32 arg2) {
    return func_16001AD0(arg0, arg1, arg2) + arg2;
}

// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_16001BB4(s32 (*arg0)(u8 *, u8 *, u32), u8 *arg1, u8 *arg2, s32 *arg3) {
    u8 *fmt;
    u8 *scan;
    u8 c;
    s32 dest;
    s32 total;
    s32 chunk;
    struct262 st;
    u8 buf[0x2C];
    u8 length_mod;
    u8 flagc;
    s32 pad_total;
    s32 remaining;
    s32 n;

    fmt = arg2;
    dest = (s32) arg1;
    total = 0;
loop_1:
    c = *fmt;
    scan = fmt + 1;
    if ((s32) c > 0) {
        while (1) {
            if (c == '%') {
                scan -= 1;
                break;
            }
            c = *scan;
            scan += 1;
            if ((s32) c <= 0) {
                break;
            }
        }
    }
    chunk = (s32) (scan - fmt);
    if (chunk > 0) {
        dest = arg0((u8 *) dest, fmt, chunk);
        if (dest != 0) {
            total += chunk;
        } else {
            return total;
        }
    }
    scan += 1;
    if (c == 0) {
        return total;
    }
    st.flags = 0;
    {
        u8 *p = (u8 *) strchr((char *) D_16004804, *scan);
        while (p != 0) {
            scan += 1;
            st.flags |= D_1600480C[p - D_16004804];
            p = (u8 *) strchr((char *) D_16004804, *scan);
        }
    }
    if (*scan == '*') {
        s32 *va = (s32 *) (((s32) arg3 + 3) & ~3);
        s32 v = *va;
        arg3 = (s32 *) ((u8 *) va + 4);
        scan += 1;
        st.unk28 = v;
        if (v < 0) {
            st.unk28 = -v;
            st.flags |= 4;
        }
        flagc = *scan;
    } else {
        st.unk28 = 0;
        flagc = *scan;
        if (((s32) flagc >= '0') && ((s32) flagc < ':')) {
            do {
                if (st.unk28 < 0x3E7) {
                    st.unk28 = (flagc + (st.unk28 * 10)) - '0';
                }
                flagc = scan[1];
                scan += 1;
            } while (((s32) flagc >= '0') && ((s32) flagc < ':'));
        }
    }
    if (flagc != '.') {
        st.width = -1;
        flagc = *scan;
    } else {
        u8 nextc = scan[1];
        scan += 1;
        if (nextc == '*') {
            s32 *va = (s32 *) (((s32) arg3 + 3) & ~3);
            arg3 = (s32 *) ((u8 *) va + 4);
            scan += 1;
            st.width = *va;
            flagc = *scan;
        } else {
            st.width = 0;
            flagc = *scan;
            if (((s32) flagc >= '0') && ((s32) flagc < ':')) {
                do {
                    if (st.width < 0x3E7) {
                        st.width = (flagc + (st.width * 10)) - '0';
                    }
                    flagc = scan[1];
                    scan += 1;
                } while (((s32) flagc >= '0') && ((s32) flagc < ':'));
            }
        }
    }
    if (strchr((char *) D_16004800, flagc) != 0) {
        length_mod = *scan;
        scan += 1;
    } else {
        length_mod = 0;
    }
    if ((length_mod == 'l') && (*scan == 'l')) {
        length_mod = 'L';
        scan += 1;
    }
    func_160021FC(&st, arg3, *scan, buf);
    pad_total = ((((st.unk28 - st.unkC) - st.padWidth) - st.len) - st.unk18) - st.unk1C;
    pad_total -= st.unk20;
    st.unk28 = pad_total;
    if (!(st.flags & 4)) {
        if (pad_total > 0) {
            remaining = pad_total;
            do {
                n = ((u32) remaining >= 0x21U) ? 0x20 : remaining;
                if (n > 0) {
                    dest = arg0((u8 *) dest, D_16003C70, n);
                    if (dest != 0) {
                        total += n;
                    } else {
                        return total;
                    }
                }
                remaining -= n;
            } while (remaining > 0);
        }
    }
    if (st.unkC > 0) {
        dest = arg0((u8 *) dest, buf, st.unkC);
        if (dest != 0) {
            total += st.unkC;
        } else {
            return total;
        }
    }
    if (st.padWidth > 0) {
        remaining = st.padWidth;
        do {
            n = ((u32) remaining >= 0x21U) ? 0x20 : remaining;
            if (n > 0) {
                dest = arg0((u8 *) dest, D_16003C94, n);
                if (dest != 0) {
                    total += n;
                } else {
                    return total;
                }
            }
            remaining -= n;
        } while (remaining > 0);
    }
    if (st.len > 0) {
        dest = arg0((u8 *) dest, st.dest, st.len);
        if (dest != 0) {
            total += st.len;
        } else {
            return total;
        }
    }
    if (st.unk18 > 0) {
        remaining = st.unk18;
        do {
            n = ((u32) remaining >= 0x21U) ? 0x20 : remaining;
            if (n > 0) {
                dest = arg0((u8 *) dest, D_16003C94, n);
                if (dest != 0) {
                    total += n;
                } else {
                    return total;
                }
            }
            remaining -= n;
        } while (remaining > 0);
    }
    if (st.unk1C > 0) {
        dest = arg0((u8 *) dest, st.dest + st.len, st.unk1C);
        if (dest != 0) {
            total += st.unk1C;
        } else {
            return total;
        }
    }
    if (st.unk20 > 0) {
        remaining = st.unk20;
        do {
            n = ((u32) remaining >= 0x21U) ? 0x20 : remaining;
            if (n > 0) {
                dest = arg0((u8 *) dest, D_16003C94, n);
                if (dest != 0) {
                    total += n;
                } else {
                    return total;
                }
            }
            remaining -= n;
        } while (remaining > 0);
    }
    if ((st.flags & 4) && (pad_total > 0)) {
        remaining = pad_total;
        do {
            n = ((u32) remaining >= 0x21U) ? 0x20 : remaining;
            if (n > 0) {
                dest = arg0((u8 *) dest, D_16003C70, n);
                if (dest != 0) {
                    total += n;
                } else {
                    return total;
                }
            }
            remaining -= n;
        } while (remaining > 0);
    }
    fmt = scan + 1;
    goto loop_1;
}
// uses jump table
#pragma GLOBAL_ASM("asm/nonmatchings/debugger_257350/func_160021FC.s")
// contains delay slot
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_1600288C(struct262 *arg0, u8 arg1) {
    f64 value;
    f64 zero48;
    f64 zeroA0;
    f64 scale;
    s32 fmt;
    s16 exp10;
    s32 exp_status;
    u8 buf[0x20];
    u8 *s2;
    u8 *s2b;
    s32 v1;
    s16 v0;
    s16 t6;
    s32 digits_left;
    s32 int_part;
    s32 out_len;
    s32 whole_digits;
    s32 round_pos;
    u8 *round_ptr;
    s32 i;
    ldiv_t qr;

    value = arg0->num.fvalue;
    s2 = &buf[0];
    zero48 = 0.0;
    zeroA0 = zero48;
    if (arg0->width < 0) {
        arg0->width = 6;
    } else if ((arg0->width == 0) && ((fmt = (s32) arg1, arg1 == 'g') || (arg1 == 'G'))) {
        arg0->width = 1;
    }
    zero48 = 0.0;
    exp_status = func_16002D2C(&exp10, (u16 *) arg0);
    if (exp_status > 0) {
        u8 *msg;
        if (exp_status == 2) {
            msg = D_16004870;
        } else {
            msg = D_16004874;
        }
        arg0->len = 3;
        func_16001AD0(arg0->dest, msg, 3U);
        return;
    }
    round_pos = 0;
    if (exp_status == 0) {
        exp10 = 0;
    } else {
        fmt = (s32) arg1;
        if (value < zero48) {
            value = -value;
        }
        v1 = 0;
        digits_left = 6;
        s2b = &buf[1];
        t6 = (s16) (((s32) (exp10 * 0x7597)) / 100000) - 4;
        exp10 = t6;
        if (t6 < 0) {
            s16 half;
            v0 = (s16) ((3 - t6) & ~3);
            exp10 = -v0;
            if (v0 > 0) {
                do {
                    half = (s16) (v0 >> 1);
                    if (v0 & 1) {
                        value *= D_16004828[v1];
                    }
                    v0 = half;
                    v1 += 1;
                } while (half > 0);
            }
        } else {
            s16 halfb;
            s32 v1b = 0;
            s16 masked = (s16) (exp10 & 0xFFFC);
            if (exp10 > 0) {
                s16 v0b = masked;
                f64 f0 = 1.0;
                exp10 = masked;
                if (masked > 0) {
                    do {
                        halfb = (s16) (v0b >> 1);
                        if (v0b & 1) {
                            f0 *= D_16004828[v1b];
                        }
                        v0b = halfb;
                        v1b += 1;
                    } while (halfb > 0);
                }
                value /= f0;
            }
        }
        if (fmt == 'f') {
            digits_left = exp10 + 0xA;
        }
        whole_digits = digits_left + arg0->width;
        if (whole_digits >= 0x14) {
            whole_digits = 0x13;
        }
        buf[0] = '0';
        if ((whole_digits > 0) && (zero48 < value)) {
            do {
                whole_digits -= 8;
                s2b += 8;
                int_part = (s32) value;
                if (whole_digits > 0) {
                    value = (value - (f64) int_part) * D_16004950;
                }
                digits_left = 8;
                if (int_part > 0) {
                    digits_left = 7;
                    do {
                        qr = ldiv(int_part, 10);
                        s2b -= 1;
                        *s2b = (u8) (qr.rem + '0');
                        int_part = qr.quot;
                        if (qr.quot > 0) {
                            digits_left -= 1;
                            if (digits_left >= 0) {
                                continue;
                            }
                        }
                        break;
                    } while (1);
                }
                digits_left -= 1;
                if (digits_left >= 0) {
                    do {
                        digits_left -= 1;
                        s2b -= 1;
                        *s2b = '0';
                    } while (digits_left >= 0);
                }
                s2 = s2b + 8;
                s2b = s2;
            } while ((whole_digits > 0) && (zeroA0 < value));
        }
        out_len = (s32) (s2 - &buf[0]) - 1;
        exp10 += 7;
        s2 = &buf[1];
        if (buf[1] == '0') {
            do {
                s2 += 1;
                out_len -= 1;
                exp10 -= 1;
            } while (*s2 == '0');
        }
        if (fmt == 'f') {
            round_pos = exp10 + 1;
        } else if ((fmt == 'e') || (fmt == 'E')) {
            round_pos = 1;
        } else {
            round_pos = 0;
        }
        round_pos += arg0->width;
        if (out_len < round_pos) {
            round_pos = out_len;
        }
        if (round_pos > 0) {
            u8 round_digit;
            round_ptr = &s2[round_pos];
            if ((round_pos < out_len) && (*round_ptr >= '5')) {
                round_digit = '9';
            } else {
                round_digit = '0';
                round_ptr = &s2[round_pos];
            }
            i = round_pos - 1;
            if (round_digit == round_ptr[-1]) {
                u8 *p = round_ptr - 1;
                u8 c;
                do {
                    c = p[-1];
                    i -= 1;
                    p -= 1;
                    round_pos -= 1;
                } while (round_digit == c);
            }
            if (round_digit == '9') {
                s2[i] += 1;
            }
            if (i < 0) {
                exp10 += 1;
                round_pos += 1;
                s2 -= 1;
            }
        }
    }
    func_16002DE4(arg0, arg1, s2, (s16) round_pos, exp10);
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_16002D2C(s16 *arg0, u16 *arg1) {
    s32 exp;
    u16 val;

    val = arg1[0];
    exp = (s32) (val & 0x7FF0) >> 4;
    if ((s16) exp == 0x7FF) {
        *arg0 = 0;
        if ((arg1[0] & 0xF) || (arg1[1] != 0) || (arg1[2] != 0) || (arg1[3] != 0)) {
            return 2;
        }
        return 1;
    }
    if ((s16) exp > 0) {
        arg1[0] = (val & 0x800F) | 0x3FF0;
        *arg0 = (s16) exp - 0x3FE;
        return -1;
    }
    if ((s16) exp < 0) {
        return 2;
    }
    *arg0 = 0;
    return 0;
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_16002DE4(struct262 *arg0, u8 arg1, u8 *arg2, s16 arg3, s16 arg4) {
    u8 *var_s1;
    s16 var_a3;
    s16 var_t0;
    s32 var_v0;
    s32 temp_v0;
    s32 temp_v1;
    u8 *ep;
    u8 *p;
    s16 e;

    var_a3 = arg3;
    var_s1 = arg2;
    if (var_a3 <= 0) {
        var_s1 = D_16004878;
        var_a3 = 1;
    }
    if ((arg1 == 'f') || (((arg1 == 'g') || (arg1 == 'G')) && (arg4 >= -4) && (arg4 < arg0->width))) {
        var_t0 = arg4 + 1;
        if (arg1 != 'f') {
            var_v0 = arg0->width;
            if (!(arg0->flags & 8) && (var_a3 < var_v0)) {
                arg0->width = (s32) var_a3;
                var_v0 = (s32) var_a3;
            }
            temp_v0 = var_v0 - var_t0;
            arg0->width = temp_v0;
            if (temp_v0 < 0) {
                arg0->width = 0;
            }
        }
        if (var_t0 <= 0) {
            s16 var_v1 = -var_t0;
            arg0->dest[arg0->len] = '0';
            arg0->len = arg0->len + 1;
            if ((arg0->width > 0) || (arg0->flags & 8)) {
                arg0->dest[arg0->len] = '.';
                arg0->len = arg0->len + 1;
            }
            if (arg0->width < var_v1) {
                var_t0 = (s16) arg0->width * -1;
                var_v1 = -var_t0;
            }
            temp_v0 = arg0->width + var_t0;
            arg0->unk18 = (s32) var_v1;
            arg0->width = temp_v0;
            if (temp_v0 < var_a3) {
                var_a3 = (s16) temp_v0;
            }
            arg0->unk1C = (s32) var_a3;
            arg3 = var_a3;
            func_16001AD0(arg0->dest + arg0->len, var_s1, (u32) var_a3);
            arg0->unk20 = (s32) (arg0->width - arg3);
        } else if (var_a3 < var_t0) {
            s16 var_a3_2;
            arg4 = var_t0;
            arg3 = var_a3;
            func_16001AD0(arg0->dest + arg0->len, var_s1, (u32) var_a3);
            arg0->len = arg0->len + arg3;
            arg0->unk18 = (s32) (arg4 - arg3);
            if ((arg0->width > 0) || (arg0->flags & 8)) {
                arg0->dest[arg0->len] = '.';
                arg0->unk1C = arg0->unk1C + 1;
            }
            arg0->unk20 = arg0->width;
        } else {
            s16 var_a3_2;
            arg4 = var_t0;
            arg3 = var_a3;
            func_16001AD0(arg0->dest + arg0->len, var_s1, (u32) var_t0);
            arg0->len = arg0->len + arg4;
            var_a3_2 = arg3 - arg4;
            if ((arg0->width > 0) || (arg0->flags & 8)) {
                arg0->dest[arg0->len] = '.';
                arg0->len = arg0->len + 1;
            }
            if ((s16) arg0->width < var_a3_2) {
                var_a3_2 = (s16) arg0->width;
            }
            arg3 = var_a3_2;
            func_16001AD0(arg0->dest + arg0->len, &var_s1[arg4], (u32) var_a3_2);
            arg0->len = arg0->len + arg3;
            arg0->unk18 = (s32) (arg0->width - arg3);
        }
    } else {
        s16 var_t0_2;
        s32 var_v0_2;
        s32 temp_t9;

        var_t0_2 = arg4;
        if ((arg1 == 'g') || (arg1 == 'G')) {
            var_v0_2 = arg0->width;
            if (var_a3 < var_v0_2) {
                arg0->width = (s32) var_a3;
                var_v0_2 = (s32) var_a3;
            }
            temp_t9 = var_v0_2 - 1;
            arg0->width = temp_t9;
            if (temp_t9 < 0) {
                arg0->width = 0;
            }
            arg1 = (arg1 == 'g') ? 'e' : 'E';
        }
        arg0->dest[arg0->len] = *var_s1;
        arg0->len = arg0->len + 1;
        if ((arg0->width > 0) || (arg0->flags & 8)) {
            arg0->dest[arg0->len] = '.';
            arg0->len = arg0->len + 1;
        }
        if ((s16) arg0->width > 0) {
            s16 var_a3_3 = var_a3 - 1;
            if ((s16) arg0->width < var_a3_3) {
                var_a3_3 = (s16) arg0->width;
            }
            arg3 = var_a3_3;
            func_16001AD0(arg0->dest + arg0->len, var_s1 + 1, (u32) var_a3_3);
            var_t0_2 = arg4;
            arg0->len = arg0->len + arg3;
            arg0->unk18 = (s32) (arg0->width - arg3);
        }
        ep = arg0->dest + arg0->len + 1;
        ep[-1] = arg1;
        if (var_t0_2 >= 0) {
            ep[0] = '+';
            p = ep + 1;
        } else {
            ep[0] = '-';
            p = ep + 1;
            var_t0_2 *= -1;
        }
        e = var_t0_2;
        if (e >= 100) {
            if (e >= 1000) {
                *p = (u8) (e / 1000 + '0');
                e = (s16) (e % 1000);
                p += 1;
            }
            *p = (u8) (e / 100 + '0');
            e = (s16) (e % 100);
            p += 1;
        }
        p[0] = (u8) (e / 10 + '0');
        p[1] = (u8) ((s16) (e % 10) + '0');
        arg0->unk1C = (s32) (((p + 2) - arg0->dest) - arg0->len);
    }
    if ((arg0->flags & 0x14) == 0x10) {
        temp_v1 = arg0->unk28;
        temp_v0 = arg0->unkC + arg0->len + arg0->unk18 + arg0->unk1C + arg0->unk20;
        if (temp_v0 < temp_v1) {
            arg0->padWidth = (s32) (temp_v1 - temp_v0);
        }
    }
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_160033A8(struct262 *arg0, s32 arg1) {
    u8 buf[24];
    u8 *table;
    s32 radix;
    s32 pos;
    s64 value;
    u64 uvalue;
    lldiv_t qr;
    s32 total;
    s32 extra;

    if ((arg1 & 0xFF) == 'X') {
        table = &D_16003CCC;
    } else {
        table = &D_16003CB8;
    }
    pos = 0x18;
    if ((arg1 & 0xFF) == 'o') {
        radix = 8;
    } else {
        radix = 0x10;
        if ((arg1 & 0xFF) != 'x' && (arg1 & 0xFF) != 'X') {
            radix = 0xA;
        }
    }
    value = arg0->num.value;
    if (((arg1 & 0xFF) == 'd' || (arg1 & 0xFF) == 'i') && value < 0) {
        value = -value;
    }
    if ((value != 0) || (arg0->width != 0)) {
        pos = 0x17;
        uvalue = value;
        buf[0x17] = table[uvalue % (u32) radix];
    }
    uvalue = value;
    value = uvalue / (u32) radix;
    arg0->num.value = value;
    if ((value > 0) && (pos > 0)) {
        do {
            qr = lldiv(value, radix);
            pos -= 1;
            arg0->num.value = qr.quot;
            buf[pos] = table[(u32) qr.rem];
            value = arg0->num.value;
        } while ((value > 0) && (pos > 0));
    }
    total = 0x18 - pos;
    arg0->len = total;
    func_16001AD0(arg0->dest, &buf[pos], total);
    if (arg0->len < arg0->width) {
        arg0->padWidth = arg0->width - arg0->len;
    }
    if ((arg0->width < 0) && ((arg0->flags & 0x14) == 0x10)) {
        extra = ((arg0->unk28 - arg0->unkC) - arg0->padWidth) - arg0->len;
        if (extra > 0) {
            arg0->padWidth = arg0->padWidth + extra;
        }
    }
}
