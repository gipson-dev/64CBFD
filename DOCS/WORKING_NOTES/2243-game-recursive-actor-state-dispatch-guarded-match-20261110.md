# Recursive actor-state dispatcher guarded match

Date: 2026-11-10. `func_1506045C` replaces its zero-return placeholder with
the complete **199-word / 796-byte** recursive dispatcher. The original
**0x50 frame**, saved-register lifetimes, argument homes and instruction
schedule are recovered. One checked branch-operand normalization uses a
register proven to hold the identical overlay byte. No insertion, omission,
frame change or compiler-profile change.

Fresh production recount: **4,312 / 5,513 (78.22%)** total; Game **3,639 /
4,840 (75.19%)**; Init **492/492**; Debugger **181/181**. Zero address drift,
**1,201** different. **99 more** accepted matches reach 4,411/5,513 and the
active 80% goal. Conversion rows and converted-function/byte totals stay fixed.

Baseline consumer `3a62da482a818972d34c3232392e43810ad9e36e`; baseline tools
`9be9fe159e437fe7866fa475a5005d3b46eacb0c`, from
[Note 2242](2242-game-actor-audio-handle-and-init-api-guarded-match-20261110.md).
The eight qualification files are banked first in tools commit
`b3eeee9fab7b7ce5621d4c20dbe69f244340e1bc`. Local commits only.

## Source, types and state behavior

Owner `conker/src/game_83300.c`; original assembly retained in
`asm/nonmatchings/game_83300/func_1506045C.s`. Retail span: VA
**0x1506045C..0x15060778**, ROM **0x8D90C..0x8DC28**. The old linked symbol
was a 12-byte placeholder. Its obsolete local declaration is replaced with:

```c
void func_1506045C(struct127 *actor, u32 buttons, u32 flags,
                  f32 height, s32 secondary);
```

The first original caller supplies the controller halfword in A1, a global
flag word in A2, and actor+0x28 float bits in A3. Other call sites also use
MFC1 to forward that float through A3. `height` is the local label for this
forwarded payload; its wider gameplay meaning remains unconfirmed. The
routine performs no float arithmetic or conversion on it.

Return early only when `D_800C35EA == 1`. For a primary dispatch, reduce the
state+0x72 unsigned-halfword timer using the signed global delta, or clear
it and set the expiry flag. The compound subtraction explicitly casts the
delta to u32, preserving SUBU/SH wrapping without signed C overflow, including
INT_MIN. Select state+0x75 with bit 0x80 removed; use the unmasked fallback
byte at 0x7C when that selection is zero.

Modes 0x29/0x2E, the overlay byte and controller bit 0x20 gate the command
query. Its positive result selects 0x1A. Reload actor+0x31C after the helper;
overlay commands 0x1A/0x2A take priority. Actor bytes 0x13C/0x137 suppress
primary selection or set the secondary force flag. A nonzero one-based slot
ID reads the original stride-0x32C category table: 12 selects 8, 35/138 select
27, 40 selects zero and the default selects 14. State+0x17 overrides with 60.

When a primary command differs from a nonzero overlay, save state+0x75 as a
word, temporarily install the overlay, and execute the real recursive call
with secondary=1. Restore the byte through the actor's **reloaded** state
pointer and reload it again before clearing the overlay. A helper can change
that pointer. Actor stun then clears both button/flag words. The nine-argument
dispatcher receives command, stun, expiry and force; the final five-argument
helper receives its result when state+0x7B or flag 0x4000 requests it.

## Recovering the natural frame and final word

The first full candidate already had 199 words/frame 0x50, with 26 differences.
Making the saved byte a word initially grew the frame to 0x58. Removing the
unnecessary named overlay local restores the natural frame while retaining
live state accesses. Declare scalar locals in the recovered order:
`stunned`, `command`, `expired`, `force`, `result`, `saved`. This recovers the
word snapshot at SP+0x38 and all original flag/result homes. The expiry
assignment precedes the timer clear; switch case order restores the original
block layout. No dummy padding or volatile fitting local is introduced.

