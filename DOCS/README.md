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
- [Reverse engineering setup](REVERSE_ENGINEERING_SETUP.md) - verified REA
  connection, scoped CLI environment and current Windows/MIPS adapter limits.
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

- [List record image sampler](WORKING_NOTES/1717-list-record-image-sampler-match-20261024.md):
  56 words/frame zero/eight bindings directly from C, no guards. Preserve
  signed bounds, live RGBA16 buffer reads and halfword-only record updates;
  type the scheduler caller without changing its complete object. Both copies
  pass six fresh prechecks, two fresh installed checks and four fingerprinted
  reuses, including constructor-layout regression. Strict 152-byte image,
  zero exclusions; adopted-ELF total 68.90%, 336 more to 75%. Full scheduler,
  hardware/gameplay and host acceptance remain outside this bounded proof.
- [List record constructor](WORKING_NOTES/1716-list-record-constructor-match-20261024.md):
  45 words/frame 32 directly from C, three bindings and zero guards; captured
  tail publication, partial initialization, late homes and typed caller/allocator
  ABI. Both copies pass six fresh prechecks, then two fresh installed checks and
  four fingerprinted reuses. Preserve seven neighbors, one GLOBAL_ASM and strict
  127-byte image, zero exclusions. Adopted-ELF total 68.88%, 337 more to 75%;
  deeper allocator/gameplay and the host remain outside this bounded proof.

- [Extended identity event](WORKING_NOTES/1715-extended-identity-event-match-20261024.md):
  45 words/frame 24, eleven checked guards, both release commands and the
  real 14-entry flag-gated dispatcher. Both copies pass eight fresh prechecks,
  then two fresh installed checks and six fingerprinted reuses. Preserve 43
  neighbors and strict 125-byte image, zero exclusions. Adopted-ELF total
  68.86%, 338 more to 75%; guarded C, not gameplay acceptance.
- [Record identity event](WORKING_NOTES/1714-record-identity-event-match-20261024.md):
  43 body words/frame 24, eleven checked role/read-order guards, canonical
  record dispatch and strict 119-byte image. Both copies pass eight fresh
  prechecks, then two fresh installed checks and six fingerprinted reuses.
  Adopted-ELF total 68.85%, 339 more to 75%; not compiler-only or gameplay proof.
- [Lifetime envelope ramps](WORKING_NOTES/1713-lifetime-envelope-ramps-match-20261024.md):
  45 words/frame zero, two checked multiply guards, both copies' fresh suites,
  original caller windows and strict 122-byte image. Adopted-ELF total 68.83%,
  340 more to 75%; guarded C, not compiler-only or gameplay acceptance.
- [Attachment identity event](WORKING_NOTES/1712-attachment-event-match-20261024.md):
  43 body words/frame 24/one binding plus two alignment words; five checked
  operand guards. Both copies pass eight fresh checks before/after, native32,
  aliases/faults, the full dispatcher, release helper and GNU links. Preserve
  14 neighbors and strict 119-byte image, zero exclusions. Fresh adopted-ELF
  total 68.81%, 341 more to 75%; not compiler-only or gameplay acceptance.
- [Pending-record drain](WORKING_NOTES/1711-pending-record-drain-match-20261024.md):
  44 words/frame 48/eight bindings; three checked setup guards. Both copies
  pass eight fresh checks before/after, helper reloads, caller boundary,
  native32, aliases/faults and GNU links. Preserve 13 neighbors and the caller
  object; strict 136-byte image, zero exclusions. Fresh adopted-ELF total
  68.79%, 342 more to 75%; not compiler-only or full-helper/gameplay acceptance.
- [Four-head lookup](WORKING_NOTES/1710-four-head-lookup-match-20261024.md):
  complete 43-word C plus 37 derived rows matches 44/frame zero/four bindings.
  Preserve column-first search, incoming home, next capture and dead move.
  Both copies pass eight fresh checks before/after, bounded caller, native32,
  aliases, faults and rebases. Preserve 32 neighbors/six handwritten routines
  and strict 151-byte image with its closed symbol cycle, zero exclusions.
  Fresh adopted-ELF total 68.77%, 343 more to 75%; not compiler-only or full-parent/
  math/gameplay acceptance. Preliminary private work remains in Note 1709.
- [Linked-record event](WORKING_NOTES/1708-linked-record-event-match-20261024.md):
  complete 42-word C normalizes to 44/frame 24/one binding with nine checked
  setup/return rows and two derived RA-load copies. Preserve the canonical
  callback ABI and late record-pointer reads; qualify the full dispatcher,
  native32, aliases and faults. Sixteen neighbors, old guard bytes and the
  strict 132-byte image pass, zero exclusions. Total 68.76%, 344 more to 75%;
  not compiler-only or full-helper/gameplay acceptance.
- [Owner-vector descriptor](WORKING_NOTES/1707-owner-vector-descriptor-direct-match-20261024.md):
  all 44 words/frame 72/seven bindings directly from C, no guards. Preserve
  the complete preset and unspecified packet bytes; type the actual caller
  without changing its object. Both copies pass native/guest/constructor
  checks, twelve neighbors and strict 201-byte image with both symbol
  cycles predicted, zero exclusions. Total 68.74%, 345 more to 75%;
  full matrix/FCSR and gameplay remain unqualified.
- [Owner-linked large payload](WORKING_NOTES/1706-large-owner-payload-match-20261024.md):
  complete 46-word C with explicit returns normalizes to 44 words/frame
  0x918/four bindings using twelve derived guards and two redundant-copy
  omissions. Preserve unspecified payload/header bytes in the guest model;
  native checks assert only defined fields and returns. Actual caller,
  factory/copy, four neighbors and strict 149-byte image pass. Total 68.72%,
  346 more to 75%; not compiler-only or full-parent acceptance.
- [Randomized vector payload](WORKING_NOTES/1705-random-vector-payload-direct-match-20261024.md):
  all 44 words/frame 72/three bindings directly from C, no guards. Explicit
  RNG sequencing preserves the early vector and late owner-byte reads.
  Qualify the callback window, actual RNG/factory/copy chain and native32;
  preserve four neighbors, the whole guard CSV and strict 130-byte image.
  Total 68.70%, 347 more to 75%; parent C and gameplay remain unqualified.
- [Recorded-input playback](WORKING_NOTES/1704-recorded-input-step-match-20261024.md):
  complete 43-word C body plus 40 checked lifetime/address/clamp-scheduling
  guards and one preserved alignment word. Qualify signed timing, all stick
  bytes, eight aliases, real caller window and native C; preserve three SDK
  neighbors and strict 192-byte image with closed symbol cycles. Total 68.68%,
  348 more to 75%; not compiler-only or full-parent acceptance.
- [Actor class dispatcher](WORKING_NOTES/1703-callback-class-dispatch-direct-match-20261024.md):
  all 44 words directly from C, no guards. Qualify all ID bytes/classes,
  world boundaries, actual selector/mask helpers, full caller and native C;
  preserve the selector neighbor, all 328 caller-owner functions and strict
  133-byte image. Total 68.66%, 349 more to 75%; callbacks remain bounded.
- [Dual-point motion callback](WORKING_NOTES/1702-dual-point-motion-match-20261024.md):
  complete 44-word typed C plus 20 checked address-role/return-scheduling
  guards. Qualify float order, twelve timestep aliases, the original callback
  window and native32; preserve 60 neighbors and strict 147-byte image.
  Total 68.65%, 350 more to 75%; not compiler-only or full-parent acceptance.
- [Computed-tail reference event](WORKING_NOTES/1701-offset-reference-event-match-20261024.md):
  complete 44-word semantic C plus 18 checked register-lifetime/operand guards.
  Qualify the referenced-object tag, aliases, actual caller/release chain and
  native C; preserve 56 neighbors and strict 121-byte image. Total 68.63%,
  351 more to 75%; not compiler-only.
- [Record collision bounce](WORKING_NOTES/1700-record-bounce-response-direct-match-20261024.md):
  all 44 words directly from typed C, no guards. Qualify settling boundaries,
  all flag bytes, aliases, the full original dispatcher and native callback;
  preserve 30 mixed-owner neighbors and strict 159-byte image. Total 68.61%,
  352 more to 75%.
- [Actor angle blend](WORKING_NOTES/1699-angle-blend-update-direct-match-20261024.md):
  all 44 words directly from C, no guards. Qualify float boundaries, the retained
  angle helper, original caller and native C; preserve 14 neighbors and strict
  163-byte image with closed metadata accounting. Total 68.59%, 353 more to 75%.
- [Actor reference event](WORKING_NOTES/1698-owner-reference-event-match-20261024.md):
  complete 43-word C body with one commutative branch guard and one preserved
  alignment word. Qualify the full retained dispatcher/release chain, aliases
  and native C; strict 119-byte image. Total 68.57%, 354 more to 75%.
- [Owner paired-reference event](WORKING_NOTES/1697-owner-pair-event-direct-match-20261024.md):
  all 41 body words directly from C, no guards, plus three preserved alignment
  words. Qualify byte commands, late tag reads, the original dispatcher and
  retained release helper; strict 114-byte image. Total 68.56%, 355 more to 75%.
- [Phase-cycle callback](WORKING_NOTES/1696-phase-cycle-gate-match-20261024.md):
  all 44 words directly from typed C, no guards. Preserve strict float wrapping,
  threshold gating, six neighbors and strict 126-byte image. Qualify the full
  parent/color chain and native C; fresh live total 68.54%, 356 more to 75%.
- [Sequence script dispatcher](WORKING_NOTES/1695-sequence-event-dispatch-match-20261024.md):
  complete 44-word C body with 27 derived layout guards, not compiler-only.
  Qualify the original VM window and 95 retained helper words; preserve three
  neighbors and strict 123-byte image. Fresh live total 68.52%; 357 more to 75%.
- [Paired-reference event handler](WORKING_NOTES/1694-pair-reference-event-match-20261024.md):
  complete 41-word body with five checked allocation guards and three unchanged
  alignment words. Preserve 41 neighbors and strict 108-byte image; qualify
  original callers and retained release routing. Fresh live total 68.50%.
- [Point sound-position callbacks](WORKING_NOTES/1693-point-sound-position-direct-match-20261024.md):
  all 44 words each directly from typed C, no guards. Qualify signed indices,
  original caller windows and the real retained helper; preserve 67 neighbors
  and strict 253-byte image. Fresh live total 68.48%; 359 more to 75%.
- [Object attachment helper](WORKING_NOTES/1692-object-attachment-direct-match-20261024.md):
  all 49 words directly from C with a signed-short key, no guards. Qualify
  all 32 original caller windows and native C paths; preserve 77 neighbors,
  the 89-function caller object and strict 147-byte image. Total 68.45%.
- [Four character-effect pairs](WORKING_NOTES/1691-character-effect-pair-direct-match-20261024.md):
  all 44 words each directly from C, no guards. Preserve 74 neighbors and
  the strict 624-byte image; qualify original caller windows and explicit
  helper boundaries. Fresh live total 68.43%; 362 more to 75%.
- [Payload-link swap event](WORKING_NOTES/1690-payload-link-swap-event-match-20261024.md):
  43 words with four checked allocation guards, plus one unchanged alignment
  word. Preserve five neighbors and the strict 119-byte image. Fresh live
  total 68.36%; 366 more to 75%.
- [Linked-owner retirement](WORKING_NOTES/1689-linked-owner-retirement-match-20261024.md):
  44 words from semantic C and two checked spill guards; preserve 22 neighbors
  and strict 117-byte image. Total 68.34%; factory helper still uncredited.
- [Paired actor child teardown](WORKING_NOTES/1688-actor-child-cleanup-direct-match-20261024.md):
  44 words each directly from C; qualify both dispatchers and preserve the
  caller object, 42 neighbors and strict 252-byte image. Total 68.32%.
- [Animated quad record](WORKING_NOTES/1687-quad-effect-record-direct-match-20261024.md):
  all 43 words/frame 32 directly from SDK-typed C, no guards. Qualify both
  callers and the original/native allocator; preserve six neighbors and the
  strict 126-byte image. Total 3,759/5,505 (68.28%).
- [Four-entry pointer/count loader](WORKING_NOTES/1686-four-entry-loader-direct-match-20261023.md):
  all 43 words/frame 64 directly from C, no guards. Qualify the actual
  variadic helper and caller window; preserve five neighbors and the strict
  135-byte image. Total 3,758/5,505 (68.27%).
- [One-shot owner-link payload](WORKING_NOTES/1685-one-shot-link-payload-direct-match-20261023.md):
  all 43 words/frame 72 directly from C, no guards. Qualify both original
  callers and the retained factory/memcpy; preserve seventeen neighbors and
  the strict 140-byte image. Total 3,757/5,505 (68.25%).
- [Owner-following endpoint callback](WORKING_NOTES/1684-effect-owner-ray-direct-match-20261023.md):
  all 43 words/frame zero directly from C, no guards. Qualify the original
  callback window, preserve 43 neighbors and account for all 134 changed
  image bytes without exclusions. Total 3,756/5,505 (68.23%).
- [Ten-record state reset](WORKING_NOTES/1683-ten-record-state-reset-match-20261023.md):
  complete 46-word C loop normalizes to 43 words with twenty checked rows.
  Qualify the full caller/native body, preserve four neighbors and account for
  all 303 changed image bytes without exclusions. Total 3,755/5,505 (68.21%).
- [Payload-link event trio](WORKING_NOTES/1682-payload-link-event-trio-match-20261023.md):
  three complete 43-word callbacks with six checked allocation guards each.
  Qualify all selector bytes, the actual dispatcher and release chain;
  preserve 84 neighbors and strict 357-byte image. Total 3,754/5,505 (68.19%).
- [Payload owner-link event](WORKING_NOTES/1681-payload-owner-link-event-match-20261023.md):
  complete 43-word callback with the actual typed ABI and four allocation
  guards. Qualify all selector bytes, the full dispatcher and release chain;
  preserve five neighbors and strict 119-byte image. Total 3,751/5,505.
- [Recursive node identifier search](WORKING_NOTES/1680-recursive-node-identifier-search-match-20261023.md):
  all 43 words/frame 32/four bindings emit directly from C without guards.
  Qualify ordered links, signed gates, actual caller prefixes and bounded
  cycles; preserve 77 neighbors and strict 123-byte image. Total 3,750/5,505.
- [Embedded actor-link event](WORKING_NOTES/1679-embedded-actor-link-event-match-20261022.md):
  complete 43-word callback with four derived allocation guards and the actual
  pointer/byte ABI. Qualify the registered dispatcher and release chain;
  preserve 43 neighbors and strict 121-byte image. Total 3,749/5,505 (68.10%).
- [Embedded owner-link event pair](WORKING_NOTES/1678-embedded-owner-link-event-pair-match-20261022.md):
  two complete 43-word callbacks, each with four checked allocation guards.
  Qualify actual registrations, callers and the release chain; preserve twenty
  neighbors and the strict 238-byte image. Total 3,748/5,505 exact (68.08%).
- [Masked record fields](WORKING_NOTES/1677-masked-record-fields-match-20261022.md):
  all 43 words/frame zero/four bindings emit directly from C without guards.
  Qualify independent field masks, late reads and the original caller path;
  preserve 27 neighbors and the strict 122-byte image.
- [Linked shape-measure node](WORKING_NOTES/1676-shape-measure-node-match-20261022.md):
  all 43 words/frame 48/three bindings emit directly from C without guards.
  Recover the sixteen-byte node and opaque caller interface; preserve the
  caller object, 34 neighbors and strict 116-byte image.
- [Randomized player byte-state](WORKING_NOTES/1675-randomized-byte-state-match-20261022.md):
  all 43 words/frame 32/four bindings emit directly from C without guards.
  Preserve the captured attachment, original branch and late counter read;
  qualify the caller/RNG and preserve fifteen neighbors and strict 126-byte image.
- [Frame-layer dispatcher](WORKING_NOTES/1674-frame-layer-dispatch-match-20261022.md):
  all 43 words/frame 24/seventeen bindings emit directly from C without
  guards. Preserve call order, late gates, unsigned accumulator wrap,
  complete caller object and strict 168-byte image with checked serialization.
- [Embedded oscillating motion](WORKING_NOTES/1673-embedded-oscillating-motion-match-20261022.md):
  all 42 words/frame 32/six bindings emit directly from C without guards.
  Preserve the separate output, embedded fields, late clocks, signed
  slot-2 callback gate, three neighbors and strict 138-byte image.
- [Circular buffer transfer pair](WORKING_NOTES/1672-ring-buffer-transfers-match-20261022.md):
  both 42-word/frame 48 bodies emit directly from C without new guards.
  Preserve wrapping transfer/count behavior, five caller-site windows,
  actual memcpy, fourteen neighbors and the strict 278-byte image.
- [Source-backed descriptor preset](WORKING_NOTES/1671-owner-descriptor-preset-match-20261022.md):
  all 42 words/frame72 match from complete C and eighteen checked scheduling
  words with a moved low relocation. Preserve the descriptor, holes, captures,
  null gate, byte variant, 22 neighbors and strict 127-byte image.
- [Parameterized owner-selector payload](WORKING_NOTES/1670-parameterized-owner-selector-payload-match-20261022.md):
  all 42 words/frame56 match from complete C and seventeen checked scheduling
  words. Preserve signed lifetime, byte selector, twelve copied bytes,
  allocation return, five neighbors and the strict 125-byte image.
- [Damped motion snapshot](WORKING_NOTES/1669-damped-motion-snapshot-match-20261022.md):
  all 42 words/frame0 match from complete C and seven checked copy-lifetime/
  scheduling words. Preserve raw snapshots, captured damping, live timestep,
  35 neighbors and the strict 139-byte image; distinguish raw from guarded state.
- [Category-gated framebuffer fill](WORKING_NOTES/1668-category-frame-fill-match-20261022.md):
  all 42 words/frame40 emit directly from C without guards. Preserve category
  and child gates, unused float homes, complete helper packet, 33 neighbors
  and the strict 136-byte image. Keep caller/helper stub limits explicit.
- [Five-field motion callback](WORKING_NOTES/1667-five-field-motion-match-20261022.md):
  all 42 words/frame0 emit directly from C without guards. Preserve live
  timestep loads, single-precision ordering, bounded callback flow and three
  neighbors; close the full 154-byte image including symbol serialization.
- [SDK command-stream relocator](WORKING_NOTES/1666-command-stream-relocator-match-20261022.md):
  all 42 words/frame8 match from complete SDK-based C and eleven cursor-field
  guards. Preserve signed opcodes, both opening reads, wrapping offsets, eight
  neighbors and the strict 126-byte image. Caller windows are bounded evidence.
- [Inline descriptor pair callback](WORKING_NOTES/1665-inline-pair-command-match-20261022.md):
  all 42 words/frame24 match from complete C and one checked commutative branch
  operand guard. Preserve the unconditional inline read, complete caller/helper
  bounds, 56 neighbors and the strict 117-byte complete-image prediction.
- [Dual-preset effect start](WORKING_NOTES/1664-dual-preset-effect-start-match-20261022.md):
  all 42 words/frame40 emit directly from C without guards. Preserve signed
  duration, byte slot, late homes, 22 neighbors and the strict 127-byte image.
  Original caller/helper checks do not finish their remaining stubs.
- [Alternate descriptor pair callback](WORKING_NOTES/1663-alternate-pair-command-match-20261022.md):
  all 42 words/frame24 match from complete C and one checked commutative branch
  operand guard. Preserve event-first loads, full dispatcher/release-helper
  bounds, 22 neighbors and the exact 113-byte complete-image prediction.
- [Linked descriptor command callback](WORKING_NOTES/1662-linked-descriptor-command-match-20261022.md):
  all42 words/frame24 match from complete C and one checked commutative branch
  operand guard. Qualify the full dispatcher and flag-transfer helper; preserve
  22 neighbors and the exact113-byte complete-image prediction.
- [Oriented triangle record](WORKING_NOTES/1661-oriented-triangle-record-match-20261022.md):
  all42 words/frame40 emit directly from C without guards. Preserve both
  complete callers, original geometry-helper bounds,40 neighbors and the
  strict120-byte complete-image prediction.
- [Descriptor-pair command callback](WORKING_NOTES/1660-descriptor-pair-command-match-20261022.md):
  all42 words/frame24 match from complete C and one checked commutative branch
  operand guard. Preserve ordered pair updates, the full dispatcher, bounded
  release helper,43 neighbors and the exact113-byte full-image prediction.
- [Actor record table index](WORKING_NOTES/1659-actor-table-index-match-20261022.md):
  all 42 words/frame0 emit directly from C without guards. Preserve full-word
  keys, unsigned lengths, ordered reads and all seven caller windows; remove
  the old overflow with closed code, relocation and ELF metadata accounting.
- [Selector callback factory](WORKING_NOTES/1658-selector-callback-factory-match-20261022.md):
  all 42 words/frame64 emit directly from C without guards. Preserve captured
  selectors, all reserved bytes, the complete caller and original helper bounds;
  keep the 32-function caller object and full guard manifest unchanged.
- [Source runtime-block factory](WORKING_NOTES/1657-runtime-block-factory-match-20261022.md):
  all 41 linked words/frame56 match from complete 40-word C and two checked
  return-join rows. Preserve all six caller windows, actual factory/memcpy
  bounds, five neighbors and the old manifest prefix.
- [Keyed node removal](WORKING_NOTES/1656-keyed-node-removal-match-20261021.md):
  all 41 words/frame48 emit directly from typed C without guards. Preserve
  unlink order, cached successors, both caller windows and bounded Init helpers.
- [Six ordered byte submissions](WORKING_NOTES/1655-six-byte-dispatch-match-20261021.md):
  all 41 words/frame40 emit directly from C without guards. Preserve the
  shared stack buffer, ordered byte stores, both original wrappers and
  selected original caller paths; keep current-stub/gameplay limits explicit.
- [SDK segment-bank draw pair](WORKING_NOTES/1654-sdk-segment-bank-draw-pair-match-20261021.md):
  40 body words/frame24 emit directly from SDK-macro C, with the original
  alignment word, complete caller, bounded original helper and no guards.
- [Quadratic position callback](WORKING_NOTES/1653-quadratic-position-callback-match-20261021.md):
  all 41 words/frame0 emit directly from C, with signed counter bounds,
  late reload, overlap qualification and the original keep/skip dispatch.
- [Paired SDK matrix callback wrappers](WORKING_NOTES/1652-matrix-callback-wrapper-pair-match-20261021.md):
  two 41-word/frame40 bodies emit directly from SDK-macro C without guards;
  both real callers and the complete unchanged caller object are qualified.
- [Actor selector callback family](WORKING_NOTES/1651-actor-selector-flag-callback-family-match-20261021.md):
  all 47/44/41 words emit directly from C, frame0, with no guards.
  Both copies pass eight pre-install and two fresh installed tests; preserve
  four neighbors and the full guard manifest. Strict ELF change: 393 bytes,
  zero exclusions. Total 3,718/5,505 (67.54%); 411 more to 75%.
- [Indexed record commands](WORKING_NOTES/1650-indexed-record-command-match-20261021.md):
  all 41 words/frame0/six bindings emit directly from C, with no guards.
  Both copies pass eight pre-install and two fresh installed tests; preserve
  four neighbors and the full guard manifest. Strict ELF change: 126 bytes,
  zero exclusions. Total 3,715/5,505 (67.48%); 414 more to 75%.
- [Two-range position sampler](WORKING_NOTES/1649-two-range-position-sampler-match-20261020.md):
  all 41 words/frame32/eight bindings emit directly from C, without guards.
  Both copies pass eight pre-install and two fresh installed tests; preserve
  28 neighbors and the full guard manifest. Strict ELF change: 123 bytes,
  zero exclusions. Total 3,714/5,505 (67.47%); 415 more to 75%.
