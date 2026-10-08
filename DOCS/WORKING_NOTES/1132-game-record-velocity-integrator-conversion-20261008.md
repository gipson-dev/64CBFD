# Game Record Vertical Velocity Integrator Conversion

Date: 2026-10-08

## Result

Continue [Note 1131](1131-game-record-state-update-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
`func_151D8718` in [generated_204660.c](../../conker/src/game/generated_204660.c)
to complete semantic C. All **19 words /76 bytes**, **frame0**, match retail
after three strictly checked FP allocation/operand-order guards; **16 words
emit directly** under existing IDO5.3 O2/g3. VA0x151D8718..0x151D8764,
ROM0x205BC8..0x205C14. No filler, new globals, pools, data, compiler profiles
or Makefile changes. [204660.s](../../conker/asm/204660.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_204660/func_151D8718.s)
remain untouched. Other retained routines in this owner are not converted.

The linked audit proves every instruction remains unchanged from the previous
checkpoint, not merely equal model outputs. Only this76-byte asm-to-C progress
row and an exact three-row guard append change.

## Recovered Contract

`void func_151D8718(f32 *position, f32 *velocity, f32 delta)`:

- The mixed pointer/pointer/float o32 ABI receives delta's bits in A2; word0
  copies them into F12. It is not the leading-floating-argument ABI. A K&R
  float-parameter experiment promotes the parameter and is not this contract.
- Load D_800AB2EC and capture the original *velocity. Store
  oldVelocity + D_800AB2EC * delta through velocity.
- Load D_800AB2F0 and position[1] after the velocity store. Advance position[1]
  by oldVelocity * delta + D_800AB2F0 * (delta * delta), preserving the
  parentheses and separate single-precision operations.
- Neither the final position update nor its old-velocity term uses the newly
  stored velocity. However, the live height/half-acceleration loads observe
  aliasing writes. A cached height or cached half-acceleration is incorrect.

Actual constants in [24FD40.rodata.s](../../conker/asm/data/24FD40.rodata.s)
are **0x3E6F9DB3** and **0x3DEF9DB3**, approximately0.2340000123 and0.1170000061.
Keep the globals, rather than inventing constants or replacing their loads.
Finite, signed-zero, subnormal, overflow, infinity and NaN model cases are
separate from hardware FCSR, signaling-NaN trap and payload qualification.

Valid native inputs use aligned float objects, a position array containing
element1, and initialized scalar globals. Native tests include velocity
aliasing the position's height/x or either scalar global. Additional guest
layouts make height alias a global through its numeric address; this is
emitted-instruction evidence, not portable pointer arithmetic across objects.

## Source Fit And Guards

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_velocity_candidates.py)
measures20 complete source forms: eleven ordinary forms, eight effective
semantic negatives and one K&R ABI-only probe. Assignment/declaration shape,
register annotation, indexing, temporary square, multiply order and the
natural expression retain three raw differences. Local step/value temporaries
produce12/11 differences; square-left gives five. Expanded position addition
changes grouping and is an effective negative, not a matching alternative.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 19 | 0 | 3 |
| O2 | 18 | 0 | 7 |
| O1/g3 | 25 | 8 | 25 |
| O1 | 25 | 8 | 25 |

Isolated and complete copied owners emit identical target words and four
symbolic HI16/LO16 relocations. IDO assigns captured velocity to F0, retail
uses F2. The complete allocation closure is function+0xC load, +0x18 add and
+0x34 multiply. The add also preserves retail's original operand order.
All other words, loads/stores, arithmetic grouping, return and delay slot
already match. The three expected/replacement pairs are respectively:

```text
0x0C: C4A00000 -> C4A20000
0x18: 46003200 -> 46061200
0x34: 460C0102 -> 460C1102
```

Guards are literal expected-word checks with no relocation changes. Their
purpose is exact instruction identity, not a claim that commutation preserves
all possible N64 NaN payloads or exception behavior. Four stale ABI/allocation
mutations are rejected. Raw finite model cases preserve public memory/events;
normalized executions also have complete GP/FP/trace/memory equality to retail.

## Qualification

[Eight tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_velocity_match.py)
reuse existing Triangle/CopyOracle, step-rounded FP helpers, native32, copied
owner/parser, guard history and real padder. Shared domain oracles are unchanged.

- **34,692 guest cases**:13 representative finite bit patterns cubed,
  256 deterministically seeded arbitrary-bit inputs, five special patterns
  in each field, seven alias layouts and two SP phases. All19 words reached;
  complete normalized GP/FP/memory/trace matches retail and an independent
  reference's load/store order. **2,448 raw finite cases** match public state.
- **23 required fault prefixes** remove bytes from required loads under all
  layouts, including a missing half-acceleration after velocity has already
  been stored. Compare complete partial guest state, not portable C fault
  semantics or hardware CP0 exception metadata.
- **12,240 actual native32 C executions** use the selected body through a
  volatile typed function pointer, five valid alias layouts, independently
  step-rounded golden vectors, every buffer word/canary and both globals.
  NaN classification, not host-specific payloads, is asserted for finite-input
  cases that generate NaNs. GCC/SSE behavior does not emulate target FCSR.
- **20 compiled forms /10,494 ordinary executions /eight effective negatives**
  expose updated velocity, missing square, wrong position element, reassociated
  multiplication/addition, position-first and cached live loads. K&R is only
  a measured ABI probe. Ordinary controls deliberately exclude exceptional
  input bit patterns from semantic equivalence claims.
- Preserve **22 complete owner neighbors**, their relative relocations and
  normalized data/rodata pools. The four existing pointer/integer warnings
  at func_151D7404/func_151D8764 call sites remain identical; isolated target
  compilation has zero diagnostics. No new warning is suppressed.
