#include <libaudio.h>
#include <os_internal.h>
#include <ultraerror.h>
#include <assert.h>
#include "n_libaudio.h"
#include "n_seqp.h"
#include "cseq.h"
#include "n_cseqp.h"

       ALMicroTime      __n_CSPVoiceHandler(void *node);
       void              __n_CSPHandleNextSeqEvent(N_ALCSPlayer *seqp);
       void             __n_CSPHandleMIDIMsg(N_ALCSPlayer *seqp, N_ALEvent *event);
       void             __n_CSPHandleMetaMsg(N_ALCSPlayer *seqp, N_ALEvent *event);
       void             __n_CSPRepostEvent(ALEventQueue *evtq, N_ALEventListItem *item);
       void              __n_setUsptFromTempo(N_ALCSPlayer *seqp, f32 tempo);

void func_1001AAE0(N_ALSeqPlayer *seqp, N_ALVoice *voice);
u8 func_1001ADA4(N_ALSeqPlayer *seqp, N_ALVoice *voice, ALMicroTime killTime);
s32 func_1001B310(N_ALVoiceState *vs, N_ALSeqPlayer *seqp);
void func_1001CA90(N_ALVoice *voice, f32 pitch);
f32 func_1001CEA4(s32 cents);
N_ALVoiceState *func_1001AFEC(N_ALSeqPlayer *seqp, u8 key, u8 channel);
ALSound *func_1001B07C(N_ALSeqPlayer *seqp, u8 key, u8 velocity, u8 channel);
s32 func_1001B7D0(N_ALSeqPlayer *seqp, s32 program, s32 channel);
s32 func_1001D9B0(s16 index);
s32 func_1001DA28(s16 index);
void func_1001DAA0(s32 object, s16 index, s32 address);
void func_1001DAE4(void *object, s16 index, s32 *address);
ALMicroTime func_1001C4F0(ALEventQueue *evtq, s16 type);
#define CONKER_CSP_PAUSED 3
#define CONKER_CSP_MIX_EVT 25
#define CONKER_CSP_CONTROL_EVT 26


void n_alCSPNew(N_ALCSPlayer *seqp, ALSeqpConfig *c)
{
    s32                 i;
    N_ALEventListItem  *items;
    N_ALVoiceState     *vs;
    N_ALVoiceState     *voices;

    ALHeap *hp = c->heap;

    /*
     * initialize member variables
     */
    seqp->bank          = 0;
    seqp->target        = NULL;
    seqp->drvr          = n_syn;
    seqp->chanMask      = 0xffff;
    func_10017B30(seqp);
    seqp->uspt          = 488;
    seqp->nextDelta     = 0;
    seqp->state         = AL_STOPPED;
    seqp->vol           = 0x7FFF;              /* full volume  */
    seqp->debugFlags    = c->debugFlags;
    seqp->frameTime     = AL_USEC_PER_FRAME;   /* should get this from driver */
    seqp->curTime       = 0;
    seqp->initOsc       = c->initOsc;
    seqp->updateOsc     = c->updateOsc;
    seqp->stopOsc       = c->stopOsc;

#if 1
    seqp->unk7C = 0.0f;
    seqp->unk80 = 1.0f;
    seqp->unk84 = 0;
    seqp->unk8D = 0;
    seqp->unk8C = c->maxVoices;
#endif

    seqp->nextEvent.type = AL_SEQP_API_EVT;  /* this will start the voice handler "spinning" */

    /*
     * init the channel state
     */
    seqp->maxChannels = c->maxChannels;
    seqp->chanState = alHeapAlloc(hp, c->maxChannels, sizeof(ALChanState) );
    __n_initChanState((N_ALSeqPlayer*)seqp);  /* sct 11/6/95 */

    /*
     * init the voice state array
     */
    voices = alHeapAlloc(hp, c->maxVoices, sizeof(N_ALVoiceState));
    seqp->vFreeList = 0;
    for (i = 0; i < c->maxVoices; i++) {
      vs = &voices[i];
      vs->next = seqp->vFreeList;
      seqp->vFreeList = vs;
    }

    seqp->vAllocHead = 0;
    seqp->vAllocTail = 0;

    /*
     * init the event queue
     */
    items = alHeapAlloc(hp, c->maxEvents, sizeof(N_ALEventListItem));
    n_alEvtqNew(&seqp->evtq, items, c->maxEvents);


    /*
     * add ourselves to the driver
     */
    seqp->node.next       = NULL;
    seqp->node.handler    = __n_CSPVoiceHandler;
    seqp->node.clientData = seqp;
#if 1
    n_alSynAddSndPlayer (&seqp->node);
#endif
#if 0
    n_alSynAddSeqPlayer( &seqp->node);
#endif
}

