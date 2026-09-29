# Current Decomp Status

Last verified: 2026-09-29

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

Fresh `progress.csv` and linked retail comparison on 2026-09-29:

| Section | C functions | Raw assembly | C bytes |
| --- | ---: | ---: | ---: |
| Total | 5,465 / 6,041 (90.47%) | 576 | 1,931,188 / 2,256,728 (85.57%) |
| Init | 495 / 538 (92.01%) | 43 | 148,424 / 164,048 (90.48%) |
| Game | 4,789 / 5,321 (90.00%) | 532 | 1,763,124 / 2,072,880 (85.06%) |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) |

| Section | Byte-exact C | Address drift | Different C |
| --- | ---: | ---: | ---: |
| Total | 2,982 / 5,465 (54.57%) | 0 | 2,483 |
| Init | 394 / 495 (79.60%) | 0 | 101 |
| Game | 2,407 / 4,789 (50.26%) | 0 | 2,382 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The full debugger inventory is complete: all 181 C-classified tracked rows are
linked byte-exact, and the sole remaining assembly row, the original
handwritten 40-word CP0/TLB routine `func_16003650`, independently matches all
40 retail words. It remains assembly by design because IDO C cannot emit its
`mtc0`, `tlbr`, and `mfc0` instruction sequence. Thus all 182 debugger rows
are accounted for and exact; 181 / 181 is only the C-matcher denominator.

The percentage increase from the old July matching snapshot remains primarily
denominator driven: the exact count is now 2,969, while
506 functions moved from C back to assembly. The paired event-swap pass added
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

## Verified build state

These commands passed from the current checkout on 2026-09-29:

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
   record identifier lifetime, with no guarded words. Continue with 19-word
   `func_151444DC`, the next ordinary Game C row with eighteen real
   differences.
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
   preserving retail's two volatile index and entry reads. Keep
   `func_151A8584`/`func_151A85D4` parked at their measured callback scheduling
   boundary. The 20-word `func_1502E474` conditional submission wrapper and
   33-word `func_150319CC` two-pass list lookup and 21-word `func_151087FC`
   event-flag handler, 21-word `func_150EC45C` preset wrapper, and 20-word
   `func_150F2390` conditional stack-record wrapper are now byte-exact directly
   from C. The former `func_150F1684` two-local register boundary is resolved
   by the guarded match in Working Note 475.
   The 21-word `func_1514A498` motion-decay update is also byte-exact after one
   guarded word preserves retail's equivalent `multu v0,t7` operand order.
   `func_15155FD4` is behaviorally recovered but parked at a register-allocation
   boundary. The 20-word `func_15181DC8` per-slot reset is byte-exact after two
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
   exact from a signed decrement and one shared result variable. Keep
   `guMtxIdentF` and `func_1506EF5C` parked at their measured compiler
   scheduling/register boundaries. The former `func_1507A4D4` boundary is now
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
   byte-exact through three guarded state-register words. Keep
   `func_15155FD4` parked. The 22-word `func_1507A47C` packed actor-mask
   clear is now byte-exact through a named mask local and eighteen guarded
   relocation-aware scheduling words. The 24-word `func_150C5310` mode-flag
   toggle is now byte-exact directly from typed C, including three tracked
   padding words. The 24-word `func_150E2FC0` marker-record swap is now
   byte-exact from typed C plus one guarded equivalent branch-operand word.
   The 26-word `func_15125628` four-timer decrement is restored to its
   original handwritten assembly ownership. Keep `func_150721A4` and the
   `func_151A8584`/`func_151A85D4` pair parked. The 33-word
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
   `func_10003BD0` was audited across several C shapes and remains at 25 real
   differences; keep it open without retaining experimental source. Resume
   with an ordinary small Game placeholder after the already documented
   parked compiler-scheduling cases. Keep `func_15015F40` parked until its
   unresolved 38-entry indirect table has authoritative ownership, and keep
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
