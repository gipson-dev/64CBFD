# PC Port Roadmap located in another project folder

## Cross-project progress - 2026-09-29

The active Windows port remains in sibling `64CBFDOGL`; this repository owns
the guest decompilation and retail-byte evidence used by that port. The current
measured decomp checkpoint is:

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,465 / 6,041 (90.47%) | 2,964 / 5,465 (54.24%) | 1 | 2,500 |
| Init | 495 / 538 (92.01%) | 393 / 495 (79.39%) | 1 | 101 |
| Game | 4,789 / 5,321 (90.00%) | 2,390 / 4,789 (49.91%) | 0 | 2,399 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Debugger is fully accounted for across all 182 rows. The table keeps the raw
conversion distinction because `func_16003650` is original handwritten
CP0/TLB assembly, but a direct linked-ELF comparison confirms that all 40 of
its words match retail. There is no remaining debugger conversion or matching
work.

The current debugger restoration batch is banked in focused commits.
`func_16001390`, `func_16000F8C`, `func_160014F0`, `func_16001BB4`,
`func_16000590`, `func_16001044`, `func_1600078C`, and `func_16000B14` are
byte-exact in the linked ELF. Debugger matching is complete at 181 / 181. The
game routine `func_15135480` and former one-difference rows `func_150AF2E0`,
`func_151061EC`, `func_15144A74`, and `func_151ACB60` are also byte-exact. See
[Current Decomp Status](CURRENT_STATUS.md) and
[Working Note 012](WORKING_NOTES/012-generated-near-match-normalization-20260925.md).
The complete debugger accounting is recorded in
[Working Note 013](WORKING_NOTES/013-debugger-completion-audit-20260925.md).
The latest game triage restored a shared epilogue and handwritten syscall to
assembly ownership; see
[Working Note 014](WORKING_NOTES/014-small-game-assembly-boundaries-20260925.md).
The next focused game pass completed the two record setters
`func_15087FC4` and `func_15087FEC`; see
[Working Note 015](WORKING_NOTES/015-game-record-pointer-byte-matches-20260925.md).
The following focused pass completed `func_1519C910`; see
[Working Note 016](WORKING_NOTES/016-game-identifier-check-byte-match-20260925.md).
The next focused pass completed `func_1517F448`; see
[Working Note 017](WORKING_NOTES/017-game-indexed-counter-byte-match-20260925.md).
The following focused pass completed `func_15079F6C`; see
[Working Note 018](WORKING_NOTES/018-game-packed-field-writer-byte-match-20260925.md).
The final two-difference pass completed `func_1516968C` and `func_151696DC`;
see [Working Note 019](WORKING_NOTES/019-final-two-difference-game-matches-20260925.md).
The next triage restored the original sine/cosine assembly slice beginning at
`func_150AD780`; see
[Working Note 020](WORKING_NOTES/020-game-trigonometry-assembly-restoration-20260925.md).
The following source-level pass completed `func_150849A0`; see
[Working Note 021](WORKING_NOTES/021-game-indexed-byte-lookup-match-20260925.md).
The next guarded register-lifetime pass completed `func_150636A4`; see
[Working Note 022](WORKING_NOTES/022-game-nested-pointer-update-match-20260925.md).
The following guarded scheduling pass completed `func_1514672C`; see
[Working Note 023](WORKING_NOTES/023-game-float-bound-load-order-match-20260925.md).
The next source-level pointer-lifetime pass completed `func_15199980`; see
[Working Note 024](WORKING_NOTES/024-game-optional-callback-match-20260925.md).
The final three-difference pass completed `func_1505D024`; see
[Working Note 025](WORKING_NOTES/025-game-call-argument-register-match-20260925.md).
The next source-level pass completed `func_15071A64` by restoring the retail
stack-local layout; see
[Working Note 026](WORKING_NOTES/026-game-stack-local-layout-match-20260925.md).
The following source-level pointer-lifetime pass completed `func_15087DCC`; see
[Working Note 027](WORKING_NOTES/027-game-global-base-pointer-match-20260925.md).
The next guarded register-lifetime pass completed `func_1509D054`; see
[Working Note 028](WORKING_NOTES/028-game-optional-pointer-call-match-20260925.md).
The following classification pass restored `func_150A7A00` as its original
synthetic-return assembly trampoline; see
[Working Note 029](WORKING_NOTES/029-game-synthetic-return-trampoline-20260925.md).
The next classification pass restored handwritten PRNG seed setter
`func_150ADACC`; see
[Working Note 030](WORKING_NOTES/030-game-prng-seed-setter-restoration-20260925.md).
The following guarded scalar-temporary pass completed `func_150BDB3C`; see
[Working Note 031](WORKING_NOTES/031-game-scalar-temporary-match-20260925.md).
The next guarded set-bit temporary pass completed `func_150F33B0`; see
[Working Note 032](WORKING_NOTES/032-game-set-bit-temporary-match-20260925.md).
The following relocation-preserving scheduling pass completed
`func_151254F4`; see
[Working Note 033](WORKING_NOTES/033-game-opening-load-schedule-match-20260925.md).
The next classification pass restored `func_1515FB70` to its original
nine-word assembly extent; see
[Working Note 034](WORKING_NOTES/034-game-noop-callback-restoration-20260925.md).
The following guarded register pass completed `func_1505841C`; see
[Working Note 035](WORKING_NOTES/035-game-motion-scale-register-match-20260925.md).
The next indexed-slot pass completed `func_150F02A0`; see
[Working Note 036](WORKING_NOTES/036-game-indexed-slot-clear-match-20260925.md).
The following source-level call-ABI pass completed `func_151B2FA0`; see
[Working Note 037](WORKING_NOTES/037-game-forwarded-call-abi-match-20260925.md).
The next source-level table-stride pass completed `func_150770E4`; see
[Working Note 038](WORKING_NOTES/038-game-table-stride-match-20260925.md).
The following classification pass restored handwritten byte-fill loop
`func_150A7770`; see
[Working Note 039](WORKING_NOTES/039-game-handwritten-byte-fill-restoration-20260925.md).
The next guarded pointer/value register pass completed `func_1515F008`; see
[Working Note 040](WORKING_NOTES/040-game-packed-fixed-point-reader-match-20260925.md).
The following packed-value scaling pass completed `func_1516F8EC`,
`func_1516F91C`, and `func_1516F984`; see
[Working Note 041](WORKING_NOTES/041-game-packed-value-scaling-cluster-20260925.md).
The next guarded frame/address pass completed `func_15019BB8`; see
[Working Note 042](WORKING_NOTES/042-game-viewport-setup-frame-match-20260925.md).
The following guarded argument-scheduling pass completed `func_1509F6B0`; see
[Working Note 043](WORKING_NOTES/043-game-sound-command-wrapper-match-20260925.md).
The next classification pass restored `func_150C7930` to its original
14-word assembly extent because IDO removes retail's dead pointer expression;
see [Working Note 044](WORKING_NOTES/044-game-dead-pointer-expression-restoration-20260925.md).
The following guarded destination-pointer scheduling pass completed
`func_150CDB6C`; see
[Working Note 045](WORKING_NOTES/045-game-destination-pointer-schedule-match-20260925.md).
The next guarded register-lifetime pass completed `func_15108B80`; see
[Working Note 046](WORKING_NOTES/046-game-countdown-register-match-20260925.md).
The following ABI and retained-field pass completed `func_1513A594`; see
[Working Note 047](WORKING_NOTES/047-game-retained-field-wrapper-match-20260925.md).
The next guarded quadrant/table-index pass completed `func_151423D8`; see
[Working Note 048](WORKING_NOTES/048-game-quadrant-register-match-20260925.md).
The following guarded outer/child pointer pass completed `func_15155EF8`; see
[Working Note 049](WORKING_NOTES/049-game-outer-child-pointer-match-20260925.md).
The next source-level pointer-order pass completed `func_151D7770` and
`func_151D779C`, closing the seven-difference game tier; see
[Working Note 050](WORKING_NOTES/050-game-source-destination-pointer-pair-20260925.md).
The following source-level narrowing pass completed `func_1509F248`; see
[Working Note 051](WORKING_NOTES/051-game-high-half-call-wrapper-20260925.md).
The next ownership audit restored `func_150C5EFC` to its original assembly
extent; see
[Working Note 052](WORKING_NOTES/052-game-dead-child-pointer-restoration-20260925.md).
Its structural twin `func_150C682C` received the same ownership correction;
see
[Working Note 053](WORKING_NOTES/053-game-dead-child-pointer-twin-restoration-20260925.md).
The following register-lifetime pass completed `func_150EA904`; see
[Working Note 054](WORKING_NOTES/054-game-indexed-record-flag-match-20260925.md).
The next frame-layout pass completed `func_1515D480`; see
[Working Note 055](WORKING_NOTES/055-game-allocation-wrapper-frame-match-20260925.md).
The following ownership audit restored `func_151AB180`, the third dead
child-pointer family member; see
[Working Note 056](WORKING_NOTES/056-game-dead-child-pointer-third-restoration-20260925.md).
The final eight-difference ownership audit restored `func_151EF610`; see
[Working Note 057](WORKING_NOTES/057-game-global-prng-step-restoration-20260925.md).
The first nine-difference pass completed `func_150771F0`; see
[Working Note 058](WORKING_NOTES/058-game-argument-load-schedule-match-20260925.md).
The next source-level pass completed `func_15080200`; see
[Working Note 059](WORKING_NOTES/059-game-chained-global-clear-match-20260925.md).
The generated display-list cursor pass completed `func_1510E634`; see
[Working Note 060](WORKING_NOTES/060-game-display-list-cursor-expansion-20260925.md).
The following register-lifetime pass completed `func_1512D6B0`; see
[Working Note 061](WORKING_NOTES/061-game-record-stride-register-match-20260925.md).
The second display-list cursor pass completed `func_15166FD8`; see
[Working Note 062](WORKING_NOTES/062-game-display-list-cursor-twin-match-20260925.md).
The callback selector register pass completed `func_15196330`; see
[Working Note 063](WORKING_NOTES/063-game-callback-selector-register-match-20260925.md).
Its structural twin `func_151963B4` is independently complete; see
[Working Note 064](WORKING_NOTES/064-game-callback-selector-twin-match-20260925.md).
The following source-level control-flow pass completed `func_151E5F64`; see
[Working Note 065](WORKING_NOTES/065-game-indexed-byte-selector-match-20260925.md).
The final nine-difference pass restored `func_151E81EC`; see
[Working Note 066](WORKING_NOTES/066-game-four-word-state-clear-match-20260925.md).
The first ten-difference pass completed `func_1502EA0C`; see
[Working Note 067](WORKING_NOTES/067-game-packed-byte-writer-match-20260925.md).
The linked-list loop pass completed `func_15033E84`; see
[Working Note 068](WORKING_NOTES/068-game-linked-list-search-match-20260925.md).
The next display-list cursor pass completed `func_15094F40`; see
[Working Note 069](WORKING_NOTES/069-game-display-list-state-clear-match-20260925.md).
Its state-byte-clear relative `func_15096934` is independently complete; see
[Working Note 070](WORKING_NOTES/070-game-display-list-state-byte-match-20260925.md).
The following source-level lifetime pass completed `func_150CF578`; see
[Working Note 071](WORKING_NOTES/071-game-global-coordinate-update-match-20260925.md).
The next source-level short-circuit pass completed `func_150DE2C4`; see
[Working Note 072](WORKING_NOTES/072-game-short-circuit-threshold-match-20260925.md).
The following placeholder-conversion pass completed `func_151318E8`; see
[Working Note 073](WORKING_NOTES/073-game-repeated-float-scale-match-20260925.md).
The next float-state reset pass completed `func_15133A50`; see
[Working Note 074](WORKING_NOTES/074-game-float-state-reset-match-20260925.md).
The following aggregate-copy pass completed `func_15133E3C`; see
[Working Note 075](WORKING_NOTES/075-game-two-word-record-forwarder-match-20260925.md).
The next guarded wrapper pass completed `func_151581D8`; see
[Working Note 076](WORKING_NOTES/076-game-seven-argument-wrapper-match-20260925.md).
The source-order pass completed `func_151D74B0` and closed the ten-difference
game tier; see
[Working Note 077](WORKING_NOTES/077-game-record-construction-order-match-20260925.md).
The first eleven-difference pass completed `func_150717E0` through a guarded
local-record pointer schedule; see
[Working Note 078](WORKING_NOTES/078-game-local-record-pointer-schedule-match-20260926.md).
The next interpolation pass completed `func_15074A94` through a direct
source-level expression and guarded FP-register normalization; see
[Working Note 079](WORKING_NOTES/079-game-interpolation-register-match-20260926.md).
The five-byte queue pass completed `func_1507EEB8` from a source-level fixed
reverse loop with no guarded rows; see
[Working Note 080](WORKING_NOTES/080-game-five-byte-queue-shift-match-20260926.md).
The record-activation loop pass completed `func_150B6D34` from a simplified
source loop plus nine guarded cursor/register schedule words; see
[Working Note 081](WORKING_NOTES/081-game-record-activation-loop-match-20260926.md).
The two-word call-wrapper pass completed `func_151090DC` directly from a typed
aggregate initializer and corrected pointer ABI; see
[Working Note 082](WORKING_NOTES/082-game-two-word-aggregate-call-match-20260926.md).
The position/phase pass completed `func_15141564` from multiplication-first
source scheduling plus two guarded base-pointer local-slot words; see
[Working Note 083](WORKING_NOTES/083-game-position-phase-update-match-20260926.md).
The byte-lookup forwarding pass completed `func_15178E14` directly from typed
callee contracts and an ANSI byte parameter; see
[Working Note 084](WORKING_NOTES/084-game-byte-lookup-forwarding-wrapper-match-20260926.md).
The conditional-minimum pass completed `func_151ACA20` directly from local
lifetime ordering and a single signed scaling assignment; see
[Working Note 085](WORKING_NOTES/085-game-conditional-minimum-update-match-20260926.md).
The table-sum pass completed `func_1501CFF8` directly from global count
expressions and local lifetime ordering; see
[Working Note 086](WORKING_NOTES/086-game-table-sum-loop-match-20260926.md).
The mirrored counter/table pass completed `func_15031E2C` with twelve guarded
register-schedule words; see
[Working Note 087](WORKING_NOTES/087-game-mirrored-counter-table-update-match-20260926.md).
The timed toggle/table pass completed `func_150337E4` directly from field-based
update, comparison, and table-index expressions; see
[Working Note 088](WORKING_NOTES/088-game-timed-toggle-table-update-match-20260926.md).
The three-byte record pass completed `func_1504BA38` with twelve guarded
pointer/value-register schedule words; see
[Working Note 089](WORKING_NOTES/089-game-three-byte-record-schedule-match-20260926.md).
The indexed signed-byte getter pass completed `func_150882B0` from local
ordering, final argument reuse, and ten guarded schedule words; see
[Working Note 090](WORKING_NOTES/090-game-indexed-signed-byte-getter-match-20260926.md).
The bounds-checked halfword getter pass completed `func_1508B194` from an
early-zero branch and five guarded base/index words; see
[Working Note 091](WORKING_NOTES/091-game-bounds-checked-halfword-getter-match-20260926.md).
The optional-pointer call-wrapper pass completed `func_150E33CC` through
twelve guarded scheduling words, including an explicit relocation move for
its sole call; see
[Working Note 092](WORKING_NOTES/092-game-optional-pointer-call-schedule-match-20260926.md).
The three-word aggregate-forwarder pass completed `func_15131D4C` directly
from a typed aggregate copy and pointer-correct callee declaration, without
guarded rows; see
[Working Note 093](WORKING_NOTES/093-game-three-word-aggregate-forwarder-match-20260926.md).
The duplicate masked-field pass completed `func_151355B8` by retaining both
retail stores through volatile field accesses and guarding five final
register-allocation words; see
[Working Note 094](WORKING_NOTES/094-game-duplicate-masked-field-store-match-20260926.md).
The allocation/copy wrapper pass completed `func_15168800` directly from an
explicit early null return, without guarded rows; see
[Working Note 095](WORKING_NOTES/095-game-allocation-copy-wrapper-match-20260926.md).
The signed-byte fallback-selector pass completed `func_151E5FAC` from
duplicated fallback returns, positive threshold control flow, and twelve
guarded relocation/scheduling words, closing the twelve-difference game tier;
see
[Working Note 096](WORKING_NOTES/096-game-signed-byte-fallback-selector-match-20260926.md).
The relative-offset tree-walk pass completed `func_15002560` from an explicit
top null test, scalar sibling-offset result, and two guarded commutative
pointer-add words; see
[Working Note 097](WORKING_NOTES/097-game-relative-offset-tree-walk-match-20260926.md).
The slot-cursor allocation pass completed `func_150356C8` from a direct
increment lifetime plus nine guarded scheduling words, including an explicit
move of the `D_800C3F08` low relocation; see
[Working Note 098](WORKING_NOTES/098-game-slot-cursor-allocation-match-20260926.md).
The chunked-boundary loop pass completed `func_15043B70` directly from a
scalar ternary that restores retail's explicit two-arm value merge, without
guarded rows; see
[Working Note 099](WORKING_NOTES/099-game-chunked-boundary-loop-match-20260926.md).
The packed four-byte reader pass completed `func_1507A3E8` through thirteen
guarded byte-load and merge-schedule words, including four explicitly moved
global relocation pairs; see
[Working Note 100](WORKING_NOTES/100-game-packed-four-byte-reader-match-20260926.md).
The retained local-record pointer pass completed `func_1507FF94` from an
asymmetric volatile pointer lifetime plus five guarded prologue scheduling
words; see
[Working Note 101](WORKING_NOTES/101-game-retained-local-record-pointer-match-20260926.md).
The null-first table-populator pass completed `func_15085B70` directly by
placing its zeroing path before its populated path, without guarded rows; see
[Working Note 102](WORKING_NOTES/102-game-null-first-table-populator-match-20260926.md).
The fourth-component continuation pass restored `func_150A7A14` from a false
C placeholder to the original thirteen-word assembly tail of
`func_150A7A00`'s synthetic-return trampoline; see
[Working Note 103](WORKING_NOTES/103-game-fourth-component-continuation-restoration-20260926.md).
The record-pointer lifetime pass completed `func_150CFBEC` directly by
materializing its output record before the condition and retaining two
volatile source-field reads, without guarded rows; see
[Working Note 104](WORKING_NOTES/104-game-record-pointer-repeated-field-match-20260926.md).
The two-component scaling pass converted `func_15131918` from a false
placeholder to byte-exact C, with float-typed scale loads at both callers and
no guarded rows; see
[Working Note 105](WORKING_NOTES/105-game-two-component-scaling-loop-match-20260926.md).
The embedded vertex-copy pass completed `func_1514143C` with thirteen guarded
words and two inserted schedule words, retaining retail's interior
`arg0 + 0x110` base without changing the logical C; see
[Working Note 106](WORKING_NOTES/106-game-embedded-vertex-copy-match-20260926.md).
The angle-normalization pass completed `func_15144B68` with a named result
local and two guarded opening schedule words; all 24 words now match retail.
Continue with 17-word `func_1518F858`; see
[Working Note 107](WORKING_NOTES/107-game-angle-normalization-match-20260926.md).
The conditional callback-dispatch pass completed all 17 words of
`func_1518F858` directly from an early return and volatile signed-byte index.
Continue with 17-word `func_1519072C`; see
[Working Note 108](WORKING_NOTES/108-game-conditional-dispatch-match-20260926.md).
The stack-record pass completed all 17 words of `func_1519072C` directly from
a contiguous local aggregate that preserves the record pointer across both
helper calls. Continue with 15-word `func_1519582C`; see
[Working Note 109](WORKING_NOTES/109-game-stack-record-pointer-match-20260926.md).
The five-global reset pass completed all 15 words of `func_1519582C` with
volatile pointer source and eight guarded opening relocation/scheduling words.
Continue with 15-word `func_151A9024`; see
[Working Note 110](WORKING_NOTES/110-game-global-reset-order-match-20260926.md).
The byte-gated call pass completed all 15 words of `func_151A9024` with
thirteen guarded argument and call-scheduling words. Continue with 15-word
`func_151C9B64`, whose generated condition is inverted relative to retail; see
[Working Note 111](WORKING_NOTES/111-game-byte-gated-call-match-20260926.md).
The nested-state flag pass completed all 15 words of `func_151C9B64` directly
from corrected branch semantics and an explicit nested-pointer lifetime.
Continue with the tied 13-word `func_151F892C` and `func_151F8960`; see
[Working Note 112](WORKING_NOTES/112-game-nested-state-flag-match-20260926.md).
Those two rows are handwritten helpers with non-ABI register inputs and are
therefore excluded from C restoration. The global-selection pass completed all
15 words of `func_1502C380` directly from an assignment chain. The fixed-matrix
pass then completed all 16 words of `func_150A7B80` with explicit source
stores and fourteen guarded overflow-slot replacements. The delimiter-split
pass completed all 16 words of `func_1516A770` directly from source. The
one-word aggregate-forwarder pass then completed all 16 words of
`func_1518F45C` directly from source. The callback-forwarding pass completed
all 16 words of `func_151A5130` directly from source. The selected state-block
reset pass completed all 17 words of `func_1508F060` with corrected source,
nine guarded rows, and three insertions. The typed float-record pass completed
all 17 words of `func_1518F89C` with twelve guarded scheduling rows and one
inserted call-delay `nop`. The second one-word aggregate-forwarder pass then
completed all 17 words of `func_151A561C` directly from source. The third pass
completed all 17 words of `func_151D343C` and corrected the shared pointer
contract without matcher regressions. The four-word record-fill pass then
completed all 18 words of `func_1519F3B8` with a typed record, nine guarded
rows, and one inserted retained-base reload; see
[Working Note 122](WORKING_NOTES/122-game-four-word-record-fill-match-20260926.md).
The fourth one-word aggregate-forwarder pass then completed all 19 words of
`func_15160274` directly from source and corrected its stale local callee
prototype; see
[Working Note 123](WORKING_NOTES/123-game-fourth-one-word-forwarder-match-20260926.md).
The float scale-and-offset pass then completed all 19 words of `func_151BD750`
with fifteen guarded scheduling rows and two insertions; see
[Working Note 124](WORKING_NOTES/124-game-float-scale-offset-match-20260926.md).
The two-word aggregate-forwarder pass then completed all 21 words of
`func_151417C4` directly from corrected source types and local ordering; see
[Working Note 125](WORKING_NOTES/125-game-two-word-byte-forwarder-match-20260926.md).
The angle-normalization pass then completed all 25 words of `func_15144BC8`
directly from an explicit result local; see
[Working Note 126](WORKING_NOTES/126-game-angle-normalization-match-20260926.md).
The random indexed-effect pass then completed all 45 words of `func_150718E4`
from corrected local ordering plus ten guarded register words; see
[Working Note 127](WORKING_NOTES/127-game-random-indexed-effect-match-20260926.md).
The bounded-index registration pass then completed all 16 words of
`func_150142AC` directly from recovered signed bounds and invalid-path return.
The indexed-float reader pass then completed all 16 words of `func_15088270`
from a separate index lifetime plus ten guarded scheduling words; see
[Working Note 129](WORKING_NOTES/129-game-indexed-float-reader-match-20260926.md).
The linked-list pass then completed all 17 words of `func_15188A58` from a
typed offset-`0x0C` node view plus thirteen guarded control-flow words; see
[Working Note 130](WORKING_NOTES/130-game-linked-list-append-match-20260926.md).
Skip the two smaller handwritten bitstream helpers and continue with 20-word
ordinary-C placeholder `func_1509F660`. The nullable callback-dispatch pass
then completed all 20 words of that function directly from recovered C, with
no guarded rows; see
[Working Note 131](WORKING_NOTES/131-game-nullable-callback-dispatch-match-20260926.md).
The scaled three-component update pass then completed all 19 words of
`func_151C4510` from explicit destination lifetimes plus fifteen guarded FP
scheduling words; see
[Working Note 132](WORKING_NOTES/132-game-scaled-vector-update-match-20260926.md).
The flag-gated high-half-mask pass then completed all 20 words of
`func_150C78E0` with six guarded scheduling replacements and one guarded dead
pointer-advance insertion; see
[Working Note 133](WORKING_NOTES/133-game-flag-gated-high-half-mask-match-20260926.md).
The scene-callback pass then completed all 20 words of `func_15130230`
directly from C by explicitly passing the incoming object pointer through the
selected callback. No guarded rows were needed; see
[Working Note 134](WORKING_NOTES/134-game-scene-callback-dispatch-match-20260926.md).
The animation sound-choice pass then completed all 59 words of
`func_1506C32C` directly from C by sharing the count/index lifetime and placing
the choices array between its scalar locals. No guarded rows were needed; see
[Working Note 135](WORKING_NOTES/135-game-animation-sound-choice-match-20260926.md).
The variable-record maximum pass then completed all 33 words of
`func_150CFDB8` directly from C by removing its redundant `p` lifetime and
mutating `arg0` through the loop. No guarded rows were needed; see
[Working Note 136](WORKING_NOTES/136-game-variable-record-maximum-match-20260926.md).
The active-buffer copy pass then completed all 23 words of `func_150CFE3C`
after recovering its nested state layout and guarding six base/register
scheduling words; see
[Working Note 137](WORKING_NOTES/137-game-active-buffer-copy-match-20260926.md).
The callback-table traversal pass then completed all 23 words of
`func_15167010` after deriving its bound from the cursor and guarding fifteen
frame, register, relocation, and epilogue words through fourteen rows; see
[Working Note 138](WORKING_NOTES/138-game-callback-table-traversal-match-20260926.md).
The record-copy builder pass then completed all 34 words of `func_15167D84`
through thirteen guarded CFG/register-scheduling rows with two insertions; see
[Working Note 139](WORKING_NOTES/139-game-record-copy-builder-match-20260926.md).
The linked-record update pass then completed all 41 words of `func_151D2E5C`
after correcting the owner-pointer call and recovering its four local
lifetimes, with one guarded commutative branch word; see
[Working Note 140](WORKING_NOTES/140-game-linked-record-update-match-20260926.md).
The global/object initializer pass then completed all 18 words of
`func_150104F0` after recovering its chained zero assignment and guarding six
base/store words; see
[Working Note 141](WORKING_NOTES/141-game-global-object-initializer-match-20260926.md).
The dimension/ratio setup pass then completed all 33 words of
`func_150492CC` through sixteen guarded floating-point and relocation schedule
words; see
[Working Note 142](WORKING_NOTES/142-game-dimension-ratio-setup-match-20260926.md).
The angle-tolerance pass then completed all 58 words of `func_150767F4`
through sixteen guarded register-scheduling words; see
[Working Note 143](WORKING_NOTES/143-game-angle-tolerance-match-20260926.md).
Keep `func_150721A4` parked as a known three-word live-C compiler overflow.
The packed actor-mask pass then completed all 21 words of `func_1507A428`
through sixteen guarded global-load, relocation, and value-lifetime words; see
[Working Note 144](WORKING_NOTES/144-game-packed-actor-mask-match-20260926.md).
The indexed-table lookup pass then completed all 20 words of `func_15084CB0`
after recovering its scalar lifetimes and array indexing, with seven guarded
signed-loop and epilogue words; see
[Working Note 145](WORKING_NOTES/145-game-indexed-u16-table-lookup-match-20260926.md).
The indexed-record lookup pass then completed all 19 words of `func_15086D48`
after recovering its 16-byte array indexing, with six guarded signed-loop and
fallback-epilogue words; see
[Working Note 146](WORKING_NOTES/146-game-indexed-record-lookup-match-20260926.md).
The nullable-field cleanup pass then completed all 19 words of
`func_150F631C` directly from C after recovering its owner lifetime and
volatile repeated first-field loads; see
[Working Note 147](WORKING_NOTES/147-game-nullable-field-cleanup-match-20260926.md).
The vector-scale pass then completed all 19 words of `func_15131958` directly
from C after restoring its count-controlled three-component loop and typed
call boundary; see
[Working Note 148](WORKING_NOTES/148-game-vector-scale-loop-match-20260926.md).
The event-record link-update pass then completed all 43 words of
`func_151419D0` after recovering its shared source-value lifetime and guarding
one commutative branch word; see
[Working Note 149](WORKING_NOTES/149-game-event-record-link-update-match-20260926.md).
The scaled angle-component pass then completed all 25 words of
`func_15143874` directly from C after correcting its signed angle ABI and
recovering explicit narrowed-angle and lookup-result lifetimes; see
[Working Note 150](WORKING_NOTES/150-game-scaled-angle-components-match-20260926.md).
The indexed callback pass then completed all 18 words of `func_15147D1C`
directly from C after restoring its three forwarded callback arguments; see
[Working Note 151](WORKING_NOTES/151-game-indexed-callback-forwarding-match-20260926.md).
The linked-node reset pass then completed all 18 words of `func_1515C158`
after restoring both row traversals and guarding thirteen persistent IDO
pointer-coloring words; see
[Working Note 152](WORKING_NOTES/152-game-linked-node-reset-match-20260926.md).
The linked-node tail-insertion pass then completed all 35 words of
`func_1515D520` after recovering its direct head test, typed next-pointer
walk, and allocation return lifetime, plus four guarded frame/scheduling
words; see
[Working Note 153](WORKING_NOTES/153-game-linked-node-tail-insert-match-20260926.md).
The indexed callback-dispatch pass then completed all 23 words of
`func_151635A8` after correcting its three-argument callback ABI and retaining
volatile table reads, plus fifteen guarded compiler-normalization rows; see
[Working Note 154](WORKING_NOTES/154-game-indexed-callback-dispatch-match-20260926.md).
The row-list head-insertion pass then completed all 20 words of
`func_15168A4C` after recovering typed node and explicit row/column scalar
lifetimes, plus four guarded register-color words; see
[Working Note 155](WORKING_NOTES/155-game-row-list-head-insert-match-20260926.md).
Keep generated unaligned-load helpers `func_151F892C` and `func_151F8960` in
the raw-assembly queue. The selected actor-state cleanup pass then completed
all 23 words of `func_150747E4` after recovering its scalar and pointer
lifetimes, plus ten guarded relocation/register-scheduling words; see
[Working Note 156](WORKING_NOTES/156-game-selected-actor-state-cleanup-match-20260926.md).
The selector-table byte pass then replaced `func_150849CC`'s zero-return
placeholder with its complete 19-word C behavior and retained one redundant
retail fallback branch through three guarded CFG rows; see
[Working Note 157](WORKING_NOTES/157-game-selector-table-byte-match-20260926.md).
The wrapping signed-byte counter pass then completed all 20 words of
`func_1508CA88` after recovering its shared return path and preserving the
independent final global-pointer reload through two guarded relocation-aware
rows; see
[Working Note 158](WORKING_NOTES/158-game-wrapping-byte-counter-match-20260926.md).
The state-gated owner-check pass then replaced `func_15116930`'s zero-return
placeholder with its complete 21-word behavior, matching directly from C
without guarded rows; see
[Working Note 159](WORKING_NOTES/159-game-state-gated-owner-check-match-20260926.md).
The nullable coordinate-copy pass then replaced `func_1511F92C`'s zero-return
placeholder with its lookup and three-halfword copy, matching all 21 words
directly from C; see
[Working Note 160](WORKING_NOTES/160-game-nullable-coordinate-copy-match-20260926.md).
The six-argument forwarding pass then replaced `func_15130374`'s zero-return
placeholder with its direct `func_15130280` call and corrected byte ABI,
matching all 18 words directly from C; see
[Working Note 161](WORKING_NOTES/161-game-six-argument-forwarder-match-20260926.md).
The two-word template-dispatch pass then replaced `func_1515572C`'s
zero-return placeholder with its typed local copy and `func_15169260` call,
matching all 21 padded words directly from C; see
[Working Note 162](WORKING_NOTES/162-game-two-word-template-dispatch-match-20260926.md).
The selector-linked-list pass then replaced `func_15178B98`'s zero-return
placeholder with its complete node traversal, matching all 19 words directly
from C; see
[Working Note 163](WORKING_NOTES/163-game-selector-linked-list-lookup-match-20260926.md).
The gated byte-result pass then replaced `func_1519257C`'s zero-return
placeholder with its two-stage call chain, matching all 18 words directly
from C; see
[Working Note 164](WORKING_NOTES/164-game-gated-byte-result-chain-match-20260926.md).
The indexed callback-forwarding pass then corrected `func_151B82CC`'s
callback contract and child-pointer lifetime, matching all 19 words directly
from C; see
[Working Note 165](WORKING_NOTES/165-game-indexed-callback-forwarding-match-20260926.md).
The object-selector record pass then replaced `func_1506AC0C`'s zero-return
placeholder with its typed local record and `func_151B7328` call, matching all
19 words directly from C; see
[Working Note 166](WORKING_NOTES/166-game-object-selector-record-match-20260926.md).
The scaled-table-reader pass then preserved `func_150881CC`'s clean null-gated
`0x84`-stride float lookup and guarded five IDO register-scheduling words,
matching all 19 words; see
[Working Note 167](WORKING_NOTES/167-game-scaled-table-reader-match-20260926.md).
The indexed-record-deactivation pass then removed `func_15088780`'s one-use
record pointer and restored the table-base-plus-scaled-index expression order,
matching all 30 words directly from C; see
[Working Note 168](WORKING_NOTES/168-game-indexed-record-deactivation-match-20260926.md).
The selector-init-wrapper pass then replaced `func_1509E8A0`'s zero-return
placeholder with its three-argument callback contract and selector-7/8
dispatch, matching all 24 padded words directly from C; see
[Working Note 169](WORKING_NOTES/169-game-selector-init-wrapper-match-20260926.md).
The record-gate-wrapper pass then replaced `func_150A34B0`'s zero-return
placeholder with its byte-`0x14` rejection, low-flag gate, and forwarded
`func_150A3504` call, matching all 21 words directly from C; see
[Working Note 170](WORKING_NOTES/170-game-record-gate-wrapper-match-20260926.md).
The matrix-identity pass then corrected `func_150A7CB0`'s final identity
element from an integer bit pattern to a real `1.0f` store and guarded the
three-word store/return schedule, matching all 20 words; see
[Working Note 171](WORKING_NOTES/171-game-matrix-identity-element-match-20260926.md).
The translation-matrix pass then restored `func_150A7DA0`'s four floating
identity-diagonal stores and three raw translation words, with six guarded
register/schedule words matching all 20 words; see
[Working Note 172](WORKING_NOTES/172-game-translation-matrix-identity-match-20260926.md).
The PRNG ownership pass then restored `func_150ADA20`'s original handwritten
18-word MIPS III body after its equivalent C was confirmed to overflow the
retail slot by one word; see
[Working Note 173](WORKING_NOTES/173-game-handwritten-prng-step-restoration-20260926.md).
The buffer-state pass then made `func_150CFE98` byte-exact by recovering its
one-use pointer and result lifetimes and guarding seven IDO frame/spill words;
see [Working Note 174](WORKING_NOTES/174-game-buffer-advance-match-20260926.md).
The float-mapper pass then converted `func_150F34A0` from its zero-return
placeholder and matched all 21 words directly from C; see
[Working Note 175](WORKING_NOTES/175-game-float-threshold-mapper-match-20260926.md).
The sibling port's generated recomp body still reflects the old placeholder
and must be refreshed through its controlled generation path before claiming
host parity. Continue decomp matching with 20-word `func_150FADC8`, which has
18 real differences. That event-bit callback is now converted from its
zero-return placeholder and matches all 20 words directly from C; see
[Working Note 176](WORKING_NOTES/176-game-event-bit-toggle-match-20260926.md).
Its sibling generated recomp body likewise remains pending controlled refresh.
Continue with 21-word `func_15133DE8`, which has 18 real differences.
That record/owner match callback is now converted from its zero-return
placeholder and matches all 21 words directly from C after making the record
identifier lifetime explicit; see
[Working Note 177](WORKING_NOTES/177-game-record-owner-match-callback-20260926.md).
Its sibling generated recomp body remains pending controlled refresh. Continue
with 19-word `func_151444DC`, which has 18 real differences.
The Init ownership pass then replaced false C placeholders for `__osGetSR`,
`osGetCount`, and `__osSetCompare` with their original handwritten CP0
assembly. All three complete 16-byte padded spans match retail; see
[Working Note 178](WORKING_NOTES/178-init-handwritten-cp0-wrapper-restoration-20260926.md).
The sibling already provides a native tracked-status override for `__osGetSR`;
no generated or host source was changed in this classification-only pass.
The adjacent control-register pass then restored handwritten `__osSetSR` and
low-level SDK `__osSetFpcCsr` to original assembly ownership. Both complete
16-byte spans match retail; see
[Working Note 179](WORKING_NOTES/179-init-control-register-wrapper-restoration-20260926.md).
The following ordinary Init pass completed two-difference `func_1000FE88`
through guarded current-pointer spill/reload slot normalization; see
[Working Note 180](WORKING_NOTES/180-init-current-pointer-frame-slot-match-20260926.md).
The following audit restored handwritten interrupt wrappers `__osRestoreInt`
and `__osDisableInt` from false C placeholders to their original eight-word
CP0 bodies; see
[Working Note 181](WORKING_NOTES/181-init-handwritten-interrupt-wrapper-restoration-20260926.md).
The next ordinary Init pass completed `func_100043B4` through a guarded,
relocation-aware six-word schedule; see
[Working Note 182](WORKING_NOTES/182-init-header-tag-update-match-20260926.md).
The following pass completed 47-word `func_1000FD38` through a guarded,
relocation-aware six-word schedule that refreshes its cached loop bound only
after the release call; see
[Working Note 183](WORKING_NOTES/183-init-release-loop-bound-refresh-match-20260926.md).
The ownership audit then restored nine-word `func_10001420` from an overflowing
C model to its original handwritten memory-clear loop; see
[Working Note 184](WORKING_NOTES/184-init-handwritten-memory-clear-restoration-20260926.md).
The sibling already has an exact generated recomp body. Continue with 11-word
`func_100038E0`. That audit restored the original handwritten MMIO setup body;
see
[Working Note 185](WORKING_NOTES/185-init-handwritten-mmio-setup-restoration-20260926.md).
Its sibling body is behaviorally equivalent but retains the old compiled
schedule pending a controlled regeneration. Continue with 12-word
`osWritebackDCacheAll`. That audit restored the original handwritten cache-op
loop from an empty C placeholder; see
[Working Note 186](WORKING_NOTES/186-init-writeback-dcache-all-restoration-20260926.md).
The next low-level audit restored the original 16-word CP0/TLB body for
`osUnmapTLB` from another empty C placeholder; see
[Working Note 187](WORKING_NOTES/187-init-unmap-tlb-restoration-20260926.md).
The paired ownership pass then restored handwritten unaligned-load helpers
`func_151F892C` and `func_151F8960` from zero-return placeholders; see
[Working Note 188](WORKING_NOTES/188-game-unaligned-bitstream-helper-restoration-20260926.md).
The following ordinary Game pass matched 19-word `func_151444DC` directly from
corrected `do/while` control flow; see
[Working Note 189](WORKING_NOTES/189-game-integer-range-wrapper-match-20260926.md).
The next pass matched all 20 words of `func_151464B8` directly from corrected C
types, lifetimes, and optimized-away register-allocation expressions; see
[Working Note 190](WORKING_NOTES/190-game-active-player-mask-predicate-match-20260926.md).
Continue with the 20-word generated-slice placeholder `func_1514ED3C`.
That lookup is now reconstructed and exact from typed linked-list C; see
[Working Note 191](WORKING_NOTES/191-game-linked-list-key-lookup-match-20260926.md).
Continue with 20-word `func_15178BE4`.
That node initializer is now exact from typed C; see
[Working Note 192](WORKING_NOTES/192-game-node-initializer-match-20260926.md).
Continue with 20-word `func_15187FC0`.
That indexed color extractor is now exact from typed C; see
[Working Note 193](WORKING_NOTES/193-game-indexed-color-extractor-match-20260926.md).
Continue with 21-word `func_15190400`.
That event-owner release handler is now exact from typed C; see
[Working Note 194](WORKING_NOTES/194-game-event-owner-release-match-20260926.md).
Continue with 21-word `func_15191B8C`.
That unregister-and-broadcast wrapper is now exact from typed C; see
[Working Note 195](WORKING_NOTES/195-game-unregister-broadcast-wrapper-match-20260926.md).
Continue with 21-word `func_151A4F7C`.
That embedded-owner release handler is now exact from typed C; see
[Working Note 196](WORKING_NOTES/196-game-embedded-owner-release-match-20260926.md).
Continue with 20-word `func_151A8584`.
The adjacent `func_151A8584`/`func_151A85D4` callback pair is behaviorally
recovered but parked: current typed C emits `0x54` bytes for each versus
retail's `0x50` because IDO homes and reloads `arg0` before the indirect call.
The independent 21-word `func_151B22F4` slot-state predicate is now exact; see
[Working Note 197](WORKING_NOTES/197-game-slot-state-predicate-match-20260926.md).
Continue with 23-word `func_151D73A8`.
That callback dispatch is now exact after preserving retail's volatile double
lookup; see
[Working Note 198](WORKING_NOTES/198-game-volatile-callback-dispatch-match-20260926.md).
Continue with 20-word `func_1502E474`.
That conditional submission wrapper is now exact from C; see
[Working Note 199](WORKING_NOTES/199-game-conditional-submission-wrapper-match-20260926.md).
Continue with 33-word `func_150319CC`.
That two-pass list lookup is now exact after preserving retail's separate
current and next-node lifetimes; see
[Working Note 200](WORKING_NOTES/200-game-two-pass-list-lookup-match-20260926.md).
Continue with 17-word `func_150721A4`.
That row remains the documented three-word compiler overflow. The next
completed direct-C row is the event-flag handler; see
[Working Note 201](WORKING_NOTES/201-game-event-flag-handler-match-20260926.md).
Continue with 21-word `func_150EC45C`.
That constant preset wrapper is now exact from a typed eight-argument call;
see
[Working Note 202](WORKING_NOTES/202-game-constant-preset-wrapper-match-20260926.md).
Continue with 22-word `func_150F1684`.
That handler's logic is recovered, but direct C still swaps retail's `v0` and
`v1` key/identity lifetimes. The next completed exact row is the conditional
stack-record wrapper; see
[Working Note 203](WORKING_NOTES/203-game-conditional-stack-record-wrapper-match-20260926.md).
The 21-word `func_1514A498` motion-decay update is now exact with one guarded
commutative `multu` operand-order word; see
[Working Note 204](WORKING_NOTES/204-game-motion-decay-update-match-20260926.md).
The 21-word `func_15155FD4` linked-list lookup is behaviorally recovered but
parked at a measured owner/end/node register-allocation boundary. The
independent 20-word `func_15181DC8` per-slot reset is now exact with two
guarded floating-zero words; see
[Working Note 205](WORKING_NOTES/205-game-per-slot-state-reset-match-20260926.md).
The 21-word `func_1518F108` two-component decay twin is now exact with one
guarded commutative `multu` operand-order word; see
[Working Note 206](WORKING_NOTES/206-game-shifted-motion-decay-match-20260926.md).
The 20-word `func_15192308` embedded-address setup wrapper is now exact
directly from a typed six-argument call; see
[Working Note 207](WORKING_NOTES/207-game-embedded-address-setup-wrapper-match-20260926.md).
The 20-word `func_151A73EC` bounded embedded-owner release helper is now exact
directly from nested typed C; see
[Working Note 208](WORKING_NOTES/208-game-bounded-embedded-owner-release-match-20260926.md).
The 20-word `func_151AF338` float ABI adapter is now exact directly from a
typed seven-argument wrapper; see
[Working Note 209](WORKING_NOTES/209-game-float-abi-adapter-match-20260926.md).
The 20-word `func_151B4C1C` embedded cleanup and callback-dispatch wrapper is
now exact directly from typed C; see
[Working Note 210](WORKING_NOTES/210-game-embedded-cleanup-dispatch-match-20260926.md).
The twin 20-word `func_151B50A4` float ABI adapter is also exact from the same
typed wrapper shape; see
[Working Note 211](WORKING_NOTES/211-game-second-float-abi-adapter-match-20260926.md).
The 21-word `func_151B7678` validated-position reader is now exact from a typed
pointer chain and short-circuit failure condition; see
[Working Note 212](WORKING_NOTES/212-game-validated-position-reader-match-20260926.md).
The 22-word `func_151B8318` optional matching-record release gate is now exact
from typed C and an explicit record-word lifetime; see
[Working Note 213](WORKING_NOTES/213-game-optional-record-release-match-20260926.md).
The 22-word `func_151D8D5C` two-event release callback is now exact from a
typed callback signature and explicit event branches; see
[Working Note 214](WORKING_NOTES/214-game-two-event-release-callback-match-20260926.md).
The 20-word `func_15083FB0` object-index wrapper is now exact after correcting
the local `func_15083E90` byte-parameter and pointer-return contract; see
[Working Note 215](WORKING_NOTES/215-game-object-index-wrapper-match-20260926.md).
The 22-word `func_1515D030` reverse-slot update is now exact from a signed byte
decrement and shared result variable; see
[Working Note 216](WORKING_NOTES/216-game-reverse-slot-update-match-20260926.md).
Measured compiler boundaries in `guMtxIdentF`, `func_1506EF5C`, and
`func_1507A4D4` are parked. The 21-word `func_15178750` conditional callback
wrapper and newly inventoried two-word `func_151787A4` no-op table callback
are separately byte-exact; see
[Working Note 217](WORKING_NOTES/217-game-conditional-callback-and-hidden-noop-match-20260926.md).
The 21-word `func_150C522C` four-slot release loop is now exact through a
typed pointer-array loop plus two guarded relocation-aware address-completion
words; see
[Working Note 218](WORKING_NOTES/218-game-four-slot-release-loop-match-20260926.md).
The 21-word `func_150C5F40` existing-record/allocator wrapper is now exact
directly from typed C; see
[Working Note 219](WORKING_NOTES/219-game-existing-record-wrapper-match-20260926.md).
Its `+0x70` structural twin `func_150C6870` is also exact directly from typed
C; see
[Working Note 220](WORKING_NOTES/220-game-existing-record-wrapper-twin-match-20260926.md).
The 21-word `func_150C7968` flag-gated optional-record update is now exact
through typed C plus five guarded scheduling/relocation entries; see
[Working Note 221](WORKING_NOTES/221-game-flag-gated-record-update-match-20260926.md).
The 21-word `func_150EB430` stack-vector sum wrapper is now exact after a
commutative source-order correction and four guarded second-vector register
words; see
[Working Note 222](WORKING_NOTES/222-game-stack-vector-sum-wrapper-match-20260927.md).
The 21-word `func_15155F3C` state-transition wrapper is now exact through
typed C plus three guarded state-register words; see
[Working Note 223](WORKING_NOTES/223-game-state-transition-wrapper-match-20260927.md).
Keep `func_15155FD4` parked. The 22-word `func_1507A47C` packed actor-mask
clear is now exact through a named mask local and eighteen guarded
relocation-aware scheduling words; see
[Working Note 224](WORKING_NOTES/224-game-packed-actor-mask-clear-match-20260927.md).
The 24-word `func_150C5310` mode-flag toggle is now exact directly from typed
C, including its three tracked trailing padding words; see
[Working Note 225](WORKING_NOTES/225-game-mode-flag-toggle-match-20260927.md).
The 24-word `func_150E2FC0` marker-record swap is now exact from typed C plus
one guarded equivalent branch-operand word; see
[Working Note 226](WORKING_NOTES/226-game-marker-record-swap-match-20260927.md).
The 26-word `func_15125628` four-timer decrement is restored to its original
handwritten assembly ownership; see
[Working Note 227](WORKING_NOTES/227-game-four-timer-decrement-restoration-20260927.md).
The 33-word `func_1505DFDC` backing-buffer reset is now exact directly from
typed C after restoring the full-width index and two table reads; see
[Working Note 228](WORKING_NOTES/228-game-backing-buffer-reset-match-20260927.md).
Keep `func_150721A4` and the `func_151A8584`/`func_151A85D4` pair parked;
the generated-slice row `func_150AD8B0` is now restored to its handwritten
19-word vector cross-product body; see
[Working Note 229](WORKING_NOTES/229-game-vector-cross-product-restoration-20260927.md).
The 22-word `func_15131C2C` flag-gated callback dispatcher is now exact
directly from typed C; see
[Working Note 230](WORKING_NOTES/230-game-flag-gated-callback-dispatch-match-20260927.md).
The 24-word `func_1515F0AC` signed fixed-point clamp is now exact from C plus
three guarded schedule entries, including one stale-checked omission of IDO's
extra FP hazard `nop`; see
[Working Note 231](WORKING_NOTES/231-game-signed-fixed-point-clamp-match-20260927.md).
The 21-word `func_1516706C` three-entry callback-table loop is now exact from
its post-tested C loop plus two guarded relocation-aware low-half address
words; see
[Working Note 232](WORKING_NOTES/232-game-callback-table-loop-match-20260927.md).
The 29-word `func_15168A9C` indexed-list unlink is now exact directly from
typed C with explicit row/index byte lifetimes; see
[Working Note 233](WORKING_NOTES/233-game-indexed-list-unlink-match-20260927.md).
The 23-word `func_15179AB8` backward active-object flag scan is now exact
directly from C; see
[Working Note 234](WORKING_NOTES/234-game-active-object-flag-scan-match-20260927.md).
The 26-word `func_15194AB4` state-to-animation selector is now exact directly
from corrected C return type, default lifetime, and switch control flow; see
[Working Note 235](WORKING_NOTES/235-game-state-animation-selector-match-20260927.md).
The 29-word `func_151957B0` list-tail insertion and newly tracked two-word
no-op `func_15195824` are now exact directly from C; see
[Working Note 236](WORKING_NOTES/236-game-list-tail-insert-and-hidden-noop-match-20260927.md).
The 22-word `func_151A8A20` bounded callback dispatcher is now exact directly
from C; see
[Working Note 237](WORKING_NOTES/237-game-bounded-callback-dispatch-match-20260927.md).
The 20-word `func_151A8F1C` coordinate-transform wrapper is now exact directly
from C; see
[Working Note 238](WORKING_NOTES/238-game-coordinate-transform-wrapper-match-20260927.md).
The 21-word `func_151AA17C` dual event-record dispatch is now exact from
recovered C semantics plus ten guarded scheduling/local-slot words; see
[Working Note 239](WORKING_NOTES/239-game-dual-event-record-dispatch-match-20260927.md).
Its 21-word structural twin `func_151AA210` is independently exact from the
same C shape and separately scoped guards; see
[Working Note 240](WORKING_NOTES/240-game-dual-event-record-dispatch-twin-match-20260927.md).
The 21-word `func_151CF844` conditional record forwarder is exact directly
from C with no guarded words; see
[Working Note 241](WORKING_NOTES/241-game-conditional-record-forwarder-match-20260927.md).
The 21-word `func_151D10E4` indexed record forwarder is exact from recovered
C semantics plus twelve guarded scheduling words; see
[Working Note 242](WORKING_NOTES/242-game-indexed-record-forwarder-match-20260927.md).
The 21-word `func_151D4D58` two-mode preset wrapper is exact directly from C
with no guarded words; see
[Working Note 243](WORKING_NOTES/243-game-two-mode-preset-wrapper-match-20260927.md).
The 23-word `func_151E7E9C` three-way state dispatcher is exact directly from
C with no guarded words; see
[Working Note 244](WORKING_NOTES/244-game-three-way-state-dispatcher-match-20260927.md).
The 22-word `func_15022190` flagged coordinate setter is exact directly from C
with no guarded words; see
[Working Note 245](WORKING_NOTES/245-game-flagged-coordinate-setter-match-20260927.md).
The 24-word `func_15023870` null-gated event-byte copy is exact directly from C
with no guarded words; see
[Working Note 246](WORKING_NOTES/246-game-null-gated-event-byte-copy-match-20260927.md).
The 32-word `func_15033328` swimming-attachment lifetime callback is exact
directly from C with no guarded words; see
[Working Note 247](WORKING_NOTES/247-game-swimming-attachment-lifetime-match-20260927.md).
The 22-word `func_1503378C` six-ID type predicate is exact directly from C with
no guarded words; see
[Working Note 248](WORKING_NOTES/248-game-six-id-type-predicate-match-20260927.md).
The 22-word `func_15044DE8` guarded mode-4 dispatcher is exact directly from C
with no guarded words; see
[Working Note 249](WORKING_NOTES/249-game-guarded-mode4-dispatcher-match-20260927.md).
The 22-word `func_15088218` fixed-point/float record value is exact from
recovered C semantics plus nine guarded scheduling words; see
[Working Note 250](WORKING_NOTES/250-game-fixedpoint-float-record-value-match-20260927.md).
The false zero-return placeholder at `func_150AF738` is restored as a 22-word
stack-record forwarder, exact from recovered C semantics plus fifteen guarded
scheduling words; see
[Working Note 251](WORKING_NOTES/251-game-stack-record-forwarder-match-20260927.md).
The false zero-return placeholder at `func_150BB700` is restored as a 24-word
event-bit updater, exact directly from C with no guarded words; see
[Working Note 252](WORKING_NOTES/252-game-event-bit-updater-match-20260927.md).
Its false-placeholder template twin `func_150D1BD0` is also restored as a
24-word event-bit updater, exact directly from C with no guarded words; see
[Working Note 253](WORKING_NOTES/253-game-event-bit-updater-twin-match-20260927.md).
The false zero-return placeholder at `func_150E411C` is restored as a 22-word
eight-argument parameter preset, exact directly from C with no guarded words;
see [Working Note 254](WORKING_NOTES/254-game-parameter-preset-match-20260927.md).
The false zero-return placeholder at `func_150EB030` is restored as a 24-word
nested state classifier, exact directly from C with no guarded words; see
[Working Note 255](WORKING_NOTES/255-game-nested-state-classifier-match-20260927.md).
The false zero-return placeholder at `func_150FB1E8` is restored as a 22-word
five-argument two-stage forwarder, exact directly from C with no guarded
words; see
[Working Note 256](WORKING_NOTES/256-game-two-stage-forwarder-match-20260927.md).
The false zero-return placeholder at `func_150FB240` is restored as a 23-word
signed-halfword mapper, exact directly from C with no guarded words; see
[Working Note 257](WORKING_NOTES/257-game-signed-halfword-mapper-match-20260927.md).
The false zero-return placeholder at `func_150FFD2C` is restored as a 22-word
type-and-flag-gated dispatcher, exact directly from C with no guarded words;
see [Working Note 258](WORKING_NOTES/258-game-type-flag-dispatcher-match-20260927.md).
The false zero-return placeholder at `func_151076A4` is restored as a 23-word
volatile callback-table dispatcher, exact directly from C with no guarded
words; see [Working Note 259](WORKING_NOTES/259-game-volatile-callback-table-dispatch-match-20260927.md).
The false zero-return placeholder at `func_1510A870` is restored as a 23-word
paired-record updater, exact from recovered C semantics plus one guarded
commutative-branch operand word; see
[Working Note 260](WORKING_NOTES/260-game-paired-record-update-match-20260927.md).
Its false-placeholder twin `func_1510A8CC` is also exact across its 25-word
tracked layout from the same C semantics and one-word guard; 23 words are
executable and two are trailing padding. See
[Working Note 261](WORKING_NOTES/261-game-paired-record-update-twin-match-20260927.md).
The false zero-return placeholder at `func_1512D6F0` is restored as a 22-word
indexed-record reset, exact directly from structured C with no guarded words;
see [Working Note 262](WORKING_NOTES/262-game-indexed-record-reset-match-20260927.md).
The 23-word `func_1513BA78` two-way type dispatcher is exact directly from C
after typed callee declarations recover retail's byte-argument register
lifetime; see [Working Note 263](WORKING_NOTES/263-game-two-way-type-dispatch-match-20260927.md).
The 37-word `func_15144598` mode-dependent area scaler is exact directly from
C after correcting its mode-byte offset, signed dimensions, case order, and
commutative operand order; see
[Working Note 264](WORKING_NOTES/264-game-mode-area-scaler-match-20260927.md).
The false zero-return placeholder at `func_15149BF4` is restored as a 25-word
two-axis float damping threshold, exact directly from C with no guarded words;
see [Working Note 265](WORKING_NOTES/265-game-float-damping-threshold-match-20260927.md).
The 23-word `func_1514ECE0` signed-key list search is exact directly from C as
the halfword-key twin of `func_1514ED3C`, with no guarded words; see
[Working Note 266](WORKING_NOTES/266-game-signed-key-list-search-match-20260927.md).
The 22-word `func_15159BB0` effect callback adapter is exact directly from C,
including its position and zero-velocity vectors and two effect-record bytes;
see [Working Note 267](WORKING_NOTES/267-game-effect-callback-adapter-match-20260927.md).
The 22-word `func_15172C50` two-table initializer is exact directly from a
16-entry C loop whose body IDO unrolls four ways; see
[Working Note 268](WORKING_NOTES/268-game-two-table-initializer-match-20260927.md).
The 22-word `func_15172D28` object state-transition wrapper is exact directly
from C, including both branch-likely early-return paths; see
[Working Note 269](WORKING_NOTES/269-game-object-state-transition-match-20260927.md).
The 22-word `func_151749A0` wrapped timer/counter updater is exact directly
from C with byte-width arithmetic preserved; see
[Working Note 270](WORKING_NOTES/270-game-wrapped-timer-counter-match-20260927.md).
The 22-word `func_1517F75C` inclusive player-timer decay loop is exact directly
from C with unsigned halfword clamping preserved; see
[Working Note 271](WORKING_NOTES/271-game-player-timer-decay-match-20260927.md).
The 22-word `func_15181D70` enabled player-state initializer is exact directly
from C as the nonzero twin of `func_15181DC8`; see
[Working Note 272](WORKING_NOTES/272-game-enabled-player-state-init-match-20260927.md).
The 24-word `func_1518A360` paired endpoint updater is exact from C with one
guarded commutative branch-operand normalization; see
[Working Note 273](WORKING_NOTES/273-game-paired-endpoint-update-match-20260927.md).
The 23-word `func_151904BC` callback/resource cleanup is exact from C with
five guarded branch and call-setup scheduling words; see
[Working Note 274](WORKING_NOTES/274-game-callback-resource-cleanup-match-20260927.md).
The 23-word `func_15197A0C` scaled query wrapper is exact directly from C after
restoring its incoming argument; see
[Working Note 275](WORKING_NOTES/275-game-scaled-query-wrapper-match-20260927.md).
The adjacent 24-word `func_1519F108` and `func_1519F168` state-clear callbacks
are independently exact from shared recovered C plus symmetric guarded
scheduling; see
[Working Note 276](WORKING_NOTES/276-game-paired-state-clear-callback-match-20260927.md).
The 23-word `func_151A09B4` conditional child teardown is exact directly from
C with no guarded words; see
[Working Note 277](WORKING_NOTES/277-game-conditional-child-teardown-match-20260927.md).
The 22-word `func_151B4E4C` position/effect wrapper is exact directly from C;
see [Working Note 278](WORKING_NOTES/278-game-position-effect-wrapper-match-20260927.md).
The 23-word `func_151EFF94` variadic formatting wrapper is exact directly from
C; see [Working Note 279](WORKING_NOTES/279-game-variadic-format-wrapper-match-20260927.md).
The 23-word `func_15044CE4` position/scale initializer is exact from C plus
seven guarded register-lifetime words; see
[Working Note 280](WORKING_NOTES/280-game-position-scale-initializer-match-20260927.md).
The existing C for 36-word `func_1508855C` is exact with 22 guarded
register-lifetime and equivalent control-flow scheduling words; see
[Working Note 281](WORKING_NOTES/281-game-indexed-record-lookup-match-20260927.md).
The former 26-word `func_150A6500` row is now correctly split: its 14-word
bounded-query wrapper is exact from recovered C plus 12 guarded scheduling
words, and 12-word `func_150A6538` remains exact original assembly pending a
source-grounded calling convention; see
[Working Note 282](WORKING_NOTES/282-game-bounded-query-wrapper-match-20260927.md).
The 23-word `func_150BE438` object-record writer is exact directly from C with
no guarded words; see
[Working Note 283](WORKING_NOTES/283-game-object-record-writer-match-20260927.md).
The 23-word `func_150D1410` object-index flag updater is also exact directly
from C with no guarded words; see
[Working Note 284](WORKING_NOTES/284-game-object-index-flag-match-20260927.md).
The 23-word `func_150D2054` six-entry cleanup loop is exact directly from C
with no guarded words; see
[Working Note 285](WORKING_NOTES/285-game-six-entry-cleanup-match-20260927.md).
The tracked 25-word `func_150D32FC` event-key forwarder, including two trailing
layout words, is exact directly from C with no guarded words; see
[Working Note 286](WORKING_NOTES/286-game-event-key-forwarder-match-20260927.md).
The tracked 26-word `func_150DEC28` paired table dispatcher, including three
trailing layout words, is exact directly from C with no guarded words; see
[Working Note 287](WORKING_NOTES/287-game-paired-table-dispatcher-match-20260927.md).
The 24-word `func_150F4CFC` two-event state/teardown handler is exact directly
from C with no guarded words; see
[Working Note 288](WORKING_NOTES/288-game-event-state-teardown-handler-match-20260927.md).
The tracked 29-word `func_151002BC` linked-record validator, including three
trailing layout words, is exact from recovered C plus seven guarded scheduling
words; see
[Working Note 289](WORKING_NOTES/289-game-linked-record-validation-match-20260927.md).
The 25-word `func_15125490` water-distance classifier is exact from typed
recovered C plus a guarded replacement of its oversized 26-word IDO body; see
[Working Note 290](WORKING_NOTES/290-game-water-distance-classifier-match-20260927.md).
The 23-word `func_1514EE70` object-request wrapper is exact directly from C,
including its typed eight-byte request and both compiler-produced call
relocations; see
[Working Note 291](WORKING_NOTES/291-game-object-request-wrapper-match-20260927.md).
The 25-word `func_1514F130` state-toggle event callback is exact directly from
typed C with no guarded words; see
[Working Note 292](WORKING_NOTES/292-game-state-toggle-event-callback-match-20260927.md).
The 24-word `func_1517F7B4` timer/phase updater is exact from recovered C plus
five guarded timer-base register words; see
[Working Note 293](WORKING_NOTES/293-game-timer-phase-update-match-20260927.md).
The 25-word `func_151A0950` linked-record event callback is exact directly from
C with no guarded words; see
[Working Note 294](WORKING_NOTES/294-game-linked-record-event-callback-match-20260927.md).
The 24-word `func_151A9060` indexed callback dispatcher is exact directly from
C with no guarded words after restoring the callback's object-and-index ABI;
see
[Working Note 295](WORKING_NOTES/295-game-indexed-callback-dispatch-match-20260927.md).
The 23-word `func_151C2E94` extended record validity predicate is exact
directly from C with no guarded words; see
[Working Note 296](WORKING_NOTES/296-game-extended-record-validity-match-20260927.md).
The 34-word `func_151DADA0` phase/scale updater is exact from typed embedded
state C plus four guarded phase-register words; see
[Working Note 297](WORKING_NOTES/297-game-phase-scale-updater-match-20260927.md).
The 24-word Init `func_1000B294` owner-reference repair is now byte-exact;
the object no-unroll profile is balanced by an explicit four-record source
unroll that keeps neighboring `func_1000B548` exact. The 23-word Game
`func_150233E4` resource cleanup loop is also byte-exact from typed C plus two
relocation-aware setup swaps. The 24-word Game `func_1503B95C` indexed flag
predicate is byte-exact directly from C. The 24-word Game `func_1503DA3C`
bounded record-byte lookup and 24-word `func_1503F904` actor-position query
wrapper are also exact directly from C. The 24-word `func_15044D40`
signed-coordinate event wrapper is exact directly from typed C. Continue with
26-word Game `func_1507488C`, now exact through guarded register scheduling.
The required full rebuild also exposed and repaired the stale overflow
trampoline for 19-word `func_1506EE60`. The 24-word `func_1507EE58`
complementary history-marker wrapper, 24-word `func_1508434C` counted object-
dispatch loop, 24-word `func_150B58F0` tagged table-value serializer, and
24-word `func_150C1660` typed effect-spawn wrapper are exact directly from C.
The 24-word `func_150DF8C0` mapped record-active predicate and 24-word
`func_150F1CB0` actor-state byte selector are also exact directly from typed C.
The 24-word `func_150F52B0` script-gated high-flag wrapper is likewise exact
directly from C. The 24-word `func_150FB188` actor parameter initializer is
exact from typed C plus seventeen guarded scheduling, FP-register, and
relocation words. The paired 26-word `func_1510281C` and 29-word
`func_151028AC` object-eligibility predicates are exact directly from typed C
with no guarded words. The 28-word `func_1510FE30` relative hierarchy-index
lookup and 24-word `func_1513164C` nine-argument dual dispatcher are also
exact directly from C. The 24-word `func_15133760` typed eight-float forwarding
wrapper is likewise exact directly from C. The 34-word Game `func_15142FBC`
cache-aware render-mode wrapper is exact from structured C plus three guarded
scheduling words. The 24-word Game `func_15143DA8` integer range clamp is exact
from structured C plus nine guarded register-allocation words. The 29-word Game
`func_151640C0` category-`0x29` identity filter is likewise exact from
structured C plus nine guarded register-allocation words. The 27-word Game
`func_1515F040` scaled signed fixed-point clamp is exact from typed C plus
three guarded scheduling/omission entries. The 25-word Game `func_15166204`
lifetime updater and expiry path is exact from C without guarded word patches.
The 24-word Game `func_1517EA4C` display-list state helper is exact directly
from three standard RDP macros. The 28-word Game `func_1518E298`
linked-position callback is exact directly from C with its explicit
four-argument callback ABI. The 24-word Game `func_1519ED24` scaled transform
copy is exact from typed C plus five guarded setup-scheduling words. The
27-word Game `func_1519EF04` fixed-scale transform copy is exact directly from
typed C. The 28-word Game `func_151AE640` mode-driven slot updater is exact
from structured C plus four guarded return-scheduling and branch words. The
24-word Game `func_151D5E30` four-handle cleanup loop is exact from typed C
plus three guarded null-test scheduling words. The 25-word Game
`func_15023440` resource-entry reset is exact directly from structured C.
The 25-word Game `func_1502DB20` resource-size selector is exact directly
from a switch using its original 64-entry jump table. The 26-word Game
`func_1502EE8C` record-byte classifier is exact from typed C plus six guarded
control-flow words. The 25-word Game `func_1503F108` indexed state initializer
is exact directly from typed C. The 27-word Game `func_15049260` aggregate
forwarding wrapper is exact directly from typed C. The 25-word Game
`func_1507A100` packed path-record writer is exact from typed C plus six
guarded register words. The 27-word Game `func_150829D8` state-flag selector
is exact directly from C using its retained original 69-entry jump table.
The 25-word Game `func_150FFCC8` seven-argument forwarding wrapper is exact
directly from typed C. The 26-word Game `func_1510448C` byte-scaled dispatch
is exact from typed C plus six guarded temporary-register words. The 25-word
Game `func_1510D630` counted halfword release helper is exact directly from
typed C. The 25-word Game `func_151148A8` paired matrix-construction wrapper
is also exact directly from typed C. The 26-word Game `func_1511BDF4` cached-
pointer fallback wrapper is exact directly from typed C. The 24-word Game
`func_1511BE5C` reference-relative angle update is exact directly from typed
C. The 27-word Game `func_15141250` optional owner update and callback dispatch
is exact directly from typed C. Continue with 25-word Game `func_1514ED8C`
while the smaller special-case rows remain parked. The 25-word Game
`func_1514ED8C` owner-list unlink and node release is exact directly from typed
C. The 26-word Game `func_15178C34` packed node update is exact directly from
typed C. The 26-word Game `func_15182768` conditional byte remap is exact
directly from typed C. The 29-word Game `func_1518804C` bounded record-float
update is exact directly from typed C. The 25-word Game `func_1519F48C`
linked-record retirement is exact from semantic C plus four guarded shared-
base words. The 29-word Game `func_151A931C` identity-gated event flag update
is exact from typed C plus four guarded early-return words. Its corrected byte
prototype also removes all 13 guards from exact caller `func_151A9024`, for a
net nine-row guard-table reduction. The 28-word Game `func_151928B0` type-
result selector is exact from structured C plus four guarded shared-epilogue
words while preserving its original five-entry jump table. The 25-word Game
`func_150ADA68` floating PRNG step is restored to original handwritten
assembly ownership after its equivalent C compiled one word beyond the retail
slot. The 65-word Game `func_1514563C` line-projection helper is exact after
restoring retail's dot-product operand order and guarding 18 frame and output-
register choices. The 28-word Game `func_151B3040` paired embedded-record
dispatch is exact directly from C with no guard rows. The 25-word Game
`func_151C9ED4` four-handler event broadcast is exact from recovered C plus
four guarded frame/local-slot words. The 26-word Game `func_151D13E0`
owned-state teardown is exact directly from C with no guard rows. The 25-word
Game `func_151E4E00` state-transition dispatch is exact directly from C with no
guard rows. The 26-word Game `func_151E7EF8` code-integrity checksum is exact
directly from recovered C with no guard rows. The 163-word Game
`func_151E7F60` object-slot spawn/setup routine is exact from semantic C plus
24 guarded stack-frame and local-slot words. The 41-word Game `func_151E8214`
timed mode transition is exact directly from C with no guard rows. The
76-word Game `func_151E82B8` marker-table cursor and timed mode transition is
exact from semantic C plus one guarded commuted equality-branch word. The
50-word Game `func_151E83E8` timed event transition is exact directly from C
with no guard rows. The 92-word Game `func_151E84B0` mode callback and indexed-
resource setup is exact from semantic C plus two guarded frame-size words. The
49-word Game `func_151E8620` display-list overflow guard is exact from semantic
C plus 14 guarded register-lifetime and scheduling words. The 175-word Game
`func_151E86E4` scaled, scissored texture-rectangle writer is exact from the
existing graphics macro plus four guarded vertical-scale register words. The
adjacent 819-word Game `func_151E89A0` HUD/status renderer is now reconstructed
as semantic C with retail's `0x158` frame and remains non-matching at 803 real
word differences; continue its matching pass from
[Working Note 364](WORKING_NOTES/364-game-hud-status-renderer-reconstruction-20260928.md).
The adjacent 427-word Game `func_151E966C` player-status row renderer is now
byte-exact with retail's `0x6AC` extent and `0x100` frame. Recovered SDK
display-list macros and corrected scalar/cursor lifetimes emit the semantic
routine; 116 relocation-aware guards normalize persistent IDO stack-slot,
register-allocation and scheduling differences. See
[Working Note 368](WORKING_NOTES/368-game-player-status-row-renderer-byte-match-20260928.md).
The next 273-word Game `func_151E9D18` team-counter panel is byte-exact with
retail's `0x444` extent and `0xA0` frame. SDK display-list macros, corrected
types and recovered local layout emit 271 words directly; two guarded words
normalize the final independent load/add schedule. See
[Working Note 367](WORKING_NOTES/367-game-team-counter-panel-byte-match-20260928.md).
The 20-word Init `func_10001000` startup entrypoint is also restored from its
false zero-return C placeholder to the original handwritten clear-and-jump
assembly. All 14 instruction words and six padding words match retail directly
with no guards. See
[Working Note 369](WORKING_NOTES/369-init-handwritten-entrypoint-restoration-20260928.md).
The 24-word Init `osMapTLBRdb` routine is likewise restored from its empty C
placeholder to the original handwritten CP0/TLB assembly. Its 22 instruction
words and two padding words match directly with no guards. See
[Working Note 370](WORKING_NOTES/370-init-handwritten-maptlbrdb-restoration-20260928.md).
The 20-word Init `__osSetHWIntrRoutine` is now byte-exact from recovered
libultra C compiled with its retail `-O1` object profile. See
[Working Note 371](WORKING_NOTES/371-init-hardware-interrupt-routine-match-20260928.md).
The 25-word Init `func_1000CBF0` channel-parameter updater is byte-exact after
recovering its 32-bit arguments and retail table-access shape. See
[Working Note 372](WORKING_NOTES/372-init-channel-parameter-updater-match-20260928.md).
The 28-word Game `func_15004CE0` display-list address relocator is byte-exact
after recovering signed command opcodes and the retail indexed scan shape.
This guest-side restoration is donor/reference progress for the sibling port;
it does not by itself establish a new host runtime milestone. See
[Working Note 373](WORKING_NOTES/373-game-display-list-address-relocator-match-20260928.md).
The 28-word Game `func_15033F70` object-state filter is byte-exact after
recovering the original global gate and attached-object state checks. All 112
bytes emit directly from C with no expected-word guards. This remains
guest-side donor/reference progress rather than a new host runtime milestone;
see
[Working Note 374](WORKING_NOTES/374-game-object-state-filter-match-20260928.md).
The 27-word Game `func_15034EB4` record-value adjuster is byte-exact after
recovering its global scale and optional second-record update. One guard
normalizes only a commutative floating-multiply operand order. This is also
guest-side donor/reference progress, not a new host runtime milestone; see
[Working Note 375](WORKING_NOTES/375-game-record-value-adjuster-match-20260928.md).
The 27-word Game `func_1507F454` sequence-state advance is byte-exact after
recovering its cursor and terminator-reset behavior. Six guards normalize only
compiler register allocation, including the table relocations. This remains
guest-side donor/reference progress rather than a host runtime milestone; see
[Working Note 376](WORKING_NOTES/376-game-sequence-state-advance-match-20260928.md).
The 27-word Game `func_1509CB68` active-record counter is byte-exact after
recovering its four-record unrolled table scan. Its object uses the retail
no-unroll profile, and four guards normalize only independent opening
scheduling with relocations preserved. This remains guest-side donor/reference
progress rather than a host runtime milestone; see
[Working Note 377](WORKING_NOTES/377-game-active-record-counter-match-20260928.md).
The 26-word Game `func_150A3330` record-output accessor is byte-exact after
recovering its `0x34`-byte record indexing and four output stores. It emits
directly from C without guards. This remains guest-side donor/reference
progress rather than a host runtime milestone; see
[Working Note 378](WORKING_NOTES/378-game-record-output-accessor-match-20260928.md).
The 31-word Game `func_150E36BC` actor-position query is byte-exact after
recovering its slot bounds, actor-type validation, and three float-to-integer
coordinate outputs. It emits directly from C without guards. This remains
guest-side donor/reference progress rather than a host runtime milestone; see
[Working Note 379](WORKING_NOTES/379-game-actor-position-query-match-20260928.md).
The 26-word Game `func_150F9720` dual event-byte dispatcher is byte-exact after
recovering its indexed byte pair, local event buffer, and two command-`0x42`
submissions. Eleven guarded stack-immediate normalizations preserve retail's
equivalent compact frame. This remains guest-side donor/reference progress;
see [Working Note 380](WORKING_NOTES/380-game-dual-event-byte-dispatch-match-20260928.md).
The 26-word Game `func_15108FFC` event-payload dispatcher is byte-exact after
recovering its copied descriptor, two-word-plus-byte payload, and event-`0x1D`
submission. It emits directly from C without guards. This remains guest-side
donor/reference progress; see
[Working Note 381](WORKING_NOTES/381-game-event-payload-dispatch-match-20260928.md).
The 26-word Game `func_15110360` indexed matrix compose is byte-exact after
recovering the matrix-builder ABI and typed `0x180`-byte record layout with its
matrix at offset `0xBC`. It emits directly from C without guards. This remains
guest-side donor/reference progress; see
[Working Note 382](WORKING_NOTES/382-game-indexed-matrix-compose-match-20260928.md).
The 25-word Game `func_15121C00` object float-range update is byte-exact after
recovering its six-argument forwarded call, intentionally unused middle float,
and post-call scaled-field store. It emits directly from C without guards. This
remains guest-side donor/reference progress; see
[Working Note 383](WORKING_NOTES/383-game-object-float-range-update-match-20260928.md).
The 28-word Game `func_1512D2F8` byte-timer state update is byte-exact after
recovering its two-state dispatch, tick accumulation, and indexed-duration
cutoff. It emits directly from C without guards. This remains guest-side
donor/reference progress; see
[Working Note 384](WORKING_NOTES/384-game-byte-timer-state-match-20260928.md).
The 26-word Game `func_1512D604` record ring-slot allocator is byte-exact after
recovering its indexed `0xB0`-byte record lookup, old-cursor return, cursor
increment, and wrap at 20 slots. Twenty relocation-aware guards preserve one
closed IDO register-allocation cycle. This remains guest-side donor/reference
progress; see
[Working Note 385](WORKING_NOTES/385-game-record-ring-slot-match-20260928.md).
The 29-word Game `func_1514F5CC` object-request builder is byte-exact after
recovering its typed 28-byte stack request and submission through
`func_150C0AC0`. The complete routine emits directly from semantic C without
guards. This remains guest-side donor/reference progress; see
[Working Note 386](WORKING_NOTES/386-game-object-request-builder-match-20260928.md).
The 26-word Game `func_15157F80` display-list matrix-pair builder is byte-exact
after recovering its two `gSPMatrix` appends, indexed 64-byte matrix lookup,
and ready-byte output. It emits directly from semantic C without guards. This
remains guest-side donor/reference progress; see
[Working Note 387](WORKING_NOTES/387-game-display-list-matrix-pair-match-20260928.md).
The 26-word Game `func_15168B44` packed-counter update is byte-exact after
recovering its volatile packed-word state, deliberate intermediate store,
timer refresh, and available-count subtraction path. Twenty scoped guards
normalize one closed IDO register/scheduling cycle. This remains guest-side
donor/reference progress; see
[Working Note 388](WORKING_NOTES/388-game-packed-counter-state-match-20260928.md).
The 26-word Game allocator-copy wrapper `func_15169900` and setup twins
`func_1518E66C` and `func_1518E6D4` are byte-exact after recovering their
allocator/setup call ABIs, typed fields, payload copy, descriptor selection,
and state stores. All three emit directly from semantic C without guards or
compiler overrides. This remains guest-side donor/reference progress; see
[Working Note 389](WORKING_NOTES/389-game-allocator-copy-and-setup-pair-match-20260928.md).
The adjacent Game object-ID state twins `func_151993E4` and `func_1519944C`
are byte-exact after recovering their six-entry ID scan and complementary
clear/set state writes. Two scoped register-lifetime guards per function are
required. This remains guest-side donor/reference progress; see
[Working Note 390](WORKING_NOTES/390-game-object-id-state-pair-match-20260928.md).
The second Game object-ID pair `func_1519BEB8` and `func_1519BF20` is
byte-exact from the same six-entry scan and complementary state writes. Two
scoped object-ID register-lifetime guards per function are required. This
remains guest-side donor/reference progress; see
[Working Note 391](WORKING_NOTES/391-game-second-object-id-state-pair-match-20260928.md).
The 26-word Game actor-target transform `func_151A4E34` is byte-exact after
recovering its target and type gates, indexed target-record address, and
transform-helper call. One scoped guard preserves retail's commutative
address-add operand order. This remains guest-side donor/reference progress;
see
[Working Note 392](WORKING_NOTES/392-game-actor-target-transform-match-20260928.md).
The 29-word Game timed-record lifecycle `func_1519EA04` is byte-exact after
recovering its frame-delta timer, optional owner clear, and deletion call. It
emits directly from semantic C without guards. This remains guest-side
donor/reference progress; see
[Working Note 393](WORKING_NOTES/393-game-timed-record-lifecycle-match-20260928.md).
The 124-word Game entrypoint `func_15007830` is byte-exact after recovering
its startup sequence, state-machine jump table, signed halfword arguments,
shared cleanup, and permanent dispatch loop. Sixty-six scoped guards preserve
the retail saved-register cycle and two omitted unreachable epilogue words.
This remains guest-side donor/reference progress; see
[Working Note 394](WORKING_NOTES/394-game-entrypoint-main-loop-match-20260928.md).
The 30-word Game packed-coordinate callback `func_1518CCA8` is byte-exact
after recovering its packed X/Y update, zero-Z gate, and callback-table
dispatch through the callback byte's low nibble. Ten scoped guards preserve
the retail temporary-register allocation cycle. This remains guest-side
donor/reference progress; see
[Working Note 395](WORKING_NOTES/395-game-packed-coordinate-callback-match-20260928.md).
The 27-word Game indexed 64-bit flag setter `func_1501D258` is byte-exact
after recovering its global enable gate and `D_800C3A60[index]` bit update.
The routine emits directly from semantic C without guards. This remains
guest-side donor/reference progress; see
[Working Note 396](WORKING_NOTES/396-game-indexed-64-bit-flag-setter-match-20260928.md).
The 26-word Game per-entry cleanup loop `func_15022754` is byte-exact after
recovering its indexed count pointer, zero-based iteration, and dynamic count
reload after every cleanup call. It emits directly from semantic C without
guards. This remains guest-side donor/reference progress; see
[Working Note 397](WORKING_NOTES/397-game-per-entry-cleanup-loop-match-20260928.md).
The 33-word Game linked-list match dispatcher `func_150303E4` is byte-exact
after recovering its explicit zero-key return, result lifetime, and pre-call
next-pointer capture. It emits directly from semantic C without guards. This
remains guest-side donor/reference progress; see
[Working Note 398](WORKING_NOTES/398-game-linked-list-match-dispatcher-match-20260928.md).
The 27-word Game current-record vector copier `func_1503A60C` is byte-exact
after recovering its destination pointer and three alias-sensitive indexed
source expressions. It emits directly from semantic C without guards. This
remains guest-side donor/reference progress; see
[Working Note 399](WORKING_NOTES/399-game-current-record-vector-copy-match-20260928.md).
The 28-word Game five-bucket byte canonicalizer `func_1503D5F0` is byte-exact
after recovering its directly indexed nested loops and assigning its generated
slice the retail no-unroll compiler profile. No guards are required. This
remains guest-side donor/reference progress; see
[Working Note 400](WORKING_NOTES/400-game-five-bucket-byte-canonicalizer-match-20260928.md).
The 27-word Game two-word bit test `func_1503E1F4` is byte-exact after
recovering its low/high flag-word selection, MIPS-masked variable shift, and
shared zero-return tail. No guards are required. This remains guest-side
donor/reference progress; see
[Working Note 401](WORKING_NOTES/401-game-two-word-bit-test-match-20260928.md).
The 28-word Game owner status-byte clear `func_150806A8` is byte-exact after
recovering its two high-bit-preserving clears and alias-sensitive owner-pointer
reload. No guards are required. This remains guest-side donor/reference
progress; see
[Working Note 402](WORKING_NOTES/402-game-owner-status-byte-clear-match-20260928.md).
The 28-word Game seven-group byte canonicalizer `func_15084D00` is byte-exact
after recovering its indexed table search and cached input-byte width. No
guards are required. This remains guest-side donor/reference progress; see
[Working Note 403](WORKING_NOTES/403-game-seven-group-byte-canonicalizer-match-20260928.md).
The 27-word Game resolved-object dispatch wrapper `func_1509F5F4` is byte-exact
after recovering its optional validation and narrowed forwarding call. No
guards are required. This remains guest-side donor/reference progress; see
[Working Note 404](WORKING_NOTES/404-game-resolved-object-dispatch-wrapper-match-20260928.md).
The 27-word Game packed-record activation routine `func_150A0264` is
byte-exact after recovering its two status-flag updates, alias-safe source load,
destination clear, and packed-field replacement. Twelve stale-checked guards
normalize only temporary-register allocation. This remains guest-side
donor/reference progress; see
[Working Note 405](WORKING_NOTES/405-game-packed-record-activation-match-20260928.md).
The 27-word Game indexed coordinate setter `func_150A3444` is byte-exact after
recovering its signed 16-bit parameters and three direct stores into a 52-byte
record. The alias-sensitive global-pointer reloads emit directly from C with no
guards. This remains guest-side donor/reference progress; see
[Working Note 406](WORKING_NOTES/406-game-indexed-coordinate-setter-match-20260928.md).
The 30-word Game staged halfword ramp `func_150B71A8` is byte-exact after
recovering its first-field priority, frame-scaled increments, and `0x1000`
clamps. Its branch-likely and early-return shape emits directly from C with no
guards. This remains guest-side donor/reference progress; see
[Working Note 407](WORKING_NOTES/407-game-staged-halfword-ramp-match-20260928.md).
The 29-word Game event-linked object removal filter `func_150BE150` is
byte-exact after recovering its narrowed event dispatch, direct payload match,
and event-zero linked-pointer match. An explicit payload local recovers the
retail load schedule with no guards. This remains guest-side donor/reference
progress; see
[Working Note 408](WORKING_NOTES/408-game-event-linked-object-removal-match-20260928.md).
The 27-word Game two-event command dispatcher `func_150C19C0` is byte-exact
after recovering its event-to-command mapping, owner lookup, and always-one
return. A two-case switch emits the retail forward-branch layout directly from
C with no guards. This remains guest-side donor/reference progress; see
[Working Note 409](WORKING_NOTES/409-game-two-event-command-dispatch-match-20260928.md).
The 28-word Game global-gated parameter dispatcher `func_150C7870` is
byte-exact after recovering its two global flag tests and alternate numeric
argument sets. The recovered `f32` callee prototype restores the retail
register-only call convention with no guards. This remains guest-side
donor/reference progress; see
[Working Note 410](WORKING_NOTES/410-game-global-gated-parameter-dispatch-match-20260928.md).
The 27-word Game single-byte allocation payload wrapper `func_150D0134` is
byte-exact after recovering its narrow formal arguments, pointer-returning
allocator signature, and eight-byte local payload buffer. All words emit
directly from C with no guards. This remains guest-side donor/reference
progress; see
[Working Note 411](WORKING_NOTES/411-game-single-byte-allocation-payload-match-20260928.md).
The adjacent 27-word Game float event-payload wrapper `func_150E8854` is
byte-exact after recovering its event-allocation arguments, `10.0f` payload,
successful-allocation gate, and four-byte copy into the allocated record.
Semantic C emits 25 words directly; two expected-word guards preserve retail's
lower local stack slot. This remains guest-side donor/reference progress; see
[Working Note 412](WORKING_NOTES/412-game-float-event-payload-match-20260928.md).
The adjacent 28-word Game float timer reset `func_150E88C0` is byte-exact after
recovering its frame-delta subtraction, negative-timer random reseed, and
follow-up event call. All words emit directly from semantic C with no guards.
This remains guest-side donor/reference progress; see
[Working Note 413](WORKING_NOTES/413-game-float-timer-reset-match-20260928.md).
The 29-word Game record selector-bit test `func_15114050` is byte-exact after
recovering its active-record gate, selector `-1` shortcut, `0xA0`-stride record
index, and per-selector mask lookup. All words emit directly from semantic C
with no guards. This remains guest-side donor/reference progress; see
[Working Note 414](WORKING_NOTES/414-game-record-selector-bit-test-match-20260928.md).
The 27-word Game packed-resource lazy initializer `func_15116110` is
byte-exact after recovering its empty-handle gate, packed selector and byte
extraction, resource lookup, returned-handle store, and packed-word clear.
Semantic C emits 20 words directly; seven guards preserve one closed
independent mask/register scheduling cycle. This remains guest-side
donor/reference progress; see
[Working Note 415](WORKING_NOTES/415-game-packed-resource-lazy-init-match-20260928.md).
The 27-word Game partial-zero payload allocator `func_1514DA38` is byte-exact
after recovering its 28-byte local record, intentionally untouched payload
word, allocation, copy, and type-`0x13` dispatch. Local declaration order
reproduces retail's stack map; all words emit directly from semantic C with no
guards. This remains guest-side donor/reference progress; see
[Working Note 416](WORKING_NOTES/416-game-partial-zero-payload-allocation-match-20260928.md).
The 34-word Game coordinate-equality classifier `func_15159230` is byte-exact
after recovering its unsigned mode argument, three exact float comparisons,
zero result for a full coordinate match, and mode-selected mismatch results.
Semantic C emits 22 words directly; eleven guarded tail words preserve
retail's ordinary branches and shared return instead of IDO's equivalent
branch-likely folding, and normal slice padding retains the final `nop`. This
remains guest-side donor/reference progress; see
[Working Note 417](WORKING_NOTES/417-game-coordinate-equality-classifier-match-20260928.md).
The 27-word Game resource-install callback `func_15166F6C` is byte-exact after
recovering its four-argument callback ABI, global resource-pointer install,
and nine-argument setup dispatch. Forwarding the installed global reproduces
retail's retained destination address and complete call schedule; all words
emit directly from semantic C with no guards. This remains guest-side
donor/reference progress; see
[Working Note 418](WORKING_NOTES/418-game-resource-install-callback-match-20260928.md).
The 28-word Game record-mediated dispatch `func_15173C90` is byte-exact after
recovering its byte-ID record lookup, null gate, high-bit-cleared flags, table
index, and five-argument dispatch. Semantic C emits 26 words directly; two
expected-word guards preserve retail's ordering of independent call-argument
staging instructions. This remains guest-side donor/reference progress; see
[Working Note 419](WORKING_NOTES/419-game-record-mediated-dispatch-match-20260928.md).
The 28-word Game owned cleanup-list teardown `func_15178DA4` is byte-exact
after recovering its resource stop, deletion-safe list walk, owner match, and
final record teardown. Function-scope declaration order preserves retail's
saved next-node cursor and stack slot; all words emit directly from semantic C
with no guards. This remains guest-side donor/reference progress; see
[Working Note 420](WORKING_NOTES/420-game-owned-cleanup-list-teardown-match-20260928.md).
The 27-word Game mapped three-byte-row dispatcher `func_1517F3A0` is
byte-exact after recovering its selector mapping, zero-map passthrough, packed
row lookup, and six-argument dispatch. The early-return source shape emits all
words directly with no guards. This remains guest-side donor/reference
progress; see
[Working Note 421](WORKING_NOTES/421-game-mapped-three-byte-row-dispatch-match-20260928.md).
The 27-word Game event callback-table dispatcher `func_15190550` is byte-exact
after recovering its event-`0x2A` pre-handler, object callback index, nullable
lookup, and three-argument forwarding call. Its typed body emits all words
directly with no guards. This remains guest-side donor/reference progress; see
[Working Note 422](WORKING_NOTES/422-game-event-callback-table-dispatch-match-20260928.md).
The 28-word Game four-pointer cleanup `func_151B222C` is byte-exact after
recovering its three-entry indexed release loop and final independent pointer
release. An `s32` counter explicitly narrowed after each increment reproduces
retail's loop; all words emit directly from C with no guards. This remains
guest-side donor/reference progress; see
[Working Note 423](WORKING_NOTES/423-game-four-pointer-cleanup-match-20260928.md).
The 29-word Game dual-layout owner release `func_151CB49C` is byte-exact after
recovering its event-`0x21` direct-owner comparison and event-zero nested-owner
comparison. An explicit referenced-object local reproduces retail's register
allocation; all words emit directly with no guards. This remains guest-side
donor/reference progress; see
[Working Note 424](WORKING_NOTES/424-game-dual-layout-owner-release-match-20260928.md).
The 28-word Game signed record-command writer `func_15034340` is byte-exact
after recovering its `0x32C`-byte record indexing, signed control-byte gate,
command-6 output, and signed value scaling by 200. Its deliberate second byte
read and cursor update emit directly from semantic C with no guards. This
remains guest-side donor/reference progress; see
[Working Note 425](WORKING_NOTES/425-game-signed-record-command-writer-match-20260928.md).
The 30-word Game gated active-object scan `func_150347E8` is byte-exact after
recovering its global disable gate, fixed record walk, two active-pointer
checks, and per-record dispatch. Scoping the end pointer inside the gate
reproduces retail's opening address schedule; all words emit directly with no
guards. This remains guest-side donor/reference progress; see
[Working Note 426](WORKING_NOTES/426-game-gated-active-object-scan-match-20260928.md).
The 27-word Game signed XZ coordinate-query wrapper `func_15045714` is
byte-exact after recovering its mode selection, float truncation, signed-16
coordinate narrowing, selector forwarding, and output store. Twenty-four
words emit directly from semantic C; three guards normalize one closed
position-pointer register cycle. This remains guest-side donor/reference
progress; see
[Working Note 427](WORKING_NOTES/427-game-signed-xz-coordinate-query-match-20260928.md).
The 30-word Game quaternion hemisphere normalizer `func_15049C40` is also
byte-exact after recovering its four-component dot product and conditional
in-place negation of the second quaternion. All words emit directly from
semantic C with no guards. This remains guest-side donor/reference progress;
see
[Working Note 428](WORKING_NOTES/428-game-quaternion-hemisphere-normalizer-match-20260928.md).
The 38-word Game floor-threshold state trigger `func_1506D6B4` is byte-exact
after recovering its two early exits, health-dependent state selection,
packed global update, and callback. Thirty-two words emit directly from
semantic C; six guards normalize one commutative FP operand order and a closed
integer temporary cycle. This remains guest-side donor/reference progress;
see
[Working Note 429](WORKING_NOTES/429-game-floor-threshold-state-trigger-match-20260928.md).
The 28-word Game indexed halfword-sequence dispatcher `func_15080784` is also
byte-exact after recovering its nullable sequence gate, byte-index end check,
optional nonzero halfword submission, and index advance. All words emit
directly from semantic C with no guards. This remains guest-side
donor/reference progress; see
[Working Note 430](WORKING_NOTES/430-game-indexed-halfword-sequence-dispatch-match-20260928.md).
The 28-word Game `func_150B1DB0` is restored from its false C placeholder to
original handwritten assembly ownership. Its two-block 64-bit mask/rotate
transform, trapping pointer increments, and complete linked span match retail.
This remains guest-side donor/reference progress; see
[Working Note 431](WORKING_NOTES/431-game-handwritten-two-block-word-transform-restoration-20260928.md).
The 35-word Game callback-gated record-state updater `func_150D0034` is now
byte-exact after recovering its volatile signed callback selector and
promoted status-byte mask. All words emit directly from semantic C with no
guards. This remains guest-side donor/reference progress; see
[Working Note 432](WORKING_NOTES/432-game-callback-gated-record-state-update-match-20260928.md).
The 30-word Game allocation payload wrapper `func_150D02B4` is now byte-exact
after recovering its signed-halfword parameter and 12-byte local record with
an eight-byte copied prefix. All words emit directly from semantic C with no
guards. This remains guest-side donor/reference progress; see
[Working Note 433](WORKING_NOTES/433-game-eight-byte-allocation-payload-match-20260928.md).
The 28-word Game subtype-2 allocation payload wrapper `func_150D04C4` is now
byte-exact after recovering its signed-halfword parameter and eight-byte local
buffer. All words emit directly from semantic C with no guards. This remains
guest-side donor/reference progress; see
[Working Note 434](WORKING_NOTES/434-game-single-byte-subtype2-payload-match-20260929.md).
The 28-word Game damped motion-state integrator `func_150D13A0` is now
byte-exact after recovering its five floating-field updates, three scale
constants, and final state-refresh call. All words emit directly from semantic
C with no guards. This remains guest-side donor/reference progress; see
[Working Note 435](WORKING_NOTES/435-game-damped-motion-state-integrator-match-20260929.md).
The 29-word Game validated payload dispatcher `func_150ECB8C` is now
byte-exact after recovering its target-state and selector gates, shared
failure invalidation, and six-byte payload dispatch. All words emit directly
from semantic C with no guards. This remains guest-side donor/reference
progress; see
[Working Note 436](WORKING_NOTES/436-game-validated-payload-dispatch-match-20260929.md).
The 28-word Game fixed payload-setup wrapper `func_150ECC00` is now byte-exact
after recovering its two calls, fixed argument tuple, and volatile selector
byte. All words emit directly from semantic C with no guards. This remains
guest-side donor/reference progress; see
[Working Note 437](WORKING_NOTES/437-game-fixed-payload-setup-wrapper-match-20260929.md).
The 28-word Game two-slot resource cleanup `func_150F739C` is now byte-exact
after recovering its indexed release loop and final owner cleanup call.
Twenty-three words emit directly from semantic C; five guards normalize one
redundant temporary and a closed counter-register cycle. This remains
guest-side donor/reference progress; see
[Working Note 438](WORKING_NOTES/438-game-two-slot-resource-cleanup-match-20260929.md).
The 28-word Game actor-indexed spatial-effect wrapper `func_150FFB6C` is now
byte-exact after recovering its position forwarding, actor index and halfword
derivation, flag merge, and final effect call. All words emit directly from
semantic C with no guards. This remains guest-side donor/reference progress;
see
[Working Note 439](WORKING_NOTES/439-game-actor-indexed-spatial-effect-wrapper-match-20260929.md).
The 30-word Game mode-gated table-value updater `func_15108BC0` is now
byte-exact after recovering its owner-relative record lookup, sentinel path,
mode-byte gate, and `0x44`-byte table indexing. Nineteen words emit directly
from semantic C; eleven guarded normalizations preserve retail scheduling and
its explicit table-path return-delay `nop`. This remains guest-side
donor/reference progress; see
[Working Note 440](WORKING_NOTES/440-game-mode-gated-table-value-match-20260929.md).
The 30-word Game two-command record updater `func_15109064` is now byte-exact
after recovering its command `0x1D` payload copy and command `0x1E` state
toggle. Twenty-six words emit directly from semantic C; four guarded
normalizations preserve retail's add and copy-return scheduling. This remains
guest-side donor/reference progress; see
[Working Note 441](WORKING_NOTES/441-game-two-command-record-update-match-20260929.md).
The 28-word Game record-ID lookup `func_151149AC` is now byte-exact after
recovering its reserved-zero handling and bounded scan of `0xA0`-byte records
for a matching ID at offset `0x72`. All words and four relocations emit
directly from semantic C with no guards. This remains guest-side
donor/reference progress; see
[Working Note 442](WORKING_NOTES/442-game-record-id-lookup-match-20260929.md).
The 29-word Game multiplayer-slot reset `func_151298C0` is now byte-exact
after recovering its multiplayer-mode gate and three indexed writes to the
`0x24`-byte slot table. All words and six relocations emit directly from
semantic C with no guards. This remains guest-side donor/reference progress;
see
[Working Note 443](WORKING_NOTES/443-game-multiplayer-slot-reset-match-20260929.md).
The 28-word Game per-slot mode initializer `func_15181D00` is now byte-exact
after recovering its zero and active-mode paths across the slot value, target,
pair, and mode tables. All words and twelve relocations emit directly from
semantic C with no guards. This remains guest-side donor/reference progress;
see
[Working Note 444](WORKING_NOTES/444-game-per-slot-mode-initializer-match-20260929.md).
The 28-word Game command `0x1E` record builder `func_1518AB60` is now
byte-exact after recovering its allocator call, null path, owner field, two
cleared words, and selector byte. Twenty-six words emit from semantic C; two
guarded words preserve retail's selector register allocation. This remains
guest-side donor/reference progress; see
[Working Note 445](WORKING_NOTES/445-game-command-1e-record-builder-match-20260929.md).
The 28-word Game position-descriptor dispatch wrapper `func_151C9AC0` is now
byte-exact after recovering its raised owner position, generated descriptor,
and dispatch through `func_151ABE40`. All words and both call relocations emit
directly from semantic C with no guards. This remains guest-side
donor/reference progress; see
[Working Note 446](WORKING_NOTES/446-game-position-descriptor-dispatch-match-20260929.md).
The 30-word Game child-pointer release loop `func_151BFB2C` is now byte-exact
after recovering its primary pointer release and two-entry indexed child
array. All words and both call relocations emit directly from semantic C with
no guards. This remains guest-side donor/reference progress; see
[Working Note 447](WORKING_NOTES/447-game-child-pointer-release-loop-match-20260929.md).
The 30-word Game selector-transition dispatcher `func_151AE06C` is now
byte-exact after recovering its admission gate and conditional selector
replacement. Twenty-nine words emit directly from semantic C; one guarded
word preserves a commutative equality-branch operand order. This remains
guest-side donor/reference progress; see
[Working Note 448](WORKING_NOTES/448-game-selector-transition-dispatch-match-20260929.md).
The 32-word Game timer and position updater `func_15174920` is now byte-exact
after recovering its capped timer subtraction, negative-expiry clear, and
signed halfword accumulators. All tracked words and both global relocations
emit directly from semantic C with no guards. This remains guest-side
donor/reference progress; see
[Working Note 449](WORKING_NOTES/449-game-timer-position-update-match-20260929.md).
The 61-word Game projection clamp `func_15145548` is now byte-exact after
using whole-structure assignments for its two fallback vector copies. This
recovers retail's raw three-word copy schedule and upper-clamp floating-point
temporary allocation without guards. This remains guest-side donor/reference
progress; see
[Working Note 450](WORKING_NOTES/450-game-projection-clamp-match-20260929.md).
The 29-word Game multi-argument forwarding wrapper `func_1503F5B8` is now
byte-exact after recovering its typed six-argument interface and twelve-
argument call to `func_1505E0C4`. The complete function emits from C with no
guards. This remains guest-side donor/reference progress; see
[Working Note 451](WORKING_NOTES/451-game-multi-argument-forwarder-match-20260929.md).
The 28-word Game active-object state updater `func_1507C370` is now byte-exact
after recovering its bounded object-array traversal and dispatch of three
state halfword pointers. The complete loop emits directly from C with no
guards. This remains guest-side donor/reference progress; see
[Working Note 452](WORKING_NOTES/452-game-active-object-state-update-match-20260929.md).
The 29-word Game packed descriptor builder `func_15095060` is now byte-exact
after recovering its direct-or-indexed source selection and packed field
copies into `D_800D2C90`. Relocation-aware expected-word guards preserve the
retail global-base lifetime and instruction schedule. This remains guest-side
donor/reference progress; see
[Working Note 453](WORKING_NOTES/453-game-packed-descriptor-builder-match-20260929.md).
The 28-word Game three-record dispatch loop `func_15096D08` is now byte-exact
after recovering its mode gate, nonempty-record scan, and early exit on a
successful update. The complete routine emits directly from semantic C with
no guards. This remains guest-side donor/reference progress; see
[Working Note 454](WORKING_NOTES/454-game-three-record-dispatch-loop-match-20260929.md).
The 32-word Game random remainder writer `func_15084C30` is now byte-exact;
see [Working Note 455](WORKING_NOTES/455-game-random-remainder-writer-match-20260929.md).
The 29-word Game coordinate-event wrapper twins `func_150B3E74` and
`func_150B3EE8` are now byte-exact directly from C. They share the recovered
position-to-event conversion and retain distinct final callbacks. This is
guest-side donor/reference progress; see
[Working Note 456](WORKING_NOTES/456-game-coordinate-event-wrapper-twins-match-20260929.md).
The 28-word Game actor-slot creation adapter `func_150E32D0` is now
byte-exact directly from C after recovering the full `func_150E3020` call ABI
and one-based slot result. This remains guest-side donor/reference progress;
see [Working Note 457](WORKING_NOTES/457-game-actor-slot-creation-adapter-match-20260929.md).
The 29-word Game type-`0x64` record allocator `func_15104170` is now
byte-exact directly from C after recovering its `void` contract and complete
record initialization. This remains guest-side donor/reference progress; see
[Working Note 458](WORKING_NOTES/458-game-type64-record-allocator-match-20260929.md).
The 30-word Game auxiliary-record reset `func_1511A7C0` is now byte-exact
directly from C, including its live-count float-array clearing loop. This
remains guest-side donor/reference progress; see
[Working Note 459](WORKING_NOTES/459-game-auxiliary-record-reset-match-20260929.md).
The 29-word Game zero-payload record dispatcher `func_1514DAA4` is now
byte-exact from semantic C plus two guarded independent scheduling words
around its allocator call. This remains guest-side donor/reference progress;
see [Working Note 460](WORKING_NOTES/460-game-zero-payload-record-dispatch-match-20260929.md).
The 17-word Game packed-byte submission wrapper `func_150721A4` is now
byte-exact from its existing semantic C after extending ordinary-object
padding to honor guarded contraction before overflow placement. This remains
guest-side donor/reference progress; see
[Working Note 461](WORKING_NOTES/461-game-packed-byte-submission-wrapper-match-20260929.md).
The 31-word Game accelerated-motion integrator `func_1515B994` is now
byte-exact from recovered timestep-based position/velocity integration and
averaged-velocity secondary accumulation. This remains guest-side
donor/reference progress; see
[Working Note 462](WORKING_NOTES/462-game-accelerated-motion-integrator-match-20260929.md).

