# Balanced Target Assignment Complete Match

Verified: 2026-10-19. **func_1508BF14 is installed and all160 linked words
are byte-exact**, with its original176-byte frame and640-byte slot.
VA1508BF14..1508C194, ROM B93C4..B9644, generated_B3020.
Consumer predecessor9b7b9bc4; tools predecessor de2850c. Bank tools
**557a160** before the consumer source/guards/docs/pin commit. No push.

This supersedes the experimental boundary in [Note1597](1597-balanced-target-assignment-semantic-recovery-and-private-layout-boundary-20261019.md).
It is a **guarded match**, not direct compiler identity: the same complete
semantic C still emits160 words/frame224 with123 differences. The production
padder applies160 expected-word/relocation rows, retains158 unique source
origins, omits two qualified words and inserts two clear-loop copies. Both
global bindings survive. Original assembly, compiler profiles and literal
pools are unchanged; no padding locals, volatile declarations or physical
register bindings were added to C.

## Behavior And Private Byte

The complete C preserves the cached context/table bases and current team,
positive-count byte clear, flag2/3-first two-pass processing, opposite-team
positive-active filtering,16-entry neighbor search with both -1 sentinels,
signed32 wrapping reuse penalties and first strict minimum. It stores cost
before target through cached bases and returns0. There are no helper calls.
Meaningful local names and the address-based exported name remain; the
other-source snapshot is not credited as a byte-exact donor.

The native C's41-byte backing makes `uses[-1]` a legal private access and
initializes that extra cell to0. **That initializer is not an original source
fact.** The emitted retail routine does not initialize SP+7B and increments
its existing byte when no candidate wins. The layout recipe explicitly omits
the native-only initializer, recovering the original private poison behavior.
It does not reset or silently assume that retail byte is0. Candidate counters
start at SP+7C and the pass word is SP+A4.

Native/reference qualification remains bounded to counts<=40 and backed current
indices0..15; counts above16 are deliberately inactive. The measured40-byte
retail scratch footprint is not an engine-wide count-bound proof. No native
out-of-range, arbitrary stack/public overlap or uninitialized-C-read claim is
made. The normalized instruction image itself is literal retail.

## Derived Layout Recipe

- Restore frame224->176 while preserving the original frame-relative saved
  register slots. Recover cached flags/active/cost/target homes (hex) D4/D0/C8/C4
  as6C/68/64/60, pass84 asA4 and the three scratch-base definitions8D as7C.
  A frame-only edit is not this transformation.
- Recover the closed saved roles: raw count S2->S3, teams S3->S4, cached team
  S4->S5 and scratch S5->S2. Exchange neighbor/receiver T1/T2 colors and recover
  the explicitly bounded V0/V1/A0 and T6/T7/T8/T9 lifetimes. Saved stores and
  restores are excluded from these register-use mappings.
- Move the existing scratch-base definition to its original opening lifetime,
  and the existing -1 definition after the clear. Split the remainder from
  the incremented clear pointer with two nontrapping copies. On the
  positive-count/remainder0 edge, the clear index is0 and cannot equal count;
  bypass that redundant entry check while retaining it for the remainder edge.
  Relabel every moved branch destination explicitly.
- Restore independent best/selected setup, the constant2 rematerialization
  after the neighbor scan and the receiver-offset branch-delay update. Swap
  only two commutative address-add operand orders and one BNE operand order.
  No score test, store offset, width or public arithmetic constant changes.
- Omit the native-only private initializer and redundant ANDI31. Feed the
  existing signed-byte result directly to SLLV, whose shift field consumes its
  low five bits. The source keeps the unsigned32 cast/mask to avoid signed
  left-shift UB in native C; the final emitted operation preserves retail.

All160 source words and both bindings are fingerprint-gated. Each retained
origin appears exactly once; no function is assembled from copied ROM words.
The unrelocated fingerprints are:

```text
Raw:        c31e39062a3c82931d51d574c1106272083e651bfc04b8e796c6b31490009795
Normalized: 530c11d19d950b3b016f6a5af8a62b0f9d7acd34759eac10434384b8d1818217
```

Generic register/declaration/aligned-backing controls did not reduce the frame
or word differences and remain rejected experiments. The local field decoder
handles ORI and BLEZL without changing shared helpers. The unused normal
profile still emits198 words and is not selected for this function; only the
pre-existing func_150891E8 normal override remains in the Make path.

## Fresh Qualification

**Eight installed tests pass in71.601 seconds**, without skips. The earlier
pre-installation run passed in42.648 seconds and is not substituted for this
installed receipt.

