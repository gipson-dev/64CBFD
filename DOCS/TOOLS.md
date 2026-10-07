# Project Tools

This page documents repository-local tooling, especially scripts that are not
upstream submodules. Run commands from the repository root unless a section
says otherwise.

## Secondary halfword output matching controls

[Driver](../tools/experiments/game_secondary_output_candidates.py) retains96
case-order/chaining/product/shared-case controls across four profiles. Selected
O2/g3 and O2 emit all120 words/frame0 directly, with fourteen original table
destinations. Two checked relocations bind the compact table at644 to the
preserved `jtbl_800A565C_game`; no instruction normalization.
The copied pool retains644 meaningful bytes, appends56 table bytes and4 padding,
total704. Related copied-owner checks pin exact earlier-table addend shifts.
[Eleven tests](../tools/tests/test_game_secondary_output_match.py) qualify65536
guest/24576 stack-alias/4096 live-input/557056 native/8192 connected two-leaf
caller-fragment cases, all120 words, full memory/ordered traces/saved state,
lazy reads, independent scale inputs and six effective compiled negatives.
Original50-word caller setup includes both delay stores and distinct mode bytes
at object0x29/0x2A. Native parameters do not model guest argument-home aliasing;
bounded caller fragments do not prove complete callers/hardware/gameplay/host adoption.

```sh
python3 -m tools.experiments.game_secondary_output_candidates
python3 -m unittest tools.tests.test_game_secondary_output_match -v
```

Ignored receipts:`conker/build/game-secondary-output/` and
`conker/build/game-secondary-output-test/`; see
[Note 1080](WORKING_NOTES/1080-game-secondary-halfword-output-direct-match-20261007.md).

## Halfword output-mode matching controls

[Driver](../tools/experiments/game_output_mode_candidates.py) retains96
case-order/chained-store/product/shared-case controls over four profiles.
Selected O2/g3 and its O2 control match all86 words directly, frame0, with the
original five destinations. Two expected-word/relocation guards bind the copied
owner's compact table at offset624 to the original `jtbl_800A5648_game`.
Prior624-byte normalized pool intact; new656-byte pool adds20 table bytes and12
alignment bytes. No instruction normalization, profile/shared-header changes.
[Eleven tests](../tools/tests/test_game_output_mode_match.py) cover65536 paired
guest mode/alias cases,24576 argument-home overlap cases,3584 unused-byte cases,
557056 actual32-bit native calls and2048 original25-word caller fragments.
All86 words, full memory/ordered traces/saved state, lazy stack/table reads,
all65536 integer products, six negatives and copied-owner/padder/HI16 carry/
stale guards qualify. Native tests cover typed values/output aliases, not guest
parameter-home aliasing. Neighboring pool tests explicitly check the appended
table and the later addend shift when copying an owner without the resolver.
No complete-caller/hardware/gameplay or host adoption claim.

```sh
python3 -m tools.experiments.game_output_mode_candidates
python3 -m unittest tools.tests.test_game_output_mode_match -v
```

Ignored receipts:`conker/build/game-output-mode/` and
`conker/build/game-output-mode-test/`; see
[Note 1079](WORKING_NOTES/1079-game-halfword-output-mode-direct-match-20261007.md).

## Fixed-point cursor updater matching controls

[Driver](../tools/experiments/game_cursor_updater_candidates.py) retains131
declaration/initialization/loop/flow/storage/profile measurements. Corrected
and asserted lower-loop transformations recover98 words/frame0.52 direct words
and46 checked guards differ only in temporary-register fields and a commutative
addition's operand order, not instructions, branch/immediate fields or frame.
All four global relocation identities/positions stay unchanged.
[Eleven tests](../tools/tests/test_game_cursor_updater_match.py) cover18944 paired
guest cases,3500 modular/global/stack alias cases,1024 count0/trap cases,11776
paired instruction-input traces,20182 actual32-bit native calls and192 original
setup/call/delay/mask fragments. Full memory/ordered reads-writes/saved state,
mode priority, live velocity rereads, lazy byte access, six negatives, copied
owner/pools/warnings, actual guarded padding and alternate HI16 carries qualify.
Stale words and relocation expectations fail closed.95 reachable words covered;
three dead trap guards are justified by the count domain. Native division
overflow and hardware HI behavior, complete callers and gameplay are unqualified.

```sh
python3 -m tools.experiments.game_cursor_updater_candidates
python3 -m unittest tools.tests.test_game_cursor_updater_match -v
```

Ignored receipts:`conker/build/game-cursor-updater/` and
`conker/build/game-cursor-updater-test/`; see
[Note 1078](WORKING_NOTES/1078-game-cursor-updater-match-20261007.md).

## Actor-gated packet matching controls

[Driver](../tools/experiments/game_actor_gated_packet_candidates.py) retains116
compiler measurements:64 gate/type/order profile controls,48 short-flag storage
controls and four selected profiles. O2/g3 recovers98 words/frame0x38 and the
original packet/result private slots. Eleven expected-word/relocation guards
normalize only the closed opening schedule, including a moved branch with the
same absolute destination; no frame/private-offset or production-profile edits.
[Ten tests](../tools/tests/test_game_actor_gated_packet_match.py) cover8192 paired
guest cases,362 callback/RNG cases,18856 actual32-bit native calls and12 original
call-delay pairs. Full eight-byte guest payload, poisoned untouched bytes,
snapshot count/live context, full-word inputs, ignored submission result,
semantic negatives, copied owner/pools/warnings and actual guarded padding
are checked. Alternate relocation carries/targets and stale metadata fail closed.
96 reachable words are covered; two dead branch-likely increments are identified.
Native padding, real actor bounds beyond26, helper/gameplay/hardware behavior
and complete callers are not claimed. Storage/profile controls qualify bounded
defined behavior, not equivalent private memory for alternate layouts.

```sh
python3 -m tools.experiments.game_actor_gated_packet_candidates
python3 -m unittest tools.tests.test_game_actor_gated_packet_match -v
```

Ignored receipts:`conker/build/game-actor-gated-packet/` and
`conker/build/game-actor-gated-packet-test/`; see
[Note 1077](WORKING_NOTES/1077-game-actor-gated-packet-match-20261007.md).

## Record-query matching controls

[Driver](../tools/experiments/game_record_query_candidates.py) retains98
measurements:64 mask/loop/order/input-type profile controls,30 storage/declaration
controls and four selected profiles. Index-before-result declarations recover
272 direct words/frame0x60. No guards, shared-header edits or production-profile
change. This owner isolates the legacy inline-array declaration and uses the
original table pointer; other owners are unchanged.
[Ten tests](../tools/tests/test_game_record_query_match.py) cover all2048 field
selections/both modes in12288 paired guest cases,196608 native calls across all
u16 flags,1470 range cases,120 field corners and32 original caller setup-call-delay
fragments. Ordered reads/writes, memory/saved state, last matching pointer,
negative controls, copied-owner/pools/warnings and actual padding/linking gates
are checked.267 reachable words covered; five dead branch-likely else words
are identified, not claimed as executed. A seeded fragment is not a complete
original caller, and guest float checks are not hardware FCSR acceptance.

```sh
python3 -m tools.experiments.game_record_query_candidates
python3 -m unittest tools.tests.test_game_record_query_match -v
```

Ignored receipts:`conker/build/game-record-query/` and
`conker/build/game-record-query-test/`; see
[Note 1076](WORKING_NOTES/1076-game-record-query-direct-match-20261007.md).

## Range-clamp matching controls

[Driver](../tools/experiments/game_range_clamp_candidates.py):baseline and
direct-pointer forms under four SDK profiles, eight maintained measurements.
Selected O2/g3 recovers36 words/frame0x10. Thirteen expected-word guards change
only temporary GPR operand fields; no opcode, address, branch, ordering or
frame rewrite. Leaf has no relocations. Prior10842 guard rows remain pinned;
10855 total. [Nine tests](../tools/tests/test_game_range_clamp_match.py) qualify
3750 paired full-memory guest cases/all36 words,1250 native typed-caller cases,
250 original call-delay fragments, four negatives, actual padding/stale words
and complete copied-owner neighbor/pool/warning preservation. A call fragment
with seeded context/synthetic return is not complete original caller execution.

```sh
python3 -m tools.experiments.game_range_clamp_candidates
python3 -m unittest tools.tests.test_game_range_clamp_match -v
python3 -m tools.experiments.game_area_sampler_exit_candidates
```

[Sampler exit driver](../tools/experiments/game_area_sampler_exit_candidates.py)
adds30 O2/g3 controls to the existing152 measurements:output volatility,
aggregate/scalar/per-case scratch, byte/word angle storage and descriptor
volatility. None closes the sampler's missing exits; new scalar variants are
screening only, not qualified replacements. Ignored receipts:
`conker/build/game-range-clamp/`, `conker/build/game-range-clamp-test/`,
`conker/build/game-area-sampler-exits/`; see
[Note 1075](WORKING_NOTES/1075-game-range-clamp-byte-match-20261007.md).

