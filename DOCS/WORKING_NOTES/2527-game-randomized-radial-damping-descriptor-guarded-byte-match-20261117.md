# Randomized radial damping descriptor guarded byte match - 2026-11-17

`func_151AFC88` now replaces the zero-return placeholder with the complete
randomized radial effect constructor. Semantic C emits **135 words / 540 bytes
with the original 0xA8-byte frame**. **Ten checked relocation-aware guards**
normalize one temporary FPR allocation permutation; there are no inserted or
omitted instructions and no embedded retail instruction ranges.

The independent production-ELF recount is **4,539 / 5,514 (82.32%)**, Game
**3,866 / 4,841 (79.86%)**, Init 492/492 and Debugger 181/181. Address drift is
zero and 975 functions remain different. The active 85% goal needs **148 further
matches**. Conversion counts/bytes and classification rows are unchanged.
Root README receives only its two aggregate matching rows.

## Source, ABI and descriptor lifetime

Owner `conker/src/game/generated_1DCA70.c`, VA151AFC88..151AFEA4,
ROM1DD138..1DD354. This is `D_8008AA00[16]`; the retained retail word at
ROM22F500 and the original callback table confirm that binding. The callback
retains **all 15 argument slots**: X/Y/Z occupy slots2/3/4, heading is the
signed low halfword of slot8 and channel the low byte of slot14. Unused slots
remain explicit. The alternate-source draft's compressed seven-argument
signature would place heading/channel incorrectly and is not adopted.

Five integer draws and two real draws retain their original order. Lifetime
is `(random & 15) + 25`; the randomized color byte is unsigned `%156 + 100`.
One captured real sample supplies both equal extents through multiply202/add101.
The next integer sample yields the signed `%21 - 20` pitch, while the next real
sample uses D_800AA110, add500 and D_800AA114 for the direction request. Separate
draws set flag bits0x40/0x80. The fixed fields, D_800AA118 load and D_800AA11C
snapshot precede allocation. Success copies four snapshot bytes to object+A8;
allocation failure skips that copy. The callback always returns1.

The recovered related packet layout is reused with private target names.
Its **116-byte local aggregate** includes all defined descriptor fields,
unwritten holes, the **112 bytes actually copied by the original factory**,
and four further retained frame bytes. The descriptor starts at SP+0x34,
the scalar snapshot at SP+0x2C and captured random word at SP+0x24. Omitting
the copied tail produced smaller frames and is rejected. Padding is not
cleared or treated as initialized data. Native checks cover defined fields;
the guest comparison separately retains seeded unwritten bytes.

Raw body SHA-256:
`5934de46b69a65cf140b11b3588b1ebc81cfa4e795857ed0927ab76ea8812882`.
All 18 original call/data relocations, six owner neighbors and normalized
pools agree. The existing O2/g3/mips2/o32 profile is unchanged.

## Independent FPR relation and focused checks

Only words48 and50..58 differ before guards. The independent derivation
swaps temporary roles F4/F10, F6/F16 and F8/F18 within words47..58. A symbolic
comparison preserves both ordered FP expressions and all three position
stores; no operands are commuted. Actual retained `func_150ADA20` and
`func_150ADA68` instructions establish that no incoming floating-point argument
is read. A forward use/write analysis through the following helper calls and
caller word81 proves every differing scratch role is killed before reuse.
Three controls reject changed coordinate destination, scale operand and
constant register. Literal pre-guard fault-register equality is not claimed.

All **six final focused checks pass fresh in both tools configurations**,
with zero failures, errors or skips: **87.397s primary /
89.504s sibling overlay.

- Both real padders process the complete owner, produce all135 retail words
  and retain all six neighbors. **12 GNU links** cover four symbol/carry
  layouts across original/generated/generic objects. **153 controls** reject
  every source-word corruption and all18 changed relocation bindings.
- **60 guard controls** cover wrong expected words, wrong replacements and
  missing rows through both padders. Exactly10 rows are appended; every prior
  CSV byte remains intact and no guard is retired.
