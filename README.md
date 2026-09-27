# Conker's Bad Fur Day (N64) Decompilation

A work-in-progress decompilation of *Conker's Bad Fur Day* for Nintendo 64.
The project reconstructs the original game code and data in a form that can be
built, studied, and matched against the retail ROM.

> [!IMPORTANT]
> This repository does not contain game assets or ROM files. You must provide
> your own legally obtained copy of the game.

Current measurements, verified build state, and the active resume boundary are
maintained in [Current Decomp Status](DOCS/CURRENT_STATUS.md). PC-port progress
and cross-project boundaries are maintained separately in the
[PC Port Roadmap](DOCS/PC_PORT_ROADMAP.md).

## Status

Snapshot verified on 2026-09-27. "Converted" means a function has C source;
"byte-exact" means its linked instructions match the retail game. See
[Current Decomp Status](DOCS/CURRENT_STATUS.md) for the detailed handoff.

| Section | Converted functions | Converted bytes |
| --- | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 85.59% |
| Init | 497 / 538 (92.38%) | 90.58% |
| Game | 4,791 / 5,321 (90.04%) | 85.07% |
| Debugger | 181 / 182 (99.45%) | 99.19% |

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | `[############------------]` 2,836 / 5,469 (51.86%) | 1 | 2,632 |
| Init | `[###################-----]` 391 / 497 (78.67%) | 1 | 105 |
| Game | `[###########-------------]` 2,264 / 4,791 (47.26%) | 0 | 2,527 |
| Debugger | `[########################]` 181 / 181 (100.00%) | 0 | 0 |

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

- **Current status:** [Decomp status](DOCS/CURRENT_STATUS.md) and
  [PC port roadmap](DOCS/PC_PORT_ROADMAP.md)
- **Start and build:** [Project overview](DOCS/PROJECT.md) and
  [code sub-project](DOCS/CODE_SUBPROJECT.md)
- **Contribute:** [Contributor and byte-matching guide](DOCS/CONTRIBUTING.md)
- **Formats and tooling:** [Asset formats](DOCS/ASSET_FORMATS.md),
  [compressed config sections](DOCS/CONFIG.md), and
  [IDO toolchain](DOCS/IDO_RECOMP.md)
- **History:** [Update log](DOCS/UPDATE_LOG.md) and
  [working notes](DOCS/WORKING_NOTES.md)
