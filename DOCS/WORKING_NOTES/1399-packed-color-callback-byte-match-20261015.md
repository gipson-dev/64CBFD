# Packed Color Callback Byte Match

Date: 2026-10-15. Continue the recovery in
[Note 1398](1398-packed-color-callback-semantic-recovery-20261015.md) and keep
the whole additional-source / Game objective open.

## Result

Replace `func_1516E8CC`'s zero-return placeholder with the complete semantic
packed-record intensity/extent/RGB callback. Preserve its address-based name
and add a measured comment. **All 248 linked words / 992 bytes match retail**
at VA `0x1516E8CC`, ROM `0x19BD7C`, in `generated_19A8B0.c`.

This is a **guarded match**, not a raw compiler match. Normal O2/g3 C emits
246 words: five initial register-allocation differences and no duplicate dead
return. Seven expected-word guards close that register lifetime and preserve
the original two-word unreachable return. Every floating-point word emits
directly from C; no FP instruction guard, fake volatile access, invented
instruction body or compiler-profile change is used. This replaces an
already-C-classified stub, so converted-function counts do not increase.

## Source And Guard Evidence

The discriminating source changes are: initialize the reused record/color
pointer before the fade accumulator; split the halfword load from its wrapping
extent addition; initialize phase from countdown before adjusting it; preserve
the initial ramp-index guard and do-loop; initialize the record/time cursor
before reading the ramp byte; and write the commutative RGB sums in the order
that emits retail's actual load/conversion sequence. Keep full live words
after byte stores, including the live-256/stored-zero completion case.

The raw body is SHA-256
`54a6c0585a754b466ed25df0c9f704eff49b1c7453f5ea9f2af686f37307e716`.
Guard its complete raw text and all ten relative relocations before applying:

| Raw Offset | Expected | Replacement | Insert After |
| --- | --- | --- | --- |
| 0xC0 | 90870026 | 90850026 | None |
| 0xCC | 24EC0008 | 24AC0008 | None |
| 0xD0 | 00EC082A | 00AC082A | None |
| 0xD8 | 00E01825 | 00A01825 | None |
| 0xDC | 00ED2821 | 00AD2821 | None |
| 0x3D0 | 03E00008 | 03E00008 | 00000000 |
| 0x3D4 | 00000000 | 03E00008 | 00000000 |

The first five words rename only the initial start value from A3 to A1;
the later threshold load defines A3 normally. The last two rows retain
`OR V0,zero,zero; JR RA; NOP; JR RA; NOP` at offsets `0x3CC..0x3DC`.
The reachable return's NOP delay slot remains intact. Static checks reject
any jump/branch into the added dead tail, and the real production padder
reports the complete 992-byte function extent. Do not discard the final
return as an implicit alignment allowance or claim it was emitted by raw C.

The preserved guard CSV prefix includes its existing mixed line endings.
Install the qualified structured CSV output without normalizing the old
15,196-line prefix; append exactly seven rows. All old guard bytes remain
unchanged. The existing duplicate-return preservation pattern is also used
by `func_1503EA54`; no shared padder change is required.

Three maintained complete forms across O2/g3, O2 and O1/g3 produce nine fresh
screen results. Selected O2/g3 and O2 are 246 words / seven positional
differences including the two absent tail words. O1/g3 is 293 / 289 and is
rejected. The earlier completion-else, double-return, integer-pointer and
register-formal probes do not produce a raw match; retain them only as
ignored exploratory evidence.

## Fresh Qualification

**All 14 installed checks pass in 36.799 seconds**:

- **3,072 cases** compare raw C, guarded C, retail and an independent model:
  all intensity bytes, countdown/word boundaries, wrapped extents, RGB/global
  aliases, access events and returns. Guarded private registers/FCSR match
  retail. The emitted function has no frame.
- **643 paired, fired guest-access faults** preserve the complete partial
  state, including registers, memory, events and the bounded FCSR model.
  This is emitted guest evidence, not portable C fault semantics.
- **1,024 further original-guest cases** drive actual freestanding native32
  C at O2 and O0, using SSE single precision and no contraction. Native cases
  use backed finite ramp starts 1 and 9. Guest cases additionally cover start
  zero when phase is below 255. Arbitrary table indices, out-of-range casts,
  full hardware FCSR behavior and gameplay acceptance are not claimed.
- Five compiled negatives fail: early byte truncation (7 cases), wrong fade
  speed (27), omitted height (247), wrong phase (160), swapped weights (87).
  Every mutant is rejected by the raw normalization fingerprint too.
- All **29 neighboring routines**, raw sizes/bytes, normalized pools and
  relative relocations remain fixed. Reject all 246 raw-word corruptions and
  all ten missing relocation sites.
- Three **independent original/selected text and data rebase pairs** match
  all 248 words across signed-low carry boundaries for the delta, threshold
  and RGB symbols. Correct the test fixture's initial contiguous-table
  assumption by backing each relocated table separately; do not relax the
  independent byte or runtime comparison.
