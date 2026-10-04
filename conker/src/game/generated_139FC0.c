#include <ultra64.h>
extern u8 D_800D9ED8[];
extern s8 D_800BC448[];
extern u16 D_80091D20[];
extern s32 D_800D9F58;
extern s32 D_800D9F5C;
extern u8 D_800D9F68[];
extern u8 D_1A37E0;
void func_10004074(void *);
void *allocate_memory(s32, s32, s32, s32);
void *func_10003C6C(s32, s32, s32, s32, s32);
s32 func_10004514(s32, void *, u32, s32);
s32 func_10006240(void *, void *, u32);
s32 func_1510D374(s32);
u32 func_1510D0EC(s32, s32 *, s32, s32);
extern u32 D_800B0E58[];
extern u16 D_800B87A0[];
extern u8 D_800DBDBA;
extern u32 D_8003809C;
extern u8 D_800D9F60;
extern s32 D_8003C8E0;
extern s32 D_800DBDBC;
void func_150AD770(void);
void func_1510D694(s32 arg0);
void func_1510D720(s32 arg0);

/* Non-matching placeholders for the text-only asm slice asm/139FC0.s. */

s32 func_1510CB10() {
    return 0;
}

s32 func_1510CDB8() {
    return 0;
}

s32 func_1510CE60(void *data, s32 unresolvedOnly, s32 retain, s32 priority, s32 *output) {
    u8 tracked[0x3CB];
    s8 *command = data;
    s32 i;
    s32 count;
    s32 failed = 0;
    s32 adjustment;
    s32 extent;
    u32 resource;
    /* Retail retains these scratch values between texture commands. */
    u32 address;
    s16 *list;
    s32 id;
    u32 bit;

    if (output != NULL) {
        for (i = 0; i < (s32)sizeof(tracked); i++) {
            tracked[i] = 0;
        }
        count = 0;
    }
    while (*command != -0x21) {
        if (*command == -3) {
            resource = *(u32 *)(command + 4);
            if ((!unresolvedOnly || (resource & 0xFF000000) == 0)
                && (resource & 0xFF000000) < 0x06000000) {
                adjustment = (s32)resource >> 22;
                if ((resource & 0x0F000000) == 0) {
                    resource &= 0xF03FFFFF;
                    address = func_1510D0EC(resource, &extent, priority, retain);
                    *(u32 *)(command + 4) = address;
                    if (output != NULL) {
                        bit = 1 << (resource & 7);
                        if ((tracked[resource >> 3] & bit) == 0) {
                            tracked[resource >> 3] |= bit;
                            count++;
                        }
                    }
                } else {
                    adjustment = 0;
                }
                if (address == 0x80000000) {
                    failed = 1;
                }
                if (adjustment != 0) {
                    resource = *(u32 *)(command + 4);
                    if (adjustment & 1) {
                        resource += (u32)extent - 0x200;
                        *(u32 *)(command + 4) = resource;
                    } else if (adjustment & 2) {
                        resource += (u32)extent - 0x20;
                        *(u32 *)(command + 4) = resource;
                    }
                    *(u32 *)(command + 4) = resource | ((adjustment & 0x3C) << 22);
                }
            }
        }
        command += 8;
    }
    if (output != NULL) {
        list = allocate_memory((count + 1) * 2, 1, 0, 2);
        *output = (s32)list;
        if (list != NULL) {
            *list++ = count;
            id = 0;
            bit = 1;
            i = 0;
            while (i != count) {
                if (tracked[id >> 3] & bit) {
                    list[i++] = id;
                }
                if (bit == 0x80) {
                    bit = 1;
                } else {
                    bit <<= 1;
                }
                id++;
            }
        }
    }
    return failed == 0;
}

u32 func_1510D0EC(s32 id, s32 *extent, s32 priority, s32 retain) {
    u32 size;
    u32 source;
    u32 skip;
    u32 amount;
    u32 address;
    u8 *compressed;
    void *expanded;

    if (id < D_800D9F58) {
        D_800D9F58 = id;
    }
    if (id > D_800D9F5C) {
        D_800D9F5C = id;
    }
    if (id < 0 || id >= 0x1E52) {
        return 0x80000000;
    }
    size = D_80091D20[id];
    if (size == 0) {
        D_800B0E58[id] = 0x80000000;
    } else if (D_800B0E58[id] == 0xFFFFFFFF) {
        D_800DBDBA = 5;
        if (priority == 0x3F) {
            priority = 0x3E;
        }
        source = func_1510D374(id);
        skip = source & 1;
        source -= skip;
        amount = size + skip;
        if (amount & 1) {
            amount++;
        }
        amount = (amount + 15) & ~0xF;
        compressed = func_10003C6C(amount, 1, 2, 1, 2);
        if (compressed == NULL) {
            return 0x80000000;
        }
        func_10004514(source, compressed, amount, 1);
        expanded = func_10003C6C(D_800B87A0[id], 1, 1, 0, 2);
        if (expanded == NULL) {
            func_10004074(compressed);
            return 0x80000000;
        }
        func_10006240(compressed + skip, expanded, D_8003809C);
        func_10004074(compressed);
        D_800B0E58[id] = (u32)expanded;
        D_800D9F68[id] = 0;
    }
    if (extent != NULL) {
        *extent = D_800B87A0[id];
    }
    address = D_800B0E58[id];
    if (D_800BC448[id] < priority) {
        D_800BC448[id] = priority;
    }
    if (retain != 0 && D_800D9F68[id] < 0xFF) {
        D_800D9F68[id]++;
    }
    return address;
}

