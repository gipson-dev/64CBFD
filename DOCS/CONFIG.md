# Compressed Config Sections

The `config/` directory contains YAML files that describe compressed ROM chunks that do not appear to have their own offset table.

Use these files with the project compression scripts when you need to extract, inspect, or rebuild those chunks.

## When to use this

Use this workflow when you are working with compressed ROM sections outside the main code build and asset-table flow.

For the normal code build, start with [Project overview](PROJECT.md) instead.

## Decompress a section

Run this from the repository root:

```sh
mkdir -p tmp
python3 tools/extract_compressed.py config/compressed.us.yaml bin/compressed.bin tmp/
```

Arguments, in order:

1. The config file, such as `config/compressed.us.yaml`.
2. The compressed input file, such as `bin/compressed.bin`.
3. The output directory for decompressed files.

If you are working with the EU ROM, use the matching `eu` config instead of the `us` config.

## Recompress a section

The same compression script used for `game` assets can rebuild these files. These chunks do not use 2-byte alignment, so pass `--no-padding`.

```sh
mkdir -p tmp2
python3 tools/compress_dir.py tmp tmp2 --no-padding
cat tmp2/*.gz > compressed.bin
```

The ROM adds `0x0` padding at the end of the compressed section so the final section size aligns to a 16-byte boundary.
