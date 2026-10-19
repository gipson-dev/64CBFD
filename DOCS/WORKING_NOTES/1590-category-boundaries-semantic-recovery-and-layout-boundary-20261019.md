# Category Boundaries Recovery And Matching Boundary

Verified:2026-10-19. **Complete experimental C recovered; not installed.**
The tested candidate has112 words/frame96, but54 words still differ from
retail. Equal extent/frame and public results do not establish a byte match.

Continue `func_15085BE8`, generated_B3020, VA `15085BE8..15085DA8`, ROM
`B3098..B3258`, from
[Note1589](1589-record-release-complete-match-20261019.md). Consumer baseline
**3ead6659**, tools baseline **f873d04**. Bank tools **46c5d3c** before the
consumer documentation/pin. Production retains its original zero-return
placeholder; no source, manifest, compiler/profile or assembly change applies.
No production build or push.

## Complete Semantics

This no-argument routine returns a signed32 overlap flag. Initialize six
maximum entries to D_8009D9C0 (-10000.0f) and minimum entries to D_8009D9C4
(10000.0f). These are **finite initial extrema**, not infinities: heights
outside that interval retain the opposite clipped initial bound.

Read signed16 D_80087290. Only a positive count loads the row pointer
D_800D2350 and scans its16-byte records. Row+2 is signed16 height; row+6
is an unsigned-byte category. Update that category's minimum and maximum.
Native qualification backs categories0..5 and all evaluated rows; no arbitrary
category, invalid stack alias or unbacked positive count is validated.

Clear the byte D_800D2358 to0. In ascending category order, compact every
category with minimum<=maximum into D_800D237C, incrementing the count after
each byte store. Do not clear the unused ID tail. For each adjacent compacted
pair, write to D_800D2360:

```text
boundary = (next minimum + current maximum) *0.5f
overlap  = 1 if any next minimum < current maximum
```

Equal heights produce an active category but are **not** an overlap between
adjacent categories. Always append D_8009D9C8 (100000.0f), including zero/one
active category. Preserve all unused output bytes/words. Signed16 inputs and
the fixed initial extrema make all evaluated sums/halves exact in float32;
no NaN, FCSR, invalid conversion or hardware exception semantics are claimed.

The immutable rodata input is
`conker/asm/data/242480.rodata.s`, SHA256
`4add61fb582bd9368ec71f1a974de8545c88624aa7ee27c41d9addd675013618`.
The old donor draft is reference only: its64-element arrays, pointer strides,
word/float row loads and ID types are wrong. It is not installed or counted
as matching C.

## Source And Matching Evidence

Use `game_category_boundaries_candidates.py` and its readable complete
`FITTED` body, with meaningful minimum/maximum/category/overlap names. The
signed row-byte limit is genuinely used; there is no padding local, dummy
effect, physical-register binding, volatile or new guard in this candidate.

The first complete indexed body emits111 words/frame96,65 differences.
Gating row-pointer access on positive count and expressing the final bound
as the active-count subtraction recovers **112 words/frame96** with the
original signed comparison, but **54 real word differences remain**. Both
complete-owner profiles emit the same tested112-word body without diagnostics.

```text
tested raw object payload SHA256:
f75286e1e136d71b028578b8f37ce5297020d74d093c2b3ce6d01615669a3722
```

Fifty-two compiler-only source screens cover fills, explicit loops, counters,
pointer/index forms, declarations and lifetimes. These are **not all proven
semantic alternatives**. In particular, the unsigned-index global-bound form
is invalid for an empty active list. A112/40 compiler screen retains an unused
bound local; it is not the tested candidate, not an accepted source recovery,
and must not be used to claim a better qualified match. Normal-profile
standalone unrolling controls also do not override the installed owner profile.

Current literal blockers include:

- Retail first reads **D_8009D9C0** into F2, then C4 into F0. The tested
  source first reads **C4**, then C0. Cut0 fires in both emitted routines and
  reports those different requested addresses. This is a measured fault-order
  boundary, not merely a register-allocation difference.
- Retail places maximum scratch at **SP+18** and minimum at **SP+30** in
  frame60. The tested C uses different offsets. Equal overall frame size is
  not the original private layout or stack-alias behavior.
- Retail's row-loop entry/reset shape and saved scratch roles differ from
  the compiler's extra limit branch/current zero placement. Source screens
  with a common counter or separate counters do not yet recover them.
- Later GP/FP allocation and relocation positions still need complete
  origin/lifetime analysis. Do not assume all54 words form one closed rename
  or normalize predicates/array addresses to retail without proving behavior.

Ignored `conker/build/game-category-boundaries/matching-boundary.json` records
every linked differing word and screen-group inventory. `qualified.c`, its
processed source/object/link and diagnostics retain the exact tested form.
There is no layout normalizer or installation command for this recovery.

## Fresh Qualification

