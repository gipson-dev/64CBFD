# Documentation

## PC-port cross-project update - 2026-09-23

The sibling `64CBFDOGL` host port now completes Training through the natural Windy entrance and a fresh retained-save reload in RelWithDebInfo; repeat traversal used FLY. The user has **VERIFIED the second-level Chapters unlock**. The Gargoyle held-release repair uses original `func_15073A50` (232 bytes); guest/ROM builds and exact-byte checks are recorded in [host Note 738](../../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md). This is scoped progression evidence, not complete retail presentation or full-game acceptance.

The host-only `conker_settings.exe` is implemented with four-port device assignments, shared keyboard/controller bindings, Save and input hot reload; Video/Audio/Paths remain placeholders. It does not add an N64-ROM settings executable or replace Ares settings. See [host settings guide](../../64CBFDOGL/DOCS/CONKER_SETTINGS.md), [current host status](../../64CBFDOGL/DOCS/CURRENT_STATUS.md) and [active host roadmap](../../64CBFDOGL/DOCS/roadmap.md). Host Release is frozen after the requested 2026-09-23 `conker_pc` build; the latest Training suite retains its documented baseline failures/errors. No guest matching percentage is inferred from these host milestones.

Use this page as the documentation index. Each subject has one primary home so
build instructions, matching guidance, research notes, and milestone history
do not compete with one another.

## Start here

| Goal | Read this |
| --- | --- |
| Understand the repository and build it | [Project overview](PROJECT.md) |
| Resume the current decomp work | [Current status](CURRENT_STATUS.md) |
| Work specifically in `conker/` | [Code sub-project](CODE_SUBPROJECT.md) |
| Match or convert a function | [Contributor and byte-matching guide](CONTRIBUTING.md) |
| Inspect the latest headline progress | [Update log](UPDATE_LOG.md) |

New contributors should read the project overview first, then the contributor
guide. The root README is intentionally brief; `PROJECT.md` owns detailed build
and progress explanations.

## Build and development

- [Project overview](PROJECT.md) — prerequisites, repository layout, supported
  environments, ROM setup, normal builds, CI behavior, and progress metrics.
- [Code sub-project](CODE_SUBPROJECT.md) — the `init`, `game`, and `debugger`
  sections and how they are compiled and replaced in the ROM.
- [Contributor and byte-matching guide](CONTRIBUTING.md) — selecting work,
  comparing retail instructions, compiler-sensitive C patterns, validation,
  and clean commit scope.
- [Project tools](TOOLS.md) — local wrappers, smoke tests, toolchain
  overrides, active Conker asset utilities, and reference-only generators.
- [IDO 5.3 recomp toolchain](IDO_RECOMP.md) — reproducing the compiler used by
  byte-matching builds.

## ROM formats and research

- [Asset formats](ASSET_FORMATS.md) — `rzip`, archive tables, models, textures,
  audio, data tables, confidence levels, and open research questions.
- [Compressed config sections](CONFIG.md) — extracting and rebuilding chunks
  described by `config/*.yaml`.

Format conclusions belong in these durable pages once verified. Temporary
hypotheses and one-session diagnostics belong in working notes until they are
confirmed.

## Planning and history

- [Latest sphere-callee frame audit](WORKING_NOTES/1085-game-sphere-callee-frame-alias-audit-20261007.md):
  Complete private memory, ordered writes and helper homes checked in 2,700
  direct-helper cases against separate retail/trial layouts. Forty-eight new
  controls recover no match; original assembly/counts remain unchanged. Next
  original private allocation/lifetimes; external success is not frame equivalence.

- [Latest sphere-callee storage recovery](WORKING_NOTES/1084-game-sphere-callee-storage-recovery-20261007.md):
  `func_151452C4`, uninstalled 126 words/frame `0x70`, 60 differences and 64
  compiler controls. 2,808 finite external-alias cases pass, but a private-slot
  probe gives retail 24.0 versus C 10.0. Original assembly/counts remain intact;
  next recover original private storage and qualify incoming/private aliases.

