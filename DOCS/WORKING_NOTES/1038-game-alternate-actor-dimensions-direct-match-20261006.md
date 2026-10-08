# Game Alternate Actor Dimensions Direct Match

Date: 2026-10-06. Starting checkpoint: `2facc8e0`.

Continuation: [Note 1039](1039-game-actor-position-queue-wrapper-direct-match-20261006.md)
completes the queued actor position-wrapper recovery and connected qualification.

**`func_1515C244` matches its complete 43-word / 172-byte slot:**
41 words directly from C, followed by two retail zero-padding words.
VA 0x1515C244..0x1515C2F0, ROM 0x1896F4..0x1897A0, no frame.
Replace the zero-return stub in
[generated_188F90.c](../../conker/src/game/generated_188F90.c) with the alternate
dimension/XYZ query, using the existing O2/g3 profile and real actor/point
layouts. No new guard, profile, header, symbol-anchor, metadata or data edit.
The ordinary generated-slice padder supplies the two zero words; they are
not another recovered operation or an executed return tail.

## Recovered Signed Fields And Access Order

This is the adjacent query's +0xE4/+0xE6/+0xE8 variant. Actor ID byte +4
below 0xBB selects two signed halfword-to-float dimension outputs and XYZ,
with signed +0xE8 added to Y. IDs 0xBB..0xFF get two 1.0f outputs and plain
XYZ. The redundant `ID != 0xFF` after the below-0xBB comparison remains to
preserve retail branches. Dimension terminology describes the routine shape;
full caller/geometric meaning is not established here.

Existing `struct127.unkE4` and `.unkE6` are signed. **`.unkE8` remains unsigned
in the shared header**, but retail reads it with `lh`. A local `(s16)` view
recovers that signed load without globally changing actor semantics. The
unqualified unsigned expression gives the wrong vertical result for negative
16-bit values and is detected by a negative test.

Preserve sequential writes and late reads: dimension one is written before
dimension two is read; both precede the X read/store; X is written before
the vertical halfword and Y are read; Y is written before Z is read. Aliases
can change all these later inputs. Do not snapshot actor fields or all
outputs first. The cached-fields negative control demonstrates different
results when the first dimension output overwrites +0xE4/+0xE6.

## Compiler Controls

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_actor_alternate_dimensions_candidates.py)
uses actual SDK/structure headers. Four source forms under four profiles:
**16 controls**, all isolated diagnostics empty.

| Forms | Profile | Body / Padding Words | Differences |
| --- | --- | --- | --- |
| Direct fields, cached ID, early return | O2/g3 and O2 | 41 / 2 | 0 |
| Reversed float-add operands | O2/g3 and O2 | 41 / 2 | 8 |
| Direct fields, early return, reversed add | O1/g3 and O1 | 43 / 0 | 42 |
| Cached ID | O1/g3 and O1 | 44 / 0 | 43 including one overflow |

Six controls match the complete padded slot. The default direct-fields
O2/g3 form is installed; no experimental profile. O1's 43-word forms fit but
remain different, unlike the previous query's smaller slot where they
overflowed. Ignored receipts: `conker/build/game-actor-alternate-dimensions/`
and `conker/build/game-actor-alternate-dimensions-test/`.

## Qualification

[Five tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_actor_alternate_dimensions_match.py)
bind the complete direct slot/padding, source, preserved unsigned header
field and absence of guards; reproduce all 16 compiler controls; compare
an independent sequential reference with retail and selected guest bodies;
and exercise actual C natively.

- **43008 guest cases, two bodies**: all 256 ID bytes, six signed-dimension/
  finite-coordinate sets, fourteen aligned output-alias layouts and two
  stack phases. Exact ordered access traces, every non-stack memory byte,
  no calls and saved GPR/FPR/SP/RA lifetimes are checked.
- Aliases cover shared dimension/point outputs, actor positions, writes
  into +0xE4/+0xE6 before the height read, +0xE8 before its signed read,
  point stores across those fields and writes into ID after its cached gate.
- **All 40 reachable words execute**. The branch-likely delay at
  0x1515C258 cannot execute after the cached ID<0xBB test, and padding at
  0x1515C2E8/0x1515C2EC is never reached. Tests structurally bind the gate,
  signed +0xE8 load and zero padding. No 43-word execution-coverage claim.
- **21504 native cases** use the actual actor-header prefix through +0xEA,
  actual point layout, explicit offsets and selected C. An independent
  byte-storage reference checks all 1088 storage bytes. Native little-endian
  overlap effects are checked locally, not asserted equal to cross-halfword
  big-endian effects; guest tests separately cover retail memory order.
- Negative controls detect the stub, threshold 0xBC, unsigned vertical
  offset, unsigned first dimension and premature cached-field reads.

The preceding query's test helpers now accept optional field offsets and
entry address; defaults retain its original behavior and tests. No shared
guest instruction runner changes. Four pre-install tests pass in
**41.670 seconds**, no skips. Qualification is bounded aligned ordinary
memory and finite single-precision arithmetic, including signed zero and
coordinates around 2^24. It does not establish arbitrary pointers, all caller
domains, MMIO/concurrent inputs, NaN/Inf/subnormal/FCSR modes, hardware
execution or gameplay acceptance.

The complete post-link suite passes **all 52 tests in 228.619 seconds**,
no skips: both actor queries, projection compiler/identity audit, descriptor
measure, pair clamp, indexed state-save, random timer and effect-packet
regressions. The preceding query's unchanged default helper behavior is
reverified by all its original tests.

## Whole Linked Audit

NON_MATCHING ELF/progress/match-progress rebuild passes. Compare all **6059
linked slots** with the preceding actor-query checkpoint: only `func_1515C244`
changes; every address/slot size remains fixed. Init, Init data, Debugger and
Game data are byte-for-byte unchanged. All **720 Game data owners / 189088
bytes** remain retail-exact; all **10646 guard rows** retain content/order.
Target slot SHA-256:
`d507057468e2a01262175d62a55e20fb405c07233430660d4f4a4255ef39d27c`.

Committed baseline and current complete owners compile independently after
the normal assembly processor: both have empty compiler diagnostics. Shared
headers are unchanged. The existing duplicate generated-recipe build warning
remains; no project-wide warning-free claim. README updates only aggregates:

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3316 / 5462 (60.71%) | 0 | 2146 |
| Game | 2643 / 4789 (55.19%) | 0 | 2146 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes remain unchanged because the old stub counted as C.
No sibling host source/build/save/frozen Release edit or push.
Root `make tools-check` and `git diff --check` pass. Documentation check:
3196 relative links across 21 documents, zero broken.

## Next Work

Inspect `func_1517D5FC`, still a zero-return stub in
`game/generated_1A89B0.c`: 37 retail words, ROM 0x1AAAAC, frame 0x28.
Retail sign-extends three coordinate arguments, selects an actor by 0x9A0
stride from `D_800DBFF0`, forwards actor float bits at +0x380, two additional
arguments and `D_800DDD1C >> 3` to `func_1517D578`. That queue helper has a
real C body; bind its linked identity and qualify the wrapper's argument
handoff and connected bounded queue before installation. Read-only inspection
confirms its complete 33-word linked helper is already retail-exact; the
wrapper's 37-word placeholder still has 36 differences. Receipt:
`conker/build/game-actor-alternate-dimensions-test/next.json`. This is static
inspection, not a new wrapper recovery or complete call-chain acceptance.
Projection/pair-clamp frames remain open; the Game matching goal stays active.
