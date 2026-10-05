#include <n_libaudio.h>

#include "macros.h"

/* Generated placeholder declarations. */
void func_10008180(void);
s32 func_10008CE8(u8 arg0, s32 arg1);
/* End generated placeholder declarations. */

typedef struct {
  u8 pad0[0x760];
} struct247; // something naudio related?

typedef struct {
  s32 unused;
  s32 source;
} SequenceMetadata;

typedef struct {
    s32 bankControl;
    s32 bankCount;
    s32 bankTable;
} AudioResourceConfig;

typedef struct {
    s32 maxVoices;
    s32 maxEvents;
    u8 maxChannels;
    u8 debugFlags;
    u8 padA[2];
    ALHeap *heap;
    void *initOsc;
    void *updateOsc;
    void *stopOsc;
} RareSeqpConfig;

extern N_ALCSPlayer *D_8003C900[];
extern N_ALCSPlayer *D_8003C90C;
extern u16           D_8003C910[];
extern u16           D_8003CA3C[];
extern u8           *D_8003CA48[];
extern ALCSeq        D_8003CA58[];
extern SequenceMetadata *D_8003CD40;
extern struct247     D_8003CD48[];
extern ALBank       *D_8003E368;
extern ALHeap        D_8003E370;
extern u8            D_80044B20[];

void *allocate_memory(s32 size, s32 tag, s32 pool, s32 flags);
void func_10004074(void *ptr);
void func_100046E4(s32 source, void *destination, u32 size);
void func_100131FC(void *config, s32 count);
void func_10015550(N_ALCSPlayer *csp, ALBank *bank);
void func_100155A0(N_ALSndpConfig *config);
void func_10017870(s32 count);
void func_10017944(s32 index, s32 value);
u32 func_1502B020(u32 *size, u32 depth, ...);
s32 func_1502B9B4(s32 arg0, s32 arg1, s32 arg2);
u32 func_1502B8E0(void *buffer, u32 cap, u32 depth, ...);

// FIXME: create header file for audio related functions
s32  func_10017A80(N_ALCSPlayer *csp);
void func_10017AF0(N_ALCSPlayer *csp, s32 arg1);
void func_10017B04(N_ALCSPlayer *arg0, s32 arg1, u8 arg2);
void func_10017B30(N_ALCSPlayer *csp);
void func_10017BB8(N_ALCSPlayer *csp, s32 arg1);
void func_10017C00(N_ALCSPlayer *csp, s32 arg1);
void func_10017C68(N_ALCSPlayer *arg0, s32 arg1, u8 arg2, u8 arg3);
void func_10017CE0(N_ALCSPlayer *arg0, s32 arg1, u8 arg2);
void func_10017D30(N_ALCSPlayer *arg0, s32 arg1, u8 arg2);
void func_10017D80(N_ALCSPlayer *arg0, u8 arg1, u8 arg2);
void func_10017DF0(N_ALCSPlayer *csp, f32 arg1, f32 arg2);
void func_10017E4C(N_ALCSPlayer *csp, u8 chan, u8 arg2);
void func_10017F10(N_ALCSPlayer *arg0, u8 arg1, u8 arg2, u8 arg3, s32 arg4);
void func_10018790(N_ALCSPlayer *arg0, s32 arg1, u32 arg2, u32 arg3);
void func_10018D00(N_ALCSPlayer *arg0, s16 arg1);
void func_10018D50(N_ALCSPlayer *seqp);

