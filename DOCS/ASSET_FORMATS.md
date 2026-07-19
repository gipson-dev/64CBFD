# Asset Formats

This document records what is currently known about the *Conker's Bad Fur Day*
asset formats: the compression scheme, the archive/container layout, and the
per-type payload formats (models, textures, audio, and data tables).

Findings are labelled by confidence:

- **Confirmed** - verified against the codebase (`tools/splat_ext/rzip.py` and the
  decompiled game code) or by round-tripping the data (decompress / re-parse).
- **Strong** - consistent across every sample inspected, interpretation is very
  likely correct but not yet cross-checked against game code.
- **Tentative** - a working hypothesis that still needs confirmation.

The primary reproducible source is the retail **US** ROM (`baserom.us.z64`,
SHA-1 `4cbadd3c4e0729dec46af64ad018050eada4f47a`) read at the section offsets in
`conker.us.yaml`. Earlier research also compared an extracted debug-prototype
corpus under `debug_proto/assets/rzip/`; that corpus is not tracked in this
checkout, so debug/retail equivalence is supporting evidence rather than a
blanket guarantee for every payload. Version-specific differences should be
recorded explicitly as they are found.

Terminology used below:

- **Section archive** - one top-level `assetsNN` ROM range described by the
  master table at `0xAB1950`.
- **Archive entry** - one file inside a section archive.
- **Container** - a payload that begins with the reusable 8-byte-entry offset
  table described in section 3.
- **Leaf payload** - the final texture, audio stream, vertex array, string, or
  structured record after all container and compression layers are removed.

## 1. The asset pipeline

```text
ROM
 └─ section archive (e.g. 0x1A37E0, or each assetsNN section)
     └─ offset table → independently stored or rzip-compressed files
         └─ file (.bin, already decompressed by splat)
             ├─ raw payload          (MP3, audio bank, image, table), OR
             └─ container            (offset table → nested rzip blocks)
                 └─ block (rzip-compressed)                  ← inner compression
                     └─ inner container (offset table → sub-resource arrays)
```

The project's `rzip` segment type is an archive walker as well as a decompressor:
the complete section is not necessarily one DEFLATE stream. Two independent
layers can use the same **rzip** leaf codec:

1. The ROM-level `rzip` segments, split by splat into individual files.
2. One or more *inner* rzip layers inside the containers (sections 4/4a) - up to
   four levels deep for `assets13` geometry. This nesting was previously
   undocumented.

## 2. Compression: `rzip` (Confirmed)

Rare's format is a stripped-down gzip: the gzip header/trailer are removed and
replaced with a 4-byte big-endian uncompressed length, followed by a raw
DEFLATE payload.

```text
+0x00  u32  uncompressed_size (big-endian)
+0x04  ...  raw DEFLATE stream (no zlib/gzip wrapper, window bits = -15)
```

Decode in Python:

```python
import struct, zlib
usize = struct.unpack(">I", data[:4])[0]
out   = zlib.decompress(data[4:], -15)
assert len(out) == usize
```

This matches `tools/splat_ext/rzip.py` and decodes cleanly on every block
tested. Compression level is not stored in the DEFLATE stream as a reliable
format field; byte-identical project recompression uses the bundled legacy
`gzip -9` path in `tools/rarezip.py`. See also `tools/rareunzip.py`.

### 2a. Compressed game-code archive (Confirmed layout; runtime paging tentative)

The game-code archive begins at ROM `0x42450`, where `conker.us.yaml` labels
`game.us.rzip`. Its table layout is distinct from the asset-container table in
section 3:

```text
+0x00  u32  archive/data length field
+0x04  u32[] XOR-encoded chunk offsets
              decoded_offset = encoded_offset ^ 0x8039CCCA
              offsets are relative to archive base 0x42450
        u32   zero terminator
```

`game.us.rzip.yaml` supplies the XOR key and
`N64SegRzip.get_game_offsets()` in `tools/splat_ext/rzip.py` implements this
table walk. The first compressed code payload begins at ROM `0x42C50`.

