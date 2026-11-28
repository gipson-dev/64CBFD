# Actor/ring proximity callback guarded byte match - 2026-11-28

`func_151987CC` in `conker/src/game/generated_1C2C60.c` now contains the full
**108-word / 432-byte** leaf callback, VA `0x151987CC..0x1519897C`, ROM
`0x1C5C7C..0x1C5E2C`. There is no alignment tail. Its existing public interface
`s32 func_151987CC(u8 *owner)` was previously repaired in Note 2656; that
four-word zero-return stub had no matching credit. This recovery adds **one**
qualified match. No shared header or other function interface is changed.

Actual production: **4,720 / 5,528 (85.38%) total**, **4,047 / 4,855 (83.36%)
Game**, Init 492/492, Debugger 181/181. Zero address drift, 808 still different.
Conversion rows and denominators are unchanged. The **90% goal remains
active**: **256 further matches** reach 4,976/5,528. Tools commit:
`445ac28f9f17dbed97c38c204e3bc3599fd2f0ad`; consumer baseline: `e7ab1b66`.

## Recovered behavior

The callback captures the 0x90-byte effect payload and 0x24-byte ring-record
pointers from owner offsets 0x98/0x94. It scans 25 inline 0x32C-byte actors,
from `D_800CC2D0` to the existing `D_800D121C` boundary marker, leaving reserved
actor 25 unscanned. Inactive actors, a nonzero byte at offset 0x65, and the
payload owner's unique ID are excluded.

For each eligible actor it walks the ring backward from the signed tail toward
the live signed head, wrapping through the unsigned capacity. A genuine
three-float point subobject is copied from each 36-byte record to a local.
Width and height are signed halfwords. The vertical offset at actor+0xE8 is
also read **signed**, requiring an explicit `s16` cast of the shared `u16`
field. The ordered single-precision proximity calculation is:

```c
dx = point.x - actor.x;
dz = point.z - actor.z;
dy = point.y - (actor.y + signed_vertical_offset);
dy *= (1.0f + width / height) * 0.5f;
inside = ((dx * dx + dy * dy) + dz * dz) < width * width + 2500.0f;
```

On overlap, the live head advances with capacity wrap and the signed count
byte decreases until head equals the current cursor. Each store is followed
by the original reloads. The routine returns **one**. Height-zero IEEE
infinity/NaN cases preserve the original operation tree and strict comparison.
Portable native cases use valid ring indices and capacities 1..127; no
termination claim is made for malformed ring metadata.

## Certified compiler normalization

Semantic C emits all 108 words with its natural **80-byte frame**. Retail uses
**96 bytes**. The point is at raw SP+56 and retail SP+64. No artificial source
padding, fake locals, insertion or omission is introduced. **Fifty bound
words match directly; 58 expected-word guards** normalize register roles,
private frame/home positions and independent quiet-load scheduling. Two
verified literal references bind the original `2500.0f` pool. The O2/g3/mips2/
o32 profile is unchanged. This is a **guarded C match**, not a raw direct match.

The independent symbolic certificate executes all six regions: prefix (1
path), actor gate (5), ring step (18), head retirement (6), actor end (2) and
return (1). These **33 inductive paths** cover the whole function without a
loop-iteration bound. It checks live storage roles at joins, preserved saved
registers, exact public writes, and each public read's address/width/count per
write epoch. Public RAM aliases remain admitted. Only ordinary nonvolatile
reads within one unchanged public-memory epoch may commute. Private storage
is aligned, disjoint, unexposed, and limited to the four FPR save words and
three point words. The map preserves the saved F20/F22 values and stack return.

Every floating operation, including integer conversions, retains its **ordered
operands, computation order and numeric controls**. No floating commutativity
or reassociation axiom is used. MMIO, races, raw fault-register identity and
floating-trap register identity are outside this proof. Normalized fault
prefixes are checked separately. Two valid temporary GPR/FPR renamings still
pass; ten effective mutations reject wrong frames/homes, unsigned offsets,
actor stride, cursor direction, identity gate, head/count stores, FP operation
and return value.

## Literal, owner and image safeguards

