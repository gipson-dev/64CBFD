# Current Decomp Status

Last verified: 2026-10-04

This page is the short, current handoff for `64CBFD`. Historical experiments
remain in [WORKING_NOTES.md](WORKING_NOTES.md); detailed session handoffs live
under [WORKING_NOTES/](WORKING_NOTES/).

## Repository state

- Branch: `master`
- The restoration baseline is banked in coherent commits beginning after
  `2ed3523` (`tool updates`): generated-slice assembly support, restored guest
  routines, OGL reference tooling, RGBA5551 tooling, and documentation.
- Before checkpointing, `git status --short` reported 123 changed tracked paths
  and 37 untracked paths. The empty personal `DOCS/user notes.md` remains
  preserved locally and excluded through `.git/info/exclude`.
- The broad assembly restoration in the current tree is buildable, but it
  reduced the number of functions represented in C. It improves original-code
  coverage and port support; it is not C-decomp completion.

## Measured progress

Init explicit-first-refill lookup fitting: [Note 873](WORKING_NOTES/873-init-explicit-first-refill-lookup-fitting-20261004.md)
adds opt-in `--lookup-first-refill` (requires shared lookup). Packed O2/O1
core save sixteen bytes; linked O2 is 4,688 / 704 excess. No shape grows
linked text or stack; all six observed descents match static bounds. Final
guest run: 33 passes / one corpus skip in 241.971s, plus sixteen supporting
passes. Omitted-option O2/O1 text matches qualified baseline exactly.
Notes 871/872 qualify that baseline, not this changed option; changed corpus
and fitting/ownership/hardware remain open. Production/defaults/README unchanged.

Init current allocation-table CU1-set corpus: [Note 872](WORKING_NOTES/872-init-allocation-table-full-masked-cu1-set-corpus-20261004.md)
passes all 507 fresh packed-remaining O2/g3 paired pages with masked CU1 set
(status 0x2400FF00), 804.532 seconds, no skips. Together with Note 871 this
qualifies 1,014 paired pages across both masked modes on unchanged current
source. Text 4,704 / 720 excess; observed descent 3,240 matches bound,
minimum SP 0x80031D68 / known-neighbor margin 88. Fifteen supporting gates
pass. Current full corpus gates checked off; fitting/ownership/hardware/
complete-reservation and resume gates remain. Production/defaults/README unchanged.

Init current allocation-table full corpus: [Note 871](WORKING_NOTES/871-init-allocation-table-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 freshly compiled packed-remaining O2/g3 paired retail pages
with exception-masked CU1 clear (status 0x0400FF00), 798.099 seconds, no skips.
Linked text 4,704 / 720 excess; observed descent 3,240 equals bound, minimum
SP 0x80031D68 / known-neighbor margin 88. Fifteen helper/selection tests pass.
This qualifies the current toggle/parent-cursor/allocation-table combination,
not merely the earlier source. Its CU1-set follow-up now passes in Note 872;
fitting/ownership/hardware gates remain open. Production/defaults/README totals unchanged.

Init stride-only replication trials: [Note 870](WORKING_NOTES/870-init-rejected-stride-only-replication-capture-20261003.md)
rejects standalone stride capture with indexed for or gated do/while fills.
Both add eight bytes to builder frames and core call bounds; neither improves
text across profiles. Source restored exactly. Fresh retained-config guest
suite passes 32 tests / one intentional corpus skip in 260.739 seconds;
all six observed descents match bounds, packed O2 linked text stays 4,704.
Production/defaults/README unchanged; full changed corpus remains open.

Init remaining helper subsets: [Note 869](WORKING_NOTES/869-init-rejected-take-bits-mask-and-drop-inlining-20261003.md)
rejects mask-only and mask-plus-drop inlining inside take_bits. Mask-only
holds O2 but grows O1 16 bytes; combined grows both 32 bytes, with no core
call-bound benefit. All three mask/drop subsets now have current-base
receipts. Source restored exactly, fourteen focused gates pass; no retained
option, production conversion or README count change. Continue structural
dataflow/caller fitting rather than repeating these subsets.

Init shared-helper fitting: [Note 868](WORKING_NOTES/868-init-rejected-take-bits-drop-inlining-20261003.md)
rejects drop-only inlining inside take_bits: packed O2 grows 16 core bytes,
O1 grows 32, with no core call-bound improvement. Source is restored exactly
to HEAD and fourteen focused gates pass. Fresh inventory remains 492 C /
47 assembly rows, with 12,252 assembly bytes. No production conversion;
the two small candidates still lack full-slot matching C, and the retained
decompressor experiment remains 720 linked bytes over budget. README unchanged.

Init table-derived allocation fitting: [Note 867](WORKING_NOTES/867-init-builder-table-derived-allocation-fitting-20261003.md)
adds opt-in direct table/header/commit dataflow. Packed O2 falls to 4,704
linked bytes / 720 excess, public builder 333 words; packed O1 text holds.
All six stack bounds hold. The new observer is corrected to retail's s3
counter at 0x10006C38, not its once-at-return FPR19 write, and ordered
allocation values pass across six builds. Fresh corrected guest run has
32 passes / one corpus skip, plus fourteen helper passes; all observed
descents match bounds. Omitted-option text matches baseline. Defaults/production/
README totals unchanged; changed corpus and fitting/ownership/hardware remain open.

Init parent-ascent cursor fitting: [Note 866](WORKING_NOTES/866-init-parent-ascent-offset-cursor-fitting-20261003.md)
adds opt-in descending parent-offset traversal. Packed O2 falls to 4,720
linked bytes / 736 excess with unchanged 392-byte core bound and 200-byte
builder frame. Packed O1 text/bound hold. Other profiles are mixed: frame
O2 saves 32 bytes; frame/aligned O1 grow 16, and aligned bounds grow eight.
Active root-descent and short-tree guard checks pass; 31 guest tests pass,
one corpus skip, plus fifteen focused passes. All observed descents match
static bounds. Rejected mask-reuse forms are removed, omitted-option text
matches baseline. Defaults/production/README totals unchanged; corpus and
fitting/ownership/hardware remain open. Unrelated Game work preserved.

Init current cache/sort fitting: [Note 865](WORKING_NOTES/865-init-toggle-cache-interactions-and-rejected-sort-cursors-20261003.md)
re-measures cache and parent/sorted-array interactions on the changed Note
864 base. All 44 fresh object receipts are no better than the base on
O2/O1 text and stack bound. Both new sorted-length cursor loops are worse
and removed; experiment source is restored exactly. Sixteen focused gates
pass, no skips. Packed O2 stays 4,736 / 752 excess; next structural targets
are allocation/parent ascent and shared-call overhead. Defaults/production/
README totals unchanged; unrelated Game work preserved.

Init reversed-code increment fitting: [Note 864](WORKING_NOTES/864-init-builder-reversed-code-toggle-first-loop-20261003.md)
adds opt-in toggle-first increment. Packed O2 public builder falls 341 to
338 words, with padding holding linked text at 4,736 / 752 excess. Packed
O1 saves 16 linked bytes, frame O1 32, aligned O2/O1 16; all stack bounds
hold. Exhaustive 131,070 host code/mask pairs pass; final checks are 44
pass / one corpus skip, with all observed descents matching static bounds.
Both omitted-option text sections
match the banked baseline. Notes 862/863 remain qualification for that
baseline, not this changed option. Defaults/production/README totals unchanged.

Init revised offset-sum CU1-set corpus: [Note 863](WORKING_NOTES/863-init-offset-sum-full-masked-cu1-set-corpus-20261003.md)
passes all 507 fresh packed/remaining O2/g3 retail pages with masked CU1 set
in 814.477 seconds. With Note 862, both masked modes now bank 1,014 paired
page executions for the unchanged Note 861 source. Terminal text/descent/
known-neighbor clearance match at 4,736/3,240/88. Sixteen corpus/helper
checks pass, no skips. Return to builder/shared-helper fitting: 752 linked
bytes remain over retail. Other profiles and ownership/hardware remain open;
production/defaults/README totals unchanged, unrelated Game work preserved.

Init revised offset-sum CU1-clear corpus: [Note 862](WORKING_NOTES/862-init-offset-sum-full-masked-cu1-clear-corpus-20261003.md)
passes all 507 fresh packed/remaining O2/g3 paired retail pages with
exception-masked CU1 clear in 790.137 seconds. This covers the Note 861
repeat-value/offset-sum/reused-accumulator combination, not the older build.
Terminal text/descent/known-neighbor clearance are 4,736/3,240/88; sixteen
corpus/helper checks pass with no skips. Matching CU1-set corpus is now
banked in Note 863 above.
Further fitting (752 bytes), other profiles and ownership/hardware remain
open. Production/defaults/README totals unchanged; unrelated Game work preserved.

Init offset accumulator stack recovery: [Note 861](WORKING_NOTES/861-init-builder-offset-accumulator-lifetime-stack-recovery-20261003.md)
reuses the dead availability variable in the opt-in prefix loop. All text
sizes hold; aligned O2/O1 and packed O2 call bounds fall eight bytes.
Packed O2 retains 4,736 linked bytes / 752 excess with restored 392-byte
core bound, 200-byte builder frame and 88-byte known-neighbor clearance.
Fresh checks pass: 43 tests, one corpus skip; all observed descents match
static bounds and both omitted-option text sections match the banked baseline.
This supersedes Note 860's stack penalty, not its historical evidence.
Notes 862/863 now qualify both masked corpus modes for this packed profile.
Defaults/production/README totals remain unchanged; further fitting and
other-profile/ownership/hardware gates stay open.

Init builder offset-sum fitting: [Note 860](WORKING_NOTES/860-init-builder-running-offset-sum-text-stack-tradeoff-20261003.md)
adds an opt-in unsigned prefix sum. Packed O2 linked text falls to 4,736,
752 over retail, but its call bound grows from 392 to 400 and known-neighbor
clearance falls from 88 to 80 bytes. The unchanged 4,752-byte baseline stays
available; this is a text/stack tradeoff, not a dominating or production
replacement. Ordered prefix stores pass all six shapes at depth boundaries.
Fresh checks pass: 43 tests, one intentional corpus skip; observed packed
descent matches its 3,248-byte bound. Changed full corpus,
further fitting and ownership/hardware gates remain open. Defaults/totals unchanged.

Init rejected copy/refill fitting: [Note 859](WORKING_NOTES/859-init-rejected-match-copy-refill-trials-and-size-ledger-20261003.md)
measures four dataflow variants; none improves the selected packed profile.
All trial branches/selectors are removed and the committed Note 858 source
is restored exactly. Fresh baseline and fifteen focused checks pass. Ledger
separates 464 core-excess bytes plus 304 adapter bytes: best linked text stays
4,752, 768 over retail. Next fitting target is builder/shared-call overhead;
its 415-word region includes a 343-word public body and 72 helper words.
Fresh changed-fill corpus/ownership/hardware remain open; defaults/totals unchanged.

Init dynamic repeat fill fitting: [Note 858](WORKING_NOTES/858-init-dynamic-repeat-value-selection-and-cursor-end-fill-20261003.md)
retains opt-in once-selected repeat values and cursor-end fills after the
overflow gate. Frame O2 saves 32 linked bytes, aligned/packed O2 16, all
O1 32; stack costs stay unchanged. Best bounded-qualified O2 is 4,752,
768 over retail. The dynamic body fits its 257-word slot by size only.
All 504 contexts, 132 builders and ordered zero/nonzero staging writes pass:
43 tests pass, one corpus skip. Notes 856/857 remain full qualification for
the prior 4,768-byte no-new-option build, not this changed fill. Fitting and
fresh corpus/ownership/hardware gates remain open; production/defaults/totals unchanged.

Init current-combination CU1-set corpus: [Note 857](WORKING_NOTES/857-init-simple-seed-full-masked-cu1-set-corpus-20261003.md)
passes all 507 fresh packed/remaining O2/g3 retail-page comparisons with
exception-masked CU1 set in 784.455 seconds. Notes 856/857 bank both masked
modes for the current combination: 1,014 paired runs. Both receipts retain
text/descent/clearance 4,768/3,240/88; corpus/helper checks this turn total
fourteen pass, no skips. Return to structural fitting: 784 linked bytes
remain over retail. Other-profile/ownership/hardware/resume gates stay open;
production/defaults/README totals unchanged.

Init current-combination CU1-clear corpus: [Note 856](WORKING_NOTES/856-init-simple-seed-full-masked-cu1-clear-corpus-20261003.md)
passes all 507 retail pages on freshly compiled packed/remaining O2/g3
with exception-masked CU1 clear in 800.807 seconds. Linked text/descent/
clearance remain 4,768/3,240/88. Full context, memory and poisoned-state
checks pass; corpus/helper checks total fourteen pass, no skips. This is
new evidence for Note 855, not reassigned histogram-only receipts. Changed
CU1-set corpus and 784-byte fitting gap remain open, along with other-profile/
ownership/hardware gates. Production/defaults/README totals unchanged.

Init option interaction fitting: [Note 855](WORKING_NOTES/855-init-cache-interaction-matrix-and-simple-seed-combination-20261003.md)
measures all 32 cache/builder combinations on both packed profiles. Adding
only existing arithmetic simple-operation selection wins all size/bound
metrics. All O2 links save 16; O1 saves 32/32/16, with unchanged stack costs.
Best packed O2 is 4,768, 784 over retail; descent/clearance remain 3,240/88.
All 492 bounded contexts and 132 builders pass, including literal/EOB and
signed stale-word cells. Final module/helper/default checks: 42 pass, one
corpus skip. Fitting and changed corpus/ownership/hardware remain open;
production/source bodies/adapter/defaults/README totals unchanged.

Init ABI seed fitting: [Note 854](WORKING_NOTES/854-init-abi-seed-pointer-cursor-and-ordered-register-copy-20261003.md)
retains an opt-in six-word seed pointer cursor with ordered read/write gates.
Frame O2 saves 64 linked bytes; aligned/packed O2 save eight stack bytes.
O1 grows 32/32/16 linked bytes with unchanged bounds. Best packed O2 remains
4,784, 800 over retail; observed descent improves to 3,240, clearance 88.
All bounded gates pass: final module/helper/default checks total 41 pass,
one corpus skip. Structural fitting and changed corpus/ownership/hardware
remain open; production, adapter, defaults and README totals unchanged.

Init adapter state fitting: [Note 853](WORKING_NOTES/853-init-core-owned-state-initialization-and-adapter-fitting-20261003.md)
omits six redundant adapter stores behind an opt-in assembler symbol.
Poisoned fields and read-before-write checks pass all 492 bounded contexts;
default adapter object stays byte-identical. All six linked images save 16:
best packed O2 is 4,784, 800 over retail, with unchanged stack depth.
Final bounded/helper/default checks: 39 pass, one corpus skip. Structural
fitting and changed corpus/ownership/hardware remain open; production,
defaults and README totals unchanged.

Init dynamic repeat fitting: [Note 852](WORKING_NOTES/852-init-dynamic-shared-repeat-extraction-and-stack-fitting-20261003.md)
retains opt-in shared repeat extraction. All O2 shapes save eight stack bytes;
all O1 shapes grow eight. Aligned O2 saves 16 linked bytes, while best packed
O2 remains 4,800, 816 over retail. All 492 bounded contexts, 114 builders,
six initializers and 48 direct header/alignment comparisons pass. Active
codes 16/17/18 and each overflow are verified; final module/helper checks:
36 pass, one corpus skip. Changed corpus and structural fitting remain open;
production, defaults and README totals unchanged.

Init stored length fitting: [Note 851](WORKING_NOTES/851-init-stored-shared-length-extraction-and-failure-bit-state-20261003.md)
retains opt-in shared 16-bit extraction with explicit failure-count restoration.
All O1 linked builds shrink 32, frame O2 16; best packed O2 stays 4,800,
816 over retail after padding. All 444 bounded contexts, 114 builders, six
initializers and 48 direct header/alignment comparisons pass. A delay-slot-aware
gate proves bad/valid restoration behavior; final module/helper checks total
35 pass, one corpus skip. Structural fitting and changed corpus/hardware/
ownership remain open; production, defaults and README totals unchanged.

Init packed header fitting: [Note 850](WORKING_NOTES/850-init-byte-packed-header-load-and-unaligned-core-qualification-20261003.md)
retains opt-in byte-packed guest header loads with enforced (4,1) layout and
actual LWL/LWR pairs. All six linked images shrink 32; best O2 is 4,800,
816 over retail, with unchanged stack bounds. All 432 bounded contexts,
114 builders, six exact initializers and 48 direct unaligned/header-format
comparisons pass. Negative layout and helper/ledger checks pass: 34 tests
pass, one corpus skip. Changed corpus and hardware/ownership remain open;
production, defaults and README totals unchanged.

Init stream fitting: [Note 849](WORKING_NOTES/849-init-stream-masked-dispatch-and-buffered-byte-rewind-fitting-20261003.md)
combines opt-in masked dispatch and buffered-byte rewind. Best linked O2 is
4,832, leaving 848 over retail; all six shapes shrink 16 with unchanged stack
bounds. All 432 bounded contexts, 114 builders and six exact initializers pass:
17 tests pass, one corpus skip. A zlib-valid constructed stream proves rewind
executes (11 bits, one byte, three remaining); sampled retail pages did not.
Continue fitting; changed corpus and ownership/hardware remain open.
Production, defaults and README totals unchanged.

Init fixed-length pointer fitting: [Note 848](WORKING_NOTES/848-init-fixed-length-pointer-ranges-and-complete-table-qualification-20261003.md)
retains an opt-in four-range pointer initializer. Best packed O2 linked text
falls to 4,848, leaving 864 over retail; O1 grows 48 bytes. All 420 bounded
contexts, 114 direct builders and six complete initializer comparisons pass:
16 tests pass, one corpus skip. Exact 318-store sequence, all 2,632 table
bytes and unchanged stack bounds are verified. Continue fitting; changed full
corpus and ownership/hardware remain open. Production/defaults/totals unchanged.

Init builder operation fitting: [Note 847](WORKING_NOTES/847-init-builder-operation-selection-fitting-and-rejected-dataflow-trials-20261003.md)
retains opt-in arithmetic operation selection. All 420 bounded contexts and
114 direct builder comparisons pass; 15 tests pass, full corpus skips.
Frame/aligned O2 shrink 32/16 bytes; all O1 shapes shrink 16. Packed O2 builder
saves two words but padding absorbs them: best linked text remains 4,864,
880 over retail. Prefix/countdown trials are removed. New-option full corpus,
fitting and ownership/hardware remain open; production/defaults/totals unchanged.

Init histogram CU1-clear corpus: [Note 846](WORKING_NOTES/846-init-histogram-cursor-full-masked-cu1-clear-corpus-20261003.md)
passes all 507 changed packed O2/g3 pages with masked CU1 clear in 768.820
seconds. Notes 845/846 now bank both masked CU1 modes: 1,014 paired runs.
Text/descent/clearance remain 4,864/3,256/72. Return to builder/shared-helper/
adapter fitting; 880 linked bytes remain. Other profiles, complete ownership
and hardware/resume remain open. Production and README totals unchanged.

Init histogram full corpus: [Note 845](WORKING_NOTES/845-init-histogram-cursor-full-masked-cu1-set-corpus-20261003.md)
passes all 507 retail pages on the changed packed/remaining O2/g3 source,
exception-masked entry with CU1 set. Terminal run: 744.102 seconds, linked
text 4,864, maximum descent 3,256, minimum SP 80031D58, neighbor clearance 72.
Next qualify CU1 clear, then continue fitting; 880 linked bytes remain over
retail capacity. Other profiles, complete reservations and hardware/resume
remain open. Production Init and README aggregates unchanged.

Init decoder histogram fitting: [Note 844](WORKING_NOTES/844-init-builder-histogram-cursor-fitting-and-bounded-qualification-20261003.md)
retains an opt-in histogram pointer loop, saving 16 packed core bytes in both
IDO profiles. Best linked text is 4,864, still 880 over retail capacity.
All 420 bounded stream/context and 114 direct builder comparisons pass;
15 tests pass, one intentional full-corpus skip. Packed O1 stack grows eight
bytes; O2 retains its 72-byte known-neighbor clearance. Changed full corpus,
fitting and complete ownership remain open. Inventory is still 492 C / 47
assembly rows; production and README totals unchanged.

Init debugger entry/footer: [Note 843](WORKING_NOTES/843-init-debugger-entry-frame-and-seeded-resume-footer-20261003.md)
executes retail early exits and explicitly seeded footer predicates. Frame is
`0x50` bytes with `0xFA8` image gap; completed paths restore saved registers/SP.
Conditional runnable, syscall-EPC advance and recognized-fatal outcomes pass.
All 62 focused tests pass. UI/TLB-generated premises, full hardware/resume and
reservations remain unproven. Next return to decoder fitting; production,
decoder/adapter and README totals unchanged.

Init diagnostic cleanup: [Note 842](WORKING_NOTES/842-init-post-diagnostic-page-state-cleanup-and-continuation-20261003.md)
executes real return-tail/table-clear/bitmap words under explicit external-call
stubs: unmap indices 2-31, 1,016 table zeros, correct bitmap masks and 513
inclusive cache operands. Zero/nonzero debugger result selects saved fault/
requeue continuation; static decoder bytes remain unchanged by CPU stores.
All 58 focused tests pass. Debugger entry, actual hardware/stubbed effects and
continuation execution remain open; production, fitting and totals unchanged.

Init diagnostic placement: [Note 841](WORKING_NOTES/841-init-diagnostic-overlay-placement-and-positive-pool-bounds-20261003.md)
executes retail overlay/SP/DMA/TLB argument arithmetic. Debugger reuses the
page pool at its next 64 KiB boundary, image 4960/SP 5958/mapping span 20000.
All 256 positive direct-count allocator cases back these extents; zero/tiny
pools do not inherit that bound. All 54 focused tests pass. Real DMA/TLB,
debugger/post-fault cleanup and complete ownership remain open; production,
fitting and README totals unchanged.

Init loaded table loop: [Note 840](WORKING_NOTES/840-init-retail-loaded-page-table-loop-write-footprint-20261003.md)
executes all 19 retail words over 508 offsets. Exactly 2,032 bytes are rewritten;
the 16-byte DMA tail and following input guard remain unchanged. Six relocated/
small-count cases and zero-count skip pass. All 41 focused tests pass. Actual
DMA/cache, other loaded writers, diagnostic storage and full reservation ownership
remain open; fitting, production and README totals unchanged.

Init block-local writer census: [Note 839](WORKING_NOTES/839-init-block-local-storage-writers-and-fr1-fixture-correction-20261003.md)
finds 55 Init/1 Debugger candidates, including 33 stores: startup pointer
publications, 35500 clear and wrapper saved context. Lexical tracking is not
all-path ownership proof. The callback fixture's old FPR-pair interpretation
is corrected to FR=1 and passes both IDO profiles. All 34 focused tests pass;
loaded-pointer/loop/diagnostic storage, complete ownership and fitting stay open.
Production and README totals unchanged.

Init static literal census: [Note 838](WORKING_NOTES/838-init-static-storage-literal-census-and-enclosing-bss-clear-20261003.md)
finds 9 Init and 1 Debugger adjacent literal pairs in the audited storage
interval; zero Game candidates is not absence proof. Startup clear-call
arguments cover enclosing BSS 8002D4B0..80043B40, not individual reservations.
All 17 focused tests pass. Scheduled-apart/computed/pointer/DMA writers and
complete capacities remain open; production, fitting and README totals unchanged.

Init syscall fault route: [Note 837](WORKING_NOTES/837-init-syscall-fault-dispatch-and-disabled-diagnostics-route-20261003.md)
executes ROM-pinned dispatch/fault/diagnostic-disabled slices. Syscall routes to
generic fault; state/flags become 1/2. With no event queue, control reaches the
scheduler boundary and seeded EPC remains at the syscall. Diagnostic bit 2000
instead enters the debugger body. All 32 focused tests pass. Full exception
entry, queued delivery, scheduling/resume, enabled diagnostics and reservations
remain unqualified; fitting and production/README totals unchanged.

Init real cleanup callback: [Note 836](WORKING_NOTES/836-init-retail-cleanup-callback-null-path-and-fatal-slot-20261003.md)
executes ROM-validated retail wrapper/renderer words with compiled Init sweep
C in both IDO profiles. Clearing the render-list global takes the null branch,
skips renderer frees and preserves sweep heap ownership in the fixture. The
fatal slot is pinned as syscall plus NOPs, not a returning C callback. All 28
focused tests pass. Async writes, syscall dispatch/resume, static reservations
and decoder fitting remain open; production and README aggregates unchanged.

Init guest tag lifetimes: [Note 835](WORKING_NOTES/835-init-guest-tag-sweep-and-retag-lifetime-contract-20261003.md)
qualifies both sweep bodies and the retag helper in fresh O2/g3 and O1 IDO
guest builds. Aging frees tag 2 and decrements 3/4; full sweep frees 1-4 while
preserving 5/FF. Pool/bitmap tag FF survives these sweeps. All 25 focused tests
pass. Real Game cleanup callback effects, fatal/reservation ownership and
fitting stay open; no production or README aggregate changes.

Init guest free/resize qualification: [Note 834](WORKING_NOTES/834-init-guest-free-reinsertion-and-resize-coalescing-20261003.md)
executes fresh, unguarded IDO C in both O2/g3 and O1 big-endian guest profiles.
All 512 private-heap resize cycles reclaim the heap; middle reinsertion,
two-sided coalescing and adjacent live payload/tag preservation also pass.
All 22 focused tests pass. Real fragmentation, tag-sweep/fatal lifetimes,
complete decoder ownership and fitting remain open. No production or README
aggregate changes; pending Game work is preserved.

Init page-pool retry contract: [Note 833](WORKING_NOTES/833-init-page-pool-retry-and-zero-count-fallback-contract-20261003.md)
pins the complete setup slot and executes success/retry/failure cases with
allocator stubs. Zero previous count can conditionally publish end=start-1;
native production-C tests show zero requests can allocate nonzero storage.
Positive requested counts therefore do not prove positive post-fallback count.
All 26 focused tests pass. No real failure reachability or complete ownership
claim; production, decoder/adapter, fitting and README aggregates unchanged.

Init storage boundaries: [Note 832](WORKING_NOTES/832-init-storage-boundaries-page-table-cache-and-output-pool-20261003.md)
executes pinned startup/table, cache-operand and output-pool arithmetic. The
2,048-byte table DMA ends at input start; max page DMA remains 3,072 with a
440-byte workspace gap. The inclusive cache sweep emits 257 operands and
crosses the workspace address range, so it is not input-capacity evidence.
Ten focused tests pass. Complete reservation/free-list/fallback/fault ownership
and fitting remain open; no production, decoder/adapter or README changes.

Init explicit CU1 corpus modes: [Note 831](WORKING_NOTES/831-init-explicit-corpus-cu1-modes-and-clear-full-pass-20261003.md)
adds set/clear/both selection with unchanged defaults and mode-local receipts.
All 507 masked CU1-clear pages pass loop-lookup packed O2 in 741.930 seconds;
text/descent/margin remains 4,880/3,256/72. That profile now has separate full
passes for both entry modes. Nine focused tests pass; ordinary corpus discovery
still skips. Other profiles, ownership/fault bounds and the 896-byte fitting
excess stay open. No production, decoder/adapter or README aggregate changes.

Init loop-lookup full masked corpus: [Note 830](WORKING_NOTES/830-init-loop-lookup-full-masked-corpus-20261003.md)
passes all 507 pages on the changed packed/remaining O2/g3 variant, masked
Status 0x2400FF00 and CU1 set, in 759.786 seconds. Linked text/descent is
4,880/3,256, lowest SP 0x80031D58, margin 72 bytes. Other full-corpus
profiles/mode, ownership/fault bounds and fitting remain open; 896 text bytes
over retail. No production, default-profile or README aggregate changes.

Init shared lookup loop: [Note 829](WORKING_NOTES/829-init-shared-lookup-loop-fitting-and-context-qualification-20261003.md)
adds an opt-in shape with 420 bounded context comparisons across six profiles
and both CU1 modes. Smallest linked text falls 16 bytes to 4,880 (896 over
retail); descent/margin remain 3,256/72. The nested-path gate executes. Across
two runs, 29 tests pass and one corpus test skips. At that checkpoint, full
changed-source corpus,
ownership/fault bounds and fitting remain open. Defaults and production unchanged.

Init shadow fitting: [Note 828](WORKING_NOTES/828-init-shadow-fitting-trials-and-helper-attribution-20261003.md)
rejects five size-only cursor/cache hypotheses; none reduces O2 text. All
temporary source edits are removed and restored compilation reproduces the
baseline. The builder's 424-word ledger includes 78 helper words; its actual
body is 346 words (53 over retail), narrowing the next fitting investigation.
Combined text remains 4,896 bytes; no new execution or production conversion.

Init full masked shadow corpus: [Note 827](WORKING_NOTES/827-init-full-masked-shadow-corpus-20261003.md)
passes all 507 retail pages with Status 0x2400FF00, CU1 set, and the
packed/remaining O2/g3 profile in 709.832 seconds. Linked text/descent remains
4,896/3,256, lowest SP 0x80031D58, neighbor margin 72 bytes. Other full-corpus
profiles/mode, complete ownership, synchronous-fault bounds and fitting remain
open. No production owner, implementation or README aggregate changes.

Init exception-entry masking: [Note 826](WORKING_NOTES/826-init-exception-entry-mask-and-masked-context-qualification-20261003.md)
executes the original IE/EXL clear prefix and pins the direct TLBL route.
Six profiles/both CU1 modes pass 72 new masked vector/sample comparisons,
bringing bounded shadow coverage to 420. All 29 focused tests pass. Corpus
context selection now distinguishes generic from exception-masked Status;
Note 825's full-page receipt remains generic, not relabeled. At this checkpoint,
full masked corpus,
storage ownership, synchronous-fault bounds and fitting stay open. No production
implementation, ownership, cost or README aggregate changes.

Init retail context footprint and first shadow corpus: [Note 825](WORKING_NOTES/825-init-context-neighbor-guard-and-first-shadow-corpus-20261003.md)
finds the SDK OSThread header is 0x1B0 bytes but retail's 32-FPR save/restore
footprint is 0x230. The neighbor guard now ends at 0x80031D10. All 507 pages
pass packed/remaining O2/g3 with CU1 set and that corrected guard: text/descent
4,896/3,256, lowest SP 0x80031D58, margin 72 bytes. All 23 focused tests pass;
the six-profile bounded shadow domain still passes 348 comparisons. Remaining
full-corpus profiles/mode, complete ownership and fitting stay open. No production
ownership, shared SDK header or README aggregate changes.

Init distance-builder/multiblock history: [Note 824](WORKING_NOTES/824-init-distance-builder-and-multiblock-fpr-history-20261003.md)
adds 144 gated context comparisons, bringing shadow coverage to 348 across
six profiles and both CU1 modes. Distance errors, accepted special trees,
multiple dynamic blocks, fixed/stored history and retained-snapshot errors pass.
Scratch f0-f11 are also checked before the wrapper's final f0 reload.
All 19 adapter/shadow/provenance tests pass. Costs and production ownership
are unchanged; full shadow corpus, actual storage ownership and fitting stay open.

Init semantic scratch-FPR publication: [Note 823](WORKING_NOTES/823-init-semantic-scratch-fpr-publication-20261003.md)
adds an opt-in 116-byte shadow state and 320-byte adapter. All 204 new bounded
context comparisons match retail across six compiled profiles, including both
CU1 modes, match-copy history, partial failures and three ROM samples.
All 110 focused tests pass, including the native all-retail-page semantic check.
Smallest combined text/descent is 4,896/3,256: still 912 text bytes over retail.
Full shadow corpus, original allocation ownership and fitting remain open.
Production Init stays 492 C / 47 assembly rows; README aggregates unchanged.

Init FPR/failure-frame recovery: [Note 822](WORKING_NOTES/822-init-fpr-provenance-and-failure-frame-corrections-20261003.md)
maps f1-f11 saves to actual live GPRs and dynamic decoding variables. Sorted
symbols now use retail signed comparisons; an opt-in frame variant preserves
the distance-root seed on literal-builder failure. All 103 focused tests pass,
including 90 matching seeded context runs and 30 unseeded frame-gap receipts.
Smallest seeded combined text/descent is 4,432/3,168, 448 text bytes over retail.
Scratch FPR publication, complete CU1-set compatibility, ownership and fitting
remain open. Production ownership and README totals unchanged.

Init original-call adapter: [Note 821](WORKING_NOTES/821-init-original-core-call-adapter-and-exception-context-20261003.md)
executes the retained exception wrapper around an isolated compiled-core adapter.
Sixty CU1-clear vector/retail-page context runs preserve full FPR/GPR state and
match decoding; six CU1-set probes expose remaining f1-f11 scratch differences.
All 95 focused checks pass. The adapter adds 224 linked text bytes: smallest
combined text is 4,384 (400 over retail), with observed/bounded core-call descent
3,144 bytes. Original storage ownership, CU1-set compatibility and fitting stay
open. Production Init assembly and README counts unchanged.

Init compiled retail corpus: [Note 820](WORKING_NOTES/820-init-all-retail-pages-through-compiled-guest-core-20261003.md)
passes all 507 retail pages through six linked IDO core images: 3,042 core
runs and compiled fixed initializations agree with retail, zlib and pristine
output. Maximum workspace writes are 3,564 bytes; maximum input reads are
3,057 bytes, with every run inside its own rounded DMA span (maximum 3,072).
All 83 focused regressions and 18 additional final-source representative core
runs pass. The note distinguishes the corpus-loaded fixture from its later
guard-seeding correction. Private buffers/O32 calls do not establish original
entry ABI, allocation ownership or hardware behavior. Production counts unchanged.

Init compiled connected paths: [Note 819](WORKING_NOTES/819-init-compiled-guest-stream-core-and-fixed-initializer-qualification-20261003.md)
executes 288 linked guest stream/core comparisons and 288 compiled fixed-table
initializations across six profiles. Stored/fixed/dynamic, mixed blocks, strict
limits, core alignment/workspace clamps and partial errors match retail. All
74 combined checks pass, including builder regressions. Full retail-page guest
replay and original-entry/hardware gates remain open; production counts unchanged.

Init compiled guest builder: [Note 818](WORKING_NOTES/818-init-compiled-guest-builder-differential-execution-20261003.md)
executes six fresh linked IDO builder images (three shapes, O2/g3 and O1) in
a bounded MIPS model. All 186 case/image comparisons agree with retail table/
scratch/state results and preserve saved O32 registers. All 63 combined tests
pass. This qualifies compiler words for the builder only, not connected guest
paths, original FPR entry ABI or hardware. Production counts/text unchanged.

Init builder symbol cursors: [Note 817](WORKING_NOTES/817-init-builder-symbol-cursor-and-capacity-qualification-20261003.md)
reaches packed remaining-count O2 4,160/376 (176 bytes over retail), trading
eight stack bytes for 32 text bytes. Aligned/end gives 4,192/360; retain uncached
no-cursor 4,224/352 as the lower-stack point. All 130 new native tests, two
rejection tests and twenty final-source guest compiles pass. Full-capacity
288-cell comparisons cover both cursor modes. Production owners/counts unchanged.

Init builder scan lead: [Note 816](WORKING_NOTES/816-init-builder-leaf-fill-and-bounded-length-scan-trials-20261003.md)
removes redundant bounds after the all-zero histogram return. Packed O2 reaches
4,192/368 and aligned 4,224/352, sixteen text bytes smaller at unchanged frame
bounds. Leaf-base capture gives no lead benefit. New unit/helper accounting
shows the old 413-word builder region contains 357 builder + 56 lookup words;
the scan trial has 352 + 56. All 135 focused tests and twenty final-source
guest compiles pass; production owners and README counts remain unchanged.
All 1,544 project tool tests pass at this checkpoint.

Init slot correction: [Note 815](WORKING_NOTES/815-init-decompressor-semantic-slot-ledger-correction-20261003.md)
adds generated retail/C slot accounting and guards the actual retail call roles.
Notes 812-813 had swapped dynamic `func_10006424` (257 words) with compressed
`func_10006E00` (167), and mislabeled the fixed wrapper. Cursor dynamic fits
at 220 words; compressed fits at 100. Builder's 413/293-word overrun is now
the main fitting target. Aggregate deficit remains 224 bytes; original-entry
ABI/storage gates and production Init assembly remain unchanged.
All 1,421 tool tests pass; eight fresh guest objects retain their text hashes.

Init lookup trials: [Note 814](WORKING_NOTES/814-init-dynamic-code-lookup-capture-and-inline-mask-trials-20261003.md)
qualifies full lookup capture, mask-only capture and inline mask calculation.
All 178 focused tests, all 1,415 project tool tests and 26 final-source guest
compiles pass, but no mode
improves O2 fitting. Inline removes the direct helper edge yet adds text;
captures increase stack. Retain cursor-only 4,208/368 and 4,240/352 comparison
points. Default hashes, production owners and README counts unchanged.

Init dynamic cursor lead: [Note 813](WORKING_NOTES/813-init-dynamic-length-base-and-pointer-cursor-trials-20261003.md)
improves packed/cached-builder O2 to 4,208 text bytes / 368-byte core call-frame
bound, 224 bytes over retail. Aligned cursor gives 4,240/352. Length base capture
alone or combined regresses stack. All 159 focused tests and 28 final-source
guest compiles pass, along with all 1,237 project tool tests. Cursor bounds
retain the 316-cell physical frame and
partial-error state. Production counts and original-entry ABI gates unchanged.

Init rolled-state trials: [Note 812](WORKING_NOTES/812-init-rolled-scratch-cache-and-local-allocation-trials-20261003.md)
reduces packed/bounded cached O2 text to 4,224 bytes, 240 over retail, at a
400-byte core call-frame bound. Uncached aligned remains the 4,256/384 lower-stack
lead. Local allocation capture gives no rolled benefit. All 102 focused tests
and all 1,078 project tool tests pass, along with 24 post-edit guest compiles.
A verified per-routine ledger distinguishes body/alignment words and exposes remaining
slot overruns and missing original wrappers. No production/README count change.

Init no-unroll lead: [Note 811](WORKING_NOTES/811-init-parent-byte-addressing-and-no-unroll-profile-20261003.md)
reduces frame-backed aligned/bounded O2 text to 4,256 bytes and core call-frame
bound to 384, leaving 272 bytes over retail. Parent byte addressing does not
improve it. All 71 focused native tests and 26 warning-clean guest compiles pass;
all 976 project tool tests also pass. Source and CLI dependency guards reject
byte-parent mode without frame tables. The new native checks cover
wrapped guest labels independently of native pointers. No production
conversion, original-entry hardware qualification or README count change.

Init workspace-base trial: [Note 810](WORKING_NOTES/810-init-builder-workspace-base-capture-trial-20261003.md)
adds opt-in pointer capture and 78 passing focused tests. Sixteen warning-clean
guest compiles and all 905 project tool tests pass. The guest receipts
show no text/stack improvement: aligned/bounded frame-backed O2
grows to 5,232 bytes / 408-byte core call-frame bound. Fewer workspace-field loads
are offset by more stack accesses. Default instruction bytes remain unchanged;
retain the previous uncached leads and exact production assembly.

Init combined builder qualification: [Note 809](WORKING_NOTES/809-init-decompressor-combined-builder-qualification-20261003.md)
tests aligned/packed entries with bounded shifts. All seventy focused tests and
all 827 project tests pass, along with eight warning-clean guest compiles.
Frame-backed packed O2 text is 5,184
bytes with a 408-byte core call-frame bound; aligned O2 is 5,200/400. Packing
trades sixteen text bytes for eight stack bytes and regresses O1 text. Its
607-word builder remains 314 words over retail, locating the main size deficit.
Production owners and README aggregates remain unchanged.

Init entry/shift trials: [Note 808](WORKING_NOTES/808-init-decompressor-entry-alignment-packing-and-bounded-shift-trials-20261003.md)
pins entry size/alignment/fields and tests direct leaf packing. Bounded builder
shifts improve frame-backed text to 5,200/5,424 bytes and core call-frame bounds
to 400/296 bytes, still overlong. All 757 tests pass, including sanitized
semantic/retail corpus and generated-tree checks; all 28 guest compiles are
warning-clean and default instruction bytes are unchanged. All modes remain opt-in; no
production owner or README aggregate change.

Init codegen trials: [Note 807](WORKING_NOTES/807-init-decompressor-flat-bit-helper-and-builder-base-codegen-trials-20261003.md)
measures a flat bit helper and two builder-base capture shapes. The smallest
frame-backed text is 5,216 bytes, still 1,232 over retail, with a larger builder
frame. Flattening reduces the stored-path frame bound but grows text. All remain
opt-in; no production conversion or README aggregate increase is claimed.
All 664 project tool tests pass, including 4,056 retail-page native C calls;
sixteen guest compiles are warning-clean and default object text is unchanged.

Init storage boundaries: [Note 806](WORKING_NOTES/806-init-exception-storage-boundaries-and-all-retail-core-page-survey-20261003.md)
extends the retained-core survey to all 507 retail pages; maximum workspace
write span is 3,564 bytes on page 50. A fresh guest probe measures SDK
`OSThread` at `0x1B0`, while retail 32-FPR context accesses extend to `0x230`.
Page-table DMA ends exactly at input; wrapper tests preserve the known context
footprint and numerical gap. These are observed boundaries, not allocation
capacity or a new production C conversion. README aggregates unchanged.

Init exception context: [Note 805](WORKING_NOTES/805-init-exception-decoder-fr1-full-width-fpr-context-model-20261003.md)
adds a connected FR=1 model using the actual wrapper/core words, full-width
FPR saves/reloads and explicitly unknown MTC1 upper halves. Both CU1 paths and
malformed streams are covered; the unconditional f0 delay load is preserved.
This is not hardware acceptance or allocation ownership. Production assembly,
README aggregates and the remaining C text/stack gates are unchanged.

Init retail page qualification: [Note 804](WORKING_NOTES/804-init-retail-page-dma-and-exception-core-address-qualification-20261003.md)
checks all 507 original Game pages against pristine decompressed bytes. Maximum
rounded DMA is 3,072 bytes, leaving 440 bytes before exception workspace.
Three selected retained-core calls pass at handler input/workspace/SP addresses;
all 98 Init tests pass. This is bounded model evidence, not full exception
context, allocation ownership or a production conversion. Aggregates unchanged.

Init frame-backed C: [Note 803](WORKING_NOTES/803-init-decompressor-frame-backed-c-and-guest-call-frame-bounds-20261003.md)
implements isolated physical scratch, guest table-address translation, and
fixed/dynamic root aliases. Fourteen frame-backed tests and all 95 Init tests
pass, including the maximum 316-cell domain and five call-analysis tests.
Guest state is 40 bytes plus a caller-owned `0xA88` frame; text is still
5,312/5,600 bytes. Conservative direct-call C frame bounds are 416/328 bytes,
excluding caller storage/adapter/context. No production owner changes;
text/stack generation and connected exception/adapter qualification remain open.
All 570 project tool tests and guest/tool/build/matcher checks pass; both
complete Init sections remain independently retail-exact.

Init decompressor frame mapping: [Note 802](WORKING_NOTES/802-init-decompressor-physical-frame-mapping-and-contract-tests-20261003.md)
adds an explicit physical `0xA88` view, guest/native offset checks, and nine
scratch/interface tests. All 76 Init tests pass. Sixteen table cells, 316
length cells, initializer output aliases, and pointer/index translation are
pinned; direct/wrapped modeled stack low-water is `0xA88`/`0xA98`.
All 551 project tool tests, guest layout checks, and project checks pass;
the linked matcher and both independent retail-exact Init sections are preserved.
The exception caller's unconditional FPR restore delay is preserved as an
open hardware-context boundary. This is not an adapter or production conversion;
next prototype frame-backed scratch C and qualify connected context ownership.

Post-pause Init assessment: [Note 801](WORKING_NOTES/801-init-post-pause-assembly-conversion-assessment-20261003.md)
freshly verifies 492 C / 47 assembly rows, all 67 Init tests, 492/492 exact C
functions, and both complete retail-exact Init sections. Bitmap/MMIO remain
small C-expressible candidates without a demonstrated matching replacement.
The tested decompressor C needs original ABI/frame recovery and a fitting
layout; SDK/boot/privileged assembly is not ordinary missing-C backlog.
No new Init conversion or aggregate change is claimed. Pending uncommitted
Game updater source/tests are preserved and outside this assessment.

Game actor-step dispatcher: [Note 800](WORKING_NOTES/800-game-actor-step-dispatcher-recovery-and-match-20261003.md)
replaces `func_1507C22C`'s zero-return placeholder with its 25-record scan and
conditional update dispatch. All 62 words match with seven independent address-
setup scheduling guards. Ten new tests, forty focused tests, and all 532 tool
tests pass; final argument-form rerun/build/matcher and section checks pass.
At the Note 800 checkpoint, connected updater/predicate placeholders remained
open, so it was not gameplay acceptance. Pending uncommitted `func_1507BDB0`
recovery needs its own final review, documentation, and coherent checkpoint;
the current Init assessment does not finish that Game handoff.
Init bitmap ordered-store trials in [Note 799](WORKING_NOTES/799-init-bitmap-volatile-store-scheduling-trial-20261003.md)
remain non-matching; production Init ownership and both exact sections are preserved.

Init guest-layout follow-up: [Note 798](WORKING_NOTES/798-init-decompressor-guest-layout-trial-and-conversion-boundary-20261003.md)
compiles the isolated decompressor with IDO O2/g3 and O1: 4,928/5,328 text bytes
versus the retained 3,984-byte region, with a 2,668-byte explicit state object.
Neither profile is an exact owner replacement. Two oversubscribed-tree fixtures
match the retained model; all nine semantic tests and all 522 tool tests pass. Both complete Init
sections remain independently retail-exact, and tool/build/matcher checks pass.
Init remains 492 C / 47 assembly rows. Next conversion work requires a new
bitmap/MMIO code-generation hypothesis or connected ABI/frame recovery; do
not repeat completed profile matrices or manufacture conversion with guards.

Init isolated C follow-up: [Note 797](WORKING_NOTES/797-init-connected-semantic-c-candidate-and-differential-oracles-20261003.md)
implements connected semantic decompression in an experimental, unlinked file.
Nine differential tests, all 67 focused Init tests, and all 522 tool tests
pass; tool checks pass.
Table/output/state comparisons include exceptional publication behavior.
Production remains exact assembly; guest layout/ABI and remaining malformed/
alias/context qualification precede any conversion claim.

Init connected-stream follow-up: [Note 796](WORKING_NOTES/796-init-dynamic-multiblock-and-core-entry-oracles-20261003.md)
adds eleven dynamic/mixed-block/core-entry tests; all 58 focused Init tests
and all 513 tool tests pass. Connected oracles now cover valid stored/fixed/dynamic streams,
repetition/error behavior, cursor rewind, both header skips, and saved-register
restoration. Production remains assembly. Next is isolated semantic C tested
against these oracles before any matching owner replacement.

Init compressed-decoder follow-up: [Note 795](WORKING_NOTES/795-init-compressed-decoder-fixed-stream-and-error-oracles-20261003.md)
adds ten fixed-stream/error oracle tests. All 47 focused Init tests, all 502
tool tests, and tool checks pass; both full Init sections remain retail-exact. Fixed streams match
zlib; output publication and malformed-stream differences are pinned as
bounded-model evidence. Production remains assembly; dynamic/multi-block/core
qualification precedes a connected C replacement.

Init table-builder follow-up: [Note 794](WORKING_NOTES/794-init-decompressor-table-builder-interface-and-canonical-oracles-20261003.md)
characterizes extra register inputs, table records, canonical lookups, and
fixed allocation indices explaining both retained root pointers. Nine builder
tests, all 37 focused Init tests, and all 492 tool tests pass; tool checks pass. Production remains
assembly; compressed-decoder/dynamic/error qualification is still required.

Init decompressor follow-up: [Note 793](WORKING_NOTES/793-init-decompressor-shared-contract-and-stored-block-oracle-20261003.md)
maps the shared frame and integer FPR contract and adds eight stored-block/
interface tests. All 28 focused Init tests, all 483 tool tests, and tool checks
pass; zlib stored
oracles cover payloads through 65,535 bytes. Production remains assembly.
Table-builder/fixed/dynamic/error qualification precedes connected C recovery.

Latest Init-only resume: [Note 792](WORKING_NOTES/792-init-resume-remaining-assembly-conversion-decision-20261003.md)
re-verifies all twenty focused Init tests, 492/492 exact C rows, and both
complete retail-exact sections. The 47 remaining assembly rows are unchanged.
Bitmap caller-domain and conditional allocator separation are characterized;
new matching code-generation evidence is needed for bitmap/MMIO conversion.
The other 45 rows are retained SDK/hardware or connected-interface work.
No new conversion, production Init edit, or README aggregate change is claimed.

Fresh `progress.csv` and linked retail comparison on 2026-10-03:

| Section | C functions | Raw assembly | C bytes |
| --- | ---: | ---: | ---: |
| Total | 5,463 / 6,042 (90.42%) | 579 | 1,930,924 / 2,256,728 (85.56%) |
| Init | 492 / 539 (91.28%) | 47 | 151,796 / 164,048 (92.53%) |
| Game | 4,790 / 5,321 (90.02%) | 531 | 1,759,488 / 2,072,880 (84.88%) |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) |