- [Color-record and pointer-table reset](WORKING_NOTES/1648-color-record-pointer-table-reset-match-20261020.md):
  all 41 words/frame40 exact with 17 checked normalization rows and one
  fixed-layout address fold. Both copies pass eight pre-install and two fresh
  installed tests; strict ELF change is 209 bytes with no exclusions.
  Total 3,713/5,505 (67.45%); 416 more to 75%.
- [Scratch-array partition guarded C match](WORKING_NOTES/1647-scratch-array-partition-byte-match-20261020.md):
  existing semantic 41-word/frame24 routine, ten checked allocation guards,
  both eight-test pre-install suites, two installed tests per copy, 25 fixed neighbors and strict 128-byte
  ELF change. Total 3,712/5,505 (67.43%); 417 more to 75%.
- [Oscillating motion direct C match](WORKING_NOTES/1646-oscillating-motion-direct-c-match-20261020.md):
  all 40 words/frame24/six bindings emit directly from C with live phase,
  timestep and coordinate ordering. Both copies pass eight tests before/after,
  the real slot-14 dispatch window, native32 and bounded retail math.
  Preserve three neighbors and all guards; exact ELF change is 132 bytes.
  Total 3,711/5,505 (67.41%); 418 more to 75%.
- [Type-0x5A color factory direct C match](WORKING_NOTES/1645-type5a-color-factory-direct-c-match-20261020.md):
  all 40 words/frame32/one binding emit directly with the recovered eight-argument
  ABI, full word value, RGB/view fields and wrapping payload-size request.
  Both copies pass eight tests before/after, all three caller sites and the
  bounded allocation/list chain. Keep 22 neighbors and all guards unchanged;
  exact ELF change is 116 bytes. Total 3,710/5,505 (67.39%); 419 more to 75%.
- [Zero-health callback direct C match](WORKING_NOTES/1644-zero-health-callback-direct-c-match-20261020.md):
  all 40 words/frame48/three bindings emit directly using the existing actor
  fields and corrected byte-pointer callback ABI. Both copies pass eight tests
  before/after installation, real dispatcher windows and bounded helpers.
  Keep 28 neighbors and all old guards; exact ELF change is 125 bytes.
  Total 3,709/5,505 (67.38%); 420 more to 75%.
- [List node cleanup guarded C match](WORKING_NOTES/1643-list-node-cleanup-guarded-c-match-20261020.md):
  all 40 words/frame48 match with five checked saved-role/setup guards.
  Both copies pass eight pre-install/installed tests, the actual caller window,
  callbacks and bounded removal chain. Preserve 77 neighbors and the old
  guard prefix; exact ELF change is 168 bytes. Total 3,708/5,505 (67.36%);
  421 more to 75%.
- [Attachment position guarded C match](WORKING_NOTES/1642-attachment-position-guarded-c-match-20261020.md):
  all 40 words/frame24 match with one checked commutative ADDU guard.
  Both copies pass eight pre-install/installed tests, the complete caller and
  bounded original math chain. Preserve 14 neighbors and the old guard prefix;
  exact ELF change is 112 bytes. Total 3,707/5,505 (67.34%); 422 more to 75%.
- [Camera heading direct C match](WORKING_NOTES/1641-camera-heading-direct-c-match-20261020.md):
  all 40 words/frame40 emit directly using the existing camera layout.
  Both copies pass eight pre-install/installed tests, both full callers and
  bounded original helper paths. The 177-byte ELF prediction accounts for
  every code/metadata change. Total 3,706/5,505 (67.32%); 423 more to 75%.
- [Dual random point direct C match](WORKING_NOTES/1640-dual-random-point-direct-c-match-20261020.md):
  all 40 words/frame48 emit directly after recovering the first RNG home through
  declaration order. Both copies pass eight pre-install and installed tests,
  including both caller windows and the complete original secondary helper.
  Preserve 16 neighbors and the strict 128-byte ELF. Total 3,705/5,505 (67.30%);
  424 more matches to 75%.
- [Actor radial point direct C match](WORKING_NOTES/1639-actor-radial-point-direct-c-match-20261020.md):
  all 39 body words/frame 56 emit directly; retain the separate alignment word.
  Both copies pass eight pre-install and installed tests, including the full
  caller and original direction/lookup chain. Preserve 43 neighbors, all 328
  caller-owner functions and the strict 122-byte ELF. Total 3,704/5,505 (67.28%);
  425 more matches to 75%.
- [Randomized point burst direct C match](WORKING_NOTES/1638-randomized-point-burst-direct-c-match-20261020.md):
  all 40 words/frame 64 emit directly, with unsigned modulo/count, float32
  scale and late point reads. Both copies pass seven pre-install and installed
  tests, including two actual caller windows. Preserve 18 owner neighbors and
  the strict 120-byte production ELF. Total 3,703/5,505 (67.27%); 426 more to 75%.
- [Context node search guarded C match](WORKING_NOTES/1637-context-node-search-guarded-c-match-20261020.md):
  complete 41-word C search normalizes to 39 retail words/frame 0 with closed
  input/origin/binding guards. Seven tests pass in both copies; preserve 51
  owner neighbors and the old manifest prefix, and reproduce the strict
  126-byte ELF. Total 3,702/5,505 (67.25%); 427 more matches to 75%.
- [Actor sound constructor direct C match](WORKING_NOTES/1636-actor-sound-constructor-direct-c-match-20261020.md):
  all 39 words/frame 56 emit directly with word-then-short coordinates and a
  preserved unsigned handle return. Seven tests pass in both copies before
  and after installation; original registration/caller and strict 117-byte
  ELF gates pass. Total 3,701/5,505 (67.23%); 428 more matches to 75%.
- [Actor position dispatch direct C match](WORKING_NOTES/1635-actor-position-dispatch-direct-c-match-20261020.md):
  all 39 words/frame 64 emit directly; both copies pass six pre-install and
  installed tests. Preserve 327 owner neighbors and fully account for overflow
  removal, relocated jumps and ELF metadata. Total 3,700/5,505 (67.21%), zero
  drift; 429 further matches to 75%.
- [Heading-projected speed direct C match](WORKING_NOTES/1634-heading-projected-speed-direct-c-match-20261020.md):
  all 39 words/frame 64 emit directly with canonical types and staged facing
  calculation. Eight pre-install and installed tests pass in both copies;
  original math-chain execution and strict 121-byte ELF audit preserve other
  code/data. Fresh total 3,699/5,505 (67.19%); 430 further matches to 75%.
- [Record effect payload and pointer return match](WORKING_NOTES/1633-record-effect-payload-pointer-return-direct-c-match-20261020.md):
  all 39 words/frame 72 emit directly, with a typed unchanged-code C caller.
  Eight pre-install and installed tests pass in both copies; strict 121-byte
  ELF audit preserves other code/data. Fresh total 3,698/5,505 (67.18%),
  zero drift; 431 further matches to the current 75% threshold.
- [Extended effect payload direct C match](WORKING_NOTES/1632-extended-effect-payload-direct-c-match-20261020.md):
  all 39 words/frame 80 emit directly after restoring the real-local layout.
  Eight pre-install and installed tests pass in both copies; strict 138-byte
  ELF audit accounts for one closed symbol cycle and fixes all other code/data.
  Fresh total 3,697/5,505 (67.16%); 432 further matches to the 75% threshold.
- [Effect position payload direct C match](WORKING_NOTES/1631-effect-position-payload-direct-c-match-20261020.md):
  all 39 words/frame 88 installed without guards, with the correct unchanged-
  code C-caller prototype. Eight pre-install and installed tests pass in both
  copies; strict 120-byte ELF audit fixes all other code/data. Fresh total
  3,696/5,505 (67.14%), with 433 further matches to the current 75% threshold.
- [Effect payload spawn direct C match](WORKING_NOTES/1630-effect-payload-spawn-direct-c-match-20261020.md):
  all 39 words/frame 72 installed without guards; the typed C caller keeps
  all 328 bodies fixed. Eight pre-install and installed tests pass in both
  copies; strict 117-byte ELF audit preserves all other code/data. Total
  3,695/5,505 (67.12%), with 434 matches to the current 75% threshold.
- [Kinematic step direct C match](WORKING_NOTES/1629-kinematic-step-direct-c-match-20261020.md):
  all 39 words/frame 16 installed directly from normal C, without guards.
  Seven pre-install and installed tests pass in both copies; strict 120-byte
  ELF prediction preserves all other code/data. Total 3,694/5,505 (67.10%);
  435 further matches are needed for the current 75% threshold.
- [Pickup update complete match](WORKING_NOTES/1628-pickup-update-complete-match-20261020.md):
  all 681 words/frame 280 installed exact through checked C origins/680 guards.
  All 27 pre-install and installed tests pass in both copies; strict whole-ELF
  audit fixes all other code/data. Total 3,693/5,505 (67.08%); the new 75% goal
  requires 436 further matches at this denominator. Earlier entries are history.
- [Pickup update private homes and selector cursor](WORKING_NOTES/1627-pickup-update-private-homes-and-selector-cursor-20261019.md):
  17 direct C homes, cached/live selector captures and 468 complete final
  memories/FPR vectors qualify in 18 tests in both copies. Raw 680/frame 280/
  636 differences; continue GPR/binding/layout gates before installation.
- [Player item and pickup update reconstruction](WORKING_NOTES/1626-player-item-and-pickup-update-reconstruction-20261019.md):
  complete experimental `func_1508DC24`, 680 words/frame 280, one word short;
  eight tests in both copies qualify 234 public-state/native32 cases and all
  681 retail words. No installation or credit; continue private/layout gates.
- [Route node search complete match](WORKING_NOTES/1625-route-node-search-complete-match-20261019.md):
  full typed C is installed, all 539 words/frame 1536 exact through guarded
  origins/lifetimes. Nineteen tests in both copies and a strict 1,632-byte ELF
  prediction pass. Game 3,019/4,832; next `func_1508DC24`, 681 words.
- [Route-search start home, extent and ordered reads](WORKING_NOTES/1624-route-search-start-home-extent-and-ordered-reads-20261019.md):
  experimental output reaches 539 words/frame 1536, closes start aliases, all
  213 public-read sequences and 426 final memories. Eleven tests in both copies;
  426 instruction differences remain. No installation or matching credit.
- [Route-search capture closure and start-home boundary](WORKING_NOTES/1623-route-search-capture-closure-and-start-home-boundary-20261019.md):
  direct typed C closes avoid reloads; a five-field experimental mapping closes
  the table home. Ten tests in both copies, 535 words/frame 1536; incoming start
  home SP+600 remains open. No installation or matching credit.
- [Route-search sentinel and capture boundaries](WORKING_NOTES/1622-route-search-sentinel-and-capture-boundaries-20261019.md):
  complete C recovers the shared loop sentinel/early coordinates, 535 words/
  frame 1536. Eight tests in both copies; four fired probes demonstrate open
  table/argument captures. No installation or matching credit.
- [Route node search recovery and retail workspace](WORKING_NOTES/1621-route-node-search-recovery-and-retail-workspace-20261019.md):
  complete experimental C recovers frame 1536, five array homes and the live
  float save. Seven tests pass in both copies; 545 versus 539 words and 488
  differences remain. Continue the same function; no install or new credit.
- [Actor state tick complete match](WORKING_NOTES/1620-actor-state-tick-complete-match-20261019.md):
  semantic C plus checked origins matches all 678 words/frame 288. Fifteen
  installed tests pass in both copies; strict ELF/body/address/data audit.
  Fresh Game 3,018/4,832, overall 3,691/5,505, zero drift. Next: `func_15086364`.
- [Actor state tick direct draw homes](WORKING_NOTES/1619-actor-state-tick-direct-draw-homes-and-cursor-lifetimes-20261019.md):
  complete experimental C retains 678 words/frame 288, recovers nineteen homes
  and reduces raw differences 600 to 344. Thirteen tests pass in both copies;
  remaining frame/cached-timer/schedule gates stay open. No installation or credit.
- [Actor state tick spill ownership](WORKING_NOTES/1618-actor-state-tick-spill-ownership-and-cached-timer-20261019.md):
  experimental post-compile cursor/call-save mappings and cached timer row;
  nine tests pass in both copies, 56 effective aliases. Draw-index/private
  stores/roles and 600 differences remain open; no production install or credit.
- [Actor state tick homes and ordered reads](WORKING_NOTES/1617-actor-state-tick-homes-and-ordered-reads-20261019.md):
  experimental `func_1508A6FC` recovers seventeen homes and the read schedule,
  678 words/frame 288; eight tests pass in both copies. Continue remaining
  cursor homes/spills/roles; no installation or new matching credit.
- [Actor state tick frame and native qualification](WORKING_NOTES/1616-actor-state-tick-frame-captures-and-native-qualification-20261019.md):
  experimental `func_1508A6FC`, 678 words/frame 288, eager bases and timer
  reload recovered; eight tests pass in both copies, including native32.
  Continue private homes/roles/read order; no installation or new match.
- [Actor state tick recovery and layout boundary](WORKING_NOTES/1615-actor-state-tick-recovery-and-layout-boundary-20261019.md):
  experimental `func_1508A6FC`, 658 words/frame 328; seven tests/262 bounded
  fixtures pass in both copies. Continue pointer captures/private frame;
  no production install or matching credit.
- [Queued-zone selection complete match](WORKING_NOTES/1614-zone-selection-complete-match-20261019.md):
  `func_1508B3F8` installed, all 369 words/frame 320 exact with checked origins;
  literal/private, GNU, native, Make and strict 897-byte image proof. Fresh
  Game 3,017/4,832, overall 3,690/5,505; next `func_1508A6FC`.
- [Zone-selection query and scalar homes](WORKING_NOTES/1613-zone-selection-query-and-scalar-homes-20261019.md):
  experimental `func_1508B3F8` retains 369 words/frame 320 and recovers four
  retail homes; 277 raw differences, 14 tests in both copies. Continue the
  measured store-order/register boundary; no production install or credit.
- [Neighbor row builder complete match](WORKING_NOTES/1612-neighbor-row-builder-complete-match-20261019.md):
  complete `func_1508A1BC` installed, 336 words/frame 168 exact; ten installed
  tests and strict full-image proof preserve other bodies/addresses/data.
  Fresh totals: Game 3,016/4,832, overall 3,689/5,505; next `func_1508B3F8`.
- [Neighbor row frame and quad loops](WORKING_NOTES/1611-neighbor-row-builder-frame-and-quad-loops-20261019.md):
  direct frame168 and explicit four-way loops for experimental func_1508A1BC;
  eleven focused tests pass in both tools copies. Continue the measured
  private save-area boundary; no production install or matching credit.
- [Neighbor row builder recovery](WORKING_NOTES/1610-neighbor-row-builder-recovery-and-private-boundary-20261019.md):
  complete experimental func_1508A1BC, ten focused tests/353 fixtures in both
  tools copies; best330 words/frame176 still needs ordered/private layout.
  No production installation or matching credit; continue this function.
- [Actor pair scheduler complete match](WORKING_NOTES/1609-actor-pair-scheduler-complete-match-20261019.md):
  complete func_1508C5B8 installed,261 words/frame192 exact through checked
  source origins and literal/private/GNU/Make/image qualification. All other
  bodies, addresses and protected data remain fixed; next func_1508A1BC.
- [Actor pair scheduler frame and buffer homes](WORKING_NOTES/1608-actor-pair-scheduler-frame-and-buffer-homes-20261019.md):
  direct C frame192, real buffer homes and saved actor lifetime; ten tests,
  complete RAM and effective aliases pass. Continue register/schedule matching
  from access15; no production installation or matching credit yet.
- [Actor pair scheduler recovery and frame boundary](WORKING_NOTES/1607-actor-pair-scheduler-recovery-and-frame-boundary-20261019.md):
  complete experimental func_1508C5B8 passes eight focused tests, but its
  256-word/frame208 raw layout still differs from retail261/frame192.
  No installation or match credit; continue this function's private layout.
- [Actor pair mask complete match](WORKING_NOTES/1606-actor-pair-mask-complete-match-20261019.md):
  complete void func_1508C1A4 installed,261 words/frame168 exact through
  direct C home recovery and261 checked layout rows. Ten installed tests,
  902 fired cuts, frame aliases and a strict829-byte image prediction pass;
  all other bodies, addresses and protected data stay fixed. Make unchanged.
- [Actor pair mask recovery and private-home boundary](WORKING_NOTES/1605-actor-pair-mask-recovery-and-private-home-boundary-20261019.md):
  complete experimental void func_1508C1A4 emits261 words/frame168 with225
  differences. Eight semantic/native/helper/caller/GNU/owner tests pass, but
  fired access13 still exposes start-Z's wrong private home. No production
  change or matching credit; continue this same function.
- [Mode context initializer complete match](WORKING_NOTES/1604-mode-context-initializer-complete-match-20261019.md):
  complete func_15089BC0 replaces its stub,247 words/frame40 exact. Two table
  binding rows, two requalified neighbor expected cells and one scoped normal
  override require no instruction-layout guards. Ten installed tests, fresh
  affected-neighbor regressions and a strict769-byte ELF prediction pass.
  All other bodies, addresses and protected data remain fixed.
- [Barrier crossing complete match](WORKING_NOTES/1603-barrier-crossing-complete-match-20261019.md):
  complete func_15086D94 installed,207 words/frame144 exact with C-recovered
  scalar homes and207 checked FP/copy/schedule guards. Ten installed tests,
  738 fired cuts and a strict251-byte code-only image prediction pass; all
  neighbors, addresses, extents, metadata and protected data remain unchanged.
- [Barrier crossing audit and matching boundary](WORKING_NOTES/1602-barrier-crossing-semantic-audit-and-matching-boundary-20261019.md):
  earlier func_15086D94 checkpoint improves experimentally to207 words/frame144/68
  differences; seven semantic/ABI/helper/owner tests pass, but fired cut12
  still exposes the minimum's wrong private home. No production change or
  matching credit; continue this same function, retaining its last-crossing quirk.
- [Cyclic weight profiles complete match](WORKING_NOTES/1601-cyclic-weight-profiles-complete-match-20261019.md):
  complete void func_1508BC20 installed,189 words/frame136 exact with188
  checked guards and one additional scoped normal-profile selection. Eight
  installed tests,1,418 fired cuts and a strict565-byte image prediction pass.
  The actual RNG's inclusive-one/count16 scratch caveat is preserved explicitly.
- [Spatial neighbor refinement complete match](WORKING_NOTES/1600-spatial-neighbor-refinement-complete-match-20261019.md):
  complete func_15086098 installed,179 words/frame112 exact through176 checked
  guards. Eight installed tests,572 private cuts, actual caller/helper/GNU
  qualification and the strict578-byte whole-image audit pass; the live record
  return correction preserves its wrapper's20 original instructions.
- [Spatial neighbor refinement recovery and matching boundary](WORKING_NOTES/1599-spatial-neighbor-refinement-semantic-recovery-and-matching-boundary-20261019.md):
  complete experimental func_15086098; eight tests,103 fixtures, native32/
  UBSan and13 effective negatives, actual helper/caller windows, GNU rebases
  and real padding/Make shadow.176 words/frame112 still fails retail179 and
  private saves. No production change or matching credit; continue this target.
- [Balanced target assignment complete match](WORKING_NOTES/1598-balanced-target-assignment-complete-match-20261019.md):
  complete func_1508BF14 installed; all160 words/frame176 exact with160 guards.
  Eight installed tests,1,080 private cuts, original miss-byte poisons, actual
  caller/GNU checks and the strict485-byte production-image audit pass.
- [Balanced target assignment recovery and private layout boundary](WORKING_NOTES/1597-balanced-target-assignment-semantic-recovery-and-private-layout-boundary-20261019.md):
  complete experimental func_1508BF14; eight tests,94 fixtures and actual
  caller/GNU/padder/Make-shadow checks. Frame224 and123 differences remain;
  the frame-only control corrupts caller RA. Historical, superseded by Note1598.
- [Weighted target selection complete match](WORKING_NOTES/1596-weighted-target-selection-complete-match-20261019.md):
  complete func_1508B9BC, all 153 words/frame96 exact with 151 checked guards.
  Eight installed tests cover helper caches, publication alias, private cuts,
  native32/UBSan, actual caller, GNU rebases and the strict 546-byte image.
- [Actor sine selector saved-lifetime match](WORKING_NOTES/1595-actor-sine-selector-saved-lifetime-match-20261019.md):
  complete C installed;136 words/frame112 exact through138 checked lifetime
  guards. Eight installed tests,1,192 private cuts, actual sine/caller,
  independent GNU maps and the strict619-byte image prediction pass.
- [Actor sine selector recovery and frame boundary](WORKING_NOTES/1594-actor-sine-selector-semantic-recovery-and-frame-boundary-20261019.md):
  complete experimental C and nine qualification tests;138 words/frame128,
  77 differences, fired private-frame mismatch and rejected slot overflow.
  Historical pre-installation boundary, superseded by Note1595 above.
- [Actor target timer complete match](WORKING_NOTES/1593-actor-target-timer-complete-match-20261019.md):
  all115 words/frame80 exact through60 checked lifetime/CSE/edge-load guards,
  explicit retail script-result qualification, eleven installed tests and a
  strict461-byte image prediction. Owner58/73 exact; next func_15089F9C.
- [Actor target timer recovery and matching boundary](WORKING_NOTES/1592-actor-target-timer-semantic-recovery-and-matching-boundary-20261019.md):
  complete experimental C, seven semantic/native/helper/caller/isolation tests,
  115 words/frame80 and60 remaining differences. Return contract stays open;
  no production edit or matching credit. Continue this function's literal fit.
- [Category boundaries complete match](WORKING_NOTES/1591-category-boundaries-complete-match-20261019.md):
  all112 words/frame96 exact with recovered source lifetimes,35 checked guards,
  twelve installed tests and a strict414-byte image prediction. Owner57/73
  exact; next audit115-word func_1508D850 and its helper/return contracts.
- [Category boundaries recovery and matching boundary](WORKING_NOTES/1590-category-boundaries-semantic-recovery-and-layout-boundary-20261019.md):
  complete experimental C, seven tests, public/native/caller/map qualification
  and a fired first-read mismatch.112 words/frame96,54 differences; not installed.
- [Record query/release complete match](WORKING_NOTES/1589-record-release-complete-match-20261019.md):
  complete78-word query/clear/coordinate capture with seven GPR-only guards,
  eleven installed tests and an exact240-byte production-image prediction.
  Owner56/73 exact; next audit112-word func_15085BE8's extrema/boundary builder.
- [Parallel array reset complete match](WORKING_NOTES/1588-parallel-array-reset-complete-match-20261019.md):
  complete52-word reset with current bounds and cached outputs, ten installed
  tests and an exact161-byte production-image prediction. Owner55/73 exact;
  continue with78-word func_1508DAEC's query/clear and coordinate paths.
- [Round-robin slot selector complete match](WORKING_NOTES/1587-round-robin-slot-selector-complete-match-20261019.md):
  complete47-word signed selector with checked layout, nine installed tests
  and an exact143-byte production-image prediction. Owner54/73 exact;
  continue with52-word func_1508DA1C and its store/count reload ordering.
- [Packed-row dispatch complete match](WORKING_NOTES/1586-packed-row-dispatch-complete-match-20261019.md):
  complete 91-word dispatcher with checked layout, two retained tail NOPs,
  ten installed tests and an exact 287-byte production-image prediction.
  Owner53/73 exact; the remaining 47-word func_1508C9CC is the next target.
