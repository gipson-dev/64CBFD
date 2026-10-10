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
| Use Codex with selective Claude review | [Agent workflow](AGENT_WORKFLOW.md) and [handoff templates](AGENT_PROMPTS.md) |
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
- [Tools repository setup](TOOLS_REPOSITORY.md) - separate tools ownership,
  recursive checkout, migration, and pinned dependency updates.
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

- [Owner threshold curve frame and delta-Y fitting](WORKING_NOTES/1198-game-owner-threshold-curve-frame-and-delta-y-fitting-20261010.md):
  76 full forms qualify; nine tests pass. Original frame/saved homes/delta-Y store
  recovered, but188-word diagnostic overflows; private/read/full-word gaps remain.

- [Owner threshold curve recovery](WORKING_NOTES/1197-game-owner-threshold-curve-recovery-20261010.md):
  Complete func_151B3FDC diagnostic and nine passing tests; not installed or exact.
  Continue original frame/private homes/lifetimes/input schedule. No matching credit.

- [Linked owner position provider match](WORKING_NOTES/1196-game-linked-owner-position-provider-match-20261010.md):
  Complete func_151B3F28 installed; all45 words exact with narrow return/FP guards.
  Nine tests pass before/after; full owner/ELF/data audit passes. Game reaches57.02%.

- [Owner point arc byte match](WORKING_NOTES/1195-game-owner-point-arc-byte-match-20261010.md):
  Complete func_151B3CF0 installed; all 142 linked words exact via certified guards.
  Twelve tests pass before/after; whole ELF/data/history audit passes. Game reaches 57.00%.

- [Owner point arc certified branch fold](WORKING_NOTES/1194-game-owner-point-arc-certified-branch-fold-20261010.md):
  Guarded 142-word/frame136 diagnostic preserves private memory and six reads.
  All 60 combined tests and final twelve-test rerun pass. Raw C still overflows;
  102 differences remain. Tools c5260a6 first; not installed, no production credit.

- [Owner point arc endpoint-read recovery](WORKING_NOTES/1193-game-owner-point-arc-endpoint-read-recovery-20261009.md):
  Six single input reads with original frame/homes and full final memory retained.
  All 48 combined tests pass; 144-word overflow and scheduling remain, no production credit.

- [Owner point arc delta-Y home recovery](WORKING_NOTES/1192-game-owner-point-arc-delta-y-home-recovery-20261009.md):
  Original delta-Y and complete final private memory recovered; 36 combined tests pass.
  144-word overflow/four redundant start reads remain; production/totals unchanged.

- [Owner point arc saved and vector home recovery](WORKING_NOTES/1191-game-owner-point-arc-saved-and-vector-home-recovery-20261009.md):
  Original frame/saved homes/nine vector homes recovered; 25 combined tests pass.
  Delta-Y and 143-word overflow remain; no production or totals changes.

- [Owner point arc workspace and frame audit](WORKING_NOTES/1190-game-owner-point-arc-workspace-and-frame-audit-20261009.md):
  39 complete source forms / 48 profile combinations qualify in 14 combined tests.
  Frame coincidences/slot overflow remain rejected; no production or totals change.

- [Owner point arc recovery and helper audit](WORKING_NOTES/1189-game-owner-point-arc-recovery-and-helper-audit-20261009.md):
  Complete func_151B3CF0 contract passes ten tests; selected diagnostic is
  141 words/frame 0xD0/118 differences, not installed. Actual trig gaps are measured.

- [Owner point initializer guarded C match](WORKING_NOTES/1188-game-owner-point-initializer-guarded-c-match-20261009.md):
  Complete 157-word func_151B3A7C is installed and exact with 99 certified
  guards; fourteen installed tests and whole linked audit pass. Next 151B3CF0.

- [Owner point initializer zero-read and induction audit](WORKING_NOTES/1187-game-owner-point-initializer-zero-read-and-induction-audit-20261009.md):
  Remove extra public zero reads; twelve tests pass. Complete 158-word diagnostic
  is one word too long and remains uninstalled. Continue direct counter/end control.

- [Owner point initializer frame and private home fit](WORKING_NOTES/1186-game-owner-point-initializer-frame-and-private-home-fit-20261009.md):
  Complete157-word func_151B3A7C now has its original0x60 frame and actual private
  position/saved-FP homes. Eleven tests pass, including exact final private bytes
  and actual layout qualification.137 word differences remain; not installed/no
  credit. Continue integer induction, second-vector zeros and scheduling.

- [Owner point initializer recovery](WORKING_NOTES/1185-game-owner-point-initializer-recovery-20261009.md):
  Recover complete ten-point func_151B3A7C and registered callback contract.
  Nine tests pass, including 2,048 guest/8,192 native32 cases and constant aliases.
  Candidate fits 157 words but has frame 0x58 versus retail 0x60 and 143 differences;
  not installed/no credit. Continue the same routine's frame/private-home fit.

- [Owner ribbon renderer guarded C match](WORKING_NOTES/1184-game-owner-ribbon-renderer-guarded-c-match-20261009.md):
  Install full 475-word/frame 0x148 renderer with 161 certified relocation-aware
  allocation/scheduling guards. Eighteen installed tests pass; whole-ELF changes
  only target slot/st_size. Game 2,743/4,816 and total 3,416/5,489 exact, zero drift;
  no conversion credit. Next: adjacent func_151B3A7C point-preparation recovery.

- [Owner ribbon renderer shared copy and GPR proof](WORKING_NOTES/1183-game-owner-ribbon-renderer-shared-copy-and-gpr-proof-20261009.md):
  Full 475-word/frame 0x148 C recovers the initial shared copy base. Certify 107
  GPR allocation words; combined FP/GPR normalization leaves 44 differences.
  Fifteen tests and final composed-proof check pass. Not installed/no credit;
  continue setup and initial scheduling in the same complete renderer.

- [Owner ribbon renderer induction and FP proof](WORKING_NOTES/1182-game-owner-ribbon-renderer-induction-and-fp-proof-20261009.md):
  Complete 475-word/frame 0x148 C recovers original loop induction; 163 raw /151
  certified FP-normalized differences remain. Fourteen tests pass, including full
  normalized-body qualification and unsafe-map controls. Not installed/no credit.
  Continue the same renderer's initial copy base and remaining GPR/scheduling fit.

- [Owner ribbon renderer frame and slot fit](WORKING_NOTES/1181-game-owner-ribbon-renderer-frame-and-slot-fit-20261009.md):
  Complete475-word/0x148-frame C, original private homes,243 real differences
  remaining. Twelve tests pass, actual owner/padder accepts slot, not installed.
  Continue the same renderer's shared copy base, loop and FP/GPR fitting.

