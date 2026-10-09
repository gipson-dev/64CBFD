# Game Payload Callback Update Match

Date: 2026-10-09

## Result And Baseline Correction

Continue [Note 1153](1153-game-actor-timer-callbacks-match-20261009.md)
under the [focused workflow](../AGENT_WORKFLOW.md), one Codex writer and
zero Claude calls. Convert **func_15147EB8** in
[generated_175250.c](../../conker/src/game/generated_175250.c):
VA **0x15147EB8..0x1514803C**, ROM **0x175368..0x1754EC**,
**97 words / 388 bytes**. Complete C is linked byte-exact with **25
expected-word guards**. Raw C emits all 97 words, frame0x20 and **25
differences**; normalized retail frame is **0x30**. This is guard-assisted
matching, not a direct compiler match. No fake filler or truncated body.

Correct the previous handoff: the live starting source used **GLOBAL_ASM**,
not a false-zero placeholder. Its assembly body already matched retail;
this checkpoint moves it into C without changing executable bytes. Start
from clean parent **e3da8ab9** and mounted tools **b3086e2**. The saved and
rebuilt complete ELF share SHA-256
`9882610856cfd36a0022c543d536b8b6817c335a3b74a95ce1c24abaea0e143e`.
All **6,058 function slots**, code, data, headers, symbols and metadata are
**byte-identical**, not masked. No new symbol-size or ordering exception.
Original assembly, other five GLOBAL_ASM bodies, profiles, Makefile, layout,
headers and shared tools stay unchanged.

Preserve **11,481 old guard rows and their exact CSV bytes**; append only
25 target rows, total **11,506**. The conversion CSV changes exactly one
row, this function's **asm -> c**. Converted functions/bytes gain **1 / 388**.
Fresh totals: **5,485 / 6,042 converted (90.78%, 85.91% bytes)** and
**3,402 / 5,485 exact (62.02%)**; Game **4,812 / 5,321 converted
(90.43%, 85.26% bytes)** and **2,729 / 4,812 exact (56.71%)**.
Init 492 / 492 and Debugger 181 / 181 stay exact. Zero address drift and
**2,083 still different**. Root README receives aggregate rows only.

## Complete Recovered Contract

Inspect the entire [retail routine](../../conker/asm/175250.s).
Return **s32 with explicit signed-byte narrowing** of boolean success;
this is compatible with the banked timer updater's s32 callback interface.
Do not substitute the last helper's V0 residue for the success result.

- Capture the payload pointer from actor **+0x98 once**. Even if a callback
  replaces actor+0x98, remaining selectors and fade fields use that captured
  payload. Public fields within it remain live across callbacks.
- Read unsigned payload selector **+0x20**. If nonzero, call
  **D_8008A3E0[selector]** with actor. A full-word zero return sets failure;
  high-word nonzero results succeed. No selector clamp or null check.
- Read live unsigned selector **+0x21**, even after the first failure.
  If nonzero and not failed, call **D_8008A3F8[selector]** with actor; zero
  sets failure. Failure suppresses this call, not the selector read.
- Read live payload flags **+0x18**. With bit0x40 and no failure, load
  signed actor timer **+0x1C**. If below signed payload limit **+0x1C**,
  multiply it by signed payload scale **+0x1E**, using the low 32-bit product.
  Compare that signed product to unsigned alpha **+0x1B**; if smaller,
  store its low byte. Preserve negative-product wrapping; no invented clamp.
- Save **success = !failed**. On failure, read live unsigned selector
  **+0x22** and call **D_8008A42C[selector]** with actor only if nonzero.
  Ignore that callback's result; success must survive its clobbers.
- Load live actor records pointer **+0x94**, including inactive cases.
  If signed actor active byte **+0x2C > 0**, read signed cursor **+0x2D**,
  select a **20-byte** record and sequentially publish its first three
  words at actor **+0x54 / +0x58 / +0x5C**. Otherwise store three positive
  floating zeros. Preserve arbitrary position bits, not float conversions.
