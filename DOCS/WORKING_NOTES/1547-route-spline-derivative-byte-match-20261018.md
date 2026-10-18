# Route Spline Derivative Byte Match

Date: 2026-10-18. Consumer predecessor **ea20ab92**, tools predecessor
**b91fd0e**. Tools banked first as **bcfe55a**. Recover **func_150498A4**,
owner `generated_76C90`, VA **0x150498A4..0x1504999C**, ROM
**0x76D54..0x76E4C**: **62 words /248 bytes /frame0x20**. Both spline
functions now have semantic C and match all **111 retail function words**.
This does not complete the Game goal or the still-stubbed vector builder.

## Semantic Recovery

Replace the false zero-return stub with
`f32 func_150498A4(f32 *points, s32 index, f32 fraction, f32 *slope)`.
Retain the address-based name and a concise semantic comment. Update only
the owner comment that previously described the derivative as unfinished.
The complete live C caller `func_15088D58` already has the correct typed
declaration and two float-return calls; its source/prototypes stay unchanged.

Use the same rounded cubic, quadratic and linear coefficients as Note1546.
The value is `((cubic*t + quadratic)*t + linear)*t + p1`. Publish derivative
`((cubic*3.0f*t) + (quadratic+quadratic))*t + linear`, and return the captured
value. The source computes value before the output store. A direct-expression
return after that store can reload p1 through a real input/output alias and
is wrong; the effective `late-value` control demonstrates this in guest and
valid native C domains. No extra clamp, null check or invented failure return.

Preserve frame32, the incoming F20/F21 FR=0 pair at SP+8, cubic at SP+0x10,
and linear at SP+0x18. In entry-SP coordinates these are -24/-20, -16 and -8.
Big-endian FR=0 stores the odd register's high word first, then the even
register's low word. F20 holds the fraction after the initial save and is
restored after the output and last fraction use. No synthetic padding,
dummy stores, inline assembly, volatile workaround or profile change.

## Independent Lineage Proof

The normal O2/g3 owner emits all **62 words/frame32**, with **45 differences**
and zero relocations/pools/calls. Append45 expected-word guards. This is a
**guarded match**, not direct compilation. The49-word cubic checker is not
generalized or weakened to accept this function.

The derivative-specific decoder tracks each rounded add/multiply node,
constant, pointer expression, save/read/store/restore and FP register value.
Both bodies have the same **58 non-identity operation events** and **four
identity-routing slots**. Raw uses two FP copies/two NOPs; retail uses three
copies/one NOP. Track copies' real register effects, while allowing a closed
identity-slot mapping. This accounts explicitly for the extra retail linear
copy; it is not an inserted arithmetic operation or an omitted instruction.
Both complete instruction budgets remain62 words.

The full bijection requires identical rounded return and derivative DAGs,
all final GPRs, preserved FPRs and ordered private/public stores. Commutative
FP operands may be routed; **no FP reassociation**. Separate ordering gates
require save-pair before all point reads, all four reads before coefficient
stores, both coefficient stores before derivative publication, and pair
restore after publication. Those gates matter when the point/output pointers
alias private homes. Raw reads offsets0/8/4/12 versus retail0/4/8/12; there is
no intervening write. All original private locations and stores remain fixed.

Raw dead-register/fault traces, NaN payload selection and hardware FCSR or
exception timing are not claimed equal. The actual guarded/padded function
matches every retail word, including original operands, copies, NOP and
schedule. The aligned atomic FR=0 pair model is not hardware MMU/partial-bus
fault emulation. Native tests exclude forged callee-private-stack pointers.

## Focused Qualification

New tools: `experiments/game_route_spline_derivative.py` and
`tests/test_game_route_spline_derivative.py`. Ignored artifacts:
`conker/build/game-route-spline-derivative/`. Fourteen frozen input fingerprints
cover the owner/ELF/guards/ROM, assembly, Makefile/symbol/header closure,
prepared IDO components and unchanged caller owner. Historical views remain
strict, serial and non-nesting; this is not an exhaustive dependency closure.

All **seven pre-install tests pass in146.080s**. A focused additional ABI
mutation check passes in12.977s. All **seven final installed tests pass
in60.811s**:

```sh
python3 -m unittest tools.tests.test_game_route_spline_derivative -v
```

- **20,568 three-way raw/padded/retail guest cases**, all62 words, complete
  private/public bytes and normalized/retail full state. Cover signed zeros,
  finite cancellation, subnormals, infinities/qNaNs, sixteen fraction patterns,
  wrapping guest index words, both stack phases, nine output aliases and
  point windows in argument/coefficient/saved-pair homes. Five incoming64-bit
  pair patterns include arbitrary, zero, subnormal and nonfinite words.
- **72,352 native32 cases per O2/O0 UBSan profile**, including all65,536
  fraction steps. A linear0/1/2/3 window independently expects value1+t and
  derivative1. Separate units execute the real typed C with four valid
  input/output float aliases and complete input/output canaries. Native
  indices stay within actual objects; arbitrary guest wrapping/private aliases
  are not portable C claims. Raw/native NaNs compare class, not payload.
- **Ten effective guest/native controls** reject wrong window, half, basis,
  quadratic, value fraction, slope factor, output stride, missing store,
  late value calculation and actual FP reassociation. All native controls exit
  wrong-result23, not a crash or private-offset difference.
- **Nine independent original/raw/padded links and360 three-way rebased
  cases** prove the actual slot at three code placements. There are no symbol
  bindings to invent. The old cubic raw body and all49 padded retail words
  remain exact, with its34 guard rows preserved in the old manifest prefix.
