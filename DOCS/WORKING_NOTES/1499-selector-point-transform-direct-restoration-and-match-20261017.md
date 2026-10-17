# Selector Point Transform Direct Restoration And Match

Date: 2026-10-17

Continue consumer **d1dd6e90**, tools **d698926**, after
[Note1498](1498-fixed-state-sine-update-direct-restoration-and-match-20261017.md).
Restore **func_150F22D0**, owner **generated_11F780**, VA
**150F22D0..150F237C**, ROM **11F780..11F82C**: **43 words / frame0x18**.
The full semantic switch replaces its12-byte zero-return placeholder.
All43 instructions match directly after binding the compiler's jump-table
relocations to the existing retail table. **No new word guards or profile
changes.** Tools **86254e6** banks qualification and exact fixture adapters
before the consumer source/binding/docs/pin checkpoint.

## Recovered Contract

The third parameter is a byte selector. Values3..8 select record indices
**0x29,0x2D,0x31,0x35,0x39,0x3D** respectively; all other byte values return0
without reading actor/output or calling a provider. For a supported selector,
load the pointer at **actor+0x1D4**, add **index*0x40**, and call
**func_15143134(D_800A1920, output, record)**, then return1 independently of
caller-saved register values left by that void helper.

The existing **struct17** is three floats,12 bytes. Use its typed output
parameter and a correctly declared float-point/float-output/byte-matrix
helper interface. D_800A1920 contains the existing float point **(0,-45,0)**,
not a newly synthesized constant. The helper accepts the game's float/fixed
matrix formats. No more specific actor/bone name is inferred from the indices.

Preserve retail's frame0x18, RA at SP+0x14, actor at SP+0x1C and original
full-word selector home at SP+0x20. The selector is masked to its low byte
after saving that word. The output pointer remains in A3 until the call.

## Preserved Jump Table

Raw target SHA-256:
`b7973680cb92b0e72b3306628475d4d27ac3b933da49d59d6a26952e9231c379`.
Five code relocations cover two table HI16/LO16 sites, two point-template
sites and one helper call. The compiler emits a32-byte pool: six R_MIPS_32
targets at target offsets **0x40,0x48,0x50,0x58,0x60,0x68**, plus eight
zero padding bytes. Validate exact relocation ownership and padding.

The original data owner **asm/data/2463E0.rodata.s** already provides the
36-byte **jtbl_800A192C**, at VA800A192C /ROM2463EC, with those six retail
labels and three trailing zero words. Its preceding12-byte template is at
VA800A1920 /ROM2463E0. Keep that complete48-byte owner unchanged; do not
duplicate the compact compiler pool into runtime data or replace its table.

Add only the generated_11F780 owner-specific **RETAIL_RODATA_SYMBOL** binding
to the Makefile's existing mechanism, plus its Makefile dependency. The
padder preserves all six exported retail jump labels. Raw isolated code
uses the same explicit relocation binding; no instruction word is replaced.
All eight other raw/padded functions and all unrelated owner pools agree.

## Caller Boundary

The actual20-word **func_150F2390** caller uses a private12-byte point at
SP+0x1C. If actor0x1D4 is nonzero it calls this routine, ignores its return,
and submits that point to **func_151C329C** with arguments255,0.

Consequently an unsupported selector leaves the point's prior stack bytes
untouched and the caller still submits them. Preserve that measured emitted
contract: do not initialize the output or add a caller return-value gate.
This is guest private-payload fidelity, not acceptance of portable C
uninitialized-value behavior, real rendering or gameplay.

## Qualification

All **ten tests pass before installation in19.846s** and **after installation
in41.365s**:

- **2,048 three-way guest/reference cases** cover all256 byte values, four
  upper-bit families and two stack phases. Verify original full-word selector
  homes, return values, calls, full private state/FPU condition and access
  order. Invalid selectors use null actor/output and stay lazy.
- **48 guest aliases** overlap output with the actor's record pointer,
  template, jump table or matrix storage. These are extended guest ABI cases,
  not native object/aliasing claims.
- **108 actual-helper cases** compose the98-word point wrapper,46-word SDK
  conversion slot and40-word matrix transform, across all six selectors,
  flags0/1/255, three finite matrices and two phases. Reuse the existing
  independent SDK reference; the fixed nonzero template does not claim the
  wrapper's null/zero-point paths. Hardware/FCSR acceptance is not claimed.
- **824 three-way real-access fault prefixes**, including actual helper
  chains, without observer-created reads. This qualifies emitted guest
  ordering, not portable C faults or hardware exceptions.
- **Nine independent original/raw/padded links**,120 three-way executions,
  all five sites and independently moved table/template low-half carries.
  Changing a live table target to the next instruction positively selects
  a different record, proving the table is actually used.
