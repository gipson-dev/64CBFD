# Packed Triangle Facing Predicate Match - 2026-11-07

`func_1510E670` replaces its zero-return placeholder with the triangle-facing
predicate used by the three orientation checks in `func_1510E950`. Its complete
77-word slot is byte-exact, including the original 88-byte frame. Three guards
normalize a closed final floating-register rename. The normal owner profile
and every neighboring linked instruction remain unchanged.

Fresh production count: **4240/5512 = 76.92%**, Game **3567/4839 = 73.71%**,
Init 492/492, Debugger 181/181, zero drift. **170 more** exact functions reach
4410/5512, the 80% threshold. This is one additional exact C function; the
conversion denominator and conversion CSV remain unchanged.

## Recovered behavior and interfaces

- Entry 1510E670..1510E7A4, retail ROM 13BB20..13BC54, 308 bytes.
- Owner `conker/src/game/generated_13BB20.c`, normal IDO 5.3 O2/g3, O32.
- Interface `s32 func_1510E670(s32 index)`; the original three calls pass a
  full-word index and consume an integer rejection/acceptance result.
- Select a 16-byte entry at D_800D3300 + index*16. Load the offset-list pointer
  at +4 and vertex-base pointer at +8. An absent list returns zero.
- The first three unsigned list words are **byte offsets**, added to the base.
  Read three signed s16 coordinates at each selected point. Build second-minus-
  first and third-minus-first edges using integer subtraction before conversion
  to f32, then call the original handwritten `func_150AD8B0` cross product.
- Reject a negative normal Y, accept zero and positive Y. The ordered negative
  comparison also accepts an injected NaN; this is tested as a helper contract
  control, not a claim that finite signed-halfword geometry creates NaNs.

The shared scratch/table symbol was previously declared as one s32. The native
object-size sanitizer correctly rejected a table read through that declaration.
It is now an s32 array, and the coordinate-query neighbor explicitly reads
`D_800D3300[0]`. All 13 raw and padded neighbors, including that query, retain
their complete words and bindings. No shared header or caller source changes.

## Matching and independent image proof

Predecessor consumer 2b3fdc4777ee0d7dfbaa5097bf96d23babaec0ad; tools
5333053f8dbbcc2820430a57b89b6e15383f207e. The preparation freezes 101
source/header/compiler/input files. Complete GLOBAL_ASM preprocessing and
postprocessing preserve the 830-word assembly caller in this owner.

An early-return body emits 76 words. Retaining the original enclosing non-null
branch and both explicit orientation returns recovers all 77 words, the frame,
all private arrays, and the original three bindings. Scalar/register-normal-Y
controls instead grow the frame to 96 and are rejected.

Raw target SHA-256:
`2c666272900b9d24ade495e477190530d66ddd2fecc4931be539254671c08819`.
Only words 62, 63 and 65 differ: load normal-Y into F4 instead of F0, create
positive zero in F6 instead of F4, and compare those corresponding roles.
The guards rename exactly those definitions and their comparison; no store,
branch, call, relocation, extent or frame changes. Both temporaries are dead
after comparison and are caller-clobbered O32 registers.

Production and strict padders agree on the complete owner. All 13 raw/padded
neighbors and allocatable pools agree. Actual Make's five-command copied-owner
recipe reproduces the qualified object, including GLOBAL_ASM processing.
Two independent GNU links verify all three relocations and signed LO16 carry.

The independently predicted whole ELF equals the actual production ELF after
**210 changed bytes, zero exclusions**: only this function's instructions and
symbol size change. All 6052 function addresses and other bodies are fixed.
All 189088 protected data bytes across 720 owners remain literal exact. The
guard manifest preserves its complete prior byte prefix and appends three rows.
No profile or Makefile change, metadata permutation, data exclusion or wholesale
function replacement is used.

Production fingerprints:

