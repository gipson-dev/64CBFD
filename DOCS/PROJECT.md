# Project Overview

This repository is a work-in-progress decompilation of *Conker's Bad Fur Day*
for Nintendo 64. It reconstructs code and data from a legally obtained retail
ROM; no ROM or copyrighted game assets are included.

## Start here

The normal contributor path is:

1. Clone the repository with submodules.
2. Add a big-endian US ROM as `baserom.us.z64`.
3. Verify and extract the ROM.
4. Build the three code sections under `conker/`.
5. Replace those sections and rebuild the ROM.
6. Measure conversion and byte-exact progress.

After the first successful build, use the
[contributor and byte-matching guide](CONTRIBUTING.md) for function work.

## Supported ROM versions

The default version is `us`. Other configured versions follow the same naming
pattern:

| Version | ROM filename | Check command |
| --- | --- | --- |
| US | `baserom.us.z64` | `make check` |
| EU | `baserom.eu.z64` | `make check VERSION=eu` |
| Debug | `baserom.debug.z64` | `make check VERSION=debug` |
| ECTS | `baserom.ects.z64` | `make check VERSION=ects` |

ROMs must be big-endian `.z64` files beginning with `80 37 12 40`.
Byte-swapped `.n64` or `.v64` dumps must be converted before use. Expected
hashes are stored in the root-level `conker.<version>.sha1` files.

The EU extraction pipeline is current and verified. Debug and ECTS configs may
still need the same modern n64splat-format cleanup before every extraction path
works end to end.

## Repository layout

```text
.
|-- .devcontainer/       VS Code devcontainer setup
|-- .github/workflows/   GitHub Actions workflows
|-- config/              YAML descriptions for compressed ROM chunks
|-- conker/              Init, game, and debugger code project
|   |-- include/         Project headers and declarations
|   |-- src/             Decompiled C source
|   |-- tools/           Code-project helpers
|   |-- *.yaml           Version-specific code split configs
|   |-- symbol_addrs.*   Version-specific symbol addresses
|   `-- Makefile         Code build and progress targets
|-- DOCS/                Project documentation
|-- ido/                 Recompiled IDO compiler used for matching
|-- tools/               Split, diff, compression, and conversion tools
|-- *.yaml               Top-level split and compression configs
|-- *.sha1               Expected ROM and section hashes
|-- Dockerfile           Reproducible build environment
|-- Makefile             Top-level extraction and ROM build
|-- packages.txt         System package list
`-- requirements.txt     Python dependency pins
```

See [Code sub-project](CODE_SUBPROJECT.md) for the internal `conker/` build and
[Documentation](README.md) for the complete subject index.

## Build environments

Docker is the easiest supported setup because it packages the expected Linux
toolchain. Native Linux and WSL are also supported. Native Windows without WSL
or Docker is not supported because the IDO compiler used for byte matching is
not a native Windows tool.

### Docker

From the repository root:

```sh
docker build . -t conker
docker run --rm -ti -v $(pwd):/conker conker bash
```

Run the normal build steps below after the container opens.

### Native Linux or WSL

Use the [Dockerfile](../Dockerfile) and [packages.txt](../packages.txt) as the
package reference, then install the Python packages from both
`requirements.txt` and `tools/n64splat/requirements.txt`.

On a Windows-hosted checkout, WSL can build directly under `/mnt/c/...`, though
a Linux-native filesystem is usually faster.

## Normal build steps

Run these commands from the repository root.

Verify and extract the top-level ROM:

```sh
make check
make extract
```

Build and replace the code sections:

```sh
make -C conker extract
make -C conker --jobs
make -C conker replace NON_MATCHING=1
```

Rebuild the complete ROM:

```sh
make --jobs
```

A completely matching build reports:

```text
build/conker.us.z64: OK
```

During active decompilation, `build/conker.us.z64: FAILED` is expected when the
rebuilt ROM differs from retail. Use the progress and matching tools below to
distinguish ordinary non-matching code from a broken environment.

## Development environment notes

### Line endings

The project expects LF line endings. If a fresh Windows clone shows widespread
changes, set the repository-local Git option:

```sh
git config core.autocrlf input
```

### Symlinks

Several tool files are symlinks. If `core.symlinks` is disabled, Git may check
them out as small text files and n64splat can fail to load project extensions.

```sh
git config core.symlinks true
```

A common symptom is `could not load segment type 'rzip'` while
`tools/splat_ext/rareunzip.py` is a short plain-text file instead of a symlink.
Re-enable symlinks and refresh the affected tracked files.

### Submodules and mounted workspaces

Clone with `--recursive`, or initialize missing submodules with:

```sh
git submodule update --init --recursive
```

Devcontainers may see mounted files as owned by another user. The supplied
configuration adds the workspace as a safe Git directory.

