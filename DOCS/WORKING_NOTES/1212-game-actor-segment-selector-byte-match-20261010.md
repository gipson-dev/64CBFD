# Actor Segment-Selector Byte Match - 2026-10-10

## Scope And Baseline

Resume [Note 1211](1211-game-actor-segment-selector-recovery-and-layout-gates-20261010.md).
Install complete typed Gfx-pointer/slot func_1502F01C in
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
VA 0x1502F01C..0x1502F264, ROM 0x5C4CC..0x5C714: all 146 words / 584 bytes
now match. Single Codex writer, zero Claude calls. No OGL, Release, saves,
editor or push work. The wider Game matching goal remains active.

Consumer baseline 5e097ba341c6eefa40ac79985efc59b67180e804; mounted tools
dede4a8d5782f298ea528c1db89f0efb05196bec. Both start clean. New ignored baseline
conker/build/game-actor-segment-selector-match-test preserves before-source,
ELF, guards, conversion CSV and rodata assembly. Older recovery, slot, phase,
color and curve baselines are historical and remain untouched.

## Semantic And Physical Recovery

Keep the recovered cached-loop ID, fresh output ID, fresh table pointer after
callbacks, retained pair, NULL retry and mode-zero override. Four actual SDK
gSPSegment commands preserve ordered w0/row-read/w1 accesses and return the
advanced graphics cursor. Explicit unsigned slot arithmetic and complete
portable-C qualification are bounded to slots 0..25.

[Layout driver](../../tools/experiments/game_actor_segment_selector_layout.py)
measures 149 forms in four subbatches: 61 initial address/storage forms, 12
scoped forms, 36 combined/gap forms and 40 storage/continue forms. These are
shape measurements, not claims that every alternative passed the full suite.
Scoping pairValues inside the non-NULL pair block removes the command-cursor
spill. Selected shift-sub-original-scoped-pair has 144 words / 576 bytes,
original 0x88 frame, 109 isolated-link differences, zero pool bytes and zero
diagnostics. Plain scoped has 143 words / 126 differences; address-second
scoped has 145 / 118. A 146-word nested-continue alternative reintroduces
the cursor spill and is not selected merely because its length matches.

Selected C retains the original saved-register lifetimes and pair-word homes
+0x68/+0x6C. Closed fitting restores selection bytes from raw +0x74/+0x75
to retail +0x80/+0x81. Saved s0..s7, fp and ra stay at +0x18..+0x3C.
No private word is dropped to conceal a different lifetime.

## Closed Compiler-Derived Recipe

[Matching helper](../../tools/experiments/game_actor_segment_selector_matching.py)
requires the entire 144-word raw certificate and all seven exact relocation
sites before emitting any fitted instructions. It does not read the ROM.
The ROM and literal original assembly are independent test oracles.

Append 144 guards: 40 changed rows and 104 unchanged dependencies. Three
inserted compiler-derived producers and one omitted certified NOP give the
full 146-word extent, with no tail padding or trim. The omitted word is raw
+0xC8 and is explicitly certified zero. HI16/LO16 actor/mode/row-table pairs
and the override call relocate with their emitted instructions.

Fitting swaps independent opening words, closes selection homes, splits the
existing mode/selector copy producers, reassociates index arithmetic, and
retains distinct pair/table index producers around both stack stores. It
inverts the equality branch and moves the emitted store into its likely delay.
One compiler-emitted unreachable duplicate LBU becomes a duplicate of the
compiler's emitted SB, preserving the original unreachable SB at +0x134.
This is an explicit closed structural normalization, not a claim that only
two scheduling words differed. Original coverage is 145/146; that unreachable
word is not claimed executed. No oracle-derived replacement body is installed.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_actor_segment_selector_match.py):
12 tests pass before installation in 71.069s and after the wider rebuild in
88.506s. After a receipt-only label correction, the final full rerun passes
all 12 in 75.781s.

- 1,013 boundary/mutation cases / 3,039 raw/original/fitted executions preserve
  public memory, ordered accesses, calls and returned cursor. Original/fitted
  also agree on complete private memory and traces. Raw private selection
  homes differ, which the receipt explicitly distinguishes from fitted homes.
- 420 aliases / 1,260 executions cover output overlapping actor bytes, mode
  storage and row data, plus pair aliases. No native big-endian alias claim.
- 384 cases / 1,152 executions connect the actual banked 24-word override
  func_1507E908 and 11-word animation reader func_150849A0. Both linked bodies
  are checked against ROM; no opaque substitution for those callees.