- [Latest sphere-wrapper direct match](WORKING_NOTES/1083-game-sphere-wrapper-direct-match-20261007.md):
  `func_151451F0`, 53 direct words/frame `0x28`, nine-position ABI, live homes,
  no guards. Retained original callee/dot helper exact; only target across 6,059
  audited slots. All 49 focused post-link tests pass in 193.212 seconds,
  zero skips/errors/failures; final linked audit and documentation gates pass.
  Next: fit and qualify the uninstalled callee C conversion.

- [Latest projection-wrapper match](WORKING_NOTES/1082-game-projection-wrapper-match-20261007.md):
  `func_15144CEC`,101 words/frame0x48,64 direct words plus37 checked register/
  commutative/four-word-schedule guards. Guest/native/real-helper/caller/alias/
  operand/owner qualification; only target across6059 audited slots.
  All 206 tests pass in 1005.830 seconds, zero skips/errors/failures; final
  linked audit and documentation gates pass. Next 53-word `func_151451F0`.

- [Latest projection-wrapper lifetime recovery](WORKING_NOTES/1081-game-projection-wrapper-lifetime-recovery-20261007.md):
  `func_15144CEC`, qualified102-word/frame0x48 experiment versus retail101;
  six-position ABI, original private slots, real helper and live aliases.
  140 compiler forms, none exact. Production/counts remain unchanged;
  next recover the101-word fit and remaining word differences.

- [Latest point-transform assembly-to-C match](WORKING_NOTES/1073-game-point-transform-assembly-to-c-match-20261006.md):
  `func_15143134`,98 words/frame0x78, typed ABI and live diagnostics;31 checked
  saved-register allocation guards. All6059 linked slots unchanged; one more
  exact C conversion. Guest/native/original-helper/call-delay qualification.
  Next254-word descriptor sampler placeholder; oriented private offsets open.

- [Latest texture resolver match and table binding](WORKING_NOTES/1072-game-texture-resolver-match-and-table-binding-20261006.md):
  `func_1514306C`,50 C-emitted words/no frame; two checked relocations bind
  original jump-table data. Guest/native/full original cache caller and
  fail-closed pool/guard qualification. Only target across6059 audited slots.
  Next98-word original-assembly point-transform/status routine.

- [Latest texture-cache submission match](WORKING_NOTES/1071-game-texture-cache-submission-match-20261006.md):
  `func_15142E24`,102 direct words/frame0x40, no guards; typed attachment/source
  ABI and observable retail self-write. Guest/native/original resolver and
  call-delay pairs qualified; full6059-slot audit changes only target.
  Next50-word resolver remains placeholder; oriented private offsets stay open.

- [Latest oriented matrix original-frame recovery](WORKING_NOTES/1070-game-oriented-matrix-original-frame-recovery-20261006.md):
  in-place normalization recovers142 words/frame0xB8; only27 private direction/
  matrix offsets remain.128 controls/thirteen tests qualify six guest bodies
  and five native candidates. Still uninstalled; matching totals unchanged.

- [Latest row matrix match and oriented layout](WORKING_NOTES/1069-game-row-matrix-match-and-oriented-layout-20261006.md):
  `func_15142838`,55 direct words/frame0x58, no guards; typed caller stays
  24-word exact. Forty post-link tests pass. Oriented recovery now has64
  controls and qualified47/44 stack-only challengers, still uninstalled.

- [Initial oriented matrix recovery checkpoint](WORKING_NOTES/1068-game-oriented-matrix-recovery-20261006.md):
  two-point basis, scaling and caller ABI qualified in copies;142-word/frameB8
  candidate has84 differences, closer frameC8 candidate has57 stack-only
  differences. Maintained controls/native/guest/original caller-converter,
  padding and owner tests pass. Not installed or counted as a new match.

