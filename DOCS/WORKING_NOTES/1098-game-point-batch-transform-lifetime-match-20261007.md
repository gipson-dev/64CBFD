# Game Point-Batch Transform Lifetime Match

Date: 2026-10-07. Baseline: `69347226`,
[Note 1097](1097-game-point-list-transform-lifetime-match-20261007.md).

## Recovery

`func_15145DB4`, VA `0x15145DB4..0x15145EA4`, ROM
`0x173264..0x173354`, transforms contiguous twelve-byte XYZ records. It is not
the two pointer-list interface of its preceding neighbor.

1. Call `func_150A8050` with descriptor float words at `0/4/8`, including for
   nonpositive counts. The rotation provider remains a bounded qualification
   hook, not a recovered full SDK/hardware implementation here.
2. After that call, reload the destination argument and maintain separate
   X/Y/Z output cursors. Read signed translation halfwords at `0x10/0x12/0x14`
   sequentially and fill the matrix's last row.
3. Only for positive counts, reload the source argument. Forward each current
   record's XYZ and all three output addresses to `func_150A7960`, decrement
   the signed count and advance every cursor by twelve bytes.
4. Keep in-place, partial-record and future-record output effects visible to
   subsequent iterations. Do not cache the complete input or precompute a
   snapshot of every result.

The [installed source](../../conker/src/game_16EE20.c) reuses its descriptor
cursor for source records after the last descriptor read. Two meaningful
signed32 translation bindings recover the original frame and matrix offset.
The labeled positive-count path keeps the source-home reload below the gate
under the unchanged O2/g3/MIPS2 profile. No volatile pointer or word-ABI cast,
extra assembly, dummy operation or unused padding local is installed.

| Body | Raw Words | Frame | Matrix Offset | Positional Differences |
| --- | ---: | ---: | ---: | ---: |
| Historical semantic C | 55 / 220 bytes | `0x80` | Wrong private layout | 60 across the padded 60-word slot |
| Recovered semantic C | 60 / 240 bytes | `0x98` | `sp+0x58` | 17 raw, zero after checked normalization |

This is **guarded byte matching, not a direct-C byte match**. Seventeen
expected-word guards normalize only three closed allocation cycles and an
independent prologue save-store permutation:

- Saved cycle `s2 -> s3 -> s4 -> s2` in the count/output-cursor body.
- Halfword temporary swaps `v0 <-> t7` and `v1 <-> t8`.
- Save-store permutation at `+0x8/+0x20/+0x24`; each physical register/home
  pairing remains the same, as do all epilogue loads.

No matrix, spill or incoming-home address moves. No FP register, arithmetic
operation, branch displacement or private read timing is patched. No word
is inserted/omitted and no constant pool is added. Both original call
relocations at `+0x40/+0xAC` remain `R_MIPS_26`; no guard touches either call.
ABI types remain `u8 *`, two `struct17 *` arguments and signed32 count.

## Maintained Controls

[Candidate driver](../../tools/experiments/game_point_batch_transform_candidates.py)
retains **119 meaningful controls**, plus the baseline measurement:

- 24 descriptor/source-phase, destination-initialization, loop and record/
  float-array view controls. Several emit 60 words but frame `0x90` and an
  eager source-home reload; none is exact.
- 36 meaningful rotation/translation/source/count scalar-storage and cursor-
  declaration-order controls, four compiler profiles and ten locally evidenced
  backend controls. Float translation bindings recover the frame/matrix
  placement but do not alone recover the gate or register allocation.
- 25 integral halfword-binding, argument qualifier/register, return/label-
  flow and no-cross-basic-block scheduling controls.
- 20 integral-binding/positive-label and alternate conditional-flow controls.
  Two signed32 Y/Z bindings plus the positive label produce 60 words/frame
  `0x98`/17 differences; the installed form is its readable equivalent.

All controls have empty diagnostics and no pools. Every control passes 24
ordinary public-effect fixtures, **2,856 candidate executions**. The bank is
119 measurements, not 119 distinct emitted bodies; none is raw byte-exact.
Only the fully qualified selected form is installed; experimental profiles,
backend options, qualifiers and alternate ABI views stay out of production.

## Qualification

[Nine tests](../../tools/tests/test_game_point_batch_transform_match.py) bind
the complete raw selected, normalized and original bodies:

- **1,792 guest fixtures** over seven signed count patterns, 16 data patterns,
  four aliases, provider mutation and both stack phases. Compare complete
  memory including stack bytes, ordered public traces, forwarded calls and
  saved state. All 60 wrapper words are covered.
- **768 connected fixtures** execute all 40 original point-helper words with
  an independent public-effect reference. Cover separate outputs, in-place,
  future-record overlap and partial-record overlap. The provider remains a
  bounded hook; full SDK arithmetic is connected only for the point helper.
- **5,376 incoming-home fixtures** independently redirect source, destination
  or both at both stack phases, including nonpositive counts. Raw, normalized
  and original match. These deliberately nonstandard guest ABI probes do not
  authorize ordinary native C callees to rewrite caller arguments.
- **524,296 actual freestanding 32-bit native cases**: correlated sweeps of
  every halfword pattern in each translation field, all four record aliases
  and both provider mutation modes, plus eight nonpositive/null-source calls
  with a valid destination. Check all input/output record words, descriptor
  fences, matrix fields and call addresses. The native point routine is a
  validating copy hook, not full SDK arithmetic or a 64-bit host-port test.