- [Packed-entry peer lookup complete match](WORKING_NOTES/1585-packed-entry-peer-lookup-complete-match-20261019.md):
  complete 63-word lookup with checked argument homes/layout, ten installed
  tests and an exact 207-byte target-only production-image prediction.
- [Slot-state transfer complete match](WORKING_NOTES/1584-slot-state-transfer-complete-match-20261019.md):
  complete 189-word C recovery with checked layout, eleven installed tests and
  an exact 595-byte target-only production-image prediction.
- [Slot-state transfer recovery and matching boundary](WORKING_NOTES/1583-slot-state-transfer-recovery-and-matching-boundary-20261019.md):
  complete189-word experimental C, eight passing bounded recovery tests and
  explicit100-word/private/fault nonmatch; not installed or counted as exact.
- [Mode-dependent type code complete match](WORKING_NOTES/1582-mode-dependent-type-code-complete-match-20261018.md):
  replace the C stub with 71 exact words and 57 verified table targets, with
  only two table bindings. Eight installed tests and the exact 257-byte image
  audit pass. Tools8b851a0 first; Game2998/4832 (62.04%), total3671/5505
  (66.68%). Next audit the 189-word slot-state transfer func_1508E89C.

- [Route limit switch complete match](WORKING_NOTES/1581-route-limit-switch-complete-match-20261018.md):
  replace the zero-return C stub with all 44 exact words and 63 verified table
  targets; two relocation bindings, no scheduling guards. Eight installed tests
  and the exact 221-byte image audit pass. Tools943620e first; Game2997/4832
  (62.02%), total3670/5505 (66.67%). Next audit 71-word func_1508E780.

- [Route slot reservation direct C conversion](WORKING_NOTES/1580-route-slot-reservation-direct-c-conversion-20261018.md):
  all 61 words/frame0x28 directly exact; ten installed tests, real reset helper
  and unchanged whole-ELF audit pass. Toolsc1fbc31 first; fresh Game2996/4832
  (62.00%), total3669/5505. Next audit the 44-word C stub func_1508E6D0.

- [Route record copy direct C conversion](WORKING_NOTES/1579-route-record-copy-direct-c-conversion-20261018.md):
  all 40 words/frame0x28 directly exact; ten installed tests, real SDK overlap
  and unchanged whole-ELF audit pass. Tools5d8bc93 first; fresh Game2995/4831
  (62.00%), total3668/5504. Next audit retained 61-word func_1508868C.

- [Route event dispatcher direct C conversion](WORKING_NOTES/1578-route-event-dispatcher-direct-c-conversion-20261018.md):
  all 53 words/frame0x20 directly exact, no guards; eight installed tests and
  unchanged whole-ELF audit pass. Tools7bc7dfc first; fresh Game2994/4830,
  total3667/5503. Next audit retained 40-word func_150885EC.

- [Route actor event direct C conversion](WORKING_NOTES/1577-route-actor-event-direct-c-conversion-20261018.md):
  all 51 words directly exact, no new guards; 11 installed tests and the literal
  unchanged whole-ELF audit pass. Tools eabe57c first; fresh Game2993/4829,
  total3666/5502. Continue with the retained caller func_150880F8.

- [Route actor update complete match and installation](WORKING_NOTES/1576-route-actor-update-complete-match-and-installation-20261018.md):
  complete typed C and604 guarded exact words;17 post-install tests, actual Make,
  retained first-link reconciliation and full installed audit pass. Tools6327a76
  first; fresh Game2992/4828,total3665/5501. Continue broader Game work.
- [Route actor update casts, projection and finalizer core](WORKING_NOTES/1575-route-actor-update-casts-projection-and-finalizer-core-20261018.md):
  closed490-word core, all20 calls and60 bindings; all15 core/retained tests pass.
  Tools3ca3f0d first, no ranking/return or installed credit. Continue the same
  function's114-word retail tail, full proof and actual build integration.
- [Route actor update correction prefix layout](WORKING_NOTES/1574-route-actor-update-correction-prefix-layout-20261018.md):
  closed244-word normalized prefix only; seven tests pass with563 bounded cases,
  850 caller cuts and three GNU maps. No tail/install/count credit. Tools3076fa7
  first; continue the same function's full604-word matching qualification.
- [Route actor update local homes and error lifetime](WORKING_NOTES/1573-route-actor-update-local-homes-and-error-lifetime-20261018.md):
  complete594-word/frame456 C recovers core homes and reduces481 to450 raw
  differences. Thirteen tests pass; old source/native receipts stay separate.
  Tools b668034 first, no production/count credit. Continue the same function's
  ten-word deficit, remaining private state and installation qualification.
- [Route actor update native32 and storage boundary](WORKING_NOTES/1572-route-actor-update-native32-and-storage-boundary-20261018.md):
  six tests qualify the full C in three553-case native profiles and the same
  connected guest corpus. Five ordinary controls and one separate sanitizer
  control fire. Raw594/frame456 still has481 differences; no installation or
  credit. Tools d4113f7 first; continue the same function's private/extent match.
- [Route actor update ranking cursor](WORKING_NOTES/1571-route-actor-update-ranking-cursor-recovery-20261018.md):
  complete594-word/frame456 C recovers five tail words without changing the
  original save layout. Fifteen tests pass;10 words remain missing and481
  differences persist. Tools21db626 first, no production/count change or credit.
  Continue the same function's spill/join/private/native/matching gates.
- [Route actor update frame and save layout](WORKING_NOTES/1570-route-actor-update-frame-and-save-layout-recovery-20261018.md):
  complete589-word/frame456 C restores original saves/argument homes; first15
  and last11 words match directly. Eighteen tests and one reused owned
  compiler capture qualify the progress. Cut14 still rejects argument
  temporaries;15 words remain missing. Tools c767262 first, zero installation/
  matching credit. Continue this same function before production integration.
- [Route actor update recovery and frame boundary](WORKING_NOTES/1569-route-actor-update-semantic-recovery-and-frame-boundary-20261018.md):
  complete private604-word caller recovery; 12 tests with real helpers,
  independent float reference, ranking/width controls and both caller windows.
  Raw588/frame480/599 differences is explicitly rejected at the first private
  RA store. Tools a71464c first; no production/count change. Continue frame,
  homes and literal matching in this same function before installation.
- [Route record setup installed byte match](WORKING_NOTES/1568-route-record-setup-installed-byte-match-20261018.md):
  complete typed three-argument C, 160 words/frame0x60 normalized exactly, with
  the raw37/explicit return-and-read-join distinctions retained. Seventeen
  installed tests and actual Make reproduce the first 484-byte ELF prediction;
  all other code/data/addresses remain fixed. Tools38eefad first. Fresh Game
  2991/4828, total3664/5501; next604-word func_15087350 stub.
- [Route setup initial S7 capture and delayed stores](WORKING_NOTES/1567-route-record-setup-initial-s7-capture-and-delayed-stores-20261018.md):
  160-word/frame-0x60 experimental C improves 43 to 39 differences. Nine initial
  words match literally, with eight tests and 472 real-helper observations.
  Cut 43 closes; cut 60 reload ordering and later S7/FP roles remain. Tools
  b12e663 first. No production installation, README count change or matching credit.
- [Route record setup recovery and private order boundary](WORKING_NOTES/1566-route-record-setup-semantic-recovery-and-private-order-boundary-20261018.md):
  experimental three-argument func_150870D0, 160 words/frame 0x60/43 differences,
  six tests with guest/native32 and real helper/caller coverage. Private-order
  rejection remains explicit; no production installation or matching credit.
  Tools 483ddb2 first. Continue this same function's S7 capture and seed stores.
- [Route vector installed byte match](WORKING_NOTES/1565-route-vector-installed-byte-match-20261018.md):
  complete typed 83-word/frame-16 normalized C, with 13 installed tests,
  actual caller/Make qualification and an exact 243-byte whole-ELF prediction.
  All other code/data/addresses stay fixed. Tools a48f19d first. Fresh Game
  2990/4828 and total 3663/5501; next the 160-word func_150870D0 setup stub.
- [Route vector saved roles and isolated layout match](WORKING_NOTES/1564-route-vector-saved-role-recovery-and-isolated-layout-match-20261018.md):
  original two-save invariant roles and 83-word/frame-16 C, with a closed
  all-word normalized match. Eight tests include native32, memory prefixes,
  rebases and actual mixed-profile padding. Tools 48c467e first; production
  remains unchanged. Continue the same vector's caller/install gates.
- [Route spline payload native32 and installed byte match](WORKING_NOTES/1563-route-spline-payload-native32-and-installed-byte-match-20261018.md):
  complete305-word/frame248 normalized C, all source origins retained. Twelve
  installed tests include three6,270-case native profiles,1,644 fault prefixes,
  100 real caller cases and actual Make/padding. The1,050-byte first prediction
  reproduces with closed metadata-order accounting and all other code/data fixed.
  Tools5f0358c first. Fresh Game2989/4828, total3662/5501; next helper15088F30.
- [Route spline payload isolated layout match and private padder](WORKING_NOTES/1562-route-spline-payload-isolated-layout-match-and-private-padder-20261018.md):
  all305 words/frame248 normalized from complete C, retaining every source
  instruction origin. Eight tests cover1,069 guest states,1,644 fired fault
  prefixes, two full rebases and actual mixed-profile private padding with72
  neighbors fixed. Tools37acf9b first. Not installed; native/proof gates open.
- [Route spline payload frame and joint extent recovery](WORKING_NOTES/1561-route-spline-payload-frame-and-joint-extent-recovery-20261018.md):
  experimental305 words/frame248, three saved FP pairs, literal array homes;
  140 linked differences. Seven tests and1,069 complete-memory/call/access
  cases per new point pass; first-save fault state still differs. Tools6067024
  first. Production/README/counts unchanged; continue register/schedule fitting.
- [Alternate route payload semantics and literal array homes](WORKING_NOTES/1560-route-spline-payload-semantic-recovery-and-array-homes-20261018.md):
  complete302-word/frame288 experimental C, both modes; nine tests and1069
  public/ordered-access cases per point with four real helpers. Front declarations
  recover all96 array bytes/literal pointers, but full memories still differ.
  Frame/save ordering remains open;30 screens rejected for installation.
  Tools681037a first; no production, README or matching-count change.
- [Route dispatcher direct byte match](WORKING_NOTES/1559-route-dispatcher-direct-byte-match-20261018.md):
  all67 linked words/frame48 directly, no guard or Make change. Eight installed
  tests cover1850 guest cases,396 fired fault prefixes,40 connected projection
  cases,96 rebased cases and three1824-case native builds. The214-byte first
  ELF prediction reproduces exactly; other bodies/data fixed. Toolsb0a32ea
  first. Game2988/4828, total3661/5501, zero drift; next callee150896EC.
- [Route projection native qualification and installed byte match](WORKING_NOTES/1558-route-projection-native-qualification-and-installed-byte-match-20261018.md):
  all321 linked words exact using a target-only profile override and335 guards.
  Nine installed tests, three8225-case native builds,2148 fault prefixes and40
  connected caller cases;974-byte ELF prediction reproduced, neighbors/data
  fixed. Toolsb61d10a first. Game2987/4828, total3660/5501, zero drift.
  Next recover the67-word dispatcher15087CC0; wider Game work remains open.
- [Projection complete observational proof and isolated byte match](WORKING_NOTES/1557-projection-complete-observational-proof-and-isolated-byte-match-20261018.md):
  closed335-to321 recipe matches every retail word in isolation.23 tests,
  complete helper-inlined ordinary/nontrapping proof and two full rebases;
  native/profile/padder/linked-install gates remain open. Toolsd9ebeb9 first;
  no production or installed matching-credit change.
- [Projection call spill and integer-prefix qualification](WORKING_NOTES/1556-projection-call-spill-and-integer-prefix-cutpoint-qualification-20261018.md):
  335/frame120 restores opening roles and SP+0x48 jointly;575 full memories
  and eleven tests pass. Prefix-only proof, two rebases and a reconciled
  liveness fix;14 extra prefix words/69 aligned suffix differences remain.
  Toolsd818afc first; no production or matching-credit change.
- [Projection normal-profile roles and current node](WORKING_NOTES/1555-projection-normal-profile-roles-and-current-node-allocation-20261018.md):
  334/frame120 recovers six opening roles and240 null fault prefixes. Eight
  tests and an owned compiler capture identify the remaining SP+0x48 spill loss;
  16 screens rejected. Toolsc77fcd2 first; no production or matching-credit change.
- [Object command enqueue byte match](WORKING_NOTES/1554-object-command-enqueue-byte-match-20261018.md):
  install41-word/frame0 enqueue C after a complete two-path memory/ABI proof,
  30 guarded allocation words and ten installed tests. Exact119-byte ELF delta;
  Game2,986/4,828, total3,659/5,501, zero drift. Tools6bebb52 first. Four parent
  expression screens rejected; parent150891E8 remains open.
- [Route projection allocator provenance](WORKING_NOTES/1553-route-projection-allocator-choice-provenance-20261018.md):
  code-identical owned captures reveal168 allocator events and saved-role
  selection order. Six tests pass; eight grouped screens rejected. Tools4c718c5
  first;321/frame120/221 remains uninstalled, with no matching-credit change.
- [Route projection extent and named homes](WORKING_NOTES/1552-route-projection-extent-and-named-home-restoration-20261018.md):
  recover321/frame120 and live stack homes under the existing owner profile;
  seven tests/1458 scan prefixes pass, but221 words and actual saved-role/fault
  differences remain. Tools1614a2c first; no production change or match credit.
- [Route projection conditional lifetime](WORKING_NOTES/1551-route-projection-conditional-object-lifetime-restoration-20261018.md):
  restore null private memory and nonnull SP+3C object capture; six tests and
  240 fired null fault prefixes pass. Still302 versus321 words, no production
  change or match credit. Toolsfabe5a1 first; continue the same parent's fit.
- [Route projection recovery boundary](WORKING_NOTES/1550-route-projection-semantic-recovery-and-installation-boundary-20261018.md):
  complete experimental parent C,575 paired guest cases and six tests; reject
  raw307/frame120 against retail321 and its conditional object lifetime.
  Toolsbc4a6e8 first; production/README/totals unchanged. Continue private fit.
- [Route neighbor preference byte match](WORKING_NOTES/1549-route-neighbor-preference-byte-match-20261018.md):
  recover91 words/frame8 with52 guards, independent retail words and a4,688-path
  scalar CFG proof. Seven installed tests; tools2c94753 first. Next parent150891E8,
  keeping the vector two-save fit and wider Game queues open.
- [Route vector lifetime screens rejected](WORKING_NOTES/1548-route-vector-lifetime-screens-rejected-20261018.md):
  new strict post-spline checkpoint,28 forms and six tests; all still fail
  retail's two-save private contract. Production and matching totals unchanged;
  tools3bd5e4e first. Resume invariant/inner-loop fitting, not this dead-end screen.
- [Route spline derivative byte match](WORKING_NOTES/1547-route-spline-derivative-byte-match-20261018.md):
  recover62 words/frame32 with45 closed FP/identity/schedule guards, correct
  FR=0 pair and real output aliases. Both spline helpers complete; tools
  bcfe55a first. Next vector saved-register fitting.
- [Route cubic spline byte match](WORKING_NOTES/1546-route-cubic-spline-byte-match-20261018.md):
  recover the49-word value helper with34 closed FP-lineage/schedule guards,
  exact private homes and seven installed tests. Tools b91fd0e first;
  next derivative150498A4, with vector fitting still open.
- [Route vector semantic model and stack rejection](WORKING_NOTES/1545-route-vector-semantic-model-and-stack-rejection-20261018.md):
  seven qualification tests pass, but the83-word model still has wrong private
  saves and76 differences. No production edit or matching credit; resume the
  saved-invariant/output-register fit. Tools81049a4 first.
- [Actor route placement byte match](WORKING_NOTES/1544-actor-route-placement-byte-match-20261018.md):
  complete118-word C routine matches with three equality/temporary guards.
  Seven installed tests, 555 connected retail-helper words, all target
  instructions and atan results, original caller windows and the first exact
  402-byte ELF delta pass. Tools 0d4af42 first; next `func_15088F30`.
- [Record progress/lap updater byte match](WORKING_NOTES/1543-record-progress-lap-updater-byte-match-20261018.md):
  complete 212-word C updater matches after 88 bounded GPR/address guards.
  Seven installed tests, connected real selector, signed lap/timer boundaries,
  alias/fault/caller checks and the first 689-byte ELF prediction pass.
  Preserve all 72 raw neighbors. Tools 64c3a9f first; next `func_15088D58`.
- [Five-neighbor selector byte match](WORKING_NOTES/1542-five-neighbor-selector-byte-match-20261018.md):
  typed 88-word selector and exact class priority match with sixty GPR/
  equality guards. Seven tests, all 7,776 category combinations, whole live
  C caller execution and the first 256-byte ELF prediction pass. Preserve
  all 72 raw neighbors. Tools 155037c first; next `func_15088A08`.
- [Forward record actor selector byte match](WORKING_NOTES/1541-record-forward-actor-selector-byte-match-20261018.md):
  complete four-argument 107-word C selector matches with 37 GPR/address
  guards, ordered outputs and live post-store reloads. Seven installed tests
  and the exact 330-byte whole-link prediction pass, preserving 72 neighbors.
  Tools 77d9c40 first. Game 2,979/4,828; next `func_150888A8`.
- [Packed record separation query byte match](WORKING_NOTES/1540-packed-record-separation-query-byte-match-20261018.md):
  complete 51-word C query matches after fifteen register-role guards.
  Seven tests and the exact 154-byte whole-link prediction pass, preserving
  all 72 neighbors and prior guard bytes. Game 2,978/4,828; next `func_150883B0`.
- [Record heading setter direct byte match](WORKING_NOTES/1539-record-heading-setter-direct-byte-match-20261018.md):
  captured record and live mode/speed predicates recover all 53 words without
  guards or build changes. Seven tests and the 156-byte first whole-link
  prediction pass; all 72 neighbors stay fixed. Game 2,977/4,828; next `func_150882E4`.
- [Record heading clamp direct byte match](WORKING_NOTES/1538-record-heading-clamp-direct-byte-match-20261018.md):
  typed u16 angle lifetimes recover all 39 words without guards or build
  changes. Seven tests and the 126-byte first whole-link prediction pass;
  all 72 neighbors stay fixed. Game 2,976/4,828; next `func_15087EF0`.
- [Enabled record tag query byte match](WORKING_NOTES/1537-enabled-record-tag-query-byte-match-20261018.md):
  complete 39-word C query matches with nine closed register/schedule guards.
  Seven tests and the 118-byte full-link prediction pass; all neighbors and
  the caller object stay fixed. Game 2,975/4,828; next `func_15087E54`.
- [Gated category pass direct byte match](WORKING_NOTES/1536-gated-category-pass-direct-byte-match-20261018.md):
  typed void C restores all 39 words and live callback-pair counts without
  guards or build changes. Seven tests and the 131-byte full-link prediction
  pass; all 56 neighbors stay fixed. Game 2,974/4,828; next `func_15022B08`.
- [Actor snapshot packet direct byte match](WORKING_NOTES/1535-actor-snapshot-packet-direct-byte-match-20261018.md):
  typed void C restores all 38 words and inherited packet bytes without
  guards. Seven tests and the 119-byte full-link prediction pass; the typed
  caller object is unchanged. Game 2,973/4,828; next `func_15022848`.
- [Fractional point outputs direct byte match](WORKING_NOTES/1534-fractional-point-outputs-direct-byte-match-20261018.md):
  typed four-pointer C restores both fractional outputs; all 38 words/no
  frame match with normal pool anchoring and zero guards. Seven tests and
  the 123-byte full-link prediction pass. Game 2,972/4,828; next `func_151AB930`.
- [Record flag refresh direct byte match](WORKING_NOTES/1533-record-flag-refresh-direct-byte-match-20261018.md):
  typed void refresh replaces the false stub; all 38 words/no frame emit
  directly. Live count/base aliases, exhaustive native flags and the exact
  112-byte full-link prediction pass. Game 2,971/4,828; next `func_15107AE0`.
- [YXZ matrix constructor direct byte match](WORKING_NOTES/1532-yxz-matrix-constructor-direct-byte-match-20261018.md):
  five-call Y/X/Z composition replaces the empty body; all 37/frame0x68
  emit directly with zero guards. Seven final tests and the exact 119-byte
  full-link prediction pass. Game 2,970/4,828; next `func_15113180`.
- [Actor handle resource retirement byte match](WORKING_NOTES/1531-actor-handle-resource-retirement-byte-match-20261018.md):
  typed void handle-first retirement replaces the stub; all 46/frame0x20
  match with three guards. Seven tests and the 141-byte full-link prediction
  pass. Game advances to 2,969/4,828; next matrix constructor `func_151102CC`.
- [Actor owned resource cleanup byte match](WORKING_NOTES/1530-actor-owned-resource-cleanup-byte-match-20261018.md):
  typed void cleanup replaces the false stub, all 40/frame0x20 match with
  three guards. Seven tests and the 123-byte complete-image prediction pass.
  Game matching advances to 2,968/4,828; next paired `func_15101090`.
- [Rectangle private clipping homes byte match](WORKING_NOTES/1529-rectangle-private-clipping-homes-byte-match-20261018.md):
  all 346/frame0x88 match with six lifetime-qualified guards; raw C stays six
  differences. Fresh compiler/CFG/state/prefix proofs and the actual six-byte
  whole-ELF audit pass. Game matching advances to 2,967/4,828.
- [Rectangle flip order direct C improvement](WORKING_NOTES/1528-rectangle-flip-order-direct-c-improvement-20261018.md):
  twelve flip words now emit directly; 18 to six differences, still
  346/frame0x88 with zero guards. Thirteen final tests and the exact 21-byte
  installed-image audit pass. Next clipping-home lifetimes; totals unchanged.
- [Movement state machine installed](WORKING_NOTES/1527-movement-state-machine-production-installation-20261018.md):
  production `func_150F34F4` matches all 959 words after 134 qualified guards.
  The whole-ELF prediction, 25 installed tests and actual-object audit pass.
  Game matching advances to 2,966/4,828; next rectangle matching stays open.
- [Movement complete private byte match](WORKING_NOTES/1526-movement-complete-private-byte-match-20261018.md):
  all 959 words match with 134 private guards; complete C remains 134 raw
  differences. All 21 tests pass. Next production installation and whole-ELF
  audit; no production matching credit or main README change yet.
- [Movement physics-call register roles](WORKING_NOTES/1525-movement-physics-call-register-roles-20261018.md):
  fifteen new private rows give 88 normalized differences / 633 exact opening
  words. Complete C stays 134 differences; bounded injective lifetime proof
  and call-slot qualification do not install the body or earn matching credit.
- [Movement coefficient read/store schedule](WORKING_NOTES/1524-movement-coefficient-read-store-schedule-20261017.md):
  complete C improves 139 to 134 differences, 103 with unchanged 31 private
  rows. Sixteen tests pass, including 640 coefficient cases / 320 old-C
  rejections. No new guards, installation or credit; next role window open.
- [Movement scalar lifetimes and counter scope](WORKING_NOTES/1523-movement-scalar-lifetimes-and-counter-scope-20261017.md):
  complete C improves 152 to 139 differences, 108 with unchanged 31 private
  rows. Fifteen tests pass, including exact 24-record scans, twelve AST
  controls and 397 native cases/profile. No new guards, installation or credit.
