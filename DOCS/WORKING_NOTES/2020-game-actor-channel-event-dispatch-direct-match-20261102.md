# 2020 - Actor channel event dispatcher matched directly from C

Verified 2026-11-02. Production is **4,090/5,511 (74.22%)**; Game is
**3,417/4,838 (70.63%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,421 functions remain different. The active 80% target is
**4,409/5,511**, requiring **319 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_15172E7C` replaces its zero-return placeholder in
`conker/src/game/generated_1A0100.c`. It is the actor channel event dispatcher
at `0x15172E7C`, ROM `0x1A032C..0x1A0418`, owned by `generated_1A0100`.
Its recovered interface is:

```c
void func_15172E7C(struct127 *actor, s32 selector, s32 payload);
```

The `s32 selector` is source- and ABI-significant. A superficially narrower
`u8` declaration produces the same frame and length but differs at six words:
retail homes and reloads the complete argument before comparing it with
`D_800BE9F0`, then narrows only when publishing to `D_800DD2B0`. Likewise the
channel byte is promoted into an `s32` local, explaining retail's complete-word
spill around the callback.

The dispatcher first requires a live actor and either no state record or a
nonpositive signed state byte at offset `0x23`. With an active camera, a free
channel entry (`-1`) emits event `(0, 0, 0, 10, 1, channel)`, sets actor flag
`0x10`, then publishes the narrowed selector and payload bytes. Without a
camera, an exact 32-bit selector match against `D_800BE9F0` routes to
`func_15172D28`. All other paths are no-ops. The corrected dependent
declaration in `generated_CDE80.c` preserves its caller object's 28 function
bodies and complete padded object.

Three aligned retail `JAL` sites target this routine at ROM offsets `0xCCF48`,
`0xCF070` and `0xCFCD0`. Every caller ignores the result, confirming the
recovered `void` return type.

## Direct compiler closure

Natural retail-profile IDO C emits all **59 body words/frame48** directly, with
zero differing words and no expected-word guards. The complete 61-word retail
slot includes two unchanged trailing alignment zeros. All eight original
bindings remain: three HI16, three LO16 and two call relocations. All four
owner neighbors and normalized pools remain fixed. A strict literal
full-image prediction changes only `func_15172E7C`, preserves all 6,051
function addresses and uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 59-word object payload | `57f33ce4c5998bb05227ce39e861c9a8ef5d2988c446f7964e79d6b7db077fb0` |
| Retail linked 59-word payload | `b38b606e8695b825862fb4a2a3e735f918629d2fb7ff8133ee25f73a0f790acd` |
| Qualified/production owner | `80f30951e8b64f20fbb6c3a82128f88631247f81c1ed0c74d20ab646a4446c9e` |
| Unchanged dependent owner | `c498cda434de53868bb15a1a3458fae2a8ac2386cf32cc78671412357df3bbf0` |
| Predecessor linked ELF | `cef6e8a357527d10dfb66b5d1dd8ec6673f7e00c25cdfe0679f732ff0e762a53` |
| Qualified/production linked ELF | `8805b69515d7d2aba6ece18b7c6c2c6c5a36ee2a3a902581fb945c0633c56227` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `d85664dba787bdf08e001177b60099083a6c065e4c7d7253a22aa2a33f943aed` |

The object payload hash is taken before linker relocation, so it is expected
to differ from the retail linked payload hash even though every linked word is
exact.

## Semantic and production qualification

The raw guest oracle executes **960 cases** across actor health, null/negative/
zero/positive state records, camera and fallback paths, occupied and free
channels, full-width selector comparisons, narrowed publications, payload
boundaries and two incoming stack phases. Every body instruction is visited.
Callback hooks clobber all caller-saved integer and floating registers, so the
channel lifetime and post-call reloads are exercised rather than assumed.

Native 32-bit O0/O2/O3 profiles pass 384 cases each. Nine effective controls
cover the health and state gates, camera route, free-channel sentinel, event
duration, actor flag, selector/payload publications and fallback comparison;
all fail. The permanent four-test suite also checks the three retail callers,
four owner neighbors, 28 unchanged dependent functions, strict image
prediction, protected data and installed source/object/image coherence. All
four tests pass in 27.112 seconds. Nineteen shared layout, progress and padder
tests pass independently, including all five generated-object PC16 tests.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt both affected generated owners, linked
`conker.us.elf` and produced `conker.us.bin`; it stopped only at the expected
whole-ROM SHA mismatch because the overall decomp is incomplete. A fresh
independent recount credits exactly this function.

The candidate screen, qualification module and tests were committed first in
the tools submodule as `9c3fa48`. Retained stage:
`conker/build/game-actor-channel-event-15172E7C-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,190 nodes versus the retained 58,384
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
