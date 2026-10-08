# Game Fourth Tile Scroll Direct Match

Date: 2026-10-08

## Result

Continue the next local leaf inventoried in
[Note 1117](1117-game-attachment-selection-closed-scheduling-match-20261008.md).
Replace `func_150334B8`'s zero-return placeholder in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c) with its complete
semantic SDK Gfx routine. IDO 5.3, existing O2/g3, emits all **68 words /272
bytes directly**, **frame0**, **zero differences**. The real copied owner,
padder and fresh production ELF independently match every retail word.
No guards, filler, calls, global relocations, generated data, compiler-profile,
Makefile or shared-header change. Prior placeholder: **65 word differences**.

VA `0x150334B8..0x150335C8`, ROM `0x60968..0x60A78`.
Retail: [5D2C0.s](../../conker/asm/5D2C0.s).
Caller `func_150339C8` submits its first two arguments at `0x150339E4`.

## Recovered Contract

1. Save incoming actor in its caller home, SP+4; read `node[1]`. The actor
   pointer is never dereferenced. Every action except **0x37** returns0 without
   reading the container or command list.
2. Action0x37 loads the container from `node+0x24`, then its command pointer.
   A null command pointer returns0. The container itself remains required;
   do not add an invented container-null gate.
3. Count four signed-byte **G_SETTILESIZE /0xF2 /-14** matches. Advance past
   the first three; select the fourth. Other signed opcodes are skipped.
   Retail has no scan bound or end sentinel; missing matches fault on required
   absent storage in the bounded tests, not through a new production fallback.
4. Read selected w0 then w1. S starts at the first word's twelve-bit S field
   **minus100**. T starts at its twelve-bit T field. Each span is the
   corresponding twelve-bit field of w1 **plus2**.
5. For each axis subtract its span once when at/above it, then add its span
   once if negative. This is **one-step wrapping, not modulo**: S0/span2
   remains -98 after one addition, and S4095/span2 becomes3993 after one
   subtraction. T4095/span2 becomes4093. Repeating the wrap changes behavior.
6. Store only selected w0, encoding opcode0xF2 and the masked twelve-bit
   coordinates. Preserve all w1 bits and every other command/input byte;
   return0.

## Source And Compiler Fit

[Candidate driver](../../tools/experiments/game_node_tile_scroll_candidates.py)
retains the full routine and source/profile/negative controls. An early-return
shape emits C70/frame0/58 differences. A common return behind the positive
command-pointer guard recovers C68/frame0 with17 register differences.
Plain and `register` local-declaration permutations do not resolve those17.
Computing the S span first and initializing each coordinate pair with a chained
assignment recovers all register allocation directly. This is a measured source
shape, not proof of Rare's original declaration spelling.

Selected C68/frame0/0; register-argument control is likewise exact. Unsigned
command words give two arithmetic-shift differences; for-countdown emits
C69/55. O2 without g3 emits C67/4; O1 with or without g3 emits C116/frame0x30/
114. All standalone/copied target compilations have zero strict diagnostics.
The driver contains18 measured forms,45 ordinary control executions, two raw
exact forms and **nine effective semantic negatives**: wrong action, third
match, zero/-99 shift, +3 spans, unsigned opcode constant, omitted store,
strict boundaries and repeated wrapping. Incorrect signed comparison faults
while scanning instead of finding a command; the other negatives change output.

## Qualification

[Seven tests](../../tools/tests/test_game_node_tile_scroll_match.py) pass
pre-install in **43.357s**, zero skips/errors/failures.

- **45,063 guest cases**:1,024 selector/unused-actor/SP cases,27,648 coordinate/
  span/layout boundary cases,16,384 exhaustive-axis cases, six additional scan
  layouts and one null-command case. Every selector byte and all4,096 values
  of each coordinate axis qualify. Complete V0/GP/FP state, ordered reads/
  writes, memory and saved-register lifetime agree with retail and an independent
  semantic reference.
- **67/68 words execute**. Only word59, negative-T addition at `0x150335A4`,
  is unreachable for masked twelve-bit T and positive spans. Longer scan layouts
  cover the repeated signed-byte loop and branch-likely delay update.
