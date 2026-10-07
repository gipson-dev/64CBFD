# Game Matrix-List Transform Match

Date: 2026-10-07

## Scope And Baseline

Continue from banked point-batch checkpoint `38239bec`. Recover
`func_15145EA4`, owner
[game_16EE20.c](../../conker/src/game_16EE20.c), VA
`15145EA4..15146078`, ROM `173354..173528`: **117 words / 468 bytes**.
The production zero-return placeholder occupied the padded slot with
**106 differing words**. The original function has a `0xA0` frame, matrix at
`sp+0x5C`, saved F20 pair at `sp+0x28`, source/destination homes at incoming
`sp+0`/`sp+4`, and five calls on the two routes.

The complete 23-word caller `func_15135424` builds two two-entry pointer lists,
passes the original matrix and count two, then returns normally. Its existing
C declaration uses 32-bit words; the recovered callee uses pointer types for
the same ABI words. No shared header or caller modification is needed.

## Semantic Recovery

The recovered body preserves:

- One entry read of byte flag `D_800C3E90`. A nonzero flag calls
  `guMtxL2F` **before** the count gate, even for nonpositive counts. The
  converted matrix is used for nonzero-point transforms on that route.
- A zero flag uses the incoming float matrix directly, with no conversion.
  Both original route-specific loops remain visible in the C.
- Null points and points with all three coordinates equal to floating zero
  call `func_15142314(originalMatrix, 0, destination)`, not the converted
  matrix. Positive/negative zero compare equally; nonzero/subnormal/infinite/
  NaN inputs enter the transform route according to the lazy comparison chain.
- X is cached once; Y/Z comparisons are short-circuited, then those coordinates
  are reread for `func_150A7960`. Each list advances by four bytes, not the
  previous wrapper's twelve-byte record stride.
- Both list arguments are spilled at entry. The source home is reloaded in
  the count-gate delay even for nonpositive counts. The destination home is
  loaded only for positive counts. Conversion-time mutations/readbacks are
  therefore not replaced by cached arguments.

Real list cursors recover the incoming homes; a meaningful cached X scalar
declared before the local matrix recovers its exact placement. There is no
dummy padding, private-offset patch, ABI-word cast, instruction insertion,
omission, profile change or backend flag installation.

## Match Boundary

The first ordinary source form already emits 117 words, but has frame
`0x98`, matrix `sp+0x58`, cached argument lists and nineteen slot differences.
The selected semantic source emits **117 words / frame `0xA0` / matrix
`sp+0x5C`**, unchanged O2/g3/MIPS2, no pool or isolated diagnostics, with
**nineteen raw word differences**.

Nineteen expected-word guards normalize only:

1. One closed `s1 <-> s2` GP allocation cycle, preserving every physical
   save/restore slot and lifetime.
2. The independent stores at `+0x08`/`+0x1C`, permuted rather than moving
   their stack offsets.
3. Two `c.eq.s` operand-order commutations at `+0x78`/`+0x12C`, comparing
   the same F0/F20 pair. This is not FP register renaming.

All 117 normalized words equal retail. All seven actual relocation entries
are retained unchanged: one HI16/LO16 flag pair, one SDK conversion call,
two point-helper calls and two translator calls. No guard touches a relocation,
branch displacement, private offset or instruction count.

## Maintained Qualification

[Candidate driver](../../tools/experiments/game_matrix_list_transform_candidates.py)
retains **182** ordinary source/profile controls: 64 loop/condition/list-view/
branch-order forms, 48 cursor/count lifetimes, 32 inline/scope/order/views,
28 scalar forms, six comparison forms and four compiler profiles.
None is raw byte-exact. Each passes twelve ordinary bounded public-effect
fixtures: **2,184 candidate executions**. These ordinary fixtures do not
grant every control incoming-home or private-layout equivalence.

[Nine match tests](../../tools/tests/test_game_matrix_list_transform_match.py)
qualify the selected source, normalized words and retail:

- **10,752 guest cases**, all 117 wrapper words, complete memory, public
  reads/writes/calls, saved registers/F20, three flag values, seven signed
  counts, four point routes, four sequential record/matrix aliases, two stack
  phases, bounded conversion-time point/list mutations, and sixteen float
  patterns including signed zero/subnormals/infinities/quiet/signaling NaN bits.
- **1,152 connected cases** with the actual original SDK converter, 40-word
  point helper and 49-word translator. All 45 executable converter body words
  are covered; its 46-word slot includes padding. The SDK is not a mutation
  hook in this gate.
- **72 complete original-caller cases**, all 23 `func_15135424` words,
  all four forwarded ABI words, both temporary lists and final return.
  Selected/normalized/retail callees run with the original connected helpers
  and independently predicted final public storage/calls.
- **1,344 incoming-home readback cases**, all seven count classes,
  independent/both source/destination redirection; **42 removed-home cases**,
  **12 unused/null-list routes** and **eight required-storage cases**.
  Source home is always required after conversion, destination home only
  when the count is positive.
- **131,104 equality comparisons** over 65,552 bit patterns and both zero
  signs, unchanged FP bits; **1,200 private-matrix point/output overlaps**
  with complete memory identity and actual original helpers. The private
  offset is recovered in C, not repaired by guards.
