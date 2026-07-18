#include "n_synthInternals.h"

extern f32 D_8002C750;
Acmd *func_1001E530(s32 sampleOffset, Acmd *p);
s32 func_1001E4A0(s16 bus, ALSynConfig *c, ALHeap *hp);

#define N_ALPARAM_SIZE 0x24

/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_synthesizer/n_alSynNew.s. */
void n_alSynNew(ALSynConfig *c)
{
    s32 i;
    s32 j;
    N_PVoice *pv;
    N_PVoice *pvoices;
    ALHeap *hp = c->heap;
    ALParam *params;
    ALParam *paramPtr;
    ALLink *element;
    ALLink *after;

    n_syn->head = NULL;
    n_syn->numPVoices = c->maxPVoices;
    n_syn->curSamples = 0;
    n_syn->paramSamples = 0;
    n_syn->outputRate = c->outputRate;
    n_syn->maxOutSamples = FIXED_SAMPLE;
    n_syn->dma = (ALDMANew)c->dmaproc;
    n_syn->unk28 = c->unk14;
    n_syn->unk2C = c->unk18;
    n_syn->unk30 = c->unk1C;
    n_syn->unk34 = c->unk20;
    n_syn->unk38 = c->unk24;

    if (c->maxFXbusses > 2) {
        n_syn->maxAuxBusses = 2;
    } else if (c->maxFXbusses < 1) {
        n_syn->maxAuxBusses = 1;
    } else {
        n_syn->maxAuxBusses = c->maxFXbusses;
    }

    n_syn->auxBus = (N_ALAuxBus *)alHeapDBAlloc(0, 0, hp, n_syn->maxAuxBusses, sizeof(N_ALAuxBus));

    for (i = 0; i < n_syn->maxAuxBusses; i++) {
        n_syn->auxBus[i].sourceCount = 0;
        n_syn->auxBus[i].maxSources = 0;

        if (c->fxTypes[i]) {
            n_syn->auxBus[i].sources = (N_PVoice **)func_1001E4A0(i, c, hp);
        } else {
            n_syn->auxBus[i].sources = 0;
        }

        n_syn->auxBus[i].fx_array[7] =
            (ALFx *)alHeapDBAlloc(0, 0, hp, 1, sizeof(struct auxbus44));
        ((struct auxbus44 *)n_syn->auxBus[i].fx_array[7])->unk02 = 0;
        ((struct auxbus44 *)n_syn->auxBus[i].fx_array[7])->unk2c =
            alHeapDBAlloc(0, 0, hp, 1, sizeof(POLEF_STATE));
        ((struct auxbus44 *)n_syn->auxBus[i].fx_array[7])->unk30 =
            alHeapDBAlloc(0, 0, hp, 1, sizeof(POLEF_STATE));
    }

    n_syn->mainBus = (N_ALMainBus *)alHeapDBAlloc(0, 0, hp, 1, sizeof(N_ALMainBus));
    n_syn->mainBus->filter.handler = (N_ALCmdHandler)func_1001E530;

    n_syn->pFreeList.next = 0;
    n_syn->pFreeList.prev = 0;
    n_syn->pLameList.next = 0;
    n_syn->pLameList.prev = 0;
    n_syn->pAllocList.next = 0;
    n_syn->pAllocList.prev = 0;

    pvoices = alHeapDBAlloc(0, 0, hp, c->maxPVoices, sizeof(N_PVoice));

    for (i = 0; i < c->maxPVoices; i++) {
        pv = &pvoices[i];

        element = (ALLink *)pv;
        after = &n_syn->pFreeList;
        element->next = after->next;
        element->prev = after;
        if (after->next != 0) {
            after->next->prev = element;
        }
        after->next = element;

        pv->vvoice = 0;
        alN_PVoiceNew(pv, n_syn->dma, hp);
    }

    for (j = 0; j < n_syn->maxAuxBusses; j++) {
        n_syn->auxBus[j].sourceCount = 0;
        n_syn->auxBus[j].maxSources = 0;
    }

    params = alHeapDBAlloc(0, 0, hp, c->maxUpdates, N_ALPARAM_SIZE);
    n_syn->paramList = 0;

    for (i = 0; i < c->maxUpdates; i++) {
        paramPtr = (ALParam *)((i * N_ALPARAM_SIZE) + (s32)params);
        paramPtr->next = n_syn->paramList;
        n_syn->paramList = paramPtr;
    }

    n_syn->heap = hp;
}
// void n_alSynNew(struct07 *arg0) {
//     s32 sp44;
//     // s32 sp40;
//     // void *sp3C;
//     // s32 sp38;
//     s32 sp34;
//     // s32 sp30;
//     // void *sp2C;
//     // void *sp28;
//     // void *sp24;
//     // s32 temp_t2;
//     // s32 temp_t3;
//     // s32 temp_t4;
//     // s32 temp_t9;
//
//     sp34 = arg0->unk28;
//     D_8002BA44->unk0 = 0;
//     D_8002BA44->unk4C = arg0->unk4;
//     D_8002BA44->unk20 = 0;
//     D_8002BA44->unk1C = 0;
//     D_8002BA44->unk54 = arg0->unk2C;
//     D_8002BA44->unk58 = 184;
//     D_8002BA44->unk24 = arg0->unk10;
//     D_8002BA44->unk28 = arg0->unk14;
//     D_8002BA44->unk2C = arg0->unk18;
//     D_8002BA44->unk30 = arg0->unk1C;
//     D_8002BA44->unk34 = arg0->unk20;
//     D_8002BA44->unk38 = arg0->unk24;
//     if (arg0->unkC >= 3) {
//         D_8002BA44->unk50 = 2;
//     } else if (arg0->unkC <= 0) {
//         D_8002BA44->unk50 = 1;
//     } else {
//         D_8002BA44->unk50 = (s32) arg0->unkC;
//     }
//     D_8002BA44->unk48 = alHeapDBAlloc(0, 0, sp34, D_8002BA44->unk50, 0x44);
//     sp44 = 0;
//     if (D_8002BA44->unk50 > 0) {
// loop_6:
//         (D_8002BA44->unk48 + (sp44 * 0x44))->unk14 = 0;
//         (D_8002BA44->unk48 + (sp44 * 0x44))->unk18 = 0;
//         if ((arg0 + sp44)->unk30 != 0) {
//             (D_8002BA44->unk48 + (sp44 * 0x44))->unk1C = func_1001E4A0(sp44, arg0, sp34);
//         } else {
//             (D_8002BA44->unk48 + (sp44 * 0x44))->unk1C = 0;
//         }
//         (D_8002BA44->unk48 + (sp44 * 0x44))->unk40 = alHeapDBAlloc(0, 0, sp34, 1, 0x38);
//         (D_8002BA44->unk48 + (sp44 * 0x44))->unk40->unk2 = (u16)0;
//         (D_8002BA44->unk48 + (sp44 * 0x44))->unk40->unk2C = alHeapDBAlloc(0, 0, sp34, 1, 8);
//         (D_8002BA44->unk48 + (sp44 * 0x44))->unk40->unk30 = alHeapDBAlloc(0, 0, sp34, 1, 8);
//         temp_t4 = sp44 + 1;
//         sp44 = temp_t4;
//         if (temp_t4 < D_8002BA44->unk50) {
//             goto loop_6;
//         }
//     }
//     D_8002BA44->unk44 = alHeapDBAlloc(0, 0, sp34, 1, 0x14);
//     D_8002BA44->unk44->unk4 = (s32)func_1001E530;
//     D_8002BA44->unk4 = 0;
//     D_8002BA44->unk8 = 0;
//     D_8002BA44->unk14 = 0;
//     D_8002BA44->unk18 = 0;
//     D_8002BA44->unkC = 0;
//     D_8002BA44->unk10 = 0;
//     sp38 = alHeapDBAlloc(0, 0, sp34, arg0->unk4, 0xD0);
//     sp44 = 0;
//     if (arg0->unk4 > 0) {
// loop_11:
//         sp3C = (sp44 * 0xD0) + sp38;
//         sp28 = sp3C;
//         sp24 = D_8002BA44 + 4;
//         sp28->unk0 = (s32) *sp24;
//         sp28->unk4 = sp24;
//         if (*sp24 != 0) {
//             (*sp24)->unk4 = sp28;
//         }
//         *sp24 = sp28;
//         sp3C->unk10 = 0;
//         func_1001D6E8(sp3C, D_8002BA44->unk24, sp34);
//         temp_t3 = sp44 + 1;
//         sp44 = temp_t3;
//         if (temp_t3 < arg0->unk4) {
//             goto loop_11;
//         }
//     }
//     sp40 = 0;
//     if (D_8002BA44->unk50 > 0) {
// loop_15:
//         (D_8002BA44->unk48 + (sp40 * 0x44))->unk14 = 0;
//         (D_8002BA44->unk48 + (sp40 * 0x44))->unk18 = 0;
//         temp_t2 = sp40 + 1;
//         sp40 = temp_t2;
//         if (temp_t2 < D_8002BA44->unk50) {
//             goto loop_15;
//         }
//     }
//     sp30 = alHeapDBAlloc(0, 0, sp34, arg0->unk8, 0x24);
//     D_8002BA44->unk40 = 0;
//     sp44 = 0;
//     if (arg0->unk8 > 0) {
// loop_17:
//         sp2C = (sp44 * 0x24) + sp30;
//         *sp2C = (s32) D_8002BA44->unk40;
//         D_8002BA44->unk40 = sp2C;
//         temp_t9 = sp44 + 1;
//         sp44 = temp_t9;
//         if (temp_t9 < arg0->unk8) {
//             goto loop_17;
//         }
//     }
//     D_8002BA44->unk3C = sp34;
// }

