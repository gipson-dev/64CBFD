#include <n_libaudio.h>

void _n_handleEvent(u16 *event);

extern N_ALSndpSoundState *D_8002BA20;
extern N_ALSndpSoundState *D_8002BA24;
extern N_ALSndpSoundState *D_8002BA28;
extern N_ALSndPlayerExtended *D_8002BA2C;
extern s16 D_8002BA30;
extern u16 *D_800428B8;

s32 func_10015878(N_ALSndPlayer *sndp);
N_ALSndpSoundState *func_10017100(s32 bank, s16 soundIndex);
void func_10017298(N_ALSndpSoundState *state);
void func_10016E90(N_ALSndpSoundState *state);
void func_10016F00(N_ALSndpSoundState *state);
void func_10016F80(ALEventQueue *evtq, N_ALSndpSoundState *voice, u16 typeMask);
void func_10012C5C(void *object, void *base, s32 count);
s32 func_1001BD34(void *driver, void *resource, s32 index);
void func_1001BE1C(void *driver, s32 *resource, s32 index);
void func_1001E2A0(N_ALVoice *voice, u8 pan);
void func_1001E350(N_ALVoice *voice, u8 value);
N_ALSndpSoundState *func_10017438(ALBank *bank, s16 soundNum, u16 vol, ALPan pan, f32 pitch, u8 fxmix, u8 fxbus,
                                      N_ALSndpSoundState **handle);

#define M2C_FIELD(expr, type, offset) (*(type)((u8 *)(expr) + (offset)))
#define g_SndpAllocStatesHead        D_8002BA20
#define g_SndpAllocStatesTail        D_8002BA24
#define g_SndpFreeStatesHead         D_8002BA28
#define g_SndPlayer                  D_8002BA2C
#define g_SndpNumPlaying             D_8002BA30
#define g_SndpVolumeTable            D_800428B8

#define SNDP_PLAY_EVT                0x001
#define SNDP_PITCH_EVT               0x010
#define SNDP_API_EVT                 0x020
#define SNDP_END_EVT                 0x080
#define SNDP_STOPALL_EVT             0x400
#define SNDP_VOLTBL_EVT              0x800
#define SNDP_PLAY_SOUND_EVT          0x4000

#define SNDP_LEAF_FLAG               0x01
#define SNDP_STATE_READY_MASK        0x03
#define SNDP_HAS_VOICE_FLAG          0x04
#define SNDP_RELATIVE_DELAY_FLAG     0x10
#define SNDP_PARENT_OF_LEAF_FLAG     0x10
#define SNDP_HAS_DETUNE_PITCH_FLAG   0x20
#define SNDP_CLEAR_PARENT_FLAG_MASK  (~SNDP_PARENT_OF_LEAF_FLAG)
#define SNDP_CHANNEL_MASK            0x1F
#define SNDP_ALL_EVENT_TYPES         0xFFFF
#define SNDP_VOLUME_TABLE_FULL       0x7FFF
#define SNDP_MAX_PRIORITY            0x40
#define SNDP_INITIAL_RETRY_COUNT     2
#define SNDP_STATE_READY             5
#define SNDP_PITCH_UPDATE_DELAY      33333
#define SNDP_STATE_VOICE(state)      ((N_ALVoice *) (state)->voice)
#define SNDP_ENV_VOLUME(state)       (*(s16 *) &(state)->pad46[0])
#define SNDP_END_TIME(state)         (*(s32 *) &(state)->pad46[2])
#define SNDP_EXTRA(state)            ((state)->pad52)

void func_10015550(N_ALCSPlayer *csp, ALBank *bank) {
    N_ALEvent event;

    event.type = AL_SEQP_BANK_EVT;
    event.msg.spbank.bank = bank;

    n_alEvtqPostEvent(&csp->evtq, &event, 0, 2);
}