The **runtime interpretation** remains tentative: project-wiki research reports
that the game requests 4096-byte decompressed chunks through a TLB-miss or
bad-virtual-address exception path, effectively demand-paging code. The archive
and XOR table are locally reproducible; the precise exception-driven loading
mechanism still needs a documented trace through the init/TLB routines.

## 3. The container / offset-table format (Confirmed)

Model archives and many other files begin with a fixed directory of entries.
This layout is the same one `N64SegRzip.get_files_from_offsets` in
`tools/splat_ext/rzip.py` already parses:

```text
Entry (8 bytes), repeated:
  +0x00  u32  data_offset   (offset from the start of the container/file)
  +0x04  u32  packed
               bit 31      final-entry marker
               bits 30-28  payload type (1 = rzip-compressed)
               bits 27-0   payload length in bytes
```

- `type = (packed >> 28) & 0x7`; type `1` is **rzip-compressed**, while type
  `0` is stored raw. Existing tools expose the top byte as `flags`, where
  `flags & 0x10` is the same type-1 test.
- `length = packed & 0x0FFFFFFF`.
- `is_final = (packed & 0x80000000) != 0`.
- The **first word doubles as the table size**: `data_offset` of entry 0 equals
  the byte length of the whole table, so `entries = table_size / 8`.
- Unused trailing slots point at end-of-file with `length = 0`.
- The final-entry bit can be attached to a real, non-empty payload. It is not
  necessarily a separate zero-length terminator.
- Payload starts are **8-byte aligned**. Alignment padding is outside the
  declared payload length.

This is confirmed by `N64SegRzip.get_files_from_offsets`, direct inspection of
the retail tables, and retained reconstruction notes for `func_1502B9B4` in
[`conker/src/game_57FA0.c`](../conker/src/game_57FA0.c), which use the same
28-bit length and three-bit type masks:

```c
more = *entry & 0xFFFFFFF;                 // 28-bit length
if ((*entry & 0x70000000) == 0x10000000)   // type field, 0x1 => compressed
    func_10004514(...);                    // -> decompressor
```

The same entry layout is reused for the master table, per-section archives, and
inner containers.

### Master section table at `0xAB1950`

The US master table is `0xF0` bytes long and contains 30 entries:

- entries `0-28` map directly to `assets00-assets1C`;
- entry `29` is the final `0x90`-byte block at ROM `0x03F8B770`;
- every master entry is stored raw (`type = 0`);
- the final-entry bit is set only on entry 29;
- each entry's absolute ROM start is `0xAB1950 + data_offset`.

The first entry therefore resolves to `assets00` at `0x00AB1A40`, and entry 28
resolves to `assets1C` at `0x03F8AB18`. This table is the authoritative source
for section boundaries; `conker.us.yaml` currently records the same ranges
manually.

Examples (retail US ROM): `assets06` file 0 uses a `0x140`-byte table (40 slots,
13 live compressed blocks); `assets17` file 0 has its top-level flag set to `0x1`
(compressed) and inflates to the `"B1"` audio bank (§6).

## 4. Container payloads: object / entity bundles (Strong)

Sections such as **assets06, assets08, assets13** are containers per section 3.
Each live block is **rzip-compressed** (nested, per section 2). Decompressing a
block yields *another* container (same offset-table format) whose entries are a
contiguous partition of typed sub-resources.

> **Correction:** an earlier draft of this document described these as pure
> model/geometry files with triangle-index arrays. Decoding the actual contents
> shows they are **composite object/script bundles**, not meshes. The
> "index arrays" are small parameter records, not triangle indices.

A single decompressed block from `assets06` file 0 mixes, in order:

- **A small header record** - e.g. `00 0c 00 0c 00 0c 00 03` (counts / bounds).
- **Position arrays** - 8-byte records: three big-endian `s16` (X, Y, Z) plus a
  2-byte pad (always `0x0000`). 21 such points were decoded for one block, e.g.
  `(590, 110, -2058)`, `(408, 75, -2187)`, `(-222, 28, -1229)`. They cluster on a
  near-constant low Y with wide X/Z spread - consistent with **waypoints / spawn
  or logical points on a ground plane** rather than character-mesh vertices.
