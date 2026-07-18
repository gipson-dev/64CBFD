#include <n_libaudio.h>
#include "n_sndp.h"

/* Generated placeholder declarations. */
void func_10019D98(N_ALCSPlayer *seqp, u8 chan);
void func_1001A030(N_ALCSPlayer *seqp, s32 arg1, s32 chan, u32 sustain);
void func_1001A508(N_ALCSPlayer *seqp, N_ALEvent *event, s32 chan, s32 target);
void func_1001A704(N_ALCSPlayer *seqp, s32 event, s32 chan, s32 arg3);
void func_1001CA90(N_ALVoice *voice, f32 pitch);
f32 func_1001CEA4(s32 cents);
extern f32 fabsf(f32);
#pragma intrinsic (fabsf)
/* End generated placeholder declarations. */

#define CSP_MIN_RELEASE_TIME 0x3E80
#define CSP_DEFAULT_CHL_FADE_SPEED 0x88
#define CSP_CHL_FADE_DURATION_MASK 0x7F
#define CSP_CHL_FADE_STEP_EVENT 0xFE

void func_10019B50(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 vol) {
    N_ALSoundState *state;
    s16 tmp;
    seqp->chanState[chan].vol = vol;
    for(state = seqp->vAllocHead; state != NULL; state = state->voice.node.next) {
        if ((state->chan == chan) && (state->unk38 != 3)) {
            tmp = __n_vsVol(state, seqp);
            n_alSynSetVol(&state->voice.node.prev, tmp, __n_vsDelta(state, seqp->curTime));
        }
    }
}

void func_10019C28(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 pan) {
    N_ALSoundState *state;
    u8 tmp;
    seqp->chanState[chan].pan = pan;
    for (state = seqp->vAllocHead; state != NULL; state = state->voice.node.next) {
        if ((state->chan == chan)) {
            tmp = __n_vsPan(state, seqp);
            func_1001E2A0(&state->voice.node.prev, tmp);
        }
    }
}

void func_10019CD0(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 priority) {
    seqp->chanState[chan].priority = priority;
}

void func_10019CFC(N_ALCSPlayer *seqp, s32 arg1, s32 arg2, s32 arg3) {
    if (seqp->unk84 != 0) {
        osSendMesg(seqp->unk84, (arg3 & 7) | 0x10 | ((seqp->node.samplesLeft << 5) & -0x100), 0);
    }
}

void func_10019D6C(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    seqp->chanState[chan].unk8 = arg3;
}

void func_10019D98(N_ALCSPlayer *seqp, u8 chan) {
    N_ALVoiceState *voiceState;
    s16 filter12;
    s8 pitchOffset;
    f32 pitchBend;

    pitchOffset = seqp->chanState[chan].unk15 - 0x40;
    pitchBend = seqp->chanState[chan].pitchBend;

    for (voiceState = seqp->vAllocHead; voiceState != NULL; voiceState = voiceState->next) {
        if (voiceState->channel == chan) {
            filter12 = seqp->chanState[chan].unk14;
            n_alSynSetPan(&voiceState->voice, filter12);
            if (filter12 != 0) {
                func_1001CA90(&voiceState->voice,
                              func_1001CEA4((voiceState->key - voiceState->sound->keyMap->keyBase) + pitchOffset) *
                                  440.0f * pitchBend);
            }
        }
    }
}

void func_10019ED8(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    seqp->chanState[chan].unk14 = arg3;
    func_10019D98(seqp, chan);
}

void func_10019F38(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    seqp->chanState[chan].unk15 = arg3;
    func_10019D98(seqp, chan);
}

void func_10019F98(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    N_ALSoundState *state;
    seqp->chanState[chan].unk16 = arg3;
    for (state = seqp->vAllocHead; state != NULL; state = state->voice.node.next) {
        if (state->chan == chan) {
            func_1001E350(&state->voice.node.prev, arg3);
        }
    }
}

void func_1001A030(N_ALCSPlayer *seqp, s32 arg1, s32 chan, u32 sustain) {
    N_ALVoiceState *state;
    register s32 releaseTime;

    seqp->chanState[chan].sustain = sustain;
    for (state = seqp->vAllocHead; state != NULL; state = state->next) {
        if ((state->channel == chan) && (state->phase != AL_PHASE_RELEASE)) {
            if (sustain >= (AL_SUSTAIN + 1)) {
                if (state->phase == AL_PHASE_NOTEON) {
                    state->phase = AL_PHASE_SUSTAIN;
                }
            } else {
                if (state->phase == AL_PHASE_SUSTAIN) {
                    state->phase = AL_PHASE_NOTEON;
                } else if (state->phase == AL_PHASE_SUSTREL) {
                    state->phase = AL_PHASE_RELEASE;
                    if (((N_ALCSPExtraChanState *) &seqp->chanState[chan])->useCustomReleaseTime) {
                        if (((N_ALCSPExtraChanState *) &seqp->chanState[chan])->releaseTime < CSP_MIN_RELEASE_TIME) {
                            releaseTime = CSP_MIN_RELEASE_TIME;
                        } else {
                            releaseTime = ((N_ALCSPExtraChanState *) &seqp->chanState[chan])->releaseTime;
                        }
                        __n_seqpReleaseVoice((N_ALSeqPlayer *) seqp, &state->voice, releaseTime);
                    } else {
                        if (state->sound->envelope->releaseTime < CSP_MIN_RELEASE_TIME) {
                            releaseTime = CSP_MIN_RELEASE_TIME;
                        } else {
                            releaseTime = state->sound->envelope->releaseTime;
                        }
                        __n_seqpReleaseVoice((N_ALSeqPlayer *) seqp, &state->voice, releaseTime);
                    }
                }
            }
        }
    }
}