void func_100155A0(N_ALSndpConfig *config) {
    u32 stateIndex;
    void *ptr;
    N_ALEvent event;
    N_ALSndpSoundState *states;
    N_ALSndpSoundState *state;
    N_ALSndpSoundState *prevState;

    g_SndPlayer->maxSounds = config->maxSounds;
    g_SndPlayer->target = 0;
    g_SndPlayer->drvr = n_syn;
    g_SndPlayer->frameTime = AL_USEC_PER_FRAME;

    ptr = alHeapDBAlloc(0, 0, config->heap, config->maxStates, sizeof(N_ALSndpSoundState));
    g_SndPlayer->sndState = ptr;
    g_SndPlayer->soundTableCount = config->soundTableCount;

    ptr = alHeapDBAlloc(0, 0, config->heap, config->maxEvents, sizeof(N_ALEventListItem));
    n_alEvtqNew(&g_SndPlayer->evtq, ptr, config->maxEvents);

    g_SndpFreeStatesHead = g_SndPlayer->sndState;

    for (stateIndex = 1; stateIndex < (u32) config->maxStates; stateIndex++) {
        states = g_SndPlayer->sndState;
        state = &states[stateIndex];
        prevState = &states[stateIndex - 1];
        state->node.next = prevState->node.next;
        state->node.prev = &prevState->node;
        if (prevState->node.next != 0) {
            prevState->node.next->prev = &state->node;
        }
        prevState->node.next = &state->node;
    }

    g_SndpVolumeTable = alHeapDBAlloc(0, 0, config->heap, sizeof(u16), config->maxVolumes);
    for (stateIndex = 0; stateIndex < config->maxVolumes; stateIndex++) {
        g_SndpVolumeTable[stateIndex] = SNDP_VOLUME_TABLE_FULL;
    }

    g_SndPlayer->node.next = 0;
    g_SndPlayer->node.handler = (ALVoiceHandler) func_10015878;
    g_SndPlayer->node.clientData = g_SndPlayer;
    n_alSynAddPlayer(&g_SndPlayer->node);

    event.type = SNDP_API_EVT;
    n_alEvtqPostEvent(&g_SndPlayer->evtq, &event, g_SndPlayer->frameTime, 3);
    g_SndPlayer->nextDelta = n_alEvtqNextEvent(&g_SndPlayer->evtq, &g_SndPlayer->nextEvent);
}

s32 func_10015878(N_ALSndPlayer *sp) {
    N_ALSndPlayer *alsp;
    N_ALEvent event;

    alsp = sp;
    do {
        switch (alsp->nextEvent.type) {
        case SNDP_API_EVT:
            event.type = SNDP_API_EVT;
            n_alEvtqPostEvent(&alsp->evtq, &event, alsp->frameTime, 3);
            break;
        default:
            _n_handleEvent((u16 *)&alsp->nextEvent);
            break;
        }
        alsp->nextDelta = n_alEvtqNextEvent(&alsp->evtq, &alsp->nextEvent);
    } while (alsp->nextDelta == 0);

    alsp->curTime += alsp->nextDelta;
    return alsp->nextDelta;
}

