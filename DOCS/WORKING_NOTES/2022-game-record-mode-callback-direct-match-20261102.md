# 2022 - Record mode callback matched directly from C

Verified 2026-11-02. Production is **4,092/5,511 (74.25%)**; Game is
**3,419/4,838 (70.67%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,419 functions remain different. The active 80% target is
**4,409/5,511**, requiring **317 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_15013C38` replaces its zero-return placeholder in
`conker/src/game_40490.c`. It is the record mode callback dispatcher at
`0x15013C38`, ROM `0x410E8..0x411E8`, owned by `game_40490`. Its recovered
interface is:

```c
s32 func_15013C38(u8 *record);
```

The routine first sets bit `0x04` in `record[0x16]`, then reads the signed
mode at `record + 0x18`. It returns without dispatch when status byte
`((u8 *)D_800D2E4C)[0x11]` carries bit `0x04` while `D_800BE9F0` is `0x13`,
or when player mode `D_800C35EA` is one and sequence byte `D_800C35E8` is
`0x0F`, `0x10` or `0x11`. A signed mode of six or greater is also a no-call
path.

Otherwise, `D_80082F28[mode]` supplies an optional callback. A non-null
callback receives the record pointer and the unsigned word at
`record + 0x1C`, converted to single precision and multiplied by
`D_80096650`. The retail unsigned conversion is visible in the emitted
`CVT.S.W` plus conditional `2^32` correction; declaring the payload as `u32`
is therefore ABI- and instruction-significant. The local `scaled` lifetime
is likewise compiler-significant: it assigns the product to `$f0` and makes
the complete routine direct byte-exact C.

The function has no direct `JAL` callers. Its sole aligned reference is a
literal registry pointer at ROM `0x2279AC`; that pointer remains fixed. The
callback table contains six known mode handlers beginning at `D_80082F28`.
Retail's signed upper-bound test does not reject negative modes. The guest
qualification therefore includes a mapped mode `-1` table slot, while the
native C harness stays within its declared six-element table object.

## Direct compiler and image closure

Retail-profile IDO emits the complete **64 words/frame24** directly from the
semantic body. No retail-word guards, insertions, omissions, assembly blocks,
profile changes or Makefile changes are required. All twelve HI16/LO16
relocations remain attached to their original symbols:

- `D_800D2E4C`, `D_800BE9F0`, `D_800C35EA` and `D_800C35E8` for suppression;
- `D_80082F28` for callback selection; and
- `D_80096650` for the scale.

All 31 other functions in `game_40490`, normalized owner pools, all 6,051
function addresses and the entire allocated image outside this function
remain fixed. Strict full-image prediction uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 64-word object payload | `34b2c0353824d08639866a1ada408cb75de972c80a6326015ab47a2947e387d8` |
| Retail linked 64-word payload | `174e01b00d44e45611c7a6f5c9dc0cb876bee4c8003600dae67a61407f21145d` |
| Qualified/production owner | `86f33795cc6c03668d9cd2f3f882cba139d4be860b7363aafde2e73027075c82` |
| Predecessor linked ELF | `132f3c9b225ce7cad92cfdd3c8667f49b03ce41c50a9875f1c81e28d2a090f8c` |
| Qualified/production linked ELF | `07ad10cd6c8628054831ce3929ebb3ddd83f581853d415cef27953315c910a01` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `e9a5efc0f61b7f4e9988a0ddfa70771bdcb60632e68e111f67ebf5dc0b08fb10` |

The natural object hash masks relocation immediates, while the retail body
hash is taken from the linked ROM, so those two hashes are intentionally not
equal.

## Semantic and production qualification

The raw big-endian guest oracle executes **5,120 cases** across both stack
phases, both suppression gates, all three blocked sequence values, signed
modes `-1`, `0`, `5` and `6`, null/non-null callbacks, all unsigned conversion
boundaries and two finite scales. It compares every external memory byte,
callback argument and return value against an independent reference while
clobbering caller-saved integer and floating registers at the callback. Every
independently dispatched body word is visited; offset `0x8C` executes only as
a branch-likely delay word and is also fixed by the literal byte comparison.

Native 32-bit O0/O2/O3 profiles pass 10,000 cases each. Ten effective controls
cover the flag write, both suppression predicates, special sequence set,
mode bound, unsigned conversion, scale operation, callback index and return
value; all fail as intended. The permanent four-test suite additionally
verifies the sole registry pointer, 31 owner neighbors, literal full-image
prediction, protected data and installed source/object/image coherence.
Together with the 19 shared progress, PC16, padder and protected-layout tests,
all **23 tests pass in 29.145 seconds**.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the owner, linked `conker.us.elf` and
produced `conker.us.bin`; it stopped only at the expected whole-ROM SHA
mismatch because the overall decomp is incomplete. A fresh independent
recount credits exactly this function.

The candidate screen, qualification module and tests were committed first in
the tools submodule as `28756d3`. Retained stage:
`conker/build/game-record-mode-callback-15013C38-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,213 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

Continue from the fresh ordinary Game ranking at `func_1507FEA0` after the
known handwritten/custom-entry, parked, stack-resume and private candidates.
Keep `func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside an ordinary direct-C screen until
their existing boundaries are resolved. Every candidate still requires
source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount and documentation gates before credit.
