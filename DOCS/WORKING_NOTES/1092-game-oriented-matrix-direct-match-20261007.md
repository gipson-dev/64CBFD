# Game Oriented Matrix Direct Match

Date: 2026-10-07. Baseline: `40be2b0f`,
[Note 1091](1091-game-actor-lookup-byte-abi-direct-match-20261007.md).
Supersedes the uninstalled layout handoff in
[Note 1070](1070-game-oriented-matrix-original-frame-recovery-20261006.md).

`func_15142600`, VA `0x15142600..0x15142838`, ROM
`0x16FAB0..0x16FCE8`, now emits **all 142 words / 568 bytes directly from C**
under the unchanged **O2/g3** owner profile. The original **frame `0xB8`**,
private direction/matrix slots, saved F20/F22 lifetime, arithmetic sequence,
branches, delays and converter relocation all match. No guards, frame/private
offset rewriting, instruction insertion/deletion, padding locals or shared
header/profile/padder changes.

## Real Storage Recovery

The previous in-place candidate already matched all nonprivate instructions,
but ten direction references were four bytes low and seventeen matrix
references eight bytes low. The new
[lifetime driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_oriented_matrix_lifetime_candidates.py)
retains 48 measured O2/g3 forms:

- Sixteen homogeneous-vector, SDK-aligned matrix and nested-scope controls.
  An unscoped SDK `Mtx` union produces the same instructions as the plain array;
  zero-W vector forms still fail the frame/offset fit. Nested scopes grow to
  147 words. These are controls, not the installed form.
- Twenty-four declaration permutations of the original meaningful aggregates.
  The six matrix-first orders fix every matrix reference, leaving **10**
  direction differences; the other eighteen retain **27**. All fit 142/B8.
- Eight orders separating the two meaningful horizontal scalars. Four are
  **142/B8/zero differences**: `20314`, `21304`, `20341`, `21340`.
  Select `20314`, without the now-unused horizontal typedef.

The selected declaration order is matrix, left X, direction, left Z, up,
inverse. Structured `.mdebug` locals are entry-relative: matrix `-64`,
leftX `-68`, direction `-80`, leftZ `-84`, up `-96`, inverse `-100`.
These are compiler debug local homes, not a substitute for instruction-offset
verification. The actual generated direction references use frame
`+0x68/+0x6C/+0x70` and matrix `+0x78..+0xB4`, exactly retail.
Every declared local participates in the computation; no dummy padding,
volatile or SDK union is needed in the installed source.

Together with the 128 maintained historical controls, this is **176
measurements**, not 176 distinct emitted bodies. Do not count the separate
historical ignored scratch sweeps as part of that maintained total.

## Contract And Caller

- Twelve input positions: output pointer, two row factors, three column
  factors, start point and end point. Normalize end-minus-start, its horizontal
  perpendicular and their cross product independently.
- Preserve the original binary32 multiply/add/divide/sqrt ordering. Column
  factor multiplication precedes row factor multiplication; rows zero/two
  use `row0`, row one uses `row1`.
- Translation is the original start point, not a view-matrix negative dot.
  The horizontal Y and first three fourth-column entries are zero; final
  homogeneous entry is one. Call `guMtxF2L` once.
- Coincident or vertical points have no epsilon/identity fallback. Preserve
  the original NaN/Inf propagation rather than introducing a new guard.

Correct local declarations and the body of `func_150B9D14` in
`generated_E5E90.c` to `Mtx *` / float fields, with a void builder declaration.
All **eight raw owner functions**, relative relocations and pools remain
identical, zero warnings; the caller stays **30 retail words** with its single
builder relocation at `+0x58`. Install the typed caller and builder together.
The original assembly references remain intact.

## Qualification

[Ten fitting tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_oriented_matrix_match.py) bind
the selected source, direct object, production owners and linked slots:

- **2,448 guest fixtures**: 204 finite/special-bit inputs, three destination
  aliases, both stack phases and both source-mutation modes. An independent
  reference checks all matrix fields, complete external storage and call
  effects. Additionally raw C/retail agree on complete memory, events, every
  GPR/FPR, calls and instruction visits. All 142 target words execute.
  Arithmetic NaNs are classification-compared against the independent
  reference; complete C/retail model effects are still compared exactly.
- **144 connected fixtures** execute every word of the original 30-word
  caller, 142-word builder and 115-word `guMtxF2L`. The independent packed
  matrix reference is restricted to finite exactly integral signed32 scaling.
  Caller forwarding and status one agree; complete guest effects also match.