- **Small parameter records** - 8-byte records holding tiny integers
  (`00 01 …`, `00 02 01 …`). Counts/flags, **not** triangle indices.
- **Float records** - 8 bytes: a big-endian IEEE-754 `float` plus a 4-byte tag,
  e.g. `36.0`, `28.0`, `-13.0`. Likely transforms / spline or timing parameters.
- **Name and dialogue strings** - plain ASCII, e.g. object tags and lines such as
  `"ah ! right, don'…"`, `"whoa ! i take it"`. Their presence is what identifies
  these blocks as game-object / cutscene-script data.

So `assets06` is **entity / script data**.

**Per-dialogue-line data confirmed via differential ROMs (Strong, 2026-07-14):**
two independent US romhacks corroborate that `assets06` carries per-line
dialogue data (subtitle text and/or timing metadata):

- The "Uncensored" hack (restores censored voice lines; byte-identical to
  retail US outside asset data) changes exactly **15 of the 50 `assets06`
  files** - indices 1, 4, 6, 7, 8, 12, 14, 15, 16, 22, 30, 33, 40, 47, 48 -
  and leaves the container offset table byte-identical (files replaced
  strictly in place). The changed files keep identical headers and diverge
  later in the payload. The same hack replaces 23 `assets16` audio files
  (§6), so these 15 files are the natural samples for reversing the bundle
  schema: we know exactly which dialogue they belong to.
- A Spanish fan-translation hack rewrites ~396 KB across `assets06` (about
  10x what censorship alone accounts for) while leaving `assets16` audio at
  retail - exactly what a subtitle translation has to touch.

**Byte-exact change boundaries (2026-07-15):** obtained the actual
`Conker's Bad Fur Day (Uncensored).bps` patch (BPS1 footer: source crc32
`CE8CC172` = `baserom.us.z64` exactly, target crc32 `E1B9019B` = the
Uncensored `.z64` exactly - confirms `baserom.us.z64` is genuine retail).
Rather than parse the BPS op stream, a direct full-ROM byte diff (both
ROMs are 67,108,864 bytes; XOR-then-regex approach, ~1.3s total) plus the
`assets06`/`assets16` file offset tables reconstructed from ROM addresses
`0x0117FE50`/`0x01330478` (per `conker.us.yaml`) gives exact per-file
change spans. Totals match the earlier file-level finding exactly
(39,919 / 2,020,358 bytes, 15 / 23 files), confirming both methods agree:

| `assets06` file | file size | first changed byte | last changed byte | change span |
|---|---|---|---|---|
| 0001 | 25,208 | 3,078 | 21,992 | 75.0% of file |
| 0004 | 44,744 | 12,814 | 13,583 | 1.7% |
| 0006 | 15,008 | 1,638 | 4,792 | 21.0% |
| 0007 | 11,408 | 384 | 11,394 | 96.5% |
| 0008 | 25,752 | 11,526 | 25,749 | 55.2% |
| 0012 | 19,432 | 5,590 | 8,320 | 14.0% |
| 0014 | 30,936 | 11,336 | 12,985 | 5.3% |
| 0015 | 1,128 | 327 | 1,119 | 70.2% |
| 0016 | 3,280 | 326 | 1,809 | 45.2% |
| 0022 | 21,328 | 6,868 | 11,526 | 21.8% |
| 0030 | 3,600 | 324 | 2,215 | 52.5% |
| 0033 | 4,408 | 324 | 1,936 | 36.6% |
| 0040 | 6,832 | 324 | 3,340 | 44.1% |
| 0047 | 31,416 | 5,662 | 23,646 | 57.2% |
| 0048 | 8,672 | 326 | 1,671 | 15.5% |

Each file's changes are a cluster of small runs (dozens of 1-100-byte
diffs) starting well after byte 0, not a single contiguous block - i.e.
the leading header/table portion of every file is untouched, and one
*specific sub-block* of that file's container (per §3's nested offset-table
format) is what got replaced.

By contrast, every one of the 23 changed `assets16` files diverges
starting at byte 2 (right after the 2-byte MPEG frame-sync header) through
nearly the end of the file - confirming these are wholesale audio
replacements, not a structured format worth reversing further.

