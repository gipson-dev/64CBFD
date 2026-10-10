# Actor Segment-Selector Recovery And Layout Gates - 2026-10-10

## Scope And Baseline

Resume [Note 1210](1210-game-slot-byte-updater-byte-match-20261010.md).
Target func_1502F01C: VA 0x1502F01C..0x1502F264, ROM 0x5C4CC..0x5C714,
146 words / 584 bytes. Owner:
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
Recover complete diagnostic Gfx-pointer/slot C without installing it until
the physical frame, extent, private lifetimes and every linked word qualify.

Consumer baseline 272eec9220113b020ba9c64b8f9195b8247ea38d; mounted tools
da955e65b47ccd5e5b6ea448e221013aa4319672. Both start clean. Fresh ignored
baseline: conker/build/game-actor-segment-selector-recovery-test. Historical
slot, phase, color and curve baselines remain untouched. Single Codex writer,
zero Claude calls; no OGL, Release, saves, editor or push work.

Source baseline SHA-256
1c452a1b4f04240496c2465a40cc814171414fa388e3251fb5dfcbb159b924a1;
ELF 2fbe08aae305eb4d949561b5a84199e72f8b0502149e1299640aa06d98408acf;
guards 4fd76deaa81932da3a078bc21dcdec433707b74342ff1841083f493b89bea712.
Fresh final suite checks these exact hashes, conversion CSV and rodata assembly.

## Recovered Semantics

Return is an advanced Gfx cursor, not s32/void. Actor is D_800CC2D0 plus
slot*0x32C, with explicit unsigned offset arithmetic. Cache ID byte +4 before
two iterations for D_800D1C90[id]. Reload ID after all callbacks for the output
table D_800C5338[id]. Callback ID changes must not redirect the cached loop
lookup, but must redirect the final output table.

For bytes +0x6C/+0x6D, mode >=10 selects mode minus ten and skips table/pair
work. Otherwise read the cached-ID table pointer, fresh selector +0x6F and
table[index*3+mode+8] in the original emitted order. The retained pair starts
NULL. If the selector is nonzero and pair is NULL, call
func_1507E908(actor,selector). NULL permits another call on the next iteration;
non-NULL persists even if the next fresh selector is zero.

For a non-NULL pair read both bytes in order into word temporaries. Reload the
cached-ID table pointer after the callback. Use pair[index] if it equals
table[index*3+10], or if the freshly reread actor mode is zero. The equality
path skips that mode reread. Retain the redundant second pair check in complete
diagnostic C. The original unreachable SB at +0x134 stays a future layout gate.

After the final ID reload, NULL output table emits nothing but does not bypass
selection/callback work. Otherwise emit four ordered SDK gSPSegment commands,
row stride twelve and row word zero: segment 6/0xDB060018 from selection zero,
7/0xDB06001C from selection one, 10/0xDB060028 from fresh actor byte +0x68,
and 11/0xDB06002C from fresh +0x69. Each command writes w0 before its row read
and w1; the cursor advances 32 bytes. Output/table/actor aliases require these
ordered accesses, not just the same final commands in a disjoint fixture.

## Actual Callees And Caller Correction

Actual banked func_1507E908 is 24 words / 96 bytes, frame 0x18. It saves the
selector's full word at caller argument home SP+0x1C and calls the actual
11-word func_150849A0. That reader loads actor byte +0x1C9 and pointer +0x2C4;
zero count selects the first animation byte, otherwise count minus one.
The override helper indexes D_800D1C90 by that animation ID, returning NULL
if its table pointer or the word at table-8 is NULL. Otherwise return that
word plus selector*10. Both complete banked bodies are verified against ROM.
The connected qualification uses their actual instructions, not opaque hooks.

Correct the preceding handoff: the call at VA 0x1502CE50 / ROM 0x5A300 belongs
to retail func_1502CCFC, not func_1502C974. It passes s0 as a0 with a1 already
holding the slot, forwards returned v0 to func_1502F9FC, then writes more
commands. Current func_1502CCFC source is a zero-return placeholder. This turn
does not claim a complete banked-caller connection or restore that caller.
Note 1210 gets only this factual caller correction, not rewritten receipts.

## Compiler Measurements And Installation Rejection

[Candidate driver](../../tools/experiments/game_actor_segment_selector_candidates.py)
measures 36 complete/profile forms. Selected O2/g3: 149 words, 0x90 frame,
135 isolated-link differences, zero pool bytes and zero diagnostics. O2:
149 words / 146 differences; O1/g3 and O1: 197 words, 0x50 frame, 196 differences.
The SDK macro is used directly. Explicit stores produce a shorter 139-word
form, but a different output-store schedule; do not choose it from length alone.

Declaration order alone gives 149 words / 0x88 frame / 134 differences.
The shift-both index form gives 149 / 0x88 / 130; macro temporary form 147 /
0x90 / 134. These are measured alternatives, not full qualified/private-frame
solutions. Keep the selected public-semantic reference until replacements pass
the complete discriminating suite. No blanket profile or slice regeneration.