- [Owner ribbon renderer recovery checkpoint](WORKING_NOTES/1180-game-owner-ribbon-renderer-recovery-checkpoint-20261009.md):
  Complete nine-quad recovery; eleven tests pass, including actual material and
  full graphics walker. Selected477 words/frame304, not installed/no credit.
  Continue the same func_151B32C8 workspace/loop fit toward475 words/frame328.

- [Owner actor update direct match](WORKING_NOTES/1179-game-owner-actor-update-direct-match-20261009.md):
  All81 words emit directly, no guards; nine installed tests pass, including the
  original74-word registered walker. Only target ELF slot/size changes;
  no conversion credit. Next complete475-word renderer func_151B32C8.

- [Owner endpoint quad guarded C match](WORKING_NOTES/1178-game-owner-endpoint-quad-guarded-c-match-20261009.md):
  Match all340 words with84 certified GPR allocation guards; ten installed tests
  pass. Only target ELF slot/size changes; no conversion credit.
  Next81-word actor-update dispatcher func_151B3184, then renderer151B32C8.

- [Owner endpoint quad recovery and frame fit](WORKING_NOTES/1177-game-owner-endpoint-quad-recovery-and-frame-fit-20261009.md):
  Recover full340-word graphics callback and real dispatcher ABI; nine tests pass.
  Correct0xB8 frame,140 differences remain. No installation/credit; resume2974.

- [Owner companion setup guarded C match](WORKING_NOTES/1176-game-owner-companion-setup-guarded-c-match-20261009.md):
  Convert all176 words with69 certified private-home/prefix guards; nine installed
  tests pass. Whole ELF stays byte-identical; add704 converted bytes.
  Next340-word func_151B2974; hardware/full renderer gates remain open.

- [Owner companion setup recovery checkpoint](WORKING_NOTES/1175-game-owner-companion-setup-recovery-checkpoint-20261009.md):
  Recover two retained requests and a late40-byte effect; nine tests pass.
  Original176-word assembly stays installed, no new credit. Resume2690 fitting.

- [Owner link setup guarded C match](WORKING_NOTES/1174-game-owner-link-setup-guarded-c-match-20261009.md):
  Convert210-word original assembly with25 certified closed GPR guards;
  nine installed tests qualify raw holes and actual allocator-wrapper chain.
  Whole ELF remains byte-identical; add840 converted bytes. Next176-word2690.

- [Owner link allocator direct match](WORKING_NOTES/1173-game-owner-link-allocator-direct-match-20261009.md):
  Restore all53 words directly; eight installed tests qualify the mixed ABI,
  derived floats and actual setup chain. Game2,738/4,814 exact; setup fitting next.

- [Owner link setup recovery checkpoint](WORKING_NOTES/1172-game-owner-link-setup-recovery-checkpoint-20261009.md):
  Three-request semantics and allocator ABI recovered; five bounded tests pass.
  Stack/register fitting remains open, original210-word assembly retained.

- [Owner state callback direct match](WORKING_NOTES/1171-game-owner-state-callback-direct-match-20261009.md):
  Restore67-word callback directly/no guards and two falsely typed helpers
  as original assembly. Game2,737/4,814 exact; two fewer C conversion rows.
  Actual classifier/cleanup and registered dispatcher qualify mutation order;
  next recover210-word func_151B2348 as semantic C.
- [Owner descriptor constructor direct match](WORKING_NOTES/1170-game-owner-descriptor-constructor-direct-match-20261009.md):
  Restore all40 words directly, no guards; eight installed tests qualify
  raw holes/capture order, native32, connected caller/wrapper and whole ELF.
  Game exact2,736/4,816; next67-word descriptor consumer func_151B2100.
- [Endpoint-pair callback direct match](WORKING_NOTES/1169-game-endpoint-pair-callback-direct-match-20261009.md):
  Restore all39 words directly, no guards; eight installed tests qualify
  alias/reload behavior, native32, actual dispatcher and whole-ELF preservation.
  Game exact2,735/4,816; next same-owner constructor func_151B2060.
- [Ribbon alpha defined signed scaling](WORKING_NOTES/1168-game-ribbon-alpha-defined-signed-scaling-20261009.md):
  Remove negative signed-shift UB while preserving the already-exact15-word
  body and every ELF byte; seven tests, exhaustive guest/native32 values.
  No new credit. Next recover actual39-word callback func_151B2F04.
- [Ribbon effect constructor direct match](WORKING_NOTES/1167-game-ribbon-effect-constructor-direct-match-20261009.md):
  Install all107 retail words directly, no guards; eight tests qualify the
  mixed ABI, connected callees, native32 calls, rebases and whole-ELF audit.
  Game exact2,734/4,816; conversion rows and protected data unchanged.
- [Camera ribbon register exclusions](WORKING_NOTES/1166-game-camera-ribbon-register-lifetime-exclusions-20261009.md):
  Two passing tests exclude shared-phase/output-reuse layouts across18
  complete forms; retain the13-home primary and continue constructor recovery.
- [Current camera ribbon color homes/callback](WORKING_NOTES/1165-game-camera-ribbon-renderer-color-homes-callback-20261009.md):
  Complete545-word form matches13 private homes and retail save slots;
  directly typed537-word byte-buffer reference retains different saves.
  Twelve tests pass in212.922s; fresh primary rebases and tools426c56c.
  Raw matching and production installation remain open.
- [Current camera ribbon exit-flow qualification](WORKING_NOTES/1164-game-camera-ribbon-renderer-exit-flow-qualification-20261009.md):
  Complete 545-word short-input body fits the slot and retains five retail
  private slots with corrected active/cursor exit shapes. Four independent
  symbol sets qualify relocation behavior; twelve tests pass in145.688s.
  Tools8a71e51 banked first; raw matching/production installation remain open.
- [Current camera ribbon private slots/view staging](WORKING_NOTES/1163-game-camera-ribbon-renderer-private-slots-view-staging-20261009.md):
  Fourteen tests; five retail private slots and16-bit input retained in a
  complete547-word form. Color homes/register roles/raw matching still open.
- [Current camera ribbon retail frame/save slots](WORKING_NOTES/1162-game-camera-ribbon-renderer-retail-frame-save-slots-20261009.md):
  Two complete same-frame/save-slot forms and eleven passing tests; safe
  last-output scale reuse. Register roles/private layout/raw matching open.
- [Current camera ribbon lifetime qualification](WORKING_NOTES/1161-game-camera-ribbon-renderer-lifetime-qualification-20261009.md):
  Ten passing tests, typed/stride full bodies and128 nonlinear guest/native32
  cases per form; three unsafe decompiler negatives. Neither installed/exact.
- [Current camera ribbon frame fitting](WORKING_NOTES/1160-game-camera-ribbon-renderer-frame-fitting-20261009.md):
  Two complete0x120-frame forms qualified by eight tests; register layouts
  still differ, production uninstalled. Next recover S3 view/stride lifetime.
