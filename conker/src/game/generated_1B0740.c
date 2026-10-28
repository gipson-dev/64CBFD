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

extern u8 D_800DDF68[];

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

s32 func_15183C28() {
    return 0;
}

s32 func_15183D28() {
    return 0;
}

s32 func_15184118(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x31C);

    if ((temp_v0 != 0) && (*(temp_v0 + 0x57) != 0)) {
        return 1;
    }
    return 0;
}
