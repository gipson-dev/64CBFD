# Slot Byte-Updater Byte Match - 2026-10-10

## Scope And Baseline

Resume [Note 1209](1209-game-object-phase-updater-byte-match-20261010.md).
Target func_1502EEF4: VA 0x1502EEF4..0x1502F01C, ROM 0x5C3A4..0x5C4CC,
74 words / 296 bytes. Owner:
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
Replace its false zero-return placeholder with complete void semantic C and
typed slot declaration. The banked func_1502BD84 caller ignores the return;
its unchanged statement forwards the slot, not an actor pointer.

Consumer baseline 2e659428132add885c4b5277dde78a6bb037b7e9; mounted tools
7ae085c6c68b250b0f9dc719b99f04b7a7fd2195. Both start clean. Fresh ignored
baseline: conker/build/game-slot-byte-update-match-test. Historical phase,
color and curve baselines remain untouched. Single Codex writer, zero Claude
calls. No OGL, Release, saves, editor or push work.

## Recovered Semantics

Actor base is D_800CC2D0 + slot*0x32C. Two iterations inspect bytes +0x6C
and +0x6D. Values >=10 skip the classifier. Otherwise call
func_1502EE8C(slot,index), interpreting only the low return byte. State zero
decrements a freshly reread positive byte; state one increments a freshly
reread byte below two; other states store one. Keep callback-sensitive reads,
the advanced byte cursor and the distinct one-valued saved lifetimes.

The final callback func_1507E3C0 receives the original actor, not the advanced
cursor. Its address calculation remains separate. Explicit unsigned arithmetic
implements slot-offset wrapping; portable complete-C qualification is bounded
to valid slots 0..25, not arbitrary invalid pointers.

Actual banked func_1502EE8C is a 26-word classifier: actor bytes +0x6A/+0x6B
map values below two unchanged, below four minus two, and others to two.
Actual banked 80-word func_1507E3C0 is no-op for IDs other than 15, 70 and 76.
For those IDs it derives two states from the updated bytes, ORs flags +0x94
with 0x7E, then clears the appropriate first/second channel bits. Qualification
executes both complete banked bodies, not opaque substitutes for these callees.

## Compiler And Closed Layout

[Candidate driver](../../tools/experiments/game_slot_byte_update_candidates.py)
measures 32 complete/profile forms. Selected O2/g3 emits 74 words, frame 0x30,
27 isolated-link differences, zero pool bytes and zero diagnostics. O2 has
37 differences; O1/g3 and O1 emit 78 words/frame 0x28 with 77 differences.
The straightforward pointer-loop baseline emits 64 words/frame 0x40 with
54 differences. Different address-expression trees can reduce word differences
but do not replace the selected complete original-shape arithmetic.

[Matching driver](../../tools/experiments/game_slot_byte_update_matching.py)
certifies every raw word and all six relocation sites before deriving output
from compiled instructions. It never reads/copies the retail body. All 74 CSV
rows are closed guards: 27 changed words and 47 unchanged dependencies, zero
insertions, omissions or tail padding. Twenty-five explicit field renames
close four saved-register roles and the final address-register lifetimes;
an independent opening-save permutation restores the original schedule.
The SLL operand is its rt field, not rs. Physical saved homes remain unchanged.

Frame 0x30 saves s0..s5 and ra at +0x14,+0x18,+0x1C,+0x20,+0x24,+0x28,+0x2C.
The private +0x10 word is untouched. Six relocations: D_800CC2D0 HI16/LO16
at +68/+72 and +240/+244, func_1502EE8C call +120, func_1507E3C0 call +252.
No compact pool is introduced, so existing phase/color addends stay unchanged.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_slot_byte_update_match.py): eleven
tests pass before installation (22.802s) and after installation (21.251s).

- 7,664 cases / 22,992 executions compare original, fitted and complete raw C:
  all 256 byte values, eight boundary gates, wide low-byte returns, current/
  next-byte callback mutations and bounded slots 0,1,12,24,25. Full private
  memory/events/calls agree for original/fitted; raw C agrees with an independent
  public reference and ordered accesses. Seventy-three retail words are reached;
  the original unreachable SB at word 48 is exact, but not claimed as coverage.
- 450 fault prefixes / 900 executions compare full memory and event prefixes,
  with verified gates and 24 reserved-hole controls. Private stack +0x10 is
  unmapped and untouched. This is not a portable C fault-semantics claim.
- Twelve independent links over four symbol sets exercise signed LO16 carries;
  80 rebase cases agree for original, fitted and raw compiled bodies.
- All 37 copied-owner neighbors retain complete relative bodies, relocations
  and pools. Actual padded owner changes only the 296-byte target.
- Actual padder rejects 74 stale-word controls and six stale-relocation controls;
  the closed recipe also rejects every stale raw word.
- Actual native32 complete C passes 239,616 cases over all 26 bounded slots,
  callback mutations and wide classifier returns.
