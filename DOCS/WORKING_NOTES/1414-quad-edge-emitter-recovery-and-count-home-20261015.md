# Quad Edge Emitter Recovery And Count Home

Date: 2026-10-15. Continue the additional-source / Game matching objective
from consumer **b4ed5d88**, tools **9bc6852**, both initially clean.
The previous turn made verified progress by installing 15170034 directly.
This checkpoint recovers the next routine's bounded complete packet behavior
and improves compiler shape; **151700D8 is not installed or byte-exact**.
Preserve the original archive, older dirty tools mirror and frozen host
Release. No push, host build/launch, dependency installation or Claude call.

## Steps

1. [x] Inspect all 266 original words, archival C, three copied tables and every aligned direct JAL in the prepared code image.
2. [x] Recover the ten-input mixed word/float ABI, four-edge interpolation and all 31 physical factory fields.
3. [x] Qualify public packet/mutation behavior, actual caller interfaces, factory/allocator effects and bounded native C.
4. [x] Restore the addressable count lifetime: 264 -> 266 words, 194 -> 149 differences, retaining the actual post-factory reload.
5. [x] Verify padding, neighbors, independent relocations, effective controls and all 62 immutable production inputs; reject premature installation.
6. [x] Bank tools first, preserve the older mirror, update working docs and keep official matching credit unchanged.
7. [ ] Recover frame 0x190, remaining homes/register/scheduling words and literal private/fault parity before C adoption.
8. [ ] Continue the complete additional-source repair/binding/unanchored and Game queues, retaining earlier inherited-stack deferrals.

## Target And Source

**func_151700D8**, VA **0x151700D8**, ROM **0x19D588**, is **266 words /
1,064 bytes**, frame **0x190**, RA saved at SP+0xDC. The owner is
[generated_19A8B0.c](../../conker/src/game/generated_19A8B0.c); its current
production body remains the unchanged zero-return placeholder.

The archive is a semantic lead, not a byte-exact donor. Correct the inferred
64-word integer range array, integer vertex loads, scaled typed-pointer
arithmetic and unaligned halfword color reads. Retain retail's initial
12-byte table copy even though this routine never subsequently reads it.

| Table | Original Copy | Contents / Use |
| --- | --- | --- |
| D_8008CBF4 | SP+0x12C, 12 bytes | Float words 143, 30, 30; copied but not used later |
| D_8008CC00 | SP+0x120, 12 bytes | Float words 571, 130, 130; initial lifetime range |
| D_8008CC0C | SP+0x114, 9 bytes | RGB triples 134/106/60, 200/190/180, 255/210/128 |

The ten inputs are vertex pointer, X origin, Z origin, low-byte **preset**,
float scale, palette/range index, X-edge count, Z-edge count, low-byte flag
and full context. The fourth input is not a color mode: factory field 19
becomes record byte **0x2C**, which **func_1516F024** uses to select its
scale/growth/limit/fade tables. Keep the address-based function name and a
short comment describing the perimeter emission, not an invented retail name.

Snapshot scale at entry. Snapshot the initial range and copied tables.
For edges 0/2 select X count; edges 1/3 select Z count. The current vertex
cursor advances by 12 bytes; the next vertex wraps from 3 to 0. Incoming
vertex-base, origins, palette index and edge counts remain live at the
corresponding outer-edge loads. Preset is sampled per active edge, while
flag/context are reloaded per factory call. These home mutations are guest
diagnostics, not portable C argument mutation.

Compute each edge's X/Z midpoint deltas with ordered binary32 operations,
double and truncate them, then split their low 16 bits into high/low bytes.
For a positive count use reciprocal **1/(count-1)** and interpolate each
coordinate at **index*reciprocal**, including both endpoints. Read vertices
again for each particle. Each particle makes exactly three independent RNG
calls followed by the factory call.

## Complete Physical Packet

Start all 31 words at zero, then set the following fields. TRUNC denotes
the original signed-word floating conversion; the native domain below is
separately bounded.