void _n_handleEvent(u16 *arg0) {
    s32 spA4;
    s8 spA0;
    s16 sp9E;
    s16 sp9C;
    ALSound *sp98;
    ALKeyMap *sp94;
    u8 sp93;
    void *sp84;
    u16 sp80;
    f32 sp78;
    N_ALSndpSoundState *sp74;
    u16 sp70;
    s32 sp6C;
    s32 sp68;
    s32 sp64;
    s32 sp60;
    s32 sp5C;
    s32 sp58;
    s32 sp54;
    s32 sp50;
    N_ALSndpSoundState *sp4C;
    N_ALSndpSoundState *sp48;
    s32 sp44;
    s32 var_s0;
    s32 var_s0_2;
    s32 var_s0_3;
    s32 var_s0_4;
    s32 var_s0_5;
    s32 var_s1;
    s32 var_s1_2;
    s32 var_s1_3;
    s32 var_s1_4;
    u16 temp_s0;
    u16 temp_t7;
    u8 temp_s0_2;
    u8 temp_t9;
    ALKeyMap *temp_t3;

    sp54 = 1;
    sp50 = 0;
    sp4C = NULL;
    sp48 = NULL;
loop_1:
    if (sp48 != NULL) {
        sp74 = sp4C;
        sp70 = M2C_FIELD(arg0, u16 *, 0);
        sp78 = M2C_FIELD(arg0, f32 *, 8);
        arg0 = &sp70;
    }
    sp4C = M2C_FIELD(arg0, N_ALSndpSoundState **, 4);
    if (sp4C == NULL) {

    }
    sp98 = sp4C->sound;
    sp48 = (N_ALSndpSoundState *)sp4C->node.next;
    if ((sp98 == NULL) && (M2C_FIELD(arg0, u16 *, 0) != 0x4000)) {
        if (sp4C->retryCount > 0) {
            temp_t7 = M2C_FIELD(arg0, u16 *, 0);
            if ((temp_t7 != 4) && (temp_t7 != 8) && (temp_t7 != 0x100) && (temp_t7 != 0x10) && (temp_t7 != 0x800) && (temp_t7 != 0x2000)) {
                sp4C->retryCount--;
            }
            n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *)arg0, 0x8235, 2);
        } else {
            func_10016E90(sp4C);
        }
        goto block_174;
    }
    temp_s0 = M2C_FIELD(arg0, u16 *, 0);
    switch ((s32) temp_s0) {                        /* switch 1; irregular */
    case 0x4000:                                    /* switch 1 */
        if (sp98 == NULL) {
            sp98 = (ALSound *)func_1001BD34(g_SndPlayer->drvr, (u8 *)sp4C->bank + 0xC, sp4C->soundNum);
            sp4C->sound = sp98;
            if (sp98 == NULL) {
                M2C_FIELD(arg0, u16 *, 0) = 0x4000;
                sp4C->state = 5;
                sp4C->retryCount--;
                n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *)arg0, 0x8235, 2);
                goto block_174;
            }
        }
        if (sp98 != NULL) {
            if ((u32) M2C_FIELD(sp98, u32 *, 0) < 0x01000000U) {
                func_10012C5C(sp98, sp98, g_SndPlayer->soundTableCount);
            }
            if ((M2C_FIELD(sp98, u32 *, 0) & 0xFF000003) != 0x80000000) {
                goto block_174;
            }
            temp_t3 = sp98->keyMap;
            sp94 = temp_t3;
            sp4C->sound = sp98;
            sp44 = (sp98->envelope->decayTime + 1) == 0;
            sp4C->priority = (u8) (sp44 + 0x40);
            sp4C->flags = (temp_t3->keyMax & 0xF0) | 1;
            if (sp4C->flags & 0x20) {
                sp4C->basePitch = alCents2Ratio((sp94->keyBase * 0x64) - 0x1770);
            } else {
                sp4C->basePitch = alCents2Ratio(((sp94->keyBase * 0x64) + sp94->detune) - 0x1770);
            }
            if (sp44 != 0) {
                sp4C->flags |= 2;
            }
            goto block_50;
        }