- [Movement pitch and surface source order](WORKING_NOTES/1522-movement-pitch-and-surface-source-order-20261017.md):
  complete C improves 200 to 152 differences, 121 with the unchanged 31 private
  rows. Thirteen tests pass, including 256 new surface cases and sixteen
  old-read rejections. No new guards, installation or matching credit.
- [Movement release index speed copy and heading roles](WORKING_NOTES/1521-movement-release-index-speed-copy-and-heading-roles-20261017.md):
  complete C improves 270 to 200 differences; three new bounded research rows
  give 169 differences and 478 exact opening words. Twelve tests pass, with
  100 speed-alias rejections / 480 heading cases; not installed or credited.
- [Movement clamp acceleration and pitch lifetimes](WORKING_NOTES/1520-movement-clamp-acceleration-and-pitch-lifetimes-20261017.md):
  complete 959-word/frame0x80 C improves 389 to 270 differences, 242 after the
  unchanged 28 private rows. Nine tests pass, including actual-retail alias
  controls and AST zero-lifetime checks; no new guards, installation or credit.
- [Movement flag path lifetimes and CFG role proof](WORKING_NOTES/1519-movement-flag-path-lifetimes-and-cfg-role-proof-20261017.md):
  three natural C FP improvements give 389 raw differences; 28 total private
  research rewrites give 361 differences and 469 exact opening words. Nine
  tests pass, with 3,072 kernel cases / 6,600 active prefixes; not installed.
- [Movement turn-role certificate and argument controls](WORKING_NOTES/1518-movement-turn-role-certificate-and-argument-controls-20261017.md):
  raw C remains 392 differences; seven certified research-only rewrites give
  385 differences and 406 exact opening words. Eight full/two focused tests
  pass; no production guards, installation or credit.
- [Movement float lifetimes and field heading recovery](WORKING_NOTES/1517-movement-float-lifetimes-and-field-heading-recovery-20261017.md):
  complete 959-word/frame-0x80 candidate, 392 differences and 361 exact opening
  words. Eight tests pass, including 4,600 active prefixes; the FP gap is closed
  at the first remaining GPR boundary, not installed or credited.
- [Movement preloads and smoothing lifetimes](WORKING_NOTES/1516-movement-preloads-and-smoothing-lifetimes-20261017.md):
  complete 959-word/frame-0x80 candidate, 420 differences and 337 exact opening
  words. Eight tests pass, including 160 complete mode-0 private states;
  remaining literal/private gaps stay open, not installed or credited.
- [Movement return boundary and full-width buttons](WORKING_NOTES/1515-movement-return-boundary-and-full-width-buttons-20261017.md):
  complete 959-word/frame-0x80 candidate, 475 differences and 137 exact opening
  words. Disabled private path agrees in the bounded model; not installed.
- [Movement controller allocation and pickup access order](WORKING_NOTES/1514-movement-controller-allocation-and-pickup-access-order-20261017.md):
  complete 959-word/frame-0x80 candidate, 721 differences and opening controller
  gap closed. Eight tests pass; return/PC provenance still differs, not installed.
- [Movement retail extent frame and live homes](WORKING_NOTES/1513-movement-retail-extent-frame-and-live-homes-20261017.md):
  complete 959-word/frame-0x80 candidate, qualified storage traces and initial
  private prefixes. Still 744 differences/cut-10 allocation gap; not installed.
- [Actor input movement recovery and fitting boundary](WORKING_NOTES/1512-actor-input-movement-recovery-and-fitting-boundary-20261017.md):
  complete routine/ABI recovery and eleven tests; 962/959 words, frame 0x70/0x80
  and private state still differ. No installation/credit; continue the same fit.
- [Owner burst emitter restoration and match](WORKING_NOTES/1511-owner-burst-emitter-restoration-and-match-20261017.md):
  complete 288-word C/frame 0x150, twenty bounded guards, seven installed/seven
  research/four historical checks and exact first image. Game 61.41%, total
  66.13%, zero drift. Paused resume point: 959-word `func_150F34F4`.
- [Owner burst UOPT reservations and source controls](WORKING_NOTES/1510-owner-burst-uopt-reservations-and-source-controls-20261017.md):
  all 12 extra optimizer bytes bound to three actual expressions; four tests,
  78 controls and rejected source forms. Frame/matching still open; not installed.
- [Owner burst frame trace and aligned packet qualification](WORKING_NOTES/1509-owner-burst-frame-trace-and-aligned-packet-qualification-20261017.md):
  compiler-backed packet addresses and 3,928 complete public comparisons,
  including unmasked padding. Frame/private/85-word gap still open; not installed.
- [Owner burst emitter recovery and private layout gap](WORKING_NOTES/1508-owner-burst-emitter-recovery-and-private-layout-gap-20261017.md):
  full 288-word candidate and six research tests; frame, private state and
  nonuniform padding still differ. Not installed; production/totals unchanged.
- [Actor scale timer restoration and match](WORKING_NOTES/1507-actor-scale-timer-restoration-and-match-20261017.md):
  complete 90-word C with two multiply guards; seven installed/nine historical
  checks and exact first image. Game 61.39%, total 66.12%, zero drift.
- [Indexed threshold mask direct restoration and match](WORKING_NOTES/1506-indexed-threshold-mask-direct-restoration-and-match-20261017.md):
  complete42-word C without guards; seven installed/two historical checks and
  exact whole first image; Game61.37%, total66.10%, zero address drift.
- [Actor record gate register reuse and reload control](WORKING_NOTES/1505-actor-record-gate-register-reuse-and-reload-control-20261017.md):
  actual GPR2 reuse observed;139-word reload-only control still fails words
  and private state; four fresh tests, no installation or matching credit.
- [Actor record gate expression image sharing](WORKING_NOTES/1504-actor-record-gate-expression-image-sharing-20261017.md):
  two distinct opening loads acquire one image before global passes; three
  fresh tests and unchanged normal object, no installation or matching credit.
- [Actor record gate compiler stages and prolog control](WORKING_NOTES/1503-actor-record-gate-compiler-stages-and-prolog-control-20261017.md):
  full-object-preserving compiler captures and a qualified eight-word prolog
  control; full routine still unmatched, production and totals unchanged.
- [Actor record gate recovery and private mismatch](WORKING_NOTES/1502-actor-record-gate-recovery-and-private-mismatch-20261017.md):
  uninstalled137/139-word candidate, five recovery tests and a measured saved-register
  counterexample; production and matching totals unchanged, same target remains open.
- [Actor state and event value direct restoration and match](WORKING_NOTES/1501-actor-state-and-event-value-direct-restoration-and-match-20261017.md):
  complete189/48-word C with no new guards, eight installed and three selected
  historical checks; all nine owner functions match; Game61.35%, total66.08%.
- [Halfword point update direct restoration and match](WORKING_NOTES/1500-halfword-point-update-direct-restoration-and-match-20261017.md):
  complete64-word C, actual frame0x88 private homes and no new guards;
  eight installed and three selected historical checks; Game61.31%, total66.04%.
- [Selector point transform direct restoration and match](WORKING_NOTES/1499-selector-point-transform-direct-restoration-and-match-20261017.md):
  complete43-word C with preserved retail table and no new word guards;
  ten installed and six selected historical checks; Game61.29%, total66.02%.
- [Fixed state sine update direct restoration and match](WORKING_NOTES/1498-fixed-state-sine-update-direct-restoration-and-match-20261017.md):
  complete40-word C with no new guards, ten installed and three selected
  checkpoint checks; Game61.27%, total66.01%, zero drift.
- [Sine phase update restoration and match](WORKING_NOTES/1497-sine-phase-update-restoration-and-match-20261017.md):
  complete38-word C with one commutative ADDU guard; ten final installed and
  seven selected compatibility checks; Game61.25%, total65.99%, zero drift.
- [Actor counter motion direct restoration and match](WORKING_NOTES/1496-actor-counter-motion-direct-restoration-and-match-20261017.md):
  Complete39-word C without new guards, exact entire image, ten installed
  tests and21 affected checks; Game61.23%, total65.97%, zero drift.
- [White text fade candidate and private lifetime gap](WORKING_NOTES/1495-white-text-fade-candidate-and-private-lifetime-gap-20261017.md):
  Eight tests qualify public behavior and positively reject private payload
  parity. Still uninstalled69/70 body words; next ordinary C: func_150B9560.
- [Text reveal renderer direct restoration and match](WORKING_NOTES/1494-text-reveal-renderer-direct-restoration-and-match-20261017.md):
  Complete102-word C with no new guards, exact full image and ten installed
  tests; Game61.21%, total65.95%, zero drift. Tools b3020e9 first.
- [Text buffer constructor restoration and match](WORKING_NOTES/1493-text-buffer-constructor-restoration-and-match-20261017.md):
  Complete73-word C, twelve scratch guards, exact full image and eleven
  installed tests; Game61.18%, total65.93%, zero drift.
- [Dual fade native caller-save selection](WORKING_NOTES/1492-dual-fade-native-caller-save-selection-20261017.md):
  Actual allocator costs, compare flags, opposite S0-positive control and
  three tests explain the still-uninstalled candidate's T1 selection.
- [Dual fade argument home and allocation trace](WORKING_NOTES/1491-dual-fade-argument-home-and-allocation-trace-20261017.md):
  Qualified SP+0x30 home and actual copied-word recovery, five owned compiler
  traces and ten tests. Still uninstalled with S0/private/full-slot differences.
- [Dual buffer fade candidate and private payload gap](WORKING_NOTES/1490-dual-buffer-fade-candidate-and-private-payload-gap-20261017.md):
  Complete public-qualified C, eight tests and a real variadic-wrapper
  counterexample. The 65/69-word/private-home gap keeps it uninstalled.
- [Link event callback match](WORKING_NOTES/1489-game-link-event-callback-match-20261017.md):
  Complete 43-word semantic callback with one commutative guard, exact full
  image, nine installed tests and unchanged data. Fresh Game 61.16%.
- [Transition burst real object layout and guarded match](WORKING_NOTES/1488-transition-burst-real-object-layout-and-guarded-match-20261017.md):
  Complete 251-word semantic C, real object homes, eleven scratch guards and
  exact first complete image. Fresh Game 61.14%; wider matching remains open.
- [Transition burst pointer and flag lifetime recovery](WORKING_NOTES/1487-transition-burst-pointer-and-flag-lifetime-recovery-20261017.md):
  91 -> 47 differences with original prefix/roles/branch/tail recovered;
  eight focused tests pass, aggregate homes still prevent installation.
- [Transition child motion guarded match](WORKING_NOTES/1486-transition-child-motion-guarded-match-20261017.md):
  Complete 48-word semantic callback, ten narrow guards, exact first full
  image and ten installed tests. Fresh Game 61.12%; adjacent burst still open.
- [Transition burst frame recovery and native qualification](WORKING_NOTES/1485-transition-burst-frame-recovery-and-native-qualification-20261017.md):
  Correct 251-word / frame-0x108 shape, actual frontend home captures and
  bounded native/guest evidence. Still 91 word differences, no installation.
- [Transition completion burst candidate and frame gap](WORKING_NOTES/1484-transition-completion-burst-candidate-and-frame-gap-20261017.md):
  Complete 251-word typed candidate, correct callback/factory ABI and exact
  literal pool; 93 word differences and the larger frame keep it uninstalled.
  Public/caller checks are not private/native or installation acceptance.
- [Fixed transition constructor direct match](WORKING_NOTES/1483-fixed-transition-constructor-direct-match-20261017.md):
  Complete 96-word typed C, proper factory ABI and actual copies/padding
  qualified. Eight final tests plus twelve affected checks pass; first full
  image exact with 294 changed bytes, no guards/data changes. Fresh Game 61.10%.
- [Paired scrolling tile windows direct match](WORKING_NOTES/1482-paired-scrolling-tile-windows-direct-match-20261017.md):
  Complete 38-word SDK C emitter, proper Gfx interface and live reads. Eight
  installed tests plus ten affected/context checks pass; whole-image prediction
  exact with 128 changed bytes, no guards/data changes. Fresh Game 61.08%.
- [Overlay fade packet recovery and reload gap](WORKING_NOTES/1481-overlay-fade-packet-recovery-and-reload-gap-20261017.md):
  Complete 53/54-word C diagnostic, inherited padding, actual memcpy and all
  four callers audited. Seven tests pass; three-versus-one duration loads
  remain. Exact assembly retained, no new guards or credit, production unchanged.
- [Overlay mode defaults direct match](WORKING_NOTES/1480-overlay-mode-defaults-direct-match-20261017.md):
  Complete 50-word direct C reset, byte stores, late named constant and original
  caller qualified. Nine final tests and seven affected checks pass; entire
  image prediction exact, no exclusions/guards. Fresh Game 61.06%, total 65.82%.
- [Mirrored texture float color saturation](WORKING_NOTES/1479-mirrored-texture-float-color-saturation-20261017.md):
  Actual mode5 constraints and partial positiveX residency recovery. Still
  624/633 words with wrong homes/roles, no renderer installation or C credit.
- [Mirrored texture upstream home provenance](WORKING_NOTES/1478-mirrored-texture-upstream-home-provenance-20261017.md):
  Four owned compiler traces and five passing tests locate positiveY/rate
  homes in UOPT output. Comparison forms remain nonmatching, no installation
  or C credit; production/README unchanged. Same target stays open.
- [Mirrored texture candidate and private gap](WORKING_NOTES/1477-mirrored-texture-candidate-and-private-gap-20261017.md):
  Complete four-rectangle SDK candidate and seven passing audit tests.
  Public packets/native/callers agree, but 626/633 words and private spill
  homes differ. Not installed, no new credit; same target stays open.
- [Clipped rectangle direct match](WORKING_NOTES/1476-clipped-rectangle-direct-match-20261017.md):
  Complete 106-word direct C leaf, signed clipping, original cursor homes
  and all 27 neighbors preserved without new guards/profile/pool/build changes.
  All 13 final tests pass; first entire image matches. Fresh Game 61.04%,
  total 65.81%, zero drift. Next the 633-word textured rectangle routine.
- [Overlay projection direct match](WORKING_NOTES/1475-overlay-projection-direct-match-20261017.md):
  Complete 120-word direct C recovery, original literal binding, frame/private
  ABI and all 27 neighbors preserved without new guards/profile/data.
  All 36 final tests pass; entire first image matches. Fresh Game 61.02%,
  total 65.79%, zero drift. Pulse lifetime remains open; next clipped rectangle.
- [Pulsed overlay private lifetime audit](WORKING_NOTES/1474-pulsed-overlay-private-lifetime-audit-20261017.md):
  Retail pulse-off RGB depends on inherited SP+0x20 bits. Actual helper/
  caller/setter chains and 10 passing checks reject zero substitution and
  undefined-local adoption. No production changes or matching credit.
- [Color overlay draw direct match](WORKING_NOTES/1473-color-overlay-draw-direct-match-20261017.md):
  Complete 197-word direct SDK C match, typed callers, live unsigned bounds,
  no new guards/profile and 38 unchanged surrounding routines. All 26 tests
  pass; first whole image matches. Fresh Game 61.00%, total 65.77%, no drift.
- [Color channel aggregate direct match](WORKING_NOTES/1472-color-channel-aggregate-direct-match-20261017.md):
  First-candidate 44-word direct C match, frame 0x30/F20 lifetime, real
  helper/sequence chains and 22 passing installed tests. No guards/profile
  changes; entire image changes only 129 code bytes and one size byte.
- [Color progress accessor direct match](WORKING_NOTES/1471-color-progress-accessor-direct-match-20261017.md):
  All 43 words directly exact from signed C, no guards/profile changes,
  27 unchanged neighbors, actual callers and 20 passing installed tests.
  Whole image changes only 124 code bytes and one size byte; Game 60.96%.
- [Color state submit direct match](WORKING_NOTES/1470-color-state-submit-direct-match-20261017.md):
  Complete 48-word C leaf, precise signed mode interface, no guards/profile
  changes and 89 unchanged surrounding routines. All 17 tests pass; first
  whole-image prediction matches. Fresh Game 60.94%, total 65.72%, no drift.
- [Sequence event scan installed guarded match](WORKING_NOTES/1469-sequence-event-scan-installed-guarded-match-20261017.md):
  All 219 words exact with 77 certified guards, full scratch/LO proof and
  actual setup/color chains. All 29 tests pass; complete prediction matches.
  Fresh Game 60.92%, total 65.70%, no drift. Next the 48-word color helper's C.
- [Sequence record setup installed guarded match](WORKING_NOTES/1468-sequence-record-setup-installed-guarded-match-20261017.md):
  Install all 473 retail-exact words with certified guards, both typed
  callers and actual helper chains. All 25 tests pass; whole first prediction
  and protected data match. Fresh Game 60.89%, total 65.68%, no drift.
- [Sequence record setup certified guarded match qualification](WORKING_NOTES/1467-sequence-record-setup-certified-guarded-match-qualification-20261016.md):
  All 473 retail words from complete C plus 165 certified guards, original
  frame/homes, eight passing tests. Not installed or credited; next caller/
  helper gates and first whole-image prediction before installation.
- [Sequence record setup frame and private home recovery](WORKING_NOTES/1466-sequence-record-setup-frame-and-private-home-recovery-20261016.md):
  Recover frame 0x78, all eight homes and literal memory/call-cut equivalence
  for complete 473/474-word fits. Five tests pass; no installation or credit.
  Next resolve the second descriptor preheader and remaining register fields.
- [Sequence record setup recovery and frame boundary](WORKING_NOTES/1465-sequence-record-setup-recovery-and-frame-boundary-20261016.md):
  Complete func_1501D348 C passes five public qualification tests but remains
  471 words / frame 0xA8 / 405 differences versus retail 473 / 0x78. Research
  only, no production changes or credit; next fit this same function's homes.
- [Sequence state reset installed guarded match](WORKING_NOTES/1464-sequence-state-reset-installed-guarded-match-20261016.md):
  Restore all 100 words using semantic C, a proper caller prototype and 13
  bounded guards. Twenty-four final tests and the entire first 651-byte ELF
  prediction pass; next func_1501D348.
- [Priority record maximum installed guarded match](WORKING_NOTES/1463-priority-record-maximum-installed-guarded-match-20261016.md):
  Install all 105 words using semantic C and 48 bounded guards. Twenty-eight
  final tests and the entire first 371-byte ELF prediction pass; next func_1501D044.
- [Microcode loader installed guarded match](WORKING_NOTES/1462-microcode-loader-installed-guarded-match-20261016.md):
  Install all 97 words using semantic C and 23 guards. Eighteen final tests
  and the entire first 361-byte ELF prediction pass; next func_1501CE54.
- [Microcode loader guarded match qualification](WORKING_NOTES/1461-microcode-loader-guarded-match-qualification-20261016.md):
  Qualify all 97 retail words using 96 semantic C words and 23 bounded guards.
  Seven native/guest/chain/rebase/fault tests pass; installation completed in Note 1462.
- [Microcode loader recovery and matching boundary](WORKING_NOTES/1460-microcode-loader-recovery-and-matching-boundary-20261016.md):
  Bank the 97-word/frame-0x30 candidate and seven passing research tests.
  Still 44 retail differences, not installed; production and credit unchanged.
- [Graphics task submission direct match](WORKING_NOTES/1459-graphics-task-submission-direct-match-20261016.md):
  Restore all 239 words using SDK task records and graphics macros. Twelve
  final tests and the entire 800-byte ELF prediction pass; retire nine old
  caller guards without adding guards. Next 97-word func_1501CC3C.
- [Viewport initializer direct match](WORKING_NOTES/1458-viewport-initializer-direct-match-20261016.md):
  Restore all 373 words directly, preserve frame/homes and live callback
  semantics. Twelve final tests and the entire first 1,181-byte ELF prediction
  pass. All eleven owner functions now match; next 239-word func_1501C880.
- [Viewport initializer recovery and matching boundary](WORKING_NOTES/1457-viewport-initializer-recovery-and-matching-boundary-20261016.md):
  Bank the complete 373-word/frame-0x48 candidate and seven passing recovery
  tests. Historical 49-difference boundary, now completed in Note 1458.
- [View point projection direct match](WORKING_NOTES/1456-view-point-projection-direct-match-20261016.md):
  Restore all 87 words directly from C with the real transform tail and live
  aliases. Eleven final tests and the entire 276-byte image prediction pass;
  continue the 373-word viewport/projection initializer.
- [View scissor setup direct match](WORKING_NOTES/1455-view-scissor-setup-direct-match-20261016.md):
  Restore all 124 words directly from C with real SDK/clamp behavior and no
  new guards/profile. Ten final tests and the entire 376-byte image prediction
  pass; owner recipe warning fixed. Continue the 87-word projection wrapper.
- [Two-row display-list setup guarded match](WORKING_NOTES/1454-two-row-display-list-setup-guarded-match-20261016.md):
  Restore two live SDK command rows, all 61 words with a target-only no-unroll
  object and 38 closed guards. Eleven final tests and the entire 193-byte ELF
  prediction pass; continue the adjacent 124-word scissor/cursor stub.
- [View initialization guarded match](WORKING_NOTES/1453-view-initialization-guarded-match-20261016.md):
  Restore all 95 words with eight closed prologue guards; eleven final tests
  and the entire 300-byte ELF prediction pass. Continue the 61-word two-row
  graphics setup stub; timing and full startup/gameplay stay separate.
- [Frame timing frontend allocation provenance](WORKING_NOTES/1452-frame-timing-frontend-allocation-provenance-20261016.md):
  Bind byte promotion and residual address roles before UGEN; reject 19 source
  controls with five passing tests. Timing remains open; queue view initialization next.
- [Frame timing allocation and signed-zero fit boundary](WORKING_NOTES/1451-frame-timing-allocation-and-signed-zero-fit-boundary-20261016.md):
  Reject a score-only allocation fit and a peeled history's negative-zero
  regression. Seven focused tests pass; production stays at 141 differences.
- [Frame timing state semantic restoration](WORKING_NOTES/1450-frame-timing-state-semantic-restoration-20261016.md):
  Restore the complete 191-word timing/history body with byte-index alias and
  float-rounding qualification. Ten final tests and the full 755-byte image prediction
  pass; its 141-word instruction difference remains open, with no new guards.
- [View overlay matrices guarded match](WORKING_NOTES/1449-view-overlay-matrices-guarded-match-20261016.md):
  Recover the original S0 lifetime using compiler evidence, then close all 102
  words with 37 scratch-role guards. Normal output matches the complete
  318-byte ELF prediction; continue the separate timing/state updater stub.
- [View overlay matrices semantic restoration](WORKING_NOTES/1448-view-overlay-matrices-semantic-restoration-20261016.md):
  Replace the zero-return stub with qualified unguarded C; nine final tests
  and the complete 324-byte image prediction pass. The 102-word instruction
  match remains open at 94 differences; aggregate matching is unchanged.
- [Shared overlay provider guarded match](WORKING_NOTES/1447-shared-overlay-provider-guarded-match-20261016.md):
  Recover the 175-word overlay/framebuffer pass with 79 derived role/address/
  schedule guards. The rebuild equals the full 566-byte ELF prediction;
  keep the remaining provider stubs and full gameplay boundary explicit.
- [View render provider guarded match](WORKING_NOTES/1446-view-render-provider-guarded-match-20261016.md):
  Restore all 215 words with five viewport temporary guards and a binary-unchanged
  return-interface correction. The rebuild equals the entire 680-byte ELF prediction;
  continue the remaining frame-driver providers without a full gameplay claim.
- [Scheduler frame driver guarded match](WORKING_NOTES/1445-frame-scheduler-driver-guarded-match-20261016.md):
  Restore the complete 412-word routine with 55 derived guards, pass ten
  final checks, and reproduce the full 1,301-byte ELF prediction.
  Keep remaining render-provider stubs explicit.