## Area-sampler recovery controls

[Driver](../tools/experiments/game_area_sampler_candidates.py) retains38 forms
across four SDK profiles (152 controls), including switch/exit structure,
scratch lifetimes, RNG temporaries, signed flags and scaling alternatives.
Selected candidate252 words/frame0x50, not yet254-word retail. Integer scaling
recovers the count but not the arithmetic sequence. No guards/profiles installed.
[Ten tests](../tools/tests/test_game_area_sampler_recovery.py) cover1024
independent-reference guest cases,48 bounded conversion cases,1536 original
angle-helper cases,64 complete original caller cases,256 native cases,
six compiled negatives and copied-owner/pool/warning preservation.
Native conversion inputs are finite and nonnegative within the unsigned domain;
invalid conversion paths are guest-only bounded models, not FCSR emulation.

```sh
python3 -m tools.experiments.game_area_sampler_candidates
python3 -m unittest tools.tests.test_game_area_sampler_recovery -v
```

Ignored receipts:`conker/build/game-area-sampler/` and
`conker/build/game-area-sampler-test/`; see
[Note 1074](WORKING_NOTES/1074-game-area-sampler-qualified-recovery-20261006.md).
This suite deliberately checks that the candidate is uninstalled and no target
guards exist. Update that gate only with a qualified future installation.

## Point-transform compiler and diagnostic controls

[Driver](../tools/experiments/game_point_transform_candidates.py):17 source
shapes/plain versus volatile global declarations,34 O2/g3 measurements;
selected body additionally checked under all four SDK profiles. Early fixed-path
clear/return recovers98 words/frame0x78.31 checked allocation/save-order guards
close the s1/s2/s3 cycle; no arithmetic/control/frame/insert/omit normalization.
[Eleven tests](../tools/tests/test_game_point_transform_match.py) bind1950
paired guest cases/all98 words/full memory/external traces,180 connected original
SDK/matrix/translation cases,144 actual32-bit native callers and39 original
call/delay sites/234 seeded cases. Preserve diagnostics, zero/null fallback,
signed-zero gate and conversion input rereads. Six compiled negatives and
mapped-memory gates reject incorrect status/outputs/call contracts.
Native uses the actual SDK conversion body with bounded transform/translation
helpers; guest original connections are separate, finite-qualified evidence.
Original translation helper is49 words, not the stale handoff's53.

Copied owners preserve88 typed neighbors,624-byte relocation-owned pool and
two warnings after assembly post-processing; all6059 final linked slots are
unchanged. Actual padder checks expected words/relocations and alternate global
carry/helper addresses. At Note1073, guard history pinned10811 prior rows plus
exactly31 point-transform rows,10842 total. The range-clamp section above
describes the current10855-row history, including the thirteen new rows. Commands:

```sh
python3 -m tools.experiments.game_point_transform_candidates
python3 -m unittest tools.tests.test_game_point_transform_match -v
make -C conker VERSION=us NON_MATCHING=1 progress
```

The progress target's normal checksum gate still fails for the nonmatching
whole project; NON_MATCHING=1 refreshes reporting, not retail acceptance.
Ignored receipts:`conker/build/game-point-transform/` and
`conker/build/game-point-transform-test/`; see
[Note1073](WORKING_NOTES/1073-game-point-transform-assembly-to-c-match-20261006.md).
No FCSR/NaN-payload,64-bit host, whole-caller or gameplay acceptance.

## Texture resolver compiler and owner-pool controls

[Driver](../tools/experiments/game_texture_resolver_candidates.py):18 forms
across four SDK profiles,72 controls. Two repeated-source-field O2/g3 forms
emit all50 words/no frame; separate-word/index-only forms emit49 instead.
[Ten resolver tests](../tools/tests/test_game_texture_resolver_match.py) bind
13824 paired full-storage/trace guest cases,19200 actual32-bit native cases,
486 complete original102-word cache-caller/50-word resolver cases and ten
compiled negatives. Preserve low-byte kind, signed indices, unsigned10000000
threshold and original six-case jump-table order. Native uses valid arrays/
real pointers; exact threshold/negative-index probes are guest-only.
Actual padder retains200 bytes, excludes eight text-alignment bytes and tests
all five relocation pairs at normal/alternate carry addresses. Copied owner
retains92 neighbors/two warnings/prior600 payload bytes and appends six table
targets at offset600. Two expected-word/relocation guards bind this pair to
original jtbl_800A562C_game, without a scheduling/register/frame rewrite.
Full owner assembly post-processing is required before actual padding.

[Pool comparator](../tools/tests/game_owner_pool.py) uses actual R_MIPS_32
text relocations to compare function-relative targets while keeping every other
byte exact. [Three independent fixtures](../tools/tests/test_game_owner_pool.py)
reject changed targets/literals, missing/unsupported relocations and unowned
targets. Neighbor guard checks pin the original10809-row digest, two exact
resolver-table bindings, the31 point-transform guards and the thirteen clamp
rows described above. Commands:

```sh
python3 -m tools.experiments.game_texture_resolver_candidates
python3 -m unittest tools.tests.test_game_texture_resolver_match tools.tests.test_game_owner_pool -v
```

Ignored receipts:`conker/build/game-texture-resolver/` and
`conker/build/game-texture-resolver-test/`; see
[Note1072](WORKING_NOTES/1072-game-texture-resolver-match-and-table-binding-20261006.md). Submit remains a bounded model;
no original rendering/gameplay, native private-home or64-bit host acceptance.

## Texture-cache submission controls

[Driver](../tools/experiments/game_texture_cache_candidates.py):eight
early-return/captured-world/volatile-world forms across four SDK profiles,
32 controls. Only default O2/g3 emits all102 words/frame0x40 directly.
[Eleven tests](../tools/tests/test_game_texture_cache_match.py) bind2304
paired full-trace/storage guest cases,88 guest-only homes,486 connected
original-resolver cases,6912 native32-bit typed-helper cases, nine original
call/delay pairs and ten compiled negatives. Preserve signed packed shifts,
cache-hit no-sync-read, callback-live flags/cache fields and observable
attachment reload/same-value-store. Original resolver uses the actual exact
Game-data jump table; submit is bounded, call pairs are not full callers.
Actual padder preserves408 bytes, excludes eight alignment bytes and retargets
both calls. Copied owner retains92 neighbors/pools/two warnings; production
binds102 words/nine exact neighbors/the unchanged10809-row prefix plus two
resolver-table bindings plus31 point-transform guards (10842 total). Commands:

```sh
python3 -m tools.experiments.game_texture_cache_candidates
python3 -m unittest tools.tests.test_game_texture_cache_match -v
```

Ignored receipts:`conker/build/game-texture-cache/` and
`conker/build/game-texture-cache-test/`; see
[Note1071](WORKING_NOTES/1071-game-texture-cache-submission-match-20261006.md).
No original submit-helper, whole-caller, native private-home, hardware/RDP/
gameplay or64-bit host acceptance. Resolver is now recovered as described above.

## Row matrix compiler controls

[Driver](../tools/experiments/game_row_matrix_candidates.py):translation-first/
last and row/column store ordering across four actual SDK profiles,16 controls.
Translation-first, row-order O2/g3 emits55 direct words/frame0x58 without guards.
[Eleven tests](../tools/tests/test_game_row_matrix_match.py) bind2160 paired
guest/full ordered trace/storage cases,192 float edges,36 guest-only live-home
probes,1176 actual32-bit native caller cases and nine compiled semantic negatives.
288 connected cases cover all24 original caller/55 builder/115 converter words
on finite exactly integral fixed conversions. Rotation remains a bounded model;
native converter captures float payloads, with classification-only arithmetic
NaN comparison. Actual padder retains220 symbol bytes, excludes four alignment
bytes and retargets both calls. Copied owners preserve92 builder neighbors,
all31 caller functions/pools/relocations and warnings2->2 in each. Production
binds target, caller, eight neighbors/the unchanged10809-row prefix plus two
resolver-table bindings plus31 point-transform guards (10842 total). Commands:

```sh
python3 -m tools.experiments.game_row_matrix_candidates
python3 -m unittest tools.tests.test_game_row_matrix_match -v
```

Ignored receipts:`conker/build/game-row-matrix/` and
`conker/build/game-row-matrix-test/`; see
[Note1069](WORKING_NOTES/1069-game-row-matrix-match-and-oriented-layout-20261006.md).

## Oriented matrix recovery controls