- [Current camera ribbon renderer recovery](WORKING_NOTES/1159-game-camera-ribbon-renderer-recovery-20261009.md):
  Full semantic candidate and nine passing tests; production remains exact
  assembly.547 words/frame0x130/443 raw differences; frame fitting open.
- [Latest record height response match](WORKING_NOTES/1158-game-record-height-response-match-20261009.md):
  Complete C143/frame0x58 linked exact with three closed guards; conditional
  snapshot, backwards integration, height query and six-argument responses.
  Entire ELF unchanged, one conversion row, actual nine-word response connected.
- [Previous record growth match](WORKING_NOTES/1157-game-record-growth-match-20261009.md):
  Complete C140/frame0x10 directly exact; conditional stack-step behavior,
  ordered integration/insertion/phase loops and the actual dispatch chain.
  Entire ELF unchanged, one conversion row, no new guards.
- [Previous record phase shaping match](WORKING_NOTES/1156-game-record-phase-shaping-match-20261009.md):
  Convert complete GLOBAL_ASM `func_15148DE0` to frameless C70, directly
  exact without guards. Entire ELF and all guards remain byte-identical;
  one conversion row changes. Nine final tests/native32/public aliases/
  complete successful timer-payload-leaf connection and 35 shared tests
  pass. Totals 5,487 converted/3,404 exact, zero drift. Tools 741b405
  first, exact parent pin second, no push. Next full C140 `func_151488C4`;
  conditional stack step and wider acceptance remain open.

- [Previous wrapped record step match](WORKING_NOTES/1155-game-wrapped-record-step-match-20261009.md):
  Convert complete GLOBAL_ASM `func_15148AF4` to frameless C44, linked
  exact with one commutative-add guard; raw C has one difference. Full ELF
  stays byte-identical, one conversion row changes. Eight focused tests,
  native32, live time alias and complete timer/payload/leaf connection pass.
  Totals 5,486 converted/3,403 exact, zero drift. Tools 919a0c1 first,
  exact parent pin second, no push. Next C70 callback `func_15148DE0`;
  wider callback/hardware/gameplay/graph gates remain open.

- [Previous payload callback update match](WORKING_NOTES/1154-game-payload-callback-update-match-20261009.md):
  Convert complete GLOBAL_ASM `func_15147EB8` to C97, linked exact with
  25 frame/return guards; raw is 25 differences. Full ELF byte-identical,
  one conversion row changes. Nine final tests/native32/connected timer
  updater/public aliases pass. Totals 5,485 converted/3,402 exact, zero
  drift. Tools a2e5ea7 first, parent pin second, no push. Next C44 candidate
  `func_15148AF4`; wider callback/hardware/gameplay/graph gates remain open.

- [Previous actor timer callbacks match](WORKING_NOTES/1153-game-actor-timer-callbacks-match-20261009.md):
  Complete void `func_15147740`, C100/frame0x20, linked exact with six
  guarded private spill accesses; raw C has six differences. Timer/selector/
  callback/cleanup order recovered. All other code/data and logical symbols
  preserved; precise ABS-symbol ordering swap audited separately. Totals
  5,484 converted / 3,401 exact, zero drift. Eight focused tests/native32/
  retail table identities and 25 shared tests pass. Tools b3086e2 first,
  parent pin second, no push. Next 97-word callback `func_15147EB8`;
  trail's 61 differences and wider acceptance remain open.

- [Previous actor graphics dispatch match](WORKING_NOTES/1152-game-actor-graphics-dispatch-match-20261009.md):
  Complete `func_15147C4C`, C52/frame0x38, directly byte-exact without
  guards; signed index, lazy optional word, live selector/table and distinct
  callback result recovered. Only target ELF slot/symbol size change;
  totals 5,484 converted / 3,400 exact, zero drift. Eight focused tests,
  native32, retail-table identities and 25 shared tests pass. Tools 7b88702
  first, parent pin second, no push. Next 100-word `func_15147740`;
  trail's 61 differences and wider acceptance remain open.

- [Previous effect allocation core match](WORKING_NOTES/1151-game-effect-allocation-core-match-20261009.md):
  Complete `func_15147A80`, C115/frame0x38, directly byte-exact without
  guards; request/header/optional record and live resource-count loop recovered.
  Corrected direct-call interfaces leave their instructions unchanged. Only
  core slot/symbol size change; totals 5,484 converted / 3,399 exact, zero drift.
  Tools 2807f51 first, parent pin second, no push. Next 52-word `func_15147C4C`;
  trail's 61 differences and wider acceptance remain open.

- [Previous effect-record constructor match](WORKING_NOTES/1150-game-effect-record-constructor-match-20261009.md):
  Complete `func_15147DA0`, C70/frame0x40, directly byte-exact without
  guards. Corrected caller prototype leaves its entire owner unchanged;
  `func_151DA6F8` remains 61 differences. Only callee slot/symbol size change.
  Totals 5,484 converted / 3,398 exact, zero drift. Tools 658b615 first,
  parent pin second, no push. Allocation/core/caller/hardware gates stay open.

- [Previous table-driven effect constructor restoration](WORKING_NOTES/1149-game-table-driven-effect-constructor-restoration-20261009.md):
  Complete semantic `func_151DA6F8`, C144/frame0xD0, improves 143 -> 61
  linked differences; still non-matching, no guards or progress credit.
  Only target slot/symbol size change; all other ELF bytes/data are unchanged.
  Tools 77001d3 first, exact parent pin second, no push. Continue its remaining
  layout/scheduling differences; wider acceptance remains open.

- [Latest random-effect timer restoration](WORKING_NOTES/1148-game-random-effect-timer-restoration-20261009.md):
  Complete void `func_151D9EB0` matches all 68 words directly, no guards;
  61 owner neighbors/data stay unchanged. Only target ELF slot/symbol size
  change; totals 5,484 converted / 3,397 exact, zero drift. Tools 061d223
  first, exact parent pin second, no push. Next false-zero 144-word
  `func_151DA6F8`; wider acceptance stays open.

- [Latest record constructor restoration](WORKING_NOTES/1147-game-record-constructor-restoration-20261009.md):
  Complete `func_151D71B0` matches all 45 words directly, no guards; typed
  caller bytes stay unchanged. All 23 owner functions exact. Only its ELF
  slot/symbol size change; totals 5,484 converted / 3,396 exact, zero drift.
  Tools ce159a5 first, exact parent pin second, no push. Next false-zero
  68-word `func_151D9EB0`; wider acceptance stays open.