- Native32 **O2/O0 + UBSan**, separately typed caller, all256 selectors per
  profile, additional invalid-selector null-output probes and four effective
  record/stride controls. Use complete nonaliased objects and a real float
  array through the opaque output-pointer round trip. The native provider
  is a scripted three-pointer ABI probe, not a replacement math engine.
- Three effective **IDO negatives** break byte truncation, the last record
  index and output preservation. An initialization negative changes the real
  nested private output for an unsupported selector.
- **48 executions of the complete20-word caller image**, with present/absent
  record banks, upper selector bits and two phases. Eight cases preserve and
  submit the prior private stack point exactly; draw remains a scripted boundary.
- **43 word /five binding /nine pool /488 live-and-frozen /18 checkpoint /
  16 metadata** corruption controls. All **244 protected entries /225 paths**
  remain fail-closed.

Two initial checks rejected negative frame displacements as alignment phases.
Keep the reused oracle's0/8 alignment check and explicitly position entry SP
at the real nested frame; preserve its saved-SP check. Only the local fixture
changes. The corrected complete suites above pass without altering shared
oracles or any production behavior for that fixture issue.

## Complete Normal Image

Freeze the six-member first prediction before production edits:
`eee066d8abb11de3473df415ef421bd144125ebb82062660fd1ce78742880765`.
The normal N64 build exits0 and the entire ELF equals that first prediction.
Make's final up-to-date check exits0. There are **125 code bytes +one extent
byte +78 checked metadata bytes =204 changed bytes**, zero exclusions.

The first strict prelink attempt caught those metadata bytes before any
production edit. Permit only these exact adjacent symbol/name permutations,
with every original definition checked:

- **D_80041F00 /D_80088A90**, swapped.
- **jtbl_800A192C /D_800A1180 /D_800AAEB0 /D_800A5480**, order1,2,3,0.
- **D_800A1920 /D_800A1550**, swapped.

No symbol definition changes except the target's12-to172-byte extent.
Compare all **6,057 function bodies**: only this target changes and every
function address agrees. All **189,088 Game-data bytes /720 owners** remain
exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Guard bytes, compiler flags, layouts and nominal conversion rows stay
unchanged. The owner-specific Makefile binding causes a broader rebuild,
but no other function body changes. Existing duplicate-recipe and unrelated
broad-build warnings remain; this is not a warning-free claim.

Fresh official matching is **Game2,959/4,828 (61.29%)**, total
**3,632/5,501 (66.02%)**, **1,869 different**, zero address drift.
Init492/492 and Debugger181/181 remain exact. The placeholder already counted
as C, so nominal conversion totals do not increase. README changes only
two aggregate rows; function narratives stay in working documents.

## Fixture History And Bank

The six exact pins cover ELF, owner, Makefile, prior fixed-sine checkpoint
and the two affected sine test adapters. Roll forward all aliases of an
owned path to the same measured baseline, preserving their separate frozen
input gates. Unknown bytes do not gain a fallback acceptance path.

Fresh affected checks: **six pass in164.427s**: fixed-sine emission/input/
first-image checks, sine-phase input/first-image checks and reveal first-image
audit. These are selected checks, not fresh full historical suites. Their
audits retain original first images and compatibility pins, validating exact
current inverses before comparing archived inputs. The installed target
suite supplies the current complete-image gate.

Twelve shared checks and a smoke check pass in each tools copy;14 ASCII/AST
parses and seven task pairs agree. Exact old mirror destinations were checked
before copying. Preserve **1,101 unrelated mirror hashes**, **1,108 dirty
paths**, and mirror HEAD **ddbdd16b**. No standalone commit/reset, push,
dependency/provider/account change, Claude call, host-port operation or
frozen Release action. Tools86254e6 first, then the consumer checkpoint.
Verify the native post-commit Graphify receipt and retain the19398 excluded
nodes /2972 existing files before closing.

## Finish And Next

- [x] Recover all43 instructions, selector width, helper ABI and lazy default.
- [x] Validate compiler pool ownership and preserved retail-table binding;
  keep all original vector/table bytes and word guards unchanged.
- [x] Qualify actual math, aliases/faults, private caller payload, native32,
  independent links and effective semantic/corruption controls.
- [x] Freeze the entire first image before installation, require normal-build
  equality, and pass ten installed tests plus six affected checks.
- [x] Pass both tools-copy checks; bank tools86254e6 before consumer source/
  binding/docs/pin and refresh only README aggregate rows.
- [x] Finish **func_150F25A0** in Note1500, same owner,64 words/frame0x88,
  VA150F25A0..150F26A0, ROM11FA50..11FB50. Inspect both matrix helpers,
  actual matrix/point homes and the repeated actor0x14 output-pointer reloads
  before the three truncated halfword stores.
- [ ] Keep both fade S0/private-lifetime gaps and wider Game matching open.
  Handwritten func_150A76F0 remains in the separate assembly workstream.

```sh
python3 -m tools.experiments.game_selector_point_transform
python3 -m unittest tools.tests.test_game_selector_point_transform -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
