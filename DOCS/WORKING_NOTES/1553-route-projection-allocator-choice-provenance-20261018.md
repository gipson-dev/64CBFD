# Route Projection Allocator Choice Provenance

Date: 2026-10-18. Consumer predecessor **e0621279**; tools predecessor
**1614a2c**, new tools checkpoint **4c718c5** banked first. Continue
**func_150891E8**, owner `generated_B3020`,321 words/frame120. This pass
observes the prepared compiler's actual allocation choices and rejects grouped
scan alternatives. The Note1552 body remains uninstalled at221 differences;
there is no production conversion, guard append or matching credit.

## Measured Choices

An isolated source containing only the target and its actual declarations
reproduces the complete owner's exact321 words and18 bindings, SHA-256
`2eee0341eb75fa11db9eefb78183ed892110ba1287b1ab35e17083e263dc36b7`.
Use the existing compiler-only no-unroll wrapper; do not send its option to
asm-processor. The first isolation attempt did that and was rejected before
compilation. Correcting the adapter reproduces the pinned object with no
diagnostics and no other function definitions.

`tools/experiments/game_route_projection_allocation_trace.py` reuses the
fingerprint-locked UOPT diagnostics and read-only native allocator probes.
Two owned compiler captures complete: mode5 listing and native color choices.
All CFE/UOPT/UGEN/AS1 children and their driver exit0; final inferior is null.
Diagnostic-buffer and real-number-printer probes actually fire. Complete
object text, function definitions, bindings and all data/pool sections remain
identical to normal compilation. No allocator color or priority is written.

The native capture contains **168 events**. Local coloring precedes global
coloring, then initialization, ranking/selection/splitting and global return.
Six stable live-range pointers are checked throughout one UOPT process/table.
All six saved-role expressions form a mutual interference clique. At global
initialization **none forbids saved colors14..19**. Actual choice order:

| Order | Expression | Role | Final Color / MIPS Register | Retail Register |
| --- | --- | --- | --- | --- |
| 1 | 109 | Current ID | 14 / S0 | S3 |
| 2 | 27 | Anchor node | 15 / S1 | S1 |
| 3 | 113 | Previous ID | 16 / S2 | S4 |
| 4 | 262 | Table address | 17 / S3 | S0 |
| 5 | 18 | Record argument, P0 | 18 / S4 | S2 |
| 6 | 2 | Actor argument, P4 | 19 / S5 | S5 |

The final native assignments/forbidden sets agree with the independent mode5
listing and emitted instructions. Saved colors become forbidden as earlier
choices are made; the initial table does not force current to S0 or record
to S4. This establishes a choice-order problem for this reconstructed source,
not the original source's priorities. Expression15, M749:-60, remains color-1
and corresponds to the already observed object spill at SP+3C.

Raw native gain words are retained as hex in the receipt. Do not interpret
suppressed real-number diagnostic text, numeric timings or unproven cost units.
The observations concern an owned x86-64 compiler process, not native game
execution, retail optimizer state, MMU/FCSR behavior or gameplay acceptance.

## Rejected Groups

`game_route_projection_grouped_fit.py` tests a first slot plus a real four-slot
group, using three counter carriers and a pointer cursor. All four target
word vectors/bindings agree between normal and existing owner profiles:

| Carrier | Words | Frame | Word Differences |
| --- | --- | --- | --- |
| Byte next | 327 | 120 | 308 |
| Byte current | 327 | 120 | 304 |
| Word first | 325 | 112 | 309 |
| Pointer cursor | 325 | 120 | 303 |

All eight screens preserve72 raw neighbors/relative bindings and normalized
pools against their own profile baseline.192 sampled complete public states
and actual helper calls agree with the reference. None has the required joint
extent/frame/allocation contract; none is an installable replacement. The
current-ID counter recovers the opening record-S2 save order, but still has
tableS1/anchorS3/currentS0 and a real counter increment/mask/branch. Do not
repeat these four groups or insert/delete words to fit their extent.

## Qualification

```sh
python3 -m tools.experiments.game_route_projection_grouped_fit --qualify
python3 -m tools.experiments.game_route_projection_allocation_trace --observe
python3 -m tools.experiments.game_route_projection_allocation_trace --colors
python3 -m tools.experiments.game_route_projection_allocation_trace --audit --colors
python3 -m unittest tools.tests.test_game_route_projection_allocation_trace -v
```

Six final tests pass in **9.297s**. They audit the already completed captures,
not new debugger executions. Missing captures can be produced by the explicit
observation commands. Fresh grouped qualification compiles all eight cases;
the final tests audit those unchanged complete source/object/receipt triples.