- [Frame coordinator direct match](WORKING_NOTES/1444-frame-coordinator-direct-match-20261016.md):
  Restore all 185 words without guards, pass ten final checks, and match the
  complete 516-byte ELF prediction with closed metadata accounting.
  Keep the upstream frame-loop stub separate.
- [View matrix preparation direct match](WORKING_NOTES/1443-view-matrix-preparation-direct-match-20261016.md):
  Restore all 40 words without new guards, pass ten final checks and reproduce
  the complete 138-byte ELF prediction. Keep the discovered caller stub explicit.
- [Packed point slot provider byte match](WORKING_NOTES/1442-packed-point-slot-provider-byte-match-20261016.md):
  Restore the provider stub as 71-word semantic C with 33 closed scratch-role
  guards; pass ten final checks and reproduce the complete 220-byte ELF prediction.
- [Packed point transform byte match and rectangle step screens](WORKING_NOTES/1441-packed-point-transform-byte-match-and-rectangle-step-screens-20261016.md):
  Match all 55 transform words with two independent schedule guards, pass
  ten final checks and reproduce the complete 208-byte ELF prediction.
  Twelve rectangle forms improve none; its 18 differences and provider stub stay open.
- [Packet rectangle macro temporary pool and native blockers](WORKING_NOTES/1440-packet-rectangle-macro-temporary-pool-and-native-blockers-20261016.md):
  Observe actual UOPT pool/forbidden bits for the installed 18-word form,
  pass ten diagnostic checks and reject 29 equivalent/worse source forms.
- [Packet rectangle inner flag capture and allocator order](WORKING_NOTES/1439-packet-rectangle-inner-flag-capture-and-allocator-order-20261016.md):
  Use fired allocator cost gates to reduce 71 -> 18 differences without guards;
  pass 20 final checks and reproduce the complete 204-byte slot-only prediction.
- [Packet rectangle lifetime screens and private-home rejection](WORKING_NOTES/1438-packet-rectangle-lifetime-screens-and-private-home-rejection-20261016.md):
  Revalidate 105 source forms and eight checks; reject equal-count fits with
  changed private homes. Production remains at 71 differences, no new C match.
- [Packet rectangle constant and spill provenance](WORKING_NOTES/1437-packet-rectangle-constant-and-spill-provenance-20261016.md):
  Qualify compiler streams, constant sharing and UOPT stack homes with
  12 diagnostic tests. Evidence only: production remains at 71 differences.
- [Packet rectangle extent and lifetime fitting](WORKING_NOTES/1436-packet-rectangle-extent-and-lifetime-fitting-20261016.md):
  Restore 346 words / frame 0x88, reduce 331 -> 71 differences without
  guards, and qualify literal prefix/suffix spans with 15 final tests.
- [Packet scissored rectangle semantic recovery](WORKING_NOTES/1435-packet-scissored-rectangle-recovery-20261016.md):
  Replace the renderer's zero stub with SDK rectangle/tint and byte animation,
  pass 14 checks, and keep its 331 retail differences explicit for the next stage.
- [Packet visibility provider byte match](WORKING_NOTES/1434-packet-visibility-provider-byte-match-20261016.md):
  Recover all 129 words with seven closed FPR guards, qualify 12 final
  checks and connect the real projection/depth/visibility pipeline in the guest model.
- [Visible-depth packet byte match](WORKING_NOTES/1433-visible-depth-packet-byte-match-20261016.md):
  Recover the 102-word unsigned-depth/visibility routine with four closed
  scratch-register guards; pass 12 checks and account for all ELF metadata.
- [Projected-packet draw and projection byte match](WORKING_NOTES/1432-projected-packet-draw-and-projection-byte-match-20261016.md):
  Match the 84-word SDK draw directly and its 73-word provider with ten
  closed scheduling guards; pass 13 checks and retain the renderer's C deferral.
- [Four-byte saturation direct byte match](WORKING_NOTES/1431-four-byte-saturation-direct-byte-match-20261016.md):
  Recover all 58 words directly, qualify conditional byte accesses and the
  actual callback path, and pass 12 final checks with an exact full-image audit.
- [Actor effect dispatch and owner completion](WORKING_NOTES/1430-actor-effect-dispatch-and-owner-completion-20261016.md):
  Finish the final placeholder and all nine linked slots / 4,368 bytes,
  qualify 13 final checks and preserve the external-helper acceptance limits.
- [Rectangle preset dispatch direct byte match](WORKING_NOTES/1429-rectangle-preset-dispatch-direct-byte-match-20261016.md):
  Recover all 127 instructions and the three-to-thirteen-input ABI, pass
  13 final checks and account for the complete 449-byte linked-image change.
- [Random packet burst direct byte match](WORKING_NOTES/1428-random-packet-burst-direct-byte-match-20261016.md):
  Recover the fourteen-input ABI and all 256 instructions directly, pass
  14 final checks and reproduce every byte of the first predicted ELF.
- [Table debris direct byte match](WORKING_NOTES/1427-table-debris-direct-byte-match-20261016.md):
  Recover all 158 instructions directly with the exact float-literal pool
  alias, pass 15 final checks and close every pre-install predicted ELF byte.
- [Table debris semantic recovery](WORKING_NOTES/1426-table-debris-semantic-recovery-20261016.md):
  Qualify unsigned-halfword/float-table packets and two RNG draws with
  seven focused tests; keep production fixed and explicitly reject the
  remaining frame/saved-lifetime mismatch and missing current caller.
- [Six-piece debris guarded byte match](WORKING_NOTES/1425-six-piece-debris-guarded-byte-match-20261016.md):
  Install all 205 checked words with full 96-byte packet qualification;
  pass 16 tests and close the exact ELF audit, explicitly preserving the
  rejected initial prediction and accounting for 84 serialization bytes.
- [Randomized ring emitter guarded byte match](WORKING_NOTES/1424-randomized-ring-emitter-guarded-byte-match-20261016.md):
  Install all 193 normalized ring words and the genuine typed ABI; pass
  15 final checks and close the complete first-predicted ELF without exclusions.
- [Six-piece debris semantic recovery](WORKING_NOTES/1423-six-piece-debris-semantic-recovery-20261015.md):
  Qualify packet/RNG/ring behavior while explicitly rejecting the oversized
  candidate and typed-ring neighbor change. Production and counts stay fixed.
- [Scaled random spray guarded byte match](WORKING_NOTES/1422-scaled-random-spray-guarded-byte-match-20261015.md):
  Recover the counted seven-input spray and escaped output writes, match
  its complete 119-word slot and pass 15 final whole-loop/image checks.
- [Record random drag guarded byte match](WORKING_NOTES/1421-record-random-drag-guarded-byte-match-20261015.md):
  Recover slot 6's full-word fade and repeated-X threshold, normalize only
  13 register words and close all 117 retail words and the complete ELF.
- [Directional burst guarded byte match](WORKING_NOTES/1420-directional-burst-guarded-byte-match-20261015.md):
  Recover both complete factory packets and install all 184 normalized
  words; pass 15 checks and close the entire initially predicted ELF.
- [Quad edge emitter guarded byte match](WORKING_NOTES/1419-quad-edge-emitter-guarded-byte-match-20261015.md):
  Install all 266 normalized words, qualify literal/private/native behavior
  and account for the complete image, including exact symbol-order cycles.
- [Quad emitter symbolic loop obligations](WORKING_NOTES/1418-quad-emitter-symbolic-loop-obligations-20261015.md):
  Check arbitrary-index loop/call dependencies with explicit assumptions;
  pass eight tests while retaining the uninstalled 137-difference baseline.
- [Quad rectangle wrapper proven guarded byte match](WORKING_NOTES/1417-quad-rectangle-wrapper-proven-guarded-byte-match-20261015.md):
  Install the complete rectangle C with all 61 guarded words exact; qualify
  its framed value proof, literal private/fault behavior and whole-image closure.
- [Quad emission loop provenance and wrapper recovery](WORKING_NOTES/1416-quad-emission-loop-provenance-and-wrapper-recovery-20261015.md):
  Qualify the complete rectangle wrapper and preset ABI, reject a false
  edge-home substitute and keep both nonmatching production stubs unchanged.
- [Quad edge emitter named frame and home recovery](WORKING_NOTES/1415-quad-edge-emitter-named-frame-and-home-recovery-20261015.md):
  Recover the retail 0x190 frame and table/range/count homes, pass 13 checks
  and retain 137 remaining differences without installing or crediting C.
- [Quad edge emitter recovery and count home](WORKING_NOTES/1414-quad-edge-emitter-recovery-and-count-home-20261015.md):
  Twelve checks qualify complete bounded packets and caller/native behavior;
  retain the uninstalled 266-word candidate's frame and 149-word matching gap.
- [Paired overlay stack contract and random direction match](WORKING_NOTES/1413-paired-overlay-stack-contract-and-random-direction-match-20261015.md):
  Defer FE1C's undefined inherited input after live-caller/packet qualification;
  match func_15170034's 41 words directly and verify the entire predicted ELF.
- [Record fade/acceleration direct match](WORKING_NOTES/1412-record-fade-acceleration-direct-match-20261015.md):
  All 51 raw/padded words with zero new guards; 14 checks, live post-movement
  fields, actual slot-5 chain and target-only whole-image closure.
- [Record color fade proven normalization and match](WORKING_NOTES/1411-record-color-fade-proven-normalization-and-match-20261015.md):
  All 97 padded words exact with defined C and 84 bounded guards; symbolic
  dependency proof, 14 checks, actual slot-4 chain and target-only ELF closure.
- [Record color fade semantics and compiler gap](WORKING_NOTES/1410-record-color-fade-semantics-and-compiler-gap-20261015.md):
  Qualify full-width fade, signed size steps and unsigned interpolation;
  ten checks pass, but reject the 98-word candidate and keep production fixed.
- [Preset 0x1B coordinate types and direct match](WORKING_NOTES/1409-preset-1b-coordinate-types-and-direct-match-20261015.md):
  Recover signed coordinate formals and the complete six-input factory packet;
  all 81 words directly from C, 14 checks and target-only whole-image closure.
- [Record fade callback direct match and live dispatch chain](WORKING_NOTES/1408-record-fade-callback-direct-match-and-live-dispatch-chain-20261015.md):
  All 49 words directly from C, 14 checks and target-only whole-image closure;
  qualify the actual slot-3 dispatcher, helpers and completion cleanup path.
- [Paired record/event direct match and compiler spill recovery](WORKING_NOTES/1407-paired-record-event-direct-match-and-compiler-spill-recovery-20261015.md):
  All 199 words directly from C, no guards; real compiler spill provenance,
  17 checks, complete image closure and unchanged caller/runtime boundaries.
- [Paired record/event ABI and candidate rejection](WORKING_NOTES/1406-paired-record-event-abi-and-candidate-rejection-20261015.md):
  Recover all 17 inputs and three packets, pass ten focused checks and reject
  all 33 nonmatching forms. Production C and matching credit remain unchanged.
- [Dual factory preset direct match](WORKING_NOTES/1405-dual-factory-preset-direct-match-20261015.md):
  All 148 words directly from C, no guards; two full packets, live homes,
  14 checks and complete image closure. Original/current caller limits stay explicit.
- [Table-fade callback frame restoration and match](WORKING_NOTES/1404-table-fade-callback-frame-restoration-and-guarded-match-20261015.md):
  Genuine live operands recover the frame; 27 bounded guards make all 103
  linked words exact. Sixteen checks and the complete ELF audit pass.
- [Table-fade callback recovery and frame gap](WORKING_NOTES/1403-table-fade-callback-recovery-and-frame-gap-20261015.md):
  Typed table snapshots and full-word semantics pass ten checks; 103 raw/padded
  words still have 19 differences and the wrong frame. No installation or credit.
- [Counter preset guarded match](WORKING_NOTES/1402-counter-preset-guarded-match-20261015.md):
  Install all 84 linked words with a closed index/register normalization,
  literal private/fault/rebase qualification and complete linked-image closure.
- [Counter preset recovery and private schedule gap](WORKING_NOTES/1401-counter-preset-semantic-recovery-and-private-schedule-gap-20261015.md):
  Recover the signed gate, full packet and pre-call clear; retain the strict
  rejection of 85-word C and distinguish an exact diagnostic from installation.
- [Actor-type preset direct match](WORKING_NOTES/1400-actor-type-preset-direct-match-20261015.md):
  Recover all 91 words directly from C, including the byte gate, full packet,
  actual factory chain and complete image closure without new guards.
- [Packed RGB callback byte match](WORKING_NOTES/1399-packed-color-callback-byte-match-20261015.md):
  Install all 248 linked words with explicit register/tail guards, full image
  closure and real callback-chain qualification; retain raw-C limitations.
- [Packed color callback semantic recovery](WORKING_NOTES/1398-packed-color-callback-semantic-recovery-20261015.md):
  Recover and test packed intensity, extent and RGB behavior while explicitly
  rejecting the still-nonmatching C body; preserve all production inputs.
- [Packed-coordinate preset direct match](WORKING_NOTES/1397-packed-coordinate-preset-direct-match-20261015.md):
  Recover all 85 words directly from C through an explicit signed low-half
  mask, retaining the complete o32 packet, private frame, real factory chain
  and whole-image closure with no new guards.

- [Additional-source coverage refresh and preset handoff](WORKING_NOTES/1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md):
  Recheck all original sources, comments, conditional bodies and retained
  object screens; keep a [durable obstruction queue](ADDITIONAL_SOURCE_REVIEW_QUEUE.csv).
  Continue packet-qualified but deliberately unmatched preset fitting.

- [Packed fade/scale callback and renderer deferral](WORKING_NOTES/1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md):
  Recover all 47 callback words with three relocation-aware guards, including
  live word clamps and actual updater/cleanup. Document positive inherited
  stack evidence for deferring the renderer's C recovery; audit the full image.

- [Packed record callback update and guarded match](WORKING_NOTES/1394-packed-record-updater-callback-and-guarded-match-20261015.md):
  Recover the actual callback/removal contract and wrapping 24.8 update, all
  48 linked words with three register guards. Qualify live state, aliases,
  actual construction/cleanup and every installed image change.

- [Small record factory direct match](WORKING_NOTES/1393-small-record-factory-direct-match-20261015.md):
  Recover the 31-argument packed factory and optional position/scale binding,
  all 100 words directly from C. Qualify pointer lifetime, live fields, nulls,
  actual helper chains and the complete linked image without adding guards.

- [Packed record factory widths and guarded match](WORKING_NOTES/1392-packed-record-factory-widths-and-guarded-match-20261015.md):
  Recover the real 49-argument factory and all 125 linked words with six closed
  scheduling guards. Preserve its direct caller and qualify packed writes,
  aliases, connected allocation and the complete installed image.

- [Factory preset wrapper widths and direct match](WORKING_NOTES/1391-factory-preset-wrapper-widths-and-direct-match-20261015.md):
  Recover all 78 words directly from C, fixing two archived argument narrowings.
  Qualify the complete packet, ABI and linked image while leaving the factory's
  separate recovery and the wider additional-C queue open.

- [Original rotation kernel and real math chains](WORKING_NOTES/1390-original-rotation-kernel-and-real-math-chain-restoration-20261015.md):
  Restore the original 84-word assembly slot and actual provider chains while
  correcting its false C classification. Keep C-fit/native-formula evidence
  distinct from assembly identity and return to the wider additional-C queue.

- [Actor world-matrix builder direct match](WORKING_NOTES/1389-actor-world-matrix-builder-direct-match-20261015.md):
  Recover all 40 words with no guards, preserving signed/live fields and alias
  order. Qualify actual helper/consumer connections and every ELF change while
  keeping the lower rotation-provider and full gameplay boundaries explicit.

- [Special-object position matrix frame and guarded match](WORKING_NOTES/1388-special-object-position-matrix-frame-and-guarded-match-20261015.md):
  Recover the real matrix/selector/call ABI and match all 51 words with two
  frame-only guards. Preserve the raw mismatch and still-stubbed matrix-helper
  boundary; close every ELF change and continue the wider source/Game audit.

- [Capture-request compiler roles and guarded byte match](WORKING_NOTES/1387-capture-request-compiler-roles-and-guarded-byte-match-20261015.md):
  Match all40 linked words through22 proven allocation/scheduling guards, keeping
  raw compiler identity distinct. Qualify full private states, prefixes, rebases
  and the complete121-byte ELF delta; preserve host and source-audit boundaries.

- [Capture-request inline copy reconstruction](WORKING_NOTES/1386-capture-request-inline-copy-reconstruction-20261015.md):
  Recover the complete typed C body and real36-byte copy. Qualify public behavior
  while preserving22 word differences and private-prefix failures; keep this
  seed private, production/README counts unchanged and the matching goal active.

- [Selected-view render pass dispatch match](WORKING_NOTES/1385-selected-view-render-pass-dispatch-match-20261015.md):
  Recover all79 words directly with a typed cursor and unsigned viewport stride.
  Qualify live gates, native/private behavior, rebases and the actual viewport
  helper; close151 ELF byte changes to one existing code slot with no guards.

- [Actor mode flags donor and original table binding](WORKING_NOTES/1384-actor-mode-flags-donor-and-original-table-binding-20261015.md):
  Recover the complete53-word C dispatcher with zero guards and its real retail
  jump table. Qualify actual caller/native/private behavior and a closed168-byte
  image delta; keep host transfer and the broader source/Game queues separate.

- [Texture vertex span lifetime role tradeoffs](WORKING_NOTES/1383-texture-vertex-span-lifetime-role-tradeoffs-20261015.md):
  Test27 complete controls and trace the partial maximum/count allocation
  recovery without claiming a match. Qualify two public candidates while
  retaining the private mismatch and unchanged production/README metrics.

- [Texture vertex span optimizer allocation and controlflow traces](WORKING_NOTES/1382-texture-vertex-span-optimizer-allocation-and-controlflow-traces-20261015.md):
  Capture actual CFE/UOPT/UGEN phases and mode5 integer constraints, ruling
  out60 more forms without claiming a match. Keep production and README fixed;
  continue this scanner's optimizer lifetime/value-use shape.

- [Texture vertex span real home recovery and fit screens](WORKING_NOTES/1381-texture-vertex-span-real-home-recovery-and-fit-screens-20261015.md):
  Recover all three real homes without new storage;18 private-home aliases
  improve against retail. Record102 fitting screens and the still-open258-word
  scheduling mismatch without changing production metrics.

- [Texture vertex span reconstruction and private boundary](WORKING_NOTES/1380-texture-vertex-span-reconstruction-and-private-boundary-20261015.md):
  Reconstruct the339-word scanner privately and qualify public behavior,
  packed fields, output aliases and effective controls. Record259 remaining
  word differences and the private/native domain limits; no production credit.

- [View matrix pass and product kernel restoration](WORKING_NOTES/1379-view-matrix-pass-and-product-kernel-restoration-20261015.md):
  Recover the 73-word C pass with twenty GPR-role guards and restore its
  original 78-word assembly dependency. Qualify actual helper connections,
  overlaps and native32; close all 506 ELF byte changes to code/extents only.

- [View clipping command and queue reconstruction](WORKING_NOTES/1378-view-clipping-command-and-queue-reconstruction-20261014.md):
  Recover the49-word command directly and55-word queue with seven FP-role
  guards. Qualify live homes/count/base, native/guest storage and actual matrix
  child connections; close all328 ELF byte changes without metadata allowances.

- [Pending view queue reconstruction](WORKING_NOTES/1377-pending-view-queue-reconstruction-20261014.md):
  Recover the42-word live-count command with three closed schedule guards.
  Qualify callback mutations, native/guest storage and actual parent/child
  connections; account for all132 ELF byte changes without metadata allowances.

- [View orthographic setup reconstruction](WORKING_NOTES/1376-view-orthographic-setup-reconstruction-20261014.md):
  Direct46-word semantic C match with zero guards, signed16 defaults and a
  typed eight-word call. Qualify full native/guest state and actual SDK
  connections; preserve all protected data and non-target code/definitions.

- [Original fixed-matrix converter ownership and rounding restoration](WORKING_NOTES/1375-original-fixed-matrix-converter-ownership-and-rounding-restoration-20261014.md):
  Restore the116-word unrolled guMtxF2L slot and current-rounding semantics;
  distinguish it from the64-word C guMtxF2L2 implementation. Qualify all382
  changed ELF bytes, bounded rounding/aliases and actual family connections.
  Correct C ownership without claiming a new C match or hardware acceptance.

- [View projection family matrix child and native qualification](WORKING_NOTES/1374-view-projection-family-matrix-child-and-native-qualification-20261014.md):
  Install complete129/38-word parent/child guarded matches and a directly exact
  typed33-word wrapper. Native32 callback ordering and the entire594-byte ELF
  delta are qualified; keep SDK math, guMtxF2L matching and runtime open.

- [View projection command lifetime and product fitting](WORKING_NOTES/1373-view-projection-command-lifetime-and-product-fitting-20261014.md):
  Improve41->19 raw differences and qualify a private19-word recipe that closes
  all129 retail words under both padders/rebases. Pass13 focused checks; native,
  actual child and integrated installation remain open, with production fixed.

- [View projection command private recovery](WORKING_NOTES/1372-view-projection-command-reconstruction-20261014.md):
  Screen130 complete forms and qualify public behavior of a129-word/frame0x50
  draft with41 remaining differences. Preserve the first private-fault witness,
  typed-wrapper/child boundaries and unchanged production; no new match credit.

- [View FOV transfer reconstruction](WORKING_NOTES/1371-view-fov-transfer-reconstruction-20261014.md):
  Restore the 99-word/two-index body with thirteen closed prologue guards,
  ten preserved neighbors and exact whole-image accounting. Pass 65 selected
  target/history checks; the final view command remains a production stub.

- [Game single-precision cosine direct match](WORKING_NOTES/1370-game-single-precision-cosine-direct-match-20261014.md):
  Recover85 code words/three NOPs directly with SDK copy/literal-type shape,
  53 focused/history checks and exact image/symbol accounting. Both trig
  helpers are restored; complete camera/culling and the wider Game goal remain open.

- [Game single-precision sine and cosine recovery](WORKING_NOTES/1369-game-single-precision-sine-and-cosine-recovery-20261014.md):
  Direct104-word sine match,42 focused/history checks and a closed code/
  metadata transition. Cosine remains unmatched; connected retail-cosine
  evidence does not establish functioning production camera/culling.

- [View frustum side-plane guarded match](WORKING_NOTES/1368-view-frustum-side-plane-guarded-match-20261014.md):
  Restore59 code words and two NOPs with four disjoint local-home guards,
  ten fixed neighbors and a closed image change. Pass39 fresh checks; keep
  one stale historical image gate and the two math-helper stubs explicit.

- [Record payload constructor direct match](WORKING_NOTES/1367-record-payload-constructor-direct-match-20261014.md):
  Convert103 words directly with a three-word structure assignment,58 fixed
  neighbors, unchanged shared ABI and a byte-identical complete ELF.
  Pass32 fresh checks; keep all failed/binding/runtime boundaries separate.

- [Codec frame dispatcher guarded match](WORKING_NOTES/1366-codec-frame-dispatch-guarded-match-20261014.md):
  Match 109 code words plus three alignment NOPs with six checked guards,
  proper buffer/count outputs, 12 fixed neighbors and a closed image change.
  Pass 113 checks; keep layer decoder stubs and runtime acceptance separate.

- [Codec input refill guarded match](WORKING_NOTES/1365-codec-input-refill-guarded-match-20261014.md):
  Restore74 words with the established reader ABI and one commutative guard,
  preserve12 neighbors and close the full image change to its slot/extent.
  Pass101 checks; keep all failed/binding queues and runtime boundaries open.

