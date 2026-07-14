As with every page in the wiki, this is a work-in-progress and will be updated as more information is understood about the ROM.

# Header

The header is pretty straightforward. The one thing of interest is the suggestion that this uses `libultra 2.0G` (Revision: 0x14 => 20, 0x47-> "G"), but there is newer code than G (i.e. the libnaudio), so presumably this is wrong!
```s
.section .header, "a"

.word 0x80371240              /* PI PSD Domain 1 register */
.word 0x0000000F              /* Clockrate setting */
.word 0x80001000              /* Entrypoint address */
.word 0x00001447              /* Revision */
.word 0x30C7AC50              /* Checksum 1 */
.word 0x7704072D              /* Checksum 2 */
.word 0x00000000              /* Unknown 1 */
.word 0x00000000              /* Unknown 2 */
.ascii "CONKER BFD          " /* Internal ROM name */
.word 0x00000000              /* Unknown 3 */
.word 0x0000004E              /* Cartridge */
.ascii "FU"                   /* Cartridge ID */
.ascii "E"                    /* Country code */
.byte 00                      /* Version */
```
# Boot

TBD; has not yet been looked at.

# Code

Three sections of code have been discovered so far:
 - 0x00001000 to 0x000290D0; initialisation code and (some) libultra
 - 0x00042C50 to 0x00186b50; game code (and some libultra) compressed with gzip
 - 0x0019EA88 to 0x001A2190; debugger (and some libultra code)

## 0x1000000

The first section of the game is TLB'd to 0x10000000. 

## 0x1500000

The compressed section is TLB'd to 0x15000000. Compressed pages appear to be paged into 0x80033330 and decompressed.

## 0x1600000

The third (and final?) section is TLB'd to 0x16000000. This appears to be the debugger (as seen in older builds) as well as some duplicate libultra functions.

TODO: investigate ECTS/debug build to see whether we can easily re-enable debugger for retail ROM.

# Assets

The rest of the ROM contains a mixture of compressed and uncompressed sections. 

## compressed

Immediately after the last code section is a compressed chunk. This differs from the later chunks as it do not appear to have a corresponding section in the ROM that gives the individual file offsets.

