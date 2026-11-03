# 2019 - Ring message writer matched directly from C

Verified 2026-11-02. Production is **4,089/5,511 (74.20%)**; Game is
**3,416/4,838 (70.61%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,422 functions remain different. The active 80% target is
**4,409/5,511**, requiring **320 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_15043BB8` replaces its empty placeholder in
`conker/src/game_70200.c`. It is the aligned ring-message writer at
`0x15043BB8`, ROM `0x71068..0x71154`, owned by `game_70200`. Its corrected
public interface is:

```c
s32 func_15043BB8(struct105 *queue, u8 *input, s32 length);
```

For a nonzero length and non-null source, the recovered routine reserves four
bytes for the length, rounds the complete record up to four-byte alignment and
checks the queue's write cursor against its read cursor. It returns one
without publishing anything when the record would fill or cross the available
region. Otherwise it writes the original payload length and then the payload
through `func_15043A20`, publishes the resulting cursor at queue offset
`0x0C`, and returns zero. Zero-length and null-source requests are successful
no-ops, as in retail.

The positive guarded body is source-significant. The equivalent-looking
early-return formulations compile to 62 words with 52 differences, while the
recovered positive body compiles to the exact retail shape. Signed source
arithmetic is retained because it is what the retail instruction stream and
ABI establish. The sole aligned retail `JAL` is at ROM `0x12570`, inside Init
wrapper `func_10012560`; that wrapper ignores the return value but supplies a
real queue, source and length.

## Direct compiler closure

Natural retail-profile IDO C emits all **59 words/frame40** directly, with
zero differing words and no expected-word guards. Both original `R_MIPS_26`
bindings to `func_15043A20` remain at offsets `0x0AC` and `0x0C8`. All 15
owner neighbors and normalized pools remain fixed. A strict literal
full-image prediction changes only `func_15043BB8`, preserves all 6,051
function addresses and uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 59-word object payload | `db6a3f24d611a017f1fb1d1105d0f976ef2a7729512431b7951ad729b0490fad` |
| Retail linked 59-word payload | `643d92a8336b6c69082799e9b9314b74f80c3b812c85e0705b86a53c8323df92` |
| Qualified/production owner | `9f95d7c360bfb2a4d02ae24339b144a794993464732d18e58e0836f143aedc2a` |
| Predecessor linked ELF | `7ef404e2d38e1367e12689ad0cce2caac0b47c3f913638506eeb840230db08c6` |
| Qualified/production linked ELF | `cef6e8a357527d10dfb66b5d1dd8ec6673f7e00c25cdfe0679f732ff0e762a53` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `d85664dba787bdf08e001177b60099083a6c065e4c7d7253a22aa2a33f943aed` |

The object payload hash is taken before linker relocation, so it is expected
to differ from the retail linked payload hash even though every linked word is
exact.

## Semantic and production qualification

The raw guest oracle covers zero and null requests, exact-fit rejection,
linear and wrapped capacity checks, all alignment classes, both helper calls,
publication and two incoming stack phases. It executes **6,146 cases** against
retail and candidate behavior. All reachable instructions are visited; the
duplicate load at `+0x90` is structurally unreachable because both incoming
paths use branch-likely delay slots. Native 32-bit O0/O2/O3 profiles pass,
while seven effective wrong-C controls fail.

The permanent four-test suite also executes the complete 10-word Init wrapper
connected to the writer, checks its 24-byte frame and fixed queue address,
verifies the sole caller census, 15 owner neighbors, strict image prediction,
protected data and installed source/object/image coherence. All four tests
pass in 26.490 seconds. Nineteen shared layout, progress and padder tests pass
independently.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the generated, converted and libultra corpus,
linked `conker.us.elf` and produced `conker.us.bin`; it stopped only at the
expected whole-ROM SHA mismatch because the overall decomp is incomplete. A
fresh independent recount credits exactly this function.

The qualification module and tests were committed first in the tools
submodule as `9f87722`. Retained stage:
`conker/build/game-ring-message-send-15043BB8-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,182 nodes versus the retained 58,384
and failed closed without `--force`, preserving 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. The retained graph
SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

Continue from a fresh ordinary Game ranking. Keep handwritten/custom-entry
`func_150A76F0`, `func_150A613C`, `func_151F8870` and stack-resume
`func_150AE280` outside ordinary C screens. `func_15115F68` and
`func_151AE2BC` remain private and uncredited until their compiler and ABI
boundaries are closed. Every candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount and documentation gates before credit.