- **18 required-storage removal fixtures**, **28 removed-home fixtures** and
  four nonpositive routes with all record storage unmapped. Destination home
  is always required, source home only for positive counts. An eager-reload
  control incorrectly reads the removed source home for count zero and is
  explicitly rejected.
- **384 private descriptor/matrix overlap fixtures** connect the original
  point helper: 368 complete-memory identical routes and 16 intentional
  required faults. Six descriptor offsets, both stack phases, zero/positive
  counts and provider mutation are retained. The old matrix layout changes
  public storage in sixteen completed cases. In sixteen positive-count cases,
  the descriptor's translation mutation overlaps the incoming source home,
  corrupting it to an unmapped pointer; all three qualified bodies fail
  closed while the old cached-argument body incorrectly continues.
- Seven compiled negatives each change public storage: unsigned translation,
  exact-one gate, wrong source stride, wrong X destination stride, stale source,
  translation before the provider and old cached arguments. No ineffective
  negative is counted.
- Copied owner retains 89 functions, all 88 non-target bodies/relative
  relocations, normalized pools and two old pointer warnings. Selected raw
  owner bytes equal the isolated 240-byte body. The actual padder emits all
  60 words without overflow; both calls independently rebase by `0x01000000`.
- Guard-history checks retain every previous checkpoint and pin the new
  seventeen-row suffix. The prior pointer-list test now checks its nineteen
  rows at the original bounded range, rather than assuming they remain last.

### Harness Corrections

The first pre-install run rejected two checks, not a production edit. The
initial instruction-field assertion wrongly treated reordered save-store
offsets and an R-format destination-register field as unchanged immediate
bits. It now checks the complete physical store set and the correct operand
field masks, while every expected/replacement word remains fully pinned.

The initial private-overlap reference omitted the routine's actual incoming
argument spills and reload timing. It now models those real writes/reads,
including descriptor mutations that corrupt the source home. Intentional
required faults are explicitly retained, not discarded as inconvenient cases.
The corrected two-test gate passes in 3.371 seconds; then all **eight
pre-install tests pass in 128.524 seconds**, zero skips/errors/failures.
Failed exploratory assertions are not counted as qualification.

## Linked Audit And Regression

US ELF rebuild passes in 219.531 seconds, with the affected owner's two
existing pointer warnings at lines 191/1608 and the old duplicate-recipe
warning. No new owner diagnostic. A fresh `69347226` before snapshot and
linked after snapshot verify:

- Exactly one changed body, `func_15145DB4`, among 6,042 retail slots /
  6,058 linked symbols. All other 6,041 retail bodies and all 16 overflow
  symbols stay unchanged.
- All addresses/extents stay fixed. `.init`, `.init_data`, `.debugger` and
  `.game_data` hashes stay unchanged. All 720 Game-data owners and 189,088
  bytes remain exact, zero different bytes.
- All previous 11,025 guard rows stay identical; seventeen appended rows
  bring the total to 11,042. Conversion progress file hash stays unchanged.
- All 60 target words are byte-exact; total **3,362 / 5,466 (61.51%)**,
  Game **2,689 / 4,793 (56.10%)**, **2,104 still different**, zero address
  drift. Init remains 492/492 exact and Debugger 181/181 exact.

All **43 combined tests pass in 460.335 seconds**, zero skips/errors/failures:
the nine point-batch match tests, eight point-list match tests, nine historical
point-list audit tests, translator recovery, shared owner/guard-history and
actual padder checks.

```sh
python3 -m unittest tools.tests.test_game_point_batch_transform_match tools.tests.test_game_point_list_transform_match tools.tests.test_game_point_list_transform_audit tools.tests.test_game_matrix_translation_recovery tools.tests.test_game_owner_pool tools.tests.test_pad_c_object_word_patches -v
make tools-check
python3 -m conker.build.game-point-batch-transform-test.verify_docs
```

Tools, Python syntax and scoped whitespace checks pass. The documentation
checker verifies **80 documents / 3,936 relative links / zero broken links**.
README receives only the two measured aggregate matching-row updates.
Ignored receipts live in
`conker/build/game-point-batch-transform/` and
`conker/build/game-point-batch-transform-test/`.

## Continue

1. Recover `func_15145EA4`, the contiguous **117-word** matrix/list wrapper
   still represented by a zero-return placeholder. Its `0xA0` frame contains
   the matrix at `sp+0x5C` and saved F20 pair at `sp+0x28`. Preserve both
   fixed-matrix conversion and float-matrix routes, null/all-zero point
   fallbacks, signed-zero/NaN lazy comparisons, incoming-home timing and
   calls to `guMtxL2F`, `func_15142314` and `func_150A7960`.
2. Translator `func_15142314` stays C49/frame0/34 differences; all 178 retained
   controls and arithmetic recovery are unchanged here.
3. Sampler `func_151432BC` still needs per-path RA loads and circle RNG-byte
   scheduling. No sampler installation or new measurements here.

This is guest matching progress, not new hardware/FCSR/rendering/gameplay or
PC-port acceptance. No sibling source, frozen Release, real save, runtime or
push action. README receives aggregate rows only; details live here and in
the documentation indexes.
