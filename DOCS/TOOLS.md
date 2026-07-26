# Project Tools

This page documents repository-local tooling, especially scripts that are not
upstream submodules. Run commands from the repository root unless a section
says otherwise.

## Toolchain smoke test

Validate the project-native raw-object, minimal-ELF, and standard vertex
conversion helpers without a ROM:

```sh
make tools-check
```

The check creates an isolated seven-byte fixture, wraps it in a 16-byte-aligned
big-endian MIPS object, links it at `0x80000000`, validates both ELF files, and
checks known and malformed standard `Vtx` records. It writes only to the
system temporary directory.

The scripts use `mips-linux-gnu-` by default. Set `CROSS` to another MIPS
binutils prefix, including or omitting its trailing hyphen. `MIPS_AS` and
`MIPS_LD` can override the individual commands.

## Raw binary object wrapper

`tools/mkrawobject` converts an arbitrary file into a big-endian, 32-bit MIPS
relocatable object with a `.data` section:

```sh
tools/mkrawobject INPUT OUTPUT [ALIGNMENT]
```

The default alignment is `0x10`. The input is zero-padded to that boundary.
This is useful when a linker must consume an opaque extracted binary while
preserving an explicit N64 alignment.

Example:

```sh
tools/mkrawobject assets/debugger.us.bin build/debugger.us.o 0x10
```

The normal ROM build already wraps its checked-in binary assets directly with
GNU `ld -r -b binary`; do not replace those established Makefile rules merely
to use this helper. Use `mkrawobject` when section alignment or an independent
diagnostic object is specifically needed.

## Minimal ELF linker

`tools/mksimpleelf` links one MIPS object into a small executable ELF:

```sh
tools/mksimpleelf INPUT_OBJECT OUTPUT_ELF [BASE_ADDRESS]
```

The default base is zero. The linker script is generated in an isolated
temporary directory and retains `.text`, `.rodata`, `.data`, and `.bss`.
This is intended for inspection, conversion, and small tooling fixtures, not
as a replacement for `conker.ld` or the ROM linker scripts.

Example:

```sh
tools/mksimpleelf build/debugger.us.o build/debugger.us.elf 0x16000000
```

## Standard N64 vertex converter

`tools/vertconvert.py` converts packed standard 16-byte SDK `Vtx` records into
C initializers:

```sh
tools/vertconvert.py HEX_DATA
tools/vertconvert.py --file vertices.hex --array-name display_vertices
```

Input can contain whitespace, commas, underscores, and repeated `0x`
prefixes. A file may contain `dlabel` lines, which are ignored. With no
positional input or file, the tool reads standard input. It validates that the
input contains complete 16-byte records instead of silently discarding
malformed data.

The record layout is three signed 16-bit coordinates, a 16-bit flag, two
signed 16-bit texture coordinates, and four color/normal bytes. This helper is
useful for SDK-style display-list data and assembly-to-C work.

It is deliberately not an `assets13` decoder. Conker's verified model records
there contain only three signed 16-bit coordinates per six-byte vertex, with
no inline flag, texture coordinates, color, or normal. Use the decoder in
[Asset formats](ASSET_FORMATS.md#4a-model-geometry-assets13-vertex-arrays-confirmed)
for those records.

## Conker asset tools

Use the following tools for the current Conker formats:

- `tools/asset_dump.py` lists and extracts the master asset-table sections.
- `tools/rareunzip.py` and `tools/rarezip.py` decode and encode Conker's
  four-byte-size-header Rarezip blocks.
- `tools/extract_compressed.py` and `tools/compress_dir.py` implement the
  config-driven compressed-section workflow.
- n64splat's image handling and its `n64img` dependency should be tried first
  for standard N64 texture formats.

See [Asset formats](ASSET_FORMATS.md) and
[Compressed config sections](CONFIG.md) for the verified format details.

## Reference-only imported asset generators

The newly added `tools/assetmgr/` scripts and the top-level
`tools/mktextures` are not Conker asset builders. Their schemas and output
formats describe a different Rare N64 asset pipeline:

- they require a `ROMID`-keyed `src/assets/...` tree that this repository does
  not have;
- their compressor writes a `0x1173` marker and a three-byte size, while
  Conker Rarezip uses a four-byte big-endian size followed by raw DEFLATE;
- their language banks, pad/waypoint records, room tiles, animation tables,
  sequence tables, and texture manifests have no verified mapping to Conker's
  containers.

These entry points therefore stop with an incompatibility message by default.
For controlled cross-game format research only, set:

```sh
ALLOW_PD_ASSET_FORMATS=1
```

That opt-in does not make the formats Conker-compatible, and none of these
generators are part of the build graph. Do not publish generated Conker assets
from them without first documenting and verifying a real format mapping.

## Upstream submodules

`asm-differ`, `asm-processor`, `mips_to_c`, `n64splat`, `texture2c`, and
`ultralib` retain their upstream documentation. Project-specific usage and
format conclusions belong under `DOCS/`.