- [Latest record actor position conversion](WORKING_NOTES/1146-game-record-actor-position-conversion-20261008.md):
  Complete `func_151D75C4` is C and matches all 88 words with six qualified
  frame guards. Full rebuilt ELF/data unchanged; totals 5,484 converted /
  3,395 exact, zero drift. Tools de603ef first, exact parent pin second, no push.
  Next false C constructor `func_151D71B0`, 45 words; wider acceptance stays open.

- [Latest record callback update conversion](WORKING_NOTES/1145-game-record-callback-update-conversion-20261008.md):
  Complete `func_151D7264` is C and matches all 81 words with nine qualified
  scheduling guards. Full rebuilt ELF/data unchanged; totals 5,483 converted /
  3,394 exact, zero drift. Tools f7272ba first, exact parent pin second, no push.
  Next retained 88-word `func_151D75C4`; linked/hardware/gameplay gates stay open.

- [Latest record ring renderer conversion](WORKING_NOTES/1144-game-record-ring-renderer-conversion-20261008.md):
  Complete `func_151D80C4` is C and matches all 405 words with 185 qualified
  GP/save/factor guards. Full rebuilt ELF/data unchanged; totals 5,482 converted /
  3,393 exact, zero drift. Tools 36bead0 first, exact parent pin second, no push.
  Next retained 81-word `func_151D7264`; linked/hardware/gameplay gates stay open.

- [Latest record ring renderer live-value proof](WORKING_NOTES/1143-game-record-ring-renderer-live-value-proof-20261008.md):
  Same complete uninstalled `func_151D80C4`, 405 words/frame0xD0/185 raw
  differences. Close factor-arm/delay reorder and conditionally check live
  values across 383 CFG nodes/404 words/560 obligations/six calls, with four
  independent rebases. 131,072 opacity pairs, 432 three-stream cases and 30
  distinct focused tests pass across selected runs. Installed state/README
  unchanged. Tools 4253f3a first, exact parent pin second; older dirty work
  preserved, no push. Normalization/private fault-state gates remain open.

- [Latest record ring renderer setup fitting](WORKING_NOTES/1142-game-record-ring-renderer-setup-fitting-20261008.md):
  Same complete uninstalled `func_151D80C4`, 405 words/frame0xD0, raw
  differences 198 -> 185 and retail mode-input order restored. 22 focused
  tests pass, including 432 whole-entry public prefixes, 668 early fault
  pairs and 16 output-equivalent mode-order negatives. Use SETUP_FITTED;
  GP-only +0x28C is part of the factor block, not a proven rename.
  Tools b0f5e40 first, exact parent pin second; installed state/README
  aggregates unchanged, older mirror preserved, no push. CFG/private-state/
  whole-body GP mapping remain gates before installation; wider gates open.

- [Latest record ring renderer scheduling audit](WORKING_NOTES/1141-game-record-ring-renderer-scheduling-audit-20261008.md):
  Same complete uninstalled `func_151D80C4`, 405 words/frame0xD0 and 198
  raw differences after 26 full forms. 25 tests pass, including 408 bounded
  post-MODE lookahead fault-prefix pairs and an ordinary-output-passing
  early-exit negative. 167 GP-only / 31 other is not a proven remap.
  Tools 1f3f5be first, exact parent pin second; installed state and README
  aggregates unchanged, older mirror preserved, no push. Next factor/setup
  schedule, full-entry/private fault state and closed mapping; wider gates open.

- [Latest record ring renderer frame fitting](WORKING_NOTES/1140-game-record-ring-renderer-frame-fitting-20261008.md):
  Same complete uninstalled `func_151D80C4`, now 405 words/frame0xD0 and
  retail private/saved slots; raw differences 319 -> 198. 21 tests pass,
  including 64 guest aliases and 768 independent rebased executions.
  Preserve all installed bodies/data/progress/guards and 22 neighbors.
  Tools 9d466ca first, exact parent pin second; older mirror preserved,
  no push or root README change. Next fit GP roles/schedule and qualify
  fault prefixes/closed transformations before installing; wider gates open.

- [Latest record ring renderer recovery](WORKING_NOTES/1139-game-record-ring-renderer-recovery-20261008.md):
  Complete uninstalled `func_151D80C4`, retail 405 words/frame0xD0;
  natural C 405/frame0xE0/319 differences. Nine tests pass; 1,086 native32
  cases and original render-table callback 16/actual backend qualify.
  Preserve 22 neighbors and all installed bodies/data/progress/guards.
  Tools a22175b first, exact parent pin second; older mirror preserved,
  no push. Counts unchanged; same target next for frame/lifetime fitting,
  aliases/rebases and installation gates. Linked setup and wider gates open.

- [Latest record ring shaping conversion](WORKING_NOTES/1138-game-record-ring-shaping-conversion-20261008.md):
  Complete `func_151D7CD0`, 253 words/frame0xB8; 183 direct plus 70 closed
  guards. Native32, private normalized state, fault traces and 13-site
  independent rebases qualify. All linked bodies/data unchanged; sole
  1,012-byte conversion. Eight installed tests and eleven affected checks
  pass. Tools 5c9e50b banked first, exact parent pin second; no push or older
  mirror reset. Next `func_151D80C4`, 405 words/frame0xD0; wider gates open.

- [Latest record ring shaping recovery](WORKING_NOTES/1137-game-record-ring-shaping-recovery-20261008.md):
  Complete uninstalled `func_151D7CD0`, retail 253 words/frame0xB8 versus
  natural C 256/frame0x98. Seven tests pass; third-table callback 4 and
  real helper connections qualify. The real padder rejects oversize.
  All installed bodies/data/progress/guards and README aggregates unchanged.
  Tools 856ba00 banked first, exact parent pin second; no push or older mirror
  reset. Fit this same target's extent/frame/lifetimes before installation;
  native32, rebases, graph repair and hardware/gameplay remain open.

- [Latest record ring sampling conversion](WORKING_NOTES/1136-game-record-ring-sampling-conversion-20261008.md):
  `func_151D7A38`, 166 words / frame 0xC8; 129 direct plus 37 closed guards.
  Seven installed tests and nine affected older checks qualify captured
  storage, interpolation, live signed ring updates and consumed callback result.
  All bodies/data unchanged; sole 664-byte conversion. Tools 9fb0eb2 banked
  first, parent pins it; no push or older standalone reset. Next retained
  `func_151D7CD0`, 253 words / frame 0xB8. Original dispatcher connection,
  linked restoration and hardware/gameplay remain distinct; graph refresh open.

- [Latest record ring update conversion](WORKING_NOTES/1135-game-record-ring-update-conversion-20261008.md):
  `func_151D792C`, 67 words / frame 0x30; 54 direct words plus 13 closed
  final-output guards. Eight installed tests and six affected older checks
  qualify signed/live ring state, captured storage and consumed callback return.
  All bodies/data unchanged; sole 268-byte conversion. Tools 74cbbdc banked
  first, parent pins it; no push or older standalone reset. Next retained
  `func_151D7A38`, 166 words / frame 0xC8. Original dispatcher connection,
  linked placeholder restoration and hardware/gameplay remain distinct;
  graph refresh remains open.

