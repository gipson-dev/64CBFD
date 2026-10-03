# Init Bitmap Leaf Contract and Compiler Experiment

Date: 2026-10-02

## Contract

`func_10005BE0` occupies `0x10005BE0..0x10005C2C`, nineteen words /
76 bytes, within the standalone `init_5AB0` assembly owner. It fills every
byte from the pointer loaded at `D_8003BE70` through the pointer loaded at
`D_8003BE7C`, inclusive, with `0xFF`. If the signed-halfword count at
`D_8003BE78` has nonzero low three bits, the final byte becomes
`(1 << (count & 7)) - 1`.

The allocator in `func_10005B04` requests `(count + 7) >> 3` bitmap bytes,
stores the returned pointer at `D_8003BE70`, and stores the inclusive last
address at `D_8003BE7C`. Retail calls exist in the Init startup/reset paths,
including `func_10001194`, `init_1420.c`, and the debug/reset assembly path
at `0x100080BC`. The leaf itself uses an ordinary return and temporary
registers; it does not share the decompressor frame.

The shared header currently declares `D_8003BE70` as `s32` and
`D_8003BE7C` as `s8`. Retail loads both as words and uses them as pointers.
The isolated candidate therefore uses proper local pointer declarations;
this audit does not change shared declarations or unrelated consumers.

## Compiler Trials

Three fixtures were compiled with the existing IDO 5.3 `-O2 -g3 -mips2
-o32` profile:

| Source shape | Meaningful words | Result |
| --- | ---: | --- |
| Inclusive postincrement loop; `2 << (bits - 1)` mask | 20 | XOR comparison temporary and different tail schedule |
| Explicit break before cursor increment | 20 | Additional unconditional loop-back branch |
| Inclusive postincrement loop; `1 << bits` mask | 19 | Fits retail span, but is not a direct instruction match |

The final ignored fixture at `conker/build/init-bitmap-experiment.c` is:

```c
typedef unsigned char u8;
typedef short s16;
extern u8 *D_8003BE70;
extern u8 *D_8003BE7C;
extern s16 D_8003BE78;

void func_10005BE0(void) {
    u8 *cursor = D_8003BE70;
    u8 *end = D_8003BE7C;
    int bits;

    do {
        *cursor = 0xFF;
    } while (cursor++ != end);
    bits = D_8003BE78 & 7;
    if (bits != 0) {
        *end = (1 << bits) - 1;
    }
}
```

The count-fitting candidate still uses XOR plus a zero-test rather than
retail's direct pointer branch, different opening load order, and a different
mask schedule. No production source replacement or normalization batch is
established by these trials. Extracting one leaf from `init_5AB0` would also
require preserving all neighboring code, interior labels, and layout ownership;
that machinery was not changed just for an unmatched candidate.

## Behavior Evidence

An ignored host fixture compiles the actual final candidate and checks every
byte of a sentinel-filled 4,104-byte buffer after two calls. All 65 cases
pass: counts 1 through 64 plus 32,767. These cover all eight remainder classes,
single-byte ranges, multiple complete bytes, the largest positive signed-halfword
count, preserved surrounding bytes, and repeat calls.

This tests the candidate's behavior, not execution of the guest assembly or
a completed conversion. Zero-size or reversed ranges are not qualified; the
candidate deliberately retains retail's unconditional initial store rather
than adding a defensive early return with different behavior.

## Disposition

Keep `func_10005BE0` in a deferred matching/extraction queue, alongside the
MMIO experiment in Note 737. Init remains 492 C / 47 assembly rows. These
are conditional custom-leaf rewrites, not evidence of missing original C.
The next ordinary Game target was `func_15157FE8`; Note 739 completes it
and independently reconfirms both complete Init sections remain exact.