[Driver](../tools/experiments/game_oriented_matrix_candidates.py):eight
array/reversed-struct up-vector, row/column store-order and early-first-element
forms, eight direction-layout/captured-start forms and sixteen in-place direction/
up normalization and horizontal-vector forms across four actual SDK profiles,
128 controls. This is an uninstalled recovery driver:142 words/frameB8/
84 differences,142/frameB8/27 private differences, or142/frameC8/57,
142/frameC8/47 and142/frameD0/44 differences
confined to stack immediates. It does not patch the frame or install guards.
[Thirteen tests](../tools/tests/test_game_oriented_matrix_recovery.py) bind2448
six-body guest cases,1224 actual32-bit native typed-caller cases per candidate,
144 complete original caller/builder/converter cases per body, all142 builder
words, eighteen compiled negatives across two source bodies and native
integer-load rejection. Preserve
three independent normalizations, separate multiply rounding, start-point
translation and retail's lack of a degenerate fallback. Converter execution
is restricted to finite exactly integral fixed results; native conversion
uses a float-payload capture. Arithmetic NaNs are classification-compared,
not native payload/FCSR/exception-mode acceptance. Actual padder retains568
bytes in both the original fitting and new in-place candidate, and retargets
one call in each. All five copied builder owners preserve92 neighbors/
pools/two warnings; the typed caller copy preserves all eight raw functions,
pools and zero warnings. Private trace identity across differing layouts is
not claimed. Five native candidates and five copied builder owners are qualified.
The new candidate has the original frame/homes and only ten direction references
at retail-4 plus seventeen matrix references at retail-8; the test checks this
without rewriting any words.
No oriented production change. Commands:

```sh
python3 -m tools.experiments.game_oriented_matrix_candidates
python3 -m unittest tools.tests.test_game_oriented_matrix_recovery -v
```

Ignored receipts:`conker/build/game-oriented-matrix/` and
`conker/build/game-oriented-matrix-test/`; resume the stack-only challenger in
[Note1070](WORKING_NOTES/1070-game-oriented-matrix-original-frame-recovery-20261006.md).
The prior layout follow-up is in
[Note1069](WORKING_NOTES/1069-game-row-matrix-match-and-oriented-layout-20261006.md),
with the initial checkpoint in
[Note1068](WORKING_NOTES/1068-game-oriented-matrix-recovery-20261006.md).

## Scaled matrix compiler controls

[Driver](../tools/experiments/game_scaled_matrix_candidates.py):four explicit/
common-product and translation-order shapes across four actual-SDK profiles,
16 controls. Explicit element updates and translation-first order recover67
direct words/frame0x68 under O2/g3. No guards or shared profile/header changes.
[Twelve tests](../tools/tests/test_game_scaled_matrix_match.py) bind6480 paired
guest/full trace/storage cases,696 float edges,48 guest-only home probes,
3372 actual32-bit native caller cases, ten compiled negatives and a native
integer-load rejection. All12 arguments are typed; integer field loads must
not numerically convert raw float bits under the corrected declaration.
432 connected cases execute the original30-word caller and115-word converter
around both67-word bodies, restricted to finite exactly integral fixed values.
General rounding modes, FCSR flags, NaN/out-of-range conversion and the original
rotation provider remain outside that gate. Actual padder retains268 symbol
bytes, excludes the four-byte section alignment tail, and retargets both calls.
Copied owners preserve92 other builder functions and all31 caller functions/
relocations/pools, warnings2->2 in each. Production binds target, exact caller,
seven neighbors/the unchanged10809-row prefix plus two resolver-table bindings
and31 point-transform guards (10842 total). Ignored receipts:
`conker/build/game-scaled-matrix-test/`; see
[Note1067](WORKING_NOTES/1067-game-scaled-matrix-match-20261006.md).

## Scaled descriptor compiler controls

[Driver](../tools/experiments/game_scaled_descriptor_candidates.py):sixteen
aggregate/field-wise copy, integer/float literal, header-placement and constant-
read-order shapes across four actual-SDK profiles,64 controls. Aggregate copy,
integer literal `2 * width` and original header store order recover all80 words/
frame0x70 directly under O2/g3. No guards, profile/frame rewriting or shared
header changes. [Eleven tests](../tools/tests/test_game_scaled_descriptor_match.py)
bind10800 paired guest/full ordered trace/storage cases,2240 byte/float/constant
edges,28 guest-only private overlap/home probes,20992 actual32-bit native cases,
42 original jal/delay-pair cases and12 compiled negatives. Preserve opaque32-bit
word, low-byte slot, all76 descriptor bytes and the position-subrecord pointer.
Native padding61..63 is unspecified; arithmetic NaNs are classification-compared,
not FCSR/NaN-payload acceptance. Actual padding preserves320 bytes and five
HI16/LO16/call relocations, including alternate constant addresses with low-half
carry. Copied owner preserves92 other raw functions/relocations, original pool
and two warnings; production binds80 words, six neighbors and10809 unchanged
guards. Submit helper and connected caller continuations are bounded models,
not original helper/full-caller execution. Ignored receipts:
`conker/build/game-scaled-descriptor-test/`; see
[Note1066](WORKING_NOTES/1066-game-scaled-descriptor-match-20261006.md).

## Random descriptor compiler controls

[Driver](../tools/experiments/game_random_descriptor_candidates.py):sixteen
signed/unsigned descriptor, boolean and declaration-order shapes across four
actual-SDK profiles,64 controls. Unsigned-byte descriptor with branch-shaped
s32 boolean and original declaration order emits96 words/frame0x78 directly.
The signed SDK descriptor materializes six -1 values instead of255; retain
the shared SDK type and install a local layout, not six word guards.
[Eleven tests](../tools/tests/test_game_random_descriptor_match.py) bind6912
paired guest/full ordered trace/storage cases,944 byte/float edges,48 guest-only
home reload probes,57856 actual32-bit native cases,144 original call/delay-pair
cases and12 compiled negatives. Preserve two integer draws, unsigned%61,
masked second draw, separately rounded float operations, captured source+18
before float provider, and all16 arguments including the source+4 address.
Actual padding preserves384 bytes and four call relocations under alternate
targets; copied owner preserves92 other functions/relocations, pool and two
warnings. Production binds96 words, five neighbors and all10809 guards.
Native padding33/38/39 is unspecified. NaN results are classification-checked,
not NaN payload/FCSR acceptance; private-home mutations are guest-only. RNG and
submit helpers remain bounded models; caller tests execute original jal/delay
pairs in bounded wrappers, not complete original callers. Ignored receipts:
`conker/build/game-random-descriptor-test/`; see
[Note1065](WORKING_NOTES/1065-game-random-descriptor-match-20261006.md).

## Effect-record updater compiler controls

[Driver](../tools/experiments/game_effect_record_updater_candidates.py):eight
record-lifetime/cursor/scope shapes across four actual-SDK profiles,32 controls.
Minimal12-byte request and separate created-record lifetime recover80 words/
frame0x60;56 direct plus24 guards. Derivation closes the pre-allocation S0/S1/
S2 cycle, search-argument/payload scheduling, private cursor store/reload and
four private request offsets. No frame rewrite, insertion or omission.
[Eleven tests](../tools/tests/test_game_effect_record_updater_match.py) bind
7680 three-body guest/7680 native cases,1728 connected original-search cases,
3072 guest/1536 native checked-caller cases, private actor-home probes, full
selector width/guest-only unchecked index cases, ten negatives and actual
padding/alternate table relocation/stale guards. Copied owner preserves all
92 other raw functions and pool bytes, warnings3->2; production binds all80
words, four retained neighboring slots and the unchanged10785-row prefix.
Raw/native request tail bytes9..11 are indeterminate; compare all other
external storage. Normalized and retail compare complete traces and storage,
including those three bytes. Raw extra cursor reads bind exactly to SP-8 and
live T4. This is not raw full-trace identity or real allocator/link acceptance.
Ignored receipts: `conker/build/game-effect-record-updater-test/`; see
[Note1064](WORKING_NOTES/1064-game-effect-record-updater-match-20261006.md).

## Context-classifier compiler controls

[Driver](../tools/experiments/game_context_classifier_candidates.py):global/local
world reads and inside/outside defaults across four actual-SDK profiles,
16 controls; eight O2/g3 or O2 controls match57 words directly, no frame/guards.
[Eight tests](../tools/tests/test_game_context_classifier_match.py) bind
full32-bit inputs,15822 two-body guest cases,5308551 actual32-bit native
cases,2688 connected dispatcher cases, eight semantic negatives, strict guest
range/override gates and actual padding with alternate world/pool addresses.
Full-owner compile checks all150 table targets, six pool references, addend
0x218,608-byte private pool (eight final padding bytes), original640-byte
data owner, unchanged neighboring code/relocations and the same three warnings.
Compiler pool is discarded; no shared padding-tool or compiler-profile change.
Ignored receipts: `conker/build/game-context-classifier-test/`; see
[Note 1063](WORKING_NOTES/1063-game-context-classifier-match-20261006.md).
Dispatcher experiment now uses both typed classifier declarations.

