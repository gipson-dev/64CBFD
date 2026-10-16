# Quad Edge Emitter Named Frame And Home Recovery

Date: 2026-10-15. Continue **func_151700D8** from consumer **3dfa6f97**,
tools **b7c245a**, both initially clean. This checkpoint recovers the retail
frame and five named homes, but **does not install or credit the C body**.
The wider additional-source / Game objective remains unfinished. Preserve
the older dirty tools mirror and frozen host Release; no push or host action.

## Steps

1. [x] Observe complete fingerprint-locked CFE, UOPT and UGEN runs without modifying the compiler or emitted code.
2. [x] Recover the 0x190 frame through meaningful scalar lifetimes and declarations, with no fake padding, volatility or word guards.
3. [x] Recover all three initializer homes, the initial range limit and live post-factory count home.
4. [x] Reject recomputed-reciprocal and cached-count regressions through effective private count-home probes.
5. [x] Pass 13 focused checks, real padding, independent links, current factory/allocator effects and all 62 immutable production-input checks.
6. [x] Bank tools first, preserve all older-mirror fingerprints and keep official totals / README unchanged.
7. [ ] Recover the remaining loop-state/preset homes, register allocation and schedules; prove literal private/fault parity before adoption.
8. [ ] Continue all additional-source repair/binding/unanchored, caller and inherited-stack queues after this target.

## Target And Observation

**func_151700D8**, VA **0x151700D8**, ROM **0x19D588**, occupies **266 words /
1,064 bytes** in [generated_19A8B0.c](../../conker/src/game/generated_19A8B0.c).
Its production body remains the zero-return placeholder. The complete
semantic contract and actual caller boundaries remain in
[Note 1414](1414-quad-edge-emitter-recovery-and-count-home-20261015.md).

New tooling:
[frame experiment](../../tools/experiments/game_quad_edge_frame.py) and
[focused qualification](../../tools/tests/test_game_quad_edge_frame.py).
Reuse the existing compiler observer, binary parser, IDO owner builder,
MIPS/native32 oracles and relocation/padder gates; no new compiler or library.

The observation wrapper requires an owned output below `conker/build`, a
simple label, the prepared cc/cfe/uopt/ugen fingerprints, fired frame/input
captures and every producer/consumer/driver exit 0. Isolated target bytes
and relative relocations must equal the complete owner, and tracing must
preserve text/functions/relocations/pools. Normal and traced object files
differ only in `.mdebug`, not generated code. Missing gates, damaged captures,
changed compiler fingerprints and escaping output paths are rejected.

| Quantity | Previous Selected C | Named-Home Candidate |
| --- | ---: | ---: |
| CFE named M reservation | 156 bytes | 140 bytes |
| UOPT M reservation / final local area | 192 bytes | 176 bytes |
| Saved-register area | 96 bytes | 96 bytes |
| Outgoing argument area | 128 bytes | 128 bytes |
| Observed UGEN temporary allocation | 0 bytes | 0 bytes |
| Final frame | 416 / 0x1A0 | 400 / 0x190 |
| Words | 266 | 266 |
| Retail word differences | 149 | 137 |

Frame events are exactly **0 -> 96 -> 224 -> final frame** for both bodies;
the temporary pool remains empty. UOPT adds 36 bytes in both cases. Thus
the measured 16-byte excess was upstream named-local allocation, not a
hidden UGEN spill. The corrected frame is a C-shape result, not a binary patch.

## C Shapes And Homes

Inline pure width/lifetime expressions and the interpolation fraction, and
use the current X coordinate directly before any opaque call. Retain the
reciprocal in a separate per-edge snapshot and retain `(&count)[0]` reads.
Reorder only the existing scalar declarations and the unchanged initializer
copies. The declaration-order helper rejects missing, duplicate or unknown
locals. No artificial locals or new ABI inputs are introduced.

| Home | Retail | Named-Home Candidate |
| --- | --- | --- |
| First, unused 12-byte initializer | SP+0x12C | SP+0x12C |
| Three float lifetime ranges | SP+0x120 | SP+0x120 |
| Nine copied RGB bytes | SP+0x114 | SP+0x114 |
| Initial scaled lifetime range limit | SP+0x150 | SP+0x150 |
| Live count, including after factory | SP+0x138 | SP+0x138 |

The original first table remains copied even though this routine does not
read it again. Do not confuse corrected named homes with complete stack
parity. In particular the candidate's next-edge home is still **SP+0x108**
instead of **SP+0x104**, and its per-edge preset save is **SP+0xE0** instead
of **SP+0xF4**. The original current-edge register is a1 with its inner-loop
SP+0x18C lifetime; the candidate uses v1 and lacks that same inner reload/save.
Register, operand and load schedules remain different.

| Screen | Words | Frame | Differences |
| --- | ---: | --- | ---: |
| Historical selected | 266 | 0x1A0 | 149 |
| Inline width/lifetime/reciprocal | 266 | 0x198 | 166 |
| Also inline fraction | 266 | 0x190 | 158 |
| Instead inline current X | 266 | 0x190 | 158 |
| Restore reciprocal snapshot, inline fraction/current X | 266 | 0x190 | 141 |
| Reorder actual named homes | 266 | 0x190 | 137 |
| Also address current edge | 266 | 0x190 | 139 |
| Advance edge directly, remove next-edge scalar | 264 | 0x198 | 203 |
| Keep named integer width/lifetime, inline Y/Z starts | 266 | 0x190 | 140 |