ALMicroTime __n_CSPVoiceHandler(void *node)
{
    N_ALCSPlayer *seqp = (N_ALCSPlayer *)node;
    N_ALEvent evt;
    N_ALVoice *voice;
    N_ALVoiceState *vs;
    ALMicroTime delta;
    void *oscState;
    f32 oscValue;
    s32 object;
    s32 oldState;
    u8 chan;

    do {
        switch (seqp->nextEvent.type) {
        case AL_SEQ_REF_EVT:
            __n_CSPHandleNextSeqEvent(seqp);
            break;

        case AL_SEQP_API_EVT:
            evt.type = AL_SEQP_API_EVT;
            n_alEvtqPostEvent(&seqp->evtq, &evt, seqp->frameTime, 1);
            break;

        case AL_NOTE_END_EVT:
            voice = seqp->nextEvent.msg.note.voice;
            n_alSynStopVoice(voice);
            n_alSynFreeVoice(voice);
            vs = (N_ALVoiceState *)voice->unk10;
            if (vs->flags != 0) {
                __n_seqpStopOsc((N_ALSeqPlayer *)seqp, vs);
            }
            func_1001AAE0((N_ALSeqPlayer *)seqp, voice);
            break;

        case AL_SEQP_ENV_EVT:
            voice = seqp->nextEvent.msg.vol.voice;
            vs = (N_ALVoiceState *)voice->unk10;
            if (vs->envPhase == AL_PHASE_ATTACK) {
                vs->envPhase = AL_PHASE_DECAY;
            }
            delta = seqp->nextEvent.msg.vol.delta;
            vs->envEndTime = seqp->curTime + delta;
            vs->envGain = seqp->nextEvent.msg.vol.vol;
            n_alSynSetVol(voice, __n_vsVol(vs, (N_ALSeqPlayer *)seqp), delta);
            break;

        case AL_TREM_OSC_EVT:
            vs = seqp->nextEvent.msg.osc.vs;
            oscState = seqp->nextEvent.msg.osc.oscState;
            delta = seqp->updateOsc(oscState, &oscValue);
            vs->tremelo = (u8)oscValue;
            n_alSynSetVol(&vs->voice, __n_vsVol(vs, (N_ALSeqPlayer *)seqp),
                          __n_vsDelta(vs, seqp->curTime));
            evt.type = AL_TREM_OSC_EVT;
            evt.msg.osc.vs = vs;
            evt.msg.osc.oscState = oscState;
            n_alEvtqPostEvent(&seqp->evtq, &evt, delta, 0);
            break;

        case AL_VIB_OSC_EVT:
            vs = seqp->nextEvent.msg.osc.vs;
            oscState = seqp->nextEvent.msg.osc.oscState;
            chan = seqp->nextEvent.msg.osc.chan;
            delta = seqp->updateOsc(oscState, &oscValue);
            vs->vibrato = oscValue;
            n_alSynSetPitch(&vs->voice,
                            vs->pitch * vs->vibrato * seqp->chanState[chan].pitchBend);
            if (seqp->chanState[chan].unk14 != 0) {
                func_1001CA90(&vs->voice,
                              func_1001CEA4(seqp->chanState[chan].unk15 + vs->key -
                                            vs->sound->keyMap->keyBase - 0x40) *
                                  440.0f * seqp->chanState[chan].pitchBend * vs->vibrato);
            }
            evt.type = AL_VIB_OSC_EVT;
            evt.msg.osc.vs = vs;
            evt.msg.osc.oscState = oscState;
            evt.msg.osc.chan = chan;
            n_alEvtqPostEvent(&seqp->evtq, &evt, delta, 0);
            break;

        case AL_SEQP_MIDI_EVT:
        case AL_CSP_NOTEOFF_EVT:
            __n_CSPHandleMIDIMsg(seqp, &seqp->nextEvent);
            break;

        case AL_SEQP_META_EVT:
            __n_CSPHandleMetaMsg(seqp, &seqp->nextEvent);
            break;

        case AL_SEQP_VOL_EVT:
            seqp->vol = seqp->nextEvent.msg.spvol.vol;
            for (vs = seqp->vAllocHead; vs != NULL; vs = vs->next) {
                n_alSynSetVol(&vs->voice, __n_vsVol(vs, (N_ALSeqPlayer *)seqp),
                              __n_vsDelta(vs, seqp->curTime));
            }
            break;

        case CONKER_CSP_MIX_EVT:
            seqp->unk7C = seqp->nextEvent.msg.unknown0.unk0;
            seqp->unk80 = seqp->nextEvent.msg.unknown0.unk4;
            for (vs = seqp->vAllocHead; vs != NULL; vs = vs->next) {
                if (vs->envPhase != AL_PHASE_RELEASE) {
                    n_alSynSetFXMix(&vs->voice,
                                    (u8)func_1001B310(vs, (N_ALSeqPlayer *)seqp));
                }
            }
            break;

        case CONKER_CSP_CONTROL_EVT:
            if (seqp->nextEvent.msg.unknown2.unk1 < 8) {
                object = func_1001D9B0(seqp->nextEvent.msg.unknown2.unk0);
                if (object != 0) {
                    func_1001DAA0(object,
                                  (seqp->nextEvent.msg.unknown2.unk2 << 3) |
                                      (seqp->nextEvent.msg.unknown2.unk1 & 7),
                                  (s32)&seqp->nextEvent.msg.unknown2.unk4);
                }
            } else {
                object = func_1001DA28(seqp->nextEvent.msg.unknown2.unk0);
                if (object != 0) {
                    func_1001DAE4((void *)object, seqp->nextEvent.msg.unknown2.unk1,
                                  &seqp->nextEvent.msg.unknown2.unk4);
                }
            }
            break;

        case AL_SEQP_PLAY_EVT:
            if (seqp->state != AL_PLAYING && seqp->target != NULL) {
                oldState = seqp->state;
                seqp->state = AL_PLAYING;
                if (__alCSeqNextDelta(seqp->target, &delta)) {
                    evt.type = AL_SEQ_REF_EVT;
                    if (oldState == CONKER_CSP_PAUSED) {
                        delta = *(ALMicroTime *)seqp->unk88;
                    }
                    n_alEvtqPostEvent(&seqp->evtq, &evt, delta, 0);
                }
            }
            break;

        case AL_SEQP_STOP_EVT:
            if (seqp->state == AL_PLAYING) {
                seqp->state = CONKER_CSP_PAUSED;
                *(ALMicroTime *)seqp->unk88 = func_1001C4F0(&seqp->evtq, AL_SEQ_REF_EVT);
            }
            break;

        case AL_SEQP_STOPPING_EVT:
            if (seqp->state == AL_STOPPING) {
                while ((vs = seqp->vAllocHead) != NULL) {
                    n_alSynStopVoice(&vs->voice);
                    n_alSynFreeVoice(&vs->voice);
                    if (vs->flags != 0) {
                        __n_seqpStopOsc((N_ALSeqPlayer *)seqp, vs);
                    }
                    func_1001AAE0((N_ALSeqPlayer *)seqp, &vs->voice);
                }
                seqp->state = AL_STOPPED;
                for (chan = 0; chan < AL_MAX_CHANNELS; chan++) {
                    if (seqp->chanState[chan].instrument != NULL) {
                        ((void (*)(void *))seqp->drvr->unk34)(
                            seqp->bank->instArray[*(s16 *)((u8 *)&seqp->chanState[chan] + 0x38)]);
                        seqp->chanState[chan].instrument = NULL;
                    }
                }
            }
            break;

        case AL_SEQP_UNUSED_EVT:
            if (seqp->state == AL_PLAYING || seqp->state == CONKER_CSP_PAUSED) {
                func_1001C4F0(&seqp->evtq, AL_SEQ_REF_EVT);
                func_1001C4F0(&seqp->evtq, AL_CSP_NOTEOFF_EVT);
                func_1001C4F0(&seqp->evtq, AL_SEQP_MIDI_EVT);
                for (vs = seqp->vAllocHead; vs != NULL; vs = vs->next) {
                    if (func_1001ADA4((N_ALSeqPlayer *)seqp, &vs->voice, KILL_TIME)) {
                        __n_seqpReleaseVoice((N_ALSeqPlayer *)seqp, &vs->voice, KILL_TIME);
                    }
                }
                for (chan = 0; chan < AL_MAX_CHANNELS; chan++) {
                    seqp->chanState[chan].unkD = seqp->chanState[chan].unkE;
                    if (seqp->chanState[chan].unkD == 0) {
                        seqp->chanMask &= ~(1 << chan);
                    } else {
                        seqp->chanMask |= 1 << chan;
                    }
                }
                seqp->state = AL_STOPPING;
                evt.type = AL_SEQP_STOPPING_EVT;
                n_alEvtqPostEvent(&seqp->evtq, &evt, AL_EVTQ_END, 0);
            }
            break;

        case AL_SEQP_PRIORITY_EVT:
            chan = seqp->nextEvent.msg.sppriority.chan;
            seqp->chanState[chan].priority = seqp->nextEvent.msg.sppriority.priority;
            break;

        case AL_SEQP_SEQ_EVT:
            seqp->target = seqp->nextEvent.msg.spseq.seq;
            seqp->chanMask = 0xFFFF;
            if (seqp->bank != NULL) {
                __n_initFromBank((N_ALSeqPlayer *)seqp, seqp->bank);
            }
            break;

        case AL_SEQP_BANK_EVT:
            seqp->bank = seqp->nextEvent.msg.spbank.bank;
            __n_initFromBank((N_ALSeqPlayer *)seqp, seqp->bank);
            break;
        }

        seqp->nextDelta = n_alEvtqNextEvent(&seqp->evtq, &seqp->nextEvent);
    } while (seqp->nextDelta == 0);

    seqp->curTime += seqp->nextDelta;
    return seqp->nextDelta;
}

