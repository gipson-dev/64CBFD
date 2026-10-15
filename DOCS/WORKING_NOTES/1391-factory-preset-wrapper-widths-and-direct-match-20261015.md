# Factory Preset Wrapper Widths And Direct Match

Verified 2026-10-15. Continue the whole additional-C / Game goal; this is one
qualified wrapper, not completion of its factory or gameplay.

## Target And Source Evidence

| Item | Value |
| --- | --- |
| Function / owner | func_1516F1C0 / generated_19A8B0 |
| VA / ROM | 0x1516F1C0 / 0x19C670 |
| Complete retail slot | 78 words / 312 bytes |
| Frame / factory | 0xD0 / func_1516D99C |
| Consumer / tools predecessor | 5d86f92a / 18698b3 |
| Profile | Existing O2/g3, no change |

The archive body in `game/game_19A8B0.c` supplies the semantic 49-argument
preset-0x2D call. Freshly compile it in the complete current owner: 78 words,
two real differences, no diagnostics. Retail loads arg0 and arg1 as full
words; the archive incorrectly narrows them to u8 and u16. Remove only those
two narrowings. Retail explicitly loads arg2 with LBU; retain its u8 cast.
Arg3 also stays full-width and is written in the call delay slot.

Install the corrected void wrapper, preserving its address-based name rather
than inventing unproven field roles. Add a succinct width/preset comment.
No shared declarations, factory body/signature, guards, data, assembly,
compiler profile, linker layout or other source function changes.
The factory remains a zero-return placeholder. This wrapper's exact call
interface does not make that callee or gameplay functional.

## Fresh Qualification

Run `python3 -m tools.experiments.game_factory_preset_wrapper`, then the three
`test_game_factory_preset_wrapper`, `_candidates` and `_installed` modules.
All **13 focused checks pass in 29.641 seconds** after the normal build.

- All 78 raw words equal retail, with no extra/omitted padding words. The
  actual generated-owner padder independently preserves the exact slot.
- All 29 copied-owner neighbors retain raw bytes, extents, relative relocation
  ownership and normalized pools. Existing neighbor guards remain unchanged.
- 786 guest cases cover high bits/sign boundaries, both stack phases, the
  independent 49-word expected packet, all incoming homes, the 208-byte frame,
  saved RA/register lifetimes, and the final argument's call-delay store.
- Opaque-provider cases clobber caller-saved registers and outgoing/incoming
  homes, and produce externally visible effects. They do not model a recovered
  factory. The guest model is bounded low-word execution, not N64 hardware.
- 110 paired, fired guest memory-access fault prefixes agree. This qualifies
  emitted guest order, not portable C fault semantics.
- Actual selected C passes **65,536 native32 cases per O2/O0 profile**. Five
  compiled negatives fail in both guest and native fixtures: narrow arg0,
  narrow arg1, widen arg2, wrong preset and wrong final argument. Each negative
  remains 78 words but differs from retail in one word and changes the packet.
- Independently assemble the complete original routine and compare three
  independent text/callee rebase pairs, then execute each rebased packet.

Two initial failures were test-fixture issues, not production regressions:
the intentional wrong-final-argument control leaves arg3 unused; allow that
warning in native fixtures. A corruption probe initially addressed BSS as
file-backed bytes; use an actual protected constant instead. Both corrected
fixtures run successfully in the complete 13-check suite.

## Linked Image And Progress

Normal `make -C conker -j4 build/conker.us.elf progress.csv` succeeds. Build the
entire expected ELF independently from the pinned predecessor, the 312 retail
bytes and only the function symbol's `12 -> 312` extent. The installed ELF is
identical: **233 changed bytes**, all target slot/extent, zero metadata
allowances. Every other ELF byte and all **189,088 protected bytes / 720
owners** remain fixed. Known duplicate generated_12D630 recipe warnings remain.

| Input | SHA-256 |
| --- | --- |
| ELF | 0ec266dba69999d339a38627660ad721f6d52acd2f3a8d58ed71cd6949956918 |
| Owner | 34978246da6af69450cb5a28a5bb064e82115169f438ef6105d36bda07e146fc |
| Unchanged progress CSV | 595443d0129e7d6ccd1f824b050854d5759c0f45c1af5b0818ef7cde682528ee |
| Unchanged guards | 311c81d50de789b4a51e3d27ac3ad2d0e0aabb9b07393ce004d34fdd1c822af2 |

Check all **41 input paths**: two deliberate changes, 39 unchanged. Effective
corruption controls alter every input, source text and five real in-file
code/symbol/data locations. Exact-input successor fixtures reject unknown or
corrupt inputs and captures. Current image/function checks use no inverse.
Prior unchanged broad neighbor suites are not rerun or reported as fresh.
All **801 original archive fingerprints** are checked freshly and unchanged.

Fresh `match-progress NON_MATCHING=1`: Game **2,890/4,828 (59.86%)**, total
**3,563/5,501 (64.77%)**, different **1,938**, zero address drift. Init remains
492/492 and Debugger 181/181 exact. Converted total stays **5,501/6,044
(91.02%), bytes 86.04%**; Game **4,828/5,323 (90.70%), bytes 85.41%**.
The target was already counted C, so this adds one exact C body, not another
conversion. Generated progress CSV stays ignored and is not force-added.
Root README changes only the two affected aggregate rows.

## Banking And Continuation

Bank tools **f0e67c2** before the consumer pin/source/docs. Shared tools checks,
standalone syntax for five files and all three ROM-free tests pass. Preserve
the independent older-mirror HEAD `ddbdd16` and all **618 initial dirty-file
fingerprints** before/after copying only five absent owned files. All **623
final fingerprints** remain verified; no mirror commit/reset or history copy.
No push, host source/build/launch, save/configuration or frozen Release action.
Claude calls: zero. Ignored receipts remain under
`conker/build/game-factory-preset-wrapper/`.

Seven documents / 4,936 relative Markdown links validate with zero broken.
The full Graphify update refuses 19,296 nodes against 41,077 curated nodes,
retaining 19,398 nodes from 2,972 excluded-but-present files. Preserve that
fail-closed result; use the incremental commit worker without forcing a scan.

Next inspect the still-stubbed **func_1516D99C**, the actual factory used here.
Its retail slot is 125 words. The older isolated archive screen emits 158
words with 140 real differences, so it is a reference lead, not qualified C.
Recover its real allocation/field-store ABI and independently qualify its
complete owner before installation. Other additional-source/binding failures,
handwritten Init hardware routines and func_1510BF60 remain open.

## Post-Bank Verification

Consumer **63f5eaf7** banks the wrapper, tools f0e67c2 pin, aggregate README
rows and working documentation. All **13 post-bank checks pass in 29.006
seconds**, including the independent complete image, 41 installed input states
and fresh 801-file archive audit. The normal ELF/progress build is up to date.

Both active checkouts are clean before this receipt. The older mirror retains
its independent ddbdd16 HEAD and all 623 final fingerprints, including the
618 initial fingerprints; all five owned copies remain exact. The source
commit's incremental graph worker completes at **41,085 nodes / 81,179 edges /
4,099 communities**, without forcing the refused smaller full scan. No push,
host/Release operation or claim that the factory is recovered. Continue the
whole additional-C / Game goal at func_1516D99C.
