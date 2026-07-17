unsigned long long __ull_rshift(unsigned long long value, unsigned long long shift) {
    return value >> shift;
}

unsigned long long __ull_rem(unsigned long long value, unsigned long long divisor) {
    return value % divisor;
}

unsigned long long __ull_div(unsigned long long value, unsigned long long divisor) {
    return value / divisor;
}

unsigned long long __ll_lshift(unsigned long long value, unsigned long long shift) {
    return value << shift;
}

long long __ll_rem(unsigned long long value, long long divisor) {
    return value % divisor;
}

long long __ll_div(long long value, long long divisor) {
    return value / divisor;
}

unsigned long long __ll_mul(unsigned long long left, unsigned long long right) {
    return left * right;
}

void __ull_divremi(unsigned long long *div, unsigned long long *rem, unsigned long long value, unsigned short divisor) {
    *div = value / divisor;
    *rem = value % divisor;
}

long long __ll_mod(long long value, long long divisor) {
    long long rem = value % divisor;

    if ((rem < 0 && divisor > 0) || (rem > 0 && divisor < 0)) {
        rem += divisor;
    }
    return rem;
}

long long __ll_rshift(long long value, long long shift) {
    return value >> shift;
}
