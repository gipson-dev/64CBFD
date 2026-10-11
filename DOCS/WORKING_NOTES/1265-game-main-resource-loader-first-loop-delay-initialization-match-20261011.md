# Game Main Resource Loader First-Loop Delay Initialization

Date: 2026-10-11. Same complete func_1503CF20, VA
0x1503CF20..0x1503D368, ROM 0x6A3D0..0x6A818, 274 words / 1,096 bytes.
Owner: conker/src/game/generated_6A3D0.c. Qualified scheduling improvement,
not a conversion or complete byte-exact match. The wider Game goal is active.

## Baseline And Decision

Consumer 42db50ad8a9ef12e8820115f67f5ce963afdb0fb, mounted tools
5a5e17e5930a669660a8bae72a2f45f3127f2481. Both active checkouts were clean.
[Note 1264](1264-game-main-resource-loader-private-layout-and-count-schedule-improvement-20261011.md)
banked all 274 words, original 0x78 frame/S0..S6/early S6/continuous S5,
three recovered private slots and count/event schedule, with 24 raw
differences and no guards. Freeze that exact source/ELF checkpoint in the
new qualification; do not refresh its hashes to the selected candidate.

Recover the first loop's two independent initialization instructions with
`if ((index = 0, D_800C4778[identity] > 0))`. This initializes the index even
for an empty first loop, after the public count store and before its test.
The comma sequence preserves the actual behavior and lets IDO place the
existing half-index store at +0x1A4 and S1 zero at +0x1B8, the BLEZ delay
slot. Both now emit directly as AFA6004C and 00008825. No padding locals,
synthetic uses, altered ABI, compiler-profile changes or expected-word guards.

## Complete-Body Experiments

New tools: experiments/game_main_resource_loader_remaining_schedule.py and
tests/test_game_main_resource_loader_remaining_schedule.py. Reuse the retail
O2/g3/no-loop-unroll profile and existing compiler/MIPS/native32/padder helpers.
The final 45 complete diagnostic forms all compile without diagnostics or
data pools; only the selected body has full acceptance qualification.

| Complete Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Banked body / index before store | 274 | 0x78 | 24 |
| Selected: initialization in comma test | 274 | 0x78 | 22 |
| Initialization only inside positive branch | 273 | 0x78 | 165 |
| Lexically scoped cleanup value | 274 | 0x80 | 47 |
| Direct request-error return | 285 | 0x70 | 282 |
| Separate request-error literal-return label | 285 | 0x70 | 281 |
| Nested request-success body | 286 | 0x70 | 282 |
| Nested request-failure status join | 274 | 0x78 | 220 |
| Reused main/cleanup table slot with selected schedule | 274 | 0x78 | 22 |

Real scoped cleanup values still enlarge the frame; direct literal request
returns still lose saved S6 and exceed the slot. Existing output/boundary
reuse, register hints and table-slot rebinding do not improve the selected
body. Do not install those alternatives or change the void free-callee ABI.
An initial diagnostic incorrectly marked addressed output as register;
IDO rejected its address operand. Remove that invalid form and rerun the
complete 45-form sweep successfully. This was an experiment-input error,
not a production defect or warning-free first-run claim.

## Fresh Qualification

- All twelve pre-install tests pass in 25.345 seconds; all twelve installed
  tests pass in 25.975 seconds, with zero candidate/owner diagnostics.
- All 273 reachable original/current words execute against the independent
  complete public-memory/access/call/error reference: 1,021 cases / 2,042
  runs. Only the original duplicate compare at +0x48 is unreachable.
- Thirty live-loop/cleanup callback cases, 175 width/sign/unsigned-size/alias
  cases, nine independent links and 1,800 fired public-access fault pairs pass.
  Private-frame faults remain explicitly unqualified.
- Ten freshly compiled semantic controls, two effective incoming-status/
  request-error controls, three stale-install guards and 96 ignored-word
  identity/presence/extras cases pass. Private output addresses are normalized.
- Actual native32 complete C passes 6,048 cases each at O2/O0, full modeled
  memory/helper traces and an effective missing-main-free control.
- All 14 owner neighbors, extents, relocations and pools are preserved by
  both actual padders; the typed five-word caller contract is unchanged.
- The actual 104-word parent/274-word main/56-word extras/nine-word relocator/
  194-word buffer chain passes 768 cases / 1,536 runs. Reached words are
  41/256/56/9/140 respectively; do not claim complete chain/runtime coverage.
- Exact difference partition: 14 spill references, two request-return words
  and six cleanup transfers remain. All other 252 words emit directly exact.
  Comparison with the immutable banked 24-difference body proves that only
  +0x1A4/+0x1B8 change; both are independently verified against retail.
