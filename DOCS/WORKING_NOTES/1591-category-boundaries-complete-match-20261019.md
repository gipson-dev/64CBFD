# Category Boundaries Complete Match

Verified:2026-10-19. **Installed complete C recovery: all112 words /448 bytes
match retail, including frame96, scratch arrays and initializer/access order.**

Finish `func_15085BE8`, generated_B3020, VA `15085BE8..15085DA8`, ROM
`B3098..B3258`, after
[Note1590](1590-category-boundaries-semantic-recovery-and-layout-boundary-20261019.md).
Consumer predecessor **4c026176**, tools predecessor **46c5d3c**. Bank tools
**6dbeb82** before the consumer source/guards/docs/pin. No push.

## Source Recovery

Retain Note1590's complete category-extrema, compact-ID, midpoint, strict
overlap and unconditional sentinel semantics. Use a signed32 no-argument
result and upgrade the existing forward declaration to `(void)`. Keep the
confirmed height-boundary comment and meaningful category/minimum/maximum
names; do not invent original source names or a speculative record type.

The source now genuinely reads maximum initializer D_8009D9C0 before minimum
D_8009D9C4. Reuse the real upper/lower scalar lifetimes for initial fills,
row height and later adjacent extrema. Place the two six-float arrays after
the scalar/pointer declarations. This recovers **maximum at SP+0x18, minimum at
SP+0x30, frame0x60**, without padding locals or a frame/address patch.

The row scan uses a logical index below signed16 D_80087290 and computes
row=D_800D2350+index*16 in the body. IDO recovers retail's scaled byte cursor,
positive-count entry, two entry clears and post-loop reset. No explicit outer
gate/product-bound combination or new branch patch is needed. Initialization
and row access are now in the original order; all normal inputs and the backed
guest aliases below also retain the complete raw private memory/access trace.

The accepted readable source emits **112 words/frame96**,35 allocation/schedule
differences, with empty diagnostics in both complete-owner profiles. New
screens compare explicit initializers, scalar reuse, logical/byte indices,
single/duplicate gates, scratch placement and inline extrema; none is an
automatic acceptance criterion. The previous unqualified112/40 screen with
an unused bound local is not used. No dummy effect, volatile, physical-register
binding, compiler/profile change, shared-pad change or assembly/data edit.

## Explicit Recipe

`game_category_boundaries_layout.py` specifies only:

- The initial F0/F2 allocation exchange, including loads and stores, while
  preserving the already-recovered initializer memory order.
- Row-loop GP roles at origins20..47, the two later base definitions at52/53,
  final-loop roles at75..103 and final scratch-shift role at106/107. The
  source category value and subsequent maximum pointer have disjoint live
  ranges coalesced into retail V0; this is a lifetime mapping, not a blanket
  whole-function register substitution.
- The final extrema F0/F2 exchange. Decode only actual FP fields: arithmetic
  FS/FT/FD, comparison FS/FT, or LWC1/SWC1 FP register. Do not treat comparison
  CC fields or COP1 branches as FP registers.
- Swap origins89/90, two independent **ADDU** address calculations. Validate
  both opcodes and that neither destination is an operand of either add.
  They cannot trap, and no memory operation, comparison or branch moves.

All112 source origins are retained exactly once. All20 HI/LO bindings remain
at the same positions with the same symbols. Opcodes, immediates, frame and
comparison CC bits are unchanged. Thirty-five expected-word/relocation rows
encode the recipe and preserve the old manifest prefix byte-for-byte. Exact
raw SHA, binding dictionary and normalized SHA gate the transformation.

```text
raw:        6b07847f295342b95623749ed173b20a3c0969dd8dda5f9831ef329c18148a77
normalized: 9111eb1829ded7f968afba03b8f8449dd03b722f1017dd9d2231b4633c486e4d
```

## Fresh Qualification

All **12 pre-install tests pass in24.624 seconds**; the strengthened canonical
symbol assertion also passes its focused pre-install rerun. **All12 installed
tests pass in32.835 seconds**, without skips. Repeated corpus, caller and maps
are not additional independent input domains.

- **677 fixtures/two phases:1,354 full literal-state pairs** agree in GP,
  FP, LO, private/public memory, ordered events, return and modeled compare
  condition. The same corpus separately checks raw C against the independent
  public reference and ordered public stores; all112 words are visited.
  Raw C also matches retail's **entire private memory and access-event trace**,
  despite its different scratch register names.
- **364 fired access-cut pairs** confirm each requested address. Normalized
  and retail states agree at every cut; raw C's partial private memory/events
  and requested address agree too. The old cut0 initializer-order failure is
  resolved by source recovery, not bypassed by a guard. This is modeled order,
  not evidence of hardware exceptions or FCSR equivalence.
- **34 completed backed guest cases** cover categories6/7/8/31/255, including
  maximum[6] overlapping minimum[0], plus row pointers into both initialized
  scratch arrays. Additional scratch reads are explicitly backed with finite
  floats. Retail/normalized state and raw private traces agree. These are
  emitted-binary guest checks, not portable/native out-of-bounds C claims.
- Native32 **O0, O2 and O2+UBSan** each pass677 full-buffer fixtures, all
  **65,536 signed16 height views per category** and **32,769 nonpositive count
  views**. As in Note1590, the single-category sweep checks public ID/count/
  sentinel behavior, not invisible extrema. Paired ranges discriminate signs,
  clipping, equality, ordering, gaps and overlap. Native categories are0..5;
  all evaluated rows are backed. Check all1,024 input bytes,16 ID bytes and
  seven boundary-buffer words, including the unchanged spare before IDs.
- Five effective native C negatives change signed height, active equality,
  overlap equality, midpoint arithmetic or sentinel. Each exits21; positive
  profiles exit0. No signal/trap is accepted as a successful negative.
