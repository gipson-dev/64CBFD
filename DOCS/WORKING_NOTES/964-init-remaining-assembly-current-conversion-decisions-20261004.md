# Init Remaining Assembly: Current Conversion Decisions

Date: 2026-10-04. Starting HEAD: `d13d95be`.

## Answer

**Some remaining Init assembly can be represented in C, but none is currently
ready for production conversion.** Retain the exact baseline while addressing
specific fitting, calling-interface and provenance gates. This refresh answers
the request to resume and determine what remaining Init assembly can convert.
It follows [Note 958](958-init-resume-remaining-assembly-readiness-20261004.md)
and the rejected fitting experiments in
[Note 959](959-init-decoder-packed-parent-and-bit-tail-fitting-trials-20261004.md).

The fresh production link still reports **492 / 539 C functions (91.28%)**,
**151796 / 164048 C bytes (92.53%)**, leaving **47 assembly entries / 12252 bytes**.
The complete Init code/data is retail-exact, including every retained ASM slot.
This is not evidence that every assembly routine should become C.

| Remaining group | Functions / bytes | Decision and current gate |
| --- | ---: | --- |
| Bitmap `func_10005BE0` | 1 / 76 | Best small compiler-shape target; nineteen-word full match still missing |
| MMIO `func_100038E0` | 1 / 44 | C-expressible ordered volatile accesses; full eleven-word match still missing |
| Connected decoder `func_10006240`..`func_1000709C` | 10 / 3984 | Semantic C exists; best executable remains 4512 bytes, 528 over, with stack/entry ownership unresolved |
| Cleanup/diagnostic/glyph path | 5 / 1308 | Partial C exists; best connected formatter is 608 versus 412 bytes, 196 over; caller/interior entry and placement unresolved |
| Boot/hardware/context/SDK | 30 / 6840 | Retain proven original assembly and machine/register interfaces |
| Total | 47 / 12252 | Seventeen investigation targets, not seventeen approved conversions |

The complete function-by-function map remains
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md).
Some retained SDK algorithms are C-expressible; retention reflects provenance
and actual machine interfaces, not mathematical impossibility.

## Fresh Evidence

**102 focused tests pass in 64.464 seconds, no skips.** They freshly compile
retained bitmap and connected formatter controls plus both decoder profiles,
reassemble the MMIO owner, and check all retained ASM ownership and raw slots.
The separate Game checkpoint in
[Note 963](963-game-asset-table-cache-lookup-and-block-load-recovery-20261004.md)
contains the production relink; this Init assessment adds no production owner
changes or new compiler hypotheses.

The current right-shift/value bitmap candidate is twenty optimized words,
one over nineteen. Address-difference remains twenty-two; equality-exit forms
remain twenty-one. Older nineteen-word candidates fit but are non-matching;
their old compilation results were not rerun. The fresh model tests preserve
captured endpoints, inclusive filling, post-fill signed count reloads, aliases
and bounded reversed-range behavior. Fitting, behavioral qualification and
byte matching remain distinct requirements.

MMIO is freshly reassembled and its ordered store contract rechecked:
word `0xBC000C02` to `0x80038070`, halfword `0x4040` to `0x80038074`, then
halfword `0x4040` to `0xBC000C02`. The old eleven-word O1 C trial still lacks a
complete match; its C matrix was not rerun. No extra global reads or invented
return contract may be added merely to force compiler register choices.

Decoder fresh optimized C text is 4336 bytes plus the actual 176-byte adapter:
4512 executable bytes. O1 is 5808 plus 176 = 5984. Adapter cost must remain in
the total. Ten entries share registers and inherited stack state; converting
them as ordinary independent C helpers is not safe. Neither full 507-page
guarded CU1 corpus was rerun in this refresh. Note 959's new packing and bit-tail
shapes already regress size; repeating them unchanged is not a new reduction.

Formatter fresh separate/shared/split controls remain 624/608/624 bytes and
48/80/64-byte stack descent against 412 connected retail bytes. The glyph
writer fits twenty-nine words in thirty, but its caller/adapter path does not.
Experimental placement at `0x10009000` overlaps existing `func_10008F90`;
fitting a leaf does not resolve ownership of its complete calling path.

Raw linked section verification after the production relink:

| Section | Bytes / owners | Raw differences | SHA-256 |
| --- | ---: | ---: | --- |
| Init code | 164048 | 0 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| Init data | 17376 | 0 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |
| Game data | 189088 / 720 | 0 | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

The focused command is Note 958's first command plus
`tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction`
in one invocation. Bounded compiler/model tests do not prove hardware or gameplay.

## Where To Pick Up

1. Start with bitmap `func_10005BE0` only after identifying a new compiler-shape
   hypothesis for the direct endpoint branch and increment delay slot. Preserve
   captured endpoints, alias timing and the late signed count read; require all
   nineteen retail words before changing the owner.
2. Keep MMIO second. A justified address-lifetime/scheduling hypothesis must
   retain all three stores, widths and order and match the complete eleven-word
   slot. Repeating the old published-address trial is not an adoption candidate.
3. For sustained connected work, reduce the existing decoder by at least 528
   executable bytes without moving costs into uncounted wrappers. Then resolve
   private-stack reservation and entry/frame ownership and rerun both full
   guarded CU1 corpora before production placement.
4. Treat glyph/formatter recovery as a separate connected project. Close its
   196-byte fitting gap plus interior-entry, caller-stack and placement gates.
5. Adopt only a fully qualified owner, relink and regenerate counts, and verify
   neighbors plus complete Init code/data and Game data against retail.

- [x] Recount all remaining assembly and verify every owner/raw slot.
- [x] Freshly recheck retained fitting and behavioral controls, no skips.
- [x] Preserve the full retail-exact Init baseline after production relink.
- [x] Separate C-expressible candidates from approved conversion and intentional ASM.
- [ ] Qualify a complete new small-leaf replacement before adoption.
- [ ] Resolve connected fitting, stack/entry ownership and corpus gates.

No new Init conversion, word guard, profile override or README aggregate change.
No broad conversion batch is justified. No sibling source/build, frozen Release,
save, ROM promotion, hardware/gameplay acceptance or push is included.
