This page is to track any useful bits and pieces discovered.

# Compression

## Discord chat

> **gamemasterplc Today at 19:16**
>
> the compressed code is split into 4096 byte chunks
>
> the 4096 bytes is the decompressed size
>
> they abuse the bad virtual address handler to load compressed chunks
>
> i know they use one of the rare gzip compressions for these chunks
>
> one chunk is at 0x42C50
>
> the table of chunks is at 0x42454 but is encrypted with a xor key of 0x8039CCCA
>
> and based with the rom address 0x42450
>
> also there is a length of the data chunk at 0x42450


Rodata

> literal strings first, in order, then everything else (floats, doubles, jump tables) after, in order again

## gedecompress

[gedecompress](https://github.com/jombo23/N64-Tools/tree/master/GEDecompressor) is a tool can extract a bunch of stuff from the rom. This tool is no longer required, n64splat + python scripts can extract all compressed assets from all 4 ROMs.

# Function names

```
0x800226f0,bzero/_bzero/blkclr/_blkclr
0x80022a30,__osSetSR
0x80022a40,__osGetSR
0x80022a50,__osSetFpcCsr
0x80022a60,osStartThread
0x80022bb0,osSetThreadPri
0x80022c90,osInvalICache
0x80022d10,osInvalDCache
0x80022dc0,__osDisableInt
0x80022de0,__osRestoreInt
0x80022e00,osStopThread
0x80022ec0,memcpy
0x80022eec,strlen
0x80022f14,strchr
0x80022f60,lldiv
0x80023060,ldiv
0x800230f0,_Litob
0x80023390,__osAiDeviceBusy
0x800233c0,osVirtualToPhysical
0x80023440,osRecvMesg
0x80023580,osSendMesg
0x80023790,osCreateMesgQueue
0x800237c0,osSetEventMesg
0x80023830,osGetThreadPri
0x80023850,osPiRawStartDma
0x80023930,osEPiRawStartDma
0x80023a10,bcopy/_bcopy
0x80023d20,osWritebackDCache
0x80023da0,__osSpSetStatus
0x80023db0,__osSpSetPc
0x80023df0,__osSpRawStartDma
0x80023e80,__osSpDeviceBusy
0x800242b0,__osViInit
0x80024400,__osGetActiveQueue
0x80024400,osPiGetDeviceType
0x80024400,__osViGetNextContext
0x80024400,__osGetCurrFaultedThread
0x80024400,__osViGetCurrentContext
0x80024410,__osViSwapContext
0x80024770,osGetCount
0x80024780,__osDequeueThread
0x800247c0,osViSetMode
0x80024830,osViSwapBuffer
0x80024880,osSetIntMask
0x80024920,osPiStartDma
0x80024a30,osAiGetStatus
0x80024a40,osSetTimer
0x80024b20,osSpTaskYielded
0x80024ba0,osSpTaskYield
0x80024bc0,osContStartReadData
0x80024c84,osContGetReadData
0x80024ea0,osViSetEvent
0x80024f10,osWritebackDCacheAll
0x80024f40,osGetTime
0x80024fd0,osPfsIsPlug
0x80025170,__osPfsRequestData
0x8002526c,__osPfsGetInitData
0x80025340,osContInit
0x80025538,__osContGetInitData
0x80025608,__osPackRequestData
0x800257c0,__osSiRawStartDma
0x80025870,__osContRamWrite
0x80025c20,__osContRamRead
0x80025fd0,__osContAddressCrc
0x80026080,__osContDataCrc
0x80026150,osDestroyThread
0x80026250,osViBlack
0x800262c0,osPiGetStatus
0x800262d0,osUnmapTLB
0x80026310,osMapTLB
0x800263d0,osAiSetFrequency
0x80026530,sqrtf
0x80026540,__sinf/fsin/sinf
0x80026700,__osSiRawReadIo
0x80026700,__osSpRawReadIo
0x80026750,__osSpRawWriteIo
0x80026750,__osSiRawWriteIo
0x800267a0,osPiRawReadIo
0x80026800,__ull_rshift
0x8002682c,__ull_rem
0x80026868,__ull_div
0x800268a4,__ll_lshift
0x800268d0,__ll_rem
0x8002690c,__ll_div
0x80026968,__ll_mul
0x80026998,__ull_divremi
0x800269f8,__ll_mod
0x80026a94,__ll_rshift
0x80026ac0,__osSetHWIntrRoutine
0x80026b10,__osLeoInterrupt
0x800273d0,__osProbeTLB
0x80027490,__osSetCompare
0x800274a0,osJamMesg
0x800275f0,osPiGetCmdQueue
0x80027620,__osSpGetStatus
0x80027630,__osSiDeviceBusy
0x80027660,osPfsInit
0x80027714,__osPfsGetStatus
0x80027820,osLeoDiskInit
0x80027910,__osSumcalc
0x8002796c,__osIdCheckSum
0x800279d4,__osRepairPackId
0x80027dec,__osCheckPackId
0x80027f84,__osGetId
0x800281e0,__osCheckId
0x800282dc,__osPfsRWInode
0x800285fc,__osPfsSelectBank
0x80028670,osPfsChecker
0x80028d34,corrupted_init
0x80028ee8,corrupted
0x8002be30,osViModePalLan1
0x8002be80,osViModeMpalLan1
0x8002bed0,osViModeNtscLan1
0x8002c850,__osRcpImTable
0x8002c920,__libm_qnan_f
```
via [Encryption64](http://en64.shoutwiki.com/wiki/Conker%27s_Bad_Fur_Day)

## memory ranges

```
/* 80000000 RDRAM */
/* A3F00000 RDRAM Registers */
/* A4000000 SP DMEM */
/* A4040000 SP Registers */
/* A4080000 SP PC Register */
/* A4100000 DP Control Registers */
/* A4300000 MI Registers */
/* A4400000 VI Registers */
/* A4500000 AI Registers */
/* A4600000 PI Registers */
/* A4700000 RI Registers */
/* A4800000 SI Registers */
/* A5000000 DD Registers */
/* A8000000 Cartridge Save Data */
/* B8000000 Cartridge ROM */
/* BFC00000 PIF ROM */
/* BFC007C0 PIF RAM */
```