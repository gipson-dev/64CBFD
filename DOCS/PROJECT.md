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
|   |-- texture2c/       N64 texture format to C converter (submodule)
|   |-- ultralib/        Stock libultra reverse-engineering reference (submodule)
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

Last regenerated: 2026-07-18, from a fully working `.map`-based build
(`make -C conker progress NON_MATCHING=1`).

| Section | Progress bytes | Functions |
| --- | --- | --- |
| total | `[########################]` 98.34% | 5973 / 6033 (99.01%) |
| init | `[######################--]` 90.79% | 508 / 538 (94.42%) |
| game | `[########################]` 98.93% | 5284 / 5313 (99.45%) |
| debugger | `[########################]` 99.19% | 181 / 182 (99.45%) |

Recent passes moved init/libultra helpers and debugger functions out of raw
assembly, carried game raw conversion to `5284 / 5313 (99.45%)`, and pushed
total raw conversion to `5973 / 6033 (99.01%)`. Only 60 tracked raw functions
remain: 26 handwritten `init_5AB0` TLB functions, 23 functions in slices with
embedded data or four-byte slots, six mixed code/data functions, two static
audio routines, the init `sinf`/`sqrtf` pair, and the debugger CP0 reader.
Debugger raw conversion is complete
except `func_16003650`, a hardware CP0/TLB reader that executes `tlbr` and
CP0 register moves and is intentionally left as raw assembly. The newly
converted functions are C-shaped recovery bodies, not yet byte-matched
retail code; see the byte-matching snapshot below before using them as
examples of final matched source.

Two caveats about what this table measures:

- A function counts as "done" here when it has been converted from raw
  assembly to C (no `GLOBAL_ASM` pragma), **not** when it byte-matches the
  retail ROM. Byte-matching is tracked separately below.
- Earlier snapshots quoted in past revisions of this file were carried over
  from documentation and never re-verified against a working build in this
  checkout; the 2026-07-14 baseline above is the first trustworthy one.
  Regenerate with `make -C conker progress NON_MATCHING=1` going forward.
