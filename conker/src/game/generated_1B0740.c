#include <ultra64.h>

typedef struct {
    s32 words[5];
} Record15183974;

extern Record15183974 D_800DDE80[11];
extern u8 D_800A72D0[];
extern u32 D_800DDF78[];
void func_15183ACC(s32 index);

/* Non-matching placeholders for the text-only asm slice asm/1B0740.s. */

s32 func_15183290() {
    return 0;
}

extern u8 D_800DDF69[];
void *func_1502B6BC(s32 *size, s32 count, s32 *relocated, s32 depth, ...);

/* Load the adjacent record on demand and copy its owner fields. */
void func_151838B0(s32 index) {
    s32 *result;

    if (D_800DDE80[index].words[0] == 0) {
        func_15183ACC(index);
    }
    if (D_800DDE80[index + 1].words[0] == 0) {
        result = func_1502B6BC(0, 0, 0, 2, 9, index + 0xAE);
        if (result != NULL) {
            D_800DDE80[index + 1].words[0] = (s32)result;
            D_800DDE80[index + 1].words[1] = result[0];
            D_800DDE80[index + 1].words[2] = result[2];
            D_800DDE80[index + 1].words[3] = D_800DDE80[index].words[3];
            D_800DDE80[index + 1].words[4] = 0;
            D_800DDF69[index] = 1;
        }
    }
}

void func_15183974(s32 arg0) {
    Record15183974 *record;

    record = &D_800DDE80[arg0];

    if (record[0].words[0] == 0) {
        func_15183ACC(arg0);
    }
    if (record[1].words[0] == 0) {
        func_15183ACC(arg0 + 1);
        record[1].words[3] = record[0].words[3];
    }
}

extern s8 D_800DDF68[];

/* Load a second record after its prerequisite record becomes available. */
void func_151839F0(s32 requiredIndex, s32 index) {
    s32 *result;

    if (D_800DDE80[requiredIndex].words[0] == 0) {
        func_15183ACC(requiredIndex);
    }
    if (D_800DDE80[requiredIndex].words[0] != 0) {
        if (D_800DDE80[index].words[0] == 0) {
            result = func_1502B6BC(0, 0, 0, 2, 9, index + 0xAD);
            if (result != NULL) {
                D_800DDE80[index].words[0] = (s32)result;
                D_800DDE80[index].words[1] = result[0];
                D_800DDE80[index].words[2] = result[2];
                D_800DDE80[index].words[3] = result[6];
                D_800DDE80[index].words[4] = 0;
                D_800DDF68[index] = 1;
            }
        }
    }
}

s32 func_1510CE60(void *data, s32 unresolvedOnly, s32 retain, s32 priority, s32 *output);

/* Load an empty record and prepare its referenced graphics resources. */
void func_15183ACC(s32 index) {
    s32 *result;

    if (D_800DDE80[index].words[0] == 0) {
        result = func_1502B6BC(0, 0, 0, 2, 9, index + 0xAD);
        if (result != NULL) {
            D_800DDE80[index].words[0] = (s32)result;
            D_800DDE80[index].words[1] = result[0];
            D_800DDE80[index].words[2] = result[2];
            D_800DDE80[index].words[3] = result[6];
            D_800DDF78[index] = result[4];
            func_1510CE60((void *)D_800DDF78[index], 0, 1, 0x3E,
                          &D_800DDE80[index].words[4]);
            D_800DDF68[index] = 1;
        }
    }
}

Gfx *func_15183BA4(Gfx *dl, s32 selector, s16 arg2, s16 arg3) {
    s32 index;
    s32 i;
    u32 *entry;

    index = -1;
    for (i = 0; i < 11; i++) {
        if (selector == D_800A72D0[i]) {
            index = i;
            break;
        }
    }

    if (index != -1) {
        entry = &D_800DDF78[index];
        if (*entry != 0) {
            gSPDisplayList(dl++, *entry);
        }
    }
    return dl;
}

extern s8 D_800DDF70;
extern s8 D_800DDF71;
extern s32 D_800DDF20;
extern u32 D_800DDF98;
void func_1510D630(s16 *allocation);
void func_10004074(void *allocation);