## Actor-classifier compiler controls

[Driver](../tools/experiments/game_actor_classifier_candidates.py):eight
identity/default shapes across four actual-SDK profiles,32 controls. s32 local
under existing O2/g3 emits45 direct words, no frame or instruction guards.
[Eight tests](../tools/tests/test_game_actor_classifier_match.py) bind every
byte, exact read contract, full storage, native record alignments, connected
dispatcher, six negatives, production source/slots and both original table
owners. Actual padding maps four pool relocations with addends0/180; alternate
anchor tests prove signed-low carry handling. No private pool or padding may
replace the neighboring context table.16384 actual32-bit native cases and8192
two-body guest cases;4608 connected dispatcher cases.
Ignored receipts under `conker/build/game-actor-classifier-test/`; see
[Note 1062](WORKING_NOTES/1062-game-actor-classifier-match-20261006.md).
Dispatcher experiment uses the recovered actor-classifier prototype; the
context-classifier declaration was subsequently typed in Note1063.

## Effect-dispatch compiler controls

[Driver](../tools/experiments/game_effect_dispatch_candidates.py):eight
selector/cursor/loop forms across four actual-SDK profiles,32 controls, actual
function label; selected100-word/frame0x48 source derives75 direct/25 guarded
words. [Eleven tests](../tools/tests/test_game_effect_dispatch_match.py) bind
raw/normalized/retail,70848 actual32-bit native cases, full-storage live aliases,
registered cursor updates, connected retail classifiers/list search/caller,
semantic negatives, invalid/cyclic guest boundaries, actual padding and moved
HI/LO metadata. Alternate relocation addresses and stale guards are tested.
Explicit scoped helper-result sequencing follows a failed native callback-table
mutation check on the earlier nested-call source. Only one proven raw private
cursor reload site is removed from trace comparison; normalized traces compare
fully. Production guard prefix unchanged plus25, full slot/caller binding.
Ignored receipts under `conker/build/game-effect-dispatch-test/`; see
[Note 1061](WORKING_NOTES/1061-game-effect-dispatch-match-20261006.md).
This is not restored helper C, host adoption, hardware or gameplay acceptance.

## Historical effect-dispatch investigation receipts

[Note 1060](WORKING_NOTES/1060-game-effect-dispatch-investigation-20261006.md)
records112 ignored actual-SDK controls,13,824-case guest probes and69,632-case
connected classifier checks under
`conker/build/game-position-projection-test/next-effect-dispatch/`.
Selected100-word/frame0x48 body differs in21 words; a closed linked derivation
matches all retail words but is not an installed relocation-aware guard recipe.
Private cursor reloads are bound at one exact opcode/site; all other traces,
storage and calls compare independently. No broad stack filtering or raw-trace
identity claim for this source. Switch/list instructions execute; callbacks
remain bounded models. Native/negative/padder/production gates pending. These
are investigation receipts, not new maintained acceptance tests.

## Position-projection compiler controls

[Driver](../tools/experiments/game_position_projection_candidates.py): eight
scope/sum shapes across four SDK profiles and four typed-caller controls,
**36 controls**, no installation. Delta declarations before the matrix give
all 63 direct words/frame 0x80 under existing O2/g3; caller 16 body words plus
two zero padding words remains exact. [Nine tests](../tools/tests/test_game_position_projection_match.py)
bind actual source, complete production slots, call relocations and unchanged
10760 guards. Full-storage guest/native alias and mutation cases, connected
retail rotation/coordinate instructions with bounded finite trig responses,
typed caller, special-float direct bits and ten compiled semantic negatives.
Only arithmetic NaNs classify; no real trig/FCSR/hardware/gameplay or native
float-return claim. Guest saved-home mutation probes are not legal native
private-frame alias claims. Ignored receipts under
`conker/build/game-position-projection-test/`; see
[Note 1059](WORKING_NOTES/1059-game-position-projection-match-20261006.md).

## Historical position-projection investigation receipts

[Note 1058](WORKING_NOTES/1058-game-position-projection-investigation-20261006.md)
records60 ignored SDK compiler controls and two126-case guest probes under
`conker/build/game-actor-event-dispatch-test/`. The coordinate helper executes
40 retail words; rotation is a bounded identity provider. Fitting source fails
alias behavior; cached source passes this probe but exceeds the slot/frame.
These are investigation receipts, not maintained native/production acceptance
tests, an installed source recovery, or a word-normalization recipe.

## Actor-event dispatch compiler controls

[Driver](../tools/experiments/game_actor_event_dispatch_candidates.py):eight
selector/status/branch/address forms, four profiles, **32 controls**, actual SDK.
Selected unsigned N64 address subtraction gives55 direct words/frame0x18 under
existing O2/g3; no guards or driver installation. [Nine tests](../tools/tests/test_game_actor_event_dispatch_match.py)
bind full production source/slot/relocations and unchanged guard metadata;
60724 two-body guest and262144 actual32-bit native cases, repeated lookup,
byte command, live callback/event/status aliases and nine semantic negatives.
Saved-home/provider and invalid-target probes are guest-only; native table
aliases use native byte order. Helpers are bounded models, not complete
helper/hardware/gameplay acceptance. Ignored receipts under
`conker/build/game-actor-event-dispatch-test/`; see
[Note 1057](WORKING_NOTES/1057-game-actor-event-dispatch-match-20261006.md).

## Piecewise envelope compiler controls

[Driver](../tools/experiments/game_piecewise_envelope_candidates.py):
eight scope/sum forms, four profiles, **32 controls**. Branch-local factors
recover69 words/no frame;13 differences derive from four bounded closed FPR
cycles and commutative operands. No driver installation. [Nine tests](../tools/tests/test_game_piecewise_envelope_match.py)
bind actual padder/link/source/slot/metadata, full guest storage/accesses,
native live aliases, float boundaries, bounded loops and eleven negatives.
Only arithmetic NaNs classify; direct copies/untouched bytes exact. Reference-
budget cases are not native terminating-call acceptance; no N64 FCSR/exception/
flush-mode/gameplay claim. Ignored `conker/build/game-piecewise-envelope-test/`
receipts; see [Note 1056](WORKING_NOTES/1056-game-piecewise-envelope-match-20261006.md).

## Timed interpolation compiler controls

[Driver](../tools/experiments/game_timed_interpolation_candidates.py):
eight pointer/sample/tail forms, four profiles, **32 controls**. Explicit RNG
sample statements give59 words/frame0x30/nine private-home/commutative FP
differences under existing O2/g3; no driver installation. [Nine tests](../tools/tests/test_game_timed_interpolation_match.py)
derive all words, bind actual object padder/link/production metadata, qualify
full-storage/callback/access/saved-pointer and actual native-C behavior.
Special-float arithmetic NaNs are classified separately from exact untouched
storage; not N64 FCSR/exception/payload-propagation or gameplay acceptance.
Ten compiled negatives bind live callback reads and semantic boundaries.
Ignored receipts under `conker/build/game-timed-interpolation-test/`; see
[Note 1054](WORKING_NOTES/1054-game-timed-interpolation-match-20261006.md).

## Grid/channel updater compiler controls

[Driver](../tools/experiments/game_grid_channel_updater_candidates.py):
36 declaration/return and36 payload/loop forms, two profiles, **144 controls**.
Selected O2/g3 gives96 words/frame0x18/43 closed register/address-schedule
differences; no installation by the driver. Two register permutations plus
one independent LO16 schedule derive every retail word, including V0=4.
[Nine tests](../tools/tests/test_game_grid_channel_updater_match.py) bind actual
object relocation padding/linking, complete production slot/source/metadata,
144 controls,1728 three-body guest storage/trace cases, signed-bound/byte-wrap
edges,864 native actual-owner-body cases and ten compiled negatives. Shared
false global declarations are interpreted locally, not rewritten. Native
fixtures stay in valid storage; bound255 cycling is guest-only bounded
evidence, not a terminating/native/hardware/gameplay claim.
Ignored receipts under `conker/build/game-grid-channel-updater[-test]/`;
see [Note 1053](WORKING_NOTES/1053-game-grid-channel-updater-match-20261006.md).

## Payload-copy wrapper compiler controls