- Actual padder emits exactly76bytes without filler and retains all four
  relocations. **Six independent links /840 executions** exercise HI16
  signed-low carries, high/wrapped addresses and an independent entry address.
  Expected relocated words are independently calculated before execution.
- **768 complete actual `func_151D792C` caller connections** execute all67
  retail caller words, its real epilogue and the complete helper. Four-record
  ring wrap, no-work paths, enable gate, delta load in A2, velocity+0xC
  delay-slot setup and final coordinate copying match independent public
  expectations. Normalized/retail complete raw states agree. No later callee
  is replaced by a gameplay claim; the second caller remains unqualified.
- Guard history retains all11,152 prior rows and their original prefix hashes
  and suffix checks, accepting only this exact three-row append. The preceding
  state-update fixture now checks its four-row slice while validating the
  complete manifest, so subsequent owners can append without weakening it.

Pre-install seven tests pass in76.963s; the added actual caller test passes
separately in2.179s. Final installed regression and banking receipts follow
below. Ten shared word-patch/PC16 tests pass in0.044s. Mounted and standalone
tools project checks, candidate CLI help and syntax checks pass. Both copies
receive identical task fixtures; unrelated older standalone work is preserved.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` exits0. The CSV dependency
triggers the expected broad rebuild and existing warnings, including duplicate
generated_12D630 recipes. This is not a warning-free full build.

Fresh audit compares [Note 1131](1131-game-record-state-update-conversion-20261008.md)'s
`game-record-state-update-test/after.json`:

- All **6,058 bodies, addresses and extents** unchanged:6,042 retail rows plus
  16 overflow symbols. Protected Init/init-data/debugger/game-data unchanged.
- All720 game-data owners /189,088 bytes exact; actual acceleration constants
  are unchanged. The target's complete19 linked words equal retail.
- Prior **11,152 guards** unchanged, plus exactly three:11,155 total.
- Exactly one progress row changes:func_151D8718,76bytes, asm -> c.
- Total converted **5,476 /6,042 (90.63%)**, bytes1,933,740 /2,256,728 (85.69%).
  Game **4,803 /5,321 (90.26%)**, bytes1,762,304 /2,072,880 (85.02%).
- Fresh matcher:total **3,387 /5,476 (61.85%)**, Game **2,714 /4,803 (56.51%)**;
  2,089 different, zero address drift. Init492/492 and debugger181/181 exact.

Ignored receipts live in `conker/build/game-record-velocity-test/`:slot,
guest, faults, native, controls, owner-padder, connected, installed,
audit-baseline, audit-installed and the new `after.json` baseline.
Root README receives aggregate rows only; narratives stay here and in the
concise status/index/roadmap updates.

## Workflow And Next Target

Baseline source `80014c44ba0502c2e7d0cd2989f6966f5157bd5b`,
mounted tools `8e1a208bbeb5fa7b790571809c8dd7a872fe47f8`; both clean on entry.
Pre-edit SHA-256 fingerprints:

```text
source: 78c73ef23d86ace2a0ca06f18734b5324a6a5698a1eb4f33eefaf7c584975eff
reference ASM: 14c690097e848287eb8f9e5f3f1031cfa7c3fd65ebdb31075cdafc30a732fa48
Makefile: d5e4c8459b9bf1ac7485b913f559fe9e0242ec284d76cddf0650c210e2a73466
guard CSV: 2c03beead9be3da5c98d0708dffd244ad2f9d908ab1dc9e4f7983ea7f301360c
prior linked snapshot: 352f7508f05290fcd7cf218dcf1241c60ac5b616a2ad281d808d4d3f02e16d67
```

Zero Claude calls; routine assembly/ABI questions resolved locally. Prior
49-test state/neighbor receipt is historical, not relabeled as a fresh suite.

Graph query forfunc_151D8718 exits0 without a node. Refresh exits1:16,741 new
versus38,528 existing nodes; it refuses overwrite and preserves19,398 nodes
from2,972 excluded-but-existing files. Do not force overwrite or alter ignore
rules. Graph completion is separate from matching evidence.

Next retained target **`func_151D77C8`**,26words/104bytes/frame0 at
VA0x151D77C8..0x151D7830, ROM0x204C78..0x204CE0. It captures an attached record's
nested pointer, updates flags through live owner-pointer reloads, clears both
nested/owner links, and leaves the owner+0x28 address in V0. Recover its return
contract and qualify null/alias/reload order before fitting or installation.
No new candidate is qualified yet. The wider Game goal remains active;
second caller, hardware/FCSR and gameplay are open. No host/runtime/save/editor
or bridge/account changes; OGL Release stays frozen.

## Installed Regression And Banking

Fresh combined installed execution passes all eight integrator tests and four
affected state-update/constructor owner and connection tests in186.832s. That
invocation exits1 only because an extra selector names nonexistent
`GameNodeEffectCallbackTests`; it does not represent a target or fixture failure.
Corrected `GameNodeEffectCallbackMatchTests.test_07_installed_or_original_stub_and_guard_history`
then passes independently in6.860s, exit0. Thus all13 intended actual tests
pass across those invocations, with no skipped tests; do not describe the
first invocation as a clean thirteen-test suite. No shared-domain engine edit.

Documentation check:118 files,3,989 relative links, zero broken;25 relevant
mounted/standalone tools files byte-identical. Both scoped diff checks pass.
Mounted tools commit **f36e9aff91515dd4398196b265cc6e84db4cc27c** banks the
candidate/test, exact guard-history extension and preceding fixture slice
adjustment. Parent source/docs checkpoint records that exact tools pin, per
"Keep commited"; no push. The older independently dirty standalone tools
checkout receives identical task files without reset, stash, unrelated edits
or a duplicate divergent commit. Full Graphify refresh remains incomplete.
