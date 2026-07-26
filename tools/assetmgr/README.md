# Reference Asset Generators

These scripts were imported from a different Rare N64 asset workflow and are
kept only as structural reference material. They are not part of the Conker
build.

The entry points are disabled by default because their outputs are not
compatible with the formats verified in `DOCS/ASSET_FORMATS.md`. In
particular, `assetmgr.zip` emits a `0x1173` marker plus a three-byte
uncompressed length; that is not Conker's four-byte-size-header Rarezip
format.

The scripts also expect an unavailable `ROMID`-keyed `src/assets` tree:

- `mkanims` — animation table and payload packer.
- `mklang` — fixed language-bank layout and custom Japanese encoding.
- `mkpads` — pad, waypoint, waygroup, and cover records.
- `mksequences` — sequence table using the incompatible compressor.
- `mktextures` — external texture data/list table.
- `mktiles` — room collision/tile records.

For controlled cross-game research, opt in explicitly:

```sh
ALLOW_PD_ASSET_FORMATS=1 ROMID=<reference-id> tools/assetmgr/<generator> ...
```

The opt-in only removes the safety guard. It does not supply the missing
inputs or make the result usable by Conker.

For active project tools and verified alternatives, read
`DOCS/TOOLS.md`.