**Dialogue text schema decoded (Strong, 2026-07-15):** walked each of the
15 changed `assets06` files' own container table (§3 format) using the
`first changed byte` offsets above, following the structure one level
deeper than §4's block-level description:

```text
assets06/NNNN.bin (raw file, top-level §3 table, ~40 slots)
 └─ entry 1 (rzip-compressed, per §2) - decompressing yields ANOTHER
    §3-format container, whose entries are the position/param/float
    records already described above, plus...
     └─ the LAST entry (`packed` bit 31 set - the §3 final-entry marker) -
        **the subtitle/dialogue text string itself**, plain ASCII,
        `0x0A` = line break within the subtitle, null-padded to the
        record's declared length.
```

Confirmed directly in **7 of the 15** censored files, where the changed
bytes fall exactly inside this last entry (the other 8 files' censored
line lives in an earlier string-type entry of the same nested table - not
checked in detail, but the container format and text encoding are the
same). Two clean examples (`file 0033` entry 58, `file 0007` entry 36),
decoded and diffed retail vs. the Uncensored hack:

```text
retail:     what the [a6][a2][b5][b2][b4][b3][a1] !␊   it's that␊bloody squirrel !␊quick, into␊character !
uncensored: what the fuck !␊   it's that␊bloody squirrel !␊quick, into␊character !

retail:     you twat !␊don't ever do␊ that again. ␊now [a6][a2][b2][a2][b5][a2][b3][a2][b4][a1] off !
uncensored: you twat !␊don't ever do␊ that again. ␊now fuck off !
```//(`␊` = the literal `0x0A` byte; `[XX]` = a raw byte outside printable ASCII)

**Censorship mechanism:** the retail (censored) build doesn't delete or
silence the profane word in the subtitle - it substitutes a run of
placeholder glyph bytes from a small fixed set (`0xA1 0xA2 0xA3 0xA4 0xA6`
and `0xB2 0xB3 0xB4 0xB5` observed so far, i.e. two clusters of "special
character" codes above the printable-ASCII range) in its place, roughly
but not exactly matching the redacted word's length (`fuck` → 7 bytes,
`fuckin'` → 7 bytes with spaces between each glyph, `fuckers` → 9 bytes,
`shit` → 7 bytes) - not a fixed per-letter cipher, likely chosen to keep
the on-screen redaction visually plausible / lip-sync-adjacent rather than
to encode the original word. `0xBD` is a *separate*, non-censorship glyph
- it appears identically in both retail and Uncensored text (e.g. as a
pause/dash between clauses), so don't confuse it with the redaction set.
The Uncensored hack's patch is simply: replace the glyph run with the
literal ASCII word, leaving everything else in the entry (and the rest of
the file) byte-identical - consistent with the file-level "changes cluster
in one entry, near the end" finding above.

Not yet decoded: the exact selection rule for which of the ~9 placeholder
glyphs is used at each position (likely font-table-driven, low priority),
and the schema for the 8 files where the censored line isn't the final
entry (probably just "another string-type entry earlier in the same
table" - the position/param/float record shapes from §4's block-0 survey
should make string-type entries easy to spot: no fixed record stride,
mostly bytes in `0x20-0x7E` plus `0x0A`/`0xBD`, null-padded).

**assets08** is a related but simpler bundle: one block per game chapter, each
holding 20-byte records plus an ASCII name. The names are the actual CBFD chapter
titles - **Hungover, Windy, Bats Tower, Barn Boys, Sloprano, Ugga Bugga, Spooky,
It's War, The Heist** - so this is front-end / level-select metadata.

## 4a. Model geometry: `assets13` vertex arrays (Confirmed)

**assets13** is **render geometry**, and its vertex format has been decoded and
validated across every record in the section (US ROM). It nests four levels deep:

```text
assets13 section (archive of files)
 └─ file (container, §3)
     └─ block (container, §3)
         └─ record (rzip-compressed, §2)
             └─ vertex array   ← decoded below
```

A decoded record is a **plain vertex array**:

- **Vertex = 6 bytes**: big-endian `s16` X, `s16` Y, `s16` Z. No per-vertex UV,
  color, or normal is stored inline (so those are supplied elsewhere - a separate
  block and the §5 textures).