- [Commented-source audit and object notification match](WORKING_NOTES/1364-commented-source-audit-and-object-notification-match-20261014.md):
  Screen440 objects from353 commented records; recover one59-word routine
  with two checked scheduling guards,88 fixed neighbors and unchanged ELF.
  Keep raw-donor, failed-interface and pool-binding results distinct.

- [Failed-source function isolation and two exact recoveries](WORKING_NOTES/1363-failed-source-function-isolation-and-two-exact-recoveries-20261014.md):
  Compile1,044 individually isolated bodies from58 failed files, recover two
  more exact routines, and keep99 real compilation failures explicit. Correct
  the pointer-return inventory and preserve all old image/guard checkpoints.

- [Whole-source draft audit and nine exact recoveries](WORKING_NOTES/1362-whole-source-draft-audit-and-nine-exact-recoveries-20261014.md):
  Inventory558 C files, compile291 previously unlinked drafts, and install
  nine more exact routines with preserved neighbors and isolated wrapper ABI.
  Failed files/binding gaps remain explicit; no automatic host transfer.

- [All remaining byte-exact donor recoveries](WORKING_NOTES/1361-all-remaining-byte-exact-donor-recoveries-20261014.md):
  Install all 19 remaining exact C donors, preserve 742 neighbors and all data,
  and exhaust the linked-C donor queue without a broad source import.

- [First byte-exact donor conversions](WORKING_NOTES/1360-first-byte-exact-donor-conversions-20261014.md):
  Install three complete routines directly from C with proper names/comments,
  active ABI qualification and an entirely unchanged ELF; the remaining19 are completed in Note1361.

- [Alternative source byte-match audit](WORKING_NOTES/1359-alternative-source-byte-match-audit-20261014.md):
  Read-only comparison after the function commit:1,478 exact executable C
  slots,22 potential individual donors, preserved archive and diagnostic-link caveats.

- [Actor threshold flags guarded match](WORKING_NOTES/1358-game-actor-threshold-flags-guarded-match-20261014.md):
  Install the complete 47-word leaf through semantic C and 26 scheduling/
  allocation guards. Close the entire image and preserve all prior routines.

- [Actor effect packet guarded match](WORKING_NOTES/1357-game-actor-effect-packet-guarded-match-20261014.md):
  Install all108 words/frame0x98 through semantic C and eight closed FPU
  allocation guards. Full image, actual factory/copies and prior regressions pass.

- [Actor burst contact direct match](WORKING_NOTES/1356-game-actor-burst-contact-direct-match-20261014.md):
  Install all 117 words/frame0x48 directly from C, zero guards. All 67 checks
  pass; mixed callback ABI, prior consumer and every linked-image byte qualify.

- [Actor burst consumer guarded match](WORKING_NOTES/1355-game-actor-burst-consumer-guarded-match-20261014.md):
  Install all315 words/frame0x168 through semantic C and ten guarded rows.
  All40 checks pass; complete image and producer regressions stay qualified.

- [Actor burst consumer float and scheduling recovery](WORKING_NOTES/1354-game-actor-burst-consumer-float-lifetimes-and-angle-conversions-20261014.md):
  Recover saved-float roles and modeled return states;15 fresh checks pass.
  Initial diagnostic-only checkpoint; installation completes in Note1355 above.

- [Actor burst consumer partial recovery](WORKING_NOTES/1353-game-actor-burst-consumer-semantic-recovery-20261014.md):
  Complete semantic candidate and four exact private homes;10 fresh checks pass.
  Initial311-versus315-word checkpoint; continued in Note1354 above.

- [Actor burst packet direct match](WORKING_NOTES/1352-game-actor-burst-packet-direct-match-20261014.md):
  Recover all67 words/frame0x78 directly from C, zero guards. All18 checks pass,
  including untouched holes, the original mode1 consumer and closed image gates.

- [Actor vector mode-1 direct match](WORKING_NOTES/1351-game-actor-vector-mode1-direct-match-20261013.md):
  Recover all40 words/frame0x38 directly from C, zero guards. All17 checks pass,
  including shared mode0 regression, real table7 and exact whole-image gates.

- [Actor descriptor spawn direct match](WORKING_NOTES/1350-game-actor-descriptor-spawn-direct-match-20261013.md):
  Recover all65 words/frame0x60 directly from C, zero guards. All16 checks pass,
  including SDK layouts, true factory failure/copy paths and closed image gates.

- [Actor vector snapshot direct match](WORKING_NOTES/1349-game-actor-vector-snapshot-direct-match-20261013.md):
  Recover all40 words/frame0x38 directly from C, zero guards. All16 installed
  checks pass, preserving raw coordinates, private arrays and subtraction order.

- [Signed actor mask scan direct match](WORKING_NOTES/1348-game-signed-actor-mask-scan-direct-match-20261013.md):
  Recover all 39 words/frame 0x30 directly from C, zero guards. All 15 installed
  checks pass, preserving the signed snapshot, callback ABI and original dispatch.

- [Actor payload creator direct match](WORKING_NOTES/1347-game-actor-payload-creator-direct-match-20261013.md):
  Recover all38 words/frame0x48 directly from C, with zero guards. All16 checks
  pass, including actual dispatcher/creator/memcpy and private padding/alias cuts.

- [Matrix translation guarded byte match](WORKING_NOTES/1346-game-matrix-translation-guarded-byte-match-20261013.md):
  Finish49 words/frame0 using34 source-derived scheduling guards with unchanged
  C. All17 checks pass; only104 target ELF bytes change, no metadata exceptions.

- [Matrix reflection guarded byte match](WORKING_NOTES/1345-game-matrix-reflection-guarded-byte-match-20261013.md):
  Install the complete486-word routine with238 source-derived operand guards;
  all21 checks pass and fresh Game matching reaches2,825/4,823. Raw C is not
  direct-matching; the exact image audit accounts for code and its size field.

- [Matrix reflection original prologue recovery](WORKING_NOTES/1344-game-matrix-reflection-original-prologue-recovery-20261013.md):
  Recover all22 opening words at486/frame0x190/240 differences, uninstalled.
  All26 checks pass; modeled agreements192 ->3,648 without loss. Production
  stays fixed; cache/offset roles and later schedules remain open.

- [SDK-typed matrix reflection saved index](WORKING_NOTES/1343-game-matrix-reflection-sdk-typed-saved-index-recovery-20261013.md):
  Recover four original s2 shifts and callback pointer roles at486/frame0x190,
  improving331 ->259 differences. All25 checks pass; production remains fixed.
  Saved-store order, cache/offset roles and full matching remain open.

- [Matrix reflection direct homes and cache removal](WORKING_NOTES/1342-game-matrix-reflection-direct-home-dispatch-and-cache-removal-20261013.md):
  Uninstalled486/frame0x190/331 with recovered direct homes, s6 and flag roles.
  All24 checks pass; saved schedule/index/full matching remain open. Restarted
  REA is connected but its Windows Ghidra adapter rejects MIPS ELF.

- [Matrix reflection economical index and conditional homes](WORKING_NOTES/1341-game-matrix-reflection-economical-index-and-conditional-homes-20261013.md):
  Best literal332 and separate407 access-order diagnostic, both uninstalled.
  All22 checks pass; preserve192 modeled agreements/10,196 fired cuts. Recover
  direct home lowering and saved roles before any matching credit.

- [Matrix reflection pointer roles and cache provenance](WORKING_NOTES/1340-game-matrix-reflection-pointer-roles-and-cache-provenance-20261013.md):
  Uninstalled486/frame0x190 candidate improves347 ->333 differences. All prior
  sampled contracts and128 fault agreements survive; reflection cache is already
  in UOPT. Saved roles/index lifetime and full matching remain open, no credit.

- [Matrix reflection candidate and private-buffer layout](WORKING_NOTES/1339-game-matrix-reflection-candidate-and-private-buffer-layout-20261013.md):
  Complete19-slot candidate486/frame0x190/347, uninstalled. Restore scratch
  SP+0x84 using existing locals;4,800 complete-RAM cases and all17 checks pass.
  Saved-role fault cut1/register allocation remain open. Production, matching
  totals and root README unchanged; continue the same function.

- [Actor command-finalizer guarded match](WORKING_NOTES/1338-game-actor-command-finalizer-guarded-match-20261013.md):
  All 405 words / frame 0x48 match through 76 source-derived guards; raw C stays
  unchanged. Full private/fault, owner, rebase and guard-control gates pass.
  Installed audit changes 145 target bytes only; Game 2,824 / total 3,497,
  1,999 different and zero drift. Not a direct C match. Next func_15034F30.

- [Actor command-finalizer category promotion cache provenance](WORKING_NOTES/1337-game-actor-command-finalizer-category-promotion-cache-provenance-20261013.md):
  Production405/frame0x48/76 remains fixed.55 source forms/nine viable literal
  families give no improvement; owned input captures locate the typed cache
  before bias already in UOPT (656/704). Nine checks pass85.576s, no rebase/
  credit. Toolsce3980b first/older425 hashes fixed; next bias conversion/cache
  formation and still-open cuts10/7.

- [Actor command-finalizer bounds, clamp and secondary-tail alignment](WORKING_NOTES/1336-game-actor-command-finalizer-bounds-clamp-and-secondary-tail-alignment-20261013.md):
  Recover three source shapes;405/frame0x48,266->76 differences, no guards/credit.
  Secondary block aligned/four clamp words exact; exact states1322->1598/2938,
  no prior loss.15 pre-install tests and792-byte target-only image/data proof
  pass. All17 installed checks pass63.247s; tools56a0cee first. Next remaining
  category/noise/lower and register-allocation words.

- [Actor command-finalizer secondary value register restoration](WORKING_NOTES/1335-game-actor-command-finalizer-secondary-value-register-restoration-20261013.md):
  Recover a2/a0/a3/v0 secondary roles with the signed value local;405/frame0x48,
  267->266 differences, no guards/credit. Exact sampled states1086->1322/2938;
  all prior agreements/six slots/homes retained. Full qualification and55-byte
  target-only image/data proof pass. All16 installed checks pass77.702s,
  tools6217aa4 first. Next clamp/allocation, alignment/cuts10/7.

- [Actor command-finalizer tag-dependency canonicalization](WORKING_NOTES/1334-game-actor-command-finalizer-tag-dependency-canonicalization-20261013.md):
  20 complete forms emit two existing arrays; one bounded advisory is measured
  and rejected. Raw AS1 offsets166/165 do not change the instruction stream.
  Production405/frame0x48/267 stays fixed; eight checks pass, toolsa71abb7 first.
  Next actual source/optimizer ordering with cut9 preserved and cuts10/7 open.

- [Actor command-finalizer owned UGEN/AS1 boundary](WORKING_NOTES/1333-game-actor-command-finalizer-owned-ugen-as1-boundary-20261013.md):
  Production remains405/frame0x48/267, no guards/credit. Actual AS1 input and
  fired200-load/68-emitter probes qualify an upstream lower-placement difference;
  14 tag forms do not fit.11 checks pass, tools3fb2ea0 first, existing older hashes
  fixed. Next source/optimizer ordering and still-open cuts10/7/full matching.

- [Actor command-finalizer primary jitter load-order restoration](WORKING_NOTES/1332-game-actor-command-finalizer-primary-jitter-load-order-restoration-20261013.md):
  func_15034860 retains405/frame0x48,269->267 differences, no guards/credit.
  Two retail load words are restored; exact states720->1086/2938 with no earlier
  agreement lost. All15 installed checks/six-byte image proof pass. Tools2b16f4f
  first; next owned lower/tag evidence and the still-open primary10/secondary7.

- [Actor command-finalizer direct byte input and primary cut9 restoration](WORKING_NOTES/1331-game-actor-command-finalizer-direct-byte-input-and-primary-cut9-restoration-20261013.md):
  func_15034860 stays405/frame0x48/six live slots, differences298->269, no guards
  or credit. Primary cut9 closes on44 paths; exact fault states452->720/2938.
  All13 installed tests and181-byte target-only image/data/text gates pass.
  Tools9cd126b first; next same function's primary cut10 and second-selector cut7.

- [Actor command-finalizer scalar predicates and cut5 restoration](WORKING_NOTES/1330-game-actor-command-finalizer-scalar-predicate-and-cut5-restoration-20261013.md):
  func_15034860 stays405/frame0x48, differences299->298. First14 words exact;
  cut5 closes on52 paths, equal fault states260->452/2,938. All13 installed
  tests and50-byte target-only image/data/text gates pass, no guards or credit.
  Tools79fe8a8 first; next same function's primary cut9 and second-selector cut7.

- [Actor command-finalizer selector delay slot and nested noise fit](WORKING_NOTES/1329-game-actor-command-finalizer-selector-delay-slot-and-nested-noise-fit-20261013.md):
  func_15034860 retains405/frame0x48, differences307->299, no guards or credit.
  Retail word9's selector delay-slot load is restored; twelve installed tests,
  six live slots/160 home aliases and254-byte target-only image/data gates pass.
  Cut5 remains different in GPR3/7. Tools e37e4b3 first; next finish these roles
  and full private/fault matching on the same function.

- [Actor command-finalizer opening fault boundary](WORKING_NOTES/1328-game-actor-command-finalizer-opening-fault-boundary-and-fit-rejections-20261013.md):
  No improved source fit among 46 screens; production stays405/frame0x48/307.
  Six tests and 2,938 fired fault pairs locate the first GPR divergence at cut5,
  before the selector load at retail word9/source word27. All production bytes
  stay fixed. Tools b04caa1 first; next recover this same opening schedule.

- [Actor command-finalizer live temporary slots](WORKING_NOTES/1327-game-actor-command-finalizer-live-temporary-slot-restoration-20261013.md):
  func_15034860 retains405 words/frame0x48, differences342->307, still unmatched.
  Six live slots restored; eleven installed tests/80 slot probes/160 home aliases,
  compiler observations and269-byte target-only image/data/text gates pass.
  Toolscf06d70 before consumer, older work preserved; aggregate matching fixed.
  Next this same function's307 differences and full private/scratch/fault match.

- [Actor command-finalizer extent, frame and home restoration](WORKING_NOTES/1326-game-actor-command-finalizer-extent-frame-and-home-restoration-20261013.md):
  func_15034860 now emits405 words/frame0x48, differences398->342, still unmatched.
  Ten installed tests,160 input-home aliases/fired compiler observations and
  exact image/data/text gates pass; no guards or new metadata exception.
  Toolsda7ddac before consumer; aggregate matching remains fixed. Next this same function's
  allocation/scheduling/private/fault fit, not an easier neighbor.

- [Actor command-finalizer semantic recovery and matching boundary](WORKING_NOTES/1325-game-actor-command-finalizer-semantic-recovery-and-matching-boundary-20261013.md):
  The full two-channel body replaces func_15034860's placeholder. Raw395/
  frame0x40/398 differences is not exact against retail405/frame0x48.
  Ten installed tests, real parent/rebases/owner and closed image/data/text gates
  pass. Toolsb6ba284 first; matching totals stay fixed. Next the same function's
  exact length, parameter-home, frame and scheduling work; broader gates stay open.

- [Actor command-dispatch direct match and table layout](WORKING_NOTES/1324-game-actor-command-dispatch-direct-match-and-table-layout-20261013.md):
  func_15033FE0 matches all119 words/frame0x28 directly, no target guards.
  Compiler captures explain first-result home/local shrink; one derived neighbor
  table-address adapter preserves retail code/data. Eight installed tests and
  literal image/data/text gates pass. Tools1943c4d first; Game2,823/4,823.
  Next405-word func_15034860; wider Game/text/translator/runtime gates remain open.

- [Actor command-stream guarded match](WORKING_NOTES/1323-game-actor-command-stream-guarded-match-20261013.md):
  func_150341BC matches all97 linked words/frame0 using52 derived register/
  cursor/branch guards, not direct C. Eight installed tests/final native rerun,
  both owner padders/rebases and literal image/data/text gates pass. Tools
  c30d7a0 first; Game2,822/4,823. Next119-word func_15033FE0; wider gates remain open.

- [Actor callback direct match and frame provenance](WORKING_NOTES/1322-game-actor-callback-dispatch-direct-match-and-frame-provenance-20261012.md):
  func_150345E4 matches all81 words/frame0x20 directly, no guards. Fired compiler
  captures explain local16->8; nine installed tests and eight-byte literal image/
  data/text gates pass. Tools80e6fed first; Game2,821/4,823. Next97-word
  func_150341BC, text/translator and wider Game/runtime remain open.

- [Actor callback semantic recovery and frame boundary](WORKING_NOTES/1321-game-actor-callback-dispatch-semantic-recovery-and-frame-boundary-20261012.md):
  func_150345E4 now has the complete81-word body, differences78->8; source frame
 0x28 remains original0x20's unresolved boundary. Seven target tests/image/data/
  text gates pass, no new guards/matching credit. One advisory has no accepted
  fix. Tools e5c3868 first; continue the same function, text/translator still open.

- [Actor matrix clear byte match](WORKING_NOTES/1320-game-actor-matrix-clear-byte-match-20261012.md):
  func_15034728 matches all48 linked words/frame0x20 with18 mathematically derived
  register/operand guards; raw C still differs. Eight pre-/post-install tests
  qualify the live-mask aliases, actual25-record caller/helper chain, whole owner
  and literal image/data/text gates. Game2,820/4,823; tools9691502 first,
  next func_150345E4. Text/translator remain open.

- [Actor type dispatch direct match](WORKING_NOTES/1319-game-actor-type-dispatch-direct-match-20261012.md):
  func_1503453C matches all42 words/frame0x18 and its five table entries directly,
  no guards/profile change. Seven pre-/post-install tests qualify the complete
  owner and connected caller; literal image/data/text gates pass. Game2,819/4,823;
  tools84cfb3a first, next func_15034728. Text/translator/helper remain open.

- [Grouped actor dispatch direct match](WORKING_NOTES/1318-game-grouped-actor-dispatch-direct-match-20261012.md):
  func_150226BC matches all38 words directly at the unchanged owner profile,
  frame0x20/no guards. Seven pre-/post-install tests qualify real connected
  caller/helpers, 56 neighbors/both padders and the closed image/data audit.
  Game matching2,818/4,823; tools a7b5b37 first, next func_1503453C.
  Text/translator stay open.

- [One-shot timer direct match](WORKING_NOTES/1317-game-one-shot-timer-direct-match-20261012.md):
  func_1501BB20 matches all38 words directly, frame0x28/no guards. Seven pre-
  and post-install tests qualify unsigned64/O32 behavior, seven neighbors,
  both padders and a closed whole-image audit. Game matching2,817/4,823;
  next func_150226BC. Tools 6a9eb2d first; hardware queue/interrupt behavior
  is not claimed.

- [Rectangle bounds predicate direct match](WORKING_NOTES/1316-game-rectangle-bounds-predicate-direct-match-20261012.md):
  func_1501AE94 matches all44 words directly, frame0/no guards. Seven pre-
  and post-install tests qualify rounding/NaNs, caller window, ten neighbors,
  both padders and literal image/data gates. Game matching2,816/4,823; next
  func_1501BB20. Tools 0a939ff first; prior unchanged broader receipts are not
  called fresh.

- [Event record constructor direct match](WORKING_NOTES/1315-game-event-record-constructor-direct-match-20261012.md):
  func_15015104 matches all52 words directly, frame0x58/no guards; seven pre-
  and seven post-install tests pass. Full image/data and 31-neighbor gates
  retain protected bytes. All22 current/regression tests pass; tools ec4865d
  first. Game matching2,815/4,823; next func_1501AE94.
  Text/matrix boundaries and host/gameplay qualification remain open.

- [Mode callback dispatcher direct match](WORKING_NOTES/1314-game-mode-callback-dispatcher-direct-match-20261012.md):
  func_15008930 matches all160 slot bytes directly, frame0x30/no guards; all
  fourteen tests and whole-image/data gates pass. Tools d3426e6 first; Game
  matching2,814/4,823. Text/matrix boundaries remain open; next func_15015104.

- [Text measurer repeated predicate and font-load boundary](WORKING_NOTES/1313-game-text-measurer-repeated-predicate-and-font-load-fault-boundary-20261012.md):
  218/114 retains the recovered lifetimes and matches 53 literal metrics words;
  710/768 named access-cut states match, with first A failure at font-pointer
  cut27. All thirteen tests pass, tools 4dbdcbe first; no installation or match.

- [Text measurer address work and retail save roles](WORKING_NOTES/1312-game-text-measurer-address-work-lifetime-and-retail-save-roles-20261012.md):
  seven opening roles, frame0x80, common zero and SP+0x68 recovered together;
  216/171 still fails full matching. Five bodies / 3,775 guest / 7,330 native32
  comparisons and all twelve tests pass; tools 4cf5203 first, no match.

- [Text measurer shared zero and source-home call-save](WORKING_NOTES/1311-game-text-measurer-shared-zero-and-source-home-call-save-20261012.md):
  split source recovers early T0 zero and SP+0x68 lifetime; extra font-address
  save still rejects the 218/frame0x80 body. Seven bodies / 5,285 public
  comparisons and all twelve tests pass; tools 54c4808 first, no match.

- [Text measurer switch and register-hint provenance](WORKING_NOTES/1310-game-text-measurer-switch-and-register-hint-provenance-20261012.md):
  six forms / three bodies / 2,265 public comparisons. Literal user-register
  VREGs differ from anonymous records; unscoped UOPT output is byte-identical
  and has no call-save. All twelve tests pass; tools 615bdc9 first, no match.

- [Text measurer explicit assignment and predicate boundaries](WORKING_NOTES/1309-game-text-measurer-explicit-assignment-and-predicate-boundaries-20261012.md):
  six bodies / 4,530 public comparisons; assignment spelling does not fix
  post-call flag loads, and separated effects fail the ordinary text-read
  boundary despite a real R8 save. All twelve tests pass; tools 54ded39 first.

- [Text measurer font controls and initializer call-save](WORKING_NOTES/1308-game-text-measurer-font-controls-and-initializer-call-save-20261012.md):
  six new tests / 2,265 public comparisons and a complete M-24/R8 capture;
  four controls produce three bodies, all rejected for saves/early zero.
  Nine regression tests pass; tools 01a4cd8 first, same target/full Game active.

- [Text measurer wire operands and source-marker provenance](WORKING_NOTES/1307-game-text-measurer-wire-operands-and-source-marker-provenance-20261012.md):
  descriptor-defined decoding qualifies actual named-flag streams and
  distinguishes CFE records from UOPT markers. All 22 tests pass; five new
  shapes remain rejected. Tools b3d042d first, same target/full Game active.

- [Text measurer carrier layout and register roles](WORKING_NOTES/1306-game-text-measurer-carrier-layout-and-register-role-qualification-20261012.md):
  six tests qualify ten distinct bodies / 7,550 public comparisons and paired
  CFE homes. T0 spill traffic can belong to maximum width, not the flag.
  All forms rejected; tools e7ebb38 banked first, same target/full Game active.

- [Text measurer frontend vreg and UOPT call-save provenance](WORKING_NOTES/1305-game-text-measurer-frontend-vreg-and-uopt-call-save-provenance-20261012.md):
  six tests qualify complete wire captures and 3,020 public comparisons;
  UOPT introduces register-8 call-save from a CFE temporary. All new source
  forms remain rejected. Tools da8a377 banked first; same target/full Game
  active, production/totals unchanged.

