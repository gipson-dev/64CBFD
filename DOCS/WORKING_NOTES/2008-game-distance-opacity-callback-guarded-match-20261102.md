# 2008 - Distance-opacity callback matched as guarded C

Verified 2026-11-02. Production **4,075/5,511 (73.94%)**; Game
**3,402/4,838 (70.32%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,436 different; one generated zero-return placeholder is replaced by
recovered C and is newly byte-exact. The active 80% target is **4,409/5,511**,
requiring **334 more**. This is progress toward that goal, not completion.

## Semantic recovery and callback interface

`func_15179CB0` is the frame-zero distance-opacity callback at VA
`0x15179CB0` and ROM `0x1A7160` in
`conker/src/game/generated_1A6360.c`. Its recovered O32 interface is:

```c
void func_15179CB0(u8 *record);
```

The routine reads the signed planar coordinates at record offsets `0xA0` and
`0x9C`, subtracts the viewer coordinates at offsets `0x300` and `0x2F8` from
`D_800DBFF0`, computes the Euclidean distance, and writes the converted opacity
byte at record offset `0xB4`:

```c
record[0xB4] = (u32)(255.0f - sqrtf(dx * dx + dz * dz) * 160.0f / 1000.0f);
```

The callback is installed in the pointer table at ROM `0x2314C0`, data address
`0x8008CA00`, within `D_8008C9C8`. The table boundary consumes only `a0`; no
direct C caller was found. The permanent qualification checks the pointer-table
entry and freezes the retail inputs rather than inventing a public prototype or
retail symbol name.

## Guarded compiler closure

Fresh IDO emits the complete 62-word body with the retail frame and both
relocations. The owner contributes the two original zero tail words, making the
complete 64-word retail slot exact. The raw C body differs at only `+0x060`:
candidate `0x46080282`, retail `0x46004282`. These are equivalent commutative
`MUL.S` operand orders. One checked expected-word replacement preserves the
retail schedule and fails closed if the compiler output changes. There are no
omissions or insertions.

The two relocations are the `R_MIPS_HI16`/`R_MIPS_LO16` pair for
`D_800DBFF0` at `+0x008` and `+0x010`; the linked words are `0x3C02800E` and
`0x8C42BFF0`.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `11f3b612a912130eabe0507cea1949b5b41eb8e250e8113c9721a269cdbf5855` |
| Qualified/production owner | `291f4ac202439a9306d1383d77385813038017aeb5be8ec1db024be36a39f7ae` |
| Qualified/production linked ELF | `b8717679215b85d1a3cb5cad066dd5db772d3fa1b4a0747590f8b74eb343a969` |
| Raw candidate object body | `3ccd9207905b3a5d2cf18c30f0070c0936503e7f363c15c073e862c536a5eb7a` |
| Raw candidate linked body | `4ea50c1839b7cea994c29fb54ba5d3eab2d43cd62dc0746032d566d157527015` |
| Retail body, first 248 bytes | `baa36d41695d70961d322d9a8be4796ca009b84427ea488abdcdd7a719f07511` |
| Retail/guarded 256-byte slot | `7ab3e37f5ec40fea045320a042a94c4045ba39338defb1cdb4113e631aa2c823` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Guard manifest | `6351da2f812e6d054b6821028c3e20244e9c1a18eb9b91f91bd359ac3bf1e902` |

## Semantic, owner and image qualification

Eight permanent tests pass in 60.970 seconds. The guest corpus runs 231 cases
through both the retail and candidate bodies, or 462 guest executions. It
covers the finite distance grid, negative-opacity fallback, NaN and infinity
conversion paths, four incoming FCSR patterns, and at least 57 body words.
Native O0, O2 and O3 builds each pass 225 selected cases. Six effective wrong
controls per profile reject the record offset, viewer offset, missing axis,
scale, base and byte-store alternatives.

The owner contains nine functions; all eight neighbors remain byte-for-byte
unchanged. Strict whole-image closure covers all 6,051 functions, changes only
the target body, keeps every address fixed and uses zero exclusions. Actual
Make reproduced the qualified owner and predicted linked ELF byte-for-byte. A
clean dependency rebuild completed successfully. The full
`make -C conker all -j2` pipeline generated the development ROM and failed only
the expected final retail SHA-1 check because the wider decomp image is not yet
byte-identical.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Converted-C totals do not change because the former placeholder was already in
the generated C inventory. This is instruction-level and bounded semantic
proof, not a claim of natural whole-game visual or gameplay acceptance.

The permanent experiment and qualification suites were committed first in the
tools submodule as commit `4bbefc8`. No public header declaration was added
because this is a pointer-table callback with no direct C caller. The root
README changes only its aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,108 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep the
parked compiler-exit, custom-ABI, handwritten and proven sparse-read cases on
their separate tracks, and keep every new candidate private until all
qualification gates pass.