- **1,572,872 freestanding 32-bit native cases**, actual repository SDK
  conversion, every high/low halfword in each of sixteen fixed matrix fields
  through correlated sweeps, all 255 nonzero flag bytes, both matrix routes,
  null/zero/nonzero points, three sequential record aliases and complete
  record/matrix fences. Eight cases use nonpositive counts and null lists.
  Native point/translation helpers are validating bounded hooks; this is not
  a claim of full native SDK arithmetic, FCSR or 64-bit port acceptance.
- **Eight compiled negatives**, each with an actual public-storage
  counterexample: flag/count gates, source/destination stride, zero gate,
  translation index, matrix route and cached argument homes. Unexpected
  faults are not counted as successful negative detection.
- Copied owner retains 89 functions, all 88 neighboring raw bodies/relative
  relocations, normalized pools and two old warnings. Isolated and owner
  raw target bytes match; actual padder emits 117 words, no overflow.
  All four referenced symbols independently rebase, including a low-half
  carry for the flag, with all seven relocations retained.

### Harness Corrections

Exploratory scalar controls initially forwarded conditionally assigned Y/Z
locals despite short-circuiting. They were corrected to preserve the original
call-time rereads **before qualification**; those unsafe exploratory forms
are not counted as passing controls.

The first core pre-install run passed six tests but the native fixture failed
warnings-as-errors on two mixed `&&`/`||` conditions. Explicit parentheses
fixed the fixture without weakening its compiler gate. Its integer initializer
also uses unsigned shifts, not undefined signed-left-shift overflow.
The corrected **eight core pre-install tests pass in 315.497 seconds**,
zero skips/errors/failures. Strengthened complete-caller and both-halfword SDK
checks pass separately before installation; the final combined suite covers
their current maintained source. No failed exploratory run is qualification.

## Linked Audit And Regression

Fresh pre-install US ELF snapshot exactly equals the previous point-batch
checkpoint: 6,058 symbols, 6,042 retail slots, 16 overflow symbols, protected
section hashes, conversion progress hash and all 11,042 prior guards.
US ELF rebuild passes in **262.986 seconds**, with the affected owner's two
existing pointer warnings at lines 191/1608 and the old duplicate-recipe
warning. No new owner diagnostic. Linked after snapshot verifies:

- Exactly one changed body, `func_15145EA4`, among 6,042 retail slots /
  6,058 linked symbols. All other 6,041 retail bodies and all 16 overflow
  symbols stay unchanged.
- All addresses/extents stay fixed. `.init`, `.init_data`, `.debugger` and
  `.game_data` hashes stay unchanged. All 720 Game-data owners and 189,088
  bytes remain exact, zero different bytes.
- All previous 11,042 guard rows stay identical; nineteen appended rows
  bring the total to 11,061. Conversion progress file hash stays unchanged.
- All 117 target words are byte-exact; total **3,363 / 5,466 (61.53%)**,
  Game **2,690 / 4,793 (56.12%)**, **2,103 still different**, zero address
  drift. Init remains 492/492 exact and Debugger 181/181 exact.

All **63 combined tests pass in 759.125 seconds**, zero skips/errors/failures:
the nine matrix-list match tests, nine point-batch match tests, eight
point-list match tests, nine historical point-list audits, nine translator
recovery tests, eleven single-point wrapper checks, three shared owner-pool
tests and five actual-padder checks.

```sh
python3 -m unittest tools.tests.test_game_matrix_list_transform_match tools.tests.test_game_point_batch_transform_match tools.tests.test_game_point_list_transform_match tools.tests.test_game_point_list_transform_audit tools.tests.test_game_matrix_translation_recovery tools.tests.test_game_point_transform_match tools.tests.test_game_owner_pool tools.tests.test_pad_c_object_word_patches -v
make tools-check
python3 -m conker.build.game-matrix-list-transform-test.verify_docs
```

Tools, Python syntax, scoped whitespace and final post-regression linked
audit checks pass. The documentation checker verifies **81 documents /
3,947 relative links / zero broken links**. README receives only the two
measured aggregate matching-row updates; roadmap verification gates are
checked off. No remaining production qualification gate for this target.
Ignored receipts live in `conker/build/game-matrix-list-transform/` and
`conker/build/game-matrix-list-transform-test/`.

## Continue

1. Recover `func_15146078`, the next **148-word** routine currently retained
   as original assembly, not a false C stub. It has a `0x48` frame,
   zero-vector rejection, byte-sized zero-axis counting, special two-zero
   basis outputs and the general four-call vector path. Audit early private
   byte reads at `sp+0x45`/`sp+0x46` and their downstream liveness before
   inventing initial values or claiming a C match.
   Read-only caller evidence is retained at `func_1514FB98 +0x1C` and
   `func_150D5A6C +0x344`: both supply an input vector and two output vectors;
   the former uses the boolean result to gate its following call.
   The four-call path uses two sequential `func_151450B4` cross products,
   then two `func_15145128` in-place normalizations with shared private
   length/reciprocal outputs. Preserve those alias/order effects and the
   exact retail division/subtraction, not a substituted basis algorithm.
2. Translator `func_15142314` remains C49/frame0/34 raw differences;
   arithmetic recovery and all 178 retained controls are unchanged.
3. Sampler `func_151432BC` still needs per-path RA loads and circle RNG-byte
   scheduling. No sampler installation or new measurements here.

This is guest decomp/matching progress, not hardware/FCSR/rendering/gameplay
or PC-port acceptance. No sibling source, frozen Release, real save, runtime
or push action. README receives aggregate rows only; details belong here.
