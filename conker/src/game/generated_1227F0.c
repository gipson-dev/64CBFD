#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1227F0.s. */

typedef struct { u32 indices[17]; } RecordReloadPreset1227F0;
typedef struct { u8 bytes[0x34]; } ReloadRecord1227F0;
extern RecordReloadPreset1227F0 D_800A1AB0;
extern ReloadRecord1227F0 *D_800D3098;
void func_151C970C(s32 mode, s32 recordAddress);
void func_1515F170(s32 category, u8 enabled);

/* Reload the seventeen preset records, then enable category nine. */
void func_150F5340(void) {
    u8 index;
    RecordReloadPreset1227F0 preset = D_800A1AB0;

    for (index = 0; index < 17; index++) {
        func_151C970C(1, (s32)&D_800D3098[preset.indices[index]]);
    }
    func_1515F170(9, 1);
}
