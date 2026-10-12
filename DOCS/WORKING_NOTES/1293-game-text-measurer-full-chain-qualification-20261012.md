# Game Text Measurer Full-Chain Qualification

Date: 2026-10-12. Continue func_150428D4 in
conker/src/game/generated_6E770.c. Original VA 0x150428D4..0x15042C40,
ROM 0x6FD84..0x700F0: 219 words / 876 bytes, frame 0x80. This checkpoint
banks the complete semantic candidate, focused execution tools and a concrete
layout handoff. It is not an installation or byte match. The production
zero-return placeholder remains at 199 word differences; matching/conversion
totals and all recorded production inputs are unchanged. Do not mark the
function or wider Game goal finished.

## Baseline And Recovered Contract

Consumer 5de932b11955281eae991dcfba872eff8fde21f0 and mounted tools
05875fe0def7acca6c67977c7ca19d80b620c7c7 were clean at entry.
[Note 1292](1292-game-character-normalizer-guarded-match-20261012.md)
left this target after matching its character lookup. Read the full original
routine, nine direct callsites and live data dependencies. Query Graphify;
run the existing local m2c in mips-ido-c mode for an independent structural
reading. Codex sole writer, zero Claude calls, no bridge/install/account change.

The original and all nine callsite continuations support a void interface:
text pointer and three integer-output pointers. Callers consume output memory,
not V0. Width and height are supported by their centering/extent uses; the
candidate's baseline label describes the third output's maximum adjustment
and X scaling, not a recovered original identifier.

- NULL leaves all outputs untouched. Non-NULL clears width, height and third
  output in that order. Empty text adds twelve to height; it is not NULL.
- Byte 0xBC skips itself and one payload byte, including a zero payload.
  Re-test the advanced cursor, not the ignored payload.
- Use actual func_15042C40 normalization. Space/index 0x60 adds four to
  width and makes current line height at least twelve. Codes 0xA1..0xA7
  skip ordinary/extended measurement. Extended 0xA8..0xFF call the actual
  six-argument func_150415E0; ordinary codes use font metadata or newline.
- A newline updates maximum width, clears the current width, makes line
  height at least twelve, accumulates height and resets the line height.
  The end uses max(final width, earlier line maxima) and adds the final line.
- D_80085994 is a live pointer to four-byte font records. Read horizontal
  fields 0/2, write width, reload that pointer, then read fields 3/1 for
  current line height. Do not cache the pointer or read vertical fields early.
- Extended height uses two truncations: truncate height*factor, convert back
  to single, subtract the returned adjustment, truncate again, then add one.
  The third output compares against that live adjustment before truncating it.
- Final writes are width*D_800380A0, height*D_800380A4, then third output*
  D_800380A0. Read scales live at each stage and retain output/global aliases.

The font pointer/table and character lookup live in
conker/asm/data/2275E0.data.s; existing metrics pool/float ownership remains
unchanged. Integer sums use explicit unsigned 32-bit wrapping before the
actual ABI's signed reinterpretation. Floating qualification is finite and
in-range, single-precision rounding plus truncation; no FCSR/invalid-conversion
or portable pointer/private-stack claim.

## Candidate Screen

The clear first complete C body emits 216 words/frame 0x80/211 differences,
no pool, under both owner no-unroll and O2/g3. Default O2 gives 215/206;
O1/g3 gives 253/frame0x50/242, O1 gives 252/0x50/246. Signed sums do not
improve the owner form and are not selected for overflow behavior.

Moving the initial zero-index/cursor lifetime inside the nonempty block gives
217/frame0x80/185 differences. That closer candidate is separately qualified
in 378 complete cases, but still not matching. Integer/byte classification,
declaration order, flag scope, explicit saved flag, cached byte/offset/row
lifetimes, record fields, pointer-array/integer-address representations,
volatile reads and the local m2c lifetime form were screened in bounded groups.
Do not infer semantic qualification for every unselected form from its word
score; the two tested bodies are named explicitly in the suite.

A metrics-state structure reaches 219 words but frame 0x78 and 186 differences:
not acceptable just because length fits. M2c lifetime output gives 218/frame
0xA0/214 differences. The established allocator controls were tried only in
isolated candidates; none is installed. For the closer form, no_const_in_reg
gives 216/frame0x78/204, do_opt_saved_regs 218/frame0x80/193, noprecolor
216/frame0x80/211; the other tested controls retain 217/frame0x80/185.
Preserve the actual owner profile and existing helpers/guards.

The original saves S0..S6 and RA. The tested 216/217 forms save S0..S8 and RA,
cache the font-global address in S7, keep the use-font flag in a saved register
and shift metric-local homes. Retail instead spills the flag through SP+0x68
around the metrics call, uses its seven original saved-register lifetimes and
issues the original font-address setup in the font path. Initial text-read
CSE and cursor setup also differ. These explain many positional differences;
they are not 185 independent scheduling words. Do not use a broad retail-copy
guard batch or add dummy state to force the observed score.

## Full-Chain Qualification

Seven final tests pass in 10.556 seconds. Receipts:
conker/build/game-text-measurer-recovery-test/.
The two final immutable-production/corruption gates pass after all indexes
in 5.404 seconds. All 4,442 relative links in the six edited docs and unchanged
root README resolve; git diff --check passes.

