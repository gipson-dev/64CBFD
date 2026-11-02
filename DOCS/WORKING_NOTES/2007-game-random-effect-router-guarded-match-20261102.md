# 2007 - Random-effect router matched as guarded C

Verified 2026-11-02. Production **4,074/5,511 (73.92%)**; Game
**3,401/4,838 (70.30%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,437 different; one placeholder is replaced by recovered C and is
newly byte-exact. The active 80% target is **4,409/5,511**, requiring **335
more**. This is progress toward that goal, not completion.

## Semantic recovery and callback interface

`func_151AE890` is the 244-byte/61-word random-effect router at VA
`0x151AE890` and ROM `0x1DBD40` in
`conker/src/game/generated_1D92F0.c`. Its recovered O32 interface is:

```c
void func_151AE890(f32 x, f32 y, f32 z, s32 effect_arg0_bits,
                   s32 effect_arg1_bits, s32 effect_arg2_bits, u8 *actor);
```

The function copies the three coordinates into a stack position vector and
uses `func_150ADA68` to select one of three routes. A sample below
`D_800A9D84` returns without creating an effect. A surviving sample below
`0.25f` calls `func_151AEAB4` with a second random positive/nonpositive flag
and `actor[0xC]`. The remaining route calls `func_151AE984` with the three raw
effect payload words, a second random comparison against `D_800A9D88`, and
the same actor byte.

The payload parameters deliberately remain signed 32-bit words. Treating them
as floating arguments would promote them through the old-style constructor
calls and change the O32 argument layout. The source comment names only the
recovered behavior; it does not invent a retail symbol name.

The callback is installed in `conker/asm/data/22E4E0.rodata.s` at ROM
`0x22E548`, data address `0x80089A88`, in table `D_80089A70`. That table entry
and the seven-argument callback boundary are checked permanently. The two
selected constructors, `func_151AE984` and `func_151AEAB4`, remain their
original 12-byte generated-C placeholders and are not credited as recovered.

## Guarded compiler closure

Fresh IDO emits the correct 61 words, 56-byte frame and all nine relocations.
Only two independent scheduling words differ. At `+0x064` raw C emits the
actor load `0x8FAE0050` while retail emits the initial zero flag
`0x00002825`; at `+0x068` the two words occur in the opposite order. Two
checked expected-word replacements preserve retail scheduling. There are no
omissions or insertions.

| Artifact | SHA-256 |
| --- | --- |
| Predecessor linked ELF | `c46e4ee1a389a91913bc5a3a9b8279caabba33aff233e073c91e3317d122e260` |
| Qualified/production owner | `ceda832d4286618ccc59d52b386cdba5ab039f4da8bb1d62d2c77da36af0cdec` |
| Qualified/production linked ELF | `11f3b612a912130eabe0507cea1949b5b41eb8e250e8113c9721a269cdbf5855` |
| Raw candidate object | `7fdc9f7f2a69654ce0e978c25e9d3d32199b6ae850b1a9ef733e29b6c536f04d` |
| Raw candidate linked slot | `61d6255f1061db28cb370d6730658d14e242aca93fe84c06388ee214d0582540` |
| Retail/guarded slot | `6ec7bca342935b2481f256dac830439aacb206aff2b0248709aafa6751088bff` |
| Production map | `0f9af6c3578cff80ed406b8510f09e8dd211b6d07abb0e1c6614b4640522165d` |
| Guard manifest | `aab17cf843862641624fe0b6cf87c94a311c7b9d484a0432d50a07acf9f88f6d` |

## Semantic, owner and image qualification

Eight permanent tests pass in 50.704 seconds. The guest corpus runs 240 main
matrix cases and 18 coordinate/payload cases through both retail and candidate
bodies, or 516 executions. It covers all three routes, exact threshold edges,
positive/nonpositive flags, actor-byte extremes, raw payload bit patterns,
signed zero, infinities and NaNs. Callback clobbers verify that values needed
after each call are preserved according to the retail lifetime. Source controls
also reject floating payload types that would alter O32 argument passing.

The owner contains 33 functions; all 32 neighbors remain byte-for-byte
unchanged. The two downstream placeholders remain exactly 12 bytes. Strict
whole-image closure covers all 6,051 functions, changes only the target body,
keeps every address fixed and uses zero exclusions. Actual Make reproduced the
qualified owner and predicted linked ELF byte-for-byte. The full
`make -C conker all -j2` pipeline generated the development ROM and failed only
the expected final retail SHA-1 check because the wider decomp image is not yet
byte-identical.

Protected Game data remains exactly 189,088 bytes across 720 owners with zero
different bytes, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Converted-C totals do not change because the former placeholder was already in
the generated C inventory. This is instruction-level and bounded semantic
proof, not a claim that the unfinished constructors or natural whole-game
effect path are complete.

The permanent experiment and qualification suites were committed first in the
tools submodule as commit `634f821`. The retained qualification stage is
`conker/build/game-random-effect-router-151AE890-guard-match/`. The root README
changes only its aggregate byte-exact rows. No Claude call was needed.

## Graph retention and next step

The required Graphify update extracted 24,101 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is retention evidence, not a full-corpus refresh claim.

Continue the ordinary Game queue from a fresh non-exact ranking. Keep
`func_151AE984` and `func_151AEAB4` in the unmatched queue until their own
interfaces, semantics, callers, owners and whole-image closures pass. Keep
handwritten/custom-ABI work on its separate track, and keep every new candidate
private until all qualification gates pass.
