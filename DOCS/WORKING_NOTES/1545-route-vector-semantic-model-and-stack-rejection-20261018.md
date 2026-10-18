# Route Vector Semantic Model And Stack Rejection

Date: 2026-10-18. Consumer predecessor **de9720e6**; tools predecessor
**0d4af42**, new tools checkpoint **81049a4** banked first. Target
**func_15088F30**, owner `generated_B3020`, VA **0x15088F30..0x1508907C**,
ROM **0xB63E0..0xB652C**, **83 words /332 bytes /frame0x10**.
This checkpoint qualifies a **non-installable experiment**, not a new match.
Production source, guards, build profile, ELF and root README are unchanged.
The wider Game matching goal remains active.

## Recovered Contract

Use `void func_15088F30(u8 *record, f32 *x, f32 *y, f32 *z)`; observed callers
ignore V0. Do not invent a semantic word return from retail's final loop count.
Keep the address-based function name and a concise control-point comment.

Process four record IDs at +0x2B..+0x2E, advancing the byte cursor by one.
An FF ID emits `(float(slot*64), +0.0f, +0.0f)`. For each valid ID, freshly
load the table pointer through D_800D2350 and use 0x10-byte route records.
Scan exactly five neighbor IDs at +9..+0xD; ignore FF and select the **first
type4** entry at candidate+0xE. If none qualifies, select the current record.
Class byte+0xF is irrelevant here, unlike the parent's last-class scan.
The assigned `i=5` exit still performs the loop increment before terminating.

Read signed-halfword currentX, selectedX, float record speed, selectedZ and
currentZ in that order before the first output store. Convert full signed32
coordinate differences to float; do not narrow the differences to s16.
Store X using the captured speed and delta, then freshly read/store currentY.
After Y, freshly read currentZ and record speed for the Z store, using the
previously captured deltaZ. Advance each float output by four bytes.

Outputs may overwrite record speed, later neighbor bytes, route fields or
the table-pointer word in the guest address model. The current point must
retain its captured table, while later valid points reload the global.
Do not cache Y/Z or speed across the intervening output stores. Incompatible
float/halfword/pointer guest aliases are not claims about portable native C.
Hardware FCSR, NaN payload selection, unaligned accesses and MMU behavior
remain outside this bounded qualification.

## Why Installation Is Rejected

`tools/experiments/game_route_vector_builder.py` retains bounded source
forms and pins the selected `assigned-exit` semantic model. It compiles under
the existing B3020 O2/g3 compiler-only no-unroll profile to **83 words,
frame16, no diagnostics**, but still differs from retail in **76 words**.
Most visibly, its saved-register layout is wrong:

| Body | Saved Registers And Homes |
| --- | --- |
| Retail | S1 at SP+0xC; S0 at SP+8 |
| Model | S2 at SP+0xC; S1 at SP+8; S0 at SP+4 |

The model saves output cursors; retail keeps them in T2/T3/T4 and saves the
global table-address invariant in S0 and shared type/loop constant4 in S1.
The first private-store fault leaves different stack bytes, not just a dead
register difference. The necessary retail stack gate therefore rejects it.
That gate is not, by itself, a complete matching or installation decision.
No broad expected-word normalization, assembly substitution or matching
credit is added. The real padder preserves the model and its bindings but
does **not** make it equal to retail.

Retained probe receipts also show: initial break form87/frame24;
reconstructed form82/frame16; chosen-index form84/frame16. The
named-invariants reconstructed form has82 words and two saves, but introduces
extra global loads and changes the X-versus-Z read order. It is not a valid
replacement. Whole-owner versus isolated compilation and bounded alternate
profiles did not resolve the contract. No compiler/profile change is installed.

## Focused Qualification

New test module: `tools/tests/test_game_route_vector_builder.py`.
Ignored sources, objects and JSON receipts live under
`conker/build/game-route-vector-builder/`. Thirteen frozen input fingerprints
cover the owner/ELF/guards/ROM, retail assembly, Makefile/symbol/header closure
and four prepared IDO components. They do not cover every unlisted dependency.
The model is tied to this physical baseline; do not relax its checks to reuse
it after a later production edit without a deliberate predecessor view.

All **seven tests pass in107.818s**:

```sh
python3 -m unittest tools.tests.test_game_route_vector_builder -v
```

- **9,205 paired raw-model/retail guest cases** compare complete public memory,
  exact interleaved read/write traces and saved ABI state. Exercise all243
  neighbor categories, all16 FF masks, signed coordinate boundaries, sixteen
  speed bit patterns, ten guest aliases and IDs0/127/128/254/255. Visit82 words
  in each body; raw word67 and retail word68 are unreachable duplicate MTC1
  paths. The full83-word slots are retained, not shortened.
- **74,696 native32 cases per O2/O0 UBSan profile**, including all65,536 signed
  coordinate values. The exhaustive arithmetic case independently expects
  X/Z=-0.5 for opposite signed coordinates. Compare full output/record/table
  buffers and pointer canaries. Five valid float-buffer aliases use typed
  union backing; short-table/global-pointer/metadata aliases remain guest-only.
  Native NaNs compare class, not payload; no `-fwrapv` or alias bypass is used.
