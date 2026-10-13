# Game Rectangle Bounds Predicate Direct Match - 2026-10-12

## Scope And Recovery

Continue the full Game matching goal from consumer `c82455a1` / tools
`ec4865d` and [Note 1315](1315-game-event-record-constructor-direct-match-20261012.md).
Both active repositories were clean. Query the local graph, inspect the complete
retail routine, its actual caller and the existing owner/profile before editing.
Preserve the open text218/114/cut27 and translator49/34 boundaries.

Target `func_1501AE94` in [game_476D0.c](../../conker/src/game_476D0.c:140):
VA0x1501AE94..0x1501AF44, ROM0x48344..0x483F4, 44 words /176 bytes/frame0.
The three-word zero-return C placeholder had37 real differences. The recovered
body and local signed32 argument declaration emit all44 words directly under
unchanged O2/g3/MIPS2, no guard, pool, header/profile/Makefile change.

The first width-height-record source form is byte-exact. An unsigned index
expression emits the same words, preserving MIPS low32 offset arithmetic.
Record-first/width-record-height controls retain44 words but differ10/9;
inline-height and inline-limits expand45/47 and are rejected. No broad source
sweep, physical register binding or invented struct fields are used. The shared
0x180 record type leaves these early fields opaque, so keep a byte/float view.

## Contract

- Input is a signed32 record index, not a narrowed byte. Compute the low32
  index*0x180 offset through D_800BE628; do not add a range-validation branch.
- Convert signed D_800BE620 to float32, subtract2.0f with single rounding;
  convert signed D_800BE624 to float32. Preserve their original eager loads.
- Reject if the float at+0x2C is below2.0f or+0x30 exceeds the horizontal limit.
  Then reject if+0x24 is below0.0f or+0x28 exceeds the vertical limit.
- Otherwise return1, including ordered comparisons involving quiet NaNs that
  do not fire a rejection. An inside conjunction is not equivalent on NaNs.
- The function writes no memory, allocates no frame and calls no helper.
  Retain every instruction, including the original unreachable duplicate load.

The retail caller `func_1501A8C0` restores its original index into A0 before
the call and writes V0's low byte to record+1 afterward. Its complete350-word
body still has an unrecovered C placeholder; this checkpoint does not restore
that caller or claim full rendering/gameplay behavior.

## Qualification

```sh
python3 -m tools.experiments.game_rectangle_bounds_candidates
python3 -m unittest tools.tests.test_game_rectangle_bounds_match -v
```

Seven pre-install tests pass in9.604 seconds; seven post-install tests pass
in18.629 seconds, no skips.

- 10,692 guest cases cover nine signed dimension patterns per axis, 16 raw
  float patterns varied independently at each bound, equal limits, both stack
  phases and rotating full-word indices. Compare complete RAM/events/GPR/FPR/
  condition/read states against all44 original words and independent results.
- Signed zeros, subnormals, adjacent2.0f values, finite extremes, infinities,
  quiet NaNs and signed conversion rounding boundaries are included. Native
  SSE2/RNE tests independently validate the single-precision expression shape.
  This bounded software oracle does not model FCSR/exception/EPC/hardware state.
- Sparse full-word guest indices map their selected record after low32 offset
  wrap. Those probes are not portable out-of-array native C claims. Native
  indices0..3 remain inside a valid four-record allocation.
- Original memory-read counts are4/5/6/7/7 across the five rejection/success
  paths. Eager height reads remain observable even on horizontal rejection.
  Every byte of each reached load fails closed if unmapped; skipped fields can
  remain unmapped. All58 fired own-access cut pairs agree, with terminal controls.
- Native32 O2/O0 runs32,768 cases each, 65,536 comparisons, comparing the real
  untouched source body against ordered-reference results and the complete
  record allocation. Fresh compiled negatives expose an inside conjunction,
  missing horizontal margin and wrong record stride.
- Ten actual copied-owner neighbors retain body bytes and relative relocations;
  all normalized pools are unchanged, both full-owner padders agree, and the
  isolated raw target/relocations equal its production-owner counterpart.
