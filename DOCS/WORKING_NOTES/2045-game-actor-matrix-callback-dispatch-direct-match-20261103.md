# Game Actor Matrix Callback Dispatch Direct Match

Date: 2026-11-03

## Result

`func_15132A88` now replaces its zero-return placeholder with byte-exact direct
C. Its complete retail slot is **62 words / 248 bytes**, frame `0x18`, VA
`15132A88..15132B80`, and ROM `15FF38..160030`. A fresh production recount
credits exactly this function:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 4,115 / 5,511 (74.67%) | 0 | 1,396 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,442 / 4,838 (71.15%) | 0 | 1,396 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The active 80% target now needs **294 more** exact functions.

## Source recovery and direct closure

The update first clears actor flag `0x200000`. Flag `0x20000` suppresses the
rest of the update. When flag `0x400` and the pointer at actor offset `+0x6C`
are both present, `func_151464B8` can also defer the update. The routine then
reloads the live flags: flag `0x80000` republishes `0x200000` without invoking
a matrix callback.

Otherwise the unsigned callback selector at `+0x78` indexes
`D_8008998C`. The callback receives the selected fixed-matrix output at
`actor + D_800BE9C0 * 0x40 + 0x90` and the actor itself. Return `-1` retires
the actor through `func_1516972C`; zero clears flag `0x40000`; any other value
sets `0x240000` in the callback's live post-call flags.

The critical source shape is the in-place opening clear followed by a reload:
`actor->flags &= ~0x200000; flags = actor->flags;`. A detached expression and
store changes IDO's temporary-register allocation across 25 words. With the
in-place form, IDO emits the retail 24-byte frame, branch-likely delay slots,
caller-home lifetime, indirect-call schedule, and all **62 words directly from
C**. There are zero guards, insertions, or omissions.

The compact-object payload, with relocation fields unresolved, has SHA-256
`d8369d118c0bfd39199a9304ee94072be81bca54bb86d543d63be37666263029`.
The linked retail payload has SHA-256
`ae72b23bedc2985367c742e841bedf5ff2ca9283b87d065a45d578f2e4eafd43`.
All six original bindings remain semantic: J26 `func_151464B8` at `+0x040`,
HI16/LO16 `D_800BE9C0` at `+0x058/+0x078`, HI16/LO16 `D_8008998C` at
`+0x07C/+0x088`, and J26 `func_1516972C` at `+0x0A8`.

## ABI, routing, and semantic qualification

The installed definition has the recovered void update ABI and a named
`ActorMatrixDispatch15F680` containing the verified fields at `+0x60`, `+0x6C`,
and `+0x78`. The ROM contains no direct JAL to this routine. Its two aligned
pointer literals are at ROM `0x230488` and `0x230E14`, descriptor slots
`D_8008B4D4+0x4F4` and `D_8008B4D4+0xE80`. The selected callback's two-argument
ABI is independently fixed by its table and the already-qualified
`func_15133A94` implementation.

The big-endian guest oracle runs 216 executions across twelve control-flow
states, three matrix slots, three callback indices, and two stack phases. It
checks helper/callback clobbers, live flag mutations after both calls, output
addressing, callback identity, actor retirement, and all three callback-result
routes. Every structurally reachable retail word executes. The duplicate flag
reload at `+0xD8` is behind the branch-likely/nonzero target and the zero-route
unconditional branch, so it is unreachable by construction and checked
statically.

Native 32-bit O0, O2, and O3 builds pass. Ten independent controls alter the
opening clear, three gates, callback index, output stride, negative-result
test, zero-result clear, positive-result mask, or retirement call; every
control fails as intended. Forty-two clean pre-install owner/callback
regressions passed in 45.622 seconds, followed by five fresh installed tests
in 22.910 seconds. Two unrelated legacy suites were not counted because their
cleaned frozen build snapshots were unavailable; no test from those suites ran.

## Image, data, and production closure

The complete owner preserves all thirty neighboring functions. Strict
qualified-versus-production comparison retains all 6,051 function addresses,
uses zero exclusions, and reports only `func_15132A88` changed before
installation and no changed function afterward. Protected Game data remains
exact at 189,088 bytes across 720 owners, zero different bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Qualified/production owner | `338f935dc4aeb4da567af9f9666f23e399bbb9d6a9743269aa265b1b341258d5` |
| Installed source | `f11a7915c3fb7b7a6657c0e3e9981d14141b596223d2d3368705e54471f13ebb` |
| Predecessor linked ELF | `4cf04115a373a08db538e8d4f6a6b1e61f95a4d562c06428b7725432620d6d21` |
| Qualified/production linked ELF | `c4058a6c3c89494a1fa4458a77124343908aa9fabd4ac7ae42eff135d871700f` |
| Production map | `1cbc78ec7ba3bfd4cd8bef4b83bfdf51fc96dd1d5cf45ab59794d62d86946da1` |
| Unchanged production guard table | `2da43f2c2acf5fed809fd5e948b1b1342a1a085801a78751b352a33cd7974664` |

The actual production Make used the owner's retail `-O2 -g3` profile, rebuilt
the padded object and linker script, linked `conker.us.elf`, and generated
`conker.us.bin`. It stopped only at the expected final whole-ROM SHA mismatch
while the decomp remains incomplete. The permanent candidate screen, strict
qualifier, guest/native oracle, ABI checks, and negative controls were committed
before production source as tools commit `3231af4`
(`test(game): qualify actor matrix callback dispatch`).

## Graph retention

The required bounded Graphify update retained 31,816 nodes from 3,754
still-existing files outside the reduced scan corpus. It rebuilt a 58,192-node
graph with 112,153 edges and 5,083 communities; visualization was skipped at
the configured 5,000-node limit. The retained/refreshed
`graphify-out/graph.json` is 75,499,759 bytes with SHA-256
`502b4aa2e4fa90c1ac05b4f7755174eabc8751cfd1c41f534da42b0a8b732f22`.
This is bounded old-node retention evidence, not a full-corpus extraction
claim.

## Continuation

The seven documented handwritten/custom-ABI boundary cases remain outside the
ordinary queue. The fresh ordinary ranking now starts at `func_150CB0E0` (64
words, 61 real differences), followed by the other 61-difference tie members.
Every candidate still requires source, ABI/caller, owner, guest/native, actual
Make, complete-image, protected-data, production recount, documentation, and
graph-retention gates before credit.
