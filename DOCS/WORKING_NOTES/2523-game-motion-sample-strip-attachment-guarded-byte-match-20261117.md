# Motion-sample strip attachment guarded byte match - 2026-11-17

`void func_151AE0E4(u8 *actor, u8 key)` now replaces the zero-return
placeholder with the complete motion-sample strip attachment routine. Its
**96-word / 384-byte slot and 0x38-byte frame are byte-exact in production**.
Semantic C emits 95 words; **49 relocation-aware checked guards and one NOP
insertion** recover the original allocation, FP operand order and schedule.
No original instruction range is embedded in the C body.

Live progress is **4,535 / 5,514 (82.25%)**, Game **3,862 / 4,841 (79.78%)**,
Init 492/492 and Debugger 181/181, zero drift and 979 still different.
The active 85% goal needs **152 further matches**. Converted totals and bytes
are unchanged; the root README receives only the two aggregate matching rows.

## Source, ABI and behavior

Owner `conker/src/game/generated_1D92F0.c`, VA151AE0E4..151AE264,
ROM1DB594..1DB714. The old prototype's return type was false: the original
routine has a two-word incoming interface and no meaningful C return value.
Both original direct calls are in the complete 30-word `func_151AE06C`.
Its existing commutative-selector guard is preserved byte for byte.

The lookup receives the low byte of the incoming key. A null lookup retains
retail's stationary self-branch and NOP delay slot. Eligibility uses the
record's signed16 status, actor enable byte and actor disable byte. The
projection call has **five arguments**, including Z at the O32 stack argument
home; its three float arguments are not promoted to doubles.

After the opaque projection provider, record count, spacing, points and the
actor's child/fraction are read again. The index uses the original truncated
140/spacing quotient, count-minus-quotient-minus-one span, fraction product
and 24-byte point stride. Three sampled coordinates retain their stack homes.
Distance preserves the original ordered subtractions, squares and additions.
The comparison is `!(cutoff < distance)`, including its unordered/NaN behavior.
The four attachment writes preserve their widths, order and child reload.

Existing curve typedefs move unchanged before the new body to support the
complete projection prototype. The later lookup structure tag remains the
same type. The separate donor has incorrect widths and an incomplete helper
interface, so its body is not adopted as a byte-exact input.

## Complete relation and execution evidence

All five final checks pass freshly in **both tools configurations**, with
zero failures, errors or skips: **147.204s primary /
149.685s sibling overlay**. The source-aware tests compile the
complete owner and preserve all 32 neighboring functions and normalized pools.

- The instruction-driven relation covers **six complete paths**: one null
  spin and five returning paths. It compares every 72 private/incoming-home
  bytes, full provider arguments, ordered public writes and FP/status events,
  public byte state and stable-read multisets. Both providers may mutate public
  memory, argument homes, caller-saved GPR/FPR state and abstract FP status.
  Return paths restore the full required GPR/FPR/stack/RA state.
- An independent scratch-register allocation passes. Eight effective negatives
  reject wrong status width, fifth Z argument, index bound, point stride,
  attachment value/store width, null spin and frame restore.
- Retail, raw and derived streams each execute **624 guest cases**. Derived
  full RAM, provider/private frames and all **8,064 ordered FP observations**
  agree with retail. Execution visits95/96 retail and derived words and94/95
  raw words. The stationary spin's branch and otherwise unexecuted delay NOP
  are separately checked literally; full execution coverage is not claimed.
- The complete original caller executes **128 cases per stream**, visiting
  all 30 caller words. Admission, packet reload after admission, zero/equal/
  different selectors, reset mutation, captured requested byte and propagated
  null spin pass. A wrong packet-byte address rejects. Derived full RAM,
  private stack and FP events agree with retail.
- Native32 C is compiled freshly at **O0/O2/O3**, each passing **616 cases**.
  Four freshly compiled controls reject wrong status width, missing Z,
  wrong span and an incorrect unordered-distance branch. All public regions
  and five helper arguments are compared. Native cases exclude null spinning;
  no native FP-status or private-stack claim is made.