- [Latest attachment allocation direct conversion](WORKING_NOTES/1134-game-attachment-allocation-direct-conversion-20261008.md):
  `func_151D7830`, 63 words / frame 0x88 directly exact; no guards. Eight installed
  tests qualify packets, eleven arguments, allocation failure, captured lifetime
  and bounded original caller/constructor connections. All bodies/data/guards
  unchanged; sole 252-byte conversion. Tools 56c4132 banked first, parent pins it;
  no push or older standalone reset. Next `func_151D792C`, 67 words / frame 0x30.
  Linked constructor restoration, alternate branches and hardware/gameplay stay
  separate; graph refresh remains open.

- [Latest attached-record cleanup direct conversion](WORKING_NOTES/1133-game-attached-record-cleanup-direct-conversion-20261008.md):
  func_151D77C8,26 words/frame0 directly exact; typed void interface, captured
  nested link and live owner/flag writes qualify. All ten installed target/
  neighbor tests pass, all bodies/data/guards unchanged; sole104-byte conversion.
  Nextfunc_151D7830,63 words/frame0x88: packets/allocator/copy recovery pending.
  Tools6f18cf1 banked first, parent records exact pin, no push or older standalone
  reset; graph/hardware/gameplay remain open.

- [Latest record vertical velocity integration](WORKING_NOTES/1132-game-record-velocity-integrator-conversion-20261008.md):
  `func_151D8718`,19 words/frame0,16 direct plus three FP guards; mixed ABI,
  alias order, native32 and complete ring caller qualify. Eight installed tests
  pass; all bodies/data unchanged, sole76-byte conversion. Next26-word
  `func_151D77C8` needs return/cleanup/reload recovery. Hardware/FCSR and graph
  refresh remain open. Five affected checks pass; toolsf36e9af committed first,
  parent records the exact pin, no push or older standalone reset.

- [Latest record timer and player-state update](WORKING_NOTES/1131-game-record-state-update-conversion-20261008.md):
  `func_151D8A24`,64 words/frame0x28;60 direct words plus four private-byte
  guards. Timer/callback/live updates/free ordering qualify; all49 installed
  target/five-neighbor tests pass. All bodies/data unchanged;
  sole256-byte conversion. Tools8e1a208 banked first, parent pins it, no push. Next
  retained19-word `func_151D8718` has three raw differences, not qualified.

- [Latest record allocation and player registration](WORKING_NOTES/1130-game-record-player-registration-conversion-20261008.md):
  `func_151D8868`,111 words/frame0x30;109 direct words plus two guarded
  scheduling words. All41 fresh target/neighbor tests pass; complete predicate
  connection, mutations, native32, copied owner and rebases qualify. All
  bodies/data unchanged; two guards appended, sole444-byte conversion.
  Tools6e2e24d committed first, parent pins it, no push. Next retained64-word
  `func_151D8A24` candidate has four raw differences, not yet qualified.

- [Latest selected-player state direct conversion and banking](WORKING_NOTES/1129-game-selected-player-state-direct-conversion-20261008.md):
  `func_151D87E0`,34 words/frame0 directly exact; ordered selected mapping/
  flag reads and early returns qualify. Eight installed tests pass,173,184
  guest /3,608,576 native32 cases and bounded actual caller gate. All bodies/
  data/guards unchanged; sole136-byte conversion. Authorized tools/source
  checkpoint banks Notes1126-1129, no push. Next retained111-word full caller
  `func_151D8868`; positive continuation and wider gameplay remain open.

- [Latest record player-mask direct conversion](WORKING_NOTES/1128-game-record-player-mask-direct-conversion-20261008.md):
  `func_151D8B24`,25 words/frame0x20 directly exact; live mask/callback
  lifetime, actual clearer aliases and both complete direct callers qualify.
  Eight installed tests pass; all bodies/data/guards unchanged, sole100-byte
  conversion. Next34-word `func_151D87E0` has a direct complete candidate,
  pending qualification and installation.

- [Latest record distance-level direct conversion](WORKING_NOTES/1127-game-record-distance-level-direct-conversion-20261008.md):
  `func_151D8C00`,87 words/frame0x38 directly exact; typed layout/caller,
  complete unsigned conversion and wrapper connection qualify. All bodies/
  data/guards unchanged; sole348-byte conversion. Focused workflow, zero
  Claude calls; next25-word `func_151D8B24` live player-mask loop.

- [Latest embedded record callback conversion](WORKING_NOTES/1126-game-embedded-record-callback-direct-conversion-20261008.md):
  `func_151D8BE0`,8 words/frame 0x18 directly exact. Callback table/JALR and
  embedded+0x18 transport qualify; all bodies/data/guards unchanged. Eight
  post tests pass in 33.021s; focused workflow, zero Claude calls. External Git
  commits preserved. Next 87-word helper has a directly exact complete C
  candidate, but behavior/owner qualification and installation remain open.
- [Latest node group swap direct conversion and workflow](WORKING_NOTES/1125-game-node-group-swap-direct-conversion-20261008.md):
  complete `func_15033EC4`, 18 words/frame0 directly exact; full32 comparisons,
  byte swaps and captured-current/live-future links qualify. Eight post-install
  tests pass in 48.169s; all bodies/data/guards unchanged, only the 72-byte conversion
  changes. Focused gates/prior-receipt reuse, zero Claude calls. Graph refresh
  incomplete; no commit/push. Next retained 8-word `func_151D8BE0` wrapper.
- [Latest node group collector direct conversion](WORKING_NOTES/1124-game-node-group-collector-direct-conversion-20261008.md):
  complete `func_15033E28`, 23 words/frame0 directly exact, converting retained
  assembly rather than a placeholder. Per-node actor group and captured next
  preserve aliased output behavior. All bodies/data/guards stay unchanged;
  only the 92-byte conversion row changes. New baseline
  `game-node-group-collector-test/after.json`; next local `func_15033EC4`,
  retained assembly, 18 words/frame0. Mirrored tools changes uncommitted;
  complete caller/runtime and wider Game work remain open.
- [Previous effect callback scheduling match](WORKING_NOTES/1123-game-effect-callback-scheduling-match-20261008.md):
  complete `func_15033BDC`, 137 words/frame0x40 byte-exact, 135 directly
  emitted words and two independent scheduling guards. Actual Init callback
  ABI, volume/type/audio lifecycle and state-before-call qualify. Only target
  changes; data/conversions/prior guards intact. New baseline
  `game-node-effect-callback-test/after.json`; next local `func_15033E28`,
  retained assembly, 23 words/frame0. Mirrored tools changes uncommitted;
  full callees/runtime and wider Game work remain open.