/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_synthesizer/n_alAudioFrame.s. */
s32 __n_nextSampleTime(ALPlayer **client);
s32 _n_timeToSamplesNoRound(s32 micros);
Acmd *func_1001FB40(s32 sampleOffset, Acmd *cmdList);

Acmd *n_alAudioFrame(Acmd *cmdList, s32 *cmdLen, s16 *outBuf, s32 outLen) {
    ALPlayer *client;
    Acmd *cmdlEnd = cmdList;
    s32 nOut;
    s16 *lOutBuf = outBuf;
    Acmd *cmdPtr;
    Acmd *cmdPtr2;

    if (n_syn->head == 0) {
        *cmdLen = 0;
        return cmdList;
    }

    for (n_syn->paramSamples = __n_nextSampleTime(&client);
         (u32)(n_syn->paramSamples - n_syn->curSamples) < (u32)outLen;
         n_syn->paramSamples = __n_nextSampleTime(&client)) {
        n_syn->paramSamples &= ~0xf;
        client->samplesLeft += _n_timeToSamplesNoRound((*client->handler)(client));
    }

    n_syn->paramSamples &= ~0xf;

    while (outLen > 0) {
        nOut = MIN(n_syn->maxOutSamples, outLen);

        cmdlEnd = func_1001FB40(n_syn->curSamples, cmdlEnd);
        cmdPtr = cmdlEnd++;
        cmdPtr->words.w0 = 0x0D000000;

        cmdPtr2 = cmdlEnd++;
        cmdPtr2->words.w0 = 0x062E0000;
        cmdPtr2->words.w1 = (u32)lOutBuf;

        outLen -= nOut;
        lOutBuf += nOut << 1;
        n_syn->curSamples += nOut;
    }

    *cmdLen = (s32)(cmdlEnd - cmdList);
    _n_collectPVoices();
    return cmdlEnd;
}