| Section | Byte-exact C | Address drift | Different C |
| --- | ---: | ---: | ---: |
| Total | 3,271 / 5,463 (59.88%) | 0 | 2,192 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,598 / 4,790 (54.24%) | 0 | 2,192 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Game `func_1507C324` converts its retained nineteen-word assembly to semantic
nested float copy/clamp C. Eight stale-checked guards normalize only a closed
FPR permutation; the complete 76-byte slot remains byte-exact. Fourteen new
tests, thirty focused copy/clamp/dimension tests, and all 475 tool tests pass;
full rebuild/project checks pass. Earlier exact slots, ten non-matching hashes,
restored spans, and both Init sections are preserved. C count/bytes rise by
one/76 and exact-C count rises by one; README changes only aggregate tables.
Next inspect the connected `func_1507BDB0` / `func_1507C22C` placeholders before
recovering their interfaces. See
[Note 791](WORKING_NOTES/791-game-nested-float-copy-clamp-conversion-and-match-20261003.md).

Game dimension helper `func_1507C3E0` now replaces its empty body with retail
type/subtype selection, state overrides, distinct radii, attachment expansion,
optional scaling, and ordered nullable halfword outputs. Sixteen focused tests
and all 461 tool tests pass; build/project checks pass. It remains non-matching:
310 body words plus ten padding nops, 312 differences, no new guards/profiles.
The adjacent refresh wrapper and retained leaf remain exact; earlier Game
regressions and both complete Init sections are unchanged. Aggregates/README
were unchanged for that checkpoint. Its then-pending `func_1507C324` conversion
is completed in Note 791; dimension matching and whole-chain acceptance remain
open. See
[Note 790](WORKING_NOTES/790-game-actor-dimension-helper-semantic-recovery-20261003.md).

Init allocator `func_10003C6C` now corrects a duplicate twelve-byte header
addition in its rear-allocation C path, found by production-body host tests.
Six allocator tests establish conditional valid-heap separation from bitmap
configuration storage; all alignment classes and both directions are covered.
All twenty focused Init tests and all 445 tool tests pass.
The existing guarded retail layout is refreshed to 231 rows for the corrected
257-word C body and trailing nop. Full rebuild/matcher, independent allocator
and complete Init-section comparisons, and Game regressions pass. This is a
semantic correction, not an assembly-to-C conversion or direct compiler match;
Init/README aggregates are unchanged. See
[Note 789](WORKING_NOTES/789-init-bitmap-allocator-provenance-and-rear-bound-correction-20261003.md).

Init bitmap `func_10005BE0` now has eight instruction-word-driven contract tests,
including invalid-count and alias timing. The only direct retail resize call
has statically positive counts 107..362; indirect/external calls and allocator
provenance remain unproven. All fourteen focused Init tests, all 439 tool tests,
and project tool checks pass. Assembly ownership, section parity, aggregates,
and README are unchanged. Next establish allocator provenance and a new compiler/dataflow
hypothesis before conversion trials. See
[Note 788](WORKING_NOTES/788-init-bitmap-retail-caller-domain-and-edge-contract-20261003.md).

Game `func_1510F800` now explicitly forwards its s32 context argument to the
retained setter. All eight words remain directly byte-exact with no guards or
profile changes. Fifteen focused/integrated tests and all 431 tool tests pass;
build/project checks pass. Twenty-six earlier exact slots, nine prior hashes,
restored spans, and both Init sections are unchanged; the setter's retained
256-byte interval independently matches. Aggregates/README are unchanged.
Its then-pending dimension helper is semantically recovered in Note 790;
whole-chain acceptance and the earlier dispatcher/matrix/query matching remain
open. See
[Note 787](WORKING_NOTES/787-game-context-forwarding-interface-recovery-20261003.md).

Game `func_1504452C` replaces its zero-return placeholder with the three-vertex
offset/origin/coefficient transform, not a context dispatcher. All 75 words
match; twenty expected-word guards normalize only closed register cycles and
two independent origin-load schedules. Eleven focused tests and all 416 tool
tests pass; full rebuild/project checks pass. Earlier exact slots, nine prior
non-matching hashes, restored spans, and both Init sections are unchanged.
README matcher aggregates are updated. Its then-pending explicit context
forwarding is recovered in Note 787; the setter remains assembly and dimension
helper recovery remains open. See
[Note 786](WORKING_NOTES/786-game-three-vertex-transform-recovery-and-match-20261003.md).

Game `func_15044380` replaces its zero-return placeholder with the complete
actor/context dispatcher, preserving descending/optional ascending passes,
live eligibility, preparation-time context capture, and final reset/byte restore.
Fourteen focused tests and all 405 tool tests pass; build/project checks pass.
It remains non-matching: 107 body words, no padding, twenty differences, no new
guards/profiles. All 22 exact regression slots, eight prior non-matching hashes,
restored spans, and both Init sections are unchanged. Aggregate tables/README
are unchanged for that recovery. Its then-pending `func_1504452C` is recovered
as a vertex transform in Note 786. Dimension recovery and the context wrapper's
explicit argument remain open, so whole-chain acceptance is open. See
[Note 785](WORKING_NOTES/785-game-actor-context-dispatcher-semantic-recovery-20261003.md).

Game `func_15044660` replaces its false zero-return C placeholder with the
complete original actor-preparation assembly. All 156 words / 624 bytes match.
Special actor types load a stack word not initialized by the routine, so
ordinary C recovery needs a reachability/stack-provenance decision rather than
an invented index value. Its interface is void(actor, x, y, z), not s32(void).
The C count decreases by one; exact-C counts are unchanged. Its then-pending
dispatcher `func_15044380` is recovered in Note 785; its dimension helper
remains a placeholder. See
[Note 784](WORKING_NOTES/784-game-actor-preparation-restoration-and-stack-boundary-20261003.md).

Game `func_15047700` now replaces its empty body with the reflection look-at
matrix builder, retail-specific degenerate-axis branches, and complete
direction/color output with preserved padding. Fourteen focused tests and
all 388 tool tests pass; build/project checks pass. It remains non-matching:
282 body words plus six padding nops, 245 differences, no new guards/profiles.
Both matrix wrappers and nineteen earlier exact routines remain exact; seven
non-matching hashes, restored spans, and both Init sections are unchanged.
Next inspect the earlier actor/context placeholder cluster `func_15044380`
and its preparation dependency `func_15044660`. See
[Note 783](WORKING_NOTES/783-game-reflection-look-at-matrix-semantic-recovery-20261003.md).

The latest Init pause resume reassesses remaining assembly. Fresh inventory
still reports 492 C / 47 assembly rows; all 492 C rows and both complete Init
sections match retail. Six focused Init tests pass. Only bitmap `func_10005BE0`
and MMIO `func_100038E0` remain bounded ordinary-C candidates, with no proven
matching replacement. Prefer a genuinely new bitmap dataflow/provenance
hypothesis; do not repeat the completed compiler matrices. The follow-up at
clean baseline `21070c9` re-verifies both sections and six focused tests, and
records the bitmap's unchecked resize argument, configured-pointer lifetime,
and post-fill count reload. Caller-domain/allocator provenance remains open.
Production Init and
README aggregates are unchanged; pending Game work is preserved. See
[Note 782](WORKING_NOTES/782-init-pause-resume-conversion-assessment-20261003.md).

Game `func_15047390` now replaces its empty body with the complete SDK-grounded
look-at matrix builder, including retail's three exact-zero length fallbacks
and ordinary `sqrtf` calls. It remains non-matching: 188 body words plus two
padding nops, 171 differences, no new guards or compiler profiles. Twelve
focused tests and all 374 tool tests pass; full build/project checks pass.
The fixed-matrix wrapper is exact; nineteen prior exact neighbors, six
non-matching hashes, restored spans, and both Init sections remain unchanged.
Aggregate tables/README are unchanged. The then-pending reflection builder
`func_15047700` is now recovered in Note 783 and remains non-matching. See
[Note 781](WORKING_NOTES/781-game-look-at-matrix-semantic-recovery-20261003.md).

Game `func_150472C0` now converts retained assembly to the complete void
descriptor-to-height-result builder. All 52 words match directly without new
guards or profiles. It preserves the eighteen-byte coordinate copy, separate
flag expressions, post-publication state reload, and final value read. Eight
focused tests and all 362 tool tests pass; full build/project checks pass.
Eighteen exact neighbors, six non-matching hashes, restored spans, and both
Init sections remain unchanged. Its then-pending matrix builder
`func_15047390` is now recovered in Note 781 and remains non-matching. See
[Note 780](WORKING_NOTES/780-game-descriptor-height-result-builder-direct-match-20261003.md).

Game `func_1504715C` now replaces its zero-return placeholder with the complete
void actor-to-height-result builder. It copies or synthesizes the nine vertex
coordinates, preserves result padding, and publishes metadata/state/entity
ownership with retail's alias-sensitive read order. It remains non-matching:
85 body words plus four padding nops, 76 differences, no new guards/profiles.
Twelve focused tests and all 354 tool tests pass; full build/project checks
pass. Eighteen exact neighbors, five query hashes, restored spans, and both
Init sections remain unchanged. Aggregate tables and README are unchanged.
Its then-pending descriptor/result builder `func_150472C0` is now recovered
in Note 780; this actor builder's byte matching remains open. See
[Note 779](WORKING_NOTES/779-game-actor-height-result-builder-semantic-recovery-20261003.md).

Game `func_15046D00` now replaces its zero-return placeholder with the complete
outer highest-height combiner. All 161 words match directly without new guards
or profiles. Ties/unordered comparisons select the context-3 non-entity result;
both failure paths clear only flag bit 2. Twelve focused tests and all 342
tool tests pass; full build/project checks pass. Seventeen exact neighbors,
five non-matching query hashes, restored spans, and both complete Init sections
remain unchanged. Converted totals are fixed; one different C row becomes
exact. Its then-pending actor/result builder `func_1504715C` is now recovered
in Note 779 and remains non-matching. See
[Note 778](WORKING_NOTES/778-game-outer-highest-combiner-direct-match-20261003.md).

Game `func_1504697C` now replaces its zero-return placeholder with the complete
highest entity/terrain combiner. All 161 words match directly without new
guards/profiles. Both early rejection and the both-failed fallback clear only
flag bit 2, preserving state/value. Twelve focused tests and all 330 tool
tests pass; full build/project checks pass. Sixteen exact neighbors, four
entity-query hashes, restored spans, and both Init sections remain unchanged.
The terrain highest query retains its documented 76 differences and prior
hash. Converted totals are unchanged; one different C row becomes exact.
Its then-pending outer combiner `func_15046D00` is now recovered in Note 778. See
[Note 777](WORKING_NOTES/777-game-entity-terrain-highest-combiner-direct-match-20261003.md).

Game `func_150466F8` now converts retained assembly to the complete entity/
terrain lowest-height combiner. All 161 words match directly without new guards
or profiles. It snapshots both records before querying, interprets both
returns through their low byte, and gives terrain precedence on ties or
unordered comparisons. Failure clears only flag bit 2. Twelve focused tests
and all 318 tool tests pass; full build/project checks pass. Fifteen exact
neighbors, four entity-query hashes, restored spans, and both entire Init
sections remain unchanged. Its then-pending highest entity/terrain combiner
`func_1504697C` is now recovered in Note 777. See
[Note 776](WORKING_NOTES/776-game-entity-terrain-lowest-combiner-direct-match-20261003.md).

Game `func_15046460` now replaces its zero-return placeholder with the complete
highest-height combiner. All 166 words match directly with no new guards or
profile changes. Early rejection clears state/value and flag bit 2; the
both-failed fallback instead retains the selected record's state/value and
clears only bit 2. Ten new tests and all 306 tool tests pass; full build and
project checks pass. Prior recovered neighbors/spans and both entire Init
sections remain unchanged. Converted totals are unchanged; one different C
row becomes exact. Its then-pending entity/terrain combiner `func_150466F8`
is now recovered in Note 776. See
[Note 775](WORKING_NOTES/775-game-highest-height-combiner-direct-match-20261003.md).

Game `func_150461D0` now has its complete lowest-height combiner in semantic
C instead of retained assembly. All 164 words match directly without new
guards or compiler profiles. It snapshots both complete result records before
count preparation, truncates both query returns to bytes, and chooses the
lower height with second-result precedence on ties/unordered comparisons.
Ten new tests and all 296 tool tests pass; the full code build and project
checks pass. Neighboring recovered routines, collector/producer spans, and
both complete Init sections remain unchanged. Its then-pending highest-height
combiner `func_15046460` is now recovered in Note 775. See
[Note 774](WORKING_NOTES/774-game-lowest-height-combiner-direct-match-20261003.md).

Game `func_15045D48` now has its complete context-3 entity lowest-height query
in semantic C instead of retained assembly ownership. It uses scratch
`D_800D3830`, the exact retail lowest-height sentinel, state `3`, and a cached
entity pointer for the later flag read. Its 145-word slot contains 144 body
words plus one padding nop, with 72 differences and no new guards. Fifteen
new tests and all 286 tool tests pass; full code build and project checks pass.
Prior recovered spans and both complete Init sections remain exact. This adds
a converted row, not an exact match. Its then-pending combiner `func_150461D0`
is now recovered in Note 774; entity-query matching and gameplay qualification
remain open.
See [Note 773](WORKING_NOTES/773-game-context3-entity-lowest-height-query-recovery-20261003.md).

Game `func_15045AE4` now has the complete context-2 entity highest-height
query instead of a zero-return placeholder. It uses scratch `D_800D37E0`,
the retail -10000 sentinel, state `2`, and late entity-index/base reloads.
Its 153-word slot contains 150 body words plus three padding nops, with
88 differences and no new guards. Fifteen new tests and all 271 tool tests,
full code build, and project checks pass. Previously recovered spans and
both entire Init sections remain exact. Aggregate tables are unchanged.
Its then-pending `func_15045D48` is recovered semantically in Note 773;
matching and natural gameplay qualification remain open.
See [Note 772](WORKING_NOTES/772-game-context2-entity-highest-height-query-recovery-20261003.md).

Game `func_15045880` now has its complete entity-indexed lowest-height query
in semantic C, replacing retained assembly ownership. Its 153-word slot is
150 body words plus three padding nops, with 88 word differences and no new
guards. Fifteen new tests cover metadata, helper reloads, and result/candidate/
entity-table aliasing; all 256 tool tests, full code build, and project checks
pass. Earlier recovered spans and both entire Init sections remain exact.
This adds a converted row, not an exact C match. Its then-pending adjacent
`func_15045AE4` placeholder is recovered semantically in Note 772;
lowest/highest entity-query matching and gameplay qualification
remain open. See
[Note 771](WORKING_NOTES/771-game-entity-lowest-height-query-semantic-recovery-20261003.md).

Game `func_150470B0` and its four-argument dispatch `func_15046C00` now
match all 43 and 32 words directly from semantic C. Eleven new integrated
tests cover the opposite-bound cached query and both caller shapes; all 241
tool tests, full code build, and project checks pass. Correcting the existing
three-argument `func_1504530C` signature preserves its exact 120 bytes.
No new guards or profile changes; retained fallback assembly remains untouched.
Earlier recovered spans and both complete Init sections remain exact. Its
then-pending entity lowest-height query is recovered semantically in Note 771; the
highest-height entity query's 72 differences and gameplay acceptance are open.
See [Note 770](WORKING_NOTES/770-game-opposite-cached-height-query-and-dispatch-direct-match-20261003.md).

Game `func_15045800` now dispatches through the recovered cached-height
status query `func_15047004`. Both match directly from semantic C: 32 and
43 words, no new guards or profile changes. Twelve integrated tests exercise
the actual cached query, dispatch, and fallback wrapper; all 230 tool tests,
full code build, and project checks pass. Both sibling dispatch wrappers,
earlier recovered spans, and both complete Init sections remain exact.
Its then-pending opposite-bound query is completed in Note 770; downstream
entity-query matching and natural gameplay qualification remain separate.
See [Note 769](WORKING_NOTES/769-game-cached-height-query-and-dispatch-direct-match-20261003.md).

The resumed Init audit confirms 47 assembly rows / 12,252 bytes, with all
492 C rows exact and both complete code/data sections matching retail.
Only `func_100038E0` (44 bytes) and `func_10005BE0` (76 bytes) remain bounded
ordinary-C candidates; neither has a proven matching replacement after the
documented compiler trials. The other 45 rows retain SDK, hardware, boot, or
shared-register contracts. No Init source conversion is claimed. See
[Note 768](WORKING_NOTES/768-init-remaining-assembly-current-decision-20261003.md).

Game `func_15045780` is now semantic C and matches all 32 words directly,
without guards or profile changes. Five new tests cover the early-rejection
flag mask, two-count buffer, raw return forwarding, helper mutations, NaNs,
and all halfword selectors. All 218 tool tests and project checks pass;
both complete Init sections and previously restored spans remain exact.
The entity query retains its 72 differences. Its then-pending dispatch wrapper
`func_15045800` and cached query `func_15047004` are completed in Note 769;
natural gameplay qualification is separate. See
[Note 767](WORKING_NOTES/767-game-entity-height-wrapper-direct-match-20261003.md).