- [Previous delayed effect direct match](WORKING_NOTES/1122-game-delayed-effect-direct-match-20261008.md):
  complete `func_15033AD8`,65 words/frame0x40 directly exact. Proximity-before-
  state, signed timer, twelve-word allocation and callback overwrite qualify.
  Only target changes; data/guards/conversions intact. New baseline
  `game-node-delayed-effect-test/after.json`; next local `func_15033BDC`.
  Tools working changes mirrored but uncommitted; full callees/runtime open.
- [Previous effect registration direct match](WORKING_NOTES/1121-game-effect-registration-direct-match-20261008.md):
  complete `func_150339C8`, all 68 words/frame0x40 directly exact. Tile scroll
  precedes mode/freeze gates; callback handle observations, clearing and
  signed16 effect creation qualify with connected guest/native checks.
  Only target changes; data/guards/conversions intact. New baseline
  `game-node-effect-registration-test/after.json`; next local `func_15033AD8`.
- [Previous attachment state latch direct match](WORKING_NOTES/1120-game-attachment-state-latch-direct-match-20261008.md):
  complete `func_15033838`, all 100 words/frame0x20 directly exact. Ordered
  activation/hold gates and callback latch lifetime qualify with guest/native,
  fault/alias/negative/owner/padder checks. Only target changes; data/guards/
  conversions intact. New `game-node-attachment-latch-test/after.json`;
  next local `func_150339C8`. Full callback/runtime work remains open.
- [Previous matrix creation and transform setup direct matches](WORKING_NOTES/1119-game-matrix-creation-and-transform-setup-direct-matches-20261008.md):
  complete caller/helper C113/frame0x168 andC45/frame0x20 directly exact.
  Live argument homes, matrix outputs, position reset and allocation/alias
  contracts qualify with connected guest/native checks; full matrix libraries
  remain open. Only two targets change; all data/guards/conversions intact.
  New `game-node-matrix-creation-test/after.json`; next local `func_15033838`.
- [Previous fourth tile scroll direct match](WORKING_NOTES/1118-game-fourth-tile-scroll-direct-match-20261008.md):
  complete semantic `func_150334B8`, all68 words/frame0 directly exact. Signed
  fourth-command scan and one-step coordinate wrap, no guards/new data.
  Guest/native/fault/alias/owner/padder checks qualify; only target changes.
  New baseline `game-node-tile-scroll-test/after.json`; next local placeholder
  `func_150335C8`,113 words/frame0x168. Full runtime remains open.
- [Previous attachment selection closed scheduling match](WORKING_NOTES/1117-game-attachment-selection-closed-scheduling-match-20261008.md):
  complete semantic C installed, all1148 words/frame0x48 exact with14 table
  bindings and67 closed scheduling guards, not a direct compiler-only match.
  All674 retained table targets fit; every instruction origin occurs once.
  Only target changes; sections/data/conversions unchanged. Its next local
  leaf is subsequently matched in Note1118; full runtime remains open.
- [Previous attachment selection frame and opening recovery](WORKING_NOTES/1116-game-attachment-selection-frame-and-opening-recovery-20261008.md):
  complete experimental C1148/frame0x48/319 differences; original private homes,
  first19 and final68 words exact. Twelve field-pointer forms retain identical
  emitted text/pools. Original model/flags scheduling and84 shifted table
  targets still block installation; production/README aggregates unchanged.
- [Previous attachment selection lifetime and table binding](WORKING_NOTES/1115-game-attachment-selection-lifetime-and-table-binding-20261008.md):
  complete experimental C1148/frame0x38/349 differences, A3 tail recovered.
  Seven original table addresses qualify with14 experimental rows, real padder,
  56 rebases and stale/effective controls;39 postprocessed neighbors unchanged.
  Frame/private scheduling and original target-PC compatibility still block
  installation. Production/README counts unchanged.
- [Previous attachment selection dispatcher recovery](WORKING_NOTES/1114-game-attachment-selection-dispatcher-recovery-20261008.md):
  complete qualified experiment-only C1147/frame0x38/394 differences; all model/
  action/type routes, callbacks/state/clamp, guest/native/fault/alias qualification.
  Owner measurement confirms the scalar gap. Production and aggregate counts
  unchanged; continue original frame/scheduling and physical table binding.
- [Latest fourth tile-size command direct match](WORKING_NOTES/1113-game-fourth-tile-size-command-direct-match-20261008.md):
  placeholder becomes exact C83/frame0, SDK Gfx/opcode scan, type/progress
  arithmetic and first-word-only update. No guards/profile edits; qualified
  guest/native/owner/padder/rebases, only target changes. Next large dispatcher
  has the experiment-only semantic recovery above; matching and full runtime stay open.
- [Latest node cleanup dispatcher direct match](WORKING_NOTES/1112-game-node-cleanup-dispatcher-direct-match-20261008.md):
  placeholder becomes exact C134/frame `0x38`, null actor gate, callback
  registration, private packet pair and final cleanup keys. Documented volatile
  pointer-home annotation; no guards/profile edits. Guest/native/owner/padder/
  rebase checks qualify; only target changes, full callbacks/PC-port stay open.
- [Latest node action dispatcher direct match](WORKING_NOTES/1111-game-node-action-dispatcher-direct-match-20261008.md):
  placeholder becomes exact C113/frame `0x28`, recovered void API, both switch
  tables, flag/counter mutations and callback ABI. No instruction guards or
  profile edits; fixed original table anchor, qualified guest/native/owner/
  padder/rebases. Only target changes; full callbacks/PC-port not qualified.
- [Latest attachment progress copy direct match](WORKING_NOTES/1110-game-attachment-progress-copy-direct-match-20261008.md):
  placeholder becomes exact C49/frame `0x30`, cached actor source, setup index
  gate, copy-induced pointer reload and inclusive float clamp. No guards/profile
  edits; guest/native/alias/fault/owner/padder qualification. Only target changes;
  setup remains a validating callback, not full callee or PC-port acceptance.
- [Latest attachment progress direct match](WORKING_NOTES/1109-game-attachment-progress-direct-match-20261007.md):
  placeholder becomes exact C43/frame `0x28`, setup gate and post-call home/
  pointer reload, binary32 threshold. No guards/profile changes; guest/native/
  owner/padder qualification, only target changes. Setup remains a validating
  callback; no full setup-callee or PC-port acceptance.