Current host-port progression and acceptance boundaries:

- Training reaches Windy in normal `RelWithDebInfo`; the retained save reloads
  and the second-level Chapters unlock was user-verified.
- Windy's east-pool collision and swimming path are restored. Authored water,
  current and natural dry-ground exit were verified; this was a host-only
  repair and does not require a guest-decomp transplant. See
  [host Note 744](../../64CBFDOGL/DOCS/WORKING_NOTES/744-windy-water-collision-and-swimming-restored-20260924.md).
- The `FLY` cheat is implemented and should be used for mobility while
  scouting and resuming broad single-player progression. The accepted code is
  exactly `FLY`; this does not waive ordinary-movement checks for final route
  acceptance.
- The user reports the current play position is the Death/Grim Reaper area.
  Treat that as the next manual resume marker, not as complete level or visual
  acceptance until a dated runtime witness is recorded in the host project.
- Disabling right-stick C-button emulation (`controller_c_stick: 0`) was
  confirmed to stop controller/camera drift. It is a temporary configuration
  workaround and must be undone during the future matched camera/input pass.
- Ordinary host work remains `RelWithDebInfo`. The latest authorized Release
  artifact is frozen; do not rebuild or launch Release without a new explicit
  instruction.

These host facts are summarized here for dependency planning. The authoritative
implementation queue remains the sibling's
[current status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and
[active roadmap](../../64CBFDOGL/DOCS/roadmap.md).

## PC-port cross-project update - 2026-09-23

The sibling `64CBFDOGL` host port now completes Training through the natural Windy entrance and a fresh retained-save reload in RelWithDebInfo; repeat traversal used FLY. The user has **VERIFIED the second-level Chapters unlock**. The Gargoyle held-release repair uses original `func_15073A50` (232 bytes); guest/ROM builds and exact-byte checks are recorded in [host Note 738](../../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md). This is scoped progression evidence, not complete retail presentation or full-game acceptance.

The host-only `conker_settings.exe` is implemented with four-port device assignments, shared keyboard/controller bindings, Save and input hot reload; Video/Audio/Paths remain placeholders. It does not add an N64-ROM settings executable or replace Ares settings. See [host settings guide](../../64CBFDOGL/DOCS/CONKER_SETTINGS.md), [current host status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and [active host roadmap](../../64CBFDOGL/DOCS/roadmap.md). Host Release is frozen after the requested 2026-09-23 `conker_pc` build; the latest Training suite retains its documented baseline failures/errors. No guest matching percentage is inferred from these host milestones.

The plan below is a historical proposal for the ROM-decompilation repository.
The PC implementation now lives in sibling `64CBFDOGL`; use the active host
roadmap linked above for implementation status. Unchecked items below do not
mean the corresponding host feature is absent. This repository continues to
own guest decompilation, original-byte validation and ROM builds.

The phases are ordered by dependency, not by date. There are no target dates
here on purpose - decomp projects like this progress in bursts tied to
contributor time, not calendar time. For live decomp completion numbers, run
`make -C conker progress NON_MATCHING=1` or see
[PROJECT.md](PROJECT.md#current-progress). Published milestones are in the
[update log](UPDATE_LOG.md); temporary recovery details are in
[working notes](WORKING_NOTES.md).

## Guiding decision: hand-port vs. static recompilation

Before Phase 1 tooling work starts, pick one approach:

- **Hand-port** - rewrite the decompiled C against a new PC-native runtime
  (SDL2/GLFW + OpenGL/Vulkan), function by function, discarding libultra.
  This is the traditional path older N64 PC ports used. It only works well
  for code that has already been decompiled and matched, so it's gated by
  decomp progress. The restored-assembly baseline currently measures 85.65%
  by converted bytes and 91.04% by tracked functions; byte-exact C is measured
  separately above and in [PROJECT.md](PROJECT.md#current-progress).
- **Static recompilation** - run a MIPS-to-C recompiler (the approach used by
  projects such as [N64Recomp](https://github.com/N64Recomp/N64Recomp),
  Zelda64Recomp, and the sm64 static-recomp forks) over the ROM's compiled
  code, then connect the output to a PC-native runtime. This does **not**
  require the underlying code to be decompiled first, so it can start earlier,
  at the cost of the recompiled portions staying opaque MIPS-shaped C rather
  than readable source.

These aren't mutually exclusive: a common pattern is to statically recompile
everything, then progressively replace recompiled functions with the
hand-decompiled equivalents as decomp coverage grows. Record the decision
made (and why) in [WORKING_NOTES.md](WORKING_NOTES.md) once it's made, and
update this file's Phase 1 accordingly.

## Phase 0 - Prerequisites (current work)

This is the decompilation project as it exists today. It isn't blocking to
*start* Phase 1 under the static-recompilation path, but the following make
every later phase cheaper and safer:

- [ ] Continue matching the `init` and `game` sections (`make -C conker progress`).
- [x] Complete debugger matching: 181 / 181 converted functions are linked
      byte-exact, including the final 286-word `func_16000B14` main loop.
- [ ] Finish mapping the ROM layout (see the layout notes in [PROJECT.md](PROJECT.md#rom-layout)).
- [x] Document the RSP microcode(s) in use (F3DEX-family display lists,
      `libultra`'s `gbi.h`/`gs2dex.h` already in `conker/include/2.0L/PR/`)
      well enough to know which graphics commands a renderer needs to support.
      The sibling now has a working Conker F3DEXBG interpreter feeding RT64;
      exact command and presentation parity remains ongoing.
- [x] Document the audio microcode/sequence format (`n_libaudio.h`,
      `libaudio.h`) well enough to implement the current native audio backend.
      Complete perceptual and gameplay-audio parity remains open.
- [x] Locate and document controller/PIF input handling (how the game reads
      `OS_INPUT`/`osContGetReadData` and maps buttons/stick to game actions) -
      this now backs keyboard, mouse and SDL controller remapping in Phase 4.
- [ ] Finish the asset format work in [ASSET_FORMATS.md](ASSET_FORMATS.md) -
      the model/texture/audio containers are what a PC renderer and audio
      backend will need to load directly (or convert once, offline).

## Phase 1 - Toolchain and build target

- [x] Decide hand-port vs. static recompilation: the port uses static
      recompilation with selected native overrides and restored original bodies.
- [x] Evaluate N64Recomp and the
      [N64 Modern Runtime](https://github.com/N64Recomp/N64ModernRuntime#ultramodern)
      (`ultramodern` plus `librecomp`) against this ROM's compiler (IDO 5.3),
      libultra usage, and RCP configuration; produce a first recompiled build
      that at least links.
- [x] Stand up the separate `64CBFDOGL` sibling with its own CMake build,
      independent of the ROM-matching build in `conker/`.
- [x] Use SDL2 for windowing/input and RT64 as the graphics backend.
- [x] Complete the initial window/render smoke test. The original triangle
      milestone is superseded by visible title, menu and gameplay rendering.

## Phase 2 - OS/runtime shim

Do not start by rewriting the entire libultra layer. The
[N64 Modern Runtime](https://github.com/N64Recomp/N64ModernRuntime#ultramodern)
is a concrete candidate: `ultramodern` already covers threads, controllers,
audio, message queues, timers, RSP task handling, and VI timing, while
[`librecomp`](https://github.com/N64Recomp/N64ModernRuntime#librecomp) bridges
N64Recomp output and supplies features such as overlays, PI DMA, and save
storage. It still expects the game project to provide platform I/O callbacks
and a graphics renderer. Keep it reference-only until a compatibility spike
proves it can support Conker's Rare-specific code and microcode without
forcing changes into the byte-matching ROM build.

Whether reusing that runtime or filling its gaps locally, use the headers
already extracted in `conker/include/2.0L/PR/` (`os.h`, `os_cont.h`, `os_ai.h`,
`abi.h`, etc.) as the contract to satisfy:

- [ ] Finish the compatibility inventory that maps every libultra call used
      by Conker to `ultramodern`, `librecomp`, or a project-owned missing shim.
- [x] Pin the runtime in the separate PC build and keep
      it out of the ROM-matching `conker/` dependency graph.
- [x] Implement the threading/scheduler and message-queue path needed by the
      current PC main loop. Exact scheduler/audio timing parity remains open.
- [x] Implement PI DMA and recomp memory access against the packaged ROM/data
      image. Direct extracted-asset loading remains a separate future path.
- [x] Implement VI/framebuffer timing sufficiently for current title, menu and
      gameplay execution. Stable retail timing and uncapped operation remain
      separate acceptance items.
- [x] Implement file-backed save storage. Retained saves, reloads and
      multiplayer profile persistence have runtime evidence.

## Phase 3 - Graphics pipeline

- [x] Evaluate [RT64](https://github.com/rt64/rt64), the renderer recommended
      by `ultramodern`, against Conker's actual display lists and Rare-specific
      RSP microcode.
- [x] Integrate RT64 and implement the Conker-specific F3DEXBG/RDP path needed
      to walk current game display lists. Remaining commands and exact visual
      parity continue as scoped restoration work.
- [x] Render through RT64's original-resolution and 4:3 configuration before
      treating higher resolution or widescreen as accepted Phase 8 features.
- [ ] Get textures loading directly from the documented RGBA5551 asset
      containers (assets00-05 per [ASSET_FORMATS.md](ASSET_FORMATS.md)).

## Phase 4 - Input: keyboard, mouse, controller

The original game only understands an N64 controller read through the PIF
(`os_cont.h`). The host input bridge now supplies that contract:

- [x] Map SDL2 gamepad input to the game's existing controller-read
      call sites identified in Phase 0, so a modern controller (Xbox/PS/etc.)
      works as a drop-in replacement first.
- [x] Add keyboard movement and optional relative mouse-look as a second input
      profile. Final camera parity is still open, and the confirmed
      `controller_c_stick: 0` drift workaround is temporary.
- [x] Add rebindable input configuration through JSON and
      `conker_settings.exe`, including four controller-port assignments and
      runtime input reload.
- [x] Map game rumble requests to SDL controller vibration. Physical-device
      rumble acceptance remains open.

## Phase 5 - Audio

- [x] Reimplement the sequence/sample playback path against the SDL/native
      audio backend. Recognizable music, dialogue and effects play; complete
      timing, mix and perceptual parity remain open.
- [ ] Load audio directly from the documented MP3 streams (assets16) and the
      `"B1"` sample-bank format (assets17) per [ASSET_FORMATS.md](ASSET_FORMATS.md).

## Phase 6 - First playable milestone

This is the "playable in a keyboard/mouse/controller sense" target the rest
of the roadmap builds toward:

- [x] Boots to the title screen without running through an emulator.
- [x] Loads and progresses through Training into Windy.
- [x] Keyboard, optional mouse-look and controller paths are implemented and
      have scoped gameplay evidence. Complete device/camera parity remains open.
- [x] Save/load is functional; retained adventure saves and multiplayer
      profiles survive application restart in the tested scopes.
- [ ] Runs at a stable frame rate matching the original timing.

## Phase 7 - Stabilization

- [ ] Triage and fix crashes/undefined behavior surfaced by recompiled or
      hand-ported code that never had to run outside an emulator's
      forgiving environment.
- [ ] Add a settings menu (video, audio, controls) instead of config files only.
      The external `conker_settings.exe` input editor is complete for its
      current scope; Video, Audio and Paths are still placeholders.
- [ ] Windowed/borderless/fullscreen and multi-monitor handling.

## Phase 8 - Modern graphics update (longer-term)

Everything here assumes Phase 6 is done and stable. This is explicitly a
"plan for later," not scoped work yet:

- [ ] Uncapped/variable frame rate option (depends on the Phase 2 VI/timing shim).
- [ ] Internal resolution scaling above the original N64 output resolution.
- [ ] Widescreen/ultrawide aspect ratio support (camera and UI both need
      review - N64-era HUDs are frequently hardcoded to 4:3).
- [ ] Texture filtering options (as an alternative to the original's nearest/
      bilinear look) and, further out, an HD texture-pack pipeline built on
      the asset formats documented in [ASSET_FORMATS.md](ASSET_FORMATS.md).
- [ ] Enhanced lighting/shadows beyond what the original RDP pipeline
      produced, once Phase 3's interpreter is solid enough to extend rather
      than just replicate.
- [ ] Evaluate a modern-API renderer path (Vulkan/D3D12, or an existing
      renderer used by comparable recomp projects) as a stretch goal once
      the OpenGL path from Phase 3 is stable - this is the point where
      ray-traced lighting would become realistic to attempt, not before.

## Keeping this file honest

Check off items only once they're actually true, and update the phase text
if the plan changes - this file will go stale fast otherwise. Day-to-day
"what am I doing right now" belongs in [WORKING_NOTES.md](WORKING_NOTES.md),
not here; this file is the map, that file is the current position on it.
