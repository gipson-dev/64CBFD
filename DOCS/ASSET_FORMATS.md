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

`tools/vertconvert.py` is not applicable to these records. It converts the
standard 16-byte N64 SDK `Vtx` structure, not this six-byte position-only
format.

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

**Found the real per-vertex consuming code (2026-07-28), confirming the
vertex-animation-frame hypothesis directly from game logic, not just data
shape.** `conker/include/structs.h`'s `vertex` type (`f32 x,y,z` - a plain
runtime position) is written by exactly one function,
**`func_15043FF0(vertex *arg0, struct113 *arg1)`** (`conker/src/game_71240.c`,
real matched C):

```c
void func_15043FF0(vertex *arg0, struct113 *arg1) {
    arg0->x = arg1->unk18;
    arg0->y = arg1->unk1A;
    arg0->z = arg1->unk1C;
    arg0->x += arg1->unk38 * 0.000015258789f; // 1/65536
    arg0->y += arg1->unk3A * 0.000015258789f;
    arg0->z += arg1->unk3C * 0.000015258789f;
}
```

This is a **two-keyframe vertex blend**: a base position (`struct113`'s
`unk18`/`1A`/`1C`, `s16` each - exactly `assets13`'s own 6-byte-vertex
layout) plus a fixed-point fractional delta (`unk38`/`3A`/`3C`, same
1/65536 scale libultra uses for fixed-point elsewhere in this codebase)
toward a second keyframe. `struct113` is a 0x40 (64)-byte record with only
those six halfwords named so far — the rest is very likely per-vertex
UV/normal/color and other animation fields `func_15043FF0` doesn't touch,
still unidentified. This is almost certainly the "vertex-animation frame"
blend `assets13`'s own near-identical sibling records (differing by a
unit or two per coordinate, see above) were always suspected to feed.

Traced `func_15043FF0`'s only two real callers: `func_1505327C`
(`game_77AD0.c`, disabled/non-matching draft, actor knockback-reaction
code — calls it as `func_15043FF0(&sp3C, arg0->unk1D4 + (arg4 << 6))`,
where `<<6` = **×64**, matching `struct113`'s exact size — `unk1D4` is a
**per-actor pointer to an array of `struct113` records**, i.e. every
spawned actor with a deformable mesh owns its own vertex-blend buffer);
and `func_1503A830` (`conker/asm/64120.s`, 1041 real asm instructions, no
C draft anywhere), which also calls a second large unmatched function
(`func_150379DC`, 468 instructions, same file) and the project's own
already-identified 64-bit PRNG (`func_150ADA20`) — consistent with a
real-time per-vertex deformation/effect system (cloth, water, or
particle-style vertex jitter), not a one-shot static mesh loader.
`func_1503A830` itself is called from exactly one place
(`func_1502BD84`, `conker/asm/58F80.s`), which itself has **no caller
anywhere in the codebase** — reachable only via some not-yet-found
function-pointer/dispatch table, the same shape as every other
actor/model-specific mechanism this project's PC port has hit.

