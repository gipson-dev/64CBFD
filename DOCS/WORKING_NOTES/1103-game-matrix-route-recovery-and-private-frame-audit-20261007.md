# Game Matrix-Route Recovery And Private-Frame Audit

Date: 2026-10-07

## Scope And Installed Baseline

Continue Game matching from lighting-dispatch commit `e5a09efd`, with the
basis follow-up separately banked in `81c5cfb6`. Audit `func_1514654C`,
VA `1514654C..1514672C`, ROM `1739FC..173BDC`: **120 words / 480 bytes**.

The live [owner](../../conker/src/game_16EE20.c) and ELF still contain the
**three-word zero-return C placeholder**, padded to 120 words. The
[original assembly](../../conker/asm/nonmatchings/game_16EE20/func_1514654C.s)
is a reference, not the installed implementation. No conversion, semantic
replacement or byte match is installed in this batch. No production source,
header, compiler profile, guard row or root README edit.

## Recovered Contract

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_matrix_route_candidates.py)
recovers six incoming ABI words: actor, raw descriptor, signed matrix index,
input-point pointer list, output-point pointer list and signed count.

- Null actor, null descriptor or null actor bank at `+1D4` returns zero.
  These gates are lazy; they do not read unused descriptors or points.
- Descriptor attachment `+48` requires attachment byte `+3F6` nonzero.
  Select attachment's matrix-bank pointer at `+3E8 + page*4`, then add
  `index*64`. Page is the unsigned byte `D_800BE9C0`; no index clamp.
- Otherwise, nonzero unsigned-halfword key `+1E` calls
  `func_1503195C(actor,key,0)`. Null lookup returns zero. Resolve the node
  using `func_15031070(node,actor,&primary,&other)`; zero result returns zero.
  Only after resolution, reread the lookup's attachment `+48`. If nonnull,
  add descriptor's unsigned-halfword `+20` matrix offset to primary.
- Otherwise, descriptor matrix bank `+34` selects `bank + page*64`.
- With none of those routes, delegate to the matched `func_15145EA4` using
  actor bank plus descriptor byte `+2` times 64. Pass both lists and the
  unchanged count; return one regardless of the void helper's incidental
  return-register contents.
- Other routes reject a null selected matrix, convert the fixed matrix with
  `guMtxL2F`, then reload incoming list/count homes. Positive counts call the
  typed seven-word `func_150A7960` point transform, advancing both lists by
  four bytes. Zero/negative counts return one without dereferencing lists.
- Common fixed routes do not have the delegated helper's null/all-zero-point
  fallback. Preserve this distinction and the full zero/one return word.

The production resolver is still a separate zero-return placeholder. Tests
can connect its original instructions, but this does not recover that callee
into production C or establish PC-port runtime acceptance.

## Source Fit And Installation Gate

Selected `layout-key0-counter1-binding0-zero0` emits **119 meaningful words,
frame `0xA8`, 58 full-slot word differences**, no pool or isolated diagnostic.
Its isolated text section has 120 words because of a trailing alignment nop;
the function symbol/body is 119 words, not a complete 120-word matching body.
The point-call loop and all three cursor/counter
updates at `+16C..+1A8` emit directly as retail. The eight opening saved-
register/assignment words also agree.

The unresolved differences are substantive, not just independent scheduling:

| Private State | Selected C | Retail |
| --- | --- | --- |
| Frame | `0xA8` | `0xA0` |
| Converted matrix | `sp+68`, entry SP minus `40` | `sp+4C`, entry SP minus `54` |
| Resolver primary output | `sp+5C` | `sp+90` |
| Resolver secondary output | `sp+60` | `sp+8C` |

Lookup-key register/branch shape, primary reload order and common null/count
return topology also remain open. Some source forms obtain the `0xA0` frame
but emit 121 words and retain larger differences. Formal-list reuse controls
are ordinary-input measurements, not proofs of incoming-home equivalence.

Actual connected converter/point instructions expose public output
counterexamples when a synthetic guest input point overlaps retail's private matrix.
**Do not install this candidate or normalize frame/private offsets with
word guards.** Keep the production placeholder untouched while recovering
the original source allocation and branch shape. No guard generator, word
insertion, omission or bulk instruction replacement is added.

## Maintained Qualification