// void *n_alAudioFrame(void *arg0, void *arg1, s32 arg2, u32 arg3) {
//     void *sp3C;
//     void *sp38;
//     s32 sp34;
//     s32 sp30;
//     void *sp2C;
//     void *sp28;
//     s32 temp_t5_2;
//     void *temp_t0;
//     void *temp_t1;
//     void *temp_t2;
//     void *temp_t5;
//     void *temp_t7;
//     void *temp_t8;
//     void *temp_t9;
//
//     sp38 = arg0;
//     sp30 = arg2;
//     if (*D_8002BA44 == 0) {
//         *arg1 = 0;
//         return arg0;
//     }
//     D_8002BA44->unk1C = func_10019A04(&sp3C);
//     temp_t2 = D_8002BA44;
//     if ((u32) (temp_t2->unk1C - temp_t2->unk20) < arg3) {
// loop_3:
//         temp_t7 = D_8002BA44;
//         temp_t7->unk1C = (s32) (temp_t7->unk1C & -0x10);
//         sp3C->unk10 = (s32) (sp3C->unk10 + _n_timeToSamplesNoRound(sp3C->unk8(sp3C)));
//         D_8002BA44->unk1C = func_10019A04(&sp3C);
//         temp_t5 = D_8002BA44;
//         if ((u32) (temp_t5->unk1C - temp_t5->unk20) < arg3) {
//             goto loop_3;
//         }
//     }
//     temp_t9 = D_8002BA44;
//     temp_t9->unk1C = (s32) (temp_t9->unk1C & -0x10);
//     if ((s32) arg3 > 0) {
// loop_5:
//         temp_t5_2 = D_8002BA44->unk58;
//         if (temp_t5_2 < (s32) arg3) {
//             sp34 = temp_t5_2;
//         } else {
//             sp34 = (s32) arg3;
//         }
//         sp38 = func_1001FB40(D_8002BA44->unk20, sp38);
//         temp_t0 = sp38;
//         sp38 = temp_t0 + 8;
//         sp2C = temp_t0;
//         *sp2C = 0xD000000;
//         temp_t1 = sp38;
//         sp38 = temp_t1 + 8;
//         sp28 = temp_t1;
//         sp28->unk0 = 0x62E0000;
//         sp28->unk4 = sp30;
//         arg3 = arg3 - sp34;
//         sp30 = sp30 + (sp34 * 2 * 2);
//         temp_t8 = D_8002BA44;
//         temp_t8->unk20 = (s32) (temp_t8->unk20 + sp34);
//         if ((s32) arg3 > 0) {
//             goto loop_5;
//         }
//     }
//     *arg1 = (s32) ((s32) (sp38 - arg0) >> 3);
//     _collectPVoices();
//     return sp38;
// }