- [Latest scaled matrix match](WORKING_NOTES/1067-game-scaled-matrix-match-20261006.md):
  67 direct words/frame0x68, no guards; correct twelve-input pointer/float ABI,
  typed caller without guest-code changes, row/column products and translations.
  Native/guest, original caller/converter and actual padding qualified within
  documented bounds. Next142-word `func_15142600`.

- [Latest scaled descriptor match](WORKING_NOTES/1066-game-scaled-descriptor-match-20261006.md):
  80 direct words/frame0x70, no guards;76-byte descriptor, position copy,
  live original constants and five-argument submit. Native/guest, original
  call-delay pairs and actual padding qualified. Next67-word `func_151424F4`.

- [Latest random descriptor match](WORKING_NOTES/1065-game-random-descriptor-match-20261006.md):
  96 direct words/frame0x78, no guards;40-byte unsigned descriptor, ordered
  RNG/live reads and all16 submit arguments. Native/guest, original call-delay
  pairs and actual padding qualified. Next80-word `func_15142180`.

- [Latest effect-record updater match](WORKING_NOTES/1064-game-effect-record-updater-match-20261006.md):
  80 words/frame0x60,56 direct plus24 closed register/private-home guards;
  all-match refresh, create/copy/link failure gates, native/guest and checked
  caller qualification. Next96-word descriptor constructor `func_15141F78`.

- [Latest context-classifier match](WORKING_NOTES/1063-game-context-classifier-match-20261006.md):
  57 direct words, no frame/guards; world overrides/full-width context inputs,
  the original table at the shared pool's addend0x218, guest/native/connected
  qualification. Next80-word effect-record updater `func_15141E38`.

- [Latest actor-classifier match](WORKING_NOTES/1062-game-actor-classifier-match-20261006.md):
  45 direct words, no frame or new guards; both original switch tables preserved,
  guest/native and connected dispatcher cases. Next57-word context classifier
  has an initial direct candidate, not yet installed or qualified.

- [Latest effect-dispatch match](WORKING_NOTES/1061-game-effect-dispatch-match-20261006.md):
  100 words/frame0x48,75 direct plus25 guards; explicit native live lookup,
  repeated selectors and registered cursor mutations. Only target slot changes;
  next45-word `func_15141C0C` needs original switch-table-preserving recovery.

- [Historical effect-dispatch investigation](WORKING_NOTES/1060-game-effect-dispatch-investigation-20261006.md):
  100-word target,112 controls; fitting100/frame0x48/21 candidate and complete
  closed linked derivation. Guest/live cursor and connected classifier evidence;
  native, relocation-aware guards and production gates remain. Not installed.

- [Latest position-projection match](WORKING_NOTES/1059-game-position-projection-match-20261006.md):
  63 direct words/frame 0x80, no guards; float-height caller stays 18-word exact.
  Live guest/native aliases, connected retail SDK instructions and float boundaries.
  Next `func_15141A7C` (100 words/frame 0x48).

- [Historical position-projection investigation](WORKING_NOTES/1058-game-position-projection-investigation-20261006.md):
  63-word target,60 controls; cached origin reads fix tested alias behavior but
  the67-word/frame0x88 candidate still exceeds retail. No installation.

- [Latest actor-event dispatch match](WORKING_NOTES/1057-game-actor-event-dispatch-match-20261006.md):
  55 direct words/frame0x18, no guards;60724 guest/262144 native cases qualify
  byte ABI, repeated lookup and live status dispatch. Next `func_1514182C`.

- [Latest piecewise envelope match](WORKING_NOTES/1056-game-piecewise-envelope-match-20261006.md):
  69 words,56 direct plus13 FPR-lifetime guards; scoped factors recover rise
  scheduling, guest/native/live/float-boundary qualification. Next `func_151416E8`.

- [Earlier piecewise envelope investigation](WORKING_NOTES/1055-game-piecewise-envelope-investigation-20261006.md):
  69-word `func_151415D4`;32 controls,720 finite guest cases/eight bounded loops.
  Candidate still68 words; original source shape and remaining gates pending.