- 94 fixtures/two phases give188 completed retail/normalized/raw triples
  against the independent mutable-table reference. Check complete public
  buffers, ordered cost/target stores and zero result. Retail/normalized also
  agree on all modeled GP/FP/LO/condition state, private bytes, ordered reads/
  writes, requested accesses, calls and visited PCs. All160 retail words run.
- 1,080 fired access-cut pairs across six edge profiles/two phases agree on
  the actual requested address/width/value and complete modeled state. Cuts
  are dispatched accesses, not observer-generated faults or hardware tests.
- Native32 O0, O2 and O2+UBSan each pass all94 fixtures with empty sanitizer
  diagnostics. Ten semantic negatives remain effective, covering pass order,
  ties, reuse, activity/team tests, signed scores, both sentinels, flag width
  and row bounds. They compile and fail behaviorally, not through signals.
- 1,536 signed-byte/score instruction tuples qualify removing the explicit
  mask. Four private poison seeds0/7F/A5/FF preserve literal retail miss-cell
  increments and full normalized private state, including wrap cases. Raw
  private identity is explicitly not claimed.
- The actual caller window at ROM CB564/VA1509E0B4 runs27 times with retail,
  normalized and raw bodies. Retain JAL/NOP, branch/RA delay load and original
  S0/SP/JR/NOP epilogue, with the72-byte caller frame as a live-in. The
  frame-only negative corrupts the real caller RA home and is rejected.
- Three independent GNU maps include HI/LO carry boundaries, move code/global/
  context backing, and reproduce independently assembled retail bytes.
  Thirty-three rebased raw/normalized pairs agree with the reference.
- A completed backed guest alias lets the first cost overwrite D_800D23B0;
  later receivers still use the captured bases. The full normalized state
  remains retail-exact. This is not a native overlapping-region assertion.
- All160 raw-word and two relocation mutations are rejected. The real padder
  rejects stale expected words/relocations; four complete-image corruptions
  fail. Canonical symbols change only in target size12->640.
- Both complete-owner profiles preserve72 neighbors and every pool. The actual
  padder and expanded seven-command Make shadow reproduce all qualified code,
  bindings and metadata, with all73 owner addresses fixed.

Shared tools checks and both mirror syntax checks pass. The three new match
files are mirrored identically while preserving all1,377 pre-existing dirty
leaf hashes and the standalone mirror's older HEAD. That checkout is not
committed or reset. No Claude call, REA setup, dependency or host operation was
needed. Full switch/gameplay, hardware exceptions and full64-bit CPU state are
outside this low-word/native32 qualification.

## Production Image And Bank

The production build reproduces the exact **485-byte image change**:
483 target-code bytes and two target-size bytes. No symbol-order permutation,
blanket metadata allowance, data change or Makefile edit is needed. All6,056
other function bodies and every address remain fixed. Protected Game data is
exact across189,088 bytes/720 owners, with zero differing bytes/owners.

Target diagnostics are empty. The overall dependent-object rebuild retains
legacy compiler warnings and the known duplicate generated_12D630 recipe
warning; it is not reported as warning-free. Git's existing CSV CRLF/LF warning
does not change the qualified structured guard rows; no line-ending policy is
changed here.

Installed fingerprints:

```text
Owner:  b03873bc9c984f3ce9eac8649d91170673bb8607b238b11f4686389edff11359
Guards: 6a9e810059f31fc023e7fec0e58165fa71b8e5a32bfecb103aa1388c11e2f6b5
ELF:    6dae1b0cfba38f03c17601e1b9afdecefcfbd03f8302c4db89501b04801ac0bc
```

Fresh matching: **Game3,009/4,832 (62.27%)**, **total3,682/5,505 (66.88%)**,
**1,823 different/zero drift**. Init492/492 and Debugger181/181 remain exact.
Owner **61/73 exact,12 remaining**. Conversion remains5,505/6,044 (91.08%) and
86.08% bytes. Root README changes only its two matching aggregate rows;
function narratives remain in docs. Commit tools first, then consumer source/
guards/docs/pin. No push, save changes or frozen host Release operations.

## Resume

Next: **func_15086098**, the shortest remaining owner nonmatch:179 words,
frame112,168 real differences, VA15086098..15086364, ROM B3548..B3814.
Freeze this installed baseline, inspect its complete assembly and actual
caller/interface, then recover and qualify it without a broad conversion batch.
The other11 owner nonmatches and preparation helpers remain unfinished; this
match does not credit their implementations. Keep the wider Game goal active.

```sh
python3 -m unittest tools.tests.test_game_balanced_target_assignment_match -v
python3 -m tools.experiments.game_balanced_target_assignment_integration --audit
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored compiler controls, original padded object, immutable inputs, mask/
private/caller/rebase receipts, Make shadow, first link, production build/audit,
installed hashes and remaining-owner inventory live under
`conker/build/game-balanced-target-assignment/`.