- 84 private cases exercise both stack phases and pair aliases into saved,
  pair-word and selection-byte homes. All 5,228 full access-fault prefixes /
  10,456 executions verify the exact fired gate, entire memory and trace prefix.
  Reserved SP+0x10..+0x13 is unmapped and untouched. These emitted-order probes
  are not portable C fault semantics or hardware acceptance.
- Twelve independent links over four symbol sets qualify 96 cases, including
  HI16/signed-LO16 carry boundaries and complete fitted/original private traces.
- 425,984 native32 complete-C cases cover all 26 bounded slots, callback
  mutations and first-call NULL retries using preprocessed actual SDK headers.
- Seven fresh complete compiled negative controls remain effective. Actual
  padder rejects all 144 stale raw words and all seven stale relocation sites.
- All 37 copied-owner neighbors preserve bodies, relative relocations and
  decoded pools; both complete copied-owner compiles have zero diagnostics.
  Actual padded owner changes only the target 584-byte slot.
- Forty-eight call-site cases execute nine literal retail words at 0x1502CE50
  / ROM 0x5A300 in a synthetic ABI wrapper. The actual installed helper and
  banked callees preserve slot/cursor forwarding; a bounded hostile downstream
  callback exercises caller-saved clobbers. This is not a complete banked
  func_1502CCFC test: its current source remains a zero-return placeholder.

## Installation And Progress

Fresh wider build, matcher and tools-check pass. Existing shared-project
pointer/type/assembly warnings and duplicate generated_12D630 recipe warning
remain; do not confuse zero copied-owner diagnostics with a warning-free build.

Whole linked ELF audit changes only the target 584-byte code slot and symbol
extent, normalizing symbol/string metadata for the comparison. Old guards
remain an exact byte prefix, parsed rows equal old rows plus the 144 new rows,
and conversion CSV/rodata assembly remain exact. Protected .game_data remains
189,088 bytes / 720 owners, zero byte or owner differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Final source SHA-256
787d31fd554192cd8e738a74c66e465ceb3f66a7a1f68d316f3db10967b5025c;
ELF 92ef2d2c1eea16e0fa4b1aaf61179228c80fd1284900cfc6af7b691320ab76c1;
guards 95d0a0c48e8d5f1fc6dd35b77d69d4888dbdb6216f5bd6aea882732b32cb477c;
conversion CSV 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Fresh match-progress: Game 2,754/4,816 (57.18%), total 3,427/5,489 (62.43%),
Init 492/492 and Debugger 181/181 exact; zero drift / 2,062 different.
Converted function/byte totals stay unchanged because the old stub already
counted as C. Root README updates only the two aggregate matching rows.

## Bank And Resume

Bank mounted tools 35a4757c04184464d7ae79df941c240169396899 first, then
consumer source/guards/docs/pin.
Mirror only the three absent authored files to the older tools checkout;
preserve HEAD ddbdd16 and both tracked-dirty fingerprints. Older dirty entries
increase from 180 to 183 solely for those new mirrors. No older commit or push.

Scoped validator passes: 34 documents / 4,161 relative links, zero broken
links; 55 authored tools have exact older mirrors and AST parsing in both
copies. Older HEAD and both tracked-dirty fingerprints remain unchanged.

Final manual graphify update exits 1, refusing 39,322 to 17,541-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files. No force,
purge, package install or policy change. Existing skill/package and zero-node
devcontainer warnings remain. Verify the new consumer detached hook separately
from preceding historical logs before reporting the checkpoint banked.

1. Next is func_1502F264, adjacent 89-word / 356-byte leaf attachment updater,
   VA 0x1502F264..0x1502F3C8, ROM 0x5C714..0x5C878. Its current source is a stub.
2. Recover its slot ABI and one-based attached-slot lookup. Preserve bit-2 early
   exit, NULL matrix fallback versus 0x40-stride matrix translation, fresh flag
   loads, repeated halfword +0x76 read and bit-0x20/0x40 copy gates.
3. Preserve the signed inclusive D_80082FA0 loop limit and each fresh limit
   read; do not silently replace it with a fixed byte count. Qualify aliases,
   leaf shape, floating raw-bit copies, whole owner and actual dispatcher.
4. Only install after complete physical/semantic/relocation gates pass. Preserve
   the separate uninstalled curve handoff in
   [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).

Hardware and live gameplay acceptance remain separate from this linked match.