- [Latest timed interpolation match](WORKING_NOTES/1054-game-timed-interpolation-match-20261006.md):
  59 words,50 direct plus nine private-home/commutative FP guards; explicit RNG
  ordering, live fields and full-storage/access/native qualification.
  Next69-word `func_151415D4`:68-word preliminary candidate, not installed.

- [Latest grid/channel updater match](WORKING_NOTES/1053-game-grid-channel-updater-match-20261006.md):
  96 words,53 direct plus43 closed register-cycle/address-schedule guards;
  live signed coordinates/bounds/grid aliases and byte wrap, normalized V0=4.
  Next59-word `func_15141478`: nine remaining word differences, native/padder
  qualification pending; its production placeholder remains untouched.

- [Latest payload-copy wrapper match](WORKING_NOTES/1052-game-payload-copy-wrapper-match-20261006.md):
  53 words, 43 direct plus ten relocation-aware closed schedule guards;
  callee pointer ABI corrected with28 unchanged direct words, connected/native
  payload/counter qualification. Next `func_151412BC` grid lookup.

- [Latest list-key sorter recovery](WORKING_NOTES/1051-game-list-key-sort-match-20261006.md):
  72-word body/73-word slot; 54 direct instructions plus18 register-only
  guards and nop, stable keys and captured/live link qualification.
  Next `func_151407D0`; sibling cycle safeguards remain separate.

- [Latest basis-vector quad builder match](WORKING_NOTES/1050-game-basis-quad-builder-match-20261006.md):
  167 words, 165 direct plus two load scheduling guards; captured components,
  live translation aliases and actual owner/backend qualification.
  Next `func_151406AC`; sibling host adoption remains separate.

- [Latest cached quad builder match](WORKING_NOTES/1049-game-cached-quad-builder-match-20261006.md):
  134 words, 129 direct plus five scheduling guards; actual matrix callee,
  live fresh-copy/translation/cursor qualification. Next `func_15140410`.

- [Latest vertex attribute initializer direct conversion](WORKING_NOTES/1048-game-vertex-attribute-initializer-direct-match-20261006.md):
  Retained assembly converted to 48 direct C words; transient flags, signed
  colors and actual constructor/two-helper qualification. Next `func_15140190`.

- [Latest view corner initializer direct conversion](WORKING_NOTES/1047-game-view-corner-initializer-direct-match-20261006.md):
  Retained assembly converted to 55 direct C words; typed byte ABI, modulo
  dimensions and actual constructor/helper qualification. Next `func_151400D0`.

- [Latest source effect constructor direct match](WORKING_NOTES/1046-game-source-effect-constructor-direct-match-20261006.md):
  114 direct words; captured flags, live descriptor/helper/default/view contract
  and actual wrapper/updater qualification. Next inspect `func_1513FFF4`.

- [Latest source effect packet direct match](WORKING_NOTES/1045-game-source-effect-packet-direct-match-20261006.md):
  96 direct words; complete 88-byte descriptor and twelve-argument handoff.
  Next recover retained placeholder constructor `func_1513D2F0`.

- [Latest source-backed actor packet recovery](WORKING_NOTES/1044-game-actor-source-packet-byte-match-20261006.md):
  102 semantic words with 14 opening-schedule guards; full descriptor and
  conditional source-pointer copy. Next inspect `func_1519ED84`.

- [Latest effect-configuration packet direct match](WORKING_NOTES/1043-game-effect-configuration-packet-direct-match-20261006.md):
  69 direct words; complete 60-byte packet and separately captured float.
  Callee remains a C placeholder; next inspect `func_1519EB8C`.

- [Latest address-record allocator direct match](WORKING_NOTES/1042-game-address-record-allocator-direct-match-20261006.md):
  37 direct words; seven-argument pointer ABI, retained allocation/list linking.
  Next qualify `func_1519EA78`'s configuration-packet wrapper.