- **80 actual six-word returning-caller pairs** retain JAL/NOP, RA reload,
  SP+18 and JR/NOP at15085BD0 /B3080. The aligned ROM scan finds one direct
  site. Its24-byte frame is an explicit live-in; upstream loading is not
  executed and scratch-register identity is not asserted for raw C.
- **Three GNU maps /144 executed cases** independently assemble identical
  retail/normalized code and all20 bindings, including HI/LO carry boundaries.
  Code, all eight global/constant anchors and rows are rebased. The inherited
  separate raw-C map check also passes; its repeated fixtures are not a new
  domain or a claim that unnormalized instructions are identical.
- Twenty-seven raw/binding/recipe corruptions reject. Six actual-padder stale
  manifest controls fire; five changed-image controls reject, including symbol
  value and symbol-string corruptions. The early cut harness now compares
  compare-condition definedness before the first FP comparison, rather than
  assuming the model already has a condition field.
- Both owner profiles and actual padding preserve72 other routines and
  normalized pools. All73 owner addresses remain fixed. Seven expanded Make
  commands reproduce qualified raw code, bindings and padded metadata.

## Strict Image And Production

The initial code/size-only prediction correctly rejected the first private
image: the new constant references also changed symbol serialization. Diagnose
the **whole image**, not a broad canonical-symbol exclusion. All symbol
identities, values, sizes, info and section indices are unchanged except the
target size12 ->448. Only these exact contiguous runs reorder:

```text
C0, D_8009D1E0, D_800A6060 -> D_8009D1E0, D_800A6060, C0
C4, D_8008A450             -> D_8008A450, C4
func_15044964, D_800A0500   -> D_800A0500, func_15044964
```

Here C0/C4 mean D_8009D9C0/D_8009D9C4. Predict the exact seven symbol rows
and corresponding bounded string runs, validating the old names, contiguity
and literal strings. Preserve all fields other than their string offsets.
The canonical-symbol assertion independently requires only the target size
change. Initial failed receipt/diagnosis are retained, not presented as a
first-attempt prediction success.

The corrected strict prediction and actual production Make agree across the
entire3,257,636-byte ELF: **414 changed bytes =337 target-code bytes +two
target-symbol size bytes +75 serialization bytes** (33 symtab,42 strtab).
Every other6,056 linked body, every function address, all189,088 protected
Game-data bytes /720 owners and all other frozen inputs stay fixed. No
metadata permutation is performed on the actual output to make it pass.

The full manifest-triggered rebuild succeeds with inherited duplicate
generated_12D630 recipes and diagnostics from untouched code. Target owner
profiles have empty diagnostics, not the whole build. Full ignored log:
`conker/build/game-category-boundaries/lifetime-fit/integration/production-build.log`.
Git's existing CRLF advisory is not a manifest parse/build failure.

```text
owner:  f6aa1bdcd664ae77bb54512d09baac1a6277f6bafc959743ea10a05ff37c5f57
guards: d59c93d7b205eb3f77acd7715b29e87fc447b5f2094bc5ffef81b0f07081f2df
ELF:    06b437552ed0b3d57ac5522b1d821f063f150fa77c053b993dd4534d30914505
```

Fresh matching: **Game3005/4832 (62.19%)**, **total3678/5505 (66.81%)**,
Init492/492, Debugger181/181, **1,827 different / zero drift**. Conversion
counts/bytes remain5505/6044 (91.08%),86.08% overall and4832/5323 (90.78%),
85.44% Game: the old stub already counted as C. Root README gets aggregates
only; this note owns the recovery narrative.

Both tools copies pass three setup tests and smoke checks; consumer
`make tools-check` passes. Four new task files are identical ASCII/Python in
the standalone mirror. Preserve its ddbdd16 HEAD and all1,351 previous dirty
leaf hashes; four additions make1,355 leaves, without mirror commit/reset.
Retain post-commit graph preservation in ignored `integration/graph-audit.json`.
No compiler capture, Claude/REA call, sibling host or frozen Release action.

```sh
python3 -m unittest tools.tests.test_game_category_boundaries_match -v
python3 -m tools.experiments.game_category_boundaries_integration --audit
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Next Target

Fresh owner audit: **57/73 exact,16 different**, complete list in ignored
`integration/owner-completion.json`. Continue **func_1508D850**, VA
`1508D850..1508DA1C`, ROM `BAD00..BAECC`: **115 words/frame80**,107 real
differences, still a placeholder. One aligned direct JAL0D423614 appears at
VA1509E13C /ROMCB5EC in CB3D0.s; its delay loads a full-word slot from S0+8.
Do not infer a meaningful signed return merely from the dispatcher epilogue.

Recover the early nested actor+129 byte store before negative-target rejection,
horizontal X/Z distance and classes at5000/2000, signed selector/halfword
threshold table, timer+29C reset, fresh context/mask reads and optional
func_1508EB90(slot,0x61,0x2000) notification. Keep cached original actor/timer
pointers across that helper. If the timer is0, clear nested+12A, call
func_150ADA68 and use its float result*100 with the freshly reloaded signed
selector/probability table, then possibly set the current nested+12A to1.
Qualify actual helper contracts, reload/spill lifetimes, FP/signed boundaries,
shift domain and caller/return semantics before installation.

The supplying `2424E0.rodata.s` already belongs to frozen inputs; current SHA
`c734fe5ab4d490c6c84cfdb1d4e3d3be1e573a0f3d7f6bc26c352f208efe420a`.
D_8009DA8C is5000.0f. Keep this bounded target separate from larger remaining
owner conversions. The broader Game decomp/matching goal remains active.
