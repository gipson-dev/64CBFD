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

Findings were derived from two independent extractions and cross-checked between
them: the `debug` prototype under `debug_proto/assets/rzip/`, and the retail
**US** ROM (`baserom.us.z64`, SHA-1 `4cbadd3c…`) read directly at the section
offsets in `conker.us.yaml`. Both versions use identical formats; only the data
differs. Offsets and section names below match `conker.us.yaml`.

## 1. The asset pipeline

```text
ROM
 └─ rzip section (e.g. 0x1A37E0, or each assetsNN section)   ← outer compression
     └─ archive: a run of independently compressed files
         └─ file (.bin, already decompressed by splat)
             ├─ raw payload          (MP3, audio bank, image, table), OR
             └─ container            (offset table → nested rzip blocks)
                 └─ block (rzip-compressed)                  ← inner compression
                     └─ inner container (offset table → sub-resource arrays)
```

Two independent things are called "compression" here, and both use the same
**rzip** codec:

1. The ROM-level `rzip` segments, split by splat into individual files.
2. One or more *inner* rzip layers inside the containers (sections 4/4a) - up to
   four levels deep for `assets13` geometry. This nesting was previously
   undocumented.

## 2. Compression: `rzip` (Confirmed)

Rare's format is a stripped-down gzip: the gzip header/trailer are removed and
replaced with a 4-byte big-endian uncompressed length, followed by a raw
DEFLATE (level 9) payload.

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

This matches `tools/splat_ext/rzip.py` and round-trips cleanly on every block
tested. See also `tools/rareunzip.py` / `tools/rarezip.py`.

### 2a. Compressed *code* loading (Tentative - not independently verified here)

Distinct from the asset-container `rzip` usage above: per the project wiki's
`Useful-Info` page (community find via Discord, `gamemasterplc`), compressed
**code** is loaded on demand in 4096-byte decompressed chunks, triggered by
deliberately abusing the CPU's bad-virtual-address exception handler (a
TLB-miss-driven demand-paging trick, not the straightforward container
walk `func_1502B9B4` does for assets in §3). Reported details:

- One chunk sample sits at ROM `0x42C50`.
- The chunk table is at ROM `0x42454`, encrypted with XOR key `0x8039CCCA`,
  and its offsets are relative to ROM base `0x42450`.
- A chunk-length field also lives at `0x42450`.

Not reproduced or cross-checked against this repo's own extraction yet
(`0x42450` falls inside the `init`/boot range per `conker.us.yaml` - worth
comparing against how `init`/`init_data` are actually split before trusting
the exact offsets). Recorded here so it doesn't need rediscovering; treat as
a lead, not a confirmed mechanism.

## 3. The container / offset-table format (Confirmed)

Model archives and many other files begin with a fixed directory of entries.
This layout is the same one `N64SegRzip.get_files_from_offsets` in
`tools/splat_ext/rzip.py` already parses:

```text
Entry (8 bytes), repeated:
  +0x00  u32  data_offset   (offset from the start of the container/file)
  +0x04  u8   flags
         u24  length        (bytes of payload; combined field = compressed>>24 / &0x0FFFFFFF)
```

- `flags & 0x10` (i.e. the high halfword reads `0x1000`) marks the block as
  **rzip-compressed**; otherwise it is stored raw.
- The **first word doubles as the table size**: `data_offset` of entry 0 equals
  the byte length of the whole table, so `entries = table_size / 8`.
- Unused trailing slots point at end-of-file with `length = 0`.
- The final slot carries flag `0x80` (`0x8000` in the halfword) as a terminator.
- Every block is **padded to an 8-byte boundary**.

This is confirmed by the decompiled game code in
[`conker/src/game_57FA0.c`](../conker/src/game_57FA0.c) (`func_1502B9B4`), which
walks the master asset offset table at `0xAB1950` and does:

```c
more = *entry & 0xFFFFFFF;                 // 28-bit length
if ((*entry & 0x70000000) == 0x10000000)   // type field, 0x1 => compressed
    func_10004514(...);                    // -> decompressor
```

So the top byte is a 3-bit type/flag field (mask `0x70000000`), value `0x1` means
the block is rzip-compressed, and the low 28 bits are the length. The same
entry layout is reused for the master table, the per-section archives, and the
inner containers.

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
     └─ the LAST entry (flags 0x80 - the §3 terminator bit doubles as
        "final real entry" here, it is not always zero-length) -
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
  boundary**. `V` is recoverable as `floor(payload/6)`.

This was checked against **all 69 records** in `assets13`: 69/69 decompress to a
16-byte-aligned length with trailing zero padding, and `V` ranges 13–338.
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
V = len(rec) // 6                      # trailing bytes are zero pad to 16
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

