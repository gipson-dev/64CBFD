# Game Grid/Channel Updater Match

Date: 2026-10-06
Baseline: `816ad86f` ([Note 1052](1052-game-payload-copy-wrapper-match-20261006.md)).

## Scope And Recovered Contract

Replace the false zero-return `func_151412BC` placeholder in
[`game_16DC80.c`](../../conker/src/game_16DC80.c). Complete slot: **96 words /
384 bytes**, VA `0x151412BC..0x1514143C`, ROM `0x16E76C..0x16E8EC`, frame
**0x18**, existing **O2/g3**. No compiler profile, address, slot or data change.

Traverse four live indexed buckets in each of two **0x1A0-byte rows** rooted at
`D_800DCE50`. Follow each node's next pointer at **+8**. Capture flags at **+0x58**:
bit **0x2000** clears the four halfwords in retail order **+0x162, +0x160,
+0x15E, +0x15C**; bit **0x10** additionally enables grid sampling.

For each byte-wrapped channel from zero through the **live signed**
`D_80082FA0` bound, read signed X at **+0x134 + channel*4**. Only an in-range X
permits the signed Y load at **+0x144 + channel*4**. Capture width for the
unsigned-halfword grid index **Y*width+X**, then store at **+0x15C+channel*2**.
Invalid coordinates store **0x7FFF**. Grid pointer, height, bound and bucket
indices remain live; no cached bound, clamp, cycle guard or coordinate fix.

The source uses a word-sized channel explicitly narrowed to a byte at the
backedge. A bound of **255** therefore wraps to zero and keeps looping if
stores do not change that bound. Guest tests exercise the cycle; they do not
pretend it completes or introduce a native out-of-bounds call.

`variables.h` still falsely describes `D_800A5168` as a scalar float and
`D_800BE9C4` as a scalar integer. Interpret their table/pointer storage through
**owner-local casts**; leave shared declarations and all original data intact.
The local prototype is now **`void func_151412BC(void)`**, not a fabricated
integer-return/no-argument-list placeholder. The sole direct reference across
all pristine ROM slots is `func_1501878C` at `0x15018820`; its first
post-delay instruction overwrites V0. This is direct-caller evidence, not a
proof that no indirect caller exists. The caller remains a placeholder in
the rebuilt ELF; searching that placeholder does not establish retail callers.

## Compiler And Normalization Evidence

The persisted [driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_grid_channel_updater_candidates.py)
screens declaration orders, byte/direct/typed payloads, return-type controls,
and byte-loop shapes against two profiles. It installs nothing. Earlier
ignored controls in Note 1052 remain useful history, not current source.

The selected byte-payload/early-channel/bottom-assignment form emits **96
words, frame0x18, 43 differences**. **53 words compile directly**. All remaining
words derive from these closed register cycles (raw -> retail):

```text
v0 -> a0 -> v1 -> v0
a2 -> a3 -> t2 -> t0 -> a2
```

Rotate the independent opening LO16 address loads at word indices **12..18**:
raw12 -> retail18, raw13..18 -> retail12..17. HI16 owners remain paired with
their corresponding moved LO16 references. Branch opcode, likely behavior,
target displacement, delay instruction, arithmetic constant and instruction
count do not change. No insertion, omission, trampoline, synthetic return,
register-lifetime split or payload-offset replacement is used.

Deriving those two permutations reproduces **every retail word**. The raw
void candidate leaves V0 at the end-row address **0x800DD190**; its bucket
index lives in V1. The closed cycle restores retail's bucket index in V0,
leaving **V0=4** without adding a return instruction. Guest return-state
qualification covers raw, derived-normalized and retail bodies separately;
native void C does not claim a defined scalar return.

The actual object padder parses, validates, applies, assembles and links all
**43 expected-word/relocation guards**. The resulting symbol is exactly
**384 bytes / 96 words**, not a padded prefix or truncated routine.

## Tests And Audit

[Nine focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_grid_channel_updater_match.py):

- **144 persisted compiler controls**: 36 declaration/return forms and 36
  payload/loop forms, each under O2/g3 and O2; empty compiler diagnostics.
  Several controls deliberately lack byte wrap or return a scalar and are
  not selected or claimed semantically equivalent.
- **1728 guest cases / three bodies**: complete external storage and ordered
  accesses, signed X/Y limits, four flag patterns, live bound/grid-field
  aliases, empty/nonempty lists and two SP phases. **95 reachable words**
  covered; the unreferenced word at VA **0x151413DC** is not artificially run.
  Saved GPR/FPR/SP/RA and normalized V0 are checked.
- **12 extended signed-bound cases / three bodies**: bounds including signed
  minimum, -1, 0, 127, 128 and 254. Three bound-255 guest runs verify repeated
  channel-zero stores and no successor load before the instruction budget;
  this is bounded evidence of byte cycling, not a terminating call.
- **864 native 32-bit actual-owner-body cases**: whole-node/grid/root storage,
  empty lists, signed bounds and live bound/grid aliases. The independent
  expected pass uses row/bucket ordinals and shadow storage, not guest opcode
  rewriting. Byte indexing preserves unchecked semantics; native fixtures
  stay inside their valid storage.
- **Ten compiled negatives** distinguish incorrect gates, clear offsets/order,
  payload base, sentinel, grid index, omitted clear, captured bound and eager
  Y access by real storage/access differences or strict unmapped access, not
  an unsupported emulator instruction.
- Owner-local interpretation compiles against the actual SDK header and gives
  exactly the same raw body. Production source, complete linked slot, sole
  direct caller, all guard fields and total guard count are bound explicitly.