[Recovery tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_matrix_route_recovery.py) bind
the complete experimental wrapper, independent routing/math reference,
ordinary public-storage equivalence and explicit non-equivalence boundary.

- **6,916 routing fixtures**: four routes, lookup/resolver/null-matrix failures, signed counts, two
  ordinary pages, negative/positive valid indices, sequential point/output
  aliases, both stack phases and finite binary32 coordinates.
- **336 home-readback fixtures**, all seven combinations of the three incoming-home mutations after
  conversion, plus **24 attachment-change fixtures** during resolver callbacks. Caller-saved
  GP/FP registers are clobbered by bounded hooks.
- **866 connected fixtures plus six acyclic recursive cases**: original lookup (28 words), resolver (85), SDK converter (45 meaningful
  words), point transform (40), matched list wrapper (117) and translator
  (49), including delegated null/zero points. Observed helper coverage is
  21/28 lookup, 77/85 resolver, 45/45 converter, 40/40 point, 73/117 list and
  41/49 translator words; this is not complete callee-path coverage.
- Twelve required-storage faults, lazy null/unused-list gates and four
  guest-only wrapping index cases. Native C stays within valid matrix objects.
- **Sixteen private-matrix overlaps**, compared using actual original helpers.
  All sixteen produce public-output differences retained as rejection evidence.
- **208 source/profile forms**, none raw exact: 24 primary, 24 lifetime,
  36 branch, 32 register, 48 parameter-phase, 24 layout, 16 route/workspace
  and four compiler-profile controls. Ordinary-input qualification does not
  imply every form preserves lazy faults, private overlap or home timing.
  All **4,992 ordinary candidate executions** pass.
- Six compiled negatives require actual output/return differences, not an
  unexpected fault: attachment flag, page, index, lookup key, count gate and
  source stride. Matrices/pages are distinguishable and mapped for each probe.
- **9,216 native 32-bit cases plus three lazy gates**, actual complete
  selected C and actual SDK converter C, warnings-as-errors. Other native
  helper callbacks remain bounded validating models. No general FCSR claim.
- Copied owner: **89 functions / 88 unchanged neighbors**, same two warning
  statements, equal normalized data pools and target bytes/relocations equal
  to the isolated object. This is context qualification, not installation.

The initial harness assumed the original assembly was installed, omitted
unreachable branch-likely duplicates from coverage accounting and did not
exercise delegated translation. Live ELF inspection corrects the baseline;
explicit null/zero fixtures close the connected route gate. The first negative
page probe selected an unmapped matrix; valid distinguishable page pointers
replace it. These failed harness runs are not qualification receipts.

All **eight combined tests pass in 497.879 seconds**, zero skips, errors or
failures. Executable coverage is 114/119 selected words and 116/120 retail
words; the five/four remaining words are explicitly pinned unreachable
branch-likely duplicate loads, not omitted code. Tools, Python syntax and
scoped whitespace checks pass. The documentation checker verifies
**85 documents / 3,985 relative links / zero broken links**.

```sh
python3 -m unittest tools.tests.test_game_matrix_route_recovery -v
make tools-check
```

## Linked Audit And Resume

All **6,058 symbols / 6,042 retail slots / 16 overflow symbols** remain
identical to the lighting-dispatch checkpoint, including body bytes, addresses
and extents. All **11,063 guard rows**, protected Init/Debugger/Game-data
sections and conversion-ledger hash remain unchanged. All **720 Game-data
owners / 189,088 bytes** remain exact. No production rebuild is needed for
this experiment/documentation-only batch.

Matching remains **3,364/5,466 total (61.54%)**, **2,691/4,793 Game
(56.14%)**, **2,102 different**, zero address drift. Init is 492/492 and
Debugger 181/181 exact. README aggregates remain unchanged.

Resume source fitting from the selected driver's complete contract and
private counterexample, not from a new guessed body. Recover frame `0xA0`,
matrix `sp+4C`, primary/secondary `sp+90/+8C`, original primary read order
and full 120-word branch/return topology. Requalify private overlaps and
incoming homes before considering any narrowly proven register/scheduling
guards. Preserve matched neighbors `func_151464B8`, `func_15146508` and
`func_1514672C`. Resolver C recovery, basis layout, translator scheduling and
sampler lifetime remain separate work.

No sibling repository, frozen Release, real save, runtime/hardware or push work.
