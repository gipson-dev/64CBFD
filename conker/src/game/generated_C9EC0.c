#include <ultra64.h>
extern s32 D_8008743C[];
extern u8 *D_800D2FB0;
extern u8 D_800D2E70[];

/* Non-matching placeholders for the text-only asm slice asm/C9EC0.s. */

void func_1509CCB4();
void func_1509CE64(u16 *dependency, void (*visit)(s32));

extern u8 D_8008743A[];

typedef struct {
    s32 field0;
    s32 field4;
    u16 field8;
    u8 padA[0xA];
} GeneratedC9EC0Entry;

extern GeneratedC9EC0Entry D_80087430[];
extern GeneratedC9EC0Entry D_80088420[];

s32 func_1509CA10(register s32 arg0) {
    return D_80087430[arg0].field0;
}

u16 func_1509CA30(register s32 arg0) {
    return D_80087430[arg0].field8;
}

s32 func_1509CA50(s32 arg0) {
    return *(u16 *) (D_8008743A + arg0 * 0x14) & 0xFFF;
}

s32 func_1509CA78(register s32 arg0) {
    return D_80087430[arg0].field4;
}

/* Find the first active record whose masked key equals the requested value. */
s32 func_1509CA98(u32 key) {
    s32 index = 0;
    GeneratedC9EC0Entry *entry = D_80087430;

    do {
        if (entry[0].field0 != 0 &&
            ((u32)entry[0].field4 & 0x1FFFFFFF) + 1 == key) {
            return index;
        }
        if (entry[1].field0 != 0 &&
            ((u32)entry[1].field4 & 0x1FFFFFFF) + 1 == key) {
            return index + 1;
        }
        if (entry[2].field0 != 0 &&
            ((u32)entry[2].field4 & 0x1FFFFFFF) + 1 == key) {
            return index + 2;
        }
        if (entry[3].field0 != 0 &&
            ((u32)entry[3].field4 & 0x1FFFFFFF) + 1 == key) {
            return index + 3;
        }
        index += 4;
        entry += 4;
    } while (index != 204);
    return 204;
}

s32 func_1509CB68(void) {
    GeneratedC9EC0Entry *end = D_80088420;
    s32 count = 0;
    GeneratedC9EC0Entry *entry = D_80087430;

    do {
        if (entry[0].field0 != 0) {
            count++;
        }
        if (entry[1].field0 != 0) {
            count++;
        }
        if (entry[2].field0 != 0) {
            count++;
        }
        if (entry[3].field0 != 0) {
            count++;
        }
        entry += 4;
    } while (entry != end);

    return count;
}

extern u8 *D_800D2E4C;

/* Require every dependency to be recursively ready and marked active. */
s32 func_1509CBD4(s32 index) {
    u16 *initial = *(u16 **)((u8 *)D_8008743C + index * 20);
    u16 *dependency;
    s32 child;
    s32 result;
    if ((child = *initial) != 0xFFFF) {
        dependency = initial;
        do {
            result = func_1509CBD4(child);
            child = *dependency;
            if (!(D_800D2E4C[child >> 3] & (1 << (child & 7))) || result == 0) { return 0; }
            child = *++dependency;
        } while (child != 0xFFFF);
    }
    return 1;
}

void func_1509CC94(s32 arg0) {
    func_1509CCB4(arg0);
}

void func_1509CCB4(s32 arg0) {
    func_1509CE64(*(u16 **) ((u8 *) D_8008743C + arg0 * 20), func_1509CCB4);
}

typedef struct {u16 *entries;u8 reserved[16];} DependencyActivationRow;
extern DependencyActivationRow D_80087440[];
extern u8 *D_800D2E4C;
extern u8 D_800D2E70[];
void func_1509CCB4(s32);
/* Mark every listed dependency active and count newly activated callbacks. */
s32 func_1509CCF4(s32 index) {
    u16 *entry = D_80087440[index].entries;
    s32 resource;
    s32 count = 0;
    if ((resource = *entry) != 0xFFFF) {
        do {
            D_800D2E4C[resource >> 3] |= 1 << (resource & 7);
            if (D_800D2E70[*entry] != 3) {
                D_800D2E70[*entry] = 3;
                func_1509CCB4(*entry);
                count++;
            }
            resource = *++entry;
        } while (resource != 0xFFFF);
    }
    return count;
}

// Matched with guarded loop-invariant allocation normalization.
void func_1509CDDC(s32 arg0) {
    s32 changes;
    s32 index;
    u8 *state;

    func_1509CCF4(arg0);
    do {
        changes = 0;
        state = D_800D2E70;
        index = 0;
        do {
            if (*state == 3) {
                changes += func_1509CCF4(index);
            }
            index++;
            state++;
        } while (index != 0xCC);
    } while (changes != 0);
}

/* Visit a sentinel-terminated dependency list, then mark each live entry. */
void func_1509CE64(u16 *dependency, void (*visit)(s32)) {
    s32 index;
    u16 *cursor;
    if (*dependency != 0xFFFF) {
        index = *dependency;
        cursor = dependency;
        do {
            visit(index);
            D_800D2E70[*cursor] = 3;
            index = *cursor++;
            D_800D2E4C[index >> 3] |= 1 << (index & 7);
            index = *cursor;
        } while (index != 0xFFFF);
    }
}

s32 func_1509CF28() {
    return 0;
}

// Matched with guarded call-argument lifetime normalization.
void func_1509D054(void) {
    u8 *temp_v0 = D_800D2FB0;

    if (temp_v0 != 0) {
        func_10004074(temp_v0);
        D_800D2FB0 = 0;
    }
}

s32 func_1509D08C() {
    return 0;
}

s32 func_1509D180() {
    return 0;
}

s32 func_1509D780() {
    return 0;
}

s32 func_1509D8FC() {
    return 0;
}

s32 func_1509DBBC() {
    return 0;
}