**Answers the open "where are the faces" question at the mechanism
level, but doesn't unblock the PC port further right now**: the real
vertex-consuming code exists, is now identified precisely, and confirms
`assets13` records are genuine two-keyframe animation blend sources for
a real per-actor deformable-mesh system — but reaching it requires a
live, model-bearing actor instance, which needs the same level/actor
asset loading (`assets06`) this whole project has independently
converged on as the standing wall from the game-state-machine, category-
dispatch, and asset-loading investigations. Full trace (including the
64CBFDOGL PC port's own reachability check) in that project's
`DOCS/WORKING_NOTES/`.

## 5. Textures / images (RGBA5551 confirmed by visual round-trip for several files; per-file format/dimension inventory still open)

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
common sizes also fit 16-bit images (`12,800 = 80 × 80 × 2`).

**Upgraded to Confirmed for a real sample (2026-07-27, refined same day):
decoded numerous `assets00` files as big-endian RGBA5551 and visually
rendered them (`tools/render_rgba5551.py`) - most produce clearly
structured, non-random images (small icon/character/plant motifs repeated
in a grid, most likely animation frames or a flipbook-style icon strip,
not one large background texture), not noise.**

**Correction to the first pass of this same investigation:** the initial
check picked dimensions by "does `byte_count/2` factor into this one
plausible-looking `w×h`" without comparing against sibling factor pairs of
the *same* byte count, and got at least one file wrong. Re-checked with a
tool that renders and ranks *every* valid factor pair (by average
local-pixel-gradient - a genuine image has much lower pixel-to-neighbor
variation than the same bytes reinterpreted at the wrong width, which
scrambles unrelated rows together): `assets00/0039.bin` (12,800 bytes) is
**not** a coherent image at the originally-guessed 80×80 (looks like the
same content mangled into a 5-wide grid); at **32×200** it's a clean,
sharp repeated icon (a grape-bunch-like shape). Always compare a "looks
plausible" dimension against its lower-gradient siblings before trusting
it - a wrong width scrambling a simple, sparse icon can still look
superficially "structured" by coincidence.

Confirmed-good widths by file, cross-checked visually (not just by
gradient score) - all render as a small icon/character repeated in a
grid at the given width:

| Bytes (pixels) | Width | Example files | Visual content |
| ---: | ---: | --- | --- |
| 2,560 (1,280px) | 32 | 0021, 0033, 0036, 0045, 0046 | grape-bunch-style icon |
| 3,520 (1,760px) | 32 | 0015-0020, 0022, 0024, 0034, 0035, 0038 | octopus/creature icon |
| 3,520 (1,760px) | 16 | 0047, 0049 | leaf/stick icon (same byte size, *different* width than the majority above) |
| 12,800 (6,400px) | 32 | 0001, 0039, 0040 | grape-bunch icon (tall strip) |
| 12,800 (6,400px) | 64 | 0002, 0003, 0055 | colorful character/rainbow icon (same byte size, *different* width) |
| 15,360 (7,680px) | 32 | 0052 | yellow/green plant icon |
| 19,200 (9,600px) | 48 | 0050 | flower-with-berries icon |
| 20,480 (10,240px) | 64 | 0014 | (consistent with the 64-width family, not individually re-checked) |
| 21,120 (10,560px) | 64 | 0000, 0004, 0012, 0053, 0054 | vine/plant icon |
| 28,160 (14,080px) | 64 | 0013 (largest `assets00` file) | vine/plant icon |

**Files of the *identical* byte size can have different correct widths**
(3,520B: 32 vs 16; 12,800B: 32 vs 64) - byte size alone does not determine
width even within one section; a real per-file metadata source (see "Still
needed" below) is the only fully reliable answer, this per-file visual
check is a stopgap that happens to work often.

**One size class remains genuinely unresolved, not just unchecked:** the
**17,600-byte (8,800px) class**, roughly 21 files (`0005`-`0011`, `0023`,
`0025`-`0032`, `0041`-`0044`, `0051`). None of their factor-pair dimensions
(`40×220`, `88×100`, `100×88`, `160×55`, `55×160`, `50×176`, etc.) render as
a coherent RGBA5551 image - all show the same repeating, meaningless
diagonal/horizontal stripe pattern regardless of width. Also tried
reinterpreting the raw bytes as 8-bit CI8 grayscale indices (no palette) at
several widths - still just noise, not recognizable shapes. This is a
real, distinct puzzle, not a rendering bug: either (a) genuine CI4/CI8 data
that needs an actual color palette (not grayscale) to look right, (b) a
different non-image data type that happens to share this byte-size
profile, or (c) a dimension/layout this exact-factor search can't reach
(e.g. a header offset, or non-8-bit-aligned width). Don't re-guess widths
blind for this class - find the loading code or palette table instead.

Reusable tooling: `tools/render_rgba5551.py`. For a given file (or a whole
directory of `asset_dump.py` output), tries every `w` in `[4, 256]` where
`w` divides the file's `pixel_count` evenly with a resulting `h` also in
`[4, 256]`, decodes big-endian RGBA5551 (`r=(v>>11)&0x1F`, `g=(v>>6)&0x1F`,
`b=(v>>1)&0x1F`, `a=v&1`, each channel expanded 5-bit→8-bit via
`(c<<3)|(c>>2)`), ranks candidates by average per-pixel neighbor-difference
("gradient" - lower means smoother/more image-like), and renders only the
top-N lowest-gradient candidates as PNGs. **Always still eyeball the
result** - the score is a stopgap heuristic, not ground truth (it correctly
picked the right dimension for every file checked *except* the 17,600-byte
class above, where it just picked the least-bad-looking noise).

**Not every file factors this cleanly, which is itself useful negative
evidence.** `assets01/0000.bin` (24,184 bytes → 12,092 pixels) and
`assets05/0005.bin` (2,056 bytes → 1,028 pixels) both have pixel counts with
a large prime factor (12,092 = 4×3023; 1,028 = 4×257) and thus **no
reasonable `w×h` factor pair in the `[4,256]` range at all** - a plain flat
RGBA5551 image can't have arbitrary-prime dimensions this large in a
console-era N64 game. Two live hypotheses, neither confirmed yet: (a) a small
fixed-size header (few bytes of width/height/format metadata) precedes the
raw pixel data, so the *true* pixel payload is `file_size - header_size`, not
the whole file - worth re-testing the failing files with a few small header
sizes (4, 8, 16 bytes) subtracted first; (b) these specific files are CI4/CI8
(palette-indexed, 1 or 0.5 bytes/pixel, not 2) rather than RGBA5551, which
would need a separate palette blob (still unlocated) to render correctly.

**Swept `assets01-assets05` the same way (2026-07-28) — negative result:
`assets00` is the outlier, not a representative sample.** Ran
`tools/render_rgba5551.py` (no-image-saved summary mode) over all 503
numbered files across the five remaining sections (183+145+77+59+39).
**176 of 503 (35%) have no valid `w×h` factor pair at all** in `[4,256]²`
at 2 bytes/pixel — far more than the two isolated examples noted above;
this is the norm for over a third of the remaining files, not an
exception. Checked whether a small fixed header (2-32 bytes) would fix
this for two representative failures (`assets01/0000.bin`,
`assets05/0005.bin`): their pixel counts (12,092 = 2²×3023; 1,028 =
2²×257) stay "prime-heavy" under every tested header size and under a
1-byte-per-pixel (CI8) or 4-bit (CI4) reinterpretation too — no header
size or bit-depth assumption makes either factor cleanly. This specific
header-subtraction test is also too weak a filter to trust on its own
(it "succeeds" for nearly any file once several header sizes and lenient
factor ranges are tried at once, confirmed by testing it against files
that already factor cleanly) — dropped as a dead end rather than reported
as a fix.

Of the **327 files that do factor cleanly, a visual sample across all
four sections checked (`assets01`, `assets02`, `assets03`, `assets04`)
rendered as the same sparse-colored-noise-on-transparent-background
pattern already identified for `assets00`'s 17,600-byte class** — not
coherent icons. This held even for files whose factor pair matched
`assets00`'s own *confirmed-good* widths (16/32/48/64): e.g.
`assets02/0002.bin` at 16×15 and `assets02/0008.bin` at 32×10 both render
as scattered noise, not clean shapes, despite the "right" width by
`assets00`'s own pattern. Also noticed some of the lowest-gradient
"winners" are actively misleading: `assets01/0011.bin` (120 bytes) decodes
at 12×5 with an artificially low gradient score because the raw bytes are
mostly zero with a handful of small integers (`0x04`, `0x0C`, `0x10`,
`0x48`, `0x4C`, `0x5C`, ...) that look far more like a small offset/count
table than pixel data — a near-constant "image" trivially scores well on
this gradient heuristic without being one. **The gradient-score method
needs a sparsity/density check added before trusting a "low gradient"
result** - it currently can't distinguish a genuine flat-color image
region from non-image data that happens to be mostly zero.

**Conclusion: `assets00`'s simple, uniform-per-file RGBA5551 encoding does
not generalize to `assets01-05`.** Whatever format the majority of these
five sections actually use — CI4/CI8 with a real (non-grayscale) palette,
a different bit-depth or channel layout, a real per-file header this
factor-pair search doesn't account for, or non-texture data entirely
mixed in among these sections — the exact-factor-pair-plus-gradient method
that worked for `assets00` cannot crack it, and applying more guesswork
here would just produce more false "confirmations" like the ones caught
above. No amount of further blind dimension-guessing across `assets01-05`
is likely to succeed where it already failed on a representative sample;
next steps need real metadata (loading code, a palette table, or a
documented header) rather than more heuristic sweeping.

Still needed:

- locate width, height, format, and palette metadata in the referencing tables
  or rendering code (the exact-factor-pair heuristic above is a workaround for
  *some* files, not a substitute for finding real per-file metadata - it
  cannot disambiguate two equally-clean-looking candidates without a human,
  and has now demonstrably failed outright for an entire size class, plus
  apparently the majority of `assets01-05`);
- crack the CI4/CI8-with-real-palette hypothesis specifically: find the
  in-game texture-loading code (likely near the `Gfx`/texture-tile setup in
  `conker/include/2.0L/PR/gbi.h` usage) or a palette table in the ROM, rather
  than continuing to guess bit depths against the raw asset bytes alone;
- explain the very small records (candidate non-image offset/count tables,
  see `assets01/0011.bin` above), the 901,040-byte `assets02` payload, and
  the ~35% of `assets01-05` files with no clean factor pair at any bit depth
  before labeling the full `assets00-assets05` range as uniformly textures —
  `assets00` itself may be the special case (a flat icon/sprite-strip pool),
  not representative of what the other five sections hold.

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

### 6a. Authored animation events: assets0F (Confirmed layout)

The original US loader `func_1503D660` loads section 0x0F, advances the
allocation by 0x10, and publishes that address in `D_800D1588[model]`.
`func_1503D484` walks eight-byte records until their first BE halfword is
999, then stores the record count in `D_800C5A90[model]`. At each record:

| Offset | Type | Meaning |
| --- | --- | --- |
| +0 | BE u16 | Internal animation index; 999 terminates the table. |
| +2 | BE u16 | Flags; individual bits not established in this audit. |
| +4 | BE u32 | Zero or event offset relative to allocation +0x10. |

`func_1503D438` relocates ordinary nonzero offsets; `func_1505E650` indexes
the records by eight bytes, and `func_1505E0C4` copies the record's event
pointer to actor+0x1C4. Events are 12-byte records: BE float frame, BE u32
command word (low byte selects the callback), BE u32 argument. Every
nonempty list in this archive terminates at frame 999.

The container has 187 actual rows, with 35 empty slots and 152 nonempty
payloads. All nonempty payloads parse with bounded reads and terminator
validation. Preserve empty slot numbering. Conker files 0 and 128 each
contain 857 animation records; their table sentinel is payload +0x1AD8.
Header word +0x0C is not the animation count. The remaining header
semantics are not fully established.

The three loader/relocator bodies (36/140/276 bytes) match the original
decompressed ROM bytes exactly. Thirteen retained native Training event
lists also match original file 0 bytes; this is data identity, not audio
playback or callback-execution proof. The authored command-0x0A inventory
has 33 events in 25 animation records, including aliases; some preceding
command-9 arguments deliberately lack the deferred-sound flag.

Evidence and reproducible local read-only parser:
[Note 308](../../64CBFDOGL/DOCS/WORKING_NOTES/308-rom-animation-event-inventory-and-audio-boundary-20260908.md).
No sound or dive correctness conclusion follows from an event list alone:
gameplay code can also call sound producers directly.

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
| assets00-05 | RGBA5551 visually confirmed for 3 sample files (§5); full per-file dimension/format inventory still open, some files don't factor as plain RGBA5551 | Partial |
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

The imported `tools/assetmgr/` generators and top-level `tools/mktextures`
must not be used to rebuild these assets. They expect a different Rare-game
schema and compression header (`0x1173` plus a three-byte size), not the
four-byte-size-header Rarezip format documented above. They are guarded and
reference-only; see [Project tools](TOOLS.md#reference-only-imported-asset-generators).