void func_10008180(void) {
    N_ALSndpConfig sndpConfig;
    ALSynConfig synthConfig;
    RareSeqpConfig seqpConfig;
    AudioResourceConfig resourceConfig;
    ALBankFile *bankFile;
    ALSeqFile *seqHeader;
    N_ALCSPlayer **player;
    u16 *sequenceId;
    u8 **sequenceData;
    u8 *sequenceCursor;
    u16 *sequenceLength;
    s32 bankFileSize;
    s32 bankControl;
    s32 bankTable;
    s32 sequenceSource;
    s32 sequenceFileSize;
    s32 i;
    s32 length;
    u32 unsignedLength;

    alHeapInit(&D_8003E370, D_80044B20, 0x3E000);

    synthConfig.maxVVoices = 0x2C;
    synthConfig.maxPVoices = 0x28;
    synthConfig.maxUpdates = 0x40;
    synthConfig.maxFXbusses = 2;
    synthConfig.dmaproc = NULL;
    synthConfig.fxTypes[0] = 6;
    synthConfig.fxTypes[1] = 6;
    synthConfig.outputRate = 0;
    synthConfig.heap = &D_8003E370;

    resourceConfig.bankControl = 0x5604;
    resourceConfig.bankCount = 1;
    resourceConfig.bankTable = 0xC00;

    synthConfig.unk24 = (void *)func_1502B020(0, 2, 0x17, 2);
    func_10008F90((s32)&synthConfig, 0xC, (s32)&resourceConfig);

    bankFileSize = func_1502B9B4(2, 0x17, 0);
    bankFile = allocate_memory(bankFileSize, 0xFF, 2, 0);
    func_1502B8E0(bankFile, bankFileSize, 2, 0x17, 0);

    bankControl = func_1502B020(0, 2, 0x17, 1);
    bankTable = func_1502B020(0, 2, 0x17, 2);
    func_10012934(bankFile, (u8 *)bankTable, bankControl);
    D_8003E368 = bankFile->bankArray[0];

    sequenceSource = func_1502B020(0, 2, 0x17, 3);
    seqHeader = allocate_memory(0x10, 1, 2, 0);
    func_100046E4(sequenceSource, seqHeader, 0x10);
    sequenceFileSize = (seqHeader->seqCount * sizeof(ALSeqData)) + 4;
    func_10004074(seqHeader);

    D_8003CD40 = allocate_memory(sequenceFileSize, 0xFF, 2, 0);
    func_100046E4(sequenceSource, D_8003CD40, ALIGN16(sequenceFileSize));
    alSeqFileNew((ALSeqFile *)D_8003CD40, (u8 *)sequenceSource);

    sequenceCursor = (u8 *)D_8003CD40;
    sequenceLength = D_8003C910;
    i = 0;
    do {
        length = *(s32 *)(sequenceCursor + 8);
        i += 8;
        sequenceCursor += 8;
        unsignedLength = length & 0xFFFF;
        *sequenceLength = length;
        if (unsignedLength & 1) {
            *sequenceLength = unsignedLength + 1;
        }
        sequenceLength++;
    } while (i <= 0x4AF);

    seqpConfig.maxVoices = 0x2C;
    seqpConfig.maxEvents = 0x68;
    seqpConfig.debugFlags = 0;
    seqpConfig.maxChannels = 0x10;
    seqpConfig.heap = &D_8003E370;
    func_100131FC(&seqpConfig, 0x58);

    player = D_8003C900;
    sequenceId = D_8003CA3C;
    sequenceData = D_8003CA48;
    do {
        *sequenceId = 0xFFFF;
        *sequenceData = NULL;
        *player = alHeapDBAlloc(0, 0, &D_8003E370, 1, 0x90);
        n_alCSPNew(*player, (ALSeqpConfig *)&seqpConfig);
        func_10015550(*player, bankFile->bankArray[0]);
        player++;
        sequenceId++;
        sequenceData++;
    } while (player != &D_8003C90C);

    sndpConfig.maxEvents = 0x40;
    sndpConfig.maxStates = 0x40;
    sndpConfig.maxSounds = 0x14;
    sndpConfig.maxVolumes = 8;
    sndpConfig.heap = &D_8003E370;
    sndpConfig.soundTableCount = bankTable;
    func_100155A0(&sndpConfig);
    func_10017870(4);
    func_10017944(0, 2);
    func_10017944(1, 2);
}

void func_100084D8(u8 idx) {
    if ((n_alCSPGetState(D_8003C900[idx]) == 0) || (n_alCSPGetState(D_8003C900[idx]) == 3)) {
        func_10017AA0(D_8003C900[idx]);
    }
}

s32 func_1000853C(u8 idx) {
    return n_alCSPGetState(D_8003C900[idx]);
}

void func_10008570(u8 idx, s32 arg1) { // arg1 is OSMesgQueue ?
    func_10017AF0(D_8003C900[idx], arg1);
}

void func_100085A4(s32 arg0, s32 arg1, s32 arg2) {
}

void func_100085B8(u8 idx, s32 arg1, u8 arg2) {
    func_10017B04(D_8003C900[idx], arg1, arg2);
}

void func_100085F8(u8 idx, s32 arg1) {
    func_10017BB8(D_8003C900[idx], arg1);
}

void func_1000862C(u8 idx, s32 arg1) {
    func_10017C00(D_8003C900[idx], arg1);
}

void func_10008660(u8 idx, u8 chan, u8 arg2, s32 arg3) {
    if (arg3 > 0) {
        arg3 = (arg3 * 10) / 60;
        if (arg3 == 0) {
            arg3 = 1; // final?
        } else if (arg3 >= 128) {
            arg3 = 127; // more to come?
        }
    } else {
        arg3 = 0; // empty?
    }
    func_10017C68(D_8003C900[idx], chan, arg2, arg3);
}

void func_100086FC(u8 idx, u8 arg1, u8 arg2) {
    func_10017CE0(D_8003C900[idx], arg1, arg2);
}

