# Conker's Bad Fur Day (N64) Decompilation

DOCS/PC_PORT_ROADMAP.md

A work-in-progress decompilation of *Conker's Bad Fur Day* for Nintendo 64.
The project reconstructs the original game code and data in a form that can be
built, studied, and matched against the retail ROM.

> [!IMPORTANT]
> This repository does not contain game assets or ROM files. You must provide
> your own legally obtained copy of the game.

## Project status

2026-09-08: restored `func_15060778` in `conker/src/game_83300.c` and
corrected the `func_10010E78` return ABI to preserve sound handles. The
swimming selection callback already exists in `game_981E0.c`. Full
non-matching ELF/bin build passes; core guest audio placeholders remain,
so this is not guest audio parity. Native counterpart and runtime limits:
[Note 305](../64CBFDOGL/DOCS/WORKING_NOTES/305-swimming-sound-callback-and-player-adapter-20260908.md).

The codebase is nearly fully represented in C, but byte matching is a separate
measurement. "Converted" means a function has C source; "byte-exact" means the
compiled instructions match the retail game exactly.

Snapshot verified on 2026-09-25. The current tree includes a broad restoration
of original assembly, so conversion is lower than the July snapshot; this is
not a regression in buildability or a byte-matching gain.

| Section | Converted functions | Converted bytes |
| --- | ---: | ---: |
| Total | 5,493 / 6,038 (90.97%) | 85.65% |
| Init | 508 / 538 (94.42%) | 90.79% |
| Game | 4,804 / 5,318 (90.33%) | 85.12% |
| Debugger | 181 / 182 (99.45%) | 99.19% |

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | `[###########-------------]` 2,544 / 5,493 (46.31%) | 1 | 2,948 |
| Init | `[##################------]` 387 / 508 (76.18%) | 1 | 120 |
| Game | `[##########--------------]` 1,976 / 4,804 (41.13%) | 0 | 2,828 |
| Debugger | `[########################]` 181 / 181 (100.00%) | 0 | 0 |

Debugger is complete across its full 182-row inventory. The one row outside
the C denominator is the original handwritten CP0/TLB routine
`func_16003650`; its complete 40-word linked extent also matches retail.

The sole address-only blocker is `func_10012588`; its C instructions match,
but its call still resolves to the wrong linked target. Regenerate the
measurements with:

```sh
make -C conker progress NON_MATCHING=1
make -C conker match-progress NON_MATCHING=1
```