- The array is `V` vertices (`6·V` bytes) **zero-padded up to a 16-byte
  boundary**. The padded payload length alone does **not** always identify `V`:
  padding can be 6 bytes or more (for example, 14 vertices use 84 bytes but pad
  to 96, and `floor(96/6)` would incorrectly report 16). Exact counts need the
  referencing metadata or a validated per-record count; zero-valued trailing
  vertices cannot safely be distinguished from padding by stripping zeros.

This was checked against **all 69 records** in `assets13`: 69/69 decompress to a
16-byte-aligned length with trailing zero padding. Earlier provisional counts
using `floor(payload/6)` ranged 13-338, but records with six or more padding
bytes need recounting once their metadata field is identified.
Coordinates are small and **bilaterally symmetric** (e.g. `(-23, 28, 33)` paired
with `(23, 28, 33)`), exactly as expected for a centered model.

Within one block the records are near-identical vertex arrays that differ by a
unit or two per coordinate - i.e. **vertex-animation frames** (or LOD variants)
of the same mesh. No raw F3DEX display lists (`G_VTX` / `G_ENDDL`) appear in the
data, so the engine most likely builds display lists from these arrays at load
time.

Decode one record:

```python
import struct
V = vertex_count_from_metadata         # do not infer this from padded size alone
verts = [struct.unpack(">hhh", rec[i*6:i*6+6]) for i in range(V)]
```

### Where are the faces?

`assets13` holds **only vertex positions** - the topology is not here. Evidence
(whole section, US ROM): across all **69 leaf records** there are **zero** F3DEX
`G_ENDDL` (`0xDF……`) display-list markers, and no record decodes as
vertex-index triples. The X-coordinate sign balance across every record is almost
exactly even (2936 negative vs 2845 positive), i.e. the data is purely centered
vertex geometry.

So triangle/face indexing, UVs, normals, material/texture binding, and the
animation timing are stored **outside** the vertex arrays - either built at load
time by the renderer or held in a separate resource. A survey of the neighbouring
sections did not turn up inline display lists paired with these vertices
(`assets12` is a table of repeating 4-byte records; `assets14` starts with a
distinct `10 00 00 00 …` header). Pinning down the topology source is best done
from the model-drawing code in `conker/src` that consumes these vertex streams,
not from the data alone - see §9.

## 5. Textures / images (Partial; per-file formats not yet inventoried)

The extracted numbered files in **assets00-assets05** are leaf payloads rather
than nested §3 containers, and all currently extracted file sizes are even.
That is consistent with 16-bit pixels or palette records, but it is not enough
to classify every file as RGBA5551.

Current US extraction inventory:

| Section | Numbered files | Smallest | Largest |
| --- | ---: | ---: | ---: |
| assets00 | 56 | 2,560 | 28,160 |
| assets01 | 183 | 120 | 50,840 |
| assets02 | 145 | 32 | 901,040 |
| assets03 | 77 | 184 | 4,792 |
| assets04 | 59 | 872 | 225,664 |
| assets05 | 39 | 376 | 48,040 |

`assets00/0005.bin` contains long runs of big-endian `0x4210`, which decodes as
an RGBA5551 gray value and is consistent with a flat raster region. Several
common sizes also fit 16-bit images (`12,800 = 80 × 80 × 2`), so RGBA5551 is a
**strong per-sample interpretation**, not yet a section-wide specification.

Still needed:

- locate width, height, format, and palette metadata in the referencing tables
  or rendering code;
- render every plausible RGBA16 file and reject obviously structured data;
- test for CI4/CI8 plus palette pairs, intensity formats, masks, mip levels, and
  atlases;
- explain the very small records and the 901,040-byte `assets02` payload before
  labeling the full `assets00-assets05` range as textures.

## 6. Audio (Confirmed / Strong)

