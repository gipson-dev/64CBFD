# Game Point-List Transform Lifetime Match

Date: 2026-10-07. Baseline: `7f1de4a6`,
[Note 1096](1096-game-matrix-scheduling-and-point-list-lifetime-audit-20261007.md).

## Recovery

`func_15145CD0`, VA `0x15145CD0..0x15145DB4`, ROM
`0x173180..0x173264`, transforms points through two lists of pointers. The
descriptor supplies three float angles before `func_150A8050` and three
signed translation halfwords after it. Positive counts traverse both lists
in four-byte strides, forwarding XYZ and destination addresses to the point
helper `func_150A7960`. Nonpositive counts still build the matrix and read
translation; they do not touch either list.

The recovered source in [game_16EE20.c](../../conker/src/game_16EE20.c)
uses the descriptor and input-list cursor in successive phases of one pointer.
All descriptor reads finish before that pointer is reassigned. Destination
cursor initialization also follows the matrix provider. These real lifetimes
produce the original incoming A1/A2 spills and reloads, save homes and matrix
offsets without volatile ABI casts, dummy work or a profile change.

| Body | Complete Words | Frame | Raw Differences | Linked Differences |
| --- | ---: | ---: | ---: | ---: |
| Historical semantic C | 57 / 228 bytes | `0x88` | 46 | 46 |
| Recovered lifetime C | 57 / 228 bytes | `0x88` | 19 | 0 after checked normalization |

This is **not a direct-C byte match**. Unchanged O2/g3/MIPS2 emits every
instruction; nineteen expected-word guards normalize only:

- A closed saved-register allocation cycle `s0 -> s1 -> s2 -> s0` through
  the descriptor/list/count body. Save and restore homes stay physical.
- Independent prologue save stores at `+0x8/+0x20` and independent argument
  moves at `+0x10/+0x14`.

No private offsets or incoming homes move. No instructions are inserted or
omitted. No constant or jump-table pool is added. Calls retain their actual
`R_MIPS_26` relocations at `+0x38` and `+0xB0`; no guard touches either call.
ABI types remain `u8 *`, two `struct17 **` lists and signed32 count.

## Measured Controls

[Candidate driver](../../tools/experiments/game_point_list_transform_candidates.py)
adds **40 meaningful measurements** while retaining the historical 48:

- Twelve address-taking/volatile parameter views produce genuine reloads but
  59-61 words/frame `0x90`, not the retail slot.
- Twelve structure/inline/typed-descriptor/word-view controls produce 57-60
  words with frames `0x80..0x90`; none raw exact. Word-ABI controls remain
  experiments, not installed interface changes.
- Eight descriptor/input phase controls: explicit cursor reuse with separate
  source/destination locals produces C57/frame `0x88`/19 differences; inlining
  produces C57/frame `0x80`/27, and union forms do not recover the slot.
- Eight meaningful count/register controls retain C57/frame `0x88`/19 for
  register qualifiers or C59/frame `0x88`/57 for extra count locals.

The bank is 40 measurements, not 40 distinct emitted bodies. Every measurement
passes 18 ordinary public-effect fixtures, **720 candidate executions**.
No raw exact candidate is claimed. Selected raw C additionally passes the
complete incoming-home and full-memory qualification below.

## Maintained Qualification

[Eight match tests](../../tools/tests/test_game_point_list_transform_match.py)
compare raw selected C, normalized C and all 57 original wrapper words:

- **1,344 guest fixtures**, including seven signed count patterns, 16 data
  patterns, three aliases, provider mutation and both stack phases.
- **576 connected fixtures** execute all 40 words of the original point
  helper. All 57 wrapper and all 40 helper words are covered; the rotation
  provider remains a bounded hook validating the complete matrix.
- **2,304 incoming-home fixtures**, rewriting source, destination or both
  homes independently at both stack phases, including zero and positive
  counts. Raw, normalized and original match on complete memory including
  stack bytes, public traces, calls and saved state. These are deliberately
  nonstandard guest ABI probes, not permission for native C callees to alter
  their caller's argument homes.
- **131,076 actual native 32-bit cases**, correlated sweeps of every signed
  halfword pattern in each translation field with both provider mutation
  modes. Validate all five input/output records, descriptor fence bytes and
  four nonpositive/null-list routes. Native point arithmetic is a validating
  copy hook, not full SDK matrix arithmetic or a 64-bit port test.