- All four older loader suites pass freshly: 44 tests in 92.723 seconds.
  Their installed audits recognize only the exact source successor and
  independently compiled complete body before checking the whole ELF.
- All five historical status-join tests pass freshly in 128.597 seconds,
  including complete prior variants, live callbacks, independent rebases,
  ignored-word/effective controls and exact linked-baseline preservation.
- Consumer/mounted/older WSL tools checks and native py_compile for all seven
  changed tool files plus both copied new files pass. Required build/CSV
  finishes before installed tests. Preserve the duplicate generated_12D630
  recipe warning; this is not a warning-free full build claim.

Request/child/auxiliary/cleanup/allocator/copy/free internals remain bounded.
No real heap, hardware, rendering, gameplay, emulator/guest debugger, editor
or 64-bit host acceptance is claimed. Previous uninstalled diagnostic forms
and unchanged prior receipts are not fresh full-acceptance tests.

## Whole-ELF Delta

Installed source SHA-256:
f43fa661893aadea680107f8ebe446bdad763489b5558996c8a906802beca058.
Installed ELF SHA-256:
c4f1a877f41ffc7b442de46f68bae070e47fbb192776913d3d8fa14c785e93c4.

Only eight target ELF bytes change from the banked Note 1264 checkpoint.
Every other ELF byte, symbol name/value/extent and metadata byte is identical.
All 189,088 protected data bytes / 720 owners stay exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Guard manifest, conversion CSV, rodata source, symbols, auto assignments and
layout retain their immutable hashes. No other production routine changes.
Root README stays unchanged, SHA-256
0c2e0ab2781b9f7dcc9e86e79bbcc3f8b57d107ca28b02e51f524b8232a6f1cd.
No matching or conversion credit until the complete function is byte-exact.

Fresh `make -C conker match-progress NON_MATCHING=1` finishes successfully:
Game 2,789/4,822 (57.84%), total 3,462/5,495 (63.00%), Init 492/492 and
Debugger 181/181, zero address drift / 2,033 different. These unchanged
aggregate rows are measured from the linked ELF, not inferred from the
selected body's 22-word difference count.

## Ownership And Workflow

Single Codex writer, zero Claude calls: complete compiler output and
independent references settle this decision locally. Preserve the original
candidate/reference/control/frozen-input history in the five older suites;
only exact qualified-successor recognition changes in their installed audits.
Commit mounted tools first, then consumer source/docs/pin. No push.
Mounted tools b9eae4717cd9f9b38a2c1fde31f9903254723e9b banks the two new
authored paths and five exact-successor audit extensions; its checkout is
clean before updating the consumer pin.
Preserve the older sibling's independent history and conflicting audit tests;
copy only the two absent new authored paths. No OGL/Release/save/editor/
private-input changes; Release stays frozen. The OGL sibling needs no import
for this decomp-only independent-instruction schedule.
Older HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 20 protected
existing file fingerprints are unchanged. Dirty entries 297 -> 299 reflect
only the two absent-path copies; their hashes match the mounted new files.

Native Graphify query verifies the target/direct caller/helpers. Refresh the
graph after code changes without force/purge/install. Preserve protective
scan/version warnings. After the consumer commit, require fresh hook-log
growth/UTC, a fresh Rebuilt record and zero actual Graphify/Python workers.
The native update refuses unsafe shrink 39,802 -> 18,030 and retains
19,398 nodes from 2,972 existing excluded files. Its protective exit 1 and
devcontainer/version warnings are preserved, not overridden.

## Remaining 22 Words

Continue this same full routine, not an easier neighbor:

- Fourteen references to main SP+0x50 versus retail +0x58 and word displacement
  SP+0x54 versus +0x5C. Original frame/saves, output +0x6C, boundary +0x68 and
  half-index +0x4C are preserved and the initialization schedule now matches.
- Two request-return words +0xB0/+0xB4: current branch joins S6-to-V0 return;
  retail jumps straight to the epilogue with literal V0 = 1.
- Six cleanup transfers +0x3BC/+0x3C0/+0x3CC and +0x3E4/+0x3E8/+0x3F4:
  current loads/tests A0 with NOP call delay; retail loads/tests V0 and moves
  it into A0 in the delay slot.

Recover real source lifetimes/control flow without forced locals, pointer
type punning, guards or ABI changes. Requalify full faults/aliases/native32/
owner/padders/caller behavior and whole-ELF preservation after improvements.
Private-frame fault order and deeper runtime remain separate open gates.
