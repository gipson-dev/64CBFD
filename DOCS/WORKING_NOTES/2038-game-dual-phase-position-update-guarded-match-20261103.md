# Game Dual-Phase Position Update Guarded Match

Date: 2026-11-03

## Result

`func_15190F9C` now replaces its zero-return placeholder with byte-exact
guarded C. Its complete retail slot is **60 words / 240 bytes**, frame
`0x30`, VA `15190F9C..1519108C`, and ROM `1BE44C..1BE53C`. A fresh
production recount credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,108 / 5,511 (74.54%) | 0 | 1,403 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,435 / 4,838 (71.00%) | 0 | 1,403 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **301 more** exact functions.

## Source recovery and guarded closure

The recovered callback takes one mutable state pointer. It advances phase
bytes at `state+0x131` and `state+0x132` by the signed rates at `+0x133` and
`+0x134`, each multiplied by the live clock step `D_800BE9E4`. Both updated
phases are sampled through `func_151423D8((u8)(phase - 0x40))`. The parameter
block begins at `state+0x110`: its bases at `+0x28/+0x2C` and scales at
`+0x30/+0x34` form two planar targets. The current coordinates at
`state+0x2C/+0x30` are each eased halfway toward their target before the
callback returns one.

The natural compiler body has the same 60-word topology and naturally retains
both clock-step bindings, both helper calls, all phase and parameter offsets,
and both smoothing stores. Nine checked positional words isolate a natural
`0x20` frame/spill layout and two commutative floating additions:

| Raw offset | Compiler word | Retail word | Qualified action |
| ---: | ---: | ---: | --- |
| `0x000` | `27BDFFE0` | `27BDFFD0` | Expand the callback frame from `0x20` to retail `0x30`. |
| `0x05C` | `AFA50020` | `AFA50030` | Move the owner argument home with the frame. |
| `0x060` | `8FA50020` | `8FA50030` | Reload the owner from its retail home. |
| `0x064` | `E7A00018` | `E7A00024` | Move the first trigonometric sample home. |
| `0x088` | `C7A60018` | `C7A60024` | Reload the first sample from its retail home. |
| `0x08C` | `8FA50020` | `8FA50030` | Reload the owner after the second helper call. |
| `0x0BC` | `46022180` | `46041180` | Preserve retail's first commutative smoothing addition. |
| `0x0DC` | `460C3200` | `46066200` | Preserve retail's second commutative smoothing addition. |
| `0x0EC` | `27BD0020` | `27BD0030` | Restore the retail frame size. |

Every row checks its expected compiler word and fails closed when stale. No
instruction is inserted or omitted and no relocation is normalized. The four
natural relocations remain HI16/LO16 bindings for `D_800BE9E4` at offsets
`0x004/0x008` and J26 bindings for `func_151423D8` at `0x058/0x07C`. The
unqualified compact body has SHA-256
`52091310d7e6b013da7983026d9319ae33f43d87ec66ed5ecd4f3b243f9dc816`;
the qualified retail body has SHA-256
`7a2e91e3091eddf1fa276397cda86170175116475f2e2d141e4a7e3cf692fce3`.

## Semantic, registry, and production qualification

The big-endian guest oracle runs 2,752 cases and covers every one of the 60
retail words. Its helper mutations validate both updated phase arguments and
the live late reads of the parameter block, current coordinates, and second
clock update. The same contract passes native 32-bit O0, O2, and O3 builds;
ten independent behavior-changing source controls prove the phase offsets,
rate offsets, clock use, helper transform, parameter bases/scales, smoothing
factor, and coordinate destinations. A proposed signed-versus-unsigned rate
control is deliberately not counted: after byte wrapping, the low-byte phase
result is observably equivalent, so it would not be an effective mutation.
The three focused tests and 19 shared progress, Game-data-layout,
generated-PC16, and guarded-padder tests all pass.

There are no direct JAL callers. The sole aligned pointer literal is at ROM
`0x22E7A8`, the callback entry `D_80089CB8[12]`. The complete 61-function
owner preserves the other 60 functions. Strict qualified-versus-production
comparison retains all 6,051 function addresses, uses zero exclusions, and
reports only `func_15190F9C` changed before installation and no changed
function afterward. Protected Game data remains exact at 189,088 bytes
across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `0eca92fb9e84faf6510cd2736fc4e08f766c69fc734c7b233b17af463b397ac9` |
| Predecessor linked ELF | `90b315f46491d60912ae9db12c5ba8dea367cd93a63fc25ff2f459bdf450ef01` |
| Qualified/production linked ELF | `d3db31e76a768dcf445c57e947152fe0130c8657802d83b680f200dd381022ca` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `16a3b92d8b62d17de7e6117c9c52cca968c8f6ddea93f01cf434eafe892cd110` |

The actual `make all -j4` rebuilt the complete guarded corpus, regenerated the
linker script, linked `conker.us.elf`, and generated `conker.us.bin`. Every
existing guard remained valid. The build stopped only at the expected final
whole-ROM SHA mismatch while the decomp remains incomplete.

The permanent qualifier and evidence tools were committed first in the tools
submodule as `ed27243` (`test(game): qualify dual phase position update`).
Production source and the nine checked rows were installed only after that
tools commit.

## Graph retention

The required bounded Graphify update extracted 24,320 nodes versus the
retained 58,384. It failed closed without `--force`, preserving 31,816 nodes
from 3,754 still-existing files outside the reduced scan corpus. The retained
`graphify-out/graph.json` remains 77,250,386 bytes with SHA-256
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. The
existing Graphify 0.9.20-skill/0.9.26-package and empty `devcontainer.json`
warnings remain non-blocking and did not replace the graph.

## Continuation

The fresh ordinary Game ranking keeps the same seven documented boundary
cases outside the direct-C queue: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue with ordinary candidate `func_151A9BA0` (64 words,
60 real differences), followed by `func_151AE6B0`, `func_151B1828`, and
`func_151B9214` in the same 60-difference tier. Every candidate still
requires source, ABI/caller, owner, guest/native, actual Make, complete-image,
protected-data, production recount, documentation, and graph-retention gates
before credit.
