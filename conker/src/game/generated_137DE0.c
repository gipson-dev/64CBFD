#include <ultra64.h>
extern u8 D_800917EC[];
extern f32 D_800A26A0;
void *func_15169968(void *);
typedef struct {
    u8 *asset;
    u32 retained04;
    u32 packedFirstSecond;
    u32 packedThirdSum;
    s32 field10;
    s16 sum;
    s16 field16;
    s16 field18;
    u8 retained1A[2];
    f32 field1C;
    f32 field20;
    s16 field24,field26,field28,field2A,field2C,field2E;
    u8 field30,field31,field32,field33,field34,field35,field36,field37;
    u8 retained38;
    u8 field39;
    u8 retained3A[2];
} PackedArgumentDescriptor;

/* Pack three argument words and their wrapping sum into the copied descriptor. */
void *func_1510A930(u32 first,u32 second,u32 third) {
    PackedArgumentDescriptor descriptor;
    u32 sum=first+second+third;
    u32 packed=(first<<16)|second;
    descriptor.asset=D_800917EC;
    descriptor.field30=10;
    descriptor.field2C=64;
    descriptor.field2E=32;
    descriptor.field28=0x18FC;
    descriptor.field2A=0x1A12;
    descriptor.field36=7;
    descriptor.field39=0;
    descriptor.packedFirstSecond=packed;
    descriptor.packedThirdSum=(third<<16)|sum;
    descriptor.field10=10000;
    descriptor.sum=sum;
    descriptor.field18=0;
    descriptor.field24=0;
    descriptor.field26=0;
    descriptor.field31=1;
    descriptor.field32=255;
    descriptor.field33=255;
    descriptor.field34=255;
    descriptor.field37=17;
    descriptor.field35=0;
    descriptor.field16=0;
    descriptor.field1C=228.0f;
    descriptor.field20=D_800A26A0;
    return func_15169968(&descriptor);
}