- **assets16 - streamed dialogue: MPEG-2 Layer III (Confirmed).** All 453
  numbered retail-US files begin with frame header `0xFFF3`, whose version and
  layer bits identify MPEG-2 Layer III. They play and convert with standard MP3
  tooling. `ffprobe` reports the checked `0000.bin` sample as 22,050 Hz, mono,
  24 kbps; a full corpus-level rate/channel inventory is still worth adding.
  The debug prototype contains roughly 900 files. The retail bank is confirmed
  as specifically **dialogue** by the "Uncensored"
  romhack (2026-07-14): it swaps exactly 23 of the 453 files wholesale, in
  place (indices 5, 19, 20, 27, 34, 35, 36, 47, 83, 119, 126, 143, 149, 150,
  175, 287, 289, 325, 341, 384, 387, 426, 439 - the censored voice lines),
  with the offset table untouched. The same hack's `assets06` changes (§4)
  identify the matching per-line metadata.
- **assets17/0000 - libaudio-compatible instrument bank (`"B1"`) (Confirmed
  root structures).** `0x4231` is `AL_BANK_VERSION`, defined in this repo's
  `conker/include/2.0L/PR/libaudio.h`. The beginning of `0000.bin` is a standard
  `ALBankFile` followed by an `ALBank`:

  ```text
  +0x00  s16  ALBankFile.revision       0x4231 = "B1"
  +0x02  s16  ALBankFile.bankCount      1
  +0x04  u32  ALBankFile.bankArray[0]   0x00000008
  +0x08  s16  ALBank.instCount          0x00AA = 170
  +0x0A  u8   ALBank.flags              0
  +0x0B  u8   ALBank.pad                0
  +0x0C  s32  ALBank.sampleRate         22050
  +0x10  u32  ALBank.percussion         0
  +0x14  u32  ALBank.instArray[0]       0x000002BC
  ```

  The game calls `func_10012934(ALBankFile *, u8 *table, s32)` to validate the
  `B1` revision and relocate its banks. That function is explicitly marked as
  a non-vanilla `alBnkfNew`: the root structures are standard libaudio, while
  later instrument/sample pointer packing includes game-specific behavior.
  `0002.bin` is the associated ~21 MB sample data. The individual sample codec
  and the meaning of the custom encoded instrument pointers remain open.