- 535 core cases run the complete 219-word original and complete 216-word
  candidate with actual normalizer65 and metrics115 instructions. All bytes,
  NULL/empty, spaces, newlines, mixed extended glyphs and two-byte skips agree
  with an independent reference on complete public memory and call sequence.
  There are no helper hooks or call-window substitutions.
- 240 cases cover all three outputs aliasing each other, a mutable font
  record, live factor/scales, text and two stack phases under different final
  scales. The model compares public memory, not private stack or scratch/FPR
  equality. The core corpus observes 212 of 219 body words; do not claim
  complete instruction coverage or classify the other seven as unreachable
  merely from this corpus.
- A guest-only font-pointer/output alias produces pointer 32, then 41 after
  width writes. The required fresh second load gives height 30; caching the
  first row pointer gives 15. Low mapped addresses are synthetic guest-model
  evidence, not a native/portable pointer claim.
- Setting the live AA factor to 1/18 exercises height*factor near 1.5 and an
  adjustment of two: the first truncation changes the result across zero.
  Removing it produces an effective public-height mismatch.
- Eight fresh compiled complete-body negatives fail: empty height, one-byte
  skip, space width, omitted newline clear, wrong Y scale, vertical font
  fields read before width, one truncation and cached font pointer. These are
  public mismatches using the actual helpers, not fingerprint-only failures.
- The closer 217-word/frame-0x80/185-difference form passes 378 further cases
  with the actual helpers and original/reference comparisons, including its
  live-pointer and zero-crossing checks. It is not installed or byte-exact.
- Frozen literal production and protected-data gates reject source corruption,
  four ELF mutations across target/helpers/table and guard corruption. There
  is no baseline refresh or metadata projection to pass a mismatch.

No native C, full copied-owner/padder, independent rebase, deliberate full-
measurer fault-prefix or hardware/renderer/gameplay qualification is claimed
here. Prior unchanged helper receipts in Notes 1291/1292 support the literal
helper fingerprints, not fresh full-measurer tests. No source or ELF rebuild
was needed/performed for this tools-only checkpoint; isolated candidates were
compiled with the prepared IDO and MIPS tools.

~~~sh
python3 tools/mips_to_c/m2c.py -t mips-ido-c --globals none -f func_150428D4 conker/asm/6E770.s
python3 -m tools.experiments.game_text_measurer_candidates --profiles
python3 -m tools.experiments.game_text_measurer_candidates --filter=initial-index-late --allocation
python3 -m unittest tools.tests.test_game_text_measurer_recovery -v
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Immutable Production And Checkpoint

All nine recorded inputs are unchanged: source, entire ELF, guards, generated
progress CSV, Makefile, original slice ASM, table data, metrics pool and retail
layout. Protected data is still 189,088 bytes/720 owners, zero differences,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Unchanged Input | SHA-256 |
| --- | --- |
| Source | 802b4d27659c80620c2ca509df4c3da84d136c5c92b758d7a6390c4428d2273d |
| ELF | 978d39eab009d4134e5c03d4bdd2d433010812544a5be599c823fdff1ce2aa14 |
| Guards | 3f12cf872b84100963934734de2e67f5f07073ce3112ccbd2e5c4cb8af84666e |

Fresh matcher: Game 2,813/4,823 (58.32%), total 3,486/5,496 (63.43%),
Init 492/492 and Debugger 181/181; zero drift/2,010 still different.
No matching/conversion credit. Root README aggregates remain correct and
unchanged; the working narrative belongs here and in concise current indexes.

Bank mounted tools 688ae3be8186b8a3dc4e60dc1b901ad84dbe572d first, then
consumer docs/exact gitlink, no push. Consumer/mounted/older WSL shared checks
and native Windows py_compile pass. Preserve older standalone HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 77 prior hashes; copy only
two absent files with equal hashes, dirty count 354 -> 356, final 79 hashes.
Do not commit/reset the older checkout. One mirror py_compile command omitted
the test_ prefix; the corrected exact-path command passes, with no code change.

Graphify query completes; native update exits one on protective shrink refusal:
18,273 candidate nodes versus 40,051 saved. Keep 19,398 excluded-but-existing
nodes from 2,972 files. No force/purge/install. Before final reporting require
a fresh terminal post-consumer-commit Rebuilt receipt, advanced log bytes/UTC
and zero native workers. Launching a hook is not completion.

## Continue This Function

1. Use the qualified complete bodies and reference as the semantic baseline;
   continue original 219-word/frame-0x80 fitting, not another easier function.
   Start with the original seven saved-register lifetimes, SP+0x68 flag spill,
   initial text/cursor setup and unhoisted font-address setup. Re-run the full
   semantic suite for every promising layout change; keep both actual helpers.
2. Complete native32 actual-C qualification, copied full owner/seven neighbors,
   metrics pool and both real padders, independent links and fired access-fault
   gates at the appropriate scope. Do not infer those from public-model tests.
3. Only after the complete byte match and literal linked audit, install the
   qualified body and any narrow justified guards, measure fresh aggregates,
   update README totals and bank tools before consumer source/docs/pin.
4. Then recover func_150417AC, the remaining 1,098-word formatter. Existing
   guard removal and the full Game goal remain open, as do independent
   hardware/FCSR/RSP/RDP/renderer/gameplay acceptance.

No OGL build/change, private input/save or active editor/debugger mutation.