- [Text measurer effectful predicates and upstream call-save](WORKING_NOTES/1304-game-text-measurer-effectful-predicates-and-upstream-call-save-20261012.md):
  seven tests qualify16 source forms/nine bodies and6,795 public comparisons.
  Bitwise forms expose an upstream T0 call-save at wrong homes; all forms,
  including219/0x80, remain rejected. Tools d515411 banked, production/totals
  unchanged; continue the same target/full Game.

- [Text measurer UGEN register-node observation](WORKING_NOTES/1303-game-text-measurer-ugen-register-node-observation-20261012.md):
  read-only probes fire90 load events per early/late body; six tests qualify
  object identity and cleanup before AS1. Zero-event spill probes remain
  inconclusive. Tools7da0ac2 banked, production/totals unchanged; continue
  UOPT flag lifetime for the same target/full Game.

- [Text measurer vreg marker and memory residence](WORKING_NOTES/1302-game-text-measurer-vreg-marker-and-memory-residence-20261012.md):
  removing the marker/color still emits an extra stack write, not a T0-only
  temporary. Ten tests pass; source/interface screens yield no fit. Tools
  c28e130 banked, production/data/totals unchanged; same target/full Game active.

- [Text measurer forbidden-register constraints](WORKING_NOTES/1301-game-text-measurer-forbidden-register-constraints-20261012.md):
  real mode5 traces expose different early/late flag constraints; eight tests
  qualify parsing and source-shape rejections. Tools e1abcff banked, production/
  data/totals unchanged. No accepted fit; continue the same target/full Game.

- [Text measurer UOPT allocation trace](WORKING_NOTES/1300-game-text-measurer-uopt-allocation-trace-20261012.md):
  completed mode4/6/7 output preserves the normal candidate object. Six tests
  qualify the fingerprint-locked owned-process helper; tools 17bd18b banked.
  Numeric timing output is suppressed/unusable, and seed222 remains oversized
  and unmatched. Production/data/totals unchanged; same target/full Game active.

- [Text measurer instruction fault boundary and review](WORKING_NOTES/1299-game-text-measurer-instruction-fault-boundary-and-review-20261012.md):
  768 fired cuts isolate the missing post-normalizer T0 reset, with RAM/events/
  RA equal at the first divergence. Twenty tests pass; one tool-free review
  provides no new edit or exhaustion proof. Tools faec3b7 banked; same target/
  full Game active, no production installation or matching credit.

- [Text measurer seven-save lifetime qualification](WORKING_NOTES/1298-game-text-measurer-seven-save-lifetime-qualification-20261012.md):
  two late-flag bodies have original first13 words and 28 equal early fault
  pairs each; three bodies pass public/native and six bounded flag-home cases. Actual
  padding rejects a match/produces an overflow trampoline. Eighteen tests
  pass, tools fb5162b banked; same target/full Game active, no new match.

- [Text measurer UGEN diagnostic checkpoint](WORKING_NOTES/1297-game-text-measurer-ugen-diagnostic-checkpoint-20261012.md):
  pending experiments and a code-identical diagnostic trace are banked in
  tools 5e14815; 16 tests pass with four effective trace-rejection controls.
  Production and matching totals are unchanged; matching remains paused.

- [Text measurer independent links and frame fault rejection](WORKING_NOTES/1296-game-text-measurer-independent-links-and-frame-fault-rejection-20261012.md):
  original219/candidate and actual helpers/tables link independently at retail
  and two rebases; 1,554 cases and HI/LO carries pass. Fifteen focused tests
  pass. Four fired fault pairs expose original S6 versus candidate S7 at the
  first saved frame word; do not treat that rejection gate as full fault or
  word equivalence. Candidate218/0x80/174 remains unchanged and uninstalled,
  as do all production inputs/data/totals. Tools 44bec83 first, older unrelated
  work preserved/no push. Continue original S3/T0 lifetimes and full219 fit.

- [Text measurer flag lifetime and owner qualification](WORKING_NOTES/1295-game-text-measurer-flag-lifetime-and-owner-qualification-20261012.md):
  recover indexed reads/font-address rematerialization under the unchanged
  profile. Reject the 168-difference shape for private alias behavior; the
  call-only capture fixes six bounded SP+0x68 cases, but remains 218 words /
  174 differences with one extra saved register. Thirteen tests, public/
  native qualification and both copied owners/seven neighbors/pools/padders
  pass; a late-read control is effective. Production/data/totals are unchanged,
  tools ce4cc1a first, older unrelated work preserved/no push. Continue the
  same target's original T0/S3 lifetime fit and full private/fault/rebase/
  linked qualification; no installation or matching credit, full Game open.

- [Text measurer native32 qualification](WORKING_NOTES/1294-game-text-measurer-native32-qualification-20261012.md):
  both complete C candidates and recovered helpers pass 733 native cases each
  at O2/O0, including portable aliases, guarded buffers/table and eleven
  effective semantic/canary controls. Nine focused tests pass. An isolated
  219-word/frame-0x80 form still has 206 differences; no profile, source or
  ELF installation. Production inputs/data/totals stay unchanged. Tools
  b5e4600 first, older history/unrelated hashes preserved/no push. Continue
  the same target's original layout and owner/padder/rebase/fault/linked
  qualification; full Game and hardware/renderer/gameplay stay open.

- [Text measurer full-chain qualification](WORKING_NOTES/1293-game-text-measurer-full-chain-qualification-20261012.md):
  complete original219/candidate chains use actual normalizer65/metrics115,
  no hooks. Seven tests, live pointer/truncation and eight compiled controls
  pass. The closer 217-word/frame-0x80 candidate has 185 differences, not a
  match or installation. All nine production inputs/data and aggregate totals
  are unchanged. Tools 688ae3b first, older work preserved/no push. Continue
  this function's original layout, native/owner/padder/rebase/fault and linked
  qualification; the full Game goal remains open.

- [Character normalizer guarded match](WORKING_NOTES/1292-game-character-normalizer-guarded-match-20261012.md):
  complete 68-word slot, 65-word/frame-zero C body/twelve guards/three zeros,
  not direct C. Restore byte normalization and first match in the original
  95-entry table; exercise 61 reachable words and preserve four unreachable
  words. Nine pre-install/nine final installed tests, native32, aliases/rebases/
  faults and caller windows pass. Only 198 target/size ELF bytes change;
  other bytes/ten inputs/seven neighbors exact. Tools 05875fe first, older
  work preserved/no push. Next full text measurer func_150428D4, 219 words /
  199 differences, frame 0x80; wider Game goal remains open.

- [Extended-character metrics direct match](WORKING_NOTES/1291-game-extended-character-metrics-direct-match-20261012.md):
  all 115 words/frame zero direct C, unchanged no-unroll profile/no guards;
  six-argument switch bound to the original 19-entry table and live floats.
  Nine installed tests, native32, aliases/rebases/faults and actual callsite
  windows pass, not full formatter acceptance. Only 521 ELF bytes change:
  312 target/two size/207 exact metadata reorderings; other bytes/nine inputs/
  seven neighbors exact. Tools 5d3c18b first, older work preserved, no push.
  Next func_15042C40, 68-word slot/62 differences, byte normalizer/glyph lookup;
  full Game goal stays open.

- [Glyph rectangle and typed caller guarded match](WORKING_NOTES/1290-game-glyph-rectangle-and-typed-caller-guarded-match-20261012.md):
  full 54-word/frame-zero SDK draw, eleven closed allocation guards, not
  direct C. Correct caller/prototype scalar-coordinate/Gfx types without
  changing its raw object or nine guards. Eight pre-install/eight installed
  tests, actual caller/lookup/draw chain, full SDK native32 and controls pass.
  Only 165 target/size ELF bytes change; other bytes/ten inputs/seven neighbors
  and old guard prefix remain exact. Tools 69d7a80 first, older work preserved,
  no push. Next func_150415E0, 115/112 words/differences, metrics resolver;
  guard removal and full Game goal remain open.

- [Intensity texture setup direct match](WORKING_NOTES/1289-game-intensity-texture-setup-direct-match-20261012.md):
  all 79 words direct SDK-macro C under the existing no-unroll owner profile;
  no frame/pool/guards/header/caller changes, one local declaration.
  Eight pre-install/eight installed tests, full SDK native32, ordered writes,
  rebases/fired faults and effective controls pass. Only 241 target/size ELF
  bytes change; every other byte/eleven inputs/seven neighbors remain exact.
  +1 matching only; tools 3fb9a26 first, older work preserved/no push.
  Next func_15041508, 54 words / 52 differences, glyph rectangle and typed
  scalar-coordinate/Gfx caller ABI. Full Game goal remains open.

- [Matrix decomposer guarded C conversion](WORKING_NOTES/1288-game-matrix-decomposer-guarded-c-conversion-20261011.md):
  all 141 words/frame 0xC0 exact with 63 allocation/scheduling guards, not
  direct C. Nine pre-install/nine final installed tests, actual vector helpers,
  native32 and wrapper/SDK/decomposer chain pass. Entire ELF unchanged; old
  guard prefix plus 63 rows and one generated progress asm-to-c cell.
  Converted +1/564 bytes. All 22 owner C rows exact with existing guards,
  no ASM/placeholders. Tools 6bee275 first, older work preserved/no push.
  Next display-list setup placeholder func_150412C0, 79/78 words/differences;
  guard removal, actual copy/trig and full Game goal remain open.

- [Matrix forward direct match](WORKING_NOTES/1287-game-matrix-forward-direct-match-20261011.md):
  all 40 executing words direct plus three original zero tail words; existing
  O2/g3 profile, two required local declarations, no new guards/callers.
  Ten pre-install/ten installed tests, actual SDK, native32 and original
  caller152 pass. Only 119 target/size ELF bytes change; every other byte/
  eight inputs/21 neighbors exact. Tools dbc0f0d first, older work preserved,
  no push. All 21 C rows here match with existing guards; next full 141-word
  matrix decomposer func_1503E5F8 ASM-to-C recovery. Full Game goal open.

- [Group-2 active timer direct match](WORKING_NOTES/1286-game-record-mask-active-direct-match-20261011.md):
  all 85 words direct C, no guards/pools/declaration/header/caller/profile
  changes. Eleven pre-install/eleven installed tests, native32 and original
  dispatcher/finish/active/teardown/query chain pass. Only 285 target/extent
  ELF bytes change; all other bytes/seven inputs/21 neighbors are exact.
  Tools a96b414 first, older work preserved/no push. Next func_1503F404,
  43 slot words / 38 differences, matrix forwarding wrapper; full Game goal open.

- [Group-2 mask finish direct match](WORKING_NOTES/1285-game-record-mask-finish-direct-match-20261011.md):
  all81 direct C, no guards/pools/header/caller/profile changes; twelve
  pre-install/twelve installed tests, native32 and actual dispatcher/predicate/
  finish/query chain pass. Only 274 target/extent ELF bytes change; other
  metadata/data/guards/seven inputs and 21 neighbors unchanged. Tools c7869ae
  first, older work preserved/no push. Next func_1503F2B0, 85/84 differences;
  prior Note 1278's caller/query evidence is available, full Game goal open.

- [Random vertical rate direct match](WORKING_NOTES/1284-game-record-random-vertical-rate-direct-match-20261011.md):
  complete45 direct C, no guards/profile/header/declaration/caller changes;
  twelve pre-install/twelve installed tests, native32 and actual dispatcher/
  predicate/finish/RNG chain pass. Only 135 target/extent ELF bytes change;
  all other metadata/data/guards/seven inputs and 21 neighbors unchanged.
  Tools 4cc2121 first, older work preserved/no push. Next func_1503F16C,
  81/80 differences; remaining callbacks and full Game goal stay open.

- [Record ground collision guarded match](WORKING_NOTES/1283-game-record-ground-collision-guarded-match-20261011.md):
  complete134 linked exact, 119 direct plus 15 closed initialization/register
  guards; twelve pre-install/twelve installed tests, native32 and actual timer/
  context chains pass. Only 443 ELF bytes change including one exact metadata
  swap; 21 neighbors/data/six inputs unchanged. Tools 7730335 first, older
  work preserved/no push. Former next func_1503EFC4 is directly matched in Note 1284; remaining
  bodies, guard removal and the full Game goal stay open.

- [Record impulse guarded match](WORKING_NOTES/1282-game-record-impulse-guarded-match-20261011.md):
  all 74 linked words exact, 69 direct plus five coefficient-register guards;
  twelve pre-install/twelve installed tests, native32 and actual caller/RNG
  chains pass. Only 257 ELF bytes change, including the measured four-entry
  metadata rotation; 21 neighbors/data/six inputs remain exact. Tools f6b3f22
  first, older work preserved/no push. Former next func_1503ECA0 is guarded-exact in Note 1283;
  guard removal and the full Game goal remain open.

- [Record motion guarded tail match](WORKING_NOTES/1281-game-record-motion-guarded-tail-match-20261011.md):
  all 71 reachable words direct C, one checked dead-return insertion, all 73
  linked exact but not full direct C. Twelve pre-install/twelve installed
  tests, native32 and actual five-body caller chain pass within documented
  boundaries. Only 226 target/extent ELF bytes change; 21 neighbors/data/six
  inputs exact, old guard prefix plus one row. Tools 6f16f59 first, older work
  preserved/no push, README aggregates only. Former next func_1503EB78 is
  guarded-exact in Note 1282; guard removal and full Game goal remain open.

- [Record matrix update direct match](WORKING_NOTES/1280-game-record-matrix-update-direct-match-20261011.md):
  complete138 direct C, no guards/profile/header/caller-body changes; thirteen
  pre-install/thirteen installed tests, native32 and actual matrix helpers/
  dispatcher chain pass within documented boundaries. Only 460 target/extent
  ELF bytes change, 21 neighbors/data/guards/seven inputs exact; +1 matching.
  Tools 73745f6 first, older work preserved/no push, README aggregates only.
  Next func_1503EA54, 73/71 differences; remaining callees/Game goal stay open.

- [Record transform setup direct match](WORKING_NOTES/1279-game-record-transform-setup-direct-match-20261011.md):
  complete141 direct C, no guards/profile/caller-body changes; thirteen
  pre-install/thirteen installed tests, native32 and connected retail helpers/
  dispatcher chain pass within documented boundaries. Only 445 target/extent
  ELF bytes change; 21 neighbors/data/guards/seven inputs exact, +1 matching.
  Tools 036e55c first, older work preserved/no push, README aggregates only.
  Next func_1503E82C, 138/138 differences; deeper callees/Game goal remain open.

- [Record mask teardown guarded match](WORKING_NOTES/1278-game-record-mask-teardown-guarded-match-20261011.md):
  complete 89-word body, 87 direct words/two closed spill guards,
  linked exact but not direct C;
  eleven pre-install/eleven installed tests and actual retail caller/predicate/
  query chain pass. Only 287 target/extent ELF bytes change, other bytes/inputs
  and 21 neighbors exact; +1 matching only. Tools 1c81a02 first, older work
  preserved/no push, README aggregates only. Next func_1503E3C4, 141/136
  differences; direct guard removal and full Game goal remain open.

- [Record-state dispatcher direct match](WORKING_NOTES/1277-game-record-state-dispatcher-direct-match-20261011.md):
  complete171 direct C/no guards, actual caller/predicate chain; thirteen
  pre-install/22 installed and caller tests green. Only 562 target/extent/
  verified metadata bytes change, other bytes/inputs and 21/38 owner neighbors
  exact, +1 matching only. Tools 72fe857 first, older work preserved/no push,
  README aggregates only. Next unmatched func_1503E260, 89/89 differences.

- [Actor group mask command direct match](WORKING_NOTES/1276-game-actor-group-mask-command-direct-match-20261011.md):
  complete39 direct C/no guards, actual helper/three callers, ten pre-install /
  eleven installed tests plus focused controls green. Exactly 127 ELF bytes
  change, 21 neighbors/data/guards/other inputs exact, +1 matching only.
  Tools 3b4d8ec first, older work preserved/no push; README aggregates only.
  Next unmatched func_1503DF48, 171 words/168 linked differences.

- [Third-loader exit scheduling and drop removal](WORKING_NOTES/1275-game-third-resource-loader-exit-scheduling-and-drop-removal-20261011.md):
  raw37/7 -> 36/2, two final scheduling guards/no drop, 34 direct words and
  linked36 exact; not direct C. Fourteen pre-install/151 installed and regression
  tests pass; entire ELF/data/seven other inputs/counts unchanged. Tools 36adf10
  first, older work preserved/no push, root README unchanged. Next unmatched
  func_1503DE70, 39 words/38 linked differences; final raw guards stay open.

- [Third-loader lifetime and guard reduction](WORKING_NOTES/1274-game-third-resource-loader-incoming-result-lifetime-and-guard-reduction-20261011.md):
  raw 37/15 -> 37/7, six normalizations -> three plus one drop; linked 36
  exact, not direct C. Thirteen pre-install/137 installed and regression tests
  pass, actual seventeen-body chain. Entire ELF/data/seven other inputs exact,
  counts/root README unchanged. Tools 5eb0c4a first, older work preserved,
  no push. Remaining shared-status exit guards and deeper runtime stay open.

- [Third-loader guard audit and actual chain](WORKING_NOTES/1273-game-third-resource-loader-guard-audit-and-actual-chain-20261011.md):
  existing guarded 36 words exact; raw 37/15, guard elimination still open.
  Twelve new/fifteen SDK tests pass, actual seventeen-body chain and real
  status-two failures. Production inputs/data/counts and root README unchanged.
  Tools b6877d5 first, older history/fingerprints preserved, no push.

- [Record resource-cleanup direct match](WORKING_NOTES/1272-game-record-resource-cleanup-direct-match-20261011.md):
  all 43 body words directly exact, original frame/lifetimes and live callback
  loop, 172-byte extent / 180-byte slot. Twelve pre-install/97 installed and
  regression tests pass, actual cleanup/release and sixteen-body parent chains.
  Exactly 149 ELF bytes change including fourteen checked metadata bytes;
  other bytes/data/inputs exact. +1 matching, tools 663f63b first, older history
  preserved/no push. Next already-exact third-loader guard elimination and
  actual chain qualification, not another matching credit; runtime stays open.

- [Group publication-propagation direct match](WORKING_NOTES/1271-game-group-publication-propagation-direct-match-20261011.md):
  all 56 words directly exact, void/full-word identity, cached group inputs/
  live ordered values, no new guards/profile changes. Twelve pre-install/85
  installed and regression tests pass, actual seven-/14-body chains. Only
  165 ELF bytes change; all other bytes/data/guards/recipe/CSV exact.
  +1 matching, tools 0e3d520 first, older history preserved/no push.
  Next full 43-word func_1503DD1C / 45-word padded slot; third loader already
  guarded-exact, raw guard elimination and deeper runtime remain separate.

- [Descriptor resource-loader direct match](WORKING_NOTES/1270-game-descriptor-resource-loader-direct-match-20261011.md):
  all 69 words directly exact, original frame/lifetimes, no new guards/profile
  changes. Twelve pre-install/73 installed and regression tests pass, actual
  13-body chain/all target words. Only 197 ELF bytes change; other bytes/data/
  guards/recipe/conversion inputs exact. +1 matching, tools 9359eb3 first,
  older history preserved/no push. Next full 56-word func_1503D510;
  parent/pair guard elimination and deeper runtime remain separate.

- [Vertex-coordinate copy guarded match](WORKING_NOTES/1269-game-vertex-coordinate-copy-guarded-match-20261011.md):
  full 96 linked words exact, 92 direct plus four frame/count-spill guards.
  Per-function unrolled selection preserves all 14 neighbors. Twelve
  pre-install/61 final installed and regression tests pass; actual child
  replaces its model in the eight-body loader chain. Only 298 ELF bytes
  change; other bytes/data/conversion inputs exact, old guard prefix intact.
  +1 matching, tools 1310ff7 first/no push. Next full 69-word func_1503D660;
  raw guard elimination and deeper runtime stay separate.

- [Command weight counter direct match](WORKING_NOTES/1268-game-command-weight-counter-direct-match-20261011.md):
  all 46 words directly exact, no frame or new guards. Eleven pre-install/49
  installed and regression tests pass, every counter word reached in the
  actual seven-body loader chain. Only 126 ELF bytes change; all other bytes/
  data/guards/CSV exact. +1 matching, tools 23570e9 first/no push. Next full
  96-word func_1503D804; parent guard elimination and runtime stay separate.

- [Command-stream relocator direct match](WORKING_NOTES/1267-game-command-stream-relocator-direct-match-20261011.md):
  full 52-word SDK Gfx scan emits directly, original frame, no new guards.
  Eleven pre-install/38 installed and regression checks pass, including the
  actual child in the loader chain. Only 159 ELF bytes change, all other
  bytes/data/guards/CSV exact. One matching credit, tools 349aa21 first/no push.
  Next full 46-word func_1503D984; parent guard elimination/runtime separate.

- [Main resource-loader full guarded match](WORKING_NOTES/1266-game-main-resource-loader-guarded-match-20261011.md):
  all 274 linked words exact, unchanged semantic C/original frame; 252 direct
  words plus 22 closed guards. All 76 installed/older tests pass, complete
  stack/public faults and stale-guard rejection; only 26 target ELF bytes
  change, all other bytes/data/CSV exact. One matching credit only.
  Next full 52-word command-stream relocator func_1503D368; raw guard
  elimination and deeper runtime remain separate, tools first/no push.

- [Main resource-loader first-loop delay initialization](WORKING_NOTES/1265-game-main-resource-loader-first-loop-delay-initialization-match-20261011.md):
  same full 274-word/original-frame loader recovers two independent initialization
  words; raw differences 24 -> 22, no guards. Twelve installed tests pass;
  only eight target ELF bytes change, every other byte/data/guard/CSV exact.
  Same function's spill slots/request return/cleanup remain open, no matching credit.

- [Main resource-loader private layout and count schedule](WORKING_NOTES/1264-game-main-resource-loader-private-layout-and-count-schedule-improvement-20261011.md):
  full 274-word/original-frame loader recovers three private slots, unmasked
  count store/register cycle and event order; raw differences 98 -> 24,
  no guards. Twelve final/32 older/five historical tests pass; only 92 target
  ELF bytes change, all other bytes/data/guards/CSV exact. Same full function remains
  next, no matching credit or README aggregate change.

- [Main resource-loader original-frame improvement](WORKING_NOTES/1263-game-main-resource-loader-original-frame-improvement-20261011.md):
  full 274-word loader restores original 0x78 frame/S0..S6 and removes the
  count-pointer stack copy; raw differences 271 -> 98, no guards. Eleven
  final selected tests and 21 older tests pass; only 882 target ELF bytes
  change, every other byte/data/guard/CSV exact. No credit; same full
  function's private slots and remaining schedule stay next.

- [Main resource-loader status-join experiment](WORKING_NOTES/1262-game-main-resource-loader-status-join-experiment-20261011.md):
  controlled return join selects S6; five tests/31 complete isolated candidates
  pass. Frame still wrong, no installation or matching credit. Eleven fresh
  installed tests pass; whole linked baseline and README unchanged. Continue
  this same full function's extra count-pointer copy, frame and byte matching.

- [Main resource-loader retail-length improvement](WORKING_NOTES/1261-game-main-resource-loader-retail-length-improvement-20261011.md):
  full func_1503CF20 emits all 274 words, smaller 0x80 frame/271 raw
  differences, no guards; not yet byte-exact. Eleven final tests plus ten
  fresh recovery tests pass. Only 566 target/extent ELF bytes change,
  all other code/data/guards/CSV exact. No matching credit; continue this
  same complete function's original frame, S6 status and byte matching.