s32 func_1510D374(s32 arg0) {
    s32 offset = (s32)&D_1A37E0;
    s32 i;

    for (i = 0; i < arg0; i++) {
        offset += D_80091D20[i];
    }

    return offset;
}

void func_1510D404(void) {
    s32 last = D_800D9F5C;
    s32 first;
    s32 i;
    s8 state;
    u32 *entry;
    u32 temporary;

    if (last == -1) {
        return;
    }
    if (D_800DBDBA == 0) {
        if (D_800D9F60 != 0) {
            return;
        }
    } else {
        D_800DBDBA--;
    }
    first = D_800D9F58;
    D_800D9F58 = 0xFFFF;
    D_800D9F5C = -1;
    if (first < 0 || last >= 0x1E53) {
        D_8003C8E0 = 0x0C000046;
        func_150AD770();
    }
    D_800DBDBC = -1;
    for (i = first; i <= last; i++) {
        state = D_800BC448[i];
        if (state != 0) {
            if (state < 4) {
                D_800BC448[i] = state - 1;
                if (D_800BC448[i] == 0) {
                    D_800DBDBC = i;
                    func_10004074((void *)D_800B0E58[i]);
                    D_800B0E58[i] = 0xFFFFFFFF;
                } else {
                    if (i < D_800D9F58) {
                        D_800D9F58 = i;
                    }
                    if (i > D_800D9F5C) {
                        D_800D9F5C = i;
                    }
                }
            } else if (state & 0x40) {
                entry = (u32 *)D_800B0E58[i];
                temporary = entry[0];
                func_10006240((void *)(temporary + entry[1]), entry, D_8003809C);
                func_10004074((void *)temporary);
                D_800BC448[i] &= ~0x40;
                if (i < D_800D9F58) {
                    D_800D9F58 = i;
                }
                if (i > D_800D9F5C) {
                    D_800D9F5C = i;
                }
            }
        }
    }
    D_800DBDBC = -2;
}

void func_1510D608(s32 arg0, s32 arg1) {
    s8 *temp_v0 = D_800BC448 + arg0;
    s8 temp_v1 = *temp_v0;

    if (temp_v1 != 0) {
        *temp_v0 = (temp_v1 & 0x40) | arg1;
    }
}

void func_1510D630(s16 *arg0) {
    s16 *allocation = arg0;
    s32 count = allocation[0];
    s16 *entry = allocation + 1;

    if (count > 0) {
        s16 *end = allocation + count + 1;

        do {
            func_1510D694(*entry);
            entry++;
        } while (end != entry);
    }

    func_10004074(allocation);
}

/* Decrement an indexed activity count and finalize its zero transition. */
void func_1510D694(s32 arg0) {
    u8 *entry;
    u8 value;

    if (D_800BC448[arg0] != 0) {
        entry = &D_800D9F68[arg0];
        value = *entry;
        if (value != 0) {
            *entry = value - 1;
            if (*entry == 0) {
                if (arg0 < D_800D9F58) {
                    D_800D9F58 = arg0;
                }
                if (arg0 > D_800D9F5C) {
                    D_800D9F5C = arg0;
                }
                func_1510D608(arg0, 3);
            }
        }
    }
}

/* Finalize the corresponding countdown transition into state two. */
void func_1510D720(s32 arg0) {
    u8 *entry;
    u8 value;

    if (D_800BC448[arg0] != 0) {
        entry = &D_800D9F68[arg0];
        value = *entry;
        if (value != 0) {
            *entry = value - 1;
            if (*entry == 0) {
                if (arg0 < D_800D9F58) {
                    D_800D9F58 = arg0;
                }
                if (arg0 > D_800D9F5C) {
                    D_800D9F5C = arg0;
                }
                func_1510D608(arg0, 2);
            }
        }
    }
}

void func_1510D7AC(s32 arg0) {
    s8 *priority = &D_800BC448[arg0];
    s8 state = *priority;
    u8 *activity;
    s32 count;
    u32 *cache;

    if (state != 0) {
        activity = &D_800D9F68[arg0];
        count = *activity;
        if (count != 0) {
            *activity = count - 1;
            if (*activity == 0) {
                if (state & 0x40) {
                    func_10004074((void *)*(u32 *)D_800B0E58[arg0]);
                }
                cache = &D_800B0E58[arg0];
                func_10004074((void *)*cache);
                *cache = 0xFFFFFFFF;
                *priority = 0;
            }
        }
    }
}

extern u8 D_800D9ED0;

void func_1510D864(void) {
    D_800D9ED0 = 0;
}

void func_1510D874(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    s32 temp_v0 = D_800D9ED0;

    if (temp_v0 < 8) {
        u8 *slot = D_800D9ED8 + temp_v0 * 16;

        *(s32 *) slot = arg0;
        *(s32 *) (slot + 4) = arg1;
        *(s32 *) (slot + 8) = arg2;
        *(slot + 0xC) = arg3;
        *(slot + 0xD) = arg4;
        D_800D9ED0 = temp_v0 + 1;
    }
}

s32 func_1510D8C0() {
    return 0;
}