| Fields | Value |
| --- | --- |
| 0, 1, 2 | Signed low halves of TRUNC(interpolated X/Y/Z) |
| 3 | 13 |
| 5, 6, 7 | Three copied RGB bytes for the selected palette |
| 12 | 2, the callback-table slot |
| 13, 14, 15, 16 | X high/low and Z high/low midpoint bytes |
| 19 | Per-edge preset byte |
| 23, 24 | Signed low half of RNG1 % U32(TRUNC(836*scale)) + TRUNC(D_800A6E84*scale) |
| 25 | (RNG0 & 31) + 15 |
| 26 | Full word RNG2 % U32(initial range) + TRUNC(143*scale) |
| 29, 30 | Live low flag byte / full context |

D_800A6E84 is the live float **731** in the retail data. Its product is
snapshotted per active edge; a provider write affects subsequent edges,
not particles already on the current edge. Do not substitute the unused
143/30/30 table for this value. Preserve unsigned remainders, first-table
entry timing, byte colors, paired signed-half extents and full physical
field 26. Native capture uses the actual factory prototype and therefore
projects field 26 to s16 at that C boundary; it is not a claim that the
original caller narrows its stored word.

## Compiler Progress

The first typed complete body emits **259 words / frame 0x178 / 233
length-inclusive differences**. Recovering the original branch/address and
vertex-temporary shapes gives **264 / 0x1A0 / 194** without diagnostics.

Using indexed reads of the initialized local count, `(&count)[0]`, restores
its post-factory reload and frees the original saved-register role. The
selected body now emits **266 words / frame 0x1A0 / 149 differences**.
It has no data/rodata pool, artificial volatility or new word guards. The
actual production padder retains all 266 words unchanged; padding is not
the remaining problem. The strict word/frame/diagnostic/pool gate rejects
installation. All 29 copied-owner neighbors, relative relocations and
normalized pools stay fixed.

An effective private probe changes the active count from 2 to 3 after the
first factory call. Original and selected code emit **nine packets**, keeping
the old reciprocal; the cached-count control emits **eight**. The original
count home is SP+**0x138**, the candidate SP+**0x194**. Those are not equal
private addresses, and the frame remains 16 bytes too large.

Fresh table/assignment and local-lifetime screens:

| Form | Words | Frame | Differences | Literal Pool |
| --- | ---: | --- | ---: | ---: |
| Selected / addressed count | 266 | 0x1A0 | 149 | 0 |
| Explicit struct assignments | 266 | 0x1A0 | 149 | 0 |
| Mutable literal tables | 266 | 0x1A0 | 149 | 48 data bytes |
| Const literal tables | 266 | 0x1A0 | 149 | 48 rodata bytes |
| Reading initial[0] instead of literal 143 | 264 | 0x1A0 | 209 | 48 data bytes |
| Plain cached count | 264 | 0x1A0 | 194 | 0 |
| Inline invariants | 264 | 0x198 | 194 | 0 |
| Addressed edge only | 264 | 0x1A0 | 195 | 0 |
| Inline invariants plus addressed edge/count | 266 | 0x198 | 152 | 0 |

These are measurements, not accepted alternatives. Literal pools are linked
at the actual table anchor for comparison, but no Makefile/data binding is
installed. A smaller frame alone is not a matching improvement. The final
preset rename retains complete owner text/functions/relocations/pools.
It is a naming correction, not additional matching credit.

## Qualification And Limits

All **12 focused checks pass in 64.212 seconds**, exit 0, after the naming
correction. The preceding same-code run passed in 54.980 seconds.