- **720 fault prefixes across80 fixtures** compare raw finite memory prefixes
  and full normalized/retail fault states/traces. Raw read ordering and dead
  fault-register equality remain explicitly unclaimed.
- **96 three-way complete118-word caller executions**,555 connected helper
  words, exact public results/calls and preserved saved ABI. Only u16 atan is
  a bounded provider. Both spline bodies now exist in production; the vector
  overlay remains retail for qualification, not a converted production helper
  or whole-gameplay acceptance claim.
- Mutation checks reject all62 raw-word changes, an unexpected binding,
  all45 changed guard expectations, reassociation, four alias-order violations,
  a lost identity slot and all28 live/snapshot input changes. Three actual
  ABI word mutants reject F20 clobbering, wrong pair restoration and early
  restoration before a saved-word output alias. No shared test runner,
  old normalizer, fixture, guard or profile is weakened.

The first run exposed a **fixture assumption**, not a production defect:
the shared runner always asserts incoming F20 preservation, but forged guest
outputs can deliberately overwrite a saved-pair word. Retail triggers the
same assertion. The new oracle locally tracks that explicit publication in
its expected restore state and synchronizes custom incoming pair patterns.
Ordinary calls retain the strict incoming-pair check; the three real ABI
mutants above prove it still fires. Independent full-memory/return/slope and
restore checks remain active. No production edit preceded the passing tests.

Correct Note1546 and its roadmap entry from **192 to96 cubic caller cases**.
The authoritative existing `game-route-cubic-spline/caller.json` receipt is96;
no code or prior test result is changed or newly claimed by that correction.
Prior unchanged cubic-suite receipts are reused, not described as fresh runs.
Fresh raw-neighbor, full padded-owner and connected-caller checks cover this
installation's interaction with the already-matched cubic function.

Shared padder/PC16 tests pass **eleven per tools copy**, both smoke checks and
root tools-check pass. Four copies pass ASCII/AST parsing; both task pairs are
byte-identical. Older mirror HEAD ddbdd16 remains fixed: preserve all
**1,220 previous dirty hashes**, add only two absent task paths for1,222.
No mirror commit/reset, push, new Claude call, host or frozen Release action.

## Installation Audit

Predict before production edits; append only45 generated CRLF rows after
checking the complete old prefix and successor hash. Keep the existing build
profile and suppress guard timestamps for focused builds/reporting:

```sh
make -C conker -o Makefile -o retail_word_patches.us.csv -j4 \
    build/src/game/generated_76C90.c.o build/conker.us.elf progress.csv
make -C conker -o Makefile -o retail_word_patches.us.csv \
    -o build/conker.us.elf -o progress.csv match-progress NON_MATCHING=1
```

Actual whole ELF equals the **first prediction byte-for-byte**:
**206 changed bytes =205 derivative-code bytes +one target-size encoding byte
in .symtab**. Zero metadata exclusions. Canonical definitions change only
target extent12->248. Preserve all **6,057 function addresses**, every other
body and section byte, the raw/padded cubic neighbor and all earlier guard
bytes. Actual padded owner and bindings agree with qualification. Protected
Game data remains **189,088 bytes /720 owners /zero differences**.

| Artifact | SHA-256 |
| --- | --- |
| Raw derivative | 95dc59ef79203db705b8f261e6497fd8ab8402edb6bf62b977044e339b3faea0 |
| Whole ELF | fc9f2b74bd97121aa678270092047b76914852ea483a10c1bc35a32b504c021b |
| Owner source | 8e9c9885e7772fbd356120a036307a2ba8202d04fc72de82a3027dba7f750dde |
| Guards | 65de253d70fd8071c62dd8c1f87dbe89107c2713dbb3d30ae3a728d5b9a6447f |
| Unchanged Makefile | 840897f11d9fea8109c4e67c57e927efa6e1686de2b399fec2c9025828b92d49 |

Fresh official totals: **Game2,984/4,828 (61.81%)**, **total3,657/5,501
(66.48%)**, Init492/492, Debugger181/181, **1,844 different /zero drift**.
The false C stub was already counted converted. Root README changes only
its Total/Game aggregate matching rows; detailed function updates stay here.

## Next Work

Resume **func_15088F30**,83 words/frame16, owner `generated_B3020`. Its
semantic model still has the wrong S2/S1/S0 saves versus retail's S1/S0 pair;
do not normalize away that private-memory difference. Fit S0=&D_800D2350,
S1=4 and T2/T3/T4 output cursors while preserving first-type4 selection,
fresh table/speed reads, ordered stores and the complete original frame.
Notes1545/1546 retain the bounded source and owned-compiler allocation evidence.
Do not repeat the complete136-form screen by default.

The old vector fixture intentionally pins an older ELF/guard baseline. Use
a deliberately verified read-only predecessor view or establish a fresh strict
checkpoint before new fitting; do not replace hashes merely to bypass gates.
Its source/caller owner remains unchanged. Both spline helpers are now real C,
but vector recovery, parent15087350 and the wider Game queues remain open.

Scoped Graphify refresh: **42,545 nodes /82,623 links /4,060 communities**.
Preserve19,398 nodes from2,972 excluded-but-existing files. All42,533 other
old IDs remain; three line-disambiguated UPDATE_LOG heading IDs relocate with
their labels preserved. The new note contributes seven nodes. Cubic and
derivative definitions resolve at L6/L23. Tools retain the configured submodule
scan exclusion; no fresh graph AST-coverage claim for the new tool files.
Original graph and preservation audit are ignored task artifacts. No full-scan
purge, graph-output commit or history rewrite.