These sections can be decompressed with the `extract_compressed.py` script and corresponding config yaml. See the [README](https://github.com/mkst/conker/blob/master/config/README.md) for more information.

Contains 7760 files in `us` version, 7762 in `eu`, 7808 in `debug` and 8427 in `ects`.

## assetsXX

After the larged compressed chunk is an offsets table that gives the starts of 20 (0x00 thru 0x1C) additional compressed sections. Each of these compressed sections contains a header with the offsets of the compressed sections within it.

### assets00

2D Animated Sprites

### assets01

3D Character etc. Models 

### assets02

3D Character etc. Animation Skeletons 

`0000.bin` appears to contain 1500+ (file?) offsets followed by some unknown data.

### assets03

3D Objects misc. In-game chocolate piece health model etc.

Contains 77 files

#### 0002.bin

This file is `472` bytes long. In the 'header' of the file are two numbers, 0x00000128 (296) and 0x000000b0 (176), they sum to make `472`.

```
00000000: 0000 0128 0000 00b0 0000 0000 0000 0000  ...(............
00000010: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000020: 0000 0000 8000 0000 0013 0012 0013 001f  ................
00000030: 2656 264e ffff ffff 0021 fffe 0021 0041  &V&N.....!...!.A
00000040: 2803 2804 ffff ffff 0021 fffe ffdf 00c0  (.(......!......
00000050: 281e 2017 ffff ffff 0013 0012 ffed 00e2  (. .............
00000060: 2665 21bd ffff ffff 0021 fffe 0021 0000  &e!......!...!..
00000070: 2803 2804 a7a7 a7ff 0023 fff0 0023 0000  (.(......#...#..
00000080: 2899 289c ffff ffff 0021 fffe ffdf 0000  (.(......!......
00000090: 281e 2017 a7a7 a7ff 0023 fff0 ffdd 0000  (. ......#......
000000a0: 28b7 1f7f ffff ffff ffed 0012 ffed 00dd  (...............
000000b0: 21c8 21aa ffff ffff ffdf fffe ffdf 00d3  !.!.............
000000c0: 201c 1ff6 ffff ffff ffdd fff0 ffdd 00a7   ...............
000000d0: 1f82 1f59 ffff ffff ffdf fffe ffdf 00a7  ...Y............
000000e0: 201c 1ff6 a7a7 a7ff ffed 0012 0013 0018   ...............
000000f0: 21b8 263b ffff ffff ffdf fffe 0021 004e  !.&;.........!.N
00000100: 2001 27e3 ffff ffff ffdd fff0 0023 0000   .'..........#..
00000110: 1f64 2876 ffff ffff ffdf fffe 0021 0000  .d(v.........!..
00000120: 2001 27e3 a7a7 a7ff d700 0002 ffff ffff   .'.............
00000130: e700 0000 0000 0000 fd50 0000 0000 00bb  .........P......
00000140: f550 0000 0700 0000 f300 0000 073f f000  .P...........?..
00000150: f540 0800 0001 8060 f240 2402 004f e4fe  .@.....`.@$..O..
00000160: fd10 0000 0080 00bb f560 0100 0600 0000  .........`......
00000170: e600 0000 0000 0000 f000 0000 0603 c000  ................
00000180: fc12 19ff 5f15 fe3f de00 0000 0800 0040  ...._..?.......@
00000190: d9fa fdff 0000 0000 d9ff ffff 0000 0400  ................
000001a0: 0101 0020 0100 0000 1314 90a6 c011 0043  ... ...........C
000001b0: 1329 18ea c624 2049 15b9 ad4e d096 312d  .)...$ I...N..1-
000001c0: 1794 bdc5 18d0 01a1 1021 8d00 1472 95ca  .........!...r..
000001d0: df00 0000 0000 0000
```

Part of the data is static displaylist:

```c
{
    gsDPPipeSync(),
    gsDPSetTextureImage(G_IM_FMT_CI, G_IM_SIZ_16b, 1, 0x000000BB),
    // ...
    gsDPSetTextureImage(G_IM_FMT_RGBA, G_IM_SIZ_16b, 1, 0x008000BB),
    gsDPSetTile(G_IM_FMT_IA, G_IM_SIZ_4b, 0, 0x0100, 6, 0, G_TX_NOMIRROR | G_TX_WRAP, G_TX_NOMASK, G_TX_NOLOD, G_TX_NOMIRROR | G_TX_WRAP, G_TX_NOMASK, G_TX_NOLOD),
    gsDPLoadSync(),
    gsDPLoadTLUTCmd(6, 15),
    gsDPSetCombineLERP(TEXEL0, ENVIRONMENT, SHADE, PRIMITIVE, TEXEL0, 0, SHADE, 0, 0, 0, 0, COMBINED, COMBINED, 0, ENVIRONMENT, 0),
    gsSPDisplayList(0x08000040),
    gsSPClearGeometryMode(G_CULL_FRONT | G_FOG | G_TEXTURE_GEN),
    gsSPSetGeometryMode(G_CULL_BACK),
    sSPVertex(0x01000000, 16, 0),
    // ...
    gsSPEndDisplayList(),
}
```


### assets04

Level Map/Cutscene Assets

### assets05

Level Culling Data?

### assets06

Contains cutscenes

```sh
mkdir -p text
python3 tools/extract_compressed.py config/assets06.yaml rzip/assets06/assets06.bin text/
```

### assets07

### assets08

Chapters Loader

Contains some compressed files:
```
0x48 268435456 16
0x80 268435456 16
0xe0 268435456 16
0x148 268435456 16
0x1a8 268435456 16
0x1f0 268435456 16
0x258 268435456 16
0x298 268435456 16
0x310 268435456 144
```

### assets09

Weapons, objects from idle animations, misc.

### assets0A

Pause Tail Animation Related?

### assets0B

Level Water and Sub-objects Positions Map Data

### assets0C

Level Environmental Lighting, Interaction Objects, Cameras and Loading Zones

### assets0D

Skybox Related?

### assets0E

Level Actor Loading List

### assets0F

Character Behavior Data

### assets10

Object Movement Radius List?

### assets11

Character Eyes/Misc. Data?

### assets12

Playable Character Voice List Slots

### assets13

Conker's Models Structure?

Contains a handful of compressed files.
```
24 0 0
2264 0 0
3072 0 128
56 268435456 16
368 268435456 16
680 268435456 16
992 268435456 16
1304 268435456 16
1616 268435456 16
1928 268435456 144
```

### assets14

Story Mission Data?

### assets15

Level Story/Cutscene Data?

### assets16
These are all the MP3s used in the game; sound effects and speech

### assets17

This is all the music used in the game:

 - 0000; gzip'd data; TBD
 - 0001; 420KB; TBD
 - 0002; 21MB; Sound Bank. Extract from the baserom via N64 Midi Tool into [DLS](https://en.wikipedia.org/wiki/DLS_format) format. Use [Vienna](http://www.synthfont.com/Downloads.html) to convert the .dls into .sf2.
 - 0003; 2800KB; Contain offsets table followed by all 149 (format TBD) music files, 
 - 0004; 140 bytes; appears to contain offsets into 0006?
 - 0005; TBD
 - 0006; TBD

#### assets17/0001 investigation

```
$ xxd 0000.bin | head
00000000: 4231 0001 0000 0008 00aa 0000 0000 5622  B1............V"
00000010: 0000 0000 0000 02bc 006c b91f 006d 9f05  .........l...m..
00000020: 006d bc13 006e 4013 006e c413 006f 4807  .m...n@..n...oH.
00000030: 006f 6b07 006f 8e0b 006f d105 006f ee0b  .ok..o...o...o..
00000040: 0070 318f 0074 9c07 0074 bf35 0076 4f23  .p1..t...t.5.vO#
00000050: 0077 5a27 0078 8007 0078 a30d 0079 020b  .wZ'.x...x...y..
00000060: 0079 4507 0079 6807 0079 8b07 0079 ae07  .yE..yh..y...y..
00000070: 0079 d183 007d d107 007d f407 007e 1705  .y...}...}...~..
00000080: 007e 3405 007e 515b 0081 1707 0081 3a07  .~4..~Q[......:.
00000090: 0081 5d1f 0082 431f 0083 2907 0083 4c07  ..]...C...)...L.
```
`0x4231` is referenced in `func_80012934`. The surrounding functions have matching C code so ought to be able to figure this out.

`0x4231` is the `AL_BANK_VERSION` per `libaudio.h`, hopefully not a coincidence!

**NOTE:** `0x5622` is `22050`, fairly common sample rate and is used for some of the MP3s.

```
$ $ file assets16/0000
assets16/0000: MPEG ADTS, layer III, v2,  24 kbps, 22.05 kHz, Monaural
```

#### assets17/0003 breakdown

Is this a `ALSeqFile` struct?

```
00000000: 5331 0095 0000 04ac 0000 0061 0000 0510  S1.........a....
00000010: 0000 76fe 0000 7c10 0000 07b2 0000 83c4  ..v...|.........
00000020: 0000 0870 0000 8c34 0000 20ea 0000 ad20  ...p...4.. .... 
00000030: 0000 0b5f 0000 b880 0000 10ca 0000 c94c  ..._...........L
00000040: 0000 0700 0000 d04c 0000 0075 0000 d0c4  .......L...u....
```

- `0x5331` - 'S1' - AL_SEQBANK_VERSION
- `0x0095` - 149; number of offsets
- `0x000004ac` - 1196; offset 1
- `0x00000061` - 97; length 1
- `0x00000510` - 1296; offset 2
- `0x000076fe` - 30462; length 2
- .. etc

### assets18

### assets19

### assets1A

Tutorial/Manual Dialogue Text

### assets1B

### assets1C

Contains a bunch of text including:
 - Level names
 - Cheat codes (and swear words)
 - Credits

```sh
mkdir -p text/
python3 tools/extract_compressed.py config/assets1C.yaml rzip/assets1C/assets1C.bin text/
```

#### Cheats
```q
q)flip 34 cut (19*34)#1548 _ first read0 `:c:/tmp/00000020.bin
"VM INFO            "
"CHOCOLATESTARFISH  "
"BEELZEBUBSBUM      "
"SPUNKJOCKEY        "
"EASTEREGGSRUS      "
"WELLYTOP           "
"CHINDITVICTORY     "
"EATBOX             "
"BEEFCURTAINS       "
"BOVRILBULLETHOLE   "
"DRACULASTEABAGS    "
"DUTCHOVENS         "
"SPANIELSEARS       "
"XFYHIJERPWAL IELWZS"
"MONKEYSCHIN        "
"WELDERSBENCH       "
"RUSTYSHERIFFSBADGE "
"BILLYMILLROUNDABOUT"
"SKIP CUTSCENES     "
"SPEEDY MOVE        "
"ALL GOOD CHEATS    "
"INFO               "
"EASY               "
"VERYEASY           "
"ANCHOVYBAY         "
"PRINCEALBERT       "
"CLAMPIRATE         "
"*HEAT TWENTY SIGHT "
"*HEAT TWENTY EINE  "
"*HEAT THIRTY N     "
"*HEAT THIRTY ONE   "
"*HEAT THIRTY TWO   "
"\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
"\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000\000"
```