/* Release a record's resources and its shared backing allocation when ready. */
void func_15183C28(s32 index) {
    s16 *resources;

    resources = (s16 *)D_800DDE80[index].words[4];
    if (resources != 0) {
        func_1510D630(resources);
        D_800DDE80[index].words[4] = 0;
    }
    if (index == 8) {
        if (D_800DDF71 != -2) {
            return;
        }
    } else if (index == 9) {
        if (D_800DDF70 == -2 && D_800DDF20 != 0) {
            func_10004074((void *)D_800DDF20);
            D_800DDF20 = 0;
            D_800DDF98 = 0;
        }
    }
    if (D_800DDE80[index].words[0] != 0) {
        func_10004074((void *)D_800DDE80[index].words[0]);
        D_800DDE80[index].words[0] = 0;
        D_800DDF78[index] = 0;
    }
}

typedef struct {
    u8 unused00[0x18];
    f32 position[3];
    f32 phase;
    f32 extentA;
    f32 extentB;
    f32 scale;
    s32 unused34;
} RecordUpdate15183D28;
extern RecordUpdate15183D28 D_8008D0B0[];
extern RecordUpdate15183D28 D_8008D318[];
extern u8 *D_8008D3C0[];
extern u8 D_800A72E8[];
extern u8 D_800DDF60[];
extern u8 D_800DDF64[];
extern s32 D_800BE9E4;
void func_15165C80(f32 *position, void *vertices, f32 scale, f32 *phase,
                   f32 extentA, f32 extentB, u8 *indices, u8 count);
void func_1517725C(u8 index);
void func_15179DB0(u8 index);
void func_15183C28(s32 index);

/* Update active record geometry, release expired records, and age their flags. */
void func_15183D28(void) {
    s32 age;
    s32 i;
    s32 remaining;
    u8 *timer;
    s8 *flags;
    RecordUpdate15183D28 *update;

    for (i = 0, flags = D_800DDF68; ; ) {
        if (*flags >= -1) {
            if (D_800DDE80[i].words[0] == 0 || D_800DDF78[i] == 0) {
                *flags = -2;
            }
        }
        i++; flags++;
        if (i >= 11) break;
    }
    /* Four byte timers use the current signed frame-tick decrement. */
    timer = D_800DDF60;
    do {
        if (*timer > 0) {
            remaining = *timer - D_800BE9E4;
            if (remaining < 0) {
                remaining = 0;
            }
            *timer = remaining;
        }
        timer++;
    } while (timer < D_800DDF64);
    for (i = 0, flags = D_800DDF68; i < 7; i++, flags++) {
        if (*flags == 1) {
            update = &D_8008D0B0[i];
            func_15165C80(update->position, (void *)D_800DDE80[i].words[2],
                update->scale, &update->phase, update->extentA, update->extentB,
                D_8008D3C0[i], D_800A72E8[i]);
        }
    }
    /* Rows 2..4 have a second vertex stream in record word 1. */
    for (i = 2, flags = D_800DDF68 + 2; i < 5; i++, flags++) {
        if (*flags == 1) {
            update = &D_8008D318[i - 2];
            func_15165C80(update->position, (void *)D_800DDE80[i].words[1],
                update->scale, &update->phase, update->extentA, update->extentB,
                D_8008D3C0[i], D_800A72E8[i]);
        }
    }
    if (D_800DDF68[7] == 1) {
        func_1517725C(7);
    }
    for (i = 0, flags = D_800DDF68; i < 2; i++, flags++) {
        if (flags[8] == 1) {
            func_15179DB0(i + 8);
        }
    }
    /* Reread after the providers above: they can change the live flags. */
    if (D_800DDF68[7] == 1) {
        D_800DDF68[10] = 1;
    }
    for (i = 0, flags = D_800DDF68; i < 11; i++, flags++) {
        if (*flags == -2 && D_800DDE80[i].words[0] != 0) {
            func_15183C28(i);
        }
    }
    /* Positive flags become 0, then age through -1 to expired (-2). */
    for (age = 0; age < 11; age++) {
        if (D_800DDF68[age] > 0) { D_800DDF68[age] = 0; } else if (D_800DDF68[age] >= -1) { (D_800DDF68[age])--; }
    }
}

s32 func_15184118(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x31C);

    if ((temp_v0 != 0) && (*(temp_v0 + 0x57) != 0)) {
        return 1;
    }
    return 0;
}