- [Latest conditional packet allocator direct match](WORKING_NOTES/1041-game-conditional-packet-allocator-direct-match-20261006.md):
  38 direct words; post-cleanup gate, failure publication and untouched padding.
  Next qualify `func_1519E970`'s seven-argument record allocator.

- [Latest random selector/output direct match](WORKING_NOTES/1040-game-random-selector-outputs-direct-match-20261006.md):
  37 direct words; seven-pointer ABI, third RNG and sequential palette stores.
  Next qualify `func_1519E6BC`'s conditional allocation/packet contract.

- [Latest actor position-queue wrapper direct match](WORKING_NOTES/1039-game-actor-position-queue-wrapper-direct-match-20261006.md):
  37 direct words; signed coordinates, actor float capture and connected queue.
  Next recover `func_1518E5D8`'s RNG/selector/output contract.

- [Latest alternate actor-dimension direct match](WORKING_NOTES/1038-game-alternate-actor-dimensions-direct-match-20261006.md):
  41 direct words plus two retail padding words; signed +0xE8 view and ordered
  aliased outputs. Next qualify `func_1517D5FC`'s queue handoff.

- [Latest actor-dimension/position direct match](WORKING_NOTES/1037-game-actor-dimensions-position-direct-match-20261006.md):
  41 words directly; signed dimensions, ordered alias-sensitive XYZ stores.
  Next independently qualify the adjacent `func_1515C244` twin.

- [Latest projection-wrapper ABI/frame audit](WORKING_NOTES/1036-game-projection-wrapper-abi-and-frame-audit-20261006.md):
  20 controls, no match/source installation; retained helper identity verified.
  Next inspect `func_1515C1A0`; wrapper execution qualification remains open.

- [Latest descriptor shape-measure direct match](WORKING_NOTES/1035-game-descriptor-shape-measure-direct-match-20261006.md):
  all 56 words directly, signed/wrapped dimensions, masked dispatch and ordered
  float work; no guards/profile. Next inspect the adjacent projection wrapper.
- [Latest pair-clamp backend audit](WORKING_NOTES/1034-game-pair-clamp-saved-register-backend-audit-20261006.md):
  nine accepted controls, frame still open, no production change. Next
  qualify the adjacent descriptor-measure recovery.
- [Latest pair-clamp register-lifetime audit](WORKING_NOTES/1033-game-integer-pair-clamp-register-lifetime-audit-20261006.md):
  128 source/profile controls, no direct match or production change.
  Saved-pointer frame and return-tail work remains open.
- [Latest integer pair-clamp access recovery](WORKING_NOTES/1032-game-integer-pair-clamp-xor-access-recovery-20261006.md):
  ordered XOR exchange recovered; 24576 guest and 12288 native cases.
  Still non-matching at 36 differences; saved-pointer frame and return tail
  remain open. No new guards or profile, aggregate counts unchanged.
- [Latest indexed state-save direct match](WORKING_NOTES/1031-game-indexed-state-save-direct-match-20261006.md):
  all 38 words under existing O2/g3; correct two-scale indexing, sequential
  overlap and connected bit-selector/zero-mask boundary qualification.
- [Latest random-reload timer direct match](WORKING_NOTES/1030-game-random-reload-timer-direct-match-20261006.md):
  all 39 words from typed C; wrapped countdown, unsigned remainder,
  post-callback fields and bounded zero-divisor trap qualification.
- [Latest float-reference packet wrapper direct match](WORKING_NOTES/1029-game-float-reference-packet-wrapper-direct-match-20261006.md):
  all 37 words directly under existing O2/g3; bounded packet/native and
  connected-retail qualification; unchanged production callee already 50/50 exact.
- [Latest linked-record position tail match](WORKING_NOTES/1028-game-linked-record-position-tail-match-20261006.md):
  all 72 linked words exact through three closed-layout guards and one RA
  insertion; 3360 guest cases, source unchanged and 6058 other slots intact.