### Python versions

Use the checked-in dependency pins. Known-sensitive packages include
`spimdisasm==1.33.0` and `pycparser<3`.

## GitHub Actions

The full ROM build requires private baserom material and uses two repository
secrets:

- `PRIVATE_REPO_ACCESS` — token that can read the private baserom repository.
- `CONKER_BASEROM_US` — passphrase for the encrypted US baserom.

If either secret is absent, CI reports a notice and skips baserom-dependent
steps. This keeps forks and clean setups usable without exposing ROM data.

## Current progress

Progress is reported in two different ways:

- **Converted:** the function has C source instead of raw assembly.
- **Byte-exact:** the compiled function instructions match the retail ROM.

Snapshot verified on 2026-07-19 with:

```sh
make -C conker progress NON_MATCHING=1
make -C conker match-progress NON_MATCHING=1
```

### C conversion

| Section | Progress bytes | Functions |
| --- | ---: | ---: |
| Total | `[########################]` 98.34% | 5,973 / 6,033 (99.01%) |
| Init | `[######################--]` 90.79% | 508 / 538 (94.42%) |
| Game | `[########################]` 98.93% | 5,284 / 5,313 (99.45%) |
| Debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Sixty tracked raw functions remain. Most are handwritten TLB code, embedded or
mixed code/data slices, tiny four-byte slots, static audio routines, or
hardware CP0 operations that are not ordinary C conversion targets.

### Byte-exact matching

| Section | Byte-exact | Blocked by address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | `[##########--------------]` 2,393 / 5,973 (40.06%) | 1 | 3,579 |
| Init | `[#################-------]` 367 / 508 (72.24%) | 0 | 141 |
| Game | `[########----------------]` 1,860 / 5,284 (35.20%) | 1 | 3,423 |
| Debugger | `[######################--]` 166 / 181 (91.71%) | 0 | 15 |

`match-progress` compares linked functions by symbol against pristine retail
bytes at name-implied addresses. Add `LIST=1` to list every non-exact function
from the smallest real diff upward.

Historical milestones and matcher corrections are recorded in the
[update log](UPDATE_LOG.md). Matching technique and validation requirements
belong in the [contributor guide](CONTRIBUTING.md), not in this progress page.

## ROM code sections

The code project contains three main sections:

- `init` — startup code and libultra, loaded near `0x10000000`.
- `game` — core game code, loaded at `0x15000000`.
- `debugger` — debugger overlay, loaded at `0x16000000`.

The `game` section is compressed in US, EU, and debug builds. It is uncompressed
in the earlier ECTS build.

## ROM layout

Several regions use Rare's stripped gzip-derived format, called `rzip` in this
project. It replaces the normal gzip header and trailer with a four-byte
uncompressed-size header.

High-level US layout:

```text
[header]  0000 0000 -> 0000 0040
[boot]    0000 0040 -> 0000 1000
[code]    0000 1000 -> 0004 2C50   init + libultra
[rzip]    0004 2C50 -> 0018 6B50   game text
[rzip]    0018 8328 -> 0019 C7D8   game data
[code]    0019 EA88 -> 001A 2190   debugger text
[data]    001A 2190 -> 001A 37E0   debugger data
[rzip]    001A 37E0 -> 00AB 1950   compressed data
[offsets] 00AB 1950 -> 00AB 1A40   asset offset table
[rzip]    00AB 1A40 -> 03F8 B800   asset groups 00-1C
[padding] 03F8 B800 -> 0400 0000
```

See [Asset formats](ASSET_FORMATS.md) for confirmed payload behavior and
[Compressed config sections](CONFIG.md) for config-driven extraction.

## Tools and references

Project tools include `rarezip`, `rareunzip`, progress scripts, linker-layout
helpers, and generated-slice padding tools.

Important external tools and references:

- [asm-differ](https://github.com/simonlindholm/asm-differ) — assembly diffs.
- [asm-processor](https://github.com/simonlindholm/asm-processor) — embedded
  `GLOBAL_ASM` support.
- [n64splat](https://github.com/ethteck/n64splat) — ROM splitting.
- [mips_to_c](https://github.com/matt-kempster/mips_to_c) — first-pass C
  translation.
- [ultralib](https://github.com/decompals/ultralib) — stock libultra reference.
- [ido-static-recomp](https://github.com/Emill/ido-static-recomp) — IDO compiler
  reconstruction.
- [gzip](https://github.com/mkst/gzip) — matching legacy compression behavior.
- [N64ModernRuntime](https://github.com/N64Recomp/N64ModernRuntime#ultramodern) —
  PC-runtime architecture reference; tracked as a reference, not an active
  dependency.

The `tools/` submodules keep their upstream READMEs. Project-specific guidance
stays under `DOCS/`.