- Return the saved signed-byte-narrowed success, **0 or 1**.

The protected actual **D_8008A200[1] at 0x8008A204** points to this routine.
Inner table labels/boundaries do not authorize invented selector bounds.
In particular D_8008A42C's neighboring labels are not evidence of a safe
nonzero-entry range. Synthetic full-byte fixtures provide consistent callable
targets, including addresses shared by adjacent tables; actual inner callback
bodies, null/out-of-range hardware behavior and upstream dispatch remain open.

## Source Fitting And Closed Guard Proof

The [candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_payload_callback_update_candidates.py)
and [qualification suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_payload_callback_update_match.py)
reuse existing IDO/GNU object and pool parsers, assembly processor/padder,
signed-byte-capable instruction oracle, native32 harness and linked audit.
Screen complete bodies rather than prefixes. Scoped product lifetime gives
the correct complete 97-word branch/call/register shape. Retain O2g3; no
owner profile override. Four profiles are measured in slot.json.

Normalize **25 expected non-relocated words**, with no insertions/omissions:

- **16 frame/home words**: grow frame **0x20 -> 0x30**, retain RA offset
  +0x14 and matching epilogue, and move captured payload **+0x1C -> +0x2C**,
  incoming actor home **+0x20 -> +0x30**, and first/second failure byte
  **+0x1B -> +0x2B**. Their absolute addresses relative to caller SP stay
  unchanged; RA moves into the new owned frame. Four outgoing homes are
  independently clobbered, so none may be used as persistent storage.
- **Two commutative operands**, word49 MULTU and word77 pointer ADDU.
  Both operand values and destinations remain unchanged.
- **Seven closed boolean-return words**, indices **55 / 56 / 64 / 68 /
  90 / 91 / 92**. Compute success in A1 before the failure branch, preserve
  it as a word at owned SP+0x18 around the optional third call, and retain
  the retail signed-byte return sequence. Convert the old branch-likely/
  delay-load path coherently, retaining the single live public active-byte
  read after callbacks. Raw uses the failure byte and computes success late.

The other **72 words** are unchanged. All **three HI/LO pairs** remain
symbolic at their original offsets, and no guard touches a relocation.
Reject every stale expected word; an unaffected-word control proves the
normalizer does not secretly replace other instructions. Branches and result
lifetime are qualified as complete streams, not presumed from matching words.
No private-frame actor/payload aliases or hardware traps are claimed.

## Qualification Receipts

- **10,216 cases / 30,648 raw, normalized and retail executions**: every
  byte in all three selectors and flags, signed timer/limit/scale boundaries,
  signed active/cursor bytes, full-word callback results, live payload/table/
  position changes, failure suppression and outgoing-home clobbers. Raw and
  normalized public calls, memory and access traces agree; normalized and
  retail full register/FP/event/memory states agree at SP phases 0 / 8.
  All **96 reachable words** execute. Word **85**, a duplicate positive-zero
  FPU setup, is structurally unreachable but emits naturally and matches.
- **151 missing-public-byte pairs** retain exact normalized/retail fault
  prefixes. Additional lazy-field checks cover inactive record contents,
  cursor, disabled fade/timer fields. These are emitted-order facts, not
  portable C fault guarantees.
- **100 complete compiled forms / seven samples each** include **93
  positive forms** and **seven effective negatives**: signed selector,
  unsigned timer/active/cursor, ignored first failure, reloaded payload and
  returned third result. Every negative completes and changes observable
  behavior; no crash is used as proof. Early fixture defects were corrected:
  map the unsigned-cursor negative's buffer and use distinct record words,
  so -1 and 255 cannot accidentally produce equal periodic data.
- Preserve all **10 copied-owner neighbors**, sizes, bytes, relative
  relocations and pools, with **zero diagnostics** before/after. Run actual
  GLOBAL_ASM post-processing for the remaining assembly routines. Actual
  guarded padder emits **388 bytes without .space**. **Four independent GNU
  links / 288 cases** exercise moved table symbols, HI/LO carry and entries.