- [Main resource-loader recovery](WORKING_NOTES/1260-game-main-resource-loader-recovery-20261011.md):
  complete func_1503CF20 replaces its zero-return stub; 272 emitted words
  in the 274-word slot, larger frame/273 raw differences, no guards.
  Ten final tests, full reachable retail coverage, native32, aliases/faults
  and actual five-routine chain pass within bounded deeper helpers.
  All other code/data/guards/CSV exact. No matching credit; continue this
  same function's original frame and byte matching.

- [Resource extras loader direct match](WORKING_NOTES/1259-game-resource-extras-loader-direct-match-20261011.md):
  all 56 func_1503DC3C words/original frame directly from complete C, no
  guards. Ten final tests, live count/base publication aliases and actual
  caller/extras/buffer chain pass. Only 170 target/extent ELF bytes change;
  all other bytes/guards/CSV exact, +1 matching. Full main-loader semantics
  are recovered in Note 1260; its byte matching/deeper runtime stay open.

- [Resource preparation caller direct match](WORKING_NOTES/1258-game-resource-preparation-caller-direct-match-20261011.md):
  all 104 func_1503DA9C words/original frame directly from complete C, no
  guards. Ten final tests, full caller coverage, live extras mutations and
  actual buffer-callee failures pass. All other code/data/guards/CSV exact;
  +1 matching only. Its then-open extras loader is finished in Note 1259;
  main resource loader/deeper runtime remain open.

- [Resource buffer preparation guarded match](WORKING_NOTES/1257-game-resource-buffer-preparation-guarded-match-20261011.md):
  full 194-word func_15084044/retail frame, complete C plus 29 bounded
  register/copy-schedule guards, not a direct C match. Fourteen final tests,
  high-bit pointer cases and 116 fired stale-guard rejections pass.
  Only 47 target ELF bytes change; all other bytes/old guard history exact.
  +1 matching only. Next: complete 104-word resource-preparation caller;
  deeper resource loading/hardware/gameplay remains open.

- [Resource buffer retail-length improvement](WORKING_NOTES/1256-game-resource-buffer-retail-length-improvement-20261011.md):
  func_15084044 emits all 194 words/retail frame without guards; raw
  differences 130 -> 39. Twelve final tests and both WSL tools checks pass.
  Only target slot/extent change from the committed recovery, 317 ELF bytes;
  all other bytes and protected inputs exact. Byte matching stays open,
  no inflated progress credit; continue opening allocation/copy fallback.

- [Resource buffer preparation recovery](WORKING_NOTES/1255-game-resource-buffer-preparation-recovery-20261011.md):
  complete func_15084044 modes/sharing/copy/failure rollback, retail frame;
  eleven final tests, native32/faults/rebases and bounded SDK/caller connections.
  All neighbors/data/guards unchanged, no new guards or progress credit.
  Not yet byte-exact: 130 word differences remain; continue this function.

- [Record identity selector direct match](WORKING_NOTES/1254-game-record-identity-selector-direct-match-20261011.md):
  all 27 words directly from C, no frame/guards; preserve retail restart
  at index one and 0xFF cap. Nine final tests/both WSL tools checks pass,
  exhaustive pairs/native32/fault prefixes and complete retail caller within
  explicit callback/category bounds. All 30 neighbors/data/guards/CSV exact,
  +1 matching only. Next: full 194-word buffer pair ownership/preparation;
  deeper caller/resources/hardware/gameplay remains open.

- [Actor-identity lookup direct match](WORKING_NOTES/1253-game-actor-identity-lookup-direct-match-20261011.md):
  all 72 words directly from C, no frame/guards; original scans 26 slots,
  correcting the previous handoff bound. Ten final tests/both WSL tools
  checks pass, full access faults/native32/rebases and two actual linked
  callers plus retail record-query connection. All 30 neighbors/data/guards/
  CSV exact, +1 matching only. Next: complete 27-word record identity selector;
  actual initializer/hardware/gameplay remains open.

- [Record-index query direct match and census](WORKING_NOTES/1252-game-record-index-query-direct-match-and-census-20261011.md):
  all 33 words directly from C, no frame/guards. Ten final tests/both WSL
  tools checks pass; full access faults/native32/rebases and complete retail
  caller (current C caller still a stub). Correct omitted native symbol/layout
  row; 30 neighbors/data/guards exact, converted bytes unchanged. Next:
  full 72-word actor-identity lookup; actual runtime remains open.

- [Animation child cleanup direct match](WORKING_NOTES/1251-game-animation-child-cleanup-direct-match-20261011.md):
  all 66 words/original 0x30 frame directly from C, no guards. Nine final
  tests/both tools checks pass, full fault pairs/native32, both padding
  routes and actual complete two-call caller; 30 neighbors/data/guards/CSV
  exact, +1 matching only. Next: full 33-word record-index query; runtime open.

- [Animation state allocation direct match](WORKING_NOTES/1250-game-animation-state-allocation-direct-match-20261011.md):
  all 51 words/original 0x28 frame directly from C, no new guards. Typed
  constructor scale call preserves its full fingerprint. Ten final tests/
  both tools checks pass, modeled faults/native32 and actual three-helper
  connection; all 30 neighbors/data/guards/CSV exact, +1 matching only.
  Next: full 66-word descriptor-child cleanup; actual SDK/runtime remains open.

- [Actor resource fields direct match](WORKING_NOTES/1249-game-actor-resource-fields-direct-match-20261011.md):
  all 68 words/original 0x18 frame directly from C, no new guards. Nine final
  tests/both tools checks pass, 1,265 full fault pairs, native32 and actual
  complete constructor connection. All 30 neighbors/data/guards/CSV exact;
  only target slot/extent changes, +1 matching. Next: full 51-word animation
  helper; actual deeper resource/hardware/gameplay acceptance remains open.

- [Child actor constructor byte match](WORKING_NOTES/1248-game-child-actor-constructor-byte-match-20261011.md):
  all 182 words/original 0x38 frame using unchanged C and checked closed
  normalization; thirteen final tests/both tools checks pass. Public/native32/
  actual caller/helper and original private frame/2,214 full fault pairs
  qualify. All 30 neighbors/other ELF/metadata/data/CSV exact; +1 matching.
  Next: full 68-word resource-field initializer; actual runtime remains open.

- [Child actor constructor reconstruction](WORKING_NOTES/1247-game-child-actor-constructor-reconstruction-20261011.md):
  all 182 C words without new guards, ordered status/scale writes, live
  allocation limit and incoming homes. Nine final tests/both tools checks
  pass, public faults/native32 and actual caller/resource helper qualified.
  All 30 neighbors/other ELF/data/guards/CSV exact; no matching credit.
  Next: original 0x38 frame and 125 remaining word differences; runtime open.

- [Animation scratch preparation byte match](WORKING_NOTES/1246-game-animation-scratch-preparation-byte-match-20261011.md):
  all 191 words/original 0x68 frame with checked closed normalization;
  thirteen final tests/both tools checks pass. Public/native32/actual caller
  and fitted private frame/fault qualification; all 37 neighbors/other ELF/
  data/CSV exact and old guard prefix retained. +1 matching credit only.
  Next: full 182-word constructor; actual PI/hardware/renderer/gameplay open.

- [Animation scratch loop shape improvement](WORKING_NOTES/1245-game-animation-scratch-loop-shape-improvement-20261011.md):
  guarded do-loop drops raw/linked differences 162 -> 102 without guards;
  ten final tests/both tools checks pass, public faults/native32 and actual
  refresh/caller requalified. All 37 neighbors/other ELF/data/guards/CSV exact;
  no matching credit then. Original 191-word/0x68 match and fitted private
  fault order completed in Note 1246; actual runtime stays open.

- [Animation scratch preparation reconstruction](WORKING_NOTES/1244-game-animation-scratch-preparation-reconstruction-20261011.md):
  complete one/two-bank C, aligned PI packets and wrap/live reloads; ten final
  tests, nine scoped submit regressions and both tools checks pass. Actual
  refresh/caller connections, native32 and public fault/alias qualification;
  37 neighbors/all other ELF/data/CSV unchanged. Typed void declaration retires
  three submit guards, preserving its exact body with two. No matching credit:
  preparation had 162 differences, then 102 in Note 1245, now byte-exact in
  Note 1246. Actual PI/hardware and full renderer/gameplay remain open.

- [Complete node transform submission byte match](WORKING_NOTES/1243-game-node-transform-submission-byte-match-20261011.md):
  full 66-word C/original frame with five checked guards; ten final target
  tests, nine scoped behavior regressions and both tools checks pass. Live
  selector, NULL preparation, transform packet, native32, actual bounded
  timeline helpers and three synthetic caller windows qualify. All four owner
  routines exact; all other ELF/data/CSV retained. +1 matching credit only.
  Preparation semantics restored in Note 1244; its byte match and runtime stay open.

- [Complete alternate resource loader byte match](WORKING_NOTES/1242-game-complete-node-alternate-loader-byte-match-20261011.md):
  full 99-word C/original frame and 24 closed S0/S1 guards; ten final target
  tests, 17 scoped regressions and both tools checks pass. Live outputs,
  NULL-free gates, guest unwritten-count boundary and real initializer/default/
  action chain qualify. Three neighbors/all other ELF/data/CSV exact; +1
  matching credit only. Full 66-word follow-up completed in Note 1243; runtime stays open.

- [Complete default resource loader direct byte match](WORKING_NOTES/1241-game-complete-node-resource-loader-direct-byte-match-20261011.md):
  full 114-word C/original frame without guards; ten final tests/both tools
  checks pass. Live record/count loop, cache rollover, native32 and actual
  initializer consuming real outputs qualify; all 39 neighbors/other ELF/data/
  guards/CSV exact. +1 matching credit. Alternate-loader follow-up completed
  in Note 1242; complete resource/allocator/gameplay work stays open.

- [Complete node release byte match](WORKING_NOTES/1240-game-complete-node-release-byte-match-20261011.md):
  full 102-word C with five closed register-transfer guards and retail memory
  order; ten final tests/both tools checks pass. Native32, actual dispatcher
  and factory/initializer rollback qualify; all 39 neighbors/other ELF/data/CSV
  exact. +1 matching credit. Next: full 114-word func_1502FE10; complete
  resource/allocator and hardware/live gameplay work remain open.

- [Complete node resource initializer byte match](WORKING_NOTES/1239-game-complete-node-resource-initializer-byte-match-20261011.md):
  full 96-word C with 12 checked guards; ten final tests and both tools checks
  pass. Both loader packets, allocation rollback, native32 and actual caller/
  factory/action connection qualify. All 39 neighbors/other ELF/data/CSV exact;
  +1 matching credit. Deeper zero loaders lack required outputs, not restored
  resources. Next: full func_15030158; cleanup/gameplay remain open.

- [Complete animation node constructor byte match](WORKING_NOTES/1238-game-complete-animation-node-constructor-byte-match-20261010.md):
  full 152-word C with 47 checked scheduling guards; ten final tests pass.
  Actual caller/action consumer, native32 and eight retail samples qualify.
  All 39 neighbors and other ELF/data/CSV bytes exact; +1 matching credit.
  Next: full func_1502FFD8; actual resource/cleanup bodies and gameplay stay open.

- [Complete actor animation constructor byte match](WORKING_NOTES/1237-game-complete-actor-animation-constructor-byte-match-20261010.md):
  full 89-word C with 17 checked guards; nine final tests pass. Actual caller
  chain and eight retail descriptor samples qualify. Explicit helper signature
  correction adds four incoming home stores but remains a zero stub; all 29
  other neighbors and remaining ELF/data/CSV bytes exact. +1 matching credit.
  Next: full func_15030AF4; actual deeper helpers and gameplay remain open.

- [Actor animation request direct conversion](WORKING_NOTES/1236-game-actor-animation-request-direct-conversion-20261010.md):
  all 30 words emit directly from C without guards; nine final tests pass.
  Signed scale/typed float packet and actual record caller/lookup/list/classifier
  chain qualify. Whole ELF/guards/data/symbols/14 neighbors exact; +120 C bytes.
  Next: full func_15083568 constructor, still a zero-return placeholder;
  its actual body and FCSR/hardware/live gameplay acceptance remain open.

- [Actor definition count direct conversion](WORKING_NOTES/1235-game-actor-definition-count-direct-conversion-20261010.md):
  all 32 words emit directly from C without guards; ten final tests pass.
  Actual channel/count/lookup/classifier/list chain and original animation
  bytes qualify. Whole ELF/guards/data/symbols/14 neighbors exact; +128 C bytes.
  Next: full func_1507EA44; animation/finish/runtime acceptance stays open.

- [Actor definition lookup direct conversion](WORKING_NOTES/1234-game-actor-definition-lookup-direct-conversion-20261010.md):
  all 24 words emit directly from C without guards; nine final tests pass.
  Actual classifier/channel caller and native callbacks qualify. Whole ELF,
  guards/data/symbols and 14 neighbors exact; +1 conversion / 96 C bytes.
  Next: full func_1507E968; real assets/runtime remain separate open gates.

- [Complete actor channel transition conversion](WORKING_NOTES/1233-game-complete-actor-channel-transition-conversion-20261010.md):
  full 73-word C with five checked guards; nine final tests pass. Code/data
  unchanged; remove one stale absolute assignment and recover the omitted map
  boundary; tracked Splat declaration prevents regeneration. +1 counted/converted
  function and 292 C bytes. Next: func_1507E908.

- [Actor channel reset direct conversion](WORKING_NOTES/1232-game-actor-channel-reset-direct-conversion-20261010.md):
  all 28 words emit directly from C without guards; ten final tests and actual
  helper/caller checks pass. Whole ELF/guards/data unchanged, +1 conversion.
  Next: complete func_1507E7E4, including its other priority branches.

- [Complete actor resource transition byte match](WORKING_NOTES/1231-game-complete-actor-resource-transition-byte-match-20261010.md):
  install full 70-word routine with 15 checked guards; nine final tests,
  full linked audit, preserved prefix/data and +1 matching credit.
  Next: full func_1507EABC; actual helpers/runtime remain separate open gates.

- [Complete actor animation selector byte match](WORKING_NOTES/1230-game-complete-actor-animation-selector-byte-match-20261010.md):
  install full 98-word routine with 14 qualified guards; nine final tests,
  full linked audit, retained prefix/data and +1 matching credit.
  Next: full func_150837D4; actual callbacks and runtime acceptance stay open.

- [Complete tile updater and actual special helper byte match](WORKING_NOTES/1229-game-complete-tile-updater-and-special-helper-byte-match-20261010.md):
  install both full bodies, 123 guarded/direct 52-word matches; eight final
  tests, whole linked audit, preserved prefix/data and +2 matching credit.
  Next: complete func_1502FBE8; separate runtime/FCSR gates remain open.

- [Complete actor texture tile updater qualified schedule and padding](WORKING_NOTES/1228-game-actor-texture-tile-updater-qualified-schedule-and-padding-20261010.md):
  all 123 fitted words exact, complete 120-word C, no missing-body fill; pass
  private order/faults/rebases/stale/native/caller checks. Actual special helper
  and production installation remain open; no new matching credit.

- [Complete actor texture tile updater recovery and layout gates](WORKING_NOTES/1227-game-actor-texture-tile-updater-recovery-and-layout-gates-20261010.md):
  qualify full commands/callbacks, aliases/faults, native SDK and actual callers.
  Original 123-word layout remains open; production/counts unchanged.

- [Actor color provider and complete renderer byte match](WORKING_NOTES/1226-game-actor-color-provider-and-complete-renderer-byte-match-20261010.md):
  install both full bodies; eight post-install tests, whole linked audit,
  preserved guards/data and +2 matching credit. Bounded callbacks remain open.

- [Complete actor renderer actual color and matrix connections](WORKING_NOTES/1225-game-complete-actor-renderer-actual-color-and-matrix-connections-20261010.md):
  qualify complete original color/fog and both banked matrix chains, full
  caller paths and fired connected faults. Original/fitted private state exact;
  raw saved-PC adjustment is explicit. Recover production color C before installation.

- [Complete actor renderer native32 SDK qualification](WORKING_NOTES/1224-game-complete-actor-renderer-native32-sdk-qualification-20261010.md):
  pass 660 complete executions with actual SDK macros, expanded boundaries,
  four effective negatives and pointer-provenance regression. Not installed;
  complete actual helper-chain qualification remains open.

- [Complete actor renderer certified schedule and padding](WORKING_NOTES/1223-game-complete-actor-renderer-certified-schedule-and-padding-20261010.md):
  fit all 532 words with original private homes; qualify closed guards,
  actual whole-owner padding, full fault prefixes and independent links.
  Not installed; native32 SDK and complete real-helper chain remain open.
- [Complete actor renderer original private layout](WORKING_NOTES/1222-game-complete-actor-renderer-original-private-layout-20261010.md):
  recover original frame and private homes; eight tests qualify complete
  private access order, aliases, fired fault prefixes and exact neighbors.
  Raw remains 531/532 words; close layout and real-helper gates before installation.
- [Complete actor renderer recovery and private gates](WORKING_NOTES/1221-game-complete-actor-renderer-recovery-and-private-layout-gates-20261010.md):
  recover the full 532-word renderer; nine tests pass, with public order and
  37 neighbors exact. Frame/private homes were open, now closed in Note 1222.
  Not installed; complete layout and connected qualification remain open.
- [Complete actor alpha-shading byte match](WORKING_NOTES/1220-game-actor-alpha-shading-byte-match-20261010.md):
  restore all 125 words and original private outputs; qualify closed guards,
  full fault prefixes and real dispatcher/RGB/shading/matrix connections.
  Next: complete 532-word eight-argument renderer func_1502CCFC.
- [Actor RGB parameter writer direct match](WORKING_NOTES/1219-game-actor-rgb-parameter-writer-direct-match-20261010.md):
  restore all 57 words directly from C; qualify ordered aliases/faults,
  native32, independent links and complete actual dispatcher connections.
  Next: full shading/alpha callback func_1502D630 and matrix-helper contract.
- [Complete actor render-dispatch byte match](WORKING_NOTES/1218-game-actor-render-dispatch-byte-match-20261010.md):
  restore all 176 words and original private homes; qualify closed guards,
  complete fault prefixes, aliases and real parent/helper connections.
  Next: full RGB parameter callback func_1502D54C.
- [Actor render-dispatch lifetime and private counterexamples](WORKING_NOTES/1217-game-actor-render-dispatch-lifetime-and-private-counterexamples-20261010.md):
  measure 62 full/profile forms; scoped flag reaches 176 words, but original
  frame/private homes remain open. Bank public/native tests and explicit
  private/ABI counterexamples without installation or matching credit.
- [Actor render-dispatch recovery and layout gates](WORKING_NOTES/1216-game-actor-render-dispatch-recovery-and-layout-gates-20261010.md):
  qualify the complete caller's public behavior and real helper connections;
  retain installation gates for 176-word length and original private homes.
- [Actor distance-tier updater byte match](WORKING_NOTES/1215-game-actor-distance-tier-updater-byte-match-20261010.md):
  restore all 163 words and private homes; qualify ordered float thresholds,
  selector clamp, real identity leaf and bounded caller forwarding.
  Next: complete 176-word caller func_1502C974.
- [Actor counter-updater direct byte match](WORKING_NOTES/1214-game-actor-counter-updater-byte-match-20261010.md):
  restore all 56 words and private homes directly without guards; qualify
  signed wraps, callback mutations and actual dispatcher/classifier connections.
  Next: 163-word distance-tier updater func_1502C6E8.
- [Actor attachment-updater byte match](WORKING_NOTES/1213-game-actor-attachment-updater-byte-match-20261010.md):
  restore all 89 words; qualify raw float copies, aliases, fresh inclusive
  limits and actual dispatcher/updater connections. Next: state-2 counter.
- [Actor segment-selector byte match](WORKING_NOTES/1212-game-actor-segment-selector-byte-match-20261010.md):
  restore all 146 words and private homes; qualify complete fault traces,
  actual callees and bounded call-site forwarding. Next: attachment updater.
- [Actor segment-selector recovery and layout gates](WORKING_NOTES/1211-game-actor-segment-selector-recovery-and-layout-gates-20261010.md):
  qualify complete callback-sensitive selection and ordered SDK commands; reject
  installation pending the original physical frame and 146-word extent.
- [Slot byte-updater byte match](WORKING_NOTES/1210-game-slot-byte-updater-byte-match-20261010.md):
  restore all 74 words, qualify real classifier/flag-helper/dispatcher connections,
  and preserve every other linked byte; next is the four-segment graphics selector.
- [Object phase-updater byte match](WORKING_NOTES/1209-game-object-phase-updater-byte-match-20261010.md):
  All 78 linked words match with signed/wrapping products and fresh tick reloads.
  Ten tests pass before/after; one neighboring table guard requalified, its code
  unchanged. Game 2,752 exact. Next: 74-word slot updater func_1502EEF4.

- [Object color-mode helper byte match](WORKING_NOTES/1208-game-object-color-mode-helper-byte-match-20261010.md):
  All 150 linked words match with original frame/case starts and protected table.
  Ten tests pass before/after; Game 2,751 exact. Next: 78-word phase updater.

- [Object color-mode recovery and table gates](WORKING_NOTES/1207-game-object-color-mode-semantic-recovery-and-table-gates-20261010.md):
  Complete 148-word diagnostic with original frame; seven tests pass.
  Not installed: case starts, owner pool addend and full-word matching remain.

- [Captured-object metadata adapter byte match](WORKING_NOTES/1206-game-owner-captured-object-metadata-adapter-byte-match-20261010.md):
  All89 linked words match with original0x68 frame and closed register renames.
  Ten tests pass before/after; Game2,750 exact. Next: production helper func_1502EC34.

- [Owner fixed-span point initializer byte match](WORKING_NOTES/1205-game-owner-fixed-span-point-initializer-byte-match-20261010.md):
  All41 linked words match through41 guarded dependencies/no omissions.
  Nine tests pass before/after; Game2,749 exact. Next:89-word func_151B4A14.

- [Owner X-axis point interpolation byte match](WORKING_NOTES/1204-game-owner-x-axis-point-interpolation-byte-match-20261010.md):
  All44 linked words match through a closed46-row recipe/two omissions.
  Nine tests pass before/after; Game2,748 exact. Next:41-word func_151B4B78.

- [Linked-node endpoint transform direct match](WORKING_NOTES/1203-game-linked-node-endpoint-transform-direct-match-20261010.md):
  All65 words emit directly from C; nine tests pass before/after and only target
  slot/symbol extent changes. Game2,747 exact; next44-word func_151B48DC.

- [Owner threshold curve squared-copy/physical-frame gates](WORKING_NOTES/1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md):
  One squared copy and prior float boundaries qualify in a frame-shifted form.
  Eleven tests pass; saved writes/slot gates reject installation. Prior forms unchanged.

- [Owner threshold curve limit/projection home qualification](WORKING_NOTES/1201-game-owner-threshold-curve-limit-and-projection-home-qualification-20261010.md):
  Retail limit copies/two reads and projection home qualify; ten tests pass.
  Complete186-word diagnostic overflows; prior178-word slot form remains unchanged.

- [Owner threshold curve private vector-home recovery](WORKING_NOTES/1200-game-owner-threshold-curve-private-vector-home-recovery-20261010.md):
  Complete178-word diagnostic retains retail frame/saved homes with zero padding.
  Nine vector values/write multisets qualify; scalar/access/full-word gaps remain.

- [Owner threshold curve slot and delta-Y read recovery](WORKING_NOTES/1199-game-owner-threshold-curve-slot-and-delta-y-read-recovery-20261010.md):
  Complete170-word diagnostic fits; original frame/saved homes and full-path
  delta-Y home/read qualify. Nine tests pass; private/full-word gaps remain.

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