block_50:
        M2C_FIELD(arg0, u16 *, 0) = 1;
    case 0x1:                                       /* switch 1 */
        temp_t9 = sp4C->state;
        if ((temp_t9 != 5) && (temp_t9 != 4)) {
            return;
        }
        sp94 = sp98->keyMap;
        sp9E = sp4C->fxbus;
        sp9C = sp4C->priority;
        spA0 = 0;
        spA4 = M2C_FIELD((M2C_FIELD(M2C_FIELD(sp4C, void **, 0x3C), s32 *, 0xC) + (M2C_FIELD(sp4C, s16 *, 0x4C) * 4)), s32 *, 0x10);
        sp5C = g_SndpNumPlaying >= g_SndPlayer->maxSounds;
        if ((sp5C == 0) || (sp4C->flags & 0x10)) {
            sp50 = n_alSynAllocVoice(SNDP_STATE_VOICE(sp4C), (ALVoiceConfig *)&sp9C);
        }
        if (sp50 == 0) {
            if ((sp4C->flags & 0x12) || (sp4C->retryCount > 0)) {
                sp4C->state = 4;
                sp4C->retryCount--;
                n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *)arg0, 0x8235, 2);
            } else {
                func_10016E90(sp4C);
            }
            return;
        }
        sp4C->flags |= 4;
        SNDP_ENV_VOLUME(sp4C) = sp98->envelope->attackVolume;
        sp4C->fxbus = sp9E;
        sp6C = (s32) (((f32) sp98->envelope->attackTime / sp4C->pitch) / sp4C->basePitch);
        SNDP_END_TIME(sp4C) = g_SndPlayer->curTime + sp6C;
        sp64 = (s32) (g_SndpVolumeTable[sp94->keyMin & SNDP_CHANNEL_MASK] *
                      ((s32) (SNDP_ENV_VOLUME(sp4C) * sp4C->vol * sp98->sampleVolume) / 16129)) / 32767;
        if (sp64 <= 0) {
            sp64 = 0;
        } else {
            sp64--;
        }
        sp60 = (sp4C->pan + sp98->samplePan) - 0x40;
        if (sp60 > 0) {
            var_s0 = sp60;
        } else {
            var_s0 = 0;
        }
        if (var_s0 < 0x7F) {
            if (sp60 > 0) {
                var_s1 = sp60;
            } else {
                var_s1 = 0;
            }
            sp93 = (u8) var_s1;
        } else {
            sp93 = 0x7F;
        }
        sp68 = (sp4C->fxmix & 0x7F) + ((sp94->keyMax & 0xF) * 8);
        if (sp68 < 0) {
            var_s0_2 = 0;
        } else {
            var_s0_2 = sp68;
        }
        if (var_s0_2 >= 0x80) {
            sp68 = 0x7F;
        } else {
            if (sp68 < 0) {
                var_s1_2 = 0;
            } else {
                var_s1_2 = sp68;
            }
            sp68 = var_s1_2;
        }
        sp68 |= sp4C->fxmix & 0x80;
        func_1001BE1C(g_SndPlayer->drvr, (s32 *)((u8 *)sp4C->bank + 0xC), sp4C->soundNum);
        n_alSynStartVoiceParams(SNDP_STATE_VOICE(sp4C), sp98->wavetable, sp4C->pitch * sp4C->basePitch, sp64, (s32) sp93, sp68, 0, 0.0f, 0, sp6C);
        sp4C->state = 1;
        g_SndpNumPlaying++;
        if (!(sp4C->flags & 2)) {
            if (sp6C == 0) {
                SNDP_ENV_VOLUME(sp4C) = sp98->envelope->decayVolume;
                sp64 = (s32) (g_SndpVolumeTable[sp94->keyMin & SNDP_CHANNEL_MASK] *
                              ((s32) (SNDP_ENV_VOLUME(sp4C) * sp4C->vol * sp98->sampleVolume) / 16129)) / 32767;
                if (sp64 <= 0) {
                    sp64 = 0;
                } else {
                    sp64--;
                }
                sp6C = (s32) (((f32) sp98->envelope->decayTime / sp4C->basePitch) / sp4C->pitch);
                SNDP_END_TIME(sp4C) = g_SndPlayer->curTime + sp6C;
                n_alSynSetVol(SNDP_STATE_VOICE(sp4C), sp64, sp6C);
                sp80 = 2;
                sp84 = sp4C;
                n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *)&sp80, sp6C, 2);
                if (sp4C->flags & 0x20) {
                    func_10016F00(sp4C);
                }
            } else {
                sp80 = 0x40;
                sp84 = sp4C;
                sp6C = (s32) (((f32) sp98->envelope->attackTime / sp4C->pitch) / sp4C->basePitch);
                n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *)&sp80, sp6C, 2);
            }
        }