extern void (*jtbl_8002C4CC[])(void);
void __n_CSPHandleNextSeqEvent(N_ALCSPlayer *seqp)
{
    N_ALEvent evt;

    if (seqp->target == NULL || seqp->state == CONKER_CSP_PAUSED) {
        return;
    }

    n_alCSeqNextEvent(seqp->target, &evt, 1);

    switch (evt.type) {
    case AL_SEQ_MIDI_EVT:
        __n_CSPHandleMIDIMsg(seqp, &evt);
        __n_CSPPostNextSeqEvent(seqp);
        break;

    case AL_TEMPO_EVT:
        __n_CSPHandleMetaMsg(seqp, &evt);
        __n_CSPPostNextSeqEvent(seqp);
        break;

    case AL_SEQ_END_EVT:
        seqp->state = AL_STOPPING;
        evt.type = AL_SEQP_STOPPING_EVT;
        n_alEvtqPostEvent(&seqp->evtq, &evt, AL_EVTQ_END, 0);
        break;

    case AL_TRACK_END:
    case AL_CSP_LOOPSTART:
    case AL_CSP_LOOPEND:
        __n_CSPPostNextSeqEvent(seqp);
        break;

    default:
        break;
    }
}
typedef union {
    ALChanState standard;
    struct {
        u8 pad0[0x1C];
        ALMicroTime attackTime;
        ALMicroTime decayTime;
        ALMicroTime releaseTime;
        u8 useCustomEnvelope;
        u8 attackVolume;
        u8 decayVolume;
        s8 detune;
        u8 tremType;
        u8 tremRate;
        u8 tremDepth;
        u8 tremDelay;
        u8 vibType;
        u8 vibRate;
        u8 vibDepth;
        u8 vibDelay;
        u8 pad34;
        u8 oscArgument;
        u8 missingInstrument;
        u8 pad37[5];
    } custom;
} ConkerCSPChanState;

