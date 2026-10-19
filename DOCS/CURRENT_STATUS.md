# Current Decomp Status

Last verified: 2026-10-18

This page is the short, current handoff for `64CBFD`. Historical experiments
remain in [WORKING_NOTES.md](WORKING_NOTES.md); detailed session handoffs live
under [WORKING_NOTES/](WORKING_NOTES/).

## Repository state

- Branch: `master`
- Decomp tools now live in the separate `64CBFD-Tools` repository, pinned at
  `tools/`. See [tools repository setup](TOOLS_REPOSITORY.md) for the
  2026-10-08 split and existing-checkout bootstrap. The latest authorized
  checkpoint pins tools 943620e; tools are committed before the consumer pin.
  No push requested/performed. Preserve the independently dirty older
  standalone tools mirror without resetting or duplicating its history.
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

**Route limit switch restored and byte-exact: all 44 words**:
[Note 1581](WORKING_NOTES/1581-route-limit-switch-complete-match-20261018.md).
Replace func_1508E6D0's zero-return stub with its complete full-word switch.
All code and 63 table entries match; two checked bindings select the retained
retail table, without scheduling guards. Eight installed tests pass: 1,805
guest/native32 cases, 126 fired cuts, 18 bounded caller windows and three
executed GNU code/data maps. Actual Make reproduces the exact 221-byte image
prediction; all other 6,056 bodies, all addresses and protected data stay fixed.
Fresh Game **2997/4832 (62.02%)**, total **3670/5505 (66.67%)**, **1,835 different /
zero drift**. Tools **943620e** first; README aggregate rows only. Continue with
71-word func_1508E780, its signed-halfword mode gate and 57 active table entries.
Broader Game matching stays active; no host or Release changes.

**Route slot reservation converted directly to exact C: all 61 words**:
[Note 1580](WORKING_NOTES/1580-route-slot-reservation-direct-c-conversion-20261018.md).
Complete func_1508868C preserves signed count/base bytes, wrapping bit scan,
the real reset helper and ordered table reloads, with no new guards. Ten
installed tests pass: 1,496 guest/native32 inputs, 372 fired cuts, six effective
source negatives and eight bounded caller windows. The entire ELF, all 6,057
bodies/addresses and protected data stay fixed. Fresh Game **2996/4832 (62.00%)**,
total **3669/5505 (66.65%)**, **1,836 different / zero drift**. Tools **c1fbc31**
first; README aggregate rows only. This removes the owner's last GLOBAL_ASM,
not its remaining C stubs. Next audit the 44-word switch func_1508E6D0 and its
63-entry table; broader Game work stays active.

**Route record copy converted directly to exact C: all 40 words**:
[Note 1579](WORKING_NOTES/1579-route-record-copy-direct-c-conversion-20261018.md).
Complete void func_150885EC preserves the destination ID/state, overlap-safe
SDK copy and ordered table reloads, with no new guards. Ten installed tests pass:
448 guest/native32 cases, real SDK code/144 overlap cases, 988 fired cuts and
16 bounded actual caller windows. The entire ELF, all 6,057 bodies/addresses
and protected data stay fixed. Fresh Game **2995/4831 (62.00%)**, total
**3668/5504**, **1,836 different / zero drift**. Tools **5d8bc93** first; README
aggregate rows only. Next audit the actual 61-word func_1508868C, ending at
15088780. Broader Game work stays active.

**Route event dispatcher converted directly to exact C: all 53 words**:
[Note 1578](WORKING_NOTES/1578-route-event-dispatcher-direct-c-conversion-20261018.md).
Complete func_150880F8 preserves the null-table return, signed slot, child
status and counter order with no new guards. Eight installed tests pass:
1,760 native32/connected cases, 550 fired cuts, 261 extra guest pairs and three
GNU maps. The entire ELF, all 6,057 bodies/addresses and protected data stay
fixed. Fresh Game **2994/4830**, total **3667/5503**, **1,836 different / zero
drift**. Tools **7bc7dfc** first; README aggregate rows only. Next audit retained
40-word func_150885EC; broader Game conversion/matching stays active.

**Route actor event converted directly to exact C: all 51 words**:
[Note 1577](WORKING_NOTES/1577-route-actor-event-direct-c-conversion-20261018.md).
Replace func_1508802C's GLOBAL_ASM with the typed returning routine and correct
the stale local void declaration. Eleven installed tests pass: 1,112 native32/
guest cases, 310 fired cuts, 72 actual caller cases and three GNU maps. The
entire ELF, all 6,057 bodies/addresses, guards, Makefile and protected data stay
unchanged. Fresh Game **2993/4829**, total **3666/5502**, **1,836 different /
zero drift**. Tools **eabe57c** first. README aggregate rows only; next audit
retained 53-word caller func_150880F8. Wider Game work remains open.

**Route actor update restored and installed: all604 words exact**:
[Note1576](WORKING_NOTES/1576-route-actor-update-complete-match-and-installation-20261018.md).
Replace func_15087350's false zero-return C with its complete typed body and
source-derived guarded layout. All17 post-install tests pass; actual Make and
the original first-link prediction agree. The other6,056 bodies/addresses and
all protected Game data stay fixed; five bounded symbol-order groups are explicit.
Fresh counts: **Game2992/4828**, **total3665/5501**, **1,836 different /zero drift**.
Tools **6327a76** first; README gets aggregate rows only. Continue Game work;
next useful audit is retained51-word GLOBAL_ASM func_1508802C, not another change
to this completed routine. No host/Release action.

**Route actor update core matches through the finalizer in isolation**:
[Note 1575](WORKING_NOTES/1575-route-actor-update-casts-projection-and-finalizer-core-20261018.md).
The source-derived recipe now emits490 exact words, all20 calls and60 bindings;
ranking/return is not emitted. All15 core/retained-prefix tests pass, including
581 corpus/boundary cases,18 wide casts and1,090 fired core cuts. Raw C remains
594/frame456/450 differences; no production/count credit. Tools **3ca3f0d** first,
all23 protected inputs fixed. Continue this same routine's114-word retail tail,
live-in roles, full proof and actual integration before installation.

**Route actor update correction prefix matches in isolation**:
[Note1574](WORKING_NOTES/1574-route-actor-update-correction-prefix-layout-20261018.md).
A closed source-derived recipe emits only244 exact opening words, with no tail
or installation. Seven tests pass:553 existing corpus cases, ten added boundary
cases,850 fired caller cuts and three independent GNU maps. The raw C remains
594/frame456/450 differences; normalized-prefix cut14 closes, raw cut14 does not.
Tools **3076fa7** first; all23 production inputs/counts and old receipts stay
fixed. Continue the same function's real spills, projection/ranking and full proof.

**Route actor update core local homes and error lifetime recovered**:
[Note1573](WORKING_NOTES/1573-route-actor-update-local-homes-and-error-lifetime-20261018.md).
The new selected C keeps594 words/frame456 and reduces481 to450 differences.
Thirteen tests pass, including553 native cases per three profiles, the same
connected guest corpus,64 recovered-home/payload cases,492 screen cases and
16 caller windows. Core scalar/array homes emit at retail offsets; the ten-word
deficit and cut14 private rejection remain. Tools **b668034** first; old point/
native receipts retained separately. No production/README/count change or credit.
Continue the same function's real spills/joins, roles and all-word integration.

**Route actor update native32 qualified, matching still open**:
[Note 1572](WORKING_NOTES/1572-route-actor-update-native32-and-storage-boundary-20261018.md).
Six tests pass:553 complete native cases per O0/O2/O2+UBSan build with five real
C helpers, the same553 connected guest cases, five effective ordinary controls
and a separate fired float-cast overflow control. Ten new storage screens add
120 guest cases but no selected source. Raw594/frame456/481 differences remains
unchanged and ten words short. Tools **d4113f7** first; no production/README/
count change or credit. Continue this same function's spill/extent, private
homes/access order and all-word/integration gates. Keep the old capture intact.

**Route actor update ranking cursor recovered, matching still open**:
[Note 1571](WORKING_NOTES/1571-route-actor-update-ranking-cursor-recovery-20261018.md).
The selected complete C advances from589 to594 words, retaining frame456,
original saves/argument homes and the first15/final11 literal words. All five added
words are in the ranking tail; it remains10 words short/481 differences.
Fifteen tests pass:703 real-helper cases,12 wide-coordinate cases,228 screen
cases,16 caller windows and seven effective semantic negatives. Tools
**21db626** first; completed compiler capture audited without rerunning.
Opening28/34 still rejects at cut14. No production/README/count change or
credit. Continue the same function's conversion spill, joins, homes/roles and
native/private/all-word/integration gates. Preserve Note1568's installed totals.

**Route actor update frame and original save layout recovered**:
[Note 1570](WORKING_NOTES/1570-route-actor-update-frame-and-save-layout-recovery-20261018.md).
The complete private func_15087350 C is now589 words/frame456, with original
GP/FP saves and argument homes; first15 and last11 words match directly.
Eighteen tests pass, including703 real-helper cases and372 screen cases.
One owned compiler capture of the older point locates its480-byte frame in
upstream locals; no debugger rerun in tests. Opening prefixes improve to28/34;
cut14 first rejects T6/T8 argument temporaries. Tools **c767262** first,
including the early recapture guard that preserves completed evidence.
Still15 words short/481 differences: no production/README/count change or
credit. Continue this same604-word function's roles, homes and literal extent,
then native/private/all-word and production integration gates.

**Route actor update complete candidate, frame matching still open**:
[Note 1569](WORKING_NOTES/1569-route-actor-update-semantic-recovery-and-frame-boundary-20261018.md).
Recover the full private func_15087350 C and typed index/active/float interface,
including correction, look-ahead and stable ranking. Twelve tests pass with
703 paired real-helper cases, an independent float reference, seven effective
semantic negatives, 144 source/profile cases and 16 actual caller windows.
Raw588/frame480/599 differences fails the first private RA-store address;
all twelve screens remain non-installable. Tools **a71464c** first; production,
README and counts stay frozen at Note1568. Continue this same604-word/frame456
function's frame/homes/roles, then native/private/all-word/link qualification.

**Route record setup installed byte-exact**:
[Note 1568](WORKING_NOTES/1568-route-record-setup-installed-byte-match-20261018.md).
Replace func_150870D0's placeholder with complete typed three-argument C and
its 160-word/frame0x60 normalized match. Raw C remains 37 differences; the
explicit recipe includes copy coalescing, an epilogue-derived return restore
and the restored speculative read/gate join. Seventeen installed tests pass,
including full normalized-state prefixes, native32, callers, actual Make and
independent rebases. The first 484-byte ELF prediction reproduces with zero
metadata exceptions; all other bodies/addresses/protected data stay fixed.
Tools **38eefad** first. Fresh Game **2991/4828 (61.95%)**, total **3664/5501
(66.61%)**, **1,837 different / zero drift**. Conversion counts/bytes unchanged;
README aggregates only. Next the adjacent 604-word func_15087350 stub.

**Route setup initial S7 capture restored, matching still open**:
[Note 1567](WORKING_NOTES/1567-route-record-setup-initial-s7-capture-and-delayed-stores-20261018.md).
The experimental func_150870D0 C remains 160 words/frame 0x60 and improves
43 to 39 raw differences. Nine initial call/capture/store words now match
literally; 472 real-helper observations verify S7 and the delayed seed stores.
Eight tests pass, including guest/native32/caller checks. The cut-43 rejection
is closed; 174/465 private memory/access prefixes agree, with cut 60 now first.
Later S7/FP roles still swap. Tools **b12e663** first; production/README/counts
unchanged, zero credit. Continue the same function's reload order and later
roles before full matching/install gates. Note 1565 figures remain in force.

**Route record setup recovered, matching still open**:
[Note 1566](WORKING_NOTES/1566-route-record-setup-semantic-recovery-and-private-order-boundary-20261018.md).
The experimental three-argument func_150870D0 C emits 160 words/frame 0x60,
43 raw differences, with all 72 owner neighbors fixed. Six tests pass:
1,259 guest cases, two 1,286-case native32 profiles, real linked helpers and
41 retail caller windows. A fired private-order gate still rejects matching:
325/465 paired memory cuts differ, starting at the first seed's early store.
Tools **483ddb2** first. No production/README/count changes or matching credit.
Continue this same function's S7 capture and delayed stores, then the full
layout/padder/Make/rebase/prediction/install/audit gates. Note 1565's installed
Game 2990/4828 and total 3663/5501 figures remain unchanged, not freshly recounted.

**Route vector installed byte-exact**:
[Note 1565](WORKING_NOTES/1565-route-vector-installed-byte-match-20261018.md).
Replace func_15088F30's stub with complete typed 83-word/frame-16 C and its
closed normalized match, retaining every source origin and the original two
saved invariant roles. Thirteen installed tests pass, including 144 complete
live C caller cases, 576 bounded retail-only windows, native32 and actual
seven-command Make qualification. The 243-byte whole-ELF prediction reproduces
without metadata changes; all 6,057 addresses, other bodies and protected Game
data stay fixed. Tools **a48f19d** first. Fresh Game **2,990/4,828 (61.93%)**,
total **3,663/5,501 (66.59%)**, **1,838 different / zero drift**. README aggregate
rows only. Next the adjacent 160-word func_150870D0; the other retail caller
func_15087350 remains a three-word production stub, not retained assembly.

**Alternate route payload installed byte-exact**:
[Note1563](WORKING_NOTES/1563-route-spline-payload-native32-and-installed-byte-match-20261018.md).
Replace func_150896EC's stub with complete typed C and its305-word/frame248
normalized match. All305 source origins remain, with no insertions/omissions
or Make change. Twelve installed tests pass:6,270 native cases per three
profiles with nine effective controls,1,069 guest states,1,644 fault prefixes,
100 connected caller cases and two full rebases. All seven actual Make commands
and72 neighbors remain qualified. The1,050-byte first ELF prediction reproduces
with three closed named metadata-order groups, unchanged definitions,6,057
fixed addresses and189,088 protected data bytes. Tools **5f0358c** first.
Fresh Game **2,989/4,828 (61.91%)**, total **3,662/5,501 (66.57%)**, **1,839
different /zero drift**. README aggregates only. Next func_15088F30, the83-word
route XYZ output helper; wider Game work and explicit FP/provider limits remain.

**Route dispatcher directly byte-exact**:
[Note1559](WORKING_NOTES/1559-route-dispatcher-direct-byte-match-20261018.md).
Replace func_15087CC0's stub with typed void C; all 67 words/frame48 emit
directly under the existing owner profile, with no new guards or Make changes.
Update its sole direct caller's prototype; all 16 caller-owner bodies stay
fixed. Eight installed tests pass:1,850 guest cases,396 fired fault prefixes,
40 connected projection cases,96 rebased cases and1,824 native cases per
O0/O2/O2+UBSan build with seven effective controls. The real ELF reproduces
the214-byte first prediction; all other bodies/addresses/protected data stay
fixed. Tools **b0a32ea** first. Fresh Game **2,988/4,828 (61.89%)**, total
**3,661/5,501 (66.55%)**, **1,840 different /zero drift**. Conversion counts
remain fixed; README aggregates only. Next recover func_150896EC (305 words,
frame248), still a production stub. Vector15088F30 and wider Game work stay open.

**Route projection installed byte-exact**:
[Note1558](WORKING_NOTES/1558-route-projection-native-qualification-and-installed-byte-match-20261018.md).
Replace func_150891E8's stub with complete typed C and its321-word/frame120
normalized match. A target-only normal-profile override preserves72 no-unroll
neighbors and four GLOBAL_ASM routines. Nine installed tests pass:8225 native
cases per O0/O2/O2+UBSan build,575 complete guest cases,2148 fired nonnull fault
prefixes and40 connected retail-caller cases. The real ELF reproduces the974-byte
prediction;6057 addresses and189088 protected Game-data bytes remain fixed.
Tools **b61d10a** first. Fresh Game **2,987/4,828 (61.87%)**, total
**3,660/5,501 (66.53%)**, **1,841 different /zero drift**. Converted counts
stay5501/6044; root README aggregates only. Next recover67-word caller
func_15087CC0; vector15088F30, other parent150896EC and wider Game work stay open.

**Projection isolated normalized byte match; installation gates remain**:
[Note1557](WORKING_NOTES/1557-projection-complete-observational-proof-and-isolated-byte-match-20261018.md).
The unchanged335-word/frame120 semantic body now has a closed321-word layout
recipe matching every retail word. Complete observational proof inlines both
real helpers:7/2734 prefix paths,1/10242/6832 suffix paths, one null epilogue
and two full data/call rebases.23 tests pass. FP traps/interleaving stay excluded;
no hardware or raw nonnull-fault claim. Eight source forms remain rejected.
Tools **50e46b9**, then **d9ebeb9** first. No production/README/guard/total change.
Next native32, isolated-profile/padder qualification and first linked prediction
before installation, full ELF audit and recount.

**Projection call spill recovered; integer prefix qualified, parent still open**:
[Note1556](WORKING_NOTES/1556-projection-call-spill-and-integer-prefix-cutpoint-qualification-20261018.md).
335/frame120 jointly restores opening roles and SP+0x48; all575 full memories
agree, with445/575 public traces. Eleven tests pass, including240 null fault
prefixes,1458 first-call prefixes and a seven-entry/2734-iteration prefix
proof with two rebases. One bounded review exposes a latent CTC1 liveness
gap; independently reproduce, fix and test it. Tools **d818afc** first.
No install, guards, production/README change or new matching credit. Analyze
the14 extra prefix words and69 aligned suffix differences; full suffix/FPU,
native/rebase/fault/normalization/installation gates remain open.

**Projection normal-profile roles recovered; joint layout still fails**:
[Note1555](WORKING_NOTES/1555-projection-normal-profile-roles-and-current-node-allocation-20261018.md).
The typed loop emits334/frame120 with all six initial saved roles and240/240
null fault prefixes. Eight tests pass:575 public cases,404 complete memories,
1458 first-call prefixes and one code-identical owned compiler capture. The
remaining171 memories differ solely atSP+0x48; the current-node range is color15
and that store is absent. Sixteen screens are rejected. Tools **c77fcd2** first.
Keep this point separate from321/frame120/221; neither is installed. Production,
README and Note1554 totals are unchanged. Next recover the current-node call
lifetime jointly with the original extent, homes and saved-role order.

**Object command enqueue byte-exact; projection parent remains open**:
[Note1554](WORKING_NOTES/1554-object-command-enqueue-byte-match-20261018.md).
Replace func_1512D560's placeholder with typed command/payload enqueue C;
all41 words match after30 guards proven over both complete ordered-memory
paths. Ten installed tests pass, including352 full-memory/trace cases,
244 fault prefixes,5120 native cases per build and575 connected parent cases.
The real ELF reproduces the119-byte first prediction; all other bodies,
addresses and189088 protected Game-data bytes stay fixed. Tools **6bebb52**
first. Fresh Game **2,986/4,828 (61.85%)**, total **3,659/5,501 (66.52%)**,
**1,842 different /zero drift**. Four node-expression screens fail extent;
the parent's321/frame120/221-difference model remains uninstalled.

**Route projection allocator choices observed; no new body installed**:
[Note1553](WORKING_NOTES/1553-route-projection-allocator-choice-provenance-20261018.md).
Two owned, code-identical compiler captures show168 native events and the
current/anchor/previous/table/record/actor selection order. Initial saved colors
are not forbidden; object is already spilled at3C. Six tests pass with strict
capture/input/corruption gates; eight grouped screens are rejected. One bounded
tool-free advisory is reconciled, not accepted as a fix. Tools **4c718c5**
first. The321-word/frame120 body stays at221 differences; production/README
and totals unchanged. Continue loop/invariant expression priorities and the
joint saved-role contract, with zero new matching credit.

**Route projection extent and named homes recovered; allocation still open**:
[Note1552](WORKING_NOTES/1552-route-projection-extent-and-named-home-restoration-20261018.md).
Experimental C now emits321 words/frame120 under the existing owner profile,
with original30/3C/44/48/50/5C homes. Seven tests pass:575 equal public states
and parent frames,1458 five-slot prefixes,24 high-bit cases and effective
preference-home controls. Still221 differences:301 cases retain one different
child S0-save word, and48 null fault prefixes expose save-order differences.
Tools **f2871fa**, then **1614a2c** first. Four original-loop screens recover
opening roles but fail extent. No production/README or totals change; jointly
finish allocation/save ordering before installation. Zero new matching credit.

**Route projection conditional object lifetime recovered**:
[Note1551](WORKING_NOTES/1551-route-projection-conditional-object-lifetime-restoration-20261018.md).
Experimental302-word/frame120 C now preserves retail's null private memory,
conditional object save and nonnull SP+3C home with all seven original save
slots. Six tests pass:575 public cases,24 high-bit pointer cases,16 complete
null cases/240 fired fault prefixes and nine effective C controls. Tools
**fabe5a1** first. Still non-installable: retail321, other homes/unrolling and
raw access order remain open. Production/README and totals are unchanged;
continue the same parent's remaining fit, with zero new matching credit.

**Route projection semantics recovered; installation rejected**:
[Note1550](WORKING_NOTES/1550-route-projection-semantic-recovery-and-installation-boundary-20261018.md).
Complete experimental C for `func_150891E8` passes six tests and575 paired
guest cases with both real helpers and nine effective compiled C controls.
Raw307/frame120 versus retail321 still fails the conditional object/private
lifetime; raw read traces agree in only240/480 base cases. Tools **bc4a6e8**
first. No production/README edit or matching credit; totals below remain
unchanged. Continue the original extent/homes/unrolling fit before installation;
enqueue1512D560 still has a production C stub. Native/rebase/fault/caller and
gameplay acceptance are not claimed.

**Route neighbor preference restored and byte-matched**:
[Note1549](WORKING_NOTES/1549-route-neighbor-preference-byte-match-20261018.md).
`func_1508907C` now has complete typed C, 91 words/frame8 and its original
argument homes/S0 save. Fifty-two guards have an independent retail-vector,
4,688-path scalar CFG proof with explicit duplicate-delay gates. Seven installed
tests pass: 7,826 guest cases, 71,786 native cases/profile, 593 fault prefixes,
288 rebased cases and112 actual call/delay windows. ELF equals the first263-byte
prediction; every other byte/address and Game data are fixed. Tools **2c94753**
first. Game **2,985/4,828 (61.83%)**, total **3,658/5,501 (66.50%)**,
**1,843 different /zero drift**. Next parent150891E8; vector's two-save fit
and wider queues remain open. Root README receives aggregate rows only.

**Route vector lifetime screens rejected; production unchanged**:
[Note1548](WORKING_NOTES/1548-route-vector-lifetime-screens-rejected-20261018.md).
A fresh strict post-spline checkpoint tests28 qualifier/declaration forms.
All retain three saves;83/frame16 and82/frame16 both fail the actual first
private-store witness. Six tests pass,336 paired guest cases,72 unchanged
owner neighbors/pools,165 raw-word/four binding and26 input rejection checks.
Tools **3bd5e4e** first. No production C/guard/ELF or root README change and no
matching credit; totals below remain unchanged. Continue the two-save/inner-loop expression
fit; the old vector model's pre-spline fingerprints remain deliberately fixed.

**Route spline derivative restored and byte-matched**:
[Note1547](WORKING_NOTES/1547-route-spline-derivative-byte-match-20261018.md).
`func_150498A4` now has complete typed C,62 words/frame32, saved F20/F21 and
correct value/derivative outputs under real aliases. Forty-five guards have
a separate rounded-lineage proof with58 non-identity events/four identity
slots and strict save/read/store/restore ordering. Seven installed tests pass:
20,568 guest cases,72,352 native cases/profile,720 fault prefixes and96 whole
caller cases. Actual ELF equals the first206-byte prediction; other code,
all addresses, the matched cubic neighbor and Game data stay fixed. Tools
**bcfe55a** first. Both spline helpers now match111 retail words. Game
**2,984/4,828 (61.81%)**, total **3,657/5,501 (66.48%)**, **1,844 different
/zero drift**. Next: resume the vector builder's two-save/invariant fitting
under Note1545; its model is still uninstalled and gameplay is not claimed.

**Cubic route value helper restored and byte-matched**:
[Note1546](WORKING_NOTES/1546-route-cubic-spline-byte-match-20261018.md).
`func_150497E0` now has complete typed float-return C,49 words/frame16.
Thirty-four guards implement a proven49-operation FP-lineage bijection with
unchanged private stores and no reassociation/insertion/omission. Seven final
installed tests pass:18,212 guest cases,71,216 native cases/profile, effective
controls and the complete live caller. Actual ELF equals the first167-byte
prediction; all other code/addresses and Game data remain fixed. Tools
**b91fd0e** first. Game **2,983/4,828 (61.79%)**, total **3,656/5,501
(66.46%)**, **1,845 different /zero drift**. Next: qualify62-word derivative
`func_150498A4`; vector saved-register fitting under Note1545 remains open.
Raw read/fault/NaN limits and incomplete production helper/gameplay scope are
explicit in the note. Root README gets aggregate rows only.

**Route vector model qualified; installation rejected**:
[Note1545](WORKING_NOTES/1545-route-vector-semantic-model-and-stack-rejection-20261018.md).
`func_15088F30` has a semantic83-word/frame16 experimental C model, but76
word differences and three saves instead of retail's S0/S1 pair. Seven tests
pass, including9,205 paired guest cases,74,696 native cases per O2/O0 UBSan
profile, alias/fault/rebase controls and the complete118-word caller. The
first private save demonstrably differs; no production source/guard/ELF or
README change and zero matching credit. Tools **81049a4** first. Totals below
are unchanged. Next: fit the retail invariant/output-register lifetimes using
the pinned tests, then qualify before installation; spline stubs remain open.

**Actor route placement restored and byte-matched**:
[Note1544](WORKING_NOTES/1544-actor-route-placement-byte-match-20261018.md).
`func_15088D58` now has complete `void(u8 *actor)` C, 118 words/frame0xA8,
with the last qualifying type4 neighbor class, repeated real progress calls,
three spline positions and angle/rotation outputs. Three expected-word guards
normalize one symmetric equality and a two-word final temporary lifetime;
no schedule, frame, stack-buffer, floating-operation or profile changes.
Seven installed tests pass: 3,890 three-way guest cases, all118 target words,
555 connected retail-helper words, 69,414 native cases per O2/O0 UBSan profile,
all65,536 atan return values, eleven guest/ten native controls, thirty
independent main/helper links, 96 rebased cases, 48 paired retained-caller
windows and 1,608 fault prefixes. Native lookup/vector/spline/atan helpers are
bounded typed models; guest helpers execute retail code except the atan
provider. Five invalid conversions fail closed without invented FCSR results.
Actual ELF equals the first prediction: 362 code plus40 symbol/string-table
encoding bytes. Only target extent changes canonically; all other code and
addresses, 72 raw neighbors, prior guards and protected Game data stay fixed.
Tools **0d4af42** first. Game **2,982/4,828 (61.76%)**, total
**3,655/5,501 (66.44%)**, **1,846 different /zero drift**. Next: recover
83-word/frame0x10 `func_15088F30`, then the downstream spline stubs. The
connected retail overlays are not a claim that the current production C
call chain or full gameplay is complete.

**Record progress/lap updater restored and byte-matched**:
[Note1543](WORKING_NOTES/1543-record-progress-lap-updater-byte-match-20261018.md).
`func_15088A08` now has complete `s32(u8 *record,f32 delta)` C, 212 words/
frame0x18, with one fractional boundary step, real neighbor selection,
mode-specific events, signed lap arithmetic and capped best/finish timers.
Eighty-eight expected-word guards normalize bounded GPR roles and five
commutative address operands, not control flow, scheduling or floating ops.
Seven installed tests pass: 7,556 three-way guest cases, 72,867 native cases
per O2/O0 UBSan profile, thirteen guest/ten native controls, nine main plus
three helper links, 144 rebased cases, 36 paired original caller windows
and 1,355 access-fault prefixes. All 208 non-trap/non-duplicate words run;
all 212 words match. Reject zero division without inventing hardware results;
keep guest aliases/negative actor domains distinct from valid native objects.
Actual whole ELF equals the first prediction: 628 code bytes plus 61 symbol/
string-table encoding bytes. Only target extent changes canonically; other
bodies/addresses, all 72 raw neighbors, prior guards, profile and protected
Game data stay fixed. Tools **64c3a9f** first. Game **2,981/4,828 (61.74%)**,
total **3,654/5,501 (66.42%)**, **1,847 different /zero drift**. Next: recover
118-word/frame0xA8 `func_15088D58`, preserving its route-step loop and actor
projection/angle outputs. Both caller parents remain production stubs;
bounded caller windows are not whole-parent or gameplay acceptance.

**Five-neighbor selector restored and byte-matched**:
[Note1542](WORKING_NOTES/1542-five-neighbor-selector-byte-match-20261018.md).
`func_150888A8` now has typed `s32(u8,u8,s8)` C, 88 words/frame8, with five
byte neighbor IDs, exclusion/disable gates, nonzero-class priority and last
requested-class fallback. Sixty expected-word guards normalize bounded GPR
roles and symmetric equality operands; opcode sequence, branch displacements,
delays, memory order and both bindings remain fixed. No direct/guard-free
claim or profile change. Remove one redundant caller mask now supplied by
the typed byte parameter: all 72 raw neighbors, including the complete
34-word live C caller, retain identical bytes and relative bindings.
Seven installed tests pass: 16,584 three-way guest cases, all 7,776 category
combinations in both modes, 16,832 native cases per O2/O0 UBSan profile, nine
observable controls, nine independent links/144 rebased cases, 144 paired
whole-caller executions and 472 fault prefixes. All 85 reachable words run;
the three retail unreachable tail duplicates are preserved, not discarded.
Actual ELF equals the first prediction: 254 code bytes plus two target-size
bytes. Other bodies/addresses/definitions, old guards, build and Game data
remain fixed. Tools 155037c first. Game **2,980/4,828 (61.72%)**, total
**3,653/5,501 (66.41%)**, 1,848 different, zero drift. Next: recover the
212-word record-progress/lap updater `func_15088A08`, using the now-matched
selector and auditing its three original call sites and numeric boundaries.

**Forward record actor selector restored and byte-matched**:
[Note1541](WORKING_NOTES/1541-record-forward-actor-selector-byte-match-20261018.md).
`func_150883B0` now has typed four-argument pointer-return C, 107 words/frame0x20,
with strict positive projected-distance selection, signed actor/tag/count
fields and ordered output stores followed by fresh ID/count reads. Thirty-seven
relocation-aware guards normalize only bounded GPR roles and three commutative
integer address additions; all floating-point operations, branches, memory
access order and ten bindings remain fixed. No direct/guard-free claim.
Seven installed tests pass: 1,040 three-way guest cases, 5,328 native cases
per O2/O0 UBSan profile, twelve observable guest controls/six native controls,
nine independent links/270 rebased cases, 36 paired real caller windows and
740 fault prefixes. Guest byte aliases and negative actor address domains are
not portable native alias/object claims; FCSR and complete gameplay remain
outside scope. The retained-assembly caller's whole 4,108-byte slot is exact.
The actual whole ELF equals the first prediction: 312 code bytes and eighteen
symbol/string-table encoding bytes. Canonical definitions change only the
target extent; all 72 raw neighbors, other bodies/addresses, prior guard bytes,
build and Game data remain fixed. Tools 77d9c40 first. Game **2,979/4,828
(61.70%)**, total **3,652/5,501 (66.39%)**, 1,849 different, zero drift.
Next: audit and recover 88-word `func_150888A8`; intervening `func_1508855C`
already matches its complete 36-word slot and receives no new credit.

**Packed record separation query restored and byte-matched**:
[Note1540](WORKING_NOTES/1540-packed-record-separation-query-byte-match-20261018.md).
`func_150882E4` now has complete typed word-return C, 51 words/no frame,
including signed count/ID scanning, first non-self match and unsigned packed
separation arithmetic. Fifteen expected-word guards normalize only cursor/ID
and arithmetic temporary register roles; no control-flow, operation-order,
instruction-count or profile changes. Seven installed tests pass: 6,402
three-way guest cases, 115,457 native cases per O2/O0 UBSan profile, nine
observable controls, nine links/288 rebased cases, 144 paired caller windows
and 264 fault prefixes. Nonfinite/out-of-range conversion behavior remains
outside the qualification; no FCSR emulation claim. The production caller
parent remains a stub. All 72 raw neighbors stay fixed; actual ELF equals
the first prediction: 153 target-code bytes plus one extent byte. Other
bodies/addresses/symbols, old guard prefix, build and data stay fixed. Tools
3f4b1c9 first. Game **2,978/4,828 (61.68%)**, total **3,651/5,501 (66.37%)**,
1,850 different, zero drift. Next 107-word directed actor selector `func_150883B0`.

**Mode-dependent record heading setter restored and directly byte-matched**:
[Note1539](WORKING_NOTES/1539-record-heading-setter-direct-byte-match-20261018.md).
`func_15087EF0` now emits all 53 words/frame0x20 directly from typed void C,
with no guards or build changes. Preserve the captured record pointer,
post-helper mode/speed reads and distinct ordered float predicates, including
quiet NaNs. Seven installed tests pass: 3,168 paired guest cases, 32 extra
null/wide-index/helper-effect cases, 403,712 native cases per O2/O0 UBSan
profile, nine effective controls, six independent links/288 rebased cases,
576 bounded caller windows and 512 fault prefixes. The containing production
parent remains a stub. All 72 raw neighbors stay fixed; actual ELF equals
its first prediction: 155 target-code bytes plus one extent byte. Other
bodies/addresses/symbols, guards/build and data stay fixed. Tools e1ce81b first.
Game **2,977/4,828 (61.66%)**, total **3,650/5,501 (66.35%)**, 1,851 different,
zero drift. Next `func_150882E4`, a 51-word packed record-separation query.

**Record-driven heading clamp restored and directly byte-matched**:
[Note1538](WORKING_NOTES/1538-record-heading-clamp-direct-byte-match-20261018.md).
`func_15087E54` now emits all 39 words/frame0x18 directly from typed void C.
Recovering u16 target/delta lifetimes preserves the asymmetric 0xDBFF/0x2401
limits without guards, inserted/omitted words or profile changes. Seven
installed tests pass: 810 paired guest cases, 24 extra null/wide-index/helper
effect cases, 262,876 native cases per O2/O0 UBSan profile, seven effective
controls, six independent links/540 rebased cases, 96 bounded retail caller
windows and 272 fault prefixes. The retail caller's production parent remains
a stub; its complete gameplay behavior is not claimed. All 72 raw neighbors
stay fixed. Actual ELF equals the first prediction: 125 target-code bytes
plus one extent byte, with guards/build/data unchanged. Tools f81bd64 first.
Game **2,976/4,828 (61.64%)**, total **3,649/5,501 (66.33%)**, 1,852 different,
zero drift. Next `func_15087EF0`, the adjacent 53-word conditional heading setter.

**Enabled record tag query restored and byte-matched**:
[Note1537](WORKING_NOTES/1537-enabled-record-tag-query-byte-match-20261018.md).
`func_15022B08` now has complete typed boolean-return C, 39 words/no frame,
including the unreachable increment. Nine relocation-aware guards normalize
only a closed A0/A2 allocation cycle and independent pointer-load schedule;
no inserted/omitted instructions or profile changes. Seven installed tests
pass: 2,688 raw/normalized/retail cases, 16,384 native cases per O2/O0 UBSan
profile, seven result controls, nine independent links, 162 full restored-C
caller cases, 48 other retail windows and 472 access-fault prefixes. All 56
neighbors and the complete 84-function caller object stay fixed. Actual ELF
equals its first prediction: 117 target-code bytes plus one extent byte.
The old guard prefix and data remain unchanged. Tools 5abdd73 first. Game
**2,975/4,828 (61.62%)**, total **3,648/5,501 (66.32%)**, 1,853 different,
zero drift. Next `func_15087E54`, a 39-word angular clamp with asymmetric limits.

**Gated category pass restored and directly matched**:
[Note1536](WORKING_NOTES/1536-gated-category-pass-direct-byte-match-20261018.md).
`func_15022848` now emits all 39 words/frame0x28 directly from typed void C,
preserving its exact-one gate, context flag and live count after each callback
pair. The slice's existing no-unroll profile is retained; no guards or build
changes. Seven installed tests pass: 4,902 paired guest cases, 14,336 native
cases per O2/O0 UBSan profile, seven effective controls, 126 rebased sequences,
126 bounded caller windows and 760 fault prefixes. All 56 raw neighbors,
including the caller, stay fixed after correcting the local declaration.
Actual ELF equals its first prediction: 130 target-code bytes plus one extent
byte. Tools 3cc55c3 first. Game **2,974/4,828 (61.60%)**, total
**3,647/5,501 (66.30%)**, 1,854 different, zero drift. Both callback bodies
remain stubs. Next `func_15022B08`, a 39-word frameless enabled-record tag query.

**Actor snapshot packet restored and directly matched**:
[Note1535](WORKING_NOTES/1535-actor-snapshot-packet-direct-byte-match-20261018.md).
`func_151AB930` now emits all 38 words/frame0x48 directly from typed void C,
including the full 0x1C-byte copy and six inherited padding bytes. No guards,
profile or Makefile changes. Seven installed tests pass: 6,000 paired guest
cases, native O2/O0 UBSan, effective controls, 54 rebased sequences, 48 actual
caller/helper chains and 1,920 fault prefixes. Correct the direct caller's
prototype/cast without changing its complete 328-function object. Actual ELF
equals the first prediction: 118 target-code bytes plus one extent byte.
Other bodies/addresses/symbols, guards and data stay fixed. Tools 0f19fe7 first.
Game **2,973/4,828 (61.58%)**, total **3,646/5,501 (66.28%)**, 1,855 different,
zero drift. Next `func_15022848`, 39-word gated category pass with a live byte
count and two ordered helper calls per entry; audit its caller ABI first.

**Fractional point outputs restored and directly matched**:
[Note1534](WORKING_NOTES/1534-fractional-point-outputs-direct-byte-match-20261018.md).
`func_15107AE0` now has a typed four-pointer void interface and retains original
deltas across sequential output stores. Exact 0.333f/0.6667f literals reproduce
all 38 words/no frame after the existing per-owner rodata binding, with zero
instruction guards or profile override. Seven installed tests pass: 10,240
finite overlap cases, native O2/O0 UBSan, effective controls, pool rebases,
24 bounded retail caller windows and 2,888 fault prefixes. Actual ELF equals
its first full-link prediction: 122 target-code bytes plus one extent byte.
Other bodies/addresses/symbols, guards and original data are fixed. Tools
4d3a3d8 first. Game **2,972/4,828 (61.56%)**, total **3,645/5,501 (66.26%)**,
1,856 different, zero drift. Next `func_151AB930`, 38-word stack-packet creator;
qualify helper contracts and inherited padding before copying its 0x1C bytes.

**Record flag refresh restored and directly matched**:
[Note1533](WORKING_NOTES/1533-record-flag-refresh-direct-byte-match-20261018.md).
`func_15113180` now refreshes bit0x40 across the 0xA0-byte records with live
base/count reloads. All 38 words/no frame emit directly from void C with no
guards. Its sole observed caller discards V0; correcting its declaration
leaves the actual caller object byte-identical. Seven final tests pass,
including 14,336 guest flag cases, exhaustive native O2/O0 UBSan, six effective
memory-changing controls, independent rebases/aliases and 462 fault prefixes.
Actual ELF equals its first full-link prediction: 111 target-code bytes plus
one extent byte; other bodies/addresses/symbols, guards and Game data are fixed.
Tools d13c136 first. Game **2,971/4,828 (61.54%)**, total **3,644/5,501 (66.24%)**,
1,857 different, zero drift. Next `func_15107AE0`, 38-word dual fractional-point
output; retain its exact 0.333f/0.6667f constants and alias-sensitive reloads.

**YXZ matrix constructor restored and directly matched**:
[Note1532](WORKING_NOTES/1532-yxz-matrix-constructor-direct-byte-match-20261018.md).
`func_151102CC` now builds Y rotation, composes X, then composes Z using one
local matrix. All 37 words/frame0x68 emit directly from C with no guards.
Seven final tests pass, including 544 guest cases, native O2/O0 UBSan, four
effective controls, real matrix kernels, 12 mixed-angle wrapper/alias cases
and 180 target-memory fault prefixes. Actual ELF equals its first full-link
prediction: 118 target-code bytes plus one extent byte. All other bodies,
addresses, symbol definitions, guards and Game data remain fixed. Tools
236d562 first. Game **2,970/4,828 (61.52%)**, total **3,643/5,501 (66.22%)**,
1,858 different, zero drift. Next same-owner `func_15113180`, 38-word record
flag updater; verify caller result use and alias-sensitive reloads first.

Actor **handle-first resource retirement restored and matched**:
[Note1531](WORKING_NOTES/1531-actor-handle-resource-retirement-byte-match-20261018.md).
`func_15101090` now stops the unsigned handle, retires five ordered resources,
then retires its actor. All 46 words/frame0x20 match with three handle-register
guards; raw C remains three differences. Seven installed tests pass, including
5,120 guest cases, native O2/O0 UBSan, seven effective controls, 4,488 memory
fault prefixes and 256 real dispatcher sequences. Actual ELF equals its first
full-link prediction: 140 target-code bytes plus one extent byte; all other
bodies/addresses/symbols and Game data are fixed. Tools 29952ff first.
Game **2,969/4,828 (61.50%)**, total **3,642/5,501 (66.21%)**, 1,859 different,
zero drift. Next ordinary C target `func_151102CC`, 37-word matrix construction.

Actor **owned-resource cleanup restored and matched**:
[Note1530](WORKING_NOTES/1530-actor-owned-resource-cleanup-byte-match-20261018.md).
`func_15101148` now has typed, commented void cleanup C: five ordered releases,
then actor destruction. All 40 words/frame0x20 match with three first-argument
register/setup guards; raw C stays three differences. Seven final tests pass,
including native O2/O0 UBSan, callback mutation, aliasing, 1,928 fault prefixes
and 128 actual dispatcher sequences. Real ELF equals the first full-link
prediction: 122 target-code bytes plus one extent byte; all other bodies,
addresses, symbol definitions and Game data are fixed. Tools e371724 first.
Game **2,968/4,828 (61.47%)**, total **3,641/5,501 (66.19%)**, 1,860 different,
zero drift. Next paired `func_15101090` handle/resource cleanup, 46 words.

Rectangle **private clipping homes byte-matched**:
[Note1529](WORKING_NOTES/1529-rectangle-private-clipping-homes-byte-match-20261018.md).
All 346 words/frame0x88 of `func_15095D34` now match after six closed private-
home guards; raw semantic C remains six differences. Fresh compiler captures,
384 CFG states, 5,760 paired executions and 2,912 fault prefixes qualify the
ABI-owned frame mapping. Nine target tests, twelve source regressions and
the strengthened child-identity check pass. Actual ELF equals its six-byte
target-only prediction with all other bodies/addresses/symbols/data fixed.
Tools bcedfb7 first. Game **2,967/4,828 (61.45%)**, total **3,640/5,501
(66.17%)**, 1,861 different, zero drift. Next ordinary C target:
`func_15101148`, 40-word resource cleanup; retain handwritten ABI deferrals.

Rectangle **direct C improvement, 18 to six differences**:
[Note1528](WORKING_NOTES/1528-rectangle-flip-order-direct-c-improvement-20261018.md).
`func_15095D34` now emits all twelve flip words directly after two source
assignment-order changes. Still 346 words/frame0x88, now 205 literal opening
words, no old exact losses or new guards. All 13 final tests pass; the actual
ELF equals the emitted-C prediction with only 21 target bytes changed among
6,057 bodies and unchanged symbols/data. Tools d8111ab first. Totals below
and root README stay unchanged. Continue at **0x15096068**: six private
clipping-home accesses remain unresolved; do not force their stack offsets.

Movement **state machine installed, 959 words byte-exact**:
[Note1527](WORKING_NOTES/1527-movement-state-machine-production-installation-20261018.md).
`func_150F34F4` now has its complete typed semantic C body in production.
All 959 words/frame0x80 match after 134 qualified guards; raw C still has
134 differences. The actual full ELF equals the first 3,579-byte prediction:
3,010 code bytes, two extent bytes and 567 explicitly closed metadata bytes,
with no exclusions. All 6,057 bodies/addresses, 189,088 Game-data bytes /
720 owners, callback and actual target object/167 relocation sites pass.
All 25 installed tests and the strengthened object audit pass. Tools
ddd9d88 first. Fresh Game **2,966/4,828 (61.43%)**, total **3,639/5,501
(66.15%)**, 1,862 different, zero drift. Conversion unchanged; README only
updates aggregate rows/date. Next reopen rectangle `func_15095D34` (346
words / 18 real differences), respecting Notes 1440/1441's native blockers.

Movement **complete private byte match qualified**:
[Note1526](WORKING_NOTES/1526-movement-complete-private-byte-match-20261018.md).
Complete `func_150F34F4` now matches all 959 words/frame0x80 after 134 private
rows; raw C is unchanged at 134 differences. The last 88 differences close
with a call-invalidated tail permutation and two independently relocated
ADDIU words. All 21 tests pass, including 325 tail controls, 324 poisoned
call cases, 24 bound-symbol rebases and 392 complete private states / 30,629
equal prefixes. Tools cc0020c first; 319 inputs, production, totals and main
README stayed unchanged at that checkpoint. Note1527 above now installs
and audits the real successor; this paragraph records the private stage.

Movement **physics-call temporary roles qualified**:
[Note1525](WORKING_NOTES/1525-movement-physics-call-register-roles-20261018.md).
The unchanged complete `func_150F34F4` still has 134 raw differences. Fifteen
new private rows extend the 31-row research table to 46: 88 normalized
differences and 633 exact opening words, still 959/frame0x80. Local and
continuation proofs cover both sides of the injective map. The private
frontier advances to `0x150F3EE0`, with 8,844 equal prefixes / 100 active
states. Production, totals and main README remain unchanged; no installation
or matching credit. Continue the same function at `0x150F3ED8`: 86 remaining
GPR-field-only differences and the address schedule at `0x150F4098/9C`.
Eighteen tests pass, including 89 effective controls and 576 poisoned call
cases / 384 mutations. Tools d5406cd first; 317 inputs and prior mirror hashes
preserved. No Claude call or frozen Release action.

Movement **coefficient read/store schedule recovered**:
[Note1524](WORKING_NOTES/1524-movement-coefficient-read-store-schedule-20261017.md).
Complete `func_150F34F4` improves 139 to 134 raw differences, 108 to 103 after
the unchanged 31 private rows. Five C words change and become exact; no old
exact losses. Still 959/frame0x80 and 478 exact opening words. Sixteen tests
pass, including 640 coefficient cases / 320 old-C rejections and 52 layout
controls. Tools 12befaa first; 315 inputs, production, totals and main README
unchanged. One read-only advisory reconciled; no new guards/installation/credit.
Next qualify the 149-word register window with fifteen differing words;
static correspondence alone is not a certificate. Wider matching stays open.

Movement **scalar lifetimes and counter scope recovered**:
[Note1523](WORKING_NOTES/1523-movement-scalar-lifetimes-and-counter-scope-20261017.md).
Complete `func_150F34F4` improves 152 to 139 raw differences, 121 to 108 with
the byte-identical 31 private rows. Thirteen gains emit directly from C, with
no old exact losses. Still 959/frame0x80 and 478 exact opening words. Fifteen
tests pass, including twelve AST controls, exact 24-record counter scans and
397 native cases/profile. Tools 5910e6c first; 313 inputs, production, totals
and README unchanged. No new guards/installation/credit. Same earlier flag
and private gaps remain; 101 GPR-field-only / seven other words need work.

Movement **surface source order recovered**:
[Note1522](WORKING_NOTES/1522-movement-pitch-and-surface-source-order-20261017.md).
Complete `func_150F34F4` improves 200 to 152 raw differences, 169 to 121 with
the byte-identical 31 private rows. All 48 gains emit directly from C; no old
exact words are lost. Still 959/frame0x80, first 478 normalized words exact.
Thirteen tests pass, including 256 new surface cases / sixteen old-read
rejections. Tools 74c3bf7 first; 311 inputs, production, totals and README
unchanged. No new guards/installation/credit. Same earlier flag/private gaps
remain; 111 GPR-field-only and ten other words need recovery/proof.

Movement **release indexing, speed read and heading roles recovered**:
[Note1521](WORKING_NOTES/1521-movement-release-index-speed-copy-and-heading-roles-20261017.md).
Complete `func_150F34F4` improves to 200 raw differences / 169 with 31 private
rows, still 959/frame0x80, first 478 normalized words exact. Twelve tests pass,
including 100 old speed-read rejections, 480 heading cases and 6,700 prefixes.
Tools 201eff8 first; 309 inputs, production, fresh totals and README unchanged.
Three new research rows, zero production rows/installation/credit. Continue
the same flag/constant roles at `0x150F3C6C`, private gap `0x150F3C88`, and
remaining FP/surfacing/full-function gates.

Movement **clamp/acceleration/pitch lifetimes recovered**:
[Note1520](WORKING_NOTES/1520-movement-clamp-acceleration-and-pitch-lifetimes-20261017.md).
Complete `func_150F34F4` improves to 270 raw differences / 242 after the same
28 private research rewrites, still 959/frame0x80. Nine tests pass, including
sixteen old-candidate alias rejections and AST zero-lifetime checks. Tools
ad45714 first; 307 protected entries, production, fresh totals and README
unchanged. No new guards/installation/credit. Continue the same heading GPR
gap at `0x150F3C48`, private frontier `0x150F3C6C`, and remaining full gates.

Movement **button velocity and branch CFG roles qualified**:
[Note1519](WORKING_NOTES/1519-movement-flag-path-lifetimes-and-cfg-role-proof-20261017.md).
Raw `func_150F34F4` C improves to 389 differences; 28 total private research
rewrites give 361 differences and 469 exact opening words, still 959/frame0x80.
Nine tests pass, including 3,072 adverse kernel cases and 6,600 active prefixes.
Tools 852c2eb first; 305 protected entries, production, totals and README
unchanged. Not installed/credited. Continue the same routine at `0x150F3C48`
and private gap `0x150F3C6C`; remaining whole-function gates stay open.

Movement **bounded turn-role certificate qualified**:
[Note1518](WORKING_NOTES/1518-movement-turn-role-certificate-and-argument-controls-20261017.md).
Raw `func_150F34F4` C remains 959 words/frame `0x80`, 392 differences. Seven
private research rewrites leave 385 differences and 406 exact opening words.
Eight tests and two focused checks pass, including 480 adverse kernel cases
and 5,900 normalized active prefixes. No production guards/installation/credit.
Tools a0ea7dd first; 303 protected entries, production, fresh totals and README
unchanged. Continue the same controller/flag GPR lifetimes at `0x150F3B4C` /
`0x150F3B58`, then all remaining whole-function gates.

Movement **float lifetimes and field heading recovered**:
[Note1517](WORKING_NOTES/1517-movement-float-lifetimes-and-field-heading-recovery-20261017.md).
Complete `func_150F34F4` retains 959 words/frame `0x80`, now 392 differences
and 361 exact opening words. Eight tests pass, including 4,600 equal active
prefixes across 100 states; all FPRs agree at the first remaining GPR gap.
Tools 7a40f3f first; 301 protected entries, production, fresh totals and README
unchanged. Not installed or credited. Continue the same temporary GPR ordering
at `0x150F3A98` and private gap at `0x150F3AB8`, then the remaining full gates.

Movement **preloads and smoothing lifetimes recovered**:
[Note1516](WORKING_NOTES/1516-movement-preloads-and-smoothing-lifetimes-20261017.md).
Complete `func_150F34F4` retains 959 words/frame `0x80`, now 420 differences
and 337 exact opening words. Eight tests pass: 880 active prefixes, all 160
mode-0 private states / 8,320 fault prefixes, and the prior disabled paths.
Tools de8f5ff first; all 299 protected entries, production, totals and README
unchanged. Not installed or credited. Continue the same high-position velocity
allocation at `0x150F3A38`, then the smoothing/private gap at `0x150F3AB8`.

Movement **return boundary and full-width buttons recovered**:
[Note1515](WORKING_NOTES/1515-movement-return-boundary-and-full-width-buttons-20261017.md).
Complete `func_150F34F4` now has 959 words/frame `0x80`, 475 differences and
137 exact opening words. Eight tests pass, including 800 active prefixes and
80 complete disabled private states / 2,700 disabled fault prefixes. The next
gaps are mode-0 preloads and active FPR4/FPR18 allocation. Tools 22cdaac first;
297 protected entries, production/checkpoints, totals and root README unchanged.
Not installed or credited; continue the same complete literal matching work.

Movement **controller allocation recovered; return gap remains**:
[Note1514](WORKING_NOTES/1514-movement-controller-allocation-and-pickup-access-order-20261017.md).
The complete `func_150F34F4` candidate retains 959 words/frame `0x80`, improves
744 to 721 differences and matches its opening 66 words. Eight tests pass;
460 initial private prefixes agree across twenty states. The next gap is
disabled-path branch/PC provenance, not the controller register. Tools f63eb42
first; all production/checkpoints, aggregate totals and root README unchanged.
Not installed, no matching credit; continue the same complete routine.

Actor input/movement **retail extent, frame and live homes restored**:
[Note1513](WORKING_NOTES/1513-movement-retail-extent-frame-and-live-homes-20261017.md).
The full `func_150F34F4` candidate now emits 959 words/frame `0x80`, with
744 differences. Four compiler captures bind the live homes; seven full tests
(182.922s) and two focused checks (25.191s, 49 effective controls) pass.
The first ten modeled fault boundaries now agree in eight initial states;
cut 10 still differs in controller GPR3/GPR10 at `0x150F3544`. Not installed;
no new guards or matching credit. All 290 protected entries and the complete
production baseline remain intact. Tools f0fadc5 first; preserve 1,150 prior
mirror hashes / 1,152 paths. Fresh totals and README unchanged. Goal active:
continue this same routine's allocation, scheduling and full private matching.

Actor input/movement **fully recovered; extent/frame fitting remains open**:
[Note1512](WORKING_NOTES/1512-actor-input-movement-recovery-and-fitting-boundary-20261017.md).
The complete `func_150F34F4` candidate emits 962/959 words, frame `0x70`/`0x80`,
811 overlapping differences. The padder rejects its three-word overflow;
private state differs at cut zero. Eleven tests pass (72.175s): 2,496 core
comparisons, 947 reachable words / twelve statically unreachable duplicates,
native32, mutations and effective controls. All 284 protected entries and the
complete production ELF remain unchanged; no guards/installation/credit.
Tools 6f22514 first; preserve all 1,146 prior mirror hashes / 1,150 paths.
Fresh totals remain Game **61.41%**, total **66.13%**, zero drift; README
unchanged. Goal active: continue this same routine's real scalar homes/frame,
extent, then register/schedule/private matching before installation.

Owner burst emitter **restored and byte-exact with twenty bounded guards**:
[Note1511](WORKING_NOTES/1511-owner-burst-emitter-restoration-and-match-20261017.md).
`func_150F2D14` now matches all 288 words/frame `0x150`: actual literal-pool
binding and real scalar homes resolve the storage gap; two closed groups
normalize the remaining allocation/schedule differences. Seven installed
tests (58.929s), seven research tests (91.351s) and four historical checks
(85.068s) pass. The entire first normal ELF equals its 993-byte prediction,
with zero exclusions; all 6,057 bodies and 189,088 Game-data bytes audited.
Fresh Game **61.41%**, total **66.13%**, zero drift. Tools 971eddb first;
preserve 1,133 unrelated mirror hashes / 1,146 paths. README aggregates only.
This checkpoint was paused when banked; the resumed `func_150F34F4` work is
recorded above. The gate, fade gaps and full runtime remain open.

Owner burst emitter **12 extra UOPT bytes traced to three reservations**:
[Note1510](WORKING_NOTES/1510-owner-burst-uopt-reservations-and-source-controls-20261017.md).
Two normal-object-identical traces bind the slots to actor+0x28, owner state
and its integer conversion; no explicit output M operands target those slots.
Four tests pass (51.504s), with 78 effective controls. Frame-only source
changes overflow; the literal-scale pool remains unqualified. No installation,
guards or matching credit. Tools a825058 first; preserve 1,137 prior mirror
hashes / 1,139 paths. Production, fresh totals and README unchanged. Continue
this same function's reservation eligibility/register dataflow, then full match.

Owner burst emitter **public packet padding resolved; private frame still open**:
[Note1509](WORKING_NOTES/1509-owner-burst-frame-trace-and-aligned-packet-qualification-20261017.md).
Three fingerprint-locked traces bind compiler storage to seven emitted
addresses. The aligned alternative matches all caller-relative packet
addresses and 3,928 complete public comparisons, without padding masks.
Six tests pass (68.711s), with 39 fail-closed controls. It still emits 288
words/frame `0x160`, 85 unequal words and a 16-byte private SP gap: not
installed, no new guards or matching credit. Tools c2c5a97 first; preserve
1,134 prior mirror hashes / 1,137 paths. Production ELF, fresh Game **61.39%**,
total **66.12%**, zero drift and README unchanged. Continue this same function
at UOPT local-area expansion/scalar homes, then register roles and scheduling.

Owner burst emitter **fully recovered as an uninstalled candidate**:
[Note1508](WORKING_NOTES/1508-owner-burst-emitter-recovery-and-private-layout-gap-20261017.md).
`func_150F2D14` emits 288 words, but frame `0x158` versus `0x150` and 85
unequal words remain. Six research tests pass, including explicit rejection
checks: nonuniform stack bytes expose nine copied padding differences, and
private state already diverges at fault cut zero. No guards or production
inputs change; matching credit is zero. Tools 44ac35d first; preserve all
1,132 prior mirror hashes / 1,134 paths. Fresh totals remain Game **61.39%**,
total **66.12%**, zero drift; README unchanged. Continue this same function's
automatic-storage, packet offsets, register roles and scheduling.

Actor scale/timer **restored and byte-exact with two multiply guards**:
[Note1507](WORKING_NOTES/1507-actor-scale-timer-restoration-and-match-20261017.md).
`func_150F3214` matches all 90 words/frame `0x28`. Seven installed and nine
affected historical checks pass; the complete first normal ELF equals its
267-byte declared-change prediction, with zero exclusions. All 6,057 bodies
and 189,088 Game-data bytes are audited. Fresh Game **61.39%**, total
**66.12%**, zero drift. Tools e033fe7 first; preserve 1,124 unrelated mirror
hashes / 1,132 paths. README aggregates only. Next: `func_150F2D14` (288 words,
frame `0x150`); the 139-word gate and both fade lifetime gaps remain open.

Indexed threshold mask **restored and byte-exact directly from C**:
[Note1506](WORKING_NOTES/1506-indexed-threshold-mask-direct-restoration-and-match-20261017.md).
func_150F33F8 emits all42 words/frame0 with no new guards. Seven installed
tests and two affected historical checks pass. The complete first normal ELF
matches its prediction:124 code/one extent/24 exactly accounted metadata bytes,
zero exclusions. All6,057 bodies and189,088 Game-data bytes are audited; only
the target body changes and every address remains fixed. Fresh Game **61.37%**,
total **66.10%**, zero drift. Tools6a6aca2/9a968aa first; preserve1,120 unrelated mirror
hashes /1,128 dirty paths. README changes only aggregate rows. Next:
func_150F3214; the139-word gate, both fade lifetime gaps and wider Game stay open.

Actor-record gate **actual register reuse observed; reload-only control rejected**:
[Note1505](WORKING_NOTES/1505-actor-record-gate-register-reuse-and-reload-control-20261017.md).
Both gate-load nodes share one lookup result; emission materializes one memory
load into GPR2 and uses it for both predicates. Four fresh tests pass, with41
provenance/five lifecycle controls. A diagnostic reload control emits139 words
but fails134 words and private fault cut0; it is not a recovered qualifier or
installable fix. Production, totals and README unchanged. Tools8a5bfb6 first;
preserve1,122 mirror hashes /1,124 paths. Continue block752 actor-address
rematerialization and saved-register pressure in the same target; Game stays open.

Actor-record gate **shared expression image observed before global passes**:
[Note1504](WORKING_NOTES/1504-actor-record-gate-expression-image-sharing-20261017.md).
Two distinct opening-load nodes acquire one image during input construction,
before patchvectors/copypropagate/codemotion. A fresh normal capture preserves
the complete object and all child/driver exits; three tests,33 provenance
controls and five lifecycle controls pass. No production/guard/CSV/README
change or matching credit. Toolsf983786 first; preserve1,120 mirror hashes
/1,122 dirty paths. Continue the same target's expression-image lookup and
later reuse decision, plus actor-address rematerialization; wider Game stays open.

Actor-record gate **compiler stages qualified; prolog-only control, no install**:
[Note1503](WORKING_NOTES/1503-actor-record-gate-compiler-stages-and-prolog-control-20261017.md).
Three UOPT captures and one CFE/UOPT/UGEN wire capture preserve their complete
normal objects and prove the prepared optimizer's global-load CSE, loop-test
rewrite and bound/address promotion. A bounded remaining-count control removes
S5 and emits the exact first eight retail words; seven early fault prefixes
agree, then cut7 rejects the opening global-load state. The full control is
135/139 words with130 padded-slot differences, worse overall than the original
137-word/120-difference candidate. Five new tests pass; no source or guard is
installed and no matching credit is added. Production ELF/data/CSV and README
remain unchanged. Tools40a1e62 first; preserve1,118 unrelated mirror hashes
/1,120 dirty paths. Continue the same target's opening CSE/rematerialization;
both fade lifetime gaps and wider Game stay open.

Actor-record gate **semantic recovery banked, not installed or matching**:
[Note1502](WORKING_NOTES/1502-actor-record-gate-recovery-and-private-mismatch-20261017.md).
func_150F2A60's candidate has137/139 words, frame0x40,118 overlapping-word
differences and120 full padded-slot differences. Five recovery tests pass,
including actual28-word lookup/six-word offset setter and native32. Private
fault cut2 already rejects the saved-register lifetime, and the initial global
read count is1 instead of2. Seven reproducible screens and one bounded advisory
yield no installable fix. All253 protected inputs /233 paths, the complete
production ELF and189,088 Game-data bytes remain unchanged. Matching totals
stay Game61.35%, total66.08%, zero drift. Toolsb0ae735 first; preserve1,116
unrelated mirror hashes /1,118 dirty paths. Continue this same139-word target;
next inspect normal compiler live ranges/CSE rather than repeating equivalent
source forms. Both fade lifetime gaps and wider Game remain open.

Actor-state update and ordered event-value dependency **restored and byte-exact
directly from C**:
[Note1501](WORKING_NOTES/1501-actor-state-and-event-value-direct-restoration-and-match-20261017.md).
func_150F26A0/func_150F2994 emit all189/48 words, both frame0x28, with no new
guards, pools or profile changes. Eight installed tests and three selected
historical checks pass. The complete first normal image matches:767 code/three
extent/zero metadata bytes; all6,057 bodies and189,088 Game-data bytes audited.
All nine linked functions in generated_11F780 are now byte-exact. Fresh Game
**61.35%**, total **66.08%**, zero drift. Tools2fae596 then whitespace-only
3daba3b before the consumer pin; preserve1,110 unrelated mirror hashes /1,116
dirty paths. Next: func_150F2A60, owner generated_11FF10. Both fade lifetime
gaps and wider Game remain open.

Owner-relative point update **restored and byte-exact directly from C**:
[Note1500](WORKING_NOTES/1500-halfword-point-update-direct-restoration-and-match-20261017.md).
func_150F25A0 emits all64 words, frame0x88, with the actual matrix/point homes,
repeated owner/destination pointer loads and signed truncation before the three
halfword stores. No new guards, pools or compiler-profile changes. Eight installed
tests and three selected historical checks pass. The entire first normal image
matches:174 code/two extent/zero metadata bytes; all6,057 bodies and189,088
Game-data bytes audited. Fresh Game **61.31%**, total **66.04%**, zero drift.
Toolsa1a59ae first; preserve1,106 unrelated mirror hashes /1,112 dirty paths.
Its next target and dependency are finished in Note1501. Both fade lifetime gaps and wider Game remain open.

Selector point transform **restored and byte-exact directly from C**:
[Note1499](WORKING_NOTES/1499-selector-point-transform-direct-restoration-and-match-20261017.md).
func_150F22D0 emits all43 words, frame0x18, with its preserved retail jump
table and no new word guards. Ten installed tests and six selected historical
checks pass. The entire first normal image matches:125 code/one extent/78
exactly checked metadata bytes; all6,057 bodies and189,088 Game-data bytes
audited. Fresh Game **61.29%**, total **66.02%**, zero drift. Tools86254e6
first; preserve1,101 unrelated mirror hashes /1,108 paths. Its next target is finished in Note1500.
Both fade lifetime gaps and wider Game remain open.

Fixed-state sine update **restored and byte-exact directly from C**:
[Note1498](WORKING_NOTES/1498-fixed-state-sine-update-direct-restoration-and-match-20261017.md).
func_150F23E0 emits all40 retail words, frame0x20, real actor home and delayed
S0 lifetime, with no new guards. Ten installed tests and three selected
checkpoint checks pass. The entire first normal image matches:128 code/one
extent/zero metadata bytes; all6,057 bodies and189,088 Game-data bytes audited.
Fresh Game **61.27%**, total **66.01%**, zero drift. Toolsd698926 first; preserve
1,098 unrelated mirror hashes /1,104 dirty paths. Its next target is finished in Note1499.
Both fade lifetime gaps and wider Game remain open.

Sine/phase update **restored and byte-exact with one commutative ADDU guard**:
[Note1497](WORKING_NOTES/1497-sine-phase-update-restoration-and-match-20261017.md).
func_150F2480 has38 words/frame0x20, the captured state pointer and four float
calls. Ten final installed tests and seven selected compatibility checks pass.
The entire first normal image matches:119 code/one extent/zero metadata bytes;
all6,057 bodies and189,088 Game-data bytes audited. Fresh Game **61.25%**,
total **65.99%**, zero drift. Tools931d6c2 first; preserve1,093 unrelated mirror
hashes /1,100 dirty paths. Its next target is finished in Note1498.
Both fade lifetime gaps stay open.

Actor counter motion **restored and byte-exact directly from C**:
[Note1496](WORKING_NOTES/1496-actor-counter-motion-direct-restoration-and-match-20261017.md).
func_150B9560 emits all39 retail words, frame0, with no new guards. Ten
installed tests and21 affected checks pass. The entire normal ELF equals
its first prediction:120 code/one extent/51 checked metadata bytes; all6,057
bodies and189,088 Game-data bytes audited. Fresh Game **61.23%**, total
**65.97%**, zero drift. Tools39c4f4e first; preserve1,088 unrelated mirror
hashes /1,096 paths. Its next target is finished in Note1497.
Both fade lifetime issues stay open.

White text fade **public candidate qualified, private gap rejects installation**:
[Note1495](WORKING_NOTES/1495-white-text-fade-candidate-and-private-lifetime-gap-20261017.md).
func_150D0534 has69 candidate/70 body/71 slot words, frame0x30 and the real
P0 home, but62 full-slot differences and wrong S0/RA/state lifetimes. Eight
tests pass (39.443s), including28 actual-wrapper private counterexamples.
No production/guard/ELF/README change or matching credit. Fresh Game61.21%,
total65.95%, zero drift. Tools017c9c4 first; preserve all1,090 mirror hashes /
1,092 paths. The next actor target is subsequently finished in Note1496.
Both fade lifetime issues remain open; handwritten func_150A76F0 stays in
the assembly workstream.

Text reveal renderer **restored and byte-exact directly from C**:
[Note1494](WORKING_NOTES/1494-text-reveal-renderer-direct-restoration-and-match-20261017.md).
func_150D032C now emits all102 retail words, frame0x80 and actual message/
header/payload homes, with no new guards. Ten installed tests and eleven
constructor checks pass. The entire normal ELF matches its first prediction:
296 code/two extent/20 checked metadata bytes; all6,057 function bodies and
189,088 Game-data bytes audited. Fresh Game **61.21%**, total **65.95%**, zero
drift. Tools b3020e9 first; preserve1,084 unrelated mirror hashes /1,090 paths.
The white fade is subsequently investigated in Note1495; both fade S0/private
gates and wider Game remain open.

Text buffer constructor **restored and byte-exact with twelve scratch guards**:
[Note1493](WORKING_NOTES/1493-text-buffer-constructor-restoration-and-match-20261017.md).
func_150CFF10 replaces its zero-return placeholder with complete73-word C,
the40-byte descriptor, original0x68 frame and dual-buffer allocation path.
The normal ELF equals its first prediction:220 code bytes plus two extent
bytes, zero other metadata changes. Eleven installed tests and21 affected
checks pass; all189,088 Game-data bytes remain exact. Tools f5cd863 first;
preserve1,078 unrelated mirror hashes /1,086 paths. Fresh Game **61.18%**,
total **65.93%**, zero drift. Root README changes only two aggregate rows.
The reveal renderer is subsequently finished in Note1494; the earlier fade
S0/private gates and wider Game stay open.

Dual fade **native caller-save decision explained, still uninstalled**:
[Note 1492](WORKING_NOTES/1492-dual-fade-native-caller-save-selection-20261017.md).
Two owned compiler traces measure old-weight caller cost2 versus first-use
S0 cost4 and observe the actual rejecting comparison flags; the normal-record
control positively selects S0. Three tests pass (20.913s), with 162 effective
event controls. No candidate or production change, guards or credit; the
68/69-word, 61-full-slot-difference gap remains. Tools 59d8398 first; preserve
all 1,080 mirror hashes / 1,082 paths. Fresh Game61.16%, total65.92%, zero
drift. Next: recover block/live-unit topology or prove an original profile
difference, then S0/RA/state/private/fault/image gates. Wider Game stays open.

Dual fade **argument home recovered, S0/private gaps still reject installation**:
[Note 1491](WORKING_NOTES/1491-dual-fade-argument-home-and-allocation-trace-20261017.md).
func_150D01A0 now has a qualified 68-word/frame0x30 candidate retaining the
real SP+0x30 record argument home without extra storage. Actual text-wrapper
payload word8 agrees with retail, while other private words remain different.
Five owned compiler captures isolate formal promotion from the still-unresolved
old-weight caller-save decision. Ten tests pass in 66.689s. There are still
61 full-slot word differences, not merely one scheduling word; no installation,
guards or credit. Tools 0a0712a first; preserve all 1,078 mirror hashes /
1,080 paths. Fresh Game **61.16%**, total **65.92%**, zero drift; production
and README unchanged. Next: inspect old-weight live-range/callee-save selection,
then complete private/helper/fault/image gates. Wider Game stays open.

Dual-buffer fade **candidate qualified, still uninstalled**:
[Note 1490](WORKING_NOTES/1490-dual-buffer-fade-candidate-and-private-payload-gap-20261017.md).
func_150D01A0 has a complete one-pointer C candidate, signed byte countdown,
wrapped clock subtraction and live buffer-index behavior. Eight tests pass
in 34.140s, including 9,216 public cases and the full actual caller. It emits
65 of retail's 69 words/frame0x30, with S0=record instead of previousWeight.
The actual 42-word text wrapper positively exposes different sixteen-word
copied payloads. No installation, guards or matching credit. One bounded
advisory suggestion is falsified by IDO; inspect owned CFE/UOPT formal/home
constraints next. Fresh Game **61.16%**, total **65.92%**, zero drift;
production and root README unchanged. Tools 7960b37 first; preserve all
1,076 initial mirror hashes / 1,078 dirty paths. Wider Game stays open.

Link-event callback **installed, all 43 words exact with one commutative guard**:
[Note 1489](WORKING_NOTES/1489-game-link-event-callback-match-20261017.md).
func_150CF484 now has its full void(record, packet, u8 event) interface,
removal/link-swap behavior, original pointer/access lifetimes and frame 0x18.
The normal ELF equals the first complete prediction: 118 code bytes plus one
size byte, zero metadata differences or exclusions. All 24 owner neighbors
and 189,088 Game-data bytes remain unchanged. Nine installed tests pass in
20.308s; four burst/child emission/behavior checks pass in 33.305s. Fresh
Game **2,953/4,828 (61.16%)**, total **3,626/5,501 (65.92%)**, different
**1,875**, zero drift. Tools fed3c57 first; preserve 1,071 unrelated mirror
hashes / 1,076 dirty paths. Root README gets aggregate rows only. Next nearby
placeholder: **func_150D01A0**, the 69-word dual-buffer fade callback;
wider Game matching and real destructor/gameplay acceptance remain open.

Transition completion burst **installed, all 251 words exact with eleven guards**:
[Note 1488](WORKING_NOTES/1488-transition-burst-real-object-layout-and-guarded-match-20261017.md).
func_150CF800 now has its full semantic C, real SP+0xAC/SP+0x9C objects,
frame 0x108, correct pointer/flag lifetimes and existing six-word constant
anchor. A real scalar declaration move closes the stack gap; only scratch
register roles are guarded. The normal ELF equals the first full prediction:
759 code bytes, two size bytes and twelve explicitly accounted metadata bytes,
zero exclusions. All 189,088 Game-data bytes remain exact. Fresh Game
**2,952/4,828 (61.14%)**, total **3,625/5,501 (65.90%)**, different **1,876**,
zero drift. Next nearby placeholder: **func_150CF484**; wider Game stays open.
All twelve installed tests pass in 133.014s; thirteen affected predecessor/
child checks pass in 76.513s. Tools e537123 first; preserve 1,066 unrelated
mirror hashes / 1,072 dirty paths. Main README receives aggregate rows only.

Transition burst **pointer/flag lifetimes recovered, 91 -> 47 word gap**:
[Note 1487](WORKING_NOTES/1487-transition-burst-pointer-and-flag-lifetime-recovery-20261017.md).
func_150CF800 retains 251 words/frame 0x108 and now has the original 47-word
opening, S4/S3 roles, SP+0x84 transition reload, first flag branch and 41-word
tail. Aggregate homes remain four bytes high; remaining scratch choices and
private/rebase/fault/image gates keep it uninstalled, with zero guards/credit.
Eight tests pass in 61.553s, including 2,688 guest cases, native32 O2/O0,
compiler captures, caller checks and 390 protected-input controls. Tools
e12376f first; preserve all 1,065 mirror hashes / 1,067 paths. Fresh Game
61.12%, total 65.88%, zero drift; production and root README stay unchanged.
This uninstalled snapshot is superseded by the installed recovery in Note 1488.

Transition child motion **installed, 48 words exact with ten narrow guards**:
[Note 1486](WORKING_NOTES/1486-transition-child-motion-guarded-match-20261017.md).
func_150CFC60 now has its one-pointer kind-13 interface, live-clock quadratic
motion, strict floor comparison and velocity damping. Ten installed tests
pass in 29.536s; the normal ELF equals the first full prediction, with only
141 code bytes and one size byte changed, no metadata exclusions, all 24
neighbors and 189,088 Game-data bytes unchanged. Fresh Game **2,951/4,828
(61.12%)**, total **3,624/5,501 (65.88%)**, different **1,877**, zero drift.
Native linker aliases pass at O0 only; optimized alias and double-NaN limits
are explicit. The adjacent func_150CF800 is subsequently installed in Note 1488;
the earlier 47-word snapshot remains archived. Wider Game remains open.
Eleven predecessor behavior/compiler checks also pass (80.770s); current-input
corruption checks supersede two historical literal-baseline tests. Tools
36eccea is banked first; preserve 1,058 unrelated mirror hashes / 1,065 paths.

Transition completion burst **retail frame recovered, still uninstalled**:
[Note 1485](WORKING_NOTES/1485-transition-burst-frame-recovery-and-native-qualification-20261017.md).
func_150CF800 now has **251 words / frame 0x108**, with **91 word differences**.
Actual compiler captures show automatic homes reduced from 144 to 128 bytes.
Extended guest and native32 checks include the actual factory/copies and
demonstrate why native-only byte-width checks are insufficient. Descriptor/
payload homes and saved-register ownership still differ; no production,
README or matching credit. Continue those lifetimes and remaining private gates.
Seven tests pass in 53.736s plus six predecessor checks in 24.634s. Native
O2/O0 each cover 1,728 cases; the guest covers 2,688 three-way cases. Tools
5a038ed first; preserve 1,056 mirror hashes / 1,059 paths. Fresh Game 61.10%,
total 65.86%, zero drift. Root README and production source/ELF stay unchanged.

Transition completion burst **recovered as a complete uninstalled candidate**:
[Note 1484](WORKING_NOTES/1484-transition-completion-burst-candidate-and-frame-gap-20261017.md).
func_150CF800 emits 251 words, but 93 differ and frame 0x118 still exceeds
retail's 0x108. Correct byte fields, full 88/16-byte objects, callback/factory
ABI and the six-word literal pool are audited. Public guest/reference and
actual callback-window checks do not certify private/native/installation
state. Production source/ELF and README remain unchanged, with no matching
credit. Six tests pass in 21.605s: 2,304 public cases, 128 original caller
cases and effective source/word/binding/input controls. Tools f36356e first;
preserve all 1,053 initial mirror hashes / 1,056 final paths. Fresh Game
61.10%, total 65.86%, zero drift. Continue this function's real
frame/register/object lifetimes.

Fixed transition constructor **installed, all 96 words directly exact from C**:
[Note 1483](WORKING_NOTES/1483-fixed-transition-constructor-direct-match-20261017.md).
func_150CF680 has its void/signed-ID/byte-slot interface, complete 88-byte
descriptor, 16-byte payload and seven-word factory call. Eight final tests
pass in 70.848s; twelve affected checks in 51.749s. Actual factory/copy words
execute, preserving all nine inherited bytes; native field checks alone do
not certify padding. The normal ELF equals the first complete prediction:
292 code bytes and two size bytes only, no guards/profile/pool/data changes,
all 24 owner neighbors unchanged. Fresh Game **2,950/4,828 (61.10%)**, total
**3,623/5,501 (65.86%)**, different **1,878**, zero drift. Tools **791eb66**
first; preserve 1,045 unrelated mirror hashes / 1,053 paths. README aggregate
rows only. Next **func_150CF800**, 251 words/frame 0x108; wider Game stays open.

Paired scrolling tile windows **installed, all 38 words directly exact from C**:
[Note 1482](WORKING_NOTES/1482-paired-scrolling-tile-windows-direct-match-20261017.md).
func_150CF5E8 now emits its two SDK tile-size commands and returns the advanced
Gfx pointer. Eight installed tests pass in 38.987s; nine affected checks in
54.048s and one downstream context check in 5.319s. The normal ELF equals the
first complete prediction: 127 instruction bytes and one size byte only,
no guards/profile/pool/data changes, all 24 owner neighbors unchanged.
Fresh Game **2,949/4,828 (61.08%)**, total **3,622/5,501 (65.84%)**, different
**1,879**, zero drift. Tools **6737b65** first; preserve 1,037 unrelated mirror
hashes / 1,047 final paths. README aggregate rows only. Fade tracing finds
three CFE/UOPT LODs plus a VREG annotation before one UGEN LH; no fade adoption.
Next **func_150CF680**, 96 words/frame 0x98, constructor plus 16-byte copy.

Overlay fade packet **recovered and audited, not installed or byte-exact**:
[Note 1481](WORKING_NOTES/1481-overlay-fade-packet-recovery-and-reload-gap-20261017.md).
func_15182670's complete typed C emits 53/54 words, frame 0x40, with 45
ordinal differences. Seven final tests pass in 124.087s, including actual
memcpy, inherited padding, all four call sites and independent rebases.
Retail reloads duration three times versus C's one; moving the division late
does not close that gap. Keep the exact original assembly and no new guards
or credit. Fresh Game **61.06%**, total **65.82%**, zero drift; production
and root README unchanged. Tools **72f748d** first; preserve all 1,037 mirror
hashes / 1,041 final paths. Trace the duration home before another source
experiment; the 633-word renderer and wider Game queue remain open.

Overlay mode defaults **installed, all 50 words directly exact from C**:
[Note 1480](WORKING_NOTES/1480-overlay-mode-defaults-direct-match-20261017.md).
func_15181E18 now has its void/channel interface, three byte-sized color clears
and mode-dependent defaults, preserving the late named float read. Nine final
tests pass in 97.507s; seven affected predecessor/compiler checks in 109.690s.
The entire normal image equals the first complete prediction: 170 code bytes,
one size byte, 30 exactly certified symbol/string bytes, no exclusions/guards.
Fresh Game **2,948/4,828 (61.06%)**, total **3,621/5,501 (65.82%)**, different
**1,880**, zero drift. Tools **e3da0c4** first; preserve 1,028 unrelated mirror
hashes / 1,037 paths. Root README aggregate rows only. Resume the still-open
633-word renderer; [Note 1479](WORKING_NOTES/1479-mirrored-texture-float-color-saturation-20261017.md)
locates its six-color saturation and partial positiveX residency recovery.

Mirrored texture **upstream homes traced; no installation or C credit**:
[Note 1478](WORKING_NOTES/1478-mirrored-texture-upstream-home-provenance-20261017.md).
Four owned compiler traces preserve normal words/bindings/pools. Five tests
pass in 28.916s. UOPT already supplies positiveY's M-120 / SP+0x60 home and
three rate homes; promoting the rate removes one copy but still fails retail.
Game remains **61.04%**, total **65.81%**, zero drift; production/README
untouched. Tools **b44bad7** first; preserve 1,029 mirror hashes / 1,031 paths.
Continue the same routine's coordinate lifetimes and shared rate residency.

Mirrored texture **complete SDK candidate audited; not installed or byte-exact**:
[Note 1477](WORKING_NOTES/1477-mirrored-texture-candidate-and-private-gap-20261017.md).
func_1517FB9C's four rectangles / 24 words / 96-byte advance agree with an
independent reference in 15,576 guest pairs and 948 native cases/profile.
All seven final tests pass in 150.349s, including four original caller
windows, rebases and fail-closed input gates. The C candidate has 626 words,
frame 0xD8, 604 ordinal differences including its seven-word length deficit.
Retail's first private FP spill is +0x54; C's is +0x60. Do not install or add
guards on public equivalence alone. All production bytes/totals stay unchanged:
Game **61.04%**, total **65.81%**, zero drift. Tools **5deb8e2** banks first;
preserve all 1,025 initial mirror hashes / 1,029 paths. Continue this same
routine's float spill / step-home code-generation investigation next.

Clipped rectangle **installed, all 106 words directly exact from C**:
[Note 1476](WORKING_NOTES/1476-clipped-rectangle-direct-match-20261017.md).
func_1517F9F4 has the recovered Gfx pointer/six-word interface, signed sort,
four signed viewport conversions, strict edge gates and SDK fill command.
No new guards/profile/pool/build changes; all 27 owner neighbors are unchanged.
All 13 final tests pass in 199.893s. The entire normal ELF equals the
first prediction: 329 target code bytes and two size bytes only, with exact data.
Fresh Game **2,947/4,828 (61.04%)**, total **3,620/5,501 (65.81%)**, different
**1,881**, zero drift. Tools **d52744e** banks first; preserve 1,015 unrelated
mirror hashes / 1,025 paths. Next **func_1517FB9C**, the 633-word textured
rectangle routine, frame 0xD8. The pulse wrapper remains deferred without C credit.

Overlay projection **installed, all 120 words directly exact from C**:
[Note 1475](WORKING_NOTES/1475-overlay-projection-direct-match-20261017.md).
func_1517F814 preserves its 0x40 frame, actual matrix tail/private output
homes, ordered clamps and live relative-coordinate stores. The existing
literal-pool binding reuses the original three constants; no new instruction
guards, compiler profile or runtime data. All 27 owner neighbors are unchanged.
All 36 final tests pass in 482.491s. The entire normal ELF equals the
first prediction: 369 target code bytes and two size bytes only, with exact data.
Fresh Game **2,946/4,828 (61.02%)**, total **3,619/5,501 (65.79%)**, different
**1,882**, zero drift. Tools **9d0f799** banks first; preserve 1,008 unrelated
mirror hashes / 1,018 final paths. Next **func_1517F9F4**, the 106-word clipped
rectangle leaf. func_1517F564 remains deferred: reset/indexed-writer evidence
does not establish a defined inherited-blend lifetime or all-program invariant.

Pulsed-overlay **private-lifetime audit banked; no C adoption or new credit**:
[Note 1474](WORKING_NOTES/1474-pulsed-overlay-private-lifetime-audit-20261017.md).
func_1517F564's pulse-off blend is inherited stack data, read at SP+0x20
without a preceding local write. Actual setter/updater/lookup/draw and the
175-word caller reproduce the dependence. A compiled zero-blend candidate
changes output; the archive also reads an uninitialized local.
All 10 final checks pass in 134.517s, protecting 154 input entries / 145 paths.
Source, ELF, CSV, guards and archive are unchanged; fresh Game remains 61.00%,
total 65.77%, zero drift. Tools **381d541** banks first; preserve all 1,008
initial mirror hashes / 1,011 final paths. Keep this same routine open:
resolve a supported lifetime or all-writer precondition before accepting C.

Color-overlay renderer **installed, all 197 words directly exact from C**:
[Note 1473](WORKING_NOTES/1473-color-overlay-draw-direct-match-20261017.md).
func_1517F08C uses typed SDK display-list commands, coverage-save blending,
live viewport bounds and four unsigned FP conversions. No guards/profile
change; all 38 surrounding owner/caller routines remain unchanged.
All 26 installed tests pass in 321.565s. The entire normal ELF equals its
first prediction: only 537 code bytes and two size bytes change, with exact data.
Fresh Game 2,945/4,828 (61.00%), total 3,618/5,501 (65.77%), zero drift.
Tools **33dda28** banks first; preserve 999 unrelated mirror hashes / 1,008 paths.
Next func_1517F564's 111-word pulse/palette wrapper; resolve its pulse-off
SP+0x20 blend lifetime before accepting C. Full gameplay stays open.

Color-channel aggregate **installed, all 44 words directly exact from C**:
[Note 1472](WORKING_NOTES/1472-color-channel-aggregate-direct-match-20261017.md).
func_1517EFDC preserves its live signed limit, progress/float gate, tally,
frame 0x30 and saved F20 pair. No new guards/profile; 27 neighbors unchanged.
All 22 installed tests pass in 361.799s, including real progress/sequence
chains and native32 O2/O0/UBSan. The entire normal ELF equals its first
prediction: only 129 code bytes and one size byte change, with exact data.
Fresh Game 2,944/4,828 (60.98%), total 3,617/5,501 (65.75%), zero drift.
Tools **83a87d2** banks first; preserve 992 unrelated mirror hashes / 1,001 paths.
Next func_1517F08C, the 197-word overlay display-list leaf. Full gameplay stays open.

Signed color-progress accessor **installed, all 43 words directly exact from C**:
[Note 1471](WORKING_NOTES/1471-color-progress-accessor-direct-match-20261017.md).
func_1517EF00 now preserves busy, signed division, upper clamp and wrapped
mode inversion; no new guards/profile, 27 raw/padded neighbors unchanged.
All 20 installed tests pass in 262.871s; two strengthened caller tests pass
again in 3.385s. The entire normal ELF equals its first prediction: only 124
code bytes and one size byte change, with 146 protected inputs and exact data.
Fresh Game 2,943/4,828 (60.96%), total 3,616/5,501 (65.73%), zero drift.
Tools **5298c5e** banks first; preserve 985 unrelated mirror hashes / 994 paths.
Next func_1517EFDC, the 44-word channel aggregate. Full gameplay stays open.

Color-state submitter **installed, all 48 words directly exact from C**:
[Note 1470](WORKING_NOTES/1470-color-state-submit-direct-match-20261017.md).
func_1517EE40 now has its complete six-argument leaf and signed-byte mode
interface. No new guards/profile; 89 owner/caller routines and all guard bytes
remain unchanged. All 17 final tests pass in 216.960s; normal ELF equals the
first full prediction, protecting 144 inputs and 189,088 data bytes. Fresh Game
2,942/4,828 (60.94%), total 3,615/5,501 (65.72%), different 1,886, zero drift.
Tools **aecf777** banks first; preserve 978 unrelated mirror hashes / 987 paths.
Next func_1517EF00, the 43-word progress/division accessor. Full gameplay stays open.

Sequence event scan **installed, all 219 words guarded-exact**:
[Note 1469](WORKING_NOTES/1469-sequence-event-scan-installed-guarded-match-20261017.md).
func_1501DAAC now has complete typed C, frame 0x80 and original homes/roles;
77 certified guards normalize opening scheduling and scratch/LO roles.
All 29 tests pass in 327.067s, including actual color and setup/helper chains.
Normal ELF equals the first whole-image prediction; protect 141 inputs and
189,088 data bytes. Fresh Game 2,941/4,828 (60.92%), total 3,614/5,501 (65.70%),
different 1,887, zero drift. Tools **abf9d17** banks first; preserve 969 unrelated
mirror hashes / 980 paths. Next func_1517EE40, the still-stubbed 48-word color
helper; its assembly oracle is not a C recovery. Query engine/gameplay stay open.

Sequence record setup **installed, all 473 words guarded-exact**:
[Note 1468](WORKING_NOTES/1468-sequence-record-setup-installed-guarded-match-20261017.md).
func_1501D348 replaces its stub with complete C under the existing profile;
165 certified guards preserve the frame/homes and omit one dead scale word.
Both typed C callers and all 56/6/60 owner neighbors remain unchanged.
Actual six-helper chains, both full C callers and nine original assembly
call packets pass. All 25 final tests pass in 325.866s. The normally rebuilt
ELF equals the first complete prediction with no metadata exclusions;
140 inputs and 189,088 data bytes / 720 owners are protected. Fresh Game
2,940/4,828 (60.89%), total 3,613/5,501 (65.68%), different 1,888, drift zero.
Tools **987e90b** banks first; preserve 964 unrelated mirror hashes / 971
paths. Root README changes only date and aggregate rows. Next func_1501DAAC,
219 words/frame 0x80, not full gameplay acceptance. Whole-project retail
checksum remains non-matching; explicit development build passes.

Sequence record setup **all 473 words guarded-exact, qualified but not installed**:
[Note 1467](WORKING_NOTES/1467-sequence-record-setup-certified-guarded-match-qualification-20261016.md).
func_1501D348's complete 474-word C retains frame 0x78 and all homes/saves.
Certify cursor-one induction and closed scratch roles across all loops/32
calls, then emit 473 retail words with 165 guards and one omission. All eight
tests pass in 122.782s: 484 three-way cases, native32 O2/O0/UBSan, effective
controls, 417 fault prefixes and independent rebases. Preserve 56 raw/padded
neighbors and all 136 inputs. Tools **c7c0d87** banks first, preserving 964
mirror hashes / 967 paths. Production, root README and installed counts remain
unchanged. Next actual caller/helper gates and first whole-image prediction,
then installation/build/audit and fresh progress. Wider Game stays open.

Sequence record setup **frame and private homes recovered, not installed**:
[Note 1466](WORKING_NOTES/1466-sequence-record-setup-frame-and-private-home-recovery-20261016.md).
func_1501D348 now has two complete frame-0x78 fits: **473 words / 273
differences** and **474 words / 275 differences**. Both preserve saves and
all eight homes, literal memory/events and saved roles at every provider
in 484 three-way cases. All five tests pass in 207.068s, including both
native32 O2/O0/UBSan bodies, sixteen effective controls and 58 bounded
screens. Preserve 56 neighbors and all 136 inputs. Tools **b9e0781** banks
first, preserving 962 mirror hashes / 964 paths. No production/root README change
or matching credit; Note 1464's installed counts remain current. Next is
the 474-word fit's second descriptor preheader, then remaining register/
instruction qualification and installation. Wider Game/gameplay stays open.

Sequence record setup **recovered and publicly qualified, not installed**:
[Note 1465](WORKING_NOTES/1465-sequence-record-setup-recovery-and-frame-boundary-20261016.md).
func_1501D348 has a complete typed five-word C candidate and five tests
passing in 100.001s: 484 two-way guest cases, 60 native32 O2/O0/UBSan cases
each and eight effective controls. It remains **471 words / frame 0xA8 / 405 differences**
versus retail 473 / 0x78. S0-S5/RA saves already match; private homes do not.
Preserve 56 raw neighbors and all 136 production inputs. Tools **332b6ba**
banks research only, preserving all 957 initial mirror hashes / 962 paths.
No source/guard/image/CSV/README change or matching credit; the last installed
counts remain Note 1464 below. Next: fit this same function's frame/homes,
then qualify the eventual match and installation. Gameplay remains open.

Sequence state reset **installed, all 100 words byte-exact with 13 guards**:
[Note 1464](WORKING_NOTES/1464-sequence-state-reset-installed-guarded-match-20261016.md).
func_1501D044 replaces its zero-return stub with void(s32 slot) C, correctly
scaled stores, captured float limit, actor-table clear and two post-call flag
clears. Retain frame 0x18 / RA+0x14, call-delay SH, existing no-unroll profile,
56 raw neighbors and all six caller-owner functions. All 24 final tests pass
in 170.864s; the normal 695-compile rebuild equals the entire first 651-byte
ELF prediction, zero exclusions. Protect 136 inputs and 189,088 data bytes /
720 owners. Fresh Game **2,939/4,828 (60.87%)**, total **3,612/5,501 (65.66%)**,
different **1,889**, zero drift; conversion unchanged. Tools **b7775f4** banks
first, preserving 946 other mirror hashes / 957 paths. Next **473-word
func_1501D348**, frame 0x78, still stubbed in this owner. This is a guarded,
not direct, match; wider Game, timing's 141 differences and gameplay remain open.

Priority record maximum **installed, all 105 words byte-exact with 48 guards**:
[Note 1463](WORKING_NOTES/1463-priority-record-maximum-installed-guarded-match-20261016.md).
func_1501CE54 replaces its zero-return stub with void(s32 slot) semantic C,
signed overrides/maxima and preferred-before-fallback priority. Retain the
frame-free 105-word body, existing no-unroll profile and 56 raw neighbors.
All 28 final tests pass in 158.460s, including the previous loader suites;
normal rebuild equals the entire first 371-byte ELF prediction, zero
exclusions. Protect 136 inputs and 189,088 data bytes / 720 owners. Fresh
Game **2,938/4,828 (60.85%)**, total **3,611/5,501 (65.64%)**, different
**1,890**, zero drift; conversion unchanged. Tools **199b23f** banks first,
preserving 937 other mirror hashes / 948 paths. Next **100-word
func_1501D044**, the adjacent state-reset stub. This is a guarded, not direct,
match; wider Game, timing's 141 differences and full gameplay remain open.

Microcode loader **installed, all 97 words byte-exact with 23 guards**:
[Note 1462](WORKING_NOTES/1462-microcode-loader-installed-guarded-match-20261016.md).
func_1501CC3C replaces its false zero-return stub with complete semantic C;
retain 96 raw words, frame 0x30, original homes/saves and no-unroll profile.
The normal 695-compile rebuild equals the entire first 361-byte ELF prediction,
zero exclusions. All 18 final tests pass in 101.175s, including 192 actual
startup caller cuts and the real task/setup/loader chain. Protect 136 inputs,
56 raw neighbors and 189,088 data bytes / 720 owners. Fresh Game **2,937/4,828
(60.83%)**, total **3,610/5,501 (65.62%)**, different **1,891**, zero drift;
conversion unchanged. Tools **fb26ff8** banks first, preserving 932 other
mirror hashes / 939 paths. Next **105-word func_1501CE54**, a frame-free
record scan still stubbed in the same owner. Keep hardware/startup/gameplay
boundaries and timing's 141 differences separate; this is not a direct C match.

Microcode-loader **guarded match qualified, not installed**:
[Note 1461](WORKING_NOTES/1461-microcode-loader-guarded-match-qualification-20261016.md).
func_1501CC3C's complete C emits 96 words / frame 0x30; 23 closed relocation-
aware guards produce all 97 retail words, preserving homes/saved lifetimes
and 56 raw neighbors. Seven tests pass in 42.751s: 770 guest cases, 80
callbacks, 449 native32 cases each at O2/O0/UBSan, 192 real parent/setup/loader
cases, independent rebases and 346 fault prefixes. All 135 production inputs
remain unchanged. Tools **27dc235** banks first, preserving 931 mirror hashes
/ 935 paths. This pre-install checkpoint is completed by Note 1462's caller,
whole-image, build, audit and progress gates. Its no-credit boundary is
historical; Note 1462 owns the installed measurements.

Microcode-loader recovery checkpoint, **not installed**:
[Note 1460](WORKING_NOTES/1460-microcode-loader-recovery-and-matching-boundary-20261016.md).
func_1501CC3C's complete C candidate has 97 words / frame 0x30, still **44
retail word differences**. Seven research tests pass in 15.679s: 770 selector/
cache cases, 80 fired callback cases, 24 real-table cases and two functional
controls. Preserve all 56 raw neighbors, including the 239-word matched
caller, and all 135 production input hashes. Tools **932b4de** banks first,
preserving 928 mirror hashes / 931 paths. No guards, installation, matching
credit or root README change. This historical 44-word boundary is superseded
by Note 1461's guarded qualification; installation remains open.

Graphics-task submission restored, **239 words directly byte-exact from C**:
[Note 1459](WORKING_NOTES/1459-graphics-task-submission-direct-match-20261016.md).
func_1501C880 now uses SDK OSScTask/Gfx records, cached signed row capacity,
ordered cursor repair, live task/page reloads, blocking submission and page/
counter publication. Retain frame 0x28 and the existing no-unroll profile;
add no guards and retire **nine obsolete caller guards** after correcting its
void prototype and equivalent comparison order. Preserve 56 raw neighbors
and all sixteen padded caller functions. All **12 final tests pass in
92.616s**: 1,656 guest cases, 72 callbacks, 864 native32 O2/O0 cases each,
16 real caller cuts, 61 real setup words and 1,136 fault prefixes. The normal
695-compile rebuild equals the entire first **800-byte** ELF prediction,
zero exclusions; 134 inputs/protected data pass. Fresh Game **2,936/4,828
(60.81%)**, total **3,609/5,501 (65.61%)**, different **1,892**, zero drift;
conversion unchanged. Tools **44ac318** banks first, preserving 921 mirror
hashes / 928 paths. Next **97-word func_1501CC3C**, still a microcode-loader
stub. Timing's 141 differences, wider Game and gameplay remain open; cache,
queue and microcode providers are bounded, not hardware/host acceptance.

Viewport initializer restored, **373 words directly byte-exact from C**:
[Note 1458](WORKING_NOTES/1458-viewport-initializer-direct-match-20261016.md).
func_1501A8C0 now preserves frame 0x48, sine SP+0x34, live base/page reads,
signed origin/flag and full-word depth semantics. Three named ratio values
and explicitly sequenced cosine calls resolve the prior 49-word boundary;
no new guards/profile. All **12 final tests pass in 159.799s**: 1,144 guest,
216 callback, 475 native32 O2/O0 cases each, 108 real-helper-chain cases,
12 original caller cuts and 1,962 fault prefixes. The entire normal ELF
equals the first **1,181-byte** prediction, including two exact metadata
swaps, zero exclusions. All 130 inputs/protected data pass; all eleven owner
functions now match. Fresh Game **2,935/4,828 (60.79%)**, total **3,608/5,501
(65.59%)**, different **1,893**, zero drift; conversion unchanged. Tools
**34c77ae** banks first, preserving all 914 mirror hashes / 921 paths.
The **239-word func_1501C880** recovery is completed in
[Note 1459](WORKING_NOTES/1459-graphics-task-submission-direct-match-20261016.md).
Timing's 141 differences, wider Game and gameplay remain
open; angle/SDK leaves are bounded, not full hardware or host acceptance.

View point projection restored, **87 words directly byte-exact from C**:
[Note 1456](WORKING_NOTES/1456-view-point-projection-direct-match-20261016.md).
func_1501A764 now preserves its signed seven-word interface, real eight-word
transform tail, ordered reciprocal/projection and live base/page reloads.
All **11 final tests pass in 66.018s**: 1,488 guest cases, 348 native32 cases
at each optimization level, 72 actual caller cuts and 672 connected fault
prefixes. Every root/helper word executes. The normal ELF equals the entire
first **276-byte** prediction, no new guards/profile or metadata exclusions;
128 inputs and protected data pass. Fresh Game **2,934/4,828 (60.77%)**, total
**3,607/5,501 (65.57%)**, different **1,894**, zero drift; conversion unchanged.
Tools **fed3fa9** banks first, preserving 905 mirror hashes / 911 paths.
The **373-word func_1501A8C0** recovery is completed in
[Note 1458](WORKING_NOTES/1458-viewport-initializer-direct-match-20261016.md).
Timing's 141 differences and wider Game remain open; no full gameplay claim.

View scissor setup restored, **124 words directly byte-exact from C**:
[Note 1455](WORKING_NOTES/1455-view-scissor-setup-direct-match-20261016.md).
func_1501A490 now emits pipe sync/scissor commands, handles the signed view
and full-surface path, calls the real clamp and returns its advanced cursor.
Branch-local float values and inline typed record accesses recover the original
0x48 frame/homes/schedule: **no new guards or compiler profile**. All **10 final
tests pass in 45.415s**, including 2,996 completed guest cases, 928 invalid-cast
prefixes, 1,252 native32 O2/O0/UBSan cases each, 48 original caller cuts and
402 connected fault prefixes. All 124 root / 83 reachable clamp words execute;
four dead helper words have explicit static checks and literal byte coverage.
The normal ELF equals the entire first **376-byte** slot/extent prediction,
zero metadata exclusions; preserve ten neighbors, all guards, 117 other inputs
and protected data. Fresh Game **2,933/4,828 (60.75%)**, total **3,606/5,501
(65.55%)**, different **1,895**, zero drift; conversion unchanged. Tools
**e72f87b** banks first; both copies' checks pass, preserving 899 mirror hashes /
905 paths. The new owner recipe warning is fixed. The adjacent **87-word
func_1501A764** recovery is completed in
[Note 1456](WORKING_NOTES/1456-view-point-projection-direct-match-20261016.md).
Timing's 141 differences and wider Game remain open; no full gameplay claim.

Two-row display-list setup restored, **61 words guarded byte-exact**:
[Note 1454](WORKING_NOTES/1454-two-row-display-list-setup-guarded-match-20261016.md).
func_1501A39C emits five real SDK commands for each of two input rows and
publishes both cursors with live table/depth/view alias semantics. Select only
this function's no-unroll object; 38 closed scratch-role/schedule guards recover
retail while all ten normal-profile neighbors stay unchanged. All **11 final
tests pass in 51.237s**, including 688 guest cases, 344 native32 O2/O0/UBSan
cases each, seven effective controls, 48 original caller cuts and 456 fault
prefixes. The entire normal ELF equals the first **193-byte** slot/extent
prediction, zero metadata exclusions; protect 113 other inputs and data layout.
Fresh Game **2,932/4,828 (60.73%)**, total **3,605/5,501 (65.53%)**, different
**1,896**, zero drift; conversion unchanged. Tools **a83f3a4** banks first,
both copies' checks pass, preserving 893 initial mirror hashes / 899 paths.
The adjacent **124-word func_1501A490** direct recovery and owner recipe-warning
cleanup are completed in [Note 1455](WORKING_NOTES/1455-view-scissor-setup-direct-match-20261016.md).
Timing's 141 differences and wider Game remain open. The original
func_1501C880 caller remains stubbed; no full startup/frame/gameplay claim.

View initialization restored, **95 words guarded byte-exact**:
[Note 1453](WORKING_NOTES/1453-view-initialization-guarded-match-20261016.md).
func_1501A220 now implements wrapping allocation sizes, signed height rounding,
live-count callbacks and final flag publication. Eight closed prologue guards
normalize save/copy scheduling and equivalent argument aliases; no profile
change or padding. All **11 final tests pass in 41.745s**, including 1,704
three-way guest cases, 852 native32 O2/O0/UBSan cases each, 420 prologue joins,
128 fault prefixes and original-caller cuts. The entire normal ELF equals the
first **300-byte** slot/extent prediction, with zero metadata exclusions.
Preserve ten neighbors, 111 other inputs and protected 189,088 bytes / 720
owners. Fresh Game **2,931/4,828 (60.71%)**, total **3,604/5,501 (65.52%)**,
different **1,897**, zero drift; conversion unchanged. Tools **51ebd75** banks
first; both copies' checks pass, preserving 887 original mirror hashes / 893
paths. The adjacent **61-word func_1501A39C** display-list setup recovery is
now completed in [Note 1454](WORKING_NOTES/1454-two-row-display-list-setup-guarded-match-20261016.md).
Timing's 141 differences and wider Game stay open. Original startup caller
remains stubbed; no full startup/gameplay, push or host/Release claim.

Timing frontend allocation boundary now captured:
[Note 1452](WORKING_NOTES/1452-frame-timing-frontend-allocation-provenance-20261016.md).
Two completed CFE/UOPT/UGEN owner compiles prove the retained residual address
is assigned before UGEN. Unsigned zero comparisons add a conversion; eight
declaration-order controls are word-identical. All five final tests pass in
**72.853s**, with 19 complete-owner controls and corruption gates. No source
fit is adopted: production stays **191 words / frame 0x18 / 141 differences**,
and all 109 live inputs/aggregates stay fixed. Tools **dbca3c5** banks first;
both copies' checks pass, preserving 885 original mirror hashes / 887 paths.
Keep this timing match open. The queued 95-word **func_1501A220** recovery is
now completed in [Note 1453](WORKING_NOTES/1453-view-initialization-guarded-match-20261016.md).

Latest timing fitting pass rejects source-only false improvements:
[Note 1451](WORKING_NOTES/1451-frame-timing-allocation-and-signed-zero-fit-boundary-20261016.md).
Production func_15019F20 stays **191 words / frame 0x18 / 141 differences**.
Four owned UOPT traces identify the retained T1 residual address and explain
why a 139-difference candidate still has the wrong accumulator role. A peeled
history loop changes retail's positive-zero mean to negative zero and is
rejected by actual guest execution. All seven final tests pass in **53.158s**,
including 6,908 three-way guest cases and 24 opening fault cuts. All 109 live
inputs, matching/conversion totals and README aggregates stay unchanged.
Tools **061bde1** banks first; both copies' checks pass, preserving all 883
original mirror hashes / 885 paths. Next recover the byte-gate promotion and
branch-local residual addressing; no new guards or installed code change.

Frame timing/state updater restored as **semantic C, not byte-exact**:
[Note 1450](WORKING_NOTES/1450-frame-timing-state-semantic-restoration-20261016.md).
func_15019F20 now preserves the unusual quotient arithmetic, phase/counter
wrapping, byte-index aliases and ordered ten-sample float mean. Recover its
void interface; the actual direct caller func_1501905C remains all 53 words
byte-exact. The 191-word body / frame 0x18 and one padding word still have
**141** slot differences; no new guards or profile changes.
All **ten final tests pass in 48.712s**, including 6,860 guest cases, 3,430
native32 cases each at O2/O0 with UBSan, ten controls, all byte encodings,
source rebases and 180 real caller cuts with the prior-result delay store.
The entire normal ELF equals the first **755-byte** prediction, including
173 explicitly accounted metadata bytes and no exclusions. Preserve all
107 other inputs, guard bytes and protected 189,088 bytes / 720 owners.
Fresh totals stay Game **2,930/4,828 (60.69%)**, total **3,603/5,501
(65.50%)**, different **1,898**, zero drift; conversion and README aggregates
unchanged. Tools **511d98a** banks first; both copies' checks pass, preserving
all 877 original mirror hashes / 883 paths. Next finish this instruction match,
especially address lifetimes and zero-reciprocal access order. The previous
func_15019CC8 match remains 102 words guarded-exact in [Note 1449](WORKING_NOTES/1449-view-overlay-matrices-guarded-match-20261016.md).
No full-frame/gameplay, push or host/frozen Release claim.

View render provider installed, **215 words guarded byte-exact**:
[Note 1446](WORKING_NOTES/1446-view-render-provider-guarded-match-20261016.md).
Restore func_150195A0's gated, ordered scene/overlay passes, original frame
0x30 and saved state-pointer lifetime. Five viewport temporary guards close
the raw C's five differences; the caller and corrected 18E88 return interface
remain binary unchanged. All ten final tests pass in **66.748s**. The normal
build equals the entire **680-byte** slot/extent prediction, with no metadata
adjustment or exclusion; preserve 15 neighbors, 102 other inputs and protected
189,088 bytes / 720 owners. Fresh Game **2,928/4,828 (60.65%)**, total
**3,601/5,501 (65.46%)**, different **1,900**, zero drift; conversion unchanged.
Tools **dc4765f** banks first; both copies' syntax/padder checks and tools-check
pass, preserving all 853 original mirror hashes. README aggregate rows only.
Next **func_150198FC**, 175 words / frame 0x28, still a 12-byte stub.
Remaining providers, full gameplay and the wider Game queue remain open.
No push or host/frozen Release action.

Scheduler frame driver installed, **412 words guarded byte-exact**:
[Note 1445](WORKING_NOTES/1445-frame-scheduler-driver-guarded-match-20261016.md).
Restore func_1501878C's message dispatch, ordered display-list passes,
buffer rollback, audio transition and shutdown drain. The semantic C emits
411 words / frame 0x68; 55 derived guards recover temporary roles, crossing
branches and one store/call delay-slot schedule with its original NOP.
All ten final tests pass in 217.608s. The normal rebuild equals the
complete first 1,301-byte ELF prediction, including 111 explicitly accounted
metadata bytes and zero exclusions. Both recovered return interfaces and
all 15 neighboring bodies/bindings stay binary unchanged; preserve 101
other inputs, guard history and protected 189,088 bytes / 720 owners.
Fresh Game **2,927/4,828 (60.63%)**, total **3,600/5,501 (65.44%)**,
different **1,901**, zero drift. Tools 5f98c97 banks first; both copies'
syntax/padder checks pass, preserving all 847 initial mirror hashes.
README aggregate rows only. Next **func_150195A0**, still a 12-byte stub
versus 215 original words; other render providers remain unfinished.
No full gameplay/hardware claim, push or host/frozen Release action.

Frame coordinator installed, **185 words directly byte-exact; no new guards**:
[Note 1444](WORKING_NOTES/1444-frame-coordinator-direct-match-20261016.md).
Restore func_15019130's ordered callbacks, live signed/u8 view loops,
success return and wrapping ages for 508 software-page records. All ten
final tests pass in 179.908s, including real 40/46/78-word matrix
helpers, native32 O2/O0/UBSan, fault/wrap cuts and complete image/input
controls. The normal guest build equals the complete first 516-byte ELF
prediction, including 16 explicitly modeled metadata-serialization bytes
and no exclusions. All 15 neighbors, 101 other inputs, guards and protected
189,088 bytes / 720 owners remain fixed. Fresh Game **2,926/4,828 (60.60%)**,
total **3,599/5,501 (65.42%)**, different **1,902**, zero drift. Tools
c820bde banks first; both tools copies' syntax/padder checks pass,
with all 841 initial mirror hashes preserved. README aggregate rows only.
The upstream **func_1501878C remains a 12-byte stub** versus 412 retail
words; original eight-word caller-cut tests do not restore the full caller
or establish gameplay. Continue that independent recovery next. No host
or frozen Release action, push or Claude/auth retry.

View matrix preparation installed, **40 words directly byte-exact; no new guards**:
[Note 1443](WORKING_NOTES/1443-view-matrix-preparation-direct-match-20261016.md).
Restore func_15094EA0's two fixed-matrix conversions and ordered product,
using the existing 0x180-byte view record, original frame 0x98 and live
frame/base rereads. All ten final tests pass in 148.649s: real freshly built
SDK/product helpers, 2,432 complete-state guest cases, 1,800 fault prefixes,
480 retail caller-loop cases / 744 invocations and native32 O2/O0/UBSan with
128 cases each, plus effective controls and independent relocation carries.
The normal guest build equals the entire first 138-byte code/extent prediction;
all 18 neighbors, 100 other inputs, guard CSV and protected 189,088 bytes /
720 owners remain fixed. Fresh Game **2,925/4,828 (60.58%)**, total
**3,598/5,501 (65.41%)**, different **1,903**, zero drift; conversion unchanged.
README aggregate rows only. Tools d7a8bb1 banks first; both copies' syntax/
eleven shared padder tests and tools-check pass, all 837 initial mirror hashes
/ 841 paths preserved at HEAD ddbdd16. **func_15019130 is still a 12-byte C
stub**, versus 185 retail words: caller-loop tests use the original ROM block,
not a restored installed caller. Recover that caller next. The adjacent
250-word func_15094AB8 and rectangle's 18-word fit remain open, with no full
gameplay/hardware claim, push, Claude/auth retry or host/frozen Release action.

Packed point slot provider installed, **71 words byte-exact with 33 scratch-role guards**:
[Note 1442](WORKING_NOTES/1442-packed-point-slot-provider-byte-match-20261016.md).
Replace func_1509499C's zero stub with its signed-bound sixteen-slot builder
and correct void prototype. The caller/provider pair is now recovered C;
raw C still differs in 33 compiler scratch-register fields, explicitly guarded.
Ten final tests pass in 112.747s: 6,144 provider cases, 4,608 access-prefix
cases, 2,048 real caller/provider/matrix cases and actual-provider native32
O2/O0/UBSan with 2,560 cases each, plus effective corruption controls.
The normal guest build equals the entire first 220-byte ELF prediction:
218 code bytes and two extent bytes, no metadata reorder or exclusions.
Preserve 18 neighbors, 97 other inputs and protected 189,088 bytes / 720 owners.
Fresh Game **2,924/4,828 (60.56%)**, overall **3,597/5,501 (65.39%)**,
different **1,904**, zero drift; conversion unchanged, README aggregate rows only.
Tools cc49cf5 banks first; both copies' syntax/eleven shared padder tests and
tools-check pass. Preserve all 833 initial mirror hashes / 837 dirty paths
at HEAD ddbdd16. Next recover the adjacent 40-word func_15094EA0 (frame 0x98,
two guMtxL2F calls and matrix combination). Rectangle func_15095D34 stays
at 18 differences; wider Game work remains open. No full gameplay/hardware
claim, push, Claude/auth retry or host/frozen Release action.

Packed point transform installed, **55 words byte-exact with two schedule guards**:
[Note 1441](WORKING_NOTES/1441-packed-point-transform-byte-match-and-rectangle-step-screens-20261016.md).
Replace func_150948C0's zero stub with signed-coordinate transformation of
sixteen optional slots, preserving untouched output rows and the matrix ABI.
Two relocation-aware guards swap independent matrix-address/count setup;
this is not an unguarded raw-C match. All ten final tests pass in 103.223s,
including retail-helper guest execution, native32 O2/O0/UBSan, full-image,
protected-layout and effective corruption controls. The normal guest build
equals the complete first 208-byte ELF prediction: 167 code, one extent and
40 explicit symbol/string serialization bytes, no exclusions. Preserve
18 neighbors, 97 other inputs and protected 189,088 bytes / 720 owners.
Fresh Game **2,923/4,828 (60.54%)**, overall **3,596/5,501 (65.37%)**,
different **1,905**, zero drift; conversion counts unchanged. README changes
only those aggregate rows. Tools 6909297 banks first; preserve all 828 initial
mirror hashes / 833 dirty paths at unchanged HEAD ddbdd16. Both tools copies'
syntax/eleven shared padder tests and tools-check pass. Twelve rectangle
typed-step/staged-corner screens improve none: func_15095D34 stays at 18
differences. **func_1509499C remains its original production stub**; its
71-word recovery and the rectangle remain open, with no gameplay-pipeline
claim, push, Claude/auth retry or host/frozen Release action.

Packet rectangle native temporary blockers, **evidence only; still 18 differences**:
[Note 1440](WORKING_NOTES/1440-packet-rectangle-macro-temporary-pool-and-native-blockers-20261016.md).
Capture the installed 18-word form separately from the earlier 19-word form.
Three identical CFE/UOPT stream pairs, actual 24-event UOPT pool lifetimes
and a mode-5 capture establish why macro X/Y choose M-132/-136. Native
forbidden vectors directly block the first two/three candidate homes; do
not substitute a graph inference or intermediate 144-byte pool extent for
the emitted 136-byte frame. All 29 source forms remain at best 18; no
production C/guard/ELF/CSV/README change. Ten final tests pass in 19.501s,
including raw native gate, ownership, stream and all-input controls. Fresh
Game 2,922/4,828, total 3,595/5,501, different 1,906, zero drift. Tools
e3dca0d banks first; preserve all 826 original mirror hashes / 828 paths.
Next map coordinate ranges 73/107 and signed-16 S-step range 235 to one
typed-step/clipping-stage source hypothesis, retaining full-width Y sign
semantics. Note 1439's runtime qualification is prior unchanged evidence.
No push, Claude/auth retry or host/frozen Release action.

Packet rectangle inner flag capture, **71 -> 18 differences; still not byte matched**:
[Note 1439](WORKING_NOTES/1439-packet-rectangle-inner-flag-capture-and-allocator-order-20261016.md).
Fired native allocator probes show flags take cheap color 12 first; fractional
T then fails a cost gate, not complete register exhaustion. Capture flags
inside the flip branch, recover the original S-step role and inner constant
spelling, retaining 346 words / frame 0x88 with literal 148/91-word spans.
All 20 final tests pass in 127.844s, including fresh native32/UBSan, modeled
guest/caller/alias/trap checks, 64 complete prefix states and strict installed
image/corruption checks. The normal guest rebuild equals the first prediction:
204 changed ELF bytes, all inside the same 1,384-byte slot, zero exclusions
or new guards. Protected 189,088 bytes / 720 owners and 98 other inputs stay
fixed. Fresh Game 2,922/4,828, total 3,595/5,501, different 1,906, zero drift;
no new full-function match or README change. Tools 05ca56d banks first;
preserve all 820 initial mirror hashes / 826 dirty paths. Next recover twelve
flip-block scratch/schedule words and six macro-home words in this same routine.
No hardware/gameplay parity claim, Claude retry, push or host/frozen Release action.

Packet rectangle lifetime screens, **evidence only; still not byte matched**:
[Note 1438](WORKING_NOTES/1438-packet-rectangle-lifetime-screens-and-private-home-rejection-20261016.md).
All 105 complete-owner forms remain at best 71 differences; no production
C/guard/ELF/CSV or README change. Eight tests pass in 15.580s. A split-step
control retains 346 words / frame 0x88 / 71 differences / literal 104/91 spans,
but shifts eight stack accesses by four bytes: 32 guest execution pairs have
equal public output and different private memory. Do not promote equal-count
fits. Read-count probes add four words here and are rejected. Next observe
the pinned UOPT's actual spill-victim decision; do not repeat these source
families or infer executed probes from static symbols. Fresh Game 2,922/4,828,
total 3,595/5,501, different 1,906, zero drift. Tools 3cbb68b banks first;
preserve 818 original mirror hashes / 820 dirty paths. One tool-free Claude
invocation fails with expired OAuth / 401; no advisory completed or account
change. No fresh broad runtime claim, push or host/frozen Release action.

Packet rectangle compiler provenance, **evidence only; no production change**:
[Note 1437](WORKING_NOTES/1437-packet-rectangle-constant-and-spill-provenance-20261016.md).
All 45 complete-owner screens remain at best 71 differences; func_15095D34
stays 346 words / frame 0x88 with literal 104/91-word spans. Qualified
CFE/UOPT captures explain the two FP constant roles, but both allocation
traces retain the same flag/fractional-T conflict. The wrong M-128/-132 homes
already exist in UOPT output; focus next on computed-expression lifetime,
not speculative UGEN scratch padding. All 12 diagnostic tests pass in
15.687s, including 100 frozen/live inputs and effective corruption controls.
Fresh totals stay Game 2,922/4,828 (60.52%), total 3,595/5,501 (65.35%),
different 1,906, zero drift. No new C match, guard, ELF/CSV edit or rebuild;
README unchanged. Tools 9533be8 banks first; preserve all 815 original
mirror hashes / 818 paths. Prior semantic qualification remains prior
unchanged evidence, not a fresh native/gameplay claim. No push or host/Release action.

Packet rectangle extent/lifetime fitting installed, **not byte matched**:
[Note 1436](WORKING_NOTES/1436-packet-rectangle-extent-and-lifetime-fitting-20261016.md).
func_15095D34 now emits the original 346 words / frame 0x88, reducing
331 -> **71** pointwise differences without guards. Its first 104 and last
91 words are literal matches; continue the same routine's 151-word middle
window. All 15 final tests pass in 125.719s, including 64 complete prefix-state
pairs and an effective private-home control. The guest rebuild equals the
first 1,152-byte code/extent prediction; all other ELF bytes / 98 inputs,
18 neighbors, prior guards and protected data remain fixed, no exclusions.
Fresh totals stay Game 2,922/4,828 (60.52%), total 3,595/5,501 (65.35%),
different 1,906, zero drift; README unchanged. Tools aff42ac banks first;
preserve 811 mirror hashes / 815 paths. No full later private/hardware/gameplay
claim, push or host/frozen Release action.

Packet scissored rectangle semantically recovered, **not byte matched**:
[Note 1435](WORKING_NOTES/1435-packet-scissored-rectangle-recovery-20261016.md).
Replace func_15095D34's zero stub with SDK rectangle/tint emission and byte
animation state. The C body is 345 words / frame 0x88 versus retail 346,
with 331 pointwise differences and no new guards. All 14 final tests pass
in 148.459s. The installed ELF equals its complete 1,035-byte pre-install
prediction; every other byte / 98 inputs, 18 neighbors, prior guards and
protected data remain fixed. Fresh totals stay Game 2,922/4,828 (60.52%),
total 3,595/5,501 (65.35%), different 1,906, zero drift; README unchanged.
Tools 552f48e banks first; preserve 806 mirror hashes / 811 paths. Continue
the **same function's** missing instruction, register lifetimes and scheduling
under a new immutable semantic baseline. No full private/hardware/gameplay
claim, push or host/frozen Release action.

Packet visibility provider installed:
[Note 1434](WORKING_NOTES/1434-packet-visibility-provider-byte-match-20261016.md).
func_15095B08 matches all 129 words / leaf frame 0x18 with seven closed
initial-FPR guards. Recover full-word visibility, signed extents, unsigned
descriptor dimensions, live view scales, exact overlap bounds and seven
global outputs. All 18 neighbors remain fixed; all 12 final tests pass in
117.051s, including 48 real projection/depth/visibility connections. The
full guest rebuild equals the first 551-byte ELF prediction, including
157 explicit symbol/string serialization bytes, every other byte / 95 inputs
and protected data fixed, no exclusions. Fresh Game 2,922/4,828 (60.52%),
total 3,595/5,501 (65.35%), different 1,906, zero drift. Tools 3a933e0 banks
first; preserve 801 mirror hashes / 806 paths. Next func_15095D34, 346 words /
leaf frame 0x88, consuming the recovered globals. Matrix modeling and current
draw stubs are not full renderer/gameplay acceptance. Keep inherited-stack
C deferrals and the broader queues open. No push or host/frozen Release action.

Visibility-qualified packet depth installed:
[Note 1433](WORKING_NOTES/1433-visible-depth-packet-byte-match-20261016.md).
func_150958B0 matches all 102 words / frame 0x48 with four closed scratch-GPR
guards. Recover signed coordinates, the full-word visible output, live
16352.0f scale and unchanged unsigned-conversion/FCSR sequence; preserve
all 18 neighbors. All 12 final tests pass in 133.716s. The complete rebuilt
ELF equals the first prediction: 317 bytes, including 32 explicitly modeled
symbol/string swaps, no exclusions; every other byte / 94 inputs and
protected data fixed. Fresh Game 2,921/4,828 (60.50%), total 3,594/5,501
(65.33%), different 1,907, zero drift. Tools 23a25ff banks first; preserve
796 mirror hashes / 801 paths. Next func_15095B08, 129 words / frame 0x18:
audit real visibility writes, extents, view scales and seven output globals.
Its current zero stub and bounded providers are not full rendering/gameplay
acceptance. Keep inherited-stack C deferrals and wider queues open.
No push or host/frozen Release action.

Projection and signed-packet drawing installed together:
[Note 1432](WORKING_NOTES/1432-projected-packet-draw-and-projection-byte-match-20261016.md).
func_15095760 matches all 84 words / frame 0x48 directly through the SDK
graphics macros. Its float-ABI provider func_1509563C matches all 73 words /
frame 0x28 with ten closed output-scheduling guards, not a raw direct match.
Preserve all 17 neighbors and prior guard history. All 13 final tests pass
in 123.196s; the full guest rebuild exactly reproduces the first complete
ELF prediction: 490 code/extent bytes, every other byte / 93 inputs fixed,
protected data exact, no exclusions. Fresh Game 2,920/4,828 (60.48%), total
3,593/5,501 (65.32%), different 1,908, zero drift. Tools 51f51e1 banks first;
preserve 791 mirror hashes / 796 paths. Next func_150958B0, 102 words /
frame 0x48; audit its visible-output pointer and unsigned-depth/FCSR path.
func_1516D738 remains C-deferred under the existing Note 1395 inherited-stack
evidence. Four original caller windows remain zero-filled in the current
ELF; bounded providers are not full render/gameplay acceptance. No push or host/Release action.

Four-byte saturation installed as a direct instruction match:
[Note 1431](WORKING_NOTES/1431-four-byte-saturation-direct-byte-match-20261016.md).
func_1516D400 matches all 58 words / 232 bytes, no frame or target guards.
Recover the four-byte array view and conditional live increment; preserve
all 29 neighbor bodies, including the guarded counter accessor. All 12
final tests pass in 80.304s. Production exactly reproduces the complete
pre-install prediction: 164 code/extent bytes, every other ELF byte and
90 inputs fixed, protected data exact, no exclusions. Fresh Game
2,918/4,828 (60.44%), total 3,591/5,501 (65.28%), different 1,910, zero
drift. Tools eee5a08 banks first; preserve 787 mirror hashes / 791 paths.
Next func_1516D738, 153 words / frame 0x98 in the same owner; audit its
cached render state and SP+0x5C read before assuming an initialized local.
The current callback connection is bounded, not whole-game acceptance.
No push or host/frozen Release action.

Actor effect dispatcher and complete 19E040 owner:
[Note 1430](WORKING_NOTES/1430-actor-effect-dispatch-and-owner-completion-20261016.md).
func_15171BF4 matches all 42 body words / frame 0x28 directly, plus its
separate retail padding nop for the full 43-word slot. No target guards.
All nine owner slots / 4,368 bytes are now linked byte-exact, and no
zero-return placeholders remain in generated_19E040.c. Earlier guarded
matches are preserved, not reclassified as raw direct matches. All 13
final tests pass in 75.277s. The complete ELF equals its first pre-install
prediction: 127 changed code/extent bytes, every other byte / 87 inputs
and protected data fixed, no metadata exclusions. Fresh Game 2,917/4,828
(60.42%), total 3,590/5,501 (65.26%), different 1,911, zero drift. Tools
166a8a1 banks first; preserve 782 initial mirror hashes / 787 final paths.
Next func_1516D400, 58-word leaf in generated_19A8B0.c. The three external
effect helpers and original caller remain unfinished; muted sound-guard
connections are not audible/gameplay acceptance. No push or host/Release action.

Rectangle preset dispatcher installed as a direct instruction match:
[Note 1429](WORKING_NOTES/1429-rectangle-preset-dispatch-direct-byte-match-20261016.md).
func_15171600 matches all 127 words / frame 0x40 with its three-input
void ABI and all thirteen rectangle-emitter arguments restored. No target
instruction guards, new pool or compiler-profile change. All 13 final
checks pass in 84.073s, including all 256 selector values, native32,
effective negatives, rebases, caller captures and the current rectangle
emitter. Preserve the rejected slot-only prediction; explicitly account
for one three-symbol cycle / 53 metadata bytes and reproduce all 449 ELF
changes with no exclusions. Every other byte / 80 inputs and protected
data stay fixed. Fresh Game 2,916/4,828 (60.40%), total 3,589/5,501 (65.24%),
different 1,912, zero drift. Tools 20f2701 banks first; preserve 777 initial
mirror hashes / 782 final paths. Next func_15171BF4, 43-word retail slot
including one padding nop, frame 0x28. Caller func_150265CC and all wider
queues remain unfinished. No push or host/frozen Release action.

Random packet burst installed as a direct instruction match:
[Note 1428](WORKING_NOTES/1428-random-packet-burst-direct-byte-match-20261016.md).
func_15171200 matches all 256 words / frame 0xE0, packet SP+0x7C, with
the fourteen-argument ABI and no target instruction guards. Recover signed
high-half and unsigned low-half RNG roles, live packet scales, word-to-byte
duration conversion and the original literal pool. All 14 final tests pass
in 88.956s. The complete production ELF equals its first pre-install
prediction: 793 slot/extent bytes, no extra metadata changes or exclusions;
every other byte / 80 inputs and the protected layout remain fixed. Fresh
Game 2,915/4,828 (60.38%), total 3,588/5,501 (65.22%), different 1,913,
zero drift. Tools baff8d3 banks first; preserve all 771 initial mirror
hashes / 777 final paths. Next func_15171600, 127 words / frame 0x40.
Caller func_15169C70 remains a placeholder; all broader queues remain
open. No push or host/frozen Release action.

Table debris installed as a direct instruction match:
[Note 1427](WORKING_NOTES/1427-table-debris-direct-byte-match-20261016.md).
func_15170F4C matches all 158 words / frame 0xE8, packet SP+0x84, with
no target instruction guards. Recover genuine float literals, bind their
12-byte retail pool through the existing Makefile alias and recover the
last schedule through real initialization order. Fired owned compiler
observations explain local reservation 144 -> 128 without spill growth.
All 15 final tests pass in 102.084s. The complete ELF matches its first
pre-install prediction: 507 slot/extent + 121 exactly accounted metadata
bytes, every other byte / 75 inputs fixed, protected layout exact, no
exclusions. Fresh Game 2,914/4,828 (60.36%), total 3,587/5,501 (65.21%),
different 1,914, zero drift. Tools a9f3606 banks first; preserve 767 mirror
hashes / 771 paths. Next func_15171200, 256 words / frame 0xE0; caller
func_1511C638 and all broader queues remain open. No push or host/Release action.

Table debris pre-install recovery:
[Note 1426](WORKING_NOTES/1426-table-debris-semantic-recovery-20261016.md).
Recover func_15170F4C's unsigned-halfword/float-table contract, late kind
reread, coefficient snapshots, two float draws and byte actor update.
All seven tests pass in 42.123s: 648 paired whole sequences, native32
O2/O0 with 1,024 cases each, eleven compiled negatives, original ABI
captures, 48 actual consumer/allocator runs and 78 fixed input keys.
Do not install or take matching credit: selected 158 words / frame 0xF8,
packet SP+0x98 and 121 real differences versus retail 158 / 0xE8 / +0x84.
All eight neighbors/pools and production C/guards/ELF remain fixed. The
sole caller func_1511C638 is still a placeholder; its current call-site
window is zero-filled. Official numbers below were freshly confirmed
unchanged. Tools 57f58b3 banks first; preserve 763 mirror hashes / 767
paths. Resume this target's frame/saved lifetimes, retaining all broader
queues. No push or host/frozen Release action.

Six-piece debris installed with checked guards:
[Note 1425](WORKING_NOTES/1425-six-piece-debris-guarded-byte-match-20261016.md).
func_15170B90 matches all 205 retail words / frame 0x120; raw C retains
44 real differences. Preserve all 96 packet bytes and SP+0xBC, normalize
only two checked scheduling/register regions and the unescaped kind home.
All 16 final tests pass in 167.798s, including 1,440 full sequences, 844
fault pairs, native32 O2/O0, caller/rebase and 144 connected consumer cases.
Reject and preserve the initial slot-only prediction; account for exactly
84 extra symbol/string serialization bytes and reproduce the entire ELF
with two full relinks. Final 759 changes, every other byte and 72 inputs
fixed, protected layout exact, no metadata exclusions. Fresh Game
2,913/4,828 (60.34%), total 3,586/5,501 (65.19%), different 1,915, zero
drift; conversions fixed. Tools c0bbd87 banks first; preserve all 757 older
mirror hashes / 763 paths. Next func_15170F4C, 158 words / frame 0xE8;
all broader queues remain active. No push or host/frozen Release action.

Randomized ring emitter installed with checked register guards:
[Note 1424](WORKING_NOTES/1424-randomized-ring-emitter-guarded-byte-match-20261016.md).
func_151718F0 matches all 193 retail words / frame 0x140, with the genuine
ten-input void ABI. Raw C stays eight temporary-register words different;
no frame/home/schedule/FP/branch/binding change. All 15 final tests pass in
91.919s, including 864 loop cases, 514 fault pairs, native32 O2/O0, four
caller windows, three rebase sets and 216 current helper-chain cases.
The full rebuilt ELF matches its original prediction: 602 slot/extent
changes, every other byte and 72 inputs fixed, protected layout exact,
no exclusions. Fresh Game 2,912/4,828 (60.31%), total 3,585/5,501 (65.17%),
different 1,916, zero drift; conversions fixed, README aggregate rows only.
Tools 6f03b11 banks first; preserve 751 mirror hashes / 757 paths. Resume
func_15170B90's 205-word / 0x120 shape with the typed ring prerequisite now
resolved, retaining all broader queues. No push, gameplay or host/Release action.

Six-piece debris pre-install recovery:
[Note 1423](WORKING_NOTES/1423-six-piece-debris-semantic-recovery-20261015.md).
Recover func_15170B90's 96-byte packet, signed RNG, live tables and typed
ten-input ring call. Five checks pass: 1,440 guest cases, native32 O2/O0
with 1,024 cases each, ten effective guest/native negatives and 75 unchanged
input gates. No new match: candidate 210 words / frame 0x128 versus retail
205 / 0x120, with a typed-ring stub neighbor growing 12 -> 28 bytes.
All seven other neighbors are fixed. Production C/guards/ELF/progress and
root README stay unchanged; Note 1422 counts below are not freshly rerun.
Bank tools b88e200 first, preserve 747 mirror hashes / 751 paths. Continue
the target shape/lifetimes and genuine func_151718F0 definition before
installation; retain all broader queues and frozen host/Release boundaries.

Scaled random spray installed with checked guarded normalization:
[Note 1422](WORKING_NOTES/1422-scaled-random-spray-guarded-byte-match-20261015.md).
func_151709B4 matches its full 119-word retail slot: 118 body words plus
one padding NOP, frame 0xF8, symbol size 472 rather than slot size 476.
Recover word coordinate inputs, positive-count gating, stable scale/flags/
context and the complete 31-word factory packet; preserve all three escaped
float output objects and their scaled writebacks. Raw C has 47 real word
differences, with finite multiplication commutation an explicit assumption.
All 15 final checks pass in 100.717s: 3,000 whole-loop cases, 1,260 fault
prefixes, native32 O2/O0 with 1,048,576 cases each, arbitrary-index loop
obligations, three caller windows and 640 connected helper-chain cases.
The full rebuilt ELF matches its initial prediction: 365 target-slot/extent
changes, every other byte and 66 inputs fixed, protected layout exact,
no exclusions. Fresh Game 2,911/4,828 (60.29%), total 3,584/5,501 (65.15%),
different 1,917, zero drift; conversions unchanged, README aggregate rows
only. Tools de7c6d8 banks first; preserve 741 mirror hashes / 747 paths.
Next func_15170B90, 205 words / frame 0x120, in generated_19E040.c. Keep
func_1516D400, inherited-stack func_1516FE1C and all broader Game/additional-
source queues open. No push, gameplay or host/Release operation.

Callback-six fade and random drag installed with checked register guards:
[Note 1421](WORKING_NOTES/1421-record-random-drag-guarded-byte-match-20261015.md).
func_151707E0 matches all 117 retail words / frame 0x28. Preserve byte record
fields, full-word fade/completion, unsigned lifetime RNG, signed drag RNG,
post-movement field reads and retail's repeated-X threshold, including its
signed wrap at -32768. Raw C remains 117 words / 13 register differences;
104 identity and 13 transforming guards change no instruction, branch,
home or binding. All 15 final tests pass in 80.861s: 4,032 literal/public
cases, 444 fault prefixes, native32 O2/O0 with 1,048,578 cases each, 960
connected slot-6 cases and all 801 archive fingerprints. All 116 reachable
words execute; retain and guard the unreachable duplicate load too. The
whole rebuilt ELF matches the initial prediction: 316 target-slot/extent
changes, every other byte and 64 inputs fixed, protected layout exact, no
exclusions. Fresh Game 2,910/4,828 (60.27%), total 3,583/5,501 (65.13%),
different 1,918, zero drift; conversions unchanged, README aggregate rows
only. Tools bce2d08 banks first; preserve 736 mirror hashes / 741 paths.
Next func_151709B4, frame 0xF8, 118 instructions plus one padding NOP in
its 119-word slot. Keep all broader additional-source/Game, caller and
inherited-stack queues active. No push, gameplay or host/Release operation.

Directional burst installed with checked guarded normalization:
[Note 1420](WORKING_NOTES/1420-directional-burst-guarded-byte-match-20261015.md).
func_15170500 now matches all 184 retail words / frame 0x100. Recover its
seven typed inputs, signed remainder, pre-call default-angle snapshot and
complete compact/extended factory packets. Raw C remains 185 words / 97
differences; 185 closed guards retain 184 operations and omit one duplicate
zero transfer. All 15 final tests pass in 95.713s, including 4,608 literal
state pairs, 944 fault prefixes, native32 O2/O0 with 262,144 cases each,
576 current RNG/trig/factory chain pairs and all 801 archive fingerprints.
The full rebuilt ELF exactly matches the pre-install prediction: 575 changed
target-slot/extent bytes, all other bytes and 64 inputs fixed, protected
189,088 bytes / 720 owners exact, no metadata exclusions. Fresh Game
2,909/4,828 (60.25%), total 3,582/5,501 (65.12%), different 1,919, zero
drift; conversions unchanged and README edits aggregate rows only. Tools
d585639 banks first; preserve 729 older-mirror hashes / 736 final paths.
Next func_151707E0, 117 words / frame 0x28; retain the entire additional-
source/Game, unconverted-caller and inherited-stack queues. No push,
gameplay acceptance or host/Release operation.

Quad edge emitter installed with checked guarded normalization:
[Note 1419](WORKING_NOTES/1419-quad-edge-emitter-guarded-byte-match-20261015.md).
func_151700D8 now matches all 266 retail words / frame 0x190 in the rebuilt
ELF; raw C still has 137 differences. All 16 final checks pass in 129.507s,
including 2,304 private pairs, 1,452 fault prefixes, native32 O2/O0 and the
actual wrapper/factory chain. The initial slot-only image prediction was
rejected by 64 symbol-serialization bytes; two exact named cycles and two
independent relinks close the entire ELF to 898 changes, no exclusions.
All other bytes and 60 inputs are fixed, protected layout exact. Fresh Game
2,908/4,828 (60.23%), total 3,581/5,501 (65.10%), different 1,920, zero
drift; conversions unchanged and README edits aggregate rows only. Tools
679f05f banks first; preserve 725 older-mirror hashes / 729 final paths.
Next func_15170500, 184 words / frame 0x100, keeping the full additional-
source/Game and inherited-stack queues open. No push or host/Release action.

Quad emitter loop obligations checked, production unchanged:
[Note 1418](WORKING_NOTES/1418-quad-emitter-symbolic-loop-obligations-20261015.md).
func_151700D8 remains 266 words / frame 0x190 / 137 differences and an
uninstalled stub. A new current-checkpoint fixture passes eight tests in
22.383s: 24 outer cases, 24 arbitrary-index step obligations, nine effective
instruction negatives, 288 guest pairs and all 63 unchanged inputs / 29
neighbors. Finite addition commutation and framed memory are explicit
assumptions; raw private/fault/FCSR parity is not established. Two source
screens reach 134 differences but are not qualified replacements. Tools
bf8dbb3 banks first; all 722 older-mirror hashes survive / 725 final paths.
Fresh official totals below are unchanged, as are the ELF and README rows.
Next derive/qualify the remaining retained-operation schedule and private
edge operations before adoption; keep all broader Game queues open.

Quad rectangle wrapper installed with proven guarded normalization:
[Note 1417](WORKING_NOTES/1417-quad-rectangle-wrapper-proven-guarded-byte-match-20261015.md).
func_151717FC now matches all 61 retail words / frame 0x80 in the rebuilt
ELF. Raw C remains 63 words; 63 closed expected-word guards normalize its
register/schedule layout and omit two nonescaping home operations. The
framed C value proof is separate from literal normalized private/fault checks;
no raw FP-environment equivalence claim. All 14 installed checks pass in
101.707s, including the entire predicted ELF: 190 target-slot/extent changes
only, all other bytes and 60 of 63 inputs fixed, protected layout exact.
Fresh Game 2,907/4,828 (60.21%), total 3,580/5,501 (65.08%), different 1,921,
zero drift; conversions unchanged and README updates aggregate rows only.
Tools 94deb33 is banked first; preserve 717 initial older-mirror fingerprints
/ 722 final paths. Return to func_151700D8's 266/0x190/137 gap, folding the
new successor fingerprints into its experiment. Its stub and the wider
additional-source/inherited-stack queues remain open. No host/Release action
or push; the staged original-emitter chain is not current production C.

Random direction writer installed directly from C:
[Note 1413](WORKING_NOTES/1413-paired-overlay-stack-contract-and-random-direction-match-20261015.md).
func_15170034 matches all 41 raw/padded words, frame 0x30, with no new
guards/profile/header changes. All 18 installed checks pass in 53.253s,
including the complete predicted ELF: 128 target-slot/extent byte changes,
every other ELF byte and 55 of 57 inputs fixed. Fresh Game 2,906/4,828
(60.19%), total 3,579/5,501 (65.06%), different 1,922, zero drift;
conversions unchanged. FE1C's real 31-word exact caller and slot-7 table
reference are now confirmed; its conditional incoming-SP-4 input remains
unresolved for defined C, so that stub stays unchanged. Tools 9bc6852 is
banked first; preserve all 705 initial older-mirror fingerprints / 710 final
paths and frozen Release. Next func_151700D8, 266 words / frame 0x190;
continue the inherited-stack and entire additional-source/Game queues.

Fade/acceleration callback installed directly from C:
[Note 1412](WORKING_NOTES/1412-record-fade-acceleration-direct-match-20261015.md).
func_1516FD50 matches all 51 raw/padded words and frame 0x18 with zero target
guards/profile/header changes. Preserve full-word fade/completion, the live
record home across movement, and signed byte 0x2C plus halfword 0x18 after
the helper. All 14 installed checks pass in 145.837s: 3,072 complete private
pairs, 504 fired fault prefixes, 48 bounded aliases, native32 O2/O0 with
UBSan (24,576 cases each), eight guest/native controls, three rebases and
801 archive hashes. The actual slot-5 dispatcher/callback/move/cleanup chain
passes 276 pairs, including 116 completions and all release/destructor
paths under opaque lower hooks. The entire ELF equals the pre-install
prediction: 144 changed bytes, target slot/extent only. Every other ELF byte,
55 of 57 inputs, guard CSV/profiles/progress and 189,088 protected bytes /
720 owners stay fixed. Fresh Game 2,905/4,828 (60.17%), total 3,578/5,501
(65.04%), different 1,923, zero drift; conversions unchanged. Bank tools
76e1e02 first; preserve all 701 initial older-mirror fingerprints / 705 final
paths. Next func_1516FE1C, 134 words / frame 0x100: inspect its inherited
SP+0xFC word and full two-packet/caller ABI before adopting the archival C.
Keep the full additional-source/Game objective and all broader queues open.
Consumer 6d7ddb42 banks the function, aggregate-only README rows, working
docs and tools 76e1e02 pin. All 14 post-bank checks pass in 49.127s, exit 0;
the whole predicted ELF, all inputs/captures, archive hashes, private/fault/
native/rebase checks and actual installed chain remain qualified. Normal
ELF/progress targets are up to date; all 705 final older-mirror fingerprints
stay fixed. Eight docs resolve 5,074 relative inline links, zero broken.
The source-commit graph update completes at 41,317 nodes / 81,428 edges,
retaining excluded-but-present inputs without forcing a smaller scan.
Continue func_1516FE1C's full contract and the broader queues above.

Record color fade installed with proven MIPS normalization:
[Note 1411](WORKING_NOTES/1411-record-color-fade-proven-normalization-and-match-20261015.md).
func_1516FBCC now matches all 97 padded retail words, leaf/no frame. Raw C
remains 98 words / 89 length-inclusive differences; 84 target-only guards
omit one redundant SLLV mask, shorten two crossing branches and normalize
closed temporary/color-load/LO lifetimes. The C keeps its defined mask.
Symbolic equivalence covers all 54 syntactic CFG paths, including infeasible
width combinations, with exact branch edges/delay slots, return, preserved
ABI registers and symbolic stores. Four dependency mutants are rejected;
an independent legal schedule is accepted. All 14 installed checks pass in
33.767s: 3,586 full private pairs, 194 fired faults, 20 aliases, native32
O2/O0 with UBSan, eight negatives, three rebases, 801 archive hashes and
256 actual-current dispatch/cleanup pairs (160 completions, release types
0/1/2, both destructor branches). Lower unlink/destructors remain opaque.
After the 694-compile normal rebuild, the entire ELF equals the pre-install
prediction: all 281 changed bytes belong to the target slot/extent; every
other ELF byte, 54 of 57 inputs, old guard prefix, profiles, progress and
189,088 protected bytes / 720 owners stay fixed. Fresh Game 2,904/4,828
(60.15%), total 3,577/5,501 (65.02%), different 1,924, zero drift; conversions
unchanged. Bank tools aa35689 first; all 697 initial older-mirror fingerprints
remain fixed across 701 final paths. Next func_1516FD50, 51 words / frame
0x18, slot 5. Keep the complete additional-source/Game queues open.
Consumer e22e176f banks C, target guards, scoped docs, aggregate-only README
rows and tools aa35689. All 14 post-bank checks pass in 54.601s, exit 0;
the complete predicted image, inputs/captures, symbolic/private/fault/native/
rebase checks and actual installed chain remain qualified. Normal ELF/progress
targets are up to date; all 701 final older-mirror fingerprints stay fixed.
Eight scoped docs resolve 5,068 relative inline links, zero broken. The
source-commit graph update completes at 41,304 nodes / 81,413 edges while
retaining excluded-but-present inputs rather than forcing a smaller scan.
Continue func_1516FD50 and all broader queues above.

Historical func_1516FBCC candidate checkpoint, before Note 1411:
[Note 1410](WORKING_NOTES/1410-record-color-fade-semantics-and-compiler-gap-20261015.md).
Ten checks pass in 26.686s: 3,586 C/ROM public-state pairs, all byte shift
counts/phase values, 20 bounded global aliases, eight effective guest/native
negatives, three independent rebases, native32 O2/O0 with UBSan trap checks
(131,074 cases each), 128 staged dispatcher/cleanup pairs and 801 archive
hashes. The defined C is 98 words / 89 length-inclusive differences against
97-word retail; both the exact-match gate and real padder reject it. The
97-word unmasked diagnostic still differs at 65 words and is not selected.
All 3,586 private states differ; 26 of 27 fired prefixes differ. Do not claim
private/fault parity or current callback execution: production is still a
three-word stub, while only the current dispatcher/cleanup bodies are used
around staged callback code. Retail FCC0 is unreachable, so cover 96 reachable
words rather than inventing a 97-word execution claim. All 57 production
inputs and matching totals remain fixed. Tools 64fcc0d is banked first;
preserve all 695 initial older-mirror fingerprints / 697 final paths. Continue
this exact-match gap and the full additional-source/Game queues.
Consumer d65ea282 banks candidate docs and tools 64fcc0d; all ten post-bank
checks pass in 32.988s, exit 0. Production hashes, all 697 final older-mirror
fingerprints and the explicit private/fault rejection evidence remain fixed.
Seven scoped docs resolve 5,043 relative inline links, zero broken. The
source-commit graph update completes at 41,291 nodes / 81,399 edges without
forcing a smaller scan or purging excluded-but-present inputs. Continue FBCC;
this checkpoint is not a completed conversion or new byte match.

Preset-0x1B wrapper installed directly from C:
[Note 1409](WORKING_NOTES/1409-preset-1b-coordinate-types-and-direct-match-20261015.md).
func_1516FA88 matches all 81 raw/padded words and frame 0xD0 with signed
16-bit coordinate formals, full-word variant/context and a narrowed flag.
No guards/profile/shared-header changes. All 14 installed checks pass in
64.906s: 1,554 complete private pairs, 324 fired faults, native32 O2/O0 over
all 16-bit coordinate patterns, eight effective guest/native negatives,
three rebases, 100 actual-current factory/allocator pairs and 801 archive
hashes. Close all 241 ELF changes to target slot/extent only; all other
bytes, 55 of 57 inputs and protected data stay fixed. Fresh Game
2,903/4,828 (60.13%), total 3,576/5,501 (65.01%), different 1,925, zero drift;
conversions unchanged. No aligned direct JAL/address-word references found
in the original ROM; this is not proof of unreachability or gameplay parity.
Tools 2be3d9f is banked first; all 691 initial older-mirror fingerprints
remain fixed across 695 final paths. Next func_1516FBCC, 97 words, leaf,
slot-4 callback. The full additional-source/Game objective remains open.
Consumer f3c47afb banks source, scoped docs, aggregate-only README rows and
tools 2be3d9f. All 14 post-bank checks pass in 59.104s, exit 0; the complete
image/input/capture/native/private/fault/rebase/factory-chain controls remain
qualified. Normal ELF/progress targets are up to date. All 695 final older-
mirror fingerprints stay fixed; eight docs resolve 5,056 relative inline
links, zero broken. The source-commit graph update completes at 41,279 nodes /
81,387 edges while retaining excluded-but-present inputs rather than forcing
a smaller scan. Continue func_1516FBCC and the full queues above.

Record fade callback installed directly from C:
[Note 1408](WORKING_NOTES/1408-record-fade-callback-direct-match-and-live-dispatch-chain-20261015.md).
func_1516F9C4 matches all 49 raw/padded words and frame 0x18, without guards
or profile changes. Preserve the signed full-word clamp/completion value,
exact byte/halfword stores and original record pointer in both helper calls.
All 14 installed checks pass in 48.885s: 3,072 complete private pairs,
408 fired faults, bounded global aliases, native32 O2/O0 across all 256 byte
values, eight effective guest/native controls, three rebases and 801 archive
hashes. The actual current slot-3 callback table/dispatcher/helper/cleanup
chain passes 276 pairs, including 116 cleanup paths; all eight connected
bodies / 213 words are freshly retail-exact. Lower unlink/type destructors
remain opaque; no full-gameplay claim. Close all 138 ELF changes to target
slot/extent only; all other bytes, 55 of 57 inputs, guards/progress and
189,088 protected bytes / 720 owners stay fixed. Fresh Game 2,902/4,828
(60.11%), total 3,575/5,501 (64.99%), different 1,926, zero drift; conversions
unchanged. Bank tools f9563ed first; preserve all 687 initial older-mirror
fingerprints / 691 final paths. Next func_1516FA88, 81 words / frame 0xD0;
retain the full additional-source/Game objective and remaining repair queues.
Consumer 2bf98aaa banks the function, aggregate-only README rows, working docs
and tools f9563ed pin. All 14 post-bank checks pass in 48.135s, exit 0;
the complete image, inputs/captures, archive hashes and actual dispatch chain
remain qualified. Normal ELF/progress targets are up to date. All 691 final
older-mirror fingerprints remain fixed, preserving all 687 initial dirty
files. Eight docs resolve 5,052 relative links, zero broken. The source-commit
incremental graph update finishes at 41,266 nodes / 81,372 edges without
forcing the refused smaller scan. Continue func_1516FA88 above.

Paired factory/event routine installed directly from C:
[Note 1407](WORKING_NOTES/1407-paired-record-event-direct-match-and-compiler-spill-recovery-20261015.md).
func_1516F548 matches all 199 raw/padded words and frame 0xF8, with no guards
or profile changes. Repeated narrowed expressions let UOPT create the actual
40-byte spill region, without named-local reservation or frame rewriting.
Four hash-gated compiler traces establish CFE/UOPT/UGEN provenance. All 17
installed checks pass in 62.530s: 2,072 complete private pairs, 1,152 fired
faults, native32 O2/O0, seven effective guest controls, three rebases, 128 real
factory/allocator pairs, both original caller windows and 801 archive hashes.
One unsigned-coordinate source control optimizes away in IDO and is native-
only. Both linked caller windows remain placeholders; the exact Init event/
callback are bound but not executed. Close all 620 ELF changes to the target
slot/extent only; every other byte, 55 of 57 inputs, guards/progress and all
189,088 protected bytes / 720 owners stay fixed. Fresh Game 2,901/4,828
(60.09%), total 3,574/5,501 (64.97%), different 1,927, zero drift; conversions
unchanged. Bank tools 2018515 first; preserve 682 initial older-mirror
fingerprints / 687 final paths. Next func_1516F9C4, 49 words / frame 0x18;
keep the full additional-source/Game objective and caller restorations open.
Consumer 5a4baee1 banks the C/docs/aggregate rows and tools 2018515 pin. All
17 post-bank checks pass in 89.417s, exit 0; every input/capture/image and
compiler/private/native/chain gate remains qualified. The normal ELF/progress
targets are up to date. All 687 final older-mirror fingerprints stay fixed,
preserving every 682 initial dirty file. Eight docs resolve 5,046 relative
links, zero broken. Actual source-commit graph workers finish at 41,253 nodes /
81,356 edges without forcing the refused smaller scan. Continue F9C4 above.

Earlier paired record/event ABI checkpoint (resolved above):
[Note 1406](WORKING_NOTES/1406-paired-record-event-abi-and-candidate-rejection-20261015.md).
func_1516F548 consumes 17 physical argument slots, including live slots 15/16
beyond unused 12..14. Recover the ten real saved word homes, signed coordinate
aliases, two complete 49-word factory packets and final 12-word Init packet.
All ten checks pass in 20.978s: 2,072 original guest cases, 1,152 original fault
prefixes, native32 O2/O0, seven effective controls, three rebases, 128 real
factory/allocator pairs and both original caller windows. The linked caller
windows remain placeholders; the Init event/callback are bound and exact but
not executed. None of 33 diagnostic-free C forms is exact. The tested 199-word
candidate has frame 0xF8 but 162 differences and fails all 518 forced private-
home cases; the closest 199-word form has 73 differences and frame 0x118.
Keep the production stub, ELF, guards/profiles and all 57 pinned inputs fixed;
zero new credit. Fresh Game stays 2,900/4,828 (60.07%), total 3,573/5,501
(64.95%), different 1,928, zero drift. Bank tools 07a68c3 first, preserve all
680 initial older-mirror fingerprints / 682 final paths, and inspect actual
compiler home/spill reservations next. README stays aggregate-only.

Dual factory preset installed directly from C:
[Note 1405](WORKING_NOTES/1405-dual-factory-preset-direct-match-20261015.md).
func_1516F2F8 matches all 148 raw/padded words, frame 0xD8, with no new guards
or profile changes. Indexed reads preserve the live fifth input and saved
first-byte home across two complete factory packets. All 14 installed checks
pass in 158.928s: 4,120 private guest cases, 636 fired faults, native32 O2/O0,
seven effective guest negatives, eight native negatives, three rebases and
256 real two-factory/allocator pairs. Three narrowing casts optimize away in
IDO and are native-only controls. Five original caller windows are qualified
at their call boundaries, but all five linked windows remain placeholders.
Close all 442 ELF changes to target slot/extent; every other byte, 53 of 55
inputs, guards/progress and protected data stay fixed. Fresh Game 2,900/4,828
(60.07%), total 3,573/5,501 (64.95%), different 1,928, zero drift; conversions
fixed. Bank tools 28f7a09 first; preserve 676 initial older-mirror fingerprints /
680 final paths. Next func_1516F548, 199 words / frame 0xF8; full goal stays open.
Consumer 63e6b1b3 banks source/docs/pin; all 14 post-bank checks pass in
52.117s, exit 0. All 55 input states / 801 archive files / 680 final mirror
fingerprints remain fixed, preserving 676 initial dirty files. Eight docs
resolve 5,030 relative links, zero broken; actual incremental graph workers
finish at 41,229 nodes / 81,332 edges without forcing the smaller scan.
Next routine reads slots 15/16 and coordinate-home aliases absent from the
archive's fourteen-formal declaration; retain that precise ABI handoff.

Table-fade callback installed and guarded-exact:
[Note 1404](WORKING_NOTES/1404-table-fade-callback-frame-restoration-and-guarded-match-20261015.md).
func_1516F024 matches all 103 linked words and frame 0x68. Genuine live tail
operands recover CFE/UOPT/local reservations 72/76/80; raw C remains 103/15.
Twenty-seven guards normalize 15 scheduling/register words and check 12
remaining bindings, with no frame/FP/profile guards. All 16 installed checks
pass in 72.903s: 8,352 literal private cases, 232 fired prefixes, native32
O2/O0, eight controls, three rebases and 264 actual helper-chain pairs. Of
28 aliases, 26 complete and two retain identical unmapped-read prefixes.
Close all 413 ELF changes to 307 target slot/extent bytes and 106 bytes of
four exact symbol/name swaps; every other byte, 49 of 52 inputs and protected
data stay fixed. Fresh Game 2,899/4,828 (60.05%), total 3,572/5,501 (64.93%),
different 1,929, zero drift; conversions fixed. Bank tools 908f406 first and
preserve 671 initial older-mirror fingerprints / 676 final paths. Next
func_1516F2F8, 148 words / two full factory packets; keep the full objective open.
Consumer f01675b3 banks source/guards/docs/pin; all 16 post-bank checks pass
in 121.611s, exit 0, with the complete independent image and all 52 input
states / 801 archive files fixed. All 676 final mirror fingerprints remain
pinned, preserving 671 initial dirty files. Eight docs resolve 5,024 relative
links, zero broken; the actual incremental graph finishes at 41,218 nodes /
81,320 edges without forcing the smaller scan. Normal build is up to date.

Table-fade callback semantically recovered, not installed:
[Note 1403](WORKING_NOTES/1403-table-fade-callback-recovery-and-frame-gap-20261015.md).
func_1516F024 has 103 raw/padded words / 19 differences, frame 0x60 versus
retail 0x68. Typed 11-byte table snapshots, full-word clamps, packed fields and
actual helpers pass ten checks in 37.649s: 8,352 guest cases, 270,336 native32
cases per O2/O0, eight effective controls, 1,024 partial-word cases and 264 real
helper-chain pairs. All 116 fired fault pairs still fail literal private state;
retain that rejection and strict installation gate. Preserve all 52 production
inputs, 29 neighbors, protected data and 801 archive hashes. Fresh Game remains
2,898/4,828, total 3,571/5,501, different 1,930, zero drift; README unchanged.
Bank tools e086765 first; preserve all 669 initial dirty older-mirror files /
671 final paths. Next resolve this same callback's six frame/home words and
two scheduling/register groups via actual compiler frame provenance. No
guards/profile/source adoption, host operation or whole-goal completion.
Consumer e8e7c7f9 banks docs/pin; all ten direct WSL post-bank checks pass in
42.291s, exit 0. All 52 live inputs / 801 archive files / 671 final mirror
fingerprints remain fixed. Seven docs resolve 5,015 relative links, zero broken;
the actual incremental graph completes at 41,207 nodes / 81,301 edges without
forcing the smaller scan. The production stub and match totals remain unchanged.

Counter preset installed and guarded-exact:
[Note 1402](WORKING_NOTES/1402-counter-preset-guarded-match-20261015.md).
func_1516EED4 matches all 84 linked words, frame0xD0. Raw C remains 85/76;
38 guards preserve a closed temporary-register cycle, one redundant-load
omission, its branch adjustment and the unchanged call binding. All 14 installed
checks pass in 138.988s: 3,240 literal private guest cases, 138 fired prefixes,
native32 O2/O0, ten controls, three independent rebases, 24 aliases and 128 actual
current factory-chain pairs. Close all 252 ELF changes to target slot/extent,
with every other byte and 49 of 52 inputs fixed, including protected data and
all old guards/progress rows. Fresh Game 2,898/4,828 (60.02%), total 3,571/5,501
(64.92%), different 1,930, zero drift; conversions unchanged. Bank tools a4ac643
first and preserve all 665 initial older-mirror fingerprints / 669 final paths.
Next func_1516F024, 103 words/frame0x68; retain the full source/Game objective.
Consumer be0f980a banks source/guards/pin/docs; all 14 post-bank checks pass
in 50.628s. All 52 input states / 801 archive files / 669 final mirror paths
remain pinned, preserving all 665 initial dirty mirror files. Normal build
is up to date; 5,009 relative links in seven docs resolve. The source commit's
incremental graph finishes at 41,196 nodes / 81,291 edges without forcing
the smaller scan. All 84 linked words remain guarded-exact, not direct C.

Historical counter-preset semantic recovery, superseded by Note 1402 above:
[Note 1401](WORKING_NOTES/1401-counter-preset-semantic-recovery-and-private-schedule-gap-20261015.md).
Recover func_1516EED4's signed slot/threshold gate, pre-call counter clear
and complete 49-word packet. Inline subscripts repair input-home clear ordering;
raw C stays 85 words / 76 differences versus 84 retail words. All 11 checks pass
in 142.171s: 3,240 guest cases, native32 O2/O0, ten effective negatives, three
rebases, 12 repaired home aliases, 138 fired prefixes and 128 real factory-chain
pairs. All 52 production inputs / 801 archive hashes stay fixed. A hash-gated
diagnostic describes 84 exact words by one load omission, branch adjustment
and a closed temporary-register cycle; it emits no guards and is not matching
qualification. Keep strict installation rejection and README aggregates fixed:
Game 2,897/4,828, total 3,570/5,501, different 1,931, zero drift. Bank tools f14494c
first, preserve all 663 initial older-mirror fingerprints / 665 final paths,
and finish this same function's private/rebase/linked-image gates next.
The full additional-source / Game objective remains open.
Consumer 9f5b8cf7 banks docs/pin; all 11 post-bank checks pass in 59.781s.
All 52 production inputs / 801 archive files / 665 final mirror fingerprints
remain fixed, preserving all 663 initial dirty mirror files. The incremental
graph completes at 41,186 nodes / 81,281 edges without forcing the smaller
scan; 5,003 relative links in seven docs validate. No new match credit.

Actor-type preset recovered directly from C:
[Note 1400](WORKING_NOTES/1400-actor-type-preset-direct-match-20261015.md).
func_1516ED68 matches all 91 raw/padded words, frame0xD0, with its byte type
gate and complete four-input/49-word packet. No new guards/profile changes.
All 13 checks pass in 43.045s: 4,626 guest cases, ten aliases, 146 fired
prefixes, native32 O2/O0, eight effective guest controls, two native-only
narrowing probes, three rebases and 256 actual factory-chain cases. Close all
280 ELF changes to target slot/extent; every other byte and 50 of 52 inputs
remain fixed, including all guards/progress rows and protected data. Fresh
Game 2,897/4,828 (60.00%), total 3,570/5,501 (64.90%), different 1,931,
zero drift; conversions unchanged. Bank tools 50205ee first and preserve all
659 initial older-mirror fingerprints / 663 final paths. Next func_1516EED4,
84 words, with the original signed slot gate and pre-call byte clear. Keep
the complete additional-source / Game objective open.
Consumer b1b985f3 banks source/pin/docs. All 13 post-bank checks pass in
104.578s; all 52 input states / 801 archive files / 663 final mirror paths
remain pinned, with all 659 initial dirty mirror fingerprints preserved.
Normal ELF/progress build is up to date; 4,997 relative links in seven docs
resolve without errors. The source commit's incremental graph completes at
41,176 nodes / 81,272 edges without forcing the refused smaller full scan.

Packed RGB callback installed and byte-exact with explicit guards:
[Note 1399](WORKING_NOTES/1399-packed-color-callback-byte-match-20261015.md).
func_1516E8CC matches all 248 linked words. Raw C is 246 words with five
initial register differences; seven guards retain that lifetime and the dead
duplicate return. No FP guard/profile change. All 14 checks pass in 36.799s:
3,072 semantic cases, 643 fired prefixes, native32 O2/O0, five controls, three
independent rebases, 256 real callback/cleanup cases and 801 archive hashes.
Close all 713 ELF changes to target slot/extent plus 21 explicitly modeled
symbol/name-order bytes; all canonical bindings, other code and protected
data remain fixed. Of 52 inputs, only owner/ELF/guards change. Fresh Game
2,896/4,828 (59.98%), total 3,569/5,501 (64.88%), different 1,932, zero drift;
converted counts/bytes unchanged. Bank tools 8981c28 first and preserve all
654 initial older-mirror fingerprints / 659 final paths. Next func_1516ED68,
the 91-word type-gated factory preset; keep the broader source/Game goal open.
Consumer 7c1c25ec banks source/guards/pin/docs; all 14 post-bank checks pass
in 68.595s. All 52 input states / 801 archive files / 659 final mirror
fingerprints remain pinned, and the normal build is up to date. The incremental
graph completes at 41,166 nodes / 81,262 edges without forcing the smaller scan.

Packed color callback semantic recovery, deliberately not installed:
[Note 1398](WORKING_NOTES/1398-packed-color-callback-semantic-recovery-20261015.md).
Recover func_1516E8CC's packed widths, full live clamps, extent growth and
unsigned RGB interpolation. Seven checks pass in 29.801s: 3,072 paired guest
cases, 1,024 further guest/native32 O2/O0 cases, five effective controls,
29 fixed owner neighbors, all 52 fixed production inputs and 801 archive
hashes. The tested clean body is 241 words / 234 positional differences;
a separate nested-return form is 245 / 153. Neither is byte-exact; the
installation gate rejects both, and no C/guard/profile/progress change is
made. Fresh official Game 2,895/4,828, total 3,568/5,501, different 1,933,
zero drift. Bank tools af89f68 first, preserve all 652 initial older-mirror
fingerprints and continue at the original V0 record/color lifetime, live
loop bound and exit-shape mismatch. Full private/fault/rebase/lifecycle/image
qualification and the broader additional-source / Game objective remain open.
Consumer 7f267179 banks docs/pin; all seven post-bank checks pass in 61.892s.
All 52 inputs / 801 archive files / 654 final mirror fingerprints remain
fixed, and the incremental graph completes at 41,156 nodes / 81,252 edges
without forcing the refused smaller scan. No byte-match credit is added.

Packed-coordinate preset recovered directly from C:
[Note 1397](WORKING_NOTES/1397-packed-coordinate-preset-direct-match-20261015.md).
func_1516E778 matches all 85 raw and padded words with an explicit low-half
mask, no new guards or profile changes. Preserve its full five-input/49-word
packet and original frame/delay-store lifetime. All 15 installed checks pass
in 36.720s: 3,096 guest cases, 112 fired prefixes, native32 O2/O0, six effective
controls, three independent rebases and 256 actual factory/allocator cases.
Close all 258 ELF changes to target slot/extent; all 29 neighbors, protected
data, guards, shared headers and progress rows remain fixed. Fresh Game
2,895/4,828 (59.96%), total 3,568/5,501 (64.86%), different 1,933, zero drift;
conversions unchanged. Bank tools 8445ba1 first; preserve archive, independent
older mirror and frozen Release. Next: func_1516E8CC, the 248-word callback.
The older 293-word / 291-difference draft is only a lead. Whole additional-C /
Game queues and actual gameplay/provider acceptance remain open.
Consumer 1002474c banks source/pin/docs. All 15 post-bank checks pass in
33.135s; all 50 installed input states / 801 archive files / 652 final mirror
fingerprints remain pinned. Normal ELF/progress build is up to date. The
incremental graph completes at 41,146 nodes / 81,243 edges without forcing
the refused smaller scan. All 85 words are directly exact, with no new guards.

Prior complete additional-source/commented/conditional coverage refreshed:
[Note 1396](WORKING_NOTES/1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md)
and the [173-entry obstruction review queue](ADDITIONAL_SOURCE_REVIEW_QUEUE.csv).
Verify all 801 original files; scan 558 C files, 91 headers and one assembly
include. Find 4,131 active lexical definitions and 353 commented records:
213 already exact active C, 140 needing qualification; no hidden header bodies.
Revalidate/re-link all 1,717 historical successful objects across four corpora
and refresh the linked diagnostic comparison: zero new raw imports. Retain
57 commented / 70 individual compile-failure functions, 38 binding/translation
cases and eight unanchored definitions. These are obstruction queues, not the
whole unmatched Game backlog; do not add duplicated profile/owner counts.
Resume func_1516E778 matching: selected 85 words / 46 real differences,
complete 49-word packet verified in 1,560 guest cases and native32 O2/O0.
All 46 checks pass in 10.018s. The installation gate rejects this mismatch;
no C, guards, ELF or progress rows change. Fresh official Game 2,894/4,828,
total 3,567/5,501, different 1,934, zero drift. Bank tools 8ec9137 first and
preserve archive, 643 initial older-mirror fingerprints and frozen Release.
Next finish compiler-role/owner/private/fault/rebase gates before installing
the preset; keep failed-comment/binding repairs and the full goal open.
Consumer 83fb85fa banks docs, the durable queue and tools 8ec9137 pin. All 46
post-bank checks pass in 9.357s; all 49 production inputs, 801 archive files,
173 exported source locations and 647 final mirror fingerprints remain fixed.
The source commit's incremental graph completes at 41,136 nodes / 81,232
edges without forcing the refused smaller full scan. No C match is added.

Prior packed fade/scale callback recovered, renderer C recovery explicitly deferred:
[Note 1395](WORKING_NOTES/1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md).
func_1516ECAC matches all 47 linked words with three relocation-aware guards;
raw C remains three operand-load words different. Recover the actual byte
fields, live signed-word clamps, wrapping product, two halfword extents and
completion return. All 14 installed checks pass in 123.060s; the added exact
checkpoint/capture check passes separately in 0.765s. Exercise 6,144 guest
cases, 130 fired prefixes, native32 O2/O0, six effective negatives, three
independent rebases and 256 real updater/callback/cleanup cases.
Close all 135 ELF changes to target slot/extent; retain 29 neighbors, protected
data, shared headers, progress rows and every old guard byte. Fresh Game
2,894/4,828 (59.94%), total 3,567/5,501 (64.84%), different 1,934, zero drift;
conversion counts/bytes unchanged. Bank tools 94c4245 first and preserve the
archive, older mirror and frozen Release. Root README remains aggregate-only.
func_1516D738's mode-cache hit reads inherited sp+0x5C: 24 bounded original
cases through actual texture helpers reproduce it. The packet writer writes
sp+0x94, not that word. Do not initialize or adopt an undefined C local for
matching credit; the renderer is unchanged/unrecovered. Next recover the
85-word preset wrapper func_1516E778 and its true five-input/call-packet ABI.
Full additional-C / Game, renderer and gameplay/provider qualification remain
open; no automatic host transfer or whole-goal completion claim.
Consumer c899b74f banks source/guards/pin/docs. All 15 post-bank checks pass in
45.794s; all 49 installed input states, 801 archive files and 643 final mirror
fingerprints remain pinned. Normal ELF/progress build is up to date. The
incremental graph worker completes at 41,125 nodes / 81,222 edges without
forcing the smaller full scan. Raw C still differs at three load words.

Prior callback-driven packed-record update recovered with three register guards:
[Note 1394](WORKING_NOTES/1394-packed-record-updater-callback-and-guarded-match-20261015.md).
func_1516D678 matches all 48 linked words. Raw C remains three words different
in one closed final-temporary allocation and commutative addition; no profile
change. Recover the actual callback-table lookup, exact return-1 removal,
post-callback live fields/delta, halfword lifetime clear and wrapping 24.8 Y.
All 14 focused checks pass in 26.586s, including 1,536 guest cases, 152 fired
prefixes, native32 O2/O0 and 128 constructor/update/cleanup lifecycle cases.
Close all 140 ELF changes to target slot/extent; 29 neighbors, data, shared
header contents and progress rows remain fixed. Preserve every old guard byte,
appending only three rows. Fresh Game 2,893/4,828 (59.92%), total
3,566/5,501 (64.82%), different 1,935, zero drift; conversions unchanged.
Bank tools 6ee5fbe first; preserve archive/mirror/frozen Release. Next:
func_1516D738, still a 153-word stub. Its older 150-word / 150-difference
archive draft is only a lead. Lower callbacks/unlink/destructors and full
gameplay remain separate qualification boundaries; no automatic host transfer.
Consumer 26623707 banks the source/guards/pin/docs. All 14 post-bank checks pass
in 31.496s; all 46 input states / 801 archive files / 638 final mirror
fingerprints remain fixed. Normal ELF/progress build is up to date. The
incremental graph worker completes at 41,114 nodes / 81,211 edges; raw C still
differs by three register-allocation words.

Prior packed 0x34-byte factory and optional position/scale binding recovered directly:
[Note 1393](WORKING_NOTES/1393-small-record-factory-direct-match-20261015.md).
func_1516D4E8 matches all 100 words without new guards or profile changes.
Recover all 31 inputs, packed field widths and the typed optional pointer;
ordinary statement/declaration order preserves the retail sp+0x34 lifetime.
All 14 focused checks pass in 47.525s: 3,072 guest cases, 630 fault prefixes,
native32 O2/O0 and 128 cases connecting actual allocator/position-scale helpers.
Close all 299 ELF changes to target slot/extent; all 29 neighbors, data, guards
and progress rows stay fixed. Fresh Game 2,892/4,828 (59.90%), total
3,565/5,501 (64.81%), different 1,936, zero drift; conversions unchanged.
Bank tools b545f58 first and preserve archive, older mirror and frozen Release.
Next: func_1516D678, the still-stubbed 48-word record updater. Its older archive
screen emits 50 words / 38 real differences, only a lead. Lower heap,
registration and record-builder providers remain opaque in the connected
model; no full gameplay or host-transfer acceptance is claimed.
Consumer f3a2ee59 banks the source/pin/docs. All 14 post-bank checks pass in
47.216s; all 45 input states / 801 archive files / 633 final mirror fingerprints
remain pinned. Normal ELF/progress build is up to date. The incremental graph
worker finishes at 41,104 nodes / 81,201 edges; this C match needs no new guards.

Prior packed 0x4C-byte record factory recovered with six scheduling guards:
[Note 1392](WORKING_NOTES/1392-packed-record-factory-widths-and-guarded-match-20261015.md).
func_1516D99C now matches all 125 linked words. Raw C remains six words
different in two closed load/store schedules; no profile changes. Correct the
archive's overlapping word stores to packed byte/halfword fields and preserve
the already-exact 78-word caller. All 14 focused checks pass in 45.597s,
including 2,048 guest cases, 456 fault prefixes, native32 O2/O0 and 128 actual
wrapper/factory/allocator chains. Close all 374 ELF changes to target slot /
extent; 29 neighbors, protected data and progress rows stay fixed. Preserve
every previous guard byte and append six rows. Fresh Game 2,891/4,828 (59.88%),
total 3,564/5,501 (64.79%), different 1,937, zero drift; conversions unchanged.
Bank tools 49b76f0 first, preserve all 801 archive files / 623 initial older
mirror fingerprints and frozen Release. Next: the still-stubbed 100-word
0x34-byte factory func_1516D4E8; its old 120-word / 106-difference archive
screen is only a lead. Heap allocation and registration remain opaque in
the connected model; no complete gameplay or host-transfer claim.
Consumer f3b01c10 banks the source/guards/pin/docs. All 14 post-bank checks pass
in 36.854s, with all 43 input states / 801 archive files / 628 final mirror
fingerprints fixed. Normal ELF/progress build is up to date. The incremental
graph worker finishes at 41,095 nodes / 81,191 edges; raw C still differs by six.

Prior preset-0x2D factory wrapper recovered directly from C:
[Note 1391](WORKING_NOTES/1391-factory-preset-wrapper-widths-and-direct-match-20261015.md).
func_1516F1C0 matches all 78 words without new guards or profile changes.
The archive's two incorrect narrowings are removed; only arg2 narrows to a
byte. All 13 focused checks pass in 29.641s, including the 49-word packet,
786 guest cases, 110 fault prefixes, native32 O2/O0 and three original-assembly
rebases. Close all 233 ELF changes to target slot/extent; 29 neighbors, data,
guards and progress rows stay fixed. Fresh Game 2,890/4,828 (59.86%), total
3,563/5,501 (64.77%), different 1,938, zero drift; conversions unchanged.
Tools f0e67c2 are banked first; all 801 archive and 618 initial older-mirror
fingerprints remain fixed, with only five absent owned files copied.
Next: recover the still-stubbed 125-word factory func_1516D99C. Its older
archive screen emits 158 words / 140 differences, not adoption evidence.
The wrapper's factory boundary remains opaque; no gameplay or host claim.
Consumer 63f5eaf7 banks the source/pin/docs. All 13 post-bank checks pass in
29.006s; 41 input states, all 801 archive files and all 623 final mirror
fingerprints remain pinned. The ELF/progress build is up to date, and the
incremental graph worker completes at 41,085 nodes / 81,179 edges.

Prior original rotation kernel restored; one false C conversion removed:
[Note 1390](WORKING_NOTES/1390-original-rotation-kernel-and-real-math-chain-restoration-20261015.md).
func_150A8050 matches its complete 84-word slot as original assembly, not C.
Four C/profile screens do not fit; preserve the split frame and FP lifetime.
All 14 checks pass in 97.427s, including actual math and complete builder /
position chains without opaque providers. Close all 280 ELF changes to target
slot/extent, preserve data/guards and change only its generated progress row
from C to assembly. Converted total 5,501/6,044 (91.02%), bytes 86.04%; Game
4,828/5,323 (90.70%), bytes 85.41%. C-exact numerators stay 3,562 total / 2,889
Game; fractions 64.75% / 59.84%, different 1,939, zero drift. No new C credit.
Bank tools 18698b3 first; preserve archive, older mirror and Release. Next:
freshly qualify the archived func_1516F1C0 factory-call wrapper, still a stub.
Consumer 51eb0dad banks the adapter/pin/aggregate correction/docs. All 14
post-bank checks pass in 93.223s; all 38 input states and 618 final mirror
fingerprints stay fixed. The incremental graph worker finishes at 41,075
nodes / 81,169 edges without forcing a smaller scan. C credit remains zero.

Prior actor world-matrix builder recovered directly from C:
[Note 1389](WORKING_NOTES/1389-actor-world-matrix-builder-direct-match-20261015.md).
func_1511490C matches all 40 words / frame 0x60 with no guards or profile changes.
All 14 checks pass in 146.515s: 3,072 guest cases, 576 fired prefixes, native
O2/O0 controls, three rebases and actual helper/position-consumer connections.
The full ELF closes to 123 changed bytes, target slot/extent only; all protected
data and 32 other input paths stay fixed. Game 2,889/4,829 (59.83%), total
3,562/5,502 (64.74%), different 1,940, zero drift; conversions unchanged.
Bank tools 3e43b4a first and preserve archive, older mirror and Release.
Next: inspect func_150A8050's empty rotation-provider boundary and retail
saved-FP lifetime. Its archived GLOBAL_ASM is not byte-matching C or gameplay proof.
Consumer 1f226f06 banks source/pin/docs. All 14 post-bank checks pass in
138.253s; all 34 expected input states and 612 final mirror fingerprints stay
fixed. The incremental graph worker finishes at 41,066 nodes / 81,171 edges
without forcing the smaller full scan. The lower rotation boundary remains open.

Prior special-object position recovered and guarded byte-exact:
[Note 1388](WORKING_NOTES/1388-special-object-position-matrix-frame-and-guarded-match-20261015.md).
func_1511F31C matches all 51 linked words with a real 64-byte matrix, typed
helper calls and two frame-only guards. Raw C still differs at allocation and
release, so this is not a direct compiler match. All 14 checks pass in 77.922s;
2,560 guest cases, 122 fired prefixes, native O2/O0 controls, three rebases and
the actual point-transform connection pass. The full ELF closes to 152 changed
bytes, target slot/extent only; protected data and 25 other inputs stay fixed.
Game 2,888/4,829 (59.81%), total 3,561/5,502 (64.72%), different 1,941, zero
drift; converted counts unchanged. Bank tools c51788d first, preserve archive,
601 older mirror fingerprints and Release. Next: recover matrix-builder
func_1511490C, still a production stub; no complete gameplay or host claim.
Consumer 37621fb5 banks source/guards/pin/docs. All 14 post-bank checks pass
in 75.216s; all 28 input hashes and 606 final mirror fingerprints stay fixed.
The incremental graph worker finishes at 41,055 nodes / 81,161 edges without
forcing the smaller full scan. Keep the guarded/raw boundary explicit.

Prior capture-request slot installed and guarded byte-exact:
[Note 1387](WORKING_NOTES/1387-capture-request-compiler-roles-and-guarded-byte-match-20261015.md).
func_151745F0 matches all40 linked words with its complete typed C body and22
relocation-aware allocation/scheduling guards. Raw C still differs22 words;
this is not an unguarded/direct compiler match. Fresh phase probes identify the
cursor/end roles in UOPT;18 new controls give no direct improvement. Prove the
closed instruction permutation,14,336 full guest states,322 fired prefixes,
three original-assembly rebases/768 executions and native/negative controls.
All21 final top-level checks pass101.665s, including historical image gates.
The normal rebuild equals the independently pinned3257636-byte ELF with only
121 changed bytes, target code and12->156 extent only. Every other ELF byte
and189,088 protected data bytes stay fixed. ELFd8f985cd; progress3ad7466c.
Fresh Game2,887/4,829 (59.78%), total3,560/5,502 (64.70%), different1,942,
zero drift; conversions unchanged. README aggregate rows only. Bank tools
d59c316/fdae1b3 first; preserve801 archive hashes,595 older mirror fingerprints
and Release. Host output remains a stub; no transfer. Next: func_1511F31C's
prototype/64-byte matrix reconstruction, not an assumed jump-table binding.
Consumerb8c40270 banks source/guards/pin/docs after toolsd59c316/fdae1b3. All21
post-bank checks pass67.669s, all26 expected installed hashes stay fixed and
the build is up to date. The graph worker completes41,045 nodes/81,162 edges
without forcing a smaller scan. Keep the guarded/raw distinction explicit.

Prior unguarded capture-request reconstruction checkpoint:
[Note 1386](WORKING_NOTES/1386-capture-request-inline-copy-reconstruction-20261015.md).
Reopen func_151745F0's pseudo-copy gap. Recover the real three-record layout,
byte fields, FP/O32 ABI and inline36-byte struct assignment. All54 controls have
zero diagnostics; keep the39-word body/one alignment NOP/22-difference seed.
Qualify14,336 guest cases,2,048 native cases/profile and three returned controls,
but preserve8,288 private-state and306/322 fired-prefix mismatches. Retail has
38 reachable words, one unreachable duplicate increment and one alignment NOP.
All15 final top-level checks pass45.771s, including current image/history gates.
Bank tools10ccd75 first; preserve all26 production inputs,801 archive hashes,
592 older mirror fingerprints, README/metrics and frozen Release. Continue
THIS function's cursor/end allocation and parameter/copy schedule before installing.
Consumerf1234a74 banks pin/docs after tools10ccd75. All15 post-bank checks pass
54.909s, all26 production hashes stay fixed and the graph worker completes
41,033 nodes/81,148 edges without forcing a smaller scan. Keep every recorded
private mismatch visible; no additional match or conversion is claimed.

Selected-view render pass recovered and byte-exact:
[Note 1385](WORKING_NOTES/1385-selected-view-render-pass-dispatch-match-20261015.md).
func_15019464 now matches all79 words directly under unchanged -O2 -g3, zero
guards. Reuse its Gfx cursor and unsigned viewport stride; preserve15 neighbors.
Qualify1,920 guest cases,948 native cases/profile,1,524 fired prefixes, three
original-assembly rebases and320 connections to the actual30-word viewport
helper. Close all151 ELF byte changes to the existing316-byte code slot with
every other ELF byte and189,088 protected data bytes fixed. ELFf3a09d0a,
progress3ad7466c. Fresh Game2,886/4,829 (59.76%), total3,559/5,502 (64.69%),
different1,943, zero drift; conversions unchanged. README aggregate rows only.
Tools49961e5/d98b8d8 are banked first. All15 final top-level checks pass118.890s,
including five embedded actor gates and their three embedded matrix gates.
Current/captured corruption controls and exact-input inverses pass; all801
archive fingerprints remain fixed. Consumer5eaad3e4 banks the source/pin/docs;
all15 post-bank checks pass53.003s, all24 expected hashes remain fixed and the
build is up to date. The graph worker completes41,023 nodes/81,138 edges without
forcing a smaller scan. Preserve586 older mirror fingerprints
and Release. The selected host translation already has this retail-shaped
function plus witness hooks; no host transfer or rebuild is implied.

Actor mode flags donor recovered and byte-exact:
[Note 1384](WORKING_NOTES/1384-actor-mode-flags-donor-and-original-table-binding-20261015.md).
Reopen the unresolved .rodata queue and replace func_1507DF10's false stub with
the archive's complete53-word C switch. Zero guards; bind the compiler pool to
the original six-entry retail table without changing any data. Preserve15 raw
neighbors and qualify2,432 guest cases,1,216 native cases/profile,37 prefixes,
three rebases and760 connections to the already-matched27-word caller. Correct
the caller reference's unsigned8 gate before claiming acceptance. All16 final
top-level checks pass36.209s, including three embedded matrix history gates.
Exactly168 ELF bytes change, confined to this slot and12->212 extent; every
other ELF byte and189,088 protected data bytes stay fixed. ELF7aee8cd7,
progress3ad7466c. Fresh Game2,885/4,829 (59.74%), total3,558/5,502 (64.67%),
different1,944, zero drift; conversions unchanged. README changes aggregate rows
only. Preserve801 archive fingerprints,580 older mirror fingerprints and Release.
Tools f2b6070/9d0e2a1 are banked first. The32 scanner return forms give no new
match; continue the real binding/failed-source/Game queues and retain its258-
difference HOMES seed. The host still selects a zero stub; no automatic transfer.
Consumer b8374cfa banks the source/pin/docs after the tools commits. All16 post-
bank checks pass41.006s, including three embedded history gates. The incremental
build is up to date, all22 installed inputs retain their expected hashes, and
the graph worker completes at41,013 nodes/81,175 edges without forcing a scan.

Texture vertex-span lifetime tradeoff verified; still NOT installed/exact:
[Note 1383](WORKING_NOTES/1383-texture-vertex-span-lifetime-role-tradeoffs-20261015.md).
Screen27 further complete controls. Merging opcode/count recovers maximumT0/
countA3 but wrongly assigns opcodeA3 and worsens to274 differences; moving the
index initialization emits310 words/288 differences. Fresh CFE/UOPT/UGEN and
31-variable/50-constraint mode5 evidence verify the tradeoff, not a numeric
priority formula. Two selected candidates pass guest/native behavior, but55/63
private prefixes still differ. All14 final checks pass56.686s after the explicit
native unused-local annotation. Bank tools518e1ab first; preserve18 production
hashes,801 archive fingerprints and576 unrelated mirror fingerprints. HOMES
remains339 words/frame0xA8/258 differences. README/metrics and Release stay fixed.
Consumer9d844d84 banks the pin/docs after tools518e1ab; all14 post-bank checks
pass72.663s. The incremental build is up to date, all18 production hashes remain
fixed, and the graph worker completes at41,002 nodes/81,163 edges without force.

Texture vertex-span compiler phase narrowed; still NOT installed/exact:
[Note 1382](WORKING_NOTES/1382-texture-vertex-span-optimizer-allocation-and-controlflow-traces-20261015.md).
Screen60 more complete forms/profile controls; none improves HOMES339 words/
frame0xA8/258 differences. Fresh unchanged-code CFE/UOPT/UGEN captures prove
maximumA3/countT0 and the unallocated end tag already differ before final UGEN
scheduling. Mode5 supplies32 variables/51 integer constraints, not valid numeric
timings. All11 selected checks pass50.484s, including15 effective capture
controls and preceding installed-image gates. Bank tools a01819f first; all18
production hashes,801 archive fingerprints and573 older mirror fingerprints
remain fixed. README/metrics are unchanged. Continue THIS scanner's optimizer
lifetime/value-use shape; no new C match, host operation or Release change.
Consumer afd9582b banks the pin/docs after tools a01819f; all11 post-bank
checks pass64.655s. The incremental ELF/progress build is up to date, all18
production hashes remain fixed, and the incremental graph worker completes
at40,992 nodes/81,153 edges without forcing the smaller full scan.

Texture vertex-span real homes recovered privately; still NOT installed/exact:
[Note 1381](WORKING_NOTES/1381-texture-vertex-span-real-home-recovery-and-fit-screens-20261015.md).
Reorder existing locals to recover extentSP+A0, indicesSP+58 and vertexBaseSP+94
in func_1510BF60, keeping339 words/frame0xA8 and executable statements unchanged.
All18 guest private-home aliases now match retail; the previous draft fails
all18. Raw differences fall259->258, but full private state and55/63 prefixes
still differ. Compile102 bounded fitting forms/controls; one tool-free advisory
is independently tested and yields no matching fix. Keep production metrics,
README and all18 production inputs unchanged. Continue this SAME function's
register roles/control flow, preserving archive/mirror and frozen Release.
All16 final selected checks pass53.618s after correcting the receipt-input
collision; shared/standalone checks pass. Bank tools474ff2c first, preserving
all801 archive hashes and570 older mirror fingerprints.
Consumer b3975451 banks the pin/docs; all8 selected post-bank checks pass24.397s.
The incremental build is up to date, all18 production hashes remain fixed and
the graph worker completes at40,981 nodes/81,142 edges without a forced scan.

Private texture-selected vertex-span reconstruction; NOT installed or exact:
[Note 1380](WORKING_NOTES/1380-texture-vertex-span-reconstruction-and-private-boundary-20261015.md).
Audit all339 words of func_1510BF60 and its original direct callers. The archive
leaves it in assembly, so no C donor is imported. Reconstruct its full scanner,
backward cursor and nested texture behavior in private C. Screen23 forms;
the selected339-word/frame0xA8 draft still differs at259 words and private homes.
Pass14 selected checks43.598s:3,872 guest cases,336 reachable retail words,
1,936 native cases/profile,48 guest/24 native output aliases and seven effective
compiled controls. Retain the native maybe-uninitialized warning and defined-
input boundary;56/63 fired prefixes and full private state still differ.
All18 production input hashes, all801 archive files and565 older mirror
fingerprints remain fixed. Production totals and root README are unchanged:
Game2,884/4,829, total3,557/5,502, different1,945, zero drift. Continue THIS
function's homes/registers/scheduling before installation; keep the full source/
Game/rectangle and actual hardware/caller/loading/gameplay boundaries open.
Tools1ffbc44 banks the five owned research paths before the consumer pin/docs.
Consumer2f46d35a banks the pin/docs; all7 selected post-bank checks pass28.561s.
The incremental build is up to date, all18 production hashes remain fixed and
the graph worker finishes at40,970 nodes/81,131 edges without a forced scan.

View matrix pass recovered with its original product dependency:
[Note 1379](WORKING_NOTES/1379-view-matrix-pass-and-product-kernel-restoration-20261015.md).
Recover func_1510B690's 73-word/frame0x90 C body with twenty closed GPR-role
guards, its signed16 loop, live page/base/count reloads and proper matrix order.
Restore func_150A7A48's original 78-word assembly slot from a false C stub;
this dependency restoration is not new C credit. Qualify actual SDK decoder,
product and frustum connections, ordered overlaps, native32, signed-wrap tail
states and effective semantic controls. Keep the native signaling-NaN ABI
witness separate from target hardware/FCSR behavior. The complete 506-byte
ELF delta is two code slots and their extents only, with no metadata allowances;
all 189,088 protected bytes/720 owners remain fixed. ELF2131709f, progress
3ad7466c. Fresh Game2,884/4,829 (59.72%), total3,557/5,502 (64.65%),
different1,945, zero drift. Converted counts fall by one/312 bytes because the
product kernel is correctly classified asm. Preserve all 801 archive hashes
and 557 unrelated mirror fingerprints. Continue func_1510BF60; broader source/
Game/rectangle and hardware/caller/gameplay acceptance remain open. All 55
selected target/history checks pass157.389s; shared and standalone tools checks
pass. Toolsc526e84 precedes consumer af045628. All15 selected post-bank gates
pass53.835s, the incremental build is up to date, and all six installed hashes
remain fixed. The graph worker finishes at40,958 nodes/81,119 edges without a
forced smaller scan. No host operation; Release remains frozen.

Previous view near/far command and clipping queue recovered and byte-exact:
[Note 1378](WORKING_NOTES/1378-view-clipping-command-and-queue-reconstruction-20261014.md).
Recover func_1510B458 directly across49 words/frame0x28, including signed-zero
defaults and three live entry homes. Recover func_1510B51C across55 words/
frame0x40 with seven complete FP-register-role guards, live count/base loads,
sentinel skips and post-call consumption. Name private view+84 matrixScale
without changing view size or shared headers/profiles. Pass13 pre-install
checks32.850s,4,880 guest cases,1,600 fired prefixes,180 native cases/profile,
nine effective compiled controls and180 actual matrix-child connections with
bounded SDK providers. All328 changed ELF bytes are target code/extents only;
no other code, metadata or protected data changes. ELF6c21a585, progress
e3ea336d. Fresh Game2,883/4,830 (59.69%), total3,556/5,503 (64.62%),
different1,947, zero drift; converted counts unchanged. Correct prior single-
target neighbor prose to13, matching receipts; this two-target batch preserves
12 neighbors. All50 selected target/history checks pass115.524s; shared and
standalone tools checks pass. Bank toolscfc5e4b first, retaining801 archive
hashes and551 unrelated mirror fingerprints. Consumer48610539 banks both
recoveries/guards/pin/docs. All12 selected post-bank checks pass44.011s; the
incremental ELF/progress are up to date with all four hashes fixed. Its graph
worker completes at40,948 nodes/81,118 edges without forcing a smaller scan.
Continue73-word
func_1510B690's matrix pass with full source/Game/rectangle and hardware/runtime
boundaries open. Archive/mirror work is preserved and host Release stays frozen.

Previous pending-view projection queue recovered and guarded byte-exact:
[Note 1377](WORKING_NOTES/1377-pending-view-queue-reconstruction-20261014.md).
Recover func_1510B3B0's complete42-word/frame0x38 void command. Preserve the
signed inclusive live count, -1.0f skip, typed five-word projection call,
call-then-consume order and unconditional dirty clear. Three expected-word
guards normalize only a closed argument-load/move cycle; no shared-header or
profile changes. Pass4,704 guest cases,2,052 fired prefixes,2,352 native cases
per O2/O0 profile and six effective controls under both compilers;96 cases
connect the actual queue/parent/child with bounded trig/SDK helpers. All132
ELF byte changes are target-slot/extent-only, with no metadata changes.
All189,088 protected bytes/720 owners and all old guard/progress bytes remain
fixed. ELF307dae85, progress e3ea336d. Game2,881/4,830 (59.65%), total3,554/5,503
(64.58%), different1,949, zero drift. Original1501878C is still a production
placeholder, not complete caller/gameplay acceptance. Continue49-word
func_1510B458, then its clipping queue, with full source/Game/rectangle work
active and host Release frozen. All44 selected target/SDK/history checks pass
107.136s; shared and standalone checks pass. Bank tools64a6bda first, preserving
all801 archive hashes and545 unrelated mirror fingerprints. Prior Note1376's
106-check receipt is reused only for unchanged non-target behavior, not claimed
as a fresh broad run. Consumer f520037c banks source/guards/pin/docs; all9
selected post-bank checks pass35.556s. Incremental ELF/progress are up to date
with all four installed hashes fixed. The incremental graph worker completes
at40,938 nodes/81,101 edges without forcing the smaller full scan.

Previous view orthographic setup directly matched from semantic C:
[Note 1376](WORKING_NOTES/1376-view-orthographic-setup-reconstruction-20261014.md).
Recover func_1510B070's46-word/frame0x28 body, retaining its unused incoming
argument home, signed16 defaults, far reload and typed eight-word matrix call.
The simplest source emits all46 words directly, with zero guards or profile/
header changes. Twenty complete forms include four exact forms; all thirteen
raw owner neighbors/pools/relocations remain fixed. Pass10 pre-install checks
21.326s and three installed image/negative/inverse gates12.008s. Cover2,052
guest cases,272 fired prefixes and1,056 native32 cases per O2/O0 profile,
including the actual SDK C bodies; four semantic controls fail under both
IDO and native32. Freshly compiled210-word SDK chains pass96 connected cases
in a finite exact-conversion domain. The full219-byte ELF delta is confined
to155 target bytes, one12->184 extent byte and three checked symbol/string
groups. All189,088 protected bytes/720 owners and all guards/progress rows
remain fixed. ELF ebe9dc50, progress e3ea336d. Game2,880/4,830 (59.63%),
total3,553/5,503 (64.56%), different1,950, zero drift; converted counts unchanged.
Original init/scene callers remain production placeholders, so this is not
working gameplay/camera or full hardware/FCSR acceptance. Next continue42-word
func_1510B3B0's pending-view queue and the full source/Game/rectangle work.
All106 selected target/SDK/caller/history checks pass201.247s, with shared and
standalone tools checks also passing. Tools5e0f509 is banked first;801 archive
hashes and538 unrelated mirror fingerprints are preserved. No host operation.
Consumer edf88a28 banks the C source/pin/docs. All28 selected post-bank checks
pass68.438s; the incremental build is up to date and all four installed
checkpoint hashes remain fixed. Its incremental graph worker completes at
40,928 nodes/81,091 edges without forcing the smaller full scan.

Previous original fixed-matrix converter restoration and C ownership correction:
[Note 1375](WORKING_NOTES/1375-original-fixed-matrix-converter-ownership-and-rounding-restoration-20261014.md).
guMtxF2L's old C equals the separate guMtxF2L2's64 retail words and truncates
where this slot follows current rounding. Restore the original115-instruction/
116-word assembly slot without guards. All382 changed ELF bytes are confined
to381 slot bytes and one256->464-byte extent byte; all other instructions,
definitions, protected data, callers, headers, profiles and guards stay fixed.
Pass16 installed/chain checks29.267s, with384 rounding cases,128 overlaps,
576 fired prefixes and432 actual projection-family/converter connections.
Native32 independently witnesses the old C mismatch across192 cases/profile
at O2/O0; it does not execute MIPS or prove N64 FCSR flags/traps. Current
ELF7328baa3/progress e3ea336d. C exact counts remain3,552 total/2,879 Game:
the corrected denominators are5,503/4,830, different1,951, zero drift. This is
not new C-match credit. Converted totals are5,503/6,044 (91.05%),86.07% bytes;
Game4,830/5,323 (90.74%),85.44% bytes. Next ordinary C target is46-word
func_1510B070's clipping/orthographic setup, with full source/Game and separate
rectangle queues still active. Keep host Release frozen.
All93 selected target/history/caller checks pass166.231s, including the
corrected historical CSV comparisons and their corruption/capture controls.
Tools0bc11d9 is banked first; all801 archive hashes and531 unrelated mirror
fingerprints are preserved. Actual hardware/FCSR/rendering remains separate.
Consumer b2f95045 banks the tracked assembly/source/pin. All28 selected
post-bank checks pass40.120s; a fresh audit retains the116-word restoration
and exact four checkpoint hashes. Incremental ELF/progress are up to date,
and the graph worker completes at40,918 nodes/81,081 edges without forcing
the smaller full scan.

Previous view projection family installation and independent image qualification:
[Note 1374](WORKING_NOTES/1374-view-projection-family-matrix-child-and-native-qualification-20261014.md).
Recover func_1510B128's129-word command and func_1510B5F8's38-word matrix
child, retaining their original frames and typed void interfaces. Explicit
sine sequencing fixes a real native callback-order issue. Twenty-three parent
guards and two commutative child guards close the complete retail slots;
the33-word wrapper emits directly and its eight obsolete guards are removed.
Pass16 installed/focused checks21.768s, including216 native32 cases per O2/O0,
128 child cases,324 actual family connections, two field aliases and86 fired
prefixes. The independent whole-image gate confines all594 changed ELF bytes
to the two slots/extents and four exact local symbol/string permutations;
189,088 protected data bytes/720 owners remain exact. Current ELF03db1e76,
progress005fd768; Game2,879/4,831 (59.59%), total3,552/5,504 (64.53%),
different1,952, zero drift. Existing guMtxF2L still has114 differences in116
words; SDK packet mocks are not matrix, camera, pixel or gameplay acceptance.
Continue that dependency and wider donor/binding/codec/Game queues, retaining
the separate rectangle history boundary and frozen host Release.
All78 selected target/history checks pass146.606s; four strengthened native/
in-file corruption checks pass19.139s. Toolsefe2ace is banked first,801 archive
hashes are fixed, and the exact mirror sync preserves528 unrelated dirty files.
Consumer e1b67fe8 banks the source/pin. All26 selected post-bank checks pass
69.408s, the incremental build retains the pinned ELF/progress, and the graph
worker completes at40,907 nodes/81,082 edges without a forced smaller scan.

Previous view projection command private guarded word fit, not installed then:
[Note 1373](WORKING_NOTES/1373-view-projection-command-lifetime-and-product-fitting-20261014.md).
Improve func_1510B128 from41 to19 raw differences with the same129 words/
frame0x50. Reversed outer product presentation recovers the literal FP sequence;
a real cosine copy restores the sharedSP+0x3C home. The private19-word recipe
uses15 closed scheduling atoms, two symmetric equality comparisons and two
branch-likely delay-fill words; no frame/math/home guard or omitted word.
Both padders and independent original/rebased links yield all129 retail words.
Pass13 focused checks38.664s, including1,080 original/raw/guarded return-state
cases,662 fired prefixes with state/PC/delay identity, real trig and actual
wrapper connections, all19 expected-word corruptions and immutable inputs.
All141 focused screens complete; no raw match. Production/guards/ELF/progress
remain fixed, so no new match credit or README aggregate change. Toolsb208c1a
first; preserve801 archive files and526 unrelated mirror fingerprints. Next:
native32/broader aliases and actual func_1510B5F8's38-word matrix child, then
integrated ABI/guard/closed-image/history qualification before installation.
Keep hardware/FCSR/camera/gameplay and the wider source/Game goal open.
Consumerfb3009e3 banks the checkpoint; all seven post-bank checks pass9.289s.
Incremental build retains f36703ce/005fd768 and the source graph worker
completes at40,895 nodes/81,075 edges, without forcing the smaller full scan.

Previous view projection command private recovery, not installed:
[Note 1372](WORKING_NOTES/1372-view-projection-command-reconstruction-20261014.md).
The archive has no C donor for func_1510B128. Screen 130 complete source forms;
retain homes-1-0-2 at 129 words/frame0x50/41 differences, all real locals.
Pass 13 focused checks in 15.678s: 1,080 paired public-state cases, six
connected recovered-trig cases, 18 actual-wrapper connections and three
effective compiled negatives. Full private/fault parity is explicitly false:
42/56 fired prefixes differ, first cut11 at PCs1510B184/188, GPR1 only,
memory/FPRs equal. Keep native32, broader aliases and matching gates open.
The typed wrapper emits all33 retail words directly, making its old eight
guards obsolete; production guards reject it as expected. Typing the still-
unrecovered matrix child also grows that stub12->28 bytes with four home stores.
Do not install this family yet or count a new match. All production inputs,
ELF f36703ce and progress005fd768 remain fixed. Tools07e0dd5 first, 801 archive
files and 523 unrelated mirror fingerprints preserved. Next continue the SAME
func_1510B128: recover the early coefficient-HI schedule, shared cosine home,
FP allocation/products and clip branch before integrated child/guard changes.
Full graph scan fails closed at19,098 vs40,873; never force it.
Consumer51602818 banks the private checkpoint. All four post-bank checks pass
2.568s, incremental build retains the pinned image/progress and the graph
worker completes at40,883 nodes/81,058 edges. No production match credit.
Subsequently close the private129-word guarded fit in Note1373; native/child/
integrated installation gates remain open, not another production match.

View FOV transfer guarded match:
[Note 1371](WORKING_NOTES/1371-view-fov-transfer-reconstruction-20261014.md).
Restore func_1501B0A0's 99-word/frame0x50 two-index body. All seven calls and
86 words emit directly; thirteen relocation-aware guards move one independent
coefficient load through the opening setup, preserving every instruction and
relocation atom. Ten neighbors, both padders and independent rebases agree.
All 65 selected target/history checks pass in 115.601s: 2,160 paired MIPS
cases, 528 fired root prefixes, 648 native32 cases per O2/O0 and 36 connected
cases using both recovered trig bodies. The angle helper and final command
remain bounded in these tests; func_1510B128's production body is still a stub.
Close the whole image to 329 target bytes, one 12-to396-byte extent and one
checked symbol/string permutation. All other bytes and protected data stay fixed.
Fresh Game 2,877/4,831 (59.55%), total 3,550/5,504 (64.50%), different 1,954,
drift 0; executable-only 3,410/5,364 (63.57%). Conversions remain 5,504/6,044.
Tools 7b6f51a first. Preserve 801 archive files and 516 unrelated mirror
fingerprints. Consumer db0141f6 banks the group; all 26 post-bank checks pass
in 56.618s. Incremental build retains f36703ce/005fd768 image/progress and the
source graph worker completes at 40,872 nodes/81,053 edges; no forced scan.
The separate stale
rectangle image gate remains open. Next: qualify func_1510B128's 129-word/
frame0x50 command, actual argument/return interface and callers before broad
interface changes. Continue all failed donor/binding/codec/original Game work.
No full caller, production-command, FCSR, gameplay or camera acceptance.

Previous Game single-precision cosine direct match:
[Note 1370](WORKING_NOTES/1370-game-single-precision-cosine-direct-match-20261014.md).
Restore all85 code words/three NOPs directly from typed float C, frame0,
no guards/profile/header changes. A separate absolute/reduction copy and
distinct comparison zero-literal types retain the exact retail schedule.
All53 focused/history checks pass85.827s, including13,392 MIPS cases,280
fired prefixes,6,696 native32 cases per O2/O0 profile, five effective controls
and48 connected frustum cases with both recovered trig bodies. Closed-image
proof accounts for258 target bytes,20-to340-byte extent and two checked
symbol/string groups; every other byte and non-target definitions/data fixed.
Fresh Game2,876/4,831 (59.53%), total3,549/5,504 (64.48%), different1,955,
drift0; executable-only3,409/5,364 (63.55%). Conversions remain5,504/6,044.
Tools2a1c847 qualifies recovery;98db41f clarifies retained sine provenance.
Consumer f71d2c96 banks the source; all30 post-bank checks pass41.855s and
incremental build retains b87dd5bc/005fd768 image/progress hashes. The source
graph worker completes at40,861 nodes/81,042 edges. Receipt-only820566f makes
non-target definition preservation explicit; its fresh image gate passes2.114s.
Preserve801 archive files and513 unrelated mirror fingerprints. Never force
the smaller full graph scan. The old rectangle literal-image gate stays open.
func_1501B0A0 subsequently completed in Note1371 with thirteen closed prologue
guards; the final view command remains unfinished. No gameplay/FCSR/camera claim.

Previous Game single-precision sine direct match:
[Note 1369](WORKING_NOTES/1369-game-single-precision-sine-and-cosine-recovery-20261014.md).
Replace sinf's zero-return placeholder with104 directly matching words,
frame0, no guards/profile changes. Close the image to316 target bytes, its
20-to416-byte extent, six newly typed symbols and two exact adjacent symbol
permutations; every other ELF byte/data/header/progress/Makefile is fixed.
All42 focused/history checks pass66.813s:6,696 MIPS cases,96 fired prefixes,
3,348 native32 cases per O2/O0 profile, effective controls and48 connected
frustum cases using actual sine plus separately identified retail cosine.
The native return-only probe proves i386 x87 quiets7F810000 to7FC10000;
MIPS still requires the exact retail NaN word. No FCSR/runtime acceptance.
Fresh Game2,875/4,831 (59.51%), total3,548/5,504 (64.46%), different1,956,
drift0; executable-only3,408/5,364 (63.53%). Conversions remain5,504/6,044.
Tools c293b24 first. Preserve801 archive files and509 unrelated mirror
fingerprints. Full graph scan fails closed; never force the smaller graph.
Consumer d1a326eb banks the group. All19 post-bank checks pass38.973s;
incremental build retains e7966de8/005fd768 image/progress hashes. The source
graph worker completes at40,850 nodes/81,030 edges, without a forced scan.
Cosine subsequently completed in Note1370. Its earlier unmatched screens are
retained; the old rectangle image gate remains open.

Previous view frustum side-plane guarded match:
[Note 1368](WORKING_NOTES/1368-view-frustum-side-plane-guarded-match-20261014.md).
Restore func_1501B22C's typed void/signed-index body:59 code words plus two
alignment NOPs, frame0x40, four checked disjoint phase-home coalescing guards.
Preserve10 neighbors, zero owner warnings, every ELF byte except190 target
bytes and one12-to236-byte extent; all progress/headers/Makefile/data fixed.
Pass11 target/capture checks18.866s and28 affected history/behavior checks
45.466s, with7,680 MIPS cases,1,116 fired prefixes and896 native32 cases per
O2/O0 profile. Fresh Game2,874/4,831 (59.49%), total3,547/5,504 (64.44%),
different1,957, drift0; executable-only total3,407/5,364 (63.52%). Conversions
remain5,504/6,044. Preserve801 archive files and502 unrelated mirror paths.
Tools46da39b first, no push or host/Release work. One old rectangle whole-image
gate is confirmed stale on the pre-frustum baseline too; preserve its old
snapshot and reconcile history separately, not a claim that all old tests pass.
Consumer5a74421f banks the group; all16 post-bank checks pass33.090s. The
incremental build retains the79eb4f32 image and005fd768 progress; the source
graph worker completes at40,838 nodes/81,017 edges, without forcing the scan.
Sine subsequently completed in Note1369; Game cosine remains open.
Init's __sinf is a distinct double-precision implementation. No retail
trig accuracy, FCSR, complete camera/culling or gameplay acceptance is claimed.

Record payload constructor direct match:
[Note 1367](WORKING_NOTES/1367-record-payload-constructor-direct-match-20261014.md).
Convert func_1513C350 from assembly/commented draft to 103 directly emitted
words, frame 0x38, zero guards or profile changes. A three-word structure
assignment removes four register differences; preserve its public prototype,
all 58 neighbors, shared headers, guards, Makefile and complete ELF bytes.
Only one progress language field changes. Pass 12 target/capture checks
19.764s and 20 affected historical/control checks21.583s+5.177s, including
4,320 MIPS cases,208 fired fault prefixes and1,944 native32 cases per O2/O0.
Fresh Game2,873/4,831 (59.47%), total3,546/5,504 (64.43%), different1,958,
drift0. Converted5,504/6,044 (91.07%),86.09% bytes; Game4,831/5,323
(90.76%),85.46% bytes. Executable-only total3,406/5,364 (63.50%).
All801 archive files and499 unrelated mirror fingerprints stay fixed;
tools4e667db first, with no push or host/Release work. Keep the owner family's
43 inherited compiler warnings unchanged, not a warning-free build claim.
Consumere1f955a6 banks the group; all16 post-bank checks pass27.177s. The
incremental build retains the identical ELF and pinned005fd768 progress;
the source graph worker completes at40,826 nodes/81,005 edges, without force.
Next: qualify func_1501B22C's61-word slot (prior59-word/four-difference
draft) and continue failed-body/interface/binding queues and original Game
matching. Layer decoder func_151F78B4 and func_151F63C4 remain unrecovered.

Codec frame dispatcher guarded match:
[Note 1366](WORKING_NOTES/1366-codec-frame-dispatch-guarded-match-20261014.md).
Restore func_151F86B0's full 112-word slot: 109 code words plus three retail
alignment NOPs, frame 0x130. Use typed buffer/count outputs, the existing
32-bit reader interface and one additional retail-g selection. Six checked
guards cover one commutative addition and a closed t0/t2 allocation exchange.
Preserve 12 neighbors under both profiles and every ELF byte except 332 slot
bytes and one symbol extent. All progress/data/overflow remains fixed.
All 113 regression checks pass in 193.589s, including 1,800 MIPS cases,
199 fired root-fault prefixes and 1,500 native32 cases per O2/O0 profile.
Fresh Game 2,872/4,830 (59.46%), total 3,545/5,503 (64.42%), different 1,958,
zero drift. Executable-only total 3,405/5,363 (63.49%); conversion stays
5,503/6,044. Preserve all 801 archive files and 497 unrelated mirror paths.
Tools a337e52 first; no push or host/Release operation. The called layer
decoder func_151F78B4 and its dependency func_151F63C4 remain zero stubs.
Consumer5e41123d banks the group; all16 corrected post-bank selectors pass
33.113s. The incremental build retains the c9ff4e7e image and unchanged
progress, and the source graph worker completes at40,812 nodes/81,004 edges.
Next: qualify func_1513C350's103-word/frame0x38 draft (four prior screen
differences), then the larger layer-decoder dependencies and remaining
failed-interface/binding queues. No matching credit for these uninstalled drafts.

Codec input refill guarded match:
[Note 1365](WORKING_NOTES/1365-codec-input-refill-guarded-match-20261014.md).
Replace func_151F7F60's zero-return placeholder with74 words/frame0x20,
using the existing32-bit reader interface, retail-g selection and one
commutative-add guard. Preserve12 neighbors under both profiles, all data/
overflow/progress, and every ELF byte except239 slot bytes and one extent.
Pass1,680 MIPS cases,177 fired fault prefixes and1,680 native32 cases per
O2/O0 profile. All101 final checks pass161.042s; retain the intermediate
source fixture and independently pin the final typed owner. Fresh Game2,871/
4,830 (59.44%), total3,544/5,503 (64.40%), different1,959, zero drift.
Executable-only total3,404/5,363; conversions remain5,503/6,044. Archive801
and492 unrelated mirror fingerprints stay fixed; no host or Release work.
Next: qualify func_151F86B0's112-word slot (retained109-word/six-difference
draft), and continue the failed-interface/binding and original Game backlog.
Consumerf9dcbae0 banks the group;16 post-bank checks pass68.142s. The incremental
build retains the pinned image/progress, and the source graph worker completes
at40,801 nodes/80,987 edges without forcing the partial scan.

Commented-source audit and guarded object-notification recovery:
[Note 1364](WORKING_NOTES/1364-commented-source-audit-and-object-notification-match-20261014.md).
Inventory353 commented records in95 files; attempt147 remaining drafts,
compile88 bodies under five IDO profiles and screen440 objects. Zero new raw
exact donors;59 compile failures and three symbol/pool gaps remain explicit.
Recover func_15063168:59 words, two independent schedule guards,88 unchanged
owner neighbors. The complete rebuilt ELF remains bbc20157 byte-for-byte;
only two guard rows and one generated C-language field change. All89 final
checks pass134.522s,31 mirror discovery checks and project tools checks pass.
Fresh Game2,870/4,830 (59.42%), total3,543/5,503 (64.38%), different1,960,
drift0; conversion5,503/6,044 (91.05%). Executable-only total3,403/5,363.
All33 earlier raw donor imports remain banked; this guarded recovery is separate.
All801 archive files and478 unrelated mirror fingerprints remain unchanged.
Next: qualify the74-word func_151F7F60 buffer refill (one commutative-add word),
then continue actual failed-body/interface recovery and func_151F4F38 matching.
Host has a generated notification implementation; no transfer/build/Release work.
Consumer7b1d1051 banks the group;12 post-bank checks pass36.349s. The incremental
build remains up to date with the same ELF/progress, and the source commit's
graph worker completes at40,790 nodes/80,977 edges without forcing the partial scan.

Failed-file isolation and two more exact C recoveries:
[Note 1363](WORKING_NOTES/1363-failed-source-function-isolation-and-two-exact-recoveries-20261014.md).
Attempt all1,143 actual definitions in the58 failed files:719 compile with
every unrelated interface retained; a used-interface-preserving retry rescues
325 more. Screen all1,044 objects, qualify/install func_150F0938 (59 words) and
func_150B003C (22), with no new guards and60 unchanged owner neighbors. Only
185 Game bytes and the preset wrapper's extent change; the category routine
preserves its original assembly bytes and becomes C. All data/overflow/guard/
Makefile bytes remain fixed, with one language row updated. All69 final checks
pass135.858s; mirror18 discovery checks and project tools checks also pass.
Fresh Game2,869/4,829 (59.41%), total3,542/5,502 (64.38%), different1,960,
drift0; conversion5,502/6,044 (91.03%). Executable-only total3,402/5,362;
Debugger remains41 real functions plus140 labels in the legacy aggregate.
Correct spaced multiple-pointer returns: the inventory now finds4,104 lexical
definitions, without changing source or adding credit for discovery. All33
individually qualified donors are installed. Current successful-object queues
are zero;99 individual compile failures and39 cumulative unresolved symbol/
pool/pseudo-operation cases remain open. Continue actual body/used-interface
reconstruction and original Game matching, including func_151F4F38's101 word differences.
Keep the preset helper func_15160A58's unrecovered placeholder separate: its
caller is matched, not the helper. Host func_150F0938 still selects a zero stub;
func_150B003C has a generated implementation. No host transfer/build/Release work.
Consumer7183fa58 banks the group;12 post-bank checks pass15.816s, the incremental
build retains the bbc20157 image and its graph worker completes at40,778 nodes/
80,966 edges. The survey recognizes296 commented draft headers across87 files,
not296 compilable routines; investigate balanced definitions and current exact
coverage next, alongside the99 real compile failures and original Game matching.

Whole-source draft scan and nine more exact recoveries:
[Note 1362](WORKING_NOTES/1362-whole-source-draft-audit-and-nine-exact-recoveries-20261014.md).
Inventory all558 C files, including291 previously uncompiled Game drafts.
Compile233 of291; qualify/install allnine newly found candidates across444
retail words, no new guards,97 unchanged owner neighbors. Keep the two factory
forwarders in an isolated translation unit so the unrecovered factory stays
unchanged. Full linked changes are confined to nine slots (1,204 changed bytes);
overflow and all189,088 protected data bytes remain fixed. Only two language
rows become C. Fresh Game2,867/4,828 (59.38%), total3,540/5,501 (64.35%),
different1,961, drift0; conversion5,501/6,044 (91.02%). Executable-only matching
is3,400/5,361; legacy Debugger still includes140 data labels.
The earlier22-function queue covered linked C only; these nine come from the
wider draft scan. The58 file-level compile failures and24 binding gaps remain
unqualified, not rejected wholesale. Continue per-function isolation/pool
binding and original Game matching. func_151F4F38's best draft has533 words,
frame0x38 and101 differences; ten fresh screens do not yield an exact match.
Six new targets are still selected zero stubs in the separate host; no host
transfer/build or frozen Release operation is authorized by this decomp work.
All50 final focused regression checks pass101.919s; both standalone mirror
padder modules pass. All801 source-archive files and471 unrelated mirror
fingerprints remain unchanged. Tools1a87cc3 is banked before the consumer pin.
The post-install draft screen has606 already exact C definitions, zero new
immediately usable word candidates; failed files/bindings remain open.
Consumercf293d90 banks this group; ten post-bank checks pass141.653s and the
incremental build retains the pinned image. Its graph worker completes at
40,765 nodes/80,973 edges without forcing a smaller full scan. A477-word
func_151C4B0C draft is not a donor: its three copy placeholders must become
actual retail inline copies, not guessed memcpy call bindings.

All remaining qualified donor recoveries:
[Note 1361](WORKING_NOTES/1361-all-remaining-byte-exact-donor-recoveries-20261014.md).
Install all 19 remaining applicable exact C donors: ten smaller Game routines
and nine streaming-audio routines, 4,117 words, zero new guards. All 742 owner
neighbors retain raw code/relocations/pools; protected data stays exact across
189,088 bytes and 720 owners. Select seven codec functions from retail -g
without changing the six O2 neighbors. Preserve retail names and add accurate
comments/local types; no shared-header merge. All 22 authorized donors are now
installed; fresh applicable linked-C donor queue is zero. The first 30 installed/history
checks pass 111.864s, followed by three effective compiled source controls.
Fresh Game 2,858/4,826 (59.22%), total 3,531/5,499 (64.21%), different 1,968,
drift zero; conversion counts remain fixed. Function-only total 3,391/5,359;
retain the separate legacy Debugger data-label counter caveat.
Resume original Game matching; adjacent func_151F4F38 is an independently
unmatched candidate, not a qualified donor. No host or frozen Release work.
Final five donor checks pass 27.386s after the pointer-return declaration;
normal rebuild and incremental recheck retain the pinned ELF. Tools249f8c3
are committed first; preserve all465 unrelated older-mirror fingerprints.
Consumer9eb367cf banks the recoveries; nine post-bank donor/audit checks pass
39.383s, project tool checks and older-mirror syntax checks also pass.

First authorized byte-exact donor group:
[Note 1360](WORKING_NOTES/1360-first-byte-exact-donor-conversions-20261014.md).
func_15125628/func_1507D158/func_151411E4 now emit26/32/27 retail words directly
from C, zero new guards. Preserve address-keyed exports, descriptive locals/
callback type and concise comments. Correct the old unsupported handwritten
timer claim. Qualify active ABI,74 owner neighbors,1,200 guest domains,30 fired
prefixes and65,536 native timer pairs per O2/O0 profile. All25 installed audit/
history checks pass47.390s; final nine donor checks12.526s include carry links.
The entire ELF and guard CSV stay byte-identical; only three rows become C.
Fresh Game2,839/4,826 (58.83%), total3,512/5,499 (63.87%), different1,987, drift0.
At that checkpoint nineteen candidates remained; all are completed in Note1361.
Toolsfb5470e were banked first.
Consumere68c9494 banks the group; seven post-bank checks pass10.249s.
No broad header merge, supplied-archive edit, host build or frozen Release work.

Alternative source audit, performed after the function bank:
[Note 1359](WORKING_NOTES/1359-alternative-source-byte-match-audit-20261014.md).
Another Source/CBFD-Recompiled/conker remains preserved and all801 original files
are unchanged; only individually qualified C is adopted. Its disposable US reconstruction has1,478/1,478 executable C
slots byte-exact (Init241, Game1,217, Debugger20), with no guards or padding
exception. Whole text2,256,728 bytes also matches, including original assembly.
Ordinary linking fails on generated rodata labels; the diagnostic ELF is not a
working/runnable build. Track22 exact individual C candidates, not a wholesale
import. The user authorizes function-by-function use of verified exact C;
the first three conversions are installed in Note1360 after the audit bank.
Counting caveat: legacy Debugger181/181 includes140 data labels. Function-only
main counts at the audit bank were41/41 Debugger and3,369/5,356 total; legacy counters are retained
pending a separate correction. The detailed audit separates these definitions.

Installed actor threshold flags checkpoint:
[Note 1358](WORKING_NOTES/1358-game-actor-threshold-flags-guarded-match-20261014.md).
func_151A77C0 matches all47 words with no frame through complete semantic C
and26 guarded allocation/scheduling words. Both clock relocations stay fixed.
All86 installed regression checks pass259.248s; tools166a171 are banked first.
Retain640 guest cases,819 fired access-prefix pairs,40 public clock aliases,
six effective semantic controls and524,288 native cases per O2/O0 profile.
Only132 ELF bytes change:131 instructions and one size byte. Append exactly
3,926 guard bytes; all720 data owners, six neighbors and converted rows stay fixed.
Fresh Game2,836/4,823 (58.80%), total3,509/5,496 (63.85%), different1,987, drift0.
After the function commit, audit Another Source/CBFD-Recompiled/conker read-only.
It is another source only; no import/adoption decision has been made.
The independently dirty PC-port copy remains a placeholder; no host Release work.

Installed actor effect packet checkpoint:
[Note 1357](WORKING_NOTES/1357-game-actor-effect-packet-guarded-match-20261014.md).
func_151A7610 matches all108 words/frame0x98 through semantic C and eight
closed F2/F12 guards, including a preserved world-coefficient LO16 relocation.
All77 checks pass232.619s; final10 effect checks pass11.706s after completing
the local signed-DIV HI model. Retain128 guest domains,376 root cuts,32 aliases,
96 native cases per O2/O0 and the actual157-word factory/11-word memcpy.
Only353 ELF bytes change, plus1,090 exact append-only guard bytes; all720 data
owners, six neighbors, layouts and converted rows remain fixed.
Fresh Game2,835/4,823 (58.78%), total3,508/5,496 (63.83%), different1,988, drift0.
Toolsfc195e3 first; next recover47-word leaf func_151A77C0 in this owner.
Consumer1b0135da banks the restoration; eight post-bank checks pass14.301s.
The sibling PC-port copy remains a placeholder in independently dirty source;
track a separate transfer/host task. No push or frozen Release work.

Installed actor burst contact checkpoint:
[Note 1356](WORKING_NOTES/1356-game-actor-burst-contact-direct-match-20261014.md).
func_151A743C matches all117 words/frame0x48 directly from C, zero guards.
All67 checks pass234.138s, including7,680 guest domains,680 fired root cuts,
64 aliases,1,920 native32 cases per O2/O0 profile and full prior regressions.
Exactly358 ELF bytes change:356 instructions and two function-size bytes.
No serialization, guard, data, conversion, layout or neighbor changes.
Fresh Game2,834/4,823 (58.76%), total3,507/5,496 (63.81%), different1,989, drift0.
Toolsbb793d8 first; next recover108-word/frame0x98 func_151A7610 in this owner.
The wider Game goal remains active. No push or frozen host Release work.
Consumera39ab592 is banked; seven post-bank checks pass10.729s. The PC port's
generated callback still returns zero; keep its independently dirty source
unchanged and track a separate transfer/host-qualification task in Note1356.

Installed actor burst consumer checkpoint:
[Note 1355](WORKING_NOTES/1355-game-actor-burst-consumer-guarded-match-20261014.md).
func_151A6F00 matches all315 words/frame0x168 through semantic C and ten exact
guards: two restored idle slots, their store/branch swaps and branch distances.
All40 installed checks pass124.436s, including4,080 root cuts,168 alias prefixes,
both real padders/carry links and full producer/native regressions. Exactly1,048
ELF bytes are accounted:988 instructions, two size bytes and58 asserted symbol/
string bytes. All other image/data/history/converted rows remain fixed.
Fresh Game2,833/4,823 (58.74%), total3,506/5,496 (63.79%), different1,990, drift0.
Toolseb93e2e first; next recover the117-word func_151A743C in this same owner.
Consumere4b8e39a banks the checkpoint; seven fresh post-bank checks pass28.068s
with all installed hashes fixed. The incremental graph hook completes40,669
nodes/81,150 edges without a remaining worker; no push or host Release work.

Installed actor burst packet checkpoint:
[Note 1352](WORKING_NOTES/1352-game-actor-burst-packet-direct-match-20261014.md).
func_1506A5F0 matches all67 words/frame0x78 directly from C, zero guards. Keep
the0x5C packet,14 untouched holes, six raw coefficients and typed integer-zero
assignment. All18 installed checks pass100.732s:10,800 guest/108 alias cases,
1,404 fired cuts, native32 O2/O0 and original315-word consumer/table0/memcpy.
Exactly292 ELF bytes are accounted, including three asserted symbol/string
permutations; all other data/history/layouts stay fixed. Fresh Game2,832/4,823
(58.72%), total3,505/5,496 (63.77%), different1,991, drift0. Tools23e45f5 first.
No zero-return placeholders remain in this owner; next recover the still-stubbed
func_151A6F00 beyond the bounded mode1 test domain.
Consumerb3df40d1 banks this checkpoint; seven fresh post-bank checks pass14.316s.
All installed hashes and all459 post-update older-mirror fingerprints remain
fixed. The incremental graph hook finishes40,637 nodes/81,116 edges with no
worker; no push or frozen host Release work.

Installed mode1 actor/vector snapshot checkpoint:
[Note 1351](WORKING_NOTES/1351-game-actor-vector-mode1-direct-match-20261013.md).
func_1506A968 matches all40 words/frame0x38 directly from C, zero guards. Keep
raw coordinates, private arrays, global differences and the kind1 JAL delay.
All17 installed checks pass37.209s:11,904 guest/60 alias cases,792 fired cuts,
native32 O2/O0 and original dispatcher/table7. Shared mode0 regression passes
with restored source binding. Only123 code bytes and one size byte change;
all other ELF/data/guards/profiles/layouts/conversion rows stay fixed. Fresh
Game2,831/4,823 (58.70%), total3,504/5,496 (63.76%), different1,992, drift0.
Tools7f557cd first; next func_1506A5F0's mixed packet and global coefficients.
Consumer7d6700c9 banks this checkpoint; seven fresh post-bank checks pass6.066s.
All installed hashes and the older mirror's452 untouched initial fingerprints
remain fixed. The incremental graph hook finishes40,626 nodes/81,105 edges
with no worker; no push or frozen host Release work.

Installed actor descriptor/coordinate spawn checkpoint:
[Note 1350](WORKING_NOTES/1350-game-actor-descriptor-spawn-direct-match-20261013.md).
func_1506A864 matches all65 words/frame0x60 directly from C, zero guards. Reuse
the SDK Header/Header2, retain signed truncation, untouched pad5 and eleven-slot
factory/copy flow. All16 installed checks pass61.688s:20,736 guest/216 alias
cases,1,944 fired cuts, native O2/O0 and real factory/wrapper/memcpy/parent paths.
The whole image accounts for195 code bytes, two size bytes and39 exact symbol/
string serialization bytes, with unchanged named definitions otherwise. All
data/guards/profiles/layouts/conversion rows stay fixed. Fresh Game2,830/4,823
(58.68%), total3,503/5,496 (63.74%), different1,993, drift0. Tools6d54751 first;
next func_1506A968's mode1 actor/vector snapshot callback.
Consumer4d0bfbb9 banks this checkpoint; six fresh restart/post-bank checks
pass13.824s, and matching totals are reconfirmed. The incremental graph hook
finishes40,616 nodes/81,095 edges with no worker; all455 older-mirror
fingerprints remain unchanged. REA6.4.0 reconnects with Ghidra/Java readiness
confirmed; its documented Windows MIPS ELF limitation is not matching credit.

Installed actor/vector snapshot checkpoint:
[Note 1349](WORKING_NOTES/1349-game-actor-vector-snapshot-direct-match-20261013.md).
func_1506A79C matches all 40 words/frame0x38 directly from plain C, zero guards.
Preserve the raw actor copies, two private arrays and global-vector subtraction
order. All 16 installed checks pass in49.161s:11,904 guest/60 alias cases,792
fired cuts, native32 O2/O0 and original dispatcher/table4. Only122 target code
bytes and one size byte change; all other ELF/data/guards/profile/layout and
conversion rows stay fixed. Fresh Game2,829/4,823 (58.66%), total3,502/5,496
(63.72%), different1,994, drift0. Tools7222bfa first; next func_1506A864's
coordinate truncation, descriptor and conditional payload copy.
Consumer228f4e71 banks this checkpoint; six fresh post-bank checks pass5.469s,
with matching totals reconfirmed and all older-mirror fingerprints preserved.

Installed signed actor-mask scan checkpoint:
[Note 1348](WORKING_NOTES/1348-game-signed-actor-mask-scan-direct-match-20261013.md).
func_1506AAE0 matches all 39 words/frame 0x30 directly from plain C, zero guards.
Preserve the signed snapshot, every-bit actor stride and six-slot callback ABI.
All 15 installed checks pass in 67.757s: 33,688 positive cases, 64 signed-negative
prefixes, 1,200 fired cuts, native32 O2/O0 and original indirect dispatcher setup.
Only 131 target code bytes and one size byte change; all other ELF bytes/data,
guards/profile/layout/conversion rows stay fixed. Fresh Game 2,828/4,823 (58.64%),
total 3,501/5,496 (63.70%), different 1,995, drift 0. Tools 3d88555 first;
next func_1506A79C and its actor/vector snapshots and floating differences.
Consumer003a7a80 banks this checkpoint; six fresh post-bank checks pass 5.329s,
with matching totals reconfirmed and all older-mirror fingerprints preserved.

Installed actor/payload creator checkpoint:
[Note 1347](WORKING_NOTES/1347-game-actor-payload-creator-direct-match-20261013.md).
func_1506AA48 matches all38 words/frame0x48 directly from C, with zero guards.
Real local order recovers packet SP+0x34; retain nine-slot creation and all16
copied bytes, including untouched padding. All16 installed checks pass38.245s,
with6,400 guest/400 alias cases,1,728 fired cuts, native O2/O0 and real dispatch/
creator/memcpy execution. Only112 code bytes and one size byte change; all other
ELF bytes/data/guards/profile/layout/conversion rows stay fixed. Fresh Game2,827/
4,823 (58.61%), total3,500/5,496 (63.68%), different1,996, drift0. Tools3c7f8ca
first; next func_1506AAE0 and its signed mask/actor scan.
Consumer02787267 banks that checkpoint; six fresh post-bank checks pass4.884s,
with matching totals reconfirmed and the older tools mirror unchanged.

Installed matrix-translation checkpoint:
[Note 1346](WORKING_NOTES/1346-game-matrix-translation-guarded-byte-match-20261013.md).
func_15142314 matches all49 words/frame0 through34 source-derived scheduling
guards; the recovered C stays unchanged and raw34 differences remain explicit.
All17 installed checks pass91.981s, covering halfwords/aliases/native O2/O0,
the original parent,864 fired cuts, both owner padders and signed-low rebases.
Only104 target ELF bytes change; all symbol fields/data/source/profile/layout/
conversion rows stay fixed. Fresh Game2,826/4,823 (58.59%), total3,499/5,496
(63.66%), different1,997, drift0. Tools4e3cd4c first; next func_1506AA48.
Consumerff5a1244 banks the exact pin/guards/docs; six post-bank checks pass4.434s.
The first incremental hook completes40,575 nodes/81,062 edges with no worker.

Installed matrix-reflection checkpoint:
[Note 1345](WORKING_NOTES/1345-game-matrix-reflection-guarded-byte-match-20261013.md).
func_15034F30 now has its complete486-word C body/frame0x190 and238 source-derived
operand guards; raw C differs238 words, guarded body is retail-exact. All21
installed checks pass64.167s, including4,800 guest cases/10,260 fired cuts.
The whole ELF changes only its target slot and named size field12 ->1944;
1,465 bytes total, all protected data/profile/layout/conversion rows fixed.
Fresh Game2,825/4,823 (58.57%), total3,498/5,496 (63.65%), different1,998, drift0.
Tools5c4c157 first; older441 initial hashes fixed, two verified text pins and
three absent additions. Next func_15142314; the wider Game goal stays active.
Consumer23fa40a6 banks the exact pin/source/docs; six post-bank checks pass4.209s.
The first incremental graph hook finishes40,565 nodes/81,053 edges with no worker.

Current matrix-reflection original-prologue checkpoint:
[Note 1344](WORKING_NOTES/1344-game-matrix-reflection-original-prologue-recovery-20261013.md):
Direct identity call leaves the input formal unchanged and recovers all22
opening words, including the early s6 save/move. Candidate486/frame0x190,
259 ->240 differences,19 changed words; all later words stay fixed, uninstalled.
All26 checks pass75.233s. Across10,260 fired cuts, full modeled agreements grow
192 ->3,648 without loss; first mismatch moves cut1 ->19. Matrix addresses,
live homes, four shifts and all old controls survive. Frontend/UOPT M284/292
retain physical400. Tools579be6c first; all440 older hashes fixed/two additions.
Production/totals/root README unchanged. Next s4/s5 roles and later240 words.
Consumer5be301e1 banks the exact pin/docs; eight post-bank checks pass10.018s.
Incremental graph hook completes40,555 nodes/81,041 edges with no live workers.

Current SDK-typed matrix-reflection saved-index checkpoint:
[Note 1343](WORKING_NOTES/1343-game-matrix-reflection-sdk-typed-saved-index-recovery-20261013.md):
func_15034F30 remains uninstalled at486 words/frame0x190,331 ->259 differences,
125 changed words. Recover all four retail s2 shifts, s0 cursor/s1 matrix roles
and the actor's s0 pointer restoration; remove the extra advancing input cursor.
All25 checks pass99.151s. Against331,10,260 fired cuts retain192 prior modeled
agreements; the old eight lower329 rejection domains remain within48 current
rejections. Saved-store order, s4/s5 cache/offset roles and returnGPR9/14 stay
different. Production/totals/README fixed. Tools4efe06f first; all438 older hashes
preserved/two additions. Next remaining259 words and full private/linked fit.
Consumer481d38c3 banks the exact pin/docs; eight post-bank checks pass6.292s.
Incremental graph hook completes40,544 nodes/81,031 edges with no live workers.

Current matrix-reflection direct-home and cache-removal checkpoint:
[Note 1342](WORKING_NOTES/1342-game-matrix-reflection-direct-home-dispatch-and-cache-removal-20261013.md):
func_15034F30 remains uninstalled at486 words/frame0x190/331 differences.
Recover direct output-home loads, the missing live mode read, input bank s6
and flag roles; remove reflection's fp cache. Saved-store order and shifted
index are still wrong. All24 checks pass76.603s, retaining192 prior modeled
agreements over10,196 fired cuts. The inherited407 diagnostic stays distinct;
its eight lower329 rejection domains remain effective. Production/totals/root
README unchanged. Toolsaf0ed5c first; all436 older hashes preserved/two additions.
Restarted REA is connected; its Windows Ghidra adapter rejects MIPS ELF. See
[verified setup](REVERSE_ENGINEERING_SETUP.md). Next saved schedule/index/full fit.
Consumer85439397 banks the exact pin/docs; seven post-bank checks pass6.224s.
Incremental graph hook finishes40,533 nodes/81,029 edges with no live workers.

Current economical-index and conditional-home checkpoint:
[Note 1341](WORKING_NOTES/1341-game-matrix-reflection-economical-index-and-conditional-homes-20261013.md):
func_15034F30 best literal branch improves333 ->332,26 changed words, uninstalled.
A separate486/frame0x190/407 diagnostic restores guarded/tail output-home reads;
lower329 forms fail count gates.85 named forms expose equal-score/nonidentical
arrays. All22 diagnostic/text checks pass98.059s;10,196 fired cuts retain192
prior full modeled agreements, no new ones. Return witness9/12 remains different.
Address work is already lda P+16/ilod in CFE and UOPT. Production/totals/README
stay fixed; next direct home lowering without address work, then saved roles.
Tools6bd2222 first; consumer2cab99bf records the exact pin/docs. Five post-bank
checks pass24.736s; hook completes40,515 nodes/81,005 edges with no workers.
All434 older fingerprints remain fixed with only two newly added files.

Current matrix-reflection pointer-role and cache checkpoint:
[Note 1340](WORKING_NOTES/1340-game-matrix-reflection-pointer-roles-and-cache-provenance-20261013.md):
func_15034F30 remains uninstalled:486 words/frame0x190,347 ->333 differences,
21 changed words. Screen100 complete forms/19 eligible literal arrays; reject
a score344 lost-home-read form. Reflection's fp cache is already in UOPT.
6,912 fired common fault cuts preserve128/128 prior agreements, no new ones;
opening cut1 and returnGPR9/13 remain different. The ordinary flag initializer
is not an early snapshot; a compiled volatile control is an effective negative.
All19 target/text checks pass107.605s. Production/totals/root README stay fixed.
Next restore saved roles/index lifetime
and remaining333 words before installation. Full qualification/banking in note.
Toolsfb42981 is banked first; consumerf84a413b records the exact pin/docs.
Four post-bank checks pass3.938s. Incremental hook completes40,502 nodes/
80,993 edges with no workers; all432 older hashes stay fixed/two additions.

Current matrix-reflection candidate and private-buffer fit:
[Note 1339](WORKING_NOTES/1339-game-matrix-reflection-candidate-and-private-buffer-layout-20261013.md):
func_15034F30 has a complete uninstalled 19-slot candidate:486 words/frame0x190,
347 differences. Twenty initial forms restore the extent/homes;56 local
placements restore SP+0x84 without padding. Equal scores hide two changed words.
4,800 cases match complete sampled RAM/helper packets; caller windows, native32
controls, both owners/padders, three rebases and owned frame capture pass.
All17 target/text checks pass89.139s. Return GPR9/13 and fired fault cut1 remain
different; mixed-format provider result and full fault/hardware scope stay open.
Production source/ELF/guards/profile/progress and root README remain unchanged;
no credit. Toolsf3e8f92 first; older HEAD/all430 hashes fixed with two additions.
Consumer5a910345 records the exact pin/docs; three post-bank production/private/
fault checks pass2.325s. Incremental graph hook completes40,489 nodes/80,981 edges.
Continue this same routine's opening saved-role schedule and remaining347 words.

Current actor command-finalizer guarded match:
[Note 1338](WORKING_NOTES/1338-game-actor-command-finalizer-guarded-match-20261013.md):
func_15034860 matches all 405 words with its original frame 0x48. Semantic C
stays unchanged at 76 raw differences; 76 source-derived expected-word guards
normalize bounded schedules, scratch lifetimes and two commutative operands.
This is not a direct C match. All 18 pre-install tests pass, including 2,938
full modeled fault-state pairs and three independently linked carry layouts.
Installed audit changes 145 target bytes only; the entire remaining ELF and
189,088 bytes / 720 Game data owners are exact. Fresh matching: Game
2,824/4,823 (58.55%), total 3,497/5,496 (63.63%), drift 0, different 1,999.
Conversion counts unchanged. All 20 installed target/text checks pass in
117.798s; tools c0ca061 is banked first. Older HEAD/426 unrelated fingerprints
stay fixed; only its verified text-pin edit and three absent additions change.
Consumer 29770eeb banks the exact tools pin/guards/docs. Three post-bank image/
text checks pass4.869s. Next func_15034F30, 486 words / frame 0x190.
Direct graph update fails closed; the incremental commit hook then completes
at40,478 nodes/80,971 edges with retained history. No forced shrink or push.

Current actor command-finalizer category-cache diagnostic checkpoint:
[Note 1337](WORKING_NOTES/1337-game-actor-command-finalizer-category-promotion-cache-provenance-20261013.md):
Production stays405/frame0x48/76, all source/ELF/guard/profile/progress hashes
fixed.55 complete forms yield24 extent/opening-valid bodies in nine literal
families, no improvement; all retain1598/2938 sampled agreements. Three owned
captures preserve objects: baseline/mixed2 store dtype-L/R3 at656 before bias
equ-L704, already in UOPT. Signed counter changes cached constants/R3 roles;
real52->48 access-count rejection remains effective. Nine checks pass85.576s,
no pin rebase/credit. Toolsce3980b first; older HEAD/all425 hashes preserved
with only two absent additions. Next bias conversion/cache formation/liveness
and cuts10/7.

Previous actor command-finalizer bounds/clamp/tail checkpoint:
[Note 1336](WORKING_NOTES/1336-game-actor-command-finalizer-bounds-clamp-and-secondary-tail-alignment-20261013.md):
func_15034860 restores explicit bounds arms, primary clamp orientation and
direct signed tail velocity:405/frame0x48,266->76 differences. Clamp words
210..213 exact; secondary block aligned, a2/a0/a3/v0 roles/six slots retained.
Exact sampled states1322->1598/2938 with no prior loss. All15 pre-install tests
and installed792-byte target-only image/data proof pass.25 bodies reject
overflow and a70-score cut9 regression. All17 installed checks pass63.247s;
tools56a0cee first, older HEAD/unrelated423 hashes preserved apart from the
verified ELF-pin edit. Next category/noise/lower scheduling
and remaining register/operand allocation; cuts10/7/full matching stay open.

Previous actor command-finalizer secondary-value checkpoint:
[Note 1335](WORKING_NOTES/1335-game-actor-command-finalizer-secondary-value-register-restoration-20261013.md):
func_15034860 restores secondary sign/choose/reverse/value roles a2/a0/a3/v0
by reusing the existing signed value local.405/frame0x48,267->266 differences;
exact sampled states1086->1322/2938, no earlier agreements lost. Six slots,
homes, full owner/rebase/parent contracts stay fixed. The installed literal
audit changes55 target bytes only; all720 data owners exact, no guards/credit.
All16 installed target/text checks pass77.702s; tools6217aa4 first and older
421 unrelated inputs retained apart from the verified protected ELF-pin edit.
19 source forms distinguish word identity from equal scores. Next primary
clamp/allocation, block alignment and still-open cuts10/7/full matching.

Previous actor command-finalizer tag-dependency checkpoint:
[Note 1334](WORKING_NOTES/1334-game-actor-command-finalizer-tag-dependency-canonicalization-20261013.md):
Production stays405/frame0x48/267; source/ELF/guards/profile/progress fixed.
20 real tag/factor and advised placement forms emit exactly the same two word
arrays (267 current/261 rejected). One bounded advisory is independently
rejected: its raw AS1 lower positions166/165 have the same instruction ordinal38
and all312 instruction records identical. Eight focused/image/text checks
pass14.780s; no matching credit or pin rebase. Toolsa71abb7 first; older HEAD/
all419 existing hashes preserved/no push. Next actual source/UOPT/UGEN lifetime
and ordering proof, preserving cut9 and still-open cuts10/7/full gates.

Previous actor command-finalizer owned backend-boundary checkpoint:
[Note 1333](WORKING_NOTES/1333-game-actor-command-finalizer-owned-ugen-as1-boundary-20261013.md):
Production source/ELF stay405/frame0x48/267 differences. Owned UGEN probes fire
200 load/68 immediate-memory events per body, with normal/traced object identity.
Actual AS1 input correlates all68 events: lower immediate records184 current /
165 early, tag home189 both. This locates an upstream ordering difference,
not complete AS1 causality.14 tag forms produce no eligible fit. All11 focused
diagnostic/integrity checks pass10.548s; no guards/pin rebase/credit. Tools3fb2ea0
first; older HEAD/all416 existing hashes preserved/no push. Next source/UOPT/
UGEN ordering around byte/tag/lower/conversion, plus still-open cuts10/7/full gates.

Previous actor command-finalizer primary jitter-load checkpoint:
[Note 1332](WORKING_NOTES/1332-game-actor-command-finalizer-primary-jitter-load-order-restoration-20261013.md):
func_15034860 restores LBU T3 / LB T9 order,269->267 real differences. Only
two words/six target ELF bytes change;405/frame0x48/six slots/160 homes fixed.
Exact represented fault states720->1086/2938, no previously exact sampled state
lost. Primary cut10 and disabled-primary cut7 remain open. All15 installed
target/text checks pass46.959s; all other ELF bytes and720 data owners fixed.
Tools2b16f4f first; older HEAD/413 unrelated hashes preserved/no push. README
aggregates fixed. Next owned lower/tag/conversion evidence and remaining267
differences under complete private/fault/owner/rebase/image gates.

Previous actor command-finalizer direct-byte/cut9 checkpoint:
[Note 1331](WORKING_NOTES/1331-game-actor-command-finalizer-direct-byte-input-and-primary-cut9-restoration-20261013.md):
func_15034860 retains405/frame0x48 and all six slots/160 homes; differences
298->269, no guards or credit. Direct numeric-byte conversion restores T7/T4
and closes primary cut9 on44 paths. Exact represented fault states452->720
of2938 pairs; first divergence cut10 on44 paths and cut7 on eight, not full parity.
All13 pre-install/installed tests pass (42.357s/44.410s); exactly181 target ELF
bytes change, all other bytes and720 Game-data owners fixed. Protected-text
integrity/corruption checks pass1.670s. Tools9cd126b first; older HEAD and411
unrelated hashes preserved/no push. README totals already agree and stay fixed.
Post-bank all15 target/text checks pass58.606s, no skips; source commit
b22b87a0's graph hook completes and all4639 checked relative links are valid.
Next same function's primary lower-bound schedule at cut10 and second-selector
allocation at cut7, then269 remaining differences under the complete gates.

Previous actor command-finalizer scalar/cut5 checkpoint:
[Note 1330](WORKING_NOTES/1330-game-actor-command-finalizer-scalar-predicate-and-cut5-restoration-20261013.md):
func_15034860 retains405/frame0x48, differences299->298, no guards or credit.
Unsigned category views/inverted noise restore the first14 words and close cut5
on all52 sampled paths. Exact complete fault states260->452 of2,938 pairs;
first divergence now cut9 on44 paths and cut7 on eight. Full parity remains open.
All13 target tests plus two protected-text checks pass post-bank (47.426s),
including guest/native/slot/home/frame/owner/rebase/parent qualification.
Only50 target ELF bytes change; all other bytes/720 data owners fixed.
Fresh protected text integrity passes. Tools79fe8a8 first, older HEAD/132
unrelated hashes preserved/no push. Correct README aggregates stay fixed.
Next same function's primary byte/tag/lower schedule at cut9 and second-selector
register allocation at cut7, then remaining298 differences under full gates.

Previous actor command-finalizer selector/noise-fit checkpoint:
[Note 1329](WORKING_NOTES/1329-game-actor-command-finalizer-selector-delay-slot-and-nested-noise-fit-20261013.md):
func_15034860 stays405 words/frame0x48, differences307->299, no guards or credit.
The combined ordinary-parameter/nested-noise/late-bound/delta-input source
restores the selector load at retail word9 in the suppression delay slot.
All13 target tests plus two protected-text checks pass post-bank (47.244s).
Six live slots and160 input-home aliases remain qualified. Cut5 still differs,
now only GPR3/7; all2,938 sampled fault pairs fire,
260 equal states unchanged. Full private/fault parity is not achieved.
Owned frame/object, guest/native/owner/rebase/parent and254-byte target-only
ELF/data gates pass; observation labels and protected text integrity are checked.
Tools e37e4b3 first, older HEAD/130 unrelated hashes preserved/no push.
Matching aggregates and correct README rows stay fixed. Next same function's
GPR3/7 opening roles and299 remaining differences under all full matching gates.

Previous actor command-finalizer opening-fault checkpoint:
[Note 1328](WORKING_NOTES/1328-game-actor-command-finalizer-opening-fault-boundary-and-fit-rejections-20261013.md):
46 unchanged-profile source screens find no better fit; production remains
405 words / frame0x48 / 307 differences, no guards or credit. Six new tests pass.
All 52 sampled paths first differ at access cut5 before the first-selector load:
retail word9 versus source word27. Memory/events/FPRs/RA agree there; GPRs differ.
All 2,938 actual fault pairs fire, with 260 equal complete represented states.
Do not claim full private/fault or hardware exception parity. An invalid Claude
packet loses its code excerpts; its advisory is discarded, not accepted evidence.
Tools b04caa1 first; all eight production inputs/ELF/data stay fixed, older
HEAD/129 existing hashes preserved/no push. README aggregates stay correct.
Next same function's opening suppression/type/selector schedule and cut5,
retaining its six live slots and full extent before broader matching gates.

Previous actor command-finalizer live-temporary checkpoint:
[Note 1327](WORKING_NOTES/1327-game-actor-command-finalizer-live-temporary-slot-restoration-20261013.md):
func_15034860 retains405 words/original0x48 frame, real differences342->307.
Reordered existing locals restore six actual live stack slots; the promoted
actor-type predicate improves code fit. No guards/profile/ABI change or credit.
Eleven installed tests pass, including80 slot probes/16 old-body failures and
160 retained incoming-home aliases. Compiler M definition44->48, frame unchanged;
normal/traced objects agree. Guest/native/owner/rebase/parent gates and literal
269-byte target-only ELF/data proof pass. Fresh text integrity passes.
Toolscf06d70 before consumer; older HEAD/126 unrelated hashes preserved/no push.
Game2,823/4,823, total3,496/5,496, zero drift/different2,000 remain fixed.
Correct README rows stay unchanged. Next same function's307 differences and
full private/scratch/fault match; full Game/text/translator/runtime remain open.

Previous actor command-finalizer extent/frame/home checkpoint:
[Note 1326](WORKING_NOTES/1326-game-actor-command-finalizer-extent-frame-and-home-restoration-20261013.md):
func_15034860 now emits the full405 words/original0x48 frame; real differences
398->342, no guards/profile/ABI change or matching credit. Captured full-word tag
indices restore observable input-home behavior:160 private-output cases pass
and the old body fails50. The qualifier alone is not proven necessary for homes.
Ten installed tests pass; fired compiler captures show locals40->48, saved8/
outgoing16 fixed, traced objects identical. Guest/native/owner/rebase/real-parent
and literal1,318-byte image/data gates pass; no new metadata exception.
Fresh text integrity passes. Toolsda7ddac before consumer, older work preserved/no push.
Game2,823/4,823 (58.53%), total3,496/5,496 (63.61%), drift0/different2,000,
converted fixed. Correct README rows stay unchanged. Next same function's342
allocation/scheduling/stack-layout differences, exact private/fault gates;
full Game/earlier guard elimination/text/translator/runtime remain open.

Previous actor command-finalizer semantic-recovery checkpoint:
[Note 1325](WORKING_NOTES/1325-game-actor-command-finalizer-semantic-recovery-and-matching-boundary-20261013.md):
func_15034860's placeholder is replaced by the complete two-channel contract.
Raw C395/frame0x40 versus retail405/frame0x48 leaves398 word differences,
not a match or improvement in exact-word score. No guards/profile/ABI change.
Ten installed tests pass:15,288 guest,385 selector/alias,8,192 native32,
480 independently rebased and200 real119-word parent cases; nine neighbors/
pools/both padders stay fixed. Literal image accounts1,161 target/two size/
79 closed metadata bytes; all other code/data/guards remain unchanged. Fresh
text integrity passes. Toolsb6ba284 first; older work preserved/no push.
Game2,823/4,823 (58.53%), total3,496/5,496 (63.61%), drift0/different2,000,
converted fixed. README aggregate rows already agree and stay unchanged.
Next same func_15034860's length, first-parameter home, frame and scheduling;
physical/private/fault matching, full Game/text/translator/runtime remain open.

Previous actor command-dispatch direct-match checkpoint:
[Note 1324](WORKING_NOTES/1324-game-actor-command-dispatch-direct-match-and-table-layout-20261013.md):
func_15033FE0 replaces its placeholder with the complete119-word dispatcher,
directly exact/frame0x28/no target guards. Declaration order recovers first-result
home M-8 rather than M-16; fired read-only compiler captures preserve object
identity. The37-entry table is exact. One derived neighbor LO16 layout adapter
translates148->160 over retail floats/alignment, preserving all neighbor code.
Eight installed tests pass; connected119/97-word parent/child, owner/padder/rebase,
356-byte literal image and unchanged189,088-byte data gates pass. Fresh text
integrity passes. Game2,823/4,823 (58.53%), total3,496/5,496 (63.61%),
drift0/different2,000, converted fixed. Tools1943c4d first; older unrelated work
preserved/no push. Next func_15034860,405 words/frame0x48/372 differences.
Direct guard elimination for earlier matches, text/translator and full
Game/runtime/hardware gates remain open.

Previous actor command-stream guarded-match checkpoint:
[Note 1323](WORKING_NOTES/1323-game-actor-command-stream-guarded-match-20261013.md):
func_150341BC's full typed body replaces its zero-return placeholder. All97 linked
words/frame0 match using52 derived register/cursor/branch guards; raw C96/62
is not a direct match. Eight installed tests plus final focused native rerun
qualify signed values, aliases,166 faults, both owner padders and three rebases.
Whole ELF changes only292 target/two size/66 closed metadata bytes; all data and
old guard history stay fixed. Text integrity passes; tools c30d7a0 first, older
HEAD/unrelated hashes preserved. Game2,822/4,823 (58.51%), total3,495/5,496
(63.59%), drift0/different2,001, converted fixed. Next func_15033FE0,
119 words/frame0x28/115 differences. Direct guard elimination, text/translator
and hardware/gameplay gates remain open; no push.

Previous actor callback direct-match checkpoint:
[Note 1322](WORKING_NOTES/1322-game-actor-callback-dispatch-direct-match-and-frame-provenance-20261012.md):
func_150345E4 now matches all81 words directly, original frame0x20/no guards.
Read-only compiler captures trace local reservation16->8; preserve outgoing16
and saved8. Nine installed tests pass, literal stack/fault/owner/rebase gates;
whole ELF changes only eight frame-word bytes, all other bytes/data fixed.
Fresh text integrity passes; tools80e6fed first, older HEAD/unrelated hashes
preserved. Game2,821/4,823 (58.49%), total3,494/5,496 (63.57%), drift0/different
2,002, converted fixed. Next func_150341BC,97 words/frame0/94 differences;
text/translator and hardware/gameplay gates remain open, no push.

Previous actor callback semantic-recovery checkpoint:
[Note 1321](WORKING_NOTES/1321-game-actor-callback-dispatch-semantic-recovery-and-frame-boundary-20261012.md):
func_150345E4's zero-return placeholder is replaced by the complete81-word
dispatcher and a typed void caller prototype. Differences78->8: all73 other
words match, but source frame0x28 remains original0x20's unresolved boundary.
No frame guards or matching credit. Seven pre-/post-install tests pass:65,536
guest plus24 home/36 flag cases,65,536 native32 and65 logical fault pairs.
Nine target-owner neighbors/all38 caller-owner functions, both padders/pools
and three rebases agree. Whole ELF changes only242 target bytes/two size bytes;
all data/guards/other inputs stay fixed. Text integrity passes. One tool-free
Claude review completes; its two proposed controls fail, no accepted fix or
proven compiler cause. Tools e5c3868 first; older HEAD/unrelated work preserved.
Matching stays Game2,820/4,823 (58.47%), total3,493/5,496 (63.56%), drift0,
different2,003, converted fixed. Next same func_150345E4's eight frame words;
text/translator remain open, no hardware/gameplay parity or push.

Previous actor matrix-clear byte-match checkpoint:
[Note 1320](WORKING_NOTES/1320-game-actor-matrix-clear-byte-match-20261012.md):
func_15034728 now emits the complete48-word/192-byte/frame0x20 matrix clear.
Raw C has18 allocation/operand-order differences;18 expected-word guards derive
one closed post-helper GPR cycle and commutative addition, not a copied body.
Eight pre-/post-install tests pass: 4,320 guest plus24 alias cases, 32,792 native32,
36 real caller/helper/table chains and361 fired fault triples. All nine neighbors,
both padders/pools and three rebases agree. Caller scan is25 records, not26.
Whole ELF changes only147 target bytes and one size byte; data stays exact,
old guards stay byte-identical with only18 appended rows, all other inputs fixed.
Archived text ELF/guard receipts advance after proof; fresh integrity controls
pass. Game2,820/4,823 (58.47%), total3,493/5,496 (63.56%), drift0/different2,003,
converted fixed. Next func_150345E4's81-word actor callback dispatch;
text218/114/cut27 and translator remain open. Tools9691502 first, no push;
older HEAD/all unrelated fingerprints preserved. No direct-C/hardware/gameplay claim.

Previous actor-type dispatch direct-match checkpoint:
[Note 1319](WORKING_NOTES/1319-game-actor-type-dispatch-direct-match-20261012.md):
func_1503453C replaces its placeholder with the complete actor-type switch,
all42 words/168 bytes/frame0x18 directly, no guards/profile change. Its five
table entries match retail; a scoped Makefile binding keeps the original owner.
Seven pre-/post-install tests pass: 6,144 guest, 26,624 native32, 360 actual
connected-caller cases and23 fired fault pairs. All nine neighbors, both full-
owner padders and three rebases agree. Literal whole ELF permits only119 target
bytes and one size byte; all data/guards/progress/layout remain fixed. Archived
text ELF/Makefile receipts advance only after that gate; fresh integrity controls
pass. Game2,819/4,823 (58.45%), total3,492/5,496 (63.54%), drift0/different2,004,
converted totals fixed. Next func_15034728's48-word masked matrix clear;
text218/114/cut27 and translator stay open. Tools84cfb3a first, no push;
older HEAD/all unrelated fingerprints preserved. Downstream helper remains opaque.

Previous grouped-actor dispatch direct-match checkpoint:
[Note 1318](WORKING_NOTES/1318-game-grouped-actor-dispatch-direct-match-20261012.md):
func_150226BC replaces its zero-return placeholder with the recovered two-index
descriptor/actor dispatcher. All38 words/152 bytes match directly, frame0x20,
using the unchanged owner no-unroll profile and no guards. Seven pre-/post-
install tests pass: 17,280 isolated guest, 288 actual connected caller/helper
cases, 16,816 native32 comparisons and 266 fired cuts. All56 neighbors/pools,
both full-owner padders and three rebases agree. Whole ELF changes only120
target bytes, size12->152 and a closed16-byte ABS value/string permutation;
named definitions/data/guards/layout remain exact. Text integrity controls pass,
broader unchanged receipts reused. Game2,818/4,823 (58.43%),
total3,491/5,496 (63.52%), drift0/different2,005, converted totals unchanged.
Next func_1503453C, the42-word actor-type/jump-table dispatcher; keep the text
218/114/cut27 and matrix translator open.
Tools a7b5b37 is banked first; older HEAD/unrelated dirty work preserved.

Previous one-shot timer direct-match checkpoint:
[Note 1317](WORKING_NOTES/1317-game-one-shot-timer-direct-match-20261012.md):
func_1501BB20 replaces its zero-return placeholder with the gated void timer
routine. All38 words/152 bytes match directly, frame0x28/no guards/profile
change. Seven tests pass before/after installation: 36,864 guest cases,
233,472 native32 comparisons, 92 fired access-cut pairs, seven owner neighbors,
both padders and three independent rebases. Whole-image audit permits only
121 target bytes, one size byte12->152 and eight bytes of a closed two-ABS-
symbol value/string serialization permutation; all named definitions remain
unchanged except target size. All Game data/protected inputs remain exact.
Fresh text integrity controls pass; unchanged broader receipts are reused,
not called fresh. Game2,817/4,823 (58.41%), total3,490/5,496 (63.50%),
drift0/different2,006, converted totals unchanged. Next func_150226BC's grouped
record/actor dispatch; text218/114/cut27 and matrix translator remain open.
Tools 6a9eb2d is banked first; older HEAD/unrelated dirty work preserved.

Previous rectangle-bounds direct-match checkpoint:
[Note 1316](WORKING_NOTES/1316-game-rectangle-bounds-predicate-direct-match-20261012.md):
func_1501AE94 now replaces its zero-return placeholder with the original ordered
float rejection predicate. All44 words/176 bytes match directly, frame0/no
guards or profile change. Seven target tests pass before/after installation:
10,692 guest cases, 65,536 native32 comparisons, 58 access-cut pairs and 18
authentic caller-window cases; all ten neighbors and both full-owner padders
agree. Literal ELF audit changes only124 target bytes and size12->176; all
Game data/protected inputs stay fixed. Two text immutable/corruption controls
pass against the independently qualified new image; prior unchanged broader
regressions are reused, not called fresh. Game2,816/4,823 (58.39%),
total3,489/5,496 (63.48%), drift0/different2,007, converted totals unchanged.
Next func_1501BB20, the 38-word gated one-shot timer setup; text218/114/cut27
and matrix translator remain open.
Tools 0a939ff is banked first; older HEAD and unrelated dirty work preserved.

Previous event-record direct-match checkpoint:
[Note 1315](WORKING_NOTES/1315-game-event-record-constructor-direct-match-20261012.md):
func_15015104 now emits all 52 retail words directly, frame0x58/no guards,
after retaining the raw flag word and spelling its two tests independently.
Seven pre-install and seven post-install tests pass: 15,552 guest cases,
49,152 native32 comparisons, 240 fired access-cut pairs and literal ELF/data
gates. Only 105 target bytes and one size-field byte change, 200->208; all 31
owner neighbors and protected inputs stay fixed. Game2,815/4,823 (58.37%),
total3,488/5,496 (63.46%), drift0/different2,008; converted totals unchanged.
All16 combined target/text tests and six retained callback regressions pass;
tools ec4865d is banked first. The older tools mirror retains HEAD/dirty work.
Next func_1501AE94, a 44-word rectangle-bounds predicate still represented by
a zero-return placeholder. Text218/114/cut27 and matrix translator remain open.

Previous mode-callback direct-match checkpoint:
[Note 1314](WORKING_NOTES/1314-game-mode-callback-dispatcher-direct-match-20261012.md):
func_15008930 now emits all 38 retail instructions plus its two original
alignment words directly, frame0x30/no guards. Literal whole-ELF audit allows
only its slot and size field, 12->152; data/guards/layout/converted totals stay
fixed. All fourteen dispatcher/text tests pass; tools d3426e6 first. Game now
2,814/4,823 (58.35%), total3,487/5,496 (63.45%), drift0/different2,009.
Next inspect func_15015104; text218/114/cut27 and matrix translator remain open.

Retained repeated-predicate/font-load-boundary checkpoint:
[Note 1313](WORKING_NOTES/1313-game-text-measurer-repeated-predicate-and-font-load-fault-boundary-20261012.md):
func_150428D4: 218/frame0x80/114 preserves the seven opening roles/common zero/
SP+0x68 and matches a literal 53-word metrics region. Space/newline/A8 match
all named access cuts; A first rejects at font-pointer cut27, with RAM/events
and RA still equal. All thirteen tests pass, tools 4dbdcbe first; no installation,
production/totals/main README unchanged, same target/full Game active.

Previous address-work/retail-save-role checkpoint:
[Note 1312](WORKING_NOTES/1312-game-text-measurer-address-work-lifetime-and-retail-save-roles-20261012.md):
func_150428D4: forward ternary work recovers all seven retail opening roles,
frame0x80, common early T0 zero and named M-24 / SP+0x68 together. Its
216-word / 171-difference body remains rejected. Five bodies pass 3,775 guest
and 7,330 native32 comparisons; all twelve new/regression tests pass.
Tools 4cf5203 first; production/totals/main README unchanged, full Game active.

Previous shared-zero/source-home checkpoint:
[Note 1311](WORKING_NOTES/1311-game-text-measurer-shared-zero-and-source-home-call-save-20261012.md):
func_150428D4: split updates recover common early T0 zero and named M-24 /
SP+0x68 save in a 218/frame0x80 body, but an extra font-address save still
rejects it. Seven bodies pass 5,285 public comparisons; all twelve distinct
new/regression tests plus focused capture rerun pass. Tools 54c4808 first;
production/totals/main README unchanged, same target/full Game active.

Previous switch/register-hint checkpoint:
[Note 1310](WORKING_NOTES/1310-game-text-measurer-switch-and-register-hint-provenance-20261012.md):
func_150428D4: six five-field forms / three bodies pass 2,265 public comparisons
but keep an extra S4 flag and stale T0 at both first-read boundaries. Register
adds a literal CFE VREG with raw level 0; the unscoped UOPT stream stays byte-
identical with no call-save. All twelve tests pass, tools 615bdc9 first;
production/totals/main README unchanged, same target/full Game active.

Previous assignment/predicate-boundary checkpoint:
[Note 1309](WORKING_NOTES/1309-game-text-measurer-explicit-assignment-and-predicate-boundaries-20261012.md):
func_150428D4: six forms pass 4,530 public comparisons but remain rejected.
Explicit assignment keeps the source flag load post-call; separated effects
spill real R8 at SP+0x58 but have T0=1 at the first ordinary text reread.
All twelve new/regression tests pass. Tools 54ded39 first; production/totals/
main README unchanged, same target/full Game active.

Previous font-control/initializer checkpoint:
[Note 1308](WORKING_NOTES/1308-game-text-measurer-font-controls-and-initializer-call-save-20261012.md):
func_150428D4: four qualifier controls / three bodies pass 2,265 public
comparisons. Real R8 M-24 call-save maps to SP+0x68, but the 219/frame0x80
initializer still has eight saves and late zero. Six new and nine regression
tests pass; tools 01a4cd8 first. No recovered volatile declaration or match;
production/totals/root README unchanged, same target/full Game active.

Previous wire-operand/source-marker checkpoint:
[Note 1307](WORKING_NOTES/1307-game-text-measurer-wire-operands-and-source-marker-provenance-20261012.md):
func_150428D4: descriptor-aware decoding qualifies the actual named-flag
streams without interpreting undefined LOC fields. Literal CFE VREG records
are not the UOPT source-variable marker; compound flag loads occur post-call.
All 22 focused tests pass. New 219/134 shape still fails frame/roles/reset.
Tools b3d042d first; production/totals/root README unchanged, full Game active.

Previous carrier-layout/register-role checkpoint:
[Note 1306](WORKING_NOTES/1306-game-text-measurer-carrier-layout-and-register-role-qualification-20261012.md):
func_150428D4: ten distinct layouts pass 7,550 public comparisons but fail
the retail frame. Paired captures move the record, not the M-56 call-save;
one T0-spilling form actually carries maximum width. Six new tests and both
isolated regressions pass. Tools e7ebb38 first; production/totals/root README
unchanged. Recover shared default-zero merge and all final matching gates.

Previous frontend/UOPT provenance checkpoint:
[Note 1305](WORKING_NOTES/1305-game-text-measurer-frontend-vreg-and-uopt-call-save-provenance-20261012.md):
func_150428D4: complete CFE/UOPT streams prove UOPT introduces register-8
call-save from a CFE temporary. Six tests / 3,020 public comparisons pass;
the original seven-test predicate regression also passes. A shape-only
219/0x80/SP+0x68 form still has an extra saved register and late zero.
Tools da8a377 first; production/totals/root README unchanged. Recover source
temporary placement and the shared early zero, then all final matching gates.

Previous effectful-predicate checkpoint:
[Note 1304](WORKING_NOTES/1304-game-text-measurer-effectful-predicates-and-upstream-call-save-20261012.md):
func_150428D4:16 source forms/nine instruction bodies pass6,795 public
comparisons but remain non-matching. Bitwise forms expose an upstream T0
call-save at wrong SP+0x50/0x4C homes; the219/0x80 form has wrong saved roles.
Seven focused tests pass after scoped fixture fixes. Tools d515411 first;
production/data/totals/root README/older84 fingerprints unchanged. Recover
the shared zero, correct call-save and full219 before final matching gates.

Previous UGEN register-node checkpoint:
[Note 1303](WORKING_NOTES/1303-game-text-measurer-ugen-register-node-observation-20261012.md):
func_150428D4: read-only probes fire90 load-node events per early/late body,
observing already assigned register-class nodes while preserving normal code.
Six tests qualify driver/object/probe/lifetime gates; the zero-event spill
probe remains inconclusive. Tools7da0ac2 first, production/data/totals/root
README unchanged. Return to UOPT flag live ranges/shared T0/full219; seed222
remains oversized and unmatched. Older82 fingerprints/history preserved.

Previous vreg/memory-residence checkpoint:
[Note 1302](WORKING_NOTES/1302-game-text-measurer-vreg-marker-and-memory-residence-20261012.md):
func_150428D4: removing the flag's UOPT vreg suffix/global color produces an
uncolored memory variable and extra SP+0x50 write, not retail's T0 temporary.
Ten tests pass; fifteen source forms and six isolated return declarations
yield no fit. Tools c28e130 first, production/data/totals/root README unchanged.
Next inspect UGEN temporary/cached-register handling read-only; recover shared
T0/full219 before final gates. Seed222/0x80/146 remains oversized/unmatched.

Previous forbidden-register checkpoint:
[Note 1301](WORKING_NOTES/1301-game-text-measurer-forbidden-register-constraints-20261012.md):
func_150428D4: qualified mode5 traces expose distinct early/late flag forbidden
sets and glyph interference while preserving both normal candidate objects.
Eight diagnostic tests pass. Six source forms find no accepted fit; a
counterfactual219-word reset still has the wrong0x88 frame/eight saves.
Tools e1abcff first; production/data/totals/root README unchanged. Investigate
the actual coloring/live-range boundary, then shared T0/full219/final gates.

Previous UOPT allocation-diagnostic checkpoint:
[Note 1300](WORKING_NOTES/1300-game-text-measurer-uopt-allocation-trace-20261012.md):
func_150428D4 now has completed mode4/6/7 traces with text/functions/relocations/
pools identical to the normal seed222/0x80/146 compile. A fingerprint-locked,
owned-process helper works around debug-output-only runtime failures; numeric
timings are not valid. Six new tests pass. Tools 17bd18b first; production,
protected data and totals unchanged. Use the actual allocation trace to fit
the shared T0 reset/full219 and final gates; no matching credit.

Previous instruction-fault boundary checkpoint:
[Note 1299](WORKING_NOTES/1299-game-text-measurer-instruction-fault-boundary-and-review-20261012.md):
func_150428D4: 768 fired access cuts compare independently linked original219
and seed222 at the same diagnostic entry. First divergence occurs after
normalization: RAM/events/RA agree, but retail resets T0 to zero and the seed
does not. Twenty tests pass, including a corrected non-gated observer control.
One verified tool-free packet review gives no new edit; its exhaustion claim
is not accepted. Source screens find no final fit. Tools faec3b7 first; keep
seed222/0x80/146 and recover shared T0/full219, then complete final gates.
No production/data/totals/root README changes or new matching credit.

Previous resumed seven-save lifetime checkpoint:
[Note 1298](WORKING_NOTES/1298-game-text-measurer-seven-save-lifetime-qualification-20261012.md):
func_150428D4: qualify nested late flags222/0x80/146 and flat222/0x80/178,
including exact first13 words, original S0..S6/RA homes, 755 public/six flag-
home cases and 733 native cases per O2/O0 body. Each has 28 equal fired early
fault-prefix pairs. A third seven-save form still fails the first store.
Strict padding rejects all three oversized bodies; legacy padding produces
an overflow trampoline, not a match. Eighteen tests pass; tools fb5162b first.
Next fitting seed is nested flag-branches-captured222; recover original T0,
full219 and final qualification, without broad word-copy/overflow substitutes.
Production/data/totals/root README stay unchanged; no new matching credit.

Previous committed diagnostic checkpoint while matching was paused:
[Note 1297](WORKING_NOTES/1297-game-text-measurer-ugen-diagnostic-checkpoint-20261012.md):
bank the pending text-measurer experiments and verified 166,944-byte UGEN
trace. Sixteen tests pass, including four effective trace-rejection controls.
Tools 5e14815 is committed first; production inputs/data/totals and root
README stay unchanged. No function installation or matching credit. The
next target remains func_150428D4, capture218/0x80/174 differences, awaiting
original S3/T0 lifetimes and full219 qualification on an explicit resume.

Previous text-measurer independent-link/fault rejection checkpoint:
[Note 1296](WORKING_NOTES/1296-game-text-measurer-independent-links-and-frame-fault-rejection-20261012.md):
func_150428D4: independently assemble/link original219 and padded candidate
with actual helpers/full slots, original lookup/table/float payloads and
controlled font/scales. Fifteen tests pass, including 1,554 cases at retail
and two rebases crossing HI/LO boundaries. No helper hooks or code patching.
Four fired fault pairs expose the saved-register mismatch: after the first
frame store, original SP+0x38 contains incoming S6, candidate S7. This is a
rejection gate, not complete fault qualification or a match. New scope/type/
predicate/callback screens do not supersede capture218/0x80/174 differences;
it still has an extra saved register and no production installation.
All nine production inputs/data/totals stay exact; no new target guards.
Tools 44bec83 first, older HEAD/78 other hashes preserved/two checked updates,
no push. Continue original S3 text/glyph and T0 flag lifetimes, full219 fit,
then complete private/fault/rebase/linked qualification. Full Game stays open.

Previous text-measurer lifetime/owner qualification, not yet installed:
[Note 1295](WORKING_NOTES/1295-game-text-measurer-flag-lifetime-and-owner-qualification-20261012.md):
func_150428D4: source-local font-address rematerialization and indexed input
recover a 218-word/frame-0x80/168-difference shape with exact original saves
and five metrics homes, under the unchanged profile. That shape is rejected
for private equivalence: width aliasing SP+0x68 exposes its always-stored flag.
A call-only capture/reload fixes six bounded private flag-home cases and
passes 755 public guest cases plus native733 O2/O0. It is 218/0x80/174
differences, still S0..S7 rather than original S0..S6. Thirteen focused tests
pass; both candidates preserve all seven neighbors/pools and both padders.
A freshly compiled late-reload negative fails the private gate. All nine
production inputs/data/totals stay exact; no source/ELF installation or new
target guards. Tools ce4cc1a first, older HEAD/78 other hashes preserved/two
verified updates, no push. Continue the call-only capture's original T0 flag,
S3 text/glyph reuse and 219-word fit, then full private/fault/rebase/linked
qualification. No broad 168/174 retail-copy guards. Full Game stays open.

Previous text-measurer native32 qualification, not yet installed:
[Note 1294](WORKING_NOTES/1294-game-text-measurer-native32-qualification-20261012.md):
func_150428D4's clear216 and closer217 complete C bodies pass 733 cases each
at O2/O0 with both complete recovered C helpers: 2,932 executions, portable
output/font/factor/scale/text aliases and guarded buffers/table. Nine focused
tests pass, including seven effective native semantic negatives and four
effective canary negatives. A byte-order-aware independent reference keeps
guest big-endian and native little-endian alias writes distinct. The isolated
no_r23 form reaches 219 words/frame 0x80 but still has 206 differences; its
register/home layout is wrong, and no compiler profile is installed.
All nine production inputs/data and matching/conversion totals remain
unchanged. Tools b5e4600 first; older HEAD/77 other hashes preserved, two
verified mirror updates/one new identical file, final 80 hashes, no push.
Continue this same target's original lifetime/layout fit and copied-owner/
padder/rebase/fired-fault/linked qualification. Native C is now qualified
for the two named bodies, not a byte match or portable low-pointer claim.
Full Game matching and hardware/FCSR/renderer/gameplay remain open.

Previous text-measurer full-chain qualification, not yet installed:
[Note 1293](WORKING_NOTES/1293-game-text-measurer-full-chain-qualification-20261012.md):
func_150428D4's complete 219-word/frame-0x80 routine and nine direct callers
establish a void text/three-output interface. Full original/candidate chains
execute the actual normalizer65 and metrics115, with no helper hooks.
Seven tests pass: 535 core cases, 240 alias cases, 378 closer-layout cases,
live font-pointer reload, nested truncation and eight effective compiled
controls. The closer candidate is 217 words/frame 0x80/185 differences;
it is not byte-exact. Production source/entire ELF/guards/progress/Makefile
and all nine recorded inputs remain unchanged. No matching or conversion
credit; README totals remain correct. Tools 688ae3b first, older HEAD/77
hashes preserved/two absent identical copies, no push. Continue this same
function: fit its original body and register/stack lifetimes, then qualify
owners/padders, rebases/faults and literal installation. Native C follows in
Note 1294 above. Full Game
matching and independent hardware/renderer/gameplay acceptance stay open.

Latest character-normalizer guarded match:
[Note 1292](WORKING_NOTES/1292-game-character-normalizer-guarded-match-20261012.md):
func_15042C40 restores byte narrowing, lowercase normalization, early space
mapping and first match across the original 95-entry table. The complete
68-word slot matches: 65-word/frame-zero C body with twelve cached-byte/
scratch-register guards, plus three original zeros, not direct C. All 61
reachable words are exercised; four unreachable retail words are retained.
Nine pre-install/nine final installed tests, native32, all 95 forced indices,
aliases/rebases/fired faults and actual caller windows pass. Only 198 target/
size ELF bytes change; every other byte/ten inputs/seven neighbors remain
exact, with twelve rows appended to the unchanged old guard prefix.
Game 2,813/4,823 (58.32%), total 3,486/5,496 (63.43%), zero drift /
2,010 different; +1 matching only. Tools 05875fe first, older HEAD/75 hashes
preserved/two identical new copies, no push. Next func_150428D4: 219 words /
199 differences, frame 0x80, full text measurer and its three-output contract.
Hardware/renderer/gameplay and the full Game goal remain open; README
aggregates only.

Previous extended-character metrics direct match:
[Note 1291](WORKING_NOTES/1291-game-extended-character-metrics-direct-match-20261012.md):
func_150415E0 replaces its zero-return placeholder with the six-argument
width/height/scale/mode/factor switch. All 115 words/frame zero emit directly
under the unchanged no-unroll profile, no guards. Bind the generated switch
to the original 19-entry table; its five live float constants stay untouched.
Nine installed tests pass, including native32, aliases/rebases/fired faults
and actual callsite windows, not full formatter/gameplay acceptance.
Only 521 ELF bytes change: 312 target, two size, 207 exact symbol/string
reorderings; all other bytes, nine inputs and seven neighbors remain exact.
Game 2,812/4,823 (58.30%), total 3,485/5,496 (63.41%), zero drift /
2,011 different; +1 matching only. Tools 5d3c18b first, older HEAD/73 hashes
preserved/two new identical copies, no push. Next func_15042C40: 68-word
slot / 62 differences, byte normalizer/first-match glyph lookup, a dependency
of the remaining width measurer and formatter. Full Game goal remains open;
README aggregates only.

Previous glyph-rectangle and typed-caller guarded match:
[Note 1290](WORKING_NOTES/1290-game-glyph-rectangle-and-typed-caller-guarded-match-20261012.md):
func_15041508 replaces its zero-return placeholder with a full signed-index
8-by-12 SDK rectangle and Gfx return. All 54 words/frame zero are exact with
eleven closed V1/T0/T1 allocation guards, not direct C. Correct the caller/
prototype scalar-coordinate/Gfx types; its complete 33-word raw object and
existing nine guards are unchanged. Eight pre-install/eight installed tests,
actual caller/lookup/draw chain, full SDK native32, rebases/faults/controls pass.
Only 165 target/size ELF bytes change; every other byte/ten inputs/seven
neighbors and old guard prefix remain exact. Game 2,811/4,823 (58.28%),
total 3,484/5,496 (63.39%), zero drift / 2,012 different; +1 matching only.
Tools 69d7a80 first, older HEAD/71 hashes preserved/two new identical copies,
no push. Next func_150415E0: 115 words / 112 differences, extended-character
metrics resolver; inspect its six-argument ABI and original 19-entry pool.
Guard removal, independent hardware/renderer/gameplay and full Game goal stay
open; README aggregates only.

Previous intensity-texture setup direct match:
[Note 1289](WORKING_NOTES/1289-game-intensity-texture-setup-direct-match-20261012.md):
func_150412C0 replaces its zero-return placeholder with twelve SDK commands
and the advanced Gfx pointer. All 79 words emit directly under the existing
O2/g3/no-unroll profile, with no frame/pool/guards/header/caller changes.
Eight pre-install/eight installed tests, full SDK native32, ordered writes,
rebases/fired faults and effective controls pass. Only 241 target/size ELF
bytes change; every other byte, eleven inputs and seven neighbors are exact.
Game 2,810/4,823 (58.26%), total 3,483/5,496 (63.37%), zero drift /
2,013 different; +1 matching only, converted counts/bytes unchanged.
Tools 3fb9a26 first, older HEAD/69 hashes preserved/two identical new
copies, no push. Three exact C rows and five remaining placeholders in
this owner. Next func_15041508: 54 words / 52 differences, glyph rectangle;
recover its scalar-coordinate/Gfx ABI with the already exact caller.
Existing guard removal, hardware/renderer/gameplay and full Game goal remain
open; README aggregates only.

Previous matrix-decomposer guarded C conversion:
[Note 1288](WORKING_NOTES/1288-game-matrix-decomposer-guarded-c-conversion-20261011.md):
func_1503E5F8 replaces the last GLOBAL_ASM reference in generated_6B320.
All 141 words/frame 0xC0 match with 63 allocation/scheduling guards, not
direct C. Nine pre-install/nine final installed tests, actual vector helpers,
native32 and wrapper/SDK/decomposer chain pass. Entire ELF is identical;
old guard prefix plus 63 rows, only one generated progress asm-to-c cell.
Game 2,809/4,823 (58.24%), total 3,482/5,496 (63.36%), zero drift /
2,014 different. Converted +1/564 bytes. Tools 6bee275 first; older HEAD/
67 hashes preserved, two absent copies, no push. All 22 owner C rows now
match with existing guards, no ASM/placeholders. Next genuine placeholder:
func_150412C0, 79 words / 78 differences, display-list setup leaf.
Guard removal, actual copy/trig, independent SDK/hardware/gameplay and full
Game goal remain open; README aggregates only.

Previous matrix-forward direct match:
[Note 1287](WORKING_NOTES/1287-game-matrix-forward-direct-match-20261011.md):
func_1503F404 emits all 40 executing words directly with its original three
zero tail words (43-word slot), existing O2/g3/frame 0x70 and two required
local declarations. Ten pre-install/ten installed tests, actual SDK,
native32 and full original caller152 pass. Only 119 target/size ELF bytes
change; other bytes/eight inputs/21 neighbors remain exact.
Game 2,808/4,822 (58.23%), total 3,481/5,495 (63.35%), zero drift /
2,014 different. Tools dbc0f0d first; older HEAD/65 hashes preserved, two
absent copies, no push. All 21 converted C rows in this owner match with
their existing guards; one ASM remains. Next: full matrix decomposer
func_1503E5F8, 141 words, already linked-exact but not C-converted.
Guard removal and independent SDK/hardware/gameplay/full Game goal stay open.

Previous group-2 active timer direct match:
[Note 1286](WORKING_NOTES/1286-game-record-mask-active-direct-match-20261011.md):
func_1503F2B0 emits all 85 words directly under existing O2/g3/frame 0x20.
No guards/pools/declaration/header/caller/profile changes. Eleven pre-install/
eleven installed tests, native32 and original dispatcher/finish/active/
teardown/predicate/query chain pass. Only 285 target/extent ELF bytes change;
every other byte, seven inputs and 21 neighbors remain exact.
Game 2,807/4,822 (58.21%), total 3,480/5,495 (63.33%), zero drift /
2,015 different. Tools a96b414 first; older HEAD/63 hashes preserved, two
absent copies, no push. Next func_1503F404: 43 slot words / 38 differences,
matrix conversion/copy forwarding wrapper, not a group-one active row.
Guard removal, independent SDK/hardware/gameplay and full Game goal stay open.

Previous group-2 mask-finish direct match:
[Note 1285](WORKING_NOTES/1285-game-record-mask-finish-direct-match-20261011.md):
func_1503F16C emits all 81 words directly under existing O2/g3/frame 0x20;
no guards/pools/header/caller/profile changes, one required local timer alias
declaration. Twelve pre-install/twelve installed tests, native32 and actual
dispatcher171/predicate27/finish81/query30 chain pass. Only 274 target/extent
ELF bytes change; other bytes/metadata/data/guards/seven inputs and 21 neighbors
remain exact. Game 2,806/4,822 (58.19%), total 3,479/5,495 (63.31%), zero
drift / 2,016 different. Tools c7869ae first, older HEAD/61 hashes preserved/
two absent copies, no push; README aggregates only. Next func_1503F2B0,
85 words / 84 differences; use Note 1278's existing retail caller/query
qualification. Guard removal, deeper SDK/hardware/gameplay and full Game
goal stay open.

Previous random vertical-rate direct match:
[Note 1284](WORKING_NOTES/1284-game-record-random-vertical-rate-direct-match-20261011.md):
func_1503EFC4 emits all 45 words directly under existing O2/g3/frame 0x30;
no guards, pools, header/declaration/caller/profile changes. Twelve pre-install/
twelve installed tests, native32 and actual dispatcher171/predicate27/finish45/
RNG18 chain pass. Only 135 target/extent ELF bytes change; every other byte,
metadata/data/guards/seven inputs and 21 neighbors remain unchanged. Game
2,805/4,822 (58.17%), total 3,478/5,495 (63.29%), zero drift / 2,017 different.
Tools 4cc2121 first, older HEAD/59 hashes preserved/two absent copies, no push;
README aggregates only. Next func_1503F16C, 81 words / 80 differences. Existing
guard removal, remaining callbacks and hardware/FCSR/gameplay acceptance stay
open; full Game goal active.

Previous record-ground-collision guarded match:
[Note 1283](WORKING_NOTES/1283-game-record-ground-collision-guarded-match-20261011.md):
func_1503ECA0 is complete and linked-exact across 134 words; 119 direct plus
15 closed initialization/register guards, not full direct C. Twelve pre-install/
twelve installed tests, native32 and actual timer35/context8 chains pass.
Only 443 ELF bytes change: 402 target/two extent/39 exact two-entry metadata
swap; all other bytes/data/six inputs and 21 neighbors remain unchanged.
Game 2,804/4,822 (58.15%), total 3,477/5,495 (63.28%), zero drift / 2,018
different. Tools 7730335 first, older HEAD/57 hashes preserved/two absent
copies, no push; README aggregates only. Former next func_1503EFC4 is directly matched in Note 1284.
Height/context/retirement bodies, guard removal, hardware/FCSR/gameplay
acceptance and the full Game goal remain open.

Previous record-impulse guarded match:
[Note 1282](WORKING_NOTES/1282-game-record-impulse-guarded-match-20261011.md):
func_1503EB78 is complete and linked-exact across 74 words; 69 direct words
plus five closed coefficient-register guards, not full direct C. Twelve
pre-install/twelve installed tests, native32 and actual three-caller/64-bit
RNG chains pass. Only 257 ELF bytes change: 233 target/two extent/22 exact
four-entry metadata rotation; every other byte/data/six inputs and 21 neighbors
remain unchanged. Game 2,803/4,822 (58.13%), total 3,476/5,495 (63.26%),
zero drift / 2,019 different. Tools f6b3f22 first, older HEAD/55 fingerprints
preserved/two absent copies, no push; README aggregates only. Its former next
func_1503ECA0 is guarded-exact in Note 1283. Guard removal, deeper hardware/
FCSR/gameplay acceptance and the full Game goal remain open.

Previous record-motion guarded tail match:
[Note 1281](WORKING_NOTES/1281-game-record-motion-guarded-tail-match-20261011.md):
func_1503EA54 replaces its placeholder with all 71 reachable words directly;
one checked insertion retains an unreachable return, all 73 linked words
exact, not full direct C. Twelve pre-install/twelve installed tests pass,
native32 and actual five-body dispatcher chain within documented boundaries.
Only 226 target/extent ELF bytes change; other bytes/data/six inputs and 21
neighbors exact, original guard byte prefix plus one row. Fresh Game
2,802/4,822 (58.11%), total 3,475/5,495 (63.24%), zero drift / 2,020 different;
+1 matching only. Tools 6f16f59 first, older HEAD/53 fingerprints preserved,
two absent copies/no push; README aggregates only. Its former next target
func_1503EB78 is guarded-exact in Note 1282. Tail/earlier guard removal and independent hardware/
FCSR/gameplay acceptance remain separate; full Game goal active.

Previous direct record-matrix rebuild:
[Note 1280](WORKING_NOTES/1280-game-record-matrix-update-direct-match-20261011.md):
func_1503E82C replaces its placeholder with all 138 words directly from C,
no guards/profile/header/caller-body changes. Thirteen pre-install and thirteen
installed tests pass, native32 and actual helpers/four-body dispatcher chain
within documented boundaries. Only 460 target/extent ELF bytes change;
other bytes/data/guards/seven inputs and 21 neighbors exact. Fresh Game
2,801/4,822 (58.09%), total 3,474/5,495 (63.22%), zero drift / 2,021 different;
+1 matching only. Tools 73745f6 first, older HEAD/51 fingerprints preserved,
two absent copies/no push; README aggregates only. Its former next target
func_1503EA54 is guarded-exact in Note 1281. Remaining callees, existing guard
removal and deeper
hardware/FCSR/gameplay acceptance remain separate; full Game goal active.

Previous direct record-transform setup:
[Note 1279](WORKING_NOTES/1279-game-record-transform-setup-direct-match-20261011.md):
func_1503E3C4 replaces its placeholder with all 141 words directly from C,
no guards/profile/caller-body changes. Thirteen pre-install and thirteen
installed tests pass, native32 and connected retail helpers/dispatcher chain
within documented boundaries. Only 445 target/extent ELF bytes change;
other bytes/data/guards/seven inputs and 21 neighbors exact. Fresh Game
2,800/4,822 (58.07%), total 3,473/5,495 (63.20%), zero drift / 2,022 different;
+1 matching only. Tools 036e55c first, older HEAD/49 fingerprints preserved,
two absent copies/no push; README aggregates only. Its former next target
func_1503E82C is directly matched in Note 1280. Decomposer/other callees,
existing guard removal
and deeper hardware/gameplay acceptance remain separate; Game goal active.

Previous guarded record-mask teardown:
[Note 1278](WORKING_NOTES/1278-game-record-mask-teardown-guarded-match-20261011.md):
func_1503E260 replaces its placeholder with a complete 89-word body,
87 direct words and
two closed private spill guards; all 89 linked exact, not direct C. Eleven
pre-install/eleven installed tests pass, native32 and actual retail caller/
predicate/query chain qualified within documented boundaries. Only 287 ELF
bytes change: 285 target/two extent; all other bytes/data/six inputs and 21
owner neighbors exact, old guard byte prefix plus two rows only. Fresh Game
2,799/4,822 (58.05%), total 3,472/5,495 (63.18%), zero drift / 2,023 different;
+1 matching only. Tools 1c81a02 first, older HEAD/47 fingerprints preserved,
two absent copies/no push; README aggregates only. Its former next target
func_1503E3C4 is directly matched in Note 1279. Spill guard removal and deeper
setup/callback/allocator/hardware/gameplay acceptance remain separate.

Previous direct record-state dispatcher checkpoint:
[Note 1277](WORKING_NOTES/1277-game-record-state-dispatcher-direct-match-20261011.md):
func_1503DF48 replaces its placeholder with all 171 words directly from C,
no guards/profile changes. Thirteen pre-install and 22 installed/caller tests
pass, actual 88-word caller/27-word predicate connected. Only 562 ELF bytes
change: 554 target, two extent, six verified symbol-permutation bytes; all
other bytes/data/guards/inputs exact, 21 target/38 caller-owner neighbors.
Fresh Game 2,798/4,822 (58.03%), total 3,471/5,495 (63.17%), zero drift /
2,024 different; +1 matching only. Tools 72fe857 first, older HEAD/45
fingerprints preserved/two absent copies, no push; README aggregates only.
Its former next target func_1503E260 is guarded-exact in Note 1278.
Setup/callback/tail implementations and third-loader guard elimination
remain separate open work.

Latest direct actor/group mask command:
[Note 1276](WORKING_NOTES/1276-game-actor-group-mask-command-direct-match-20261011.md):
func_1503DE70 replaces its placeholder with all 39 words directly from C,
no guards/profile changes. Ten pre-install / eleven installed tests plus a
focused integrity rerun pass; actual helper and all three callers qualified.
Exactly 127 ELF bytes change in the target slot/extent; 21 neighbors/data/
guards/seven other inputs exact. Fresh Game 2,797/4,822 (58.00%), total
3,470/5,495 (63.15%), zero drift / 2,025 different; +1 matching only.
Tools 3b4d8ec first, older HEAD/43 fingerprints preserved, no push. README
gets aggregate rows only. Next unmatched func_1503DF48: 171 words / 168
linked differences; two third-loader scheduling guards remain open.

Latest installed third-loader exit/drop removal:
[Note 1275](WORKING_NOTES/1275-game-third-resource-loader-exit-scheduling-and-drop-removal-20261011.md):
func_1503D774 emits 36 raw words / two differences, versus 37/7. Three
normalizations plus one drop become two independent final scheduling guards,
no drop; 34 direct retail words, all 36 linked exact, not direct C.
Fourteen pre-install and 151 installed/regression tests pass. Entire ELF/data/
seven other inputs unchanged, zero matching credit. Fresh Game 2,796/4,822,
total 3,469/5,495, zero drift / 2,026 different. Tools 36adf10 first, older HEAD/
41 fingerprints preserved/two absent copies, no push or root README churn.
The former next target func_1503DE70 is directly matched in Note 1276.

Latest installed third-loader lifetime and guard reduction:
[Note 1274](WORKING_NOTES/1274-game-third-resource-loader-incoming-result-lifetime-and-guard-reduction-20261011.md):
func_1503D774 reuses the ignored argument as request result/shared status.
Raw 37/15 becomes 37/7; six normalizations become three, one drop remains.
All 36 linked words exact, 33 direct; not a direct C match. Thirteen pre-install
and 137 installed/regression tests pass, including actual seventeen-body chain.
Entire ELF/protected data/seven other inputs unchanged; zero matching credit.
Fresh Game 2,796/4,822, total 3,469/5,495, zero drift / 2,026 different.
Tools 5eb0c4a first, older HEAD/39 fingerprints preserved/two absent copies,
no push. Root README unchanged. Next remaining shared-status exit guards.

Latest third-loader audit and actual-chain qualification:
[Note 1273](WORKING_NOTES/1273-game-third-resource-loader-guard-audit-and-actual-chain-20261011.md):
func_1503D774 remains exact over 36 linked words with its six existing
normalizations and one instruction drop; raw C is 37 words / 15 differences.
No production input or matching-credit changes. Twelve new and fifteen SDK
tests pass; actual seventeen-body parent chain / 3,840 executions, including
real status-two NULL failures. All nine inputs/protected data exact. Fresh
Game 2,796/4,822, total 3,469/5,495, zero drift / 2,026 different. Tools b6877d5
first, older HEAD/37 fingerprints preserved/two absent copies, no push.
README unchanged. Actual chain done; direct guard elimination remains next.

Latest installed record-resource cleanup direct match:
[Note 1272](WORKING_NOTES/1272-game-record-resource-cleanup-direct-match-20261011.md):
complete func_1503DD1C emits all 43 retail body words directly, 172-byte
extent / 180-byte padded slot, void identity contract and live callback-aware
record/count behavior. No new guards/profile/recipe changes. Twelve pre-install
and 97 installed/regression tests pass; actual cleanup/release and sixteen-body
parent chains. Exactly 149 ELF bytes change: 134 target, one extent, fourteen
checked two-symbol metadata permutation; all other bytes/data/inputs exact.
Fresh Game 2,796/4,822, total 3,469/5,495, zero drift / 2,026 different.
+1 matching only; README aggregate rows only. Tools 663f63b first, older HEAD/
35 fingerprints preserved/two absent copies, no push. Next eliminate the
existing third-loader guards and qualify its actual parent-chain body;
func_1503D774 is already linked-exact, no additional matching credit.

Latest installed group publication-propagation direct match:
[Note 1271](WORKING_NOTES/1271-game-group-publication-propagation-direct-match-20261011.md):
complete func_1503D510 emits all 56 retail words directly, void/full-word
identity contract, cached group count/list and ordered live pointer/halfword
propagation. No new guards/frame/profile/recipe/global-declaration changes.
Twelve pre-install and 85 installed/regression tests pass, actual seven-body
helper chain/all 56 words and 14-body parent chain. Only 165 ELF bytes change
(164 target, one extent); every other byte/data/guard/recipe/conversion input
exact. Fresh Game 2,795/4,822, total 3,468/5,495, zero drift / 2,027 different.
+1 matching only; README aggregate rows only. Tools 0e3d520 first, older HEAD/
33 fingerprints preserved/two absent copies, no push. Next func_1503DD1C:
43-word cleanup body / 45-word padded slot. Third loader already guarded-exact;
parent/pair/third guard elimination and deeper runtime remain separate.

Latest installed descriptor resource-loader direct match:
[Note 1270](WORKING_NOTES/1270-game-descriptor-resource-loader-direct-match-20261011.md):
complete func_1503D660 emits all 69 retail words directly, original frame/
saved lifetimes, no new guards/profile/recipe changes. Twelve pre-install and
73 installed/regression tests pass, including the actual 13-body loader chain
and all 69 target words. Only 197 ELF bytes change (195 target, two extent);
other bytes/data/guards/Makefile/conversion inputs exact. Fresh Game
2,794/4,822, total 3,467/5,495, zero drift / 2,028 different. +1 matching only;
README aggregate rows only. Tools 9359eb3 first, older HEAD/31 fingerprints
preserved/two absent copies, no push. Next complete 56-word func_1503D510.
Parent/pair guard elimination and deeper heap/hardware/renderer/gameplay stay open.

Latest installed vertex-coordinate copy guarded match:
[Note 1269](WORKING_NOTES/1269-game-vertex-coordinate-copy-guarded-match-20261011.md):
complete func_1503D804 matches all 96 linked words: 92 direct plus four closed
frame/count-spill guards, not a direct C match. Only this function selects the
unrolled profile; all 14 owner neighbors remain exact. Twelve pre-install and
61 final installed/regression tests pass, including the actual eight-body
loader chain. Only 298 ELF bytes change (296 target, two extent); other bytes/
data/conversion inputs exact, old guard prefix plus four rows. Fresh Game
2,793/4,822, total 3,466/5,495, zero drift / 2,029 different. +1 matching only;
README aggregate rows only. Tools 1310ff7 first, older HEAD/29 fingerprints
preserved/two absent copies, no push. Next complete 69-word func_1503D660.
Raw guard elimination and deeper heap/hardware/renderer/gameplay stay open.

Latest installed first-stream command weight counter direct match:
[Note 1268](WORKING_NOTES/1268-game-command-weight-counter-direct-match-20261011.md):
complete func_1503D984 emits all 46 retail words directly, no frame or new
guards/profile changes. Eleven pre-install and 49 installed/regression tests
pass, every word reached and the actual counter in the seven-body loader chain.
Only 126 ELF bytes change (125 target, one extent); every other byte/data/
guard/CSV exact. Fresh Game 2,792/4,822, total 3,465/5,495, zero drift / 2,030
different. One matching credit, no conversion; README aggregate rows only.
Tools 23570e9 first, older HEAD/27 fingerprints preserved/two absent copies,
no push. Next full 96-word func_1503D804 allocation/signed-pair copy helper.
Parent's 22 guards and deeper heap/hardware/renderer/gameplay stay open.

Latest installed command-stream relocator direct match:
[Note 1267](WORKING_NOTES/1267-game-command-stream-relocator-direct-match-20261011.md):
complete func_1503D368 emits all 52 retail words directly with original 0x38
frame/S0..S6, typed SDK Gfx/void/u32 interface and no new guards/profile changes.
Eleven pre-install and 38 installed/parent/focused historical tests pass;
actual 52-word child replaces its bounded loader-chain hook. Only 159 ELF
bytes change (158 target, one extent); every other byte/data/guard/CSV exact.
Fresh Game 2,791/4,822, total 3,464/5,495, zero drift / 2,031 different.
One matching credit, no conversion; README aggregate rows only. Tools 349aa21
banked first, older HEAD/25 fingerprints preserved/two absent copies, no push.
Next: full 46-word func_1503D984 command counter, still a placeholder.
Parent's 22 raw guards and deeper heap/hardware/renderer/gameplay stay open.

Latest installed main resource-loader full guarded match:
[Note 1266](WORKING_NOTES/1266-game-main-resource-loader-guarded-match-20261011.md):
complete func_1503CF20 matches all 274 linked words with its original 0x78
frame/S0..S6. Source stays unchanged: 252 directly exact words, 22 guarded
spill/request-return/cleanup words, not a direct C match. All 76 installed
and older regression tests pass, including 4,180 complete stack/public fault
pairs and 88 stale-word/relocation rejections. Only 26 target ELF bytes change;
all other bytes/metadata/extents/data/CSV exact, original guard prefix intact.
Fresh Game 2,790/4,822, total 3,463/5,495, zero drift / 2,032 different.
One matching credit only, no conversion. README aggregate rows updated only.
Tools first, no push; older HEAD/22 fingerprints preserved, three absent-path
copies only. Next connected recovery: full 52-word func_1503D368 command-stream
relocator, still a zero-return placeholder. Loader guard elimination and
deeper helper/heap/hardware/renderer/gameplay acceptance remain separate.

Latest installed main resource-loader first-loop initialization improvement:
[Note 1265](WORKING_NOTES/1265-game-main-resource-loader-first-loop-delay-initialization-match-20261011.md):
same complete func_1503CF20 preserves 274 words/original 0x78 frame/S0..S6
and recovers the half-index store plus S1 zero in the first-loop branch delay.
Raw differences 24 -> 22, no guards/profile/ABI changes; not yet byte-exact.
Twelve installed/44 older/five historical tests pass, all reachable words/
public faults/native32/owner/padders/actual bounded chain. Only eight target ELF bytes change;
all other bytes/metadata/extents/data/guards/CSV exact. No credit, README
unchanged. Fresh Game 2,789/4,822, total 3,462/5,495, zero drift / 2,033
different; mounted tools b9eae47 banked first, no push.
Continue this same full routine's two spill slots, request-error
return and six cleanup register transfers; private faults/runtime separate.

Latest installed main resource-loader private-layout/count-schedule improvement:
[Note 1264](WORKING_NOTES/1264-game-main-resource-loader-private-layout-and-count-schedule-improvement-20261011.md):
complete func_1503CF20 keeps 274 words/original 0x78 frame/S0..S6 and recovers
request output +0x6C, boundary +0x68, half-index +0x4C, unmasked count store,
temporary-register cycle and event-opening order. Raw differences 98 -> 24,
no guards/profile changes; still not byte-exact. Twelve final tests and 32
fresh older loader tests pass, public faults/native32/owner/padders/actual
chain within documented bounds. Only 92 target ELF bytes change; every other
byte/extent/metadata/data/guard/CSV exact. No credit, README unchanged.
Five historical experiment tests pass; the exact remaining-word partition
is verified, with 250 words directly byte-exact and no broad normalization.
Fresh matching totals stay Game 2,789/4,822, total 3,462/5,495, zero address
drift / 2,033 different. Mounted tools 5a5e17e is banked; no push.
Continue this same full function's two spill slots, request-error return,
first-count delay initialization and cleanup register transfers.

Latest installed main resource-loader original-frame improvement:
[Note 1263](WORKING_NOTES/1263-game-main-resource-loader-original-frame-improvement-20261011.md):
complete func_1503CF20 retains all 274 words, restores original 0x78 frame,
saved S0..S6/early status and removes the redundant count-pointer stack copy.
Raw differences 271 -> 98, no guards/profile changes; not yet byte-exact.
Eleven final selected tests plus 21 fresh older loader tests pass, public
faults/native32/owner/padders/actual chain within documented helper bounds.
Only 882 target ELF bytes change; every other byte/extent/metadata/data/
guard/CSV exact. No credit, README aggregates unchanged, tools first/no push.
Mounted tools f8fac55 is banked; 46 diagnostic forms/five prior-experiment
tests and all tools checks pass, older 16 fingerprints/history preserved.
Continue this same complete function's private slots and remaining schedule.

Latest uninstalled main resource-loader status-join experiment:
[Note 1262](WORKING_NOTES/1262-game-main-resource-loader-status-join-experiment-20261011.md):
request-failure return join selects S6 under the unchanged retail profile;
31 complete candidates pass five new tests at isolated entries. No candidate
restores the original frame; keep the installed 274-word/0x80/271-difference
baseline. Eleven installed-loader tests pass freshly; the whole ELF/data/
guards/CSV and README are unchanged, no matching credit. Tools 9aa880b first,
older dirty work preserved, no push. Next: redundant count-pointer stack copy/reload,
original 0x78 frame/private layout and matching for this same full routine.

Installed complete main resource-loader retail-length improvement:
[Note 1261](WORKING_NOTES/1261-game-main-resource-loader-retail-length-improvement-20261011.md):
func_1503CF20 now emits all 274 slot words, frame 0x88 -> 0x80, raw
differences 273 -> 271, no guards/profile changes; still not byte-exact.
Recover mixed indexed/byte cursors and qualify ignored second-word scratch
reuse without installing cleanup pointer casts. Eleven final tests plus
ten fresh recovery tests pass, all reachable original/current words,
public faults/native32/actual five-routine chain within documented bounds.
Only 566 ELF bytes change: 565 target, one extent; every other byte,
14 neighbors/data/guards/CSV exact. WSL checks pass. Matching unchanged:
Game 2,789/4,822, total 3,462/5,495, zero drift / 2,033 different; no credit.
README aggregate rows stay unchanged. Tools e06635c first, older preserved,
no push. Continue this same full function's original 0x78 frame/S6 status
lifetime/private layout/scheduling; deeper runtime remains separate.

Previous complete main resource-loader semantic recovery, not yet matching:
[Note 1260](WORKING_NOTES/1260-game-main-resource-loader-recovery-20261011.md):
func_1503CF20 replaces its zero-return stub with complete publication,
both relocation loops, extras/event/helper gates and every failure rollback.
Qualified C emits 272 of 274 slot words, frame 0x88 versus retail 0x78,
273 raw word differences, no guards. Ten final tests pass: all 273 reachable
retail words (one unreachable duplicate compare), 1,800 fired public-access
fault pairs, ten effective controls and 12,096 native32 cases. A 768-case
actual parent/main/extras/relocator/buffer chain passes within documented
deeper-helper bounds. All 14 neighbors/data/guards/CSV exact; 828 ELF bytes
change only in target/extent/verified metadata ordering. WSL checks pass.
Matching totals unchanged: Game 2,789/4,822, total 3,462/5,495, zero drift,
2,033 different; no matching/conversion credit. Root README remains correct
and unchanged. Tools b503474 first, older dirty work preserved, no push.
Next: match this same full function's original 0x78 frame, saved S6 error
lifetime, stack layout and instruction schedule without dropping any path.
Deeper helper/heap/hardware/renderer/gameplay acceptance stays separate.

Previous complete resource-extras loader direct match:
[Note 1259](WORKING_NOTES/1259-game-resource-extras-loader-direct-match-20261011.md):
func_1503DC3C emits all 56 words/original 0x38 frame directly from complete
C, no guards. Preserve unsigned live count, 12-byte descriptors, publication
base reloads including self-aliasing stores, and exact 0x80000000 failure
sentinel. Ten final tests pass: all words reached, 936 fired fault pairs,
eleven effective IDO controls, 4,032 native32 cases and 6,144 connected cases
through actual 104-word caller/56-word extras/194-word buffer code.
Only 170 ELF bytes change: 169 target and one extent; every other byte,
all 14 neighbors/data/guards/CSV exact. WSL checks pass. Game 2,789/4,822
(57.84%), total 3,462/5,495 (63.00%), zero drift / 2,033 different; +1 matching
only. Tools 563924a first, no push, older dirty work preserved.
The then-open full main loader is semantically recovered in Note 1260;
its original frame/byte matching and deeper runtime remain separately open.

Previous complete resource-preparation caller direct match:
[Note 1258](WORKING_NOTES/1258-game-resource-preparation-caller-direct-match-20261011.md):
func_1503DA9C emits all 104 retail words/original 0x48 frame directly from
complete C, with no guards. Recover auxiliary/extras gates, unsigned descriptor
threshold, live count/list reloads and loader/helper failure propagation.
Ten final tests pass: all 104 words reached, 36,864 native32 cases, 3,200
fired fault pairs, ten effective IDO controls, both padders/all 14 neighbors,
and 4,608 cases through the actual 194-word buffer callee. Only 364 ELF bytes
change: 324 target, two extent, 38 existing metadata-order bytes; all other
code/data/names/values/guards/CSV exact. WSL checks pass. Game 2,788/4,822
(57.82%), total 3,461/5,495 (62.98%), zero drift / 2,034 different; +1 matching
only. Tools 160bba0 first, no push, older dirty work preserved.
The then-open full 56-word func_1503DC3C extras loader is directly matched
in Note 1259; main loader, deeper callbacks/heap/hardware/gameplay stay open.

Previous complete resource-buffer preparation guarded byte match:
[Note 1257](WORKING_NOTES/1257-game-resource-buffer-preparation-guarded-match-20261011.md):
func_15084044 now matches all 194 linked retail words/original 0x60 frame.
Complete semantic C has 29 raw differences after a qualified O32 scratch-word
lifetime recovery; 26 register-field guards and three copy-branch schedule
guards normalize them. This is guarded, not direct C matching. All fourteen
final tests pass, including high-bit pointer round trips and 116 fired stale
word/relocation rejections through both padders. Only 47 ELF bytes change
from Note 1256, all inside the target; every other byte/extent/data/CSV exact.
All old guard bytes preserved, only 29 target rows appended. Both WSL tools
checks pass; wider dependency rebuild retains unrelated source warnings.
Game 2,787/4,822 (57.80%), total 3,460/5,495 (62.97%), zero drift / 2,035
different; +1 matching only. Tools 8e07c9e first, no push, older work preserved.
The then-open complete 104-word caller is directly matched in Note 1258;
deeper loaders/hardware/gameplay remain open.

Previous resource-buffer retail-length improvement; matched in Note 1257:
[Note 1256](WORKING_NOTES/1256-game-resource-buffer-retail-length-improvement-20261011.md):
func_15084044 now emits all 194 retail words with the original 0x60 frame,
no guards; raw differences fall 130 -> 39. Recover mode-one reload joins
and mode-two cursor recomputation/initialization. Twelve final tests pass,
including all eleven prior semantic gates and a direct committed-recovery
delta audit. Exactly 317 ELF bytes change from Note 1255: 316 target bytes
and one extent byte (768 -> 776); every other ELF byte and all protected
inputs are identical. Both WSL tools checks pass; native older-mirror
check hits WinError 193, its WSL check and new-file py_compile pass.
Fresh totals unchanged: Game 2,786/4,822, total 3,459/5,495, zero drift;
no matching/conversion credit. Tools 2a4183d first, no push, older dirty
work preserved. Next: finish this function's opening register allocation
and mode-two copy/fallback branch; actual resource/hardware/gameplay open.

Previous complete resource-buffer preparation recovery; improved in Note 1256:
[Note 1255](WORKING_NOTES/1255-game-resource-buffer-preparation-recovery-20261011.md):
func_15084044 replaces its zero-return stub with all modes, sharing/counts,
allocation/copy and failure rollback. Semantic C emits 192 of 194 slot words
with the retail 0x60 frame, no new guards; 130 word differences remain.
Eleven final tests pass: 3,632 full fault pairs, 24,576 native32 cases,
rebases/aliases, actual wrapper/SDK copy and complete original caller within
explicit resource/callback bounds. All 30 neighbors/data/guards/CSV exact;
620 ELF bytes change only in target slot and size/existing symbol order.
Fresh matching totals unchanged: Game 2,786/4,822, total 3,459/5,495,
zero drift, no converted or matching credit. Tools 7f64ce9 first, no push;
older mirror preserved. Next: finish matching this same complete function.

Previous complete record-table identity selector direct match:
[Note 1254](WORKING_NOTES/1254-game-record-identity-selector-direct-match-20261011.md):
func_15083DA0 emits all 27 words directly from C, no frame/guards.
Preserve unsigned cached count/base, identity candidate 1, retail restart at
index one and final 0xFF cap. Nine final tests/both WSL tools checks pass:
131,646 reference guest runs, 434 all-access fault pairs plus four sampled
saturation faults, 133,120 native32 cases and complete retail caller identity
publication within bounded category-zero/scene-mask-zero paths. All 30
neighbors/data/guards/CSV exact; only target slot/12 -> 108 size changes,
77 ELF bytes. Game 2,786/4,822 (57.78%), total 3,459/5,495 (62.95%),
zero drift / 2,036 different; +1 matching only. Tools e2237b9 first,
no push, older mirror preserved. Next: full 194-word func_15084044 buffer
pair ownership/preparation; deeper caller/resources/hardware/gameplay open.

Previous complete actor-identity lookup; selector finished in Note 1254:
[Note 1253](WORKING_NOTES/1253-game-actor-identity-lookup-direct-match-20261011.md):
func_15083E90 emits all 72 words directly from C, no frame/guards.
Retail scans 26 slots (0..25), correcting the preceding handoff's 25-slot
assumption. Preserve byte selector/full argument home, word presence gates,
812-byte stride and first active identity match/NULL return. Ten final tests/
both WSL tools checks pass: 31,604 independent-reference guest runs, 402 full
fault pairs, 43,008 native32 cases, actual index/two-call linked callers and
retail caller with the banked record query. All 30 neighbors/data/guards/CSV
exact; only target ELF slot/16 -> 288 size changes, 226 bytes. Game
2,785/4,822 (57.76%), total 3,458/5,495 (62.93%), zero drift / 2,037
different; +1 matching only. Tools 69e37a6 first, no push, older mirror
preserved. Next: full 27-word func_15083DA0 record-table identity selector;
actual initializer/hardware/gameplay acceptance remains open.

Previous complete record-index query and corrected census; lookup finished in Note 1253:
[Note 1252](WORKING_NOTES/1252-game-record-index-query-direct-match-and-census-20261011.md):
func_15083E0C emits all 33 words directly from C, no frame or guards.
Recover byte selector, zero/-1 sentinels, cached 48-byte record traversal,
first identity match and pointer-difference return. Ten final tests/both WSL
tools checks pass: 23,088 reference guest runs, 584 fired full fault pairs,
10,240 native32 cases and complete retail caller connection (current C caller
remains a stub). Fix omitted layout boundary and tracked Splat defined symbol;
one previously omitted C function is counted, not an asm conversion. Only
102 ELF bytes change in target slot/size/section; 30 neighbors/data/guards
exact. Converted 5,495/6,044, Game 4,822/5,323; converted bytes unchanged.
Matching Game 2,784/4,822 (57.74%), total 3,457/5,495 (62.91%), zero drift /
2,038 different. Tools 630eaf9 first, no push, older dirty mirror preserved.
Next: full 72-word func_15083E90 actor-identity lookup; actual runtime open.

Previous complete descriptor-driven child cleanup; query finished in Note 1252:
[Note 1251](WORKING_NOTES/1251-game-animation-child-cleanup-direct-match-20261011.md):
func_150836CC emits all 66 words/original 0x30 frame directly from C,
no guards. Recover reset-before-lookup, cached records, live descriptor count,
signed parent-slot division and gated child cleanup. Nine final tests/both
tools checks pass: 866 full fault pairs, 8,192 native32 cases, rebases,
both production padding routes and actual complete two-call caller. All 30
neighbors/data/guards/CSV exact; only target ELF slot/extent changes. Game
2,783/4,821 (57.73%), total 3,456/5,494 (62.90%), zero drift / 2,038
different; +1 matching only. Tools 71822b6 first, no push, older mirror
preserved. Next: full 33-word func_15083E0C record-index query; runtime open.

Previous complete animation-state allocation direct match; cleanup finished in Note 1251:
[Note 1250](WORKING_NOTES/1250-game-animation-state-allocation-direct-match-20261011.md):
func_150838EC emits all 51 words/original 0x28 frame directly from C,
no new guards. Recover table gates, NULL result store/failure return, 64-byte
clear and typed float delegation. The cleaner typed constructor call preserves
its complete 182-word fingerprint. Ten final tests/both tools checks pass,
2,894 modeled full fault pairs, 32,768 native32 cases and actual constructor/
initializer/resource-helper connections. All 30 neighbors/guard fingerprints/
data/CSV exact; only target ELF slot/extent changes. Game 2,782/4,821 (57.71%),
total 3,455/5,494 (62.89%), zero drift / 2,039 different; +1 matching only.
Tools ed89891 first, no push, older dirty mirror preserved. Next: full
66-word func_150836CC descriptor-child cleanup; actual runtime open.

Previous complete actor resource-field initializer direct match; next helper finished in Note 1250:
[Note 1249](WORKING_NOTES/1249-game-actor-resource-fields-direct-match-20261011.md):
func_150839B8 emits all 68 words/original 0x18 frame directly from C,
no new guards. Recover three-argument void ABI, full-word identity gate,
optional configuration/world override, ordered field copies and live count
reloads. Nine final tests/both tools checks pass, including 1,265 full fault
pairs, 16,384 native32 cases and actual complete constructor calls. All 30
neighbors/guard fingerprints/data/CSV exact; only target ELF slot and extent
change. Game 2,781/4,821 (57.69%), total 3,454/5,494 (62.87%), zero drift /
2,040 different; +1 matching only. Tools 83ade71 first, no push, older dirty
mirror preserved. Next: full 51-word func_150838EC; actual runtime open.

Previous complete child actor constructor byte match; next initializer finished in Note 1249:
[Note 1248](WORKING_NOTES/1248-game-child-actor-constructor-byte-match-20261011.md):
func_15083AC8 matches all 182 words/original 0x38 frame with unchanged
semantic C and checked closed frame/base/register/scheduling normalization.
All 182 raw words/22 relocations guarded; 125 changed words, 57 identity
checks, no inserts/omissions. Thirteen final tests/both tools checks pass:
public/native32/actual caller-helper and private frame/2,214 full fault pairs
qualify. All 30 neighbors/other ELF/metadata/data/CSV unchanged, old manifest
prefix preserved. Game 2,780/4,821 (57.66%), total 3,453/5,494 (62.85%),
zero drift / 2,041 different; +1 matching only. Tools a9694bd first, no push,
older dirty mirror preserved. Next: full 68-word func_150839B8 resource-field
initializer. Raw C still 182/0x50 with 125 differences, not direct exact;
actual deeper resource/hardware/gameplay acceptance remains open.

Previous complete child actor constructor recovery; matching finished in Note 1248:
[Note 1247](WORKING_NOTES/1247-game-child-actor-constructor-reconstruction-20261011.md):
func_15083AC8's nine-argument zero placeholder is replaced with all 182 C
words: parent/status/scale fields, live inclusive allocation loop and cached
global-toggle bracket. Full C fits without guards but frame 0x50 versus retail
0x38 and 125 linked differences remain. Nine final tests/both tools checks
pass, including 390 public fault pairs, 36,864 native32 cases and actual
89-word caller/70-word resource helper with eight linked descriptors. All 30
neighbors/other ELF/data/guards/CSV unchanged, both adjacent placeholders
preserved. Matching stays Game 2,779/4,821 (57.64%), total 3,452/5,494
(62.83%), zero drift / 2,042 different; no extra credit. Tools 03d8ec2 first,
no push, older dirty mirror preserved. Next: this constructor's original
frame/register schedule and private fault order; actual resources/gameplay open.

Previous complete animation scratch preparation byte match:
[Note 1246](WORKING_NOTES/1246-game-animation-scratch-preparation-byte-match-20261011.md):
func_1502D824 matches all 191 words/original 0x68 frame. Existing full semantic
C is unchanged; 187 expectation rows protect the complete compiler fingerprint,
46 changed words/four inserts normalize closed frame/constants/registers and
branch schedules. Thirteen final tests and both tools checks pass; 912 fitted/
retail full-access fault pairs, independent private-frame contract, native32,
rebased helpers and actual refresh/caller qualify. All 37 neighbors/other ELF/
data/CSV exact; old guard prefix retained. Game 2,779/4,821 (57.64%), total
3,452/5,494 (62.83%), zero drift / 2,042 different; +1 matching credit only.
Tools 672c03d first, no push, older dirty mirror preserved. Next: full 182-word
func_15083AC8 constructor; timeline matching and actual resource/PI/hardware/
renderer/gameplay acceptance remain open. Raw C still 187/0x50, not direct exact.

Previous animation scratch loop matching improvement:
[Note 1245](WORKING_NOTES/1245-game-animation-scratch-loop-shape-improvement-20261011.md):
func_1502D824 now uses retail's guarded do-loop shape. Full unguarded C emits
187 words / 0x50 frame, reducing raw/linked differences 162 -> 102 against
retail 191 / 0x68. Ten final tests and both tools checks pass; ordered public
aliases/faults, 24,576 native32 runs and actual refresh/caller connections
requalified. Only target slot/extent changes, all 37 neighbors/other ELF/data/
guards/CSV exact; caller stays exact. Matching totals unchanged, no credit.
Tools 995fcc3 first, no push, older dirty mirror preserved. Original matching
and fitted private fault order are completed in Note 1246; actual PI/hardware
and full renderer/gameplay stay open.

Previous complete animation scratch preparation restored; matching remains open:
[Note 1244](WORKING_NOTES/1244-game-animation-scratch-preparation-reconstruction-20261011.md):
func_1502D824's zero placeholder is replaced with full semantic C for one/two
banks, frame/stride selection, aligned PI packets and wrap copies. C emits
188 words / 0x50 frame against retail's 191 / 0x68; 162 linked word
differences remain, no new guards or matching/converted credit. Ten final
tests, nine scoped submit regressions and both tools checks pass, including
24,576 native32 runs, ordered public aliases/faults, actual 33-word refresh
and complete 66-word caller connections. Private frame/fault order, invalid
float conversions, actual PI/hardware and full renderer/gameplay stay open.
Only preparation slot/extent changes in ELF; 37 neighbors, all other ELF/data/
CSV exact. Correct typed void caller declaration retires three superseded
base guards; the submit stays byte-exact with two placement guards, all four
owner routines exact. Game 2,778/4,821, total 3,451/5,494, zero drift /
2,043 different unchanged. Tools ee484d7 first, no push, older dirty mirror
preserved. Original frame/word match is completed in Note 1246.

Previous complete node transform submission restored and byte-exact:
[Note 1243](WORKING_NOTES/1243-game-node-transform-submission-byte-match-20261011.md):
func_1503F4B0 replaces the last zero placeholder in this owner with all 66
words/original 0x48 frame. Five checked terminator-placement/closed-base
guards; no inserts/omissions. Ten final target tests, nine scoped alternate
behavior regressions and both tools checks pass. Live selector/count reloads,
NULL temporary preparation, eight-word transform packet and unconditional
typed timeline call qualify. Actual retail/current timeline helpers execute
in bounded finite/null-actor cases; current helper still has 237 differences.
Three authentic call windows use synthetic wrappers, not complete callers.
All four owner routines now exact; only target slot/extent changes, all other
ELF/data/CSV and old guard prefix retained. Game 2,778/4,821 (57.62%), total
3,451/5,494 (62.81%), zero drift / 2,043 different; +1 matching credit only.
Tools e999db1 first, no push; older dirty mirror preserved. The full
preparation body is restored in Note 1244; its byte matching remains open. Full 182-word
func_15083AC8, timeline matching and resource/allocator/hardware/gameplay stay open.

Previous complete alternate node resource loader restored and byte-exact:
[Note 1242](WORKING_NOTES/1242-game-complete-node-alternate-loader-byte-match-20261011.md):
func_1503F62C replaces its zero placeholder with all 99 words/original 0x40
frame; 24 checked closed S0/S1 guards, no inserts/omissions. Ten final target
tests, 17 scoped regressions and both tools checks pass. Real initializer/
default/action chain, live attachment/count reloads and inverted NULL-free
gates qualify; unwritten count on nested failure is a guest-only boundary.
Three neighbors/all other ELF/data/CSV exact; old guard prefix retained.
Game 2,777/4,821 (57.60%), total 3,450/5,494 (62.80%), zero drift /
2,044 different; +1 matching credit only. Tools 030412c first, no push;
older dirty mirror preserved. Full 66-word follow-up completed in Note 1243.
Full 182-word func_15083AC8 and actual resource/allocator/gameplay stay open.

Previous complete default node resource loader emits directly from C:
[Note 1241](WORKING_NOTES/1241-game-complete-node-resource-loader-direct-byte-match-20261011.md):
func_1502FE10 replaces its zero placeholder with all 114 words/original 0x50
frame, no guards. Ten final tests/both tools checks pass; live record/count
loop, retained-cache rollover, native32 and actual initializer consuming real
source outputs qualify. All 39 neighbors/other ELF/data/guards/CSV exact;
+1 matching credit only. Game 2,776/4,821 (57.58%), total 3,449/5,494
(62.78%), zero drift / 2,045 different. Tools daabcf7 first, no push; older
dirty mirror preserved. Next: full 99-word func_1503F62C alternate loader;
its ignored nested status/unwritten output and NULL-free branches need explicit
qualification. Complete resource/allocator and hardware/live gameplay stay open.

Latest complete node release restored and byte-exact:
[Note 1240](WORKING_NOTES/1240-game-complete-node-release-byte-match-20261011.md):
func_15030158 replaces its zero placeholder with all 102 semantic words,
original 0x20 frame and five closed register-transfer guards; full memory/call
order preserved. Ten final tests and both tools checks pass, including 97,280
native32 runs, actual 134-word dispatcher and factory/initializer rollback.
All 39 neighbors and other ELF/data/CSV bytes exact; +1 matching credit only.
Game 2,775/4,821 (57.56%), total 3,448/5,494 (62.76%), zero drift /
2,046 different. Tools 088efd4 first, no push; older dirty mirror preserved.
Next: full 114-word func_1502FE10, whose zero stub lacks required success
outputs. Complete resource/allocator work and hardware/live gameplay stay open.

Latest complete node resource initializer restored and byte-exact:
[Note 1239](WORKING_NOTES/1239-game-complete-node-resource-initializer-byte-match-20261011.md):
func_1502FFD8 replaces its zero placeholder with all 96 semantic words,
original 0x40 frame and 12 checked read-schedule/register/delay-mask guards.
Ten final tests and both tools checks pass; both seven-argument loaders,
paired allocation/copy/rollback, 25,604 native32 runs and actual caller/
factory/action connection with eight retail samples qualify. All 39 neighbors
and other ELF/data/CSV bytes exact; +1 matching credit only. Game 2,774/4,821
(57.54%), total 3,447/5,494 (62.74%), zero drift / 2,047 different.
Tools 8ec8484 first, no push. Deeper zero loaders do not satisfy the required
success-output contract; cleanup and hardware/live gameplay remain open.
Next: full 102-word func_15030158.

Latest complete animation node constructor restored and byte-exact:
[Note 1238](WORKING_NOTES/1238-game-complete-animation-node-constructor-byte-match-20261010.md):
func_15030AF4 replaces its zero placeholder with all 152 semantic words,
original 0x30 frame and 47 checked initialization-scheduling/register guards.
Ten final tests and both tools checks pass; typed thirteen-argument ABI,
nullable allocations/rollback decisions, 528,384 native32 runs, actual
89-word caller and 113-word action consumer/eight retail samples qualify.
All 39 neighbors and other ELF/data/symbol bytes are exact; only target
slot/extent changes. Conversion CSV unchanged; +1 matching credit only.
Game 2,773/4,821 (57.52%), total 3,446/5,494 (62.72%), zero drift /
2,048 different. Tools d2ad015 first, no push. Next: full 96-word
func_1502FFD8; resource/cleanup stubs and hardware/live gameplay remain open.

Latest complete actor animation constructor restored and byte-exact:
[Note 1237](WORKING_NOTES/1237-game-complete-actor-animation-constructor-byte-match-20261010.md):
func_15083568 replaces its zero placeholder with all 89 semantic words,
original 0x68 frame and 17 checked register/scheduling guards. Nine final
tests and both tools checks pass; actual record-caller/helper chain, native32,
live count and eight ROM-verified descriptor samples qualify. Explicit
func_15083AC8 ABI correction emits four home stores but remains a zero stub;
29 other neighbors and all remaining ELF/data/symbol bytes are unchanged.
Conversion CSV is byte-identical; +1 matching credit only. Game 2,772/4,821
(57.50%), total 3,445/5,494 (62.70%), zero drift / 2,049 different.
Tools 975e23b first, no push. Next: full 152-word func_15030AF4;
both deeper helper restorations and hardware/live gameplay remain open.

Earlier actor animation request converted directly to byte-exact C:
[Note 1236](WORKING_NOTES/1236-game-actor-animation-request-direct-conversion-20261010.md):
func_1507EA44 emits all 30 words / original 0x18 frame without guards.
Nine final tests and both tools checks pass: exact signed-integer/single-float
O32 packet, live reloads, native32 and actual record caller/lookup/list/classifier
chain qualify. Whole ELF/guards/data/symbols/14 neighbors unchanged; only one
asm-to-c row changes: +1 converted function / 120 bytes and +1 matching credit.
Game 2,771/4,821 (57.48%), total 3,444/5,494 (62.69%), zero drift / 2,050 different.
Conversion totals: 5,494/6,043 and Game 4,821/5,322. Tools da7086a first,
no push. Next: full 89-word func_15083568, still a zero-return C placeholder;
its actual body, FCSR/hardware and live gameplay acceptance remain open.

Earlier actor definition count converted directly to byte-exact C:
[Note 1235](WORKING_NOTES/1235-game-actor-definition-count-direct-conversion-20261010.md):
func_1507E968 emits all 32 words / original 0x18 frame without guards.
Ten final tests and both tools checks pass, including actual channel/count/
lookup/classifier/list chain and original animation bytes. Whole ELF,
guards/data/symbols and 14 neighbors unchanged; only one asm-to-c row changes:
+1 converted function / 128 bytes and +1 matching credit. Game 2,770/4,820
(57.47%), total 3,443/5,493 (62.68%), zero drift / 2,050 different.
Conversion totals: 5,493/6,043 and Game 4,820/5,322. Tools 2c8eae2 first,
no push. Next: full 30-word func_1507EA44; animation/finish/runtime remain open.

Earlier actor definition lookup converted directly to byte-exact C:
[Note 1234](WORKING_NOTES/1234-game-actor-definition-lookup-direct-conversion-20261010.md):
func_1507E908 emits all 24 words / original 0x18 frame without guards.
Nine final tests and both tools checks pass; actual classifier/channel caller,
full-word indices, aliases/faults and native32 callbacks qualify. Whole ELF,
guards/data/symbols and 14 neighbors unchanged; only one asm-to-c row changes:
+1 converted function / 96 bytes and +1 matching credit. Game 2,769/4,819
(57.46%), total 3,442/5,492 (62.67%), zero drift / 2,050 different.
Conversion totals: 5,492/6,043 and Game 4,819/5,322. Tools 6bc9c5a first,
no push. Next: full 32-word func_1507E968; other callbacks/runtime remain open.

Earlier complete actor channel arbitration converted to byte-exact C:
[Note 1233](WORKING_NOTES/1233-game-complete-actor-channel-transition-conversion-20261010.md):
func_1507E7E4 matches all 73 words / original 0x30 frame with five checked
register/equality guards. Nine final tests and both tools checks pass. All
code/data and 14 neighbors are unchanged; only two ELF symbol-section bytes
change after removing its stale absolute assignment. Recover its omitted map
boundary: +1 counted/converted function, +292 C bytes, +1 matching credit.
Game 2,768/4,818 (57.45%), total 3,441/5,491 (62.67%), zero drift / 2,050 different.
Tracked Splat defined-symbol declaration prevents regenerated stale overrides.
Corrected conversion totals: 5,491/6,043 and Game 4,818/5,322. Tools 4da6c0b
first, no push. Next: full 24-word func_1507E908; deeper callbacks/runtime remain open.

Earlier actor channel reset converted directly to byte-exact C:
[Note 1232](WORKING_NOTES/1232-game-actor-channel-reset-direct-conversion-20261010.md): func_1507EABC emits all 28 words, original 0x20 frame,
without guards. Ten post-install tests and both tools checks pass; whole ELF,
guards/data and all 14 owner neighbors unchanged. Only its asm-to-c row changes:
+1 converted function / 112 bytes and +1 matching credit. Game 2,767/4,817
(57.44%), total 3,440/5,490 (62.66%), zero drift / 2,050 different.
Tools 8355983 first, no push. Next: complete 73-word func_1507E7E4, including
priority !=3; current actual helper proof is its priority-3 context only.

Earlier complete actor resource transition installed byte-exact:
[Note 1231](WORKING_NOTES/1231-game-complete-actor-resource-transition-byte-match-20261010.md): func_150837D4 matches all 70 words, original 0x30 frame,
with 15 checked register/common-epilogue guards. Nine post-install tests and
both tools checks pass; only its 280-byte slot/extent changes. Data/conversion
rows and guard prefix exact. Game 2,766/4,816 (57.43%), total 3,439/5,489
(62.65%), zero drift / 2,050 different. Tools 49e2558 first, no push.
Next: full 28-word func_1507EABC; actual callbacks/runtime acceptance stay open.

Earlier complete actor animation selector installed byte-exact:
[Note 1230](WORKING_NOTES/1230-game-complete-actor-animation-selector-byte-match-20261010.md): func_1502FBE8 matches all 98 words, original 0x40 frame,
with 14 qualified register/spill/schedule guards. Nine post-install tests and
both tools checks pass; only its 392-byte slot/extent changes. Prior guard
prefix/data/conversion rows exact. Game 2,765/4,816 (57.41%), total
3,438/5,489 (62.63%), zero drift / 2,051 different. Tools 0474fdc first, no push.
Next: full 70-word func_150837D4; callbacks/runtime acceptance remain separate.

Earlier complete tile updater and actual special helper installed byte-exact:
[Note 1229](WORKING_NOTES/1229-game-complete-tile-updater-and-special-helper-byte-match-20261010.md): func_1502F9FC matches all 123 words with 120 checked guards;
func_150C3160 emits all 52 words directly from C, no guards. Eight post-install
tests and root tools-check pass. Only two linked slots/extents change, 700 bytes;
old guard prefix/data/conversion rows exact. Game 2,764/4,816 (57.39%), total
3,437/5,489 (62.62%), zero drift / 2,052 different. Tools 041a6fa first, no push.
Next: recover complete 98-word func_1502FBE8; keep separate runtime/FCSR gates.

Earlier complete texture-tile updater scheduling qualification, not installed then:
[Note 1228](WORKING_NOTES/1228-game-actor-texture-tile-updater-qualified-schedule-and-padding-20261010.md): full func_1502F9FC now fits all 123 retail words.
Complete C emits 120 words, original 0x20 frame; retain every producer and copy
three address/move producers, no omitted behavior or missing-body padding.
Pass three-form memory/order, 518 fired prefixes, 12 rebased links, every word/
relocation stale gate, native SDK and actual renderer boundary checks.
All 17 scheduling/install regressions pass; production/counts unchanged.
Tools f2dd1c3 first, no push. Next: execute actual 52-word special helper,
then install/rebuild/audit. Bounded helper model is not that gate's completion.

Latest complete texture-tile updater recovery, not installed:
[Note 1227](WORKING_NOTES/1227-game-actor-texture-tile-updater-recovery-and-layout-gates-20261010.md): recover full func_1502F9FC semantic C.
Retail is 123 words / 492 bytes; selected C is 111 words, original 0x20 frame,
118 word differences. Nine new tests plus eight installation regressions pass.
Cover all types/words, 85 aliases, 518 fired fault pairs, 40,960 native SDK
executions and 88 complete actual-caller cases. Copied owner's 37 neighbors
exact; production/counts unchanged. Tools c5df5cc first, no push.
Layout/rebase/stale gates are closed in Note 1228; actual special helper and installation remain open.

Latest installed color provider and complete actor renderer byte match:
[Note 1226](WORKING_NOTES/1226-game-actor-color-provider-and-complete-renderer-byte-match-20261010.md): install complete func_1502CC34 and func_1502CCFC.
All 50 color words emit directly from C; full 532-word renderer uses its
certified 531 guards. Eight post-install tests and tools-check pass; only
2,328 target bytes/two symbol extents change, old guard prefix and data exact.
Game 2,762/4,816 (57.35%), total 3,435/5,489 (62.58%), zero drift / 2,054
different. Tools cc74178 first, no push; bounded callbacks/hardware remain open.

Latest complete actor renderer actual color/matrix connections, not installed:
[Note 1225](WORKING_NOTES/1225-game-complete-actor-renderer-actual-color-and-matrix-connections-20261010.md).
326 renderer and 168 complete caller cases execute actual color/fog and both
matrix chains; all 21 connected/native/schedule tests pass. Original/fitted
private bytes/order are exact; raw comparison adjusts proven saved PCs only.
Production/counts unchanged. Tools baacebd first, no push. Next: recover the
still-empty 50-word color provider before combined owner installation/audit.

Earlier complete actor renderer native32 SDK qualification, not installed:
[Note 1224](WORKING_NOTES/1224-game-complete-actor-renderer-native32-sdk-qualification-20261010.md).
330 complete cases at -O2/-O0 pass with actual SDK graphics macros; four
effective negatives and explicit pointer/scalar provenance checks pass.
All 13 native/schedule tests pass; production and matching counts unchanged.
Tools e5f59e3 first, no push. Next: complete actual renderer/helper-chain
qualification, then installation and fresh linked audit.

Earlier complete actor renderer certified schedule/padding, not installed:
[Note 1223](WORKING_NOTES/1223-game-complete-actor-renderer-certified-schedule-and-padding-20261010.md).
Full func_1502CCFC now fits all 532 words with original 0x150/private homes.
531 guards normalize 122 words, insert two existing branch/read copies and
omit only the redundant emitted mask. Eight tests pass: complete private order,
actual whole-owner padding, nine links and every stale dependency. Production
and matching counts stay unchanged. Tools e59626e first, no push. Next:
native32 SDK and complete actual dispatcher/RGB/shading/renderer/helper chain.

Earlier complete actor renderer original private layout, not installed:
[Note 1222](WORKING_NOTES/1222-game-complete-actor-renderer-original-private-layout-20261010.md).
Full func_1502CCFC now emits original 0x150 frame and all ten exact color homes.
Eight tests pass: 273 full private/public cases, 16 aliases, 1,963 fired fault
prefix pairs, six links and 37 exact neighbors. Raw remains 531/532 words;
production/counts unchanged. Tools 755a04d first, no push. Next: close full
instruction layout, actual padding, native32 SDK and complete real-helper chain.

Earlier complete actor renderer recovery, not installed:
[Note 1221](WORKING_NOTES/1221-game-complete-actor-renderer-recovery-and-private-layout-gates-20261010.md).
Full eight-argument func_1502CCFC: all 532 retail words exercised. Nine tests
pass: 273 cases, eight effective negatives, six links and 37 exact neighbors.
Public semantics/order agreed; that candidate's 0x148 frame and color homes
differed from retail. Note 1222 closes frame/private qualification without
installing the renderer; full layout and connected gates remain open.
Tools 4d76cac first; no push, matching credit or hardware/live claim.

Latest complete actor alpha-shading byte match:
[Note 1220](WORKING_NOTES/1220-game-actor-alpha-shading-byte-match-20261010.md).
Restore full func_1502D630: 125 words / original 0x58 frame and private outputs.
121 closed guards normalize 16 words and insert four existing constant/setup
producers; no missing-body padding. Nine tests pass before/after: 358 verified
fault prefixes, 203,972 native32 cases and 168 real dispatcher/RGB/shading/
58-word matrix-chain connections. Only target 500-byte slot/symbol extent
changes; 37 neighbors, old guard prefix, conversion rows and data exact.
Game 2,760/4,816 (57.31%), total 3,433/5,489 (62.54%), zero drift / 2,056
different. Tools 89e8ece first; no push. Next: complete 532-word eight-argument
renderer func_1502CCFC. Hardware/FCSR/live acceptance remains separate.

Latest direct actor RGB parameter match:
[Note 1219](WORKING_NOTES/1219-game-actor-rgb-parameter-writer-direct-match-20261010.md).
Restore full frame-free func_1502D54C: all 57 words directly from C, no guards.
Nine tests pass before/after: 1,683 guest cases, 1,248 aliases, 115 verified
fault prefixes, 399,872 native32 cases and 336 real dispatcher connections.
Only target 228-byte slot/symbol extent changes; 37 neighbors, guards,
conversion rows and protected data exact. Game 2,759/4,816 (57.29%), total
3,432/5,489 (62.53%), zero drift / 2,057 different. Tools b216274 first.
Next: full 125-word shading/alpha callback func_1502D630, including its actual
matrix-helper contract. Renderer and hardware/live acceptance remain separate.

Latest complete actor render-dispatch byte match:
[Note 1218](WORKING_NOTES/1218-game-actor-render-dispatch-byte-match-20261010.md).
Restore full func_1502C974: 176 words / original 0x58 frame and private homes.
177 complete guards normalize 111 words and omit only the redundant emitted
shift mask; portable C retains masking. Fifteen tests pass before/after:
2,160 guest cases, 590 complete fault prefixes, 144 private aliases,
1,491,048 native32 cases and complete banked 173-word parent connections.
Only target 704-byte slot/symbol extent changes; all 37 neighbors, old guard
prefix, conversion rows and protected data exact. Game 2,758/4,816 (57.27%),
total 3,431/5,489 (62.51%), zero drift / 2,058 different. No push.
Next: full 57-word RGB parameter callback func_1502D54C; remaining render
callbacks and hardware/live qualification are separate.

Prior actor render-dispatch lifetime checkpoint:
[Note 1217](WORKING_NOTES/1217-game-actor-render-dispatch-lifetime-and-private-counterexamples-20261010.md).
Measure 62 full/profile bodies; an explicit overflow flag restores nonvolatile
actor-in-a3 lifetime. Scoped flag reaches 176 words but keeps a 0x60 frame.
Four tests pass: 19,344 candidate executions, three native32 forms and 64
verified private-fault executions. All 31 O2/g3 public traces agree; O1/g3
wide-view ABI mismatches and wrong private callback homes remain recorded.
Original ten-test recovery suite also passes. Tools 2b91082 first; production
and matching totals unchanged. Continue the same caller's original homes,
complete schedule and private qualification before installation.

Latest complete actor render-dispatch semantic recovery:
[Note 1216](WORKING_NOTES/1216-game-actor-render-dispatch-recovery-and-layout-gates-20261010.md).
Full five-argument func_1502C974 preserves early gates, two alpha queries,
ordered parameter callbacks, signed factor product and fresh cursor rollback.
Ten tests pass in 20.258s: 2,160 public guest cases, 2,228 factor/cursor cases,
63 public fault prefixes, 1,491,048 native32 cases, seven effective negatives
and 60 complete-caller connections to banked selector/distance/identity bodies.
All 37 owner neighbors/pools and production source/ELF/guards/data unchanged.
Not installed: initial form is 162 words / 0x60 frame; volatile-actor form
recovers 0x58 but remains 167 words with wrong private homes. Retail needs 176.
Tools 3dba67b first. Matching totals stay Game 2,757/4,816 (57.25%), total
3,430/5,489 (62.49%). Next remains this full caller: recover physical homes
and complete extent, then qualify private aliases/faults before installation.

Latest actor distance-tier updater byte match:
[Note 1215](WORKING_NOTES/1215-game-actor-distance-tier-updater-byte-match-20261010.md).
Complete typed func_1502C6E8 matches all 163 words and original 0x50 frame
through 163 closed guards, 33 changed words and no insertions/omissions.
The actor selector caps tiers; signed view only selects the player record.
Eleven tests pass before/after, final 20.308s: 2,303 guest cases, 430 fault
prefixes, 1,437,800 native32 cases and seven effective negatives. Actual
11-word identity leaf qualifies; update callback is bounded opaque and the
four-instruction caller receipt is not complete caller acceptance.
Only target 652-byte slot/symbol extent changes; old guard prefix, 37 neighbors,
conversion rows and protected data exact. Game 2,757/4,816 (57.25%), total
3,430/5,489 (62.49%), zero drift / 2,059 different. Tools 6c5b8a4 first.
Next: complete 176-word caller func_1502C974; preserve separate curve gates
and hardware/live boundaries.

Latest actor counter-updater direct byte match:
[Note 1214](WORKING_NOTES/1214-game-actor-counter-updater-byte-match-20261010.md).
Complete void/slot func_1502C608 emits all 56 words and original 0x28 frame
directly, without guards. Ten tests pass before/after, final 10.830s: 4,330
guest cases, 162 fault prefixes, 1,992,704 native32 cases, six effective
negatives and actual banked 88-word dispatcher/19-word classifier connections.
Only target 224-byte slot/symbol extent changes; guards, 37 neighbors,
conversion rows and protected data unchanged. Game 2,756/4,816 (57.23%),
total 3,429/5,489 (62.47%), zero drift / 2,060 different. Tools 0483bc8 first.
Next: 163-word distance-tier updater func_1502C6E8; preserve separate curve
rejection gates and hardware/live boundaries.

Latest actor attachment-updater byte match:
[Note 1213](WORKING_NOTES/1213-game-actor-attachment-updater-byte-match-20261010.md).
Complete void/slot func_1502F264 matches all 89 linked words and original leaf
ABI through 89 closed guards, 29 changed words and no insertions/omissions.
Preserve one-based attachment lookup, raw float copies, fresh flags, repeated
halfword access and signed inclusive limit reloads. Twelve tests pass before/
after, final 22.409s: 14,106 guest cases, 1,428 fault prefixes, 319,488 native32
cases, eight effective negatives and 320 actual banked dispatcher/updater
connections. Only target 356-byte slot/symbol extent changes; old guards,
37 neighbors, conversion rows and protected data unchanged. Game 2,755/4,816
(57.21%), total 3,428/5,489 (62.45%), zero drift / 2,061 different.
Tools 9f1e85e first. Next: 56-word state-2 counter updater func_1502C608;
preserve separate uninstalled curve gates and hardware/live boundaries.

Latest actor segment-selector byte match:
[Note 1212](WORKING_NOTES/1212-game-actor-segment-selector-byte-match-20261010.md).
Complete typed func_1502F01C matches all 146 linked words and original 0x88
frame/private homes through 144 closed guards, 40 changed rows, three producer
insertions and one certified NOP omission. Twelve tests pass before/after,
final 75.781s: 5,228 full fault prefixes, 425,984 native32 cases and actual
banked override/animation-reader connections. Forty-eight literal call-site
cases qualify cursor/slot forwarding, not the complete placeholder caller.
Only target 584-byte slot/symbol extent changes; old guards, 37 neighbors,
conversion rows and protected data unchanged. Game 2,754/4,816 (57.18%),
total 3,427/5,489 (62.43%), zero drift / 2,062 different. Tools 35a4757 first.
Next: 89-word attachment updater func_1502F264; preserve separate curve gates.

Latest actor segment-selector semantic recovery:
[Note 1211](WORKING_NOTES/1211-game-actor-segment-selector-recovery-and-layout-gates-20261010.md).
Complete diagnostic C for func_1502F01C preserves cached/reloaded actor IDs,
NULL retry/retained override pair and four ordered SDK segment writes. Nine
tests pass: 1,013 boundary/mutation cases, 420 aliases, 494 public fault prefixes,
425,984 native32 cases and both actual banked override callees. All 37 copied-
owner neighbors/pools and production source/ELF/guards/data remain unchanged.
Not installed: selected body has 149 words / 0x90 frame instead of 146 / 0x88,
with 135 isolated-link differences. Recover physical homes and closed layout
before installation. The retail caller is func_1502CCFC, not func_1502C974;
its current source is a placeholder, not a qualified complete banked caller.
Matching totals stay Game 2,753/4,816 (57.16%), total 3,426/5,489 (62.42%).

Latest slot byte-updater byte match:
[Note 1210](WORKING_NOTES/1210-game-slot-byte-updater-byte-match-20261010.md).
Complete void func_1502EEF4 replaces its zero-return stub; all 74 linked words
match with 74 closed guards, 27 changed words and no insertions or omissions.
Original 0x30 frame/saved homes, slot ABI, two byte gates and callback-sensitive
reloads qualify. Eleven tests pass before/after: 7,664 guest cases, 450 fault
prefixes, 239,616 native32 cases, actual banked classifier/flag-helper and
dispatcher connections. Only target 296-byte slot/symbol extent changes;
old guard prefix, all 37 owner neighbors, conversion rows and data unchanged.
Game 2,753/4,816 (57.16%), total 3,426/5,489 (62.42%), zero drift /
2,063 different. Next: 146-word segment selector func_1502F01C; preserve curve gates.

Latest object phase-updater byte match:
[Note 1209](WORKING_NOTES/1209-game-object-phase-updater-byte-match-20261010.md).
Complete func_1502EAFC replaces its zero-return stub; all 78 linked words match
with 75 closed dependency guards, three insertions and the original leaf ABI.
Ten tests pass before/after: 7,868 guest cases, 168 fault prefixes, 720,896
native32 cases and actual banked dispatcher connections. A fresh renderer/
adapter regression also passes. The new compact switch shifts the neighboring
color table by 24 bytes; one existing expected-addend field is requalified,
while its padded/linked code stays unchanged. Whole ELF changes only the
312-byte target slot/symbol extent; conversion rows and protected data remain
exact. Game 2,752/4,816 (57.14%), total 3,425/5,489 (62.40%), zero drift /
2,064 different. Next: 74-word slot updater func_1502EEF4; preserve curve gates.

Latest object color-mode helper byte match:
[Note 1208](WORKING_NOTES/1208-game-object-color-mode-helper-byte-match-20261010.md).
Complete func_1502EC34 replaces its zero-return stub; all 150 linked words
match with 148 dependency guards and two inserted lifetime/scheduling words.
Original 0x28 frame, private homes, seven case starts and protected table remain
exact. Ten tests pass before/after, including 73,728 native32 cases, 210 fault
prefixes and the complete banked renderer/adapter using the installed helper.
Whole ELF changes only the 600-byte slot/symbol extent; all 37 owner neighbors,
old guard prefix, conversion rows and data unchanged. Game 2,751/4,816 (57.12%),
total 3,424/5,489 (62.38%), zero drift / 2,065 different. Next: 78-word leaf
func_1502EAFC's six-way phase updater; preserve the separate curve handoff.

Latest object color-mode semantic recovery:
[Note 1207](WORKING_NOTES/1207-game-object-color-mode-semantic-recovery-and-table-gates-20261010.md).
Complete diagnostic C for func_1502EC34 emits 148 words with the original
0x28 frame and private store homes. Seven tests pass: 1,697 guest cases,
65 public fault prefixes, four effective compiled negatives and 144 connections
to the banked linked adapter. All 37 copied-owner neighbors stay unchanged.
Not installed: modes 6/7 start four bytes early, the owner table addend is 0x100
instead of 0x124, and 77 isolated-link word differences remain. Production
source/ELF/guards/conversion rows/data and matching totals stay unchanged.
Resolve these table/extent gates, then qualify the installed helper with the
adapter/renderer. Preserve Note 1202's separate curve rejection handoff.

Latest captured-object metadata adapter byte match:
[Note 1206](WORKING_NOTES/1206-game-owner-captured-object-metadata-adapter-byte-match-20261010.md).
Complete func_151B4A14 replaces its zero-return stub; all89 linked words match
with89 dependency guards/15 register renames, original0x68 frame/private homes
and full14-argument ABI. Ten tests pass before/after, including complete original
renderer/helper connections; only target356-byte slot/symbol extent changes.
Old guard prefix, conversion rows and protected data unchanged. Game2,750/4,816
(57.10%), total3,423/5,489 (62.36%), zero drift /2,066 different. Next:150-word
func_1502EC34, still a production zero-return stub; preserve curve rejection gates.

Latest owner fixed-span point initializer byte match:
[Note 1205](WORKING_NOTES/1205-game-owner-fixed-span-point-initializer-byte-match-20261010.md).
Complete func_151B4B78 replaces its zero-return stub; all41 linked words match
with41 dependency guards/no omissions, preserving leaf ABI, early constant
read, repeated rounding and untouched velocities. Nine tests pass before/after;
only target164-byte slot/symbol extent changes. Old guard prefix, conversion
rows and protected data unchanged. Game2,749/4,816 (57.08%), total3,422/5,489
(62.34%), zero drift /2,067 different. Next:89-word func_151B4A14; preserve
Note1202 curve rejection gates and take a fresh baseline for future curve work.

Latest owner X-axis point interpolation byte match:
[Note 1204](WORKING_NOTES/1204-game-owner-x-axis-point-interpolation-byte-match-20261010.md).
Complete func_151B48DC replaces its zero-return stub; all44 linked words match
with46 guarded dependencies/two omissions, preserving the leaf ABI, repeated
rounding, constant alias order and untouched velocities. Nine tests pass before/
after; only target176-byte slot/symbol extent changes. Old guard prefix, conversion
rows and protected data unchanged. Game2,748/4,816 (57.06%), total3,421/5,489
(62.32%), zero drift /2,068 different. Next:41-word leaf func_151B4B78.

Latest linked-node endpoint transform direct match:
[Note 1203](WORKING_NOTES/1203-game-linked-node-endpoint-transform-direct-match-20261010.md).
Complete func_151B47D8 replaces its zero-return stub; all65 words emit directly
from C with original frame0x18, no new guards/padding. Nine tests pass before/
after; only target260-byte slot/symbol extent changes in the whole linked ELF.
Guards/conversion rows/protected data unchanged. Game2,747/4,816 (57.04%),
total3,420/5,489 (62.31%), zero drift /2,069 different. Next:44-word leaf
func_151B48DC; curve fitting/rejection handoff remains preserved in Note1202.

Latest owner threshold-curve squared-copy/frame separation:
[Note 1202](WORKING_NOTES/1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The first squared-length copy now qualifies at incoming SP-0xB4 with all prior
float boundaries, but this complete186-word form has a0x120 frame and all saved
write locations shift downward by8 bytes. Eleven tests plus a strengthened
saved-write rerun pass; frame/slot gates explicitly reject installation.
40 full forms measured; prior slot and scalar objects unchanged. Recover one
form satisfying frame, private values and178-word extent together; no matching
credit, production/guards/totals unchanged.

Latest owner threshold-curve scalar-home qualification:
[Note 1201](WORKING_NOTES/1201-game-owner-threshold-curve-limit-and-projection-home-qualification-20261010.md).
Threshold/quarter stores, two reads each, and projection store/read/final values
now qualify at their retail homes, retaining the nine vector/delta-Y boundaries.
Ten tests pass; 67 complete forms and eight profile forms measured. The complete
186-word diagnostic overflows by32 bytes; prior178-word slot form is unchanged.
Five scalar homes, spill/access scheduling and full-word matching remain open.
Not installed; production/guards/totals unchanged.

Latest owner threshold-curve private vector-home recovery:
[Note 1200](WORKING_NOTES/1200-game-owner-threshold-curve-private-vector-home-recovery-20261010.md).
Complete178-word diagnostic retains original0x118 frame/saved homes and fits
the712-byte slot without padding. All nine vector write multisets/final values
and full-path delta-Y store/read/value qualify; final nine tests pass.
58 full forms measured;154 raw instruction differences and scalar homes/
access ordering remain. Not installed; production/guards/totals unchanged.

Latest owner threshold-curve slot/full-path delta-Y recovery:
[Note 1199](WORKING_NOTES/1199-game-owner-threshold-curve-slot-and-delta-y-read-recovery-20261010.md).
Complete170-word diagnostic fits with original0x118 frame/saved homes and
delta-Y store/read/value on every path. Nine tests pass;72 full forms qualify,
plus a final independent-control rerun. Actual padder leaves32 bytes padding.
Other private homes/read order and full178-word matching remain open; not
installed. Production/guards/totals unchanged.

Latest owner threshold-curve frame/delta-Y fitting:
[Note 1198](WORKING_NOTES/1198-game-owner-threshold-curve-frame-and-delta-y-fitting-20261010.md).
76 complete forms qualify; final nine tests pass. Selected188 words restores
original0x118 frame, physical saved homes and delta-Y store at SP+0x110,
but overflows by40 bytes. No-work private read, other homes/input schedule and
full-word matching remain open. Not installed; production/guards/totals unchanged.

Latest owner threshold-curve recovery:
[Note 1197](WORKING_NOTES/1197-game-owner-threshold-curve-recovery-20261010.md).
Complete func_151B3FDC diagnostic qualifies all three paths; nine tests pass.
Selected169 words/frame0x110 versus retail178/frame0x118. Original dispatcher,
actual157-word initializer, native/guest/rebases and sixteen neighbors qualify.
Not installed; production/guards/totals unchanged. Continue original private
workspace, saved-value lifetimes and input schedule before full-word matching.

Latest linked-owner position provider match:
[Note 1196](WORKING_NOTES/1196-game-linked-owner-position-provider-match-20261010.md).
Complete func_151B3F28 replaces its zero-return stub and matches all45 words.
Raw C44 words; nine word edits and one shared-return copy retain the leaf ABI,
pointer reloads and fallback access order. Nine tests pass before/after; whole
ELF changes only target slot/symbol size. Game2,746/4,816 (57.02%),
total3,419/5,489 (62.29%), zero drift /2,070 different. Next: func_151B3FDC,
178 words/frame0x118. Hardware/FCSR/live acceptance remains separate.

Latest owner point-arc byte match:
[Note 1195](WORKING_NOTES/1195-game-owner-point-arc-byte-match-20261010.md).
Complete func_151B3CF0 replaces the zero-return placeholder and matches all
142 linked words with original frame/homes/ABI. Raw C is 144 words; 144 guards
cover register/scheduling edits, two omissions and unchanged proof dependencies.
All twelve tests pass before and after installation; whole ELF changes only the
target slot/symbol size. Game2,745/4,816 (57.00%), total3,418/5,489 (62.27%).
Next: adjacent 45-word func_151B3F28; actual trig/hardware/live acceptance separate.

Latest owner point-arc certified branch fold:
[Note 1194](WORKING_NOTES/1194-game-owner-point-arc-certified-branch-fold-20261010.md).
Guarded diagnostic fits 142 words / frame136 / 102 differences, retaining full
private memory and six input reads. Raw C remains 144 words / 138 differences;
35 source-only forms do not fit. Actual padder/owner/rebases and stale-window
controls qualify. All 60 combined tests pass in 463.986s; the final twelve-test
fold rerun passes in 96.182s. Not installed or byte-exact; production/guards/totals unchanged.
Continue FP/cursor/counter/branch-delay matching; real trig/FCSR/live remain separate.

Latest owner point-arc endpoint-read recovery:
[Note 1193](WORKING_NOTES/1193-game-owner-point-arc-endpoint-read-recovery-20261009.md).
Complete diagnostic now reads all six endpoint words once while retaining
original frame, saved/vector/delta-Y homes and full final private memory.
All 48 combined tests pass in 345.780s. Selected 144 words / 138 raw differences
still overflow the retail slot; no production/guard/credit change. Continue Z-delta and
half-constant scheduling, FP allocation and counter/cursor/branch-delay fit.

Latest owner point-arc delta-Y home recovery:
[Note 1192](WORKING_NOTES/1192-game-owner-point-arc-delta-y-home-recovery-20261009.md).
The complete diagnostic now preserves the original frame, saved/vector homes
and delta-Y store/load; entire final memory agrees in qualified cases.
All 36 combined tests pass in 306.741s. Selected 144 words / 135 differences
still overflow the 142-word slot. Four redundant start-coordinate reads remain; production,
guards and totals unchanged. Continue input reads and full-slot FP/cursor/
branch-delay scheduling. Real trig/FCSR/live acceptance remains separate.

Latest owner point-arc saved/vector-home recovery:
[Note 1191](WORKING_NOTES/1191-game-owner-point-arc-saved-and-vector-home-recovery-20261009.md).
Complete diagnostic now has original frame 0x88, all saved-register homes and
all nine private vector homes. Final memory differs only in the missing four-byte
delta-Y home in qualified cases. All 25 combined tests pass in 174.430s; 114
full source forms qualify. Still 143 words / 140 differences, and actual padder
rejects one-word overflow. No production/guard/credit changes. Continue delta-Y
storage, redundant endpoint reads, full-slot and FP/cursor/branch-delay scheduling.

Latest owner point-arc workspace/frame fitting audit:
[Note 1190](WORKING_NOTES/1190-game-owner-point-arc-workspace-and-frame-audit-20261009.md).
39 complete forms / 48 form-profile combinations qualify; all 14 combined
recovery/fitting tests pass in 71.805s. New midpoint-pointer diagnostic has
147 words/frame 152 bytes, but overflows the retail slot. An O1 136-byte frame
coincidence has 178 words and wrong saved-register homes; reject installation.
Retain Note 1189's 141-word/118-difference compact baseline. Production, guards
and totals unchanged; continue private homes/FP lifetimes/current-next cursor.

Latest owner point-arc recovery and linked-helper audit:
[Note 1189](WORKING_NOTES/1189-game-owner-point-arc-recovery-and-helper-audit-20261009.md).
Complete func_151B3CF0 is recovered and qualified in ten tests / 26.746s.
Selected diagnostic has 141 words/frame 0xD0/118 differences; retail is 142
words/frame 0x88. Not installed, no guards or matching/conversion credit.
Actual sinf/cosf return zero; the full 80-word angle-helper slot is already exact.
Production/data/progress and README totals remain unchanged. Continue the arc
routine's frame/private homes and saved-FP scheduling; real trig/live parity is separate.

Earlier owner point-initializer guarded C match:
[Note 1188](WORKING_NOTES/1188-game-owner-point-initializer-guarded-c-match-20261009.md).
Complete func_151B3A7C is installed and exact across all 157 linked words,
with 99 certified expected-word/relocation guards, one dead-control omission
and no inserted words or frame patches. Fourteen installed tests pass in
19.579s; full owner/ELF/data/guard-history and independent rebases pass.
Game 2,744/4,816 and total 3,417/5,489 exact, zero drift / 2,072 different.
Conversion rows are unchanged. Next is 142-word func_151B3CF0's helper/loop contract;
hardware/FCSR/live acceptance remains separate.

Latest owner point-initializer zero-read/induction audit:
[Note 1187](WORKING_NOTES/1187-game-owner-point-initializer-zero-read-and-induction-audit-20261009.md).
Explicit second-vector stores remove two extra public reads per call; the complete
diagnostic has 158 words/frame 0x60 and 110 differences. Twelve tests pass in
112.575s, zero skips. Actual owner/padder rejects the one-word overflow; no
installation/guards/credit. Keep Note 1186's 157-word fit separately. Continue
direct counter/end control, then allocation/scheduling. Production and totals unchanged.

Earlier owner point-initializer frame/private-home fitting checkpoint:
[Note 1186](WORKING_NOTES/1186-game-owner-point-initializer-frame-and-private-home-fit-20261009.md).
Complete func_151B3A7C now fits all 157 words/frame 0x60 and original SP+0x44
position/SP+0x08 saved-FP homes directly from actual actor fields and live locals.
Raw differences fall 143 to 137. Eleven tests pass in 122.336s, zero skips:
full guest/native32/alias/dispatch/rebase/fault gates plus exact final private bytes
and no extra private writes. Twenty-nine full source forms pass eight fixtures
each; actual copied owner/padder preserves 16 neighbors/pools/relocations.
Still uninstalled/nonmatching, no guards/credit. Source/ELF/guards/progress and
protected data remain unchanged. Continue its integer induction, second-vector
zero emission and independent FP/setup scheduling; do not patch frame words.

Earlier owner point-initializer recovery checkpoint:
[Note 1185](WORKING_NOTES/1185-game-owner-point-initializer-recovery-20261009.md).
Recover complete func_151B3A7C's ten 24-byte point records, ordered binary32
increments, zero second vectors and flag-bit-2 clear/success return. Actual
D_8008FAF8[0] callback ABI is qualified through the complete 81-word update.
Nine tests pass in 35.481s, zero skips: 2,048 guest/8,192 native32 cases,
independent scales/first-record constant aliases, effective negatives, fault
prefixes, independent rebases and actual owner/padder qualification.
Candidate fits 157 words but has frame 0x58 versus retail 0x60 and 143 real
word differences. It is not installed or matched; production hashes, old guards,
protected data and aggregate totals remain unchanged. Continue this function's
real workspace/private position home, induction and scheduling fit before guards.

Latest installed owner ribbon-renderer guarded C match:
[Note 1184](WORKING_NOTES/1184-game-owner-ribbon-renderer-guarded-c-match-20261009.md).
func_151B32C8 now matches all 475 linked words/frame 0x148. Complete semantic C
emits 314 words unchanged; 161 certified relocation-aware guards close allocation
and four setup scheduling windows. Ordinary read-only table loads may reorder;
this is not direct compiler output or a hardware/FCSR/gameplay proof.
Eighteen installed tests pass in 42.269s, zero skips. Whole ELF changes only the
target slot/st_size; preserve 16 neighbors, 189,088 protected bytes, old guard
prefix and byte-identical conversion rows. Eleven shared guard/progress tests and
project tools-check pass. Game 2,743/4,816 exact; total 3,416/5,489, zero drift
and 2,073 different. Converted counts/bytes unchanged; no conversion credit.
Adjacent 157-word/frame 0x60 func_151B3A7C's point-preparation ABI and complete
candidate are recovered in Note 1185; frame/word fitting remains before installation.
Full helpers/second material/caller overflow/hardware/gameplay remain separate.

Earlier owner ribbon-renderer shared-copy and GPR allocation checkpoint:
[Note 1183](WORKING_NOTES/1183-game-owner-ribbon-renderer-shared-copy-and-gpr-proof-20261009.md).
Complete func_151B32C8 retains 475 words/frame 0x148 and original private homes.
Moving the real points-base assignment before the last helper recovers all three
initial second-copy shared-base loads directly; raw differences fall 163 to 161.
Certify 107 closed GPR allocation words on the separately FP-normalized body;
120 combined FP/GPR changed words leave 44 differences, down from 151.
All vertex/loop/epilogue words now agree after certified normalization.
Fifteen full tests pass in 60.131s, zero skips; final composed-proof/collision
check passes 1.348s after tightening proof composition. Full raw/native and
combined normalized guest/mutation/rebase/material/walker/fault/FP preservation.
Fourteen full source forms pass all 32 bounded fixtures each; copied owner and
padder accept the raw slot, 16 neighbors/pools/relocations preserved.
No installation/guards/credit. Production hashes/protected data/README totals
unchanged. Finish argument-home setup, render-mode/table preparation and initial
copy/FP-load scheduling before installation; full hardware/gameplay is separate.

Latest owner ribbon-renderer induction and FP allocation checkpoint:
[Note 1182](WORKING_NOTES/1182-game-owner-ribbon-renderer-induction-and-fp-proof-20261009.md).
Complete func_151B32C8 retains 475 words/frame 0x148 and original private homes.
Real point-base and dead-tangent scale lifetimes recover the original byte-offset
loop and two advancing pointers directly from C; raw differences fall 243 to 163.
A 13-word FP-field-only remap leaves 151 differences. Its ordered-operand proof
covers all 1,024 paths through nine iterations and closes saved FP lifetimes.
Fourteen tests pass in 62.407s, zero skips; full raw/native and normalized guest/
mutation/rebase/material/walker/fault/coverage checks, effective unsafe-map controls.
45 complete source forms pass 32 bounded contract fixtures each. Owner/padder
accepts the raw slot unchanged; 16 neighbors, pools and relocations preserved.
No installation, new guards or credit. Source/ELF/guards/progress/protected data
unchanged. Continue the same renderer's initial copy base and remaining GPR/
scheduling fit; full helper/hardware/gameplay acceptance remains separate.

Latest owner ribbon-renderer frame/slot fitting checkpoint:
[Note 1181](WORKING_NOTES/1181-game-owner-ribbon-renderer-frame-and-slot-fit-20261009.md).
The complete func_151B32C8 C now emits475 words/frame0x148 with original cursor,
point, origin, sync and material homes. Real squared-normal and offset temporaries,
allocation scope and source ordering reduce432 to243 real word differences.
Twelve tests pass55.814s, zero skips; full guest/native/mutation/rebase/callback/
walker/fault qualification plus all475 candidate words and12 saved FP words.
43 full source forms/46 profile rows; reject O2's reordered command writes.
Actual copied owner and padder accept the1,900-byte slot unchanged;16 neighbors/
pools/relative relocations preserved. No installation, guards or matching credit.
Source/ELF/guards/progress and189,088 protected bytes remain unchanged.
Continue the same32C8 shared-copy-base/loop and FP/GPR scheduling/allocation fit;
do not synthesize retail words. Full helpers/hardware/gameplay remain separate.

Earlier owner ribbon-renderer recovery checkpoint:
[Note 1180](WORKING_NOTES/1180-game-owner-ribbon-renderer-recovery-checkpoint-20261009.md).
Recover complete475-word func_151B32C8, all nine quads/20 vertices and14-argument
material ABI. Eleven tests pass23.776s, zero skips:512 guest/385 mutation/7,680
native32,64 rebases, actual34-word material callback and348-word original walker.
All475 retail words reached; preserve40 vertex flag bytes and fresh texture steps.
Selected C477 words/frame304/432 differences; target475/frame328. Actual padder
rejects overflow; no installation. Production source/ELF/guards/progress and
189,088 protected bytes unchanged; no new matching/conversion credit.
Resume the same32C8 real-local workspace/loop fit. Full helpers, caller overflow/
rollback, hardware/live rendering/gameplay stay separate. Totals remain Note1179.

Latest installed owner actor-update direct C match:
[Note 1179](WORKING_NOTES/1179-game-owner-actor-update-direct-match-20261009.md).
func_151B3184 emits all81 words directly/frame0x20, no guards. Nine installed
tests pass11.396s, zero skips:6,048 guest/102,400 native32, mutations, complete
original74-word registered walker, independent rebases, lazy reads and faults.
Whole ELF changes only target slot/st_size; preserve16 neighbors,189,088
protected bytes and byte-identical guard/conversion rows. No conversion credit.
Game2,742/4,816 exact,total3,415/5,489,zero drift/2,074 differences.
The same-owner renderer func_151B32C8 is now installed and guarded byte-exact;
[Note 1184](WORKING_NOTES/1184-game-owner-ribbon-renderer-guarded-c-match-20261009.md)
supersedes Note 1183's remaining 44 differences. Full helpers/hardware/gameplay
remain open; original connected walker is not installed C. Earlier entries are history.

Earlier endpoint quad guarded C match:
[Note 1178](WORKING_NOTES/1178-game-owner-endpoint-quad-guarded-c-match-20261009.md).
func_151B2974 matches all340 words/frame0xB8 with84 certified closed GPR
allocation guards; this is not direct compiler output. Ten installed tests
pass17.255s, zero skips:384 guest/11,520 native32, rebases, actual20-word caller,
effective negatives and faults. Whole ELF changes only target slot/st_size;
preserve17 neighbors/189,088 protected bytes and all11,604 old guard rows.
Conversion rows stay unchanged: the old false placeholder was already C.
Game2,741/4,816 exact,total3,414/5,489,zero drift/2,075 differences.
Next adjacent-owner81-word/frame0x20 func_151B3184 actor-update dispatcher,
then its neighboring full renderer151B32C8. Full helpers/hardware/gameplay and
renderer remain open. Checkpoints below are historical, not the current handoff.

Earlier endpoint quad recovery/frame fit, superseded by Note1178:
[Note 1177](WORKING_NOTES/1177-game-owner-endpoint-quad-recovery-and-frame-fit-20261009.md).
Recover complete340-word func_151B2974, actual three-argument graphics ABI,
endpoint/matrix/origin lifetimes, four partial-write vertices and two triangles.
Selected C now has the correct0xB8 frame but140 word differences; not installed.
Nine tests pass29.375s:384 guest/11,520 native32,96 rebase and48 actual20-word
dispatcher cases, effective negatives and faults. Reach339 retail words;
the unreachable duplicate at151B2A14 is separately verified.
Production placeholder/source/ELF/guards/progress stay unchanged, no new credit.
Resume the same2974 private-workspace fit, not another target. Full helpers,
hardware/gameplay and renderer remain open. Totals below remain current.

Latest owner companion setup C match:
[Note 1176](WORKING_NOTES/1176-game-owner-companion-setup-guarded-c-match-20261009.md).
func_151B2690 matches all176 words/frame0xD8 with69 certified private-home/
prefix guards; not direct compiler output or a GPR-only permutation.
Nine installed tests pass14.788s, zero skips:384 guest/16,384 native32,
64 independent rebase and64 actual-wrapper chain cases, negatives and faults.
Entire ELF remains byte-identical; preserve17 neighbors/189,088 protected bytes.
Append only69 guards/change one ASM-to-C row, adding704 converted bytes.
Game2,740/4,816 exact,total3,413/5,489,zero drift/2,076 differences.
Converted5,489/6,042 (90.85%),85.98% bytes; Game4,816/5,321 (90.51%),85.33%.
Next same-owner340-word/frame0xB8 func_151B2974, currently a false zero-return
placeholder; recover full caller/graphics ABI before fitting. Hardware/full
renderer gates remain separate. Earlier checkpoints below are historical.

Latest owner companion recovery checkpoint:
[Note 1175](WORKING_NOTES/1175-game-owner-companion-setup-recovery-checkpoint-20261009.md).
Recover complete176-word func_151B2690's two retained link requests and late
40-byte effect packet. Nine tests pass61.269s:384 guest/16,384 native32,
64 independent rebase and64 actual53-word wrapper-chain cases. Complete guest
memory/raw copied holes agree, but access traces and emitted words do not match.
Selected C is176/frame0xD8/122 differences; all56 persisted profile rows are
rejected for installation. Original assembly/source/ELF/guards/progress stay
unchanged, with no new matching/conversion credit. Totals remain those below.
Resume the same2690 actor-home/initialS1 scheduling fit; the ignored69-difference
volatile probe has an exact105-word suffix but is not qualified for installation.

Latest owner link setup C match:
[Note 1174](WORKING_NOTES/1174-game-owner-link-setup-guarded-c-match-20261009.md).
func_151B2348 matches all210 words/frame0xA8 with25 certified closed T6/T7
guards; this is not direct compiler output. Nine installed tests pass25.020s:
768 guest/32,768 native32/384 actual-wrapper chain cases, independent rebases,
faults and copied-owner preservation. Entire ELF remains byte-identical;
all11,510 old guards and189,088 protected data bytes are preserved.
Exactly one ASM-to-C row adds840 converted bytes. Game2,739/4,815 exact,
total3,412/5,488,zero drift/2,076 differences. Converted5,488/6,042 (90.83%),
85.95% bytes; Game4,815/5,321 (90.49%),85.30% bytes.
Resume original176-word/frame0xD8 companion func_151B2690.

Latest owner link allocator match:
[Note 1173](WORKING_NOTES/1173-game-owner-link-allocator-direct-match-20261009.md).
func_151B30B0 emits all53 words directly, frame0x28/no guards. Eight installed
tests pass29.437s:7,168 guest/774,144 native32 cases and128 actual setup-chain
cases. Only target loadable code/size meaning change; verified symbol ordering
is permitted, all20,318 symbols otherwise retain meaning. Guards/progress and
protected data unchanged. Game2,738/4,814 exact,total3,411/5,487,zero drift,
2,076 differences; no new conversion credit. Resume210-word func_151B2348
with its now-exact allocator dependency and real-local declaration-order fitting.

Latest recovery checkpoint:
[Note 1172](WORKING_NOTES/1172-game-owner-link-setup-recovery-checkpoint-20261009.md).
func_151B2348's three-request semantics and allocator ABI are recovered.
Five bounded tests pass23.790s,384 cases/768 executions; all210 retail words
exercised. No candidate matches retail stack/register layout; original assembly
stays installed. Source/ELF/guards/progress unchanged, no new matching credit.
Next fit retainedS2 and private packetSP34/requestSP64, then qualify installation.

Latest owner state callback match:
[Note 1171](WORKING_NOTES/1171-game-owner-state-callback-direct-match-20261009.md).
func_151B2100 emits all67 words directly, frame0x38/four relocations/no guards.
Ten installed tests pass64.965s, zero skips; tools d6552d0 is banked first.
Correct void callee contracts require removing two false zero-return C bodies:
func_151B2348/151B2690 are restored as complete210/176-word retail assembly,
not new C matches. Guest21,552/native32 150,528, actual classifier/cleanup96
and registered-dispatcher672 cases qualify lazy gates and callee mutations.
Only three reviewed code slots/sizes change; symbol/string order may change,
but all20,318 symbols retain meaning except the three intended sizes.
Protected data/guards unchanged; exactly two C-to-ASM progress rows.
Game exact2,737/4,814 (56.86%), total3,410/5,487 (62.15%), zero drift,
2,077 differences. Converted5,487/6,042,85.91% bytes; Game4,814/5,321,85.26%.
Next recover genuine210-word func_151B2348; renderer remains pending.

Latest owner descriptor constructor match:
[Note 1170](WORKING_NOTES/1170-game-owner-descriptor-constructor-direct-match-20261009.md).
`func_151B2060` emits all40 retail words directly, original0x50 frame/four
relocations and no guards. Eight installed tests pass in51.065s:6,146 guest,
7,680 native32,96 rebase cases and60 connected cases using actual caller/
allocation wrapper. Preserve five raw packet holes and pre-helper capture.
Whole ELF changes only target160-byte slot/st_size12->160; preserve17
neighbors/four existing warnings, guard/progress rows and protected data.
Game exact2,736/4,816 (56.81%), total3,409/5,489 (62.11%), zero drift,
2,080 differences; no conversion credit. Next recover descriptor consumer
`func_151B2100`,67 words; renderer remains pending.
Tools0353bcb banked first; source/docs and exact consumer pin follow.

Latest endpoint-pair callback match:
[Note 1169](WORKING_NOTES/1169-game-endpoint-pair-callback-direct-match-20261009.md).
`func_151B2F04` replaces its false placeholder with all39 retail words
directly under existing O2/g3, frame0 and no guards. Eight installed tests
pass in12.221s:4,352 guest,13,056 native32,194 fault pairs, independent
rebases and actual23-word dispatcher2,048 routing cases. Preserve17 owner
neighbors, four existing warnings, actual table pointer and all other ELF
bytes; only target156-byte slot/st_size12->156 change. Game exact2,735/4,816
(56.79%), total3,408/5,489 (62.09%), zero drift and2,081 differences.
No conversion credit; protected data/guards/progress CSV unchanged.
Next recover same-owner40-word `func_151B2060`; renderer remains pending.
Toolsc6b2d59 banked first; source/docs and exact consumer pin follow.

Latest byte-preserving callback qualification:
[Note 1168](WORKING_NOTES/1168-game-ribbon-alpha-defined-signed-scaling-20261009.md).
`func_151490C8` was already15-word exact. Replace negative signed left
shift with safe multiplication by8; the entire rebuilt ELF is byte-identical.
Seven installed tests pass in30.800s:65,536 guest cases,589,824 native32
calls,192 alias/phase cases, seven fault pairs, four negatives and rebases.
Actual selector6/table pointer remains correct. No new matching/conversion
credit; root README unchanged. Next recover complete39-word `func_151B2F04`,
currently a zero-return placeholder; renderer and handwritten fragments stay open.
Tools0269fbb banked first; source/docs and exact consumer pin follow.

Latest installed constructor match:
[Note 1167](WORKING_NOTES/1167-game-ribbon-effect-constructor-direct-match-20261009.md).
`func_15148F1C` emits all 107 retail words directly from semantic C, with
the original 0xB8 frame and no guards. Eight tests pass in37.223s after
installation, including actual lookup/delegate callees, native32 typed
calls, four independent symbol sets and whole-ELF preservation.
Game exact rises to2,734/4,816 (56.77%); total3,407/5,489 (62.07%).
Conversion rows,11,510 guards and189,088 protected Game data bytes remain
unchanged. Root README changes aggregate rows only. Next audit neighboring
`func_151490C8`; full ribbon renderer matching remains pending.
Older renderer suites retain their historical pre-install fingerprints;
this real restoration deliberately supersedes those whole-source/ELF hashes.
Tools468cd97 banked first; source/docs and exact consumer pin follow.

Current renderer register exclusions:
[Note 1166](WORKING_NOTES/1166-game-camera-ribbon-register-lifetime-exclusions-20261009.md).
18 complete forms/12 instruction streams/54 finite controls eliminate the
shared-phase/ray-output installation path; two tests pass in16.292s.
Retain the qualified13-home primary; new forms exceed the slot or shift
saves. Next recover neighboring107-word constructor func_15148F1C's
zero-return placeholder. Production bytes/credit/root README unchanged.

Current renderer color-home/callback qualification:
[Note 1165](WORKING_NOTES/1165-game-camera-ribbon-renderer-color-homes-callback-20261009.md).
Complete typed545/frame0x120/509 differences form now matches13 private
homes and retail save slots. The directly typed byte-buffer callback is537/
frame0x120/538 differences, with different GPR/FP saves. Both retain the
full renderer;51 forms/36 instruction streams screened. Raw schedule,
register roles and complete native caller acceptance remain open. Neither
installed/exact; production bytes/credit and root README unchanged.
Twelve tests pass in212.922s; fresh primary rebases qualify four symbol sets.
Tools426c56c banked first, exact parent pin second.

Current renderer exit-flow qualification:
[Note 1164](WORKING_NOTES/1164-game-camera-ribbon-renderer-exit-flow-qualification-20261009.md).
The complete 16-bit-input outer-active form emits 545 words, fits the slot,
and retains the retail 0x120 frame, save slots and five private slots.
Its active/null-cursor branch shapes are now retail-shaped; 509 raw word
differences remain. Independent original/candidate links qualify four
symbol sets (eight links/25 relocation uses/184 cases). Twelve tests pass
in145.688s, including804 guest,536 native32,128 nonlinear and14 view cases.
The62-form catalog has39 instruction streams; compare fingerprints, not
shape metrics alone. Tools8a71e51 first, exact parent pin second.
Exact register roles, color homes, FP schedule and callback
integration remain open. Production source/ELF/guards/credit unchanged;
root README unchanged. Bank tools before the exact consumer pin.

Current renderer private-slot/view qualification:
[Note 1163](WORKING_NOTES/1163-game-camera-ribbon-renderer-private-slots-view-staging-20261009.md).
Complete short-input547/frame0x120/433 differences form now matches five
retail private slots plus frame/save slots. Fourteen tests pass in204.038s,
including804 guest,536 native32,128 nonlinear and14 raw-view cases per form.
Keep16-bit input; wide-input545/519 is a layout experiment, not a proven
original signature. Color homes, register roles, exit CFG and callback
integration remain open. Neither installed/exact; production bytes/credit
unchanged. Tools d940c7e first, exact parent pin second.

Previous renderer retail-frame/save-slot qualification:
[Note 1162](WORKING_NOTES/1162-game-camera-ribbon-renderer-retail-frame-save-slots-20261009.md).
Two complete forms now match retail0x120 frame, four GPR save slots and five
FP pairs: selected547/463 raw differences, outer545/512. Eleven tests pass
in221.346s, including804 guest,536 native32 and128 nonlinear guest/native32
cases per form. Safe last-output scale reuse is qualified; early overwrite
still fails. Neither is exact or installed. Next resolve payload/records/
view register roles and private stack slots; all production bytes/credit
stay unchanged. Tools df3bbd1 first, exact parent pin second.

Previous renderer lifetime qualification:
[Note 1161](WORKING_NOTES/1161-game-camera-ribbon-renderer-lifetime-qualification-20261009.md).
Ten tests pass in220.493s for complete typed547/frame0x130/440 differences
and stride545/frame0x120/526 differences forms. Each receives804 guest,
536 native32 and128 additional nonlinear guest/native32 cases. Three
compiled negatives reject unsafe decompiler capture/head/texture changes.
Catalog73 forms produces35 distinct instruction streams; sampled controls
are not full qualification of all forms. Neither installed or exact: typed
still exceeds the slot, stride saves only three GPRs. Next recover typed
private slots and retail view/texture/stride lifetime. All credit unchanged.

Previous renderer frame fitting:
[Note 1160](WORKING_NOTES/1160-game-camera-ribbon-renderer-frame-fitting-20261009.md).
Two complete forms reach frame0x120: inline rays543 words/544 raw differences,
and mixed lifetimes546/513. Eight tests pass in138.152s; both forms receive
804 guest and536 native32 cases, owner isolation and actual dispatcher16
cases/32 executions. Neither is installed or exact: inline saves only three
GPRs, mixed adds an FP pair. Next recover retail S3 view/stride lifetime and
original private layout. Production bytes, root README and credit unchanged.

Previous complete renderer recovery:
[Note 1159](WORKING_NOTES/1159-game-camera-ribbon-renderer-recovery-20261009.md).
Full func_1514803C semantic candidate is qualified but **not installed**:
547 words/frame0x130/443 raw differences versus retail546/frame0x120.
Nine tests pass in106.260s, including804 guest cases,536 native32 cases,
eight effective negatives, ten owner neighbors and actual52-word graphics
dispatcher connection. All production source/ELF/guards/progress bytes stay
unchanged; no conversion or exact-match credit. Next fit private locals and
record-pointer lifetime across setup, then qualify linking/installation.
Root README aggregates stay unchanged. Preserve the independent tools mirror.

Latest Game record height response match:
[Note 1158](WORKING_NOTES/1158-game-record-height-response-match-20261009.md).
Convert GLOBAL_ASM `func_15148BA4` to complete C143/frame0x58, linked exact
with three expected-word guards: one commutative addition and a closed
payload carry slot. Raw C retains three differences, not direct matching.
Recover conditional old-position snapshot, backwards integration, strict
height comparison/query and two live six-argument response tables. Preserve
the flags&7 versus flags&0x17 private lifetime without a guessed initializer.
Nine final tests pass in 69.618s, including 50,689 native32 defined cases, 37 public aliases,
eight effective negatives and complete 100+97+143+9-word dispatch through
the actual `func_15148EF8` response body. Height query is still a bounded
model, not newly proven hardware/gameplay. Every ELF byte/all 6,058 slots
remain unchanged; one asm -> c row and exactly three guard rows, total
11,510. Thirty-five shared tests and both tools checks pass. Fresh totals
5,489 converted /3,406 exact, Game 4,816 /2,733; zero drift, 2,083 different.
Tools f0818a5 first, exact parent pin second, no push/older mirror reset.
Next full `func_1514803C` renderer: 546 words/frame0x120, the owner's last
GLOBAL_ASM. Other response/cleanup/upstream/hardware/gameplay and graph
corpus repair remain open. Root README receives aggregate rows only.

Previous Game record growth match:
[Note 1157](WORKING_NOTES/1157-game-record-growth-match-20261009.md).
Convert GLOBAL_ASM `func_151488C4` to complete 140-word C/frame0x10,
directly byte-exact without guards or profile changes. Recover forward
integration, bitwise position insertion, initial vertical velocity, stored
head narrowing/wrap, phase shaping and full-capacity selector transition.
Preserve conditional SP+0 u16 step: zero active skips initialization, so
qualify emitted prior-stack behavior separately from defined native C.
Eight final tests pass in 32.874s, including 81,534 native32 cases, 49 public aliases,
nine effective negatives and the complete 100+97+140-word dispatch chain.
All ELF bytes/all 6,058 slots and all 11,507 guard rows/bytes are unchanged;
exactly one conversion row changes asm -> c. Thirty-five shared tests and
both tools checks pass. Fresh totals: 5,488 converted / 3,405 exact, Game
4,815 / 2,732; zero drift, 2,083 different. Tools 9d3bfa0 first, exact
parent pin second; no push or older mirror reset. Next complete slot-3
`func_15148BA4`, 143 words/frame0x58, including conditional position snapshot,
backwards integration, height query and six-argument response callbacks.
Other callbacks/cleanup/upstream/hardware/gameplay and graph corpus repair
remain open. Root README has aggregate rows only.

Previous Game record phase shaping match:
[Note 1156](WORKING_NOTES/1156-game-record-phase-shaping-match-20261009.md).
Convert GLOBAL_ASM `func_15148DE0` to complete 70-word frameless C,
directly byte-exact without guards or profile changes. Recover signed active
gate/decrement, narrowed signed head, captured pointers, u16 division/phase
and the forward loop's live flags/count/head. All ELF bytes/all 6,058 slots,
data/symbols/metadata and all 11,507 guard rows/bytes remain unchanged;
exactly one conversion row changes asm -> c. Nine final tests pass in
90.033s, including 66,560 native32 cases, 26 public aliases, seven effective
negatives and the complete 100+97+70-word successful dispatch chain.
Thirty-five shared tests and both tools checks pass. Fresh totals: 5,487
converted / 3,404 exact, Game 4,814 / 2,731; zero drift, 2,083 different.
Tools 741b405 first, exact parent pin second, no push or older mirror reset.
Next complete 140-word GLOBAL_ASM callback `func_151488C4`, preserving
its conditional SP+0 step lifetime. Other callbacks/cleanup/upstream/
hardware/gameplay and graph corpus gates remain open. Root README has
aggregate rows only.

Previous Game wrapped record step match:
[Note 1155](WORKING_NOTES/1155-game-wrapped-record-step-match-20261009.md).
Convert GLOBAL_ASM `func_15148AF4` to complete 44-word frameless C,
linked exact with one commutative pointer-add guard; raw C has one
difference, not a direct compiler match. Recover backwards wrapped records,
signed start/endpoint, unsigned live count and four ordered float updates
with live time reloads. Entire rebuilt ELF/all 6,058 slots are byte-identical;
one asm -> c conversion row changes, one guard appends, total 11,507.
Eight focused tests cover 66,176 native32 cases, all 44 words, nine effective
negatives and the actual complete 100+97+44-word dispatch chain. Thirty-five
shared tests and both tools checks pass. Fresh totals: 5,486 converted /
3,403 exact, Game 4,813 / 2,730; zero drift, 2,083 different.
Tools 919a0c1 first, exact parent pin second, no push or older mirror reset.
Next complete 70-word GLOBAL_ASM phase-shaping callback `func_15148DE0`.
Other callbacks/cleanup/upstream/hardware/gameplay and graph corpus gates
remain open. Root README contains aggregate rows only.

Previous Game payload callback update match:
[Note 1154](WORKING_NOTES/1154-game-payload-callback-update-match-20261009.md).
Convert GLOBAL_ASM `func_15147EB8` to complete 97-word C, linked exact with
25 closed frame/return-lifetime guards; raw frame0x20 has 25 differences,
retail frame0x30. The entire rebuilt ELF is byte-identical to its assembly
baseline. Only one conversion row changes, asm -> c, and 25 guards append.
Nine final tests pass in 162.883s, including 328,448 native32 cases and
connected execution of the banked timer updater into this callback.
Fresh totals: 5,485 converted / 3,402 exact, Game 4,812 / 2,729; zero drift,
2,083 different. Tools a2e5ea7 first, exact parent pin second, no push or
older mirror reset. Next 44-word GLOBAL_ASM callback `func_15148AF4`.
Actual inner callback/cleanup/upstream/hardware/gameplay and graph corpus
gates remain open. Root README contains aggregate rows only.

Previous Game actor timer callbacks match:
[Note 1153](WORKING_NOTES/1153-game-actor-timer-callbacks-match-20261009.md).
Restore false-zero `func_15147740`, 100 words / 400 bytes / frame0x20,
linked exact with six guarded private failure-flag spill accesses; raw C
has six differences, not a direct compiler match. Recover wrapped signed
timer, two unsigned selectors, signed -1 sentinel, live flags/tables,
callback failure suppression, continued validation, cleanup and void return.
Eight post-install tests pass in 64.224s, including 721,664 native32 cases,
all 99 reachable words, six effective negatives and actual table identities.
All 6,058 slots and other code/data remain unchanged; target size 12 -> 400
and an exact six-byte ABS-symbol ordering permutation are audited against
the saved baseline. Every logical symbol remains unchanged except target size.
Preserve all 11,475 old guards/bytes; append six, total 11,481. Conversion
CSV unchanged. Fresh totals: 5,484 converted / 3,401 exact, Game 4,811 /
2,728; zero drift and 2,083 different. Twenty-five shared tests and both
tools checks pass. Tools b3086e2 first, exact parent pin second, no push or
older mirror reset. Next first-table callback `func_15147EB8`, 97 words/
frame0x30; trail remains 61 differences. Wider callback/cleanup/upstream/
hardware/gameplay and graph corpus gates remain open.

Previous Game actor graphics dispatch match:
[Note 1152](WORKING_NOTES/1152-game-actor-graphics-dispatch-match-20261009.md).
Restore false-zero `func_15147C4C`, 52 words / 208 bytes / frame0x38,
directly byte-exact without guards. Recover signed-halfword forwarding,
lazy optional word, nine-argument graphics call, live selector/table reads,
cleanup/zero-selector graphics return and distinct callback-result return.
Eight post-install tests pass in 27.622s, including 655,616 native32 cases,
all 52 words, six effective compiled negatives and 1,344 bounded cases
using actual retail table identities. Preserve 10 neighbors/pools/relocations
and seven diagnostics. Only target ELF slot and symbol size 12 -> 208 change;
all other bytes/data, 6,058 slots, conversion CSV and 11,475 guards unchanged.
Fresh totals: 5,484 converted / 3,400 exact, Game 4,811 / 2,727;
zero drift and 2,084 different. Twenty-five shared tests and both tools
checks pass. Bank tools 7b88702 before exact parent pin; preserve older
mirror changes/history, no push. Next false-zero `func_15147740`,
100 words/frame0x20; trail remains 61 differences. Actual helper/callback/
upstream/hardware/gameplay and graph corpus repair remain open.

Previous Game effect allocation core match:
[Note 1151](WORKING_NOTES/1151-game-effect-allocation-core-match-20261009.md).
Restore false-zero `func_15147A80`, 115 words / 460 bytes / frame0x38,
directly byte-exact without guards. Recover its eleven-word ABI, unsigned
allocation size, live request copy, 160-byte header, optional 36-byte record,
live resource-count loop, null path and original-pointer return. Argument 8
is the nullable optional-record address, not an extra byte count. Correct two
direct-call declarations/casts without changing their instructions; preserve
10 owner neighbors and all 42 functions in three direct-caller owners.
Eight post-install tests pass in 73.219s, including 65,536 native32 cases
and 192 connected cases through all three direct callers plus the complete
trail constructor. Only the core ELF slot and symbol-size field 12 -> 460
change; all other ELF bytes, 6,058 addresses/extents, conversion rows/bytes
and 11,475 guards are unchanged. Fresh totals: 5,484 converted / 3,399 exact,
Game 4,811 / 2,726; zero drift and 2,085 different. Twenty-five shared tests
and both tools checks pass. Bank tools 2807f51 first, parent source/docs pin
second, no push or older standalone reset. The 144-word trail constructor
remains 61 differences. Next recover neighboring 52-word `func_15147C4C`
or continue that caller's matching. Wider allocator/resource/hardware/gameplay
and graph gates stay open; OGL Release remains frozen.

Previous Game effect-record constructor match:
[Note 1150](WORKING_NOTES/1150-game-effect-record-constructor-match-20261009.md).
Restore false-zero `func_15147DA0`, 70 words / 280 bytes / frame0x40,
directly byte-exact without guards. Recover its full fifteen-word interface,
request state, eleven-argument allocation call, lazy null path, descriptor
copy, six low-byte stores, eight-word render copy and original return pointer.
Correct the caller's prototype to full-word active/fade parameters; every
instruction in its 62-function owner remains unchanged, including the
144-word `func_151DA6F8` with 61 actual differences. None of 73 additional
caller fitting forms is installed; the render-prefix placement is unresolved.
All nine post-install tests pass in 39.334s, including 65,536 native32 cases
and the complete 225-word caller/callee/memcpy path. Only the target's ELF
slot and symbol-size field 12 -> 280 change; all other ELF bytes, all 6,058
addresses/extents, converted rows/bytes and 11,475 guards are unchanged.
Fresh totals: 5,484 converted / 3,398 exact, Game 4,811 / 2,725;
zero drift and 2,086 different. Twenty-five shared tests and both tools
checks pass. Bank tools 658b615 first, then exact parent source/docs pin;
preserve older standalone edits/history without pushing. Next recover the
115-word allocation core `func_15147A80` or continue the caller's 61
remaining differences. Original callers, unspecified padding, graph repair
and hardware/gameplay remain open. OGL Release remains frozen.

Previous Game table-driven effect constructor restoration:
[Note 1149](WORKING_NOTES/1149-game-table-driven-effect-constructor-restoration-20261009.md).
Replace false-zero `func_151DA6F8` with complete semantic C, 144 words /
576 bytes / frame0xD0. Recover the 18-argument ABI, four records, table/flag
choices, 15-argument creation call, null path, payload copy and preserved
pointer. Linked differences improve 143 -> 61; explicitly still non-matching,
no new guards or progress credit. Whole ELF changes only its target slot and
symbol-size field 12 -> 576; all 61 owner neighbors, other ELF bytes/data,
6,058 addresses/extents, conversion rows and 11,475 guards are unchanged.
Totals remain 5,484 converted / 3,397 exact, Game 4,811 / 2,724, zero drift.
Eight post-install tests pass, including native32 and connected original
retail callee/copy qualification; 25 shared tests and both tools checks pass.
Tools 77001d3 first, exact parent source/docs pin second; no push or older
standalone reset. Continue this target's 61 remaining layout/scheduling words.
Unspecified render padding, allocation core, original callers, graph repair
and hardware/gameplay stay open. OGL Release remains frozen.

Previous Game random-effect timer restoration:
[Note 1148](WORKING_NOTES/1148-game-random-effect-timer-restoration-20261009.md).
Replace false-zero `func_151D9EB0` with complete 68-word / 272-byte /
frame0x60 semantic C, directly matching retail without guards. Recover its
void contract, signed-halfword timer wrap, ordered RNG calls, live field reads,
16-argument effect call and timer reset. Preserve all 61 copied-owner neighbors,
pools, relative relocations and six existing diagnostics. Whole ELF changes
only the target slot and its symbol-size field 12 -> 272; all 6,058 slot
addresses/extents, protected data, converted rows/bytes and 11,475 guards stay
unchanged. Total 5,484 converted / 3,397 exact; Game 4,811 / 2,724;
zero drift and 2,087 different. All eight post-install tests pass in 36.990s,
no skips; 24 shared tests and both tools checks pass. Qualify 8,092 guest
cases, 328,968 native32 cases and the actual callback table slot-74 path.
Tools 061d223 first, exact parent source/docs pin second, no push or older
mirror reset. Next false-zero `func_151DA6F8`, 144 words/frame0xD0,
is a constructor in the same owner. Graph repair and hardware/gameplay stay
open; OGL Release remains frozen. See Note 1148 for receipts and limits.

Previous Game constructor restoration:
[Note 1147](WORKING_NOTES/1147-game-record-constructor-restoration-20261009.md).
Replace false-zero `func_151D71B0` with its complete 45-word / 180-byte /
frame0x50 C body. It emits every retail word directly, without guards.
Recover the mixed O32 ABI, 24-byte initial payload, conditional copy and
preserved allocation result. The typed `func_151D74B0` caller remains
byte-identical. All 23 functions in generated_204660.c now match retail.
Full linked audit permits only the target's 180-byte slot and its symbol-size
field 12 -> 180; every other ELF byte and all 6,058 slot addresses/extents
remain unchanged. Converted counts/bytes and all 11,475 guards are unchanged.
Total 5,484 converted / 3,396 exact; Game 4,811 / 2,723; zero drift and
2,088 different. All eight post-install tests pass in 33.365s, no skips;
24 shared tests and both tools checks pass. Tools ce159a5 banked first,
exact parent source/docs pin second, no push; preserve older mirror edits.
Next false-zero `func_151D9EB0`, 68 words/frame0x60, is a timer/randomized
effect callback in game_2062D0.c. Graph repair and hardware/gameplay stay
open; OGL Release remains frozen. See Note 1147 for receipts and limits.

Previous Game actor position conversion:
[Note 1146](WORKING_NOTES/1146-game-record-actor-position-conversion-20261008.md).
Install complete `func_151D75C4`: 88 words / 352 bytes / retail frame 0x30.
Recover actor/identity/optional gates, unsigned joint mapping, the complete
point transform and signed secondary callback with forwarded s32 return.
Raw C has six frame differences; a closed fingerprinted frame/home mapping
derives six guards. All seven relocation words and every other instruction
stay unchanged. Fresh full audit preserves every ELF byte, all 6,058 symbols
and protected data; only this 352-byte row changes asm -> c. Total 5,484
converted / 3,395 exact; Game 4,811 / 2,722; zero drift, 2,089 different and
11,475 guards. Tools de603ef banked first, exact parent pin/source/docs second;
no push. Root README aggregates only. Qualify 14,912 three-stream cases,
73,728 native cases, complete point/SDK helpers and actual primary slot-0 caller.
Next `func_151D71B0`, 45 words/frame0x50, is still a false zero-return C
constructor. `func_151D7538` is already restored as a three-argument event
handler, not an unqualified primary callback. No GLOBAL_ASM remains in this
owner, but semantic placeholders remain. Linked setup, graph repair and
hardware/gameplay stay open; host Release remains frozen. All ten post-install
tests pass in 134.082s, no skips; 24 shared tests and both tools checks pass.
132 docs / 4,133 relative links / zero broken. See Note 1146 for detailed receipts.

Previous Game callback update conversion:
[Note 1145](WORKING_NOTES/1145-game-record-callback-update-conversion-20261008.md).
Install complete `func_151D7264`: 81 words / 324 bytes / frame 0x40.
Recover the unsigned callback selector, pre-call position/flag capture, live
distance/attachment gate and failure writes. Selected C has nine raw word
differences; a closed nine-word reorder derives nine guards without looking
up retail words. All seven relocated words remain unchanged. Fresh full
linked audit preserves every ELF byte, all 6,058 symbols and protected data;
exactly one progress row changes asm -> c. Total 5,483 converted / 3,394 exact;
Game 4,810 / 2,721; zero drift, 2,089 different and 11,469 guards. Tools f7272ba
banked first, exact parent source/docs pin second, no push. README aggregates only.
Focused qualification covers raw/normalized/retail public access order,
fault prefixes, 67,736 native C cases, real table callbacks 2/3/4, complete
allocation/constructor bodies, copied-owner neighbors and effective negatives.
Next retained `func_151D75C4`, 88 words/frame0x30, is actual callback table slot 0.
Table slot 1, linked setup, Graphify reduced-corpus repair and hardware/gameplay
acceptance remain open. Host Release stays frozen. All 11 post-install tests
pass in 77.792s, no skips; 24 shared tests and both tools checks pass.
131 docs / 4,125 relative links / zero broken. See Note 1145 for detailed receipts.

Previous Game renderer conversion:
[Note 1144](WORKING_NOTES/1144-game-record-ring-renderer-conversion-20261008.md).
Install complete `func_151D80C4`: 405 words / 1,620 bytes / frame 0xD0.
Raw C differs at 185 words; the qualified GP/save/factor normalizer derives
185 guarded adjustments without a retail-word lookup, insertion or padding.
All 16 relocated words remain unchanged. Fresh linked audit confirms the
complete ELF, all 6,058 bodies/addresses/extents and protected data unchanged;
only this 1,620-byte progress row changes asm -> c. Total 5,482 converted /
3,393 exact; Game 4,809 / 2,720; zero drift and 2,089 different. Guards 11,460,
with the old 11,275-row prefix preserved byte-for-byte. Tools 36bead0 banked
first; parent source/docs pin follows, no push. Root README aggregates only.
Next retained `func_151D7264`: 81 words / frame 0x40, callback-driven record
update and distance gate. Linked setup, graph refresh repair and hardware/
gameplay acceptance remain separate and open; host Release stays frozen.
Fresh 31 post-install tests pass in 227.669s, no skips; 14 shared tests and
both tools checks pass. 130 docs / 4,117 relative links / zero broken.

Previous Game live-value proof:
[Note 1143](WORKING_NOTES/1143-game-record-ring-renderer-live-value-proof-20261008.md).
Same complete uninstalled `func_151D80C4`, 405 words/frame0xD0 and 185 raw
differences. Derive the closed factor-arm/delay reorder; validate GP live
relationships over 383 CFG nodes/404 words/560 obligations and all six calls,
including loop joins, volatile kills and owned-frame save closure. Four
independent rebases pass. 131,072 exhaustive opacity pairs and 432 whole-entry
three-stream cases pass; 30 distinct focused tests pass across selected runs.
No production normalization/source/progress/guard/README change. Tools 4253f3a
first, exact parent pin second; older unrelated dirty work preserved, no push.
Next derive/qualify relocation-aware normalization and private fault-state
boundaries before installation/rebuild/credit. Wider acceptance stays open.

Previous Game setup fitting:
[Note 1142](WORKING_NOTES/1142-game-record-ring-renderer-setup-fitting-20261008.md).
Same complete uninstalled `func_151D80C4`, 405 words/frame0xD0; raw differences
198 -> 185, mode-input order restored and default-factor hoisting removed.
Use SETUP_FITTED next. 22 focused tests pass in 134.298s: new complete-body
qualification, 432 whole-entry public prefix cases, 668 early fault pairs,
408 final-lookahead pairs and 16 effective mode-order negatives. 176 GP-only /
nine other is not a proven remap; GP-only +0x28C belongs to the factor CFG block.
All installed bodies/data/source/progress/11,275 guards and README unchanged.
Tools b0f5e40 first, exact parent pin second; older mirror preserved, no push.
Next factor-arm CFG and consistent GP/private-state mapping before installation;
linked setup, reduced-corpus graph repair and hardware/gameplay stay open.

Previous Game scheduling audit:
[Note 1141](WORKING_NOTES/1141-game-record-ring-renderer-scheduling-audit-20261008.md).
Same complete uninstalled `func_151D80C4`, still 405 words/frame0xD0 and
198 raw differences after 26 full forms. Partition: 167 GP-field-only,
31 other words; not a proven register remap. 25 tests pass in 200.736s,
including 408 post-MODE final-lookahead fault-prefix pairs and an effective
early-exit negative that passes ordinary outputs. All installed bodies/data/
source/progress/11,275 guards and README aggregates unchanged. Tools 1f3f5be
first, exact parent pin second; older dirty mirror preserved, no push.
Next fit factor initialization and mode-input load order in this same body;
whole-entry/private fault state and closed mapping remain gates before
installation. Linked setup, reduced-corpus graph repair and gameplay stay open.

Previous Game fitting:
[Note 1140](WORKING_NOTES/1140-game-record-ring-renderer-frame-fitting-20261008.md).
Same complete uninstalled `func_151D80C4`: C now matches the 405-word/frame
0xD0 extent and retail private/saved slots; raw differences fall 319 -> 198.
21 tests pass in 148.226s, requalifying original and fitted bodies, plus
64 guest aliases and 768 independently linked rebased executions. Preserve
22 neighbors and all installed bodies/data/source/progress/11,275 guards.
Tools 9d466ca banked first, exact parent pin second; older dirty mirror
preserved, no push or README change. Next fit this same body's GP roles and
schedule, then qualify fault prefixes/closed transformations before installing.
Linked setup, graph repair and hardware/gameplay remain open.

Previous Game recovery:
[Note 1139](WORKING_NOTES/1139-game-record-ring-renderer-recovery-20261008.md).
Complete uninstalled `func_151D80C4` ribbon recovery: retail 405 words/frame
0xD0; natural C 405/frame0xE0/319 raw differences. Nine tests pass in
63.057s: 988 guest cases, 512 cursor/count cases, 1,086 native32 cases,
22 missing-byte gates, eight negatives and 256 connected cases. Qualify
render-table entry 16 through original caller/actual backend; setup/deep
calls stay bounded. Preserve 22 copied-owner neighbors and every installed
body/data/source/progress/11,275 guards. Tools a22175b banked first, exact
parent pin second; older dirty mirror preserved, no push. Counts and README
aggregates unchanged. Next fit this same target's extent/frame/private and
saved lifetimes, then aliases, independent rebases and installation gates.
Linked dispatcher/combiner, graph repair and hardware/gameplay remain open.

Previous Game shaping conversion:
[Note 1138](WORKING_NOTES/1138-game-record-ring-shaping-conversion-20261008.md).
Finish complete `func_151D7CD0`: 253 words / 1,012 bytes / frame 0xB8,
183 direct words plus 70 closed allocation/spill/scheduling guards.
Eight installed tests pass in 163.182s; eleven affected-neighbor checks
pass in 117.305s. Tools 5c9e50b is banked first; source/docs record its exact
pin. Native32 covers 155,964 cases; six independent links
verify 13 relocation sites with 240 executions. All 6,058 linked bodies,
addresses, extents and protected sections/data unchanged; prior 11,205
guard rows/raw prefix preserved, sole 1,012-byte ASM-to-C conversion.
Converted 5,481 / Game 4,808; exact 3,392 / Game 2,719; zero drift.
README aggregates only. Next retained `func_151D80C4`: 405 words/frame0xD0.
Linked dispatcher restoration, hardware/gameplay and reduced-corpus graph
repair remain open. No host/runtime/Release changes or push.

Previous Game recovery checkpoint:
[Note 1137](WORKING_NOTES/1137-game-record-ring-shaping-recovery-20261008.md).
Complete uninstalled `func_151D7CD0` recovery: retail 253 words/frame0xB8,
natural C 256/frame0x98/253 differences. Seven tests pass in 71.119s:
1,861 guest cases, 84 bounded conversion cases, 66 faults, eleven negatives
and 48 connected cases / 96 executions. Correct third-table callback 4
and preserve original dispatcher/linked-placeholder distinction.
Copied owners preserve 22 neighbors/pools/relocations; real padder rejects
the oversized candidate. All 6,058 installed bodies/data/progress/11,205
guards unchanged. Tools 856ba00 banked first, parent records exact pin;
older dirty mirror preserved, no push. No conversion credit or README change.
Next: fit this same target's complete extent/frame/saved lifetimes, then
native32, independent rebases and installation qualification. Graph refresh
refuses reduced corpus; hardware/gameplay and linked dispatcher remain open.

Previous Game recovery and authorized banking:
[Note 1136](WORKING_NOTES/1136-game-record-ring-sampling-conversion-20261008.md).
Convert retained `func_151D7A38`: 166 words / 664 bytes / frame 0xC8;
129 direct words plus 37 closed register/spill/loop-scheduling guards.
Seven installed tests pass in 104.050s: 1,889 guest / 264,704 native32 cases,
314 faults, eleven negatives, 120 rebases and 96 connected cases across raw,
normalized and retail bodies. Nine affected older checks pass in 112.141s
after preserving shared declarations/later guards in the ring fixture.
All 6,058 bodies/addresses/extents/protected sections/data unchanged; prior
11,168 guards/raw prefix preserved plus 37, sole 664-byte conversion.
Converted 5,480 / Game 4,807; exact 3,391 / Game 2,718; zero drift.
Tools 9fb0eb2 banked first, parent records exact pin; no push or older
standalone reset. New sampling baseline; README aggregates only.
Next retained `func_151D7CD0`: 253 words / frame 0xB8; backward passes and
FCSR conversion require fresh callee/lifetime qualification. Original
dispatcher connections do not restore its linked placeholder; hardware/
gameplay and graph refresh remain open. No host/runtime/Release changes.

Previous Game recovery and authorized banking:
[Note 1135](WORKING_NOTES/1135-game-record-ring-update-conversion-20261008.md).
Convert retained `func_151D792C`: 67 words / 268 bytes / frame 0x30;
54 direct words plus 13 strict final-output scheduling/register guards.
Eight installed tests pass in 113.683s: 2,743 guest / 404,131 native32 cases,
157 faults, ten negatives, 144 rebases and 512 connected cases against both
bodies. Six affected older checks pass in 66.113s. Original dispatcher
connection is separate from its still-placeholder linked C body.
All 6,058 bodies/addresses/extents/protected sections/data unchanged; prior
11,155 guards/raw prefix preserved plus 13, sole 268-byte conversion.
Converted 5,479 / Game 4,806; exact 3,390 / Game 2,717; zero drift.
Tools 74cbbdc banked first, parent records exact pin; no push or older
standalone reset. New ring-update baseline; README aggregates only.
Next retained `func_151D7A38`: 166 words / frame 0xC8, interpolation and
live ring-state recovery pending. Graph refresh, linked dispatcher/constructor,
hardware/gameplay remain open; no host/runtime/Release changes.

Previous Game recovery and authorized banking:
[Note 1134](WORKING_NOTES/1134-game-attachment-allocation-direct-conversion-20261008.md).
Convert retained `func_151D7830`: 63 words / 252 bytes / frame 0x88 directly
exact, no guards. Two position packets, eleven-argument ABI, lazy allocation
failure and captured owner/record lifetime qualify. Eight installed tests pass
in 54.737s: 4,114 guest / 138,752 native32 cases, 632 fault prefixes, eight
negatives, 180 rebases and 64 connected cases / 128 executions. Original retail
constructor connection is separate from its still-placeholder linked C body.
All 6,058 bodies/addresses/extents/protected sections/data/11,155 guards unchanged;
sole 252-byte conversion. Converted 5,478 / Game 4,805; exact 3,389 / Game 2,716;
2,089 different / zero drift. New allocation baseline; README aggregates only.
Tools 56c4132 committed first; parent records its exact pin, no push or older
standalone reset. Next retained `func_151D792C`: 67 words / frame 0x30, backward
ring cursor, live goal/state reloads and captured ring-buffer recovery pending.
Graph refresh, alternate caller/constructor branches and hardware/gameplay
remain open; no host/runtime/Release changes.

Previous Game recovery and authorized banking:
[Note 1133](WORKING_NOTES/1133-game-attached-record-cleanup-direct-conversion-20261008.md).
Convert retained `func_151D77C8`:26 words/104 bytes/frame0 directly exact,
no guards. Typed void interface, captured nested link, unsigned flag updates,
live owner reloads and nested-before-owner clear qualify. All ten installed
target/neighbor tests pass in47.235s:66,304 guest /786,432 native32 cases,
93 fault prefixes, eight negatives,768 rebases and224 complete wrapper links.
All6,058 bodies/addresses/extents/protected sections/data/11,155 guards unchanged;
sole104-byte conversion. Converted5,477/Game4,804; exact3,388/Game2,715;
2,089 different/zero drift. New cleanup baseline; README aggregates only.
Tools6f18cf1 committed first; parent records its exact pin, no push or older
standalone reset. Next retainedfunc_151D7830:
63 words/frame0x88, stack-packet allocation/copy recovery pending. Graph refresh,
larger gate caller, hardware/gameplay remain open; no host/runtime/Release changes.

Previous Game recovery and authorized banking:
[Note 1132](WORKING_NOTES/1132-game-record-velocity-integrator-conversion-20261008.md).
Convert retained `func_151D8718`:19 words/76 bytes/frame0;16 direct words
plus three strict captured-velocity FP allocation/operand-order guards.
Eight installed target tests pass:34,692 guest /12,240 native32 cases,
23 fault prefixes, eight negatives,840 rebases and768 complete ring-caller
connections. All6,058 bodies/addresses/extents/protected sections/data
unchanged; prior11,152 guards plus three, sole76-byte asm-to-C conversion.
Converted5,476/Game4,803; exact3,387/Game2,714;2,089 different/zero drift.
New velocity baseline; root README aggregates only. Four affected state/
constructor checks and the callback guard-history check also pass. Tools
f36e9af committed first; source checkpoint records its exact pin, no push.
Next retained `func_151D77C8`:26 words/frame0; recover return/attached-record
cleanup and live pointer reloads before fitting. Second caller, hardware/FCSR,
gameplay and Graphify refresh remain open; no host/runtime/Release changes.

Previous Game recovery and authorized banking:
[Note 1131](WORKING_NOTES/1131-game-record-state-update-conversion-20261008.md).
Convert final retained `func_151D8A24` in generated_205C90:64 words/256 bytes/
frame0x28,60 direct words plus four strict private expiry-byte guards.
Timer truncation, signed callback selector, captured expiry/owner, live
mask/level and clear-before-register/free-last ordering qualify.
Fresh all49 installed target/five-neighbor tests pass in867.646s, no skips.
267,364 guest /1,607,424 native32 cases,38 fault prefixes,640 mutations,
nine negatives,216 rebases and1,152 complete wrapper/clearer connections pass.
All6,058 bodies/addresses/extents/protected sections/data unchanged; prior
11,148 guards preserved plus four, sole256-byte asm-to-C conversion.
Converted5,475/Game4,802; exact3,386/Game2,713;2,089 different/zero drift.
New state-update baseline; root README aggregates only. Tools8e1a208 banked
before source/docs/exact pin; no push, older dirty mirror preserved.
Next retained `func_151D8718`:19 words/frame0, complete float integration
candidate has three raw differences, uninstalled/unqualified. Graph refresh
incomplete; controlled later callees and hardware/gameplay remain open.

Previous Game recovery work:
[Note 1130](WORKING_NOTES/1130-game-record-player-registration-conversion-20261008.md).
Convert complete `func_151D8868`:111 words/444 bytes/frame0x30;
109 words direct plus two strict branch/limit-load scheduling guards.
Ordered gates, live validation mask/limit, allocation failure, eight-byte copy,
live registration mask/level and captured-owner lifetime qualify.
Fresh expanded41-test suite passes in601.805s, including nine target tests:
110,604 guest /2,163,968 native32 cases,68 required fault prefixes, eight
effective negatives, six links/576 rebases and9,216 complete predicate links.
Controlled later callees and bounded C-domain/fault limitations remain explicit.
All6,058 bodies/addresses/extents/protected sections/data unchanged; prior
11,146 guards preserved plus two, sole444-byte asm-to-C conversion row.
Converted5,474/Game4,801; exact3,385/Game2,712;2,089 different/zero drift.
New registration baseline; root README aggregates only. Tools6e2e24d banked
before parent pin; no push. Dirty older standalone mirror preserved.
Next retained `func_151D8A24`:64 words/frame0x28, complete candidate has four
raw differences, uninstalled and not behavior-qualified. Graph refresh
incomplete; zero Claude calls, no runtime/Release changes.

Previous Game recovery work:
[Note 1129](WORKING_NOTES/1129-game-selected-player-state-direct-conversion-20261008.md).
Convert retained `func_151D87E0`:34 words/frame0 directly exact, no guards/
data/profile changes. Selected-only byte reads and invalid-first/ready-first
returns qualify. Installed eight tests pass in102.672s:173,184 guest /
3,608,576 native32 cases,24 fault prefixes, seven negatives, eight independent
links and24,576 bounded actual caller-prefix/real-epilogue cases. Positive
caller continuation is synthetic; full caller/gameplay remains open.
All6,058 bodies/data/11,146 guards unchanged; sole136-byte conversion.
Converted5,473/Game4,800; exact3,384/Game2,711;2,089 different/zero drift.
New selected-player baseline; root README aggregates only. Bank completed
Notes1126-1129 in coherent tools/source commits per "Keep commited" request.
Tools7f3c323/fbd3fd8 committed locally; no push. Zero Claude calls.
Next retained `func_151D8868`:111 words/frame0x30, complete contract/fitting
and positive-continuation qualification pending. Graph refresh incomplete.

Previous Game recovery work:
[Note 1128](WORKING_NOTES/1128-game-record-player-mask-direct-conversion-20261008.md).
Convert retained `func_151D8B24`:25 words/frame0x20 directly exact, no guards/
data/profile changes. Live per-player mask reads, captured owner and byte
counter qualify; explicit pointer casts retain both caller bodies.
Installed eight tests pass in145.264s:197,120 guest /1,114,368 native32 cases,
twelve faults, seven negatives,25,600 actual clearer/alias and3,072 complete
caller cases. All6,058 bodies/data/11,146 guards unchanged; sole100-byte
conversion. Converted5,472/Game4,799; exact3,383/Game2,710;2,089 different/
zero drift. New player-mask baseline; root README aggregates only.
Next retained `func_151D87E0` has a complete34-word direct candidate, not
installed/behavior-qualified. Graph refresh incomplete; zero Claude calls,
external source/tools commits preserved, no Codex commit/push.

Previous Game recovery work:
[Note 1127](WORKING_NOTES/1127-game-record-distance-level-direct-conversion-20261008.md).
Convert retained `func_151D8C00`:87 words/frame 0x38 directly exact,
typed parameters and forward declaration; wrapper cast retains its8 words.
Eight pre tests pass, installed helper/wrapper16 tests pass; latest typed
wrapper8 tests pass. Qualify49,152 guest /6,144 native32 helper cases,
72 mutation/alias cases, ten faults, six negatives,48 connected cases and
ten unchanged neighbors. All6,058 bodies/data/11,146 guards unchanged;
sole348-byte conversion. Converted5,471/Game4,798; exact3,382/Game2,709;
2,089 different/zero drift. Fresh distance-level baseline and README
aggregates only. Source/tools commits and frozen OGL Release preserved.
Next retained `func_151D8B24`:25-word four-player live-mask loop.
Its complete ignored candidate already matches all25 words under O2/g3;
mutation/native/caller qualification and installation remain pending.
Graph refresh remains incomplete; no Codex commit/push or Claude calls.

Previous Game recovery work:
[Note 1126](WORKING_NOTES/1126-game-embedded-record-callback-direct-conversion-20261008.md).
Convert retained `func_151D8BE0` callback to complete C: all 8 words/frame 0x18
directly exact, no guards/data/profile changes. Actual table/dispatcher
confirms one record argument, embedded+0x18 forwarding and ignored result.
Eight pre/post tests pass in 29.054s/33.021s:131,248 guest /1,048,576 native32
cases,96 mutation/alias cases, ten faults,96 actual indirect dispatch cases,
ten owner neighbors and six independent links. All6,058 linked bodies/data/
guards unchanged; only 32-byte conversion row changes. Converted 5,470,
Game 4,797; exact 3,381, Game 2,708, 2,089 different/zero drift. Fresh baseline
`game-record-embedded-callback-test/after.json`; ten shared checks pass.
External commits advance source to c73a85af and parent/mounted tools pin to
8d84f4b; preserve them. No commit/push by Codex; own source/test work remains
local, standalone tools mirrored. Graph refresh still incomplete; old graph
preserved. Zero Claude calls under the focused workflow.
Next `func_151D8C00` complete candidate is already87 words/frame 0x38 directly
exact, but remains assembly-backed pending FP/conversion/mutation/native/
copied-owner and connected-wrapper qualification. Wider Game remains open.

Previous Game recovery work:
[Note 1125](WORKING_NOTES/1125-game-node-group-swap-direct-conversion-20261008.md).
Convert retained `func_15033EC4` to complete C: all 18 words/frame0 directly
exact, no new guards/filler/data/profile changes. Preserve full32 key
comparisons, byte writes, captured head/current link and live future links.
All eight pre-install/post-install tests pass in 98.473s/48.169s: 114,945
guest /16,951,557 native32 cases, ten faults, three aliases, seven negatives,
39 owner neighbors, six links and 50 actual caller-prefix/callee cases.
All 6,058 bodies/addresses/extents/protected sections/data/11,146 guards stay
unchanged; only the 72-byte conversion row changes. Converted total 5,469,
Game 4,796; exact total 3,380, Game 2,707, 2,089 different /zero drift.
New `game-node-group-swap-test/after.json`. Ten shared padder checks pass.
[Agent workflow](AGENT_WORKFLOW.md) is installed: focused fresh gates and
unchanged-body audit, explicit reuse of prior broad-suite receipts, zero
Claude calls. Validate 111 documents /3,896 relative links, zero broken;
eleven relevant tools files byte-identical. Graphify refresh refused reduced
corpus; old graph preserved. No commit/push. Preserve mounted tools 35dd106 versus parent
pin ddbdd16 difference and ignore edits. Next `func_151D8BE0`, retained
8-word wrapper; caller/return contract and wider Game/runtime remain open.

Previous Game recovery work:
[Note 1124](WORKING_NOTES/1124-game-node-group-collector-direct-conversion-20261008.md).
Convert retained `func_15033E28` assembly to complete C: all 23 words/frame0
directly exact, no guards/filler/data/profile changes. Capture list head once,
reload actor group each iteration and capture next before aliased output stores.
Qualify 69,633 guest /262,152 native32 cases, all 23 words, byte pairs/masks/
topologies, thirteen faults, five aliases, seven negatives, 39 owner neighbors
and six independent links/eighteen executions. Static retail caller confirms
actor/pointer-array/count interface; full calling workflow remains open.
All 6,058 bodies/addresses/extents/protected sections/720 data owners/11,146
guards unchanged. Only conversion row changes asm -> c, 92 bytes. Converted
total 5,468/6,042 (90.50%), Game 4,795/5,321 (90.11%), Game bytes 84.95%.
Exact total 3,379/5,468 (61.80%), Game 2,706/4,795 (56.43%), 2,089 different,
zero drift. README aggregates only; new baseline:
`game-node-group-collector-test/after.json`. Seven corrected pre-install tests
pass in 57.702s. All 61 combined post-install tests pass in 852.236s, then
all eight strengthened collector tests pass in 88.381s, including six actual
stack-output-layout cases; 62 unique focused checks, zero skips/errors/failures.
Ten shared padder tests/tools/syntax/driver/profile/CLI/whitespace checks pass.
Validate 107 documents /3,868 relative links, zero broken; all eight changed
tools files byte-identical. Tools files mirrored locally,
uncommitted/unpublished; pin unchanged. Next local `func_15033EC4`, retained
assembly, 18 words/frame0, full32-key group swap; static inventory only.
Wider Game goal remains open.

Previous Game recovery work:
[Note 1123](WORKING_NOTES/1123-game-effect-callback-scheduling-match-20261008.md).
Complete `func_15033BDC` is installed: 137 words/frame0x40 byte-exact,
135 words directly emitted plus two independent scheduling guards. Recover
the actual seven-pointer Init callback ABI, third-argument volume, coordinate
copies, live type/audio lifecycle and state-before-allocation behavior.
Qualification: 12,352 guest /524,288 native32 cases, 135 reachable words,
callback mutations, twenty faults, three aliases, eleven effective negatives,
39 owner neighbors and seven independent links. Only target changes across
6,058 symbols; addresses/extents/protected sections/720 data owners and all
11,144 prior guards/conversions unchanged. Append exactly two rows (11,146).
Exact total 3,378/5,467 (61.79%), Game 2,705/4,794 (56.42%), 2,089 different,
zero drift. README aggregates only. New baseline:
`game-node-effect-callback-test/after.json`. Seven corrected pre-install tests
pass in 96.442s. All 54 post-install tests pass in 439.695s, zero skips/errors/
failures; ten shared padder tests/tools/syntax/driver/profile/CLI/whitespace
checks pass. Validate 106 documents /3,856 relative links, zero broken; all
six changed tools files byte-identical in both copies. Full callees/FP/FCSR/
runtime open.
Tools changes mirrored locally, uncommitted/unpublished; committed pin
unchanged. Next local `func_15033E28`, retained compiler-generated assembly,
23 words/frame0, linked-list group collector; static inventory only.
Wider Game goal remains open.

Previous Game recovery work:
[Note 1122](WORKING_NOTES/1122-game-delayed-effect-direct-match-20261008.md).
Complete `func_15033AD8` is installed: all65 words/frame0x40 directly exact,
no guards, filler, data or profile changes. Optional proximity precedes state;
signed timer below30 adds the live step once, otherwise twelve-word effect
creation stores returned handle then state0x513, including zero result.
Qualification:10,360 guest/524,288 native32 cases, all65 words, all flag bytes,
all u16 results/signed16 X actually observed, callbacks/faults/aliases/negatives,
39 owner neighbors and seven independent links. Full callees/FP/FCSR/runtime
remain open. Only target changes across6,058 symbols; addresses/extents/
protected sections/720 data owners/11,144 guards/conversions unchanged.
Exact total3,377/5,467 (61.77%), Game2,704/4,794 (56.40%),2,090 different,
zero drift. README aggregates only. New baseline:
`game-node-delayed-effect-test/after.json`. Seven pre-install tests pass
in64.312s. All47 post-install focused tests pass in544.431s, zero skips/errors/
failures; ten padder tests/tools/syntax/driver/profile/CLI/whitespace pass.
Documentation:105 documents/3,844 relative links, zero broken.
Tools changes mirrored in both checkouts, not yet committed or
published; committed tools pin unchanged. Next local `func_15033BDC`,137 words/
frame0x40, effect callback; static inventory only. Wider Game goal remains open.

Previous Game recovery work:
[Note 1121](WORKING_NOTES/1121-game-effect-registration-direct-match-20261008.md).
Complete `func_150339C8` is installed: all 68 words/frame0x40 directly exact,
no guards, filler, data or profile changes. Recover tile-scroll-before-gates,
freeze/unregister/clear order, existing handles and twelve-argument effect
creation with signed16 coordinates/high handle bit. Qualification: 14,208
guest cases, 576 actual-helper-connected cases, 1,572,864 native32 executions,
67/68 reachable words, lazy/fault/alias/negative checks, 39 owner neighbors and
eight independent symbol/entry links. Native arrays prove all u16 results and
signed16 X coordinates observed at creation; invalid FP/FCSR stay unqualified.
Only target changes across 6,058 symbols; 6,057 other bodies, addresses/extents,
protected sections, 720 data owners, 11,144 guards and conversions unchanged.
Exact total 3,376/5,467 (61.75%), Game 2,703/4,794 (56.38%), 2,091 different,
zero drift. README aggregates only. New baseline:
`game-node-effect-registration-test/after.json`. Eight strengthened pre-install
tests pass in96.321s. Final 37 post-install focused tests pass in221.412s,
zero skips/errors/failures, including six added connected faults. Preserve
two shared prototypes in the earlier cleanup fixture; strict comparisons
unchanged. Ten padder tests/tools/syntax/driver/profile/CLI/whitespace pass.
Documentation:103 documents/4,200 relative links, zero broken.
Next local `func_15033AD8`, 65 words/frame0x40,
timer-gated effect creation; inventory only. Wider Game/full runtime open.

Previous Game recovery work:
[Note 1120](WORKING_NOTES/1120-game-attachment-state-latch-direct-match-20261008.md).
Complete `func_15033838` is installed: all 100 words/frame0x20 directly exact,
no guards, padding, generated data or profile changes. Recover action/type/
subtype gates, mode-6 bypass, ordered activation/hold fields and latch writes
before callbacks. Qualification: 33,792 guest cases, 794,368 actual native32
executions, 99/100 reachable words, six lazy gates, 23 faults, four aliases,
eight effective negatives, 39 owner neighbors and three padder/call links.
Only target changes across 6,058 symbols; other 6,057 bodies, all addresses,
protected sections, 720 data owners, 11,144 guards and conversions unchanged.
Exact total 3,375/5,467 (61.73%), Game 2,702/4,794 (56.36%), 2,092 different,
zero drift. README aggregates only. New baseline:
`game-node-attachment-latch-test/after.json`. Initial seven tests pass in43.922s;
strengthened native test passes in1.141s. All 29 post-install focused tests
pass in233.647s, zero skips/errors/failures; ten shared padder tests/tools/
syntax/driver/profile/whitespace checks pass. Documentation validation:
102 documents/4,183 relative links, zero broken.
Next local `func_150339C8`, 68 words/frame0x40, effect-registration gate;
inventory only. Full callback/runtime and wider Game work remain open.

Previous Game recovery work:
[Note 1119](WORKING_NOTES/1119-game-matrix-creation-and-transform-setup-direct-matches-20261008.md).
Complete `func_150335C8` and its final helper `func_15030D54` are installed:
113 words/frame0x168 and45 words/frame0x20 directly exact, no guards/padding/
new data/profile changes. Recover matrix-backed creation, post-callback homes,
position/angle decomposition and six-float record allocation with live pointer
reloads. Qualification:10,058 caller/961 helper/480 connected guest cases,
65,536 native32 executions,112/113 and45/45 reachable words, allocation failures,
faults/aliases/controls/padder/call rebases. Matrix/allocator callbacks remain
controlled hooks, not complete-library/hardware/gameplay acceptance.
Only these two targets change across6,058 symbols; all other6,056 bodies,
addresses/extents/protected sections/720 data owners/11,144 guards/conversion
hash intact. Exact total3,374/5,467 (61.72%),Game2,701/4,794 (56.34%),2,093
different,zero drift. README aggregates only; new baseline:
`game-node-matrix-creation-test/after.json`. All28 post-install focused tests
pass in176.922s, no skips/errors/failures; ten shared padder tests/tools/syntax/
CLI/owner/profiles/whitespace pass. Strengthened eight tests pass in48.566s,
including twenty fault prefixes. Next local `func_15033838`,100 words/
frame0x20, attachment-state latch; inventory only. Wider Game/full runtime open.
Documentation:101 documents/4,169 relative links,zero broken.

Previous Game recovery work:
[Note 1118](WORKING_NOTES/1118-game-fourth-tile-scroll-direct-match-20261008.md).
`func_150334B8` is installed: all68 words/frame0 emit directly from C, no
guards/padding/relocations/generated data. Recover action0x37's fourth signed
tile-size scan, S-100 and per-axis span+2 one-step wrapping, not modulo.
Seven pre-install tests pass in43.357s:45,063 guest/16,384 native32 cases,
all selector bytes and4,096 coordinate values per axis,67/68 reachable words,
faults/aliases/controls/owner/padder/entry rebases. Native opcode seeding's
host-endian T-byte overlap is explicit; guest tests provide big-endian coverage.
Only target changes across6,058 symbols; all addresses/extents/protected sections,
720 data owners/11,144 guards/conversion hash intact. Exact total3,372/5,467
(61.68%),Game2,699/4,794 (56.30%),2,095 different,zero drift. README matching
aggregates only. New baseline: `game-node-tile-scroll-test/after.json`.
All20 post-install focused tests pass in112.504s, zero skips/errors/failures,
including earlier owner/padder and dispatcher binding/scheduling checks.
Ten shared padder tests/tools/syntax/CLI/profiles/whitespace pass.
Documentation:100 documents/4,153 relative links,zero broken.
Next local placeholder `func_150335C8`,113 words/frame0x168, matrix-backed
creation path; inventory only. Full callee/hardware/gameplay/PC-port and wider
Game work remain open.

Previous Game recovery work:
[Note 1117](WORKING_NOTES/1117-game-attachment-selection-closed-scheduling-match-20261008.md).
Complete semantic `func_15031FC8` is installed and byte-exact across all1148
words/frame0x48. Raw C has304 differences;14 symbolic table bindings and67
checked closed-scheduling rows normalize existing instructions and derived
branch destinations. This is not a direct compiler-only match. Every compiler
instruction origin occurs once; four cached-model reads retarget A0 to V1.
All674 retained table targets and assembled label offsets fit, no generated
data or filler. Source action0x85/0x98 shapes recover the last15 raw differences.
Only target changes across6,058 symbols;6,057 other bodies and all addresses/
extents/protected sections/720 data owners/conversion hash remain intact.
Prior11,063 guards preserved;81 target rows added. Exact total3,371/5,467
(61.66%), Game2,698/4,794 (56.28%),2,096 different,zero drift. Converted counts
unchanged; README matching aggregates only. New baseline:
`game-node-selection-test/after.json`.
All40 unique checks qualify across combined/targeted runs; final20 focused
tests pass in116.371s, zero skips/errors/failures. Two copied-owner assumptions
were corrected with checked pool relocation/ownership, not production edits.
Exhaustive92,992 dispatch and12,348 native32 cases pass. Ten padder tests,
tools/syntax/CLI/whitespace and99-document /4,139-relative-link checks pass,
zero broken links. The focused coverage receipt is
corrected from the older overcount4,005 to3,925 actual executions; coverage
remains1,125 words. The normalized actual-padder execution checks6,352 cases.
Next local placeholder: `func_150334B8`,68-word leaf/frame0; static inventory
only. Full callee/FCSR/hardware/PC-port and broader Game boundaries remain open.

Previous Game recovery work:
[Note 1116](WORKING_NOTES/1116-game-attachment-selection-frame-and-opening-recovery-20261008.md).
Experimental C1148/frame0x48/319 recovered the six private homes, first19 and
final68 words without guards. Twelve field-pointer forms emit identical raw
text/pools. Its C321 intermediate passes34 tests, then13 final C319 tests pass
in495.191s. Model/flags scheduling and84 shifted table targets were still open
at that checkpoint; Note1117 above closes installation. The older focused-case
receipt4,005 was an80-case reporting overcount, now corrected to3,925.

Previous Game recovery work:
[Note 1115](WORKING_NOTES/1115-game-attachment-selection-lifetime-and-table-binding-20261008.md).
Complete experiment-only `func_15031FC8` improves to C1148/frame0x38/349
differences, down from394, recovering retail's A3 tail attachment lifetime.
Four binding tests pass:14 experimental rows qualify seven physical table
addresses across the scalar gap,56 rebases,six stale controls,two effective
negatives and39 fully postprocessed owner neighbors. No generated data,
padding/insertion/omission, production CSV or README changes. Frame0x48,
private homes/scheduling and original table-target PC fit remain open; correct
table bases alone do not qualify installation. Target PCs are590/674 exact;
the other84 entries are one word late in C. All6,058 installed symbols,
protected sections/data/11,063 guards/conversion hash remain unchanged against
`game-node-tile-test/after.json`. Continue this dispatcher before installation.
All34 recovery/binding/installed tile-cleanup-action tests pass in578.223s;
ten padder/word-patch regressions pass in0.044s. Tools/syntax/CLI/whitespace
and97-document /4,115-relative-link checks pass, zero broken links. Defined
effects qualify; full callee/FCSR/hardware/PC-port boundaries remain open.

Previous Game recovery work:
[Note 1114](WORKING_NOTES/1114-game-attachment-selection-dispatcher-recovery-20261008.md).
Complete semantic `func_15031FC8` candidate is retained in experiments, not
installed. Selected C1147/frame0x38 has394 differences against retail1148/
frame0x48; no guards or production/profile edits. Nine tests pass across targeted
runs:92,992 guest dispatch,2,415 callback/float,12,348 native32,all674 table keys,
1,125 retail words,aliases/faults/controls/negatives. All21 installed tile/
cleanup/action regressions pass in225.613 seconds. Owner39 neighbors unchanged;
new table addends start412 instead of original416, confirming the scalar gap.
All6,058 installed symbols/sections/data/guards/conversion hash unchanged;
README totals remain unchanged. Continue this dispatcher's frame/scheduling and
physical table binding from the qualified candidate before installation.
Authoritative installed baseline remains `game-node-tile-test/after.json`.
Tools/syntax/CLI/whitespace and96-document /4,104-relative-link checks pass,
zero broken links; no full callee/FCSR/hardware/PC-port acceptance claim.

Latest direct Game placeholder recovery:
[Note 1113](WORKING_NOTES/1113-game-fourth-tile-size-command-direct-match-20261008.md).
`func_15031E7C` now emits all 83 words / 332 bytes directly, no frame, zero
differences versus 77 previously. Recover SDK Gfx/signed opcode scanning, the
fourth tile-size first-word update, actor-type overrides and inclusive binary32
progress arithmetic. Two-step factor computation recovers the retail FP sequence
without guards/profile/Makefile/header changes or generated data.
Seven pre-install tests pass in 29.428 seconds; strengthened alias checks pass
separately in 3.194 seconds. Qualification covers 13,152 guest / 19,728 native32
cases, 137 float patterns, six scan layouts, lazy/faults, five aliases, 12 controls
/ 960 ordinary executions, effective negatives, owner/padder/carry rebases.
Native raw opcode bytes are seeded for host endian; this is not graphics runtime,
full FCSR/hardware or PC-port acceptance. Only target changes across 6,058
symbols; all other bytes/addresses/extents/overflows/sections/720 Game-data
owners/11,063 guards/conversion hash intact. Exact total 3,370/5,467 (61.64%),
Game 2,697/4,794 (56.26%), 2,097 different, zero drift; conversions unchanged.
README matching aggregates only. Checkpoint: `game-node-tile-test/after.json`.
All 73 installed tile/cleanup/action/attachment/lookup/resolver regression
tests pass in 433.831 seconds, zero skips/errors/failures; tools/syntax/CLI/
whitespace and 95-document / 4,090-relative-link checks pass, zero broken links.
`func_15031FC8` now has the complete qualified experiment-only recovery above;
its production placeholder still has1,119 differences. Complete-owner pool
measurement confirms the four-byte scalar gap; matching/binding remain open.
Remaining Game and matrix/callee/runtime boundaries stay open.

Previous direct Game placeholder recovery:
[Note 1112](WORKING_NOTES/1112-game-node-cleanup-dispatcher-direct-match-20261008.md).
`func_15031C14` now emits all 134 words/frame `0x38` directly, zero differences
versus 129 previously. The complete cleanup dispatcher retains the null-actor
gate, counter/flag clears, registration callback, two private packets, paired
event lifetime and final cleanup keys. A documented volatile pointer home is
a matching annotation, not proof of the original source declaration.
No guards, compiler-profile, Makefile or shared-header changes. Six pre-install
tests pass in 110.238 seconds; the native32 test passes separately in 0.917
seconds. Qualification covers 51,200 guest / 1,024 null-actor / 30,720 native32
cases, nine required faults, 13 controls / 3,328 ordinary executions and four
effective negatives, complete table targets, copied owner/padder and rebases.
Only target changes across 6,058 symbols; all other bytes/addresses/extents/
overflows/protected sections/720 Game-data owners/11,063 guards/conversion hash
remain intact. Exact total 3,369/5,467 (61.62%), Game 2,696/4,794 (56.24%),
2,098 different, zero drift; conversion totals unchanged. Root README matching
aggregates only. Checkpoint: `game-node-cleanup-test/after.json`.
All 66 installed cleanup/action/attachment/lookup/resolver regression tests
pass in 439.488 seconds, zero skips/errors/failures; tools/syntax/CLI/whitespace
and 94-document / 4,076-relative-link checks pass, zero broken links.
Next local placeholder: `func_15031E7C`; intervening `func_15031E2C` is already
exact. Full callbacks/hardware/PC-port acceptance and matrix boundaries stay open.

Previous direct Game placeholder recovery:
[Note 1111](WORKING_NOTES/1111-game-node-action-dispatcher-direct-match-20261008.md).
`func_15031A50` now emits complete exact C113/frame `0x28`, both original
switch tables, action/callback ABIs, flag/counter mutations and signed random
threshold. Recover `void` signature; the original caller overwrites V0 and the
selected guest body preserves all incidental retail V0 values. No instruction
guards/profile/shared-header changes; one Makefile table-anchor mapping retains
physical Game-data ownership. Seven pre-install tests pass in 68.216 seconds:
61,440 guest / 30,720 native32 cases, all words/selectors/table targets, lazy/
fault paths, 15 controls, owner/padder and independent symbolic rebases.
Only target changes across 6,058 symbols; all other bodies/addresses/extents/
overflows/sections/720 data owners/11,063 guards/conversion hash unchanged.
Exact total 3,368/5,467 (61.61%), Game 2,695/4,794 (56.22%), 2,099 different,
zero drift; conversion counts unchanged, README aggregate matching rows only.
Authoritative ignored checkpoint: `game-node-action-test/after.json`.
All 59 installed action/attachment/lookup/resolver regression tests pass in
436.351 seconds, zero skips/errors/failures; tools/syntax/CLI/whitespace and
93-document / 4,062-relative-link checks pass, zero broken links.
Next local function: `func_15031C14`; full callbacks/hardware/PC-port acceptance,
resolver C84/40 and matrix boundaries remain open.

Previous direct Game placeholder recovery:
[Note 1110](WORKING_NOTES/1110-game-attachment-progress-copy-direct-match-20261008.md).
`func_150331B8` now emits complete exact C49/frame `0x30`, setup index gate,
cached actor source, post-call incoming node home, copy-induced pointer reload
and binary32 inclusive end clamp. No guards/profile/Makefile/shared-header edits.
Ten pre-install tests pass in 45.008 seconds: 60,000 guest / 75,000 native32
cases, 97 aliases, 13 required faults, 11 controls, owner/padder/rebase gates.
Five compiled negatives and prior progress-owner fixture recheck pass before
installation. Only target changes across 6,058 symbols, preserving all other
bodies/addresses/extents/overflows/sections/720 data owners/11,063 guards and
conversion hash. Exact total 3,367/5,467 (61.59%), Game 2,694/4,794 (56.20%),
2,100 different, zero drift; conversion totals unchanged. README date and
aggregate matching rows only. Setup remains a validating callback, not full
setup-callee/hardware/PC-port acceptance.
Authoritative ignored checkpoint: `game-attachment-copy-test/after.json`.
All 52 installed copy/progress/lookup/key-fit/resolver regression tests pass in
452.150 seconds, zero skips/errors/failures; tools/syntax/CLI/whitespace and
92-document / 4,052-relative-link checks pass, zero broken links.
Next local function: `func_15031A50`; resolver C84/40 and matrix boundaries remain open.

Previous direct Game placeholder recovery:
[Note 1109](WORKING_NOTES/1109-game-attachment-progress-direct-match-20261007.md).
`func_1503327C` now emits complete exact C43/frame `0x28`, attachment setup
gate, post-call node-home/pointer reload and binary32 end-minus-one predicate.
No guards, profile/Makefile or shared-header changes. Ten pre-install tests
pass in 57.072 seconds: 45,000 guest cases, 45,000 native32 cases, aliases,
faults, 19 controls and owner/padder/independent call-rebase checks.
Only target changes across 6,058 linked symbols; other bodies/addresses/extents/
overflows/sections/720 data owners/11,063 guards/conversion hash stay intact.
Exact total 3,366/5,467 (61.57%), Game 2,693/4,794 (56.17%), 2,101 different,
zero drift. Conversion counts unchanged; README matching rows only.
Setup is a validating callback, not full setup/hardware/PC-port acceptance.
Authoritative ignored checkpoint: `game-attachment-progress-test/after.json`.
All 42 installed attachment/lookup/resolver regression tests pass in 265.112
seconds, zero skips/errors/failures; tools/syntax/CLI/staged whitespace and
91-document / 4,043-relative-link checks pass, zero broken links.

Latest direct Game assembly-to-C match:
[Note 1108](WORKING_NOTES/1108-game-matrix-parent-lookup-direct-match-20261007.md).
`func_1503195C`, the recursive resolver's group/key/ordinal list lookup,
now emits all 28 retail words directly from C: no frame, guards, profile or
header changes. All 6,058 linked symbols retain identical bytes/addresses/
extents; all protected sections/720 data owners/11,063 guards remain intact.
The conversion CSV adds exactly one function / 112 bytes. Total converted
5,467/6,042 (90.48%), Game 4,794/5,321 (90.10%); byte-exact total
3,365/5,467 (61.55%), Game 2,692/4,794 (56.15%), 2,102 different, zero drift.
Ten pre-install tests pass in 66.371 seconds: 7,168 guest cases, 12,779,520
native32 cases, 58 source/profile controls and actual recursive connections.
All 32 installed lookup/resolver regression tests pass in 206.762 seconds,
zero skips/errors/failures; tools/syntax/CLI/whitespace and 90-document / 4,034-relative-link
checks pass, zero broken links.
Root README aggregate rows updated; detailed progress stays in these docs.
Resolver C84/40 and wrapper/basis/translator/sampler boundaries remain open.
Authoritative ignored checkpoint: `game-matrix-parent-lookup-test/after.json`.

Latest matrix-pair bank-phase/key-lifetime fit, **still not byte-exact**:
[Note 1107](WORKING_NOTES/1107-game-matrix-pair-bank-phase-and-key-lifetime-fit-20261007.md).
A one-expression slot-first pointer addition recovers the retail actor/slot/
bank/shift GP sequence directly. Only four target words change; each now equals
retail. Installed complete C84/frame `0x20` improves from 44 to 40 full-slot
differences, no new guards, instructions, production types or profile changes.
86 new controls / 2,752 ordinary executions, 155 total forms, none raw exact.
All eleven pre-install guest/alias/home/lazy/native/owner/padder/actual-wrapper
tests pass in 81.271 seconds. The linked audit preserves all other slots,
overflows/sections/data/11,063 guards/relocations/conversion hash and README
aggregates. The key still loads directly into A1; recover the original V0 move
in a genuine 85-word body before scheduling guards.
All 51 combined tests pass in 577.143 seconds, zero skips/errors/failures;
tools/syntax/CLI/whitespace and 89-document / 4,025-relative-link checks pass,
zero broken links. Six isolated word/void argument probes also stay C84/40,
without an additional ordinary-contract claim.
Authoritative ignored checkpoint: `game-matrix-pair-key-test/after.json`.

Previous installed matrix-pair resolver recovery, **not byte-exact**:
[Note 1106](WORKING_NOTES/1106-game-matrix-pair-resolver-semantic-recovery-20261007.md).
`func_15031070` now replaces its zero-return placeholder with complete recursive
C84/frame `0x20`, four matrix routes, store-induced rereads and original actor/
secondary incoming-home lifetime. The 85-word retail slot contains one trailing
padding nop; 44 raw differences remain versus 85 in the placeholder, no new
guards. Guest/alias/home/lazy/native/owner and complete actual-wrapper checks
qualify; 69 source/profile forms / 1,104 ordinary executions, none exact.
The completed linked audit changes only target; all other slot bodies, addresses,
extents, overflows, protected sections, 720 data owners, 11,063 guards and
conversion hash stay intact. Matching totals and root README aggregates remain
unchanged. Resume key V0/argument-move source fitting before GP/schedule guards.
All 40 combined tests pass in 495.848 seconds, zero skips/errors/failures;
three receipt rechecks pass in 11.533 seconds. Tools/syntax/CLI/whitespace
and 88-document / 4,016-relative-link checks pass, zero broken links.
That checkpoint: `game-matrix-pair-resolver-test/after.json`.

Latest matrix-route register-phase/source follow-up, **no new byte match**:
[Note 1105](WORKING_NOTES/1105-game-matrix-route-register-phases-and-branch-source-audit-20261007.md).
Experimental C119/frame `0xA0` now emits the original seventeen opening words,
matrix in A1, node/input S1, actor/output S2 and all sixteen shifted loop words
directly as retail, with unchanged actual private addresses. Key branch and
primary-read topology still differ; 74 full-slot differences remain, and the
body is one word short of retail. Do not install it or insert a word. Retain 92
new controls / 2,208 ordinary executions, 377 total forms, none raw exact.
Private/home/actual-helper/native/owner gates pass; all nine new tests pass in
114.007 seconds. The installed C120/60-difference body, all linked symbols,
11,063 guards, data/conversion hash and README totals remain unchanged.
All 29 combined tests pass in 419.377 seconds, zero skips/errors/failures;
tools/syntax/whitespace and 87-document / 4,005-relative-link checks pass,
zero broken links.
Continue the key/primary source fit with this qualified register-phase evidence.

Latest installed matrix-route semantic recovery, **not byte-exact**:
[Note 1104](WORKING_NOTES/1104-game-matrix-route-private-layout-and-semantic-recovery-20261007.md).
`func_1514654C` replaces its padded zero-return placeholder with complete
C120/frame `0xA0`, matrix `sp+4C`, resolver outputs `sp+90/+8C`, all four
routes and incoming-home timing. No new guards; 60 instruction differences
remain versus 115 in the old placeholder. All sixteen previous private-matrix
counterexamples now agree, plus 560 additional original-helper overlaps;
ordinary/public/private-argument/home/native/owner/padder/rebasing gates pass.
77 additional controls bring the source audit to 285 forms, none raw exact.
All twenty combined tests pass in 313.807 seconds, zero skips/errors/failures.
Tools/syntax/whitespace and 86-document / 3,996-relative-link checks pass,
zero broken links; three receipt-only rechecks pass in 4.211 seconds.
The linked audit changes only target; other bodies/addresses/extents/overflows/
protected sections/720 data owners/11,063 guards/conversion hash remain intact.
Exact total 3,364, Game 2,691 (56.14%), 2,102 different, zero drift; README
aggregates unchanged. Continue key-branch, primary-read and saved-register
lifetime fitting, not bulk instruction normalization. Note 1106 now separately
recovers the production resolver; no PC-port or full stack-memory acceptance.
That checkpoint: `game-matrix-route-layout-test/after.json`.

Previous matrix-route recovery/private-frame audit, **no installed match at that checkpoint**:
[Note 1103](WORKING_NOTES/1103-game-matrix-route-recovery-and-private-frame-audit-20261007.md).
`func_1514654C`'s complete experimental six-word-ABI wrapper emits C119/frame
`0xA8`/58 differences; retail is 120 words/frame `0xA0`. Ordinary routes,
home reloads, connected original helpers, native SDK and copied-owner gates
qualify, but actual private-matrix overlaps change public outputs. Do not
normalize private offsets or install that candidate. At that checkpoint the
production slot remained the padded three-word zero-return placeholder;
original assembly was the reference only. Retain 208 source/profile controls, none exact. Full
linked snapshot/11,063 guards/data/conversion hash and README aggregates
remain unchanged. All eight tests pass in 497.879 seconds, zero skips/errors/
failures, with 4,992 ordinary candidate executions and six effective negatives.
Tools/syntax/whitespace and 85-document / 3,985-relative-link checks pass,
zero broken links. Note 1104 supersedes this private-frame/installed-source handoff.

Previous installed lighting Game match:
[Note 1102](WORKING_NOTES/1102-game-lighting-dispatcher-match-20261007.md).
`func_151462C8` replaces its zero-return placeholder with complete C124/frame
`0x48`, lazy resource gates, actor/global/position lighting dispatch and the
nine-word incoming ABI. Two guards swap only an independent signed-index load
and temporary initialization; all 124 linked words match, all 13 relocations
retained. Full linked audit changes only target across 6,058 symbols/6,042
slots; other bodies/addresses/extents/overflows/protected sections/720 data
owners and 11,061 prior guards intact, new count 11,063. Exact total
3,364/5,466 (61.54%), Game 2,691/4,793 (56.14%), 2,102 different, zero drift;
conversions unchanged. Guest/native/candidate/owner/padder/rebasing qualification
uses bounded renderer hooks, not connected renderer or PC-port acceptance.
All nine lighting/prior-neighbor tests pass in 324.913 seconds, zero skips/
errors/failures. Tools/syntax/whitespace and 84-document / 3,976-relative-link
checks pass, zero broken links.
That checkpoint's next target was 120-word `func_1514654C`, now complete
nonmatching C in Note 1104. Basis,
translator and sampler boundaries remain open; no sibling/Release/save/push.

Latest basis source-control follow-up:
[Note 1101](WORKING_NOTES/1101-game-vector-basis-coordinate-and-workspace-controls-20261007.md).
68 additional coordinate/workspace/seed forms bring the audit to 186 controls,
none raw exact, and 2,136 ordinary candidate executions. All 19 combined
basis/normalizer tests pass in 151.122 seconds, zero skips/errors/failures.
The selected C144/frame `0x48`/93-difference boundary and installed original
assembly remain unchanged. Continue the layout/lifetime recovery below;
adjacent lighting-dispatch matching is a separate batch.

Latest vector-basis recovery/liveness audit, **no new conversion or byte match**:
[Note 1100](WORKING_NOTES/1100-game-vector-basis-recovery-and-liveness-audit-20261007.md).
`func_15146078` remains original 148-word assembly. Its complete experimental
C is 144 words/frame `0x48`/93 differences, with unrecovered scalar offsets
and special-case floating-zero lifetime. The early byte reads are real but
their initial values are publicly dead; 16,384 fixtures and 28 required faults
qualify that boundary. Ordinary/alias/actual-helper/native/complete-caller
tests qualify, but two private-output overlaps still differ. Retain 118
source/profile controls, none exact; do not install private-offset patches.
All 6,058 linked symbols, 11,061 guards, protected sections/data and conversion
hash remain identical to the banked baseline; README aggregates unchanged.
All 19 combined recovery/normalizer tests pass in 114.064 seconds, zero skips/
errors/failures; tools/syntax/whitespace and 82-document / 3,958-relative-link
checks pass, zero broken links.
Continue the source lifetime/layout recovery in Note 1100.

Latest matrix/list wrapper match:
[Note 1099](WORKING_NOTES/1099-game-matrix-list-transform-match-20261007.md).
`func_15145EA4` replaces its zero-return placeholder with both original matrix
routes, lazy null/zero-point gates, cached X, list strides and incoming-home
reloads. Complete C117/frame `0xA0`/matrix `sp+0x5C`, unchanged O2/g3/MIPS2,
19 raw differences versus 106 in the old padded slot. Nineteen expected-word
guards close one GP cycle, independent save order and two equality operand
orders; all 117 linked words match, no private-offset/relocation/instruction
edits. 10,752 guest / 1,152 connected / 72 complete original-caller / 1,344
home-readback / 1,572,872 native cases qualify, plus 131,104 equality comparisons,
1,200 private overlaps, fail-closed/lazy-list gates and eight effective
public-storage negatives. All 182 controls remain raw nonmatching;
2,184 ordinary candidate executions pass. Eight core pre-install tests pass
in 315.497 seconds, with strengthened caller/SDK checks also passing.
US ELF changes only target across 6,042 slots / 6,058 symbols; all other
bodies/addresses/extents/16 overflows/protected sections/720 data owners and
11,042 previous guards intact, new count 11,061. Exact total 3,363/5,466
(61.53%), Game 2,690/4,793 (56.12%), 2,103 different, zero drift; conversion
unchanged. All 63 combined tests pass in 759.125 seconds, zero skips/errors/
failures; tools/syntax/whitespace and 81-document / 3,947-relative-link checks
pass, zero broken links. Next 148-word
`func_15146078`, retained original assembly; audit private axis-byte liveness.
Translator/sampler remain open. No sibling/frozen Release/save/runtime/push.

Previous point-batch lifetime match:
[Note 1098](WORKING_NOTES/1098-game-point-batch-transform-lifetime-match-20261007.md).
`func_15145DB4` recovers the original descriptor/source phase, three twelve-
byte-stride coordinate cursors and source reload only for positive counts.
Complete C60/frame `0x98`/matrix `sp+0x58` under unchanged O2/g3/MIPS2;
17 raw differences, down from 60 across the old padded slot. Seventeen
expected-word guards close saved/halfword-register cycles and a three-store
prologue permutation; all 60 normalized words match, with no private-offset,
FP-register, relocation, insertion, omission or ABI changes. Meaningful signed
translation temporaries recover the frame; a plain-C label preserves the gate.
1,792 guest, 768 connected original-helper, 5,376 incoming-home and 524,296
native cases qualify, plus 384 private-overlap cases (368 completed, 16 matched
faults), seven public-storage negatives and a lazy-home negative. All 119
controls remain raw nonmatching; 2,856 bounded candidate executions qualify.
Eight pre-install tests pass in 128.524 seconds. US ELF audit changes only target
across 6,042 retail slots / 6,058 symbols; other bodies/addresses/extents/16
overflows/protected sections/720 data owners and previous 11,025 guards stay
intact, new guard count 11,042. Exact total 3,362/5,466 (61.51%), Game
2,689/4,793 (56.10%), 2,104 different, zero drift; conversions unchanged.
All 43 combined tests pass in 460.335 seconds, zero skips/errors/failures;
tools/syntax/whitespace and 80-document / 3,936-relative-link checks pass,
zero broken links. Next: 117-word matrix/list wrapper
`func_15145EA4`, still a zero-return placeholder. Translator scheduling and
sampler remain open. No sibling/Release/save/runtime/hardware/push action.

Previous point-list lifetime match:
[Note 1097](WORKING_NOTES/1097-game-point-list-transform-lifetime-match-20261007.md).
`func_15145CD0` reuses the descriptor cursor for the input list after its final
descriptor read. Complete C57/frame `0x88` under unchanged O2/g3/MIPS2;
19 raw differences, down from 46. Nineteen expected-word guards close one
saved-register cycle and two independent prologue permutations; all 57 linked
words match retail. No private offsets, incoming homes, call relocations,
instructions, ABI types or pools are changed by normalization.
1,344 guest, 576 connected original-point-helper, 2,304 independent/both-home
readback and 131,076 native cases qualify, plus seven effective negatives,
fail-closed storage and copied-owner/actual-padder/two-call relocation gates.
Forty new meaningful measurements are retained; none is raw byte-exact.
US ELF audit changes only target across 6,042 retail slots / 6,058 symbols;
all other bodies/addresses/extents/16 overflows/protected sections/720 data
owners and previous 11,006 guards stay intact. Nineteen new guards bring the
count to 11,025. Exact total 3,361/5,466 (61.49%), Game 2,688/4,793 (56.08%),
2,105 different, zero drift; conversions unchanged. All 34 combined tests
pass in 319.291 seconds, zero skips/errors/failures; tools/syntax/whitespace
and 79-document / 3,924-relative-link checks pass, zero broken links.
Next: contiguous point-batch transform `func_15145DB4`; translator scheduling
and sampler remain open. No sibling/Release/save/runtime/push acceptance.

Previous matrix scheduling / point-list lifetime audit, **no new byte match**:
[Note 1096](WORKING_NOTES/1096-game-matrix-scheduling-and-point-list-lifetime-audit-20261007.md).
26 additional typed-view/backend controls do not resolve `func_15142314`;
its installed C49/frame0/34 differences is unchanged. Begin `func_15145CD0`:
semantic C57/frame `0x88`/46 differences; 48 nonmatching loop/lifetime/readback
measurements retained. 1,344 public-effect guest, 580 original-point-helper
connected and 131,076 native cases plus five effective negatives qualify the
ordinary routes; two incoming-argument-home probes confirm the remaining
retail readback difference. All 6,058 symbols/6,042 slots/16 overflows/data/
11,006 guards and production sources/profiles/headers/README aggregates remain
unchanged; total 3,360 exact, Game 2,687, 2,106 different, zero drift.
25 combined tests pass in 376.363 seconds; strengthened two-test gate and
final nine-test audit pass, plus tools/syntax/whitespace and 78-document /
3,910-relative-link checks, zero broken. Continue pointer-list readback lifetime;
translator scheduling and sampler remain open. No sibling/Release/runtime/push.

Latest qualified matrix translation recovery, **not byte-exact**:
[Note 1095](WORKING_NOTES/1095-game-matrix-translation-qualified-recovery-20261007.md).
`func_15142314` now restores separate float conversions before addition,
safe signed-high multiplication, unsigned32 address wrap and sequential
outputs. Complete C49/frame0/no pool, unchanged O2/g3/MIPS2, no guards.
34 word differences remain, down from 46; 152 controls, none exact. 65,536
halfword guest tuples, 20,576 aliases/edges, 66,816 native and 1,152 complete
parent null/zero-route cases qualify, plus seven negatives and owner/padder/
flag-relocation gates. Only target changes across 6,042 slots / 6,058 symbols;
other bodies/addresses/extents/overflows/data/11,006 guards unchanged. Converted/
matching totals unchanged: total 3,360, Game 2,687, 2,106 different, zero drift.
38 tests pass in 322.863 seconds, zero skips/errors/failures; strengthened
public-storage/wrong-sign negative gate also passes. Tools/syntax/whitespace
and 77-document / 3,897-relative-link gates pass, zero broken links.
README aggregates already current and unchanged. Continue this translator's
constant/ordinary-branch/return-delay schedule; do not treat recovery as a match.
Sampler exits/RNG remain untouched. No sibling/Release/save/runtime/push claim.

Latest cached primitive-color direct match:
[Note 1094](WORKING_NOTES/1094-game-cached-primitive-color-direct-match-20261007.md).
`func_15142CF0` emits all 77 words/frame `0x8` directly under unchanged O2/g3,
no guards. Six-field positive miss gate plus the actual SDK macro recovers all
words; 48 controls/one exact form. 174,720 complete-effect guest, 448 incoming-
home overwrite and 7,280 native cases, seven negatives and copied-owner/actual-
padder/six independently rebased cache symbols qualify. US ELF/audit changes
only target across 6,042 retail slots / 6,058 symbols; all addresses/extents/
overflows/protected sections/data/11,006 guards intact. Exact total 3,360/5,466
(61.47%), Game 2,687/4,793 (56.06%), 2,106 different, zero drift; conversion
unchanged. Combined regression: 23 tests in 269.557 seconds, zero skips/errors/
failures; tools/syntax/whitespace and 76-document / 3,886-relative-link gates
pass, zero broken links. Main README aggregate rows only. Next 49-word
translation extractor
`func_15142314`: recover separate float conversions before addition and original
addressing. Sampler exits/RNG remain open and untouched, no new sampler sweep.
No host/sibling/Release/save/runtime/rendering/hardware/push claim.

Latest cached environment-color direct match and sampler flow audit:
[Note 1093](WORKING_NOTES/1093-game-cached-environment-color-match-and-sampler-flow-audit-20261007.md).
`func_15142C10` emits all 56 words/frame `0x8` directly under unchanged O2/g3,
no guards. Positive cache-miss gate plus the actual SDK macro recovers the
original lazy reads, packet allocation and cache-store schedule. Forty-eight
measurements, one exact form; 62,400 full-effect guest and 5,200 native cases,
six negatives and copied-owner/actual-padder/independent cache-rebasing gates
qualify. Only target changes across 6,042 retail slots / 6,058 linked symbols;
all addresses/extents/overflows/data/protected sections/11,006 guards unchanged.
Exact total 3,359/5,466 (61.45%), Game 2,686/4,793 (56.04%), 2,107 different,
zero drift; conversions unchanged. Main README aggregate rows only.
Combined regression: 50 tests in 336.828 seconds; tools/syntax/whitespace pass,
75 documents / 3,874 relative links, zero broken.
Sampler: 54 new flow/register measurements, none exact, all one RA reload
versus retail three. 82,944 public-reference candidate runs and 2,592 conversion
runs qualify; no sampler installation. Next 77-word primitive-color neighbor
`func_15142CF0`, then remaining sampler exit/RNG schedule. No hardware/rendering/
host/sibling/Release/save/runtime/push claim.

Latest oriented-matrix direct match:
[Note 1092](WORKING_NOTES/1092-game-oriented-matrix-direct-match-20261007.md).
`func_15142600` emits all 142 words/frame `0xB8` directly under unchanged O2/g3,
no guards. Matrix-first storage plus meaningful split horizontal scalars recover
every original private offset. Forty-eight maintained controls, four exact
forms; 176 measurements including historical controls. Install the typed
`func_150B9D14` caller without changing any of its owner's eight raw functions.
2,448 guest/full-effect, 144 original caller/converter, 288 private-overlap and
1,224 native cases qualify; the old layout changes output in 156 overlap cases.
Copied builder retains 88 neighbors/pools/relocations/two warnings; actual
padder emits the direct slot and preserves the rebased converter call.
US ELF rebuilt: only target changes across 6,042 retail slots / 6,058 linked
symbols; all addresses/extents/overflows/protected sections/data/11,006 guards
unchanged. Exact total 3,358/5,466 (61.43%), Game 2,685/4,793 (56.02%),
2,108 different, zero drift; conversions unchanged. README aggregate rows only.
Oriented layout is complete; next sampler's legitimate exit/RNG schedule or
another ordinary Game function. All 64 focused tests pass in 353.549 seconds,
zero skips/errors/failures; tools/syntax/whitespace and 74-document/3,857-link
gates pass, zero broken links. No FCSR/hardware/gameplay/host/sibling/Release/
save/runtime/push claim.

Latest actor-lookup direct match:
[Note 1091](WORKING_NOTES/1091-game-actor-lookup-byte-abi-direct-match-20261007.md).
`func_15142444` emits all 44 words/frame `0x18` directly under O2/g3, no guards.
Nested final checks plus the original byte helper ABI recover its full exits;
correct only this owner's helper declaration, not the shared header.
62 source/ABI measurements, 17 exact forms; copied owner retains 88 neighbors,
pools/relocations and two warnings. 24,552 reference-backed guest cases, eight
callback cases, 1,664 complete original-helper cases and 12,276 native cases
qualify. Helper coverage is 68/72, with four unreachable return-tail loads.
US ELF rebuilt: all 6,042 retail addresses/extents fixed, 6,040 other slots
unchanged. Target overflow removed; following overflow moves -184 bytes with
identical body and one collateral trampoline word rebased. 6,058 linked symbols
now include 16 compiler overflows; do not count overflows as retail slots.
Protected sections/720 data owners/11,006 guards and conversion counts unchanged.
Exact total 3,357/5,466 (61.42%), Game 2,684/4,793 (56.00%), 2,109 different,
zero drift. README aggregate rows only. New sampler lifetime screen: 16 controls
all identical C252/frame `0x50`/109 differences; sampler remains uninstalled.
All 44 focused tests pass in 156.500 seconds, zero skips/errors/failures;
tool/syntax/whitespace and 73-document/3,843-link gates pass, zero broken links.
Next sampler exit/RNG schedule or oriented matrix `func_15142600` (Note 1070).
No full-ROM/hardware/gameplay/host/helper-C/sibling/Release/save/runtime/push claim.

Latest scaled-sphere direct caller match:
[Note 1090](WORKING_NOTES/1090-game-scaled-sphere-query-direct-match-20261007.md).
`func_15145AD8` now emits all 110 words directly from semantic C under the
unchanged O2/g3 profile. Nested scale/reciprocal lifetimes recover the original
frame/private offsets, lazy branches and exact helper-call delay stores,
including both scale reads before the aliased inverse spill. No target guards.
Fifty-one new controls, 191 measurements total, three independently exact forms.
Copied owner retains 88 neighbors/pools/relocations/two warnings; actual padder
emits the complete direct slot, and each helper relocation independently rebases.
US ELF rebuilt: only this slot changes; all 6,058 others, every address/extent,
720 data owners and 11,006 guards remain unchanged. Exact total 3,356/5,466
(61.40%), Game 2,683/4,793 (55.98%), 2,110 different, zero drift; conversion,
Init/Debugger unchanged. README aggregate rows updated, no recovery narrative.
All 112 tests pass in 688.694 seconds, including 37,808 fitting-caller guest
fixtures/full memory/events/register comparisons and 126,720 native finite calls.
Tool/syntax/whitespace and 72-document/3,826-link gates pass; no broken links.
Next after banking this recovery: still-open sampler `func_151432BC`.
No ROM-checksum/hardware/gameplay/host/sibling/Release/save/runtime/push claim.

Historical capture-lifetime recovery, superseded by Note 1090:
[Note 1089](WORKING_NOTES/1089-game-scaled-sphere-query-capture-lifetime-20261007.md).
Broader actor-in-caller-frame evidence finds that the old `func_15145AD8`
candidate spills inverse before reading aliased actor `0xDC`, changing scale
2.0 to 0.5 and both output Y words. Prefer the new `SCALE_FIRST` experimental
body; it retains frame/private offsets and corrects the observed lifetime,
but remains 111 words/72 differences versus retail 110. 10,368 private-actor
cases extend the requalified guest bank to 37,808; 126,720 native finite calls
run the improved body. Thirty-nine new code-generation controls, 140 measured
controls total, none exact. Scoped source changes the second branch to plain
`bc1f` but leaves a comparison NOP and still 111 words. Copied owner retains
88 neighbors/pools/relocations/two warnings; real padder still uses overflow.
Final regression: 93 tests / 529.685 seconds, then three source-binding/read/
lazy-gate checks / 4.276 seconds. Fresh audit retains all 6,059 slots, 720 data
owners and 11,006 guards; tool/syntax/whitespace/documentation gates pass.
Counts/main README unchanged. Next fitting source, full frame/read-timing and
actual fitting-body installation gates; the older candidate stays a negative.
No full-float/FCSR/NaN/MMIO/hardware/gameplay/host or sibling/push claim.

Historical caller boundary audit, extended by Note 1089:
[Note 1088](WORKING_NOTES/1088-game-scaled-sphere-query-boundary-audit-20261007.md).
`func_15145AD8` remains 111 words/frame `0x88`, original private slots and
72 differences versus retail 110. Thirty new controls, 101 maintained
measurements, none exact. 27,440 bulk guest fixtures now compare bounded
caller-local/incoming-home snapshots at the real normalizer/wrapper calls;
9,216 signed vertical-offset and 216 private-input cases are new. Native bank
expanded to 126,720 actual finite calls through all five C helpers. Copied
owner preserves 88 neighbors, relocation/pool ownership and its two warnings;
actual padder emits an overflow trampoline, not an in-slot match. Production
placeholder/counts/README aggregates unchanged. Next original-profile 110-word
fit, complete private-frame/read-timing and actual fitting-body install gates.
No full-frame/FCSR/NaN/hardware/gameplay/host or sibling/Release/save/runtime/push claim.
All 76 focused tests pass in 317.745 seconds, zero skips/errors/failures;
final retained audit, tools/syntax/whitespace and 70-document/3,800-link gate pass.

Historical complete caller recovery, extended by Note 1088:
[Note 1087](WORKING_NOTES/1087-game-scaled-sphere-query-recovery-20261007.md).
`func_15145AD8` now has its complete eight-position ABI, reversed non-null
redirections and original private slots/frame `0x88`, but emits 111 words
versus retail 110, 72 differences. Seventy-one compiler controls, none exact.
18,008 bulk guest cases plus natural late-pointer-home/fail-closed probes and
25,344 native finite calls connect all five real helpers. Caller coverage
109/110; unreachable duplicate load explicitly excluded. Ten tests pass in
45.498 seconds, zero skips/errors/failures. Retain production placeholder;
all 6,059 slots/720 data owners/11,006 guards/counts and README aggregates
unchanged. Next 110-word O2/g3 fit, broader private/helper-frame/read-timing
qualification and owner/install gates. No installed-caller, full-float/FCSR/
NaN/hardware/gameplay/host or sibling/frozen Release/save/runtime/push claim.
All 72 focused tests pass in 273.813 seconds, zero skips/errors/failures;
final retained audit, tools/syntax/whitespace and 69-document/3,789-link gate pass.

Last installed callee allocation match:
[Note 1086](WORKING_NOTES/1086-game-sphere-callee-allocation-match-20261007.md).
`func_151452C4` is now semantic C, all 126 linked words/frame `0x70` exact.
Meaningful local order plus the direction union recover original private slots;
raw C and retail both produce 24.0 in the former private-alias counterexample.
73 raw aligned words plus 53 checked FP/closed-schedule guards; no private/frame/
branch/insert/omit changes. 3,724 full-memory/operand-trace guest cases and
6,318 native finite external-alias calls qualify. Copied owner/pools/warnings/
relocations and actual padder/alternate-target/stale gates pass. US ELF/fresh
audit preserves all 6,059 slots/protected sections/720 owners and 10,953 prior
guards, 11,006 total. Converted +1/504 bytes: 5,466/6,042 (90.47%, bytes 85.61%),
Game 4,793/5,321 (90.08%, bytes 84.94%). Exact 3,355/5,466 (61.38%), Game
2,682/4,793 (55.96%), 2,111 different, zero drift. README aggregate rows only.
Next active 110-word/frame `0x88` placeholder `func_15145AD8`; recover full
ABI/dependency/private-output lifetimes before fitting and installation.
No complete-caller/FCSR/NaN/hardware/gameplay/host adoption or sibling/frozen
Release/save/runtime/push claim. Sampler/oriented work remains open.
All 57 focused tests pass in 187.474 seconds, zero skips/errors/failures;
final linked audit, tools/syntax/whitespace and 68-document/3,776-link gate pass.

Historical callee frame audit, superseded by Note 1086:
[Note 1085](WORKING_NOTES/1085-game-sphere-callee-frame-alias-audit-20261007.md).
1,404 direct-helper external-alias and 1,296 private-output/home cases now
check complete memory and ordered writes against layout-specific references.
Early point pointers and late distance-pointer homes are confirmed. Retail
second-X 24.0 versus trial 10.0 remains an installation blocker. Forty-eight
new meaningful layout controls recover no exact form. Six new tests pass in
6.698 seconds. No production change or new matching increment. Next inspect
IDO allocation/lifetimes and recover original private slots before installation.
All 46 focused tests pass in 212.519 seconds, zero skips/errors/failures.
Final retained audit, tools/syntax/whitespace and 67-document/3,762-link gate pass.

Historical callee recovery, not installed:
[Note 1084](WORKING_NOTES/1084-game-sphere-callee-storage-recovery-20261007.md).
`func_151452C4` now fits 126 words/frame `0x70`, with 60 differences. Sixty-four
compiler controls retain no exact form. Its direction/origin/relative private
slots remain wrong: a frame `+0x58` output alias produces retail second-X 24.0
versus trial 10.0. Retain the exact assembly and existing direct wrapper;
private offsets must not be word-patched. 2,808 bounded finite external-alias
cases pass; seven new tests pass in 14.016 seconds. All 6,059 retained slots,
protected sections, 720 data owners, 10,953 guards and counts stay unchanged.
Next recover original private storage/lifetimes and qualify private/home aliases.
README aggregate rows are already current; no new native geometry acceptance.
All 40 focused recovery/wrapper/projection/owner-pool tests pass in 160.675
seconds, zero skips/errors/failures. Tools/syntax/whitespace/final retained
audit pass; 66 documents/3,749 relative links/zero broken.

Sphere-wrapper direct match:
[Note 1083](WORKING_NOTES/1083-game-sphere-wrapper-direct-match-20261007.md).
`func_151451F0`: all 53 words emit directly from C, original `0x28` frame,
nine-position ABI/eight forwarded arguments and live threshold/output homes.
The original 126-word callee and 13-word dot helper remain byte-exact assembly/C;
no new guards or profile/header/padder changes. Connected geometry, native
staging, both caller fragments, natural home writes and effective negatives pass.
Only target changes across 6,059 slots; all addresses/extents/protected sections,
720 data owners and 10,953 guards unchanged. Exact 3,354/5,465, Game 2,681/4,792,
2,111 different, zero drift; conversion unchanged. README aggregate rows only.
All 13 pre-install tests pass in 40.702 seconds; all 49 focused post-link tests
pass in 193.212 seconds, zero skips/errors/failures. Final linked audit, tools,
syntax, whitespace and 65-document/3,738-relative-link gate pass.
Next: fit the uninstalled 128-word/frame `0x68` callee C trial into
retail's 126 words/frame `0x70`, preserving private layout and live final reads.
No full-caller/hardware/FCSR/NaN arithmetic/gameplay/host-adoption or sibling/
frozen Release/save/runtime/push claim. Sampler/oriented work remains open.

Projection-wrapper match:
[Note 1082](WORKING_NOTES/1082-game-projection-wrapper-match-20261007.md).
`func_15144CEC`:101 words/frame0x48, original six-position ABI/private fallbacks,
real58-word matrix/W helper chain and live index/reciprocal/view behavior.
64 direct words plus37 checked temporary/commutative/four-word-schedule guards;
no insertion/omission/branch/frame/profile/header/helper change. Raw C, retail
and guarded code qualify separately, including natural W/index-home overlap,
1728 operand-input traces,1536 original caller setups and4096 varied finite cases.
US ELF/audit changes only target across6059 slots; all addresses/extents/protected
sections/720 owners/10916 prior guards unchanged,10953 total.
Exact3353/5465 (61.35%), Game2680/4792 (55.93%),2112 different, zero drift;
conversion unchanged. README aggregate rows only. All 206 regression tests pass
in 1005.830 seconds, zero skips/errors/failures; final post-regression linked
audit, project tools, syntax and whitespace pass. Documentation gate:
64 documents/3727 relative links/zero broken.
Next53-word `func_151451F0`, nine arguments/eight-position forwarding and live
sign/threshold acceptance; sampler/oriented work stays open. No complete-caller/
hardware/FCSR/NaN/gameplay/host adoption, sibling/Release/save/runtime or push claim.

Projection-wrapper lifetime recovery, not installed:
[Note 1081](WORKING_NOTES/1081-game-projection-wrapper-lifetime-recovery-20261007.md).
`func_15144CEC`: retail101 words/frame0x48; qualified experimental C102 words/
frame0x48,46 aligned differences. Original null-output private slots and the
real58-word synthetic-return matrix/W helper chain are recovered. Live index,
Y-product capture, reciprocal and view reloads pass guest/native qualification.
140 maintained compiler forms have zero diagnostics; none is byte-exact.
36864 paired guest/384 depth/512 index-home/92160 native cases, fail-closed
required fields and three effective compiled alias negatives qualify.
Inline-Y's closer44-word difference score is rejected: Y2.5 versus retail26.5.
Retained US ELF re-audit keeps every6059 slot/protected section/720 data owner/
10916 historical guard unchanged. Counts and README aggregate rows unchanged.
All26 focused recovery/audit/helper regression tests pass in211.955s, zero
skips/errors/failures;63 documents/3714 relative links/zero broken. Project
tools, Python syntax and whitespace checks pass; no new full164-test run claimed.
Next: recover101-word fit and remaining scheduling/register differences before
installation. No FCSR/NaN/hardware/full-caller/gameplay/host adoption claim;
no sibling/frozen Release/save/runtime or push work.

Secondary halfword output direct match:
[Note 1080](WORKING_NOTES/1080-game-secondary-halfword-output-direct-match-20261007.md).
`func_151442FC`:120 direct C words/frame0, fourteen ABI positions, fourteen
unsigned modes/default, live argument7 and shared2/3,7/12 cases. Separate4/5
product blocks, chained zero rereads, scale snapshots and live later-byte order
are recovered. Two checked table bindings; no instruction normalization.
Guest65536/stack-alias24576/live-input4096/native557056/two-leaf caller8192
cases, six effective negatives and owner/padder/stale/alternate-carry gates pass.
Pool retains644 meaningful bytes/old owner identities, adds56 table bytes/4
padding,704 total. Earlier-table copied baselines pin exact later addend shifts.
US ELF/audit changes only target across6059 slots; all addresses/extents/
protected sections/720 owners/10914 prior guards unchanged,10916 total.
Exact3352/5465 (61.34%), Game2679/4792 (55.91%),2113 different, zero drift;
conversion unchanged. All164 post-link tests pass in736.713s, zero skips/errors/
failures.62 documents/3701 relative links/zero broken; project tools, syntax,
whitespace and final post-regression linked audit pass.
README aggregate matching rows only. Next101-word `func_15144CEC`; sampler/
oriented recoveries stay open. No full-caller/hardware/gameplay/host adoption,
native guest-home-alias, sibling/Release/save/runtime or push claim.

Halfword output-mode direct match:
[Note 1079](WORKING_NOTES/1079-game-halfword-output-mode-direct-match-20261007.md).
`func_151441A4`:86 direct C words/frame0, fourteen-position ABI and unsigned
five-case/default switch. Halfword stores/rereads, live byte inputs, scale
snapshot and duplicated scaled cases recovered. Two checked relocations bind
the appended compact table to the original owner; no instruction normalization.
Guest65536/stack-overlap24576/unused-input3584/native557056/caller-fragment2048
cases, six negatives and owner/padder/stale/alternate-carry checks qualify.
All86 words covered. Prior624-byte normalized pool intact, new656-byte pool
contains the20-byte table plus12 alignment bytes. Neighboring pool tests now
check this extension explicitly, not a generic allowance for drift.
US ELF/audit changes only target across6059 slots; all addresses/extents/
protected sections/720 owners/10912 prior guards unchanged,10914 total.
Exact3351/5465 (61.32%), Game2678/4792 (55.88%),2114 different, zero drift.
Conversion unchanged; README aggregate rows only. All153 post-link regression
tests pass in578.698s, zero skips/errors/failures.61 documents/3690 relative
links/zero broken; tools/syntax/diff and final post-regression linked audit pass.
Next120-word `func_151442FC`.
No whole-caller/hardware/gameplay/host adoption, sibling/Release/save/runtime
or push claim. Sampler/oriented recoveries remain open.

Fixed-point cursor updater match:
[Note 1078](WORKING_NOTES/1078-game-cursor-updater-match-20261007.md).
`func_1514401C`:98 words/frame0; low-u8 inputs, live tick scaling, upper/lower
mode priorities and alias-sensitive wrap/reflection stores recovered.
52 direct words,46 checked register-field/commutative-add guards; instruction
order, branches, immediates, frame and four relocations remain unchanged.
Guest18944/extremes3500/traps1024/native20182/caller-fragment192 cases,
11776 paired instruction-input traces, six negatives and owner/pool/padder/
stale/alternate-HI16 checks qualify.95 reachable words, three dead trap guards.
US ELF/audit changes only target across6059 slots; addresses/extents/protected
sections/720 owners/all10866 prior guards unchanged,10912 total.
Exact3350/5465 (61.30%), Game2677/4792 (55.86%),2115 different, zero drift.
Conversion unchanged; README aggregate rows only. All142 post-link regression
tests pass in672.201s, zero skips/errors/failures.60 documents/3679 relative
links/zero broken; tools/syntax/diff and final post-regression linked audit pass.
Next86-word `func_151441A4`; sampler/oriented recoveries remain open.
Invalid native division and hardware overflow-HI behavior are not claimed.
No complete-caller/gameplay/host adoption, sibling/Release/save/runtime or push.

Actor-gated packet match:
[Note 1077](WORKING_NOTES/1077-game-actor-gated-packet-match-20261007.md).
`func_15143E94`:98 words/frame0x38, full-word command/flags and byte return.
Signed-byte snapshot count, health/checker gates, live context, two RNG calls
and partially initialized eight-byte packet recovered. Eleven checked guards
normalize only the closed opening schedule; branch target/dependencies and
private layout unchanged. Scope the checker ABI locally, shared headers untouched.
8192 paired guest/362 callback-RNG/18856 native/12 original caller-pair cases,
six negatives, poisoned padding and actual owner/pool/padder/stale gates qualify.
US ELF/audit passes; only target changes across6059 slots, all addresses/extents/
protected sections/720 owners/10855 prior guards unchanged,10866 total.
Exact3349/5465 (61.28%), Game2676/4792 (55.84%),2116 different, zero drift;
conversion unchanged. README aggregate matching rows only.
All131 post-link regression tests pass in692.507s; final10 packet tests rerun
after trace/frame-reporting improvements pass in61.780s. Zero skips/errors/
failures.59 documents/3668 relative links/zero broken; tools/syntax/diff and
final post-regression linked audit pass.
Next98-word cursor updater `func_1514401C`; sampler exits/oriented27 offsets
stay open. No sibling/Release/save/runtime, complete-caller/hardware/gameplay,
host adoption or push.

Record-query direct match:
[Note 1076](WORKING_NOTES/1076-game-record-query-direct-match-20261007.md).
`func_151438D8`:272 direct C words/frame0x60, no guards/profile changes.
Typed pointer return,11 field groups, u16 any/all masks, matched range helper
and last-match selection recovered. Scope the legacy table-array declaration
to this owner; shared headers/other owners stay unchanged.
12288 paired guest/196608 native/1470 range/120 field/32 original caller-fragment
cases, four negatives, copied owner/624-byte pool/two warnings and actual
padder qualify. US ELF passes; only target changes across6059 slots, all
addresses/extents/protected sections/720 owners/10855 guards unchanged.
Exact3348/5465 (61.26%), Game2675/4792 (55.82%),2117 different, zero drift;
conversion unchanged, README aggregate rows only. All121 post-link tests pass
in445.383s, zero skips/errors/failures;58 docs/3657 relative links/zero broken,
tool/syntax/diff checks pass. Final post-regression audit passes.
Next sampler exit recovery or
forward placeholder `func_15143E94`; oriented27 private offsets remain open.
No sibling/Release/save/runtime, whole-caller/hardware/gameplay or push.

Range-clamp byte match:
[Note 1075](WORKING_NOTES/1075-game-range-clamp-byte-match-20261007.md).
`func_15143D18`:36 words/frame0x10; using the argument pointers directly recovers
the original saved-pointer shape. Thirteen expected-word guards normalize only
temporary GPR allocation, with no frame/arithmetic/control/ordering changes.
3750 paired guest/1250 native/250 original call-delay cases and copied-owner/
actual-padder gates pass. Only target changes across6059 slots; all addresses,
protected sections/720 data owners and10842 prior guards unchanged,10855 total.
Exact3347/5465 (61.24%), Game2674/4792 (55.80%),2118 different, zero drift.
Conversion unchanged; README updates aggregate rows/date only.
All111 post-link tests pass in368.274s, zero skips/errors/failures;
57 documents/3646 relative links/zero broken, tool/syntax/diff checks pass.
Thirty further sampler exit/storage controls find no exact form. Sampler and
oriented builder remain uninstalled. Next sampler exit recovery or272-word
record query `func_151438D8`. No sibling/Release/save/runtime, gameplay or push.

Area-sampler recovery, not installed:
[Note 1074](WORKING_NOTES/1074-game-area-sampler-qualified-recovery-20261006.md).
`func_151432BC` now has a qualified signed-descriptor/five-input C candidate:
252 words, original frame0x50, 109 positional differences against254 retail
words. Remaining work is two shortened block exits/shared RA reload and the
circle RNG-byte store schedule. No broad guards, source/profile changes or
new matching count. Ten tests pass in18.864s:1024 independent guest cases,
48 conversion controls,1536 original-angle cases,64 complete original caller
cases,256 actual32-bit native cases, six negatives and copied-owner gates.
Candidate and original preserve external writes/calls and saved state under
these bounded tests; general FCSR/real RNG/gameplay remain unqualified.
Root README and production totals remain Note1073. See the note's resume steps.
Final24-test neighboring regression passes in34.986s, zero skips/errors/failures;
152 compiler controls find no exact candidate. All6059 production slots,
protected sections/720 data owners/10842 guards unchanged;56 docs/3633 relative
links/zero broken. Tools/syntax/diff checks pass. No production rebuild or push.

Point-transform assembly-to-C match:
[Note1073](WORKING_NOTES/1073-game-point-transform-assembly-to-c-match-20261006.md)
converts `func_15143134`:98 words/frame0x78, typed three-input ABI, live
diagnostics, fixed/float matrix paths and null/zero translation fallback.
31 relocation-checked guards normalize only the closed saved-register cycle
and independent save ordering; no frame/control/arithmetic rewrite.
1950 paired guest,180 original-helper,144 native and39 original call/delay
sites/234 seeded cases qualified; six negatives, actual padding/stale metadata
and copied-owner preservation. All6059 linked slots are unchanged from the
exact assembly baseline, including all addresses/extents and protected sections.
All720 Game-data owners/189088 bytes exact, warnings2->2,10811 prior guards
unchanged,10842 total. Converted5465/6042 (90.45%), Game4792/5321 (90.06%);
exact3346/5465 (61.23%), Game2673/4792 (55.78%),2119 different, zero drift.
Next254-word placeholder `func_151432BC`; oriented27 private offsets stay open.
All92 focused post-link tests pass in371.491s, no skips/errors/failures.
55 documents/3623 relative links/zero broken, tools/syntax/diff checks pass.
README changes aggregate tables only. No sibling/Release/save/runtime, host
adoption, whole-caller/hardware/gameplay acceptance or push.

Texture resolver match and original table binding:
[Note1072](WORKING_NOTES/1072-game-texture-resolver-match-and-table-binding-20261006.md)
recovers `func_1514306C`:50 C-emitted words, no frame, exact signed-index/
low-kind-byte/unsigned-threshold behavior.72 compiler controls, two exact O2/g3
forms. Two checked HI16/LO16 guards bind only the compact table reference to
the original800A562C asset table; no instruction scheduling/register/frame edits.
All12 pre-install checks pass in53.365s:13824 paired guest,19200 native,
486 complete102-word cache-caller/50-word resolver cases, ten negatives,
actual post-processing/padding/stale guards and three independent pool checks.
US ELF/6059-slot audit passes, only target changes. Protected sections/720
data owners/189088 bytes and warnings2->2 unchanged;10809 historical guards
retained,10811 total. Exact3345/5464 (61.22%), Game2672/4791 (55.77%),
2119 different, zero drift; conversion unchanged. README aggregate rows only.
All81 focused post-link tests pass in315.971s, no skips/errors/failures;
54 documents/3611 relative links/zero broken, tools/syntax/diff checks pass.
Next98-word `func_15143134`,
currently original assembly; recover point/output/Mtx ABI and status/helper
boundaries. Oriented27 private offsets remain open. No sibling/Release/save/
runtime, host adoption, original submit/render/gameplay acceptance or push.

Texture-cache submission match:
[Note1071](WORKING_NOTES/1071-game-texture-cache-submission-match-20261006.md)
recovers `func_15142E24`:102 direct retail words/frame0x40 under unchanged
O2/g3, no guards. Typed source/attachment ABI, signed packed shifts, live flags,
cache-hit gates and observable retail attachment same-value store.
32 controls; ten pre-install tests pass in39.947s:2304 paired guest,88 homes,
486 original-resolver,6912 native and nine original call/delay pairs, negatives,
actual padding and copied-owner preservation. US ELF/6059-slot audit passes:
only target changes; protected sections/720 exact data owners/189088 bytes,
10809 guards and two warnings unchanged. Exact3344/5464 (61.20%),
Game2671/4791 (55.75%),2120 different, zero drift; conversion unchanged.
All52 post-link tests pass in215.511s, no skips/errors/failures; tools/syntax/
diff checks pass,53 documents/3596 relative links/zero broken links.
Root README updates aggregate rows only.
Next50-word `func_1514306C` remains a placeholder; original instructions
qualified, not recovered C. Oriented142/frameB8/27 private differences remain;
ten extra matrix-storage controls find no improvement. No sibling/Release/save/
runtime, host adoption, whole-caller/submit-helper/gameplay acceptance or push.

Oriented matrix original-frame recovery, not installed:
[Note1070](WORKING_NOTES/1070-game-oriented-matrix-original-frame-recovery-20261006.md)
recovers `func_15142600`'s original142 words/frame0xB8 from in-place direction
normalization. Only27 private stack immediates differ:ten direction references
are four bytes low; seventeen matrix references are eight bytes low. All input
homes, early temporaries, arithmetic, call position and saved-state words agree.
128 maintained controls, no exact candidate. Thirteen tests pass in120.279s:
2448 six-body guest cases,1224 native caller cases per candidate across five
candidates,144 original caller/converter cases per body, eighteen compiled
negatives, two actual padder bodies and five copied builder owners.
All6059 production slots/720 data owners/10809 guards/protected sections remain
the Note1069 baseline; source and root README unchanged. No new matching count.
Recover the remaining private placement from legitimate C before installation.
General FCSR/conversion, native NaN payload/private trace identity and gameplay
acceptance remain outside the bounded gates. No sibling/Release/save/runtime,
host adoption or push.

All41 focused neighboring tests pass in185.411s, zero skips/errors/failures;
52 documents/3585 relative links/zero broken links, tools/syntax/diff checks pass.

Row-scaled matrix match and oriented-layout follow-up:
[Note1069](WORKING_NOTES/1069-game-row-matrix-match-and-oriented-layout-20261006.md)
recovers `func_15142838`:55 direct words/frame0x58 under unchanged O2/g3,
no guards. Nine-input pointer/float ABI, original rotation provider, translations
before row scaling, and original guMtxF2L call. Typed local declaration and
output cast leave `func_15133760`'s24 retail words and all31 caller-owner raw
functions unchanged. Sixteen controls;2160 paired guest/full trace/storage,
192 float-edge,36 guest-only home,288 original caller/converter and1176 native
caller cases, nine compiled negatives and actual padding qualification.
Only this builder changes across6059 slots; all10809 guards, protected sections,
720 Game-data owners and both owners' two warnings unchanged.
Exact3343/5464 (61.18%), Game2670/4791 (55.73%),2121 different, zero drift;
converted counts/bytes unchanged. All40 focused post-link tests pass in119.063
seconds, no skips/errors/failures.

Oriented `func_15142600` remains uninstalled:64 maintained controls now include
142/frameC8/47 and142/frameD0/44 stack-only candidates. The former recovers
direction slots exactly; the latter recovers early delta/horizontal/up slots.
Twelve tests qualify five guest bodies and four native candidates, retaining
all previous acceptance boundaries. Recover legitimate142/frameB8 layout next;
do not install stack/frame rewriting. Rotation provider is still bounded and
original conversion qualification finite/exact integral only. No sibling/
Release/save/runtime, hardware FCSR, gameplay acceptance, host adoption or push.

Initial oriented matrix recovery checkpoint, not installed:
[Note1068](WORKING_NOTES/1068-game-oriented-matrix-recovery-20261006.md)
qualifies `func_15142600`'s two-point basis, normalization, row/column scaling,
start-point translation and twelve-input caller ABI.32 maintained SDK controls:
142 words/frame0xB8/84 differences; a closer142/frame0xC8 challenger has57
differences, all stack immediates. Every non-stack instruction already agrees.
Eleven tests pass in39.018 seconds:2448 three-body guest cases,1224 native
caller cases per candidate,144 complete original caller/converter cases per
body, nine compiled negatives, native integer-load rejection, actual padding
and copied-owner preservation. Typed caller correction is copy-only; eight
caller-owner functions stay unchanged. Both builder copies preserve92 neighbors,
pools and two warnings. No candidate or guards installed; root README and
production baseline stay unchanged. Recover the challenger's private layout
and original frame0xB8 next, without a stack/frame rewrite. Scope and remaining
verification gates are recorded in Note1068.

Scaled matrix recovery:
[Note 1067](WORKING_NOTES/1067-game-scaled-matrix-match-20261006.md)
recovers `func_151424F4`:67 direct words/frame0x68, no guards/profile changes.
Typed output pointer and eleven float inputs; original rotation call, translation
stores, separately rounded column*row and matrix-element products, guMtxF2L ABI.
Correct local caller declaration/three float loads in `func_15133510` without
changing its30 retail words or any of its owner's31 raw functions.
16 controls;6480 paired guest/full trace/storage cases,696 float edges,48
guest-only home probes,3372 native caller cases, ten compiled negatives and
a native integer-load rejection.432 connected cases execute all30 original
caller/67 builder/115 converter words on finite exactly integral conversions.
Rotation provider remains a model; general FCSR/NaN conversion, helper
restoration and gameplay acceptance are not claimed.
Only builder changes across6059 slots; all10809 guards, protected sections/
720 owners and both owners' two warnings unchanged. Exact3342/5464 (61.16%),
Game2669/4791 (55.71%),2122 different, zero drift; converted counts/bytes
unchanged. All77 focused post-link tests pass in531.767 seconds, no skips/
errors/failures;49 docs/3546 relative links/zero broken, tools/syntax/diff
checks pass.
Next142-word `func_15142600`, frame0xB8: oriented basis from two points,
normalization, scaling, translation and fixed conversion. That checkpoint's
sixteen initial scratch controls gave143 words/frame0xC8/138 differences under
O2/g3, then uninstalled/unqualified. Current qualified controls and remaining
frame recovery are in the oriented-matrix section above. No sibling/Release/
save, runtime, host adoption, gameplay acceptance or push change.

Scaled descriptor recovery:
[Note 1066](WORKING_NOTES/1066-game-scaled-descriptor-match-20261006.md)
recovers `func_15142180`:80 direct words/frame0x70, no guards/profile changes.
Typed five-input void ABI, original76-byte descriptor, three-word position copy,
four separately rounded scale products and live D_800A5470/5474 reads. Submit
descriptor/position-subrecord pointers with0,255,1; opaque third input retains
all32 bits.64 controls;10800 paired guest cases/full traces/storage,2240 edge
cases,28 guest-only private overlap/home probes,20992 native cases,42 original
call/delay-pair cases and12 semantic negatives. Native excludes only private
padding61..63; helper/full callers, hardware FCSR and gameplay remain unvalidated.
Only target changes across6059 slots; all10809 guards, protected sections/720
owners, original pool and two owner warnings unchanged.
Exact3341/5464 (61.15%), Game2668/4791 (55.69%),2123 different, zero drift;
converted counts/bytes unchanged. All65 focused post-link tests pass in513.711
seconds, no skips/errors/failures;48 docs/3533 relative links/zero broken,
tools/syntax/diff checks pass.
Next67-word `func_151424F4`, frame0x68: float matrix construction, separately
rounded row/column scaling, translation and guMtxF2L call. Sixteen initial
controls find a direct candidate, not installed or qualified. No sibling/Release/
save, runtime, host adoption, gameplay acceptance or push change.

Random descriptor recovery:
[Note 1065](WORKING_NOTES/1065-game-random-descriptor-match-20261006.md)
recovers `func_15141F78`:96 direct words/frame0x78, no guards/profile changes.
Typed six-input void ABI, original40-byte descriptor with unsigned byte fields,
two ordered integer draws and one float draw; submit all16 arguments, including
the address source+4 rather than its stored value.64 controls;6912 paired guest
cases/full traces/storage,944 byte/float-edge cases,48 guest-only home probes,
57856 native cases,144 connected original call/delay-pair cases and12 semantic
negatives. The original full callers/RNG/submit helper and hardware FCSR are not
executed by those bounded fixtures. Native excludes three unspecified padding
bytes; exact guest stack provenance retained. Only target across6059 slots;
all10809 guards, protected sections/720 owners and two owner warnings unchanged.
Exact3340/5464 (61.13%), Game2667/4791 (55.67%),2124 different, zero drift;
converted counts/bytes unchanged. All54 focused post-link tests pass in528.932
seconds, no skips/errors/failures;47 docs/3521 relative links/zero broken,
tools/syntax/diff checks pass.
Next80-word `func_15142180`, frame0x70:76-byte descriptor, copied three-word
position, live constants and five-argument submit ABI. No sibling/Release/save,
runtime, host adoption, gameplay acceptance or push change.

Effect-record updater recovery:
[Note 1064](WORKING_NOTES/1064-game-effect-record-updater-match-20261006.md)
recovers `func_15141E38`:80 words/frame0x60,56 direct plus24 closed guards.
Typed void actor/index ABI; refresh every matching live record, create/copy/
link only when none matched. Minimal12-byte request retained; four private
payload-home guards restore retail's three uninitialized tail bytes, not a
new initialized field.7680 three-body guest/7680 native cases,1728 connected
search cases,3072 guest/1536 native checked-caller cases,36 guest actor-home
probes and ten semantic negatives. Normalized/retail full traces/storage agree;
native comparison excludes only three unspecified request-tail output bytes.
Copied owner93 functions: only target changes, warnings3->2, original pool
unchanged. Production only target across6059 slots; old10785 guards unchanged
plus24, protected sections/720 owners unchanged. Exact3339/5464 (61.11%),
Game2666/4791 (55.65%),2125 different, zero drift; converted unchanged.
All56 focused post-link tests pass in430.719 seconds, no skips/errors/failures;
46 docs/3509 relative links/zero broken, tools/syntax/diff checks pass.
Next96-word `func_15141F78`, frame0x78:
descriptor/RNG construction, float call ABI and live source reads need recovery.
The old commented draft dereferences source+4, but retail passes that address.
No allocator/link-helper restoration, host/gameplay/hardware acceptance,
sibling/frozen Release/runtime or push change.

Context-classifier recovery:
[Note 1063](WORKING_NOTES/1063-game-context-classifier-match-20261006.md)
recovers `func_15141CC0`: all57 words directly from C, no frame or guards.
One signed32-bit world read, four overrides and full-width context switch.
Existing pool anchor retains the16-entry table at addend0x218 after both
actor tables; all150 targets and the original640-byte owner are unchanged.
16 controls,15822 paired guest,5308551 native and2688 connected dispatcher
cases; eight compiled semantic negatives. Only target changes across6059
slots; all10785 guards, protected sections and720 data owners unchanged,
warnings3->3. Exact3338/5464 (61.09%), Game2665/4791 (55.63%),2126 different,
zero drift; converted counts/bytes unchanged. All32 focused tests pass in
277.833 seconds, no skips/errors/failures;45 docs/3497 links/zero broken,
tools/syntax/diff checks pass.
Next `func_15141E38`:80 words/frame0x60, still a placeholder. The intervening
37-word `func_15141DA4` is already exact. Preserve live search/cursor lifetime,
refresh all matching records, then allocate/link only when none matched.
Eight initial controls: private-cursor O2/g3 candidate fits80 words but has
frame0x58 instead of0x60 and37 differences; not installed or qualified.
No sibling/Release/runtime/host adoption, hardware/gameplay acceptance or push.

Actor-classifier recovery:
[Note 1062](WORKING_NOTES/1062-game-actor-classifier-match-20261006.md)
recovers `func_15141C0C`:all45 words directly from C, no frame or new guards.
Unsigned actor byte+4,19 mapped IDs/categories0..10, default11. Existing owner
rodata anchor preserves both original45/89-entry switch tables and drops the
compiler's private pool/padding.32 controls,8192 two-body guest,16384 native
and4608 connected dispatcher cases, six compiled negatives. Only target changes
across6059 slots; all10785 guards and protected sections/720 owners unchanged,
warnings3->3. Exact3337/5464 (61.07%), Game2664/4791 (55.60%),2127 different,
zero drift; converted counts/bytes unchanged. All24 focused post-link tests
pass in257.759 seconds, no skips/errors/failures; final eight-test ownership/
measured-frame rerun passes in36.264 seconds.44 docs/3485 links/zero broken;
tools/syntax/diff checks pass.
Next57-word `func_15141CC0`:16 initial controls give a direct candidate, not
installed/qualified; preserve the neighboring context-table anchor offset.
No sibling/Release/runtime/host adoption, hardware/gameplay acceptance or push.

Effect-dispatch recovery:
[Note 1061](WORKING_NOTES/1061-game-effect-dispatch-match-20261006.md)
recovers `func_15141A7C`:100 words/frame0x48,75 direct plus25 closed guards.
Explicit scoped helper-result sequencing preserves the live classifier lookup
on native C as well as IDO. Repeated record selectors, signed payload/counts,
live list links and registered cursor aliases remain.13824 three-body guest,
69632 connected retail-classifier,70848 actual32-bit native,288 cursor-alias,
864 guest caller/240 native wrapper cases and compiled negatives qualify the
contract. Raw C's one extra private-read site is explicitly bound, not blanket
stack-filtered. Only target changes across6059 slots; original10760 guard rows
unchanged,25 appended. Protected sections/720 data owners unchanged; warnings
3->3. Converted counts/bytes unchanged; exact3336/5464 (61.05%), Game2663/4791
(55.58%),2128 different, zero drift. All48 focused post-link tests pass in
495.394 seconds, no skips/errors/failures; final portable-prefix test rerun
passes.43 documents/3473 relative links/zero broken; tools/syntax/diff pass.
Next45-word actor classifier `func_15141C0C`:two fixed retail switch tables.
No helper-C/gameplay/hardware/host adoption, sibling/Release/runtime or push.

Historical effect-dispatch investigation, superseded by Note 1061:
[Note 1060](WORKING_NOTES/1060-game-effect-dispatch-investigation-20261006.md)
continues after banked `e5bf72e0` with100-word/frame0x48 `func_15141A7C`.
112 controls: live selector99/26; private cursor-write candidate100/21.
All100 retail words derive from a phased S0/S1 swap, closed prefix/query
scheduling and equivalent private cursor operations, without installation.
13824 guest cases per pairing;100-word source adds13764 proven private cursor
reads, all other traces/storage/calls equal. Connected real classifiers/list
search:69632 cases pass on each99/100-word pairing,128 helper words mapped/122
reached;100-word source binds110976 extra private reads, other traces equal.
Native/negative/relocation/padder/production
gates remain. All6059 production slots/10760 guards/protected sections unchanged.
Game2662/4791 exact,2129 different, zero drift. No sibling/Release/runtime/push.

Position-projection recovery:
[Note 1059](WORKING_NOTES/1059-game-position-projection-match-20261006.md)
recovers `func_1514182C`: all 63 words / frame 0x80 directly from C under
existing O2/g3, no guards. Delta declarations before the matrix recover its
retail SP+0x34 layout. Preserve all live origin reads before output stores and
the separate scale-then-500 multiplications. The float-height caller
`func_15141928` remains exact across its 18-word slot. Effect-only void ABI;
incidental guest F0 is qualified separately, not a native return contract.
15488 finite/guest-home cases, 144 connected retail SDK cases, 360 connected
caller cases, 9600 native finite cases, 720 special-float cases on each guest
body and native C, 36 controls and ten compiled negatives. Only target changes
across 6059 slots; protected sections, 720 Game-data owners and 10760 guards
unchanged, owner warnings 0->0. Converted counts/bytes unchanged; exact total
3335/5464 (61.04%), Game 2662/4791 (55.56%), 2129 different, zero drift.
All 37 focused post-link tests pass in 206.840 seconds, no skips/errors/failures;
41 documents/3453 relative links/zero broken; compileall/diff/tools checks pass.
Next `func_15141A7C`: 100 words / frame 0x48; repeated callback-table reads,
live list iteration and connected classifier ABI need recovery. No host,
hardware/FCSR/gameplay acceptance, sibling/Release/runtime or push change.

Historical position-projection investigation, superseded by Note 1059:
[Note 1058](WORKING_NOTES/1058-game-position-projection-investigation-20261006.md)
continues from banked `e1298167` with63-word/frame0x80 `func_1514182C`.
60 compiler controls. The fitting63-word/31-difference candidate fails24/108
origin-alias cases; cached origin values agree in all126 bounded guest cases
but emit67 words/frame0x88/47 differences. Identity rotation is modeled;40
connected retail coordinate-helper words execute. Float height/caller and
return ABI, alias-preserving footprint, native/negative/production gates remain.
No source/guard/count change; Game2661/4791 exact,2130 different, zero drift.
No next-function acceptance, sibling/Release/runtime or push change.

Actor-event dispatch recovery:
[Note 1057](WORKING_NOTES/1057-game-actor-event-dispatch-match-20261006.md)
recovers `func_151416E8`:55 words/frame0x18, all direct under existing O2/g3,
no guards. Repeated volatile selector/table lookups, byte command, live event
gate, cleanup/signed status stores and unsigned N64 payload address retained.
60724 two-body guest/262144 actual32-bit native cases;32 controls/nine compiled
negatives. Only target changes across6059 slots; protected sections/720 owners
and10760 guards unchanged, owner warnings0->0. Converted unchanged; exact
total3334/5464 (61.02%), Game2661/4791 (55.54%),2130 different, zero drift.
All28 focused post-link tests pass in246.167 seconds, no skips;39 docs/3432
links/zero broken. Next63-word `func_1514182C`:16 initial controls give63 words/
frame0x80/31 differences. Matrix translation row, float height ABI and caller need
qualification; no next-function installation, host/hardware/gameplay acceptance
or sibling/Release/runtime/push change.

Piecewise envelope recovery:
[Note 1056](WORKING_NOTES/1056-game-piecewise-envelope-match-20261006.md)
recovers `func_151415D4`:69 words/no frame, existing O2/g3,56 direct plus13
closed FPR-lifetime guards. Scoped factors recover rise store/branch/nop
directly;6480 three-body guest/3240 native finite cases,324 special-float
cases,18 bounded loops,32 controls/eleven negatives. Strict/live/unchecked
semantics retained. Audit: only target across6059 slots; protected sections/
720 owners unchanged,10747 old guards plus13, owner warnings0->0. Converted
unchanged; exact total3333/5464 (61.00%), Game2660/4791 (55.52%),2131 different,
zero drift. All19 focused tests pass in61.523 seconds, no skips (nine new/ten
changed metadata methods, not all earlier suites).38 docs/3420 links/zero
broken, tools/compileall/diff checks pass. Next55-word `func_151416E8`,16
initial controls; selected47/frame0x18/49 differences, no qualification or
installation. No hardware/FCSR/gameplay/host acceptance,
shared-header or sibling/Release/runtime change.

Previous envelope investigation:
[Note 1055](WORKING_NOTES/1055-game-piecewise-envelope-investigation-20261006.md)
starts `func_151415D4` from banked `adbeca4e`:69-word/no-frame retail envelope,
32 compiler controls, selected68 words/52 differences (product-first49).
720 two-body finite guest storage/access cases and eight bounded unchecked-loop
runs pass.65 raw/66 retail reachable words; three duplicate preludes untouched.
One missing rise-branch word plus allocation/branch differences remain; native,
special-FP, negative, padder and production gates pending. No installation,
guard/profile/image change. Current exact counts below remain unchanged.

Timed interpolation recovery:
[Note 1054](WORKING_NOTES/1054-game-timed-interpolation-match-20261006.md)
recovers `func_15141478`:59 words/frame0x30, existing O2/g3,50 direct plus nine
derived private-pointer-home/commutative FP guards. Explicit RNG call ordering,
strict-negative expiry, live post-call fields and unclamped smoothing retained.
8640 finite/432 private-home/1008 special-FP three-body guest cases;
4320 finite/504 special-FP native cases,32 controls and ten compiled negatives.
Completed production audit: only target across6059 fixed slots; protected
sections/720 owners unchanged,10738 old guards plus nine, owner warnings0->0.
Converted unchanged; exact total3332/5464 (60.98%), Game2659/4791 (55.50%),
2132 different, zero drift. All18 focused post-link tests pass in55.115 seconds,
no skips: nine new plus nine changed metadata tests, not all101 earlier tests.
36 docs/3401 links/zero broken; tools/compileall/diff checks pass.
Next69-word `func_151415D4` piecewise envelope:16 initial controls, selected
68 words/no frame/52 differences, still a production placeholder. No hardware/
FCSR/gameplay/host claim or sibling/frozen Release/build/save/runtime change.

Grid/channel updater recovery:
[Note 1053](WORKING_NOTES/1053-game-grid-channel-updater-match-20261006.md)
recovers `func_151412BC`: 96 words/frame0x18, existing O2/g3, 53 direct words
plus43 guards derived from two closed register cycles and independent LO16
address scheduling. All branch/delay/arithmetic shapes retained, normalized
V0=4; owner-local table/pointer casts, no shared-header or data change.
1728 three-body guest storage/trace cases, signed bounds/byte cycling, 864
native cases and ten negatives; nine tests include144 compiler controls.
Only target across6059 fixed slots, protected sections/720 owners unchanged;
10695 guards plus43, total10738, owner warnings0->0, zero new. Converted
unchanged; exact total3331/5464 (60.96%), Game2658/4791 (55.48%), 2133 different,
zero drift. All92 retained post-link tests and the corrected nine-test updater
rerun pass (239.123 seconds), no skips;101 unique current tests qualified.
Initial combined run's sole caller-fixture failure is corrected/documented;
35 docs/3389 relative links/zero broken. Tools/compileall/diff checks pass.
Next59-word `func_15141478` randomized interpolation:112 initial controls.
New both-pointer-early form gives59/frame0x30/nine differences; derived six
private-slot/three commutative FP changes reproduce all words,2160 finite guest
storage/callback/access cases pass. No native/padder/full match installation.
Sibling grid updater
already retail-translated; no hardware/gameplay/host claim, sibling/Release
change or push.

Payload-copy wrapper recovery:
[Note 1052](WORKING_NOTES/1052-game-payload-copy-wrapper-match-20261006.md)
recovers `func_151407D0`: 53 words/frame0x40, existing O2/g3, 43 direct words
plus ten closed success-schedule/branch guards with counter HI16 movement.
Descriptor pre-mutations, failure, live copy/selector/counter and allocation
return qualified. Correct callee `func_1513D524`'s false void/word-descriptor
ABI; all28 direct words unchanged. 40 controls, 5376 ordinary/65536 byte-pair
guest cases, 72 join/1440 connected cases, 132352 native cases/ten negatives.
Only target across6059 fixed slots, protected sections/720 owners unchanged;
10685 guards plus ten. Two ABI warnings removed (45->43), target owner0->0,
zero new. Converted unchanged; exact total3330/5464 (60.94%), Game2657/4791
(55.46%), 2134 different, zero drift. All92 post-link tests pass in901.823
seconds, no skips; 34 docs/3377 relative links/zero broken.
Next96-word `func_151412BC` grid lookup: preliminary correct frame/length,
53 differences; 1728 two-body guest storage/trace cases agree, raw V0 still
differs. Native/complete ABI/match unqualified, no installation. Larger
`func_151408A4` unrecovered.
Sibling outer wrapper already retail-translated; no full allocator/dispatch/
hardware/gameplay/host claim, sibling/Release change or push.

List-key sorter recovery:
[Note 1051](WORKING_NOTES/1051-game-list-key-sort-match-20261006.md)
recovers `func_151406AC`: 72-word body/73-word slot, frame0x138, existing
O2/g3, 54 direct instructions plus 18 register-only lifetime guards and trailing
nop. Stable equal-key ordering, captured successor and live link repairs;
5760 two-body full-storage guest cases, 65535 two-body bypass values, 960
native storage, 65536 native signed-value and 65535 native bypass cases.
Strict guest boundaries preserve retail's null-head write and negative-key
sentinel walk; no safety/cycle fixes. Production link/audit pass: only target
changes across 6059 fixed slots, protected sections/720 owners unchanged;
10667 existing guards plus18, 45 unchanged warnings, zero new. Converted
counts unchanged; exact total3329/5464 (60.93%), Game2656/4791 (55.44%),
2135 different, zero drift. 33 docs/3365 links/zero broken.
All 83 post-link regression tests pass in 839.818 seconds, no skips.
Next adjacent 53-word `func_151407D0` allocation/copy wrapper, including the
false void return of its `func_1513D524` callee. Sibling sorter already has
retail-translated instructions with host cycle guards; leave it unchanged.
No full dispatch/hardware/gameplay/host claim, sibling/Release change or push.

Basis-vector quad builder recovery:
[Note 1050](WORKING_NOTES/1050-game-basis-quad-builder-match-20261006.md)
recovers `func_15140410`: 167 words/frame 0x68, existing O2/g3, 165 direct
plus two independent load scheduling guards. Captured scaled components,
live translations, fresh-copy slot reloads and original-pointer return qualified
with 24 controls, 1728 standalone/324 actual-backend/198 float/144 actual-owner
two-body guest cases, 576 native storage and all 65536 signed-view null cases.
Only target slot changes across 6059 fixed slots; protected sections and 720
data owners unchanged, 10665 existing guards preserved plus two. Typed owner
call removes exactly three old warnings, leaving 45 unchanged and zero new;
all 13 wrapper instructions remain exact. Converted counts unchanged;
exact total 3328/5464 (60.91%), Game 2655/4791 (55.42%), 2136 different,
zero drift. All 75 focused post-link tests pass in 765.095 seconds, no skips;
32 docs/3353 relative links/zero broken. Tools, compileall and diff checks pass.
Next adjacent `func_151406AC`: 72-word body/73-word slot, non-null list and
sentinel-key preconditions need further qualification. Preliminary 100 controls:
correct body/frame, 18 remaining differences; 864 valid-list and 65535 nonzero
bypass two-body guest cases agree with retail, not yet installed/native-qualified.
Sibling generated reference
still contains a zero-return placeholder; no host adoption/runtime claim or
sibling source/build/save/frozen Release change or push.

Cached quad builder recovery:
[Note 1049](WORKING_NOTES/1049-game-cached-quad-builder-match-20261006.md)
recovers `func_15140190`'s false stub: 134 words/frame 0xD0 under existing
O2/g3, 129 direct plus five independent first-corner scheduling guards.
24 controls, 864 two-body actual-matrix guest cases/all 174 chain words,
864 native full-storage cases and all 65536 native signed-view null cases.
Live fresh-copy slot reloads, translation reads, original return and escaped
cursor updates preserved. Only quad slot changed across 6059 slots; all
addresses/sizes, protected sections and 720 owners unchanged, 10660 existing
guards preserved plus five. 48 owner warnings unchanged, zero new. Converted
counts stay 5464/6042 and Game 4791/5321; exact total 3327/5464 and Game 2654/4791,
2137 different, zero drift. 31 docs/3341 links/zero broken. All 66 focused
post-link tests pass in 741.875 seconds, no skips.
Next adjacent 167-word `func_15140410` basis-vector quad builder; no full
backend/orientation/hardware FCSR/gameplay/host claim, sibling/Release change
or push.

Vertex attribute initializer direct C conversion:
[Note 1048](WORKING_NOTES/1048-game-vertex-attribute-initializer-direct-match-20261006.md)
converts retained `func_151400D0`: all 48 direct words/frame zero, existing
O2/g3, no guards/profile/shared header/data. Owner-local void/pointer ABI and
constructor cast corrected; all 217 constructor/two-helper words unchanged.
Transient flag stores, signed colors and alias-sensitive read order qualified
with 24 controls, 456 two-body guest cases, 65536 halfword cases, 131072 native
standalone, 3072 two-body actual-chain guest and 131072 actual-chain native
cases. All 6059 linked slots identical to assembly checkpoint; protected
sections/720 owners/10660 guards intact. 48 preexisting warnings unchanged,
zero new. Converted total 5464/6042, Game 4791/5321; exact total 3326/5464,
Game 2653/4791, zero drift, 2138 different. All 60 focused post-link tests
pass in 730.693 seconds, no skips; 30 docs/3329 relative links have no breaks.
Next recover 134-word `func_15140190` cached quad builder's false C stub;
no full backend/hardware/gameplay/host adoption, sibling source/build/save/
frozen Release change or push.

View corner initializer direct C conversion:
[Note 1047](WORKING_NOTES/1047-game-view-corner-initializer-direct-match-20261006.md)
converts retained `func_1513FFF4`: all 55 direct words/frame eight, existing
O2/g3, no guards/profile/shared header/data. Owner-local void/pointer/byte
prototype and constructor call recovered; constructor's 114 words unchanged.
Unsigned dimension underflow, variant corner stores, index-255 no-access gate
and captured dimensions qualified with 40 controls, 8192 two-body guest cases,
65536 byte-pair cases, 15 no-access cases, 256 two-body aliases, 589824 native
helper and 131072 connected native cases. 1536 two-body actual constructor/
helper cases cover all 169 chain words. All 6059 linked slots are identical
to the assembly checkpoint; protected sections/720 owners/10660 guards intact.
48 owner warnings unchanged, zero new. Converted total 5463/6042, Game
4790/5321; exact total 3325/5463, Game 2652/4790, zero drift, 2138 different.
All 52 focused post-link tests pass in 713.368 seconds, no skips.
Next inspect retained 48-word
`func_151400D0` vertex-attribute helper; no full backend/hardware/gameplay/
host adoption, sibling source/build/save/frozen Release change or push.

Source effect constructor direct match:
[Note 1046](WORKING_NOTES/1046-game-source-effect-constructor-direct-match-20261006.md)
recovers `func_1513D2F0`: all 114 words directly, frame 0x38, existing O2/g3;
no new guards/profile/shared header/data. Captured allocator flags, live
88-byte descriptor copy, helper setup, default sentinel and inclusive live
view bound. 97 compiler controls, 6912 two-body guest cases, 2048 width
cases, 18 two-body raw-default cases, 576 actual-wrapper guest cases,
131072 native constructor and 576 connected native cases. All 114 words
covered; wrapper/constructor path covers 204 reachable words. Only target
changes across 6059 fixed slots; protected sections/720 owners/10660 guards
intact. The owner's 48 preexisting warnings are unchanged; zero new warnings.
Total 3324/5462, Game 2651/4789 exact, zero drift, 2138 different.
All 43 focused post-link tests pass in 487.777 seconds, no skips. Constructor no longer a
placeholder; backend helpers remain callbacks in qualification. Next inspect
raw-assembly helper `func_1513FFF4`, not full gameplay/host acceptance.
No sibling source/build/save/frozen Release change or push.

Source-backed effect packet direct match:
[Note 1045](WORKING_NOTES/1045-game-source-effect-packet-direct-match-20261006.md)
recovers `func_1519ED84`: all 96 words directly, frame 0xA0, existing O2/g3;
no guards/profile/shared header/data edits. 88-byte packet preserves five
alignment bytes; twelve-argument handoff and conditional pointer publication.
98 compiler controls, 3456 three-body guest cases, 65536 width/byte-pair
sweeps, 128 three-body float cases, 576 connected-placeholder cases,
131072 opaque native and 192 actual-consumer native cases. Linked audit:
only target changes across 6059 fixed slots; protected sections/720 owners/
10660 guards intact; owner diagnostics empty. README total 3323/5462,
Game 2650/4789 exact, zero drift, 2139 different. All 34 focused post-link
tests pass in 497.803 seconds, no skips. Constructor `func_1513D2F0` still a placeholder; consumer
`func_1519EF04` remains exact. Next recover that 114-word constructor;
no complete gameplay/host claim, sibling/frozen Release change or push.

Source-backed actor packet recovery:
[Note 1044](WORKING_NOTES/1044-game-actor-source-packet-byte-match-20261006.md)
recovers `func_1519EB8C`: 102 words/frame 0xB8, semantic C with 14 guards
for a closed opening schedule, existing O2/g3. No new profile/shared header/
data. 124-byte descriptor preserves eight alignment bytes; conditional
source-pointer payload publication. 56 controls, 3456 three-body guest cases,
65536 halfword sweeps, 384 float-boundary cases, 131072 opaque native and 192
actual-constructor native cases. Linked audit passes: only target changes
across 6059 fixed slots; protected sections and 720 data owners stay intact.
10660 guards, exactly 14 new target rows; owner diagnostics empty. README
total 3322/5462 (60.82%), Game 2649/4789 (55.31%) exact, zero drift,
2140 different. All 56 focused post-link tests pass in 281.571 seconds,
no skips.
Constructor remains semantic/non-matching, not complete backend/hardware/
gameplay/host adoption. Next `func_1519ED84`. No sibling/Release change or push.

Effect-configuration packet direct match:
[Note 1043](WORKING_NOTES/1043-game-effect-configuration-packet-direct-match-20261006.md)
recovers `func_1519EA78`: all 69 words directly, frame 0x70, existing O2/g3;
no new guards/profile/shared header/data. Complete 60-byte packet, unsigned
selector, separate float local and eight typed call arguments. 32 controls;
1296 two-body guest cases, 65536 width sweeps, 100 two-body raw-float cases
and 131072 native cases. All 69 words covered. Only target changes across
6059 slots; protected sections/720 owners/10646 guards intact. Owner
diagnostics empty. README total 3321/5462, Game 2648/4789 exact; zero drift,
2141 different. All 26 focused post-link tests pass in 219.250 seconds,
no skips. The 228-word `func_15152190` callee
is still a C placeholder; no complete effect-path/gameplay/host claim.
Next `func_1519EB8C`'s actor packet. No sibling/frozen Release change or push.

Address-record allocator direct match:
[Note 1042](WORKING_NOTES/1042-game-address-record-allocator-direct-match-20261006.md)
recovers `func_1519E970`: all 37 words directly, frame 0x20, existing O2/g3;
no new guards/profile/shared header/data. Seven typed arguments, pointer
return, retained allocator/list linking and ordered payload stores. 48
controls; 1152 cases each in three two-body guest modes, 65536 selected width
sweeps and 131072 native cases. All 85 chain words covered. Only target
changes across 6059 slots; protected sections/720 owners/10646 guards intact.
Owner diagnostics empty. README total 3320/5462 and Game 2647/4789 exact,
zero drift, 2142 different. All 77 focused post-link tests pass in 468.864
seconds, no skips. Next `func_1519EA78`'s
configuration-packet wrapper. No complete caller/FCSR/gameplay/host adoption,
sibling/frozen Release change or push; Game remains active.

Conditional packet allocator direct match:
[Note 1041](WORKING_NOTES/1041-game-conditional-packet-allocator-direct-match-20261006.md)
recovers `func_1519E6BC`: all 38 words directly, frame 0x38, existing O2/g3;
no new guards/profile/shared header/data. Post-cleanup global gate, failure
publication and captured 12-byte packet with three untouched alignment bytes.
24 controls; 3072 cases each opaque/connected-cleanup/connected-allocation,
two bodies, plus 1536 selected code-byte sweeps and 18432 native cases.
138 reachable chain words execute; 140 linked words bound. Only target changes
across 6059 slots; protected sections/720 owners/10646 guards intact.
Baseline/current owner diagnostics empty. README total 3319/5462 and Game
2646/4789 exact, zero drift, 2143 different. All 71 focused post-link tests
pass in 369.862 seconds, no skips. Next
`func_1519E970`'s seven-argument record allocator. No complete caller/FCSR/
gameplay/host adoption, sibling/frozen Release change or push; Game stays active.

Random selector/output direct match:
[Note 1040](WORKING_NOTES/1040-game-random-selector-outputs-direct-match-20261006.md)
recovers `func_1518E5D8`: all 37 words directly, frame 0x18, existing O2/g3;
no new guards/profile/header/data. Seven-pointer ABI and ordered output stores;
retained selector's third RNG and sequential palette reads remain intact.
24 compiler controls; 4096 opaque / 16384 connected-selector / 8576 fully
connected guest cases and 14528 native cases. All 86 wrapper/helper/RNG words
covered. Whole linked audit: only target changes across 6059 slots;
protected sections/720 data owners/10646 guards unchanged. Four owner warnings
match baseline. README now total 3318/5462 and Game 2645/4789 exact, zero
drift, 2144 different. All 65 focused post-link tests pass in 310.324 seconds,
no skips. Next
`func_1519E6BC`, conditional allocator/packet wrapper still a stub. No complete
caller/FCSR/gameplay, sibling/frozen Release change or push; Game stays active.

Actor position-queue wrapper direct match:
[Note 1039](WORKING_NOTES/1039-game-actor-position-queue-wrapper-direct-match-20261006.md)
recovers `func_1517D5FC`: all 37 words directly, frame 0x28, existing O2/g3;
no new guards/profile/header/data. Signed coordinate ABI, actor stride/float
capture and shifted selector. 32 controls; 24576 opaque / 37936 connected
guest cases, 8192 opaque / 49152 connected native cases. All wrapper/helper
words covered; retained 33-word helper and its 29 old guards unchanged.
All 59 post-link tests pass in 255.215 seconds, no skips.
Only target changes across 6059 slots; protected sections/720 owners/10646
guards intact. Baseline/current owner diagnostics empty. README now total
3317/5462 and Game 2644/4789 exact, zero drift, 2145 different. Next
`func_1518E5D8`, RNG/selector/output wrapper still a stub. No complete caller/
FCSR/gameplay, sibling/frozen Release change or push; Game stays active.

Alternate actor-dimension direct match:
[Note 1038](WORKING_NOTES/1038-game-alternate-actor-dimensions-direct-match-20261006.md)
recovers `func_1515C244`: 41 direct C words plus two retail padding words,
complete 43-word slot exact under existing O2/g3. No frame/guards/profile/
header/data change; local signed +0xE8 cast preserves the shared unsigned field.
16 controls; 43008 two-body guest cases / 21504 native cases. Forty reachable
words execute, impossible delay and padding structurally bound. All 52
post-link tests pass in 228.619 seconds, no skips. Only target
changes across 6059 slots; protected sections/720 owners/10646 guards intact.
Baseline/current owner compiles have empty diagnostics. README now total
3316/5462 and Game 2643/4789 exact, zero drift, 2146 different.
Next `func_1517D5FC`, 37-word coordinate/actor queue wrapper still a stub.
No full callers/FCSR/gameplay, sibling/frozen Release change or push.

Actor-dimension/position direct match:
[Note 1037](WORKING_NOTES/1037-game-actor-dimensions-position-direct-match-20261006.md)
recovers `func_1515C1A0`: all 41 words directly, no frame/guards/profile/data
change. Real actor/point layouts, signed dimensions/vertical offset and
ordered overlapping outputs. 16 compiler controls; 36864 two-body guest
cases / 18432 native cases. Forty reachable words execute; one unreachable
delay word is structurally bound. All 47 post-link tests pass in 193.845
seconds, no skips. Only target changes across 6059 slots; protected
sections/720 owners/10646 guards intact. Both baseline/current
owner compiles have empty diagnostics. README now total 3315/5462 and
Game 2642/4789 exact, zero drift, 2147 different. Next `func_1515C244`,
the adjacent signed +0xE4/+0xE6/+0xE8 twin. No full callers/FCSR/gameplay,
sibling/frozen Release change or push; Game matching stays active.

Projection-wrapper investigation:
[Note 1036](WORKING_NOTES/1036-game-projection-wrapper-abi-and-frame-audit-20261006.md)
banks 20 O2/g3 controls for `func_15144CEC`; none matches the 101-word retail
slot/frame 0x48. All candidates use frame 0x50. The 58-word synthetic-return
matrix helper chain is linked retail-exact. Three compiler/identity tests pass
in 14.634 seconds, no skips; no execution/alias qualification or source install.
All 6059 slots/protected sections/720 data owners/10646 guards unchanged;
matching totals remain 3314/5462 total, 2641/4789 Game, zero drift.
Next inspect `func_1515C1A0`; projection and pair-clamp frames remain open.
No sibling/frozen Release change or push; Game matching stays active.

Descriptor shape-measure direct match:
[Note 1035](WORKING_NOTES/1035-game-descriptor-shape-measure-direct-match-20261006.md)
recovers `func_1514462C` across all 56 words directly under existing O2/g3,
no frame/guards/profile/data change. Pointer prototype and two float externs
replace the stub's false integer-address signature. 48 compiler controls;
21504 three-body guest cases and 10752 native cases cover signed dimensions,
all flag bytes, wrapped product and ordered float rounding. All 55 reachable
retail words execute; the one unreachable load is structurally bound.
All 58 combined tests pass in 94.861 seconds, no skips.
Only target changes across 6059 slots; protected sections/720 owners/10646
guards intact despite header-triggered rebuild. Three owner warnings equal
the independently compiled baseline source and headers. README now total
3314/5462, Game 2641/4789 exact, zero drift, 2148 different. Next inspect
101-word `func_15144CEC`, still a zero-return projection-wrapper placeholder.
Pair-clamp frame remains open. No full callers/gameplay/FCSR, sibling/frozen
Release change or push; Game matching remains active.

Pair-clamp backend audit:
[Note 1034](WORKING_NOTES/1034-game-pair-clamp-saved-register-backend-audit-20261006.md)
banks nine locally evidenced O2/g3 uopt controls. All accepted with empty
diagnostics; none recovers the saved-pointer frame or reduces 36 differences.
Seven emit the same body, one changes a closed three-word temporary lifetime,
one emits 35 words with caller-home copies. No production/profile/data/guard
or aggregate change. All nine pair tests pass in 35.646 seconds, no skips.
Next recovery candidate: adjacent `func_1514462C`,
still a zero-return placeholder; its isolated semantic form emits all 56
retail words directly, pending qualification and linked installation.

Pair-clamp register-lifetime follow-up:
[Note 1033](WORKING_NOTES/1033-game-integer-pair-clamp-register-lifetime-audit-20261006.md)
banks 128 further compiler controls after `fe925393`: separate parameter/local
register hints do not recover `func_15143D18`'s frame. All O2/g3 bodies equal
the committed 29-word recovery; O1/g3 bodies are oversized with frame 0x20.
1536 guest corner runs preserve ordered access traces and footprints;
all 51 combined tests pass in 93.572 seconds, no skips. All 6059 slots,
protected sections/720 owners/10646 guards equal the committed checkpoint.
No production/guards/profile/data or aggregate-count change. Continue the
saved-pointer allocation/frame and branch-likely/shared restore tail.
This function remains non-matching at 36 aligned differences; Game stays active.

Integer pair-clamp access recovery, still non-matching:
[Note 1032](WORKING_NOTES/1032-game-integer-pair-clamp-xor-access-recovery-20261006.md)
recovers `func_15143D18`'s ordered XOR exchange and sequential endpoint clamps.
29 emitted words, frame zero, seven padding words in the 36-word slot;
all 36 aligned words still differ. No guards/profile/header/data change.
92 compiler controls find no exact body. 24576 guest cases cover all retail
words; the old body agrees on final outputs but differs in 7168 access traces.
12288 native cases pass; all 50 combined tests pass in 64.519 seconds, no skips.
Only target changes across 6059 slots; protected
sections/720 owners/10646 guards intact. Three owner warnings equal baseline.
README aggregates remain total 3313/5462 and Game 2640/4789 exact, zero drift,
2149 different. Next: this function's saved-pointer frame/register lifetimes
and branch-likely return tail. No gameplay/caller-domain expansion, sibling
or frozen Release change or push. Game matching remains active.

Indexed state-save direct match:
[Note 1031](WORKING_NOTES/1031-game-indexed-state-save-direct-match-20261006.md)
recovers `func_15123934` across all 38 words directly from C, frame 0x18,
real actor/header definitions, no guards/profile/data change. Correct 2/4-byte
indexing, sequential overlapping saves, callback argument and pre-call mark.
32 compiler controls; 7680 opaque / 4736 connected three-way cases, six
zero-mask non-returning prefixes and 2520 native cases. All wrapper/callback
words covered; unchanged production callback already 14/14 exact. All 43
tests pass in 48.052 seconds, no skips. Only target changes across 6059;
protected sections/720 owners/10646 guards intact. Five owner warnings
verified identical to baseline. README: total 3313/5462, Game 2640/4789 exact,
zero drift, 2149 different. Next: `func_15143D18`, existing 24-word C versus
36-word retail XOR-swap/clamp, 36 differences. Full gameplay/callers/valid
domain expansion remain unqualified. No sibling/frozen Release change or push.

Random-reload timer direct match:
[Note 1030](WORKING_NOTES/1030-game-random-reload-timer-direct-match-20261006.md)
recovers `func_150D26F0`: all 39 words directly under existing O2/g3, frame
0x20, no new guards/profile/data. Typed record fixes the array body's 14
differences. 76 compiler controls; 896 gate / 1920 reload / 48 trap three-way
cases and 1408 native cases cover every retail word. Preserve wrapped timer
subtraction, unsigned remainder, post-callback fields and break 7. All 35
tests pass in 20.151 seconds, no skips. Only timer changes across 6059 slots;
protected sections/720 owners and all 10646 guards intact. README: total
3312/5462, Game 2639/4789 exact, zero drift, 2150 different. Next: recover
38-word `func_15123934`'s indexed field-save/update/callback pass. Full
dispatcher/RNG/gameplay and hardware trap delivery remain unqualified.
No sibling/frozen Release change or push; Game matching goal stays active.

Float-reference packet wrapper direct match:
[Note 1029](WORKING_NOTES/1029-game-float-reference-packet-wrapper-direct-match-20261006.md)
recovers `func_150C2804`: all 37 words directly from C under existing O2/g3,
frame 0x38, no guards/profile/data/header change. 24 compiler controls;
2304 opaque and 256 float-pattern three-way cases, 288 connected-retail-callee
cases and 14400 native cases. Full wrapper/callee word coverage; live inspection
confirms the unchanged production callee already matches all 50 retail words,
superseding the stale placeholder claim below. All 92 tests pass in 233.716
seconds; eight packet tests rerun with the callee assertion pass in 6.375
seconds, no skips. Only this slot changes across 6059; all protected
sections/720 owners and 10646 guards unchanged. README: total 3311/5462,
Game 2638/4789 exact, zero drift, 2151 different. Next: inspect 39-word
`func_150D26F0`, still a placeholder. No gameplay/
FCSR/complete allocator, sibling/frozen Release or push claim.

Linked-record position tail match:
[Note 1028](WORKING_NOTES/1028-game-linked-record-position-tail-match-20261006.md)
closes `func_150E6FAC` across all 72 retail words using three expected-word /
empty-relocation guards and one saved-RA insertion. Raw C remains 71 words
with 15 aligned differences; no source/profile/frame change. 3360 three-way
guest cases, all reachable retail words, independent emitter/stale-anchor
checks. Only this slot changes across 6059; protected sections/720 owners and
all old guards intact. All 84 tests pass in 267.948 seconds, no skips.
README: total 3310/5462 and Game 2637/4789 exact,
zero drift, 2152 different. Next ordinary candidate: `func_150C2804`, 37-word
packet dispatcher still a placeholder. Edge helper remains at 102 differences.
No full gameplay/FCSR/helper implementation, sibling/frozen Release or push claim.

Graph edge crossing scope audit:
[Note 1027](WORKING_NOTES/1027-game-graph-edge-crossing-scope-audit-20261006.md)
rejects 101 scope/plane/aggregate/operand controls without improving the
102-difference helper. All 6059 slots match the prior checkpoint; no production,
guard, profile or data change. Counts/README unchanged. Next inspect closest
remaining C match `func_150E6FAC`'s return tail. The edge helper remains open;
no full-chain/FCSR/gameplay, sibling/frozen Release or push claim.

Graph edge crossing lifetime improvement:
[Note 1026](WORKING_NOTES/1026-game-graph-edge-crossing-lifetime-improvement-20261006.md)
improves `func_15086D94` from 151 to 102 real differences. All 207 words now
emit from C without padding; frame 0x80 still differs from retail 0x90.
The saved prefix and complete outer-loop tail match directly, with one count
load. 209 new controls; qualification now compares retail and three C bodies
across 2177 cases, plus 288 native footprints; all 62 tests pass, no skips.
Only the helper changes across
6059 slots; root/parent, protected sections, 720 owners and 10643 guards intact.
README/counts unchanged: Game 2636/4789 exact, zero drift, 2153 different.
Next: frame/minimum home and normal/side/constant lifetimes. Full helper-chain/
FCSR/gameplay acceptance remains separate; the Game matching goal stays active.

Graph edge crossing semantic recovery:
[Note 1025](WORKING_NOTES/1025-game-graph-edge-crossing-recovery-20261006.md)
replaces `func_15086D94`'s zero-return placeholder with its complete horizontal
crossing pass. Not byte-exact: 206 body words / 207-word slot, frame 0x78,
151 differences. Preserve retail's last-fraction result and 100.0f initial
minimum. Thirty-nine forms / 78 controls; 2177 three-way guest cases, 198/207
retail words exercised, 288 native footprints; all 58 combined tests pass,
no skips. Only the helper changes across
6059 slots; root/parent, protected sections, 720 data owners and 10643 guards
unchanged. README/counts stay 3309/5462 total and 2636/4789 Game exact, zero
drift, 2153 different. Next: helper frame/private homes and normal lifetimes;
parent remains at 282 differences. Full helper-chain/FCSR/gameplay acceptance
is still separate. Its 151-difference checkpoint is superseded by Note 1026
above; the Game matching goal remains active.

Root neighbor lookup direct match:
[Note 1024](WORKING_NOTES/1024-game-root-neighbor-lookup-direct-match-20261006.md)
recovers `func_15085DF8` across all 168 words directly from C, frame 0x80,
no guards/profile/overflow. Seventy controls; 3275 three-way guest cases,
166 executable words (two always-annulled retail delays), 1536 native cases.
All 45 lookup/parent/lifetime/visitor tests pass, no skips. All 6059 addresses/
lengths survive; only lookup and the five-float geometric placeholder ABI
change. Parent bytes and protected sections/720 owners/all guards unchanged.
README aggregates updated: 3309/5462 total, 2636/4789 Game exact, zero drift,
2153 different. Its still-placeholder geometric-helper boundary is superseded
by Note 1025 above; neither helper nor parent is matched. Full geometry/
lookup/caller/gameplay and FCSR acceptance remain separate.

Zone/player selection lifetime improvement:
[Note 1023](WORKING_NOTES/1023-game-zone-neighbor-selection-lifetime-screen-20261006.md)
retains the typed query pointer in `func_1508B3F8`: 369 emitted words, no padding,
frame 0x140; differences fall from 340 to 282. Still not byte-exact. No new
guards/profile/assembly/overflow or query enlargement. Ninety-one additional
controls; 2990 four-way guest cases, full parent/visitor coverage and 1424
native footprints. All 17 qualification/lifetime and 13 visitor regression
tests pass. Only parent changes across 6059 slots; protected sections, all
720 Game-data owners and 10643 guards intact. README/counts unchanged.
Next: retail query/private homes and saved address lifetimes; retained
370-word / 233-difference control remains oversized and uninstalled.
The lookup-placeholder boundary at that checkpoint is superseded by Note 1024
above; full helper-chain/gameplay remains unqualified.

Zone/player neighbor selection semantic recovery:
[Note 1022](WORKING_NOTES/1022-game-zone-neighbor-selection-recovery-20261006.md)
replaces `func_1508B3F8`'s placeholder with the complete parent pass. Not a
byte match: 367 body words plus two padding nops, frame 0x140, 340 differences.
No new guards/profile/assembly/overflow. 58 controls; 2990 three-way guest
cases, all 369 parent / 84 connected visitor words and 1424 native footprints.
14 qualification and 60 shared-oracle regression tests pass, no skips.
Audit preserves all 6059 slot addresses/
lengths: only parent and four argument homes in the still-placeholder root
lookup change. Protected sections/720 data owners and all guards intact.
Counts/README aggregates unchanged: Game exact 2635/4789, zero drift.
Next: parent query homes/address lifetimes; a retained 370-word / 257-difference
form exceeds the slot by one word. Full lookup/caller/gameplay unqualified.

Recursive record-neighbor visitor byte match:
[Note 1021](WORKING_NOTES/1021-game-record-neighbor-visitor-match-20261006.md)
replaces `func_1508B2A8`'s zero-return placeholder with its complete 84-word
recursive X/Z threshold visitor. Frame 0x30 and five saved-register lifetimes
match; six guards normalize two complete V0-to-V1 temporary lifetimes.
No compiler override, insertion/omission or assembly edit. Twenty-four controls
complete; 13 qualification tests and 49 focused regressions pass, no skips.
4096 leaf and 4608 recursive three-way cases, full instruction coverage,
2304 native footprints, signed-count and physical-alias checks preserve the
retail mask collisions, strict threshold and fresh count/global reads.
Only target changes across 6059 slots; protected sections/720 data owners and
all 10637 older guards unchanged. Counts: 3308/5462 total, 2635/4789 Game
exact, zero drift, 2154 different. README aggregates updated. Next: inspect
parent `func_1508B3F8`; full parent/FCSR/gameplay remains unqualified.

Record dispatcher direct match:
[Note 1020](WORKING_NOTES/1020-game-record-dispatcher-direct-match-20261005.md)
closes `func_15040CC8` across all 38 words, removing its overflow trampoline.
Integer record ABI plus divide-by-one index update retain retail's signed
index, three saves and frame 0x28; no divide, guards or profile override.
45 controls, 12288 three-way guest cases and full instruction coverage;
16 matching/native tests and 39 shared-oracle regressions pass, no skips.
Audit removes only the target overflow symbol: 16 later bodies shift by
-156 bytes with identical hashes; 13 trampolines only retarget their first
jump word. All other surviving slots/lengths and retail addresses intact.
Protected sections/720 data owners and all 10637 older guards unchanged.
Counts: 3307/5462 total, 2634/4789 Game exact, zero drift, 2155 different.
README aggregate tables updated; callback bodies/timing/gameplay unqualified.
Continue Game matching; 1508B2A8 is an 84-word recursive visitor placeholder.

Position/radius append direct match:
[Note 1019](WORKING_NOTES/1019-game-position-radius-append-direct-match-20261005.md)
replaces `func_1508B20C`'s false zero-return placeholder with all 39 words
emitting directly from semantic C. Signed count, post-increment, truncated
XYZ and squared radius preserve five fresh base reads and store order.
No guards, header/profile/assembly change. All 34 compiler controls complete;
nine qualification tests pass, including 8192 three-way guest cases,
252 bounded actual-caller cases and 65536 native cases. All 39 words covered.
Only target changes across 6060 slots; protected sections/720 data owners
and all 10637 older guards remain intact. Another 57 regression tests pass.
Counts: 3306/5462 total, 2633/4789 Game exact, zero drift, 2156 different.
README aggregate tables updated; full caller/FCSR/gameplay unqualified.
Continue Game matching; 15040CC8 needs a new saved-register/loop lifetime
shape, while the triangle read/frame boundary remains open under 1017.

Actor context dispatcher byte match:
[Note 1018](WORKING_NOTES/1018-game-actor-context-dispatcher-byte-match-20261005.md)
closes `func_15044380` across all 107 words. A per-visit enable pointer
recovers frame 0x68 / saved context +0x5C; 15 relocation-aware guards close
one complete allocation cycle, independent initialization schedule and
commutative add. Nineteen controls; 6184 three-way guest cases cover all
107 instructions. Nine matching tests pass, no skips. Only target changes
in 6060 slots; all protected sections and 720 data owners remain exact.
Counts: 3305/5462 total, 2632/4789 Game exact, zero drift, 2157 different.
README aggregate tables updated; helper-chain/gameplay acceptance not claimed.
Continue Game matching; triangle read/frame lifetimes remain open under 1017.
All 320 affected-slice tests pass in 57.212 seconds, no skips; tools,
whitespace and 2982 relative links pass. All 19 compiler controls reproduce.

Triangle cached-iterator audit:
[Note 1017](WORKING_NOTES/1017-game-actor-triangle-cached-iterator-audit-20261005.md)
banks 78 controls and 1914 bounded comparisons. Cached reads recover 1/1,
but lower raw scores require 0x150-0x160 frames; mixed bounds exceed the
slot. None is installed. Production, counts and README are unchanged.
Next Game target: `func_15044380`'s 107-word frame/register match.

Triangle reduced-frame recovery:
[Note 1016](WORKING_NOTES/1016-game-actor-triangle-reduced-frame-and-read-lifetime-screen-20261005.md)
reduces `func_1502F490` from frame 0x160 / 273 differences to 0x140 / 242.
All seven retail array homes remain intact; all 302 body/slot words emit
without new guards/profile/padding. Still non-matching: retail frame is
0x138, and the actor argument plus early ID/count read lifetimes differ.
Seventy-seven controls include 4488 bounded comparisons; scope-only forms
do not reduce the frame, and frame-only forms do not match the body.
64 focused tests and the five final frame probes pass, no skips; only target
changes in 6060 slots. Protected sections/data/CSV and README totals stay
intact. Next: last eight frame bytes, original read and SDK-loop lifetimes.
All 367 regression tests pass in 527.136 seconds, no skips; includes the
final read-history probe. Tools, staged whitespace and 2993 relative links
pass. This is not full read-lifetime/hardware or PC gameplay acceptance.

Triangle private-home recovery:
[Note 1015](WORKING_NOTES/1015-game-actor-triangle-private-home-recovery-20261005.md)
recovers all seven retail array homes by declaration-only changes. Installed
`func_1502F490` improves from 275 to 273 differences; 298 / 302 words, frame
0x160 still wrong versus retail 0x138. No array enlargement, added padding, guards
or profile change. Thirty-six declaration/loop controls include 1848 bounded
comparisons; oversized cursor forms are not installed. Only target changes
in 6060 slots; protected sections/data owners and CSV remain intact.
README/counts unchanged. Next: excess reserved homes and SDK-loop lifetimes
while retaining the now-correct array placement. Not a new exact function.
All 60 focused tests pass in 269.380 seconds; the 362-test regression corpus
passes in 818.122 seconds, no skips. Tools, staged whitespace and all 2983
checked relative links pass. Fresh live ELF agrees with the accepted slots.

Triangle lifetime/first-match audit:
[Note 1014](WORKING_NOTES/1014-game-actor-triangle-lifetime-and-overlapping-range-audit-20261005.md)
banks 34 controls; 29 fitting forms pass 1914 bounded guest comparisons.
Frames 0x148/0x138/0x130 alone do not recover retail allocation or fitting
length. An initialized-weight form has 274 differences but remains a
limited-qualified candidate, not an installed fix. The explicit overlapping-
range gate now passes and rejects last-match overwrites; native references
expand to 64512 plus 33 aliases. Production/README counts are unchanged.
Next: reserved homes and mixed scalar/array placement, preserving original
argument spills and separate early/SDK pointer lifetimes.
All 57 focused checks pass in 309.237 seconds, no skips; tools, whitespace
and 2981 links pass. All 6060 slots and protected sections/data owners stay
unchanged or retail-exact; the prior full corpus is not rerun in this audit.

Post-checkpoint triangle layout audit:
[Note 1013](WORKING_NOTES/1013-game-actor-triangle-layout-screen-20261005.md)
banks ten array/output-cursor forms and 120 bounded guest comparisons after
`623b96ae`. None improves the installed 298-word/frame 0x160/275-difference
transform. Reordering changes bytes, not these metrics; explicit XYZ cursors
grow to 308 words and are not installed. Production/README counts remain
unchanged. Next: actual spill/first-use lifetimes and edge/matrix-loop shapes.

Actor triangle remap: [Note 1012](WORKING_NOTES/1012-game-actor-triangle-remap-semantic-recovery-and-matrix-tail-restoration-20261005.md)
replaces `func_1502F490`'s placeholder with complete semantic C: 298 body /
302 slot words, frame 0x160, 275 differences; retail frame is 0x138.
The required 40-word matrix leaf is restored to original assembly, preserving
the retained tail's A0/T9/F0/F2/F4 interface. This is not a new C byte match.
All 53 focused tests pass; 1715 three-way guest cases, 57344 native reference
cases and 33 native aliases include actual phase/matrix/tail connections.
Only these two slots change in 6060; protected sections, 720 data owners and
CSV stay intact. Counts: 3304 / 5462 total, 2631 / 4789 Game, zero drift,
2158 different. Conversion falls by one when false C becomes retained ASM.
README aggregates updated. Next: transform frame/array/loop byte matching.
No full hardware-FPU/PC gameplay claim or sibling/frozen Release change.
All 355 combined tests pass in 829.704 seconds, no skips; tools, whitespace
and 2965 relative links pass. The C transform remains non-matching.

Actor buffer copy: [Note 1011](WORKING_NOTES/1011-game-actor-buffer-copy-direct-match-20261005.md)
recovers `func_1502F948`'s ordered gates, cached ID, allocation ABI and fresh
copy inputs. All 45 words / frame 0x28 emit directly under default IDO;
no guards or compiler override. Qualification covers 13461 three-way guest
cases, 163840 native reference cases and 16384 native gate cases, including
bounded actual allocator-wrapper/SDK-copy connections. Only target changes
in 6060 slots; protected sections, all 720 data owners and CSV remain intact.
Counts now 3304 / 5463 total, 2631 / 4790 Game, zero drift; README aggregates
updated. Caller remains 109 differences. Next: `func_1502F490`'s complete
302-word semantic recovery, not just its already-qualified early return.
Heap-core/full transform/PC gameplay acceptance is not claimed.
All 41 focused checks pass in 173.674 seconds; all 343 combined checks pass
in 690.045 seconds, no skips. Tools, whitespace and 2955 relative links pass.
Conversion/47 retained Init ASM and sibling/frozen Release remain unchanged.

Actor reference coordinate phase: [Note 1010](WORKING_NOTES/1010-game-actor-reference-coordinate-phase-match-20261005.md)
recovers `func_1502F3C8`'s 25-slot scan, five-argument transform call and fresh
post-call Y/bound comparison. All 50 words / frame 0x30 are linked exact;
default IDO has 16 differences closed by relocation-aware prelude/register/
schedule guards. Only target changes in 6060 slots; protected sections and
all 720 Game-data owners remain exact. Counts now 3303 / 5463 total,
2630 / 4790 Game, zero drift. README aggregates updated. Caller remains
109 differences; transform owner remains a placeholder. Full transform/FPU
exception/gameplay acceptance is not claimed. Next: `func_1502F948`.
All 30 focused checks pass in 99.051 seconds and all 332 combined checks
pass in 374.293 seconds, no skips. Tools, whitespace and 2941 relative links
pass; conversion/Init ASM and sibling/frozen Release remain unchanged.

Actor pass lifetime audit: [Note 1009](WORKING_NOTES/1009-game-actor-pass-lifetime-audit-and-helper-handoff-20261005.md)
banks 176 reproducible compiler controls without changing production. None
improves `func_1502BEE4`'s 109 differences; correct stack homes or 176-word
length alone do not prove the retail schedule. Twenty focused checks pass in
47.471 seconds, no skips, including 48 new bounded guest comparisons.
README aggregates and linked baseline remain unchanged. Next: recover the
connected 50-word `func_1502F3C8` phase helper; caller matching remains open.

Game actor pass layout progress: [Note 1008](WORKING_NOTES/1008-game-actor-pass-array-layout-and-connected-selector-20261005.md)
reduces `func_1502BEE4` from 115 to 109 differing words, with 175 body / 176
slot words and frame 0x88. Depth/queue arrays now match SP+0x3C/SP+0x58 and
queue-count spill matches SP+0x38; maximum-depth spill remains SP+0x78, not
retail SP+0x34. No new guards/profile override. Nineteen focused checks pass,
including 400 new connections to the already-exact selector and dispatcher,
1171 total three-way cases and 16384 native reference cases. Only target
changes in 6060 slots; protected sections and patch CSV remain intact.
Counts stay 3302 / 5463 total, 2629 / 4790 Game, zero drift. README aggregates,
conversion/Init ASM and sibling/frozen Release unchanged. Next: remaining
maximum-depth spill, address lifetimes and retail instruction schedule.
All 321 combined checks pass in 289.549 seconds, no skips; tools and
whitespace checks pass. The function remains non-matching at 109 words.
All 2934 checked relative documentation links resolve.

Game actor update pass semantic recovery: [Note 1007](WORKING_NOTES/1007-game-actor-update-pass-semantic-recovery-and-captured-order-20261005.md)
replaces `func_1502BEE4`'s placeholder with live mask/activity scans,
predecessor-depth capture and stable ordered updates. It is not byte-exact:
174 body / 176 slot words, frame 0x88, 115 differences, no new guards/profile
override. All 771 three-way cases, including 257 actual connected dispatcher
cases, and 16384 native independent-reference cases pass. All 176 retail words
execute; wrong-shift/recheck controls fail and cyclic-prefix checks preserve
retail nontermination/wrapping. Seventeen pass/dispatcher focused checks pass,
no skips. Only target changes in 6060 slots; previous exact recoveries and
patch table stay intact. Rebuild: 3302 / 5463 overall, 2629 / 4790 Game, zero
drift. Conversion/47 Init ASM functions, README aggregates and sibling/frozen
Release unchanged. Next: finish this caller's stack layout and scheduling.
All 319 combined checks pass in 305.557 seconds, no skips; protected sections,
tools, whitespace and 2927 relative links pass.
After banking `981ec732`, eight further local-storage controls pass 64
boundary cases but do not improve the match. Eighteen focused checks pass
in 39.427 seconds; production remains unchanged at 115 differences.

Game actor update dispatcher direct recovery: [Note 1006](WORKING_NOTES/1006-game-actor-update-dispatch-direct-match-and-carried-slot-abi-20261005.md)
recovers `func_1502BD84`, all 88 words / frame 0x20 directly under default
IDO, no guards/profile override. Callee inspection recovers the carried slot
argument to `func_1502EEF4`; the missing-slot negative control now fails the
ABI-aware fixture. All 5194 full three-way cases, 49152 native cases/two native
mutations and 48 actual callee prefixes pass. Nine focused tests, no skips.
Prefixes stop before the callee loop; full gameplay/update acceptance remains
separate. Only target changes in 6060 audited slots. Rebuild: 3302 / 5463
overall, 2629 / 4790 Game, zero drift. Protected sections/tools pass; patch
table, conversion/47 Init ASM functions and sibling/frozen Release unchanged.
README aggregates updated. All 311 combined checks pass in 257.161 seconds,
no skips; whitespace/relative links pass. Next: `func_1502BEE4`, 176-word
caller placeholder.

Game actor display-list scan recovery: [Note 1005](WORKING_NOTES/1005-game-actor-display-list-scan-match-and-live-callback-state-20261005.md)
recovers `func_1502BAD0`, all 173 words / frame 0x48. Default IDO emits the
semantic scan; eleven expected-word guards normalize a closed constant-register
cycle and equality operand order only. All 4868 three-way target cases and
194123 native cases pass, including signed alpha gates, live callback state,
full table/cursor chains and SDK packets. Thirteen focused tests pass, no skips.
All 172 reachable words execute; a retained dead load is proved unreachable
and byte-exact. Only target changes across 6060 slots; placeholder helpers/
callers remain unchanged, not qualified as full renderers. Rebuild: 3301 / 5463
overall, 2628 / 4790 Game, zero drift. Protected sections/tools/whitespace pass;
README aggregates updated. Conversion/47 Init ASM functions and sibling/frozen
Release unchanged. All 302 combined regression checks pass in 265.481 seconds,
no skips; touched relative links resolve. Next: `func_1502BD84`, 88-word actor
update dispatcher.

Game resource-size query direct recovery: [Note 1004](WORKING_NOTES/1004-game-resource-size-query-direct-match-and-aligned-header-20261005.md)
recovers `func_1502B9B4`, all 69 body / 71 slot words and frame 0x68
directly under default IDO O2/g3, no guards/profile override. Three-u64
scratch, incoming descriptor at entry SP-0x14, both aligned-header choices
and live full-word DMA header result are preserved. Native qualification
uses positive descriptor-writing paths and explicit MIPS u64 alignment only.
All 5670 boundary, 972 actual lookup/cache, 384 native connected and 72
Init caller prefixes pass. The latter stops before bank load; full audio
startup is not claimed. Caller declaration aligned and all 214 slot words
stay retail-exact. All 6060 slots audited: only target changes.
Rebuild: 3300 / 5463 overall, 2627 / 4790 Game, zero drift.
Protected sections/tools/whitespace/links pass. All 272 combined checks
pass in 239.593 seconds, no skips.
README aggregates updated; conversion/Init ASM, patch table and sibling/
frozen Release unchanged. Next: `func_1502BAD0`, 173-word / frame 0x48
25-actor display-list routine in `game/generated_58F80.c`.

Game counted-pointer resource loader direct recovery: [Note 1003](WORKING_NOTES/1003-game-counted-pointer-loader-direct-match-and-full-caller-20261005.md)
recovers `func_1502B7F0`: all 60 words / frame 0x48 directly from default
IDO O2/g3, no guards/profile override. A for-loop update resolves the final
two store schedules. Private size, incoming descriptor at entry SP-0x14,
post-block output-home reread and final pointer-store/size-reload aliases
remain intact; native cases use positive descriptor-writing paths only.
All 1470 boundary, 162 actual-callee, 72 connected global-alias and 432 full
Game caller cases pass. Shared variadic declaration and sole active caller's
cast are aligned; its complete 112-word slot stays exact, including original
unsigned division/fallback behavior. All 6060 slots audited: only target
changes. Rebuild: 3299 / 5463 overall, 2626 / 4790 Game, zero drift.
Protected sections/tools/whitespace pass. All 261 combined checks pass in
217.336 seconds, no skips.
README aggregates updated; conversion/Init ASM, patch table and sibling/frozen
Release unchanged. Next: `func_1502B9B4`, size-query wrapper with compressed
header read and stack-phase-dependent alignment, 69 body words / frame 0x68.

Game optional-size resource loader direct recovery: [Note 1002](WORKING_NOTES/1002-game-optional-size-loader-direct-match-and-live-output-aliases-20261005.md)
recovers `func_1502B5C8` from its zero-return placeholder. All 61 words / frame
0x50 emit directly under default IDO O2/g3, no guards/profile override. The
incoming descriptor at entry SP-0x18 remains separate from the initialized-one
fallback at SP-0x10. Zero-depth seeds, live output/descriptor rereads and
distinct allocation-failure sizes are preserved; native tests qualify positive
descriptor-writing paths only, not defined native indeterminate-local behavior.
All 2940 boundary, 324 actual-callee, 72 connected global-alias and 108 full
Game caller cases pass. Six caller declarations/casts are aligned and complete
retail-exact slots/frames remain unchanged. Protected Init code/data, Debugger
code and Game data remain exact. All 247 final checks pass in 246.404 seconds,
no skips; tools/whitespace pass. Rebuild: 3298 / 5463 overall,
2625 / 4790 Game, zero drift. README aggregates updated; conversion/Init ASM,
patch table and sibling/frozen Release unchanged. Next: `func_1502B7F0`,
60 words / frame 0x48: stores a pointer through its first argument but returns
the separate size, unlike its obsolete commented void approximation.

Game buffer variadic wrapper direct recovery: [Note 1001](WORKING_NOTES/1001-game-buffer-variadic-wrapper-direct-match-and-incoming-descriptor-frame-20261005.md)
recovers `func_1502B8E0` from its zero-return placeholder. All 53 words / frame
0x48 emit directly under default IDO O2/g3, no guards/profile override. The
physical incoming descriptor at wrapper-entry SP-0x14 remains seed-sensitive
on zero depth; this preserves target instructions, not defined native C.
Native cases use positive depths with descriptor-writing lookup only.
All 2268 boundary, 600 actual-callee, 14 connected zero-depth and 48 full Game
caller cases pass; eight mismatch prefixes stop at the original syscall.
Both maintained caller slots/frames remain exact after prototype alignment;
`func_150169A0` is still a placeholder, so its assembly is reference-only.
Protected Init code/data, Debugger code and Game data remain exact.
All 232 final checks pass in 178.769 seconds, no skips; tools/whitespace pass.
Rebuild: 3297 / 5463 overall, 2624 / 4790 Game, zero drift.
README aggregates updated; conversion/Init ASM, patch table and sibling/
frozen Release unchanged. Next: `func_1502B5C8`, 61 words / frame 0x50,
including its optional size-output aliases and unwritten zero-depth descriptor.

Game caller-buffer resource-loader direct recovery: [Note 1000](WORKING_NOTES/1000-game-caller-buffer-resource-loader-direct-recovery-and-syscall-boundary-20261005.md)
recovers `func_1502B224` from its zero-return placeholder. All 75 words / frame
0x30 emit directly under default IDO O2/g3, no guards/profile override. Cap
rounding, raw DMA, compressed header capture/live scratch and retained decode
count are preserved. Native/boundary/600 actual-callee caller cases pass;
40 mismatch-prefix cases stop at the real handwritten syscall boundary.
Returning error hooks qualify only conditional continuation, not trap recovery.
All 221 final checks pass in 161.605 seconds, no skips; protected Init
code/data, Debugger code and Game data remain exact.
Rebuild succeeds: 3296 / 5463 overall, 2623 / 4790 Game, zero drift. README
aggregates updated; conversion/Init ASM, patch table and sibling/frozen Release
unchanged. Next: `func_1502B8E0`, 53 words / frame 0x48, retaining its verified
zero-depth incoming-frame descriptor dependency rather than initializing it away.

Game variadic table-address resolver recovery: [Note 999](WORKING_NOTES/999-game-variadic-table-address-resolver-recovery-and-connected-init-caller-20261005.md)
recovers `func_1502B020` from its zero-return placeholder. All 60 linked words
match with frame 0x48 and two checked independent loop-store guards, not a
direct compiler match. SDK argument consumption, initialized-one zero-depth
behavior and final output-store/descriptor-read order remain intact. Boundary,
actual lookup/cache hit/miss and connected retail Init sound-caller cases pass;
the latter covers 42/43 reachable caller words without faking an impossible
size-zero/nonzero-address result. Both Init callers use the recovered variadic
prototype; full rebuild retains Init exactness. All 210 final checks pass in
172.769 seconds, no skips; both caller slots and protected Init code/data,
Debugger code and Game data remain exact. Totals: 3295 / 5463 overall,
2622 / 4790 Game, zero drift. README aggregates updated; conversion/Init ASM
and sibling/frozen Release unchanged. Next: resource loader `func_1502B224`,
75 words / frame 0x30, including compressed-length mismatch handling.

Game variadic table-range wrapper recovery: [Note 998](WORKING_NOTES/998-game-variadic-table-range-wrapper-recovery-and-guarded-loop-stores-20261005.md)
recovers `func_1502B110` from its zero-return placeholder. All 69 linked words
match with retail's 0x48 frame and two checked independent loop-store guards;
raw C differs at those two stores only, no profile override. SDK varargs,
default root, descriptor masking/gates and unconditional final consumption
remain intact. All 8316 boundary and 200 actual-callee three-way cases pass,
alongside 1386 native boundary and 544 actual-C connected cases. Full consumer
rebuild succeeds. All 199 final checks pass in 148.664 seconds, no skips;
protected Init code/data, Debugger code and Game data remain exact.
Totals: 3294 / 5463 overall, 2621 / 4790 Game, zero drift.
README aggregates updated; conversion/Init ASM unchanged. Sibling/frozen
Release untouched. Next: recover SDK-varargs table-address resolver
`func_1502B020`, 60 words / 0x48 frame, with optional output alias gates.

Game table-range loader direct recovery: [Note 997](WORKING_NOTES/997-game-table-range-loader-direct-recovery-and-caller-qualification-20261005.md)
replaces `func_1502AF04`'s false zero-return placeholder with its semantic
DMA/in-place pair-offset body. All 71 words and the 0x40 frame emit directly
under default IDO O2/g3, no guards/profile override. Safe call-argument shape
avoids a rejected raw-exact unsequenced read/write trial. All 6336 native,
12672 instruction and 60 connected retail-wrapper cases pass; both stack
phases and buffer alignment/unsigned wrap contracts hold. All 190 final
checks pass, no skips, with protected sections exact after rebuilding.
Totals: 3293 / 5463 overall, 2620 / 4790 Game, zero drift. README aggregates
updated; conversion/Init ASM and patch table unchanged. Sibling/frozen Release
untouched. Next: recover variadic table-range wrapper `func_1502B110`,
69 words / 0x48 frame, retaining SDK varargs and descriptor-length gating.

Game cached lookup guarded match: [Note 996](WORKING_NOTES/996-game-cached-lookup-frame-and-guarded-miss-path-match-20261005.md)
matches all 159 linked `func_1502AC88` words. Address-parameter lifetime and
declaration order recover the full body, retail 0xA0 frame and exact cache-hit
path. Raw C still differs at twelve miss-path words; checked guards normalize
closed temporaries and equivalent buffer roundup on an 8-aligned N64 stack.
All 11088 three-way connected cases preserve ordered memory/call events and
returns; native 1056-case hit aliases and every omitted-guard control pass.
All 183 final combined checks pass, no skips; protected-section identity holds
after the full consumer rebuild. Totals: 3292 / 5463 overall, 2619 / 4790 Game,
zero drift. README aggregate tables updated; conversion/Init ASM unchanged.
Sibling/frozen Release untouched. Next: recover `func_1502AF04`'s 71-word
DMA table-range loader and in-place offset adjustment from its placeholder.

Game cache installer guarded match: [Note 995](WORKING_NOTES/995-game-cache-installer-alias-preserving-word-copy-and-guarded-match-20261005.md)
matches all 97 linked `func_1502AB04` words with the alias-preserving one-word
offset copy and 41 expected-word guards. Not a direct compiler match: raw C
fits the full slot and 0x28 frame but has 41 differences. Seven peel guards,
four bulk address-allocation guards and thirty bulk schedule/register guards
preserve all branches/calls and normalize only independent stores between
identical reads. All 2550 new three-way cases and every omitted-guard control
pass. The native partial-overlap rejection and 833-alias corpus remain intact.
All 176 final combined checks pass, no skips, with complete Init/Debugger/data
identity after the full consumer rebuild. Totals: 3291 / 5463 overall, 2618 / 4790 Game,
zero drift. README aggregate tables updated; conversion/Init ASM unchanged.
Sibling/frozen Release untouched. Next: cached lookup `func_1502AC88`,
158 / 159 body/slot words, 156 raw differences, 0xA0 frame in both forms.

Game cache installer frame recovery: [Note 994](WORKING_NOTES/994-game-cache-installer-frame-recovery-and-pair-copy-alias-gate-20261005.md)
recovers `func_1502AB04`'s complete 19-word prologue and 0x28 frame by preserving
an explicit count local across `bcopy`. Scalar pair copies remain intact.
Production still differs: 87 / 97 body/slot words, 74 differences instead of
93, no guards/profile change. The 128-form screen finds a raw-exact two-word
aggregate copy, but it fails a native partial-overlap witness and is rejected.
All 171 final combined checks pass, no skips; 833 bounded native aliases and
2550 three-way instruction traces preserve live reads and final cache memory.
The alias-preserving one-word-copy trial
fits 97 words with 41 differences but remains experimental. Exact/conversion
totals unchanged; README aggregate tables remain current. Sibling/frozen
Release unchanged. Next: qualify the word-copy scheduling differences or find
a directly matching scalar/word shape without weakening the alias contract.

Game block loader direct match: [Note 993](WORKING_NOTES/993-game-block-loader-direct-output-size-and-frame-match-20261005.md)
matches all 86 `func_1502B350` words directly under the unchanged default
IDO O2/g3 profile, including retail's 0x30 frame. Output-size expression shape,
explicit failure branches and one size local resolve all 78 prior differences;
no guards, profile override or interface changes. The 37-form / 296-trial
screen reproduces the match; all 165 combined checks pass, no skips.
Connected resource fixtures and complete Init/Debugger/data identity hold.
Totals: 3290 / 5463 overall, 2617 / 4790 Game, zero drift. Neighboring
relocator/variadic loader remain exact. README aggregate tables updated;
conversion/Init ASM and sibling/frozen Release unchanged. Next: 97-word
cache installer `func_1502AB04` (87 body words, 93 differences, frames 0x20/0x28).

Game offset relocator guarded match: [Note 992](WORKING_NOTES/992-game-offset-relocator-typed-scan-and-guarded-bulk-match-20261005.md)
matches all 72 linked `func_1502B4A8` words with a typed automatic-count scan
and seventeen checked bulk temporary-register guards. Not a direct compiler
match: raw C has seventeen differences, no frame or padding; the 186-form
screen finds no direct match. All 161 combined checks pass, including 5113
three-way relocation cases and every omitted-guard rejection control.
Full consumer rebuild and complete Init/Debugger/data identity hold.
Totals: 3289 / 5463 overall, 2616 / 4790 Game, zero drift; conversion/Init ASM
unchanged. The 77-word variadic loader remains directly exact. README aggregate
tables updated; sibling/frozen Release unchanged. Next: 86-word block loader
`func_1502B350` (77 body words, 78 differences, C/retail frames 0x38/0x30).

Game variadic loader direct match: [Note 991](WORKING_NOTES/991-game-variadic-resource-loader-direct-stack-match-20261005.md)
matches all 77 words of `func_1502B6BC`, including retail's 0x50 frame,
nullable-output prologue and private descriptor at sp+0x38. Separate fallback
selection and local declaration order resolve all seventeen differences
directly from C, with no guards/profile/interface changes. The 83-form screen
reproduces the result; all 155 combined checks pass, no skips, with actual
variadic/connected source fixtures and complete Init/Debugger/data identity.
Totals: 3288 / 5463 overall, 2615 / 4790 Game, zero drift; conversion/Init ASM
unchanged. README aggregates updated; no host/frozen Release change. Next:
72-word offset relocator `func_1502B4A8` (65 body words, 71 raw differences).

Game attachment guarded match: [Note 990](WORKING_NOTES/990-game-attachment-walker-guarded-register-match-20261005.md)
matches the complete 45-word linked `func_15168E54` slot with nine expected-word
guards for a closed cursor/opcode allocation and equality operand order.
Unguarded C still differs at nine words; production source/profile are unchanged.
Thirty-six source forms do not directly match. All 154 combined checks pass,
including 1427 actual-leaf three-way traces, twenty mutation cases, 458752
native command cases and incomplete-allocation rejection controls. Full consumer
rebuild succeeds; complete Init/Debugger/data and recent direct matches hold.
Totals: 3287 / 5463 overall, 2614 / 4790 Game, zero drift; conversion/Init ASM
unchanged. README updated; sibling already has this retail sequence, no host/
frozen Release change. Next: 77-word variadic loader `func_1502B6BC`.

Game resource helper match: [Note 989](WORKING_NOTES/989-game-resource-helper-address-word-direct-match-20261005.md)
completes all 46 words of `func_151336A8` directly from C. The inline unsigned
O32 address-word cast restores retail's final `v1`/`a1` handoff, without guards,
profile or public-interface changes. Three new checks reproduce nineteen source
forms and pin raw slot/neighbor identities. All 148 combined checks pass,
including actual resource/texture connections; complete Init/Debugger/data hold.
Totals: 3286 / 5463 overall, 2613 / 4790 Game, zero drift; conversion/Init ASM
unchanged. README aggregates updated. Sibling already has this retail-sequence
helper; no host/frozen Release changes. Next near-match: `func_15168E54`.

Game immediate release match: [Note 988](WORKING_NOTES/988-game-immediate-texture-release-direct-frame-match-20261005.md)
completes all 46 words of `func_1510D7AC` directly from table-indexed C.
The captured signed priority remains; default O2/g3 now emits retail's 0x28
frame and ID spill/reload. No guards/profile/padding changes. A 51-variant
screen and three regression checks pin partial-frame rejection controls and
five unchanged neighboring spans; the existing full lifecycle suite retains
callback mutation and connected release/maintenance/reload qualification.
All 65 final combined checks pass, no skips; complete Init/Debugger/data stay exact.
Totals: 3285 / 5463 overall, 2612 / 4790 Game, zero drift; conversion and Init
ASM counts unchanged. README aggregate snapshot updated. Sibling still has
a placeholder, no host/frozen Release changes. Next near-match: `func_151336A8`.

Game cleanup rematch: [Note 987](WORKING_NOTES/987-game-nullable-cleanup-typed-pointer-direct-rematch-20261005.md)
restores `func_150F631C`'s complete nineteen-word direct C match. Typed pointer
fields recover four register/scheduling words against the current callee
prototype, with no guards or profile change. Five new checks cover 343 native
callback cases, an independent integer-field rejection control, raw retail
identity and six unchanged neighbors. Fresh totals: 3284 / 5463 overall,
2611 / 4790 Game, zero drift; conversion counts and Init ASM unchanged.
All 62 combined checks pass, complete Init/Debugger/data stay exact. README
aggregate snapshot updated; sibling/frozen Release unchanged. Next near-match
is the four frame/spill words in `func_1510D7AC`; light-selector gate stays open.

Game light-selector experiment: [Note 986](WORKING_NOTES/986-game-light-selector-candidate-fitting-and-connected-frame-witness-20261005.md)
recovers full fourteen-argument `func_1515D914` as experimental C. No-unroll
O2/g3 fits 2212 body / 2224 complete bytes in the 2404-byte slot, versus
default 2444 / 2448. All three profiles pass 17410 standalone pairs each;
192 retail-derived native cases and 168 caller-relative seed products hold.
However, twelve actual caller/callee witnesses expose the C renderer's
0xB8 versus retail 0x98 frame: a first directional light reads a different
physical seed, changes count 1 to 3 and moves the final cursor sixteen bytes.
Positional-first controls agree. All 109 final combined checks pass, no skips;
complete existing Init/Debugger/data remain exact. Keep the production stub.
Resolve connected stack lifetime before adoption; helper algorithms, hardware
and pixels remain open. README totals and sibling/frozen Release unchanged.

Init bitmap unsigned sentinel: [Note 985](WORKING_NOTES/985-init-bitmap-unsigned-one-past-record-fitting-20261005.md)
tests one-past unsigned stop arithmetic with ordered scalar and grouped-record
captures. No-unroll record C fits nineteen body words with no XOR, but sixteen
positions differ; store remains in the branch delay instead of the increment.
Whole text stays 80 bytes. Initial scalar read reversal is caught and fixed
experimentally with volatile views, at three words' cost. Fourteen new checks
qualify 1098 completed pairs and eighteen prefixes, including a wrapped zero
stop and a false-empty rejection control. All 154 combined checks pass, no skips;
48 old preprocessing selections and complete existing Init/data plus Game data
hold. No production adoption, README total or sibling/frozen Release change.

Init pause-resume decision: [Note 984](WORKING_NOTES/984-init-pause-resume-current-conversion-readiness-20261005.md)
freshly confirms 492 C / 47 ASM entries: seventeen investigation targets and
thirty intentional boot/SDK/hardware/context owners. No replacement is ready
for production adoption. Bitmap fits nineteen body words but differs at seventeen;
MMIO fits eleven but differs at nine O2/g3 or eight O1 words. Current connected
decoder is freshly reproduced at 4496 / 3984 bytes, 512 over; best formatter
connection remains 608 / 412, 196 over. Entry/frame/placement/stack gates remain.
All 140 fresh focused and byte-depth identity checks pass, no skips; complete
existing Init code/data and Game data remain exact. Bitmap loop/tail is the
first small target. Paused Game experiments, production owners, README totals
and sibling/frozen Release stay unchanged; this is not a production relink.

Game renderer: [Note 983](WORKING_NOTES/983-game-viewport-renderer-semantic-recovery-20261005.md)
recovers full `func_1510B9D0`, its public cursor/s16 interface and legacy caller
casts. C fits 347 / 356 words; frame 0xB8 versus retail 0x98, 343 differences,
no guards/profile override. Fourteen new checks qualify 5379 paired traces,
including 96 actual helper/updater/color/identity connections, 4608 native cases
and four invalid prefixes. Captured suppression/actor and late base/page/table
reloads hold under mutations. All 95 final combined checks pass in 52.200 seconds,
no skips, after shared-header rebuild/link; complete existing Init/Debugger/data
and caller/adjacent identities hold. Downstream transform/finalizer/effect
placeholders and submission/pixels remain open. README totals, Init owners and
sibling/frozen Release unchanged. Next full target: 601-word `func_1515D914`.

Game command helper: [Note 982](WORKING_NOTES/982-game-viewport-command-helper-semantic-recovery-20261005.md)
replaces `func_1510B7B4`'s placeholder with its complete twelve-packet SDK body.
It emits 103 / 105 words with two padding NOPs, no frame/calls/guards/profile
override; 104 raw differences remain. Twelve new checks qualify 65600 native
cases, 97 complete ordered retail/C traces and three invalid-input prefixes.
Late page/base/table aliases retain repeated reads; a cached-page control fails.
All 81 combined checks pass in 19.953 seconds, no skips, after fresh owner build,
padding and link. Complete existing Init/Debugger/data remain exact. README
totals and sibling/frozen Release unchanged. Note 983 above subsequently recovers
full renderer `func_1510B9D0`; these fixtures do not prove submission or pixels. Init still
has 47 ASM owners, seventeen investigation targets and thirty intentional.

Init bitmap grouped view: [Note 981](WORKING_NOTES/981-init-bitmap-record-view-fitting-and-ordered-read-qualification-20261005.md)
tests direct/local volatile record addressing for the captured start/end and
late signed count. Optimized body fits nineteen words while retaining the
two-based mask, but seventeen differ: XOR loop and original schedule remain
unresolved. Complete standalone text stays 80 bytes after alignment. Ten new
checks qualify 1002 completed ordered retail/C traces and twelve bounded prefixes,
including aliases, wrapping model addresses and unused-field read rejection.
All 138 final combined checks pass in 70.804 seconds, no skips; complete existing
Init slots/code/data and Game data remain retail-exact. All 44 old-shape host/
guest preprocessing selections hold. No original-type provenance or production
adoption is inferred. README, production sources and host/Release unchanged.

Init packed-width fitting: [Note 980](WORKING_NOTES/980-init-packed-bit-width-screen-and-restored-candidate-20261005.md)
screens a wide bit-count local and both packed fields on the byte-depth lead.
Optimized public builder saves one/three words, but trailing alignment absorbs
them: complete C/adapter allocation stays 4496 bytes. Both profiles gain eight
bytes of builder frame and call bound. Reject before semantic qualification;
restore the candidate exactly, no selector or test-code change retained.
All 83 fresh restored connected/native/owner/slot/call/reporting checks pass in
345.010 seconds, no skips. Complete existing Init code/data and Game data remain
retail-exact. Note 979's unchanged candidate retains its full masked corpus
evidence; discarded trial images receive none. Still 512 bytes over, with
entry/frame/private-stack/hardware gates open. Production, README and host/Release unchanged.

Init byte-depth full corpus: [Note 979](WORKING_NOTES/979-init-byte-depth-full-masked-cu1-corpus-qualification-20261005.md)
qualifies the banked packed O2/g3 candidate across all 507 retail pages in each
masked CU1 mode: 1014 paired runs pass in 1604.214 seconds, no skips. Both
terminals report 4496 executable bytes, 3248 descent and 80-byte known-neighbor
clearance; this is not private-stack reservation proof. The instruction hash,
allocation and eight during-run source hashes hold. After receipt verification,
reporting-only failure gates and two mocked controls are added; all 32 supporting
checks pass in 1.483 seconds, no skips. The full corpus is not repeated for
that reporter-only change. No production adoption: still 512 bytes over retail,
with original entry/frame/placement, reservation and hardware gates open.
Init remains 492 C / 47 ASM: seventeen investigation targets, thirty intentional
owners. README totals, production sources and host/Release stay unchanged.

Init MMIO fitting: [Note 978](WORKING_NOTES/978-init-mmio-record-view-fitting-and-ordered-access-qualification-20261005.md)
tests a new volatile record view of the adjacent RAM publications. Direct
record text saves sixteen bytes versus the fully volatile scalar control in
three profiles, but still has nine O2/g3 or eight O1 word differences. Explicit
locals regress O1 to seventeen words/eight-byte frame. Nine new checks qualify
sixty ordered retail/C traces with no external reads and rejection controls for
store order, width and added reads. Retain the handwritten assembly; grouped
addressing is not original-type provenance or a closed register/schedule match.
Production declarations, owners, README totals and host/Release stay unchanged.
All 128 combined checks pass in 66.503 seconds, no skips; complete existing
Init slots/code/data and Game data remain retail-exact. No production relink
or hardware acceptance is claimed.

Init bitmap fitting: [Note 977](WORKING_NOTES/977-init-bitmap-all-ones-mask-fitting-and-retail-loop-boundary-20261004.md)
adds an opt-in unsigned all-ones mask and arithmetic control. The mask variant
fits nineteen optimized body words but has seventeen raw differences; IDO
rematerializes the constant, keeps the XOR loop and changes the retail tail.
Standalone optimized text stays 80 bytes: alignment absorbs the body word.
Reject adoption: this is size fitting, not a scheduling-only match. Nine new
checks qualify 1002 completed retail/C pairs and twelve prefixes; all 119
combined checks pass, no skips. Forty disabled-selector preprocessing checks
confirm unchanged Shapes 1..20. All existing Init slots/code/data and Game
data remain exact. Production owners, README totals and host/Release unchanged.
Next bitmap work must address the direct branch/increment delay and original
two-based tail, not another mask-only substitution. MMIO remains next small target.

Remaining Init decision: [Note 976](WORKING_NOTES/976-init-remaining-conversion-decision-and-decoder-cache-matrix-20261004.md)
retains 47 ASM owners: seventeen investigation targets and thirty intentional
boot/SDK/hardware/context routines. No replacement is ready. The new sixteen-
case byte-depth cache matrix improves neither complete text nor stack; a
persistent parent-mask recurrence grows O2 by 32 bytes and worsens O1 stack.
The recurrence source/selector are removed and banked source contents restored.
Best qualified decoder remains 4496 / 3984 bytes (512 over, actual adapter
included). Bitmap remains 20 / 19 words, MMIO full eleven-word match unresolved,
formatter connection 196 bytes over. Details and concrete adoption gates live
in the dedicated note. Fresh 78 decoder/owner/slot/call and 43 bitmap/MMIO/
formatter checks pass, no skips; all existing Init code/data and Game data
remain retail-exact. README totals and production owners stay unchanged.

Init byte-depth fitting: [Note 975](WORKING_NOTES/975-init-builder-byte-depth-induction-and-rejected-replication-helpers-20261004.md)
qualifies an opt-in byte-offset builder depth. Both packed profiles save sixteen
complete executable bytes: optimized C 4320 + actual 176-byte adapter = 4496,
512 over retail. Builder public/region is 330 / 398 words, frame 200, unchanged
400-byte core call bound and 3248 total descent. All 58 connected/native tests
plus twenty separate inventory/slot/call checks pass, no skips; ordered physical
table publications and both disabled packed hashes are checked. Aligned-end O2
grows sixteen bytes, so no default change. Two out-of-line replication helpers
regressed text/stack and were removed before semantic qualification. Production
Init remains 492 C / 47 ASM, all raw slots/full existing Init/data exact; no
README aggregate, production relink, full corpus, hardware or host/Release claim.
Next: another 512 complete bytes plus entry/frame/private-stack ownership.

Init decoder fitting: [Note 974](WORKING_NOTES/974-init-decoder-complement-low-mask-fitting-trial-20261004.md)
adds an opt-in complemented shared-mask expression. Two instruction words
change, but complete optimized text stays 4336 C + 176 adapter = 4512 bytes,
528 over retail. All 59 connected/native/ledger checks pass across two runs, no skips;
20 separate inventory/slot/call checks and tool checks pass. Default packed
instruction hashes remain intact; all 47 production ASM slots and complete
existing Init code/data plus Game data remain exact. The builder's 401-word
region contains a 333-word public unit and 68 embedded-helper words; next
sustained Init fitting is builder/shared-call structure and whole-image costs.
No adoption, production relink, full guarded corpus, README aggregate change,
sibling/Release change or hardware/gameplay acceptance is claimed.

Palette updater: [Note 973](WORKING_NOTES/973-game-palette-updater-and-connected-color-qualification-20261004.md)
recovers `func_1510CB10`: 168 / 170 words, retail 0x68 frame, 135 raw differences,
no guards/profile override/drift. Fourteen new checks qualify 398353 native cases,
1251 complete paired traces and three invalid-slot prefixes. Actual angle-helper/
updater/color/writer connections pass; captures, late reloads, byte-wrap-before-
clamp and both phase stores are retained. All 257 combined checks pass, no skips;
fresh source compile/padding/link preserves complete Init code/data, Debugger
code, Game data and previous identities. README aggregates unchanged. Next
full caller `func_1510B9D0` (356 words) is subsequently recovered in Note 983;
Note 982 recovers command helper `func_1510B7B4` (105-word slot).
Full renderer/RSP/RDP/natural effects and matching stay open.
Sibling already has updater plus gated diagnostics; no host/Release changes.

Palette color emitter: [Note 972](WORKING_NOTES/972-game-palette-color-emitter-byte-match-and-segment-connection-20261004.md)
finishes the interrupted `func_1510CDB8` recovery: all 42 words match directly
from actual SDK macros, frameless, no guards/profile override/drift. Six added
tests cover 262144 native alpha cases, 812 complete paired big-endian traces
and three invalid-index prefixes; actual color -> writer connections pass.
The complete module records 1710 paired traces. All 243 combined checks pass,
no skips, after forced source compile/padding/link/progress/matcher; complete
Init code/data, Debugger code and Game data remain exact. Total 3283 / 5463,
Game 2610 / 4790 exact, 2180 different, zero drift. README changes matching
aggregate rows only. Note 973 above subsequently recovers palette updater
`func_1510CB10` and qualifies its bounded color/writer connection.
Full render caller/RSP/RDP/natural effects and staged producer remain open.
Sibling already has the original emitter; no host/frozen Release changes.

Requested Init pause resume: [Note 971](WORKING_NOTES/971-init-pause-resume-remaining-assembly-decision-20261004.md)
latest recheck starts from clean banked HEAD `36b67c92` and freshly passes
110 focused checks in 63.319 seconds, no skips. Init remains
492 C / 47 ASM entries (12252 ASM bytes); every retained owner/raw slot and
complete existing Init code/data plus Game data remain retail-exact. Seventeen
entries are investigation targets, thirty intentional assembly. No replacement
is ready: best freshly checked bitmap is 20 / 19 words, decoder 528 bytes over,
formatter 196 over; MMIO's full eleven-word C match remains unresolved.
No new compiler hypothesis or production relink is claimed. Historical
interrupted Game edits are now banked by Notes 972 and 973; no source edits
were pending at this resume. Next requested Init work is a new bitmap
branch/delay-slot fitting hypothesis, followed by justified MMIO scheduling
or connected decoder fitting, not another broad conversion batch.
Production Init, README aggregates and sibling/frozen Release unchanged.

Queued segment writer: [Note 970](WORKING_NOTES/970-game-queued-segment-writer-and-big-endian-alias-qualification-20261004.md)
recovers `func_1510D8C0` using the SDK macro: 40 / 44 words, frameless,
38 raw differences, no guards. Ten new tests connect actual reset/append/write;
898 paired big-endian instruction traces qualify data/store order, byte aliases,
unsigned segments and cached/late count reads. Every body instruction is covered.
Counts above eight use extended fixtures only, not real queue-safety acceptance.
All 237 combined checks pass, no skips; fresh link preserves exact queue helpers,
complete Init code/data, Debugger code, Game data and previous identities.
Sibling writer is already recompiled; no host/Release change. Next direct render
dependency was 42-word color emitter `func_1510CDB8`; Note 972 above completes
its source recovery and bounded writer connection.
Raw matching, full caller/rendering and staged producer remain open. README unchanged.

Immediate texture release: [Note 969](WORKING_NOTES/969-game-immediate-texture-cache-release-recovery-20261004.md)
recovers `func_1510D7AC` from its zero-return stub. All 46 words fit; 42 match
directly, with four frame/spill differences (C 0x38 versus retail 0x28).
No guards. Six new tests cover all 65536 priority/activity byte pairs, all 7762
IDs, staged callback ordering and actual resolver/retain/release/maintenance/
reload. All 227 combined checks pass, no skips; fresh link preserves full
Init code/data, Debugger code, Game data and prior identities. The sibling's
active immediate-release body remains a zero-return stub; host synchronization
and real allocator/DMA/decoder/gameplay are separate. Note 970 subsequently
recovers queued segment writer `func_1510D8C0`; staged producer and matching remain open.
README aggregates, production Init and frozen Release unchanged.

Texture metadata and maintenance: [Note 968](WORKING_NOTES/968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md)
finishes the interrupted `func_15003570` / `func_1510D404` recoveries: 58 / 62
and 125 / 129 words, 54/119 raw differences, no new guards. Maintenance's C
frame is 0x40 against retail 0x60. Seventeen new checks qualify bounded metadata,
all signed priorities/work counters, callback ordering and the actual connected
cache lifecycle. All 221 combined checks pass, no skips; fresh link retains full
Init code/data, Debugger code, Game data and exact initializer/startup slots.
The two pending edits described by Notes 966/967 are now qualified and banked.
Actual guest DMA/decoder, staged producer, hardware diagnostics and natural
effects remain separate. Note 969 subsequently recovers 46-word immediate cache
release `func_1510D7AC`. README aggregates and sibling/frozen Release stay unchanged.

Init decoder fitting: [Note 967](WORKING_NOTES/967-init-decoder-entry-value-lifetime-fitting-trials-20261004.md)
tests literal/length, distance and combined immutable table-value capture.
Two variants save one optimized compressed-decoder word, but trailing alignment
absorbs it: optimized packed images retain 4336 C bytes plus 176 adapter bytes,
4512 executable against 3984 retail. Reject adoption; the gap remains 528 bytes. All 151 trial
checks and twenty ownership/section audits pass, no skips; three final size
reruns verify padding attribution. Default instruction images remain unchanged;
full linked Init code/data and Game data stay exact. No production Init/README
changes; Game metadata/maintenance was separate and uncommitted at that
checkpoint, subsequently qualified by Note 968 above.

Requested Init resume: [Note 966](WORKING_NOTES/966-init-resume-preincrement-bitmap-and-conversion-decisions-20261004.md)
rechecks 492 C / 47 ASM entries after the interrupted build finishes. All 110
focused checks pass, no skips; every retained owner/raw slot and full Init
code/data plus Game data remain exact. New preincrement bitmap emits 32/20/32
words across O2/no-unroll/O1, against nineteen retail; 501 completed model pairs
and six prefixes pass, but the best form has an extra bias and wrong delay-slot
schedule. Reject adoption. Seventeen investigation targets and thirty intentional
ASM owners remain; decoder is 528 bytes over, connected formatter 196 over.
Pending Game metadata/maintenance edits built but were not behavior-qualified or
banked by that Init checkpoint; Note 968 resolves their bounded source gates.
README totals and production Init are unchanged.

Texture setup/resolution/attachment: [Note 965](WORKING_NOTES/965-game-texture-resource-setup-resolver-and-attachment-recovery-20261004.md)
recovers `func_1510CE60`, `func_1510D0EC` and `func_15168E54`: 152 / 163,
155 / 162 and 45 / 45 words, with 159/142/9 differences and retail frame sizes.
No new guards. Sixteen new tests connect actual helper/setup/resolver/attachment
and release, including all 7762 valid IDs, signed priorities, allocation failures,
cleanup ordering and aliases. All 204 combined checks pass, no skips; fresh link
retains full Init code/data, Game data, exact leaves and prior recoveries. Setup's
first unwritten scratch paths remain unqualified. Note 968 subsequently recovers
expanded-size metadata loader `func_15003570` (62 words) and cache maintenance
`func_1510D404` (129 words), qualifying the bounded connected lifecycle.
Actual guest DMA/decompression and natural effects remain open.
README/sibling/Release unchanged.

Remaining Init decision refresh: [Note 964](WORKING_NOTES/964-init-remaining-assembly-current-conversion-decisions-20261004.md)
confirms 492 C / 47 assembly entries (12252 ASM bytes) after the fresh production
link. All 102 focused checks pass, no skips; every retained ASM slot and complete
Init code/data plus Game data remain retail-exact. Seventeen investigation
targets remain, thirty owners stay intentional assembly. No candidate is ready:
decoder executable is 528 bytes over, best connected formatter 196 over, and
neither small leaf has a complete match. Start with a new bitmap compiler-shape
hypothesis; no broad Init conversion batch or README aggregate change.

Asset cache and block loading: [Note 963](WORKING_NOTES/963-game-asset-table-cache-lookup-and-block-load-recovery-20261004.md)
recovers cache installer `func_1502AB04`, lookup `func_1502AC88` and block loader
`func_1502B350`: 87 / 97, 158 / 159 and 77 / 86 words, with 93, 156 and 78 raw
differences, no new guards. Fourteen new tests qualify cache ordering, metadata,
allocation/decode-result semantics and the actual lookup/block/variadic/relocation
connection. All 188 combined checks pass, no skips; fresh link retains full
Init code/data, Game data, prior recoveries and exact callers. Note 962's unwritten
lookup metadata gate is now resolved in source. Note 965 subsequently recovers
setup/attachment and their resolver; Note 968 resolves metadata loading and
bounded cache lifecycle. Guest DMA/decompression, byte matching and natural
effects remain separate gates.
No sibling/Release changes. README counts remain unchanged.

Variadic resource loader: [Note 962](WORKING_NOTES/962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md)
recovers `func_1502B6BC` and relocation helper `func_1502B4A8`. The loader fits
all 77 words / retail 0x50 frame, 17 raw differences; relocation fits 65 body
words in 72, 71 differences. No new guards. Typed variadic caller interfaces
preserve three complete exact caller slots. Fourteen new tests connect actual
constructor/helper/loader/relocation and other callers; all 174 combined checks
pass, no skips. Fresh link preserves full Init code/data, Game data and prior
recoveries. At that checkpoint lookup `func_1502AC88` (159 words) and block loader
`func_1502B350` (86 words) still had placeholders; Note 963 subsequently recovers
both; Note 965 recovers deeper setup/attachment and the texture resolver. Actual
guest loading and zero-depth/negative-depth calls remain unqualified. Metadata
loading/cache maintenance source and bounded lifecycle gates are resolved by
Note 968; PC child synchronization and natural effects remain open. README unchanged.

Extended child constructor: [Note 961](WORKING_NOTES/961-game-extended-child-constructor-and-resource-helper-recovery-20261004.md)
recovers `func_1513264C` and `func_151336A8` from their placeholders. Bodies
fit 255 / 256 and 45 / 46 words, with 184 and nine raw differences, no guards.
The pointer wrapper remains fifteen-word exact. Fifteen new tests connect the
actual child/constructor/resource helper; all 160 combined checks pass, no skips.
Fresh link preserves complete Init code/data, Game data and prior recoveries.
Its loader gate is subsequently recovered by Note 962 and lookup/block bodies
by Note 963; Note 965 recovers deeper `func_1510CE60` / `func_15168E54` and their
resolver; Note 968 resolves metadata and bounded cache lifecycle. PC
synchronization and natural effects remain open; retained Init assembly and
README aggregates are unchanged.

Extended child callback: [Note 960](WORKING_NOTES/960-game-extended-child-emission-semantic-recovery-20261004.md)
recovers code-0x37 `func_150E93DC`, its 124-byte descriptor and typed pointer
wrapper. C fits 206 body words / 0x138 frame in the 208-word slot, with 200
raw differences and no guards. The wrapper remains exact across fifteen words.
Thirteen new tests and all 145 combined checks pass, no skips; fresh link
preserves complete Init code/data, Game data and prior recoveries. Retail's
28-byte extra payload and descriptor holes remain unspecified. Constructor
`func_1513264C` was still a placeholder at that checkpoint; its body and resource
helper are subsequently recovered by Note 961. PC synchronization and natural effects
remain separate gates. Init assembly and README aggregates are unchanged.

Init decoder fitting: [Note 959](WORKING_NOTES/959-init-decoder-packed-parent-and-bit-tail-fitting-trials-20261004.md)
tests new opt-in parent packing and shared-refill/inline bit-tail shapes.
Optimized complete images grow to 4528 and 4544 bytes, so reject both; the
retained 4512-byte candidate remains 528 bytes over retail. All 105 connected
trial checks plus twenty baseline audit/ledger checks pass, no skips.
Default-option instruction images remain unchanged; full existing Init code/data
and Game data stay exact. No production adoption or README aggregate change.
Next fitting work must reduce the complete image and resolve entry/stack ownership.

Requested Init resume: [Note 958](WORKING_NOTES/958-init-resume-remaining-assembly-readiness-20261004.md)
freshly verifies 492 C / 47 assembly entries, all retained owners/slots and
complete existing linked Init code/data and Game data. All 102 checks pass,
no skips. Seventeen entries remain investigation targets; thirty established
boot/hardware/context/SDK owners stay assembly. No replacement is ready to
adopt: decoder remains 528 bytes over, best connected formatter 196 over,
and small leaves lack complete retail matches. Older bitmap forms do fit
nineteen words but remain non-matching. Init source and README unchanged;
the separate Game child placeholder is not edited by this assessment.

Extended weighted emitter: [Note 957](WORKING_NOTES/957-game-extended-weighted-emitter-semantic-recovery-20261004.md)
recovers `func_150E9178`'s complete code-0x36 body and 60-byte child payload.
C fits all 153 words / 0xF8 frame, with 54 differences and no guards. Eleven
new tests connect the real creator and all four actual position-writer modes;
all 132 combined tests pass, no skips. Fresh link preserves full Init code/data,
Game data, exact neighbors and prior recoveries. README aggregates unchanged.
The PC source still has an emitter stub, so synchronization is separate. Next
recover code-0x37 child `func_150E93DC` (208 words); this historical placeholder
gate is subsequently resolved by Note 960. Its constructor and downstream/
gameplay qualification remain open.

Game child-emission callback: [Note 956](WORKING_NOTES/956-game-child-emission-callback-recovery-and-fitting-20261004.md)
finishes `func_150E8D5C` and its typed pointer interfaces. Two flag shifts resolve
the interrupted 225-word build failure: C fits 219 words / 0x120 frame in the
224-word slot, with 213 raw differences and no guards. Fresh relink preserves
complete Init code/data, Game data and exact constructor/wrappers/helpers.
Thirteen new tests qualify the actual child/wrapper/spherical bodies and parent
payload connection; all 121 combined tests pass, no skips. Child-placeholder
and fitting gates are resolved in source
and tests, not gameplay; README aggregates unchanged. The sibling PC source
still has a zero-return child stub, so host synchronization remains open.
Its sibling `func_150E9178` is subsequently recovered by Note 957; downstream
rendering and byte matching remain separate tasks.

Init bitmap right-shift trial: [Note 955](WORKING_NOTES/955-init-bitmap-fill-value-right-shift-mask-trial-20261004.md)
tests reusing `0xFF` for the final mask. IDO rematerializes the constant and
retains XOR: 20 optimized words against nineteen retail. Eight new tests
qualify 501 completed model pairs/six prefixes; 34 combined tests pass, no skips.
Reject adoption; Init ownership, existing exact code/data and README unchanged.
Older nineteen-word one-based-mask forms also exist but do not match retail.
Its subsequent Game-child fitting recovery is completed by Note 956.

Init resume: [Note 954](WORKING_NOTES/954-init-resume-conversion-decision-and-interrupted-game-build-20261004.md)
confirms 492 C / 47 assembly entries (12,252 retained bytes). All retained
owners/slots and the existing ELF's complete Init code/data and Game data are
exact. Ninety-three focused tests plus one freshly compiled decoder size check
pass, no skips. Two small leaves remain candidates, but no replacement is ready
to adopt; decoder is still 528 bytes over, and connected glyph fitting/ownership
remain open. Thirty boot/hardware/SDK owners stay assembly. README unchanged.
Its interrupted Game build then failed at 225 words against 224; that gate is
now resolved by Note 956's fitted child, chain tests and fresh production link.

Game descriptor-position writer: [Note 953](WORKING_NOTES/953-game-descriptor-position-writer-and-weighted-chain-recovery-20261004.md)
restores all four `func_1514470C` modes and the void interface. Semantic C fits
179 words / 0x78 frame in the 218-word slot, with 196 raw differences and no
guards. Eleven new tests connect the actual weighted caller/writer/helpers;
all 100 combined tests pass. Fresh relink preserves complete Init code/data,
Game data and exact neighbors; sibling already has its recompiled writer.
The uninitialized-position placeholder gate is resolved in source/tests, not
accepted gameplay. Its child callback `func_150E8D5C` is subsequently recovered
by Note 956 and sibling `func_150E9178` by Note 957. Matching totals/README unchanged.

Init address-difference trial: [Note 952](WORKING_NOTES/952-init-bitmap-address-difference-induction-trial-20261004.md)
tests a new unsigned subtraction/zero-branch shape for `func_10005BE0`.
IDO removes XOR but introduces a second induction variable: 22 O2 words
against nineteen retail. Eight new tests qualify 501 pairs/six bounded prefixes;
93 combined Init tests pass. Reject adoption; all retained owners and linked
Init code/data/Game data remain exact, README totals unchanged. Next broader
semantic recovery remains the pending Game emitter's position-writer dependency.

Init resumed assessment: [Note 951](WORKING_NOTES/951-init-resume-conversion-readiness-and-repeatable-audit-20261004.md)
freshly verifies 492 C / 47 assembly and all retained raw linked slots.
Two small leaves remain C candidates; ten decoder and five diagnostic entries
need connected recovery, while thirty original boot/hardware/SDK owners stay
assembly. Seven new audit checks, 78 retained contract/compiler tests and 46
freshly compiled decoder tests pass: 131 across three runs, no skips. Best
decoder remains 4512 bytes against 3984 retail; glyph path is also oversized.
Full existing Init code/data and Game data are exact. No Init replacement is
ready to adopt; production ownership and README totals stay unchanged.

Game weighted emitter: [Note 950](WORKING_NOTES/950-game-weighted-event-emitter-semantic-recovery-20261004.md)
recovers `func_150E8B1C`'s complete code-0x33 weighted emission body. It fits
144 words and the original 0xC8 frame, but 44 words differ; no guards added.
Eighty-two tests and fresh link pass; full Init/Game data and exact neighbors
are preserved. Aggregates/README unchanged. Its then-placeholder position
writer is now restored by Note 953 and child callback `func_150E8D5C` by Note 956.
Downstream/runtime gates remain, so the actual guest pipeline is not qualified.

Game event payload creators: [Note 949](WORKING_NOTES/949-game-event-payload-creators-and-connected-dispatch-match-20261004.md)
finishes the preserved `func_150E8A80` and `func_150E90DC` edits. Both match
all 39 words directly, original 0x48 frames, no guards; actual dispatcher/timer
chains cover head mutations, failures, payload snapshots and extra RNG draws.
Seventy-two tests and fresh production link pass; Init, Game data and exact
neighbors remain intact. Game 2609 / total 3282 exact, zero drift. README
matching rows updated; next inspect `func_150E8B1C` and its updater contract.

Init bitmap equality-exit trial: [Note 948](WORKING_NOTES/948-init-bitmap-equality-exit-lifetime-trials-20261004.md)
tests cursor-address versus captured-end masks inside the equality exit.
Both remove XOR but emit 21 optimized words against nineteen retail, adding
an unconditional back edge and second return. Eight new tests / 1,002 pairs
and twelve bounded prefixes pass; all 78 combined tests pass. Reject both.
Production Init ownership,
README totals and the two unfinished Game edits remain unchanged.

Init remaining assembly: [Note 947](WORKING_NOTES/947-init-remaining-assembly-conversion-map-20261004.md)
maps all retained entries and confirms 492 C / 47 assembly, 12,252 ASM bytes.
All retained owners/slots and complete existing linked Init code/data remain
retail-exact; seventy focused tests pass. Bitmap/MMIO are small C candidates,
not qualified adoptions; decoder/glyph need connected fitting and ownership.
README totals stay unchanged. Two unfinished Game creator/test edits remain
preserved separately; this assessment does not qualify or commit them.

Game event/packet/sound dispatch: [Note 946](WORKING_NOTES/946-game-event-packet-and-sound-dispatch-direct-match-20261004.md)
recovers `func_150E8930`, all 84 words directly matching with original 0x38
frame and no guards. Its corrected no-argument call preserves all 28 timer
caller words. Sixty-five tests and fresh link pass; complete Game data, Init
sections and neighboring exact owners remain intact. Game 2607 / total 3280
exact, zero drift; README matching rows updated. Next recover `func_150E8A80`,
then `func_150E90DC`; both list-triggered creators are still placeholders.

Game world-emitter dispatch: [Note 945](WORKING_NOTES/945-game-world-emitter-dispatch-direct-byte-match-20261004.md)
recovers `func_150E81A8`'s selected world position, descriptor and random packet.
All 129 words match directly from C, original 0x90 frame, no guards. Fifty-nine
tests and a fresh production relink pass. Full Game data and Init code/data
stay exact, as do both curves and all three adjacent assembly owners. Game
2606 / total 3279 exact, zero drift; README matching rows updated. Next semantic
target is the verified `func_150E8930` placeholder; Init ownership unchanged.

Init bitmap exit-edge trials: [Note 944](WORKING_NOTES/944-init-bitmap-exit-edge-control-flow-trials-20261004.md)
tests separate-final-store and taken-edge-increment forms. The latter removes
XOR but adds an entry jump: twenty words, still over nineteen retail. Eight
new / 54 combined tests pass; 1,002 new paired executions and twelve bounded
prefixes qualify alias/wrap traces. Reject both for production; Init owners
and README totals unchanged. Game `func_150E81A8` remains the next actionable
semantic recovery under the broader decomp goal.

Init resume assessment: [Note 943](WORKING_NOTES/943-init-resume-linked-baseline-and-conversion-shortlist-20261004.md)
confirms 492 C / 47 assembly entries and the current production ELF's complete
164,048 code / 17,376 data bytes retail-exact, including all retained slots.
Sixty-two focused tests pass. Bitmap/MMIO remain the two small C candidates;
none is ready to adopt. Decoder remains 528 linked bytes over retail, and
connected glyph fitting/ownership remain open. Latest requested work is Init
assessment; the pending Game placeholder is separate. README totals unchanged.

Game physical data repair: [Note 942](WORKING_NOTES/942-game-physical-data-order-and-literal-pool-restoration-20261004.md)
restores retail owner order, four missing pools and the table's no-padding
assembly profile. Fresh full link succeeds; all 189,088 physical Game-data
bytes / 720 owners match retail. Pan coefficient is correct at 0x800A1350.
Fifty-three tests pass; Init code/data remain exact and both curves retain
194/212 direct matches. Aggregate counts unchanged. The earlier layout/build
gate is resolved statically; guest gameplay acceptance is still separate.
Next semantic target: `func_150E81A8`'s verified zero-return placeholder.

Init unsigned-induction trials: [Note 941](WORKING_NOTES/941-init-bitmap-unsigned-induction-guest-qualification-20261004.md)
reject two new bitmap shapes: unsigned equality is byte-identical to the
20-word pointer control; countdown emits 22 words against nineteen retail.
Eight new / 46 combined tests pass, including 1,002 completed retail/C pairs
and twelve bounded prefixes with alias/fence rejecting controls. Production
Init ownership/counts remain unchanged. Its then-open Game link gate is now
resolved by Note 942; the rejected bitmap forms are not production conversions.

Init pause-resume decision: [Note 940](WORKING_NOTES/940-init-pause-resume-conversion-decision-20261004.md)
recounts 492 C / 47 assembly entries and verifies all retained source owners.
Fifty-four focused tests pass, including fresh connected formatter trials.
Bitmap/MMIO remain the smallest C candidates; no replacement is ready to adopt.
Decoder is still 528 linked bytes too large; glyph fitting/ownership remain open.
Preserved pre-edit ELF Init code/data matched all retail bytes. Note 942 now
also verifies a successfully rebuilt production ELF with exact Init sections.

Game curve update: [Note 939](WORKING_NOTES/939-game-curve-update-direct-match-and-data-placement-gate-20261004.md)
recovers `func_150E7C9C` and confirms the payload cursor. All 212 words emit
directly from C, original 0xA8 frame, no guards; builder remains 194/194 exact.
Thirty-two focused tests pass, including the actual builder/update/helper chain.
Fresh matcher Game 2605 / total 3278 exact, zero instruction address drift.
**Layout gate resolved by Note 942:** the displaced coefficient is restored to
0x800A1350 with value 0x3EDCEE77, and the complete data image is exact.
Instruction/data matching still does not establish guest gameplay acceptance.

Game random curve record: [Note 938](WORKING_NOTES/938-game-random-curve-record-direct-byte-match-20261004.md)
recovers `func_150E7994`'s packet, allocator, metadata and sampled curve body.
All 194 words emit directly from C, with original 0xC8 frame and no guards.
Twenty-six focused tests pass; fresh link has no drift. Game 2604 / total
3277 exact, 2186 different. README matching rows updated; conversion counts
unchanged. Next inspect `func_150E7C9C`; Init production ownership unchanged.

Game random edge emitter: [Note 937](WORKING_NOTES/937-game-random-edge-emitter-semantic-recovery-20261004.md)
replaces `func_150E76D0`'s placeholder with its four-variant descriptor builder.
Twenty-one focused tests pass, including both actual dispatcher/helper paths.
Body 155 / slot 177 words, original 0xB0 frame, 171 differences, no guards/drift.
Semantic recovery, not a byte match; aggregates unchanged. Next inspect
adjacent placeholder `func_150E7994`; Init production owners remain unchanged.

Init split-validation trial: [Note 936](WORKING_NOTES/936-init-split-destination-validation-interface-trial-20261004.md)
tests a one-cell/scalar-return setup interface. O2 624 text / 64 stack and
O1 720 / 56 do not improve the independent controls. All 1,728 paired fixtures
and sixteen combined tests pass. Keep assembly production owners; pick up
Game alternate emitter helper `func_150E76D0` from Notes 924/925 next.

Init shared setup trial: [Note 935](WORKING_NOTES/935-init-shared-formatter-setup-text-stack-tradeoff-20261004.md)
saves sixteen linked bytes, but increases nested stack: O2 608 bytes / 80
stack, O1 688 / 56. All 1,152 paired fixtures and sixteen combined tests pass.
Helper measurement is call-target guarded. Retain opt-in only; fitting and
ownership gates remain open, production counts unchanged.

Init connected C formatters: [Note 934](WORKING_NOTES/934-init-connected-semantic-c-formatters-and-layout-cost-20261004.md)
recovers both formatter bodies calling the C writer directly. Two profiles /
576 paired fixtures and fifteen combined tests pass, including string/output
alias timing. O2 allocated text is 624 versus 412 connected retail bytes;
both profiles descend 48 bytes. Fitting/adapter/ownership remain open.

Init glyph adoption boundaries: [Note 933](WORKING_NOTES/933-init-glyph-adapter-production-placement-and-stack-boundaries-20261004.md)
pins nine inherited-stack and six overlay-stack diagnostic formatter sites.
Experimental C address is occupied by `func_10008F90`; no adjacent leaf-slot
extension is free. Overlay frame containment is conditional, not ownership.
Twenty focused tests pass; retain adapter as experimental, no conversion.

Init glyph adapter: [Note 932](WORKING_NOTES/932-init-connected-glyph-c-adapter-qualification-20261004.md)
qualifies the C writer through real formatter callers: 280 connected plus
five direct-leaf pairs, seven new / twenty combined tests pass. Adapter fits
the 120-byte leaf slot, but combined allocated text is 248 bytes and stack
descent is 56 bytes. Production placement/stack ownership remain open.

Init glyph fitting: [Note 931](WORKING_NOTES/931-init-glyph-pixel-seeding-and-countdown-fitting-20261004.md)
reduces the ordinary-ABI semantic writer from 31 to 29 words using low-halfword
pixel seeding and countdown loops. Eight variants / 2,128 paired fixtures pass;
sixteen combined tests plus a separate footprint check pass. Body fits, but
connected adapter/stack/layout and byte matching remain open. No conversion.

Init semantic glyph trial: [Note 930](WORKING_NOTES/930-init-semantic-glyph-writer-differential-qualification-20261004.md)
qualifies three compiled profiles against retail ordered memory operations
and bounded aliases: 798 paired fixtures, sixteen combined tests pass.
Smallest body is 31 words against 30 retail, before adapter cost; O1 uses a
32-byte frame. ABI adapter, fitting and ownership remain open. No conversion.

Init connected formatters: [Note 929](WORKING_NOTES/929-init-connected-glyph-formatter-contracts-20261004.md)
executes interior destination setup, both formatter callers and real glyph
writer. Pins null-buffer return links, all signed-byte mappings and hex
delay-slot predecrement/cursor effects. Five new / twenty-four combined tests
pass. Semantic C/alias and adapter qualification remain open; no conversion.

Init glyph contract: [Note 928](WORKING_NOTES/928-init-glyph-writer-register-and-pixel-contract-20261004.md)
pins `func_10007D28`'s nonstandard register inputs, two-destination ordered
8x8 pixel writes, 0x248 row stride and sixteen-byte cursor result. All 262
rendering fixtures / four new tests pass; nineteen combined tests pass.
Connected formatter/interior-entry qualification and adapter work remain open.
No production conversion or aggregate change.

Init unsigned-range bitmap trials: [Note 927](WORKING_NOTES/927-init-bitmap-unsigned-range-comparison-trials-20261004.md)
reject two new bounded-buffer predicate shapes. Both still emit twenty O2
words against nineteen retail; `sltu` replaces XOR without solving schedule.
Eleven shapes / 869 host fixtures and 33 retained-contract tests pass.
Production owners, aggregate counts and README remain unchanged.

Init readiness refresh: [Note 926](WORKING_NOTES/926-init-remaining-assembly-readiness-refresh-20261004.md)
recounts 492 C / 47 assembly routines, with 151,796 / 12,252 bytes. Bitmap
and MMIO remain small C candidates, not production-ready replacements.
Qualified decoder is 528 linked bytes too large; reservation, entry/frame and
hardware/context gates remain open. All 38 focused tests pass, no skips.
Ordered next steps are in the note; no source conversion or README change.

Game positioned emitter descriptor: [Note 925](WORKING_NOTES/925-game-positioned-emitter-descriptor-recovery-20261004.md)
recovers `func_150E75A0`'s initialized descriptor fields, submission and result
propagation. Callee's 0x58-byte copy pins extent; unwritten padding/tail stay
unwritten. Six new tests / sixteen combined pass, including real dispatcher/
helper integration. Body 74 / retail 76 words, 69 differences, no guards/drift.
Aggregate counts unchanged; alternate helper `func_150E76D0` remains a placeholder.

Game random dispatcher: [Note 924](WORKING_NOTES/924-game-probability-gated-random-dispatch-recovery-20261004.md)
recovers both `func_150E7290` branches and shared sound/command/packet tail.
Five new tests / fifteen combined pass. Production has 195 body words in its
196-word slot, 183 differing positions, original 0x68 frame and no guards/drift.
Adjacent helper call ABIs are typed, but their bodies remain placeholders.
Three preceding exact slots stay exact; aggregate counts/README unchanged.

Game fixed/random parameters: [Note 923](WORKING_NOTES/923-game-fixed-random-parameter-initializer-match-20261004.md)
recovers `func_150E71E4`'s vector-derived value, three fixed fields and four
random samples. All 43 words match directly from C, no guards. Five new tests
/ fourteen combined pass; fresh matcher Game 2603 / total 3276 exact, zero
drift. README aggregate rows updated; detailed behavior remains in the note.

Game vector random parameters: [Note 922](WORKING_NOTES/922-game-vector-random-parameter-initializer-match-20261004.md)
recovers `func_150E70EC`'s two vector-derived values and six sampled fields.
All 62 words match directly from C without guards, including square-root
intrinsic and ordered publication. Five new tests / fourteen combined pass;
fresh matcher Game 2602 exact / total 3275, zero drift. README rows refreshed.

Game linked-record exit trials: [Note 921](WORKING_NOTES/921-game-linked-record-position-exit-layout-trials-20261004.md)
tests five exit shapes across four profiles; none matches retail. Return/goto
variants retain the 71-word shared-RA tail under O2/g3; O1 emits 89 words.
All twenty host shape/test runs pass. Production's 15 differences and all
aggregate counts remain unchanged; retained driver makes the trials reproducible.

Game linked-record matching refinement: [Note 920](WORKING_NOTES/920-game-linked-record-position-stack-and-float-shape-20261004.md)
reduces `func_150E6FAC` from 38 to 15 differing positions by restoring local
declaration order and float operand source shape. All 57 non-branch words
before the return tail match directly; thirteen tests pass. Still 71 body
words versus 72 retail, no guards/drift. Return-tail layout remains open.

Game linked-record position: [Note 919](WORKING_NOTES/919-game-linked-record-position-semantic-recovery-20261004.md)
replaces `func_150E6FAC`'s zero-return placeholder with lookup, randomized
radius/angle offsets and fallback coordinates. Five new tests / thirteen
combined pass; independent IDO body fits. Production has 71 body words in
the original 72-word slot, 38 differing positions, zero guards and no drift.
This is semantic recovery, not a new exact match; README totals unchanged.

Init bitmap qualifier/sentinel trials: [Note 918](WORKING_NOTES/918-init-bitmap-store-qualifier-and-sentinel-trials-20261004.md)
reject nonvolatile stores (20 O2 words, unchanged from control) and an
end-plus-one sentinel (33 O2 words, 20 with unrolling disabled), against
nineteen retail words. Nine shapes pass 711 host fixture combinations;
33 retained-contract tests pass. No production conversion or aggregate change.

Game random range position: [Note 917](WORKING_NOTES/917-game-random-range-position-recovery-and-match-20261004.md)
recovers `func_150E6F18` as a direct 37-word C match without guards. Unsigned
six-pointer selection, pointer capture before float RNG, field reads after
that call and sequential overlapping output are preserved. Fourteen focused
tests pass; fresh matcher Game 2601 exact / total 3274, zero drift.
Init remains 492 C / 47 assembly; the qualified decoder is still 528 bytes
too large, with reservation, entry/frame ownership and hardware gates open.

Game position sound adapter: [Note 916](WORKING_NOTES/916-game-object-position-sound-adapter-and-init-return-contract-20261004.md)
recovers `func_1509F6E8`'s nullable lookup, truncated coordinates and handle
forwarding as a direct 37-word C match. Corrected Init `func_10010F88` u16
return remains exact across 29 words; complete Init code/data remain retail.
Thirteen tests pass; fresh matcher Game 2600 exact / total 3273, zero drift.
README aggregate rows updated; unrelated actor/timeline work remains unstaged.

Game status record reset: [Note 915](WORKING_NOTES/915-game-status-record-reset-recovery-and-match-20261004.md)
finishes `func_151E5034` as semantic C: sixteen selected zero stores with
retail pointer reloads. All 37 linked words match directly, no guards; nine
focused tests pass. Fresh ELF/matcher: Game 2599/4790 exact, total 3272/5463,
zero drift. Conversion totals unchanged; README aggregate rows refreshed.
Unrelated actor/timeline work remains uncommitted and excluded from this recovery.

Init dynamic fitting trials: [Note 914](WORKING_NOTES/914-init-rejected-dynamic-symbol-and-header-gate-fitting-20261004.md)
rejects symbol-before-drop (no text saving, O2 core bound +40) and encoded
header mask gate (O2 core text +16). All 16384 header predicates agree, but
neither fitting result improves the candidate. Qualified source restored
exactly; fifteen focused checks pass. Current linked 4512 / 528 excess unchanged.

Init distance operation O2 CU1-set corpus: [Note 913](WORKING_NOTES/913-init-distance-operation-o2-full-masked-cu1-set-corpus-20261004.md)
passes all 507 guarded paired pages in 818.478 seconds, no skips. With Note
912, both masked CU1 modes qualify 1014 paired runs for this fixed candidate:
text 4512, descent 3248, low `0x80031D60` / margin 80, hashes unchanged.
Twenty-two supporting checks pass. Next: fitting (528 excess), reservation,
entry/frame ownership and hardware/context; production/README unchanged.

Init distance operation O2 CU1-clear corpus: [Note 912](WORKING_NOTES/912-init-distance-operation-o2-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 guarded paired pages in 826.726 seconds, no skips. Text 4512,
descent 3248, minimum SP `0x80031D60` / margin 80 confirm Note 911's saving;
six candidate hashes hold. Twenty-two supporting tests pass. Matching CU1-set
corpus, fitting (528 excess), reservation and production gates remain open.

Init distance operation local: [Note 911](WORKING_NOTES/911-init-distance-operation-local-fitting-20261004.md)
retains an opt-in distance entry operation snapshot: packed O2 linked text
4512, sixteen saved / 528 excess; descent remains 3248. O1 complete size
unchanged. Bounded run: 45 passes / one corpus skip; separate backreference
storage guard passes. Default text identical; changed full corpora and
fitting/reservation/production gates remain open. README unchanged.

Init bitmap value-lifetime trials: [Note 910](WORKING_NOTES/910-init-bitmap-shared-fill-mask-lifetime-trials-20261004.md)
rejects a shared fill/mask variable (same 20-word O2 text as control) and
postdecrement variant (22 words), versus retail nineteen. Seven shapes pass
553 host fixture combinations; 33 retained-contract tests pass, no skips.
Experiments remain reproducible; production ownership and totals unchanged.

Init resume readiness: [Note 909](WORKING_NOTES/909-init-resume-conversion-readiness-audit-20261004.md)
recounts 492 C / 47 assembly functions and verifies all remaining assembly
source owners. All 38 focused checks pass, no skips. Bitmap/MMIO matching
remains open; the qualified dynamic-order decoder is 544 bytes too large,
with reservation/ownership/hardware gates open. No production conversion or
README aggregate change. The note provides the current ordered work list.

Init startup thread contract: [Note 908](WORKING_NOTES/908-init-startup-thread-stack-top-and-constructor-contract-20261004.md)
executes pinned call preparations and retail constructor. Stack tops
`0x8002D8B0` / `0x800318B0`, saved SP top-minus-sixteen; constructor writes
end at object +0x130, but later +0x230 FPR footprint remains protected.
Private-gap sentinels and executed crossing-store controls pass; 25 combined
tests pass. This strengthens neighbor evidence, not full reservation ownership.

Init replication deficit trials: [Note 907](WORKING_NOTES/907-init-rejected-builder-replication-span-deficit-trials-20261004.md)
rejects entry-unit and byte-unit remaining-span loops: both grow O2 core text
32 bytes and call bound sixteen; O1 also grows. Source restored exactly,
17 focused retained-builder/size/ledger tests pass. Qualified dynamic-order
candidate remains 4,528 linked / 544 excess; production and README unchanged.

Init dynamic order O2 CU1-set corpus: [Note 906](WORKING_NOTES/906-init-dynamic-order-o2-full-masked-cu1-set-corpus-20261004.md)
passes all 507 guarded paired pages in 836.723 seconds, no skips. With Note
905, both masked CU1 modes cover 1,014 paired pages for this unchanged
candidate. Text 4,528, descent 3,248, low `0x80031D60`, margin 80 and hashes
match. Fitting (544 excess), reservation and production/hardware gates open.

Init dynamic order O2 CU1-clear corpus: [Note 905](WORKING_NOTES/905-init-dynamic-order-o2-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 guarded paired pages in 835.460 seconds, no skips. Text 4,528,
descent 3,248, low `0x80031D60`, known-neighbor margin 80 confirm Note 904's
tradeoff; six recorded hashes fixed. Matching CU1-set corpus remains open,
along with fitting (544 excess), reservation and production/hardware gates.

Init dynamic order cursor: [Note 904](WORKING_NOTES/904-init-dynamic-order-cursor-text-stack-tradeoff-20261004.md)
retains an opt-in initializer countdown: packed O2 text 4,528 (32 saved,
544 excess) at eight more stack bytes; O1 text grows sixteen. Whole bounded
suite 45 passes / one corpus skip; 192 all-count prefix runs and separate
alignment/ledger checks pass. Default text exact. Changed-candidate full corpora
and production gates remain open; qualified baseline remains Notes 901/902.

Init bitmap return-lifetime trials: [Note 903](WORKING_NOTES/903-init-bitmap-return-value-lifetime-trials-20261004.md)
tests returning the advanced cursor or captured end + 1. Both retain the XOR
loop and grow optimized bodies to 21 words versus retail 19. Host behavior
and return checks pass; 33 retained-contract tests pass. No production match
or signature change; qualified pointer-owned decompressor remains unchanged.

Init pointer-owned O2 CU1-set corpus: [Note 902](WORKING_NOTES/902-init-pointer-owned-o2-full-masked-cu1-set-corpus-20261004.md)
passes all 507 guarded paired pages in 823.148 seconds, no skips. With Note
901, both masked CU1 modes now cover 1,014 paired pages for this unchanged
candidate. Text 4,560, descent 3,240, low `0x80031D68`, margin 88 match;
source hashes fixed. Fitting (576 excess), reservation and production gates open.

Init pointer-owned O2 CU1-clear corpus: [Note 901](WORKING_NOTES/901-init-pointer-owned-o2-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 guarded paired pages in 819.113 seconds, no skips. Packed
executable text 4,560, descent 3,240, minimum SP `0x80031D68`, known-neighbor
margin 88; six recorded source hashes unchanged. Combined-candidate CU1-set
qualification remains open, as do 576-byte fitting excess and production gates.

Init pointer-owned tight adapter: [Note 900](WORKING_NOTES/900-init-pointer-owned-tight-adapter-fitting-20261004.md)
combines guest input/workspace ownership with two omitted adapter stores.
Body 176, packed executable text 4,560 O2 / 5,968 O1; bounds unchanged.
O2 rodata moves sixteen bytes below the original default layout, removing
the intermediate alignment gap. Corrected bounded run: 44 passes / one corpus
skip, executed stale-read controls active. Default text exact. O2 still 576
over retail; new full corpora and production ownership/hardware remain open.

Init tight adapter: [Note 899](WORKING_NOTES/899-init-tight-adapter-return-scheduling-and-alignment-20261004.md)
adds opt-in RA delay-slot load, combined SP restore and word-aligned subsection.
Body/executable section falls 192 -> 184; packed text 4,568 O2 / 5,976 O1,
bounds unchanged. Linked O2 rodata still starts at the same aligned address:
eight-byte gap means no proven whole footprint saving. Whole bounded run
41 passes / one corpus skip; separate dependency test passes. Default adapter
text identical. Changed-adapter corpora/production gates open; README unchanged.

Init helper trials: [Note 898](WORKING_NOTES/898-init-global-mask-and-explicit-abi-copy-trials-20261004.md)
rejects global low-mask replacement (O2 bound +8, O1 text +16) and explicit
ABI copy (O2 text +16). Both restored exactly; sixteen focused tests pass,
no skips. Qualified O1/default O2 unchanged; no production/README change.

Init core return trials: [Note 897](WORKING_NOTES/897-init-core-return-control-flow-trials-20261004.md)
rejects success-first (size/bound neutral) and shared-result (O2 text +16,
bounds +24 O2 / +8 O1). Exact source restored; ten focused core/ledger/size
tests pass, no skips. Qualified O1/default O2 remain unchanged; no production
or README change.

Init fixed-length endpoint trials: [Note 896](WORKING_NOTES/896-init-fixed-length-cursor-endpoint-trials-20261004.md)
rejects distance cursors and relative literal endpoints: no complete O2
text saving, all grow O1 sixteen bytes; some initializer frames grow eight.
Exact qualified source restored; nine ledger/size/full-initializer tests pass,
no skips. Qualified O1/default O2 unchanged; production and README untouched.

Init packing trials: [Note 895](WORKING_NOTES/895-init-builder-wide-operation-and-header-packing-trials-20261004.md)
rejects wider operation and combined-header packing. Both remove two public
O2 builder words but save no whole text and add eight bytes to both call bounds.
Exact qualified source restored; twenty focused tests pass, no skips.
Qualified O1 remains 5,984 linked; default O2 remains 4,576 / 592 excess.
Production/defaults/README unchanged.

Init scan-deficit O1 CU1-set corpus: [Note 894](WORKING_NOTES/894-init-scan-deficit-o1-full-masked-cu1-set-corpus-20261004.md)
passes all 507 paired pages in 971.161 seconds, no skips. With Note 893:
1,014 paired pages across both masked modes. Text 5,984, descent 3,200 equals
bound, minimum SP 0x80031D90 / margin 128. Twenty-six supporting checks pass;
six source hashes hold. Both O1 corpus gates checked off; changed-option O2,
fitting/reservation/ownership/hardware remain. Production/README unchanged.

Init scan-deficit O1 CU1-clear corpus: [Note 893](WORKING_NOTES/893-init-scan-deficit-o1-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 paired pages in 975.542 seconds, no skips. Linked text 5,984,
maximum descent 3,200 equals bound, minimum SP 0x80031D90 / neighbor margin
128. Twenty-six supporting gates pass; six source hashes hold. Matching O1
CU1-set, changed-option O2 and production ownership/hardware gates remain.
Production/README unchanged; default best O2 remains 4,576 / 592 excess.

Init scan-deficit fitting: [Note 892](WORKING_NOTES/892-init-builder-inplace-scan-deficit-fitting-20261004.md)
adds an opt-in bounded in-place deficit scan. Packed O1 core falls 32 bytes
to 5,792 / linked 5,984; packed O2 stays 4,384 / linked 4,576 (592 excess).
Frames/bounds unchanged. Whole bounded run: 39 passes / one corpus skip;
separate executed-branch gate passes across six images. Default packed text
matches prior baseline exactly. Changed-option full corpora remain open;
production and README unchanged.

Init mask-lifetime trials: [Note 891](WORKING_NOTES/891-init-mask-before-refill-lifetime-trials-20261004.md)
rejects moving pure masks before refill: take-bits grows both core profiles
sixteen bytes, lookup grows both thirty-two, with unchanged call bounds.
Exact source restored; fifteen focused call/ledger/lookup checks pass.
Qualified linked O2 remains 4,576 / 592 excess; no production/README change.

Init builder sort-offset trials: [Note 890](WORKING_NOTES/890-init-builder-sort-offset-local-trials-20261004.md)
rejects explicit local offsets in both store orders: neither reduces complete
O2 text, both raise O2/O1 call bounds eight bytes. Both edits removed, source
blob restored exactly; seventeen semantic/ledger tests pass. Qualified linked
O2 remains 4,576 / 592 excess. No production or README change.

Init current conversion decision: [Note 889](WORKING_NOTES/889-init-current-assembly-conversion-decision-20261004.md)
rechecks 492 C / 47 assembly functions (151,796 / 12,252 bytes). Bitmap and
MMIO remain small matching candidates; the connected decoder has qualified
experimental C but is still 592 linked bytes too large. Thirty-three focused
tests pass, no skips. Resume fitting and ownership gates, not already completed
frame/adapter recovery. No production conversion or README change.

Init guarded CU1-set corpus: [Note 888](WORKING_NOTES/888-init-live-sp-guard-full-masked-cu1-set-corpus-20261004.md)
passes all 507 live-SP-guarded packed O2/g3 paired pages in 804.839 seconds,
no skips. With Note 887: 1,014 guarded paired pages across both masked modes.
Text 4,576 / 592 excess; descent 3,240 equals bound, minimum SP 0x80031D68 /
known-neighbor margin 88. Twenty-six supporting gates pass; nine source hashes
hold. Both guarded corpus gates checked off; fitting, full reservation,
entry/frame ownership and hardware/context remain. Production/README unchanged.

Init guarded CU1-clear corpus: [Note 887](WORKING_NOTES/887-init-live-sp-guard-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 live-SP-guarded packed O2/g3 paired pages in 806.976 seconds,
no skips. Text 4,576 / 592 excess; observed descent 3,240 matches bound,
minimum SP 0x80031D68 / known-neighbor margin 88. Twenty-six supporting
gates pass; nine source blobs hold. Guarded CU1-clear checked off; matching
guarded CU1-set, fitting, full reservation and hardware/ownership remain.
Candidate/production sources and README unchanged; unrelated Game preserved.

Init live-SP write guard: [Note 886](WORKING_NOTES/886-init-live-sp-write-fence-and-negative-qualification-20261004.md)
adds a separate fixture rejecting private-stack writes below current SP.
Executed below-frame store corruption is rejected across six builds and both
masked modes, even above the old neighbor fence. Whole bounded suite has
37 passes / one corpus skip; thirteen storage regressions pass. Size/bounds
unchanged, packed O2 4,576 / 592 excess. New guarded corpus and full reservation
remain open; previous corpus evidence stays scoped to its old fixture.
Production/defaults/README and unrelated Game work unchanged.

Init MMIO published-address trial: [Note 885](WORKING_NOTES/885-init-mmio-published-address-dataflow-trial-20261004.md)
measures five profiles using D_80038070 as the hardware-store destination.
O1 eliminates the read and retains the address, but adds a register copy
and delay-slot store; no complete eleven-word match. Other profiles either
exceed the slot or retain an extra read. Ten bounded store traces pass;
three production MMIO assembly tests pass. No production/profile/guard or
README changes; decoder-qualified baseline and unrelated Game work preserved.

Init descending count-clear trials: [Note 884](WORKING_NOTES/884-init-builder-descending-count-clear-trials-20261004.md)
measures post-/pre-decrement clears of all 17 buckets. Neither reduces
complete O2 core text; post-decrement adds eight bytes to both core bounds,
and both forms grow O1 text. Both removed, source restored exactly.
Thirteen focused retained gates pass, including direct builder boundaries.
Qualified linked O2 stays 4,576 / 592 excess; production/README unchanged.

Init stored-loop fitting trials: [Note 883](WORKING_NOTES/883-init-stored-output-cursor-and-countdown-trials-20261004.md)
measures an output pointer cursor and a length countdown. Both grow whole
packed core text sixteen bytes in O2/O1 and enlarge the stored frame;
maximum core bounds stay 392/352 because another path dominates. Both
removed, source restored exactly. Thirteen focused retained gates pass,
including bad-complement bit state. Qualified linked O2 remains 4,576 /
592 excess; production/defaults/README and unrelated Game work unchanged.

Init core-limit fitting trials: [Note 882](WORKING_NOTES/882-init-core-limit-predicate-and-local-lifetime-trials-20261004.md)
measures an unsigned workspace-distance gate and a local-limit variant.
Raw O2/O1 entry bodies save two/one words, but padding leaves core text
4,384/5,824 unchanged; local-limit raises O1 core bound from 352 to 360.
Both forms removed, source restored to the qualified blob. Twelve focused
retained tests pass; Notes 880/881 corpus evidence still applies to the
unchanged baseline. Linked O2 4,576 / 592 excess; production/README unchanged.

Init direct-load CU1-set corpus: [Note 881](WORKING_NOTES/881-init-direct-fpr-adapter-full-masked-cu1-set-corpus-20261004.md)
passes all 507 fresh packed O2/g3 paired pages with masked CU1 set in
790.940 seconds, no skips. Together Notes 880/881 qualify 1,014 paired pages
across both masked modes, per-page callee-return guard active. Linked text
4,576 / 592 excess; observed descent 3,240 matches bound, minimum SP
0x80031D68 / known-neighbor margin 88. Eleven supporting gates pass and eight
source blobs hold. Both direct-load corpus gates checked off; fitting,
ownership, hardware/context and full reservation remain. Production/README unchanged.

Init direct-load CU1-clear corpus: [Note 880](WORKING_NOTES/880-init-direct-fpr-adapter-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 fresh packed O2/g3 paired pages with masked CU1 clear in
808.272 seconds, no skips. Linked text 4,576 / 592 excess; observed descent
3,240 matches bound, minimum SP 0x80031D68 / known-neighbor margin 88.
Eleven supporting gates pass and all eight recorded source blobs hold.
Direct-load CU1-clear checked off; matching CU1-set, fitting/ownership/
hardware/reservation remain open. Production/defaults/README unchanged.

Init direct FPR load adapter: [Note 879](WORKING_NOTES/879-init-direct-fpr-load-adapter-fitting-20261004.md)
adds opt-in LWC1 publication of sixteen stack words, reducing adapter body
and aligned text from 256 to 192 bytes. Packed O2/g3 linked text is 4,576,
592 over retail; core text/bounds stay unchanged. Separate word-load receipts
preserve existing context gates and default assembled text matches HEAD.
Fresh bounded suite: 36 passed / one corpus skip in 254.545 seconds;
eleven shared/default regressions pass. All six observed descents match bounds.
New-option full corpus, fitting/ownership/hardware remain open; Notes 877/878
qualify only the previous adapter. Production/README unchanged.

Init current callee-adapter CU1-set corpus: [Note 878](WORKING_NOTES/878-init-callee-adapter-full-masked-cu1-set-corpus-20261004.md)
passes all 507 fresh packed-remaining O2/g3 paired pages with masked CU1 set
(0x2400FF00), 792.002 seconds, no skips. Together with Note 877 this
qualifies 1,014 paired pages across both masked modes, with callee-return
guard active on every page. Linked text 4,640 / 656 excess; observed descent
3,240 matches bound, minimum SP 0x80031D68 / neighbor margin 88. Sixteen
supporting gates pass; all source blobs hold. Current corpus gates checked
off; fitting/ownership/hardware/reservation remain. Production/defaults/README unchanged.

Init current callee-adapter CU1-clear corpus: [Note 877](WORKING_NOTES/877-init-callee-adapter-full-masked-cu1-clear-corpus-20261004.md)
passes all 507 fresh packed-remaining O2/g3 paired retail pages with masked
CU1 clear (0x0400FF00), 839.425 seconds, no skips. The callee-return boundary
guard runs on every page. Linked text 4,640 / 656 excess; observed descent
3,240 equals bound, minimum SP 0x80031D68 / known-neighbor margin 88.
Sixteen supporting gates pass; decoder/adapter/test blobs unchanged. Current
CU1-clear gate checked off; matching CU1-set now passes in Note 878, while
fitting/ownership/hardware remain open. Production/defaults/README totals unchanged.

Init pointer/argument ownership trials: [Note 876](WORKING_NOTES/876-init-unretained-pointer-argument-ownership-trials-20261004.md)
measures direct input argument, workspace address from state and their
combination. Neither aggregate profile improves; workspace-only grows O1
sixteen bytes. Two corresponding adapter-store omissions shrink body to 248
but aligned text stays 256, linked O2/O1 stays 4,640/6,080. Both sources
restored exactly; fifteen focused retained-config gates pass. No trial
semantic qualification, new option or production count change; current corpus
and fitting/ownership/hardware remain open.

Init callee-preserving adapter fitting: [Note 875](WORKING_NOTES/875-init-callee-preserving-core-adapter-fitting-20261004.md)
adds opt-in omission of ten duplicate S0-S7/GP/FP reloads, retaining saved
frame cells and RA restoration. Adapter body/aligned text is 256/256 versus
296/304; all six shapes save 48 linked bytes, packed O2 4,640 / 656 excess.
All observed descents match bounds. Fresh whole suite has 34 passes / one
corpus skip; strengthened instruction-clobber guard and sixteen helpers pass.
The initial mistaken S0-reload probe is documented. Omitted-option adapter
text matches baseline. Changed corpus and fitting/ownership/hardware remain;
production/defaults/README unchanged, unrelated Game work preserved.

Init lookup exit-shape trials: [Note 874](WORKING_NOTES/874-init-lookup-exit-shape-and-offset-predicate-trials-20261004.md)
measures child-gated common return and offset predicates on Note 873.
Common return saves raw helper words, but neither form reduces complete
packed text or core bounds; both removed with exact source restoration.
Operation caching is ruled out by the single existing load. All 256 byte
classifications pass a host algebra probe; fifteen restored-config gates pass.
Retained option remains 4,688 linked O2 / 704 excess, changed corpus open.
Production/defaults/README unchanged; unrelated Game work preserved.

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