block_174:
        sp58 = M2C_FIELD(arg0, u16 *, 0) & 0x42D1;
        sp4C = sp48;
        if ((sp48 != NULL) && (sp58 == 0)) {
            sp54 = sp4C->flags & 1;
        }
        if ((sp54 != 0) || (sp4C == NULL) || (sp58 != 0)) {
            return;
        }
        goto loop_1;
    case 0x2:                                       /* switch 1 */
    case 0x400:                                     /* switch 1 */
    case 0x1000:                                    /* switch 1 */
        if ((M2C_FIELD(arg0, u16 *, 0) != 0x1000) || (sp4C->flags & 2)) {
            temp_s0_2 = sp4C->state;
            switch (temp_s0_2) {                    /* switch 2; irregular */
            case 1:                                 /* switch 2 */
                func_10016F80(&g_SndPlayer->evtq, sp4C, 0x40);
                sp6C = (s32) (((f32) sp98->envelope->releaseTime / sp4C->basePitch) / sp4C->pitch);
                n_alSynSetVol(SNDP_STATE_VOICE(sp4C), 0, sp6C);
                if (sp6C != 0) {
                    sp80 = 0x80;
                    sp84 = sp4C;
                    n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *)&sp80, sp6C, 2);
                    sp4C->state = 2;
                } else {
                    func_10016E90(sp4C);
                }
                break;
            case 4:                                 /* switch 2 */
            case 5:                                 /* switch 2 */
                func_10016E90(sp4C);
                break;
            }
            if (M2C_FIELD(arg0, u16 *, 0) == 2) {
                M2C_FIELD(arg0, u16 *, 0) = 0x1000;
            }
        }
        goto block_174;
    case 0x4:                                       /* switch 1 */
        sp4C->pan = M2C_FIELD(arg0, u8 *, 8);
        if (sp4C->state == 1) {
            sp60 = (sp4C->pan + sp98->samplePan) - 0x40;
            if (sp60 > 0) {
                var_s0_3 = sp60;
            } else {
                var_s0_3 = 0;
            }
            if (var_s0_3 < 0x7F) {
                if (sp60 > 0) {
                    var_s1_3 = sp60;
                } else {
                    var_s1_3 = 0;
                }
                sp93 = (u8) var_s1_3;
            } else {
                sp93 = 0x7F;
            }
            func_1001E2A0(SNDP_STATE_VOICE(sp4C), sp93);
        }
        goto block_174;
    case 0x10:                                      /* switch 1 */
        sp4C->pitch = M2C_FIELD(arg0, f32 *, 8);
        if (sp4C->state == 1) {
            n_alSynSetPitch(SNDP_STATE_VOICE(sp4C), sp4C->pitch * sp4C->basePitch);
            if (sp4C->flags & 0x20) {
                func_10016F00(sp4C);
            }
        }
        goto block_174;
    case 0x100:                                     /* switch 1 */
        sp94 = sp98->keyMap;
        sp4C->fxmix = M2C_FIELD(arg0, u8 *, 8);
        if (sp4C->state == 1) {
            sp68 = (sp4C->fxmix & 0x7F) + ((sp94->keyMax & 0xF) * 8);
            if (sp68 < 0) {
                var_s0_4 = 0;
            } else {
                var_s0_4 = sp68;
            }
            if (var_s0_4 >= 0x80) {
                sp68 = 0x7F;
            } else {
                if (sp68 < 0) {
                    var_s1_4 = 0;
                } else {
                    var_s1_4 = sp68;
                }
                sp68 = var_s1_4;
            }
            sp68 |= sp4C->fxmix & 0x80;
            n_alSynSetFXMix(SNDP_STATE_VOICE(sp4C), sp68);
        }
        goto block_174;
    case 0x2000:                                    /* switch 1 */
        sp4C->fxbus = M2C_FIELD(arg0, u8 *, 8);
        if ((s32) sp4C->fxbus >= M2C_FIELD(n_syn, s32 *, 0x50)) {
            sp4C->fxbus = 0;
        }
        if (sp4C->state == 1) {
            M2C_FIELD(sp4C, s16 *, 0x2C) = sp4C->fxbus;
        }
        goto block_174;
    case 0x8:                                       /* switch 1 */
        sp94 = sp98->keyMap;
        sp4C->vol = M2C_FIELD(arg0, s16 *, 8);
        if (sp4C->state == 1) {
            sp64 = (s32) (g_SndpVolumeTable[sp94->keyMin & SNDP_CHANNEL_MASK] *
                          ((s32) (SNDP_ENV_VOLUME(sp4C) * sp4C->vol * sp98->sampleVolume) / 16129)) / 32767;
            if (sp64 <= 0) {
                sp64 = 0;
            } else {
                sp64--;
            }
            if ((SNDP_END_TIME(sp4C) - g_SndPlayer->curTime) < 0x3E8) {
                var_s0_5 = 0x3E8;
            } else {
                var_s0_5 = SNDP_END_TIME(sp4C) - g_SndPlayer->curTime;
            }
            n_alSynSetVol(SNDP_STATE_VOICE(sp4C), sp64, var_s0_5);
        }
        goto block_174;
    case 0x800:                                     /* switch 1 */
        sp94 = sp98->keyMap;
        if (sp4C->state == 1) {
            sp6C = (s32) (((f32) sp98->envelope->releaseTime / sp4C->basePitch) / sp4C->pitch);
            sp64 = (s32) (g_SndpVolumeTable[sp94->keyMin & SNDP_CHANNEL_MASK] *
                          ((s32) (SNDP_ENV_VOLUME(sp4C) * sp4C->vol * sp98->sampleVolume) / 16129)) / 32767;
            if (sp64 <= 0) {
                sp64 = 0;
            } else {
                sp64--;
            }
            n_alSynSetVol(SNDP_STATE_VOICE(sp4C), sp64, sp6C);
        }
        goto block_174;
    case 0x40:                                      /* switch 1 */
        if (!(sp4C->flags & 2)) {
            sp94 = sp98->keyMap;
            SNDP_ENV_VOLUME(sp4C) = sp98->envelope->decayVolume;
            sp64 = (s32) (g_SndpVolumeTable[sp94->keyMin & SNDP_CHANNEL_MASK] *
                          ((s32) (SNDP_ENV_VOLUME(sp4C) * sp4C->vol * sp98->sampleVolume) / 16129)) / 32767;
            if (sp64 <= 0) {
                sp64 = 0;
            } else {
                sp64--;
            }
            sp6C = (s32) (((f32) sp98->envelope->decayTime / sp4C->basePitch) / sp4C->pitch);
            SNDP_END_TIME(sp4C) = g_SndPlayer->curTime + sp6C;
            n_alSynSetVol(SNDP_STATE_VOICE(sp4C), sp64, sp6C);
            sp80 = 2;
            sp84 = sp4C;
            n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *)&sp80, sp6C, 2);
            if (sp4C->flags & 0x20) {
                func_10016F00(sp4C);
            }
        }
        goto block_174;
    case 0x80:                                      /* switch 1 */
        func_10016E90(sp4C);
        goto block_174;
    case 0x200:                                     /* switch 1 */
        if (sp4C->flags & 0x10) {
            func_10017438((ALBank *)M2C_FIELD(arg0, s32 *, 0xC), (s16)M2C_FIELD(arg0, s32 *, 8), sp4C->vol, sp4C->pan, sp4C->pitch, sp4C->fxmix, sp4C->fxbus, sp4C->handle);
        }
        goto block_174;
    case 0x8000:                                    /* switch 1 */
        SNDP_EXTRA(sp4C) = M2C_FIELD(arg0, u8 *, 8);
        if (sp4C->state == 1) {
            func_1001E350(SNDP_STATE_VOICE(sp4C), SNDP_EXTRA(sp4C));
        }
        goto block_174;
    case 0x3:                                       /* switch 1 */
    case 0x5:                                       /* switch 1 */
    case 0x6:                                       /* switch 1 */
    case 0x7:                                       /* switch 1 */
    case 0x9:                                       /* switch 1 */
    case 0xA:                                       /* switch 1 */
    case 0xB:                                       /* switch 1 */
    case 0xC:                                       /* switch 1 */
    case 0xD:                                       /* switch 1 */
    case 0xE:                                       /* switch 1 */
    case 0xF:                                       /* switch 1 */
        goto block_174;
    }
}