Raw target SHA256:
`592dd571ec252c522e1130a205e53701fde3d9432a7b9cd22bdf9f82b94608c3`.
All fourteen relocation sites already agree. Only word **131**, offset
**0x20C**, differs: raw **0x10A0001B** tests A1; retail **0x1100001B** tests T0.
Word 76 copies T0 to A1. The CFG proof establishes that copy dominates the
branch and that neither register is written between them, with no intervening
call. Normalizing that one operand therefore preserves the predicate for all
paths that reach it. Full source-word/binding fingerprints reject stale input.

## Typed unfinished callees are included in the audit

`conker/src/game/generated_90840.c` keeps two unrecovered zero-return bodies,
with consistent typed parameter lists for `func_150642AC` and `func_15065A5C`.
The target's declarations agree with both definitions. Their existing s32
return types are retained; the former's result is ignored. This avoids
incompatible caller-only types or default float-to-double argument promotion.
These signature repairs do **not** recover either helper's algorithm.

The changes are visible in production: each placeholder grows **12 -> 28
bytes**, adding four stores of A0-A3 to its legal incoming argument homes.
Both changes are predicted explicitly. They receive no matching credit and
are not excluded or hidden by padding. All **17 other helper-owner functions**,
their pools and register information stay fixed. The helper owner remains
warning-free. All **88 non-target Game-owner functions**, pools and register
information also remain equal; its eight inherited diagnostics stay fixed.
No shared header changes, and no other C caller of either helper is present.

## Functional qualification and limits

- **3,384 guest cases per body / 6,768 executions** cover every one of the
  199 instructions. Real guest code executes recursion. All 3,384 pairs agree
  on complete memory, GPR/FPU state, calls and instruction memory-access
  traces. Sweep command, fallback, overlay, slot and category bytes; cover
  mode/controller gates, full-word inputs, timer edges/wrap, helper clobbers,
  state-pointer changes, live restoration and late stun changes.
- **2,926 native SDK32 cases at O0/O2/O3**, UBSan enabled, execute actual C
  recursion: **8,778 runs** and **6,505,350 exact call/public-output bytes per
  profile**. `-fno-strict-aliasing` explicitly supports the existing byte and
  halfword state views; these runs do not establish a strict-aliasing build.
  The 458 guest-only cases for slot IDs 27..255 use mapped extension fixtures;
  native qualification stays within the real 26-slot table domain.
- **17 effective compiled semantic controls** each finish normally and
  produce an observable disagreement; zero execution errors are counted as
  witnesses. Controls include stale query/recursive state pointers, timer
  edges, fallback masking, category mapping, recursive mode, stun clearing
  and final-result forwarding.
- Both independent padders emit the complete retail target. All **213**
  raw-word/binding corruptions and both stale-guard attempts are rejected.
  **60 executions across four independent symbol sets** bind raw, normalized
  and original programs at low halves 0, 0x7FFC, 0x8000 and 0xFFFC.
- **297 exact guest instruction-access cut pairs** preserve complete prefix
  state, including recursive stack activity. These are guest instruction-fault
  checks, not portable C fault-semantics or hardware acceptance claims.

An initial category sweep used slot ID zero and never entered the category
lookup. The coverage gap exposed four missing words, 121..124. Set category
cases to slot ID one and rerun: final coverage is **199/199**, superseding
the initial 195-word receipt.

## Original caller connections

The aligned ROM census finds three external JAL sites and the internal
recursive JAL at VA 0x150606A8. Three exact caller windows are connected to
the complete target body, with **200 cases per window**, **1,200 executions**
and **600 complete state/access-trace pairs**:

| Original parent | Window | Covered words |
| --- | --- | ---: |
| `func_1504CB98` | 0x1504EF68..0x1504EF88 | 8 |
| `func_1505F298` | 0x1505F6F4..0x1505F708 | 5 |
| `func_1505F298` | 0x1505FEA8..0x1505FECC | 9 |

All 22 window words execute, including real delay slots, controller/global
loads, MFC1 float transfer and outgoing fifth arguments. Inputs outside those
windows are explicitly staged caller state. The complete 4,500/1,137-word
parent algorithms remain unqualified. The first site immediately overwrites
V0; other parent paths can retain incidental V0. Raw/retail guest equality
preserves those bits without inventing a semantic C return value.

## Actual Make and complete image accounting