All screens have no diagnostics or literal pools. These are discriminating
measurements, not accepted replacements. The first three inline forms
recompute the reciprocal from a mutated count and fail the private snapshot
control. The advancing-edge / integer-snapshot alternatives are screens only,
not separately fully qualified or installed.

The effective count probe changes count **2 -> 3 after the first factory**.
Original and the named-home candidate use the same **0x138** home and emit
the same **nine packets**, including the third extrapolated position using
the old reciprocal. The cached-count control emits eight. The recomputed
reciprocal control emits nine but wrong positions; packet count alone would
miss this regression. These are guest stack diagnostics, not portable C
mutation of a local through an unexposed pointer.

## Fresh Qualification

All **13 focused checks pass in 79.083 seconds**, exit 0:

- **2,304 complete public packet/mutation pairs**, all 31 fields, four edges, three palettes, empty/negative/singleton/ordinary counts, four scales, full-word RNG values, two stack phases and four provider modes. Every non-BREAK original word executes. All 2,304 complete private states still differ.
- **Native32 O2 and O0: 3,600 cases each**, selected C under UBSan traps. All six native negative controls fail effectively; all nine compiled guest semantic negatives remain effective.
- **2,848 fired memory prefixes**: 1,396 paired, of which **1,276 differ privately** and 120 agree; 56 retail-only, zero candidate-only. This is an improvement over all paired prefixes differing in Note 1414, not literal fault equivalence.
- Both BREAK-7 cases and empty-edge behavior remain qualified. Singular interpolation/invalid conversions and zero divisors remain guest-only, not valid native C or FCSR/hardware parity claims.
- **18 current factory/allocator pairs** execute the installed 100-word factory and 28-word allocator, including every packed record field and allocation failure; lower heap/registration remain opaque.
- Six original caller-window cases and the complete original 61-word wrapper retain the ten-input ABI. Current caller placeholders are not claimed restored.
- **Three independent original/C links / 36 public pairs**, including table rebases across the signed-low boundary, retain the actual call/data relocation bindings.
- All **801 archive fingerprints**, all **62 frozen/current production inputs**, manifest/capture corruption controls and unknown-placeholder rejection pass. This does not repeat the historical whole-source compile audit or discover a new raw donor.
- All **29 copied-owner neighbors**, relative relocations and normalized pools stay fixed. The actual production padder retains the entire 266-word candidate unchanged. The strict installation gate still rejects its **137** differences.

Native scope remains palette indices 0..2, finite in-range float-to-word
conversions, nonzero divisors and counts <=0 or >=2. Physical factory field
26 stays full-word in the caller; native capture uses the real narrowed
factory formal. Do not claim invalid palette inputs, singleton floating
conversion, whole-image adoption or natural gameplay acceptance.

## Banking And Official Status

Tools **55cd830** banks the two new files first. Preserve all **712 initial
older-mirror fingerprints**, HEAD **ddbdd16**, and add only two absent,
hash-equal owned copies: **714 final dirty paths**. Windows syntax checks
pass for both copies. The 11 shared WSL padder tests pass in each checkout,
and `make tools-check` passes. No push or host/Release operation.

A fresh `make -C conker match-progress NON_MATCHING=1` reports **Game
2,906/4,828 (60.19%)**, **total 3,579/5,501 (65.06%)**, **1,922 different**,
**zero address drift**. Init is 492/492 and Debugger 181/181 byte-exact.
Conversion rows and root README aggregates remain unchanged. All 62
production fingerprints, including the complete ELF and owner, are fixed;
no production source edit or rebuild is needed or claimed.
Eight working/index documents resolve **5,093 relative inline links**, zero
broken. The complete ELF remains SHA-256
`f4f81f08c61c5592053d8faecc3a5699eb907b5d748c04a0af38e1b4cc2fafc2`;
the owner remains
`157edad8ef697e76e55171685be5b34562d9e349de38095d8a718b5201a0a2d8`.

```sh
python3 -m tools.experiments.game_quad_edge_frame --screen
python3 -m tools.experiments.game_quad_edge_frame --label named-homes
python3 -m unittest tools.tests.test_game_quad_edge_frame -v
python3 -m unittest tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

## Next Action

Continue this **266-word function**, not 15170500 yet. Start from the fully
qualified `named-homes` body and the two captured compiler stages in
`conker/build/game-quad-edge-frame/{selected,named-homes}/`. The first
remaining real divergence is the current-edge register at offset **0xA0**;
the outer branch region then has an extra transfer and different next-edge
home. Recover the original edge a1 / SP+0x18C lifetime and next-edge 0x104
home without fake argument uses, meaningless reads, guards or padding.
Then recover preset home 0xF4 and reciprocal/interpolation schedules,
preserving per-edge snapshot and post-factory count semantics.

Repeat complete private/fault, owner/padding/rebase and independent linked
image gates before any production adoption. Keep the
[additional-source queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md),
[FE1C inherited-stack boundary](1413-paired-overlay-stack-contract-and-random-direction-match-20261015.md)
and [renderer deferral](1395-packed-fade-scale-callback-and-renderer-deferral-20261015.md)
open. Neither a correct frame nor a matching count home finishes this
function or the wider objective.
