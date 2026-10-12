# Game Text Measurer Native32 Qualification

Date: 2026-10-12. Continue func_150428D4 in
conker/src/game/generated_6E770.c. Original VA 0x150428D4..0x15042C40,
ROM 0x6FD84..0x700F0: 219 words / 876 bytes, frame 0x80. This tools-only
checkpoint completes native C qualification for the two semantic bodies in
[Note 1293](1293-game-text-measurer-full-chain-qualification-20261012.md).
It is not an installation or byte match. The production zero-return
placeholder remains at 199 word differences; no matching/conversion credit.
Keep the same target and the wider Game goal open.

## Entry And Scope

Consumer 923235e1b5b25695a8467578ac6f4b726263511b and mounted tools
688ae3be8186b8a3dc4e60dc1b901ad84dbe572d were clean at entry. Recover the
finished interrupted allocator screen from its existing artifacts and verify
that no worker remains; do not restart a possibly live compiler.
Codex sole writer, zero Claude calls. Query the existing Graphify graph and
read bounded live ASM/candidate/tests. No OGL/Release build or change, ROM/
save/config mutation, debugger/editor input or tool/account installation.

## Layout Screen

Add bounded loop, register, parameter-reuse and temporary-lifetime candidates
to the existing screen. These are experiments, not semantic qualification of
every variant or production edits. Ordinary while/for/escape-continue forms
retain the 216-word/frame-0x80/211-difference shape. Cached loop-byte form
gives 215/0x80/202; reused unsigned address parameter gives 217/0x78/186.
The register annotations do not improve the clear body. None supersedes the
qualified closer initial-index-late form: 217/0x80/185.

Add the previously omitted, locally established no_r23 allocator control.
For the clear body it emits 219 words/frame 0x80/206 differences, no pool.
Inspect the actual disassembly: it still saves S0..S8 plus RA, spills the
fourth argument at SP+0x8C and hoists the font-global address. Matching length
and frame do not recover the original seven saved-register lifetimes, metric
homes or SP+0x68 flag spill. Do not install that profile or use 206 retail-
copy guards. All compiler controls remain isolated experiments.

## Native C Gate

Add experiments/game_text_measurer_native32.py and extend
tests/test_game_text_measurer_recovery.py. Use the existing native32 compiler/
runner, static freestanding ELF, SSE single-precision arithmetic and disabled
FP contraction/strict aliasing. Compile-time assertions require pointer,
integer and float widths of four bytes. Keep both complete recovered C helper
bodies: func_15042C40 and func_150415E0; no result hooks or instruction-output
projection. A scoped diagnostic pragma retains the redundant narrowed-byte
upper-bound check rather than changing the measured function for GCC.

The independent byte-addressed reference now has an explicit byte order.
Default big-endian guest behavior remains unchanged; native fixtures use
little-endian scalar reads/writes while retaining font/text bytes in their
actual byte order. This matters when an integer output aliases font records
or text. Do not reinterpret the synthetic low-address font-pointer alias
from Note 1293 as a portable native pointer fixture.

Both clear216 and closer217 C bodies pass all 733 cases at O2 and O0:
2,932 complete native executions. Each body/profile covers 512 all-byte /
two-scale cases, 200 mixed-text/ten-alias/two-scale cases, 20 NULL cases and
one nested-truncation crossing-zero case. Include empty/NULL, spaces/newlines,
two-byte control skipping with a zero payload and live final scale writes.
Compare every text/font/output/parameter byte, the live font pointer, the
lookup table and 32-byte buffer/table guards. Portable aliases include all
three outputs, mutable font records, live factor/X/Y scale and text.

Seven freshly compiled native semantic negatives are effective: empty-height,
skip-one, space-width, no-newline-clear, wrong-height-scale, one-truncation
and early-font-height. All fail with a public byte mismatch; the nested-
truncation control fails at case 732, the last specific discriminant. Four
fresh canary-corruption controls independently fail at the expected text/
font/output/lookup guard (codes 6/7/8/9, case zero). Receipts include exact
failure code, case and byte index, not just a nonzero process exit.