Commit preparation removed trailing empty lines from four new Python modules.
Their complete ASTs, including source locations, are identical. The original
qualification/import hashes remain recorded, with a format-only receipt linking
them to the final source hashes. Those checks are explicitly reused after this
format cleanup; no new behavioral test execution is claimed for the cleanup.

The relation assumes ordinary mapped, disjoint public objects and private
stack, stable memory between provider calls/stores, nontrapping FP and valid
index/conversion inputs. The mapped finite fixtures cover counts 0..255,
negative through high indices, provider mutations and NaN coordinates/cutoffs.
This is not arbitrary-alias, literal fault-state, cycle-timing or gameplay proof.

## Object, full-image and actual production gates

Both real padders produce the independent original assembly body and all four
bindings. Twelve GNU links use four code/data layouts and HI/LO carry boundaries.
Both owner-defined helpers are explicitly bound to the same requested values
as the standalone reference; linked symbols are checked. The first fixture
mixed relocated owner-defined helpers with unrelated reference addresses;
those failed receipts are retained, and both complete suites pass after repair.

All 95 source-word corruptions reject before derivation. Object controls reject
99 raw/binding corruptions, 196 stale-CSV changes and 51 replacement/insertion
changes. The complete old CSV prefix is preserved and 49 rows are appended;
no old guard is retired and no word is omitted.

Five actual Make commands compile/pad the complete owner in the independent
shadow. Actual production Make then rebuilds source/ELF/progress; no prebuilt
object is installed. The complete-image prediction accounts for **361 changed
bytes with zero exclusions**. Its one explicitly modeled three-name symbol/
string reorder preserves every named definition. The inherited image helper's
12-byte placeholder assumption is corrected privately to this target's measured
20-byte placeholder; the shared helper and its tests remain unchanged.

All other **6,050 function bodies and every function address** are unchanged.
Exactly one of 698 frozen objects changes, with 32 neighbors retained. All
**189,088 protected data bytes / 720 owners** remain exact. Named-symbol,
name-string, protected-data and target-word corruptions reject.
The production ELF equals the independently predicted image:
`eb4a897584320799cb1f26e852e60c211bc304e1f5453780cc1d0dc7235277fa`.

Fresh post-install source compilation matches all 33 compact owner functions;
actual production instructions pass 624 guest and 128 original-caller cases.
The earlier source/padder/symbolic/native results are reused only with exact
task/input/fixture fingerprints. Production match-progress, tools-check and an
independent actual-ELF recount pass. The unchanged duplicate generated_12D630
Makefile recipe warning remains; a warning-free build is not claimed.

## Preservation, evidence and next work

The 1553-input baseline links only earlier immutable snapshot files; live
source, guards, objects and tools remain separate. Exactly four frozen inputs
change: source, guard CSV, owner object and linked ELF. Conversion classification
and retail binary remain unchanged. New task files/imports are separately sealed.
Primary imports have 351 unique tool files; sibling overlay has 353 unique files
and 355 module rows: ten overlay,301 sibling and44 primary. The sibling's 2434
dirty paths and 339 present scoped dependencies remain intact.

The host sibling still contains only `.codex` and `recomp_scene`; no source/Git
checkout is available to synchronize. It is untouched, including Release/saves.
Claude calls are 0: existing local instruction/ABI tools settle this routine.

Receipts are under `conker/build/game-next-151ae0e4-private/adoption/`:
paired sealed suites/import origins, both padders/GNU links, symbolic/native/
guest/caller controls, Make prediction, metadata controls, production audit,
post-install execution and actual recount. The native graph update preserves
old IDs and fails closed on the reduced scan; the scoped AST merge retains all
64874 prior IDs and records the explicit target reference.
This is not full-corpus re-extraction. Commit tools before consumer source,
guards, notes, aggregate rows and pin, locally only; no push.

Next inspect **func_151AE3A8**, the 122-word neighboring actor/strip position
update (frame 0x78), retaining its heading/trig calls and repeated sample loads.
The broader 85% goal remains active beyond this checkpoint.
