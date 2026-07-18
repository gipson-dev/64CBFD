#include <os_internal.h>
#include <ultraerror.h>
#include "n_synthInternals.h"

/* Generated placeholder declarations. */
s32 _allocatePVoice(N_PVoice **pvoice, s16 priority);
/* End generated placeholder declarations. */

// s32 _allocatePVoice( N_PVoice **pvoice, s16 priority);
/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_synallocvoice/n_alSynAllocVoice.s. */
s32 n_alSynAllocVoice(N_ALVoice *voice, ALVoiceConfig *vc)
{
    N_PVoice *pvoice = 0;
    ALParam *update;
    s32 stolen;
    ALLink *element;
    ALLink *linkElement;
    ALLink *after;

    voice->priority   = vc->priority;
    voice->unityPitch = vc->unityPitch;
    voice->table      = 0;
    voice->fxBus      = vc->fxBus;
    voice->state      = AL_STOPPED;
    voice->pvoice     = 0;
    voice->unk14      = (void *)vc->unk8;

    stolen = _allocatePVoice(&pvoice, vc->priority);

    if (pvoice) {
        if (stolen) {
            pvoice->offset = 0x228;
            pvoice->vvoice->pvoice = 0;
            pvoice->vvoice = voice;
            voice->pvoice = pvoice;

            update = __n_allocParam();
            if (update) {
                update->delta      = n_syn->paramSamples;
                update->type       = AL_FILTER_SET_VOLUME;
                update->data.i     = 0;
                update->moredata.i = 0x170;

                n_alEnvmixerParam(voice->pvoice, AL_FILTER_ADD_UPDATE, update);
            } else {
            }

            update = __n_allocParam();
            if (update) {
                update->delta = n_syn->paramSamples + pvoice->offset;
                update->type  = AL_FILTER_STOP_VOICE;
                update->next  = 0;
                n_alEnvmixerParam(voice->pvoice, AL_FILTER_ADD_UPDATE, update);
            } else {
            }
        } else {
            pvoice->offset = 0;
            pvoice->vvoice = voice;
            voice->pvoice  = pvoice;

            element = &pvoice->voiceLink;
            if (element->next != 0) {
                element->next->prev = element->prev;
            }
            if (element->prev != 0) {
                element->prev->next = element->next;
            }

            linkElement = &pvoice->voiceLink;
            after = (ALLink *)&n_syn->auxBus[vc->fxBus].sourceCount;
            linkElement->next = after->next;
            linkElement->prev = after;
            if (after->next != 0) {
                after->next->prev = linkElement;
            }
            after->next = linkElement;

            pvoice->dc_table = 0;
        }
    }

    return (pvoice != 0);
}