| Artifact | SHA-256 |
| --- | --- |
| ELF | 2050d53ddcc1b2fa2d1cfba360db22a2abba2bb51a68e06c7d35482693d8efda |
| Binary | a37945f171fc1275b9d7e75f61e0440e87868db027705b1438acff855cf016e8 |
| Owner | 4288a7df8042b933b53b0b0989aa7cbac8095b6ef625eeb2e2b04a2ac26119b9 |
| Guard CSV | 12d95d0d56d691f1c6f2d855bf5d00b0935a8ec9dd09cb7cbf78d827c63421cf |

## Focused validation and acceptance limits

Both mounted and sibling configurations pass six fresh tests before and after
installation. The sibling run uses a private overlay for the three new modules,
records its existing missing-pool-helper fallback, and preserves all 2434
inherited dirty sibling paths. Both shared tool smoke checks are fresh; three
unchanged shared regressions per copy are explicitly fingerprint-reused.

| Check | Evidence |
| --- | --- |
| Independent ordered guest model | 271 cases; retail, raw and normalized code |
| Instruction reachability | All 77 target words and original 19-word cross product |
| Geometry/ABI | Signed extremes, winding, degenerate points, null lists, full-word sparse guest indices, both supported stack phases |
| Private memory | Vertex/edge aliases, complete normalized state, raw memory and callee-saved roles |
| Original callers | All three JAL sites inventoried; three connected original windows, nine cases; entire 830-word caller literal checked |
| Native32 | 183 cases at O0/O2/O3; SDK widths, typed s32 callback, disjoint backing, trapping UBSan, RN/no FTZ/DAZ |
| Effective source negatives | Stub, null result, unsigned coordinate, wrong offset, swapped edges, wrong normal component, rejected zero, rejected NaN |
| Fault cuts | 100 executed access cuts with identical literal normalized state |
| Corruption controls | Raw/relocation/guard-prefix rejection; four whole-image corruptions rejected |

Sparse arithmetic and private input/output aliases are guest-only contracts.
Native qualification uses 32-bit pointers and `-fno-strict-aliasing` for the
recovered shared-memory view. Raw caller-clobbered FPR fault-state identity,
hardware FCSR/NaN payload behavior, the complete rendering caller's runtime,
and gameplay acceptance are not claimed.

Actual production Make emits one normal-profile compiler invocation and no C
warnings. Existing duplicate generated_12D630 recipe warnings remain. The
ordinary `make all` reaches the expected development-image checksum rejection;
the linked/binary artifacts and the explicit NON_MATCHING recount are verified.

Reproduce under prepared WSL from the consumer root:
`python3 -m unittest tools.tests.test_game_triangle_facing_1510e670_match -v`.
Canonical receipts live in `conker/build/game-triangle-facing-1510E670-match/`.
Tools first, then source/three guards/docs/consumer pin are committed locally.
No push, host changes or frozen Release work. Routine task: zero Claude calls.

## Oriented-strip diagnostic handoff retained

The [Note 2170](2170-game-oriented-strip-semantic-study-20261107.md) candidate
`func_1513FAB4` remains uninstalled, unmatched and uncredited. Its corrected
full-owner CFE/UOPT/UGEN capture uses actual O2/g3, completes producer/consumer/
driver and fired-probe gates, and preserves complete normal object text,
functions, relocations and pools. The target remains 337 words/frame128,
SHA99ccd0b08050604207ed8535f5b300d4a4decb6275c1e87f89d3db40db9ef672.
The capture records 13579 frontend records, 11814 optimized records and 1735
UGEN load events. The target is procedure ordinal53/block2932; its optimized
M definition reserves 84 bytes. This describes the candidate, not retail's
unknown source layout.

An isolated input instead emits 350 words/frame128 despite identical bindings;
it is not a representative diagnostic. The first full capture inherited the
text-measurer helper's no-unroll flag and was correctly rejected for two changed
neighbors. The corrected capture restores the actual owner profile; no compiler
binary is modified. Separate midpoint/viewer phases emit 358/128 and 349/128,
also rejected. These diagnostic artifacts retain their pre-triangle bank and
remain in the ignored FAB4 private folder; no new matching credit.

Next ordinary candidate: inspect `func_15146970` and its complete switch/table,
callers and owner profile. The FAB4 source/private-frame/caller gates remain
open. Keep the 80% objective active.
