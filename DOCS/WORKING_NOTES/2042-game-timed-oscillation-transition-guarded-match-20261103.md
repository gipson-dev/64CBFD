# Game Timed Oscillation Transition Guarded Match

Date: 2026-11-03

## Result

`func_151B9214` now replaces its zero-return placeholder with byte-exact
guarded C. Its complete retail slot is **63 words / 252 bytes**, frame `0x20`,
VA `151B9214..151B9310`, and ROM `1E66C4..1E67C0`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,112 / 5,511 (74.61%) | 0 | 1,399 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,439 / 4,838 (71.08%) | 0 | 1,399 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **297 more** exact functions.

## Source recovery and guarded closure

The recovered callback takes one owner pointer and updates the embedded
oscillation state at `owner+0x170`. Its nine floating fields are oscillation at
`+0x00`, amplitude at `+0x04`, phase at `+0x08`, phase rate at `+0x0C`, target
amplitude at `+0x10`, target phase rate at `+0x14`, transition time at `+0x18`,
amplitude velocity at `+0x1C`, and phase-rate velocity at `+0x20`.

Each call advances phase by the phase rate times the live frame step
`D_800BE9A4`, normalizes it through `func_15144B68`, and stores
`sinf(phase) * amplitude` as the current oscillation. While transition time is
positive, the callback subtracts another live frame-step read and integrates
both velocities. Once the timer expires, it eases amplitude and phase rate
toward their targets with `D_800AA564`. It returns one so the callback remains
active.

IDO naturally emits the complete behavior in the retail 63-word width but
selects frame `0x28`, different local homes, and a different floating-register
allocation. Twenty checked positional rows close only those compiler layout
choices:

| Raw offset | Compiler word | Retail word | Qualified action |
| ---: | ---: | ---: | --- |
| `0x000` | `27BDFFD8` | `27BDFFE0` | Use retail's 32-byte frame. |
| `0x02C` | `AFA40028` | `AFA40020` | Move the owner home with the frame. |
| `0x030` | `8FA40028` | `8FA40020` | Reload the owner from its retail home. |
| `0x044` | `AFA2001C` | `AFA20018` | Move the state-pointer home. |
| `0x048` | `8FA2001C` | `8FA20018` | Reload the state pointer from its retail home. |
| `0x054` | `C44C0004` | `C4420004` | Keep amplitude in retail F2. |
| `0x058` | `C4420018` | `C44C0018` | Keep transition time in retail F12. |
| `0x060` | `460C0482` | `46020482` | Multiply sine by retail's amplitude register. |
| `0x064` | `4602203C` | `460C203C` | Compare retail's transition-time register. |
| `0x080` | `46061281` | `46066281` | Subtract the live frame step from transition time. |
| `0x0A4` | `46106100` | `46101100` | Add amplitude velocity through retail F2. |
| `0x0B0` | `C442000C` | `C440000C` | Keep the expired-route phase rate in retail F0. |
| `0x0C0` | `46029181` | `46009181` | Subtract retail's phase-rate register. |
| `0x0C4` | `C4200000` | `C42C0000` | Load the transition scale into retail F12. |
| `0x0C8` | `460C8101` | `46028101` | Subtract retail's amplitude register. |
| `0x0CC` | `46003282` | `460C3282` | Scale the phase-rate delta through retail F12. |
| `0x0D4` | `46002482` | `460C2482` | Scale the amplitude delta through retail F12. |
| `0x0D8` | `460A1200` | `460A0200` | Add the scaled phase-rate delta through retail F0. |
| `0x0DC` | `46126180` | `46121180` | Add the scaled amplitude delta through retail F2. |
| `0x0F0` | `27BD0028` | `27BD0020` | Restore retail's frame size. |

Every row checks its expected compiler word and fails closed when stale. The
eight symbolic relocations remain intact: HI16/LO16 pairs for `D_800BE9A4` at
`0x008/0x00C` and `0x050/0x05C`, J26 calls to `func_15144B68` and `sinf` at
`0x028/0x040`, and the HI16/LO16 pair for `D_800AA564` at `0x0BC/0x0C4`.
The unqualified compact body has SHA-256
`f00d687c48b7bf5e180ad4d5da86e68af85e94edd0a6c49cb3fe79694b8dba0f`;
the qualified retail body has SHA-256
`f4d52581d33f3d3cbc8db7f8dc7fbc284fbdedb4044654668519e9ef20d812cd`.

## Semantic, registry, and production qualification

The big-endian guest oracle runs 2,048 executions across both timer routes,
all state fields, callback mutations, helper clobbers, and live frame-step
reads. Every one of the 63 retail words is covered. Native 32-bit O0, O2, and
O3 builds and ten independent behavior-changing controls pass. The three
focused tests and 22 shared oscillator, progress, Game-data-layout,
generated-PC16, and guarded-padder tests all pass: 25 installed tests in
65.932 seconds. Twenty stale-row mutations prove every guard is effective.

There are no direct JAL callers. The sole aligned pointer literal is at ROM
`0x22E394`, callback entry `D_800898B0[9]`. The complete five-function owner
preserves the other four functions. Strict qualified-versus-production
comparison retains all 6,051 function addresses, uses zero exclusions, and
reports only `func_151B9214` changed before installation and no changed
function afterward. Protected Game data remains exact at 189,088 bytes across
720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `cc59eddce5272e0a131fcd26f571e3d65232f99dede3113f9fb236657212bf24` |
| Installed source | `2aff82497ee5faec1020d04c642e92a08ad0e234a0fd5a6ae7695e9263d28bd6` |
| Predecessor linked ELF | `c48ba070872f8a762f56a9a5a1ea26ae2904e306717ad2f3c4df7249a4d4996d` |
| Qualified/production linked ELF | `cb7cd39489d81a8e68f9b1d0851ee5f3bdfe12fa07bf1aee9243915ed0f335bc` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Production guard table | `2da43f2c2acf5fed809fd5e948b1b1342a1a085801a78751b352a33cd7974664` |

The actual `make all -j4` rebuilt the complete guarded corpus, regenerated the
linker script, linked `conker.us.elf`, and generated `conker.us.bin`. Every
existing guard remained valid. The build stopped only at the expected final
whole-ROM SHA mismatch while the decomp remains incomplete.

The permanent qualifier and evidence tools were committed first in the tools
submodule as `65b8fb1` (`test(game): qualify timed oscillation transition`).
Production source and the twenty checked rows were installed only after that
tools commit.

## Graph retention

The required bounded Graphify update proposed 58,383 nodes versus the retained
58,384 and refused to overwrite without `--force`. Its fail-closed pass also
reported retention of 31,816 nodes from 3,754 still-existing files outside the
reduced scan corpus. The retained `graphify-out/graph.json` remains 77,250,386
bytes with 120,179 links and SHA-256
`2b00b0aa755a17017c25c30147af6ba7974722f5c50675421fc41f4bc545b0c8`.
This is old-node retention evidence, not a full-corpus refresh claim.

## Continuation

The fresh ranking still begins with seven documented non-ordinary boundary
cases: handwritten/custom-ABI `func_150A76F0`, `func_151F8870`,
`func_150A613C`, `func_150AE280`, `func_15115F68`, `func_151AE2BC`, and
`func_150A6760`. Several ordinary routines then tie at 61 real differences.
Continue with adjacent owner function `func_151B9310` (62 words, 61 real
differences) to reuse the now-qualified owner and callback context; this is a
workflow tie-break, not a claim that the other tied rows are lower priority.
Every candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
