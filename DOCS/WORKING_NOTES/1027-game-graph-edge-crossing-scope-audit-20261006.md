# Game Graph Edge Crossing Scope Audit

Date: 2026-10-06. Starting checkpoint: `5a2ef56a`.

Continue the source-only matching audit of `func_15086D94` from
[Note 1026](1026-game-graph-edge-crossing-lifetime-improvement-20261006.md).
**No production change or new exact match.** The verified baseline remains
207 emitted words, frame 0x80, 102 real differences, no padding or guards.

## Bounded Screen

[Scope driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_graph_edge_crossing_scopes.py)
freezes the preceding selected source independently of future recovery edits.
Its five modes compile 101 named controls under the existing no-unroll profile.
All diagnostics are empty; no candidate improves on 102 differences.

| Mode | Controls | Result |
| --- | ---: | --- |
| Local scopes | 15 | Twelve edge scopes: 114 differences; three crossing scopes: 102 |
| Separate second-plane lifetimes | 14 | Best 102; other shapes 157, 162 or 196 |
| Struct / array aggregates | 8 | Four structs unchanged at 102; arrays oversized at 210..223 words |
| Dot-product sum order | 32 | Best 102; worst 111, all 207 words / frame 0x80 |
| Product operand order | 32 | All unchanged at 207 words / frame 0x80 / 102 differences |

Identifier-boundary product replacements distinguish `x` from `ax` and
`cross_x`. The first and second plane each contain `ax * nx`; the rewriter
requires both occurrences. Missing or ambiguous anchors fail closed. Tests
bind the 101-name inventory, frozen body, protected declarations, original
normal reads during tangent construction and unchanged pre-division sides.

Ignored receipts: `conker/build/game-graph-edge-scopes/<mode>.json`.
These controls are evidence of rejected source shapes, not installed fixes.
Do not repeat these scopes, ordinary structs, operand swaps, or array spills
as promising routes to the retail frame/register allocation.

All three transformation/inventory tests pass in 0.013 seconds, no skips.
Project tool checks and whitespace checks pass. Production behavior is not
changed; the prior 62-test qualification is retained, not reported as rerun.

## Audit And Continuation

The live ELF matches all **6059** address/length/word hashes in the preceding
post-install receipt, including helper SHA-256
`f09995b4041d5bc71e391c716b87cd775b915726fe676b4d8928423d268c1530`.
No production source, guard CSV, compiler profile, assembly or protected
data changes. Counts remain total **3309/5462**, Game **2636/4789**, Init
**492/492**, Debugger **181/181**, zero drift and **2153** different Game C.
README aggregates remain correct and unchanged.

The helper still needs the retail 0x90 frame, minimum home +0x50 and normal,
side and second-plane constant lifetimes. Preserve the full-band filters,
finite-edge endpoint rules and last-fraction result from Notes 1025/1026.
The 198/207 executed-word coverage and full-chain/FCSR/gameplay boundaries
are unchanged; this tool audit adds no behavioral acceptance claim.

After banking this audit, inspect the closest remaining C match,
`func_150E6FAC`: 15 aligned differences from return-tail sharing, 71 emitted
words in a 72-word slot. Its calculation words already match; see
[Note 920](920-game-linked-record-position-stack-and-float-shape-20261004.md).
No broad guard replacement of the edge helper is installed.

## Reproduction

```sh
python3 -m tools.experiments.game_graph_edge_crossing_scopes --verify-checkpoint
python3 -m tools.experiments.game_graph_edge_crossing_scopes
python3 -m tools.experiments.game_graph_edge_crossing_scopes --planes
python3 -m tools.experiments.game_graph_edge_crossing_scopes --aggregates
python3 -m tools.experiments.game_graph_edge_crossing_scopes --sums
python3 -m tools.experiments.game_graph_edge_crossing_scopes --products
python3 -m unittest tools.tests.test_game_graph_edge_crossing_scopes -v -f
make tools-check
git diff --check
```

Checkpoint verification requires the preceding ignored
`conker/build/game-graph-edge-lifetime-test/after-slots.json` receipt; absence
is an error, not permission to assume equality. The other modes require the
retail image, IDO and MIPS binutils but do not need that receipt.
No sibling source/build/save/frozen Release change or push. Game goal active.