- **2,304 paired cases** cover all four edges, complete 31-word packets, three palettes, empty/negative/singleton/ordinary counts, four scales, full-word RNG values, two stack phases and four provider modes. Every non-BREAK retail word executes. All 2,304 available private states still differ, so public agreement is not a literal match.
- **Native32 O2/O0: 3,600 cases each**, with undefined-behavior traps for selected C. Check the actual typed factory projection, all fields, call order, live vertices/global scale and six effective native negatives. Native scope is palette indices 0..2, finite in-range conversions, nonzero divisors and counts <=0 or >=2. Singleton interpolation/invalid floating conversions and zero divisors are guest-only; unchecked out-of-range palette indices are not claimed as valid C inputs. No FCSR/hardware parity claim.
- **Nine effective compiled guest negatives**, including the archive's integer-bit table/vertex interpretations and unaligned wide color loads; six are also controlled native failures. The private cached-count control is independently effective.
- **Eight trap/empty cases** distinguish the two BREAK-7 paths: scale zero gives a zero width after RNG1; scale 0.001 gives a nonzero width but zero initial range after RNG2. Empty edges skip RNG and integer division.
- **2,848 fired memory cuts** include **1,396 paired cuts**, all privately divergent, plus **56 retail-only cuts**. Respect different access counts instead of inventing paired faults after the candidate has returned.
- **18 connected original/C pairs** execute the current retail-exact **100-word factory / 28-word allocator**, verify every packed record field and allocation failures. Include allocator context/flag stores at record+1/+0xC. Heap/registration remain declared opaque providers; the emitter is staged, not installed.
- **Three independent original/C links**, with **36 public pairs**, retain the original 266-word anchor and all four calls/four data HI/LO pairs. Rebase the table across a signed-low boundary. The C remains nonmatching under these independent links.
- All **801 original archive fingerprints** freshly agree. This is not a fresh whole-source 1,717-object compile audit or new raw donor.
- All **62 production inputs** remain byte-for-byte fixed, including the complete ELF, source owner, guards, profiles, headers, conversion rows and caller/data sources. Reject all 62 frozen-before flips, a changed manifest and an unknown placeholder.

## Callers And Banking

The prepared code image has exactly three aligned direct JALs: ROM
**0x9B730**, **0x9B8D8**, **0x19ED88**. Original call windows in
func_1506E0EC and func_1506E2CC pass kind 0, counts 4/4, flags 255,
context zero, presets 4/5 and respectively full/half actor scale. Six bounded
window cases pass. The complete **61-word func_151717FC** wrapper builds a
four-point quad from signed record coordinates and 13 incoming arguments,
then forwards all ten emitter inputs. Its quad begins at **wrapper incoming
SP-0x30**, after accounting for the 0x80 frame. Current caller placeholders
are not restored or claimed byte-exact by these original-code probes.

Tools **90506d1** banks the recovery; **b7c245a** corrects preset naming from
the actual callback use. Preserve all **710 initial older-mirror fingerprints**,
HEAD ddbdd16, and two hash-equal owned copies: **712 final dirty paths**.
Windows syntax checks pass in both copies, all 11 shared WSL padder checks
pass in both copies, and `make tools-check` passes. No push or host action.

Fresh official totals remain **Game 2,906/4,828 (60.19%)**, **total
3,579/5,501 (65.06%)**, different **1,922**, drift **0**. Init stays 492/492
and Debugger 181/181 exact. Conversion rows/bytes and root README figures
are unchanged. No production C edit, rebuild or matching credit is claimed.

Reproduce in the prepared consumer WSL checkout:

```sh
python3 -m tools.experiments.game_quad_edge_emitter
python3 -m tools.experiments.game_quad_edge_emitter --screen
python3 -m tools.experiments.game_quad_edge_emitter --lifetimes
python3 -m unittest tools.tests.test_game_quad_edge_emitter -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

## Next Action

Continue **151700D8**, not 15170500 yet. Recover the named-local/temporary
frame boundary and table homes first, retaining the proven addressable count.
Original table homes are 0x12C/0x120/0x114; the selected copies are
0x188/0x17C/0x170 in frame 0x1A0. Saved-register slots already have the
original relative offsets, but their absolute addresses differ with the frame.
Resolve the remaining register/operand/load schedules with measured C shapes
or the existing bounded compiler observer, then repeat complete private/fault,
ABI/padding/rebase and independent linked-image gates before adoption.
Do not replace all 149 words with an unproved normalization, add fake padding
locals, narrow field 26 early or silently zero a singular path.

Keep the [additional-source queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md),
[FE1C inherited-stack boundary](1413-paired-overlay-stack-contract-and-random-direction-match-20261015.md)
and [renderer deferral](1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md)
open. This checkpoint is concrete recovery progress, not completion of the
persistent whole-source / Game objective.