typedef struct {
    u8 pad0[0x3C];
    void *tremOscState;
    void *vibOscState;
} ConkerCSPVoiceOscState;

typedef ALMicroTime (*ConkerCSPOscInit)(void **state, f32 *value, u8 type,
                                     u8 rate, u8 depth, u8 delay, u8 argument);
typedef void (*ConkerCSPControl)(N_ALCSPlayer *seqp, N_ALEvent *event,
                                 u8 channel, u8 value);
extern ConkerCSPControl D_8002BA50[];
extern ConkerCSPControl D_8002BFC0[];
extern ALMicroTime D_80042810[];

void __n_CSPHandleMIDIMsg(N_ALCSPlayer *seqp, N_ALEvent *event)
{
    N_ALVoice *voice;
    s32 status;
    u8 chan;
    u8 key;
    u8 byte1;
    u8 byte2;
    ALMIDIEvent *midi = &event->msg.midi;
    N_ALEvent evt;
    ALMicroTime deltaTime;
    N_ALVoiceState *vstate;
    ConkerCSPChanState *channel;
    s32 type;

    status = midi->status & AL_MIDI_StatusMask;
    chan = midi->status & AL_MIDI_ChannelMask;
    byte1 = key = midi->byte1;
    byte2 = midi->byte2;

    if (((ConkerCSPChanState *)seqp->chanState)[chan].custom.missingInstrument &&
        status != AL_MIDI_ProgramChange) {
        evt.type = AL_SEQP_MIDI_EVT;
        evt.msg.midi = *midi;
        n_alEvtqPostEvent(&seqp->evtq, &evt, 0x8235, 0);
        return;
    }

    switch (status) {
    case AL_MIDI_NoteOn:
        if (byte2 != 0) {
            ALVoiceConfig config;
            ALSound *sound;
            s16 cents;
            f32 pitch;
            f32 oscValue;
            u8 fxmix;
            u8 filterEnabled;
            ALPan pan;
            s16 vol;
            f32 filterFrequency;
            void *oscState = NULL;
            ALInstrument *inst;

            if (seqp->state != AL_PLAYING || !(seqp->chanMask & (1 << chan))) {
                if (midi->duration) {
                    evt.type = AL_SEQP_MIDI_EVT;
                    evt.msg.midi.status = chan | AL_MIDI_NoteOff;
                    evt.msg.midi.byte1 = key;
                    evt.msg.midi.byte2 = 0;
                    deltaTime = seqp->uspt * midi->duration;
                    D_80042810[chan] = deltaTime;
                    n_alEvtqPostEvent(&seqp->evtq, &evt, deltaTime, 0);
                }
                break;
            }

            channel = (ConkerCSPChanState *)&seqp->chanState[chan];
            sound = func_1001B07C((N_ALSeqPlayer *)seqp, key, byte2, chan);
            if (!sound) {
                break;
            }
            if (!sound) {
                return;
            }
            config.priority = channel->standard.priority;
            config.fxBus = channel->standard.unkB;
            config.unityPitch = 0;
            config.unk8 = 0;
            vstate = __n_mapVoice((N_ALSeqPlayer *)seqp, key, byte2, chan);
            if (!vstate) {
                return;
            }
            voice = &vstate->voice;
            n_alSynAllocVoice(voice, &config);
            vstate->sound = sound;
            vstate->envPhase = AL_PHASE_ATTACK;
            if (channel->standard.sustain > AL_SUSTAIN) {
                vstate->phase = AL_PHASE_SUSTAIN;
            } else {
                vstate->phase = AL_PHASE_NOTEON;
            }
            cents = (key - sound->keyMap->keyBase) * 100 + sound->keyMap->detune;
            if (channel->custom.useCustomEnvelope) {
                cents += channel->custom.detune;
            }
            vstate->pitch = alCents2Ratio(cents);
            if (channel->custom.useCustomEnvelope) {
                vstate->envGain = channel->custom.attackVolume;
                vstate->envEndTime = seqp->curTime + channel->custom.attackTime;
            } else {
                vstate->envGain = sound->envelope->attackVolume;
                vstate->envEndTime = seqp->curTime + sound->envelope->attackTime;
            }
            vstate->flags = 0;
            if (channel->custom.useCustomEnvelope) {
                type = channel->custom.tremType;
            } else {
                inst = seqp->chanState[chan].instrument;
                type = inst->tremType;
            }
            oscValue = AL_VOL_FULL;
            if (type && seqp->initOsc) {
                if (channel->custom.useCustomEnvelope) {
                    deltaTime = ((ConkerCSPOscInit)seqp->initOsc)(
                        &oscState, &oscValue, channel->custom.tremType,
                        channel->custom.tremRate, channel->custom.tremDepth,
                        channel->custom.tremDelay, channel->custom.oscArgument);
                } else {
                    deltaTime = ((ConkerCSPOscInit)seqp->initOsc)(
                        &oscState, &oscValue, inst->tremType, inst->tremRate,
                        inst->tremDepth, inst->tremDelay, channel->custom.oscArgument);
                }
                if (deltaTime) {
                    evt.type = AL_TREM_OSC_EVT;
                    evt.msg.osc.vs = vstate;
                    evt.msg.osc.oscState = oscState;
                    n_alEvtqPostEvent(&seqp->evtq, &evt, deltaTime, 0);
                    vstate->flags |= 1;
                    ((ConkerCSPVoiceOscState *)vstate)->tremOscState = oscState;
                }
            }
            vstate->tremelo = (u8)oscValue;
            oscValue = 1.0f;
            if (channel->custom.useCustomEnvelope) {
                type = channel->custom.vibType;
            } else {
                type = inst->vibType;
            }
            if (type && seqp->initOsc) {
                if (channel->custom.useCustomEnvelope) {
                    deltaTime = ((ConkerCSPOscInit)seqp->initOsc)(
                        &oscState, &oscValue, channel->custom.vibType,
                        channel->custom.vibRate, channel->custom.vibDepth,
                        channel->custom.vibDelay, channel->custom.oscArgument);
                } else {
                    deltaTime = ((ConkerCSPOscInit)seqp->initOsc)(
                        &oscState, &oscValue, inst->vibType, inst->vibRate,
                        inst->vibDepth, inst->vibDelay, channel->custom.oscArgument);
                }
                if (deltaTime) {
                    evt.type = AL_VIB_OSC_EVT;
                    evt.msg.osc.vs = vstate;
                    evt.msg.osc.oscState = oscState;
                    evt.msg.osc.chan = chan;
                    n_alEvtqPostEvent(&seqp->evtq, &evt, deltaTime, 0);
                    vstate->flags |= 2;
                    ((ConkerCSPVoiceOscState *)vstate)->vibOscState = oscState;
                }
            }
            vstate->vibrato = oscValue;
            pitch = vstate->pitch * channel->standard.pitchBend * vstate->vibrato;
            fxmix = func_1001B310(vstate, (N_ALSeqPlayer *)seqp);
            filterEnabled = channel->standard.unk14;
            if (filterEnabled) {
                filterFrequency = func_1001CEA4(cents / 100 +
                    (u8)channel->standard.unk15 - 64) * 440.0f *
                    channel->standard.pitchBend;
            } else {
                filterFrequency = 127.0f;
            }
            pan = __n_vsPan(vstate, (N_ALSeqPlayer *)seqp);
            vol = __n_vsVol(vstate, (N_ALSeqPlayer *)seqp);
            if (channel->custom.useCustomEnvelope) {
                deltaTime = channel->custom.attackTime;
            } else {
                deltaTime = sound->envelope->attackTime;
            }
            n_alSynStartVoiceParams(voice, sound->wavetable, pitch, vol,
                pan, fxmix, filterEnabled, filterFrequency,
                channel->standard.unk16, deltaTime);
            evt.type = AL_SEQP_ENV_EVT;
            evt.msg.vol.voice = voice;
            if (channel->custom.useCustomEnvelope) {
                evt.msg.vol.vol = channel->custom.decayVolume;
                evt.msg.vol.delta = channel->custom.decayTime;
            } else {
                evt.msg.vol.vol = sound->envelope->decayVolume;
                evt.msg.vol.delta = sound->envelope->decayTime;
            }
            n_alEvtqPostEvent(&seqp->evtq, &evt, deltaTime, 0);
            if (midi->duration) {
                evt.type = AL_CSP_NOTEOFF_EVT;
                evt.msg.midi.status = chan | AL_MIDI_NoteOff;
                evt.msg.midi.byte1 = key;
                evt.msg.midi.byte2 = 0;
                deltaTime = seqp->uspt * midi->duration;
                D_80042810[chan] = deltaTime;
                n_alEvtqPostEvent(&seqp->evtq, &evt, deltaTime, 0);
            }
            if ((channel->standard.unk17 & 1) && seqp->unk84) {
                osSendMesg((OSMesgQueue *)seqp->unk84,
                    (OSMesg)((D_80042810[chan] & ~0xFF) |
                    (channel->standard.unk17 >> 2)), OS_MESG_NOBLOCK);
            }
            break;
        }
        /* A zero-velocity note-on is a note-off. */
    case AL_MIDI_NoteOff:
        vstate = func_1001AFEC((N_ALSeqPlayer *)seqp, key, chan);
        if (!vstate) {
            return;
        }
        channel = (ConkerCSPChanState *)&seqp->chanState[chan];
        if (vstate->phase == AL_PHASE_SUSTAIN) {
            vstate->phase = AL_PHASE_SUSTREL;
        } else {
            vstate->phase = AL_PHASE_RELEASE;
            if (channel->custom.useCustomEnvelope) {
                __n_seqpReleaseVoice((N_ALSeqPlayer *)seqp, &vstate->voice,
                                    channel->custom.releaseTime);
            } else {
                __n_seqpReleaseVoice((N_ALSeqPlayer *)seqp, &vstate->voice,
                                    vstate->sound->envelope->releaseTime);
            }
        }
        if ((channel->standard.unk17 & 2) && seqp->unk84) {
            osSendMesg((OSMesgQueue *)seqp->unk84,
                (OSMesg)((key << 16) | 8 | (channel->standard.unk17 >> 2)),
                OS_MESG_NOBLOCK);
        }
        break;

    case AL_MIDI_PolyKeyPressure:
        vstate = func_1001AFEC((N_ALSeqPlayer *)seqp, key, chan);
        if (!vstate) {
            return;
        }
        vstate->velocity = byte2;
        n_alSynSetVol(&vstate->voice, __n_vsVol(vstate, (N_ALSeqPlayer *)seqp),
                     __n_vsDelta(vstate, seqp->curTime));
        break;

    case AL_MIDI_ChannelPressure:
        {
            N_ALVoiceState *vs;
            for (vs = seqp->vAllocHead; vs != NULL; vs = vs->next) {
                if (vs->channel == chan) {
                    vs->velocity = byte1;
                    n_alSynSetVol(&vs->voice, __n_vsVol(vs, (N_ALSeqPlayer *)seqp),
                                 __n_vsDelta(vs, seqp->curTime));
                }
            }
        }
        break;

    case AL_MIDI_ControlChange:
        {
            ConkerCSPControl control;
            if (byte1 < 0x5D) {
                control = D_8002BA50[byte1];
            } else if (byte1 >= 0xFC) {
                control = D_8002BFC0[-byte1];
            } else {
                control = NULL;
            }
            if (control) {
                /* Retail retains this disabled channel-specific check. */
                if (1) {
                } else if (chan == 2) {
                }
                control(seqp, event, chan, byte2);
            }
        }
        break;

    case AL_MIDI_ProgramChange:
        type = (seqp->chanState[chan].unk8 << 7) + key;
        if (type < seqp->bank->instCount) {
            if (func_1001B7D0((N_ALSeqPlayer *)seqp, type, chan)) {
                evt.type = AL_SEQP_MIDI_EVT;
                evt.msg.midi.ticks = 0;
                evt.msg.midi.status = chan | AL_MIDI_ProgramChange;
                evt.msg.midi.byte1 = key;
                evt.msg.midi.byte2 = 0;
                n_alEvtqPostEvent(&seqp->evtq, &evt, 0x8235, 0);
            }
        } else {
        }
        break;

    case AL_MIDI_PitchBendChange:
        {
            s32 bendVal;
            f32 bendRatio;
            s32 cents;
            N_ALVoiceState *vs;

            bendVal = (byte2 << 7) + byte1 - 8192;
            cents = (seqp->chanState[chan].bendRange * bendVal) / 8192;
            bendRatio = alCents2Ratio(cents);
            seqp->chanState[chan].pitchBend = bendRatio;
            for (vs = seqp->vAllocHead; vs != NULL; vs = vs->next) {
                if (vs->channel == chan) {
                    n_alSynSetPitch(&vs->voice, vs->pitch * bendRatio * vs->vibrato);
                    if (seqp->chanState[chan].unk14) {
                        func_1001CA90(&vs->voice, func_1001CEA4(
                            (u8)seqp->chanState[chan].unk15 +
                            (vs->key - vs->sound->keyMap->keyBase) - 64) *
                            440.0f * bendRatio * vs->vibrato);
                    }
                }
            }
        }
        break;

    default:
        break;
    }
}