Freeze **2,193 input fingerprints**, retaining exact mutable baseline files.
Ten actual owner Make commands, plus independent before/proposed owner
compiles, reproduce both raw and padded outputs under their unchanged O2/g3
profiles. Private cleanup is omitted only to retain compact audit artifacts.
Production forcibly rebuilds the two affected owners, then links, emits the
binary, regenerates progress and performs the actual-ELF recount. Every
other fingerprinted input remains fixed.

The complete ELF differs at exactly **688 bytes**: the recovered target and
its **12 -> 796** symbol size, the two typed placeholders and their
**12 -> 28** sizes, and one closed two-record/string permutation:
`.L15037210_game_data` / `D_8009D660`. Reconstruct those records and contiguous
strings from baseline, preserving every named definition except the three
declared size changes. Require the complete expected byte sequence. No
section, range, metadata table or changed dependent object is excluded.
Eight structural image corruptions are independently rejected.

All **6,050 function addresses** stay fixed; only the three declared canonical
bodies change. All **189,088 protected bytes / 720 data owners** remain exact,
SHA256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The conversion CSV and every prior guard byte are preserved; append one row.
Production completes in **67.00 seconds**. Existing duplicate
`generated_12D630` recipe warnings and the expected full-ROM checksum exit 2
remain; the owner, strict image, binary and recount gates pass.

| Artifact | SHA256 |
| --- | --- |
| Production ELF | `7c6334220f41fc0cfacb82d92d2c3d22884401dfaccbd95b7d8fde9d68ca43d5` |
| Built binary | `7ca92f8e2c4cf97362c04bab08f5aec1a007649430661b3072bccb9f3796bd93` |
| Padded target owner | `8d03cd8be8ed5393b3b26d6f6b0d0d2c5690f28495eae0c0561c5a960340e65d` |
| Padded helper owner | `32d66fda1c2e87f6bdec742eea86dfa181fe6241011868d242f6933fceb571c1` |
| Guard manifest | `8d37e5d6a36e45fb20dceb5982c01f960ab1a6e71409ed501d009e45f45ec45e` |

## Tool copies, graph and continuation

All **eight preinstall checks pass freshly per tools environment**: mounted
65.47 s, sibling 74.63 s. After adoption, **two fresh installed checks per
environment** requalify actual Make/full image and complete guest behavior:
mounted 50.56 s, sibling 41.71 s. The remaining **six** checks are explicit
preinstall reuses with every tool/dependency fingerprint revalidated. Fresh
shared smoke checks pass; three unchanged pure-helper regression receipts
per environment are reused separately.

The sibling uses a private overlay for the eight new files, with explicit
read-only mounted fallbacks for missing `diagnostic_rows`, `bound_blob` and
`function_payload`. Consumer Make uses the mounted CLI; independent in-process
padder checks use sibling helpers. Its **2,434** pre-existing dirty paths
remain intact. Codex is the only writer; **zero Claude calls** are used for
this target. No host-port source, saves or frozen Release artifact is touched.

The scoped code graph contains **59,664 nodes / 113,063 links**, versus
59,662/113,064. All **59,662 old nodes remain**; definitions outside changed
paths stay equal apart from community metadata. Verify positions for 71
target-owner and six helper-owner C definitions, retaining all 18/13 assembly
pragmas. The eight new tools still have zero indexed nodes under current
submodule filters. Historical excluded nodes remain retained. This is a
scoped refresh with a recorded coverage gap, not full-corpus extraction.
Private post-commit receipts audit documentation heading relocation as well.

Reproduce in the prepared consumer root under WSL PSBBN:

```sh
python3 -m unittest tools.tests.test_game_actor_state_dispatch_1506045c_match -v
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

The suite needs exact retained pre-adoption mutable inputs under
`conker/build/game-actor-state-dispatch-1506045C-match/frozen/`. No retail ROM
or ELF binary is committed; a clean clone without those inputs is not claimed
to reproduce this workspace's image. Helpers remain typed opaque providers;
their actual algorithms and audio/gameplay behavior are unqualified. NaN/Inf
payload forwarding is covered without claiming arithmetic/FCSR behavior.

Next: investigate the remaining **86-word** `func_1505A250` in the same owner.
Its five-argument float/output-pointer declaration already exists, while its
24-byte empty placeholder remains unmatched. Recover the paired float
approach/clamp behavior and audit its original caller and output aliases.
No candidate or matching credit is assigned to that next target yet.
