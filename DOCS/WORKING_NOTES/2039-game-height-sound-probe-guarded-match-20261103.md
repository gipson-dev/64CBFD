# Game Height/Sound Probe Guarded Match

Date: 2026-11-03

## Result

`func_151A9BA0` now replaces its zero-return placeholder with byte-exact
guarded C. Its complete retail slot is **64 words / 256 bytes**, frame `0x40`,
VA `151A9BA0..151A9CA0`, and ROM `1D7050..1D7150`. A fresh production
recount credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,109 / 5,511 (74.56%) | 0 | 1,402 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,436 / 4,838 (71.02%) | 0 | 1,402 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **300 more** exact functions.

## Source recovery and guarded closure

The recovered callback takes one owner pointer and reads its attached actor at
`owner+0x18`. It copies the actor X/Z coordinates from `+0x14/+0x1C`. The Y
probe origin is either the actor top at `+0x118` plus `100.0f` when that top is
above `D_800A8F7C`, or the actor Y at `+0x18` plus `150.0f` otherwise. It then
queries downward by `300.0f` through `func_15045800`. A hit replaces Y with
the result at `owner+0x34`, submits the position and live owner metadata to
`func_151ABE40`, and starts sound `0x5208` through `func_10010FFC` using the
original attached actor pointer.

The natural compiler body has the same 64-word topology, frame size, three
calls, and five original relocations. Eleven checked positional words isolate
one independent opening schedule and the compiler's alternate actor-pointer
spill home:

| Raw offset | Compiler word | Retail word | Qualified action |
| ---: | ---: | ---: | --- |
| `0x014` | `3C010000` | `C4640014` | Move the actor-X load ahead of the threshold HI16. |
| `0x018` | `C4260000` | `3C010000` | Move the `D_800A8F7C` HI16 binding one word later. |
| `0x01C` | `C4640014` | `C4260000` | Move the threshold LO16 load one word later. |
| `0x020` | `3C014316` | `E7A40030` | Store X before preparing the `150.0f` constant. |
| `0x024` | `27A40030` | `C4600118` | Load the actor top before forming the probe pointer. |
| `0x028` | `E7A40030` | `3C014316` | Prepare the `150.0f` constant after the top load. |
| `0x02C` | `C4600118` | `27A40030` | Form the probe pointer after the independent setup. |
| `0x088` | `AFA3002C` | `AFA3003C` | Use retail's actor-pointer spill home before the query. |
| `0x0A0` | `8FA3002C` | `8FA3003C` | Reload the actor from its retail home after the query. |
| `0x0BC` | `AFA3002C` | `AFA3003C` | Preserve the actor across the effect callback at retail's home. |
| `0x0CC` | `8FA3002C` | `8FA3003C` | Reload the original actor for the sound call. |

Every row checks its expected compiler word and fails closed when stale. The
threshold relocation moves from raw offsets `0x014/0x018` to retail offsets
`0x018/0x01C`; J26 bindings for `func_15045800`, `func_151ABE40`, and
`func_10010FFC` remain at `0x094`, `0x0C4`, and `0x0E4`. The unqualified
compact body has SHA-256
`dc9556ca419ccca4e732626c1d38672907862c2eed5e9cc13fee73b79af03d0d`;
the qualified retail body has SHA-256
`8c15f9cf461a34c5f268ad45863430aa64e65d910e472b2c8c612ccaff5fab2c`.

## Semantic, registry, and production qualification

The big-endian guest oracle runs 1,728 cases across both height routes, query
outcomes, owner metadata, and callback mutations. It covers all 63
structurally reachable retail words. Offset `+0x58` is a duplicated low-route
Y load that is not independently reachable because retail executes its
equivalent branch-likely delay copy; the exclusion is explicit and does not
hide a selectable route. Retail and qualified execution agree in complete
state and callback traces, while the raw natural body agrees on the public
payload. Callback mutations prove that the effect receives live owner
metadata and that the sound call receives the cached original actor even when
the query and effect helpers mutate owner storage. Native 32-bit O0, O2, and
O3 builds plus eleven independent behavior-changing controls pass. The three
focused tests and 19 shared progress, Game-data-layout, generated-PC16, and
guarded-padder tests all pass.

There are no direct JAL callers. The sole aligned pointer literal is at ROM
`0x22FA98`, callback entry `D_8008AFD0[2]`. The complete 41-function owner
preserves the other 40 functions. Strict qualified-versus-production
comparison retains all 6,051 function addresses, uses zero exclusions, and
reports only `func_151A9BA0` changed before installation and no changed
function afterward. Protected Game data remains exact at 189,088 bytes
across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `eb633b6480ce2c084ee24e038c5e80e23ad529a3024c3cef81051d24811c7635` |
| Installed source | `a817fc3d75be07f1667201e3084a1d531c888f87c91752a97f48e87ff1d21077` |
| Predecessor linked ELF | `d3db31e76a768dcf445c57e947152fe0130c8657802d83b680f200dd381022ca` |
| Qualified/production linked ELF | `9317684d00e7c96b5bb37c765d5ca32730cd07447b44fd7a2bbc509f0a7252fc` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `4f9978e782319fc100d52c601a64f3916d16f056cfff04b0785f650845cb86ac` |

The actual `make all -j4` rebuilt the complete guarded corpus, regenerated the
linker script, linked `conker.us.elf`, and generated `conker.us.bin`. Every
existing guard remained valid. The build stopped only at the expected final
whole-ROM SHA mismatch while the decomp remains incomplete.

The permanent qualifier and evidence tools were committed first in the tools
submodule as `9322c2d` (`test(game): qualify height sound probe`). Production
source and the eleven checked rows were installed only after that tools
commit.

## Graph retention

The required bounded Graphify update extracted 24,334 nodes versus the
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
`func_150A6760`. Continue with ordinary candidate `func_151AE6B0` (64 words,
60 real differences), followed by `func_151B1828` and `func_151B9214` in the
same 60-difference tier. Every candidate still requires source, ABI/caller,
owner, guest/native, actual Make, complete-image, protected-data, production
recount, documentation, and graph-retention gates before credit.
