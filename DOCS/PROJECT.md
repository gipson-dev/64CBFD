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

The other target versions use the same pattern (`baserom.eu.z64`,
`baserom.debug.z64`, `baserom.ects.z64` with `make check VERSION=<ver>`);
expected hashes are the root-level `conker.<ver>.sha1` files. ROMs must be
big-endian (`.z64` byte order, first bytes `80 37 12 40`) - byte-swapped
`.n64`/`.v64` dumps need converting first. The `eu` extraction pipeline is
modernized and verified; `debug`/`ects` configs still need the same splat
format update (see [Working notes](WORKING_NOTES.md)).

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
|   |-- CBFD_rabbitizer/ MIPS instruction decoder, project fork of rabbitizer (submodule)
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
- Symlinks: if `core.symlinks` is `false`, symlinked tooling files may check out as plain text and break extension loading. Set `core.symlinks=true`. Telltale symptom: splat fails with `could not load segment type 'rzip'` because `tools/splat_ext/rareunzip.py` (a symlink) checked out as a 15-byte text file. Full recovery steps are in [Working notes](WORKING_NOTES.md) - this corruption has recurred on OneDrive-synced checkouts, so re-check both settings if extraction suddenly breaks.
- WSL specifics: any WSL2 distro works against a checkout on the Windows filesystem (`/mnt/c/...`). Install the packages from `packages.txt`, put the Python deps (both `requirements.txt` and `tools/n64splat/requirements.txt`) in a venv inside WSL, and prefix builds with that venv on `PATH`. A worked setup for this machine is logged in [Working notes](WORKING_NOTES.md).
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

Last regenerated: 2026-07-15, from a fully working `.map`-based build
(`make -C conker progress NON_MATCHING=1`).

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[##----------------------]` 6.77% | 1557 / 7644 (20.37%) |
| init | `[#####-------------------]` 20.16% | 232 / 547 (42.41%) |
| game | `[#-----------------------]` 5.11% | 1153 / 6915 (16.67%) |
| debugger | `[#################-------]` 70.26% | 172 / 182 (94.51%) |

Two caveats about what this table measures:

- A function counts as "done" here when it has been converted from raw
  assembly to C (no `GLOBAL_ASM` pragma), **not** when it byte-matches the
  retail ROM. Byte-matching is tracked separately below.
- Earlier snapshots quoted in past revisions of this file were carried over
  from documentation and never re-verified against a working build in this
  checkout; the 2026-07-14 baseline above is the first trustworthy one.
  Regenerate with `make -C conker progress NON_MATCHING=1` going forward.
- **The raw (`GLOBAL_ASM`) side of the "Functions" column includes
  non-function artifacts** - `.s` files under `asm/` can define three kinds
  of label: `glabel` (a real function - the only kind that should ever get
  a `GLOBAL_ASM` C stub), `jlabel` (an internal jump-table target *inside*
  a function's own instruction stream - not independently convertible,
  it's absorbed into whichever function contains it), and `dlabel` (a data
  symbol that happens to be named like a function, e.g. a jump table
  stored as rodata gets auto-named `func_XXXXXXXX` by splat even though
  it's declared `dlabel`). `progress.csv` doesn't distinguish these, so
  raw-count totals overstate real remaining function work. Checked
  2026-07-15 (cross-referencing every raw `progress.csv` row's name
  against `grep -rhoP '\bjlabel\s+\K\S+' asm/` /
  `grep -rhoP '\bdlabel\s+\K\S+' asm/`): of the raw entries above, **game's
  5764 includes 1603 artifacts (1601 `jlabel` + 2 `dlabel`, real count
  4161)**; **init's 315 includes 9 `jlabel` artifacts (real count 306)**;
  debugger's 12 had none (all real). This check only works for *still-raw*
  entries (a converted function's `.s` file/`glabel` line is gone once it
  has real C, so the same grep can't retroactively validate the
  already-converted numerator) - don't try to "correct" the C-converted
  counts the same way; `D_`-prefixed `language: c` rows there are
  legitimately-tracked data-symbol declarations, not function-conversion
  noise. Re-run the grep pair above (fast, whole-tree) before trusting a
  raw-count total for planning a conversion pass.

### Byte-matching snapshot

Of the C-converted functions above, how many compile to the exact retail
bytes (last regenerated 2026-07-15, via
`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on callees | Still differ |
| --- | --- | --- | --- |
| total | 548 / 1557 (35.20%) | 145 | 862 |
| init | 223 / 232 (96.12%) | 4 | 5 |
| game | 197 / 1153 (17.09%) | 140 | 816 |
| debugger | 128 / 172 (74.42%) | 0 | 44 |

"Blocked on callees" means the only remaining differences are `j`/`jal`
target addresses - those functions need no further edits and will
self-resolve as the functions they reference get matched. Add `LIST=1` to
print every non-exact function, smallest diff first. Note the "still
differ" column is a worst-case count: a function whose only problem is a
reference to a symbol at a drifted address will show as differing even
though its source is correct.

**2026-07-15 correction:** `tools/match_progress.py`'s `classify()` was
over-strict about function length - it declared "diff" for any length
mismatch before comparing content, but a retail symbol's declared length
(`next_symbol_addr - this_addr`) can include a few trailing
inter-function alignment nops that splat's boundary detection folded into
the *preceding* function rather than genuinely being part of it. Fixed by
trimming trailing all-zero words from `truth` before comparing when
`ours` is shorter. This alone moved 56 functions project-wide from "diff"
to "exact" with no source changes (init 201→223, game 167→197, debugger
11→15) - if you're chasing a "diff" function with a small `nwords`
mismatch and an all-zero tail in the ground truth, check this class of
false positive before touching the source.

**2026-07-15, same day: debugger jumped 15→128 byte-exact from converting
just 2 raw functions.** Converting `func_1600160C`/`func_16001678` (the
two smallest remaining `GLOBAL_ASM` functions in `debugger/debugger.c`)
from raw assembly to C incidentally fixed a pre-existing symbol-placement
bug: several `D_1600xxxx` globals in that file (`D_16003888`,
`D_16003898`, `D_160038A8`, ...) were linking ~16 bytes off from the
addresses their own names encode (confirmed via `nm build/conker.us.elf`
before/after). Every other already-converted function in the file that
referenced those globals (e.g. `func_16000424`, `func_16000058`,
`func_16000000`) was silently failing to byte-match because of it, even
though their own C was already correct. Root mechanism not fully pinned
down - likely the same class of splat boundary-detection issue as the
init-segment literal-pool drift below, but for raw-`.s`-adjacent data
symbols instead of compiler-emitted float literals. Lesson: when a file
has unexplained address-drift-looking diffs across *multiple* unrelated
functions, converting a neighboring still-`GLOBAL_ASM` function can be a
higher-leverage fix than chasing each symptom individually.

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