[Driver](../tools/experiments/game_payload_copy_wrapper_candidates.py):
six forms/four profiles plus four callee ABI forms/four profiles, **40 controls**.
Existing O2/g3 gives53 words/frame0x40/ten closed schedule differences;
callee pointer return gives28 direct words with unchanged instructions. No
driver installation. [Nine tests](../tools/tests/test_game_payload_copy_wrapper_match.py)
derive the index permutation and local branch targets, parse/apply/link actual
HI16 relocation movement, bind complete production slots and metadata.
Full guest storage/traces, byte pairs/live join/actual callee-constructor chain,
ten compiled negatives and132352 native cases qualify ordinary valid copies
and counter aliases. SDK/allocator leaves remain bounded hooks; no arbitrary
overlap/private-frame alias/hardware/dispatcher/gameplay/host qualification.
Ignored receipts under `conker/build/game-payload-copy-wrapper[-test]/`;
see [Note 1052](WORKING_NOTES/1052-game-payload-copy-wrapper-match-20261006.md).

## List-key sorter compiler controls

[Driver](../tools/experiments/game_list_key_sort_candidates.py)
screens six forms/four profiles: 24 controls, real SDK layouts/fixed table.
Selected O2/g3 gives 72 words/frame0x138 with18 register-lifetime differences;
no source/profile/guard installation by the driver.
[Eight tests](../tools/tests/test_game_list_key_sort_match.py) bind all controls,
complete production slot/body/prototype and register-only rewrite fields.
Independent stable sorting checks entire node/table footprints and ordered
guest accesses; native fixtures use independent array ordering with ordinal
ties. Every nonzero signed-halfword bypass and signed-value-high-half is swept.
Strict mapped guest fixtures preserve invalid null-head/sentinel walks instead
of adding safety changes. Not full corrupt-list, hardware-exception, dispatcher,
gameplay or sibling host qualification. Ignored receipts under
`conker/build/game-list-key-sort[-test]/`. See
[Note 1051](WORKING_NOTES/1051-game-list-key-sort-match-20261006.md).

## Basis-vector quad builder compiler controls

[Driver](../tools/experiments/game_basis_quad_builder_candidates.py)
screens six forms/four profiles: 24 controls, real SDK types/fixed anchors.
Selected O2/g3 emits 167 words/frame 0x68 with two independent load scheduling
differences; all six multiply operand orders and scalar lifetimes emit directly.
No source/profile/guard installation by the driver.
[Nine tests](../tools/tests/test_game_basis_quad_builder_match.py) bind controls,
complete source/linked slot and the exact two guards, full memory/access traces,
captured components, live translation/slot aliases and original-pointer return.
Actual 52-word buffer backend and 13-word owner wrapper execute in connected
guest fixtures; the optional null-fresh-flag backend store is unreachable for
this caller. Native full-storage fixtures check ordinary aliases; all 65536
signed-view values traverse the null path without basis/slot reads.
Eight compiled negatives distinguish memory/return and exact backend contracts.
SDK copy/allocation remain bounded providers, not full hardware FCSR/gameplay
or sibling host adoption. Ignored receipts under
`conker/build/game-basis-quad-builder[-test]/`. See
[Note 1050](WORKING_NOTES/1050-game-basis-quad-builder-match-20261006.md).

## Cached quad builder compiler controls

[Driver](../tools/experiments/game_cached_quad_builder_candidates.py)
screens six forms/four profiles: 24 controls, real SDK types/fixed anchors.
Selected O2/g3 gives 134 words/frame 0xD0, with only five independent
first-corner scheduling differences. Loop-local point scope recovers register
lifetimes and branch-delay update. No source/profile/guard installation by
the driver. [Six tests](../tools/tests/test_game_cached_quad_builder_match.py)
bind controls, complete production slot/source and the five guards; actual
40-word matrix assembly runs with the caller in two-body guest tests.
Full external memory/access traces and independent byte references qualify
fresh-copy slot reloads, live translations and escaped cursor mutations.
Native full-storage fixtures forward to recovered semantic matrix C; all
signed-view values are also swept through the null gate. SDK/backend/
orientation providers remain callbacks, not full hardware FCSR/gameplay or
host adoption. Ignored receipts `conker/build/game-cached-quad-builder[-test]/`.
See [Note 1049](WORKING_NOTES/1049-game-cached-quad-builder-match-20261006.md).

## Vertex attribute initializer compiler controls

[Driver](../tools/experiments/game_vertex_attribute_initializer_candidates.py)
screens six forms/four profiles: 24 controls with real SDK types/fixed anchors.
The direct byte-pointer loop emits all 48 words/frame zero under O2/g3;
intermediate flag writes and the final alpha-load/clear/store schedule are
preserved. The tool installs no source/profile/guards. Retail ROM, IDO and
MIPS tools required; ignored receipts under
`conker/build/game-vertex-attribute-initializer[-test]/`.
[Eight tests](../tools/tests/test_game_vertex_attribute_initializer_match.py)
bind all controls and installed source/slot, complete intermediate traces,
every halfword pattern, 19 table/output relationships and actual constructor/
two-helper chains. Native entry instrumentation forwards to both real helper
bodies; independent byte references check entire actor/input storage. Other
allocation/SDK/backend callbacks remain bounded, not full hardware/gameplay/
host adoption. See
[Note 1048](WORKING_NOTES/1048-game-vertex-attribute-initializer-direct-match-20261006.md).

## View corner initializer compiler controls

[Driver](../tools/experiments/game_view_corner_initializer_candidates.py)
screens ten forms/four profiles: 40 controls with real SDK types and fixed
anchors. A pointer ABI, explicit 12-byte table-record pointer, unsigned
halfword dimensions and shared word temporary emit all 55 words/frame eight
directly under O2/g3. No source/guard/profile installation by the driver.
Retail ROM, IDO and MIPS tools required; ignored receipts under
`conker/build/game-view-corner-initializer[-test]/`.
[Nine tests](../tools/tests/test_game_view_corner_initializer_match.py) bind
all controls and installed source/slot, index-255 no-access behavior, every
index/variant byte pair, unsigned dimension boundaries, all eight stores,
table/output aliases, and actual constructor/helper chains. Native fixtures
use the byte-exact equivalent file-scope table declaration to define storage;
only declaration scope changes, not the function's statements. Constructor
entry instrumentation forwards to actual helper C and independent reference
stores verify the complete actor. Backend/table providers remain callbacks,
not full hardware/gameplay/host adoption. See
[Note 1047](WORKING_NOTES/1047-game-view-corner-initializer-direct-match-20261006.md).

## Source effect constructor compiler controls

[Driver](../tools/experiments/game_source_effect_constructor_candidates.py)
screens 16 forms and six schedule forms under four profiles, plus nine
single-default ordering controls: 97 controls with real SDK types/fixed anchors.
Explicit flag sign-bit test, early default assignment and later byte +0xA0
clear emit all 114 words/frame 0x38 directly under O2/g3. No installation or
profile/guard changes by the driver. Retail ROM, IDO and MIPS tools required;
ignored receipts under `conker/build/game-source-effect-constructor[-test]/`.
[Nine tests](../tools/tests/test_game_source_effect_constructor_match.py)
bind all controls, complete source/linked slot, all flag branches, every byte
width, safe payload boundaries, helper/default mutations and inclusive live
bound. Guest traces cover all 114 words and 204 actual-wrapper path words.
Native actual C verifies whole storage and actual wrapper/construction/updater
publication; backend helpers remain callbacks, not complete FCSR/hardware/
gameplay/host adoption. The helper declaration/call now use the recovered
void/pointer/byte ABI; all 97 controls and 114 constructor words remain bound.
The attribute helper likewise uses its recovered void/two-pointer ABI.
Connected corner qualification is in Note 1047; both actual helpers together
are qualified in Note 1048. See
[Note 1046](WORKING_NOTES/1046-game-source-effect-constructor-direct-match-20261006.md).

## Source effect packet compiler controls

[Driver](../tools/experiments/game_source_effect_packet_candidates.py) screens
13 forms under four profiles plus 46 single-field ordering forms: 98 controls
with real SDK types and fixed anchors. Selected header order emits all 96
words/frame 0xA0 directly under O2/g3. The tool installs no source/profile/
guards. Retail ROM, IDO and MIPS tools required; ignored receipts under
`conker/build/game-source-effect-packet/`.
[Nine tests](../tools/tests/test_game_source_effect_packet_match.py) bind every
control and installed source/slot, compare full packet/call/memory traces for
three bodies, and exhaust lifetime/selector/channel widths and float boundaries.
Native opaque handoff and actual retained source-consumer C are qualified;
the recovered constructor is connected separately through success/failure
and source-pointer publication. Note 1045 records the earlier placeholder
checkpoint; Note 1046 owns its replacement. No full backend/FCSR/
hardware/gameplay/host adoption claim. See
[Note 1045](WORKING_NOTES/1045-game-source-effect-packet-direct-match-20261006.md).