void func_10008744(u8 idx, u8 arg1, u8 arg2) {
    func_10017D80(D_8003C900[idx], arg1, arg2);
}

void func_10008790(u8 idx, s32 mask, u8 arg2, s32 arg3) {
    s32 chan;

    for (chan = 0; chan < 16; chan++)
    {
        if ((1 << chan) & mask) {
            func_10008660(idx, chan, arg2, arg3);
        }
    }
}

void func_10008824(u8 idx, u8 arg1, u8 arg2) {
    func_10017D30(D_8003C900[idx], arg1, arg2);
}

void func_1000886C(u8 idx, s32 mask, u8 arg2) {
    s32 chan;

    for (chan = 0; chan < 16; chan++)
    {
        if ((1 << chan) & mask) {
            func_10008824(idx, chan, arg2);
        }
    }
}

void func_100088F0(u8 idx, s32 mask, s32 enable) {
    s32 chan;

    for (chan = 0; chan < 16; chan++)
    {
        if ((1 << chan) & mask) {
            if (enable) {
                func_1000862C(idx, chan);
            } else {
                func_100085F8(idx, chan);
            }
        }
    }
}

void func_10008988(u8 idx, s32 mask, s32 enable) {
    s32 chan;

    for(chan = 0; chan < 16; chan++) // 16 channels
    {
        if ((1 << chan) & mask) {
            if (enable != 0) {
                D_8003C900[idx]->chanMask |= mask; // enable
            } else {
                D_8003C900[idx]->chanMask &= (mask ^ 0xFFFF); // disable
            }
        }
    }
}

// is this n_alCSPGetChlVol ?
u8 func_10008A4C(u8 idx, u8 chan) {
    return D_8003C900[idx]->chanState[chan].unkD; // do we assume this is volume?
}

void func_10008A94(u8 idx, s32 mask, s32 arg2) {
    s32 chan;

    for(chan = 0; chan < 16; chan++)
    {
        if (((1 << chan) & mask) != 0) {
            func_10017E4C(D_8003C900[idx], chan, arg2);
        }
    }
}

void func_10008B2C(u8 idx) {
      n_alCSPGetTempo(D_8003C900[idx]);
}

void func_10008B60(u8 idx, u8 arg1, u8 arg2, u8 arg3, s32 arg4) {
    func_10017F10(D_8003C900[idx], arg1, arg2, arg3, arg4);
}

void func_10008BC0(u8 idx, f32 arg1, f32 arg2) {
    func_10017DF0(D_8003C900[idx], arg1, arg2);
}

void func_10008C04(u8 idx, u8 arg1, s32 arg2) {
    func_10018790(&D_8003CA58[idx], &D_8003CD48[idx], arg1, arg2);
}

void func_10008C6C(u8 idx, u8 arg1) {
    func_100186DC(&D_8003CA58[idx], (u8 *)&D_8003CD48[idx] + (arg1 * 0xEC));
}

s32 func_10008CE8(u8 idx, s32 sequence) {
    s32 source;
    u32 i;

    i = 0;
    func_10018C60(D_8003C900[idx]);
    while ((n_alCSPGetState(D_8003C900[idx]) != 0) && (i < 2000000)) {
        i++;
    }

    if (i >= 2000000) {
        func_10018C60(D_8003C900[idx]);
        while ((n_alCSPGetState(D_8003C900[idx]) != 0) &&
               (i < 4000000)) {
            i++;
        }
    }

    if (sequence != D_8003CA3C[idx]) {
        if (D_8003CA48[idx] != NULL) {
            func_10004074((s32)D_8003CA48[idx]);
            D_8003CA48[idx] = NULL;
        }

        source = D_8003CD40[sequence].source;
        if ((D_8003CA48[idx] =
                 (u8 *)allocate_memory(D_8003C910[sequence], 0xFF, 2, 2)) ==
            NULL) {
            return -1;
        }
        func_10004514(source, D_8003CA48[idx],
                      ALIGN16(D_8003C910[sequence]), 1);
        D_8003CA3C[idx] = sequence;
    }

    n_alCSeqNew(&D_8003CA58[idx], D_8003CA48[idx]);
    func_10018CB0(D_8003C900[idx], &D_8003CA58[idx]);
    func_10017B30(D_8003C900[idx]);
    return 0;
}

void func_10008EE0(u8 idx, s32 arg1) {
    func_10018D00(D_8003C900[idx], arg1);
}

void func_10008F24(u8 idx) {
    // AL_TRACK_END
    func_10018C60(D_8003C900[idx]);
}

void func_10008F58(u8 idx) {
    func_10018D50(D_8003C900[idx]);
}
