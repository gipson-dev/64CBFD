# Movement Clamp Acceleration And Pitch Lifetimes

Verified 2026-10-17. Consumer predecessor `3c1869e7`, tools predecessor
`852c2eb`; both active repositories began clean. The previous turn was
progress. Continue the same complete `func_150F34F4` from
[Note1519](1519-movement-flag-path-lifetimes-and-cfg-role-proof-20261017.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

The complete C candidate improves **389 to 270 raw differences**. Its existing
28 research rewrites now leave **242 differences**, versus 361 previously.
There are **zero new research or production guards**: the private CSV is
byte-identical to Note1519's table. Both objects retain all 959 words/frame
`0x80`; neither is installed or credited as a fully matched conversion.

| Measurement | Raw C | Research-Normalized Object |
| --- | ---: | ---: |
| Complete words | 959 | 959 |
| Frame | 128 | 128 |
| Different words | 270 | 242 |
| Exact opening words | 361 | 469 |
| First unequal PC | `0x150F3A98` | `0x150F3C48` |

Compared with the prior raw candidate, 284 emitted words change: **143 become
exact and 24 previously exact words differ**, a net gain of 119. This is not
a claim that every changed word improves or that the first GPR gap is closed.
The clamp span `0x150F3CB4..0x150F3D00` (20 words) and unmasked pitch span
`0x150F3E50..0x150F3EB4` (26 words) now match directly from C without guards.

## Complete Source Controls

`tools/experiments/game_actor_input_movement_heading_continuation.py` protects
**307 predecessor entries / 283 distinct paths**. Twenty-nine complete source
forms cover clamp lifetimes, signed heading temporaries, acceleration branch
shape, early signed Y sampling and the pitch zero lifetime. All preserve eleven
raw neighbors and pools. One 961-word form is correctly rejected by the padder.
Shorter 956/958-word forms are measured with their real extents and actual
padding, not called 959-word matches or trimmed into shape.

The selected form combines these recovered source relationships:

- Both held-free velocity comparisons assign the existing `velocity` float.
  A single assignment shortens the routine; both retain its complete shape
  and recover the FPR2 lifetime. The clamps alone give 382 raw differences.
- The two acceleration-stop conditions are an exclusive `if` / `else if`.
  This preserves the previous goto's semantics and recovers retail's separate
  true-path store/jump shape and retained duplicate instructions.
- The signed controller Y byte is sampled into existing signed `index` scratch
  before the vertical-velocity/acceleration stores. The B8 snapshot uses
  `value`; conversion and arithmetic still occur in the complete routine.
- The unmasked pitch calculation subtracts existing `contactHeight` while
  it is still its initial zero, retaining retail's explicit subtraction.
  Splitting this calculation into two assignments gives 307 differences;
  introducing a separately named signed `stickY` gives 273. Neither replaces
  the better qualified combined 270-difference form.

The combined early-Y/exclusive-branch form first had 958 words / 363 overlapping
differences. Restoring the real zero-valued subtraction recovers the 959-word
slot, matching early constant/controller-address hoists and most of the
following FP/control layout. This measured combination, not a broad compiler
profile change or arbitrary instruction patch, accounts for the large gain.

The new measurer calls the existing complete-owner measurer directly after
the stronger 307-entry freeze. This avoids re-running every historical wrapper's
redundant freeze, while retaining the original compiler/owner, pool, neighbor,
link, actual padder and stronger predecessor checks. The repeated baseline
controls reproduce the same old object; no shared helper is edited or gate
monkeypatched away.

```text
Factory: tools.experiments.game_actor_input_movement_heading_continuation.selected_body()
Form: exclusive-Y-index-height-zero
Raw target SHA256: febe5b0f8847416cc6e090fb028ffaf84533df97e551d98a7eceead8975eddb6
Normalized target SHA256: 91aea57be0905e303383818b3e09a1fed3c58dcfcaab30961178dba4ac27f6f1
Isolated source SHA256: d16663a7b5af1f8b17fe5f9a2163b0b9e157b08a5f30435c4a6ce2616c123222
Research CSV: unchanged 28 rows, zero added rows
Raw / research-normalized differences: 270 / 242
```

## Zero Lifetime And Actual Read Order

The new zero-use assumption has an executable **C AST check**, not just a
comment. Existing GCC preprocessing removes comments; installed pycparser
parses the complete selected function. It verifies the first executable
statement initializes `contactHeight` to `0.0f`, only four identifier uses
and two writes exist, no address escapes, and the pitch read occurs before
the only conditional `50.0f` update. That update follows the later physics
callback. The only goto is the existing forward disabled-exit jump, before
the pitch; no loop encloses the pitch read. Eight effective malformed-source
controls reject changed initialization/update, missing dominance, extra write,
escape, enclosing loop, new jump and changed pitch use.

This is a C-ABI local-lifetime fact. Arbitrary providers observing/modifying
unpassed caller stack storage, raw private registers and hardware/FCSR parity
remain outside the claim. No new dependencies are installed.

**Sixteen new guest alias cases** independently compare actual retail with raw
and normalized candidate execution. The actor's vertical-velocity word overlaps
controller bytes; buttons `0x4010/0xC010`, four signed Y values and two stack
phases ensure the pitch gate really fires. Both new objects agree with retail
in public memory, calls, observations and fired provider mutations. The previous
C candidate fails all sixteen, because its late Y read follows the zero store.

The previous high-level reference model samples Y late too, so it is explicitly
not used as the oracle for these new alias cases. The unchanged model remains
used for its established non-overlapping corpus. Portable C type-alias/native
byte-order equivalence is not inferred from these guest-only overlaps.

## Qualification

The final **nine-test run passes in 112.358s**. The preceding run passed eight
tests but exposed an ineffective negative: changing only a comparison while
retaining the old stored bound leaves public output unchanged. Both comparison
and stored value are now changed in the two wrong-limit controls; the complete
compiled negative bodies demonstrably reject. Earlier incomplete runs are not
counted as successful qualification.

- Twenty-nine source/extent controls, actual owner padding, target relocation
  preservation and all eleven raw/padded neighbors. The unchanged private table
  changes the same 36 bytes in 28 words. Existing turn/flag proofs re-run on the
  new body, including the new 409-state post-call scan. Their prior 95-control
  and 3,072-case kernel suites remain prior receipts, not fresh tests here.
- Eight effective AST zero-lifetime controls and sixteen effective old-candidate
  alias rejections against actual retail, with the pitch gate fired.
- Three-way retail/raw/normalized execution of **2,496 public cases**, twenty
  modeled FP edges, all nine provider-mutation modes and actual 21-word curve
  execution. All 947 reachable retail words remain covered; twelve original
  unreachable duplicate words are retained, not trimmed.
- The prior 36 cap boundaries still pass, including 24 actually entered cap
  cases. **Forty new clamp cases**, twenty with the held-free gate entered,
  cover adjacent floats around -34/26, signed zero, held gating and provider
  mutation before the clamp. Both complete wrong-limit C controls reject.
- **100 active states / 6,600 equal private fault prefixes** still stop first
  at `0x150F3C6C`. All 80 disabled final states / 2,700 fault prefixes and all
  160 mode-0 final states / 8,320 fault prefixes remain equal. These are bounded
  checks, not whole-function private acceptance.
- Native32 O2/O0 UBSan: **169 cases/profile**, eight effective controls, including
  twenty new clamp cases, nine unsigned-heading extremes and ten cap cases.
  Actual normalized-object rebases pass two links/twelve cases; twelve established
  guest aliases also agree. The new overlapping-Y cases stay guest-only.
- A fresh owned compiler capture finishes exit0 and equals the normal complete
  object, with **74 emitter events / 686 AS1 instruction records**. Actual frontend,
  optimizer and rounded local budgets remain 84/76/80; frame128, saved16,
  outgoing32 and all earlier homes remain unchanged. Upper/lower frontend stores
  use float M-32; optimizer upper uses R34, while the lower marker has no STR.
  Both actual FPR2 loads are independently checked. Signed Y uses J4 M-48/R3;
  pitch uses float M-64 and optimizer R34/R32. Twenty-nine effective new layout/
  instruction controls reject. Normalized output is not called AS1 output.
- All 307 protected entries, 6,057 installed bodies, 189,088 Game-data bytes /
  720 owners, callback slot `0x80086068` and ten immutable first-image members.

## Banked Baseline And Continuation

Tools **ad45714** is committed first. Both tools copies freshly pass twelve
shared tests and smoke checks; four ASCII/AST parses and two identical task
pairs pass. Both mirror destinations were absent. All **1,164** prior hashes
and HEAD `ddbdd16b` survive, with **1,166** dirty paths afterward. No mirror
commit/reset/clean, push, dependency update or Claude call.

Production ELF SHA256 remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different, zero drift. Init492/492 and
Debugger181/181 remain exact among converted functions. Root README remains
unchanged. No production build, host-port or frozen Release action.

Scoped AST graph refresh completes with **42,307 nodes / 82,433 links / 4,050
communities**. The new note is indexed; only three shifted UPDATE_LOG heading
IDs disappear, with their labels retained at new locations. All 19,398 existing
excluded nodes from 2,972 still-present files remain preserved; no purge or
full re-extraction is performed.

```sh
python3 -m tools.experiments.game_actor_input_movement_heading_continuation --group clamp
python3 -m tools.experiments.game_actor_input_movement_heading_continuation --group continuation
python3 -m tools.experiments.game_actor_input_movement_heading_continuation --group combined
python3 -m tools.experiments.game_actor_input_movement_heading_continuation --normalize
python3 -m tools.experiments.game_actor_input_movement_heading_continuation --reuse-trace
python3 -m tools.tests.test_game_actor_input_movement_heading_continuation -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned complete sources, raw/normalized objects, private unchanged guard CSV,
trace and qualification receipts are under
`conker/build/game-actor-input-movement-heading-continuation/`. Earlier frozen
captures are untouched. Do not restart the successful owned trace merely to
re-read it; `--reuse-trace` validates its source/compiler/object identities.

- [x] Recover the combined clamp, exclusive acceleration and signed-Y/pitch
  lifetimes, reducing real C differences by 119 without adding guard rows.
- [x] Qualify the zero lifetime, actual retail Y ordering and complete candidate.
- [ ] Continue **the same function** at normalized word469 / `0x150F3C48`:
  LH uses raw GPR11 versus retail GPR13, followed by add/MTC1 raw12 versus14.
  The normalized private frontier is still `0x150F3C6C`. Recover/prove those
  bounded heading roles and subsequent flag/constant roles without a global
  rename; further signed-Y scheduling and commutative FP words also remain.
- [ ] Complete remaining literal/private/caller/provider/first-image gates
  before installing the complete function; keep the wider Game goal open.