- **288 private converter-overlap fixtures** place output at every aligned
  frame offset `+0x28..+0xB4`, with two stack phases, row choices and starts.
  The complete original converter executes using a finite, default
  nearest/even `CVT.W.S` model. New C/retail agree on every memory byte,
  event, register and visited instruction. The old 27-difference candidate
  produces different 64-byte output in **156** cases, so its private-layout
  mismatch is observably significant, not merely a cosmetic stack offset.
- **1,224 actual freestanding native 32-bit typed-caller fixtures** check
  complete external storage and special values using the explicit bounded
  float-payload converter capture. This is not native fixed-converter or
  native private-stack-alias acceptance.
- Nine compiled semantic negatives alter known matrix/call results. Missing
  mapped actor inputs, matrix storage or destination fail closed in both
  raw/retail models.
- The production-preprocessed/postprocessed copied builder retains **89
  functions / 88 neighbors**, their raw words, relative relocations,
  normalized pools and the same **two warnings**. The selected raw 568-byte
  target equals the isolated object. The actual padder emits all 142 words
  with no overflow. Independently rebasing `guMtxF2L` by `0x1000000` changes
  only the original call at **`+0x21C`**.
- Installed source, typed caller, linked exact words and unchanged guard
  history are pinned. The thirteen historical recovery tests reconstruct
  their old placeholder/false-type baseline explicitly, retaining all prior
  candidates and expectations rather than substituting the new match.

These are bounded guest/native checks, not general FCSR/exception-mode,
native NaN-payload, hardware/gameplay, full-ROM checksum or host adoption.

Final combined regression: **64 tests pass in 353.549 seconds**, zero skips,
errors or failures. Includes ten fitting tests, thirteen historical oriented
tests, eleven row-matrix tests, twelve scaled-matrix tests, five actual-padder
tests, three pool-ownership tests and ten actor-lookup tests. The four
pre-install storage/owner gates and five pre-install behavior gates also passed;
do not count those repeated runs as additional distinct behavioral cases.
Tool smoke checks, changed Python syntax and whitespace gates pass.
Documentation gate: **74 documents / 3,857 relative links / zero broken**.

```sh
python3 -m unittest tools.tests.test_game_oriented_matrix_match \
  tools.tests.test_game_oriented_matrix_recovery tools.tests.test_game_row_matrix_match \
  tools.tests.test_game_scaled_matrix_match tools.tests.test_pad_c_object_word_patches \
  tools.tests.test_game_owner_pool tools.tests.test_game_actor_lookup_match -v
```

## Build And Audit

`make -C conker build/conker.us.elf -j2` succeeds with the two existing owner
warnings and existing duplicate-recipe warning. The fresh pre-edit/post-link
audit retains **6,058 linked symbols**, comprising **6,042 retail slots** and
16 compiler overflow symbols. Every address and extent remains unchanged;
**only `func_15142600` changes**. All 6,041 other retail bodies, including the
typed caller, and all overflow symbols remain identical.

Protected Init/Init-data/Debugger/Game-data sections, all **720 Game-data
owners / 189,088 bytes**, and all **11,006 guards** remain unchanged and exact.
Neither builder nor caller has a guard. Conversion counts/bytes do not change:
the replaced zero-return body was already counted as C.

Exact converted matching advances by one: **3,358 / 5,466 (61.43%) total**,
**2,685 / 4,793 (56.02%) Game**, **2,108 different**, zero address drift.
Init492/492 and Debugger181/181 C functions remain exact. Root README changes
only the two aggregate matching rows; detailed progress stays under DOCS.

## Resume

Bank this direct builder/caller recovery. The oriented private-layout work
is complete; do not resume the superseded 27-difference candidate. Next is the
still-open sampler `func_151432BC` from
[Note 1074](1074-game-area-sampler-qualified-recovery-20261006.md) and
[Note 1091](1091-game-actor-lookup-byte-abi-direct-match-20261007.md), specifically
its two per-path RA loads and circle RNG-byte schedule, or another ordinary
Game function. Do not add padding words or private-offset guards to force a fit.
No sibling/frozen Release, save/runtime or push work.

Ignored receipts: `conker/build/game-oriented-matrix-lifetimes/`,
`conker/build/game-oriented-matrix-match-test/`, and the historical
`conker/build/game-oriented-matrix/` / `conker/build/game-oriented-matrix-test/`.