## Source-backed actor packet compiler controls

[Driver](../tools/experiments/game_actor_source_packet_candidates.py) screens
14 forms under four profiles: 56 controls, real SDK types and fixed anchors.
Selected O2/g3 emits 102 words/frame 0xB8 with 14 opening-schedule differences.
The tool installs no source/profile/guards. Production uses relocation-aware
expected-word guards for only that closed reorder. Retail ROM, IDO and MIPS
tools required; ignored receipts under `conker/build/game-actor-source-packet/`.
[Eight tests](../tools/tests/test_game_actor_source_packet_match.py) bind all
controls and guard instructions/relocations, compare raw/guarded/retail full
packet/call/memory traces, all halfwords and floating-point boundary cases.
Native fixtures qualify initialized fields and whole storage, plus the actual
retained constructor/resource-helper C through success and allocation failures.
Snapshot the descriptor before its local lifetime ends; do not invent padding.
The constructor remains non-matching and backend providers remain callbacks,
not full caller/FCSR/hardware/gameplay/host adoption. See
[Note 1044](WORKING_NOTES/1044-game-actor-source-packet-byte-match-20261006.md).

## Effect-configuration packet compiler controls

[Driver](../tools/experiments/game_effect_configuration_packet_candidates.py)
screens eight forms under four profiles: 32 controls with real SDK types and
fixed anchors. A separate captured float local under O2/g3 emits all 69 words
directly. The tool installs no source/guards/profile. IDO, retail ROM and MIPS
tools required; ignored receipts under
`conker/build/game-effect-configuration-packet/`.
[Six tests](../tools/tests/test_game_effect_configuration_packet_match.py)
check the complete 60-byte packet, scalar narrowing, call-entry snapshots,
source/global aliases, post-capture mutations, saved registers and typed
32-bit native layout. Guest bit transport includes signaling NaNs without
FP arithmetic; native cases deliberately use finite/quiet-NaN patterns.
`func_15152190` is an opaque callback and remains a C placeholder in production.
No full effect-path/hardware/FCSR/gameplay/host claim. See
[Note 1043](WORKING_NOTES/1043-game-effect-configuration-packet-direct-match-20261006.md).

## Address-record allocator compiler controls

[Driver](../tools/experiments/game_address_record_allocator_candidates.py)
screens 12 forms under four profiles: 48 controls with real SDK types and
fixed retail anchors. Owner-before-flags O2/g3 emits all 37 words directly;
the tool installs no source, guards or profile. Retail ROM, IDO and MIPS tools
required; ignored receipts under `conker/build/game-address-record-allocator/`.
[Six tests](../tools/tests/test_game_address_record_allocator_match.py) bind
the direct wrapper and unchanged 28-word allocator/20-word list inserter.
Guest traces cover all halfwords and mode/channel pairs with high incoming
bits; native actual C verifies both allocator outcomes and all record/list
footprints. The native fixture uses one explicit 32-bit heap-address cast.
Heap remains opaque; sparse high context rows/self-head states are diagnostics,
not full caller/hardware/FCSR/gameplay or host adoption claims. See
[Note 1042](WORKING_NOTES/1042-game-address-record-allocator-direct-match-20261006.md).

## Conditional packet allocator compiler controls

[Driver](../tools/experiments/game_conditional_packet_allocator_candidates.py)
screens six forms under four profiles: 24 controls with real SDK/struct headers
and fixed retail anchors. Reserved-first O2/g3 emits all 38 words directly;
the tool installs no source, guards or profile. Retail ROM, IDO and MIPS tools
required; ignored receipts under `conker/build/game-conditional-packet-allocator/`.
[Six tests](../tools/tests/test_game_conditional_packet_allocator_match.py)
bind the direct wrapper and unchanged cleanup/allocator chains. Guest checks
include ordered calls/reads/stores, callback snapshots, allocation failure,
global/source aliases and copied untouched padding. Native actual wrapper/
cleanup C uses an opaque typed allocator and checks initialized fields without
inventing padding values. SDK/backend callbacks remain bounded models, not
hardware/gameplay/host adoption. See
[Note 1041](WORKING_NOTES/1041-game-conditional-packet-allocator-direct-match-20261006.md).

## Random selector/output compiler controls

[Driver](../tools/experiments/game_random_selector_outputs_candidates.py)
screens six forms under four profiles: 24 controls. A 32-bit selector under
O2/g3 emits all 37 words directly, retaining the callee's byte narrowing.
The tool installs no source, guards or profile; retail ROM, IDO and MIPS tools
required. Ignored receipts under `conker/build/game-random-selector-outputs/`.
[Six tests](../tools/tests/test_game_random_selector_outputs_match.py) bind the
direct wrapper, unchanged 31-word selector/18-word handwritten RNG and palette.
Ordered external traces, output aliases and call-entry snapshots are checked;
a local 64-bit guest extension executes the RNG without changing shared runners.
Native fixtures use the actual wrapper/selector C plus an independent RNG-state
model, not native execution of MIPS assembly. No hardware/FCSR/gameplay or host
adoption claim. See [Note 1040](WORKING_NOTES/1040-game-random-selector-outputs-direct-match-20261006.md).

## Actor position-queue wrapper compiler controls

[Driver](../tools/experiments/game_actor_position_queue_wrapper_candidates.py)
screens eight forms under four profiles: 32 controls with real SDK/actor
headers and fixed retail anchors. Plain typed O2/g3 emits all 37 words
directly. No source, guards or profile installed by the tool; retail ROM,
IDO and MIPS tools required. Receipts ignored under
`conker/build/game-actor-position-queue-wrapper/`.
[Seven tests](../tools/tests/test_game_actor_position_queue_wrapper_match.py)
bind the direct wrapper and unchanged helper, complete external guest traces,
signed argument homes, callback capture/mutations and connected queue stores.
Native cases use the actual complete actor and queue-record layouts plus
the retained writer C body. Raw float-bit transport is qualified, not FP
arithmetic/FCSR or gameplay. See
[Note 1039](WORKING_NOTES/1039-game-actor-position-queue-wrapper-direct-match-20261006.md).

## Alternate actor-dimension compiler controls

[Driver](../tools/experiments/game_actor_alternate_dimensions_candidates.py)
screens four forms under four profiles: 16 controls with real SDK/actor/point
headers. Six O2 forms match 41 body words plus two retail padding words; the
tool installs no source, guards or profile. Requires retail ROM, IDO and MIPS
tools; ignored receipts under `conker/build/game-actor-alternate-dimensions/`.
[Five tests](../tools/tests/test_game_actor_alternate_dimensions_match.py)
bind the complete slot/padding, local signed cast and unsigned shared field,
ordered guest traces/full footprints and actual C/real actor-prefix native
cases. Negative controls detect premature cached fields and unsigned +0xE8,
plus wrong threshold/dimension and stub. The preceding query's optional
offset/entry test helpers retain their old defaults. See
[Note 1038](WORKING_NOTES/1038-game-alternate-actor-dimensions-direct-match-20261006.md).

## Actor-dimension query compiler controls

[Driver](../tools/experiments/game_actor_dimensions_candidates.py) uses real
SDK/actor/point headers for four forms under four profiles: 16 controls.
Direct fields/cached ID/early return match under both O2 profiles; no source,
guard or profile is installed by the tool. Requires retail ROM, IDO and MIPS
tools; ignored `conker/build/game-actor-dimensions/` receipts.
[Five tests](../tools/tests/test_game_actor_dimensions_match.py) bind the
direct linked slot, sequential guest traces/complete footprints and the
actual C/real actor prefix in native cases. Negative controls detect wrong
ID threshold, unsigned fields, missing offset and the stub. Forty reachable
words execute; the impossible likely-branch delay word is structurally bound.
See [Note 1037](WORKING_NOTES/1037-game-actor-dimensions-position-direct-match-20261006.md).

## Projection-wrapper compiler audit

### Sphere wrapper and retained dependency

[Sphere driver](../tools/experiments/game_sphere_wrapper_candidates.py)
reproduces 24 source/profile controls. Selected wrapper emits 53 direct words
with its original `0x28` frame and sole call relocation; no new guards.
[Fourteen tests](../tools/tests/test_game_sphere_wrapper_match.py) qualify the
nine-position ABI, real 126-word callee/13-word dot helper, connected finite
geometry and output aliases, live parameter homes, seeded unordered/lazy
branches, native float staging, both original caller setups and delay stores,
effective compiled negatives, mapped-memory failures, copied owners/pools/
warnings/relocations and actual padder/alternate link targets. The callee C
trial remains uninstalled at 128 words/frame `0x68`; its bounded finite external
alias qualification does not establish the original private layout or byte fit.
Run `python3 -m tools.experiments.game_sphere_wrapper_candidates` to reproduce
the screen; ROM, IDO/MIPS tools and a 32-bit native compiler are required.
Ignored receipts live under `conker/build/game-sphere-wrapper/` and
`conker/build/game-sphere-wrapper-test/`. See
[Note 1083](WORKING_NOTES/1083-game-sphere-wrapper-direct-match-20261007.md).