- **256 actual updater/callback/cleanup cases**, table index zero, execute
  the real callback and cleanup: 254 stay active, two remove. Cover NULL and
  non-NULL bindings. Lower unlink/destructor providers remain modeled; no
  natural gameplay or complete heap-lifecycle claim is made.
- Verify all **52 scoped production inputs**, all 52 corrupted immutable
  predecessor captures, three exact successor inputs/captures, source-text
  and six physical corruption controls, and all **801 archive fingerprints**.

Reuse the existing MIPS, FP, native32, relocation, data-layout and image
parsers. Do not rerun unrelated unchanged suites by default: their previous
receipts are historical, not fresh checks in this note.

## Complete Linked Image

The installed **3,257,636-byte ELF** equals an independent prediction made
from the frozen predecessor and retail target bytes, with the target symbol
extent changed from 12 to 992. The first comparison also exposed **21 bytes**
of symbol/name-order serialization, which are modeled exactly, not masked.

The three adjacent global symbol/name slots change from
`D_8009CE70, D_800AAC80, D_800A1370` to
`D_800A1370, D_8009CE70, D_800AAC80`. Each name keeps its original value,
zero size, type/binding and section: D_8009CE70 remains in section 6 and the
other two remain absolute. Check the complete canonical symbol multiset,
the exact three-slot permutation and all 21 metadata bytes; reject altered
bindings, sizes, types, sections, names and unknown/already-serialized orders.
No broad metadata range is ignored and no program address changes.

There are **713 changed ELF bytes**: **692 target-slot/extent bytes** and the
**21 named metadata bytes**. Every other byte is fixed, including all other
code and **189,088 protected bytes / 720 data owners**. Of the 52 scoped
inputs, only ELF, owner and appended guard manifest change; 49 are fixed.
The progress CSV, shared headers, original assembly and table/config inputs
remain unchanged.

| Installed Input | SHA-256 |
| --- | --- |
| ELF | 66f7281e1f839b43c2987ed1fbca4e28a4044936b4544e3df1589023ba7741b3 |
| Owner | 1b4d3bb3ee8990540c119fd51a1145e93efe95eac53cfa588a93b646d5fe0b9d |
| Guards | 2b2d5139c4d138257f5e0c4ce2d169a2f248aa00d524261167fe8a38ccd9a978 |
| Unchanged progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |

Fresh official matcher: **Game 2,896/4,828 (59.98%)**, **total 3,569/5,501
(64.88%)**, **1,932 different**, zero drift. Init stays 492/492 and Debugger
181/181 exact. All converted counts/bytes are unchanged. Root README changes
only the two affected aggregate rows; detailed updates remain in DOCS.

## Banking And Next Work

Bank tools **8981c28** before the consumer source/guard/pin/docs. Shared tools
checks pass. Preserve older mirror ddbdd16 and all **654 initial dirty
fingerprints**, copying only five absent owned files for **659 final paths**;
native Windows syntax and its standalone ROM-free check pass. Never commit,
reset or copy history into that independently dirty mirror.

One focused packet-only Claude advisory ran with customizations and tools
disabled, without session persistence. Pointer reuse was a hypothesis to
test; literal duplicate C returns did not restore the tail, and an incorrect
claim about the supplied FP expression was not accepted. Codex owns all
edits, experiments, qualifications and integration. No software installation,
account-setting change, push or host/Release action was performed. Keep Release frozen.

Evidence lives in `conker/build/game-packed-color-match/` and
`conker/build/game-packed-color-control-fit/`. Reproduce with the new
`tools.tests.test_game_packed_color_match` and
`tools.tests.test_game_packed_color_match_installed` suites; the older
read-only Note 1398 screen is a predecessor, not the installed body.

Next recover **func_1516ED68**, **91 words / 364 bytes**, ROM `0x19C218`,
frame `0xD0`, in the same owner. It is a four-input actor-type-0x3A-gated
49-argument factory preset, not another record callback. Recover its packed
0x32C actor lookup, low-byte and full-word forwarding and complete packet
before matching. Keep the whole failed-comment/binding/unanchored queues in
[Note 1396](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md),
the inherited-stack renderer deferral and the broader Game objective open.
The previous 1,717-object audit is retained, not rerun here.

## Post-Bank Verification

Consumer **7c1c25ec** banks the semantic callback, seven guard rows, tools
**8981c28** pin, aggregate README rows and working docs. All **14 post-bank
checks pass in 68.595 seconds**, including full exact-image closure, all 52
expected live input states/capture controls, the exact symbol serialization
and fresh verification of all 801 archive files. The normal ELF/progress build
is up to date. Both active checkouts are clean before this receipt.

Preserve older mirror ddbdd16 and all **659 final fingerprints**, including
every one of the 654 initial inputs; do not copy history or commit that mirror.
Seven documents / **4,991 relative Markdown links** validate with no broken
target. The full graph scan refuses 19,387 nodes against 41,157 existing;
preserve its fail-closed result. The actual commit worker completes with
**41,166 nodes / 81,262 edges / 3,820 communities** without forcing a smaller
graph. No push or host/Release action. Keep the complete additional-source /
Game goal active, continuing at the 91-word func_1516ED68 preset.