Original saved homes: s0..s7, fp, ra at +0x18 through +0x3C; original frame
0x88. Pair words live at +0x68/+0x6C, selection bytes +0x80/+0x81. Selected
diagnostic frame is 0x90: pair words +0x74/+0x78, selection +0x70/+0x71,
cached-ID spill +0x7F and command cursor spilled at caller home +0x90.
It retains an extra multiplier/index-product lifetime. Shift-both removes that
multiplier but holds a private pair-array base in a saved register and still
spills the command cursor. These are observed allocation/layout differences,
not permission to omit real stores, trim instructions or synthesize the retail
body from its oracle.

Actual copied-owner padder rejects the selected object: 0x254 bytes versus
the retail 0x248-byte span. Production source remains the placeholder;
no new CSV guards, insertions, omissions, conversion or matching credit.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_actor_segment_selector_recovery.py):
nine tests pass in 22.702s after all fixture corrections.

- 1,013 boundary/mutation cases / 2,026 original-and-compiled executions cover
  every first/second byte value, gate corners, selectors 0/1/255, NULL output,
  repeated NULL pair results, retained pointers, selector changes and callbacks
  mutating IDs, mode bytes, table pointers and pair values. Slots 0,12,25 and
  both stack phases participate. Public memory, ordered accesses, calls and
  returned cursor agree with an independent reference. Original coverage is
  145/146 words; unreachable SB +0x134 is not claimed reached.
- 420 aliases / 840 executions cover output overlapping actor fields, mode
  storage and row data, plus pair pointers into actor/output. Ordered row and
  fresh byte reads agree. No native big-endian alias claim.
- 384 cases / 768 executions connect actual banked 24/11-word callees across
  slots 0/25, animation counts 0/1/2/255, selectors 0/1/2/255, byte gate corners
  and both NULL exits. No opaque substitution for those callees.
- Eight independent links over four entry/actor/table/callback symbol sets
  exercise HI16/signed-LO16 carries; 48 rebase cases agree.
- 425,984 native32 complete-C cases span all 26 bounded slots, all first byte
  values, sixteen second-byte values, callback mutations and first-call NULL
  retries. The fixture preprocesses the actual SDK mbi/gbi headers and full
  C body, rather than hand-rolling the graphics macro. No invalid-slot claim.
- Seven fresh complete compiled negative controls are effective: cached final
  ID, reloaded loop ID, suppressed NULL retry, missing zero-mode override,
  reading the first pair byte twice, wrong final segment and one iteration.
- 494 public access-fault prefixes / 988 executions verify each exact gate,
  public memory and event prefix. These emitted-order tests are not portable
  C fault semantics, and do not yet certify complete private stack lifetimes.
- All 37 copied-owner neighbors preserve bodies and relative relocations;
  pools agree by decoded ownership. Both copied-owner compiles have zero
  diagnostics. Production source/ELF/guards/conversion rows/rodata remain exact.

Fixture corrections precede acceptance: move row data out of the oracle stack
range, preprocess full SDK macro uses with mbi.h, use parse_object for function
metadata, pass audit_layout arguments in its actual order and match the actual
padder rejection text. Earlier failed runs are not counted as qualification.

## Bank And Resume

Fresh tools-check and matcher pass. Matching totals remain Game 2,753/4,816
(57.16%), total 3,426/5,489 (62.42%), Init 492/492 and Debugger 181/181 exact;
zero drift / 2,063 different. Protected data remains 189,088 bytes / 720 owners,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
No production change means no unnecessary broad rebuild. Root README's
already-current aggregate rows need no edit; detailed updates stay in DOCS.

Bank tools dede4a8d5782f298ea528c1db89f0efb05196bec first, then consumer
documentation/caller correction/pin. Mirror only the two absent authored files
to the older tools checkout; preserve HEAD ddbdd16 and both tracked-dirty
fingerprints, with no overwrite or older commit. No push. Check the new consumer
post-commit hook separately from preceding historical receipts.

Scoped validator passes: 33 documents / 4,150 relative links, zero broken
links; 52 authored tools have exact older mirrors and AST parsing in both
copies. Older HEAD and both tracked-dirty fingerprints remain unchanged.

Final manual graphify update exits 1, refusing a 39,312 to 17,541-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Existing
package/skill and zero-node devcontainer.json warnings remain. No force, purge,
install or policy change.

1. Preserve this fresh semantic baseline. Recover 0x88 frame and original
   private homes without new cached reads, alias changes or uninitialized bytes.
   Investigate index-address shapes and pair-array base lifetime while keeping
   command cursor and cached ID in the original saved lifetimes.
2. Recover the complete 146-word extent, branch/delay-store structure and
   relocation sites from compiler-derived instructions. Do not use tail trims,
   loose expected words or an oracle-derived replacement body.
3. Extend qualification to all private memory/access/fault lifetimes, stale
   word/relocation rejection, independent links, actual owner padder and a
   legitimate retail-caller boundary. Keep its production placeholder explicit.
4. Only then install typed C/closed guards, rebuild, audit every linked byte,
   remeasure progress and bank tools before the consumer checkpoint.

Preserve the separate uninstalled curve rejection handoff in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game matching goal remains active; semantic recovery is not a match
or completion of that goal. Hardware/live gameplay acceptance stays separate.