- **Thirteen guest /ten native effective controls** change public results for
  wrong neighbor priority/scan/type/sentinel, coordinate signedness, narrowed
  differences, Y field, fallback spacing, output stride or stale speed.
  Guest-only cached Y/Z/table controls fail on actual alias witnesses.
  Native controls exit wrong-result23, not a crash. Independently linked
  controls include their literal pools at a private code placement.
- **869 matching public fault prefixes across22 fixtures** preserve public
  memory/trace order. A separate first-save fault proves unequal private
  bytes: raw writes S2 at entry-SP-4, retail writes S1 there. Full private or
  dead-register fault-state equality is explicitly not claimed.
- **Nine independent original/raw/padded links and198 three-way executions**
  rebase code and the global pointer through HI16/LO16 carry boundaries.
  Raw and actual padded model words/bindings agree; retail remains different.
- **144 paired complete118-word parent executions** run555 connected helper
  words, substituting the actual model for only the vector helper. The sole
  bounded provider is u16 atan. The proposed typed void declaration preserves
  every raw parent word and all14 relative bindings. All72 raw owner neighbors
  and normalized pools remain fixed. Production vector and spline helpers are
  still stubs; these overlays are not gameplay or production-chain acceptance.
- Mutation checks reject all83 raw words, both bindings, all26 live/snapshot
  input alterations and three stack-contract corruptions. All13 physical
  baseline fingerprints still agree after qualification.

## Advisory Reconciliation

One packet-only Claude Code Pro review completed with no tools/MCP servers;
no second call or retry. Receipt/answer are ignored task artifacts. Packet
SHA-256: `3a1ae7c2ef77f610c205f3900051f7ed52f1361b11dcd4281c3cbb7959ea99a8`.
Codex verified the suggestions: chosen-index still emits84 words/three saves;
caching currentZ violates the fresh read and guest alias contract; indexed
route lookup was already tested. No advisory suggestion is installed merely
on agreement, and unproven compiler-policy explanations remain hypotheses.

## Preserved Baseline

| Artifact | Unchanged SHA-256 |
| --- | --- |
| Whole ELF | a5c5541dc8f6863ebefac2896237ce0bc39a88e3893711c35cd0393fd851ecd7 |
| Owner source | ce0cf9b5504e5b41b267c09d69c3bdc9ed2f24533ed7de0dd68935bd678f467f |
| Guards | eb4dc7f42da17c278c908b8e5ab721c4b420edd2210b4a691c343b8aa0fcfd42 |
| Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |
| Qualified raw model | 83c683a0d268e3df6320b192ca130970b42d7de2d7dd837ae616d717e9999374 |

Shared padder/PC16 tests pass eleven per tools copy, both smoke checks and
root tools-check pass. Four task copies pass ASCII/AST parsing; both pairs
are byte-identical. Older mirror HEAD ddbdd16 is unchanged: preserve all
**1,216 previous dirty hashes**, adding only two absent task files for1,218.
No mirror commit/reset, push, host or frozen Release action. The user confirmed
the accidentally overwritten `.../.vscode/Conkers` file was disposable scratch;
no recovery is needed. Compiler outputs now use relative paths without spaces.

No production rebuild or matching recount is needed for unchanged production
bytes. Last verified official totals remain **Game2,982/4,828 (61.76%)**,
**total3,655/5,501 (66.44%)**, Init492/492, Debugger181/181,
**1,846 different /zero drift**. Conversion counts/bytes also stay fixed.
Root README is untouched; this checkpoint earns zero matching credit.

## Resume Here

1. Fit invariant/register lifetimes while preserving the now-qualified public
   trace. Retail requires S0=&D_800D2350, S1=4, T2/T3/T4 output cursors, only
   two saves at their original homes, the duplicate candidate shift, original
   branch/delay layout and float operation order. Public equivalence,83 words
   or two saves alone are not sufficient. Use small discriminating probes;
   do not repeat the full retained source/profile screen by default.
2. Once a candidate satisfies the real private contract, qualify its entire
   owner, typed parent interface, actual padding and independent rebases.
   Prove any proposed guards are closed transformations before a first
   whole-link prediction, installation and complete linked audit. No automatic
   installation path or guard generator exists in the current experiment.
3. Then recover spline stubs `func_150497E0` (49 words) and `func_150498A4`
   (62 words). Parent `func_15087350`, retained assembly and wider queues stay
   open. This model checkpoint is progress, not completion or a blocked goal.

Scoped Graphify refresh: **42,527 nodes /82,600 links /4,101 communities**.
Retain19,398 nodes from2,972 excluded-but-existing files; no full-scan purge.
All42,514 other old IDs persist. Three line-disambiguated UPDATE_LOG heading
IDs relocate with their labels preserved; the new note contributes eight
nodes. Tools remain subject to the configured submodule scan exclusion, not
a fresh graph AST-coverage claim for the new experiments. Original graph and
ID-preservation audit are ignored task artifacts; no history rewrite.
