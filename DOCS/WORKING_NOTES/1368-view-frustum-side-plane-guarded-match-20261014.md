# View Frustum Side-Plane Guarded Match - 2026-10-14

## Result

Continue [Note1367](1367-record-payload-constructor-direct-match-20261014.md)
from consumer3e43200c/tools4e667db. Replace func_1501B22C's false zero-return
C placeholder with its complete view-frustum side-plane routine.
VA0x1501B22C / ROM0x486DC now matches all61 slot words (244 bytes):
59 code words plus two original alignment NOPs, frame0x40.

Four expected-word, relocation-free guards coalesce the disjoint horizontal/
vertical phase angle and cosine homes. No arithmetic, helper, output store,
branch, frame adjustment or padding operation is supplied by a guard.
Retain the public address-keyed name; correct its interface to void with one
signed index, using a declaration outside the placeholder group and
descriptive locals. Keep the existing SDK struct259 and shared headers.

The routine snapshots both half-FOV inputs, calls cosine/sine once per axis
and writes four three-component side-plane normals. The additional source's
annotation identifies fovX/fovY; map these to the active SDK's unk74/unk78,
rather than importing its renamed structure wholesale. The indexed record
stride is0x180; both scale constants are the retail pi/180 f32 value.

This is a guarded draft recovery, separate from the33 banked direct donor
imports. The original placeholder already counted as C, so conversion and
progress CSV bytes stay unchanged. The wider goal remains active.

## Steps

1. [x] Verify clean consumer/tools state, current working-note boundary, graph relationships and nine immutable input hashes.
2. [x] Inspect the complete retail slot, additional draft, active SDK structure and actual func_1510B690 signed-index call.
3. [x] Separate59 code words from two alignment NOPs and identify the four actual first-phase stack-home differences.
4. [x] Screen pointer/lifetime/volatile/union forms; retain the full O2/g3 body and qualify the bounded home-coalescing guards.
5. [x] Preserve10 complete-owner neighbors, sizes, relative relocations, normalized pools and zero compiler warnings.
6. [x] Verify both actual padders and four independent original/rebased comparisons, including external HI/LO carry addresses.
7. [x] Pass7,680 MIPS cases, all59 code words reached and1,116 actually fired root-memory fault prefixes.
8. [x] Pass896 native32 cases per O2/O0 profile with the proven SSE2 stack-realignment setup and effective compiled controls.
9. [x] Install only this body/interface/guard group; close the production ELF to190 target bytes and the12-to236-byte public extent.
10. [x] Pass11 target/capture checks18.866s and28 affected history/behavior checks45.466s; preserve immutable old checkpoints and corruption controls.
11. [x] Prove the old rectangle image gate already fails on the pre-frustum baseline; fix only its frozen-owner padder's guard-snapshot mismatch.
12. [x] Preserve801 source-archive files and502 unrelated mirror fingerprints; sync nine compatible task files and bank tools46da39b first.
13. [x] Recover Game sinf's104-word float body in [Note1369](1369-game-single-precision-sine-and-cosine-recovery-20261014.md); Game cosf's88-word slot remains open.
14. [ ] Reconcile the older rectangle literal-image history without recapturing its baseline or masking unverified changes.
15. [ ] Continue actual failed-source/interface/pool recovery, layer-decoder dependencies and original Game matching.

## Source And Home Evidence

The selected source preserves all59 original code words except:

| Offset | Expected compiled word | Retail replacement | First-phase home |
| --- | --- | --- | --- |
| 0x54 | 0xE7AC0020 | 0xE7AC0024 | Angle store20 ->24 |
| 0x58 | 0xC7AC0020 | 0xC7AC0024 | Angle load20 ->24 |
| 0x60 | 0xE7A00030 | 0xE7A00034 | Cosine store30 ->34 |
| 0x64 | 0xC7A20030 | 0xC7A20034 | Cosine load30 ->34 |

Static qualification inventories every root SP-based floating load/store:
first angle words21/22; first cosine24/25; pending vertical half19/37;
second angle40/41; second cosine43/47. First-phase values are consumed before
the corresponding second-phase definitions. Neither local's address escapes
through the four scalar float calls. Saved s0/ra remain at+0x18/+0x1C.
Only the lower16-bit displacement changes; opcode, FPR and SP base are fixed.