- [Latest graph edge-crossing scope audit](WORKING_NOTES/1027-game-graph-edge-crossing-scope-audit-20261006.md):
  101 rejected source controls, unchanged 102-difference baseline and 6059 slots;
  next inspect the closest remaining C match's return tail.
- [Latest graph edge-crossing lifetime improvement](WORKING_NOTES/1026-game-graph-edge-crossing-lifetime-improvement-20261006.md):
  151 to 102 real differences, full 207-word body and matched outer loop;
  the retail frame and floating-register lifetimes remain open.
- [Latest graph edge-crossing recovery](WORKING_NOTES/1025-game-graph-edge-crossing-recovery-20261006.md):
  complete semantic body, retail last-fraction quirk, measured 151-word
  mismatch and remaining frame/lifetime work. Not a completed byte match.
- [Current decomp status](CURRENT_STATUS.md) — measured build, conversion,
  byte-matching, dirty-tree, and immediate resume boundary.
- [Numbered working notes](WORKING_NOTES/) — concise session handoffs beginning
  with the 2026-09-24 status audit and candidate queues.
- [Temporary Banjo cross-port TODO](TEMP_BANJO_CROSSPORT_TODO.md) — five
  completed port batches, including the US v1.0/v1.1 normalized-block and
  shared-fragment recheck, plus retained source-shape references.
- [Temporary DK64 cross-port TODO](TEMP_DK64_CROSSPORT_TODO.md) — verified
  DK64 retail-body audit, three port batches, broadened structural pass,
  matcher correction, four additional divergent audio matches, residual
  references, and the current cross-game continuation checkpoint.
- [Temporary debugger byte-matching TODO](TEMP_DEBUGGER_TODO.md) — live
  173/181 checkpoint, remaining function queue, SDK source mappings, and
  compiler-shape experiments needed to finish the debugger overlay.
- [64CBFDOGL function pull](64CBFDOGL_FUNCTION_PULL.md) — extracted
  host-recomp hand-port bodies from the sibling PC port, mapped back to
  64CBFD owner files for reference-only matching work. Snapshot caveat:
  the 2026-07-26 pull predates the 2026-08-16 OGL logo/menu animation repair;
  `func_1505E650` is already exact retail assembly in this repo, while the
  RT64 float-matrix repair is host-side and not portable to IDO C.
- [PC port roadmap](PC_PORT_ROADMAP.md) — phased plan for a native port and
  later modernization work.
- [Update log](UPDATE_LOG.md) — repository-facing milestones, workflow changes,
  and published progress snapshots.
- [Working notes](WORKING_NOTES.md) — recovery notes, failed experiments, and
  detailed session history. This is an archive and scratchpad, not onboarding
  documentation.

## Where information belongs

| Information | Primary file |
| --- | --- |
| Installation, build, CI, repository layout | `PROJECT.md` |
| Function conversion and byte matching | `CONTRIBUTING.md` |
| Local tool usage and compatibility | `TOOLS.md` |
| `conker/` section build mechanics | `CODE_SUBPROJECT.md` |
| Confirmed ROM and asset behavior | `ASSET_FORMATS.md` or `CONFIG.md` |
| Future PC-port decisions | `PC_PORT_ROADMAP.md` |
| Completed milestones and public changes | `UPDATE_LOG.md` |
| Temporary findings and abandoned attempts | `WORKING_NOTES.md` |
| Current decomp handoff and next boundary | `CURRENT_STATUS.md` and `WORKING_NOTES/` |
| Banjo cross-port sweep and residual references | `TEMP_BANJO_CROSSPORT_TODO.md` |
| DK64 cross-port sweep and residual references | `TEMP_DK64_CROSSPORT_TODO.md` |
| Active debugger byte-matching handoff | `TEMP_DEBUGGER_TODO.md` |
| 64CBFDOGL hand-port reference bodies, with 2026-08-16 stale-snapshot caveat | `64CBFDOGL_FUNCTION_PULL.md` |

The `tools/` subdirectories are mostly submodules and retain their own upstream
documentation. Do not move or rewrite those READMEs as project documentation.