- [Latest matrix parent lookup direct match](WORKING_NOTES/1108-game-matrix-parent-lookup-direct-match-20261007.md):
  retained assembly becomes exact C28, no guards/profile changes; qualified
  group/key/ordinal reads, native32 and recursive connections. Linked bytes
  unchanged; conversion and byte-exact counts each gain one function / 112 bytes.
  Resolver C84/40 and its missing key move stay open.
- [Latest matrix-pair bank phase and key-lifetime fit](WORKING_NOTES/1107-game-matrix-pair-bank-phase-and-key-lifetime-fit-20261007.md):
  one-expression pointer addition closes four retail GP words directly;
  installed C84/40 remains one word short, no new guards/types/profiles.
  86 additional qualified controls, native/alias/home/owner/padder/caller gates;
  only four target words change, matching totals unchanged. V0 key move still open.
- [Previous matrix-pair resolver semantic recovery](WORKING_NOTES/1106-game-matrix-pair-resolver-semantic-recovery-20261007.md):
  installed complete recursive C84/frame `0x20`, four routes and original
  output/reread/home lifetime; slot85 with one padding nop, 44 differences,
  no new guards. Real wrapper/helpers/native/owner/padder qualification;
  only target changes, matching totals unchanged. V0 key source fit remains open.
- [Latest matrix-route register phases and branch source audit](WORKING_NOTES/1105-game-matrix-route-register-phases-and-branch-source-audit-20261007.md):
  experimental C119 recovers the retail opening, matrix A1 and complete shifted
  point loop with correct private addresses; key/primary topology still open.
  92 new controls, no raw match or installation; production C120/60 unchanged.
- [Latest matrix-route private-layout and semantic recovery](WORKING_NOTES/1104-game-matrix-route-private-layout-and-semantic-recovery-20261007.md):
  installed complete C120/frame `0xA0`, retail private matrix/resolver outputs;
  closes the sixteen old private counterexamples, no new guards. Sixty words
  still differ; key branch, primary read order and register phases remain open.
  Twenty combined tests pass; linked audit changes only target, totals unchanged.
- [Matrix-route recovery/private-frame audit](WORKING_NOTES/1103-game-matrix-route-recovery-and-private-frame-audit-20261007.md):
  complete experimental C119/frame `0xA8`/58 differences, 208 controls,
  original-helper/native/owner qualification and real private-overlap
  counterexamples. The production placeholder was unchanged at that checkpoint;
  Note 1104 supersedes the installed-source/private-layout handoff.
- [Latest lighting-dispatcher match](WORKING_NOTES/1102-game-lighting-dispatcher-match-20261007.md):
  complete 124-word actor/global/position dispatcher, two scheduling guards;
  bounded renderer hooks, not connected renderer or PC-port acceptance.
- [Vector-basis additional source controls](WORKING_NOTES/1101-game-vector-basis-coordinate-and-workspace-controls-20261007.md):
  186 controls, none exact; original assembly and private-layout boundary retained.
- [Vector-basis recovery/liveness audit](WORKING_NOTES/1100-game-vector-basis-recovery-and-liveness-audit-20261007.md):
  Complete experimental `func_15146078` C144/frame `0x48`/93 differences,
  real but publicly dead early byte values, original-helper/native/alias/caller
  qualification and explicit private-layout counterexamples. Original assembly
  remains installed; no new conversion or byte match. Linked snapshot and
  README aggregates stay unchanged. Continue source lifetime/layout recovery.

- [Latest matrix/list wrapper match](WORKING_NOTES/1099-game-matrix-list-transform-match-20261007.md):
  Complete C117/frame `0xA0`, both matrix routes, original local matrix and
  incoming-home reloads; nineteen GP/save/equality-operand guards, no private-
  offset/relocation/instruction edits. Guest/native/actual SDK/complete caller/
  home/private/equality/negative/owner/padder/relocation gates qualify; 182
  controls, none raw exact. Eight core pre-install tests pass in 315.497
  seconds, strengthened caller/SDK checks pass. Only target changes;
  other bodies/addresses/extents/overflows/data/prior guards intact.
  Exact total 3,363, Game 2,690, 2,103 different, zero drift; conversion
  unchanged. All 63 combined tests pass in 759.125 seconds, zero skips/errors/
  failures; tools/syntax/whitespace and 81-document / 3,947-relative-link checks
  pass, zero broken links. Next 148-word original-
  assembly `func_15146078`, translator/sampler still open.

- [Previous point-batch lifetime match](WORKING_NOTES/1098-game-point-batch-transform-lifetime-match-20261007.md):
  Complete C60/frame `0x98`, original matrix and lazy source reload;
  17 register-cycle/independent-store guards, no private-offset, FP-register,
  relocation or instruction edits. Guest/full-memory/home/native/private-
  overlap/negative/owner/padder/rebased-call gates qualify, 119 controls, none
  raw exact. Eight corrected pre-install tests pass in 128.524 seconds.
  Only target changes; other bodies/addresses/extents/overflows/data/prior
  guards intact. Exact total 3,362, Game 2,689, 2,104 different, zero drift;
  conversions unchanged. All 43 combined tests pass in 460.335 seconds, zero
  skips/errors/failures; tools/syntax/whitespace and 80-document /
  3,936-relative-link checks pass, zero broken links. Next 117-word matrix/list wrapper
  `func_15145EA4`, translator/sampler still open.

- [Previous point-list lifetime match](WORKING_NOTES/1097-game-point-list-transform-lifetime-match-20261007.md):
  Descriptor/input cursor phases recover C57/frame `0x88`, both incoming-list
  reloads and original private offsets. Nineteen closed register-cycle and
  independent prologue guards match all 57 words, no relocation/instruction
  edits. Guest/full-memory/home-readback/native/negative/owner/padder/rebased-
  call gates qualify; 40 new controls retained, none raw exact. Next contiguous
  point-batch transform `func_15145DB4`; translator/sampler remain open.
  Only target changes; other bodies/addresses/extents/overflows/data/prior
  guards intact. Exact total 3,361, Game 2,688, 2,105 different, zero drift;
  conversions unchanged. All 34 combined tests pass in 319.291 seconds,
  zero skips/errors/failures; tools/syntax/whitespace and 79-document /
  3,924-relative-link gates pass, zero broken links.

- [Previous matrix-scheduling / point-list lifetime audit](WORKING_NOTES/1096-game-matrix-scheduling-and-point-list-lifetime-audit-20261007.md):
  No new byte match or production change. 26 new translator controls and 48
  pointer-list loop/lifetime/readback measurements remain nonmatching. Guest/
  connected original-helper/native/negative gates qualify ordinary effects;
  incoming-home probes retain the open `func_15145CD0` lifetime boundary.
  Translator scheduling and sampler remain open; README aggregates unchanged.
  All linked slots/data/guards unchanged; 25 combined tests, strengthened gates
  and final nine-test audit pass; 78 documents / 3,910 relative links resolve.

