# Game Actor Command Stream Guarded Match - 2026-10-13

## Scope And Result

Resume the full Game matching goal from consumer `63b51153` / tools `80e6fed`
and [Note 1322](1322-game-actor-callback-dispatch-direct-match-and-frame-provenance-20261012.md).
Both active checkouts were clean. Inspect the focused graph, complete original,
direct original caller and unchanged O2/g3/MIPS2/o32 owner profile.
Preserve independent older tools work, private inputs and frozen host Release.

[func_150341BC](../../conker/src/game/generated_61490.c) replaces its zero-return
placeholder with the complete typed command-stream writer. VA0x150341BC..
0x15034340 / ROM0x6166C..0x617F0,97 words/388 bytes, no frame.
**The linked routine is byte-exact, but this is not a direct C match.**
Raw semantic C emits96 words with62 differences;52 expected-word guards derive
a closed scratch-register cycle, two commutative additions and expansion of one
compiler-combined cursor advance, with crossing branches relocated. No copied
retail body, arbitrary NOP, fabricated state, physical-register source binding,
frame guard or profile change. Guard elimination remains a separate source-fit
improvement; the wider Game goal is not complete.

Only the target body, local selected-actor/scale declarations and52 guard rows
change. The direct original caller func_15033FE0 is still a placeholder in C;
no invented caller return/prototype change. Layout, Makefile, conversion CSV,
retail assembly and scale/table data remain fixed.

## Recovered Contract

- Accept an output byte cursor and full32 actor slot; return the advanced cursor.
  First actor address uses unsigned203-word arithmetic shifted by2, equivalent
  modulo32 to the real0x32C-byte stride. No new slot-bound gate.
- Load the attached pointer at actor+0x31C. If nonnull and halfword+0x2F8 does
  not contain0x80, multiply float+0x54 by the existing float D_80097D14, bits
  43360B61 /182.0444489. Truncate to signed32, then narrow to signed16.
- Full unsigned halfword+0x84 types0x42/0x14/0x76 append `(10,value)` and
  `(4,-value)`. Others append `(6,value)` if attached byte+0x78 equals10,
  otherwise `(10,value)`. Commands occupy two signed halfwords/four bytes.
- Independently test signed byte actor+0x1D1. If nonzero, write tag6, re-read the
  signed byte after that store, and append its value times200. Do not cache the
  byte across an aliased tag write.
- Look up the globally selected actor using unsigned byte D_800C3E78[0]. If its
  attached pointer is nonnull and signed halfword+0x12 nonzero, write tag8.
  Re-read selector, actor pointer and value after that store before negation.
  Output aliases can change the selector, pointer or value; retain the reloads.

Finite float products within signed32 conversion range are qualified. Native
tests use a synthetic26-record backing and valid addresses within that backing;
guest-only sparse full-word indices are not portable C array-bounds claims.
Do not claim arbitrary NaN/out-of-range conversions, custom FCSR or real gameplay.

## Source Fit And Guard Derivation

New [candidate/derivation tool](../../tools/experiments/game_actor_command_stream_candidates.py)
reuses prepared compilers, object parsers and complete GLOBAL_ASM owner processing.
Thirty source forms are measured under the unchanged profile; other forms are
shape controls, not all separately semantically qualified.
Basic source88 words/91 differences; normal-first plus explicit extra if/else
90/92. Factored stride or a word-array view recovers the opening shift/add
calculation,96/62. Halfword/command-record cursors, post-increments, address
increments, offset locals and register hints do not finish the direct fit.
Integer cursor96/83 is worse. An initial mixed-declaration C89 screen is corrected;
its syntax rejection was not fitting evidence.

The accepted body keeps all semantic loads/stores and real cursor updates.
Normalization uses only emitted source words and this independently stated rule:

- At raw0x2C, reuse the dead multiplication-result register for the last shift.
  From0x30, map the closed scratch cycle8->25,9..15->8..14,24->15,25->24.
  Keep parameters, return, saved registers and COP1 fields outside that cycle.
- Commute only the two actor-address additions at raw0x12C/0x160.
- Insert `addiu a2,a2,4` after raw0xD4. Change raw0xD8/0xDC store offsets4/6
  to0/2, and the raw0xE0 combined increment8 to4. This restores the two real
  source cursor advances without changing memory-event order or adding padding.
- Recalculate branch origins/targets across the inserted word. Exactly three
  crossing branches gain one word; other branch relationships remain fixed.

The derivation never reads ROM replacement words. Actual compiled objects supply
each expected-word guard; changed instructions have no source relocations.
Both full-owner padders produce the same97-word body. Independent original
assembly/linking verifies the complete result at three code/data layouts.
All52 guard-word corruption controls reject stale object words, including the
unchanged second-store word that anchors the insertion.

## Qualification

```sh
python3 -m tools.experiments.game_actor_command_stream_candidates --screens
python3 -m unittest tools.tests.test_game_actor_command_stream_match -v
make -C conker -j4 build/conker.us.elf progress.csv
```

New [focused tests](../../tools/tests/test_game_actor_command_stream_match.py):
eight pre-install tests pass in18.703 seconds. Eight installed tests pass in
31.810 seconds after the independent metadata accounting below, no skips.
The final native model uses numeric32 address ranges rather than comparing
foreign pointers relationally; focused native test04 reruns in6.688 seconds.
The other seven unchanged installed receipts are retained explicitly.