- **328,448 actual native32 C cases** cover every 16-bit timer pattern over
  five signed scales, all three selector bytes, full-word results, captured
  payload/live changes and complete **256-byte actor / 128-byte payload**
  canaries. Use 32-bit pointers; callback implementations remain fixtures.
- **72 connected cases / 216 executions** run the complete banked **100-word
  timer updater** into this complete **97-word callback**, through its
  actual protected table slot, with failure/cleanup and clobbers. This is
  stronger than replacing the callback with a result stub, but inner callback
  and cleanup bodies remain bounded hooks, not gameplay acceptance.
- **56 public-alias cases / 168 executions** cover captured payload aliases
  in actor storage and sequential overlapping position publication. Qualify
  emitted streams, not portable partial struct assignment or private frames.

Pre-install eight-test gate passes in **143.273s**; the additional public-
alias gate and callback-compatible declaration/guard checks pass separately.
Manifest-triggered normal rebuild succeeds in **247.857s**, **489 cfe
warnings** across rebuilt owners; no fresh prior broad warning-count claim.
After the callback declaration clarification, a normal incremental rebuild
succeeds in **26.572s**, zero cfe warnings. The existing duplicate
generated_12D630 recipe warning remains. Fresh 25 shared tooling tests pass
in **0.317s**. Both tools checks pass. Historical baseline-sensitive target
suites are retained, not falsely reported as fresh reruns.

Final post-install **nine tests pass in 162.883s**, no skips, including the
callback-compatible s32 declaration and unaffected-word guard control.
The fresh matcher verifies the aggregate counts above against this rebuilt
ELF; the conversion totals exclude the repeated CSV header rows.

Documentation validation passes across **140 documents / 4,211 relative
links / zero broken**. All **27 mounted/mirrored tooling files** parse and
have identical bytes. The older standalone tree is not reset or committed.

## Banking And Open Boundaries

Ignored `conker/build/game-payload-callback-update-test/` contains baseline.json,
before.elf, before guards/progress, slot/guest/faults/forms/owner/linked/native/
connected/aliases/after receipts, build.log/build.json and abi-build.log/
abi-build.json. Preserve the original before.elf. Candidate-only screens live
in game-payload-callback-update/. Commit no ROM, ELF/native binary, generated
probe, progress CSV or saves.

Per "Keep commited", bank the mounted tools first and pin that exact commit
with parent source/guards/docs second. Mirror only the two absent new tools
files, preserving standalone HEAD ddbdd16, both independent dirty-file hashes,
pre-existing untracked paths and history. No duplicate standalone commit,
push, pause, reset, dependency/account change or OGL/Release/runtime/editor work.
Wider Game completion is not claimed. Zero Claude calls suffice: complete
assembly, complete fitting and independent tests settle this source/ABI case.

Tools checkpoint **a2e5ea703212b50c43a6c5050f26409c7aa5e49a** is committed
first; parent source/guards/docs/gitlink pins that exact revision. Both new
tool files parse and mirror byte-for-byte. The two independently dirty older
standalone files and its HEAD remain unchanged.

Manual Graphify update refuses **16,973 nodes** over retained **38,760**,
preserving **19,398 nodes from 2,972 excluded files still on disk**. Existing
skill-version/zero-node warnings remain. No force or dependency/account
change; the parent hook is checked separately. Reduced-corpus repair is open.

## Next Work

Recover **func_15148AF4**, first-stage table **D_8008A3E0[2]**, still
GLOBAL_ASM in this owner: VA **0x15148AF4..0x15148BA4**, ROM
**0x175FA4..0x176054**, **44 words / 176 bytes**, frameless. Its complete
retail body iterates a backwards wrapped range of 20-byte records, applies
live time-scaled gravity and three velocity/position updates, and returns 1.
Preserve signed starting/end cursors, unsigned count fallback, actual loop
termination and ordered floating operations/global reloads. Qualify the full
callback and connect it to this updater. Larger first-stage slot-1 callback
func_151488C4 and trail constructor func_151DA6F8's 61 differences stay open.