void __n_CSPHandleMetaMsg(N_ALCSPlayer *seqp, N_ALEvent *event)
{
  ALTempoEvent    *tevt = &event->msg.tempo;
  s32             tempo;
  s32             oldUspt;
  u32             ticks;
  ALMicroTime         tempDelta,curDelta = 0;
  N_ALEventListItem     *thisNode,*nextNode,*firstTemp = 0;
  N_ALEventListItem     *temp0,*temp1,*temp2;

  if (event->msg.tempo.status == AL_MIDI_Meta) {
    if (event->msg.tempo.type == AL_MIDI_META_TEMPO) {
      oldUspt = seqp->uspt;
      tempo = (tevt->byte1 << 16) | (tevt->byte2 <<  8) | (tevt->byte3 <<  0);
      __n_setUsptFromTempo (seqp, (f32)tempo);    /* sct 1/8/96 */

      thisNode = (N_ALEventListItem*)seqp->evtq.allocList.next;
      while (thisNode) {
          curDelta += thisNode->delta;
          nextNode = (N_ALEventListItem*)thisNode->node.next;
          if (thisNode->evt.type == 0x16 ) { // AL_CSP_NOTEOFF_EVT
              // custom
              temp0 = thisNode;
              if (temp0->node.next) {
                  temp0->node.next->prev = temp0->node.prev;
              }
              if (temp0->node.prev) {
                  temp0->node.prev->next = temp0->node.next;
              }
              if (firstTemp != 0) {
                  temp1 = thisNode;
                  if (1) {
                      temp2 = firstTemp;

                      temp1->node.next = temp2->node.next;
                      temp1->node.prev = temp2;

                      if (temp2->node.next != 0) {
                          temp2->node.next->prev = temp1;
                      }
                      temp2->node.next = temp1;
                  }
              } else {
                    thisNode->node.next = 0;
                    thisNode->node.prev = 0;
                    firstTemp = thisNode;
              }

              tempDelta = curDelta;                   /* record the current delta */
              if (nextNode)                           /* don't do this if no nextNode */ {
                  curDelta -= thisNode->delta;        /* subtract out this delta */
                  nextNode->delta += thisNode->delta; /* add it to next event */
              }
              thisNode->delta = tempDelta;            /* set this event delta from current */
          }
          thisNode = nextNode;
      }

      thisNode = firstTemp;
      while (thisNode) {
          nextNode = (N_ALEventListItem*)thisNode->node.next;
          ticks = thisNode->delta/oldUspt;
          thisNode->delta = ticks * seqp->uspt;
          __n_CSPRepostEvent(&seqp->evtq,thisNode);
          thisNode = nextNode;
      }
    }
  }
}