The shared-register entity producer and its return/cleanup closure now match
all 520 retail bytes across three entries. Explicit secondary-count pointer
types preserve both C helpers' exact bytes. This removes one false C inventory
row, not three, and does not add a C match. All 213 tool tests, full build, and project checks pass;
both complete Init sections and earlier collector/query spans remain exact.
Its then-pending `func_15045780` wrapper is converted in Note 767; gameplay qualification
and the entity query's 72 differences remain separate. See
[Note 766](WORKING_NOTES/766-game-entity-scan-producer-assembly-restoration-20261003.md).

Game `func_15045F8C` now has its complete entity-indexed highest-height query.
It remains non-matching: 144 body words plus one padding nop, 72 differences,
no new guards. Twelve new tests cover metadata, entity-address publication,
flag combinations, and alias-sensitive reloads. All 208 tool tests, full build, and project checks
pass; recovered neighbors, collector group, and both Init sections remain exact.
Matching aggregates did not change for that recovery. Its then-placeholder
upstream `func_150A6568` producer is restored in Note 766; natural wrapper
qualification remains open. See
[Note 765](WORKING_NOTES/765-game-entity-height-query-semantic-recovery-20261003.md).

Game `func_1504554C` now has its complete context-3 highest-height query.
All 114 words match with fifteen strict guards for the same closed compiler
layout sets as the preceding lowest-height query. Thirteen new tests and all
196 tool tests pass; full build and project checks pass. Recovered neighbors,
collector/context group, and both complete Init sections remain exact.
Its then-pending `func_15045F8C` is recovered semantically in Note 765; the
upstream producer and wrapper qualification remain open. See
[Note 764](WORKING_NOTES/764-game-context3-highest-height-query-recovery-20261003.md).

Game `func_15045384` now has its complete lowest-height query/result body.
All 114 words match with fifteen strict guards for a private spill slot,
closed count/index register swap, and equivalent vertex-copy pointer schedule.
Thirteen new tests and all 183 tool tests pass; the full build and project
checks pass. Neighbors, the collector/context group, and both whole Init
sections remain exact. Its then-pending `func_1504554C` query is completed
in Note 764. See
[Note 763](WORKING_NOTES/763-game-lowest-height-query-recovery-20261003.md).

The handwritten collector/context group now matches all 5,712 retail bytes,
replacing 23 placeholder entries across six inventory groups. All 167 tool
tests pass. This restores original code, not six new C conversions.
See [Note 760](WORKING_NOTES/760-game-collector-context-assembly-restoration-20261003.md).

The resumed Init assessment still finds 47 assembly rows / 12,252 bytes.
Only the 44-byte MMIO leaf and 76-byte bitmap leaf are bounded C candidates;
neither has a proven matching replacement. Both entire Init sections remain
exact. See [Note 761](WORKING_NOTES/761-init-resume-conversion-decision-20261003.md).

Twenty further partial-volatility/profile trials still do not match the
eleven-word MMIO leaf. All emitted store traces pass; original assembly stays
in production. Three new baseline regression tests and all 170 tool tests
pass. Both complete Init sections remain exact. Its then-pending Game
`func_15045384` recovery is now completed in Note 763; see
[Note 762](WORKING_NOTES/762-init-mmio-partial-volatility-trials-20261003.md).

Game `func_150450CC` now has its complete highest-height candidate selection,
vertex copy, optional metadata, and result-flag body instead of a zero-return
placeholder. It remains non-matching: 143 body words plus one padding nop fill
the 144-word slot, with 76 differing word positions and no new guards. Eleven
new tests and all 164 tool tests pass; the full build and project checks pass.
Previously recovered spans and both entire Init sections remain exact.
Matching aggregates were unchanged by that C recovery. Its then-placeholder
collector is now restored as original shared-register assembly in Note 760;
natural gameplay qualification remains separate. See
[Working Note 759](WORKING_NOTES/759-game-highest-height-query-semantic-recovery-20261002.md).

Game `func_15044CE4` now explicitly returns the overlap result to its record
callback caller. The complete 23-word span remains directly exact, without
guards. Six new tests cover every signed-halfword scale, result forwarding,
load/store aliasing, unrelated-byte preservation, and actual wrapper/overlap
integration. All 153 tool tests, the full build, and project checks pass;
all recovered neighboring spans and both entire Init sections remain exact.
Matching totals do not change. Its then-pending `func_150450CC` recovery is
now completed semantically, but remains non-matching, in Note 759. See
[Working Note 758](WORKING_NOTES/758-game-position-scale-overlap-wrapper-return-20261002.md).

Game `func_15044B78` now replaces its zero-return placeholder with the complete
oriented player/record overlap test. All 91 words match; six strict guards
remap three private integer stack slots without changing any other instruction.
Its angle helper `func_15048A40` now explicitly returns `f32` and remains exact
across all twelve words. Sixteen new 32-bit tests and all 147 tool tests pass;
the full build and project checks pass. Constructor, allocator, and list pass
spans remain exact, as do both entire Init sections. Its then-pending callback
return contract in `func_15044CE4` is now completed by Note 758. See
[Working Note 757](WORKING_NOTES/757-game-oriented-record-overlap-match-20261002.md).

The resumed Init audit rebuilt the production baseline and reconfirmed all
492 Init C rows and both entire Init code/data sections byte-exact. The 47
remaining assembly rows / 12,252 bytes include two deferred small-leaf C
experiments; neither has a proven matching replacement. No Init conversion
or aggregate change is claimed for that audit. Its interrupted Game draft
was preserved in stash object `5b554b70ce671454878a1025fec26b93ad457153`.
Note 757 now completes that recovery in production; retain the stash only as
historical WIP, not as a patch to apply over the completed source.
See [Working Note 756](WORKING_NOTES/756-init-resume-verification-and-conversion-boundary-20261002.md)
for the remaining groups, acceptance gates, and exact draft-resume command.

Game `func_15044A28` now replaces its zero-return placeholder with the complete
record-list callback/delay/lifetime pass. All 84 words match directly without
guards; constructor and allocator spans remain exact. Fifteen new 32-bit tests
cover mutation, cached-next traversal, unlink-before-release-mark ordering,
delay timing, and word wrap. All 131 tool tests, project checks, and the full
code build pass; both entire Init sections remain exact. Next downstream
dependency was `func_15044B78`, now completed by Note 757. See
[Working Note 755](WORKING_NOTES/755-game-record-list-processor-direct-match-20261002.md).

Game `func_15044964` now replaces its null-return placeholder with the complete
common-header allocator and tail-list registration routine. All 49 words
match directly from C without guards; its 37-word constructor remains exact.
Ten new 32-bit tests include the actual constructor-to-allocator path with
only the heap call mocked. All 116 tool tests, project checks, and the full
code build pass; both entire Init sections remain exact. Its then-pending list
processor dependency is now completed by Note 755. See
[Working Note 754](WORKING_NOTES/754-game-common-record-allocator-direct-match-20261002.md).

Game `func_150448D0` now replaces its zero-return placeholder with the complete
position/scale record constructor. All 37 words match directly from C under
the existing profile, without guards. Seven new 32-bit tests and all 106 tool
tests, project checks, and the full code build pass. Both entire Init sections
remain exact. At that checkpoint the common allocator still had a null-return
placeholder; Note 754 now completes that source dependency, without gameplay
qualification.
See [Working Note 753](WORKING_NOTES/753-game-position-scale-constructor-direct-match-20261002.md).

Game `func_15040CC8` now replaces its zero-return placeholder with the complete
thirty-record callback dispatcher and post-dispatch cleanup. It remains
non-matching: the 38-word retail slot routes to a 39-word semantic overflow
body. Eight new 32-bit tests and all 99 tool tests pass; the full code build
and project checks pass, and both entire Init sections remain exact. Aggregate
counts do not change because the placeholder already counted as C. Resume
ordinary recovery at `func_150448D0`; see
[Working Note 752](WORKING_NOTES/752-game-record-dispatcher-semantic-recovery-20261002.md).

Game `func_1501CDC0` now replaces its zero-return placeholder with the complete
row-destination byte fill. All 37 words match; two strict guards normalize
only independent opening arithmetic/counter scheduling. Six 32-bit behavior
tests cover stride, fill bounds, row isolation, duplicates, and pointer reloads.
All 91 tool tests, the full build, and project checks pass. Both entire Init
sections remain byte-exact. See
[Working Note 748](WORKING_NOTES/748-game-row-destination-byte-fill-match-20261002.md).

The resumed Init-only assessment reconfirms all 492 C rows and both entire
linked Init sections exact. Of 47 remaining assembly rows, two small leaves
are deferred C rewrite candidates: `func_100038E0` and `func_10005BE0`.
Neither has a proven matching replacement. The other 45 rows retain SDK,
privileged, shared-frame, or nonstandard-register contracts. No source or
progress totals changed; no rebuild was performed for this audit. The Init
experiment order and acceptance gates are in
[Working Note 749](WORKING_NOTES/749-init-remaining-assembly-resume-assessment-20261002.md).

Twenty additional isolated MMIO trials across five source shapes and four IDO
profiles also produce no exact `func_100038E0` body after resolving relocations
at the retail addresses. Production assembly remains unchanged. New results
include pointer-lifetime and return-delay evidence, not a completed conversion.
Resume the bounded Init experiments at bitmap leaf `func_10005BE0`; see
[Working Note 750](WORKING_NOTES/750-init-mmio-pointer-lifetime-profile-trials-20261002.md).

The bitmap follow-up completes 55 shape/profile comparisons without an exact
`func_10005BE0` body. All eleven source shapes pass 65 host behavior cases
twice each, but this is not a production conversion. Both small Init leaves
remain deferred pending a new source/compiler rationale. Keep the verified
assembly baseline; ordinary Game work can resume at `func_15040CC8`. See
[Working Note 751](WORKING_NOTES/751-init-bitmap-loop-mask-profile-trials-20261002.md).

Game `func_151DE85C` now replaces its zero-return placeholder with the complete
menu-state reset. All 35 words match directly from C without guards or a
compiler override. Five new tests cover call ordering, globals, object bytes,
call mutation, and repeated reset. All 85 tool tests, the full build, and
project checks pass. Both entire Init sections remain byte-exact. See
[Working Note 747](WORKING_NOTES/747-game-menu-state-reset-direct-match-20261002.md).

Game `func_151D2F00` now replaces its zero-return placeholder with the complete
descriptor-record constructor. All 36 words match; six strict guards normalize
only the independent allocator argument-setup schedule. Five new behavior tests
cover failure, forwarding, descriptor copy, bookkeeping resets, and every
flag-byte value. All 80 tool tests, the full build, and project checks pass.
Both entire Init sections remain exact. See
[Working Note 746](WORKING_NOTES/746-game-descriptor-record-constructor-match-20261002.md).

Game `func_151BD21C` now replaces its zero-return placeholder with the complete
owner/selector event handler. All 40 words match; nine strict entries normalize
register reuse, flag-store scheduling, and one inserted return-delay nop with
its two branch-displacement adjustments. Eight 32-bit source-behavior tests
and all 75 tool tests pass; the full build and project checks pass. Both complete
Init sections remain byte-exact. See
[Working Note 745](WORKING_NOTES/745-game-owner-selector-event-handler-match-20261002.md).

Game `func_151B1918` now replaces its zero-return placeholder with the complete
eleven-child-slot cleanup. All 35 words match; six strict guards normalize
one equivalent cursor-relative address and independent counter scheduling.
Seven new source-behavior tests execute the actual C in a freestanding
32-bit fixture, preserving the guest slot stride. All 67 tool tests, the
full build, and project checks pass. Both complete Init sections remain exact.
See [Working Note 744](WORKING_NOTES/744-game-eleven-child-slot-cleanup-match-20261002.md).

Game `func_151A4900` now replaces its zero-return placeholder with the complete
threshold-scaled record update. All 39 words match; eleven strict guards
normalize one independent counter-reload scheduling rotation and two
commutative multiply operand orders. Seven new source-behavior tests and all
60 tool tests pass, along with the full build and project checks. Both complete
Init sections remain byte-exact. See
[Working Note 743](WORKING_NOTES/743-game-threshold-scaled-record-update-match-20261002.md).

Game `func_15163504` now replaces its zero-return placeholder with position
publication from three independent float pointers followed by optional callback
dispatch. All 41 words match directly from C without guards or a compiler
override. Six source-behavior tests and all 53 tool tests pass; the full build
and project checks pass. Both complete Init sections remain byte-exact. See
[Working Note 742](WORKING_NOTES/742-game-position-publication-and-callback-direct-match-20261002.md).

Game `func_1515FFEC` now replaces its zero-return placeholder with the complete
41-word compact-record lifecycle: flags at `0x0E`, selector at `0x0F`, timer
at `0x12`, and callback table `D_8008B0D0`. Two strict guards normalize only
completion-flag spill width. The existing lifecycle fixture now tests both
record layouts independently; all 47 tool tests and the full build pass.
Both complete Init sections remain exact. See
[Working Note 741](WORKING_NOTES/741-game-compact-timed-callback-record-match-20261002.md).

Game `func_15158224` now replaces its zero-return placeholder with the complete
41-word timed-callback lifecycle using selector offset `0x12` and table
`D_8008AE00`. Two strict expected-word guards normalize only completion-flag
spill width across the callback. Eight new source-behavior tests and all 39
tool tests pass; the full build and linked comparison pass, and both complete
Init sections remain exact. See
[Working Note 740](WORKING_NOTES/740-game-secondary-timed-callback-record-match-20261002.md).

Game `func_15157FE8` now replaces its zero-return placeholder with the complete
dual projection-matrix emitter. All 36 words match directly from SDK-macro C
without guards or a profile override. Three source-behavior tests pass; all
31 tool tests and the full code build pass. Both complete Init sections remain
exact. See [Working Note 739](WORKING_NOTES/739-game-dual-matrix-emitter-direct-match-20261002.md).

Init `func_10001420` is now represented in semantic C and matches its complete
nine-word memory-clear slot. Six relocation-aware expected-word guards
normalize only the closed register allocation; no instructions are inserted
or removed. Three source-behavior tests pass, and both complete Init sections
remain byte-exact after the full rebuild. Init retains 47 assembly rows /
12,252 bytes. See
[Working Note 736](WORKING_NOTES/736-init-memory-clear-leaf-conversion-20261002.md).
Five bounded compiler trials for MMIO leaf `func_100038E0` preserve its
assembly ownership: none establishes a direct eleven-word C match. The best
count-matching trial still changes address reuse and the return delay slot.
See [Working Note 737](WORKING_NOTES/737-init-mmio-leaf-bounded-compiler-experiment-20261002.md).
Bitmap initializer `func_10005BE0` also remains assembly after three compiler
trials. The count-fitting candidate passes 65 host behavior cases but has no
direct match or completed extraction from the shared assembly owner. See
[Working Note 738](WORKING_NOTES/738-init-bitmap-leaf-contract-and-compiler-experiment-20261002.md).

Game `func_15145128` now matches all 50 words after restoring the retail
optional-length/reciprocal expression shape and output multiply order. Three
expected-word guards normalize only the leaf frame, fallback local address,
and stack restore. Nine source-behavior tests cover zero vectors, omitted
outputs, in-place operation, and output-pointer aliasing. The neighboring
cross product remains exact, and both complete Init sections remain exact.
See [Working Note 734](WORKING_NOTES/734-game-vector-normalizer-match-20261002.md).

Init `__n_CSPHandleMIDIMsg` now matches all 954 words directly from semantic
C, including Rare's custom envelope, oscillator, controller, and notification
paths. Restored interleaved audio data ownership places the physical jump
tables at their retail addresses; six original floats restore three omitted
constant slots. Direct whole-section comparison now confirms all 164,048
Init code bytes and all 17,376 initialized-data bytes byte-exact. This is
linked-image evidence, not a gameplay qualification or a claim that the
remaining original assembly must become C. See
[Working Note 733](WORKING_NOTES/733-init-midi-handler-and-complete-init-image-match-20261002.md).

The remaining Init assembly was reassessed in
[Working Note 735](WORKING_NOTES/735-init-retained-assembly-reassessment-20261002.md).
No further compiler-generated recovery is established. That audit identified
three small custom leaves as possible C rewrite experiments. Note 736 now
completes `func_10001420`; `func_100038E0` is deferred after bounded trials,
and `func_10005BE0` is deferred after its separate bounded experiment.
This distinction concerns C representation versus proven original provenance.

The supported Init C-conversion queue is complete. The ordinary Game overlap
dependency `func_15044B78` now matches all 91 words. Its record allocator,
position/scale constructor, and list pass remain exact, without gameplay
qualification of downstream callbacks. Its 23-word position/scale wrapper
`func_15044CE4` now explicitly forwards the result and remains directly exact.
`func_150450CC` now has a recovered semantic body but remains in the
non-matching queue at 76 real word differences. Audit its handwritten
`func_150A3A70` collector/cleanup group as a complete register-contract unit;
that dependency remains a placeholder. Another ordinary source recovery can
resume at `func_15045384`, without resolving that collector gap.
`func_15040CC8` has a recovered semantic body but remains in the separate
non-matching/overflow queue; its retail-slot matcher reports 36 differences.
Keep `func_150A76F0` in its handwritten/register-contract workstream and
`func_150F631C` in its separate near-match cleanup queue.

Init `__sinf` now matches all 112 words directly from SDK-grounded C in a
separate generated slice. A scoped linker anchor restores its original
constant block, which had drifted by `0x30` bytes behind absolute symbol
assignments. Direct comparisons confirm the complete routine and 224 bytes
of math/NaN constants. No word guards or compiler override are required.
See [Working Note 732](WORKING_NOTES/732-init-sdk-sine-recovery-and-constant-layout-match-20261002.md).

The Game timed callback lifecycle `func_1513B798` now matches its complete
41-word slot. It decrements the optional signed timer, dispatches the indexed
completion callback, and releases the record when either path completes. Two
guarded words normalize only IDO's completion-flag spill width across the
indirect call. See
[Working Note 728](WORKING_NOTES/728-game-timed-callback-lifecycle-match-20261002.md).

The Init sequence-event and tempo-meta handlers now match all 69 and 179
words. The meta body had been omitted by the static-function build path and
masked by an absolute assignment; explicit layout ownership restores it and
the correct call relocation. Its separate inventory row raises the Init
denominator to 539. Direct assembly review also corrects the previous
classification of `func_10006380`: it uses shared live-register and stack
state and retains assembly ownership. The follow-up audit recovered Init
`__sinf` as a second compiler-generated candidate. Both it and the 954-word
`__n_CSPHandleMIDIMsg` are now completed. The following audit separated optional
custom-leaf rewrites from the handwritten/shared-register remainder. See
[Working Note 731](WORKING_NOTES/731-init-remaining-assembly-conversion-triage-20261002.md) and
[Working Note 730](WORKING_NOTES/730-init-meta-handler-layout-and-assembly-provenance-correction-20261002.md).

The Game resource-descriptor chain callback `func_15133FD8` now matches its
complete 38-word slot. It walks the counted eight-byte descriptor array and
threads `func_15133EEC`'s display-list result through each entry. Three guarded
words normalize one commutative operand order and two independent scheduling
slots. See
[Working Note 727](WORKING_NOTES/727-game-resource-descriptor-chain-callback-match-20261002.md).

The Game resource-table prefix offset calculator `func_1510D374` now matches
all 36 retail words directly from C. It starts at linker base `D_1A37E0` and
sums the requested unsigned-halfword lengths from `D_80091D20`; IDO emits the
retail remainder loop and four-entry unroll without guards or a profile
override. See
[Working Note 726](WORKING_NOTES/726-game-resource-table-prefix-offset-match-20261002.md).

The Game owner-ID effect payload constructor `func_150F5C08` now matches all
36 retail words directly from C. It recovers the four-argument contract,
12-byte owner/ID payload, object allocation, and conditional payload copy
without guards or a profile override. The aggregate figures above already
included this live-tree match in the preceding measurement. See
[Working Note 725](WORKING_NOTES/725-game-owner-id-effect-payload-constructor-match-20261002.md).

The Game effect payload constructor `func_150F4D5C` now matches all 36 retail
words directly from C. It recovers the fixed five-argument contract, typed
12-byte payload, effect allocation, and conditional payload copy without
guards or a profile override. See
[Working Note 724](WORKING_NOTES/724-game-effect-payload-constructor-match-20261002.md).

The Game actor water-state flag transition `func_150DF820` now matches its
complete 40-word slot. It retains the staged actor-flag writes, tests the
attached actor's `in_water` byte, publishes the 750-unit state value, and
dispatches the dry-state transition when that value is already active.
Sixteen guarded words normalize one closed integer-register allocation chain.
See
[Working Note 723](WORKING_NOTES/723-game-actor-water-state-flag-transition-match-20261002.md).

The Game selector/vector output initializer `func_150B060C` now matches all
41 retail words directly from C. It stores the selector lookup, returns zero
on failure, and on success publishes two constants plus three converted
signed-halfword coordinates. No guards or profile override are required. See
[Working Note 722](WORKING_NOTES/722-game-selector-vector-output-initializer-match-20261002.md).

The Game special-event mode dispatcher `func_15015F40` now matches all 31
retail words directly from C. The retained `assets/23B040.bin` data establishes
the eight special events in its 38-entry table, and an object-specific rodata
anchor preserves retail table ownership without expected-word guards. See
[Working Note 721](WORKING_NOTES/721-game-special-event-mode-dispatch-match-20261002.md).

The Game sentinel coordinate distance `func_15086BD0` now matches its complete
40-word slot. It returns zero for either `0xFF` index and otherwise computes
the Euclidean distance between signed XYZ coordinates in two 16-byte records.
Thirteen expected-word replacements and two checked insertions normalize the
closed compiler schedule and retain retail's duplicate return. See
[Working Note 720](WORKING_NOTES/720-game-sentinel-coordinate-distance-match-20261002.md).

The Game object-control reset `func_150634E4` now matches all 35 retail words
directly from C. It canonicalizes an object through `D_800CC2D0`, clears two
attached-state bytes, dispatches controls `0x1D` and `0x1E`, and clears three
object-control bytes. The corrected typed pool contract and unsigned array
index recover retail's exact division and shift/add scaling without guards.
See
[Working Note 719](WORKING_NOTES/719-game-object-control-reset-match-20261002.md).

The Game sixteen-word varargs adapter `func_15042E3C` now matches all 36
retail words directly from C. Its true varargs signature homes the incoming
register arguments and lets IDO reproduce retail's four-way-unrolled aligned
copy into a local word array. No expected-word guards or compiler-profile
override are required. See
[Working Note 718](WORKING_NOTES/718-game-sixteen-word-varargs-adapter-match-20261002.md).

The Game trailing marked-record compactor `func_1503DDD0` now matches its
complete 40-word slot. It marks a selected 20-byte record with state bit `2`
and removes trailing marked records from the active count. Correcting
`D_800C6650` to its pointer-owned table contract restores retail indexing;
sixteen expected-word guards normalize one closed compiler loop schedule. See
[Working Note 717](WORKING_NOTES/717-game-trailing-marked-record-compactor-match-20261002.md).

The Game indexed resource lazy-loader `func_1503D774` now matches all 36 retail
words. It preserves existing entries in `D_800D1C90`, loads missing resource
kind `0x11`, returns two on failure, and publishes the wrapper's first pointer
on success. Six expected-word replacements and one checked omission normalize
the closed IDO result-publication schedule. See
[Working Note 716](WORKING_NOTES/716-game-indexed-resource-lazy-loader-match-20261002.md).

The Game table-pointer relocator `func_1503D484` now matches all 35 retail
words directly from C. It walks eight-byte records through sentinel `999`,
rebases each present pointer-like word through `func_1503D438`, and publishes
the record count in `D_800C5A90`. No expected-word guards or compiler-profile
override are required. See
[Working Note 715](WORKING_NOTES/715-game-table-pointer-relocator-match-20261002.md).

The Game slot-state updater `func_1502FD70` now matches all 40 retail words.
It restores the category-`0x1D` fast path, byte-state sentinel handling,
optional-object fallback, and scaled state increase. Correcting `D_800D2040`
to its byte-array contract restores the indexed accesses; seventeen
expected-word guards normalize only IDO sentinel allocation and fallback
scheduling. See
[Working Note 714](WORKING_NOTES/714-game-slot-state-updater-match-20261002.md).

The Game configurable randomized record spawner `func_1500F9D0` now matches all
37 retail words directly from C. It shares the random type and fixed allocation
contract of `func_1500F378`, but publishes the caller's fifth argument as the
record byte at `0x30`. See
[Working Note 713](WORKING_NOTES/713-game-configurable-randomized-record-spawner-match-20261002.md).

The Game randomized record spawner `func_1500F378` now matches all 37 retail
words directly from C. It selects a random type in `10..137`, allocates the
fixed-form record, and publishes four signed halfword values plus its active
byte. No expected-word guards or compiler-profile override are required. See
[Working Note 712](WORKING_NOTES/712-game-randomized-record-spawner-match-20261002.md).

The Game paired object-state transition `func_150CF0A0` now matches all 40
retail words directly from C. Depending on the caller's low state bits, it
either dispatches the existing-state handler or gates and sets objects `0xFE`
and `0xFD` to state two. No expected-word guards or compiler-profile override
are required. See
[Working Note 711](WORKING_NOTES/711-game-paired-object-state-transition-match-20261002.md).

The Game delta-intensity limiter `func_150BA424` now matches all 39 retail
words directly from C. It rejects a negative float delta, derives and caps two
scaled intensity candidates, writes their minimum to byte field `0x5C`, and
retains retail's unsigned-byte result check. No expected-word guards or
compiler-profile override are required. See
[Working Note 710](WORKING_NOTES/710-game-delta-intensity-limiter-match-20261002.md).

The Game plane-side predicate `func_150A2E4C` now matches all 38 retail words.
It converts the signed origin coordinates, evaluates the plane expression, and
returns whether the result is non-positive. Twenty expected-word guards
normalize IDO's floating-point register allocation and instruction schedule;
the linked 152-byte span is identical to retail. See
[Working Note 709](WORKING_NOTES/709-game-plane-side-predicate-match-20261002.md).

The Game path-state routines `func_150778F0` and `func_1507A528` now match all
46 and 62 retail words directly from C. Correcting `D_800D2108` from inline
byte storage to a pointer-owned path-count table restores their missing load,
register allocation, wrapping, and directional state-update schedules without
guards. See
[Working Note 708](WORKING_NOTES/708-game-path-count-pointer-contract-match-20261002.md).

The Game randomized-step callback `func_1518F7C4` now matches all 37 retail
words. It accumulates a timestep-scaled randomized delta, performs the object
update, and optionally dispatches through the signed callback selector at
offset `0x88`. Twenty-two stale-guarded rows normalize IDO's frame, retained
record pointer, call delays, and callback branch layout. See
[Working Note 707](WORKING_NOTES/707-game-randomized-step-callback-match-20261002.md).

The Game position-sample ring recorder `func_1515CF9C` now matches all 37
retail words. It appends a 12-byte position and float sample while capacity
remains, advances and wraps the write cursor, or writes signed status `-1`
when full. Four expected-word guards normalize only the five-word reset/exit
schedule, including one inserted branch. See
[Working Note 706](WORKING_NOTES/706-game-position-sample-ring-recorder-match-20261002.md).

The Game geometry-mode command helper `func_15142B7C` now matches all 37
retail words directly from C. It emits clear/set geometry-mode commands only
for uncached bits and merges those bits into the two cached mode masks. Using
the original SDK graphics macros restores retail's cursor lifetime and store
schedule without guards or a compiler-profile override. See
[Working Note 705](WORKING_NOTES/705-game-geometry-mode-command-helper-match-20261002.md).

The Game global-position query `func_150FCF1C` now matches all 37 retail words
from recovered C. A null coordinate source returns `1.0f`; otherwise it
converts three signed halfwords to a float vector and forwards that vector,
two fixed full-width parameters, and `D_800A1F2C` to `func_15165BB0`. Four
expected-word guards normalize only IDO's persistent local-vector stack
offset. See
[Working Note 704](WORKING_NOTES/704-game-global-position-query-match-20261002.md).

The Game scaled indexed-global updater `func_1509DF20` now matches all 37
retail words directly from C. After its event-state and global-mode gates, it
scales the event value by `1/65536`, writes the result to two indexed float
tables, and marks the corresponding status byte. Retaining the repeated event
reads reproduces the complete leaf schedule without guards. See
[Working Note 703](WORKING_NOTES/703-game-scaled-indexed-global-updater-match-20261002.md).

The Game payload-record initializer `func_1518BCD0` now matches all 36 retail
words directly from C. It allocates a selector-scoped record, copies the
caller’s 0x1C-byte payload into offset `0x10`, and initializes two independent
five-bit random fields. The recovered byte-sized selector contract and direct
null-return path reproduce the complete allocation schedule without guards.
See
[Working Note 702](WORKING_NOTES/702-game-payload-record-initializer-match-20261002.md).

The Game color-driver callbacks `func_150D149C` and `func_150D1B40` now match
their complete 37- and 36-word slots directly from C. Each advances three
float fields through `func_151467A4` with its own fixed ranges and then
publishes the truncated first component with two retained global channels.
An explicit derived pointer and the retail full-width integer publisher
contract recover both layouts without guards. See
[Working Note 701](WORKING_NOTES/701-game-color-driver-callback-family-match-20261002.md).

The Game script-result flag callback `func_150C7350` now matches its complete
36-word slot directly from C. It applies the base `0x80004000` flags, invokes
the six-argument script query, and sets or clears bit `0x00400000` from the
result. The direct early-return form reproduces the branch-likely layout and
trailing padding word without guards. See
[Working Note 700](WORKING_NOTES/700-game-script-result-flag-callback-match-20261002.md).

The Game randomized event-descriptor builder `func_150FFC3C` now matches all
35 retail words directly from C. When the nested owner exists, it constructs
the seven-byte duration, variant, one-hot mask, and terminator record before
submitting it through `func_151D8868`. The semantic byte-array form reproduces
the complete branch and call schedule without guards. See
[Working Note 699](WORKING_NOTES/699-game-randomized-event-descriptor-match-20261002.md).

The Game vector-argument forwarding wrapper `func_150E3340` now matches all
35 retail words directly from C. It duplicates a three-word vector into the
first six callee arguments, supplies the fixed mode and scale, forwards a
three-float position, and preserves the final word and signed-halfword
arguments. The direct call expression recovers the complete retail schedule
without guards. See
[Working Note 698](WORKING_NOTES/698-game-vector-argument-forwarder-match-20261002.md).

The Game timer/position updater `func_150CBA30` now matches all 35 retail words
directly from C. It decrements the signed timer, applies its scaled motion to
two position fields while the timer remains positive, and conditionally lowers
the state byte from a shifted signed value. Testing the reloaded timer directly
preserves retail's separate register lifetimes without guards. See
[Working Note 697](WORKING_NOTES/697-game-timer-position-byte-clamp-match-20261002.md).

The Game resource-teardown finalizer `func_15080C64` now matches all 36 retail
words directly from C. It gates teardown on the active flag and record state,
invokes `func_15080BE8`, sets the non-`0x29`/non-`0x2E` global flag, and
completes and clears an optional pending record. Direct global indexing
recovers retail's temporary allocation without guards. See
[Working Note 696](WORKING_NOTES/696-game-resource-teardown-finalizer-match-20261002.md).

The Game attachment-state transition callback `func_15074664` now matches all
35 retail words directly from C. It detects state-one entry and exit, invokes
`func_10011FDC` with `5` or `0`, reloads the potentially changed attachment,
and writes the requested state byte. An unsigned state comparison and one
shared final assignment reduce the former 37-word overflow to retail's exact
slot without guards. See
[Working Note 695](WORKING_NOTES/695-game-attachment-state-transition-match-20261002.md).

The Game trigonometric lookup `func_150489B0` now matches all 36 retail words.
It restores the four quadrant ranges, reflected table indexes, and signs for
the byte-angle result. Thirty-one words emit directly from C; five guarded
indexing words preserve retail's shift-before-negate schedule. Its adjacent
quarter-turn wrapper remains exact through seven stale-checked schedule words
after correcting the callee's `f32`/`u8` contract. See
[Working Note 694](WORKING_NOTES/694-game-trigonometric-lookup-match-20261002.md).

The Game timer-expiry callback `func_1503EEC0` now matches all 35 retail
words. It runs the per-entry update, subtracts the global tick count from the
signed timer while retaining the full-width result for the expiry test, stores
the truncated halfword, and dispatches the indexed callback on expiry.
Sixteen words emit directly from C; nineteen stale-checked words preserve the
retail allocation and schedule, including both global-address relocation
pairs. See
[Working Note 693](WORKING_NOTES/693-game-timer-expiry-callback-match-20261002.md).

