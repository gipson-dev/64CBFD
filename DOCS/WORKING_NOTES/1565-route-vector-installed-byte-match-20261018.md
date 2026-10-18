# Route Vector Installed Byte Match

Date: 2026-10-18. Consumer predecessor: `4507f858`. Tools committed first as
`a48f19d`. Completes the same target from
[Note 1564](1564-route-vector-saved-role-recovery-and-isolated-layout-match-20261018.md).

## Installed Result

Replace `func_15088F30`'s zero-return placeholder with complete typed
`void func_15088F30(u8 *record, f32 *xOutput, f32 *yOutput, f32 *zOutput)`.
The linked **83-word, 332-byte, frame-16** routine matches retail throughout
VA `15088F30..1508907C` / ROM `B63E0..B652C`. Its local declaration in the
live C caller is corrected to the explicit void/four-pointer interface.

This is a **normalized C match, not a direct compiler match**. Raw C retains
56 word differences; the closed layout retains all 83 source instruction
origins, with no insertion, omission or frame change. The original S0/S1
invariant roles and private saved homes are preserved. Append 83 strict
expected-word/binding rows while retaining all **2,476,075 prior guard bytes**.
No Makefile, compiler, unrelated source or original assembly change.

Fresh `make -C conker match-progress NON_MATCHING=1` reports:

| Section | Byte-Exact | Different | Address Drift |
| --- | ---: | ---: | ---: |
| Total | 3,663 / 5,501 (66.59%) | 1,838 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,990 / 4,828 (61.93%) | 1,838 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Fresh structured aggregation of progress.csv also confirms the converted
function/byte figures are unchanged: total 5,501/6,044 and 86.04% of bytes;
Game 4,828/5,323 and 85.41%. The old stub already counted as C. Root README
changes only the two verified byte-exact aggregate rows, not this narrative.

## Actual Caller Boundary

A whole-Game scan of the retail layout finds exactly five direct calls:

| Retail Caller | Call Sites | Current Production State |
| --- | --- | --- |
| func_15087350 | 150874B4, 15087744, 15087954, 1508799C | Still a three-word C stub, not retained assembly |
| func_15088D58 | 15088E58 | Complete 118-word byte-exact C caller |

Correct Note 1564's mistaken description of the former as retained assembly.
No matching credit or full production execution is claimed for that caller.

**144 connected cases** execute the actual live C caller, this vector helper,
and 472 other real linked helper words. Cover actor slots, repeated stepping,
route modes, headings, actor/record aliases and both stack phases. Both raw
C instructions and the installed body agree with the independent public
reference, full ordinary memory and saved ABI. Only atan is a bounded provider.

**576 fired retail-only windows** cover all four other direct sites using
their real argument setup, delay slots and first consumers. Include zero/one
record-speed updates, caller-stack output/record aliases, both stack phases
and V0 poisoned to zero/DEADBEEF after the vector return. Three windows execute
the real 49-word cubic consumer. The first executes its sqrt.s through an
explicit finite, nonnegative test model: 25-to-5 smoke, three invalid-domain
rejections and a required fired instruction counter. These windows are not
full execution of the unrecovered 604-word caller or production gameplay.
Unknown indirect interfaces remain outside this bounded caller qualification.

## Fresh Installed Qualification

**All 13 installed tests pass in 74.172 seconds, no skips.** The preceding
13-test pre-install run passes in 62.701 seconds. In addition to the caller
checks, the installed suite freshly repeats:

- All 83 words and both independent assembly bindings, file-free layout and
  complete source-origin retention.
- 1,650 paired guest cases with complete public/private memory and access
  order; 957 fired synthetic memory prefixes across 22 fixtures. These are
  not hardware traps or universal scratch-register/fault-PC equivalence.
- 65,680 native32 cases per O0/O2 build, both with UBSan, including all
  65,536 signed coordinates. Three effective semantic negatives exit ordinary
  wrong-result 23. Aligned host-endian/pointer32 scope and the guest-only
  incompatible aliases remain explicit.
- Six independent GNU rebase links and 198 paired guest executions across
  code/global placements and HI16/LO16 carry boundaries.
- 85 raw-word/binding controls, 64 layout controls, 44 live/snapshot input
  corruptions, wrong predicted span/unrelated-byte controls and three mixed
  source/guard/image stage rejections.
- Actual mixed-profile padding and all seven expanded Make commands. Primary
  has one no-unroll flag; the normal projection override has none. All 73
  primary functions reproduce, 72 neighbors stay fixed in both profiles,
  and the original four GLOBAL_ASM bodies and projection override remain.

The initial caller-window failure was an unsupported sqrt.s in the test
interpreter, not a production defect. The narrow, tested model above closes
that harness gap. It is not counted as a semantic negative or hardware FP
proof. General NaN payloads, FCSR/trap behavior, full portable C equivalence
and gameplay are not claimed by these finite/provider tests.

The new installation uses a guarded historical view of the 22-input baseline;
the three successor snapshots are immutable and all earlier source points and
fingerprints remain unchanged. Use the installed integration suite below,
not a predecessor-only fixture directly against the new production image.

## Whole-ELF Audit

Before production installation, the first actual link and expanded Make path
predict the complete successor image. The production build reproduces it
exactly: **243 changed ELF bytes**, only this target's instructions and its
symbol size from 12 to 332. **Zero metadata ordering groups or exemptions**.

All **6,057 function addresses** and **6,056 other function bodies** remain
fixed. All **189,088 protected Game-data bytes across 720 owners** remain
exact, with zero differing bytes/owners and data digest
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Successor | SHA-256 |
| --- | --- |
| Whole ELF | `e55a6d218b40d9216dbe690c058132eacbae0e57d009c0f2670501ff46aa65b3` |
| B3020 source | `53bab1289ba22cce5a94208fa441fb9b349cb825185748af3096e293937b685b` |
| Guard manifest | `0d6c65a40cc623678449ea344d3fcb1b4a119f33f619e6964164c4c25b46558e` |

The other 19 members retain their predecessor hashes. The production build
succeeds; the shared manifest triggers dependent recompilation and existing
warnings in untouched sources, plus the duplicate generated_12D630 Make
recipe warnings. No warning-free build is claimed. The target shadow compile
has no new diagnostics.

## Repository And Resume

Tools commit `a48f19d` precedes the consumer pin. Three repository-setup tests
and smoke checks pass in both tools copies; consumer `make tools-check` passes.
Only two absent task files are copied to the standalone mirror, preserving
all 1,268 old dirty-file hashes and its older ddbdd16 HEAD. It now has 1,270
dirty leaf paths, with no mirror reset or commit. Both task-file pairs are
byte-identical, ASCII and AST-valid. No push, Claude call, debugger/emulator
session, host-port change or frozen Release build/launch/modification.

Reproduce from the prepared consumer root under WSL:

```sh
python3 -m unittest tools.tests.test_game_route_vector_integration -v
python3 -m tools.experiments.game_route_vector_integration --audit
make -C conker match-progress NON_MATCHING=1
```

Ignored `conker/build/game-route-vector-integration/` retains first successor
snapshots, private Make plans/objects, native sources/binaries, caller and
stage receipts, prediction and installed audit. No unchanged broad neighbor
suite is described as freshly rerun.

Next recover **func_150870D0**, the adjacent 160-word route-record setup stub,
VA `150870D0..15087350`, ROM `B4580..B4800`, retail frame 0x60. Derive its full
argument/allocator/neighbor contract before editing; keep this installed
vector/spline/dispatcher baseline fixed. The larger func_15087350 caller and
the wider Game matching goal remain open.