- Thirteen required-storage/missing-match fault prefixes and five valid aliases
  qualify. Two aliases exercise caller-home storage; the actor home is written
  before the node selector or container read. No actor dereference or new gate.
- **16,384 actual native32 complete-C executions** check return, all command
  words and every node/container canary. Native first-byte opcodes are seeded
  explicitly for little-endian host scans. Expectations use the actual seeded
  words: opcode seeding overlaps the low T byte on this host. Full big-endian
  axis coverage comes from the guest test, not an incorrect native endian claim.
- Thirty-nine fully postprocessed owner neighbors, relative relocations and
  useful pool identities remain unchanged. The target has no new pool.
  Actual owner/padder assembly has272 bytes, no padding or relocations; all
  words remain identical under three independent entry bases.

The first seven-test run has five passes and two fixture failures: strict native
compilation rejects chained one-line `if` statements, and the coverage tally
omits visits from the six extra layouts, leaving word27 falsely uncounted.
Split the fixture statements and accumulate those existing visits; the clean
rerun above passes. Neither correction changes candidate or production C.
The initial for-countdown control also needed its nested-loop indentation
corrected before the complete18-form screen could compile. No diagnostics are
suppressed to accommodate these fixtures.

Production dependency-driven ELF/progress rebuild passes; existing duplicate
generated_12D630 recipe warnings remain. This is not a warning-free repository
claim. Tools, Python syntax, CLI/profiles and whitespace checks pass. Ten shared
padder/word-patch regressions pass in **0.051s**.

Post-install focused run: **20 tests pass in112.504s**, zero skips/errors/
failures. It reruns all seven new checks, three earlier tile/cleanup/action
copied-owner/padder checks, four selection binding tests and six selection
scheduling tests. The installed dispatcher still qualifies all674 original
table targets, normalized execution and independent carry/entry rebases.
The unchanged6057-symbol audit additionally protects the broader linked code;
no fresh full-repository or exhaustive92,992-case dispatcher run is claimed.
Documentation validation: **100 documents /4,153 relative links /zero broken**.

```sh
python3 -m tools.experiments.game_node_tile_scroll_candidates --profiles
python3 -m tools.experiments.game_node_tile_scroll_candidates
python3 -m unittest tools.tests.test_game_node_tile_scroll_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

## Linked Audit

Before installation, all6,058 symbols match
`conker/build/game-node-selection-test/after.json` unchanged. After rebuilding:

- All **6,058 symbols /6,042 retail slots /sixteen overflow symbols** retained.
  Only `func_150334B8` changes; **6,057 other bodies** and every address/extent
  remain unchanged.
- `.init`, `.init_data`, `.debugger` and `.game_data` unchanged. All **720
  Game-data owners /189,088 bytes** remain exact, SHA256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
- All **11,144 guard rows** and the conversion CSV hash unchanged. This
  placeholder already counted as C, so conversion counts/bytes do not increase.
- Exact total **3,372/5,467 (61.68%)**, Game **2,699/4,794 (56.30%)**,
  **2,095 different /zero drift**. Init492/492 and Debugger181/181 remain exact.
- Root README updates only the two aggregate matching rows. Detailed history
  stays here and in the documentation indexes.

Authoritative next checkpoint:
**`conker/build/game-node-tile-scroll-test/after.json`**.
Ignored auditor and before/after receipts live beside it. Additional ignored
screens: `game-node-tile-scroll/`, `game-node-tile-scroll-orders/`,
`game-node-tile-scroll-registers/`, `game-node-tile-scroll-assignments/`.

## Next Work

Next local placeholder: **`func_150335C8`**, **113 words /452 bytes**,
**frame0x168**, VA `0x150335C8..0x1503378C`, ROM `0x60A78..0x60C3C`.
Static inventory: second-argument matrix pointer at+0x1D4 gates a call to
`func_15083568`; a nonnull result receives byte/float/flag updates. Seven calls
cover creation, matrix conversion/transforms/decomposition and
`func_15030D54`; the result pointer or zero is returned. Four local matrices,
private outputs, six-argument homes and post-call reloads need independent
recovery. This is **inventory only**, not a qualified C or matching claim.

Other owner placeholders, resolver `func_15031070`, wider Game and full
callee/hardware/gameplay/PC-port qualification remain open. No sibling Release,
save, runtime, hardware or push action.
