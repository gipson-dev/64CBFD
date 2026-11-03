# 2021 - Dual identity event handler matched as guarded C

Verified 2026-11-02. Production is **4,091/5,511 (74.23%)**; Game is
**3,418/4,838 (70.65%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,420 functions remain different. The active 80% target is
**4,409/5,511**, requiring **318 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_151B5A9C` replaces its zero-return placeholder in
`conker/src/game/generated_1E26F0.c`. It is the dual identity event handler at
`0x151B5A9C`, ROM `0x1E2F4C..0x1E304C`, owned by `generated_1E26F0`. Its
recovered interface is:

```c
void func_151B5A9C(DualIdentityOwner151B5A9C *owner,
                    DualIdentityEvent151B5A9C *event, u8 command);
```

The owner embeds its identity state at offset `0x28`. That state carries two
32-bit keys at offsets `0x580` and `0x588` and their byte tags at `0x584` and
`0x58C`, corresponding to absolute owner offsets `0x5A8`, `0x5AC`, `0x5B0`
and `0x5B4`. The event provides two keys and two tags. Command `0x2D` replaces
either matching owner pair with the opposite event pair. Command zero invokes
`func_1516972C` when the event's first key or its byte at offset four matches
either owner identity. Other command bytes are no-ops. The command's `u8`
type is ABI-significant and preserves the retail narrowing at entry.

The function has no direct `JAL` callers. Its sole aligned reference is a
literal registry pointer at ROM `0x22F3EC`; that pointer remains fixed. Its
only call binding is the release route to `func_1516972C`.

## Guarded compiler closure

Natural retail-profile IDO C emits **63 words/frame24**. Retail has **64 body
words** plus one unchanged owner-tail zero word. Five checked rows form one
closed compiler schedule: four branch/schedule replacements and one guarded
insertion retain retail's independent store/epilogue ordering. The insertion
moves the sole call relocation from natural offset `0xE4` to retail offset
`0xE8`; the padder preserves that binding symbolically. No semantic operation
is replaced by an opaque assembly block.

Both owner neighbors, all 6,051 function addresses and the entire allocated
image outside this function remain fixed. Strict full-image prediction uses
zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural 63-word object payload | `31f88f922d0cd0587efc21a00a913c1ca5230f6779a79e612e018d4223dd3039` |
| Retail linked 64-word payload | `d81e4927955f1e633b95370b31158f7802ee4b6fca1ab5e9826d28ab7480f8c4` |
| Qualified/production owner | `ea5e110764f688e7d9526bae9b6dd2d2b6eb234e532c4ebe6806cb07e2cd450a` |
| Predecessor linked ELF | `8805b69515d7d2aba6ece18b7c6c2c6c5a36ee2a3a902581fb945c0633c56227` |
| Qualified/production linked ELF | `132f3c9b225ce7cad92cfdd3c8667f49b03ce41c50a9875f1c81e28d2a090f8c` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `e9a5efc0f61b7f4e9988a0ddfa70771bdcb60632e68e111f67ebf5dc0b08fb10` |

The natural payload hash is taken before linker relocation and before the one
guarded insertion, so it is expected to differ from the retail linked body.

## Semantic and production qualification

The raw big-endian guest oracle executes **3,840 cases** across both stack
phases, all command classes, first/second key matches, tag matches, no-match
paths, replacement ordering, state/event aliasing and callback clobbers. Every
reachable body instruction is visited; offset `0x50` is an unreachable
duplicate load skipped by retail control flow and is separately compared as a
literal word. Native 32-bit O0/O2/O3 profiles pass, while eight effective
controls covering command decoding, key/tag selection, replacement direction,
release conditions and callback behavior all fail as intended.

The permanent four-test suite also verifies all five stale-guard mutations
fail closed, the registry pointer, both owner neighbors, strict image closure,
protected data and installed source/object/image coherence. All four tests
pass in 27.402 seconds. Nineteen shared layout, progress and padder tests pass
independently, including all five generated-object PC16 tests.

The protected Game-data audit remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The actual `make all -j4` rebuilt the corpus, linked `conker.us.elf` and
produced `conker.us.bin`; it stopped only at the expected whole-ROM SHA
mismatch because the overall decomp is incomplete. A fresh independent
recount credits exactly this function.

The candidate screen, qualification module and tests were committed first in
the tools submodule as `27334d5`. Retained stage:
`conker/build/game-dual-identity-event-151B5A9C-match/`.

This is instruction-level and bounded semantic proof, not natural whole-game
or gameplay acceptance. The README changes only its aggregate byte-exact
rows. No Claude call was needed.

## Graph retention

The required Graphify update extracted 24,199 nodes versus the retained 58,384
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
