# Game Record Ring Renderer Setup Fitting

Date: 2026-10-08

## Result

Continue the same complete `func_151D80C4` from
[Note 1141](1141-game-record-ring-renderer-scheduling-audit-20261008.md) under
the [focused workflow](../AGENT_WORKFLOW.md). VA 0x151D80C4..0x151D8718,
ROM 0x205574..0x205BC8: **405 words / 1,620 bytes / frame 0xD0**.
The new complete C baseline reduces raw differences **198 -> 185**, restores
retail's mode-input load order and eliminates default-factor hoisting into the
XYZ-copy block. Private slots, saved-register slots, loop and memcpy offsets
stay fitted. This is fitting progress, **not a byte match or installation**.

Use **`SETUP_FITTED_NAME = retail-mode-order-reverse-factor` / `SETUP_FITTED`**
next. Preserve the older 198-difference `FITTED` and 319-difference natural
`SELECTED` as separate controls, not the active fitting baseline. No dead-local
padding, injected instructions, smaller substitute function or profile change.
Keep [original assembly](../../conker/asm/nonmatchings/generated_204660/func_151D80C4.s)
and the [complete owner slice](../../conker/asm/204660.s).

Fresh **22 focused tests pass in 134.298s**, no skips: sixteen tests for the
new complete body, four previous scheduling tests and two original/fitted
baseline checks. This is not a fresh run of every test in the expanded module.
The prior full 25-test receipt in Note 1141 remains historical. Seven protected
fingerprints, all **6,058 installed linked bodies/addresses/extents**, data,
source, assembly, Makefile, progress and **11,275 guards** are unchanged.

Converted totals stay **5,481 / Game 4,808**; exact **3,392 / Game 2,719**,
zero drift and 2,089 different. The last installed conversion remains
[Note 1138](1138-game-record-ring-shaping-conversion-20261008.md).
The target remains byte-exact retained assembly, with no C-conversion credit.
Root README remains aggregate-only and unchanged.

## Source And Schedule Findings

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_renderer_candidates.py)
adds fourteen complete `setup_candidates()` and a mutually exclusive `--setup`
screen. The fourteen recovery, 37 fitting and 26 scheduling forms are retained.

Changing the source OR expression to `D_800A4AC8[2] | D_800A4AC8[3]` makes
this IDO profile load +0xC before +0x8, as retail does. The compiler evaluates
these operands in reversed source order. The value and raw difference count
alone do not show this improvement; the emitted access-order test does.
This is not a portable C evaluation-order or missing-memory guarantee.

Reversing the factor source condition puts the constant-default arm first and
the scaled arm second. The emitted default is no longer hoisted into the
current-XYZ copy. Both arms still produce 255 or the low byte of signed
opacity times twelve. The new branch layout differs from retail; do not call
the predicate inversion and arm reordering independent scheduling words.

| Complete O2/g3 Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Older fitted baseline | 405 | 0xD0 | 198 |
| Retail mode-input order alone | 405 | 0xD0 | 198 |
| Reversed factor branch alone | 405 | 0xD0 | 185 |
| Retail mode order and reversed factor branch | 405 | 0xD0 | 185 |
| Conditional factor | 405 | 0xD0 | 198 |
| Default assignment before branch | 404 | 0xD0 | 323 |
| Signed / unsigned common narrowing | 404 | 0xD8 | 333 |
| Signed byte factor, unsigned products | 405 | 0xD0 | 226 |
| Two narrowed scaling stages | 405 | 0xD0 | 224 |
| Narrow opacity before scaling | 405 | 0xD0 | 198 |
| Index temporary for factor scaling | 406 | 0xD0 | 310 |
| View temporary for opacity | 406 | 0xD0 | 324 |
| Switch with default-factor case | 405 | 0xD0 | 196 |

Additional ignored width/control trials do not improve 185; they are not
installed or deep-qualified alternatives. The tracked fourteen complete forms
each pass the ordinary captured-buffer/copy-mutation fixture, not full-domain
or native32 sweeps for every alternative.

| New Complete Body Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 405 | 0xD0 | 185 |
| O2 | 405 | 0xD0 | 262 |
| O1/g3 or O1 | 491 | 0x90 | 484 |

No isolated diagnostics or data pools. Preserve cursor SP+0x8C, sync +0xA7,
captured buffer +0xA8, previous XYZ +0xB4, current XYZ +0xC0, GP saves
+0x48..+0x6C, F20/F22 +0x38/+0x40, loop +0x3E4 and memcpy +0x56C.

## Fresh Qualification

The [renderer suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_renderer_recovery.py)
gives the new body its own `setup-fitted/` receipt directory, retaining existing
natural/fitted paths. Reuse existing parsers, native32/MIPS models, aliases,
rebases, copied-owner and real-padder gates; no shared production helper edits.

- **988 guest cases**, **512 current/count cases plus three lazy layouts**,
  **1,086 native32 cases**, **22 required-byte fault gates**, eight effective
  compiled negatives and four profiles requalify the new complete body.
  Compare complete public memory, callbacks, return cursor and ordered stores;
  preserve saved GP/FP lifetimes. Finite bounded conversion models do not
  establish hardware FCSR/traps or invalid portable C casts.
- **256 connected cases / 512 executions** retain original 52-word caller
  `func_15147C4C`, render-table callback 16 and actual 52-word backend
  `func_151D5D60`. Deep allocator, graphics setup and memcpy stay bounded;
  alternate dispatch/release and hardware/gameplay remain open.
