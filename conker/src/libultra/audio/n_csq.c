#include <n_libaudio.h>

/* Generated placeholder declarations. */
s32 __n_alCSeqGetTrackEvent();
/* End generated placeholder declarations. */

/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_csq/n_alCSeqNew.s. */
void n_alCSeqNew(ALCSeq *seq, u8 *ptr) {
}
/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_csq/n_alCSeqNextEvent.s. */
void n_alCSeqNextEvent(ALCSeq *seq, N_ALEvent *evt) {
}
/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_csq/__n_alCSeqGetTrackEvent.s. */
s32 __n_alCSeqGetTrackEvent() {
    return 0;
}
void func_100186DC(ALCSeq *seq, ALCSeqMarker *marker) {
    s32 i;

    seq->validTracks = marker->validTracks;
    seq->lastTicks = marker->lastTicks;
    seq->lastDeltaTicks = marker->lastDeltaTicks;

    for (i = 0; i < 16; i++) {
        seq->curLoc[i] = marker->curLoc[i];
        seq->curBUPtr[i] = marker->curBUPtr[i];
        seq->curBULen[i] = marker->curBULen[i];
        seq->lastStatus[i] = marker->lastStatus[i];
        seq->evtDeltaTicks[i] = marker->evtDeltaTicks[i];
    }
}

/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/n_csq/func_10018790.s. */
void func_10018790(void *arg0, s32 arg1, u32 arg2, u32 arg3) {
}

u8 __getTrackByte(ALCSeq *seq, s32 track) {
    u8 theByte;

    if (seq->curBULen[track]) {
        theByte = *seq->curBUPtr[track];
        seq->curBUPtr[track]++;
        seq->curBULen[track]--;
    } else {
        theByte = *seq->curLoc[track];
        seq->curLoc[track]++;
        if (theByte == AL_CMIDI_BLOCK_CODE) {
            u8 loBackUp, hiBackUp, theLen, nextByte;
            u32 backup;

            nextByte = *seq->curLoc[track];
            seq->curLoc[track]++;
            if (nextByte != AL_CMIDI_BLOCK_CODE) {
                hiBackUp = nextByte;
                loBackUp = *seq->curLoc[track];
                seq->curLoc[track]++;
                theLen = *seq->curLoc[track];
                seq->curLoc[track]++;
                backup = (u32) hiBackUp;
                backup <<= 8;
                backup += loBackUp;
                seq->curBUPtr[track] = seq->curLoc[track] - (backup + 4);
                seq->curBULen[track] = (u32)theLen;
                theByte = *seq->curBUPtr[track];
                seq->curBUPtr[track]++;
                seq->curBULen[track]--;
            }
        }
    }
    return theByte;
}

u32 __readVarLen(ALCSeq *seq, s32 track) {
    u32 value;
    u32 c;

    value = __getTrackByte(seq, track);
    if (value & 0x80) {
        value &= 0x7F;
        do
        {
            c = __getTrackByte(seq, track);
            value = (value << 7) + (c & 0x7F);
        } while (c & 0x80);
    }
    return value;
}