- **Fixed at the source, 2026-07-15: `tools/progress.py` was counting
  jump-table-target local labels as their own "functions."** The table
  above already reflects the fix - noted here so the history isn't lost.
  `.s` files under `asm/` define two relevant kinds of label: `glabel` (a
  real function) and `jlabel` (an internal jump-table target *inside* a
  function's own instruction stream, e.g. `.L15029BA0` - not independently
  convertible, it's absorbed into whichever function contains it).
  `tools/progress.py`'s map-file parser had a check meant to skip these
  (`if new_function.startswith("L8"):`) that never matched anything: it
  assumed unmodified real-address-style local labels (`.L80012345`)
  without accounting for the leading `.`, and this project remaps code
  addresses to `0x10`/`0x15`/`0x16xxxxxx` besides. Every jump-table target
  in `init`/`game`/`debugger` was silently counted as its own raw
  "function," inflating every raw-count denominator (and total function
  counts) in this table. Fixed the check to `.startswith(".L")`
  (general, not tied to a specific address range) and regenerated -
  **`game` dropped from 6915 to 5313 total functions (1153→1152
  converted, same functions, smaller/more honest denominator), `init`
  from 547 to 538 (232 converted, unchanged), `debugger` unaffected (was
  already clean, no jlabel noise there)**. A same-day earlier pass had
  found this same inflation by cross-referencing `progress.csv` against
  `grep -rhoP '\bjlabel\s+\K\S+' asm/` as a manual workaround - that's no
  longer needed for the raw-count side, the numbers are now correct at
  the source. Two `dlabel` artifacts in `game` (data mis-auto-named like
  functions, e.g. `func_150AA814` - a jump table stored as rodata) are
  **not** caught by this fix (`.L`-prefix filtering only catches
  `jlabel`, not `dlabel`-tagged `func_`/`D_`-named entries) - a residual,
  much smaller inaccuracy (2 of several thousand) left undocumented-away
  rather than hardcoded around.
- **Don't try to "correct" the C-converted (`language: c`) side the same
  way** - `D_`-prefixed `c` rows there are legitimately-tracked
  data-symbol declarations (e.g. `extern u8 D_16003888;`), not
  function-conversion noise; only the raw/`asm` side had the label-miscount
  bug.

### Byte-matching snapshot

Of the C-converted functions above, how many compile to the exact retail
bytes (last regenerated 2026-07-18, via
`make -C conker match-progress NON_MATCHING=1`):

| Section | Byte-exact | Blocked on address drift | Still differ |
| --- | --- | --- | --- |
| total | 1679 / 5973 (28.11%) | 27 | 4267 |
| init | 233 / 508 (45.87%) | 7 | 268 |
| game | 1280 / 5284 (24.22%) | 20 | 3984 |
| debugger | 166 / 181 (91.71%) | 0 | 15 |

The first matching pass over the generated game slices made 40 small
functions byte-exact. The retail-layout pass then moved total byte-exact
progress above 50% by re-spacing compiled functions and relocations at their
retail-relative addresses. Oversized non-matching functions execute through
out-of-line bodies and short trampolines instead of shifting later code. The debugger overlay's
rodata displacement healed on 2026-07-16: the
`debugger_257350.c` printf engine was identified as Plauger's Standard C
Library (the N64 SDK's libc - `_Printf`/`_Ldtob`/`_Genld`/`_Litob`) and
rematched at exact retail sizes. Later game-section layout fixes collapsed
the dominant address-drift plateaus. The latest raw-conversion passes then
crossed the 25% game C milestone, moved ten debugger functions, and moved
65 init/libultra functions out of `GLOBAL_ASM`/raw asm. Function/object
re-spacing and symbol-derived linker anchors now preserve the retail layout.
The 99% conversion pass left 27 functions address-drift blocked and 1581
byte-exact; typed legacy signatures changed three previously exact init
callers, and the regression is recorded rather than hidden. The next matching
pass reconstructed 35 small typed callbacks, constant-return handlers,
accessors, and state setters, bringing the current result to 1616 byte-exact
functions. The following compact-function pass matched 63 more callbacks,
scalar helpers, field initializers, accessors, and thin wrappers, bringing the
current result to 1679 byte-exact functions while leaving all blocker and
raw-conversion counts unchanged.
The ROM mapping helper now reads code-section starts from `conker.<version>.yaml`,
finds `symbol_addrs.<version>.txt` even when using a temporary progress CSV,
and resolves `D_XXXXXXXX` data labels from their name-implied retail VRAM.

"Blocked on address drift" means the only remaining differences are
`j`/`jal` target addresses or `%lo` halves of shifted symbol addresses -
those functions need no further edits and will self-resolve as the
functions/data they reference get matched. Add `LIST=1` to print every
non-exact function, smallest diff first. Note the "still differ" column
is a worst-case count: a function whose only problem is a reference to a
symbol at a drifted address the classifier can't pair with a recent
`lui` will show as differing even though its source is correct - and
per-function diff counts for a few rows are known to over-report; trust
raw byte compares at name-implied offsets when working a specific
function.

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
- [n64img](https://github.com/decompals/n64img): N64 image-format helper used through n64splat's image segment support. Prefer it for texture/image decode probes before writing project-specific image parsing.
- [ultralib](https://github.com/decompals/ultralib): reference source for stock libultra/libgultra 2.0L matching work.
- [ido-static-recomp](https://github.com/Emill/ido-static-recomp): provides the IDO compiler.
- [gzip](https://github.com/mkst/gzip): provides the specific pre-1.5 `memzero` behavior needed for matching compression.

Reference-only upstreams:

- [N64-IPL](https://github.com/decompals/N64-IPL): matching IPL disassemblies. Useful for boot/IPL/header/checksum context, but not vendored into this project's game-code decomp workflow.
- [mips-gcc-2.7.2](https://github.com/decompals/mips-gcc-2.7.2): KMC/GCC-oriented compiler reference. Keep out of the active toolchain unless evidence turns up for a GCC/KMC-compiled code island; this project currently matches against IDO 5.3.
