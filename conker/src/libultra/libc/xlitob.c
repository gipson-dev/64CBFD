#include "stdlib.h"
#include "string.h"

#define BUFF_LEN 24
#define FLAGS_MINUS 4
#define FLAGS_ZERO 16

typedef struct {
    union {
        long long ll;
        double ld;
    } v;
    unsigned char *s;
    int n0;
    int nz0;
    int n1;
    int nz1;
    int n2;
    int nz2;
    int prec;
    int width;
    size_t nchar;
    unsigned int flags;
    char qual;
} _Pft;

extern unsigned char D_8002BD30[];
extern unsigned char D_8002BD44[];

void _Litob(_Pft *px, char code) {
    unsigned char buff[BUFF_LEN];
    unsigned char *digs;
    int base;
    int i;
    unsigned long long value;

    digs = (code == 'X') ? D_8002BD44 : D_8002BD30;
    base = (code == 'o') ? 8 : ((code != 'x' && code != 'X') ? 10 : 16);
    i = BUFF_LEN;
    value = px->v.ll;

    if ((code == 'd' || code == 'i') && px->v.ll < 0) {
        value = -value;
    }

    if (value != 0 || px->prec != 0) {
        buff[--i] = digs[value % base];
    }

    px->v.ll = value / base;
    while (px->v.ll > 0 && i > 0) {
        lldiv_t qr = lldiv(px->v.ll, base);

        px->v.ll = qr.quot;
        buff[--i] = digs[qr.rem];
    }

    px->n1 = BUFF_LEN - i;
    memcpy(px->s, &buff[i], px->n1);

    if (px->n1 < px->prec) {
        px->nz0 = px->prec - px->n1;
    }

    if (px->prec < 0 && (px->flags & (FLAGS_ZERO | FLAGS_MINUS)) == FLAGS_ZERO) {
        i = px->width - px->n0 - px->nz0 - px->n1;
        if (i > 0) {
            px->nz0 += i;
        }
    }
}
