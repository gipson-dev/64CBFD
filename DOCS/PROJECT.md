# Project Overview

This repository is a work-in-progress decompilation of *Conker's Bad Fur Day* for Nintendo 64.

You must provide your own copy of the game ROM. The ROM is not included in this repository.

## Start here

For most contributors, the usual flow is:

1. Clone the repo with submodules.
2. Put your US ROM at the repository root as `baserom.us.z64`.
3. Verify and extract the ROM.
4. Build the code sub-project.
5. Rebuild the ROM and compare it against the original.

Run this any time you want a local progress summary:

```sh
make -C conker progress NON_MATCHING=1
```

## Repository layout

```text
.
|-- .devcontainer/       VS Code devcontainer setup
|-- .github/workflows/   GitHub Actions CI workflows
|-- config/              YAML configs for compressed ROM chunks and assets
|-- conker/              Code sub-project for init, game, and debugger sections
|   |-- include/         Headers, structs, variables, and function declarations
|   |-- src/             Decompiled C source
|   |-- tools/           Code sub-project helper scripts
|   |-- *.yaml           n64splat configs for code sections by ROM version
|   |-- symbol_addrs.*   Version-specific symbol address files
|   |-- undefined_*.*    Version-specific undefined function and symbol lists
|   `-- Makefile         Code sub-project build orchestration
|-- DOCS/                Repository documentation and update log
|-- ido/                 Recompiled IDO compiler used for byte-matching builds
|-- tools/               Build and decompilation tools
|   |-- n64splat/        ROM splitter and segment tooling (submodule)
|   |-- asm-differ/      Assembly comparison tool (submodule)
|   |-- asm-processor/   Supports GLOBAL_ASM blocks inside C files (submodule)
|   |-- mips_to_c/       First-pass MIPS-to-C translation helper (submodule)
|   |-- splat_ext/       Project-specific n64splat extensions
|   |-- gzip             Matching compression helper
|   `-- *.py             Project-specific scripts
|-- *.yaml               Top-level n64splat and rzip configs by ROM version
|-- *.sha1               Expected hashes for extracted code sections
|-- .gitattributes       Line-ending rules for Docker and Linux tooling
|-- Dockerfile           Build environment definition
|-- Makefile             Top-level build orchestration
|-- packages.txt         System packages for the build environment
`-- requirements.txt     Python package pins for build and tooling scripts
```

For more detail on the `conker/` directory, see [Code sub-project](CODE_SUBPROJECT.md).
For repository-facing documentation and workflow changes, see the [Update log](UPDATE_LOG.md).

## Build requirements

The easiest build path is Docker because it packages the expected Linux toolchain. Native Linux and WSL are also usable. Native Windows without WSL or Docker is not supported because the IDO compiler used for byte matching only targets Linux and macOS.

If you want to set up the environment yourself, use the [Dockerfile](../Dockerfile) as the package reference.

## Build with Docker

From the repository root:

```sh
git clone --recursive <repository-url>
cd conker

