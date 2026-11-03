# 2029 - Fixed directional-effect input submission matched directly from C

Verified 2026-11-03. Production is **4,099/5,511 (74.38%)**; Game is
**3,426/4,838 (70.81%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 1,412 functions remain different. The active 80% target is
**4,409/5,511**, requiring **310 more**. This is progress toward that goal,
not completion.

## Recovery and interface

`func_151C61A0` replaces its zero-return placeholder in
`conker/src/game/generated_1F2730.c`. It is the fixed directional-effect
input submitter at VA `0x151C61A0`, ROM `0x1F3650..0x1F3740`, owned by
`generated_1F2730`. Its recovered interface is:

```c
void func_151C61A0(void *providerType, s32 requestValue,
                   u8 channel, s32 owner);
```

The routine constructs the established 60-byte `DirectionEffectInput` used
by the already-recovered `func_15154684` factory. It supplies count base/range
10/4, second-angle base/range -24/25, radius 5.0/7.0, scale globals
`D_800AAAF4` and `D_800AAAF8`, the raw mode/pointer word from `D_800AAAFC`,
selector 190/65, duration 200/150, time 96.0/109.0, opacity chance 1.0 and the
incoming request value. Descriptor bytes `+0x2A/+0x2B` deliberately remain
unwritten, matching retail. The factory receives the low byte of `channel`
and the original `owner`; the submitter returns `void`.

The complete retail census finds one direct JAL and no aligned literal
pointer. The sole call is at ROM `0x1643D4`, VA `0x15136F24`, inside
`func_15136C3C` owned by `game_161520`. Its argument window proves provider at
`SP+0xAC`, request value at `SP+0x7C`, the channel byte at `SP+0xD3` and owner
at `SP+0xD4`.

## Direct compiler and image closure

The retail `-O2 -g3` profile emits the complete 60-word, 88-byte-frame body
directly from the semantic C. There are no expected-word guards, insertions,
omissions, assembly blocks or profile changes. The seven natural relocations
are the HI16/LO16 pairs for `D_800AAAF4`, `D_800AAAF8` and `D_800AAAFC`, plus
the J26 call to `func_15154684`.

All seven other owner functions, all normalized owner pools, all 6,051
function addresses and every allocated image byte outside this target remain
fixed. The target's new 240-byte extent changes the target symbol size from
12 to 240 and produces one deterministic GNU-ld five-symbol `.symtab` and
`.strtab` rotation: `D_800AAAF8`, `D_800A113C`, `D_8009CC3C`, `D_8009E63C`,
and `func_15155FD4`. The strict predictor models that closed metadata cycle
literally and uses zero exclusions.

| Artifact | SHA-256 |
| --- | --- |
| Natural relocation-masked 60-word payload | `e6298d9a9f6c45f5efac3d87599bcbf78cc1e69b349978f6d82d340e3711b892` |
| Retail linked 60-word payload | `02d5d9e1e55d07a109eb61896a630abfb17871806731a124081cbae8868802dc` |
| Qualified/production owner | `1e659545006460cf098777ac5799fb4a21995751e9ffcc1715329864a9c9759b` |
| Predecessor linked ELF | `8ea0bd5a33b798d4d39b1dc1fe0450ff6efb3db4ddabf7807633c63556bb0a38` |
| Qualified/production linked ELF | `8998cb5660571804ab3e25b1e35b03b8aa2621a0d4a577f491a56757f8d959a0` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `fffe1a835fb2b55e8d20d6ebb5236ce2c3e2d2a38da108c892aed29300303618` |

## Semantic and production qualification

The big-endian guest oracle executes 16 cases across both stack phases, two
global bit-pattern sets and four argument patterns. Every one of the 60 retail
words executes. The complete 60-byte descriptor, both untouched bytes,
low-byte channel and owner forwarding agree with the reference model.

Native 32-bit O0/O2/O3 profiles each pass 4,096 cases, for 12,288 executions,
with warnings as errors and UBSan trapping on the first error. Fourteen
compiled controls independently reject wrong count, provider, reserved words,
angle, radius, global, selector, duration, time, opacity, request, channel and
owner behavior. Complete-image tests reject the predecessor payload, target
body/size corruption, every symbol/string member of the five-name cycle and a
truncated image.

The focused four-test installed suite passes in 112.199 seconds. The 19 shared
progress, generated-PC16, guarded-padder and protected-layout tests pass in
9.746 seconds. Protected Game data remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The actual `make all -j4` regenerated, compiled, padded, assembled and linked
the owner and complete corpus. It stopped only at the expected whole-ROM SHA
mismatch because the overall decomp remains incomplete. The production owner
and ELF equal their independently predicted qualified artifacts byte for byte;
a fresh production recount credits exactly this function.

The candidate qualifier and permanent tests were committed first in the tools
submodule as `6eba6d7`, followed by the interface-naming refinement in
`4f6d11c`. This is instruction-level and bounded semantic proof, not natural
whole-game or gameplay acceptance. The README changes only its aggregate
byte-exact rows. No Claude call was needed.

## Graph retention

The required bounded Graphify update extracted 24,237 nodes and 47,584 edges
versus the retained 58,384 nodes. It failed closed without `force=True`,
preserving 31,841 nodes from 3,778 still-existing files outside the reduced
scan corpus. The retained graph SHA-256 remains
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. The
structural pass used zero LLM tokens and repeated the known local
0.9.20-skill/0.9.26-package warning and one zero-node `devcontainer.json`
source.

## Continuation

The fresh ordinary Game ranking leaves the six documented boundary cases
`func_150A76F0`, `func_151F8870`, `func_150A613C`, `func_150AE280`,
`func_15115F68` and `func_151AE2BC` outside the direct-C queue. Continue with
`func_151CD3CC` (61 words, 59 current real differences), then re-rank. Every
candidate still requires source, ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount and documentation gates
before credit.
