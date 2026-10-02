#include <ultra64.h>
#include <n_libaudio.h>

#include "variables.h"
#include "n_synthInternals.h"

typedef Acmd *(*AuxBusPull)(s32 sampleOffset, Acmd *cmdList, s32 bus);

s32 func_151F2E88(s32 arg0, Acmd **arg1);
void func_1001CF38(struct139 *arg0, f32 arg1);

Acmd *func_1001FB40(s32 sampleOffset, Acmd *cmdList) {
    Acmd *current;
    s32 i;
    s32 selectedBus;

    current = cmdList;
    if ((D_800E0E04 == 0) || (func_151F2E88(0xB8, &current) == 0)) {
        aClearBuffer(current++, 0x04E0, 0x02E0);
        aClearBuffer(current++, 0x07C0, 0x02E0);
    }

    selectedBus = 0;
    for (i = 1; i < n_syn->maxAuxBusses; i++) {
        if (((struct auxbus44 *)n_syn->auxBus[i].fx_array[7])->unk02 > 0) {
            selectedBus = i;
        }
    }

    for (i = 0; i < n_syn->maxAuxBusses; i++, selectedBus++) {
        if (selectedBus >= n_syn->maxAuxBusses) {
            selectedBus = 0;
        }

        if (i != 0) {
            aClearBuffer(current++, 0x07C0, 0x02E0);
        }

        current = ((AuxBusPull)n_syn->mainBus->filter.handler)(
            sampleOffset, current, selectedBus);

        if (D_800428C4[selectedBus] != 0) {
            if (D_800428C6[selectedBus] != 0) {
                aMix(current++, 0, 0x8000, 0x07C0, 0x04E0);
            } else {
                aMix(current++, 0, 0x7FFF, 0x07C0, 0x0650);
            }
        } else {
            if (D_800428C6[selectedBus] != 0) {
                aMix(current++, 0, 0x8000, 0x07C0, 0x0650);
            } else {
                aMix(current++, 0, 0x7FFF, 0x07C0, 0x0650);
            }
            aMix(current++, 0, 0x7FFF, 0x07C0, 0x04E0);
        }

        if (((struct auxbus44 *)n_syn->auxBus[selectedBus].fx_array[7])
                ->unk02 > 0) {
            struct auxbus44 *effect;

            effect = (struct auxbus44 *)n_syn->auxBus[selectedBus].fx_array[7];
            if (effect->unk28 != 0) {
                func_1001CF38((struct139 *)effect, (f32)n_syn->outputRate);
            }

            aLoadADPCM(current++, 0x20,
                       osVirtualToPhysical((u8 *)effect + 8));
            aPoleFilter(current++, 0, 0x04E0,
                        osVirtualToPhysical(effect->unk2c) & 0xFFFFFF &
                            0xFFFFFF);
            aPoleFilter(current++, 0, 0x0650,
                        osVirtualToPhysical(effect->unk30) & 0xFFFFFF &
                            0xFFFFFF);
            effect->unk28 = 0;
        }
    }

    return current;
}