void func_10016E90(N_ALSndpSoundState *state) {
    if ((state->flags & SNDP_HAS_VOICE_FLAG) != 0) {
        n_alSynStopVoice(SNDP_STATE_VOICE(state));
        n_alSynFreeVoice(SNDP_STATE_VOICE(state));
    }
    func_10017298(state);
    func_10016F80(&g_SndPlayer->evtq, state, SNDP_ALL_EVENT_TYPES);
}

void func_10016F00(N_ALSndpSoundState *state) {
    N_ALEvent event;
    f32 res;

    res = alCents2Ratio(state->sound->keyMap->detune) * state->pitch;

    event.type = SNDP_PITCH_EVT;
    event.msg.vol.voice = (N_ALVoice *) state;
    event.msg.vol.delta = *(s32*)&res;

    n_alEvtqPostEvent(&g_SndPlayer->evtq, &event, SNDP_PITCH_UPDATE_DELAY, 2);
}

void func_10016F80(ALEventQueue *evtq, N_ALSndpSoundState *voice, u16 typeMask) {
    N_ALEventListItem *current;
    N_ALEventListItem *next;
    N_ALEventListItem *item;
    N_ALEventListItem *nextEvent;
    N_ALEvent *event;
    s32 mask;
    ALLink *unlink;
    ALLink *freeItem;
    ALEventQueue *queue;

    mask = osSetIntMask(1);
    current = (N_ALEventListItem *) evtq->allocList.next;
    if (current != 0) {
        do {
            next = (N_ALEventListItem *) current->node.next;
            item = current;
            nextEvent = next;
            event = &item->evt;
            if ((event->msg.unknown1.unk0 == (N_ALUnknownStruct1 *) voice) && (((u16) event->type & typeMask) != 0)) {
                if (nextEvent != 0) {
                    nextEvent->delta += item->delta;
                }
                unlink = (ALLink *) current;
                if (unlink->next != 0) {
                    unlink->next->prev = unlink->prev;
                }
                if (unlink->prev != 0) {
                    unlink->prev->next = unlink->next;
                }
                freeItem = (ALLink *) current;
                queue = evtq;
                freeItem->next = queue->freeList.next;
                freeItem->prev = &queue->freeList;
                if (queue->freeList.next != 0) {
                    queue->freeList.next->prev = freeItem;
                }
                queue->freeList.next = freeItem;
            }
            current = next;
        } while (current != 0);
    }
    osSetIntMask(mask);
}

