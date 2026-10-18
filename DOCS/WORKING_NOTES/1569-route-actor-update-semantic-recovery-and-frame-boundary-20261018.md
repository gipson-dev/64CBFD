# Route Actor Update Semantic Recovery And Frame Boundary

Date: 2026-10-18. **Complete private C candidate; not installed; zero credit.**

## Target And Baseline

Continue the Game goal after [Note 1568](1568-route-record-setup-installed-byte-match-20261018.md).
The prior turn made verified progress: func_150870D0 was installed, audited
and committed in consumer **aa506ab6**, with tools **38eefad** first.
This turn banks tools **a71464c** before the consumer pin and documentation.

Target **func_15087350**, owner generated_B3020, VA `15087350..15087CC0`,
ROM `B4800..B5170`, **604 words / 2,416 bytes / frame 0x1C8**. The production
body remains the original three-word C placeholder, not retained assembly.
The private candidate has the recovered interface:

```c
void func_15087350(s32 recordIndex, s32 active, f32 lookAhead);
```

Do not install this checkpoint or replace its original symbol with a guessed
public API name. Its source comment describes the observed route projection,
look-ahead update and player ranking; raw byte views do not identify original
source structs or field names.

All **23 production/reference inputs remain frozen**. In particular:

| Input | SHA-256 |
| --- | --- |
| Whole ELF | `3c8fd0411cd80d7a66440b81db22eef663fc8d557d365cdbbf5b3ce43dd5591a` |
| B3020 source | `fb512dd6fda54a37ab8adb84fa5efc50527941de4c622d66e12c6c3481c8ddbd` |
| Guard manifest | `cc92cdc4549964c1e9ebca306ee85ff5b7e57392a657bd9b15386384a8ab49d4` |

No production source, guards, Makefile, ELF, progress CSV or root README edit;
no production build or fresh matching recount. Note1568's installed totals
remain **Game 2,991/4,828 (61.95%)**, **total 3,664/5,501 (66.61%)**,
**1,837 different / zero address drift**. Do not count this private recovery.

## Complete Body And Interface

Recover every major block, not just the previously tested vector windows:

- Gate the null record table, compute the modular 32-bit 0x84-byte row offset
  and use the signed actor byte with the 0x32C-byte actor stride.
- Capture the actor's X/Z position, clear the route event, and choose either
  half-width or a separately clamped one-eighth width-target adjustment.
- Rebuild four-point vectors when required, evaluate both cubic derivatives,
  normalize the negative tangent, and form the actor's signed projection error.
- Correct only errors outside inclusive +/-50, reduce the gain after worsening
  error, clamp each progress step to +/-0.5 and stop after eleven iterations.
- Preserve the effectful selection call, old/new signed tick bytes, output
  speed arithmetic, copied-row double look-ahead, and three output coordinates.
- Retain full-width active-zero/float conversions, low-byte active storage,
  unsigned byte retest, event-specific actor values, object-coordinate truncation,
  human-row projection, modular timer update and conditional finalizer call.
- Build all score/index entries and stably rank descending, including the
  signed lap-byte bonus and low-five-bit masked-player shift behavior.

A whole-Game retail direct-call scan finds exactly two sites:

| Caller | Site | Observed Interface |
| --- | --- | --- |
| func_150538CC | `150539C0` | A0 contains the lookup result, A1 is zero, F16 is copied to A2; the call delay saves F16 |
| func_1509DFC4 | `1509E1D4` | A0 loads the command's full word, A1 loads its full word in the delay slot, A2 is `3DCCCCCD` |

Both callers overwrite V0 before any observed consumer. Sixteen actual caller
window cases execute the complete retail or candidate callee, its connected
helpers, actual argument/delay words and return consumer, with two V0 poisons
and both stack phases. The dispatcher return is an unconditional branch;
its fired checkpoint is the dispatched delay word, not an invented ordinary
branch execution. Full callers and unknown indirect interfaces remain unproved.

## Fresh Qualification

**All 12 focused tests pass in 40.108 seconds, no skips.** The initial test
first rejected the existing zero-return body on ordinary output differences.
The final suite requires the complete candidate and its frozen raw fingerprint.

**703 paired end-to-end real-helper cases** use an independent ordered-binary32
reference, complete public memory and canonical call contracts:

- 216 index/mode/active/position/stack-phase cases.
- 80 effectful selection-provider cases: three event values, mode/finalizer
  transition, or refreshed tick globals and a negative signed previous tick.
- 319 ranking cases, including all 256 lap bytes, stable ties, signed halfword
  tick extremes, masks and signed counts -128/-1/0/1/2/16/17.
- 16 null-table/full-width modular-index/signed-actor cases, including actor
  bytes -128/-1/0/31/32/127 and hardware-equivalent low-five-bit shifts.
- 72 full-width active/signed-old-tick cases, including byte-zero/full-word-
  nonzero active values and modular timer overflow.

Execute the actual current linked **494 helper words**, independently equal
to retail: vector83, cubic49, derivative62, progress212 and neighbor88. Use
the six scalar constants (28 bytes) from the frozen production ELF for these
real-helper cases. The base 216-case corpus reaches **569/604 caller words**;
do not report whole-instruction coverage from that corpus.