An initial harness compile rejected a const lookup cursor and the byte-range
warning; corrected without changing recovered body semantics. An initial
module discovery run accidentally collected an imported renderer TestCase:
its historical whole-source snapshot rejects subsequent unrelated recoveries.
Use a module-qualified runner import, not an exported imported TestCase. The
corrected measurer-module command collects exactly nine focused tests; all
pass in 31.026 seconds, including the unchanged guest/helper and frozen
production gates. Do not refresh the unrelated renderer baseline or treat
that historical failure as a measurer installation result.

After updating the indexes, the two frozen-production/corruption gates pass
again in 1.460 seconds. All 4,447 relative links in the six updated documents
and unchanged root README resolve; git diff --check passes.

Receipts: conker/build/game-text-measurer-recovery-test/native.json,
native-controls.json and the existing guest/production receipts. Generated
C/ELF fixtures remain ignored. Qualification is finite/in-range FP with
single rounding and truncation, not FCSR, invalid conversions, private home
aliases, fault-prefix order, MIPS instruction matching, hardware or gameplay.

~~~sh
python3 -m tools.experiments.game_text_measurer_candidates --filter=selected --allocation
python3 -m unittest tools.tests.test_game_text_measurer_recovery -v
make tools-check
python3 check_project_tools.py
~~~

The last command runs separately in each tools checkout. Consumer/mounted/
older ROM-free checks and native Windows py_compile pass. No production build
was needed or performed. All nine frozen inputs remain exact: source, entire
ELF, guards, progress CSV, Makefile, original slice ASM, table data, metrics
pool and retail layout. Protected data remains 189,088 bytes / 720 owners,
zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Unchanged Input | SHA-256 |
| --- | --- |
| Source | 802b4d27659c80620c2ca509df4c3da84d136c5c92b758d7a6390c4428d2273d |
| ELF | 978d39eab009d4134e5c03d4bdd2d433010812544a5be599c823fdff1ce2aa14 |
| Guards | 3f12cf872b84100963934734de2e67f5f07073ce3112ccbd2e5c4cb8af84666e |

Progress CSV and README aggregates remain unchanged: Game 2,813/4,823
(58.32%), total 3,486/5,496 (63.43%), Init 492/492, Debugger 181/181,
zero drift / 2,010 still different. These are the preserved Note 1293
measurements, not additional matching credit from native qualification.

## Bank And Continue

Bank mounted tools b5e4600 first, then consumer docs/exact gitlink, no push.
Preserve older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a
and all 77 other saved hashes. Verify the two previous measurer tool files
still match their saved hashes before copying their exact updated versions;
add only the absent native32 harness. Dirty count 356 -> 357; final 80 saved
hashes, no older history commit/reset. Root README stays aggregate-only and
unchanged. Final reporting requires clean consumer/mounted trees and a fresh
terminal post-consumer-commit Graphify Rebuilt receipt, advanced log bytes/
UTC and zero native workers; preserve excluded-but-existing graph nodes.

The standalone native Graphify update exits one on protective shrink refusal:
18,290 candidate nodes versus 40,060 saved. Keep 19,398 excluded-but-existing
nodes from 2,972 files. No force, purge, skill/package update or installation.

1. Continue the same target's original 219-word/frame-0x80 lifetime/layout
   fit. Native-qualified bodies are a semantic baseline, not an original
   stack/register match. Recover S0..S6/RA, SP+0x68 flag spill, initial text/
   cursor setup and unhoisted font-address setup without dummy state.
2. Qualify the final candidate in the full copied owner, all seven neighbors,
   existing metrics pool and both padders. Add independent links/rebases and
   deliberately fired full-measurer faults; compare at the justified scope.
   Re-run native tests for every selected semantic/layout change.
3. Install only after complete word matching and literal full-ELF/guard-
   history audit. Measure fresh progress, update README aggregate rows, bank
   tools before consumer source/docs/pin. No broad 185/206 guard batch.
4. Then recover func_150417AC, the remaining 1,098-word formatter. Existing
   guard removal, full Game matching and independent hardware/FCSR/RSP/RDP/
   renderer/gameplay acceptance remain open.