docker build . -t conker
docker run --rm -ti -v $(pwd):/conker conker bash
```

After the container shell opens, continue with the normal build steps below.

## Normal build steps

First, verify the ROM and extract the top-level split files:

```sh
make check
make extract
```

Then build and replace the code sections:

```sh
make -C conker extract
make -C conker --jobs
make -C conker replace
```

Finally, rebuild the ROM:

```sh
make --jobs
```

If the build still matches the original ROM byte-for-byte, you will see:

```text
build/conker.us.z64: OK
```

A mismatch is normal during active decompilation work. It means some code is not matched yet. Use `tools/asm-differ` to inspect exactly where your build differs from the original ROM.

## Development environment notes

These notes are most relevant when the checkout lives on a Windows filesystem and is used through WSL2 or a devcontainer.

- Line endings: this repo expects LF line endings. If a fresh clone shows many modified files, set `core.autocrlf=input` locally.
- Symlinks: if `core.symlinks` is `false`, symlinked tooling files may check out as plain text and break extension loading. Set `core.symlinks=true`.
- Submodule ownership: devcontainers can report "dubious ownership" when container users do not match mounted file owners. The devcontainer config adds `safe.directory '*'` automatically.
- Python pins: the top-level `requirements.txt` pins known-sensitive dependencies such as `spimdisasm==1.33.0` and `pycparser<3`.

## GitHub Actions

The full ROM build needs private baserom material and will only run when these repository secrets are configured:

- `PRIVATE_REPO_ACCESS`: token that can read the private baserom repository.
- `CONKER_BASEROM_US`: passphrase used to decrypt `baserom.us.z64.aes`.

If either secret is missing, CI checks out the repository and reports a notice, then skips the baserom-dependent build steps. This keeps forks and fresh repo setups green without exposing or requiring ROM files.

## Current progress

This project is still early. Current work includes:

- Converting disassembly into byte-matching C code.
- Extracting assets from the ROM and packing them back into a rebuilt ROM.
- Identifying and documenting asset formats.
- Improving tooling around extraction, comparison, and build workflows.

Run `make -C conker progress` for current local numbers.

### Code decompilation snapshot

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.77% | 1553 / 7644 (20.32%) |
| init | `[#####-------------------]` 20.16% | 232 / 547 (42.41%) |
| game | `[#-----------------------]` 5.11% | 1151 / 6915 (16.64%) |
| debugger | `[#################-------]` 70.26% | 170 / 182 (93.41%) |

These numbers come from the first `.map`-based build this repository has actually produced end
to end (`make -C conker progress NON_MATCHING=1`, since the ROM does not yet byte-match - see
[UPDATE_LOG.md](UPDATE_LOG.md) for 2026-07-14). Earlier snapshots quoted here were carried over
from documentation and were never actually re-verified against a working build in this checkout;
treat this one as the first trustworthy baseline and regenerate from `make -C conker progress`
going forward.

Progress is measured by matched bytes and matched functions. Detailed CSV files can be regenerated with:

```sh
make progress.csv
```

## ROM code sections

The ROM has three main code sections:

- `init`: initialization code plus libultra, loaded at `0x10000000`.
- `game`: core game code, loaded at `0x15000000`.
- `debugger`: debugger code, loaded at `0x16000000`.

In the `us`, `eu`, and `debug` ROMs, the `game` code is compressed. In the earlier `ects` ROM, it is not.

These sections are extracted and combined into the `conker/` code sub-project so they can be compiled consistently across versions.

## ROM layout notes

The ROM layout is still being mapped. Several sections are compressed with a stripped-down gzip format: the usual gzip header and trailer are removed, then replaced with a 4-byte uncompressed-size header. In this repo, those sections are called `rzip`.

US ROM overview:

```text
[header]  0000 0000 > 0000 0040 ; suggests libultra 2.0G
[ boot ]  0000 0040 > 0000 1000
[ code ]  0000 1000 > 0004 2C50 ; init + libultra .text
[ ???? ]  0002 90D0 > ???? ????
[ data ]  0002 C750 > 0002 C7A0 ; init + libultra .data
[ ???? ]  0002 C7A0 > 0004 2C50 ; ucode
[ rzip ]  0004 2C50 > 0018 6B50 ; game .text, compressed
[ rzip ]  0018 8328 > 0019 C7D8 ; game .data, compressed
[ code ]  0019 EA88 > 001A 2190 ; debugger .text
[ data ]  001A 2190 > 001A 37E0 ; debugger .data
[ rzip ]  001A 37E0 > 00AB 1950 ; compressed section, possibly textures
[ offs ]  00AB 1950 > 00AB 1A40 ; asset offset table
[ rzip ]  00AB 1A40 > 03F8 B800 ; assets 00 through 1C
[ ffff ]  03F8 B800 > 0400 0000 ; 0xff padding
```

The decompression and compression method for these sections is understood and currently produces matching output.

## Tools

Project-specific tools:

- `rarezip` and `rareunzip`: compress and decompress the ROM compression format.

External tools:

- [asm-differ](https://github.com/simonlindholm/asm-differ): compares compiled assembly against the original ROM.
- [asm-processor](https://github.com/simonlindholm/asm-processor): allows `GLOBAL_ASM` blocks inside C files.
- [n64splat](https://github.com/ethteck/n64splat): splits the ROM into segments.
- [ido-static-recomp](https://github.com/Emill/ido-static-recomp): provides the IDO compiler.
- [gzip](https://github.com/mkst/gzip): provides the specific pre-1.5 `memzero` behavior needed for matching compression.