### Fitting body and byte-match guards

[Schedule driver](../tools/experiments/game_projection_schedule_candidates.py)
retains32 order/add/product/profile controls and derives37 checked guards.
Selected C101 words/frame0x48,64 direct words; guards normalize temporary roles,
commutative operands and one closed four-word independent schedule. All nine
relocations remain at their original offsets/owners. No insertion, omission,
branch/frame, header/profile/helper or padder-algorithm changes.
[Sixteen match tests](../tools/tests/test_game_projection_schedule_match.py)
reuse lifetime qualification, compare raw/retail/guarded behavior and read
dependencies, close instruction inputs, exercise actual W/index-home overlap,
varied finite matrices and the original11-word caller, and pin copied-owner/
pool/relocation/padder/carry/stale/production boundaries. Requires ROM, IDO/MIPS
and32-bit native compiler. `python3 -m tools.experiments.game_projection_schedule_candidates`
reproduces the screen; ignored receipts under `conker/build/game-projection-schedule/`
and `conker/build/game-projection-schedule-test/`. See
[Note 1082](WORKING_NOTES/1082-game-projection-wrapper-match-20261007.md).

### Qualified lifetime recovery

[Lifetime driver](../tools/experiments/game_projection_lifetime_candidates.py):
`python3 -m tools.experiments.game_projection_lifetime_candidates` reproduces
140 O2/g3 lifetime forms with real headers; `--family initial` retains64
additional source templates and `--profiles` selects existing profiles.
The initial64 are not all measured by this recovery. No source/profile/guard
installation. Selected body102 words/frame0x48,46 differences; retail101.
Some controls intentionally alter alias behavior and are not qualified.
[Ten recovery tests](../tools/tests/test_game_projection_lifetime_recovery.py)
execute all58 original helper words, qualify optional outputs/live index/
pre-X Y capture/post-X reciprocal/view reads and actual32-bit native C, and
reject three compiled alias controls. These tests require ROM, IDO/MIPS tools
and the32-bit native compiler; ignored receipts are under
`conker/build/game-projection-lifetime/` and `game-projection-lifetime-test/`.
See [Note 1081](WORKING_NOTES/1081-game-projection-wrapper-lifetime-recovery-20261007.md).
Production stays the placeholder. Finite output/dependency qualification is
not identical raw read schedules, hardware/FCSR/NaN or gameplay acceptance.

### Earlier unqualified compiler audit

[Driver](../tools/experiments/game_projection_wrapper_candidates.py) runs
20 O2/g3 pointer-home/W/index-lifetime controls using real SDK/structure
headers. None matches; it installs no source, profile or guards. Requires
retail ROM, IDO and MIPS tools; ignored receipts under
`conker/build/game-projection-wrapper/`.
[Three tests](../tools/tests/test_game_projection_wrapper_audit.py) reproduce
all measurements and bind the retained 58-word synthetic-return helper chain
and the now-qualified production source/slot/guards. These are compiler/identity checks, not connected
execution or native/alias qualification. See
[Note 1036](WORKING_NOTES/1036-game-projection-wrapper-abi-and-frame-audit-20261006.md).

## Descriptor shape-measure compiler controls

[Measure driver](../tools/experiments/game_shape_volume_candidates.py)
uses the real SDK/descriptor headers for six box operand orders crossed with
two cylinder operand orders under four profiles: 48 controls. Only one O2/g3
form emits all 56 words directly. It installs no source, guards or profile;
requires retail ROM, IDO and MIPS tools. Receipts are ignored under
`conker/build/game-shape-volume/`.
[Six tests](../tools/tests/test_game_shape_volume_match.py) bind the complete
direct slot, corrected prototype/externs, actual descriptor layout and retail
coefficient words. Independent guest traces/native references preserve
wrapped box multiplication and per-operation float rounding; negative tests
detect the stub, unsigned halfwords, unmasked flags and premature float box
multiplication. Shared guest runners are unchanged. No caller-domain/gameplay
or complete FCSR qualification. See
[Note 1035](WORKING_NOTES/1035-game-descriptor-shape-measure-direct-match-20261006.md).

## Integer pair-clamp access controls

[Pair-clamp driver](../tools/experiments/game_integer_pair_clamp_candidates.py)
screens 23 forms under O2/g3, O2, O1/g3 and O1: 92 controls, empty compiler
diagnostics, no direct exact form. It installs no source, guards or profile.
Requires retail ROM, IDO and MIPS tools; receipts are ignored under
`conker/build/game-integer-pair-clamp/`.
`--register-lifetimes` separately screens 16 parameter-hint masks times
four local-hint groups under O2/g3 and O1/g3: 128 controls, receipts in
`conker/build/game-integer-pair-clamp-register-lifetimes/`. It does not
change the default 92-control inventory. See
[Note 1033](WORKING_NOTES/1033-game-integer-pair-clamp-register-lifetime-audit-20261006.md).
`--saved-registers` screens nine locally evidenced `-Wo` uopt options against
the recovered O2/g3 body; modes are mutually exclusive. Flags are passed only
to disposable candidate builds, not production. Receipts:
`conker/build/game-integer-pair-clamp-saved-registers/`. See
[Note 1034](WORKING_NOTES/1034-game-pair-clamp-saved-register-backend-audit-20261006.md).
[Nine recovery tests](../tools/tests/test_game_integer_pair_clamp_recovery.py)
bind the non-matching source/slot, compare complete guest access traces and
native footprints, and detect wrong clamp/swap controls. A local oracle adds
only XOR; shared runners remain unchanged. Explicit register-field renaming
proves correspondence of the 24-word operation core, not an installed
normalizer or whole-function match. The saved-pointer frame and return tail
remain open. See [Note 1032](WORKING_NOTES/1032-game-integer-pair-clamp-xor-access-recovery-20261006.md).
The additional register-lifetime test compiles all 128 forms, binds complete
word equality by profile/local group, and runs 1536 bounded corner traces.
The backend test checks all nine accepted controls and 108 corner traces;
`nordstore` changes only one closed temporary lifetime, while `noprecolor`
adds caller-home copies but no saved-pointer frame. No new match is inferred.

## Indexed state-save compiler controls

[State-save driver](../tools/experiments/game_indexed_state_save_candidates.py)
uses real actor/header definitions for eight forms under four profiles:
32 controls, ignored `conker/build/game-indexed-state-save/` receipts. It
installs no source, guards or profile. Requires retail ROM, IDO and MIPS tools.
[Eight state-save tests](../tools/tests/test_game_indexed_state_save_match.py)
bind the direct slot and unchanged exact callback, sequential byte traces,
opaque mutation, connected bit selection, zero-mask non-returning prefixes
and native footprints. Shared guest runners are unchanged; bounded diagnostic
indexes do not establish valid gameplay slots or portable out-of-bounds C.
See [Note 1031](WORKING_NOTES/1031-game-indexed-state-save-direct-match-20261006.md).

## Random-reload timer compiler controls

[Timer driver](../tools/experiments/game_random_reload_timer_candidates.py)
screens 19 forms under O2/g3, O2, O1/g3 and O1: 76 controls, ignored
`conker/build/game-random-reload-timer/` receipts. It installs no source,
guards or profile. Requires the retail ROM, IDO and MIPS binutils.
[Eight timer tests](../tools/tests/test_game_random_reload_timer_match.py)
bind the typed record/direct slot and compare three guest instruction bodies
with independent memory/call ordering, native footprints and break-7 cases.
The local oracle subclass adds only DIVU/MFHI/the exact trap; shared runners
are unchanged. No full dispatcher/RNG/gameplay or hardware trap claim.
See [Note 1030](WORKING_NOTES/1030-game-random-reload-timer-direct-match-20261006.md).

## Float-reference packet compiler controls

[Packet driver](../tools/experiments/game_effect_packet_wrapper_candidates.py)
screens six source forms under O2/g3, O2, O1/g3 and O1: 24 bounded controls,
empty diagnostics, ignored `conker/build/game-effect-packet-wrapper/` receipts.
It installs no source or profile. Requires the retail ROM, IDO and MIPS
binutils. [Eight packet tests](../tools/tests/test_game_effect_packet_wrapper_match.py)
bind source/production words/no guards, all 28 packet bytes and padding,
narrowing, native layout and connected original-retail-callee behavior.
Production checks also bind the unchanged callee to all 50 retail words.
Full wrapper/callee coverage does not qualify the complete allocator or
gameplay. See [Note 1029](WORKING_NOTES/1029-game-float-reference-packet-wrapper-direct-match-20261006.md).

