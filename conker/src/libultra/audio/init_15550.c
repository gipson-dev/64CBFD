#include <n_libaudio.h>

s32 _n_handleEvent(s32 arg0);

extern N_ALSndpSoundState *D_8002BA20;
extern N_ALSndpSoundState *D_8002BA24;
extern N_ALSndpSoundState *D_8002BA28;
extern N_ALSndPlayerExtended *D_8002BA2C;
extern s16 D_8002BA30;
extern u16 *D_800428B8;

s32 func_10015878(N_ALSndPlayer *sndp);
N_ALSndpSoundState *func_10017100(s32 bank, s16 soundIndex);
void func_10017298(N_ALSndpSoundState *state);
void func_10016F80(ALEventQueue *evtq, N_ALSndpSoundState *voice, u16 typeMask);

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
            _n_handleEvent(&alsp->nextEvent);
            break;
        }
        alsp->nextDelta = n_alEvtqNextEvent(&alsp->evtq, &alsp->nextEvent);
    } while (alsp->nextDelta == 0);

    alsp->curTime += alsp->nextDelta;
    return alsp->nextDelta;
}

s32 _n_handleEvent(s32 arg0) {
    return 0;
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