N_ALSndpSoundState *func_10017100(s32 bank, s16 soundIndex) {
    N_ALSndpSoundState *state;
    u32 mask;
    N_ALSndpSoundState *unlink;

    mask = osSetIntMask(1);
    state = g_SndpFreeStatesHead;
    if (state != 0) {
        g_SndpFreeStatesHead = (N_ALSndpSoundState *) state->node.next;
        unlink = state;
        if (unlink->node.next) {
            unlink->node.next->prev = unlink->node.prev;
        }
        if (unlink->node.prev) {
            unlink->node.prev->next = unlink->node.next;
        }
        if (g_SndpAllocStatesHead) {
            state->node.next = &g_SndpAllocStatesHead->node;
            state->node.prev = NULL;
            g_SndpAllocStatesHead->node.prev = &state->node;
            g_SndpAllocStatesHead = state;
        } else {
            state->node.prev = 0;
            state->node.next = state->node.prev;
            g_SndpAllocStatesHead = state;
            g_SndpAllocStatesTail = state;
        }
        osSetIntMask(mask);
        state->sound = 0;
        state->soundNum = soundIndex;
        state->bank = (ALBank *) bank;
        state->priority = SNDP_MAX_PRIORITY;
        state->state = SNDP_STATE_READY;
        state->retryCount = SNDP_INITIAL_RETRY_COUNT;
        state->flags = 0;
        state->handle = 0;
        state->basePitch = 1.0f;
    } else {
        osSetIntMask(mask);
    }
    return state;
}

void func_10017298(N_ALSndpSoundState *state) {
    N_ALSndpSoundState *unlink;

    if (g_SndpAllocStatesHead == state) {
        g_SndpAllocStatesHead = (N_ALSndpSoundState *) state->node.next;
    }
    if (g_SndpAllocStatesTail == state) {
        g_SndpAllocStatesTail = (N_ALSndpSoundState *) state->node.prev;
    }

    unlink = state;
    if (unlink->node.next) {
        unlink->node.next->prev = unlink->node.prev;
    }

    if (unlink->node.prev) {
        unlink->node.prev->next = unlink->node.next;
    }

    if (g_SndpFreeStatesHead) {
        state->node.next = &g_SndpFreeStatesHead->node;
        state->node.prev = NULL;
        g_SndpFreeStatesHead->node.prev = &state->node;
        g_SndpFreeStatesHead = state;
    } else {
        state->node.prev = NULL;
        state->node.next = state->node.prev;
        g_SndpFreeStatesHead = state;
    }
    if (state->flags & SNDP_HAS_VOICE_FLAG) {
        g_SndpNumPlaying -= 1;
    }
    state->state = AL_STOPPED;
    if (state->handle) {
        if (*state->handle == state) {
            *state->handle = 0;
        }
        state->handle = NULL;
    }
}

