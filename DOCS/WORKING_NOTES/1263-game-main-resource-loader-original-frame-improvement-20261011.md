# Game Main Resource Loader Original-Frame Improvement

Date: 2026-10-11. Same complete func_1503CF20, VA
0x1503CF20..0x1503D368, ROM 0x6A3D0..0x6A818, 274 words / 1,096 bytes.
Owner: conker/src/game/generated_6A3D0.c. This is an installed, qualified
code-generation improvement, not a new conversion or byte-exact match.

## Baseline And Decision

Consumer 4c395c033b656e6e988dec795b190326c6a537f0, mounted tools
9aa880bbdc66bac2d260d2d8109a29339634bdc0. The installed
[Note 1261](1261-game-main-resource-loader-retail-length-improvement-20261011.md)
baseline emitted 274 words, frame 0x80, late S4 status and 271 raw differences.
[Note 1262](1262-game-main-resource-loader-status-join-experiment-20261011.md)
established that a natural request-error return join selects early S6,
but left a redundant count-pointer stack transfer and a larger frame.

Install only the new selected complete body: all 274 words, original 0x78
frame, saved S0..S6 at original offsets, opening S6 zero at target +0x6C,
no redundant private S5 count-pointer store/reload, 98 raw differences.
No guards, new profile, synthetic uses, truncation or cleanup type punning.
This output proves the source/profile effect, not the optimizer's internal
cost model or the original source spelling.

## Controlled Source Changes

New tools: experiments/game_main_resource_loader_count_lifetimes.py and
tests/test_game_main_resource_loader_count_lifetimes.py. Existing retail
O2/g3/no-loop-unroll profile and independent reference helpers are reused.
The fresh 46-form complete diagnostic sweep has zero compiler diagnostics
or data pools; each source fingerprint and output shape is recorded in the
ignored count-lifetimes/measurements.json. Only the selected form receives
the full installation/native32/owner/padder qualification below.

Initialize the ignored incoming second word as status after signed identity
gates. Request failure assigns one and joins the final status return.
Use correctly typed direct main/count/primary/secondary table expressions
instead of redundant local aliases. Keep u8 **cleanupSlot correctly typed.
All public accesses, table publication, mixed indexed/byte cursors, live
primary count/base reloads, cached unsigned secondary count, extras/event
gates, fifth-word flags and callback-rebound failure cleanup remain intact.

| Complete Diagnostic Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Banked late status | 274 | 0x80 | 271 |
| Request-error join, local table aliases | 276 | 0x88 | 194 |
| Request join, direct count | 274 | 0x88 | 110 |
| Direct count and both relocation tables | 274 | 0x80 | 110 |
| Selected: direct main/count/both relocation tables | 274 | 0x78 | 98 |
| Selected plus direct cleanup arrays | 274 | 0x78 | 98 |
| All direct arrays, restore literal request-error return | 285 | 0x70 | 281 |

The direct-count form removes the observed extra S5 stack copy while retaining
continuous S5 count-pointer lifetime. Removing the other aliases resolves
remaining frame pressure. Declaration permutations alone do not recover the
frame. Literal request-error return still loses S6 and exceeds the slot;
do not install that superficially smaller-frame form. Diagnostic variants
are not automatically qualified for installation by a lower difference count.

## Fresh Qualification

- Eleven selected-candidate tests pass before installation in 22.740 seconds
  and after final rebuild in 23.023 seconds.
- All 273 reachable original and selected words execute against the full
  independent public-memory/access/call/error reference: 1,021 cases / 2,042
  guest runs. The duplicate comparison at +0x48 is statically unreachable.
- Thirty live-loop/cleanup callback cases, 175 sign/width/unsigned-size/alias
  cases, nine independent links and 1,800 fired public-access fault pairs pass.
  Private-frame fault order is not compared or accepted.
- Ten fresh effective semantic controls, effective status/request-error
  controls and three stale-install rejections pass. The 96 ignored incoming
  word cases cover early returns and both extras gates.
- Actual native32 complete C passes 6,048 cases each at O2 and O0, including
  full modeled memory/helper traces and an effective missing-main-free control.
- All 14 owner neighbors, relocations and pools are preserved through both
  actual padding routes, with zero candidate/owner compiler diagnostics.