/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_csplayer/__n_CSPRepostEvent.s. */
void __n_CSPRepostEvent(ALEventQueue *evtq, N_ALEventListItem *item)
{
	ALLink *node;
	N_ALEventListItem *nextItem;
	ALLink *element;
	ALLink *after;
	ALLink *element2;
	ALLink *after2;

	for (node = &evtq->allocList; node != 0; node = node->next) {
		if (!node->next) {
			element = (ALLink *)item;
			after = node;
			element->next = after->next;
			element->prev = after;
			if (after->next != NULL) {
				after->next->prev = element;
			}
			after->next = element;
			break;
		} else {
			nextItem = (N_ALEventListItem *)node->next;

			if (item->delta < nextItem->delta) {
				nextItem->delta -= item->delta;
				element2 = (ALLink *)item;
				after2 = node;
				element2->next = after2->next;
				element2->prev = after2;
				if (after2->next != NULL) {
					after2->next->prev = element2;
				}
				after2->next = element2;
				break;
			}

			item->delta -= nextItem->delta;
		}
	}

}


void __n_setUsptFromTempo (N_ALCSPlayer *seqp, f32 tempo)
{
  if (seqp->target)
    seqp->uspt = (s32)((f32)tempo * seqp->target->qnpt);
  else
    seqp->uspt = 488;    /* This is the initial value set by alSeqpNew. */
}

void __n_CSPPostNextSeqEvent(N_ALCSPlayer *seqp)
{
  N_ALEvent   evt;
  s32    deltaTicks;

  if (seqp->state != AL_PLAYING || seqp->target == NULL)
    return;

  /* Get the next event time in ticks. */
  /* If false is returned, then there is no next delta (ie. end of sequence reached). */
  if (!__alCSeqNextDelta(seqp->target, &deltaTicks))
    return;

  evt.type = AL_SEQ_REF_EVT;
  n_alEvtqPostEvent(&seqp->evtq, &evt, deltaTicks * seqp->uspt, 0);
}
