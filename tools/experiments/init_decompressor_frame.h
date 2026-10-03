#ifndef INIT_DECOMPRESSOR_FRAME_H
#define INIT_DECOMPRESSOR_FRAME_H

/* Physical retail scratch/save view, not an ordinary C-callable guest ABI. */
typedef struct {
    unsigned int counts[17];
    unsigned int tables[16];
    unsigned int sorted[288];
    unsigned int offsets[17];
    union {
        unsigned int lengths[316];
        struct {
            unsigned int lengths[288];
            unsigned short literalRoot;
            unsigned short pad9CA;
            unsigned int literalBits;
            unsigned short distanceRoot;
            unsigned short pad9D2;
            unsigned int distanceBits;
            unsigned char remaining[0x60];
        } fixed;
    } staging;
    unsigned short literalRoot;
    unsigned short distanceRoot;
    unsigned int literalBits;
    unsigned int distanceBits;
    unsigned int wrapperReturn;
    unsigned int savedS[8];
    unsigned int dispatcherReturn;
    unsigned int streamReturn;
    unsigned int finalBlock;
    unsigned int savedWorkspace;
    unsigned int savedFp;
    unsigned int savedGp;
    unsigned int entryReturn;
    unsigned int padA84;
} InitDecodeFrame;

#endif