All **seven tests pass in12.132 seconds**, without skips. The earlier complete
pass before adding the padded-address assertions took11.118 seconds; the final
pass includes those assertions. Repeated caller/maps/raw fixtures are not new
independent input domains.

- **677 fixtures/two phases:1,354 paired public executions** compare retail
  and emitted C independently against the reference. All112 retail and source
  words are visited. Check return, entire public memory, unchanged row bytes
  and ordered public stores. This is not full GP/FP/private-memory or access
  trace equivalence.
- Native32 **O0, O2 and O2+UBSan** each pass677 full-buffer fixtures, all
  **65,536 signed16 height views in each of six single-category cases**, and
  all **32,769 nonpositive signed16 count views** with a poisoned, unvisited
  row pointer. The single-category sweep checks public count/ID/sentinel
  behavior, not invisible scratch extrema. Paired-range fixtures discriminate
  signedness, clipped extrema, empty/equal/gapped/overlapping cases and order.
- Every native fixture checks all1,024 input bytes,16 backed ID bytes and
  seven boundary-buffer words. Six words can be written; the seventh at+18
  is an unchanged spare before real IDs begin at+1C. This backing does not
  assert an original C declaration length or validate out-of-range indices.
  Expected words are endian-neutral; preserve the established32-bit,
  stack-realignment and no-strict-aliasing harness policy.
- Five effective native C controls change height signedness, active equality,
  overlap equality, midpoint arithmetic or sentinel. Each exits21; positives
  exit0. No crash/signal/trap counts as success.
- **364 fired retail access cuts** confirm the requested address before each
  access in four representative paths/two phases. A further cut0 fires in
  both retail and raw C and proves their different first reads. No complete
  raw-versus-retail fault-state equivalence is asserted.
- **80 actual returning-caller pairs** execute six retail words at
  VA15085BD0 /ROMB3080: JAL/NOP, RA reload, SP+18 adjustment and JR/NOP.
  Aligned ROM JAL0D4216FA scan finds that one site. The24-byte caller frame
  is an explicit live-in; the upstream resource loader is not executed.
  Check public result/memory and preserved ABI, not identical scratch state.
- **Three independent GNU maps /144 public pairs** rebase code, all eight
  global/constant anchors and rows, including HI/LO carry boundaries. Both
  assembled retail and independently linked C produce correct public results,
  while their instruction bytes remain explicitly different.
- Both complete-owner profiles preserve72 other routines and normalized
  pools. Actual private padding with the existing manifest preserves those
  routines, pools and all73 function addresses. The target still differs at54
  words after actual padding. All frozen production input bytes remain fixed.

Two native-fixture mistakes were corrected before the successful pass: an
overlong twelve-word output buffer overlapped real ID storage in guest
expectations; then float-valued transport failed to preserve arbitrary
unvisited output bit patterns. The final harness bounds the spare correctly
and seeds/checks raw words. These were harness repairs, not game-code changes
or proof of hardware NaN handling. The CSV test reader is also explicitly
closed; the final pass has no resource warning.

## Checkpoint And Resume

Fresh `make -C conker match-progress NON_MATCHING=1` remains **Game3004/4832
(62.17%)**, **total3677/5505 (66.79%)**, Init492/492, Debugger181/181,
**1,828 different / zero drift**. The unchanged production image keeps the
owner at56/73 exact,17 different. Conversion rows and root README aggregates
do not change, because this recovery is deliberately not installed.

Production fingerprints remain:

```text
owner:  af0fd776d65e309e9dcc8e4d68bd3e3155dc0eff3c46faf6fa8f28da66ad96b8
guards: 5ddd1615d90ce59ff70ff6e95de91a52151b442b86156c2aea53a738393c34c3
ELF:    14bd44cfcbbb6ea376ada9c64ab529cd029dd38984f35e023ef166a594ccfcfe
```

Both tools copies pass three setup tests and smoke checks; consumer
`make tools-check` passes. Three new task files are identical ASCII/Python
in the standalone mirror. Preserve its ddbdd16 HEAD and all1,348 earlier
dirty leaf hashes; the three additions make1,351 dirty leaves. No mirror
commit/reset, compiler capture, Claude/REA call, sibling host or frozen Release
action. Post-commit graph preservation is retained in ignored `graph-audit.json`.

```sh
python3 -m tools.experiments.game_category_boundaries_candidates
python3 -m unittest tools.tests.test_game_category_boundaries_recovery -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Resume **this same function**, not a broader conversion batch. Recover the
initializer order and original scratch placement from a justified source
shape, then row-loop/counter lifetimes and closed allocation/binding changes.
Require fired-order/private-state checks before accepting any guards. Only
after exact actual padding should the strict complete first-image prediction,
source/guard installation, production rebuild and whole-image audit run.
The wider Game decomp/matching goal remains active.