- **`assets17` contains several distinct sub-file formats; two are structurally
  identified in the current retail extraction:**
  - **`0002` (~21 MB): the raw sample/instrument bank** referenced by pointers
    reached from the `B1` instrument bank. Extractable today with
    third-party tools: N64 Midi Tool → DLS →
    Vienna/SynthFont → SF2, if anyone wants to actually listen to the game's
    instrument samples rather than just parse the container format.
  - **`0003` (~2.8 MB): a second, differently-tagged bank - magic `"S1"`
    (`0x5331`), i.e. `AL_SEQBANK_VERSION`, not `AL_BANK_VERSION`.** Header:
    `ALSeqFile.revision = 0x5331`, `ALSeqFile.seqCount = 149`, followed by 149
    `(u32 offset, s32 length)` `ALSeqData` records and their payloads. The root
    container therefore matches the libaudio `ALSeqFile` definition exactly;
    the individual sequence command encoding is still tentative. This is a
    separate container from the B1 bank documented above - do not assume
    `assets17`'s sub-files share one schema.
    **Independent confirmation (2026-07-15):** a community USF rip
    (`rom backup/Conker's Bad Fur Day sound files/`, `NUS-NFUE-USA.usflib` +
    173 `.miniusf` pointer files, `usfby=Josh W. / hcs`, `artist=Robin
    Beanland`) names its tracks `sparseNN[a-g].miniusf` where `NN` is a
    **hex** index - 148 unique base indices, **contiguous `0x01`-`0x94`,
    zero gaps, no `0x00`**. That's one short of the 149-entry table above in
    exactly the way you'd expect if index `0` is a "no music"/silence slot
    (nothing to rip) and `1`-`148` are the real sequences - strong,
    independently-sourced corroboration of the 149 count from a completely
    different source than the wiki page. The `[a-g]` letter suffixes on
    some indices (e.g. `sparse01a`-`sparse01e`, six variants of track 1)
    are presumably alternate mixes/loop points for the game's adaptive
    "sparse" instrumentation system (Rare's dynamic layered-music
    technique), not separate sequences - i.e. the ROM-side count of 149
    logical entries should still hold even though the rip has more files
    than that. USF files are actual playable audio (via any PSF-family
    player, e.g. foobar2000 + `in_usf`) - useful as a real listening
    reference when trying to identify which track index corresponds to
    which in-game context.

    **Tried diffing `.miniusf` contents against the ROM container - no
    direct byte match, and that's informative, not a dead end.** USF's
    `.miniusf`/`.usflib` "reserved" area (PSF version byte `0x21`) is
    *not* zlib-compressed like the `.usflib`'s own outer PSF wrapper might
    suggest - it's raw, tagged `SR64`, and decodes cleanly as a flat
    sequence of `(u32 length, u32 address, length bytes of data)` sparse
    RDRAM-write blocks (326 blocks for `sparse01.miniusf`, consuming the
    entire reserved area with no leftover bytes - confirms the parse is
    right). Matches the "sparse" naming: a sparse set of memory pokes, not
    a full RAM dump. Extracted sequence-bank entry `[1]` from
    `assets17/0003.bin` (offset 1296, length 30462, per its own
    offset-table) and searched for it byte-for-byte in `sparse01.miniusf`'s
    blocks (individually and concatenated) - **no match**, not even an
    8-byte prefix. Same negative result testing the largest blocks (seven
    consecutive 4096-byte pages at `0x2221ac`-`0x2281ac`, clearly sample
    audio data by entropy) against the raw sample bank `assets17/0002.bin`.
    **Conclusion: the USF rip captures post-processing runtime state**
    (decompressed samples and parsed sequence structures as the game's own
    audio driver leaves them in RDRAM immediately before playback), **not
    a copy of the ROM's compressed/encoded container format** - the two
    are different pipeline stages and won't byte-match by design. Don't
    retry a direct diff; if this USF data gets used for verification, it
    would need to be compared against this project's own *decoded* output
    (once the sample codec and sequence format are understood), not the
    raw container bytes.
  - **File-index ambiguity resolved (2026-07-15):** checked this repo's
    own extraction directly (`assets/rzip/assets17/*.bin`) rather than
    trust the wiki's internally-inconsistent labeling. **`0000.bin` has
    the `B1` header** (`assets17` file 0, as this doc's own §6 text always
    said), **`0003.bin` has the `S1` header** confirming the sequence-bank
    breakdown above. `0001`/`0004`/`0005`/`0006` remain undetermined -
    `0004.bin` (144 bytes) looks like a small offset table itself (regular
    4-byte big-endian values), `0005.bin` (17408 bytes) is all zero bytes
    in its first 0x400+ (possibly padding or a mostly-empty table),
    `0006.bin` starts with small paired byte values (`02 01 ff ff 00 00
    00 00 01 02 ff ff ...`) that could be a per-note/per-channel mapping
    table - none decoded further this pass.

## 7. Data / text tables (Tentative)

- **assets1A** - fixed 8-byte structured records, each ending in an incrementing
  index (`…0001`, `…0002`, …). A table of some kind (layout or string metadata).
- **assets1C** ("text, credits" per the yaml) - the first file is a **table of
  big-endian floats** (`-0.625, 13.5, 2.5, …`), i.e. layout/positioning data
  rather than the strings themselves. Actual credit strings live in sibling
  files. Note some files here also carry `.gz` companions from extraction.

## 8. Section summary

| Section | Current classification | Confidence |
| --- | --- | --- |
| assets00-05 | Image/texture candidates plus small or oversized records; RGBA5551 confirmed only for samples (§5) | Partial |
| assets06 | Container → nested rzip → entity/script/dialogue bundle (§3, §4) | Strong |
| assets07 | Tiny 0x50-byte section | Unknown |
| assets08 | Chapter / menu metadata (§4) | Strong |
| assets09-11 | Not classified | Unknown |
| assets12 | Repeating four-byte records; possible geometry companion | Tentative |
| assets13 | Animated `s16` XYZ position arrays; topology stored elsewhere (§4a) | Confirmed payload, count metadata open |
| assets14-15 | Not classified; likely related resource tables | Unknown |
| assets16 | 453 MPEG-2 Layer III dialogue streams (§6) | Confirmed |
| assets17 | Mixed audio package: `B1` instrument bank, sample data, `S1` sequence bank, and support tables (§6) | Root structures confirmed |
| assets18 | Contains another compressed payload | Tentative |
| assets19 | Not classified | Unknown |
| assets1A | Fixed eight-byte records, language-related per YAML note (§7) | Tentative |
| assets1B | Not classified | Unknown |
| assets1C | Float layout table plus credit/text files (§7) | Tentative |
| post-assets block | Final 0x90-byte master-table entry at `0x03F8B770` | Unknown |