The compiler pool is exactly `0x451C4000` (2500.0f) plus twelve zero alignment
bytes. A per-owner checker pins all 69 compact functions, their complete text
and extents, every binding, the two pool references and pool metadata before
rebinding. ROM 0x24D59C and the frozen ELF at 0x800A8ADC confirm the original
literal. All **68 other raw and padded function bodies/bindings**, existing
pools and guard history remain unchanged; both padders reproduce the frozen
before object and agree on the selected object.

A compiled **2501.0f** source control retains the target's instruction words
and bindings. Both unchecked address-only maps would hide that wrong value;
the new checker rejects it. Across pool, text, neighbor, relocation and
section/extent mutations, **326 controls reject**. Removing each new guard is
visible in both padders (**116 controls**), and every wrong expected word
rejects (**116 controls**). The expanded actual GNU Make recipe stops at the
checker on the wrong literal before creating a bound or final object.

Twenty GNU links cover four independent rebases and signed HI16/LO16 carry
boundaries. All normalized words/bindings match original assembly. The raw
inductive transfer proof is repeated at every rebase. An independent
frozen-before-C plus original-target-assembly prediction equals the entire
private and production ELF: **331 changed bytes, zero exclusions**. All
**720 data owners / 189,088 protected bytes**, other bodies/addresses and
conversion rows remain fixed. Six existing unrelated duplicate-recipe
warnings are unchanged; no new compiler or Make diagnostics are introduced.

## Behavior and caller evidence

- Actual SDK/native32 C: **4,128 cases each at O0/O2/O3**, separate translation
  units, strict aliasing, trapping UBSan and LTO type checks. Cases exercise
  capacities 1/2/4/7/31/127, every count byte, signed offsets, zero heights,
  strict-distance boundaries, skipped actors and the last scanned actor.
  All actor/record/payload objects and every unwritten owner byte are checked.
  Six semantic controls fail with logical exit 42.
- Guest: **468 cases across four streams / 1,872 executions**. All **108 words**
  execute. Raw C public memory, writes and quiet-read epochs agree with
  retail; normalized complete machine states agree. Three owner-pointer
  domains and both stack phases are covered. **159 normalized memory-access
  fault triples** preserve complete prefixes. The oracle does not emulate
  floating exception flags; the independent ordered FP certificate supplies
  the stated normal-completion equivalence.
- Caller: **384 connected executions** use the complete original 257-word
  `func_15196748` and the real three-entry `D_8008F880` table, index **2**.
  This focused scope executes 124 parent and 102 child words; the separate
  child corpus covers all108. Signed selector -1 skips. The parent consumes
  the child's Boolean result; forcing zero causes its early-zero return.
  Other parent providers remain explicitly bounded, without helper credit.

The ten pre-install checks are retained with their original fingerprints.
Ten installed checks run freshly in both final tools copies. A one-field
Makefile phase-fingerprint correction changes no source, tool code, guards or
compiled outputs; the pre-install path never used that field. The first
installed attempt failed closed on the incorrect fingerprint before target
checks ran. The corrected value is independently pinned by the qualified
private Makefile and the byte-identical production Makefile. The real dirty sibling tools
checkout and its recorded base/extended dependency hashes are preserved.
Shared `make tools-check` passes. One tool-disabled, packet-only Claude review
found no actionable defect. Its source-to-object scope caveat is covered by
fresh whole-owner compilation, raw payload identity and actual Make replay;
Codex independently verifies all acceptance evidence.

The graph is queried and refreshed by scoped AST extraction with prior ID and
qualification-metadata retention; this is not a full-corpus re-extraction.
Final graph/hook/bank receipts are retained in
`conker/build/game-actor-ring-proximity-151987cc-private/`. Read-only inspection
of the sibling host's generated function supplies no active implementation to
transfer or qualify. No host changes, build, launch or gameplay acceptance is
claimed; host Release remains frozen. No push or subagent is used.

Next: continue ordinary unmatched Game qualification from this committed
checkpoint. N82 `func_1514EECC` remains parked pending its separate proof.

Paired installed receipt:

```json
{
  "labels": [
    "installed-v3-primary",
    "installed-v3-sibling"
  ],
  "passes": true,
  "fresh_tests": 10,
  "reused_tests": 0,
  "equal_report_rows": 9,
  "primary_imports": 328,
  "sibling_imports": 329,
  "equal_tool_data_inputs": 249,
  "independently_copied_task_files": 13,
  "closed_tools_root_proved": true,
  "source_installed": true,
  "matching_credit": 0
}
```