The Game attachment-state updater `func_150333A8` now matches its complete
38-word slot. It handles the global disable mode, clears an attached object's
state byte for active attachments, and otherwise derives byte `3` from the
reference-height equality and `+300.0f` threshold tests. Thirty-one words emit
directly from C; seven stale-checked words preserve an equivalent closed
floating-branch and delay-slot store layout. See
[Working Note 692](WORKING_NOTES/692-game-attachment-state-updater-match-20261002.md).

The Game group-record activator `func_150227BC` now matches all 35 retail
words. It walks the selected 30-byte ID row, resolves each active ID through
`func_151149AC`, and sets byte `0x6E` on the returned record while re-reading
the group count. Thirty-three words emit directly from C; two stale-checked
rows normalize only the independent row-offset and index-initialization
schedule around the opening branch. See
[Working Note 691](WORKING_NOTES/691-game-group-record-activator-match-20261002.md).

The Game counted resource-owner teardown `func_151EDB58` now matches all 33
retail words directly from semantic C. It releases the auxiliary resource and
owner allocation before walking the owner's count-sized pointer array. The
frame, saved-register lifetime, branch-likely delay slots, release order, and
loop schedule require no expected-word guards or compiler-profile override.
See
[Working Note 690](WORKING_NOTES/690-game-counted-resource-owner-teardown-match-20261002.md).

The Game event-record matcher `func_151D7538` now matches its complete 35-word
slot. Selector `0x3D` compares the object's embedded word and tag byte against
the incoming record and destroys the object when either matches; other
selectors forward both embedded-field addresses through `func_15149514`.
Fourteen stale-checked rows, including one checked insertion, preserve the
retail pointer lifetime and closed compiler register allocation without
changing either call relocation. See
[Working Note 689](WORKING_NOTES/689-game-event-record-matcher-match-20261002.md).

The Game mode-offset adjuster `func_151CD224` now matches its complete 39-word
slot. It samples the object's control value, derives a scaled adjustment from
the embedded record at offset `0x70`, and applies the positive or negative
mode-specific output at offset `0x14`. Six stale-checked rows, including one
checked insertion, preserve retail's shared record-base and mode-register
allocation; the remaining arithmetic and branch schedule emit from semantic
C. See
[Working Note 688](WORKING_NOTES/688-game-mode-offset-adjuster-match-20261002.md).

The Game output-default initializer `func_151B498C` now matches all 34 retail
words. It initializes thirteen caller-provided outputs with two packed mode
words, eight `0xFF` values, one zero, and two byte selectors before returning
success. The complete function emits directly from semantic C without guards
or a compiler-profile override. See
[Working Note 687](WORKING_NOTES/687-game-output-default-initializer-match-20261002.md).

The Game threshold/intensity updater `func_151A787C` now matches all 35 retail
words. It applies two signed threshold tests, advances two halfword fields by
an elapsed-tick-scaled step, and writes timer-scaled byte outputs. Nineteen
words emit directly from semantic C; sixteen stale-checked words normalize one
commutative multiply and a closed compiler register/scheduling cycle. See
[Working Note 686](WORKING_NOTES/686-game-threshold-intensity-updater-match-20261002.md).

The Game tick-compensated damping callback `func_1519C4E4` now matches all 34
retail words. It repeats two floating-point damping updates for every elapsed
tick, then conditionally lowers the byte at offset `0x5C` from the timer and
parameter scale. The complete function emits directly from semantic C without
guards or a compiler-profile override. See
[Working Note 685](WORKING_NOTES/685-game-tick-compensated-damping-callback-match-20261002.md).

The Game clamped height-byte updater `func_1518B1D8` now matches all 35 retail
words. It derives a nonnegative byte from the smaller of a scaled object field
and half the truncated height delta, clamps each upper bound to `0xFF`, and
stores the result at offset `0x70`. Twenty-five words emit directly from
semantic C; ten stale-checked suffix words preserve retail's compiler phi
register and equivalent branch schedule. See
[Working Note 684](WORKING_NOTES/684-game-clamped-height-byte-match-20261002.md).

The Game active-row wrapper `func_1517F4D8` now matches all 35 retail words.
It returns the incoming handle for inactive timer or mode rows and otherwise
forwards the indexed three-byte parameter row to `func_1517F08C`. The complete
routine emits directly from semantic C without guards or profile overrides.
See [Working Note 683](WORKING_NOTES/683-game-active-row-wrapper-match-20261002.md).

The Game mode dispatcher `func_15170EC4` now matches all 34 retail words after
restoring its mode-2 and mode-`0x10` parameter sets and low-byte argument
forwarding. Its sparse switch, calls, and shared epilogue emit directly from
semantic C without guards or profile overrides. See
[Working Note 682](WORKING_NOTES/682-game-mode-dispatcher-match-20261002.md).

The Game packed two-axis integrator `func_1516F864` now matches all 34 retail
words after restoring its signed high-byte and unsigned low-byte velocity
loads, global time-scale multiplication, and packed position accumulation.
Thirty-two stale-checked words preserve only compiler register allocation;
the arithmetic and instruction schedule already match. See
[Working Note 681](WORKING_NOTES/681-game-packed-two-axis-integrator-match-20261002.md).

The Game resource-release loops `func_1514795C`, `func_151571C4`, and
`func_15158A20` now match all 33 retail words apiece after restoring their
inclusive indexed scans, conditional frees, and trailing-slot releases. The
Game height/state predicate `func_15159084` also matches all 39 words; one
stale-checked word preserves retail's commutative floating-equality operand
order. See
[Working Note 680](WORKING_NOTES/680-game-resource-release-family-and-height-predicate-match-20261002.md).

The Game resource-release loop `func_151325C8` now matches all 33 retail
words after restoring its inclusive indexed scan, conditional frees, and
trailing-slot release. The Game vertex rotation helper `func_151436B4` also
matches all 34 words after making the fourth trigonometric result explicit so
IDO retains retail's call-before-store schedule. Both emit directly from
semantic C without expected-word guards or profile overrides. See
[Working Note 679](WORKING_NOTES/679-game-resource-release-and-vertex-rotation-match-20261002.md).

The Game angular integrators `func_1511515C` and `func_151151FC` now match all
40 retail words directly from semantic C. The related displacement extender
`func_15115EDC` matches all 35 words after restoring its position snapshot,
motion update, and record-type-`0x4B` extrapolation. One stale-checked word
preserves the retail cross-declaration record-pointer register. See
[Working Note 678](WORKING_NOTES/678-game-angular-motion-update-family-match-20261002.md).

The Game render-parameter wrappers `func_1510E7A4`, `func_1510E82C`, and
`func_1510E8BC` now match all 34, 36, and 37 retail words. Their recovered
word-accurate signatures preserve raw coordinate payloads, mixed stack load
widths, default bounds, and the final mode argument while adapting calls to
`func_1510E950`. All three emit directly from semantic C without expected-word
guards or compiler-profile overrides. See
[Working Note 677](WORKING_NOTES/677-game-render-parameter-wrapper-family-match-20261002.md).

The Game owner-event callback `func_15100230` now matches all 35 retail words.
It destroys the object when event `0x48` matches either owner identity field
and otherwise forwards the event with the embedded owner record. A
function-specific `-O1 -g3` object preserves its caller-spilled callback ABI;
28 stale-checked words normalize the closed instruction schedule and both call
relocations. See
[Working Note 676](WORKING_NOTES/676-game-owner-event-callback-match-20261002.md).

The Game state-flag updater `func_150F9A20` now matches its complete 36-word
slot directly from C. It queries condition `0x4025`, selects mutually exclusive
`0x80` and `0x08` state flags, and writes either `85.0f` or zero to field
`0x190`. No expected-word guards are required. See
[Working Note 675](WORKING_NOTES/675-game-condition-state-flag-match-20261002.md).

The Game command-row loop `func_150413FC` now matches all 33 retail words. It
walks a zero-terminated command-byte stream, advances its associated row by
eight bytes per command, translates each command through `func_15041480`, and
threads the result through `func_15041508`. The complete loop body and frame
emit from semantic C; nine stale-checked words normalize only the independent
prologue schedule. See
[Working Note 674](WORKING_NOTES/674-game-command-row-loop-match-20261002.md).

The Game object teardown `func_15106E78` now matches all 32 retail words
directly from C. It restores the type-indexed destructor callback, releases
the two optional child objects, and tears down the embedded record. The two
adjacent teardown-and-finalize wrappers now carry the recovered pointer ABI;
all three routines remain byte-exact without guarded words. See
[Working Note 673](WORKING_NOTES/673-game-object-teardown-match-20261002.md).

The Init sound-event dispatcher `_n_handleEvent` now matches all 1,363 retail
words, completing the Init code-function matcher queue at 487 / 487. It
restores resource resolution, voice allocation and startup, envelope timing,
pan/volume/pitch/effect updates, retry scheduling, cleanup, channel-volume
events, and child-sound dispatch. Its typed 1,241-word body is expanded by 122
checked insertions; 87 rows verify compact-object relocations. The independent
5,452-byte comparison is exact with SHA-256
`583662222304bf87a3b24bc9495055b930b2076e36ecb37183fa5612a36b8525`.
The separate shifted Init-rodata issue at absolute dispatcher table
`jtbl_8002C708_init` remains a data-layout/runtime qualification task. See
[Working Note 672](WORKING_NOTES/672-init-sound-event-dispatcher-match-20261002.md).

The Init compact-sequence voice handler `__n_CSPVoiceHandler` now matches all
684 retail words. It restores SDK event dispatch, envelope and oscillator
updates, MIDI/meta forwarding, Rare's mix and control events, restartable
play/stop behavior, voice cleanup, and channel-mask transitions. Its semantic
body compiles to 667 words; 667 stale-checked rows preserve retail's closed
layout, including 17 insertions and 45 relocation-aware rows. See
[Working Note 671](WORKING_NOTES/671-init-compact-sequence-voice-handler-match-20261001.md).

The Init path-relative spatial query `func_1000A750` now matches all 580
retail words. It restores nearest-node selection, adjacent-segment choice,
point-to-segment projection, endpoint clamping, and the final handoff to the
already matched attenuation/pan calculator. Its readable 404-word compiler
body is expanded to retail's unrolled layout by 401 stale-checked rows,
including 176 insertions and 19 relocation-aware rows. See
[Working Note 670](WORKING_NOTES/670-init-path-projection-query-match-20261001.md).

The Init 64DD interrupt handler `__osLeoInterrupt` now matches its complete
441-word retail slot. It restores the disk-presence gate, DMA-busy recovery,
mechanical and buffer-manager interrupt handling, read/write sector transfer,
C1/C2 error bookkeeping, track transitions, and completion notification. The
compiler emits 440 words; 323 match directly, 117 stale-checked rows normalize
the closed allocation and relocation layout, and the layout tool supplies the
retail trailing `nop`. See
[Working Note 669](WORKING_NOTES/669-init-64dd-interrupt-handler-match-20261001.md).

The Init conversion helper `func_10002718` now matches its complete 422-word
retail span. It restores character, signed/unsigned integer, floating-point,
pointer, string, `%n`, percent, and fallback conversions using the shared SDK
formatter descriptor. The 338-word compact body emits 42 retail words
directly; 296 stale-checked rows include 87 insertions, three omissions, and
four relocation-aware rows. See
[Working Note 668](WORKING_NOTES/668-init-conversion-helper-match-20261001.md).

The Init formatted-output dispatcher `func_100020D0` now matches its complete
402-word retail span. It restores literal-run output, format-flag parsing,
width and precision arguments, length modifiers, conversion dispatch, and
chunked field padding through the caller's output callback. The 361-word
compact body emits 95 retail words directly; 266 stale-checked rows include
44 insertions, three omissions, and ten relocation-aware rows. See
[Working Note 667](WORKING_NOTES/667-init-formatted-output-dispatcher-match-20261001.md).

The Init numeric formatter `func_10001AA8` now matches its complete 370-word
retail span. It restores fixed, scientific, and general-format placement,
precision trimming, decimal insertion, exponent emission, and width padding.
The 365-word compact body emits 87 retail words directly; 278 stale-checked
rows include 13 insertions, eight omissions, and three relocation-aware rows.
See
[Working Note 666](WORKING_NOTES/666-init-numeric-formatter-match-20261001.md).

The Init sound-record updater `func_10011624` now matches its complete
357-word retail span. It restores bounded record traversal, stale-handle
release, listener-relative volume and pan, callback dispatch, voice creation,
incremental parameter updates, and distance-driven pitch smoothing. The
semantic compact body emits 64 retail words directly; 293 stale-checked rows
include one insertion and 20 relocation-aware rows. See
[Working Note 665](WORKING_NOTES/665-init-sound-record-updater-match-20261001.md).

The Init instrument channel loader `func_1001B7D0` now matches its complete
345-word retail span directly from C. It restores resource resolution and
release, per-sound relocation, envelope and instrument-default transfer,
missing-resource state, and selected-program tracking. Its exact retail size,
stack slots, repeated channel indexing, and all relocations emit without
guards. See
[Working Note 664](WORKING_NOTES/664-init-instrument-channel-loader-match-20261001.md).

The Init audio-environment controller `func_10012020` now matches its complete
336-word retail span. It restores five environment modes, transition-state
ramps, oscillator-driven pitch targets, master gain, and two-channel parameter
updates. The generated switch table is retargeted to retail rodata; 225
stale-checked rows include one padding insertion and 103 relocation-aware
rows. See
[Working Note 663](WORKING_NOTES/663-init-audio-environment-controller-match-20261001.md).

The Init sequence transition dispatcher `func_1000D96C` now matches its
complete 300-word retail span. It restores existing-record teardown, child
allocation and attachment, mode-specific fades, shared-channel handling, and
record reinitialization. The semantic compact body emits 73 words directly;
220 stale-checked rows include seven schedule insertions and 20
relocation-aware rows. See
[Working Note 662](WORKING_NOTES/662-init-sequence-transition-dispatcher-match-20261001.md).

The Init SDK floating-point formatter `func_10001550` now matches its complete
296-word retail span. It restores `%f`, `%e`, `%E`, `%g`, and `%G` conversion,
including special values, decimal scaling, digit generation, and rounding.
The semantic C preserves retail's exact extent and control flow; 176
stale-checked rows, including 10 relocation-aware rows, normalize the closed
IDO allocation and frame-layout difference. See
[Working Note 661](WORKING_NOTES/661-init-sdk-float-formatter-match-20261001.md).

The Init audio channel updater `func_1000D2F8` now matches its complete
280-word retail span. It restores pending-sequence changes, child-channel
promotion and teardown, callback dispatch, volume ramps, and linked-channel
validation. The semantic C has retail's exact extent and control-flow order;
113 stale-checked words normalize IDO allocation and scheduling. The corrected
channel-index ABI also keeps its 133-word caller `func_1000D758` byte-exact
with two scoped guards. See
[Working Note 660](WORKING_NOTES/660-init-audio-channel-updater-match-20261001.md).

The Init audio subframe builder `func_1001FB40` now matches its complete
296-word retail span directly from C. It restores optional opening-command
interception, per-bus filter dispatch, mixer selection, effect-state refresh,
and the ADPCM and pole-filter command stream. Recovered SDK audio macros and
the original dual loop-increment form emit every retail word and relocation
without guards. See
[Working Note 659](WORKING_NOTES/659-init-audio-subframe-builder-match-20261001.md).

The Init channel event and timer updater `func_1000CEAC` now matches its
complete 275-word retail span. It drains the selected channel queue, expands
event masks into sixteen timer slots, applies the four event modes, updates
the active voice state, and decrements paired timers with the current frame
step. The semantic C has the exact retail extent; 230 stale-checked rows,
including 41 relocation-aware rows, normalize IDO's closed allocation and
layout differences. See
[Working Note 658](WORKING_NOTES/658-init-channel-event-timer-update-match-20261001.md).

The Init audio-runtime bootstrap `func_10008F90` now matches its complete
271-word retail span. It installs audio callbacks, derives frame sample counts,
initializes the synthesis parameter areas and record pools, allocates command
buffers, creates four queues, and starts the audio thread. A scoped
macro-enabled function object preserves the already matched neighboring
routines; 139 checked rows include eight insertions and 45 relocation-aware
rows. See
[Working Note 657](WORKING_NOTES/657-init-audio-runtime-bootstrap-match-20261001.md).

The Init bidirectional heap allocator `func_10003C6C` now matches its complete
258-word retail span. It applies allocation-class alignment, searches from
either end of the free list, splits or consumes the selected block, repairs
both physical and free-list links, and refreshes the largest-free-block record.
The semantic C has the exact retail extent; 216 stale-checked rows, including
42 relocation-aware rows, normalize IDO's closed allocation and scheduling
differences. See
[Working Note 656](WORKING_NOTES/656-init-bidirectional-heap-allocator-match-20261001.md).

The Init packed spatial-audio state updater `func_1000BF60` now matches its
complete 252-word retail span. It starts sound `0x22`, performs three spatial
queries, updates the changed volume and position channels, handles two mode
transitions, and returns the refreshed packed state. The semantic C emits 250
words with retail's `0x60` frame; 111 stale-checked rows, including two checked
insertions and two relocation-aware rows, normalize IDO's allocation and
scheduling. See
[Working Note 655](WORKING_NOTES/655-init-packed-spatial-audio-state-match-20261001.md).

The Init scheduler and render thread `func_100049E0` now matches its complete
244-word retail span. It restores the seven-class message loop, registered
client notifications, delayed task timer, SP yield/completion paths, pending
graphics-task dispatch, idle render advance, and guarded controller reads.
The semantic C emits 239 words; 150 stale-checked rows, including five checked
insertions and 44 relocation-aware rows, normalize IDO's frame, allocation,
switch, and unreachable epilogue schedule. See
[Working Note 654](WORKING_NOTES/654-init-scheduler-render-thread-match-20261001.md).

The Init audio-library bootstrap `func_10008180` now matches its complete
214-word retail span. It initializes the audio heap and synthesizer, loads and
relocates the bank and sequence metadata, normalizes all 150 sequence lengths,
creates three sequence players, and configures the sound player. The semantic
C emits 213 words; 64 stale-checked rows, including one checked insertion and
10 relocation-aware moves, normalize IDO's frame, local, loop, and player
setup allocation. See
[Working Note 653](WORKING_NOTES/653-init-audio-library-bootstrap-match-20261001.md).

The Init `bcopy` slot is restored to its original handwritten assembly instead
of the non-matching simplified C substitute. Direct comparison confirms all
196 words, including the optimized overlap-safe forward and backward copy
paths and three padding words, match retail. Because the authoritative matcher
tracks C rows only, this moves one function and 784 bytes from the C totals to
raw assembly without changing the byte-exact C numerator. See
[Working Note 652](WORKING_NOTES/652-init-handwritten-bcopy-restoration-20261001.md).

The Init resource-request manager `func_10009CBC` now matches its complete
208-word retail span. It resolves encoded resource requests, acquires or
evicts manager nodes, allocates and clears rounded buffers, performs cache
maintenance, submits PI DMA, and handles existing resource references. See
[Working Note 651](WORKING_NOTES/651-init-resource-request-manager-match-20261001.md).

The Init spatial attenuation and pan calculator `func_1000A420` now matches its
complete 204-word retail span. It selects planar or three-axis distance,
computes clamped attenuation, derives listener-relative pan when requested,
and writes the optional raw-distance result. See
[Working Note 650](WORKING_NOTES/650-init-spatial-attenuation-pan-match-20261001.md).

The Init resource-completion manager `func_1000A03C` now matches its complete
195-word retail span. It drains completed resource messages, moves matching
nodes between manager lists, relocates resource tables, releases idle entries,
and services the deferred cleanup flag. See
[Working Note 649](WORKING_NOTES/649-init-resource-completion-manager-match-20261001.md).

The Init audio-event parameter updater `func_1000F85C` now matches its complete
48-word retail span. It validates the sound handle, converts pitch cents to
the event's floating-point bit representation, normalizes selector `0x11`,
and dispatches to the active sound state. See
[Working Note 648](WORKING_NOTES/648-init-audio-event-parameter-update-match-20261001.md).

The Init handle-record lookup `func_1000FEF0` now matches its complete 40-word
retail span. Its no-unroll profile is selected per function so neighboring
matches retain their established object profile. See
[Working Note 647](WORKING_NOTES/647-init-handle-record-lookup-match-20261001.md).

The Init active-record lookup `func_1000FF90` now matches its complete 35-word
retail span. It scans the active 0x30-byte record array with two independently
optional selectors and rejects disabled records. See
[Working Note 646](WORKING_NOTES/646-init-active-record-lookup-match-20261001.md).

The Init listener/audio update `func_10011BB8` now matches its complete
180-word retail span. It restores listener snapshots, active audio-record
compaction, and the two-channel transition update. See
[Working Note 645](WORKING_NOTES/645-init-listener-audio-update-match-20261001.md).

The Init PRENMI shutdown thread `func_100052A0` now matches its complete
180-word retail span. It restores thread shutdown, controller-motor cleanup,
the two timed waits, cache writeback, and the terminal park loop. See
[Working Note 644](WORKING_NOTES/644-init-prenmi-shutdown-thread-match-20261001.md).

The Init packed audio-state updater `func_1000C530` now matches its complete
174-word retail span. It restores queued state transitions, sound-slot
parameter updates, transition expiry, and the high-byte fade trigger. See
[Working Note 643](WORKING_NOTES/643-init-packed-audio-state-updater-match-20261001.md).

The Init integer formatter `_Litob` now matches its complete 168-word retail
span. It restores signed magnitude handling, octal/decimal/hex digit emission,
precision zero-fill, and field-width padding. See
[Working Note 642](WORKING_NOTES/642-init-integer-formatter-match-20261001.md).

The Init common system initializer `__osInitialize_common` now matches its
complete 168-word retail span. It restores CPU/FPU setup, PIF initialization,
the four exception vectors, cache and RDB setup, clock-rate adjustment, the
cold-reset NMI clear, and the 64DD Leo interrupt probe. See
[Working Note 641](WORKING_NOTES/641-init-common-system-initializer-match-20261001.md).

The Init sound-slot dispatcher `func_10010BE8` now matches its complete
164-word retail span. It validates and reuses caller handles, scans the
16-entry sound table for an available unreserved slot, advances the slot
generation, applies the global effect mix, converts pitch cents, and starts
the selected bank sound. See
[Working Note 640](WORKING_NOTES/640-init-sound-slot-dispatcher-match-20261001.md).

The Init boot loader `func_10001194` now matches its complete 163-word retail
span. It restores memory clearing, framebuffer setup, compressed Game-image
loading, relocation-table decoding, and final subsystem startup. See
[Working Note 639](WORKING_NOTES/639-init-boot-loader-thread-match-20261001.md).

The Init music-control callback `func_1000BCBC` now matches its complete
169-word retail span. It restores initial channel setup plus the scene-gated
distance and event-level updates; 70 stale-checked rows normalize IDO's two
float-to-unsigned conversion schedules. See
[Working Note 638](WORKING_NOTES/638-init-music-control-callback-match-20261001.md).

The Init PI device-manager thread `func_10002E50` now matches its complete
148-word retail span directly from semantic C. The recovery includes the
custom direct-PI ownership handshake, the canonical libultra DMA/EDMA and
loopback dispatch order, and the retail jump table. See
[Working Note 637](WORKING_NOTES/637-init-pi-device-manager-loop-match-20261001.md).

The full debugger inventory is complete: all 181 C-classified tracked rows are
linked byte-exact, and the sole remaining assembly row, the original
handwritten 40-word CP0/TLB routine `func_16003650`, independently matches all
40 retail words. It remains assembly by design because IDO C cannot emit its
`mtc0`, `tlbr`, and `mfc0` instruction sequence. Thus all 182 debugger rows
are accounted for and exact; 181 / 181 is only the C-matcher denominator.

