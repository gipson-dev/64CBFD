# Additional-Source Coverage Refresh And Preset Handoff

Date: 2026-10-15. Predecessor consumer b848d58a, tools 94c4245, both active
trees clean. The user expands the objective: check the whole additional source
for usable commented-out functions and related material, then continue Game
matching. The previous turn is verified progress, not a blocked/no-progress
turn. Preserve the full objective rather than substituting a smaller queue.

## Steps

1. [x] Preserve all original archive inputs and current production state.
2. [x] Revisit the earlier whole-source/commented audits; identify their exact coverage and unresolved gates.
3. [x] Extend the fresh census to game headers, assembly support and conditional definitions, not just linked C.
4. [x] Verify historical source, generated/isolated inputs and successful objects before reusing compile receipts.
5. [x] Rescreen every retained successful whole-file, isolated, interface-retry and commented-profile object against the current ELF and original retail bytes.
6. [x] Refresh the diagnostic linked-C comparison without treating that diagnostic ELF as a normal/runnable build.
7. [x] Deduplicate already-recovered functions, profile variants and overlapping obstruction queues; retain failures instead of rejecting entire source owners.
8. [x] Resume Game matching with the full packed-coordinate preset body and complete caller/factory ABI, in isolated build output only.
9. [x] Verify candidate packet semantics and fail-closed installation gates; keep the real word mismatch explicit.
10. [ ] Finish func_1516E778's compiler allocation/schedule, owner/private/fault/rebase qualification and exact linked-image audit before installation.
11. [ ] Repair the remaining commented/individual declaration-expression failures and real binding/translation cases; the wider Game goal remains open.

## Complete Coverage

Archive: `Another Source/CBFD-Recompiled/conker`, read-only. Verify all **801
original recorded files** before and after the complete audit. Walk the actual
game `src` and `include` directories as well, rejecting an unrecorded source
input rather than silently excluding it. Examine **650 game source/support
inputs: 558 C, 91 headers and one assembly macro include**. The other 151
recorded files are compiler/build/configuration/script/documentation support,
not implicitly retail Game functions. The archive's three host compiler C
files are not N64 function-import candidates.

All 558 archive C files and all 91 headers still equal the prepared historical
compiler-input copy. The prior snapshot's documented assembly macro-support
generation is not an original C/header change. Do not modify either archive
or its headers to make a draft compile.

Fresh lexical census: **4,131 C definitions**, 155 trivial bodies and eight
unanchored definitions. Trivial is discovery metadata, not proof of a false
stub. Header/support scans find **zero additional active or commented function
bodies**. The real line/block-comment lexer finds **353 complete commented
records / 341 names in 95 C files**. Of these records, **213 already have
exact active C** and **140 still need qualification**. These record counts
are not a sum of unique functions or newly usable matches.

Two definitions are conditional under literal `#if 0`:

- `func_100052A0`, archive `src/init_50A0.c:49`, already has exact active C.
- `n_alSynAddSeqPlayer`, archive `src/libultra/audio/n_synaddplayer.c:55`,
  remains unanchored. It is not renamed to n_alSynAddPlayer or assigned a
  guessed address. Its extra sequence-player state is not the active helper.

## Current Word Screens

Validate **1,717 historical successful objects** and their actual source,
expanded/isolated input and object fingerprints. Historical receipts also
contain 640 error records across owners/routines/retries/profiles; that is
not 640 distinct functions. Reuse those completed compiles explicitly, then
perform fresh relocation-aware word screens. No new compiler run is implied
by an unchanged successful historical object.

| Corpus | Objects | Already Exact Active C | Word-Different | Binding/Translation Rows | Unanchored | New Raw Candidates |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Whole-file | 233 | 607 | 858 | 23 | 16 | 0 |
| Isolated failed owners | 719 | 329 | 378 | 12 | 0 | 0 |
| Used-interface retries | 325 | 147 | 176 | 2 | 0 | 0 |
| Commented, five profiles | 440 | 35 | 400 | 5 | 0 | 0 |

Rows are function/profile results, not distinct function totals; whole-file
objects can contain many functions. All five remaining commented binding
rows refer to **func_100038E0 / D_BC000C02**. The other previously reported
commented binding families have since been recovered. Across all four
corpora, deduplicate to **38 binding/translation functions**. M2C_ERROR and
M2C_MEMCPY_ALIGNED are unresolved translation placeholders, not addresses to
invent; local .rodata, nanf and named-data cases require real provenance too.

The fresh linked diagnostic comparison finds all **1,478 executable C
candidate rows** exact but **zero additional applicable raw donors**. The
snapshot remains a diagnostic, non-normally-linked, non-runnable ELF. It is
not a replacement ROM or PC-port input. This census excludes D_ labels and
NON_MATCHING bookkeeping: current executable C is **3,427 exact / 5,361**.
That is a differently scoped audit, not a regression from the main matcher.

## Durable Review Queue

