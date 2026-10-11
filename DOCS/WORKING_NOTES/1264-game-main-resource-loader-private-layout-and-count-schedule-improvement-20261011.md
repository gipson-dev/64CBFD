# Game Main Resource Loader Private Layout And Count Schedule Improvement

Date: 2026-10-11. Same complete func_1503CF20, VA
0x1503CF20..0x1503D368, ROM 0x6A3D0..0x6A818, 274 words / 1,096 bytes.
Owner: conker/src/game/generated_6A3D0.c. Installed qualified improvement,
not a conversion or byte-exact match. The full Game matching goal stays active.

## Baseline And Decision

Consumer fe1c6580cf1b20b0ef94e72c6ba8df506a0c8892, mounted tools
f8fac5551d5827c593630c0c919c3d1dcc5e85e0. The complete
[Note 1263](1263-game-main-resource-loader-original-frame-improvement-20261011.md)
checkpoint emitted 274 words, original 0x78 frame, saved S0..S6, early S6
status and continuous S5 count lifetime, with 98 raw differences and no guards.
Both active checkouts were clean. Preserve that immutable source/ELF baseline
in the new test checkpoint; do not refresh it to the installed candidate.

Install the qualified 274-word/0x78/24-difference body. Recover three original
private slots, the unmasked first-count store/separate masked branch value,
the temporary-register cycle through both relocation loops, and event-opening
index-before-offset initialization. Keep every publication/helper/error path.
No guards, new compiler profile, forced padding locals or synthetic uses.

## Discriminating Source Measurements

New tools: experiments/game_main_resource_loader_private_layout.py and
tests/test_game_main_resource_loader_private_layout.py. Reuse the existing
retail O2/g3/no-loop-unroll profile, instruction/reference/native32 helpers
and complete-owner/padder checks. Source fingerprints and complete output
shapes are recorded in ignored private-layout/measurements.json.
The final 60-form complete diagnostic sweep has zero compiler diagnostics
or data pools. Only the selected form has full installation/native32/owner/
padder qualification; do not generalize that acceptance to the other forms.

| Complete Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Banked original-frame body | 274 | 0x78 | 98 |
| Output/boundary declaration order only | 274 | 0x78 | 94 |
| Separate first-count store and test | 274 | 0x78 | 36 |
| Store separation, declaration order, explicit gated event loop | 274 | 0x78 | 28 |
| Selected: explicit word-table byte displacement | 274 | 0x78 | 24 |
| Selected with register/unsigned displacement hints | 274 | 0x78 | 24 |
| Explicit halfword displacement | 276 | 0x80 | 246 |
| Ordered direct request-error literal return | 285 | 0x70 | 282 |

The first count now has separate D_800C4778 publication and test statements.
IDO emits the unmasked shift result in SH, a separately masked branch operand,
and retail's following temporary-register cycle. Declaration order places
the request output at SP+0x6C and shared boundary at SP+0x68. Explicit wordIndex
= identity * 4 recovers the halfword-index spill at SP+0x4C. wordIndex is a
byte displacement, not a descriptor-loop index; table accesses retain each
array's actual u32/u32-pointer/u8-pointer type. Cleanup slots remain u8 **.

An explicit gated event do-loop recovers index-before-offset initialization
without caching its live count or table base. Width, alias/public access order,
cached unsigned secondary count and callback-rebound cleanup stay unchanged.
Both main output and optional cleanup pointers are reread after callbacks.

Additional real table aliases, initial-size and cleanup-value locals do not
resolve the remaining spill/cleanup allocation; some enlarge the frame or
exceed the slot. Direct request-error return still loses S6. Do not install
those lower-frame or larger bodies. Read-only free-callee inspection confirms
func_10004074 is void func_10004074(void *); do not invent a different return
type to coerce the cleanup register allocation. No compiler changes.

## Fresh Qualification

- Eleven pre-install tests pass in 22.425 seconds; the final expanded installed
  suite passes all twelve tests in 22.771 seconds, with zero candidate/owner
  compiler diagnostics. The prior eleven-test installed run also passed.
- All 273 reachable original/current words execute against the complete
  independent public-memory/access/call/error reference: 1,021 cases / 2,042
  runs. The original duplicate compare at +0x48 is statically unreachable.
- Thirty live-loop/cleanup callback cases, 175 sign/width/unsigned-size/alias
  cases, nine independent links and 1,800 fired public-access fault pairs pass.
  Private-frame faults remain explicitly unqualified.
- Ten freshly compiled semantic controls, effective incoming-status and
  request-error controls, three stale-install guards and 96 ignored-word
  identity/presence/extras cases pass. Private output addresses are normalized.
- Actual native32 complete C passes 6,048 cases at each O2/O0 profile, with
  full modeled memory/helper traces and an effective missing-main-free control.
- All 14 owner neighbors, extents, relocations and pools are preserved through
  both actual padders; no change to the typed five-word caller contract.
