# Game Matrix-Route Guarded Match

Date: 2026-11-03

## Result

`func_1514654C` is now byte-exact guarded C in production. Its complete retail
slot is **120 words / 480 bytes**, frame `0xA0`, VA
`1514654C..1514672C`, and ROM `1739FC..173BDC`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,106 / 5,511 (74.51%) | 0 | 1,405 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,433 / 4,838 (70.96%) | 0 | 1,405 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **303 more** exact functions.

## Source recovery and closure

The prior production body from Notes 1103 through 1105 was already complete
semantic C with the correct 120-word slot, frame `0xA0`, private matrix at
`sp+0x4C`, resolver outputs at `sp+0x90/+0x8C`, and 60 positional word
differences. The final source form separates the actor matrix bank from the
selected matrix, retains the lookup-node/input-cursor reuse, and reuses the
actor formal for the disjoint output-cursor lifetime. It compiles naturally as
C119 with the same frame and private addresses. Its opening saved-register
phase, complete sixteen-word transform loop, and epilogue match directly.

The retained evidence family contains 92 additional branch/register/storage
forms in this final pass and 377 measured forms across the three earlier
recovery notes. Explicit key gates, register locals, real pointer aliases,
volatile rereads, alternate output carriers, and structured/label flow forms
did not recover the remaining retail branch/read topology. Forms that reached
C120 produced at least 63 differences and lost the exact private resolver
offsets. No broad 60-row normalization was accepted.

Twelve checked rows close only the isolated compiler branch/load schedule:

| Raw offset | Qualified action |
| ---: | --- |
| `0x044` | Retarget the early-failure branch across the inserted preload. |
| `0x054` | Keep the attachment lookup key in retail V0. |
| `0x068` | Retarget the attachment-failure branch across the preload. |
| `0x084` | Retarget the attachment-success branch across the preload. |
| `0x08C` | Reload the keyed-route lookup key into retail V0. |
| `0x094` | Use retail's normal zero-key branch through V0. |
| `0x098` | Move the nonzero key to A1 in the branch delay slot. |
| `0x0AC` | Retarget keyed-lookup failure across the preload. |
| `0x0D0` | Retarget resolver failure across the preload. |
| `0x0D8` | Preserve the natural attachment load and insert primary load `0x8FA50090`. |
| `0x0FC` | Replace the now-duplicate late primary reload with a NOP. |
| `0x138` | Preserve retail's commutative delegated-bank addition order. |

Five rows are immediate-only branch retargets caused by the single inserted
word. Every row checks its expected compiler word and fails closed when stale.

The qualified body retains all nine semantic relocation sites:

| Function offset | Relocation |
| ---: | --- |
| `0x05C`, `0x070` | HI16/LO16 `D_800BE9C0` |
| `0x09C` | J26 `func_1503195C` |
| `0x0C0` | J26 `func_15031070` |
| `0x10C`, `0x118` | HI16/LO16 `D_800BE9C0` |
| `0x138` | J26 `func_15145EA4` |
| `0x150` | J26 `guMtxL2F` |
| `0x194` | J26 `func_150A7960` |

## Semantic and production qualification

The retained route oracle covers all public routes, five lazy gates, twelve
required-storage faults, four guest-only wrapping indices, 16 prior private
matrix counterexamples, and 560 additional source/destination/resolver-output
overlaps. The final source passes 1,728 public-trace fixtures, 336 home
mutations, 24 attachment changes, 864 connected original-helper cases, and
9,216 native 32-bit cases plus native lazy gates. All 92 controls compile and
pass 2,208 ordinary executions; none is treated as a match merely for sharing
public effects.

The pre-install qualifier passed all 11 tests in 799.570 seconds. After
installation and the actual production build, the same 11-test module passed
again in 155.138 seconds. It verifies the exact 120 words, all twelve stale-row
failures, actual private addresses, original helpers, native complete C and SDK
converter, equal normalized pools, and all 88 unchanged neighboring functions
in the 89-function owner. The 19 shared progress, complete Game-data-layout,
generated-PC16, and guarded-padder tests pass in 7.855 seconds.

The live linked caller census contains five direct JAL sites:

| Caller | ROM call site |
| --- | ---: |
| `func_150C44A4` | `0xF1B24` |
| `func_150D4AE0` | `0x101FFC` |
| `func_150FEFD0` | `0x12C518` |
| `func_150FF6E0` | `0x12CC8C` |
| `func_151C62D0` | `0x1F3918` |

Three earlier provisional offsets (`0x55D50`, `0x130310`, and `0x1F27FC`)
contain zero words in the production binary and are not callers.

Strict qualified-versus-production comparison retains all 6,051 function
addresses, uses zero exclusions, and reports no changed function after
installation. Protected Game data remains exact at 189,088 bytes across 720
owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `95018796760eafe7ad2c855a3b49331de5dc2d46a610b87e3989cd10c1906aaf` |
| Qualified/production linked ELF | `3ba75ce7ff9c686009dc1f8d1cb3814d8067c68c6a9d08bae52399a520d85d34` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `4b4ffe1b47865c0ba23bbc6b4fb63969c564072c94b7a01691b5c5877bd33853` |

The actual `make all -j4` rebuilt the complete guarded corpus, regenerated the
linker script, linked the ELF, and generated the binary. Every existing guard
remained valid. The build stopped only at the expected whole-ROM SHA mismatch
while the decomp remains incomplete.

The permanent qualifier and evidence tools were committed first in the tools
submodule as `1a20f53` (`test(game): qualify guarded matrix route match`). The
source and twelve production rows are installed only after that tools commit.

## Graph retention

The required bounded Graphify update extracted 24,311 nodes versus the
retained 58,384. It failed closed without `--force`, preserving 31,816 nodes
from 3,754 still-existing files outside the reduced scan corpus. The retained
`graphify-out/graph.json` remains 77,250,386 bytes with SHA-256
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim. The
existing Graphify 0.9.20-skill/0.9.26-package and empty `devcontainer.json`
warnings remain non-blocking and did not replace the graph.

## Continuation

The fresh ordinary Game ranking keeps the same seven documented boundary cases
outside the direct-C queue: `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Continue with ordinary candidate `func_1515EB84` (61 words,
60 real differences), followed by the remaining 60-difference ties. Every
candidate still requires source, ABI/caller, owner, guest/native, actual Make,
complete-image, protected-data, production recount, documentation, and graph
retention gates before credit.