- The actual 104-word parent, 274-word main, 56-word extras, nine-word
  relocator and 194-word buffer chain passes 768 cases / 1,536 runs.
  Reached words are 41/256/56/9/140 respectively; do not claim all-chain coverage.
- Both older loader suites pass freshly: 21 tests in 55.563 seconds.
  Their frozen baselines remain unchanged; only exact qualified-successor
  recognition is added to their installation audits, not weakened semantics.
- Five status-join experiment regressions pass freshly in 137.515 seconds,
  covering all 31 prior complete variants, independent rebases and effective
  controls. Their audit verifies the exact frozen checkpoint -> selected
  source/whole-ELF delta before recognizing this installed successor.
- Consumer, mounted and older WSL tools checks pass; all five changed tool
  files and both copied new files pass native py_compile. Build/CSV completes
  before final tests. Preserve the duplicate generated_12D630 recipe warning;
  this is not a warning-free full build claim.

Two initial audit failures were corrected without relaxing the checks.
The new coverage expectation inherited the six-register prologue's unreachable
compare at +0x44; the seven-register prologue correctly restores it to +0x48.
The first manual installation omitted parentheses around two table expressions.
Restore the exact qualified spelling and rebuild before accepting the audit.
Earlier failed/concurrent runs are not the final sequential passing receipts.

Request/child/auxiliary/cleanup/allocator/copy/free internals remain bounded.
No real heap, hardware, rendering, gameplay, emulator, guest debugger, editor
or 64-bit host acceptance is claimed. Deeper helper restoration stays separate.

## Linked Delta And Progress

New source SHA-256:
d36a98c471e7c89e7be7931aca89a24e273f163b76f6f3cd535371c43349b7aa.
New ELF SHA-256:
0f7e54c89e620884ea89018e2747ae83d5765672022a06043d8b13490ec3e3bc.

The frozen committed checkpoint audit proves only 882 target ELF bytes change.
Every other ELF byte, symbol name/value/extent and metadata byte is identical;
no extent adjustment. All 189,088 protected data bytes / 720 owners remain
exact, SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Guard manifest, conversion CSV, rodata source, symbols, auto assignments and
layout retain their immutable hashes. No other production function changes.

Fresh linked matcher remains Game 2,789/4,822 (57.84%), total 3,462/5,495 (63.00%),
Init 492/492 and Debugger 181/181, zero drift / 2,033 different. No credit.
Root README aggregate rows remain correct and unchanged, SHA-256
0c2e0ab2781b9f7dcc9e86e79bbcc3f8b57d107ca28b02e51f524b8232a6f1cd.

## Ownership And Workflow

Mounted tools f8fac5551d5827c593630c0c919c3d1dcc5e85e0 banks the two new
experiment/test files and three narrowly scoped audit-successor updates first.
Then bank production C, documentation and consumer pin in a separate commit.
No push requested or performed.
Only the two absent new paths are copied to the older sibling; its 16 existing
protected fingerprints and HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a
are preserved. Do not copy the mounted older-test audit edits over that dirty
checkout or commit/reset its independent history. Dirty entries 293 -> 295.
No OGL/Release/save/editor/private-input changes; Release stays frozen.

Native Graphify update refuses unsafe shrink 39,782 -> 18,000 and retains
19,398 nodes from 2,972 existing excluded files. Preserve the protective,
version and devcontainer warnings; no force/purge/install. After the consumer
commit, require fresh hook-log growth/UTC, a fresh Rebuilt record and zero
actual Graphify/Python workers before close-out.

Single Codex writer, zero Claude calls: discriminating compiler output and
independent references settle this step locally. No bridge/account changes.

## Next Work

Continue this same full func_1503CF20. The frame and early S6 lifetime are
recovered, but original private slots are not: request output +0x74 versus
retail +0x6C, main address +0x50 versus +0x58, word-index +0x54 versus +0x5C,
half-index +0x44 versus +0x4C and boundary +0x64 versus +0x68.
Recover the original initial count's unmasked halfword-store operand,
masked branch value and branch-delay index initialization; then reconcile
event initialization order and the original direct request-error return.
Preserve all public alias/fault/helper gates while resolving the remaining
98 words. Requalify complete body, owner/padders/connected chain and audit the
whole ELF after each installed improvement. Do not mask broad layout/control
differences with guards or switch to an easier neighbor. The wider Game
matching goal remains active.