- [Latest qualified matrix translation recovery](WORKING_NOTES/1095-game-matrix-translation-qualified-recovery-20261007.md):
  Correct high/low float stages, safe scaling/address wrap and sequential
  aliases; complete C49/frame0/no pool, no guards. **Not byte-exact**, 34
  differences remain; 152 controls/zero matches. Guest/native/original-parent/
  negative/owner/padder/relocation gates qualify. Only target changes; matching/
  conversions/README aggregates unchanged. Translator scheduling remains open.
  38 tests pass in 322.863 seconds; strengthened negative/tool/syntax/whitespace/
  77-document/3,897-relative-link gates pass, zero broken links.

- [Latest primitive-color direct match](WORKING_NOTES/1094-game-cached-primitive-color-direct-match-20261007.md):
  All 77 words/frame `0x8` direct under unchanged O2/g3, SDK macro, no guards.
  Six-field lazy gate, 48 controls/one fit; full-effect guest/native/incoming-
  home/negative/owner/padder/six-cache relocation gates qualify. Only target
  changes; all addresses/extents/data/guards intact. Exact total 3,360,
  Game 2,687 (56.06%), 2,106 different, zero drift. 23 tests pass in 269.557
  seconds; tools/syntax/whitespace and 76-document / 3,886-relative-link gates
  pass, zero broken links. Next 49-word translator;
  sampler remains unresolved/untouched, no new sampler measurements.

- [Latest environment-color match and sampler flow audit](WORKING_NOTES/1093-game-cached-environment-color-match-and-sampler-flow-audit-20261007.md):
  All 56 words/frame `0x8` direct under O2/g3, actual SDK macro, no guards.
  48 controls/one fit; guest/native/full-effect/copied-owner/padder/cache-relocation
  gates qualify. Only target changes; all addresses/extents/data/guards intact.
  Exact total 3,359, Game 2,686 (56.04%), 2,107 different, zero drift.
  50 tests pass in 336.828 seconds; tools/syntax/whitespace and 75-document /
  3,874-relative-link gates pass, zero broken links.
  Sampler's 54 flow/register controls all retain one RA reload versus three;
  behavior-qualified but uninstalled. Next 77-word primitive-color neighbor.

- [Latest oriented-matrix direct match](WORKING_NOTES/1092-game-oriented-matrix-direct-match-20261007.md):
  All 142 words/frame `0xB8` direct under unchanged O2/g3, original private
  offsets, no guards. Forty-eight meaningful controls/four direct fits;
  typed caller retains all eight raw owner functions. Guest/native/full-effect/
  private-overlap/copied-owner/actual-padder gates qualify. US ELF rebuilt;
  only target changes, all 6,042 retail addresses/extents remain fixed.
  Exact total 3,358, Game 2,685 (56.02%), 2,108 different, zero drift.
  All 64 focused tests pass in 353.549 seconds; final tools/documentation gates pass.
  Oriented layout complete; next sampler exit/RNG schedule or another Game function.

- [Latest actor-lookup direct match](WORKING_NOTES/1091-game-actor-lookup-byte-abi-direct-match-20261007.md):
  All 44 words/frame `0x18` direct under O2/g3, original byte helper ABI,
  no target guards. 62 controls/17 direct fits; guest/native/actual-helper,
  copied-owner/padder and full linked audits qualify. Target overflow removed;
  following body identical at -184 bytes with one collateral trampoline rebase.
  All retail addresses/extents fixed; exact total 3,357, Game 2,684 (56.00%).
  Sampler's 16 scalar-lifetime controls retain C252/109; do not install it.
  All 44 focused tests pass in 156.500 seconds; final tools/documentation gates pass.
  Next sampler exits/RNG schedule or oriented matrix (Note 1070).

- [Latest scaled-sphere direct caller match](WORKING_NOTES/1090-game-scaled-sphere-query-direct-match-20261007.md):
  Complete C110/frame `0x88`, all words direct under O2/g3, no target guards.
  Nested scale/reciprocal lifetimes recover the retail schedule and aliased capture.
  Three exact forms among 51 new controls; copied owner/pools/neighbors and real
  padded slot bind. US ELF rebuilt, only this slot changes. Exact total 3,356,
  Game 2,683; conversion/data/guards unchanged. All 112 tests pass in 688.694 seconds;
  final tool/syntax/whitespace and 72-document/3,826-link gates pass.
  Next after banking: still-open sampler `func_151432BC`.

- [Latest scaled-sphere capture-lifetime recovery](WORKING_NOTES/1089-game-scaled-sphere-query-capture-lifetime-20261007.md):
  New private-actor probes expose an old inverse spill overwriting aliased scale.
  Capture-first C corrects the observed outputs; 37,808 guest fixtures and
  126,720 native finite calls qualify, but 111 words still exceed retail 110.
  Thirty-nine new controls, no match; scoped source leaves a comparison NOP.
  Final regression passes 93 tests plus three binding/read/lazy-gate rechecks;
  retained slot/data/guard and tool/documentation audits pass.
  Resume from the improved body, keep the old one as a negative and finish
  fit/full-frame/install gates before changing production or counts.

- [Latest scaled-sphere caller boundary audit](WORKING_NOTES/1088-game-scaled-sphere-query-boundary-audit-20261007.md):
  27,440 guest fixtures now bind caller-local/home call snapshots; 126,720
  native finite calls include signed vertical offsets. Copied owner preserves
  88 neighbors/pools/relocations/two warnings. Thirty new controls retain no
  match; actual padder emits overflow. Keep placeholder/counts and finish the
  original-profile fit, full frame/read-timing and fitting-body install gates.

- [Latest scaled-sphere caller recovery](WORKING_NOTES/1087-game-scaled-sphere-query-recovery-20261007.md):
  Complete eight-position caller and five real helpers qualified in bounded
  guest/native cases. Original frame/private slots recovered, but 111 words
  versus retail 110; retain placeholder and counts. Next original-profile fit
  and stronger private/helper-frame/read-timing evidence before installation.

- [Latest sphere-callee allocation match](WORKING_NOTES/1086-game-sphere-callee-allocation-match-20261007.md):
  Semantic C replaces restored assembly; all 126 words/frame/private slots
  exact. 53 checked FP/schedule guards, 3,724 guest and 6,318 native finite
  cases. All linked slots preserved; conversion +1/504 bytes, Game exact
  2,682/4,793. Next recover the complete 110-word `func_15145AD8` placeholder.

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
| Tools repository checkout and ownership | `TOOLS_REPOSITORY.md` |
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

The `tools/` path is the pinned
[64CBFD-Tools](https://github.com/gipson-dev/64CBFD-Tools) repository. Its seven
upstream dependencies retain their own documentation. Do not move or rewrite
those READMEs as project documentation.
