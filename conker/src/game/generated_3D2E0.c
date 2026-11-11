#include <ultra64.h>

typedef struct { u8 group; u8 pad1; s8 marker; u8 pad3; s16 choice; s16 previous; s16 next; } Entry10;
extern Entry10 *D_800BE4E0;
void *allocate_memory(s32,s32,s32,s32);
u32 func_150ADA20(void);
void func_150C851C(s32);


extern s32 D_800B0E00,D_800B0E04,D_800902DC;
extern u8 *D_80088870;
void *func_15195AA8(s32,s32,s32,s32,s32,s32,s32,s32);
u8 *func_151491F4(s32,s32,s32,s32,s32,s32,s32,s32);
u8 *func_15149130(s32,s32,s32,s32,s32,s32,s32,s32,s32);

extern s32 D_800917B8;


/* Initialize ten table entries and sync their previous values. */
void func_1500FE30(void) {
    s32 i;
    D_800BE4E0 = allocate_memory(100, 1, 0, 0);
    bzero(D_800BE4E0, 100);
    for (i = 0; i < 10; i++) {
        D_800BE4E0[i].group = i / 5;
        D_800BE4E0[i].marker = -1;
        D_800BE4E0[i].choice = func_150ADA20() % 5;
    }
    func_150C851C(100);
    D_800BE4E0[0].previous = D_800BE4E0[0].next;
    D_800BE4E0[1].previous = D_800BE4E0[1].next;
    for (i = 2; i < 10; i += 4) {
        D_800BE4E0[i].previous = D_800BE4E0[i].next;
        D_800BE4E0[i + 1].previous = D_800BE4E0[i + 1].next;
        D_800BE4E0[i + 2].previous = D_800BE4E0[i + 2].next;
        D_800BE4E0[i + 3].previous = D_800BE4E0[i + 3].next;
    }
}

void func_1500FF9C(void) {
    func_1510C4AC(D_800917B8, 0, 0xAD, 0x75);
}

/* Initialize callback state and create two optional records. */
void func_1500FFCC(void) {
    f32 first;
    f32 pair[3];
    u8 *record;
    func_15195AA8(D_800B0E00, D_800902DC, 1, -1, 0, 0, 0, -4);
    func_15195AA8(D_800B0E04, D_800902DC, 1, -1, 0, 1, 0, -4);
    func_1500FE30();
    func_1500FF9C();
    first = 0.0f;
    record = func_151491F4(300, -1, 18, 0, 14, 4, 255, 0);
    if (record != 0) memcpy(record + 0x28, &first, 4);
    pair[0] = 0.0f;
    pair[1] = 0.0f;
    D_80088870 = func_15149130(300, -1, 23, -1, 0, 20, 8, 255, 1);
    if (D_80088870 != 0) memcpy(D_80088870 + 0x28, pair, 8);
}