## 9. Open questions / next steps

- **assets13 faces & attributes.** The vertex arrays are decoded (§4a) and shown
  to contain *no* topology (0 display-list markers across 69 records). Still open:
  where triangle indexing, UV/normal/material binding, and per-frame timing live -
  a separate resource or runtime-generated. Trace this from the model-drawing code
  in `conker/src` that reads these vertex streams (start from the `Gfx`/`Vtx`
  definitions in `conker/include/2.0L/PR/gbi.h`). Also locate the authoritative
  vertex-count metadata and recompute the provisional 13-338 count range.
- **assets06 bundle schema - dialogue text located (§4), rest still open.**
  The subtitle/dialogue string entry is now identified (plain ASCII, last
  nested-table entry in 7/15 censored samples) and the censorship glyph
  substitution is characterized. Still open: which sub-entries are
  positions vs float params vs the string table for the *other* record
  types in the same nested container (the §4 block-0 survey named the
  shapes but not which object/field each belongs to), how the header
  record ties sub-entries together into one logical object, the exact
  placeholder-glyph selection rule, and locating the censored line's
  entry in the 8/15 files where it isn't the final one.
- **assets17 audio internals.** Decode the custom packed instrument pointers
  processed by `func_10012934`, identify the sample codec in `0002`, decode the
  individual `S1` sequence command streams, and classify `0001`/`0004-0006`.
- **Compressed-code runtime loading (§2a).** The archive/XOR layout is confirmed;
  trace the reported 4096-byte TLB-miss demand-paging mechanism through the
  current init exception and TLB routines.
- **Textures.** Build a corpus scanner for width/height/format candidates,
  render plausible RGBA16 files, and test CI4/CI8 palette pairings before
  assigning formats to complete sections.
- **Unclassified sections.** Inventory assets07, assets09-12, assets14-15,
  assets18-19, assets1B, and the final 0x90-byte master-table payload.

## 10. Reproducing this analysis

From the tracked retail extraction under `assets/rzip/`:

```python
import struct, zlib

def read_table(data):
    """Parse the §3 table; return (offset, type, final, length) rows."""
    tsize = struct.unpack(">I", data[:4])[0]
    out = []
    for i in range(tsize // 8):
        off, packed = struct.unpack(">II", data[i*8:i*8+8])
        out.append((
            off,
            (packed >> 28) & 0x7,
            bool(packed & 0x80000000),
            packed & 0x0FFFFFFF,
        ))
    return out

def unrzip(block):
    """Decode a §2 rzip block."""
    usize = struct.unpack(">I", block[:4])[0]
    out = zlib.decompress(block[4:], -15)
    assert len(out) == usize
    return out

data = open("assets06/0000.bin", "rb").read()
for off, payload_type, is_final, length in read_table(data):
    if length == 0:
        continue
    block = data[off:off+length]
    inner = unrzip(block) if payload_type == 1 else block
```

To pull files straight from a ROM instead (verified against the retail US ROM),
use the bundled tool - it walks the archive and applies the §2/§3 decode:

```sh
python tools/asset_dump.py list                  # all master-table sections
python tools/asset_dump.py dump assets13 out/    # every file in a section
python tools/asset_dump.py dump assets17 out/ --idx 0   # a single file
```

For raw image and texture payloads, check `n64img`/n64splat image decoding
first. `tools/n64splat/requirements.txt` already pulls in `n64img>=0.1.4`, so
new custom code should focus on CBFD-specific containers, dimensions, and
resource wiring rather than reimplementing standard N64 image formats.