Pointer order matters for retail's t6/t7 roles: index*0x180 before the byte
base matches the opening words, while base-first/typed indexing adds five
register differences. Union, array, volatile and separate-sine forms change
allocation, homes, frame or sequence and are rejected; retain those private
screens rather than inventing dummy accesses or caller-saved register hints.
The selected owner remains warning-free under its normal O2/g3 profile.
The broad production build still emits inherited warnings elsewhere and
the existing duplicate generated_12D630 recipe warning.

Both padders keep the original two trailing NOPs outside the236-byte
STT_FUNC extent. Independently assembled retail agrees with primary and
generated padded objects at original and rebased code/helper/global addresses.
The actual caller uses jal followed by move a0,s0 and does not consume an
integer result. The signed-index/void interface corrects the old placeholder;
no other source caller or shared prototype is changed.

## Behavioral Qualification

The7,680 MIPS cases cross full-width indices, eight input pairs, base/scale
aliases, four helper mutation modes, eight helper return patterns and two
stack phases. Compare float F12 call arguments, all public memory and the
complete available interpreter state. Reach all59 executable words; the two
alignment NOPs remain strictly byte-checked.

Callbacks mutate the global base, FOV input, scale constants and an earlier
plane output. Qualify the cached view pointer, pre-call vertical-half snapshot,
cached first angle/cosine and live second scale lookup. Return patterns include
signed zero, infinities and quiet/signaling NaN bit patterns; negation uses
the existing bit-preserving instruction model. Index wrapping and cross-object
global aliases are guest probes, not portable C pointer-arithmetic claims.

All1,116 actually fired root-memory prefixes agree on state and actual
PC/delay-slot identity. Helpers are atomic bounded contracts; arbitrary helper
faults and portable C-fault equivalence are not claimed. The replay is not a
VR4300/FCSR exception emulator, and does not qualify retail trig accuracy.

Native32 O2/O0 each pass896 disjoint-record cases, comparing complete storage,
four float arguments and relevant global effects. Assert the used SDK record
offsets/size and use single-precision SSE2 with contraction disabled. Quiet
NaN/inf/zero helper results are covered; signaling NaNs, index wrap, partial
object aliases, FCSR behavior and actual trig accuracy remain outside this
native claim.

The initial native harness first rejects an unused helper under Werror, then
crashes before comparison. GDB identifies movaps at0x08049244 with ESP mod16=4
in the bare _start path. Reuse the existing float fixtures' mstackrealign flag;
no production source/compiler flags change. The corrected cases and wrong
stride/sign/reloaded-half controls all pass or fail as intended.
Changed expected words and expected relocation metadata are also rejected.

## Closed Image And History

The broad guard dependency rebuild completes successfully. Compare the
whole serialized ELF against the independently constructed expected image:
only190 bytes in the244-byte target slot plus its12-to236-byte extent change.
Every other function/address/symbol byte, overflow/data section, Makefile,
header, original assembly and progress byte is fixed. Protected data remains
189,088 bytes /720 owners /zero differences.

| Input | SHA-256 |
| --- | --- |
| Baseline ELF | c9ff4e7ec28882546f87fb159a96b0c0e1c2b8fac6de4eb58725d91eef78a3bd |
| Final ELF | 79eb4f3261dcc2cff366d6e1dcddef48cb1c6e6b923821272d3b56c709a82e10 |
| Final owner | 8bba4f1abbd69d9032a5fe0be73238d84f6b13ecf44716938037ef03f9cb0aae |
| Final guards | b0f5425a5a3fbe2a1a44898f5c5499b781cf0598532b595dae1c81c7534b4d99 |
| Unchanged progress | 005fd7682d37802a2b7591cfb023648b6a083c8df6b957bdfedd737222cad68e |
| Unchanged Makefile | 838070597f76ea2f7182c158dfb6710946cfcabcb5435e994f93cdb99340e313 |

The new inverse accepts only exact final full-input hashes for owner/guards/
ELF. Unknown or corrupt inputs pass through unchanged and existing history
checks reject them. Capture cannot overwrite pinned after fixtures.
All19 original direct-body recoveries and742 neighbors are freshly rechecked
through the verified history chain, not by resetting their source snapshots.