void func_1001A224(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    N_ALSoundState *state;

    seqp->chanState[chan].fxmix = (seqp->chanState[chan].fxmix & 0x7F) | (arg3 << 7);
    for (state = seqp->vAllocHead; state != NULL; state = state->voice.node.next) {
        if ((state->chan == chan) && (state->unk38 != 3)) {
            n_alSynSetFXMix(&state->voice.node.prev, seqp->chanState[chan].fxmix);
        }
    }
}

void func_1001A2F8(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    arg3 = arg3 & 0x7F;
    seqp->chanState[chan].fxmix = (seqp->chanState[chan].fxmix & 0x80) | arg3;
    func_1001A224(seqp, arg1, chan, seqp->chanState[chan].fxmix >> 7);
}

void func_1001A39C(N_ALCSPlayer *seqp, s32 arg1, s32 chan, u32 arg3) {
    if (arg3 < n_syn->maxAuxBusses) {
        seqp->chanState[chan].unkB = arg3;
    }
}

// FIXME:
typedef struct {
    u8 pad0[0x36];
    u8 unk36;
} struct24;

void func_1001A3E0(struct24 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    arg0->unk36 = arg3;
}

void func_1001A3FC(struct24 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    func_1001263C(arg0->unk36 * 100 + arg3, 0x7FFF, 0x40);
}

void func_1001A45C(N_ALCSPlayer *seqp, s32 chan) {
    N_ALSoundState *state;
    s16 vol;

    for (state = seqp->vAllocHead; state != NULL; state = state->voice.node.next) {
        if ((state->chan == (u8)chan) && (state->unk38 != 3)) {
            vol = __n_vsVol(state, seqp);
            n_alSynSetVol(&state->voice.node.prev, vol, __n_vsDelta(state, seqp->curTime));
        }
    }
}

void func_1001A508(N_ALCSPlayer *seqp, N_ALEvent *event, s32 chan, s32 target) {
    f32 fadeDelta;

    if (seqp->chanState[chan].unkF == 0) {
        seqp->chanState[chan].unkF = CSP_DEFAULT_CHL_FADE_SPEED;
    }
    if (seqp->chanState[chan].unkE != target) {
        fadeDelta = target - seqp->chanState[chan].unkD;
        seqp->chanState[chan].unk10 = fadeDelta / (seqp->chanState[chan].unkF & CSP_CHL_FADE_DURATION_MASK);
        seqp->chanState[chan].unk10 = fabsf(seqp->chanState[chan].unk10);
        if (seqp->chanState[chan].unkE == seqp->chanState[chan].unkD) {
            seqp->chanState[chan].unkE = target;
        } else {
            seqp->chanState[chan].unkE = target;
            return;
        }
    } else {
        return;
    }
    event->msg.midi.byte1 = CSP_CHL_FADE_STEP_EVENT;
    func_1001A704(seqp, (s32) event, chan, target);
}

void func_1001A704(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    u8 sp2F;
    u8 sp2E;
    s32 sp28;
    s32 sp24;
    f32 sp20;
    f32 sp1C;

    sp2F = seqp->chanState[chan].unkD;
    sp2E = seqp->chanState[chan].unkE;
    sp20 = seqp->chanState[chan].unk10;
    sp28 = sp2E - sp2F;
    if (sp28 > 0) {
        if (seqp->chanState[chan].unkF & 0x80) {
            sp20 = sp20 * 2.0f;
        }
        sp24 = sp20;
        if (sp24 == 0) {
            sp24 = 1;
            sp1C = 1.0f / sp20;
        } else {
            sp1C = sp24 / sp20;
        }
        if (sp28 > sp24) {
            sp28 = sp24;
        }
    } else {
        sp24 = sp20;
        if (sp24 == 0) {
            sp24 = 1;
            sp1C = sp20;
        } else {
            sp1C = sp24 / sp20;
        }
        sp24 = -sp24;
        if (sp28 < sp24) {
            sp28 = sp24;
        }
    }
    sp2F = sp28 + sp2F;
    seqp->chanState[chan].unkD = sp2F;
    if (sp2F != sp2E) {
        n_alEvtqPostEvent(&seqp->evtq, arg1, seqp->uspt * 100 * sp1C, 2);
    }
    if (sp2F != 0) {
        seqp->chanMask |= (1 << chan);
    } else {
        seqp->chanMask &= ~(1 << chan);
    }
    func_1001A45C(seqp, chan);
}

void func_1001A9DC(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    seqp->chanState[chan].unkF = arg3;
}

void func_1001AA08(N_ALCSPlayer *seqp, s32 arg1, s32 chan, s32 arg3) {
    seqp->chanState[chan].unkD = arg3;
    seqp->chanState[chan].unkE = arg3;
    if (arg3 == 0) {
        seqp->chanMask &= (1 << chan) ^ 0xFFFF; // disable
    } else {
        seqp->chanMask |= 1 << chan;
    }
    func_1001A45C(seqp, chan);
}
