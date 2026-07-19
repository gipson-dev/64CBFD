# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for Nintendo 64.
The project reconstructs the original game code and data in a form that can be
built, studied, and matched against the retail ROM.

> [!IMPORTANT]
> This repository does not contain game assets or ROM files. You must provide
> your own legally obtained copy of the game.

## Project status

The codebase is nearly fully represented in C, but byte matching is a separate
measurement. "Converted" means a function has C source; "byte-exact" means the
compiled instructions match the retail game exactly.

Snapshot verified on 2026-07-18:

| Section | Converted functions | Converted bytes |
| --- | ---: | ---: |
| Total | 5,973 / 6,033 (99.01%) | 98.34% |
| Init | 508 / 538 (94.42%) | 90.79% |
| Game | 5,284 / 5,313 (99.45%) | 98.93% |
| Debugger | 181 / 182 (99.45%) | 99.19% |

| Section | Byte-exact | Still different |
| --- | ---: | ---: |
| Total | `[#########---------------]` 2,255 / 5,973 (37.75%) | 3,718 |
| Init | `[#################-------]` 367 / 508 (72.24%) | 141 |
| Game | `[########----------------]` 1,722 / 5,284 (32.59%) | 3,562 |
| Debugger | `[######################--]` 166 / 181 (91.71%) | 15 |

There are currently no functions blocked only by address drift. Regenerate the
measurements with:

```sh
make -C conker progress NON_MATCHING=1
make -C conker match-progress NON_MATCHING=1
```

See the [project overview](DOCS/PROJECT.md#current-progress) for measurement
details and the [update log](DOCS/UPDATE_LOG.md) for milestone history.

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