- Raw/original/padded programs each pass **3,072 guest cases**, visiting all135
  target words. Independent packet/reference results, helper calls, public
  memory and the complete compared guest RAM/GPR/FPR state agree. The matrix
  covers signed heading boundaries, high-word noise, all flag combinations,
  allocation outcomes, two stack phases and provider/home mutation probes.
- Native32 source compiles fresh at **O0/O2/O3**, each passing **4,096 defined
  cases** under UBSan with **14 effective negative controls** for descriptor
  fields, coordinates, extent/pitch/speed, flags, scalar loads, factory context
  and return value.
- The original **16-word radial-dispatch call window** executes **80 cases per
  stream**, checking argument placement and successful continuation. The
  entire parent and the other three table-dispatch callers are not qualified.
  A late incoming-heading mutation produces FFFF8001 in all three programs.
- **80 additional cases per stream** connect the original factory wrappers
  and memcpy, whose complete retail bodies are checked against the live ELF.
  They visit all18 words of func_15130374, **41 of61** words of func_15130280
  on the selected mode/null-context paths, and all11 memcpy words. The real
  112-byte descriptor copy and final four-byte copy execute; allocation remains
  modeled. This does not claim every factory mode or hardware allocation.

The first suite stopped the guest check at a list-versus-tuple container
comparison before executing its matrix. The patched-word reader was corrected
to the harness's list representation; all3,072 guest cases and both complete
final suites were rerun. The failed receipt remains retained and uncredited.
Candidate C and guard words did not change for that fixture repair.

Defined native coverage assumes ordinary mapped, disjoint objects and bounded
finite inputs. Guest-only incoming-home/private-scalar mutation probes do not
establish portable C alias semantics. Unwritten native padding values, native
private frames, hardware FP traps, cycle timing and gameplay are not claimed.

## Actual Make, strict image and installed checks

The independent Make shadow compiles, pads and assembles the complete owner.
Real production Make compiles only that owner, then relinks and recounts;
no prebuilt object is installed. Production equals the independent ELF:
`5a731bb15283d8db71a18e99682a9d5de1242fbdac9b22df1c30bacd86dd94a1`.

Strict complete-image accounting changes **486 bytes**, with **zero exclusions**.
Three named symbol/string reorder groups are explicitly modeled, while named
definitions agree except for the declared target size. Four controls reject
symbol-value, name-byte, protected-data and target-word corruption. All other
**6,050 bodies and all6,051 function addresses** remain unchanged. Exactly one
of698 objects changes, retaining six neighbors. All **189,088 protected data
bytes / 720 owners** remain exact.

Fresh installed-source compilation agrees on all seven owner functions. Actual
production words pass another3,072 guest,80 original dispatch-window and80
connected factory/copy cases. Previous padder/link, FPR relation and native
results are reused only with exact task and fixture hashes. Production
match-progress, tools-check and an independent actual-ELF recount pass. The
pre-existing duplicate generated_12D630 recipe warning is unchanged.

## Preservation and next work

The baseline freezes **1,602 inputs**:1,599 retained/copied inputs plus three
additional observed dependencies, with no links to live-tree files. Exactly
four frozen inputs change: source, guard CSV, owner object and ELF. The seven
maintained task files and actual imports are separately fingerprinted. The
sibling's **2,434 dirty paths /343 scoped dependencies** remain unchanged.
Claude calls are0. The host directory contains only `.codex` and `recomp_scene`,
with no Git/source checkout to synchronize; Release/saves remain untouched.

Evidence is under `conker/build/game-next-151afc88-private/adoption/`: paired
sealed checks/imports, independent role proof, padders/GNU links/controls,
guest/native/dispatch/factory receipts, actual-Make prediction, production
audit/focus and recount. Native Graphify update exits fail-closed on its reduced
scan, retaining all 65138 old IDs. Scoped AST merging of
seven code files retains every ID and the explicit target reference; this is
not full-corpus re-extraction. Commit tools before consumer source, guards,
notes, aggregate README rows and pin, locally only.

Next inspect **func_151B0050**, the **90-word** placeholder in
`conker/src/game/generated_1DD500.c`. The 85% goal remains active.