- Independently assemble/link the complete retail original and C at three
  code/data layouts with signed LO16 carry boundaries. All44 words agree.
- Eighteen connected guest cases exercise five authentic retail caller words:
  JAL/delay-slot store, base reload, address add and return-byte store. Stop
  immediately after that store and compare complete states. No patched caller
  function or full350-word caller acceptance is inferred from this window.

Public paths visit43 words; literal matching includes all44. The first failed
test was a reference error: unrounded integer height comparison rejected a
bottom equal to float32(INT_MAX). Round both dimensions before comparison and
keep an explicit INT_MAX witness. Native and emitted retail instructions already
agreed. No shared oracle or production workaround is changed for that failure.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds, with only the
known duplicate generated_12D630 recipe warning and no new owner diagnostics.
The complete current ELF equals the saved before-image except124 changed target
bytes and one exact symbol-size-field byte, 12->176. The slot has37 changed
words; all other code, addresses, metadata, sections and bytes stay fixed.
All189,088 Game-data bytes /720 owners remain exact, SHA0bbc00e1. Guard history,
progress.csv, retail layout and Makefile are byte-identical.

ELF SHA-256: `ed989dee54dacd4bb6d235d909811747804a314b2dd193d00b9b6aac15cb36ad`.
Source SHA-256: `e7c5ca21bf124da076cff89601618b244604fb97485081ba0159bc454eea8368`.
Fresh matching: Game2,816/4,823 (58.39%), total3,489/5,496 (63.48%),
different2,007/drift0. Converted functions/bytes stay fixed. Root README gets
only the two aggregate matching rows; recovery narratives stay in working docs.

## Fixture And Bank

After the independent full-image gate, archive the previous C58A text fixture
manifest/image in ignored `game-rectangle-bounds-test/text-fixture-before-rectangle/`.
Advance only its expected ELF hash and generated before-image/manifest. All
other eight current/snapshot input hashes remain unchanged. Fresh target image
and text immutable/corruption controls pass as three tests in5.715 seconds.
Historical callback/event full-image gates remain frozen to their own banks.

Reuse, explicitly as prior receipts, Note1315's16 target/text and six callback
regressions: the independent literal image audit proves their linked bodies/
data unchanged, and all protected source/profile/input fingerprints remain
fixed except the declared ELF advancement. Do not repeat unchanged broad suites
or call reused receipts fresh. This checkpoint adds seven target and two fresh
text integrity controls, nine distinct checks.

Mounted tools `0a939ff7d65b7be275327cc1a928f7f487d6bc01` is committed first,
then the source, note/indexes, workflow, aggregate README and gitlink.
Preserve older tools HEAD`ddbdd16b` and unrelated dirty work;
only absent task files and the verified shared ELF fixture may be synchronized.
The two absent task files and shared fixture are hash-checked after copying.
All104 unrelated saved fingerprints remain identical; dirty382 becomes384
and task hashes105 become107. WSL consumer/mounted/older tools checks,
Windows py_compile and whitespace checks pass. All4,579 relative links across
eight checked documents resolve. No older commit or history duplication.
Require clean active checkouts, link/syntax/tools checks, post-bank integrity
controls and a fresh terminal Graphify Rebuilt receipt with zero workers.
Preserve existing graph/version/scan warnings; no force/purge/install/update.
Routine task: zero Claude calls. No push, host/OGL Release, ROM replacement,
save/config/editor change, or full Game completion claim.

## Next

Next ordinary queue entry is `func_1501BB20` in `game/generated_48FD0.c`,
38 words/frame0x28/current37 differences. Its original is in `asm/48FD0.s`.
A byte latch D_80084064 gates a one-shot osSetTimer using the unsigned64 clock
word D_8002BD10 multiplied by25 and divided by1,000,000; interval0, queue
D_8003B218, message6, then clear the latch. Recover the timer object/SDK ABI,
64-bit arithmetic and void return contract before converting. No source fit
or caller qualification is yet accepted for it. Keep the full Game goal active
and retain the separate text, translator and handwritten non-C-ABI boundaries.