- 5,760 guest gate/type/flag/attachment/value cases plus3,072 signed-byte cases
  cover all256 byte values, high halfword types, full index extremes, float
  fractions/signs/narrowing and two stack phases. Add32 real memory aliases:
  actor float/type/byte, attached byte/value, global selector and pointer.
- Raw C and retail have equal complete RAM, public memory events and returned
  cursor across those cases. Fitted code additionally matches literal GPR/FPR
  state, private storage, visits and all97 executed words. Raw scratch/fault
  register identity is not claimed.
- All166 own-access fault pairs fire and match literal completed memory/events/
  register prefixes between original and fitted instructions. Gated-off float,
  scale and type backing can be absent without a read. No hardware PC/FCSR claim.
- Native32 O2/O0 each passes65,536 cases, including aliased output and all16-bit
  selected-value patterns. Six effective unsigned-byte, tag, flag, polarity,
  narrow-type and cached-selected-record negatives fail observably. GCC/IDO
  narrowing and the existing native no-strict-aliasing profile are the scope.
- All nine owner neighbors, their relative relocations and normalized pools
  stay fixed. Complete GLOBAL_ASM processing, both full-owner padders and
  derived isolated/owner guard rows agree. Three independent links exercise
  code/global rebasing and HI/LO carries while preserving all97 original words.
- Twelve cases execute the actual five-word original caller call/return/branch
  window. Its S0 receives the returned cursor, and the delay-slot type-byte read
  observes output aliases. The complete119-word caller remains unqualified.

Local fixture corrections add signed LB handling only to the new target oracle,
provide native NULL, map enough backing for overlapping outputs, and correct
C89 declaration placement/GCC misleading indentation. No shared oracle behavior
or production fix is inferred from these fixture failures. Zero Claude calls.

## Linked Audit And Metadata

Appending guards triggers a broad dependency rebuild. It finishes successfully;
the known duplicate generated_12D630 recipe and warnings in unchanged owners
are present. Copied target-owner diagnostics remain unchanged; no warning-free
full-build claim. No ROM replacement/build or host/Release operation.

The first literal image check rejects66 residual metadata bytes. Inspect actual
symbol rows and strings; all named definitions agree after only target size12->388.
Account exactly for a three-entry ordering permutation of func_1514E7C8,
func_1506FC1C and D_800A5EFC, plus the ABS pair D_80097D14/D_80096338.
The checker derives the exact new serialization from prior records and fixed
name order, verifies values/sizes/types/sections and contiguous spans, then
compares every ELF byte. Header and metadata corruption controls still fail;
no wholesale symbol/string-table exclusion or unknown-byte allowance.

Final declared delta:292 target bytes across94 words, two size bytes and66
closed metadata serialization bytes, **360 ELF bytes total**. All other bytes
stay fixed. The guard file is exactly its old byte prefix plus52 rows:
14,641->14,693. All189,088 Game-data bytes /720 owners remain exact,
SHA0bbc00e1; progress/layout/Makefile/retail scale/table source are byte-identical.

| Artifact | SHA256 |
| --- | --- |
| Source | 7d723ce8fb243c2cd0bab9ccf79d58d6fd49db9ee97e1bd829e3c50e97a09351 |
| ELF | 286350b194c866de440d71b60987b3b7c743bb0dcc3b95842240eb74346bde22 |
| Guards | f1837eb63b155963d461e712827d60348fd9f1159dcea171757f27f6f691265b |

These are working-file fingerprints. Git reports its existing CSV CRLF/LF
normalization warning; preserve the original local prefix rather than reformatting
unrelated guard history. A future checkout can require new physical input receipts.

Fresh matching: Game2,822/4,823 (58.51%), total3,495/5,496 (63.59%), drift0,
different2,001; +1 matching, converted functions/bytes unchanged. Root README
gets aggregate rows/date only; roadmap checks this qualified task, not all Game.
Only after independent literal image/guard proof, archive the prior text manifest,
ELF and guards, advance those two fingerprints, and retain all seven other
protected inputs. Fresh text integrity/corruption tests05/06 pass in1.812 seconds.
Earlier target suites keep their own historical image snapshots; their unchanged
semantic receipts are reused, not claimed as fresh whole-image tests.

## Banking And Next

Bank mounted tools `c30d7a0` first, then consumer source/guards/docs/exact gitlink.
Consumer/mounted/older tools checks, both Windows syntax checks and whitespace
checks pass. Older HEADddbdd16b and118 unrelated saved hashes stay fixed; copy
only two absent task files and the verified shared text pin. Dirty396->398 /
fingerprints119->121, no older commit/reset/stash. Verify links, post-bank
integrity, clean active checkouts and fresh terminal Graphify Rebuilt/zero workers.
Preserve existing graph/version/scan warnings and unrelated private state. No push.

Next func_15033FE0, the original parent: VA0x15033FE0..0x150341BC,
ROM0x61490..0x6166C,119 words/frame0x28, currently115 linked differences behind
its placeholder. Focused graph and complete original are inspected, no new
candidate yet. Recover the buffer/state gate, type/table-selected writers,
returned output cursor, two func_1503DA3C lookups, func_15034860 forwarding and
0x1000 terminator. Preserve original table labels and all currently matched
neighbors/data. Full Game, direct guard elimination, text218/114/cut27,
translator49/34 and runtime/hardware gates remain open.