Completed dependency rebuild and audit: only **`func_151412BC`** changes across
**6059 fixed slots**. `.init`, `.init_data`, `.debugger`, `.game_data` unchanged;
**720 owners / 189088 Game-data bytes** remain retail-exact. All **10695
existing guards** preserved in order, plus43: **10738 total**. Baseline/current
owner warnings **0 -> 0**, zero new warnings. Both header files are unchanged.
Target SHA-256:
`9eec5cd9601d3578971c4f3e21800b573eb988de381775b8b31118d01d683546`.

Converted counts/bytes unchanged: **5464/6042**, Game **4791/5321**; converted
bytes **85.57% total / 84.89% Game**. Exact **3331/5464 (60.96%)**, Game
**2658/4791 (55.48%)**, **2133 different**, zero drift. Init492/492 and
Debugger181/181 unchanged. README aggregate statistics only.

Documentation verification passes: **35 documents / 3389 relative links /
zero broken**. Tools, compileall and diff checks pass. **92 retained post-link
tests pass**, and the **complete corrected nine-test updater rerun passes in
239.123 seconds**, no skips: **101 unique current tests qualified**.

The initial combined101-test invocation finished in **1960.245 seconds** with
one failure: the new caller-evidence assertion searched the rebuilt caller
placeholder and incorrectly expected its retail JAL. Correct the fixture to
scan every **pristine ROM slot**, then rerun all nine updater tests; all pass.
All92 retained tests passed in the initial invocation. This is qualification
across completed runs, **not a claim that the first101-test run was green**.
`regression-summary.py/json` binds exactly that one historical fixture failure,
all92 retained successes and the complete corrected nine-test receipt.

Ignored receipts under `conker/build/game-grid-channel-updater[-test]/`:
`build.log`, `audit.py/json`, `after.json`, `progress.txt`, compiler controls,
objects, relocation fixture, owner diagnostics and `regression.log`.

## Cross-Project And Next Work

Read-only sibling `64CBFDOGL/recomp_out/.c` already contains retail-translated
`func_151412BC` at line974818; no source override found. No mechanical guest C
import/regeneration or host/runtime adoption claim. No sibling source/build,
save, frozen Release, runtime or push change. No full dispatch/hardware/gameplay
acceptance inferred from unit fixtures.

Next **`func_15141478`**: **59 words/frame0x30**, VA0x15141478..0x15141564,
ROM0x16E928..0x16EA14. Decrement timer+0x180 by live timestep; on strict-negative
expiry draw a random float for reset, a random word for the low-two-bit branch,
then a second random float for one of two target intervals. Finally interpolate
payload+0x48 toward runtime+0xC with live runtime+0x18, return1. Loads after
random callbacks and float operation order need qualification; no clamping.

Ignored `next-interpolation.py` completed **112 initial controls**, empty
diagnostics. Selected O2/g3 gives **55 words/frame0x20/45 differences**;
early-runtime gives **57/frame0x38/25 differences**, still wrong frame/length.
Float-array and typed-payload/runtime forms do not improve that frame/length;
early typed-runtime forms have27 differences, not a normalization solution.
Compound/product-first/current-first tails reduce early-runtime differences to
**19**, still **57 words/frame0x38**, not the required59/frame0x30. Do not patch
the frame or insert missing tail words without recovering their source shape.

`next-interpolation-behavior.py` passes **2160 preliminary finite guest cases /
two bodies**, full external storage and random-callback snapshots, V0=1 and
saved state; all **55 raw / 59 retail words** reached. Timer/step boundaries,
low-two-bit random branches, distinct random float samples, callback mutations,
timestep/timer alias and two SP phases. **Ordered accesses differ** in the tail.
The later inline forms recover the required **0x30 frame** but initially emit
57 words. Initializing **both payload and runtime pointers before the timer
update**, using inline random expressions, and retaining the compound final
update gives **59 words/frame0x30/nine differences** under existing O2/g3.
Candidate: `next-interpolation/both-early-o2g3.c/.o/.elf`; source takes one
`u8 *actor` argument and returns1. **50 words compile directly**.

`next-interpolation-normalization.py/json` derives all nine differences:
six private runtime-pointer save/reloads move **SP+0x20 -> SP+0x24** at offsets
**0x58,0x64,0x6C,0x70,0x94,0x98**; three commutative floating operand pairs
swap at **0x4C,0x84,0xAC**. Derived words equal all59 retail words; no count,
frame, branch, opcode, arithmetic constant, call relocation or delay change.
This is a derived-word result, **not an installed byte-exact recovery**.

Rerun the2160 finite cases with `--candidate both-early`: complete external
storage, callback snapshots, **ordered accesses**, V0=1 and saved state agree;
all **59/59 words** reached. Earlier55-word candidate's access mismatch remains
historical, not a failure of this new shape. Receipts: `selected-behavior.json`
or earlier `behavior.json`, `both-early-behavior.json`, and compiler family
receipts `measurements.json`, `tails-measurements.json`, `inline-measurements.json`,
`lifetimes-measurements.json` (56+24+16+16 unique controls).

Next: bank this updater, then promote the interpolation source/driver, bind
its nine expected words to the real object padder and private saved-pointer
lifetime, qualify actual native C and special FP/raw-bit boundaries, compile
negative controls, install only after those gates, and audit the one slot.
No native, special floating-point/FCSR, padder/full match or production
qualification yet; its false placeholder remains untouched.
Large adjacent `func_151408A4` and
the remaining owner routines are still unrecovered, not owner completion.