// NON-MATCHING: plenty to figure out with the nlibaudio struct changes
// s32 n_alSynAllocVoice( N_ALVoice *voice, ALVoiceConfig *vc)
// {
//     N_PVoice  *pvoice = 0;
//     ALFilter *f;
//     ALParam *update;
//     s32 stolen;
//     N_PVoice *sp20;
//
// #ifdef _DEBUG
//     /* need two updates if voice is stolen */
//     if (n_syn->paramList == 0) {
//         __osError(ERR_ALSYN_NO_UPDATE, 0);
//         return 0;
//     } else if (n_syn->paramList->next == 0) {
//         __osError(ERR_ALSYN_NO_UPDATE, 0);
//         return 0;
//     }
// #endif
//
//     voice->priority     = vc->priority;
//     voice->unityPitch   = vc->unityPitch;
//     voice->table        = 0;
//     voice->fxBus        = vc->fxBus;
//     voice->state        = AL_STOPPED;
//     voice->pvoice       = 0;
//
//     voice->clientPrivate = vc->unk8;
//
//     stolen = _allocatePVoice( &pvoice, vc->priority);
//
//     if (pvoice) {    /* if we were able to allocate a voice */
//         if (stolen) {
//
//             pvoice->offset = 0x228; //512;
//             pvoice->vvoice->pvoice = 0; /* zero stolen voice */
//
// #if 1
//             pvoice->vvoice = voice;
//             voice->pvoice  = pvoice;
// #endif
//
//             /*
//              * ramp down stolen voice
//              */
//             update = __n_allocParam();
//             if (update) {
// #ifdef SAMPLE_ROUND
//                 update->delta      = SAMPLE184( n_syn->paramSamples );
// #else
//                 update->delta      = n_syn->paramSamples;
// #endif
//                 update->type       = AL_FILTER_SET_VOLUME;
//                 update->data.i     = 0;
//                 update->moredata.i = 0x170; //pvoice->offset - 64;
//
//                 n_alEnvmixerParam(voice->pvoice, AL_FILTER_ADD_UPDATE, update);
//             }
//             /*
//              * stop stolen voice
//              */
//             update = __n_allocParam();
//             if (update) {
// #ifdef SAMPLE_ROUND
//                 update->delta  = SAMPLE184( n_syn->paramSamples + pvoice->offset);
// #else
//                 update->delta  = n_syn->paramSamples + pvoice->offset;
// #endif
//                 update->type   = AL_FILTER_STOP_VOICE;
//                 update->next   = 0;
//                 n_alEnvmixerParam(voice->pvoice, AL_FILTER_ADD_UPDATE, update);
//
//             } else {
// #ifdef _DEBUG
//                 __osError(ERR_ALSYN_NO_UPDATE, 0);
// #endif
//             }
//
//         } else {
//             pvoice->offset = 0;
// #if 1
//             pvoice->vvoice = voice;
//             voice->pvoice  = pvoice;
//
//             sp20 = pvoice->vvoice; // + 8;
//             if (sp20->node.next != 0) {
//                 sp20->node.prev = sp20->node;
//             }
//             // if (sp20->unk4 != 0) {
//             //     *sp20->unk4 = (s32) sp20->unk0;
//             // }
//             // temp_t1 = pvoice + 8;
//             // sp1C = temp_t1;
//             // sp18 = D_8002BA44->unk48[vc->unk2].unk14;
//             // *temp_t1 = (s32) *sp18;
//             // sp1C->unk4 = sp18;
//             // if (*sp18 != 0) {
//             //     (*sp18)->unk4 = sp1C;
//             // }
//             // *sp18 = sp1C;
//             // pvoice->unk28 = 0;
// #endif
//         }
//
// #if 0
//         pvoice->vvoice = voice;     /* assign new voice  */
//         voice->pvoice  = pvoice;
// #endif
//
//     }
//
//     return (pvoice != 0);
// }


/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_synallocvoice/_allocatePVoice.s. */
s32 _allocatePVoice(N_PVoice **pvoice, s16 priority)
{
    ALLink *dl;
    N_PVoice *pv;
    s32 stolen;
    ALLink *element;
    ALLink *linkElement;
    ALLink *after;
    ALLink *element2;
    ALLink *linkElement2;
    ALLink *after2;

    stolen = 0;

    if ((dl = n_syn->pLameList.next) != 0) {
        *pvoice = (N_PVoice *)dl;
        element = dl;
        if (element->next != 0) {
            element->next->prev = element->prev;
        }
        if (element->prev != 0) {
            element->prev->next = element->next;
        }
        linkElement = dl;
        after = &n_syn->pAllocList;
        linkElement->next = after->next;
        linkElement->prev = after;
        if (after->next != 0) {
            after->next->prev = linkElement;
        }
        if (1) {
            after->next = linkElement;
        }
    } else if ((dl = n_syn->pFreeList.next) != 0) {
        *pvoice = (N_PVoice *)dl;
        element2 = dl;
        if (element2->next != 0) {
            element2->next->prev = element2->prev;
        }
        if (element2->prev != 0) {
            element2->prev->next = element2->next;
        }
        linkElement2 = dl;
        after2 = &n_syn->pAllocList;
        linkElement2->next = after2->next;
        linkElement2->prev = after2;
        if (after2->next != 0) {
            after2->next->prev = linkElement2;
        }
        if (1) {
            after2->next = linkElement2;
        }
    } else {
        for (dl = n_syn->pAllocList.next; dl != 0; dl = dl->next) {
            pv = (N_PVoice *)dl;
            if ((pv->vvoice->priority <= priority) && (pv->offset == 0)) {
                *pvoice = pv;
                priority = pv->vvoice->priority;
                stolen = 1;
            }
        }
    }

    return stolen;
}