- Check both capture lifecycles, fired probes, unchanged complete objects,
  the24-variable/44-constraint table, object spill and all six chosen roles.
- **Twelve effective fact controls** alter colors, object spill, parameter
  identities, procedure markers and an interference edge. **Twelve native
  event controls plus one producer-exit control** reject missing/order/owner/
  pointer/unit/active-row/final-color errors and an initially forbidden S0.
- **Four captured source/listing/probe corruptions** and **thirty live/snapshot
  input corruptions** fail closed. All15 historical input fingerprints remain
  strict. Three new task files pass ASCII/AST and mirror byte-identity checks.
- The Note1552 seven-test/575-case/1458-prefix result is explicitly reused on
  the unchanged target hash, compiler/input fingerprints and body, not rerun
  or claimed as fresh game matching. Its child-save/fault limitations remain.

The native capture initially failed only its post-validator's incorrect
assumption that global entry must be first. Actual retained events and clean
producer/driver exits establish local-entry/local-return before global entry.
Correct the validator to require that exact sequence, then audit the completed
capture without restarting it. Original debugger log, listing, objects and
initial trace receipt are retained; no failed capture is silently replaced.

Artifacts are ignored under `conker/build/game-route-projection-grouped-fit/`
and `conker/build/game-route-projection-allocation-trace/`. The checked native
debugger log SHA-256 is
`ef468664774403fe57439df809d08fca9ec2c5f0ef502a074d641da12c4eda00`.

## Advisory Reconciliation

One focused packet-only Claude Code Pro advisory was attempted and completed,
after fresh CLI/help/auth checks:2.1.218, claude.ai/firstParty, Pro. Effective
init reports tools=[] and mcp_servers=[]; no tool use, account/provider/model
override, permission bypass or automatic retry. The packet has2291 words;
SHA-256 `515f77c75ca5afe5980ed504fb7d58380bb6c189fa0a5ecf0ebfcf40133d1fbe`.

The question requested discriminating source/probe ideas for S0/S2 allocation
while retaining321 words and live homes. Retain its general table-address/
current-ID framing as already independently established evidence. Reject the
object-promotion explanation: raw already spills object at3C while record is
S4, and the observed object expression is uncolored. Retail uses six S
registers plus RA; this must not be confused with six total saved GPRs.
The answer supplies no independently validated source fix or approval. The
priority/source-expression explanation remains a hypothesis about how to
recover the retail order, not an observed original-compiler fact. The native
captures above replace guesses about the current candidate's choice order.

Original packet, answer, stream, receipt, runner and reconciliation remain
unchanged ignored artifacts beside the grouped screens. Call budget1/1 used;
no second review is requested for the same unresolved decision.

## Resume Here

Recover the original loop/invariant expression priorities jointly with321
words, frame120, saved order and all30/3C/44/48/50/5C homes. Investigate a
discriminating original five-slot/node-address expression using the measured
choice sequence, then verify actual emitted roles and helper saved-S0 memory.
Do not force physical colors, promote an already spilled object, repeat the
rejected grouping/register-hint screens or normalize221 words by appearance.

The current 321-word body, the302-word null-path candidate and all historical
pins stay distinct. No new body is selected. Closed normalization, independent
rebases, native32/full fault/caller qualification, installation and whole-ELF
audit remain later gates. Enqueue1512D560, vector15088F30, other parent150896EC
and wider Game queues remain open; the overall goal is active.

## Preserved Baseline

No production C, guards, ELF, Makefile/profile, progress or root README change.
Fresh hashes remain ELF4b8ab8ed, ownerf7db991f, guardsc40fe51b and
Makefile840897f1; full values are in Note1550. No production build/recount is
claimed. Note1549 totals remain **Game2,985/4,828 (61.83%)**, **total3,658/5,501
(66.50%)**, Init492/492, Debugger181/181, **1,843 different /zero drift**.

Shared padder/PC16 tests pass eleven per tools copy, both smoke checks and
consumer tools-check pass. Standalone mirror HEADddbdd16 and all1,232 prior
dirty hashes are preserved; only three absent task paths are added for1,235.
No mirror commit/reset, push, host-port or frozen Release action.

Scoped Graphify refresh: **42,599 nodes /82,666 links /3,981 communities**.
Preserve all42,586 unaffected old IDs; three duplicate UPDATE_LOG headings
relocate by eleven lines with labels/files retained. This note adds eight
nodes. Retain19,398 nodes from2,972 excluded-but-existing files. Tools stay
outside the configured corpus, not new graph AST coverage for these Python
files. Original graph/ID receipts remain ignored; no full-scan purge, committed
graph outputs or history rewrite.