ALParam *__n_allocParam(void) {
    ALParam *update = 0;

    if (n_syn->paramList) {
        update = n_syn->paramList;
        n_syn->paramList = n_syn->paramList->next;
        update->next = 0;
    }
    return update;
}


void _n_freeParam(ALParam *param)
{
  param->next = n_syn->paramList;
  n_syn->paramList = param;
}

void _n_collectPVoices(void) {
    ALLink *dl;
    ALLink *element;
    ALLink *linkElement;
    ALLink *after;
    ALLink *voiceLink;

    while ((dl = n_syn->pLameList.next) != 0) {
        element = dl;

        if (element->next != 0) {
            element->next->prev = element->prev;
        }

        if (element->prev != 0) {
            element->prev->next = element->next;
        }

        linkElement = dl;
        after = &n_syn->pFreeList;
        linkElement->next = after->next;
        linkElement->prev = after;

        if (after->next != 0) {
            after->next->prev = linkElement;
        }

        after->next = linkElement;

        voiceLink = &((N_PVoice *)dl)->voiceLink;

        if (voiceLink->next != 0) {
            voiceLink->next->prev = voiceLink->prev;
        }

        if (voiceLink->prev != 0) {
            voiceLink->prev->next = voiceLink->next;
        }

        ((N_PVoice *)dl)->voiceLink.next = 0;
        ((N_PVoice *)dl)->voiceLink.prev = 0;
    }
}

void _n_freePVoice(N_PVoice *pvoice) {
    N_PVoice *voice = pvoice;
    ALLink *element;
    ALLink *after;

    if (((ALLink *)voice)->next != 0) {
        ((ALLink *)voice)->next->prev = ((ALLink *)voice)->prev;
    }

    if (((ALLink *)voice)->prev != 0) {
        ((ALLink *)voice)->prev->next = ((ALLink *)voice)->next;
    }

    element = (ALLink *)pvoice;
    after = &n_syn->pLameList;
    element->next = after->next;
    element->prev = after;

    if (after->next != 0) {
        after->next->prev = element;
    }

    after->next = element;
}

s32 _n_timeToSamplesNoRound(s32 micros) {
    f32 tmp = (((f32) micros * (f32) n_syn->outputRate) / D_8002C750) + 0.5f; // 1000000.0f
    return (s32) tmp;
}

s32 _n_timeToSamples( s32 micros)
{
  return _n_timeToSamplesNoRound( micros) & ~0xf;
}

s32 __n_nextSampleTime(ALPlayer **client) {
    u32 delta = 0x7FFFFFFF;
    ALPlayer *current;

    *client = NULL;
    for (current = n_syn->head; current != NULL; current = current->next) {
        if ((u32)(current->samplesLeft - n_syn->curSamples) < delta) {
            *client = current;
            delta = current->samplesLeft - n_syn->curSamples;
        }
    }

    return (*client)->samplesLeft;
}

// s32 func_10019A04(void *arg0) {
//     u32 sp4;
//     void *sp0;
//     void *temp_t2;
//     void *temp_t8;
//
//     sp4 = 0x7FFFFFFF;
//     *arg0 = NULL;
//     temp_t8 = *D_8002BA44;
//     sp0 = temp_t8;
//     if (temp_t8 != 0) {
// loop_1:
//         if ((u32) (sp0->unk10 - D_8002BA44->unk20) < sp4) {
//             *arg0 = sp0;
//             sp4 = sp0->unk10 - D_8002BA44->unk20;
//         }
//         temp_t2 = sp0->unk0;
//         sp0 = temp_t2;
//         if (temp_t2 != 0) {
//             goto loop_1;
//         }
//     }
//     return (*arg0)->unk10;
// }