The first29-check historical run passes27 and reports two old rectangle
fixture failures. Its frozen-owner padder was using the live guard manifest,
which now contains the new view-body guards; use its immutable before-guards
snapshot, independently pinned at3f12cf87, and retain every production guard.
That owner/padder test then passes7.146s.

Rectangle test_07 is separately stale to pre-existing history: its c58a81de
whole-image/source snapshot predates the AF44 donor import and other banked
work. A read-only replay using the complete pre-frustum source/ELF/guards/
progress inputs still fails that old owner comparison. Its frozen source is
e3c2baf6; the existing verified history chain projects current source onto the
old rectangle's selected owner, but the older image history is not yet fully
reconciled. Preserve all snapshots and the failing test unchanged. Do not
describe the entire rectangle suite or every historical test as green.

The final deliberately scoped suite passes28 history/behavior checks45.466s,
plus11 target/capture checks18.866s:39 fresh passing checks with one explicit,
confirmed pre-existing literal-image gate still open. Current complete-image
and corruption gates remain effective; no section or symbol exclusion is added.

Receipts live in `conker/build/game-view-frustum-planes/`; earlier pointer/
lifetime screens are retained in `conker/build/game-view-half-angle-vectors/`.
Fresh source audit:
`conker/build/alternative-source-byte-audit-20261014/frustum-plane-after.json`.
The current successful linked raw-donor queue is empty; that does not complete
the failed/commented/used-interface and real pool-binding queues.

## Progress And Boundaries

Fresh Game2,874/4,831 (59.49%), total3,547/5,504 (64.44%), different1,957,
drift0. Converted5,504/6,044 and all conversion-byte percentages remain fixed.
Executable-only total3,407/5,364 (63.52%), Debugger41/41. The legacy181/181
Debugger row still includes140 data labels. Root README changes only the two
matching aggregate rows.

All801 archive files stay unchanged. Nine task mirror files agree byte-for-
byte and pass syntax checks; two standalone candidate tests pass0.005s.
Older mirror HEAD remains ddbdd16b53ce60b054fb6e11bf0649a41f48375a, dirty count
507 ->511, all502 unrelated fingerprints fixed. Preserve its independent history.
Tools46da39b8652d9fb14c6b440b6fa2fdd76e4a35ca banks before the consumer pin.
No push, Claude call, host transfer/build or frozen-Release operation occurs.

Graph update refuses19,046 partial nodes in place of40,827 curated nodes,
retaining19,398 nodes from2,972 excluded but still-present files. Never force
the smaller scan; await the incremental consumer commit worker separately.

## Next Dependency Handoff

Game cosf at0x15047C00 and sinf at0x15047D60 still contain false zero-return
C placeholders in conker/src/libultra/gu/. Their slots are88/104 words.
The additional source keeps these routines as assembly, not usable C drafts.
Inspect the complete retail polynomial/range-reduction bodies and actual f32
coefficient tables next; reconstruct from the relevant SDK/retail evidence.

Init's __sinf in conker/src/game/generated_sinf.c uses a distinct f64
implementation and separate coefficients. Do not substitute it or a host
library forwarder as though it were the Game byte-matching body. The new
frustum routine is instruction-exact, but complete camera/culling and actual
math/runtime behavior are not accepted while these dependencies remain stubs.

Continue the99 individual/59 commented compile failures, real binding cases,
layer decoder dependencies and original Game matching alongside the separate
historical rectangle-image reconciliation. No goal completion is claimed.

## Post-Bank Verification

Consumer5a74421f banks the source/interface/guard group, tools pin and docs.
All16 post-bank target/capture/historical-control checks pass33.090s. The
incremental build reports ELF/progress up to date and retains the79eb4f32
image and005fd768 progress. Main and active tools are clean before this
receipt commit; the independently dirty older mirror remains preserved.
The old rectangle test_07 snapshot issue remains separately open; these
post-bank passes do not recapture it or claim a fully green legacy suite.

The source commit's incremental graph worker completes at40,838 nodes /
81,017 edges. It preserves the curated/excluded-file boundary and skips only
the oversized HTML visualization. No smaller forced graph refresh, push,
host transfer/build or frozen-Release operation is performed.