- **64 guest aliases / 128 executions** and **four independent symbol sets /
  768 executions** requalify the revised object against separately GNU-linked
  original assembly. Preserve all sixteen symbolic uses, HI16 carry/LO16 sign,
  JAL regions and complete ordered public outputs without normalization.
- **432 ordinary whole-entry public access-prefix cases / 864 executions**
  compare all public reads/writes and call markers, three phase patterns,
  views 0/3/-1, both SP phases and six mutation modes. Complete memory,
  including private stack bytes at completed exit, agrees in all 432 cases.
  This is not a private GP/FP register-state or intermediate-store-order proof.
- **668 early fault-prefix pairs / 1,336 executions** remove every byte read
  before the first vertex store, plus every byte of that first vertex. Four
  flag modes and two SP phases. Both raw candidate and retail fault, with
  equal whole-entry public prefixes, public memory and calls. This covers the
  mode inputs and seed setup; private fault state/store prefixes are excluded.
- **408 final-lookahead fault-prefix pairs / 816 executions** requalify all
  seventeen required XYZ/alpha/phase bytes after the final wrapped segment,
  counts 4/128/255 and both SP phases. Equality is explicitly post-MODE, not
  every possible fault point or portable C/hardware fault behavior.
- A complete **405-word/frame0xD0 mode-order negative also has 185 raw
  differences**, and passes sixteen ordinary output comparisons. Sixteen
  missing-input-byte witnesses expose its extra +0x8 read before the required
  +0xC fault. Candidate/retail agree; the negative differs. Four flag modes and
  all four bytes of that input. No timeout or unsupported-opcode witness.
- Both copied owners preserve **22 neighbors**, relative relocations,
  normalized pools and four existing diagnostics. Isolated and owner target
  bytes agree. The actual padder accepts 1,620 bytes without slot padding or
  new guards; accepting the extent does not prove a byte match.

The four previous scheduling tests freshly retain the 198-difference control,
its 26 complete forms / 364 bounded cases, final-lookahead prefixes and effective
early-exit witness. The natural shape and older fitted private layout checks
also pass. Other unchanged neighbor suites are historical, not fresh runs.
Linked dispatcher/combiner zero-return placeholders are not restored here.

## Remaining Mapping Boundary

Syntactic partition: **176 GP-field-only, zero FP-only, zero combined and nine
other differences**. The other offsets are **+0x14, +0x34, +0x278, +0x280,
+0x284, +0x288, +0x290, +0x294 and +0x298**. The first two are S2/S3 save
ordering; the rest are the factor predicate and two-arm layout.

Crucially, GP-only **+0x28C also belongs to that reordered factor block**:
retail is finishing the times-twelve shift while the new layout is starting
the times-four shift. Equal opcode/literal fields do not make it a standalone
rename. Treat all **eight differing factor-block words** together. The
remaining 175 GP-field-only words outside that block still require consistent
live-value and saved-lifetime mapping, not ordinal mask agreement.

Next steps for this same complete target:

1. Start from `SETUP_FITTED`, not the old 198-difference body. Retain the
   restored mode read order and already-qualified private layout.
2. Fit retail's factor-arm layout naturally, or prove a closed predicate/arm/
   delay-slot transformation across +0x278..+0x298 and its +0x29C join.
3. Derive and prove consistent GP live-value mappings across the whole CFG,
   including S2/S3 saves/restores and +0x28C's block membership. Qualify
   intermediate private state and fault boundaries before proposing guards.
4. Requalify the complete revised/normalized body with native32, rebases,
   aliases, prefixes and connections; only then install/rebuild/audit every
   body/data/guard/progress row and refresh measured README aggregates.

No broad 185-word normalization batch, alternate smaller function or conversion
credit. Wider Game, linked setup, hardware/gameplay and graph repair remain open.

## Banking And Checks

Entry parent `511e11e8582aa6ce1a75d262b560db092f769447`, mounted tools
`1f3f5be6b6ff84cdf7c33476437ac89044c34a00`: clean. Per **"Keep commited"**,
bank the two reviewed tools files first at
**`b0f5e404a8c695a3b978b571fd7b729ebd9d8819`**, then this note, concise indexes
and that exact parent gitlink. No push.

Older standalone tools HEAD stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`.
Only the two reviewed renderer files are mirrored after prior-hash checks;
their bytes agree, and its exact pre-existing dirty status/history is unchanged.
No reset/stash or duplicate commit. Fresh **14 shared matcher/padder/setup
tests pass in 0.147s**, both tools project checks and new CLI help pass.
Fresh syntax/mirror and scoped documentation checks pass **128 documents /
4,101 relative links / zero broken links** before parent banking; remote
publication is not verified or authorized.

All seven protected SHA-256 fingerprints remain unchanged, including full ELF
`f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`.
Ignored sources/receipts remain under `conker/build/game-record-ring-renderer/`
and `conker/build/game-record-ring-renderer-test/setup-fitted/`; no ROM or
transient artifact tracked. No host/runtime/save/Release or account changes.

Graph query precedes investigation. Fresh `graphify update .` exits one,
refusing **16,848 nodes over the retained 38,637-node graph**; preserve 19,398
nodes from 2,972 still-existing excluded files. No force, upgrade, changed
ignore policy or graph-repair claim. One Codex writer, zero Claude calls.

```sh
python3 -m tools.experiments.game_record_ring_renderer_candidates --setup
python3 -m tools.experiments.game_record_ring_renderer_candidates --setup --form retail-mode-order-reverse-factor --profiles
python3 -m unittest tools.tests.test_game_record_ring_renderer_recovery.GameRecordRingRendererSetupFittingTests -v
```