See the [current status](DOCS/CURRENT_STATUS.md) for the resume boundary, the
[project overview](DOCS/PROJECT.md#current-progress) for measurement details,
and the [update log](DOCS/UPDATE_LOG.md) for milestone history.

## Build overview

Docker is the easiest supported environment. Native Linux and WSL also work;
native Windows without WSL or Docker is not supported by the matching IDO
toolchain.

1. Clone the repository with its submodules.
2. Place a big-endian US ROM at the repository root as `baserom.us.z64`.
3. Verify and extract the ROM.
4. Build the `conker/` code project.
5. Replace the rebuilt code sections and rebuild the ROM.

```sh
git clone --recursive <repository-url>
cd 64CBFD

make check
make extract
make -C conker extract
make -C conker --jobs
make -C conker replace NON_MATCHING=1
make --jobs
```

Validate the repository-local MIPS object wrappers independently with
`make tools-check`; this does not require a ROM. See
[project tools](DOCS/TOOLS.md) for usage and compatibility notes.

An unmatched development build may end with `build/conker.us.z64: FAILED`.
That means the rebuilt ROM differs from retail; it does not necessarily mean
the compiler or extraction setup is broken. Follow the
[complete build instructions](DOCS/PROJECT.md#normal-build-steps) for version,
ROM byte order, Docker, WSL, and troubleshooting details.

## Contributing

The most useful current work is byte matching game functions, finishing the
small raw-assembly remainder, documenting asset formats, and improving build
tools.

For function work, start with the
[contributor and byte-matching guide](DOCS/CONTRIBUTING.md). It covers the
normal edit/build/measure loop, retail-span constraints, generated slices,
compiler-sensitive patterns, and the checks expected before a change is
published.

## Documentation

Documentation is organized by purpose in the [documentation index](DOCS/README.md):

- **Start and build:** [Project overview](DOCS/PROJECT.md) and
  [code sub-project](DOCS/CODE_SUBPROJECT.md)
- **Contribute:** [Contributor and byte-matching guide](DOCS/CONTRIBUTING.md)
- **Formats and tooling:** [Asset formats](DOCS/ASSET_FORMATS.md),
  [compressed config sections](DOCS/CONFIG.md), and
  [IDO toolchain](DOCS/IDO_RECOMP.md)
- **Planning and history:** [PC port roadmap](DOCS/PC_PORT_ROADMAP.md),
  [update log](DOCS/UPDATE_LOG.md), and [working notes](DOCS/WORKING_NOTES.md)

## PC-port cross-project update - 2026-09-23

The sibling `64CBFDOGL` host port now completes Training through the natural Windy entrance and a fresh retained-save reload in RelWithDebInfo; repeat traversal used FLY. The user has **VERIFIED the second-level Chapters unlock**. The Gargoyle held-release repair uses original `func_15073A50` (232 bytes); guest/ROM builds and exact-byte checks are recorded in [host Note 738](../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md). This is scoped progression evidence, not complete retail presentation or full-game acceptance.

The host-only `conker_settings.exe` is implemented with four-port device assignments, shared keyboard/controller bindings, Save and input hot reload; Video/Audio/Paths remain placeholders. It does not add an N64-ROM settings executable or replace Ares settings. See [host settings guide](../64CBFDOGL/DOCS/CONKER_SETTINGS.md), [current host status](../64CBFDOGL/DOCS/CURRENT_STATUS.md) and [active host roadmap](../64CBFDOGL/DOCS/roadmap.md). Host Release is frozen after the requested 2026-09-23 `conker_pc` build; the latest Training suite retains its documented baseline failures/errors. No guest matching percentage is inferred from these host milestones.

2026-09-23 ([host Note738](../64CBFDOGL/DOCS/WORKING_NOTES/738-gargoyle-actor-and-original-held-release-20260923.md)): Restored original held-actor animation event15073A50 through existing GLOBAL_ASM in game_981E0.c. Guest/full ROM builds pass and linked/packaged232-byte body matches the ROM. Host live progression completes the Gargoyle, rock clearing and table scene, then reaches and reloads Windy. Guest runtime parity remains open.


2026-09-23 ([host Note737](../64CBFDOGL/DOCS/WORKING_NOTES/737-key-room-floor-boundary-and-frying-pan-progression-20260923.md)): Restored original authored movement boundary15055E50 and the containing1506D2E8 span with its no-op callback1506D4EC through existing GLOBAL_ASM bodies. Guest/ROM builds pass; linked/packaged768-byte and524-byte spans match the ROM. Host final RWD reaches frying pan and key pickup. Guest gameplay parity and independent terrain-producer placeholders remain open.


2026-09-23: [Note 736](../64CBFDOGL/DOCS/WORKING_NOTES/736-training-wall-collision-and-lever-release-20260923.md) restores handle attachment/release 15052260 from original GLOBAL_ASM in game_77AD0.c. Guest ELF/bin, replacement assets and outer NON_MATCHING ROM build pass; linked body matches all424 original bytes. Native lever release and key-room entry pass. Guest runtime and key-room/pan progression remain open.


2026-09-09: [Note 322](../64CBFDOGL/DOCS/WORKING_NOTES/322-helicopter-approach-cutscene-prerequisite-20260909.md) records the user-provided retail helicopter tutorial prerequisite: cross the water, approach midway on the far grass, and complete the automatically triggered scene before testing helicopter audio. No guest/native source or build change; overlapping typing input is excluded from acceptance.

2026-09-09: [Note 321](../64CBFDOGL/DOCS/WORKING_NOTES/321-signpost-effect-callback-and-audio-20260909.md) restores original GLOBAL_ASM callbacks 150B003C and 150AF200 in generated_DC6B0.c. Guest ELF/bin, replace and full non-matching ROM builds pass; all 312 linked and packaged instruction bytes match original ROM. Native signpost sound now restarts and persists. Fade cadence, complete guest gameplay and full audio parity remain open; no matching-C completion claim.

2026-09-09: [Note 320](../64CBFDOGL/DOCS/WORKING_NOTES/320-diving-splash-output-against-rom-20260909.md) verifies current native diving splash speaker output against original ROM. Existing guest water callback assembly remains intact; no source or applicable build change. Native Release remains frozen; broader audio and splash visuals remain open.


2026-09-09: [Note 319](../64CBFDOGL/DOCS/WORKING_NOTES/319-texture-backtrace-probe-and-pub-audio-20260909.md) gates a native-only texture allocator backtrace that blocks audio refills while loading PDB symbols. Guest src/init_3C40.c has no equivalent diagnostic; no IDO edit/build applies. Native default boot and full route are checked; boot-through-current-Training audio coverage remains open.

2026-09-09: [Note 318](../64CBFDOGL/DOCS/WORKING_NOTES/318-signpost-floor-query-and-intro-music-20260909.md) fixes a native-only category-06 player-query guard, restoring floor -3460 and removing unintended signpost music 3. Guest generated_13BB20.c E7A4/E950 and generated_49D30.c 1502178C remain placeholders with no equivalent guard; no IDO transplant or guest build applies to this patch. Guest collision restoration and full audio remain open.

2026-09-08: [Note 317](../64CBFDOGL/DOCS/WORKING_NOTES/317-active-surface-audio-callback-20260908.md) restores active surface callback 151A9AA4 through original GLOBAL_ASM in generated_1D6E80.c. All 252 linked bytes match original ROM; guest and outer NON_MATCHING builds pass. Native water-entry sound 0x10 now plays. Full audio and guest runtime remain unproven; no matching-C claim.

2026-09-08: [Note 316](../64CBFDOGL/DOCS/WORKING_NOTES/316-ambient-callback-and-audio-coverage-audit-20260908.md) restores native ambient callback 1000EB00. Existing guest src/init_EB00.c already links to the exact 196 ROM bytes, so no sibling source change is needed. Guest and outer NON_MATCHING builds pass. Entire audio and native natural callback dispatch remain unproven.

2026-09-08: [Note 315](../64CBFDOGL/DOCS/WORKING_NOTES/315-secondary-water-sound-owner-and-effect-lifecycle-20260908.md) restores 22 original water-effect routines through GLOBAL_ASM in four source owners. Guest ELF/bin and outer NON_MATCHING ROM builds pass; all 22 linked bodies match original ROM. Native deep dive now plays secondary 0x0A. Full audio and guest runtime parity remain open; no matching-C completion claim.

2026-09-08: [Note 314](../64CBFDOGL/DOCS/WORKING_NOTES/314-deep-water-state-and-entry-sound-20260908.md) restores six water-state/effect guest routines through original GLOBAL_ASM in three owners. Full non-matching ELF/bin builds; all six linked bodies match ROM. Native deep-water entry now plays 0x07. Remaining 0x0A, guest/runtime and full audio parity remain open; no matching-C completion claim.

2026-09-08: [Note 313](../64CBFDOGL/DOCS/WORKING_NOTES/313-water-effect-audio-owner-and-surface-query-scope-20260908.md) restores eight water-effect/audio guest bodies from original assembly in five source owners. Generated slices now support GLOBAL_ASM with retail padding. The full non-matching ELF/bin builds; all eight linked bodies match original ROM bytes and addresses. Native-only checked query scopes restore water-entry sound playback. Guest collision/audio placeholders and full audio parity remain open; no matching-C or guest runtime completion is claimed.

2026-09-08: [Note 312](../64CBFDOGL/DOCS/WORKING_NOTES/312-retail-and-native-dive-witness-and-gate-correction-20260908.md) verifies the native second-A water dive against original ROM and corrects the extra+31 gate interpretation. Original dive events only change motion; surrounding water audio remains open. Guest jump placeholder is unchanged; no guest build or complete audio parity is claimed.


2026-09-08: Note 311 records native logging-gate runtime checks and default
Training W/S validation. No source/build change; the reports remain host-only
with no IDO counterpart. Full audio and retail dive comparison remain open.
See [Note 311](../64CBFDOGL/DOCS/WORKING_NOTES/311-log-gate-runtime-check-and-training-movement-20260908.md).


2026-09-08 PAUSED: native-only DMA/script diagnostic logging candidate
built in Note 310; fresh runtime acceptance is pending. Guest counterparts
in conker/src/game_57FA0.c and conker/src/game/generated_DAFA0.c have no
such host reports, so no guest edit/build applies. Full audio remains open.
See [Note 310](../64CBFDOGL/DOCS/WORKING_NOTES/310-boot-audio-log-stall-candidate-and-pause-20260908.md).


2026-09-08: Note 309 restores native sound-owner transfer 100100E0.
The matching loop already exists in conker/src/init_EB00.c:474; no guest
source change/build is required. Natural caller execution and full audio
remain open. Native boot refill starvation is a separate host/task-flow
investigation. See [Note 309](../64CBFDOGL/DOCS/WORKING_NOTES/309-sound-owner-transfer-and-boot-refill-stall-20260908.md).


2026-09-08: Note 308 documents assets0F animation-event records from the
original ROM loader; all 152 nonempty payloads parse. See
[asset formats](DOCS/ASSET_FORMATS.md) and
[Note 308](../64CBFDOGL/DOCS/WORKING_NOTES/308-rom-animation-event-inventory-and-audio-boundary-20260908.md).
No production source change or new build; guest audio parity remains open.


2026-09-08: Animation sound-choice callback 1506C32C is restored from ROM
in game_981E0.c. The full non-matching ELF/bin build passes; downstream
1506BF5C remains a placeholder, so guest audio parity is still incomplete.
Native branch tests and boot regression are recorded in
[Note 307](../64CBFDOGL/DOCS/WORKING_NOTES/307-animation-sound-alternatives-and-boot-replay-20260908.md).