- Actual 104-word parent/274-word main/56-word extras/nine-word relocator/
  194-word buffer chain passes 768 cases / 1,536 runs. Reached words remain
  41/256/56/9/140 respectively; this is not all-chain/runtime coverage.
- All three older loader suites pass freshly: 32 tests in 116.697 seconds.
  Only exact qualified-successor recognition changes in their installation
  audits; frozen inputs, old candidate bodies and semantic controls stay intact.
- Five historical status-join tests pass freshly in 199.573 seconds, including
  all 31 complete prior variants, rebases, live callbacks and effective controls.
  The audit first verifies the exact original -> count -> private-layout
  successor source and whole-ELF patch before recognizing the installed body.
- The new remaining-difference test proves the exact four-group partition
  below, including both independent initialization words and each spill/
  return/cleanup encoding. All other 250 words are directly byte-exact.
- Consumer, mounted and older WSL tools checks pass; all six changed tool
  files and both copied new files pass native py_compile. Required build/CSV
  finishes before final tests. Preserve the duplicate generated_12D630 recipe
  warning; this is not a warning-free full build claim.

Request/child/auxiliary/cleanup/allocator/copy/free internals remain bounded.
No real heap, hardware, rendering, gameplay, emulator/guest debugger, editor
or 64-bit host acceptance is claimed. Previous neighbor receipts remain
previous unchanged evidence, not new tests for uninstalled diagnostic forms.

## Whole-ELF Delta

New source SHA-256:
e4f9fce4dedc2af6b504ce2ad7b23c253ef9254e4ba92bad340663ea4d30e0f9.
New ELF SHA-256:
6fb98976111c9c1fa5a47bfcd078f8272a4b90535f273cf5fe5bc8532f5aac5c.

Only 92 target ELF bytes change from the committed Note 1263 checkpoint.
Every other ELF byte, symbol name/value/extent and metadata byte is identical.
All 189,088 protected data bytes / 720 owners remain exact, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Guard manifest, conversion CSV, rodata source, symbols, auto assignments and
layout retain their immutable hashes. No other production function changes.
Root README aggregate rows stay correct and unchanged, SHA-256
0c2e0ab2781b9f7dcc9e86e79bbcc3f8b57d107ca28b02e51f524b8232a6f1cd.
No matching or conversion credit until the complete routine is byte-exact.

Fresh `make -C conker match-progress NON_MATCHING=1` finishes successfully:
Game 2,789/4,822 (57.84%), total 3,462/5,495 (63.00%), Init 492/492 and
Debugger 181/181, zero address drift / 2,033 different. These unchanged
aggregate matching rows are independently measured, not inferred from
the candidate's 24-word difference count.

## Ownership And Workflow

Commit mounted tools first, then production C, docs and consumer pin. No push.
Mounted tools commit 5a5e17e5930a669660a8bae72a2f45f3127f2481 banks the
new experiment/qualification and four exact-successor audit extensions;
the mounted checkout is clean before updating the consumer pin.
Copy only the two absent new paths to the older sibling; preserve its 18
existing protected fingerprints, independently dirty work and HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a. Do not overwrite its older audit
tests or commit/reset its independent history. Dirty entries 295 -> 297,
all 18 old fingerprints and HEAD verified unchanged. No OGL/Release/save/editor/
private-input changes; Release stays frozen.

Native Graphify query finds the complete target and direct caller/helper
relationships. Update refuses unsafe shrink 39,792 -> 18,010 while retaining
19,398 nodes from 2,972 existing excluded files. Preserve protective/version/
devcontainer warnings; no force/purge/install. After the consumer commit,
require fresh hook-log growth/UTC, a fresh Rebuilt record and zero actual
Graphify/Python workers before close-out. Single Codex writer, zero Claude
calls: compiler output and independent references settle this step locally.

## Remaining 24 Words

Continue this same full routine, not an easier neighbor. These are measured
raw differences, not an inferred count or permission to mask them with guards:

- Fourteen private spill references: main address SP+0x50 versus retail
  +0x58, word displacement SP+0x54 versus +0x5C. Original frame, saved-register
  slots, request output +0x6C, boundary +0x68 and half-index +0x4C now match.
- Two independent first-count initialization words at +0x1A4/+0x1B8:
  initial S1 zero and the SP+0x4C store are exchanged relative to retail.
- Two request-error return words at +0xB0/+0xB4: current branch joins final
  S6-to-V0 return; retail jumps straight to epilogue with literal V0 = 1.
- Six closed cleanup register-transfer words at +0x3BC/+0x3C0/+0x3CC and
  +0x3E4/+0x3E8/+0x3F4: current loads/tests A0 with NOP call delay;
  retail loads/tests V0 and moves it to A0 in the delay slot.

Recover the two spills and independent schedule using real source lifetimes
without forced locals, pointer type punning or ABI changes. Reconcile request
return and cleanup transfers with full fault/alias/native/owner/padder/caller
qualification. Audit the whole linked ELF after each installed improvement.
Private-frame fault order and deeper runtime remain separate open gates.