- **16 required-storage removal fixtures** fail closed for all three bodies;
  four nonpositive routes skip unmapped list/point/output storage.
- Seven compiled negatives change public storage: unsigned translation,
  exact-one count gate, wrong source stride, cached first source, wrong
  destination list, translation before the provider and historical retained
  lists. No ineffective negative is counted.
- Copied owner retains 89 functions, all 88 non-target bodies and relative
  relocations, normalized pools and both existing pointer warnings. Selected
  raw owner bytes equal the isolated 228-byte body. The real padder emits all
  57 words without overflow; both call targets independently rebase by
  `0x01000000` with the corresponding linked call changed and others intact.

The [historical audit](../../tools/tests/test_game_point_list_transform_audit.py)
retains its old body, controls and mismatch fixtures. Its installed-source
gate now explicitly pins the recovered match, while the retained mismatch
receipt is named historical, not current-production.
[Guard-history helper](../../tools/tests/game_owner_pool.py) preserves every
earlier checkpoint and pins the new nineteen-row suffix at index 11,006.

The normalizer's initial probe omitted the `LH` register-field opcode; its
full-word assertion caught the omission. It was corrected before the seven
pre-install tests, all of which passed in 53.546 seconds. No failed probe is
counted as qualification.

## Linked Audit And Regression

The US ELF rebuild passes. A fresh `7f1de4a6` before snapshot and linked after
snapshot verify:

- Exactly one changed body, `func_15145CD0`, among 6,042 retail slots /
  6,058 linked symbols. All other 6,041 retail bodies and all 16 overflow
  symbols stay unchanged.
- All addresses and extents stay fixed. `.init`, `.init_data`, `.debugger`
  and `.game_data` hashes stay unchanged. All 720 Game-data owners and
  189,088 bytes remain exact, zero different bytes.
- All previous 11,006 guard rows stay identical; nineteen appended rows
  bring the total to 11,025. Conversion progress file hash stays unchanged.
- All 57 target words are byte-exact; total **3,361 / 5,466 (61.49%)**,
  Game **2,688 / 4,793 (56.08%)**, **2,105 still different**, zero address
  drift. Init remains 492/492 exact and Debugger 181/181 exact.

The full rebuild retains unrelated baseline warnings; the affected copied
owner has exactly its two old pointer warnings, with no new diagnostic.
The combined match/historical-audit/translator/owner-pool/padder regression
passes **34 tests in 319.291 seconds**, zero skips/errors/failures:

```sh
make -C conker -j4 build/conker.us.elf
python3 -m unittest tools.tests.test_game_point_list_transform_match tools.tests.test_game_point_list_transform_audit tools.tests.test_game_matrix_translation_recovery tools.tests.test_game_owner_pool tools.tests.test_pad_c_object_word_patches -v
make tools-check
python3 -m py_compile tools/experiments/game_point_list_transform_candidates.py tools/tests/test_game_point_list_transform_match.py tools/tests/test_game_point_list_transform_audit.py tools/tests/game_owner_pool.py
```

Tool/syntax/scoped-whitespace checks pass. All **3,924 relative links across
79 documents** resolve, zero broken. After clarifying the historical mismatch
test label and removing an unused import, the historical-home/current-installed
pair passes again: two tests in 7.254 seconds, zero skips/errors/failures.
Receipts live under ignored
`conker/build/game-point-list-match-test/`.

## Continue

1. Recover the contiguous record-batch counterpart `func_15145DB4`, a
   60-word retail slot in the same owner. Inspect its original record stride
   and private lifetime before carrying over any pointer-list source shape.
   Original frame is `0x98`, matrix begins at `sp+0x58`, and three destination
   coordinate cursors advance by twelve. Destination home reload precedes
   the count gate; source home reload occurs only on the positive route.
2. Matrix translator `func_15142314` remains C49/frame0/34 differences;
   its scheduling and all 178 retained controls are unchanged here.
3. Sampler `func_151432BC` still needs its per-path RA loads and circle RNG
   byte schedule. No sampler code or new sampler measurements here.

This is guest decomp matching, not new hardware/FCSR/rendering/gameplay or
PC-port acceptance. No sibling source, frozen Release, save, runtime or push
action is part of this checkpoint. The main README receives aggregate rows
only; detailed updates belong in this note and the documentation indexes.