s32 func_100173C4(N_ALSndpSoundState **handle) {
    s32 ret;
    s32 mask;

    ret = 0;
    if (*handle) {
        mask = __osDisableInt();
        if (*handle) {
            ret = (*handle)->state;
        }
        __osRestoreInt(mask);
    }
    return ret;
}

N_ALSndpSoundState *func_10017438(ALBank *bank, s16 soundNum, u16 vol, ALPan pan, f32 pitch, u8 fxmix, u8 fxbus,
                                      N_ALSndpSoundState **handle) {
    N_ALSndpSoundState *state;
    N_ALSndpSoundState *leafState;
    s16 done;
    s32 delay;
    N_ALSndpEventPayload event;

    leafState = NULL;
    done = 0;
    if (soundNum != 0) {
        do {
            state = func_10017100((s32) bank, soundNum - 1);
            if (state != 0) {
                g_SndPlayer->target = (s32) state;
                event.type = SNDP_PLAY_SOUND_EVT;
                event.state = state;
                state->pan = pan;
                state->vol = vol;
                state->pitch = pitch;
                state->fxmix = fxmix;
                state->fxbus = fxbus;
                delay = 0;
                n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *) &event, delay + 1, 2);
                leafState = state;
            }
            soundNum = 0;
        } while ((soundNum != 0) && (state != 0));
        if (leafState != 0) {
            leafState->flags |= SNDP_LEAF_FLAG;
            leafState->handle = handle;
            if (done != 0) {
            }
        }
    }
    if (handle != 0) {
        *handle = leafState;
    }
    return leafState;
}

void func_10017594(N_ALSndpSoundState *state) {
    N_ALEvent event;

    if (state) {
        event.type = SNDP_STOPALL_EVT;
        event.msg.unknown1.unk0 = (N_ALUnknownStruct1 *) state;
        ((N_ALSndpSoundState *) event.msg.unknown1.unk0)->flags &= SNDP_CLEAR_PARENT_FLAG_MASK;
        n_alEvtqPostEvent(&g_SndPlayer->evtq, &event, 0, 2);
    }
}

void func_10017604(u8 flags) {
    s32 mask;
    N_ALSndpEventPayload event;
    N_ALSndpSoundState *state;

    mask = osSetIntMask(1);
    state = g_SndpAllocStatesHead;
    if (state != 0) {
        do {
            event.type = SNDP_STOPALL_EVT;
            event.state = state;
            if ((state->flags & flags) == flags) {
                event.state->flags &= SNDP_CLEAR_PARENT_FLAG_MASK;
                n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *) &event, 0, 2);
            }
            state = (N_ALSndpSoundState *) state->node.next;
        } while (state != 0);
    }
    osSetIntMask(mask);
}

void func_100176C4(void) {
    func_10017604(SNDP_LEAF_FLAG);
}

void func_100176EC(void) {
    func_10017604(SNDP_STATE_READY_MASK);
}

void func_10017714(N_ALSndpSoundState *state, s16 type, s32 data) {
    N_ALEvent event;

    if (state != 0) {
        event.type = type;
        event.msg.vol.voice = (N_ALVoice *) state;
        event.msg.vol.delta = data;
        n_alEvtqPostEvent(&g_SndPlayer->evtq, &event, 0, 2);
    }
}

void func_10017780(u8 channel, u16 value) {
    s32 mask;
    N_ALSndpSoundState *state;
    s32 voiceIndex;
    N_ALSndpEventPayload event;

    mask = osSetIntMask(1);
    state = g_SndpAllocStatesHead;
    g_SndpVolumeTable[channel] = value;
    for (voiceIndex = 0; state != 0; voiceIndex++, state = (N_ALSndpSoundState *) state->node.next) {
        if ((state->sound != 0) && ((state->sound->keyMap->keyMin & SNDP_CHANNEL_MASK) == channel)) {
            event.type = SNDP_VOLTBL_EVT;
            event.state = state;
            n_alEvtqPostEvent(&g_SndPlayer->evtq, (N_ALEvent *) &event, 0, 2);
        }
    }
    osSetIntMask(mask);
}
