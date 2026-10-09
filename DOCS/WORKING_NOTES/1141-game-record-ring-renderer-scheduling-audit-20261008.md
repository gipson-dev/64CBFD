# Game Record Ring Renderer Scheduling Audit

Date: 2026-10-08

## Result

Continue the same complete `func_151D80C4` from
[Note 1140](1140-game-record-ring-renderer-frame-fitting-20261008.md), following
the [focused workflow](../AGENT_WORKFLOW.md). VA 0x151D80C4..0x151D8718,
ROM 0x205574..0x205BC8: **405 words / 1,620 bytes / frame 0xD0**.
The fitted baseline still has **198 raw word differences**. None of the
26 complete scheduling forms improves it. No installed conversion, new guard,
raw-word substitution or progress credit. Keep the
[original assembly](../../conker/asm/nonmatchings/generated_204660/func_151D80C4.s)
and [complete owner slice](../../conker/asm/204660.s).

The useful new result is a narrower remaining-work boundary: **167 differing
words change only encoded GP-operand fields; 31 also change ordering or other
fields**. This is a syntactic partition, not proof of a consistent register
mapping. New tests qualify **408 final-lookahead fault-prefix pairs** after
the mode-setup callback and reject a compiled early-exit negative that passes
ordinary output checks. Whole-entry fault prefixes and private fault state
remain unqualified.

Fresh **25 tests pass in 200.736s**, no skips: the prior nine recovery and
twelve fitted-body tests, plus four new scheduling tests. The original and
fitted bodies are both requalified; use this fresh receipt rather than claiming
the prior 21-test timing as current. All production source, assembly, Makefile,
progress, retail input, linked ELF and **11,275 guards** are unchanged.

Converted totals remain **5,481 / Game 4,808**; exact **3,392 / Game 2,719**,
zero drift and 2,089 different. The last installed conversion remains
[Note 1138](1138-game-record-ring-shaping-conversion-20261008.md).
The retained target is byte-exact assembly, not matched C. Root README stays
aggregate-only and unchanged.

## Complete Source Screen

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_renderer_candidates.py)
adds `scheduling_candidates()` and `--schedule`, mutually exclusive with
`--fit`. Preserve the fourteen recovery forms, 37 fitting forms and unchanged
`FITTED = retail-local-order-wide-scaled-factor` baseline. Every trial compiles
the complete semantic body under the existing O2/g3 profile; no smaller target,
dead-local padding, inline instruction insertion or compiler-profile change.

| Complete Scheduling Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Fitted baseline | 405 | 0xD0 | 198 |
| Seed product operand order | 405 | 0xD0 | 198 |
| Both product operand orders | 405 | 0xD0 | 199 |
| Explicit byte factor cast | 405 | 0xD0 | 198 |
| Masked byte / masked half factor | 405 | 0xD0 | 215 |
| Vertex command cursor lifetime | 404 | 0xD0 | 271 |
| Triangle command cursor lifetime | 403 | 0xD0 | 243 |
| All command cursor lifetimes | 402 | 0xD0 | 281 |
| u32 / f32 word records, factored stride | 405 | 0xD0 | 198 |
| u32 / f32 word records, seven-word stride | 409 | 0xD0 | 336 |
| View reused for seed / both phase lifetimes | 405 | 0xD0 | 198 |
| Seed alpha declared first | 405 | 0xD0 | 237 |
| Factor declared before seed alpha | 405 | 0xD8 | 240 |
| Compound seven-record stride | 405 | 0xD0 | 223 |
| Byte request-count lifetime | 405 | 0xD0 | 226 |
| Signed request-count lifetime | 405 | 0xD8 | 254 |
| Initial ring-offset lifetime | 405 | 0xD0 | 223 |
| Separate tail Gfx lifetime | 405 | 0xD8 | 229 |
| Integer record addresses | 402 | 0xD0 | 379 |
| View reused for seed X | 407 | 0xD0 | 310 |
| Separate seed X lifetime | 405 | 0xD8 | 268 |
| Byte alpha and separate seed X | 404 | 0xD0 | 319 |

All 26 forms pass **364 bounded cases** comparing complete public memory,
callback arguments, return cursor and ordered stores against both retail and
the independent reference: four flag modes with two incoming SP phases, plus
six captured-buffer/copy-mutation cases per form. This is not a full-domain or
native32 sweep for every alternative. Word-record and explicit-factor changes
that emit the same bytes do not count as matching progress. Moving `output++`
outside the SDK macros changes extent/schedule and is not a fitting solution.

## New Discriminating Tests

The [renderer suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_renderer_recovery.py)
adds `RibbonAccessOracle` call markers without changing existing execution or
callee hooks, and four scheduling tests:

- **408 fault-prefix pairs / 816 executions** remove each of 17 bytes in the
  final wrapped lookahead record: all three XYZ words, alpha byte +0x14 and
  phase word +0x18. Four flag modes, counts 4/128/255 and SP phases 0/8.
  Both raw fitted and original retail bodies fault after the final segment's
  stores. Their post-MODE public read/write prefixes, complete public memory
  and callback traces agree. Stack accesses and private GP/FP fault state are
  explicitly excluded. This does not qualify whole-entry prefixes, arbitrary
  invalid storage, hardware faults or portable C fault semantics.
- A complete **410-word/frame0xD0 early-exit negative** passes ordinary
  memory/callback/result/store-order comparisons in all four flag modes.
  With a required final phase byte missing, the negative returns while both
  fitted and retail fault. Four effective witnesses prove the lookahead gate
  adds discrimination; no timeout or unsupported-opcode witness is used.
- The operand-field classifier finds **167 GP-only, zero FP-only, zero
  combined-operand and 31 other differences**. It strips encoded operand
  fields only; it does not prove a closed allocation cycle, consistent mapping,
  semantic equivalence, relocation safety, private state or guard eligibility.
- The complete-form screen preserves its 198-word minimum and leaves the
  selected body uninstalled. Ignored receipts record every trial's words,
  frame, raw differences, relocations and diagnostics.

Fresh full-suite execution also retains the established guest/native32,
lazy-read, effective-negative, caller/backend, copied-owner, alias and
independent-rebase checks described in Note 1140. Preserve 22 owner neighbors,
all sixteen symbolic uses and all 6,058 installed linked bodies/addresses/
extents. The real padder accepting 1,620 bytes is still not a byte-match proof.
Graphics setup, deep allocation and memcpy remain bounded hooks; the linked
dispatcher and combiner are still zero-return placeholders. No emulator,
hardware FCSR/traps, gameplay, host integration or OGL/Release change.

## Remaining Schedule Boundary

The 31 other differences occur at **+0x14, +0x34, +0x12C, +0x130 and every
word +0x230..+0x298 inclusive**:

- S2/S3 save-slot ordering at +0x14/+0x34 belongs to their differing
  output/index roles. Swapping register identifiers alone would not establish
  the required saved-value slots and lifetimes.
- The mode setup's global OR inputs load in reversed order at +0x12C/+0x130.
  Equal commutative results do not qualify missing-read prefixes; whole-entry
  access order is still an open gate.
- The default-factor initialization is hoisted into seed setup, interleaving
  the +0x230..+0x298 block. Retail initializes the default later, in its factor
  branch. Resolving this lifetime/schedule may also change width-index and seed
  alpha/phase temporary allocation, but that causal claim is a hypothesis.

Next: fit the full body's factor initialization and mode-input load order
before deriving any closed GP allocation transformation. Retain FITTED's
405-word/frame0xD0 private layout, loop at +0x3E4 and memcpy at +0x56C.
Do not install a broad 198-word normalization batch. Requalify full entry and
private fault state, independent rebases, aliases, native32 and connections for
any revised body. Only then install/rebuild/audit all bodies/data/guards and
refresh measured conversion counts. Wider Game and hardware/gameplay remain open.

## Banking And Checks

Entry parent `88d75e10375becad6697234166d44b162d01eeb9`, mounted tools
`9d466ca8891f3e1f452791db1be342ecdee74337`: clean. Per **"Keep commited"**,
bank the two reviewed tools files first at
**`1f3f5be6b6ff84cdf7c33476437ac89044c34a00`**, then this note, concise indexes
and that exact parent gitlink. No push.

Older standalone tools HEAD stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`.
Only the two renderer files are mirrored after exact prior-hash checks;
their bytes agree, and its full pre-existing dirty status/history is preserved.
No reset, stash or duplicate commit. Fresh **14 shared matcher/padder/setup
tests pass in 0.244s**, both tools project checks and new CLI help pass.
Unrelated neighbor suites are historical, not fresh runs.

Seven protected SHA-256 fingerprints remain unchanged, including complete ELF
`f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`.
Ignored receipts live under `conker/build/game-record-ring-renderer/` and
`conker/build/game-record-ring-renderer-test/scheduling/`. No ROM or transient
artifact is tracked. Fresh syntax/mirror checks and scoped documentation
checks pass **127 documents / 4,091 relative links / zero broken links** before
the parent commit; remote publication is neither verified nor authorized.

Graph query precedes the investigation. Fresh `graphify update .` exits one,
refusing **16,839 nodes over the retained 38,628-node graph**; preserve 19,398
nodes from 2,972 still-existing excluded files. No force, upgrade, changed
ignore policy or graph-repair claim. One Codex writer, zero Claude calls.

```sh
python3 -m tools.experiments.game_record_ring_renderer_candidates --schedule
python3 -m tools.experiments.game_record_ring_renderer_candidates --schedule --form fitted-baseline
python3 -m unittest tools.tests.test_game_record_ring_renderer_recovery.GameRecordRingRendererSchedulingTests -v
python3 -m unittest tools.tests.test_game_record_ring_renderer_recovery -v
```