The percentage increase from the old July matching snapshot remains primarily
denominator driven: the exact count is now 3,040, while
508 functions moved from C back to assembly. The paired event-swap pass added
two byte-exact functions and the debugger rectangle-fill, float-formatter,
glyph-blitter, `_Printf`, context-display, memory-view, and debugger-main-loop
passes added one each after the restoration baseline. The subsequent game
pass completed `func_15135480`, the final four one-difference game rows, and
the subsequent small game queue through `func_1509D054`; `func_150A7A00` was
then correctly restored from a false C placeholder to its original trampoline,
followed by handwritten PRNG seed setter `func_150ADACC`, the guarded
scalar-temporary match for `func_150BDB3C`, the guarded set-bit temporary
match for `func_150F33B0`, and the relocation-preserving opening-load match
for `func_151254F4`; `func_1515FB70` was then restored from a false C model
to its original nine-word assembly extent, followed by the guarded register
normalization for `func_1505841C`, indexed-slot clear `func_150F02A0`, and
call-ABI correction for `func_151B2FA0`, and byte-offset expression recovery
for `func_150770E4`.
Handwritten byte-fill loop `func_150A7770` is restored from its false C model
to the original eight-word assembly extent. Packed fixed-point reader
`func_1515F008` is byte-exact through guarded pointer/value register
normalization. Packed-byte scalers `func_1516F8EC` and `func_1516F91C` are
byte-exact through symmetric guarded temporary-register normalization, while
`func_1516F984` matches from a source-level scaled-field lifetime.
Viewport setup `func_15019BB8` is byte-exact through guarded frame-size and
relocation-preserving address-register normalization.
Sound-command wrapper `func_1509F6B0` is byte-exact through guarded incoming
argument spill/reload scheduling.
`func_150C7930` is restored to its original 14-word assembly ownership because
IDO eliminates retail's dead `temp_v0 + 0x1E0` expression.
`func_150CDB6C` is byte-exact through guarded destination-pointer
materialization and schedule normalization.
`func_15108B80` is byte-exact through guarded terminal/countdown register
lifetimes and commutative pointer-add operand order.
`func_1513A594` is byte-exact after correcting its forwarded byte ABI,
retaining the post-call field read, and guarding the empty branch shape.
`func_1515F0AC` is byte-exact from its signed float clamp C body plus three
guarded scheduling entries that move the independent lower-clamp `lui` into
the first FP comparison slot and omit IDO's resulting hazard `nop`.
`func_1516706C` is byte-exact after recovering its post-tested callback-table
loop, distinct `D_8008CB70` end symbol, and two guarded low-half address words.
`func_15168A9C` is byte-exact directly from typed link removal plus explicit
row/index byte lifetimes; no guarded retail words are needed.
`func_15179AB8` is byte-exact directly from a backward active-object scan that
sets flag `0x2` on the first eligible object.
`func_15194AB4` is byte-exact directly from C after correcting its return type
to `void` and expressing the two state mappings as a `switch` with a default
selector assignment after the object-flag store.
`func_151957B0` is byte-exact directly from a nonempty-first doubly linked-list
tail insertion that preserves retail's repeated old-tail load. Its former
trailing return pair is now correctly tracked as independent no-op
`func_15195824`, which is also byte-exact directly from an empty `void` body.
`func_151A8A20` is byte-exact directly from a typed callback-table dispatcher
that clamps selector bytes above the three-entry table to slot zero.
`func_151A8F1C` is byte-exact directly from a five-argument coordinate-transform
wrapper followed by a single float-component copy.
`func_151AA17C` is byte-exact from its recovered two-call stack-record dispatch
and final object callback, plus ten guarded scheduling and local-slot words;
all call relocations and delay slots already matched directly.
Structural twin `func_151AA210` is independently byte-exact from the same C
shape and ten separately guarded words across its own retail span.
`func_151CF844` is byte-exact directly from a null-gated five-argument record
forwarder; its branch-likely return path and call delay slot need no guards.
`func_151423D8` is byte-exact through symmetric guarded quadrant and table-index
register normalization.
`func_15155EF8` is byte-exact through guarded outer/child pointer register
lifetimes while preserving all three call relocations.
Adjacent `func_151D7770` and `func_151D779C` are byte-exact from source-level
child/destination pointer ordering and retail's wider byte-mask spelling.
`func_1509F248` is byte-exact from an explicit unsigned-halfword narrowing
that restores retail's high-half extraction and call-delay-slot schedule.
`func_150C5EFC` is restored to its original 17-word assembly extent because
IDO removes retail's otherwise dead child-pointer update before the call.
Its structural twin `func_150C682C` is restored for the same ownership reason,
with its distinct child-field clear preserved.
`func_150EA904` is byte-exact through eight guarded, relocation-preserving
base/index and byte-update register lifetime words.
`func_1515D480` is byte-exact through eight guarded frame-size and local-slot
words while preserving both call relocations.
`func_151AB180`, the `+0x70` member of the dead child-pointer family, is
restored to its original 17-word assembly extent.
`func_151EF610` is restored to its original 12-word assembly extent because
IDO retains one global address register, while retail uses independent load
and store relocations and places the store in the return delay slot.
`func_150771F0` is byte-exact through nine guarded argument-load and selector
schedule words, including eight explicitly declared relocation moves.
`func_15080200` is byte-exact from a source-level chained assignment that
restores retail's two retained global-address registers and three-store order.
`func_1510E634` is byte-exact from the typed `Gfx` writer idiom plus a guarded
two-word expansion that restores the original and advanced cursor lifetimes.
`func_1512D6B0` is byte-exact through nine guarded record-index, global-base,
and 176-byte stride temporary-register words.
`func_15166FD8` is byte-exact through the same guarded display-list cursor
expansion pattern, independently verified across its 14-word slot.
`func_15196330` is byte-exact through nine guarded pointer/selector register
words; its frame, control flow, callbacks, and relocations were already exact.
Structural twin `func_151963B4` is independently byte-exact through the same
nine guarded register words and its distinct final-call relocation.
Adjacent state-clear callbacks `func_1519F108` and `func_1519F168` are
independently byte-exact across 24 words each. Their recovered C is shared
apart from the final callback; symmetric guarded scheduling restores retail's
derived field-base lifetime and branch targets.
`func_151A09B4` is byte-exact directly from C after recovering its byte-flag
gate, child pointer or selector-byte match, and two-call teardown path.
`func_151B4E4C` is byte-exact directly from the established three-float vector
wrapper idiom, forwarding three more floats and two actor record bytes.
`func_151EFF94` is byte-exact directly from its two-fixed-argument variadic
formatting wrapper, including successful-output null termination.
`func_15044CE4` is byte-exact from its position/scale initializer plus seven
guarded register-lifetime words.
`func_151B3040` is byte-exact directly from C after recovering its two calls
over adjacent embedded records. An explicit `arg0 + 0x150` base and a volatile
byte argument reproduce retail's stack lifetime and second-call address reuse;
no guarded retail words are needed.
`func_151C9ED4` is byte-exact after recovering its event-`0x21` broadcast to
four handlers and final `D_8008CD00` clear. Four guarded frame and local-slot
words preserve retail's 40-byte allocation while the call schedule, saved
register lifetime, relocations, and behavior come directly from C.
`func_151D13E0` is byte-exact directly from C after recovering its null-gated
owned-object teardown, three separate flag updates, linked-record clear, and
owner-slot release. Retail's repeated slot loads and complete leaf schedule
need no guarded words.
`func_151E4E00` is byte-exact directly from C after recovering its state reset,
mode-3 transition, and five-argument dispatch for event `0x1D`. Its first
global clear naturally occupies the preceding call's delay slot; no guarded
words are needed.
`func_10012588` is byte-exact after the clean full regeneration removed its
stale address-drift classification. No address-drift rows remain.
`func_15155780` is byte-exact after recovering its six-argument record
allocation, null return, four field initializers, and notification call. Eight
guarded words normalize only the independent success-path schedule; see
[Working Note 485](WORKING_NOTES/485-game-record-allocator-initializer-match-20260929.md).
`func_151557FC` is byte-exact directly from C after recovering its find-or-create
path, float update, and actor-table-dependent state/timer initialization; see
[Working Note 486](WORKING_NOTES/486-game-record-find-or-create-update-match-20260929.md).
`func_1515FF74` is byte-exact directly from C after recovering its allocation
arguments, explicit null return, and eight-byte payload copy; see
[Working Note 487](WORKING_NOTES/487-game-small-record-copy-allocator-match-20260929.md).
`func_150C7D7C` is byte-exact directly from C after recovering its source
position query and three offset, truncated halfword outputs. Its 32
instructions and one trailing retail padding word match without guards; see
[Working Note 488](WORKING_NOTES/488-game-offset-position-halfword-writer-match-20260929.md).
`guMtxIdentF` is byte-exact after recovering its unrolled mixed float/integer
identity-matrix stores and O3 profile. Five guarded words normalize only the
compiler's equivalent diagonal-constant FP register; see
[Working Note 489](WORKING_NOTES/489-game-identity-matrix-initializer-match-20260929.md).
Adjacent impact-effect dispatchers `func_15194320` and `func_15194394` are
byte-exact directly from grouped switches over source states zero through
four. Their separate five-entry jump tables retain retail rodata ownership;
see
[Working Note 490](WORKING_NOTES/490-game-impact-effect-dispatch-pair-match-20260929.md).
Init arena-anchor initializer `func_10003BD0` is byte-exact across all 28
words after recovering its repeated global-head access shape. Twenty
stale-checked guards preserve one closed compiler schedule, including the
single inserted low-half word for retail's retained final-anchor pointer; see
[Working Note 491](WORKING_NOTES/491-init-arena-anchor-initializer-match-20260929.md).
Handwritten libultra cache routines `osInvalICache` and `osWritebackDCache`
are restored from empty C placeholders to their original 32-word assembly
bodies. Both complete 128-byte spans match retail; see
[Working Note 492](WORKING_NOTES/492-init-handwritten-cache-routine-restoration-20260929.md).
Init record-key updater `func_100100E0` is byte-exact across all 29 words
after recovering its nonempty pointer-range scan. Twenty stale-checked guards
normalize only one closed `$v0`/`$v1` allocation cycle; see
[Working Note 493](WORKING_NOTES/493-init-record-key-updater-match-20260929.md).
Game water-buoyancy response `func_15058F24` is byte-exact across all 135
words after preserving the original blend factor for the initial velocity
scale. Thirty stale-checked guards normalize only IDO scheduling and temporary
register allocation; see
[Working Note 494](WORKING_NOTES/494-game-water-buoyancy-response-match-20260929.md).
Init sound-handle lookup `func_1000F4D8` is byte-exact across all 36 words
directly from C after recovering its one-time in-place identifier mask; see
[Working Note 495](WORKING_NOTES/495-init-sound-handle-lookup-match-20260929.md).
Game audio DMA reader `func_151F3C4C` is byte-exact across all 75 words after
reusing its callback-state local for the DMA result. Eleven stale-checked
guards normalize two closed compiler register-allocation cycles; see
[Working Note 496](WORKING_NOTES/496-game-audio-dma-reader-match-20260929.md).
Game byte-state reset `func_15010600` is byte-exact across all 32 words after
recovering six scalar clears and a paired 12-byte array loop. Four
relocation-aware stale checks normalize only one independent scheduling
window; see
[Working Note 497](WORKING_NOTES/497-game-byte-state-reset-match-20260929.md).
Game height-gated action selector `func_1506DC10` is byte-exact across all 37
words after removing a false callback parameter. One stale-checked guard
preserves retail's commutative floating-equality operand order; see
[Working Note 498](WORKING_NOTES/498-game-height-gated-action-selector-match-20260929.md).
Game path-node spawn randomizer `func_15079790` is byte-exact across all 60
words after restoring separate actor/path-table lookups for its X and Z
updates. The complete routine emits directly from C with no guards; see
[Working Note 499](WORKING_NOTES/499-game-path-node-spawn-randomizer-match-20260929.md).
Game opcode-record byte counter `func_150027F8` is byte-exact across all 32
words after restoring its integer-address ABI and repeated eight-byte indexed
loads. Fourteen stale-checked guards normalize only the closed `v0`/`a1`
record-index/opcode allocation cycle; see
[Working Note 500](WORKING_NOTES/500-game-opcode-record-byte-counter-match-20260929.md).
Game six-word actor query `func_151420F8` is byte-exact across all 34 words
after recovering its aggregate template copy, signed actor-index division, and
explicit success branch. The complete function emits directly from C with no
guards; see
[Working Note 501](WORKING_NOTES/501-game-six-word-actor-query-match-20260929.md).
Game actor-slot selector `func_1503F964` is byte-exact across all 35 words
after replacing its false zero-return placeholder with the wrapped 25-slot
actor scan. Fourteen relocation-aware stale checks normalize only the closed
`a0`/`v1` index/table-base allocation cycle; see
[Working Note 502](WORKING_NOTES/502-game-actor-slot-selector-match-20260929.md).
Game group-value appender `func_15022640` is byte-exact across all 31 words
after recovering its duplicate scan, 30-byte row indexing, and count update.
The corrected integer value ABI and separate signed loop-bound lifetime emit
the complete routine directly from C with no guards; see
[Working Note 503](WORKING_NOTES/503-game-group-value-deduplicating-append-match-20260929.md).
Game display-list address relocator `func_15168F08` is byte-exact across all
31 words after recovering signed opcode parsing, index-based cursor updates,
and retail's two-step mask/add stores. Eighteen stale checks normalize only one
closed constant/cursor allocation chain; see
[Working Note 504](WORKING_NOTES/504-game-display-list-address-relocator-match-20260929.md).
Game cached resource setup `func_1517A9A8` is byte-exact across all 30 words
after recovering its selector cache gate, 20-byte output record, shifted
resource index, and nine-argument setup call. Six stale checks normalize only
one independent call-argument scheduling window; see
[Working Note 505](WORKING_NOTES/505-game-cached-resource-setup-match-20260929.md).
Game byte-selected coefficient clamp `func_15182F58` is byte-exact across all
33 words after recovering its 24-byte coefficient row, integer-times-40
scale, and mutually exclusive lower/upper clamp. The complete routine emits
directly from C with no guards; see
[Working Note 506](WORKING_NOTES/506-game-byte-selected-coefficient-clamp-match-20260929.md).
Game reference-counted resource release `func_1518CA04` is byte-exact across
its complete 31-word tracked slot after recovering its reserved-index gate,
short-circuit byte decrement, and two cleanup calls. It emits directly from C
with no guards; see
[Working Note 507](WORKING_NOTES/507-game-reference-counted-resource-release-match-20260929.md).
Game five-state impact dispatcher `func_15194794` is byte-exact across all 31
words after recovering its two unconditional setup calls and grouped state
switch. Two relocation-aware stale checks retarget only the generated jump
table reference to the retained retail table; see
[Working Note 508](WORKING_NOTES/508-game-five-state-impact-dispatch-match-20260929.md).
Game subsystem-state initializer `func_151DDBA0` is byte-exact across all 32
words after recovering its setup call, global mode clears, three subsystem
calls, and paired ready flags. The complete routine emits directly from C
with no guards; see
[Working Note 509](WORKING_NOTES/509-game-subsystem-state-initializer-match-20260929.md).
Game timed HUD fade helper `func_151EC178` is byte-exact across all 30 words
after recovering its saturated alpha ramp, white modulation call, fixed text
resource draw, and unchanged display-list return. Nineteen stale checks
normalize one collapsed compiler merge and the displaced call tail; see
[Working Note 510](WORKING_NOTES/510-game-timed-hud-fade-helper-match-20260929.md).
Game resource teardown `func_15080BE8` is byte-exact across all 31 words after
recovering its primary release, conditional three-allocation cleanup, owner
slot clear, and tagged final teardown. Four stale checks normalize only the
optional-allocation load/test register; see
[Working Note 511](WORKING_NOTES/511-game-resource-teardown-match-20260929.md).
Game two-angle trigonometric updater `func_150A0D14` is byte-exact across all
30 words after recovering its two scaled input angles and paired cosine/sine
outputs. The complete routine emits directly from typed C with no guards; see
[Working Note 512](WORKING_NOTES/512-game-two-angle-trigonometric-updater-match-20260929.md).
Game resource slot-array teardown `func_150B6D78` is byte-exact across all 33
words after recovering its standalone release, ten-slot allocation scan,
owner clears, and final state transition. Two relocation-aware guards
normalize only independent address-finalization words; see
[Working Note 513](WORKING_NOTES/513-game-resource-slot-array-teardown-match-20260929.md).
Game owner-payload object spawn `func_150BDE90` is byte-exact across all 31
words after recovering its eight-byte local payload, fixed object-creation
request, and conditional copy to object offset `0x28`. The complete routine
emits directly from C with no guards; see
[Working Note 514](WORKING_NOTES/514-game-owner-payload-object-spawn-match-20260929.md).
Game indexed resource-chain teardown `func_150C0A48` is byte-exact across all
30 words after recovering its signed-index table walk, resource releases,
and post-release owner table reloads. The complete routine emits directly
from C with no guards; see
[Working Note 515](WORKING_NOTES/515-game-indexed-resource-chain-teardown-match-20260929.md).
Game owner-identity object spawn `func_151001B4` is byte-exact across all 31
words after recovering its eight-byte identity payload, fixed object request,
and conditional copy to object offset `0x28`. The complete routine emits
directly from C with no guards; see
[Working Note 516](WORKING_NOTES/516-game-owner-identity-object-spawn-match-20260929.md).
Game fixed-payload object spawn `func_1514D978` is byte-exact across all 31
words after recovering its 32-byte payload, allocation, copy, and tag-`0x13`
registration. The complete routine emits directly from C with no guards; see
[Working Note 517](WORKING_NOTES/517-game-fixed-payload-object-spawn-match-20260929.md).
Game record-window initializer `func_15183974` is byte-exact across all 31
words after recovering its five-word record indexing, two conditional record
initializations, and fourth-word copy. Four guarded words preserve one
equivalent record-pointer spill slot; see
[Working Note 518](WORKING_NOTES/518-game-record-window-initializer-match-20260929.md).
Game record-match release wrapper `func_1518F49C` is byte-exact across all 32
words after recovering its five-argument forwarding call, selector gate, and
two comparison keys. The complete routine emits directly from C with no
guards; see
[Working Note 519](WORKING_NOTES/519-game-record-match-release-wrapper-20260929.md).
Game callback-state setup `func_151E4E64` is byte-exact across all 33 words
after recovering its two setup calls, counter-controlled halfword flag, and
conditional callback/state installation. The complete routine emits directly
from C with no guards; see
[Working Note 520](WORKING_NOTES/520-game-callback-state-setup-match-20260929.md).
Game 25-byte group append `func_1502225C` is byte-exact across all 33 words
after recovering its per-group deduplication scan, append, and count update.
The complete routine emits directly from C with no guards; see
[Working Note 521](WORKING_NOTES/521-game-25-byte-group-deduplicating-append-match-20260929.md).
Game collision-classifier wrapper `func_15046C80` is byte-exact across all 32
words after recovering its four-argument ABI, three-way classification, and
class-zero delegation. The complete routine emits directly from C with no
guards; see
[Working Note 522](WORKING_NOTES/522-game-collision-classifier-wrapper-match-20260929.md).
Game secondary collision-classifier wrapper `func_15046F84` is byte-exact
across all 32 words after recovering its matching four-argument dispatch and
`func_15046D00` class-zero path. The complete routine emits directly from C
with no guards; see
[Working Note 523](WORKING_NOTES/523-game-secondary-collision-classifier-wrapper-match-20260929.md).
Game bounded table-buffer append `func_1507EBB8` is byte-exact across all 32
words after recovering its selector-indexed source and length tables, strict
40-byte bound, copy, and count update. The complete routine emits directly
from C with no guards; see
[Working Note 524](WORKING_NOTES/524-game-bounded-table-buffer-append-match-20260929.md).
Game coordinate-query wrapper `func_150A32B4` is byte-exact across all 31
words after recovering its stack-local `struct127`, coordinate field writes,
query submission, and inverted success result. The complete routine emits
directly from C with no guards; see
[Working Note 525](WORKING_NOTES/525-game-coordinate-query-wrapper-match-20260929.md).
Game randomized effect wrapper `func_150B6754` is byte-exact across all 35
words after recovering its two PRNG ranges, incoming byte/context forwarding,
and eight-argument effect call. The complete routine emits directly from C
with no guards; see
[Working Note 526](WORKING_NOTES/526-game-randomized-effect-parameter-wrapper-match-20260929.md).
Game motion-threshold updater `func_150CC638` is byte-exact across all 32 words
after recovering its flag gate, scaled byte limit, record threshold, and paired
float accumulation. Thirteen stale-checked guards normalize only IDO's
equivalent register/address schedule, including two retained pointer words;
see
[Working Note 527](WORKING_NOTES/527-game-motion-threshold-updater-match-20260929.md).
Game mode-selected color wrapper `func_150D22F4` is byte-exact across all 32
words after recovering its callback ABI, record-byte selection, paired
all-white/all-zero channel arguments, and signed selector forwarding. The
complete routine emits directly from C with no guards; see
[Working Note 528](WORKING_NOTES/528-game-mode-selected-color-wrapper-match-20260929.md).
Game current-player threshold dispatcher `func_150DEB58` is byte-exact across
all 34 words after recovering the `0x9A0` player-record view, float threshold,
embedded record pointers, and signed mode forwarding. The complete routine
emits directly from C with no guards; see
[Working Note 529](WORKING_NOTES/529-game-current-player-threshold-dispatch-match-20260929.md).
Game fixed resource-constructor wrapper `func_1514DBB8` is byte-exact across
all 32 words after recovering the complete 16-argument `func_15160A58` call,
resource pointer, and fixed constructor parameters. The routine emits directly
from C with no guards; see
[Working Note 530](WORKING_NOTES/530-game-fixed-resource-constructor-wrapper-match-20260929.md).
Game owner-payload allocation wrapper `func_1514F3CC` is byte-exact across all
32 words after recovering its 12-byte stack payload, fixed allocator request,
and conditional copy to returned-object offset `0x28`. The routine emits
directly from C with no guards; see
[Working Note 531](WORKING_NOTES/531-game-owner-payload-allocation-wrapper-match-20260929.md).
Game randomized RGBA initializer `func_15152ABC` is byte-exact across all 31
words after recovering its unsigned random remainders, five-entry RGB table,
byte-width index, and alpha range. It emits directly from C with no guards; see
[Working Note 532](WORKING_NOTES/532-game-randomized-rgba-initializer-match-20260929.md).
Game descriptor-copy allocator `func_15157898` now matches all 32 words
directly from C; see
[Working Note 533](WORKING_NOTES/533-game-descriptor-copy-allocation-wrapper-match-20260929.md).
Game indexed slot teardown `func_15172CA8` now matches all 32 words directly
from C; see
[Working Note 534](WORKING_NOTES/534-game-indexed-slot-teardown-event-pair-match-20260929.md).
Game four-resource teardown `func_1519F400` now matches all 35 words directly
from C; see
[Working Note 535](WORKING_NOTES/535-game-four-resource-teardown-match-20260929.md).
Game motion-threshold update `func_151AFC08` now matches all 32 words using its
semantic C body and the established duplicate-function guard set; see
[Working Note 536](WORKING_NOTES/536-game-second-motion-threshold-update-match-20260929.md).
Game linked-endpoint event handler `func_151B70B4` now matches all 36 words
after recovering its zero-event detach state and event-`0x2D` endpoint
replacement behavior. Nineteen stale-checked guards normalize one closed IDO
register/scheduling cycle; see
[Working Note 537](WORKING_NOTES/537-game-linked-endpoint-event-handler-match-20260929.md).
Game reflected byte-position update `func_151E55A8` now matches all 33 words
directly from semantic C after recovering its signed step, boundary reflection,
and direction toggle; see
[Working Note 538](WORKING_NOTES/538-game-reflected-byte-position-update-match-20260929.md).
Init primary/child record lookup `func_1000B1FC` now matches all 38 words
directly from semantic C after restoring its two original three-entry indexed
loops; see
[Working Note 539](WORKING_NOTES/539-init-primary-child-record-lookup-match-20260929.md).
Game indexed constructor wrapper `func_1501D1D4` now matches all 33 words
directly from semantic C after restoring its seven-argument constructor call,
two local outputs, and success/failure slot update; see
[Working Note 540](WORKING_NOTES/540-game-indexed-constructor-wrapper-match-20260929.md).
Game indexed 64-bit flag query `func_1501D2C4` now matches all 33 words
directly from semantic C, including retail's `__ll_lshift` helper ABI and
split high/low-word test; see
[Working Note 541](WORKING_NOTES/541-game-indexed-64-bit-flag-query-match-20260929.md).
Game auxiliary-state allocator `func_1503B7C0` now matches all 32 words
directly from semantic C after exposing the state pointer at `struct126`
offset `0x11C` and recovering its initialization; see
[Working Note 542](WORKING_NOTES/542-game-auxiliary-state-allocator-match-20260929.md).
Game packed-byte rate updater `func_15077404` now matches all 44 words after
recovering its signed 16-bit result truncation, negative clamp, and active or
fallback packed-byte stores. Thirty-three guarded source words and one
inserted scheduling word normalize the closed compiler allocation cycle; see
[Working Note 543](WORKING_NOTES/543-game-packed-byte-rate-update-match-20260930.md).
Game state-three convergence scanner `func_1509CDDC` now matches all 34 words
after restoring its initial slot processing and repeated 204-byte scans; see
[Working Note 544](WORKING_NOTES/544-game-state-three-convergence-scan-match-20260930.md).
Game object-position forwarding adapter `func_1509F77C` now matches all 33
words directly from C after exposing its three truncated coordinate locals;
see [Working Note 545](WORKING_NOTES/545-game-object-position-forwarding-adapter-match-20260930.md).
Game absolute-value ordering helper `func_150AD9A0` is restored from its false
zero-return C placeholder to its original handwritten 32-word assembly body;
see [Working Note 546](WORKING_NOTES/546-game-handwritten-absolute-ordering-helper-restoration-20260930.md).
The Game motion timestep integrator `func_150DEACC` now matches its complete
140-byte span directly from C; see
[Working Note 547](WORKING_NOTES/547-game-motion-timestep-integrator-match-20260930.md).
The Game record-type eligibility predicate `func_150EC3D4` now matches its
complete 136-byte span directly from C; see
[Working Note 548](WORKING_NOTES/548-game-record-type-eligibility-predicate-match-20260930.md).
The Game type-0x28 object sweep `func_150FDD10` now matches its complete
144-byte span through five guarded allocation words; see
[Working Note 549](WORKING_NOTES/549-game-type-28-object-sweep-match-20260930.md).
The Game camera-vector forwarding wrapper `func_1510B32C` now matches its
complete 132-byte span through eight guarded ABI/register words; see
[Working Note 550](WORKING_NOTES/550-game-camera-vector-forwarding-wrapper-match-20260930.md).
The Game indexed countdown finalizer `func_1510D694` now matches its complete
140-byte span directly from C; see
[Working Note 551](WORKING_NOTES/551-game-indexed-countdown-finalizer-match-20260930.md).
Its state-two structural twin `func_1510D720` also matches its complete
140-byte span directly from C; see
[Working Note 552](WORKING_NOTES/552-game-state-two-countdown-finalizer-match-20260930.md).
The Game two-tag record index scan `func_1511A410` now matches its complete
132-byte span through 13 guarded scheduling/register words; see
[Working Note 553](WORKING_NOTES/553-game-two-tag-record-index-scan-match-20260930.md).
The Game mode-gated object cleanup wrapper `func_1511A738` now matches its
complete 136-byte span directly from C; see
[Working Note 554](WORKING_NOTES/554-game-mode-gated-object-cleanup-wrapper-match-20260930.md).
The Game indexed saved-state restorer `func_151239CC` now matches its complete
136-byte span through two guarded stack-slot words; see
[Working Note 555](WORKING_NOTES/555-game-indexed-saved-state-restorer-match-20260930.md).
The Game bit-zero state-operation callback `func_1514E89C` now matches its
complete 132-byte span directly from C; see
[Working Note 556](WORKING_NOTES/556-game-bit-zero-state-operation-callback-match-20260930.md).
The Game owner-list cleanup `func_1514EDF0` now matches its complete 128-byte
span through three guarded local-stack operands; see
[Working Note 557](WORKING_NOTES/557-game-owner-list-matching-node-cleanup-match-20260930.md).
The Game two-entry selection event callback `func_15158B3C` now matches its
complete 148-byte span through ten guarded scheduling/register rows; see
[Working Note 558](WORKING_NOTES/558-game-two-entry-selection-event-callback-match-20260930.md).

## Verified build state

These commands passed from the current checkout on 2026-09-30:

```sh
make -C conker replace NON_MATCHING=1 -j4
make -C conker build/conker.us.elf
make -C conker match-progress NON_MATCHING=1
make tools-check
make NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

The successful non-matching build establishes that the current source links
and emits `conker.us.bin`. It does not establish a matching ROM hash or fresh
end-to-end gameplay acceptance.

## Resume boundary

Current Init task: recover the 954-word `__n_CSPHandleMIDIMsg`. Note 730
supersedes the earlier `func_10006380` segment-splitting recommendation and
the address-drift explanation in Note 729. Preserve the exact sequence/meta
handlers and retain the handwritten `init_5AB0` calling conventions.

1. The restoration baseline is banked. Do not fold a broad conversion batch
   into it; future work should start from a new focused commit.
2. Debugger is complete: 181 / 181 C-classified rows and the one handwritten
   assembly routine are linked byte-exact. Preserve the guarded
   `func_16000B14` normalization while broader matching continues.
3. The original `func_150AD780`/`func_150AD78C` trig slice is restored, and
   `func_150849A0` is byte-exact from a source-level index-lifetime fix, and
   `func_150636A4` is byte-exact through a guarded nested-pointer lifetime
   normalization, and `func_1514672C` is byte-exact through a guarded
   relocation-preserving load reorder. `func_15199980` is byte-exact from an
   explicit callback-pointer lifetime, `func_1505D024` is byte-exact through
   guarded call-argument register normalization, and `func_15071A64` is
   byte-exact from corrected stack-local declaration order, and
   `func_15087DCC` is byte-exact from separating the global base load from the
   indexed record pointer, and `func_1509D054` is byte-exact through guarded
   call-argument lifetime normalization. The five-word `func_150A7A00` is now
   restored as its original synthetic-return assembly trampoline,
   `func_150ADACC` is restored as handwritten assembly, `func_150BDB3C` is
   byte-exact through guarded scalar-temporary normalization, and
   `func_150F33B0` is byte-exact through guarded set-bit temporary
   normalization, and `func_151254F4` is byte-exact through guarded
   relocation-preserving opening-load scheduling. The nine-word
   `func_1515FB70` is restored to assembly ownership after its C model proved
   unable to preserve the retail undefined-return branch shape.
   `func_1505841C` is byte-exact through guarded FP-temporary and global-load
   register normalization. `func_150F02A0` is byte-exact after making its
   base-pointer and index lifetimes explicit and guarding the remaining
   temporary-register choices. `func_151B2FA0` is byte-exact after correcting
   its forwarded argument and callee declaration from `s16` to `s32`.
   `func_150770E4` is byte-exact after expressing its table lookup as retail's
   combined 812-byte stride. Handwritten `func_150A7770` is restored to its
   original eight-word assembly extent after the C model overflowed the slot.
   `func_1515F008` is byte-exact through six guarded, non-relocating
   pointer/value register choices. The adjacent `func_1516F8EC`,
   `func_1516F91C`, and `func_1516F984` cluster is byte-exact, completing the
   six-difference game tier. `func_15019BB8` is now byte-exact through seven
   guarded frame/address words. `func_1509F6B0` is byte-exact through seven
   guarded spill/reload scheduling words. `func_150C7930` is restored to its
   original 14-word assembly extent after exhaustive C forms could not retain
   its dead pointer update. `func_150CDB6C` is byte-exact through seven
   guarded, non-relocating destination-pointer schedule words.
   `func_15108B80` is byte-exact through seven guarded, non-relocating
   countdown register words. `func_1513A594` is byte-exact after correcting
   the forwarded byte ABI and retaining its post-call field read, with three
   guarded words for retail's empty branch shape. `func_151423D8` is
   byte-exact through seven guarded, non-relocating quadrant/table-index
   register words. `func_15155EF8` is byte-exact through seven guarded,
   non-relocating outer/child pointer lifetime words. Adjacent 11-word
   `func_151D7770` and `func_151D779C` are byte-exact from source-level
   pointer ordering and mask recovery, completing the seven-difference game
   tier. `func_1509F248` is byte-exact from source-level unsigned-halfword
   narrowing. `func_150C5EFC` is restored to its original 17-word assembly
   extent after IDO removed its dead pointer update. Structural twin
   `func_150C682C` is restored for the same reason. `func_150EA904` is
   byte-exact through eight guarded, relocation-preserving base/index and
   byte-update register words. `func_1515D480` is byte-exact through eight
   guarded frame and local-slot words. `func_151AB180`, the `+0x70` member of
   the dead child-pointer family, is restored to its original 17-word assembly
   extent. `func_151EF610`, the final eight-difference game row, is restored
   to original assembly ownership. `func_150771F0` is byte-exact through a
   relocation-aware argument-load schedule. `func_15080200` is byte-exact
   from chained global assignment. `func_1510E634` is byte-exact through the
   generated-slice guarded-expansion path. `func_1512D6B0` is byte-exact
   through guarded record-index register lifetimes. `func_15166FD8` is
   byte-exact through an independently guarded display-list cursor expansion.
   `func_15196330` and structural twin `func_151963B4` are byte-exact through
   independently verified guarded `v0`/`v1` lifetimes. `func_151E5F64` is
   byte-exact from source-level positive-branch control-flow recovery, with no
   guarded words. `func_151E81EC` is byte-exact from a four-word state struct,
   chained assignment, and six guarded paired-store relocation words.
   `func_1502EA0C` is byte-exact through ten guarded packed-byte scheduling
   and register words. `func_15033E84` is byte-exact from source-level
   next-pointer lifetime and loop-condition assignment recovery.
   `func_15094F40` is byte-exact through the guarded generated-slice cursor
   expansion. Structural relative `func_15096934` is independently byte-exact
   through its own guarded cursor expansion and state-byte clear.
   `func_150CF578` is byte-exact from source-level scalar and product
   lifetimes, with no guarded words. `func_150DE2C4` is byte-exact from a
   source-level short-circuit OR condition, also with no guarded words.
   Former placeholder `func_151318E8` is byte-exact as a source-level
   repeated float-scale loop while its caller remains exact. `func_15133A50`
   is byte-exact through source-level sum/store scheduling plus nine guarded
   FP-register words. `func_15133E3C` is byte-exact from a two-word aggregate
   initializer and corrected pointer ABI, with no guarded words. Continue
   through `func_151581D8`, now byte-exact through ten guarded prologue and
   argument-schedule words. `func_151D74B0` is byte-exact from source-level
   record-construction order, completing the ten-difference game tier.
   `func_150717E0` is byte-exact through eleven guarded local-record pointer,
   call-relocation, and epilogue schedule words. `func_15074A94` is byte-exact
   from a source-level interpolation expression plus eleven guarded FP-register
   words. `func_1507EEB8` is byte-exact from a source-level fixed reverse loop
   with no guarded rows. `func_150B6D34` is byte-exact from a simplified
   record-activation loop plus nine guarded cursor/register schedule words.
   `func_151090DC` is byte-exact from a typed two-word aggregate initializer
   and corrected pointer ABI, with no guarded rows. `func_15141564` is
   byte-exact from multiplication-first position scheduling plus two guarded
   base-pointer local-slot words. `func_15178E14` is byte-exact from corrected
   byte and forwarded-result callee contracts, with no guarded rows.
   `func_151ACA20` is byte-exact from candidate-first local declaration and a
   direct signed four-bit scaling assignment, with no guarded rows.
   `func_1501CFF8` is byte-exact from direct global count expressions and local
   lifetime ordering, with no guarded rows. `func_15031E2C` is byte-exact from
   twelve guarded register-schedule words, including two relocation-preserving
   table-address words. `func_150337E4` is byte-exact from direct field update,
   comparison, and table-index expressions, with no guarded rows.
   `func_1504BA38` is byte-exact through twelve guarded, non-relocating words
   that restore retail's three-byte record pointer and value-register
   lifetimes. `func_150882B0` is byte-exact from pointer-first local ordering,
   final `arg0` pointer reuse, and ten guarded schedule words that explicitly
   move the global relocation pair. `func_1508B194` is byte-exact from a
   source-level early-zero branch plus five guarded record-table base/index
   words. `func_150E33CC` is byte-exact through twelve guarded scheduling
   words that preserve its call relocation while restoring retail's `v0`
   value lifetime and call-delay argument move. `func_15131D4C` is byte-exact
   directly from a typed three-word aggregate copy and pointer-correct callee
   declaration, with no guarded words. `func_151355B8` is byte-exact after
   volatile field accesses retain retail's duplicate store, plus five guarded
   loaded/result register words. `func_15168800` is byte-exact directly from
   an explicit early null return, with no guarded words. Continue with 18-word
   `func_151E5FAC` is byte-exact from duplicated fallback returns, positive
   threshold control flow, and twelve guarded relocation/scheduling words,
   completing the twelve-difference game tier. `func_15002560` is byte-exact
   from an explicit top null test, scalar sibling-offset result, and two
   guarded commutative pointer adds. `func_150356C8` is byte-exact after
   simplifying its increment lifetime, plus nine guarded scheduling words
   that move the `D_800C3F08` low relocation. `func_15043B70` is byte-exact
   directly from a scalar ternary that restores retail's explicit two-arm
   chunk-selection merge. `func_1507A3E8` is byte-exact through thirteen
   guarded byte-load and merge-schedule words that preserve all four global
   relocation pairs. `func_1507FF94` is byte-exact after retaining a volatile
   local-record pointer across its first call, plus five guarded prologue
   scheduling words. `func_15085B70` is byte-exact directly from reversing
   its null condition so the zeroing path precedes the populated path, with no
   guarded rows. `func_150A7A14` is restored to its original thirteen-word
   assembly continuation because it returns through `t9` as the second half
   of `func_150A7A00`'s synthetic-return trampoline. `func_150CFBEC` is
   byte-exact directly from an outer record-pointer lifetime and repeated
   volatile source-field loads, with no guarded rows. `func_15131918` is
   converted from a placeholder to byte-exact C by typing its two callers'
   scale fields as floats and implementing the two-component scaling loop.
   `func_1514143C` is now byte-exact with thirteen guarded words that preserve
   retail's embedded-base lifetime and two inserted schedule words after
   source-only layout probes folded or grew a frame. `func_15144B68` is now
   byte-exact after a named result local restored retail's FP-register lifetime
   and two guarded words restored the independent opening compare/copy
   schedule. `func_1518F858` is now byte-exact directly from an explicit early
   return and volatile signed-byte index, restoring retail's repeated load,
   branch-likely epilogue, and callback-table register lifetimes.
   `func_1519072C` is now byte-exact directly from a contiguous local aggregate
   that preserves retail's `sp + 0x1C` record-pointer spill and `sp + 0x20`
   record across both calls. `func_1519582C` is now byte-exact from volatile
   pointer source plus eight guarded relocation/scheduling words that preserve
   retail's opening `v0`/`v1` global-address preload. `func_151A9024` is now
   byte-exact with thirteen guarded words that preserve retail's argument-home,
   byte-narrowing, early-epilogue, and call-relocation schedule.
   `func_151C9B64` is now byte-exact directly from corrected branch semantics
   and an explicit nested-pointer lifetime; no guarded words are required.
   The tied 13-word `func_151F892C` and `func_151F8960` rows are explicitly
   handwritten and consume non-ABI live registers, so they are excluded from
   the C-restoration queue. `func_1502C380` is now byte-exact directly from an
   assignment chain that preserves its destination-address and loaded-value
   lifetimes. `func_150A7B80` is now byte-exact after expressing its eight
   clears explicitly and using fourteen guarded overflow-slot words to retain
   retail's native 64-bit stores and diagonal writes. `func_1516A770` is now
   byte-exact directly from a delimiter-splitting loop: it replaces each
   `0xBD` byte with zero and returns the replacement count plus one.
   `func_1518F45C` is now byte-exact directly after its scalar array became a
   one-word aggregate and the callee's record parameter became `void *`.
   `func_151A5130` is now byte-exact after its indirect callback expression
   explicitly forwards all three incoming arguments, restoring the signed
   halfword narrowing and live-register ABI. `func_1508F060` is now byte-exact
   after correcting its state-block base to selected row two and applying nine
   guarded rows with three insertions for retail's explicit pointer arithmetic.
   `func_1518F89C` is now byte-exact from a typed float-record view plus twelve
   guarded scheduling words that retain the field base and both call delay
   slots. `func_151A561C` is now byte-exact directly from the same one-word
   aggregate and `void *` callee contract used by `func_1518F45C`.
   `func_151D343C` is now byte-exact from the third one-word aggregate and a
   corrected shared `func_15169260(void *, ...)` contract, with no matcher
   regressions. `func_1519F3B8` is now byte-exact from a typed four-word record
   plus nine guarded scheduling rows and one inserted reload.
   `func_15160274` is now byte-exact directly from a fourth one-word aggregate
   and a corrected local pointer contract. `func_151BD750` is now byte-exact
   through fifteen guarded FP scheduling rows and two inserted terminal words.
   `func_151417C4` is now byte-exact directly from a typed two-word aggregate,
   byte-typed first argument, and one-byte array local. `func_15144BC8` is now
   byte-exact directly after its normalized angle became an explicit `ret`
   local. `func_150718E4` is now byte-exact from corrected local ordering plus
   ten guarded post-random-call register words. `func_150142AC` is now
   byte-exact directly from a signed index and explicit invalid-range return.
   `func_15088270` is now byte-exact from a separate index lifetime plus ten
   guarded scheduling words. `func_15188A58` is now byte-exact after recovering
   its offset-`0x0C` linked-list append plus thirteen guarded control-flow
   words. Skip handwritten `func_151F892C` and `func_151F8960`; continue with
   20-word ordinary-C placeholder `func_1509F660`, now byte-exact directly
   after recovering its nullable lookup and two-way callback dispatch.
   `func_151C4510` is now byte-exact from explicit destination lifetimes plus
   fifteen guarded FP scheduling words. `func_150C78E0` is now byte-exact from
   seven guarded rows, including one inserted dead pointer advance and two
   moved global relocations. `func_15130230` is now byte-exact directly after
   explicitly passing its incoming `arg0` to the selected scene callback; no
   guarded rows were needed. `func_1506C32C` is now byte-exact directly after
   sharing one local across its choice-count and selected-index phases and
   placing the choices array between its scalar locals. `func_150CFDB8` is now
   byte-exact directly after removing its redundant pointer copy, mutating
   `arg0` across the record loop, and giving `max` and `next` retail's
   lifetimes. `func_150CFE3C` is now byte-exact after recovering its nested
   active-buffer state and adding six guarded base/register scheduling words.
   `func_15167010` is now byte-exact after deriving its table bound from the
   cursor and guarding retail's frame, saved-register, relocation, and end
   pointer lifetimes. `func_15167D84` is now byte-exact through thirteen
   guarded CFG/register-scheduling rows affecting its fifteen-word tail.
   `func_151D2E5C` is now byte-exact after correcting its owner-pointer call,
   recovering four explicit local lifetimes, and guarding one commutative
   branch word. `func_150104F0` is now byte-exact after recovering its chained
   zero assignment and guarding six base/store words, including one inserted
   result materialization. `func_150492CC` is now byte-exact through sixteen
   guarded floating-point and relocation-scheduling words that preserve its
   authored divisions by `2.0f`. `func_150767F4` is now byte-exact through
   sixteen guarded register-scheduling words; its existing C computes an
   indexed object's horizontal angle and triggers `func_15075400` when the
   masked delta is inside the doubled tolerance. Keep 17-word
   `func_150721A4` parked: its live C is intentionally retained despite a
   measured three-word compiler overflow. `func_1507A428` is now byte-exact
   through sixteen guarded global-load, relocation, and packed-value register
   words. `func_15084CB0` is now byte-exact after recovering its scalar
   lifetimes and indexed `u16` table access, plus seven guarded signed-loop and
   epilogue words. `func_15086D48` is now byte-exact after recovering indexed
   16-byte record access, plus six guarded signed-loop and fallback-epilogue
   words. `func_150F631C` now matches directly after recovering its owner
   lifetime and volatile repeated first-field reads. `func_15131958` now
   matches directly after restoring the count-controlled three-component
   vector scaling loop and correcting its local call signatures.
   `func_151419D0` is now byte-exact after sharing the source endpoint lifetime
   across both event paths and guarding one commutative branch operand-order
   word. `func_15143874` now matches directly after correcting its signed
   angle ABI and recovering explicit narrowed-angle and lookup-result
   lifetimes. `func_15147D1C` now matches directly after restoring the indexed
   callback's object, scalar, and normalized-byte arguments. `func_1515C158`
   is now byte-exact after restoring its two-row linked-list reset and
   guarding thirteen persistent IDO pointer-coloring words. `func_1515D520`
   is now byte-exact after recovering direct head testing and typed tail
   insertion, plus four guarded frame/scheduling words. `func_151635A8` is now
   byte-exact after correcting the indexed callback ABI and preserving two
   volatile table reads, plus fifteen guarded rows that normalize seventeen
   persistent scheduling/register words and insert the two missing epilogue
   words. `func_15168A4C` is now byte-exact after recovering its typed
   row/column list-head insertion and explicit scalar index lifetimes, plus
   four guarded `a2`-versus-`t0` register-color words. Keep generated
   `lwl`/`lwr` helpers `func_151F892C` and `func_151F8960` in the raw-assembly
   queue. `func_150747E4` is now byte-exact after recovering separate selected
   slot, decremented index, full update value, and actor-pointer lifetimes,
   plus ten guarded relocation/register-scheduling words. Continue with
   `func_150849CC`, now converted from its zero-return placeholder and
   byte-exact after restoring both selector paths, optional index output, and
   indexed byte return, plus three guarded CFG rows retaining one retail
   branch. `func_1508CA88` is now byte-exact after restoring its signed
   wrapping-counter CFG and preserving the independent final global-pointer
   reload with two guarded relocation-aware rows. `func_15116930` is now
   converted from its zero-return placeholder and byte-exact directly from C
   after retaining the owner-slot address through the state gates. Continue
   with 21-word `func_1511F92C`, which is now converted from its zero-return
   placeholder and byte-exact directly from C after restoring its nullable
   lookup and three-halfword copy. The 18-word `func_15130374` is now converted
   and byte-exact directly from C after correcting its six-argument forwarding
   ABI. The 21-word `func_1515572C` is now converted and byte-exact directly
   from C after restoring its typed two-word template copy and dispatch call.
   The 19-word `func_15178B98` is now converted and byte-exact directly from C
   after restoring its selector-based linked-list lookup. Continue with
   The 18-word `func_1519257C` is now converted and byte-exact directly from C
   after restoring its gated two-stage byte result. Continue with 19-word
   `func_151B82CC` is now byte-exact after correcting its callback signature,
   forwarding all three inputs, and retaining the child-pointer lifetime.
   The 19-word `func_1506AC0C` is now converted and byte-exact directly from C
   after restoring its typed object-selector record and dispatch call. The
   19-word `func_150881CC` is now byte-exact after retaining its clean scaled
   table-read C behavior and guarding five IDO register-scheduling words. The
   30-word `func_15088780` is now byte-exact directly from C after removing a
   one-use record pointer and restoring base-plus-scaled-index operand order.
   The 24-word `func_1509E8A0` is now converted and byte-exact directly from C
   after restoring its three-argument callback contract and two-case selector
   dispatch. The 21-word `func_150A34B0` is now converted and byte-exact
   directly from C after restoring its byte-`0x14` rejection, low-flag gate,
   and forwarded `func_150A3504` call. The 20-word `func_150A7CB0` is now
   byte-exact after restoring its floating identity element and guarding the
   final three-word store/return schedule. The adjacent 20-word
   `func_150A7DA0` is now byte-exact after restoring the four floating
   diagonal stores and three raw translation words, with six guarded
   register/schedule words. The 18-word `func_150ADA20` PRNG step is restored
   to original handwritten assembly ownership after the equivalent C was
   confirmed to compile as a 19-word overflow trampoline. The 30-word
   `func_150CFE98` buffer-advance helper is now byte-exact after recovering
   its one-use pointer and result lifetimes, with seven guarded frame/spill
   words. The 21-word `func_150F34A0` float threshold mapper is now converted
   from its zero-return placeholder and byte-exact directly from C, with no
   guarded words. The 20-word `func_150FADC8` event-bit callback is now
   converted from its zero-return placeholder and byte-exact directly from C,
   with no guarded words. Continue with 21-word `func_15133DE8`, the next
   ordinary Game C row with eighteen real differences. That 21-word
   `func_15133DE8` record/owner match callback is now converted from its
   zero-return placeholder and byte-exact directly from C after retaining the
   record identifier lifetime, with no guarded words. The current queue has
   advanced through `func_151E4E64`, whose complete 33-word callback-state
   setup now matches directly from C with no guarded words.
   `func_15106E78` is parked on a closed 30-versus-32-word caller-saved
   allocation cycle. Init `func_1000FF90` is now byte-exact across its complete
   35-word span. The 32-word auxiliary-state allocator
   `func_1503B7C0` is now byte-exact directly from C with no guards.
   `func_150413FC` is parked on a five-versus-four saved-register allocation
   cycle. The 44-word packed-byte rate updater `func_15077404` is now
   byte-exact with 33 guarded source words and one inserted scheduling word.
   The 34-word state-three convergence scanner `func_1509CDDC` is now
   byte-exact through 18 guarded contraction/scheduling rows.
   The 33-word object-position forwarding adapter `func_1509F77C` is now
   byte-exact directly from C. The handwritten 32-word `func_150AD9A0` is now
   restored to assembly ownership and exact independently. The 35-word motion
   timestep integrator `func_150DEACC` is now byte-exact directly from C.
   The 34-word record-type eligibility predicate `func_150EC3D4` is now
   byte-exact directly from C. The 36-word type-0x28 object sweep
   `func_150FDD10` is now byte-exact through five guarded allocation words.
   The 33-word camera-vector forwarding wrapper `func_1510B32C` is now
   byte-exact through eight guarded ABI/register words. The 35-word indexed
   countdown finalizer `func_1510D694` and its state-two structural twin
   `func_1510D720` are now byte-exact directly from C. The 33-word two-tag
   record index scan `func_1511A410` is now byte-exact through 13 guarded
   scheduling/register words. The 34-word mode-gated object cleanup wrapper
   `func_1511A738` is now byte-exact directly from C. The 34-word indexed
   saved-state restorer `func_151239CC` is now byte-exact through two guarded
   stack-slot words. The 33-word bit-zero state-operation callback
   `func_1514E89C` is now byte-exact directly from C. The 32-word owner-list
   cleanup `func_1514EDF0` is now byte-exact through three guarded local-stack
   operands. The 37-word two-entry selection callback `func_15158B3C` is now
   byte-exact through ten guarded scheduling/register rows. The 35-word
   transformed-position short writer `func_1516441C` is now byte-exact
   directly from C. The 33-word three-entry position queue writer
   `func_1517D578` is now byte-exact through 29 guarded allocation/scheduling
   words. The 33-word selector display-list appender `func_15183BA4` is now
   byte-exact directly from C. The 33-word command-`0x1D` payload allocator
   `func_1518AADC` is now byte-exact through ten guarded scheduling words.
   The 33-word object-selector payload wrapper `func_15192920` is now
   byte-exact through 17 guarded scheduling words. Its 33-word structural twin
   `func_151B1AB0` is also byte-exact through an independently scoped copy of
   the same schedule guards. The 35-word midpoint-timestep integrator
   `func_151CEA20` is now byte-exact through 21 guarded FP scheduling words.
   The 34-word global mode-state updater `func_151D66F0` is now byte-exact
   directly from C. Init `__osProbeTLB` is restored to its original
   handwritten CP0/TLB ownership, and its complete 48-word slot independently
   matches retail. The 44-word signed-position effect dispatcher
   `func_15013D38` is now byte-exact through five guarded setup-schedule words.
   The 33-word table-record dispatcher `func_15024130` is byte-exact through
   one guarded commutative address-add word. The 34-word byte-table index
   lookup `func_15041480` is byte-exact directly from C under its recovered
   no-unroll profile. The 35-word scripted-position effect dispatcher
   `func_15076768` is byte-exact through five guarded scheduling words.
   The 35-word random-duration selector `func_1507F4C0` is byte-exact through
   six guarded frame/stack-allocation words. The 34-word owner-payload
   allocator `func_150B0C58` is byte-exact directly from C. Continue with
   The 37-word fixed-point coordinate interpolator `func_150B73F0` is
   byte-exact through 24 guarded register-allocation words. Continue with
   The 34-word command-`0x38` owner-payload allocator `func_150D5440` is
   byte-exact directly from C. The 35-word owner-event dispatcher
   `func_150F15F8` is byte-exact through nine guarded identity-register words.
   The 34-word object-entry matrix builder `func_150F2518` is byte-exact
   through seven guarded address-register words. The 34-word command-`0x5C`
   owner-payload allocator `func_150F2C8C` is byte-exact directly from C.
   The 35-word event-`0x3E` owner dispatcher `func_150F7310` is byte-exact
   through 12 guarded identity-register and load-schedule words. Resume Init
   matching from its remaining 87 different C rows. The 48-word `osMapTLB`
   slot is restored from its empty C placeholder to original handwritten
   CP0/TLB assembly and independently matches all 192 bytes. The 44-word
   `osInvalDCache` slot is likewise restored to its original handwritten cache
   routine and independently matches all 176 bytes. The 40-word `osSetIntMask`
   slot is restored to its original handwritten CP0/MI mask routine and
   independently matches all 160 bytes. The 42-word identifier dispatcher
   `func_1000DE1C` is byte-exact through two guarded local-array address words.
   The adjacent 41-word record cleanup `func_1000DEC4` is byte-exact directly
   from C after recovering its combined 32-bit tail clear and original
   non-prototype state-query call schedule.
   The following 59-word channel-transition updater `func_1000DF68` is
   byte-exact through 12 guarded clamp/store/epilogue scheduling words.
   The 51-word channel level/mask updater `func_1000E588` is byte-exact
   directly from recovered semantic C with no guards. The 46-word fixed-point
   parameter wrapper `func_10010E78` is byte-exact through one guarded
   commutative multiply word; its other 45 words emit directly from C. The
   40-word `bzero` row is restored from an approximate byte loop to original
   handwritten libultra assembly and independently matches all 160 bytes. The
   54-word released-node recycler `func_1000A348` is byte-exact through 19
   guarded manager-register and reusable-list scheduling words. The 52-word
   actor-coordinate refresh callback `func_1000EE70` is byte-exact through 18
   guarded temporary-register words; its frame, control flow, call, and actor
   update behavior emit directly from C. The 49-word mode-flag dispatch
   wrapper `func_1000CAE4` is byte-exact directly from semantic C with no
   guarded words. The 52-word packed-timer callback `func_1000EDA0` is
   byte-exact through 11 guarded temporary-register words after restoring its
   real seven-argument ABI and expiry dispatch. The 54-word single-node
   release recycler `func_10009BE4` is byte-exact through 26 guarded manager,
   sentinel, and reusable-list scheduling words. The 58-word halfword-table
   selector `func_10011EB8` is byte-exact after two bounded guards restore
   retail's redundant mapped-input copies and move the existing call
   relocation. SDK helpers `__osLeoAbnormalResume` and `__osLeoResume` are
   byte-exact directly from their recovered `-O1` libultra C bodies with no
   guards. The 60-word `osLeoDiskInit` is byte-exact from its recovered `-O1`
   initializer plus seven bounded guards that normalize one shared-address
   schedule and preserve the retail extent. The 68-word
   `_VirtualToPhysicalTask` is byte-exact directly from its recovered SDK
   copy-and-convert body with no guards. The 57-word spatial channel-value
   updater `func_1000C934` is byte-exact through 18 guarded value-register and
   epilogue scheduling words. The 60-word actor sound dispatcher
   `func_10010630` is byte-exact through 54 guarded saved-value, argument, and
   relocation scheduling words. The 65-word dual-framebuffer clear
   `func_10003ACC` is byte-exact through 57 guarded register-allocation and
   loop-scheduling words after recovering its scalar first fill and
   remainder-plus-four-pixel second fill; see
   [Working Note 600](WORKING_NOTES/600-init-dual-framebuffer-clear-match-20260930.md).
   The 67-word record mask filter `func_1000CDA0` is byte-exact after
   recovering its narrow mask ABI, validation gates, conditional flag update,
   and post-call index reload. Eighteen guards normalize its local slot and
   default-return schedule; see
   [Working Note 601](WORKING_NOTES/601-init-record-mask-filter-match-20260930.md).
   The 71-word entry mask value updater `func_1000E46C` is byte-exact
   directly from C after recovering its saturated percentage conversion,
   channel dispatch, mask update, and signed set-bit walk. Reusing the
   incoming value and mask parameters preserves retail's saved-register
   lifetimes without guards; see
   [Working Note 602](WORKING_NOTES/602-init-entry-mask-value-updater-match-20260930.md).
   The 70-word active-entry mode dispatcher `func_1000E2F4` is byte-exact
   after recovering its three-entry scan, channel stop/release paths, and
   final mode-byte store. Twelve guards normalize one non-relocating metadata
   test register cycle; see
   [Working Note 603](WORKING_NOTES/603-init-active-entry-mode-dispatcher-match-20260930.md).
   The 74-word chunked PI DMA reader `func_100046E4` is byte-exact after
   recovering its thread-selected queue, cache invalidation, `0x14000`-byte
   transfer loop, and blocking completion waits. Four guards normalize only
   the frame and message-local offsets; see
   [Working Note 604](WORKING_NOTES/604-init-chunked-pi-dma-reader-match-20260930.md).
   The 83-word spatial-volume callback `func_1000C7E8` is byte-exact after
   recovering its active-state setup and clamped radial channel calculation.
   Fifty guards normalize one closed IDO floating-point allocation and
   instruction schedule; see
   [Working Note 605](WORKING_NOTES/605-init-spatial-volume-callback-match-20260930.md).
   The 84-word framebuffer task dispatcher `func_10004DB0` is byte-exact
   after restoring its nonblocking task receive, VI framebuffer gates,
   countdown update, and phase dispatch. Nine guards normalize the remaining
   local branch schedule; see
   [Working Note 606](WORKING_NOTES/606-init-framebuffer-task-dispatcher-match-20260930.md).
   The 84-word nonrepeating random selector `func_1000F568` is byte-exact
   after recovering its bounded selection, per-record availability mask,
   cyclic fallback scan, and mask replenishment. Eleven guards normalize five
   shifted branches, five commutative operand orders, and one optimized-away
   reset assignment; see
   [Working Note 607](WORKING_NOTES/607-init-nonrepeating-random-selector-match-20260930.md).
   The 84-word planar direction encoder `func_1000B060` is byte-exact after
   recovering its vector normalization, signed-angle fold, caller offset,
   range bands, and encoded return value. Twenty-six guards normalize one
   closed FP/integer allocation and schedule; see
   [Working Note 608](WORKING_NOTES/608-init-planar-direction-encoder-match-20260930.md).
   The 85-word nearest-listener spatial query `func_100114D0` is byte-exact
   after recovering its inclusive entry scan, unsigned squared-distance
   selection, coordinate setup for `func_1000A420`, and fixed-point output
   scale. Fifty guards normalize one closed allocation and call schedule; see
   [Working Note 609](WORKING_NOTES/609-init-nearest-listener-spatial-query-match-20260930.md).
   The 97-word pending note-end query `func_1001ADA4` is byte-exact after
   restoring its SDK queue scan, accumulated event time, note-end selection,
   and allocated-to-free-list transfer. Twenty replacement guards and one
   checked insertion normalize the closed relink/return tail; see
   [Working Note 610](WORKING_NOTES/610-init-pending-note-end-query-match-20260930.md).
   The 91-word controller-pak read packet builder `__osPackRamReadData` is
   byte-exact after restoring Conker's opening 16-word PIF RAM clear. Its full
   packet construction and retained slot padding emit directly from C with no
   guards; see
   [Working Note 611](WORKING_NOTES/611-init-controller-pak-read-packet-builder-match-20260930.md).
   The 88-word channel-state initializer `func_1000E934` is byte-exact after
   recovering its paired table fills, per-channel reset and state clears,
   record-table clear, and 12 sentinel stores. Twenty-nine stale-checked
   guards normalize independent compiler scheduling, including six moved low
   relocations; see
   [Working Note 612](WORKING_NOTES/612-init-channel-state-initializer-match-20260930.md).
   The 91-word deferred-record compactor `func_10011310` is byte-exact after
   recovering its delay countdown, resource-slot release, survivor count, and
   unaligned in-place record compaction. Fifty-nine stale-checked guards,
   including ten checked insertions, preserve retail's rematerialized global
   addresses and integer-index schedule; see
   [Working Note 613](WORKING_NOTES/613-init-deferred-record-compactor-match-20260930.md).
   The 92-word audio-DMA cleanup routine `func_100099BC` is byte-exact after
   recovering its completion-queue drain, generation-expiry scan, active-list
   unlink, and free-list splice. Fifty-six stale-checked replacement guards
   and one checked insertion normalize the closed compiler allocation and
   branch schedule; see
   [Working Note 614](WORKING_NOTES/614-init-audio-dma-cleanup-match-20260930.md).
   The 93-word channel attachment routine `func_1000B3D4` is byte-exact after
   recovering its direct-parent replacement path, three-slot allocator scan,
   and idle-child retirement path. Sixty-five words emit directly from the
   recovered C; 28 stale-checked replacements normalize three closed register
   allocation cycles with no relocation rewriting; see
   [Working Note 615](WORKING_NOTES/615-init-channel-attachment-match-20260930.md).
   The 94-word SDK entrypoint `osCreateViManager` is byte-exact after
   restoring its event queues, manager state, priority handling, interrupt
   gate, and VI thread startup. Its complete routine emits directly from C
   with no guards; see
   [Working Note 616](WORKING_NOTES/616-init-create-vi-manager-match-20260930.md).
   The adjacent 102-word VI manager thread `viMgrMain` is also byte-exact
   after restoring the canonical retrace dispatch, client notification,
   timer interrupt, and 64-bit timekeeping loop. All opcodes emit directly
   from C; ten stale-checked relocation-only guards bind its discarded
   function-local static to the retail retrace-counter address. See
   [Working Note 617](WORKING_NOTES/617-init-vi-manager-main-match-20260930.md).
   The 96-word controller-pak write packet builder `__osPackRamWriteData` is
   byte-exact after restoring Conker's 16-word PIF RAM clear and the canonical
   channel-prefix loop shape. Its complete slot emits directly from C with no
   guards; see
   [Working Note 618](WORKING_NOTES/618-init-controller-pak-write-packet-builder-match-20260930.md).
   The 94-word audio-record cleanup and dispatch routine `func_1000E17C` is
   byte-exact after recovering its three passes over the twelve-record pool.
   Eighteen stale-checked replacements normalize one closed allocation and
   address-completion schedule; five relocation-only guards retain the three
   independent retail address lifetimes. See
   [Working Note 619](WORKING_NOTES/619-init-audio-record-cleanup-dispatch-match-20260930.md).
   The adjacent 140-word controller-pak write transaction
   `__osContRamWrite` is byte-exact after restoring Conker's per-attempt
   16-word PIF RAM initialization and status clear, then removing a redundant
   error reassignment so the existing channel error remains authoritative.
   Its complete routine emits directly from C with no guards; see
   [Working Note 620](WORKING_NOTES/620-init-controller-pak-write-transaction-match-20260930.md).
   The 104-word audio thread `func_10009400` is byte-exact after recovering
   its message loop, two-frame audio submission cycle, completion receive,
   shutdown dispatch, audio-manager close, and terminal receive loop. Twenty-
   seven stale-checked guards normalize local stack placement, one closed
   `s3`/`s4` allocation swap, and the close schedule; see
   [Working Note 621](WORKING_NOTES/621-init-audio-thread-loop-match-20261001.md).
   The 105-word nearest-anchor forwarding helper `func_1000F6B8` is byte-exact
   after recovering its signed-coordinate inputs, nearest-record scan, retained
   relative vectors, and twelve-argument `func_1000A420` dispatch. Sixty-eight
   stale-checked rows normalize 69 compiler-allocation and scheduling words,
   including relocation-aware address and call movement; see
   [Working Note 622](WORKING_NOTES/622-init-nearest-anchor-forwarder-match-20261001.md).
   The 109-word DMA page-cache helper `func_100097CC` is byte-exact after
   recovering its active-page hit scan, free-node allocation and doubly linked
   list repair, 0x800-byte DMA setup, frame stamp, and odd-address restoration.
   Thirty-five words emit directly from semantic C; 74 relocation-aware,
   stale-checked rows normalize compiler register allocation and scheduling.
   See
   [Working Note 623](WORKING_NOTES/623-init-dma-page-cache-helper-match-20261001.md).
   The 115-word object-aware audio dispatcher `func_10010FFC` is byte-exact
   after recovering its validity gates, camera-specific direct dispatch,
   three-quarter volume path, object-type scale lookup and clamp, position
   truncation, and spatial forwarding call. Eleven words emit directly from
   semantic C; 104 relocation-aware, stale-checked rows normalize a persistent
   compiler scheduling displacement and its resulting register allocation.
   See
   [Working Note 624](WORKING_NOTES/624-init-object-audio-dispatch-match-20261001.md).
   The adjacent 109-word audio request allocator `func_1000FA64` is byte-exact
   after recovering its bounded 32-entry allocation, callback-dependent flag
   setup, optional coordinate replacement, packed request initialization,
   cents-to-ratio conversion, queue submission, and committed-handle return.
   Nine words emit directly from semantic C; 100 relocation-aware,
   stale-checked rows normalize IDO's stack, scheduling, and register choices.
   See
   [Working Note 625](WORKING_NOTES/625-init-audio-request-allocator-match-20261001.md).
   The 119-word allocator free/coalescing routine `func_10004074` is also
   byte-exact after recovering its interrupt-protected physical-block merges,
   free-list repair and sorted insertion, tail update, and largest-free-block
   cache maintenance. Twenty-four words emit directly from semantic C; 95
   relocation-aware, stale-checked rows normalize IDO's frame, allocation,
   branch, and scheduling choices. See
   [Working Note 626](WORKING_NOTES/626-init-allocator-free-coalescing-match-20261001.md).
   The 145-word controller-pak read routine `__osContRamRead` is byte-exact
   directly from C after restoring the retry-time 16-word PIF RAM reset and
   preserving `CHNL_ERR` as the no-pak result instead of redundantly assigning
   the same value. No expected-word guards are used. See
   [Working Note 627](WORKING_NOTES/627-init-controller-pak-read-match-20261001.md).
   The 117-word direct PI copy routine `func_1000480C` is byte-exact after
   recovering its ownership and PI-busy waits, aligned word-copy path,
   two-byte-misaligned halfword path, and conditional PI-manager restart.
   Its 113-word semantic C body is normalized to retail's frame, saved-register
   allocation, and schedule by 112 stale-checked relocation-aware rows,
   including two inserted epilogue words. See
   [Working Note 628](WORKING_NOTES/628-init-direct-pi-copy-match-20261001.md).
   The 120-word packed audio-state transition routine `func_1000C350` is
   byte-exact after recovering its first-entry setup, mode-specific channel
   updates, level-0x1D state synchronization, and packed return value. All but
   one word emit directly from semantic C; one stale-checked guard preserves a
   commutative equality branch's retail operand order. See
   [Working Note 629](WORKING_NOTES/629-init-packed-audio-state-transition-match-20261001.md).
   The 125-word actor event/audio dispatcher `func_1000EFB4` is byte-exact
   after recovering its actor-presence gates, terminated actor-ID scan,
   position/result output, and three event-specific sound paths. Its complete
   500-byte body emits directly from semantic C without word guards. See
   [Working Note 630](WORKING_NOTES/630-init-actor-event-audio-dispatch-match-20261001.md).
   The 124-word actor positional-audio creator `func_10010154` is byte-exact
   after recovering its direct camera path, actor-ID-specific range and flag
   policy, prior-handle retirement, and positional replacement allocation.
   Seventy-eight words emit directly from semantic C; 46 stale-checked rows
   normalize IDO's remaining register allocation and scheduling. See
   [Working Note 631](WORKING_NOTES/631-init-actor-positional-audio-creator-match-20261001.md).
   The 126-word sequence-buffer replacement routine `func_10008CE8` is
   byte-exact after recovering its bounded stop polling, old-buffer release,
   8-byte metadata lookup, aligned replacement copy, and player restart.
   Semantic C emits 121 words directly; five stale-checked rows normalize two
   independent IDO stack-slot selections. See
   [Working Note 632](WORKING_NOTES/632-init-sequence-buffer-replacement-match-20261001.md).
   The 126-word threshold audio-state callback `func_1000B638` is byte-exact
   after recovering its player-value gate, level-specific channel transitions,
   and separate level-`0x27` effect bit. Semantic C emits 114 words directly;
   12 stale-checked rows normalize one closed register-allocation cycle and one
   stack-slot selection. See
   [Working Note 633](WORKING_NOTES/633-init-threshold-audio-state-callback-match-20261001.md).
   The 133-word actor secondary-audio creator `func_10010344` is byte-exact
   after recovering its direct camera path, actor-specific positional policy,
   prior-handle retirement, and replacement allocation. Semantic C emits 115
   words directly; 18 stale-checked rows normalize register allocation and an
   independent store schedule, including two relocation-aware rows. See
   [Working Note 634](WORKING_NOTES/634-init-actor-secondary-audio-creator-match-20261001.md).
   The 133-word three-channel audio-mix coordinator `func_1000D758` is
   byte-exact after recovering its record classification, prioritized channel
   policy, three-channel refresh, and frame-parameter forwarding. Semantic C
   emits 112 words directly; 21 stale-checked rows normalize one closed
   register-allocation cycle, including four relocation-preserving rows. See
   [Working Note 635](WORKING_NOTES/635-init-three-channel-audio-mix-coordinator-match-20261001.md).
   The 139-word audio-task submission routine `func_100095A0` is byte-exact
   after recovering its AI backlog policy, aligned output selection,
   `n_alAudioFrame` call, scheduler-task construction, queue submission, and
   command-buffer toggle. Semantic C emits 68 words directly; 71 stale-checked
   rows normalize compiler allocation and scheduling while preserving all
   relocation targets. See
   [Working Note 636](WORKING_NOTES/636-init-audio-task-submission-match-20261001.md).
4. Init's `__osGetSR`, `osGetCount`, `__osSetCompare`, `__osSetSR`, and
   `__osSetFpcCsr` placeholders are restored to original low-level assembly
   ownership. Their complete 16-byte padded spans match retail independently.
   The 26-word `func_1000FE88` is now byte-exact through two guarded,
   non-relocating current-pointer spill/reload words; its recovered C behavior
   is unchanged. The adjacent handwritten interrupt pair `__osRestoreInt` and
   `__osDisableInt` is also restored from false C placeholders; both complete
   32-byte spans match retail. The 22-word `func_100043B4` is now byte-exact
   through a guarded six-word store/call/epilogue schedule, including an
   explicit relocation move and retail's otherwise dead pointer adjustment.
   The 47-word `func_1000FD38` is also byte-exact through six guarded words
   that retain retail's loop bound across no-call iterations and refresh it
   only after a resource-release call. The nine-word `func_10001420` is now
   restored from its overflow-trampoline C model to its original handwritten
   memory-clear loop; its full 36-byte span matches retail independently. The
   11-word `func_100038E0` is likewise restored from an equivalent but
   compiler-shaped C model to its original handwritten MMIO setup body; its
   full 44-byte span matches retail independently. The empty
   `osWritebackDCacheAll` C placeholder is now replaced by its original
   handwritten 12-word cache-operation loop; its full 48-byte span matches
   retail independently. The empty `osUnmapTLB` placeholder is likewise
   replaced by its original 16-word CP0/TLB body; its full 64-byte span matches
   retail independently. The explicitly handwritten 13-word unaligned-load
   helpers `func_151F892C` and `func_151F8960` are now restored from false
   zero-return placeholders; both complete 52-byte spans match retail.
   The 19-word `func_151444DC` integer range wrapper is now byte-exact directly
   from C after expressing both adjustment loops as `do/while`, recovering
   retail's two branch-likely delay-slot updates without guarded words.
   The 20-word `func_151464B8` active-player-mask predicate is also byte-exact
   directly from C after recovering its byte return type, explicit loop
   initialization order, and masked-value lifetime. The final register-only
   mismatch was resolved with optimized-away expressions; no guarded retail
   words are used. Continue ordinary Game reconstruction with the 20-word
   generated-slice placeholder `func_1514ED3C`. That linked-list lookup is now
   reconstructed and byte-exact directly from typed C after retaining separate
   current/next pointer lifetimes and declaration order. Continue with
   20-word `func_15178BE4`. That node initializer is now reconstructed and
   byte-exact directly from typed C. The following 20-word `func_15187FC0`
   indexed color extractor is also reconstructed and byte-exact directly from
   typed C. The 21-word `func_15190400` event-owner release handler is now
   byte-exact directly from typed C as well. The following 21-word
   `func_15191B8C` unregister-and-broadcast wrapper is also byte-exact directly
   from typed C. The 21-word `func_151A4F7C` embedded-owner release handler is
   now byte-exact directly from typed C as well. The 21-word
   `func_151B22F4` slot-state predicate is also byte-exact directly from typed
   C. The 23-word `func_151D73A8` callback dispatch is now byte-exact after
   preserving retail's two volatile index and entry reads. The adjacent
   `func_151A8584`/`func_151A85D4` pair is now exact through symmetric guarded
   callback-path scheduling; see Working Note 482. The 20-word `func_1502E474`
   conditional submission wrapper and
   33-word `func_150319CC` two-pass list lookup and 21-word `func_151087FC`
   event-flag handler, 21-word `func_150EC45C` preset wrapper, and 20-word
   `func_150F2390` conditional stack-record wrapper are now byte-exact directly
   from C. The former `func_150F1684` two-local register boundary is resolved
   by the guarded match in Working Note 475.
   The 21-word `func_1514A498` motion-decay update is also byte-exact after one
   guarded word preserves retail's equivalent `multu v0,t7` operand order.
   `func_15155FD4` is now byte-exact after eight guarded words normalize the
   owner/end register allocation; see Working Note 484. The 20-word
   `func_15181DC8` per-slot reset is byte-exact after two
   guarded words preserve retail's redundant second floating zero. The
   21-word `func_1518F108` two-component decay twin is also byte-exact after
   one guarded word preserves retail's equivalent `multu v0,t7` operand
   order. The 20-word `func_15192308` embedded-address setup wrapper is now
   byte-exact directly from a typed six-argument call. The 20-word
   `func_151A73EC` bounded embedded-owner release helper is also byte-exact
   directly from nested typed C. The 20-word `func_151AF338` float ABI adapter
   is now byte-exact directly from a typed seven-argument wrapper. The 20-word
   `func_151B4C1C` embedded cleanup and callback-dispatch wrapper is now exact
   directly from typed C. The twin 20-word `func_151B50A4` float ABI adapter
   is also byte-exact from the same typed wrapper shape. The 21-word
   `func_151B7678` validated-position reader is now exact from a typed pointer
   chain and short-circuit failure condition. The 22-word `func_151B8318`
   optional matching-record release gate is now exact from typed C and an
   explicit record-word lifetime. The 22-word `func_151D8D5C` two-event
   release callback is now exact from a typed callback signature and explicit
   event branches. The 20-word `func_15083FB0` object-index wrapper is now
   exact after correcting the local `func_15083E90` byte-parameter and pointer
   return contract. The 22-word `func_1515D030` reverse-slot update is now
   exact from a signed decrement and one shared result variable.
   `func_1506EF5C` is now byte-exact after restoring retail's repeated active-
   object reads and guarding its register allocation; see Working Note 483.
   Keep `guMtxIdentF` parked at its measured compiler scheduling boundary.
   The former `func_1507A4D4` boundary is now
   resolved by the guarded match in Working Note 474. The 21-word `func_15178750`
   conditional callback wrapper and the previously hidden two-word
   `func_151787A4` table callback are now separately inventoried and exact.
   The 21-word `func_150C522C` four-slot release loop is byte-exact through
   two guarded relocation-aware words that preserve retail's independent
   low-half address-completion schedule. The 21-word `func_150C5F40`
   existing-record/allocator wrapper and its `+0x70` structural twin
   `func_150C6870` are byte-exact directly from typed C. The 21-word
   `func_150C7968` flag-gated optional-record update is byte-exact through
   five guarded schedule/relocation entries, including retail's dead pointer
   advance. The 21-word `func_150EB430` stack-vector sum wrapper is byte-exact
   after reversing commutative source operands and guarding four `a2`/`a3`
   lifetime words. The 21-word `func_15155F3C` state-transition wrapper is
   byte-exact through three guarded state-register words. The former
   `func_15155FD4` boundary is resolved in Working Note 484. The 22-word
   `func_1507A47C` packed actor-mask
   clear is now byte-exact through a named mask local and eighteen guarded
   relocation-aware scheduling words. The 24-word `func_150C5310` mode-flag
   toggle is now byte-exact directly from typed C, including three tracked
   padding words. The 24-word `func_150E2FC0` marker-record swap is now
   byte-exact from typed C plus one guarded equivalent branch-operand word.
   The 26-word `func_15125628` four-timer decrement is restored to its
   original handwritten assembly ownership. Keep `func_150721A4` parked; the
   former `func_151A8584`/`func_151A85D4` boundary is resolved in Working
   Note 482. The 33-word
   `func_1505DFDC` backing-buffer reset is byte-exact directly from C after
   restoring the full-width index, repeated table read, declaration order,
   and source store order. The apparent 60-word `func_150AD8B0` C row is now
   correctly restored to its handwritten 19-word vector cross-product body;
   its generated-slice span also covers 41 already exact padding/helper words.
   The 22-word `func_15131C2C` flag-gated callback dispatcher is byte-exact
   directly from its typed three-argument callback contract. The 24-word
   `func_1515F0AC` signed clamp is byte-exact from C plus three guarded
   scheduling entries. The 21-word `func_1516706C` callback-table loop is
   byte-exact from a post-tested loop plus two guarded relocation-aware words.
   The 29-word `func_15168A9C` list unlink, 23-word `func_15179AB8`
   backward active-object flag scan, 26-word `func_15194AB4` state mapper,
   29-word `func_151957B0` tail insertion, and two-word hidden no-op
   `func_15195824`, 22-word `func_151A8A20` bounded callback dispatcher, and
   20-word `func_151A8F1C` transform wrapper are byte-exact directly from C.
   The 21-word `func_151AA17C` dual event-record dispatch is byte-exact from
   recovered C semantics plus ten guarded scheduling/local-slot words.
   Its 21-word structural twin `func_151AA210` is independently byte-exact
   through the same C shape and separately scoped guards.
   The 21-word `func_151CF844` conditional record forwarder is byte-exact
   directly from C without guarded words. The 21-word `func_151D10E4`
   indexed record forwarder is byte-exact from recovered C semantics plus
   twelve guarded scheduling words, including relocation-aware movement of
   the `D_800AAF9C` table load.
   The 21-word `func_151D4D58` two-mode preset wrapper and 23-word
   `func_151E7E9C` three-way state dispatcher are byte-exact directly from C
   without guarded words. The 22-word `func_15022190` flagged coordinate
   setter, 24-word `func_15023870` null-gated event-byte copy, and 32-word
   `func_15033328` swimming-attachment lifetime callback are also byte-exact
   directly from C. The 22-word `func_1503378C` six-ID type predicate is also
   byte-exact directly from C. The 22-word `func_15044DE8` guarded mode-4
   dispatcher is also byte-exact directly from C. The 22-word
   `func_15088218` fixed-point/float record value is byte-exact from recovered
   C semantics plus nine guarded scheduling words. The false zero-return
   placeholder at `func_150AF738` is now a byte-exact stack-record forwarder
   from recovered C semantics plus fifteen guarded scheduling words. The false
   zero-return placeholder at `func_150BB700` is now a byte-exact event-bit
   updater directly from C. Its false-placeholder template twin
   `func_150D1BD0` is also byte-exact directly from C. The 22-word
   `func_150E411C` eight-argument parameter preset is byte-exact directly from
   C. The false zero-return placeholder at `func_150EB030` is now a byte-exact
   nested state classifier directly from C. The 22-word `func_150FB1E8`
   five-argument two-stage forwarder is byte-exact directly from C. The
   23-word `func_150FB240` signed-halfword mapper is byte-exact directly from
   C. The 22-word `func_150FFD2C` type-and-flag-gated dispatcher and 23-word
   `func_151076A4` volatile callback-table dispatcher are also byte-exact
   directly from C. The 23-word `func_1510A870` paired-record updater is
   byte-exact from recovered C semantics plus one guarded commutative-branch
   operand word. Its 25-word tracked-layout twin `func_1510A8CC` is also
   byte-exact from the same recovered C and guard; 23 words are executable and
   two are trailing layout padding. The 22-word `func_1512D6F0` indexed-record
   reset is byte-exact directly from structured C without guarded words.
   The 23-word `func_1513BA78` two-way type dispatcher is byte-exact directly
   from C after adding typed callee declarations; no guarded words are needed.
   The 37-word `func_15144598` mode-dependent area scaler is byte-exact
   directly from corrected field offsets, signed dimensions, case order, and
   commutative operand order. The 25-word `func_15149BF4` two-axis float
   damping threshold is byte-exact directly from C without guarded words.
   The 23-word `func_1514ECE0` signed-key list search is byte-exact directly
   from C as the halfword-key twin of `func_1514ED3C`, without guarded words.
   The 22-word `func_15159BB0` effect callback adapter is byte-exact directly
   from C with a position vector, zero velocity, and typed effect record.
   The 22-word `func_15172C50` two-table initializer is byte-exact directly
   from a 16-entry C loop whose body IDO unrolls four ways.
   The 22-word `func_15172D28` object state-transition wrapper is byte-exact
   directly from C, including both branch-likely early-return paths.
   The 22-word `func_151749A0` wrapped timer/counter updater is byte-exact
   directly from C with byte-width arithmetic preserved.
   The 22-word `func_1517F75C` inclusive player-timer decay loop is byte-exact
   directly from C with unsigned halfword clamping preserved.
   The 22-word `func_15181D70` enabled player-state initializer is byte-exact
   directly from C as the nonzero twin of `func_15181DC8`.
   The 24-word `func_1518A360` paired endpoint updater is byte-exact from C
   with one guarded commutative branch-operand normalization.
   The 23-word `func_151904BC` callback/resource cleanup is byte-exact from C
   with five guarded branch and call-setup scheduling words.
   The 23-word `func_15197A0C` scaled query wrapper is byte-exact directly
   from C after restoring its incoming argument. The adjacent 24-word
   `func_1519F108` and `func_1519F168` state-clear callbacks are byte-exact
   from shared C shapes plus symmetric guarded address-lifetime and branch
   scheduling normalization. The 23-word `func_151A09B4` conditional child
   teardown is byte-exact directly from C with no guarded words. The 22-word
   `func_151B4E4C` position/effect wrapper is also byte-exact directly from C.
   The 23-word `func_151EFF94` variadic formatting wrapper is byte-exact
   directly from C using the established `&arg1 + 1` argument cursor.
   The 23-word `func_15044CE4` position/scale initializer is byte-exact from
   recovered C plus seven guarded register-lifetime words. The existing C for
   36-word `func_1508855C` is byte-exact with 22 guarded register-lifetime and
   equivalent control-flow scheduling words; its two table relocations retain
   their original identities. The former 26-word `func_150A6500` row contained
   two functions: the recovered 14-word bounded-query wrapper is exact from C
   plus 12 guarded scheduling words, while newly identified 12-word
   `func_150A6538` remains exact original assembly pending a source-grounded
   calling convention. The 23-word `func_150BE438` object-record writer is
   byte-exact directly from recovered C with no guarded words. The 23-word
   `func_150D1410` object-index flag updater is also byte-exact directly from C
   with no guarded words. The 23-word `func_150D2054` six-entry cleanup loop
   is byte-exact directly from C after preserving its byte-width counter and
   indexed array expression. The tracked 25-word `func_150D32FC` event-key
   forwarder, including two trailing layout words, is also byte-exact directly
   from C. The tracked 26-word `func_150DEC28` paired table dispatcher,
   including three trailing layout words, is byte-exact directly from C using
   its original K&R byte-parameter ABI. The 24-word `func_150F4CFC` two-event
   state/teardown handler is byte-exact directly from C using a typed embedded
   state record. The tracked 29-word `func_151002BC` linked-record validator,
   including three trailing layout words, is byte-exact from recovered C plus
   seven guarded scheduling words. The 25-word `func_15125490` water-distance
   classifier is byte-exact from typed recovered C plus a guarded replacement
   of its oversized 26-word IDO body. The 23-word `func_1514EE70` object-request
   wrapper is byte-exact directly from C with no guarded words after restoring
   its callback ABI and typed eight-byte stack request. The 25-word
   `func_1514F130` state-toggle event callback is also byte-exact directly from
   typed C with no guarded words. The 24-word `func_1517F7B4` timer/phase
   updater is byte-exact from recovered C plus five guarded timer-base register
   words. The 25-word `func_151A0950` linked-record event callback is byte-exact
   directly from C with no guarded words. The 24-word `func_151A9060` indexed
   callback dispatcher is also byte-exact directly from C after recovering its
   two-argument callback ABI. The 23-word `func_151C2E94` extended record
   validity predicate is byte-exact directly from C with no guarded words. The
   34-word `func_151DADA0` phase/scale updater is byte-exact from typed embedded
   state C plus four guarded phase-register words. The 24-word Init
   `func_1000B294` owner-reference repair is byte-exact from recovered C, an
   object no-unroll profile, and two relocation-aware scheduling swaps; the
   adjacent `func_1000B548` remains exact after expressing its four-record
   unroll directly in C. The 23-word `func_150233E4` three-slot resource
   cleanup loop is byte-exact from typed C plus two relocation-aware setup
   scheduling swaps. The 24-word `func_1503B95C` indexed flag predicate is
   byte-exact directly from C with no guarded words. The 24-word
   `func_1503DA3C` bounded record-byte lookup is also byte-exact directly from
   C with no guarded words. The 24-word `func_1503F904` actor-position query
   wrapper is byte-exact directly from typed C with no guarded words. The
   24-word `func_15044D40` signed-coordinate event wrapper is also byte-exact
   directly from typed C with no guarded words. The 26-word `func_1507488C`
   packed event-mask updater is byte-exact through guarded register scheduling.
   A full rebuild also exposed and repaired the stale overflow trampoline for
   19-word `func_1506EE60`. The 24-word `func_1507EE58` complementary history
   marker wrapper is byte-exact directly from typed C with no guarded words.
   The 24-word `func_1508434C` counted object-dispatch loop and 24-word
   `func_150B58F0` tagged table-value serializer and 24-word `func_150C1660`
   typed effect-spawn wrapper are also byte-exact directly from typed C with no
   guarded words. The 24-word `func_150DF8C0` mapped record-active predicate is
   likewise exact directly from typed C. The 24-word `func_150F1CB0` actor-state
   byte selector is also exact directly from C. The 24-word `func_150F52B0`
   script-gated high-flag wrapper is likewise exact directly from C. The
   24-word `func_150FB188` actor parameter initializer is byte-exact from typed
   C plus seventeen guarded scheduling, FP-register, and relocation words.
   The 26-word `func_1510281C` and 29-word `func_151028AC` paired object-
   eligibility predicates are byte-exact directly from typed C with no guarded
   words. The 28-word `func_1510FE30` relative hierarchy-index lookup is also
   byte-exact directly from C. The 24-word `func_1513164C` nine-argument dual
   dispatcher and 24-word `func_15133760` typed eight-float forwarding wrapper
   are likewise exact directly from C. The 34-word `func_15142FBC` cache-aware
   render-mode wrapper is exact from structured C plus three guarded scheduling
   words. The 24-word `func_15143DA8` integer range clamp is exact from
   structured C plus nine guarded register-allocation words. The 29-word
   `func_151640C0` category-`0x29` identity filter is likewise exact from
   structured C plus nine guarded register-allocation words. The 27-word
   `func_1515F040` scaled signed fixed-point clamp is exact from typed C plus
   three guarded scheduling/omission entries. The 25-word `func_15166204`
   lifetime updater and expiry path is exact from C without guarded word
   patches. The 24-word `func_1517EA4C` display-list state helper is exact
   directly from three standard RDP macros. The 28-word `func_1518E298`
   linked-position callback is exact directly from C with its explicit
   four-argument callback ABI. The 24-word `func_1519ED24` scaled transform
   copy is exact from typed C plus five guarded setup-scheduling words. The
   27-word `func_1519EF04` fixed-scale transform copy is exact directly from
   typed C. The 28-word `func_151AE640` mode-driven slot updater is exact from
   structured C plus four guarded return-scheduling and branch words. The
   24-word `func_151D5E30` four-handle cleanup loop is exact from typed C plus
   three guarded null-test scheduling words. The 25-word `func_15023440`
   resource-entry reset is exact directly from structured C. The 25-word
   `func_1502DB20` resource-size selector is exact directly from a switch;
   generated-slice rodata relocation retargeting preserves its original
   64-entry jump table. The 26-word `func_1502EE8C` record-byte classifier is
   exact from typed C plus six guarded control-flow words. The 25-word Game
   `func_1503F108` indexed state initializer is exact directly from typed C.
   The 27-word Game `func_15049260` aggregate forwarding wrapper is exact
   directly from typed C. The 25-word Game `func_1507A100` packed path-record
   writer is exact from typed C plus six guarded register words. The subsequent
   ordinary queue through `func_1518804C` is also exact. The 25-word
   `func_1519F48C` linked-record retirement is exact from semantic C plus four
   guarded shared-base words. The 29-word `func_151A931C` identity-gated event
   flag update is exact from typed C plus four guarded early-return words; its
   corrected prototype also removes all 13 guards from exact caller
   `func_151A9024`. The 28-word `func_151928B0` type-result selector is exact
   from structured C plus four guarded shared-epilogue words, with its original
   five-entry jump table retained. The 25-word `func_150ADA68` floating PRNG
   step is restored to original handwritten assembly ownership after its
   equivalent C was confirmed to compile as a 26-word overflow trampoline.
   The 65-word `func_1514563C` line-projection helper is exact after restoring
   retail's dot-product operand order and guarding 18 independent frame and
   output-register choices. The 28-word `func_151B3040` paired embedded-record
   dispatch is exact directly from C with no guard rows. The 25-word
   `func_151C9ED4` four-handler event broadcast is exact from recovered C plus
   four guarded frame/local-slot words. The 26-word `func_151D13E0` owned-state
   teardown is exact directly from C with no guard rows. The 25-word
   `func_151E4E00` state-transition dispatch is exact directly from C with no
   guard rows. The 26-word `func_151E7EF8` code-integrity checksum is also
   exact directly from recovered C with no guard rows. The 163-word
   `func_151E7F60` object-slot spawn/setup routine is exact from semantic C
   plus 24 guarded stack-frame and local-slot words. The 41-word
   `func_151E8214` timed mode transition is exact directly from C with no
   guard rows. The adjacent 76-word `func_151E82B8` marker-table cursor is
   exact from semantic C plus one guarded commuted equality-branch word. The
   adjacent 50-word `func_151E83E8` timed event transition is exact directly
   from C with no guard rows. The adjacent 92-word `func_151E84B0` mode
   callback and indexed-resource setup is exact from semantic C plus two
   guarded frame-size words. The adjacent 49-word `func_151E8620` display-list
   overflow guard is exact from semantic C plus 14 guarded register-lifetime
   and scheduling words. The adjacent 175-word `func_151E86E4` scaled,
   scissored texture-rectangle writer is exact from the existing graphics
   macro plus four guarded vertical-scale register words. The adjacent
   819-word Game `func_151E89A0` HUD/status renderer is now reconstructed from
   its zero-return placeholder as semantic C, uses retail's `0x158` frame, and
   fits its original 3,276-byte slot. It remains non-matching at 803 real word
   differences, so continue its register-lifetime and scheduling pass from
   [Working Note 364](WORKING_NOTES/364-game-hud-status-renderer-reconstruction-20260928.md).
   Its adjacent 427-word `func_151E966C` player-status row renderer is
   byte-exact across retail's `0x6AC` code extent and `0x100` frame. Recovered
   SDK graphics macros and corrected scalar/cursor lifetimes reduce the
   semantic C body from 415 to 116 persistent compiler-only differences;
   relocation-aware expected-word guards normalize those stack-slot,
   register-allocation and scheduling words. See
   [Working Note 368](WORKING_NOTES/368-game-player-status-row-renderer-byte-match-20260928.md).
   The next 273-word `func_151E9D18` team-counter panel is byte-exact with
   retail's `0x444` code extent and `0xA0` frame. Recovered SDK graphics
   macros, corrected scalar types and local layout emit 271 words directly;
   two expected-word guards normalize one independent load/add schedule. See
   [Working Note 367](WORKING_NOTES/367-game-team-counter-panel-byte-match-20260928.md).
   The 20-word Init `func_10001000` entrypoint is restored from its false
   zero-return C placeholder to the original handwritten clear-and-jump
   assembly. Its 14 instruction words plus six retail padding words match
   directly with no guards. See
   [Working Note 369](WORKING_NOTES/369-init-handwritten-entrypoint-restoration-20260928.md).
   The 24-word Init `osMapTLBRdb` routine is also restored from an empty C
   placeholder to its original handwritten CP0/TLB assembly. Its 22
   instruction words plus two retail padding words match directly with no
   guards. See
   [Working Note 370](WORKING_NOTES/370-init-handwritten-maptlbrdb-restoration-20260928.md).
   The 20-word compiler-generated `__osSetHWIntrRoutine` now matches through
   its recovered libultra body and retail `-O1` object profile. The linked
   function span matches directly with no guards. See
   [Working Note 371](WORKING_NOTES/371-init-hardware-interrupt-routine-match-20260928.md).
   The 25-word `func_1000CBF0` channel-parameter updater is now byte-exact
   after restoring its 32-bit argument types and original repeated table
   accesses. See
   [Working Note 372](WORKING_NOTES/372-init-channel-parameter-updater-match-20260928.md).
   The 28-word Game `func_15004CE0` display-list address relocator is also
   byte-exact after recovering signed opcodes, the indexed cursor, and the
   opening opcode double-read. Ten guarded words normalize only compiler
   register allocation and a commutative add; see
   [Working Note 373](WORKING_NOTES/373-game-display-list-address-relocator-match-20260928.md).
   The 28-word Game `func_15033F70` object-state filter is byte-exact after
   recovering the global disable gate, attached-object type exclusions, and
   state-byte clear. All 28 words emit directly from C with no guards; see
   [Working Note 374](WORKING_NOTES/374-game-object-state-filter-match-20260928.md).
   The ordinary Game queue through 26-word `func_15157F80` is now byte-exact.
   It appends the fixed and indexed matrix commands, advances the display-list
   cursor twice, and sets the caller's ready byte. The recovered `gSPMatrix`
   form emits directly without guards; see
   [Working Note 387](WORKING_NOTES/387-game-display-list-matrix-pair-match-20260928.md).
   The following 26-word Game `func_15168B44` packed-counter update is also
   byte-exact. Its recovered typed state preserves retail's observable
   two-store packed-word update, timer refresh, and available-count path;
   twenty scoped guards close one IDO register-allocation and scheduling
   cycle without changing control flow or relocations. See
   [Working Note 388](WORKING_NOTES/388-game-packed-counter-state-match-20260928.md).
   The 26-word allocator-copy wrapper `func_15169900` and adjacent 26-word
   setup twins `func_1518E66C` and `func_1518E6D4` are now byte-exact from
   semantic C. Their recovered full-width ABI, typed record layout, allocator
   and setup calls, payload copy, and final state stores emit directly with no
   guards or compiler overrides; see
   [Working Note 389](WORKING_NOTES/389-game-allocator-copy-and-setup-pair-match-20260928.md).
   Adjacent object-ID state twins `func_151993E4` and `func_1519944C` are now
   byte-exact after recovering their six-entry identifier scan and clear/set
   writes into `D_800E0900`. Two scoped guards per function normalize only
   the retained object-ID register; see
   [Working Note 390](WORKING_NOTES/390-game-object-id-state-pair-match-20260928.md).
   The second clear/set pair `func_1519BEB8` and `func_1519BF20` is also
   byte-exact from the same six-ID semantic scan. Two scoped object-ID
   register-lifetime guards per routine close the only compiler differences;
   see
   [Working Note 391](WORKING_NOTES/391-game-second-object-id-state-pair-match-20260928.md).
   The following 26-word Game actor-target transform `func_151A4E34` is now
   byte-exact after recovering its null-target gate, actor type-nibble gate,
   64-byte target indexing, and transform-helper call. One scoped guard
   preserves only retail's commutative address-add operand order; see
   [Working Note 392](WORKING_NOTES/392-game-actor-target-transform-match-20260928.md).
   The 29-word Game timed-record lifecycle `func_1519EA04` is now byte-exact
   after recovering its enabled timer decrement, optional owner-field clear,
   and record deletion. It emits directly from semantic C with no guards; see
   [Working Note 393](WORKING_NOTES/393-game-timed-record-lifecycle-match-20260928.md).
   The 124-word Game entrypoint `func_15007830` is now byte-exact after
   recovering its startup sequence, five-entry state dispatch, signed
   halfword parameters, shared cleanup, and permanent main loop. Sixty-six
   scoped guards normalize one closed saved-register allocation cycle and two
   omitted unreachable epilogue words; see
   [Working Note 394](WORKING_NOTES/394-game-entrypoint-main-loop-match-20260928.md).
   The 30-word packed-coordinate callback `func_1518CCA8` is now byte-exact
   after recovering its packed X/Y offset update, zero-Z gate, and low-nibble
   callback dispatch. Ten scoped guards normalize one closed temporary-
   register allocation cycle; see
   [Working Note 395](WORKING_NOTES/395-game-packed-coordinate-callback-match-20260928.md).
   The 27-word 64-bit flag setter `func_1501D258` is now byte-exact after
   recovering its global enable gate and indexed bitset update. The complete
   routine emits directly from typed semantic C with no guards; see
   [Working Note 396](WORKING_NOTES/396-game-indexed-64-bit-flag-setter-match-20260928.md).
   The 26-word per-entry cleanup loop `func_15022754` is now byte-exact after
   recovering its indexed count pointer and dynamic post-call bound reload.
   It also emits directly from semantic C with no guards; see
   [Working Note 397](WORKING_NOTES/397-game-per-entry-cleanup-loop-match-20260928.md).
   The 33-word linked-list match dispatcher `func_150303E4` is now byte-exact
   after recovering its explicit zero-key return and pre-call next-pointer
   lifetime. It emits directly from semantic C with no guards; see
   [Working Note 398](WORKING_NOTES/398-game-linked-list-match-dispatcher-match-20260928.md).
   The 27-word current-record vector copier `func_1503A60C` is now byte-exact
   after recovering its destination pointer and three alias-sensitive source
   lookups. It emits directly from semantic C with no guards; see
   [Working Note 399](WORKING_NOTES/399-game-current-record-vector-copy-match-20260928.md).
   The 28-word five-bucket byte canonicalizer `func_1503D5F0` is now
   byte-exact after recovering its directly indexed nested-loop source and
   retail no-unroll compiler profile. No guards are required; see
   [Working Note 400](WORKING_NOTES/400-game-five-bucket-byte-canonicalizer-match-20260928.md).
   The 27-word two-word bit test `func_1503E1F4` is now byte-exact after
   recovering its low/high flag-word selection and shared zero-return tail.
   MIPS variable-shift masking supplies the high-word bit index. No guards are
   required; see
   [Working Note 401](WORKING_NOTES/401-game-two-word-bit-test-match-20260928.md).
   The 28-word owner status-byte clear `func_150806A8` is now byte-exact after
   recovering its two guarded byte clears and alias-sensitive owner-pointer
   reload. No guards are required; see
   [Working Note 402](WORKING_NOTES/402-game-owner-status-byte-clear-match-20260928.md).
   The 28-word seven-group byte canonicalizer `func_15084D00` is now
   byte-exact after recovering its table search and widening the cached input
   byte to reproduce retail's register allocation. No guards are required; see
   [Working Note 403](WORKING_NOTES/403-game-seven-group-byte-canonicalizer-match-20260928.md).
   The 27-word resolved-object dispatch wrapper `func_1509F5F4` is now
   byte-exact after recovering its optional validation and narrowed forwarding
   call. No guards are required; see
   [Working Note 404](WORKING_NOTES/404-game-resolved-object-dispatch-wrapper-match-20260928.md).
   The 27-word packed-record activation routine `func_150A0264` is now
   byte-exact after recovering its active/secondary flag updates, alias-safe
   source-value load, destination clear, and packed-field replacement. Twelve
   stale-checked guards normalize only a closed temporary-register allocation
   cycle; see
   [Working Note 405](WORKING_NOTES/405-game-packed-record-activation-match-20260928.md).
   The 27-word indexed coordinate setter `func_150A3444` is now byte-exact
   after recovering its signed 16-bit inputs and three direct stores into a
   52-byte record. Its alias-sensitive global-pointer reloads emit directly
   from C with no guards; see
   [Working Note 406](WORKING_NOTES/406-game-indexed-coordinate-setter-match-20260928.md).
   The 30-word staged halfword ramp `func_150B71A8` is now byte-exact after
   recovering its first-field priority, frame-scaled increments, and `0x1000`
   clamps. The complete branch-likely and early-return shape emits directly
   from C with no guards; see
   [Working Note 407](WORKING_NOTES/407-game-staged-halfword-ramp-match-20260928.md).
   The 29-word event-linked object removal filter `func_150BE150` is now
   byte-exact after recovering its event-byte narrowing, direct payload match,
   and event-zero linked-pointer match. An explicit payload local recovers the
   final retail load schedule; no guards are required. See
   [Working Note 408](WORKING_NOTES/408-game-event-linked-object-removal-match-20260928.md).
   The 27-word two-event command dispatcher `func_150C19C0` is now byte-exact
   after recovering its event-to-command mapping, owner lookup, and always-one
   return. A two-case switch emits the retail forward-branch layout directly
   from C with no guards; see
   [Working Note 409](WORKING_NOTES/409-game-two-event-command-dispatch-match-20260928.md).
   The 28-word global-gated parameter dispatcher `func_150C7870` is now
   byte-exact after recovering its two global flag tests and alternate numeric
   argument sets. The recovered `f32` callee prototype restores the retail
   register-only call convention; no guards are required. See
   [Working Note 410](WORKING_NOTES/410-game-global-gated-parameter-dispatch-match-20260928.md).
   The 27-word single-byte allocation payload wrapper `func_150D0134` is now
   byte-exact after recovering its narrow formal arguments, pointer-returning
   allocator signature, and eight-byte local payload buffer. All words emit
   directly from C with no guards; see
   [Working Note 411](WORKING_NOTES/411-game-single-byte-allocation-payload-match-20260928.md).
   The adjacent 27-word float event-payload wrapper `func_150E8854` is now
   byte-exact after recovering its event-allocation arguments, `10.0f`
   payload, successful-allocation gate, and four-byte payload copy. Semantic C
   emits 25 of 27 words directly; two expected-word guards preserve retail's
   lower local stack slot. See
   [Working Note 412](WORKING_NOTES/412-game-float-event-payload-match-20260928.md).
   The adjacent 28-word float timer reset `func_150E88C0` is now byte-exact
   after recovering its frame-delta subtraction, negative-timer random reseed,
   and follow-up event call. All words emit directly from semantic C with no
   guards; see
   [Working Note 413](WORKING_NOTES/413-game-float-timer-reset-match-20260928.md).
   The 29-word record selector-bit test `func_15114050` is now byte-exact after
   recovering its active-record gate, selector `-1` shortcut, `0xA0`-stride
   record index, and per-selector mask lookup. All words emit directly from
   semantic C with no guards; see
   [Working Note 414](WORKING_NOTES/414-game-record-selector-bit-test-match-20260928.md).
   The 27-word packed-resource lazy initializer `func_15116110` is now
   byte-exact after recovering its empty-handle gate, packed selector and byte
   extraction, seven-argument resource lookup, returned-handle store, and
   packed-word clear. Semantic C emits 20 words directly; seven guards
   preserve one closed independent mask/register scheduling cycle. See
   [Working Note 415](WORKING_NOTES/415-game-packed-resource-lazy-init-match-20260928.md).
   The 27-word partial-zero payload allocator `func_1514DA38` is now
   byte-exact after recovering its 28-byte local record, intentionally
   untouched payload word, allocation, copy, and type-`0x13` dispatch. Local
   declaration order reproduces retail's stack map; all words emit directly
   from semantic C with no guards. See
   [Working Note 416](WORKING_NOTES/416-game-partial-zero-payload-allocation-match-20260928.md).
   The 34-word three-coordinate equality classifier `func_15159230` is now
   byte-exact after recovering its unsigned mode argument, exact float
   comparisons, zero result for a full coordinate match, and mode-selected
   mismatch results. Semantic C emits 22 words directly; eleven guarded tail
   words preserve retail's ordinary branches and shared return instead of
   IDO's equivalent branch-likely folding, and normal slice padding retains
   the final `nop`. See
   [Working Note 417](WORKING_NOTES/417-game-coordinate-equality-classifier-match-20260928.md).
   The 27-word resource-install callback `func_15166F6C` is now byte-exact
   after recovering its four-argument callback ABI, global resource-pointer
   install, and nine-argument setup dispatch. Forwarding the installed global
   reproduces retail's retained destination address and complete call schedule;
   all words emit directly from semantic C with no guards. See
   [Working Note 418](WORKING_NOTES/418-game-resource-install-callback-match-20260928.md).
   The 28-word record-mediated dispatch `func_15173C90` is now byte-exact
   after recovering its narrowed record lookup, null gate, high-bit-cleared
   flags, table index, and five-argument dispatch. Semantic C emits 26 words
   directly; two expected-word guards preserve retail's ordering of two
   independent call-argument staging instructions. See
   [Working Note 419](WORKING_NOTES/419-game-record-mediated-dispatch-match-20260928.md).
   The 28-word owned cleanup-list teardown `func_15178DA4` is now byte-exact
   after recovering its resource stop, deletion-safe list walk, owner match,
   and final record teardown. Function-scope declaration order preserves the
   saved next-node cursor and retail stack slot; all words emit directly from
   semantic C with no guards. See
   [Working Note 420](WORKING_NOTES/420-game-owned-cleanup-list-teardown-match-20260928.md).
   The 27-word mapped three-byte-row dispatcher `func_1517F3A0` is now
   byte-exact after recovering its selector mapping, zero-map passthrough,
   packed row lookup, and six-argument dispatch. The early-return source shape
   reproduces retail's shared epilogue; all words emit directly from semantic
   C with no guards. See
   [Working Note 421](WORKING_NOTES/421-game-mapped-three-byte-row-dispatch-match-20260928.md).
   The 27-word event callback-table dispatcher `func_15190550` is now
   byte-exact after recovering its event-`0x2A` pre-handler, object callback
   index, nullable lookup, and three-argument forwarding call. Its typed body
   emits all words directly with no guards. See
   [Working Note 422](WORKING_NOTES/422-game-event-callback-table-dispatch-match-20260928.md).
   The 28-word four-pointer cleanup `func_151B222C` is now byte-exact after
   recovering its three-entry indexed release loop and final independent
   pointer release. An `s32` counter explicitly narrowed after each increment
   reproduces retail's saved-register loop; all words emit directly from C
   with no guards. See
   [Working Note 423](WORKING_NOTES/423-game-four-pointer-cleanup-match-20260928.md).
   The 29-word dual-layout owner release `func_151CB49C` is now byte-exact
   after recovering its event-`0x21` direct-owner comparison and event-zero
   nested-owner comparison. An explicit referenced-object local reproduces
   retail's register allocation; all words emit directly with no guards. See
   [Working Note 424](WORKING_NOTES/424-game-dual-layout-owner-release-match-20260928.md).
   The 28-word signed record-command writer `func_15034340` is now byte-exact
   after recovering its `0x32C`-byte record indexing, signed control-byte
   gate, command-6 output, and signed value scaling by 200. The deliberate
   second control-byte read and cursor update reproduce retail directly; all
   words emit from semantic C with no guards. See
   [Working Note 425](WORKING_NOTES/425-game-signed-record-command-writer-match-20260928.md).
   The 30-word gated active-object scan `func_150347E8` is now byte-exact
   after recovering its global disable gate, fixed `0x32C`-byte record walk,
   two active-pointer checks, and per-record dispatch to `func_15034728`.
   Scoping the end pointer inside the gate reproduces retail's opening address
   schedule; all words emit directly with no guards. See
   [Working Note 426](WORKING_NOTES/426-game-gated-active-object-scan-match-20260928.md).
   The 27-word signed XZ coordinate-query wrapper `func_15045714` is now
   byte-exact after recovering its query-mode selection, float truncation,
   signed-16 coordinate narrowing, selector forwarding, and output store.
   Twenty-four words emit directly from semantic C; three expected-word
   guards normalize one closed position-pointer register cycle. See
   [Working Note 427](WORKING_NOTES/427-game-signed-xz-coordinate-query-match-20260928.md).
   The 30-word quaternion hemisphere normalizer `func_15049C40` is now
   byte-exact after recovering its four-component dot product and in-place
   negation of the second quaternion when that dot product is negative. All
   30 words emit directly from semantic C with no guards. See
   [Working Note 428](WORKING_NOTES/428-game-quaternion-hemisphere-normalizer-match-20260928.md).
   The 38-word floor-threshold state trigger `func_1506D6B4` is now byte-exact
   after recovering its two early exits, health-dependent state selection,
   packed global update, and callback. Thirty-two words emit directly from
   semantic C; six guards normalize one commutative FP operand order and one
   closed integer temporary cycle. See
   [Working Note 429](WORKING_NOTES/429-game-floor-threshold-state-trigger-match-20260928.md).
   The 28-word indexed halfword-sequence dispatcher `func_15080784` is now
   byte-exact after recovering its nullable sequence gate, byte-index end
   check, optional nonzero halfword submission, and index advance. All 28
   words emit directly from semantic C with no guards. See
   [Working Note 430](WORKING_NOTES/430-game-indexed-halfword-sequence-dispatch-match-20260928.md).
   The 28-word `func_150B1DB0` is restored from its false zero-return C
   placeholder to original handwritten assembly ownership. Its two-block
   64-bit mask/rotate transform, trapping pointer increments, and complete
   linked span match retail. See
   [Working Note 431](WORKING_NOTES/431-game-handwritten-two-block-word-transform-restoration-20260928.md).
   The 35-word callback-gated record-state updater `func_150D0034` is now
   byte-exact after recovering the volatile signed callback selector and the
   promoted `~1` status-byte mask. All words emit directly from semantic C
   with no guards. See
   [Working Note 432](WORKING_NOTES/432-game-callback-gated-record-state-update-match-20260928.md).
   The 30-word allocation payload wrapper `func_150D02B4` is now byte-exact
   after recovering its signed-halfword parameter and 12-byte local record
   whose initialized eight-byte prefix is copied. All words emit directly
   from semantic C with no guards. See
   [Working Note 433](WORKING_NOTES/433-game-eight-byte-allocation-payload-match-20260928.md).
   The 28-word subtype-2 allocation payload wrapper `func_150D04C4` is now
   byte-exact after recovering its signed-halfword parameter and eight-byte
   local buffer. All words emit directly from semantic C with no guards. See
   [Working Note 434](WORKING_NOTES/434-game-single-byte-subtype2-payload-match-20260929.md).
   The 28-word damped motion-state integrator `func_150D13A0` is now
   byte-exact after recovering its five floating-field updates, three scale
   constants, and final state-refresh call. All words emit directly from
   semantic C with no guards. See
   [Working Note 435](WORKING_NOTES/435-game-damped-motion-state-integrator-match-20260929.md).
   The 29-word validated payload dispatcher `func_150ECB8C` is now byte-exact
   after recovering its target-state and selector gates, shared failure
   invalidation, and six-byte payload dispatch. All words emit directly from
   semantic C with no guards. See
   [Working Note 436](WORKING_NOTES/436-game-validated-payload-dispatch-match-20260929.md).
   The 28-word fixed payload-setup wrapper `func_150ECC00` is now byte-exact
   after recovering its two calls, fixed argument tuple, and volatile selector
   byte. All words emit directly from semantic C with no guards. See
   [Working Note 437](WORKING_NOTES/437-game-fixed-payload-setup-wrapper-match-20260929.md).
   The 28-word two-slot resource cleanup `func_150F739C` is now byte-exact
   after recovering its indexed release loop and final owner cleanup call.
   Twenty-three words emit directly from semantic C; five guards normalize
   one redundant temporary and a closed counter-register cycle. See
   [Working Note 438](WORKING_NOTES/438-game-two-slot-resource-cleanup-match-20260929.md).
   The 28-word actor-indexed spatial-effect wrapper `func_150FFB6C` is now
   byte-exact after recovering its position forwarding, actor index and
   halfword derivation, flag merge, and final effect call. All words emit
   directly from semantic C with no guards. See
   [Working Note 439](WORKING_NOTES/439-game-actor-indexed-spatial-effect-wrapper-match-20260929.md).
   The 30-word mode-gated table-value updater `func_15108BC0` is now
   byte-exact after recovering its owner-relative record lookup, sentinel
   handling, mode-byte gate, and `0x44`-byte table indexing. Nineteen words
   emit directly from semantic C; eleven guarded normalizations preserve the
   independent table-address/register schedule and explicit return-delay
   `nop`. See
   [Working Note 440](WORKING_NOTES/440-game-mode-gated-table-value-match-20260929.md).
   The 30-word two-command record updater `func_15109064` is now byte-exact
   after recovering its command `0x1D` payload copy and command `0x1E` state
   toggle. Twenty-six words emit directly from semantic C; four guarded
   normalizations preserve one commutative add and the explicit copy-path
   return schedule. See
   [Working Note 441](WORKING_NOTES/441-game-two-command-record-update-match-20260929.md).
   The 28-word record-ID lookup `func_151149AC` is now byte-exact after
   recovering its reserved-zero handling and bounded scan of `0xA0`-byte
   records for a matching ID at offset `0x72`. All words and four relocations
   emit directly from semantic C with no guards. See
   [Working Note 442](WORKING_NOTES/442-game-record-id-lookup-match-20260929.md).
   The 29-word multiplayer-slot reset `func_151298C0` is now byte-exact after
   recovering its multiplayer-mode gate and three indexed writes to the
   `0x24`-byte slot table. All words and six relocations emit directly from
   semantic C with no guards. See
   [Working Note 443](WORKING_NOTES/443-game-multiplayer-slot-reset-match-20260929.md).
   The 28-word per-slot mode initializer `func_15181D00` is now byte-exact
   after recovering its zero and active-mode state paths across four parallel
   tables. All words and twelve relocations emit directly from semantic C
   with no guards. See
   [Working Note 444](WORKING_NOTES/444-game-per-slot-mode-initializer-match-20260929.md).
   The 28-word command `0x1E` record builder `func_1518AB60` is now byte-exact
   after recovering its allocator call, null return, owner and selector
   fields, and two cleared words. Twenty-six words emit from semantic C; two
   guarded words preserve retail's selector reload/store register allocation.
   See
   [Working Note 445](WORKING_NOTES/445-game-command-1e-record-builder-match-20260929.md).
   The 28-word position-descriptor dispatch wrapper `func_151C9AC0` is now
   byte-exact after recovering its raised owner position, generated descriptor,
   and five-argument dispatch. All words and both call relocations emit
   directly from semantic C with no guards. See
   [Working Note 446](WORKING_NOTES/446-game-position-descriptor-dispatch-match-20260929.md).
   The 30-word child-pointer release loop `func_151BFB2C` is now byte-exact
   after recovering its primary pointer release and two-entry child array.
   A byte-canonicalizing loop assignment and source-ordered address expression
   reproduce retail's counter feedback and commutative add without guards. See
   [Working Note 447](WORKING_NOTES/447-game-child-pointer-release-loop-match-20260929.md).
   The 30-word selector-transition dispatcher `func_151AE06C` is now
   byte-exact after recovering its admission query, requested/current selector
   comparison, and conditional replacement path. One guarded word preserves
   a commutative equality-branch operand order. See
   [Working Note 448](WORKING_NOTES/448-game-selector-transition-dispatch-match-20260929.md).
   The 32-word timer and position updater `func_15174920` is now byte-exact
   after recovering its capped timer subtraction, expiry clear, and two signed
   position accumulators. All tracked words and both global relocations emit
   directly from semantic C with no guards. See
   [Working Note 449](WORKING_NOTES/449-game-timer-position-update-match-20260929.md).
   The 61-word projection clamp `func_15145548` is now byte-exact after
   expressing both fallback vector copies as whole-structure assignments.
   This restores retail's raw three-word copy schedule and the floating-point
   temporary allocation used by the upper clamp. All words and the helper-call
   relocation match directly from semantic C with no guards. See
   [Working Note 450](WORKING_NOTES/450-game-projection-clamp-match-20260929.md).
   The 29-word forwarding wrapper `func_1503F5B8` is now byte-exact after
   recovering its six-argument signature and typed twelve-argument call to
   `func_1505E0C4`. The complete frame, argument schedule, object-byte load,
   call relocation, and return emit directly from C with no guards. See
   [Working Note 451](WORKING_NOTES/451-game-multi-argument-forwarder-match-20260929.md).
   The 28-word active-object state updater `func_1507C370` is now byte-exact
   after recovering its bounded `D_800CC2D0` traversal and three-halfword
   pointer dispatch to `func_1507C3E0`. All words, seven relocations, and the
   loop delay-slot update emit directly from C with no guards. See
   [Working Note 452](WORKING_NOTES/452-game-active-object-state-update-match-20260929.md).
   The 29-word packed descriptor builder `func_15095060` is now byte-exact
   after recovering its optional descriptor publication, direct-or-indexed
   source selection, and packed halfword/byte copies into `D_800D2C90`.
   Relocation-aware expected-word guards normalize IDO's repeated global-base
   materialization, table-index schedule, and temporary-register lifetimes.
   See [Working Note 453](WORKING_NOTES/453-game-packed-descriptor-builder-match-20260929.md).
   The 28-word three-record dispatch loop `func_15096D08` is now byte-exact
   after recovering its mode gate, nonempty-record test, and early exit on a
   nonzero `func_15096A68` result. Its complete frame, saved-register
   lifetimes, branch-likely update, call relocation, and epilogue emit directly
   from semantic C without guards. See
   [Working Note 454](WORKING_NOTES/454-game-three-record-dispatch-loop-match-20260929.md).
   The 32-word type-gated random remainder writer `func_15084C30` is now
   byte-exact from typed C plus 14 guarded register-allocation words. See
   [Working Note 455](WORKING_NOTES/455-game-random-remainder-writer-match-20260929.md).
   The 29-word coordinate-event wrapper twins `func_150B3E74` and
   `func_150B3EE8` are now byte-exact directly from C. Each truncates the
   object's three position floats to signed halfwords, dispatches event
   `0x221` with duration `0xFA0`, and invokes its distinct final callback.
   See [Working Note 456](WORKING_NOTES/456-game-coordinate-event-wrapper-twins-match-20260929.md).
   The 28-word actor-slot creation adapter `func_150E32D0` is now byte-exact
   directly from C after recovering the 14-argument `func_150E3020` ABI, its
   zero/default fields, and the one-based result conversion. See
   [Working Note 457](WORKING_NOTES/457-game-actor-slot-creation-adapter-match-20260929.md).
   The 29-word type-`0x64` record allocator `func_15104170` is now byte-exact
   directly from C after recovering its `void` contract and complete record
   initialization. See
   [Working Note 458](WORKING_NOTES/458-game-type64-record-allocator-match-20260929.md).
   The 30-word auxiliary-record reset `func_1511A7C0` is now byte-exact
   directly from C, including its live-count float-array clearing loop and
   branch-likely base reload. See
   [Working Note 459](WORKING_NOTES/459-game-auxiliary-record-reset-match-20260929.md).
   The 29-word zero-payload record dispatcher `func_1514DAA4` is now
   byte-exact after recovering its object flag update, two-word zero payload,
   allocation, payload copy, and event-`0x13` dispatch. Two fail-closed guards
   preserve only the independent payload-size and retained-object spill
   schedule around the allocator call. See
   [Working Note 460](WORKING_NOTES/460-game-zero-payload-record-dispatch-match-20260929.md).
   The 17-word packed-byte submission wrapper `func_150721A4` is now
   byte-exact. Ordinary-object padding now honors guarded omission before its
   overflow decision, allowing three redundant IDO moves to be removed; nine
   guarded words preserve retail's equivalent register lifetimes and call
   schedule. See
   [Working Note 461](WORKING_NOTES/461-game-packed-byte-submission-wrapper-match-20260929.md).
   The 31-word accelerated-motion integrator `func_1515B994` is now
   byte-exact after recovering its timestep-based position and velocity
   updates plus the averaged-velocity secondary accumulation. Fourteen
   fail-closed guards preserve retail's equivalent floating-point register
   lifetimes and independent load/store schedule. See
   [Working Note 462](WORKING_NOTES/462-game-accelerated-motion-integrator-match-20260929.md).
   The 29-word object-record cleanup `func_1518E308` is now byte-exact
   directly from C. It clears two owner fields, releases live pointers from
   100 fixed-size records, and zeroes the complete record array. See
   [Working Note 463](WORKING_NOTES/463-game-object-record-cleanup-match-20260929.md).
   The 29-word oscillation/angle updater `func_151B8BE0` is now byte-exact
   from semantic C plus seven guarded floating-point temporary choices. See
   [Working Note 464](WORKING_NOTES/464-game-oscillation-angle-update-match-20260929.md).
   The 30-word type-selector state handler `func_15033440` is now byte-exact
   directly from C, including its shared selector path and branch-likely
   exits. See
   [Working Note 465](WORKING_NOTES/465-game-type-selector-state-handler-match-20260929.md).
   The 30-word owned float-array allocator `func_15036C70` is now byte-exact
   directly from C after retaining its initialization constant once across
   the repeated owner-pointer loads. See
   [Working Note 466](WORKING_NOTES/466-game-owned-float-array-allocator-match-20260929.md).
   The 30-word paired-mask predicate `func_1503EF4C` is now byte-exact from
   semantic C plus two commutative-operand guards, taking the Game matcher
   above 50%. See
   [Working Note 467](WORKING_NOTES/467-game-paired-mask-predicate-match-20260929.md).
   The 30-word classifier fallback wrapper `func_1504530C` is now byte-exact
   directly from C. Its unhandled switch path intentionally preserves the
   classifier's return value, matching retail. See
   [Working Note 468](WORKING_NOTES/468-game-classifier-fallback-wrapper-match-20260929.md).
   The 30-word descriptor-install wrapper `func_15094F70` is now byte-exact
   directly from C, including its ten-argument final dispatch. See
   [Working Note 469](WORKING_NOTES/469-game-descriptor-install-wrapper-match-20260929.md).
   The adjacent 30-word variable-tail descriptor wrapper `func_15094FE8` is
   also byte-exact directly from C. See
   [Working Note 470](WORKING_NOTES/470-game-variable-tail-descriptor-wrapper-match-20260929.md).
   The 30-word conditional record-dispatch wrapper `func_15095A90` is now
   byte-exact directly from C. See
   [Working Note 471](WORKING_NOTES/471-game-conditional-record-dispatch-wrapper-match-20260929.md).
   The 30-word descriptor float-forwarding adapter `func_150B9D14` is now
   byte-exact directly from C. See
   [Working Note 472](WORKING_NOTES/472-game-descriptor-float-forwarding-adapter-match-20260929.md).
   The 30-word normalized coordinate-output routine `func_1510B958` is now
   byte-exact from recovered C plus five guarded opening address/index words.
   See
   [Working Note 473](WORKING_NOTES/473-game-normalized-coordinate-output-match-20260929.md).
   The 21-word packed-mask setter `func_1507A4D4` is now byte-exact from its
   explicit mask local plus sixteen guarded packed-byte scheduling words. See
   [Working Note 474](WORKING_NOTES/474-game-packed-mask-setter-match-20260929.md).
   The 22-word event identity-release handler `func_150F1684` is now byte-exact
   from recovered C plus seven guarded identity-comparison register words. See
   [Working Note 475](WORKING_NOTES/475-game-event-identity-release-handler-match-20260929.md).
   The 26-word audio DMA prefetch wrapper `func_151F3D78` is now byte-exact
   directly from recovered C after restoring retail padding for its owning
   audio object. The clean full regeneration also cleared the stale address
   drift classification on unchanged Init routine `func_10012588`; every
   section now has zero drift rows. See
   [Working Note 476](WORKING_NOTES/476-game-audio-dma-prefetch-wrapper-match-20260929.md).
   The 31-word float-state scaler `func_151339D4` is now byte-exact directly
   from C after recovering its accumulated position field and six scaled
   float fields. See
   [Working Note 477](WORKING_NOTES/477-game-float-state-scaler-match-20260929.md).
   The 29-word angular state integrator `func_150AFBF4` is now byte-exact
   after recovering its timestep update, angle wrap, sine transform, and
   scalar output. See
   [Working Note 478](WORKING_NOTES/478-game-angular-state-integrator-match-20260929.md).
   The 30-word object type/status mapper `func_150B66DC` is now byte-exact
   directly from C after recovering its normalized three-way selector and
   target status-byte updates. See
   [Working Note 479](WORKING_NOTES/479-game-object-type-status-mapper-match-20260929.md).
   The 30-word parameter-block call adapter `func_15133510` is now byte-exact
   directly from C after recovering its three integer and eight float field
   arguments. See
   [Working Note 480](WORKING_NOTES/480-game-parameter-block-call-adapter-match-20260929.md).
   The 30-word list-node allocator wrapper `func_1514EBA4` is now byte-exact
   after recovering its allocator call, null return, and initialized payload,
   links, and signed key. Six guarded words preserve two independent retail
   scheduling cycles. See
   [Working Note 481](WORKING_NOTES/481-game-list-node-allocator-wrapper-match-20260929.md).
   Adjacent 20-word optional-callback teardown wrappers `func_151A8584` and
   `func_151A85D4` are now independently byte-exact after recovering their
   distinct callback tables and final calls. Symmetric guarded normalization
   preserves retail's path-sensitive object spill schedule. See
   [Working Note 482](WORKING_NOTES/482-game-optional-callback-teardown-pair-match-20260929.md).
   The 22-word packed indexed-byte updater `func_1506EF5C` is now byte-exact
   after recovering its sentinel/mode stores, packed selector, and two indexed
   byte writes through four repeated active-object reads. See
   [Working Note 483](WORKING_NOTES/483-game-packed-indexed-byte-updater-match-20260929.md).
   The 21-word two-owner linked-list lookup `func_15155FD4` is now byte-exact
   after recovering its two-owner scan and node-key comparison. Eight guarded
   words normalize one closed owner/end register-allocation cycle. See
   [Working Note 484](WORKING_NOTES/484-game-two-owner-linked-list-lookup-match-20260929.md).
   `func_10003BD0` is now byte-exact across its complete 28-word Init span.
   The tied Init cache-maintenance routines are now restored to original
   handwritten assembly ownership. Game object teardown `func_15106E78` is
   now byte-exact directly from semantic C. The 33-word command-row loop
   `func_150413FC` is also byte-exact from semantic C plus nine prologue-only
   scheduling guards. The 36-word state-flag updater `func_150F9A20` and
   35-word owner-event callback `func_15100230` are now byte-exact. The
   `func_1510E7A4`/`func_1510E82C`/`func_1510E8BC` render-parameter wrapper
   family is also byte-exact. The angular integrators `func_1511515C` and
   `func_151151FC`, plus displacement extender `func_15115EDC`, are now
   byte-exact. The 38-entry retail asset now establishes `func_15015F40`'s
   authoritative dispatch membership, and the function is byte-exact. Keep
   handwritten register-contract fragment `func_150A76F0` in the raw-assembly
   workstream.
   Keep `func_15194320` and `func_15194394` parked behind generated-slice
   jump-table/rodata ownership rather than introducing unresolved switches.
   Keep the documented lower-difference compiler cases parked. The tied Init
   cache rows remain in their SDK ownership lane.
   Keep the previously documented smaller special cases parked.
   Do not model control-register access through synthetic C or guarded
   retail-word replacement.
5. Treat raw-assembly conversion as a separate queue. Start by reviewing the
   smallest game-owned rows in `progress.csv`; exclude SDK, CP0, handwritten,
   and mixed code/data routines before converting anything.
6. After every source change, relink and rerun `match-progress`. Update public
   percentages only from a fresh linked scan.

The baseline and candidate list are in [Working Note 001](WORKING_NOTES/001-decomp-status-and-resume-boundary-20260924.md).
The completed pair and compiler-shape evidence are in
[Working Note 002](WORKING_NOTES/002-paired-event-swap-byte-match-20260924.md).
The completed debugger rectangle fill and guarded scheduling normalization are
in [Working Note 003](WORKING_NOTES/003-debugger-rectangle-fill-byte-match-20260924.md).
The completed context display and its guarded allocation normalization are in
[Working Note 007](WORKING_NOTES/007-debugger-context-display-byte-match-20260925.md).
The four completed game near-matches and generated-slice patch support are in
[Working Note 012](WORKING_NOTES/012-generated-near-match-normalization-20260925.md).
The final debugger inventory and handwritten-routine byte audit are in
[Working Note 013](WORKING_NOTES/013-debugger-completion-audit-20260925.md).
The two restored assembly boundaries are in
[Working Note 014](WORKING_NOTES/014-small-game-assembly-boundaries-20260925.md).
The two completed game record setters are in
[Working Note 015](WORKING_NOTES/015-game-record-pointer-byte-matches-20260925.md).
The completed two-field identifier check is in
[Working Note 016](WORKING_NOTES/016-game-identifier-check-byte-match-20260925.md).
The completed indexed counter update is in
[Working Note 017](WORKING_NOTES/017-game-indexed-counter-byte-match-20260925.md).
The completed packed-field writer is in
[Working Note 018](WORKING_NOTES/018-game-packed-field-writer-byte-match-20260925.md).
The completed two-difference game queue is in
[Working Note 019](WORKING_NOTES/019-final-two-difference-game-matches-20260925.md).
The restored original trigonometry slice is in
[Working Note 020](WORKING_NOTES/020-game-trigonometry-assembly-restoration-20260925.md).
The completed indexed-byte lookup is in
[Working Note 021](WORKING_NOTES/021-game-indexed-byte-lookup-match-20260925.md).
The completed nested-pointer update is in
[Working Note 022](WORKING_NOTES/022-game-nested-pointer-update-match-20260925.md).
The completed float-bound load reorder is in
[Working Note 023](WORKING_NOTES/023-game-float-bound-load-order-match-20260925.md).
The completed optional-callback cleanup is in
[Working Note 024](WORKING_NOTES/024-game-optional-callback-match-20260925.md).
The completed call-argument normalization and closed three-difference queue are
in [Working Note 025](WORKING_NOTES/025-game-call-argument-register-match-20260925.md).
The completed stack-local layout correction is in
[Working Note 026](WORKING_NOTES/026-game-stack-local-layout-match-20260925.md).
The completed global-base pointer lifetime is in
[Working Note 027](WORKING_NOTES/027-game-global-base-pointer-match-20260925.md).
The completed optional-pointer call lifetime is in
[Working Note 028](WORKING_NOTES/028-game-optional-pointer-call-match-20260925.md).
The restored synthetic-return trampoline is in
[Working Note 029](WORKING_NOTES/029-game-synthetic-return-trampoline-20260925.md).
The restored handwritten PRNG seed setter is in
[Working Note 030](WORKING_NOTES/030-game-prng-seed-setter-restoration-20260925.md).
The completed scalar-temporary normalization is in
[Working Note 031](WORKING_NOTES/031-game-scalar-temporary-match-20260925.md).
The completed set-bit temporary normalization is in
[Working Note 032](WORKING_NOTES/032-game-set-bit-temporary-match-20260925.md).
The completed opening-load scheduling normalization is in
[Working Note 033](WORKING_NOTES/033-game-opening-load-schedule-match-20260925.md).
The restored no-op callback assembly boundary is in
[Working Note 034](WORKING_NOTES/034-game-noop-callback-restoration-20260925.md).
The completed motion-scale register normalization is in
[Working Note 035](WORKING_NOTES/035-game-motion-scale-register-match-20260925.md).
The completed indexed-slot clear is in
[Working Note 036](WORKING_NOTES/036-game-indexed-slot-clear-match-20260925.md).
The completed call-ABI correction is in
[Working Note 037](WORKING_NOTES/037-game-forwarded-call-abi-match-20260925.md).
The completed table-stride expression recovery is in
[Working Note 038](WORKING_NOTES/038-game-table-stride-match-20260925.md).
The restored handwritten byte-fill loop is in
[Working Note 039](WORKING_NOTES/039-game-handwritten-byte-fill-restoration-20260925.md).
The completed packed fixed-point reader is in
[Working Note 040](WORKING_NOTES/040-game-packed-fixed-point-reader-match-20260925.md).
The completed packed-value scaling cluster is in
[Working Note 041](WORKING_NOTES/041-game-packed-value-scaling-cluster-20260925.md).
The completed viewport setup normalization is in
[Working Note 042](WORKING_NOTES/042-game-viewport-setup-frame-match-20260925.md).
The completed sound-command wrapper scheduling is in
[Working Note 043](WORKING_NOTES/043-game-sound-command-wrapper-match-20260925.md).
The restored dead-pointer-expression assembly boundary is in
[Working Note 044](WORKING_NOTES/044-game-dead-pointer-expression-restoration-20260925.md).
The completed destination-pointer scheduling is in
[Working Note 045](WORKING_NOTES/045-game-destination-pointer-schedule-match-20260925.md).
The completed countdown register normalization is in
[Working Note 046](WORKING_NOTES/046-game-countdown-register-match-20260925.md).
The completed retained-field wrapper is in
[Working Note 047](WORKING_NOTES/047-game-retained-field-wrapper-match-20260925.md).
The completed quadrant register normalization is in
[Working Note 048](WORKING_NOTES/048-game-quadrant-register-match-20260925.md).
The completed outer/child pointer normalization is in
[Working Note 049](WORKING_NOTES/049-game-outer-child-pointer-match-20260925.md).
The completed source/destination pointer pair is in
[Working Note 050](WORKING_NOTES/050-game-source-destination-pointer-pair-20260925.md).
The completed high-half call wrapper is in
[Working Note 051](WORKING_NOTES/051-game-high-half-call-wrapper-20260925.md).
The restored dead child-pointer assembly boundary is in
[Working Note 052](WORKING_NOTES/052-game-dead-child-pointer-restoration-20260925.md).
The restored structural twin is in
[Working Note 053](WORKING_NOTES/053-game-dead-child-pointer-twin-restoration-20260925.md).
The completed indexed-record flag update is in
[Working Note 054](WORKING_NOTES/054-game-indexed-record-flag-match-20260925.md).
The completed allocation-wrapper frame normalization is in
[Working Note 055](WORKING_NOTES/055-game-allocation-wrapper-frame-match-20260925.md).
The third restored dead child-pointer family member is in
[Working Note 056](WORKING_NOTES/056-game-dead-child-pointer-third-restoration-20260925.md).
The completed slot-cursor allocation is in
[Working Note 098](WORKING_NOTES/098-game-slot-cursor-allocation-match-20260926.md).
The completed chunked-boundary loop is in
[Working Note 099](WORKING_NOTES/099-game-chunked-boundary-loop-match-20260926.md).
The completed packed four-byte reader is in
[Working Note 100](WORKING_NOTES/100-game-packed-four-byte-reader-match-20260926.md).
The completed retained local-record pointer is in
[Working Note 101](WORKING_NOTES/101-game-retained-local-record-pointer-match-20260926.md).
The completed null-first table-populator path is in
[Working Note 102](WORKING_NOTES/102-game-null-first-table-populator-match-20260926.md).
The restored fourth-component trampoline continuation is in
[Working Note 103](WORKING_NOTES/103-game-fourth-component-continuation-restoration-20260926.md).
The completed record-pointer and repeated-field lifetime is in
[Working Note 104](WORKING_NOTES/104-game-record-pointer-repeated-field-match-20260926.md).
The completed two-component scaling loop is in
[Working Note 105](WORKING_NOTES/105-game-two-component-scaling-loop-match-20260926.md).
The completed embedded vertex-copy base lifetime is in
[Working Note 106](WORKING_NOTES/106-game-embedded-vertex-copy-match-20260926.md).
The completed angle-normalization register lifetime and opening schedule are
in [Working Note 107](WORKING_NOTES/107-game-angle-normalization-match-20260926.md).
The completed conditional callback dispatch is in
[Working Note 108](WORKING_NOTES/108-game-conditional-dispatch-match-20260926.md).
The completed four-slot release loop is in
[Working Note 218](WORKING_NOTES/218-game-four-slot-release-loop-match-20260926.md).
The completed existing-record/allocator wrapper is in
[Working Note 219](WORKING_NOTES/219-game-existing-record-wrapper-match-20260926.md).
The completed `+0x70` structural twin is in
[Working Note 220](WORKING_NOTES/220-game-existing-record-wrapper-twin-match-20260926.md).
The completed flag-gated optional-record update is in
[Working Note 221](WORKING_NOTES/221-game-flag-gated-record-update-match-20260926.md).
The completed stack-vector sum wrapper is in
[Working Note 222](WORKING_NOTES/222-game-stack-vector-sum-wrapper-match-20260927.md).
The completed state-transition wrapper is in
[Working Note 223](WORKING_NOTES/223-game-state-transition-wrapper-match-20260927.md).
The completed marker-record swap is in
[Working Note 226](WORKING_NOTES/226-game-marker-record-swap-match-20260927.md).
The restored handwritten four-timer decrement is in
[Working Note 227](WORKING_NOTES/227-game-four-timer-decrement-restoration-20260927.md).
The completed backing-buffer reset is in
[Working Note 228](WORKING_NOTES/228-game-backing-buffer-reset-match-20260927.md).
The restored handwritten vector cross product is in
[Working Note 229](WORKING_NOTES/229-game-vector-cross-product-restoration-20260927.md).
The completed flag-gated callback dispatcher is in
[Working Note 230](WORKING_NOTES/230-game-flag-gated-callback-dispatch-match-20260927.md).
The completed signed fixed-point clamp and guarded omission support are in
[Working Note 231](WORKING_NOTES/231-game-signed-fixed-point-clamp-match-20260927.md).
The completed three-entry callback-table loop is in
[Working Note 232](WORKING_NOTES/232-game-callback-table-loop-match-20260927.md).
The completed indexed-list unlink is in
[Working Note 233](WORKING_NOTES/233-game-indexed-list-unlink-match-20260927.md).
The completed backward active-object flag scan is in
[Working Note 234](WORKING_NOTES/234-game-active-object-flag-scan-match-20260927.md).
The completed state-to-animation selector is in
[Working Note 235](WORKING_NOTES/235-game-state-animation-selector-match-20260927.md).
The completed list-tail insertion and hidden no-op boundary are in
[Working Note 236](WORKING_NOTES/236-game-list-tail-insert-and-hidden-noop-match-20260927.md).
The completed bounded callback dispatcher is in
[Working Note 237](WORKING_NOTES/237-game-bounded-callback-dispatch-match-20260927.md).
The completed coordinate-transform wrapper is in
[Working Note 238](WORKING_NOTES/238-game-coordinate-transform-wrapper-match-20260927.md).
The completed stack-record pointer lifetime is in
[Working Note 109](WORKING_NOTES/109-game-stack-record-pointer-match-20260926.md).
The completed five-global reset ordering is in
[Working Note 110](WORKING_NOTES/110-game-global-reset-order-match-20260926.md).
The completed byte-gated optional call is in
[Working Note 111](WORKING_NOTES/111-game-byte-gated-call-match-20260926.md).
The completed record-value adjuster and its single commutative-multiply guard
are in
[Working Note 375](WORKING_NOTES/375-game-record-value-adjuster-match-20260928.md).
The completed sequence-state advance and its six relocation-aware register
allocation guards are in
[Working Note 376](WORKING_NOTES/376-game-sequence-state-advance-match-20260928.md).
The completed active-record counter, its no-unroll object profile, and four
relocation-aware opening-schedule guards are in
[Working Note 377](WORKING_NOTES/377-game-active-record-counter-match-20260928.md).
The completed record-output accessor and its direct-from-C match are in
[Working Note 378](WORKING_NOTES/378-game-record-output-accessor-match-20260928.md).
The completed actor-position query and its direct-from-C match are in
[Working Note 379](WORKING_NOTES/379-game-actor-position-query-match-20260928.md).
The completed dual event-byte dispatcher and its guarded frame-layout match are
in [Working Note 380](WORKING_NOTES/380-game-dual-event-byte-dispatch-match-20260928.md).
The completed memory viewer and its restored address/data lifetimes are in
[Working Note 009](WORKING_NOTES/009-debugger-memory-view-byte-match-20260925.md).