[ADDITIONAL_SOURCE_REVIEW_QUEUE.csv](../ADDITIONAL_SOURCE_REVIEW_QUEUE.csv)
records **173 distinct obstruction-review entries**, original source paths/
lines, origin, section, current language and unresolved symbols:
Paths are relative to the archive's `conker/` subproject, not the consumer.

- **57** still-open commented compile-failure functions, after removing exact recoveries.
- **70** still-open individual-body compile-failure functions from the latest used-interface retry.
- **38** deduplicated binding/translation functions.
- **8** unanchored lexical definitions.

Compute set unions before reporting counts; the present exported groups are
disjoint. Keep raw historical counts 59 and 99 separate from the filtered
57 and 70. These 173 entries are **not the entire unmatched Game population**:
compilable word-different routines remain in the ordinary matching backlog.
No failed/commented/unbound body is credited as completed or automatically
adopted. The new reusable coverage tool regenerates the complete machine
inventory and screens in ignored build output.

## Game Matching Resumed

Continue at **func_1516E778**, VA 0x1516E778 / ROM 0x19BC28, retail 85 words,
frame 0xD0, owner generated_19A8B0. The original caller prefix at 0x15027038
in asm/50D80.s passes packed coordinates, a full value word, a signed script
byte, an unsigned flag byte and a stack argument. Inspect the complete retail
wrapper and all 49 outgoing factory arguments, not only the archive header.

The archive body and straightforward corrected C both emit **84 words / 79
real differences**. The compiler folds the low-coordinate read to LH. An
explicit unsigned left shift followed by signed right shift restores the
retail **85-word length**, but still differs in **46 words**. Fourteen bounded
coordinate/local/formal variants do not produce a direct match. Keep the
public address-based name; no source/profile/guard/padder change is installed.

The best complete semantic candidate:

- Sign-extends both packed 16-bit coordinates.
- Preserves arg1 and arg4 as complete outgoing words.
- Passes only the low bytes of arg2 and arg3.
- Supplies every one of the factory's 49 preset arguments.

Compare **1,560 guest packet cases** at both stack phases under three provider
clobber modes, selected candidate and original retail code. The actual 49-word
packets and restored SP agree. Native32 checks all **14 candidate shapes at
O2**, the selected shape at O0, **65,536 cases per shape/profile**, and two
effective wrong-word/wrong-coordinate controls. These are packet diagnostics,
not private stack/fault/owner or hardware/gameplay acceptance.

The first native capture fixture used word-sized coordinate formals and
incorrectly rejected the no-explicit-first-cast shape. Correct the capture's
first two parameters to the actual signed-halfword contract. The original
unsigned-cast negative then becomes equivalent under that contract; replace
it with the wrong coordinate half. All controls must remain effective. No
production source or acceptance threshold is weakened to pass the fixture.

`--qualify` rejects length, word or warning mismatches. Raw 85/46 agreement
must not be reported as byte-exact, and no guard is manufactured to hide it.
The incoming ABI, field values and packet are evidence; compiler-role fitting
and complete installation gates remain next. Keep func_1516D738's inherited
stack-word C deferral and the whole additional-source/Game objective open.

## Verification And Banking

All **46 discovery/screen/preset checks pass in 10.018 seconds**, including
source/capture/object corruption controls and a fail-closed mismatch gate.
Shared project tool checks and native Windows syntax for all four new files
pass. The older standalone tools mirror retains independent ddbdd16 HEAD and
all **643 initial dirty fingerprints**; copy only four absent owned paths,
giving 647. All nine ROM-free checks and four-file syntax pass there. Do not
commit/reset the older mirror or copy history into it.

Bank tools **8ec9137** before consumer documentation/queue/pin changes. The
N64 owner, all guards and all **49 current audit input fingerprints** remain
fixed. No production function is converted or claimed matched this turn.
Normal ELF/progress build is up to date; existing duplicate generated_12D630
recipe warnings remain. Fresh official matcher: **Game 2,894/4,828 (59.94%)**,
**total 3,567/5,501 (64.84%)**, different 1,934, zero address drift. Root README
is unchanged because neither aggregate nor conversion counts changed.

Ignored audit receipts: `conker/build/additional-source-coverage-20261015/`;
matching receipts: `conker/build/game-packed-coordinate-preset/`. Re-run the
coverage tool with `python3 -m tools.experiments.alternative_source_coverage_refresh`
from the prepared consumer root; successful old objects are revalidated and
re-linked, not falsely called fresh compiles. The preset tool's `--screen`
retains all 14 recipes; normal output explicitly reports non-installability.

No push, host source/build/launch, real save/configuration change, frozen
Release operation or Claude invocation. This is a completed refreshed audit
and concrete matching progress, not completion of the full persistent goal.

The full Graphify update refuses 19,347 nodes against 41,126 existing nodes,
retaining 19,398 nodes from 2,972 excluded-but-present files. Preserve that
fail-closed result and await the incremental commit worker; do not force a
smaller graph. Normal preset-tool output confirms installable=false.