## Zone selection compiler controls

[Edge lifetime driver](../tools/experiments/game_graph_edge_crossing_lifetimes.py)
adds 209 existing-profile source controls in eight modes: default layouts,
`--loops`, `--sides`, `--coordinates`, `--registers`, `--declarations`,
`--parameters`, or `--geometry`. Modes are mutually exclusive and each writes
a separate ignored JSON receipt under `conker/build/game-graph-edge-lifetimes/`.
It freezes the preceding 151-difference body; no experiment installs source
or permits oversized code. See
[Note 1026](WORKING_NOTES/1026-game-graph-edge-crossing-lifetime-improvement-20261006.md)
for the selected 207-word / 102-difference improvement and qualification limits.

[Linked-record tail driver](../tools/experiments/game_linked_record_tail_candidates.py)
freezes the original 71-word body and measures four store-volatility forms
under four backend profiles (16 controls), with ignored receipts. Its strict
normalizer binds the three compact words of the closed return-tail expansion;
it does not install source or enable oversized bodies. Six tests qualify
3360 three-way guest cases, actual emitter/relocation rejection and production
slot equality. See [Note 1028](WORKING_NOTES/1028-game-linked-record-position-tail-match-20261006.md).

[Scope driver](../tools/experiments/game_graph_edge_crossing_scopes.py) freezes
the 102-difference body and screens 101 named controls across default scopes,
`--planes`, `--aggregates`, `--sums` and `--products`. Each writes a separate
ignored receipt. `--verify-checkpoint` compares all live ELF slots with the
preceding ignored lifetime-test receipt and fails if absent or different.
Three tests bind transformation boundaries and inventory. No source is
installed. See [Note 1027](WORKING_NOTES/1027-game-graph-edge-crossing-scope-audit-20261006.md).

[Edge-crossing driver](../tools/experiments/game_graph_edge_crossing_candidates.py)
screens 39 source forms under the existing/default-unroll profiles, writing
78 records to ignored `conker/build/game-graph-edge-crossing/screen.json`.
It preserves the semantic baseline and marks minimum-result/narrowed-band
negative controls. Requires the retail ROM, IDO and MIPS binutils. It does not
install source or permit oversized bodies. See
[Note 1025](WORKING_NOTES/1025-game-graph-edge-crossing-recovery-20261006.md)
for the original recovery; Note 1026 supersedes its 151-word mismatch with
the current 102-difference form. The original 39-form inventory stays frozen.

[Root lookup driver](../tools/experiments/game_root_neighbor_lookup_candidates.py)
measures 35 source forms under both existing/default-unroll profiles and writes
70 records to ignored `conker/build/game-root-neighbor-lookup/screen.json`.
It preserves the pointer-based recovery and old typed placeholder; the
unsigned-index forms are signed-count negative controls. Requires the retail
ROM, IDO and MIPS binutils. See
[Note 1024](WORKING_NOTES/1024-game-root-neighbor-lookup-direct-match-20261006.md)
for the direct match; its geometric-helper placeholder is now superseded by
the non-matching recovery in Note 1025.

[Recovery driver](../tools/experiments/game_zone_neighbor_selection_candidates.py)
retains the original 29-form inventory and previous source checkpoint.
[Lifetime driver](../tools/experiments/game_zone_neighbor_selection_lifetimes.py)
adds 52 lifetime, 16 cursor and 23 register-hint controls without changing the
recovered query layout. Run the latter module normally, with `--cursors`, or
with `--registers`; mode switches are mutually exclusive. Each mode writes a
separate JSON receipt under ignored `conker/build/game-zone-neighbor-lifetimes/`.
Requires the extracted retail ROM, WSL IDO and MIPS binutils. Experiment output
does not install source, enable oversized bodies or count as a byte match.
See [Note 1023](WORKING_NOTES/1023-game-zone-neighbor-selection-lifetime-screen-20261006.md)
for measurements and qualification boundaries.

## Toolchain smoke test

Validate the project-native raw-object, minimal-ELF, and standard vertex
conversion helpers without a ROM:

```sh
make tools-check
```

The check creates an isolated seven-byte fixture, wraps it in a 16-byte-aligned
big-endian MIPS object, links it at `0x80000000`, validates both ELF files, and
checks known and malformed standard `Vtx` records. It writes only to the
system temporary directory.

The scripts use `mips-linux-gnu-` by default. Set `CROSS` to another MIPS
binutils prefix, including or omitting its trailing hyphen. `MIPS_AS` and
`MIPS_LD` can override the individual commands.

## Raw binary object wrapper

`tools/mkrawobject` converts an arbitrary file into a big-endian, 32-bit MIPS
relocatable object with a `.data` section:

```sh
tools/mkrawobject INPUT OUTPUT [ALIGNMENT]
```

The default alignment is `0x10`. The input is zero-padded to that boundary.
This is useful when a linker must consume an opaque extracted binary while
preserving an explicit N64 alignment.

Example:

```sh
tools/mkrawobject assets/debugger.us.bin build/debugger.us.o 0x10
```

The normal ROM build already wraps its checked-in binary assets directly with
GNU `ld -r -b binary`; do not replace those established Makefile rules merely
to use this helper. Use `mkrawobject` when section alignment or an independent
diagnostic object is specifically needed.

## Minimal ELF linker

`tools/mksimpleelf` links one MIPS object into a small executable ELF:

```sh
tools/mksimpleelf INPUT_OBJECT OUTPUT_ELF [BASE_ADDRESS]
```

The default base is zero. The linker script is generated in an isolated
temporary directory and retains `.text`, `.rodata`, `.data`, and `.bss`.
This is intended for inspection, conversion, and small tooling fixtures, not
as a replacement for `conker.ld` or the ROM linker scripts.

Example:

```sh
tools/mksimpleelf build/debugger.us.o build/debugger.us.elf 0x16000000
```

## Standard N64 vertex converter

`tools/vertconvert.py` converts packed standard 16-byte SDK `Vtx` records into
C initializers:

```sh
tools/vertconvert.py HEX_DATA
tools/vertconvert.py --file vertices.hex --array-name display_vertices
```

Input can contain whitespace, commas, underscores, and repeated `0x`
prefixes. A file may contain `dlabel` lines, which are ignored. With no
positional input or file, the tool reads standard input. It validates that the
input contains complete 16-byte records instead of silently discarding
malformed data.

The record layout is three signed 16-bit coordinates, a 16-bit flag, two
signed 16-bit texture coordinates, and four color/normal bytes. This helper is
useful for SDK-style display-list data and assembly-to-C work.

It is deliberately not an `assets13` decoder. Conker's verified model records
there contain only three signed 16-bit coordinates per six-byte vertex, with
no inline flag, texture coordinates, color, or normal. Use the decoder in
[Asset formats](ASSET_FORMATS.md#4a-model-geometry-assets13-vertex-arrays-confirmed)
for those records.

## Conker asset tools

Use the following tools for the current Conker formats:

- `tools/asset_dump.py` lists and extracts the master asset-table sections.
- `tools/rareunzip.py` and `tools/rarezip.py` decode and encode Conker's
  four-byte-size-header Rarezip blocks.
- `tools/extract_compressed.py` and `tools/compress_dir.py` implement the
  config-driven compressed-section workflow.
- n64splat's image handling and its `n64img` dependency should be tried first
  for standard N64 texture formats.

See [Asset formats](ASSET_FORMATS.md) and
[Compressed config sections](CONFIG.md) for the verified format details.

## Reference-only imported asset generators

The newly added `tools/assetmgr/` scripts and the top-level
`tools/mktextures` are not Conker asset builders. Their schemas and output
formats describe a different Rare N64 asset pipeline:

- they require a `ROMID`-keyed `src/assets/...` tree that this repository does
  not have;
- their compressor writes a `0x1173` marker and a three-byte size, while
  Conker Rarezip uses a four-byte big-endian size followed by raw DEFLATE;
- their language banks, pad/waypoint records, room tiles, animation tables,
  sequence tables, and texture manifests have no verified mapping to Conker's
  containers.

These entry points therefore stop with an incompatibility message by default.
For controlled cross-game format research only, set:

```sh
ALLOW_PD_ASSET_FORMATS=1
```

That opt-in does not make the formats Conker-compatible, and none of these
generators are part of the build graph. Do not publish generated Conker assets
from them without first documenting and verifying a real format mapping.

## Upstream submodules

`asm-differ`, `asm-processor`, `mips_to_c`, `n64splat`, `texture2c`, and
`ultralib` retain their upstream documentation. Project-specific usage and
format conclusions belong under `DOCS/`.
