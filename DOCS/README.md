# Documentation

Use this page as the documentation index. Each subject has one primary home so
build instructions, matching guidance, research notes, and milestone history
do not compete with one another.

## Start here

| Goal | Read this |
| --- | --- |
| Understand the repository and build it | [Project overview](PROJECT.md) |
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
| `conker/` section build mechanics | `CODE_SUBPROJECT.md` |
| Confirmed ROM and asset behavior | `ASSET_FORMATS.md` or `CONFIG.md` |
| Future PC-port decisions | `PC_PORT_ROADMAP.md` |
| Completed milestones and public changes | `UPDATE_LOG.md` |
| Temporary findings and abandoned attempts | `WORKING_NOTES.md` |

The `tools/` subdirectories are mostly submodules and retain their own upstream
documentation. Do not move or rewrite those READMEs as project documentation.
