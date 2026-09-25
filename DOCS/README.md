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
| Inspect the latest headline progress | [Root README](../README.md#project-status) |

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