## 5. Textures / images (Strong for encoding, Tentative for dimensions)

**assets00–assets05** are **not** containers - they are uncompressed raster
blocks. Sampled pixels are 16-bit **RGBA5551** values: e.g. `assets00/0005.bin`
contains long runs of `0x4210` (R=G=B=8, A=0, a flat gray fill), exactly what a
solid texture region looks like in RGBA16.

- Encoding: **RGBA5551, 2 bytes/pixel, big-endian** (Strong).
- File sizes seen: 12800 (= 80×80 @ 16bpp), 17600, 21120 bytes.
- **Tentative:** dimensions are *not* stored in the file. 80×80 fits 12800
  cleanly, but the non-square sizes mean width/height must come from elsewhere
  (a header table or the referencing code). CI4/CI8 (palette-indexed) variants
  for other sections have not been ruled out.

## 6. Audio (Confirmed / Strong)

- **assets16 - streamed audio: MP3 (Confirmed).** Every file begins with an
  MPEG audio frame sync (`0xFFF3…`). These are standard MPEG-1/2 Layer III
  frames and play/convert with normal MP3 tooling. This is the game's large
  speech/music streaming bank (~900 files in the debug proto; 453 in retail
  US). Confirmed as specifically the **dialogue** bank by the "Uncensored"
  romhack (2026-07-14): it swaps exactly 23 of the 453 files wholesale, in
  place (indices 5, 19, 20, 27, 34, 35, 36, 47, 83, 119, 126, 143, 149, 150,
  175, 287, 289, 325, 341, 384, 387, 426, 439 - the censored voice lines),
  with the offset table untouched. The same hack's `assets06` changes (§4)
  identify the matching per-line metadata.
- **assets17 - audio bank / sequenced audio (`"B1"`) (Confirmed header).** Files
  start with the ASCII magic `"B1"` (`0x4231`). This is Rare's own bank format,
  **not** a standard libultra `.m64`. The header (retail US, `assets17` file 0)
  decodes as:

  ```text
  +0x00  char[2]  magic     "B1"
  +0x02  u16      version   0x0001
  +0x04  u32      0x00000008   (fixed; entry stride / header size?)
  +0x08  u16      count     0x00AA = 170   (entries in table 1)
  +0x0A  u16      0
  +0x0C  u32      0x00005622 = 22050        (sample rate, Hz)
  +0x10  u32      0
  +0x14  u32      0x000002BC = 700          (secondary count?)
  +0x18  u32[170] table 1 - monotonically increasing entries, each
                  (u24 offset, u8 type/flags), e.g. 0x006CB91F, 0x006D9F05…
                  ends at 0x2C0
  0x2C0  …        table 2 - further increasing entries (event / region data)
  ```

  The `22050` sample rate and the sorted `(offset, type)` table identify this as
  a **sample/instrument bank** whose entries point into the large sample data in
  the rest of the `assets17` section (~22 MB, ROM `0x29AE9E8`–`0x3F82170`). The
  per-sample codec and the table-2 event encoding still need the audio-driver
  code to decode fully.
- **`0x4231` ("B1") is `AL_BANK_VERSION`** per the real `libaudio.h` constant
  name (community find, 2026-07-15 via the project wiki's `Useful-Info` page,
  sourced from a Discord chat with `gamemasterplc` - not independently
  re-derived here, but consistent with and naming the header already decoded
  above). The wiki also notes `0x4231` is referenced from a function at
  `func_80012934` in an older (pre-address-remap) build of this project - not
  yet re-located under this repo's current `0x1500xxxx`/`0x1600xxxx`
  addressing, but worth grepping for if the audio-driver code is tackled.