- Five fresh complete compiled negatives are effective: cached byte, missing
  return-byte truncation, wrong byte gate, one iteration and final advanced
  pointer. The cached-byte fixture uses first byte nine before callback clears
  it: original writes zero, the wrong cached form writes eight. The initial
  ineffective fixture was corrected before acceptance.
- 3,840 cases connect the actual 26-word classifier and 80-word flag helper to
  the fitted/installed updater, with an independent flag reference and no-op IDs.
- 160 cases connect actual banked 88-word func_1502BD84, with eight verified
  updater entries, correct slot 0/25 forwarding, early state/ID/active gates,
  and metadata callback clearing active. Signal is bounded to zero; remaining
  callbacks are bounded with hostile caller-register clobbers. O32 saved GPR/
  FPR state is checked on return. No hardware or live gameplay acceptance claim.

## Linked Audit And Bank

Fresh wider build, match-progress and tools-check pass. Existing duplicate
generated_12D630 recipe, legacy pointer/type, long-double and old assembler/
compiler warnings remain. Target/copied-owner compiles are clean; this does
not mean the whole project is warning-free.

Whole rebuilt ELF differs only in the target 296-byte slot and symbol extent,
after normalizing decoded symbol/string metadata. Every other linked function
and data byte agrees with the fresh baseline. Old CSV guard bytes are an exact
prefix followed by 74 new rows; original rodata assembly and conversion rows
are byte-identical. Protected data is exact: 189,088 bytes / 720 owners,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Source SHA-256 1c452a1b4f04240496c2465a40cc814171414fa388e3251fb5dfcbb159b924a1.
ELF SHA-256 2fbe08aae305eb4d949561b5a84199e72f8b0502149e1299640aa06d98408acf.
Guard SHA-256 4fd76deaa81932da3a078bc21dcdec433707b74342ff1841083f493b89bea712.

Fresh matcher: Game 2,753/4,816 (57.16%), total 3,426/5,489 (62.42%),
Init 492/492 and Debugger 181/181 exact. Zero drift / 2,063 different.
Converted counts/bytes stay unchanged because the placeholder counted as C.
Root README changes only its two aggregate match rows, not function narratives.

Bank tools da955e6 first, then consumer source/guards/docs/aggregate rows/pin.
Mirror only the three absent authored files to the older checkout; preserve its
HEAD ddbdd16 and both independently dirty tracked fingerprints. No older commit
and no push. Check the fresh consumer hook separately from historical receipts.

Scoped validator passes: 32 documents / 4,140 relative links, zero broken
links; 50 authored tools have exact older mirrors and AST parsing in both
copies. Older HEAD and both tracked-dirty fingerprints remain unchanged.

Manual graphify update exits 1, refusing a 39,302 to 17,521-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Existing
package/skill-version and zero-node devcontainer.json warnings remain. No
force, purge, install or policy changes.

## Next: Four Display-List Segments

func_1502F01C remains a zero-return placeholder in this owner: VA
0x1502F01C..0x1502F264, ROM 0x5C4CC..0x5C714, 146 words / 584 bytes.
Frame 0x88 saves s0..s7, fp and ra at +0x18 through +0x3C. Recover
Gfx *func_1502F01C(Gfx *commands,s32 slot), preserving returned advanced cursor.
Original func_1502C974 calls it at VA 0x1502CE50 / ROM 0x5A300 and consumes v0.
Take a fresh baseline before changing this authorized neighbor.

Cache actor ID +4 before the two-byte loop for D_800D1C90[id]. Bytes +0x6C/
+0x6D >=10 select value minus ten without table/override work. Otherwise select
table[index*3+mode+8]. Fresh byte +0x6F gates override lookup. If enabled and
the retained pair pointer is NULL, call func_1507E908(actor,selectorByte).
NULL can cause another call on the second iteration; do not claim at most one.
Read both non-NULL pair bytes into original word homes SP+0x68/+0x6C in order.
Select the indexed override if it equals table[index*3+0xA], or if the fresh
actor mode byte is zero. Preserve the redundant original check/unreachable store.
Selection bytes live at SP+0x80/+0x81. Read the complete override callee before
promising its prototype or broad callback semantics.

After the loop reload actor ID +4 for D_800C5338[id]; callbacks may change it.
NULL emits no commands but does not skip preceding selection work. Otherwise
emit four 8-byte commands, row stride 12 and row word zero:
0xDB060018 from selection zero; 0xDB06001C from selection one;
0xDB060028 from fresh actor byte +0x68; 0xDB06002C from fresh byte +0x69.
Preserve output/table access order, use existing SDK macros when exact, and
qualify actual banked caller plus callback mutations, pools, ABI and linked audit.
Future compact-pool movement needs full explicit qualification, not loose guards.

Preserve the uninstalled curve rejection handoff in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game matching goal stays active; this checkpoint is not completion.