Additional checks:

- Six axis-aligned numeric-provider witnesses cover exact error +/-50,
  adjacent representable outside values and the eleven-iteration limit.
- Seven newly compiled semantic negatives produce ordinary wrong outputs or
  call contracts: inclusive upper error bound, ten-iteration cap, unsigned old
  tick, byte-only active-zero test, half look-ahead, unsigned lap and ascending
  ranking. Crashes, missing mappings and exhausted budgets are not credited.
- Six complete source forms in two real compiler profiles preserve all 72
  other owner bodies and normalized pools. An additional 144 paired guest
  cases check the forms; none is accepted as an installable match.
- All 588 raw-word mutations and all 70 binding mutations are rejected by
  the selected payload fingerprint gate. These are fingerprint controls,
  not 658 additional semantic-negative programs.
- Both actual caller windows restore saved GPR/FPR state and ignore the
  poisoned callee V0. This is bounded caller evidence, not whole-parent proof.

The opaque contracts remain selection128, bcopy, finalizer13 and sin/cos.
The static analysis VA decodes bcopy's JAL to `10023A10`; the bounded hook
implements source-first byte copy. This is not execution or rebasing of the
runtime SDK address `80023A10`. Trig uses a bounded host numeric provider;
no native retail trig, hardware, FCSR or full gameplay equivalence is claimed.

## Explicit Matching Rejection

The selected complete source is **588 words / frame 0x1E0 / 599 positional
word differences**, with 70 relative relocation bindings. It is not a match.

Raw target SHA-256:
`03e0bcd8128c750b74ad4594a9ce0cf24b83faf78b5b1276e4ae1425aaf436e8`.
Canonical binding SHA-256:
`401747e4fa7527b029b18bc9f3754e4322e42aa48d90ad2f9f7ffd81b308b7ab`.

Observe the rejection directly at the first saved-RA write:

| Model | Address Relative To Incoming SP | Value |
| --- | --- | --- |
| Retail | `SP - 0x1C8 + 0x44` = `SP - 0x184` | `DEAD0000` |
| Raw C | `SP - 0x1E0 + 0x3C` = `SP - 0x1A4` | `DEAD0000` |

Both complete ordinary runs finish with equal public output and saved ABI,
but their private memory differs. This is an observed store/address boundary,
not a complete fault-prefix or hardware-exception proof. No frame guards,
binary normalizer, raw instruction substitution, padding or installation.

| Source Form | No-Unroll Words / Frame / Differences | Normal Words / Frame / Differences |
| --- | --- | --- |
| Initial selected source | 588 / 480 / 599 | 622 / 480 / 616 |
| Reuse loop step/value carrier | 590 / 488 / 479 | 624 / 472 / 619 |
| Reuse disjoint float temporaries | 588 / 472 / 538 | 622 / 472 / 612 |
| Initial with late ranking-role reuse | 578 / 480 / 600 | 613 / 472 / 609 |
| Loop carrier with late reuse | 580 / 480 / 571 | 615 / 472 / 608 |
| Disjoint floats with late reuse | 578 / 472 / 566 | 613 / 464 / 606 |

The lower479-difference point has the wrong extent and a larger frame. The
464-byte normal-profile point is still oversized at613 words and frame464.
Keep all screens as diagnostics; do not select a point by difference count
alone or treat reusable dead locals as evidence of original source types.

## Bank And Resume

Tools **a71464c** first. Both tools copies pass three repository-setup tests
and project-tool smoke checks; consumer `make tools-check` passes. The two
new task files are identical, ASCII and AST-valid in both copies. Preserve
all **1,279** prior dirty mirror hashes and its ddbdd16 HEAD; adding only the
two absent task files leaves **1,281** dirty leaf paths, without a mirror commit.
No push, Claude invocation, debugger attach/capture, emulator, host edit or
frozen Release action. Existing REA MIPS adapter limits require no setup retry.

Reproduce under the existing WSL toolchain:

```sh
python3 -m tools.experiments.game_route_actor_update --screens
python3 -m unittest tools.tests.test_game_route_actor_update -v
python3 -m tools.experiments.game_route_record_integration --audit
```

Ignored `conker/build/game-route-actor-update/` contains the 23 before snapshots,
complete proposed owners, real compile commands, objects, linked candidates,
screen bank and per-test receipts. Do not overwrite the original frozen inputs.

Continue **the same func_15087350**. Recover604/frame456, the original three
saved FP pairs and stack array/scalar homes, then fit literal scheduling/roles.
Complete native32/UBSan, private/alias/access-prefix and full binding/word
qualification before installation. Larger positive counts above17, invalid
pointers, unbounded/invalid conversions, NaN ranking and universal portable-C
semantics remain outside this finite checkpoint. After an actual match, require
both owner profiles/72 neighbors, existing projection override and four
GLOBAL_ASM bodies, actual padding/Make, independent GNU rebases, first whole-ELF
prediction, production installation, data/address/body audit and fresh recount.
Keep the installed setup/vector/spline/dispatcher baseline fixed. Wider Game
work remains active; this checkpoint earns **zero** matching/conversion credit.