- **`assets17`'s numbered sub-files have distinct formats, only two decoded so
  far (Tentative, wiki-sourced, not independently verified against this
  ROM):**
  - **`0002` (~21 MB): the raw sample/instrument bank** referenced by table 1
    above. Extractable today with third-party tools: N64 Midi Tool → DLS →
    Vienna/SynthFont → SF2, if anyone wants to actually listen to the game's
    instrument samples rather than just parse the container format.
  - **`0003` (~2.8 MB): a second, differently-tagged bank - magic `"S1"`
    (`0x5331`), i.e. `AL_SEQBANK_VERSION`, not `AL_BANK_VERSION`.** Header:
    `u16 count` (149 in the sample seen) followed by `count` `(u32 offset,
    u32 length)` pairs, then the 149 payloads themselves (likely
    `ALSeqFile`-formatted MIDI-like sequence data, matching the "149 music
    files" description). This is a **separate container format** from the B1
    bank documented above - don't assume `assets17`'s sub-files share one
    schema.
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
    which in-game context, and `NUS-NFUE-USA.usflib` may itself embed the
    same sample-bank memory image as `assets17/0002`/`0003` - worth diffing
    against if the container format work continues.
  - `0000`/`0001`/`0004`–`0006` remain undetermined; the wiki's own file
    numbering for which one carries the B1 header is internally inconsistent
    (heading says `0001`, the shown command runs on `0000.bin`) - re-verify
    the actual index before relying on it.

## 7. Data / text tables (Tentative)

- **assets1A** - fixed 8-byte structured records, each ending in an incrementing
  index (`…0001`, `…0002`, …). A table of some kind (layout or string metadata).
- **assets1C** ("text, credits" per the yaml) - the first file is a **table of
  big-endian floats** (`-0.625, 13.5, 2.5, …`), i.e. layout/positioning data
  rather than the strings themselves. Actual credit strings live in sibling
  files. Note some files here also carry `.gz` companions from extraction.

## 8. Section summary

| Section       | Kind (yaml note)        | Format (this doc)                                       |
| ------------- | ----------------------- | ------------------------------------------------------- |
| assets00–05   | —                       | Uncompressed RGBA5551 raster (§5)                       |
| assets06      | —                       | Container → nested rzip → object/script bundle (§3, §4) |
| assets08      | —                       | Chapter / menu metadata table (§4)                      |
| assets13      | —                       | 3D model geometry: `s16` XYZ vertex arrays (§4a)        |
| assets16      | "MP3s"                  | MPEG Layer III audio frames (§6)                        |
| assets17      | "m64? files"            | `"B1"` audio bank (§6)                                  |
| assets1A      | "the `<LANGUAGE>` …"    | 8-byte record table (§7)                                |
| assets1C      | "text, credits etc"     | Float layout table + string files (§7)                  |

Sections not listed have not been classified in detail yet; most non-audio
`assetsNN` files follow either the container (§3) or raw-raster (§5) pattern.

## 9. Open questions / next steps

- **assets13 faces & attributes.** The vertex arrays are decoded (§4a) and shown
  to contain *no* topology (0 display-list markers across 69 records). Still open:
  where triangle indexing, UV/normal/material binding, and per-frame timing live -
  a separate resource or runtime-generated. Trace this from the model-drawing code
  in `conker/src` that reads these vertex streams (start from the `Gfx`/`Vtx`
  definitions in `conker/include/2.0L/PR/gbi.h`).
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
- **assets17 (`"B1"`).** Decode table-2 (the event/region data after `0x2C0`) and
  the per-sample codec; identify what `+0x04 = 8` and `+0x14 = 700` count.
  Also: verify the `"S1"`/`ALSeqFile` sub-file (§6) against this repo's own
  extraction (wiki-sourced, unverified here), resolve its file-index
  labeling inconsistency, and decode the still-undetermined sub-files
  (`0000`/`0001`/`0004`–`0006`).
- **Compressed code loading (§2a).** Reproduce/cross-check the reported
  4096-byte on-demand chunk mechanism (XOR key `0x8039CCCA`, table at ROM
  `0x42454`) against this repo's own `init`/`init_data` extraction -
  currently only a recorded lead, not verified.
- **Textures.** Find where image width/height/format is specified, and check for
  CI4/CI8 (palette) textures in other sections.
- **Master asset offset table** at ROM `0xAB1950` (`assets_offsets_table` in
  `conker.us.yaml`, walked by `func_1502B9B4`) still needs a written spec.

## 10. Reproducing this analysis

From an extraction (e.g. `debug_proto/assets/rzip/`):

```python
import struct, zlib

def read_table(data):
    """Parse the §3 offset table; return list of (offset, flags, length)."""
    tsize = struct.unpack(">I", data[:4])[0]
    out = []
    for i in range(tsize // 8):
        off, packed = struct.unpack(">II", data[i*8:i*8+8])
        out.append((off, packed >> 24, packed & 0x0FFFFFFF))
    return out

def unrzip(block):
    """Decode a §2 rzip block."""
    usize = struct.unpack(">I", block[:4])[0]
    out = zlib.decompress(block[4:], -15)
    assert len(out) == usize
    return out

data = open("assets06/0000.bin", "rb").read()
for off, flags, length in read_table(data):
    if length == 0:
        continue
    block = data[off:off+length]
    inner = unrzip(block) if flags & 0x10 else block   # nested container / geometry
```

To pull files straight from a ROM instead (verified against the retail US ROM),
use the bundled tool - it walks the archive and applies the §2/§3 decode:

```sh
python tools/asset_dump.py list                  # known sections + ROM offsets
python tools/asset_dump.py dump assets13 out/    # every file in a section
python tools/asset_dump.py dump assets17 out/ --idx 0   # a single file
```
