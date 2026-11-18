# Impact terminal callback semantic qualification and layout boundary - 2026-11-18

`func_150B8F44` has a complete **uninstalled semantic C candidate**. IDO emits
**390 words / 1,560 bytes**, with the original **416-byte frame**; retail is
**391 words / 1,564 bytes** at VA0x150B8F44..0x150B9560, ROM0xE63F4..0xE6A10.
The unshifted comparison still has **369 word differences** including the
one-word length deficit. This is not byte-exact matching. No source, production
object, ELF, guard history, compiler profile or root README is changed.

Production remains the verified image from
[Note2543](2543-game-amplitude-terminal-callback-guarded-byte-match-20261118.md):
**4,549 / 5,514 (82.50%)** total, **3,876 / 4,841 (80.07%)** Game, Init 492/492,
Debugger 181/181, zero drift and 965 different. **138 further matches** reach 85%
at this denominator. No new matching credit or fresh production-rebuild claim.

Starting commits: consumer `eb991157443d9c7db9076c3bfcf698bc7c347568`, tools
`4624e0313dd3713df25c2e936ad9d5901b226ba0`. The ignored
`conker/build/game-next-150b8f44-private` packet freezes **1,747 inputs** using
1,733 links to immutable snapshots and 14 independent copies, no live-file
hard links. All frozen live inputs remain byte-identical. The maintained
`game_impact_terminal_150b8f44` tools stem contains the C draft and its checks.

## Recovered interface and behavior

The genuine original dispatch selects **D_80089974[1]**. Its five arguments
are actor, the caller's local collision record, and old X/Y/Z. Preserve this
interface; the adjacent amplitude callback has a different six-argument ABI.
The collision record's measured position fields are +0x14/+0x18/+0x1C.

The gate uses actor+0x140 minus the absolute actor+0x48 component, with an
ordered comparison against 6.0f. The low/unordered branch zeros +0x44/+0x4C,
damps a positive vertical component, copies the collision position, scales
three other components, submits the full 64000 volume word and returns 1.
The high branch calls the class-position predicate with three narrowed signed
halfwords. When allowed, it queries the old-to-current segment and classifies
the resulting hit. Accepted hits create a randomized 88-byte burst and optional
8-byte extra copy. Every successful segment query submits a **164-byte impact
spray**, whether or not the classified hit permits the burst. The high branch
always reaches its late randomized sound and returns0, including query rejection
and allocation failure.

The collision query writes **18 bytes** of metadata, a 12-byte position and a
32-bit hit index. The spray copies all 18 metadata bytes, three negated retained
deltas and the possibly provider-mutated position. Unknown fields retain offset
names. The extra object's four unwritten bytes are intentionally retained; the
original copies all 8 bytes. Do not zero them or substitute the adjacent callback's
136-byte spray type.

Fourteen local-layout/lifetime screens retain all seven owner neighbors and
constant pools. Eliminating the unnecessary cached scale variable recovers the
416-byte frame from 424; no dummy padding or fixed-register assembly is used.
Selected raw SHA:
`fef5d1df33af00b1a3219da75e6b66a134ee98337411a880fa8a874fc212befb`.
Independent GNU assembly SHA:
`e9e2eb66e2f1c6becd7d0a6d3f899659f7adc2deaa8a0264c3c83109f91c716d`.
Assembly words/bindings are independently checked against the original ROM.

## Fresh qualification and its limits

Both final configurations pass **four tests**, no failures, errors or skips:
**71.196s primary / 81.742s private sibling overlay**.
Each seals **317 imported tool files** and all seven
task artifacts. The overlay uses 339 matching sibling files, 440 unchanged primary
fallbacks and the seven task files; it does not modify the actual dirty sibling.

- Full-owner IDO compilation preserves all seven other function bodies/bindings
  and normalized constant pools. The complete proposed owner and both independent
  function objects remain in the ignored packet.
- Guest: **2,304 cases per raw/retail stream**, all88 burst and164 spray bytes,
  all8 extra bytes,18 metadata bytes, public memory, call transcripts, returns
  and saved GPR/FPR/SP custody. Cases cover exact/adjacent thresholds, vertical
  signs, narrowed coordinates, every helper/allocator outcome, two stack phases,
  deliberate provider changes and guest-only incoming-home mutation. It visits
  390/391 original words and 389/390 source words. Original word 334 is an
  unreachable duplicate zero initialization and is retained in the retail fixture.
- Native SDK32: **864 cases each at O0/O2/O3**, strict aliasing and UBSan, with
  independent retail call transcripts and **eight effective negatives** for the
  gate, duration, descriptor kind, extra length, metadata, spray kind, volume and
  return. Native observations cover 78/158 initialized descriptor bytes and four
  initialized extra bytes. It does not assert native values for unwritten bytes.
- Genuine caller window **0x15133264..0x151332A8**, with early return0x151332C8:
  **768 cases per stream**, all 17 window words, disabled selector, both callback
  results, all five arguments, actual stack-local record and saved-register
  lifetime. The complete larger `func_15132DDC` parent is not qualified here.
- Fresh `make tools-check` passes. Routine work uses zero Claude calls and no
  REA configuration changes. No host build, Release/save change or gameplay/
  hardware acceptance is claimed.

The guest model seeds corresponding logical objects separately for each stream;
its descriptor comparisons do not establish literal private-frame identity.
The raw named objects and integer spill sit four bytes above their retail homes,
despite equal frame sizes. Saved S0/S1 roles and FP allocation/scheduling also
differ. Model agreement is bounded to the declared arithmetic and defined signed32
conversions; an unordered gate case does not qualify arbitrary NaN payloads,
FP exception timing, FCSR identity or every fault prefix. Opaque services,
including collision query/classification, factories, spray and audio, remain
modeled boundaries. No source-derived instruction relation or guard is installed.

## Continue this function

1. Resolve the 390/391 extent difference and the four-byte private-home shift;
   use the captured owner objects and full disassemblies rather than adding
   padding to the source. Inspect the query's retained Z spill/reload and the
   low-branch zero/register lifetime first.
2. Prove the complete private/provider/register/FP instruction relation,
   including retained metadata/position and the four untouched extra bytes.
   Keep finite arithmetic limits and effective counterexamples explicit.
3. Only after that proof, derive normalization from source fields if needed,
   qualify both real padders, guard corruptions and independent GNU rebases,
   and connect the relevant actual child instructions.
4. Run actual Make and the independent strict whole-image predictor, then
   production adoption, all-body/address/protected-data audit, installed tests
   and fresh recount. Credit only the verified result.

The native Graphify update exits1 while retaining all66,229 existing nodes: its
guard rejects an incomplete27,105-node scan. The subsequent scoped AST extraction
of six files and explicit source-target reference retain every old ID and produce
66,275 nodes /130,535 links before the commit hook. No full-corpus re-extraction
is claimed. Tools are committed before the consumer
documentation and pin. No push or automatic pause; the 85% goal remains active.
