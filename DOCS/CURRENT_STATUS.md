# Current Decomp Status

Last verified: 2026-09-25

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

Fresh `progress.csv` and linked retail comparison on 2026-09-25:

| Section | C functions | Raw assembly | C bytes |
| --- | ---: | ---: | ---: |
| Total | 5,484 / 6,038 (90.82%) | 554 | 1,932,736 / 2,256,728 (85.64%) |
| Init | 508 / 538 (94.42%) | 30 | 148,936 / 164,048 (90.79%) |
| Game | 4,795 / 5,318 (90.17%) | 523 | 1,764,160 / 2,072,880 (85.11%) |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) |

| Section | Byte-exact C | Address drift | Different C |
| --- | ---: | ---: | ---: |
| Total | 2,578 / 5,484 (47.01%) | 1 | 2,905 |
| Init | 387 / 508 (76.18%) | 1 | 120 |
| Game | 2,010 / 4,795 (41.92%) | 0 | 2,785 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The full debugger inventory is complete: all 181 C-classified tracked rows are
linked byte-exact, and the sole remaining assembly row, the original
handwritten 40-word CP0/TLB routine `func_16003650`, independently matches all
40 retail words. It remains assembly by design because IDO C cannot emit its
`mtc0`, `tlbr`, and `mfc0` instruction sequence. Thus all 182 debugger rows
are accounted for and exact; 181 / 181 is only the C-matcher denominator.

The percentage increase from the old July matching snapshot remains primarily
denominator driven: the exact count is now 2,570, while
493 functions moved from C back to assembly. The paired event-swap pass added
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
`func_10012588` remains the sole address-drift blocker.

## Verified build state

These commands passed from the current checkout on 2026-09-25:

```sh
make -C conker replace NON_MATCHING=1 -j4
make tools-check
make NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

The successful non-matching build establishes that the current source links
and emits `conker.us.bin`. It does not establish a matching ROM hash or fresh
end-to-end gameplay acceptance.

## Resume boundary

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
   guarded words. Continue with 10-word `func_151E81EC`, the last
   nine-difference game row.
4. Treat raw-assembly conversion as a separate queue. Start by reviewing the
   smallest game-owned rows in `progress.csv`; exclude SDK, CP0, handwritten,
   and mixed code/data routines before converting anything.
5. After every source change, relink and rerun `match-progress`. Update public
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
The completed memory viewer and its restored address/data lifetimes are in
[Working Note 009](WORKING_NOTES/009-debugger-memory-view-byte-match-20260925.md).
