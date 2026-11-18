# Actor angular trail emitter guarded byte match - 2026-11-17

`func_151B01B8` replaces its zero-return placeholder with the complete actor
angular trail emitter. Semantic C emits **128 words / 512 bytes** with the
original **0xA0-byte frame**. **50 checked relocation-aware guards** normalize
temporary roles, one private pointer home and a closed instruction schedule.
There are no inserted or omitted words, frame guards or embedded retail ranges.

The independent production-ELF recount is **4,541 / 5,514 (82.35%)**, Game
**3,868 / 4,841 (79.90%)**, Init 492/492 and Debugger 181/181. Address drift
is zero and 973 converted functions remain different. The active 85% goal
needs **146 further matches**. Conversion/classification counts and bytes are
unchanged. Root README receives only the two aggregate matching rows.

## Interface, source and retained state

Owner `conker/src/game/generated_1DD500.c`, VA151B01B8..151B03B8,
ROM1DD668..1DD868. The recovered interface is `void (u8 *actor, u8 *source)`;
all three inspected callers ignore the return register. The alternate draft's
32-bit field accesses and pointer-sized stand-ins for private objects are not
adopted. Retail uses a byte at source+4, a byte at actor+74, an unsigned halfword
at actor+7A, and a pointer at actor+1D4.

Null actor, null matrix and actor flags with low nibble F exit before providers.
The routine prepares the complete 36-byte height/surface result, then reads
the possibly changed source identity. Null source and identities 53/A5 select
type 4; other sources use `func_15134070`. Type 99 exits. The selected 16-byte
record is `D_800A3FD8[type]`; category byte+E equal to 2 exits before transforming.

Heading is `(actor->heading >> 8) + 64`, narrowed to **u8 before subtracting 104**.
This wrap matters for high bytes 192..255. The matrix pointer is loaded again
after the preparation/classifier calls. `func_15143134` transforms the three
floats at D_800AA120 through matrix+180 into the private trail position.
The cached heading survives that call, while category+E and all five scalar
globals are read afterward. A helper may change the category to 2 at this point:
the effect still submits, with selector 0; the earlier disable gate is not rerun.

The angular fields are heading-minus104,208,-27,54. The localized trail uses
D_800AA2A0/A4/A8/AC/B0, radius6, count10/range20, request3/range2,
duration30/range40, mode155/range100, chance0.5, final values16/15 and request0.
Selector is 1 only when the repeated category read equals 1. Submission passes
the angular block, complete localized trail, retained surface pointer,255,1.

The surface occupies SP2C..4F, the cached heading byte SP53, angular block
SP54..5B and 68-byte trail SP5C..9F. Native checks credit65 defined trail
bytes; its three unwritten padding bytes receive no portable C value claim.
The guest/proof separately retain and compare seeded padding bytes.

The classifier result and selected record pointer have disjoint lifetimes,
represented by one local union without reading an inactive member. This
recovers the original frame and full 128-word shape. Separate scalar locals
emit 124 words; other classifier forms emit 128 but enlarge the frame to A8.
Those shapes are rejected. The O2/g3/mips2/o32 profile is unchanged.

Raw body SHA-256:
`27ef3eece975c7bb0385a688d6711ae9ed3a8450a34b2e83afdc77b2de482114`.
All 15 owner neighbors and normalized pools are unchanged, including the prior
`func_151B0050` match and the existing `func_151B03B8` GLOBAL_ASM restoration.
The blood routine remains classified as assembly.

## Independent relation and focused gates

The independent normalizer changes only the selected record's V0/V1 lifetime,
four closed heading/count temporary lifetimes, the unexposed pointer home
SP28 to SP20, and a **bijection of words 66..113**. It neither inserts nor
omits instructions. The last global HI16/LO16 pair moves across three relocation
sites at byte offsets114/118/11C. The normalized words and complete binding map
equal a separately assembled original target, not a pasted retail body.

The instruction-driven proof is independent of that normalizer. It compares
**all 16 paths, all 128 words and 176 private/incoming bytes**, ordered calls,
public read footprints, FCSR and restored saved GPRs/FPRs/SP/RA. It models
arbitrary public aliases and retained helper mutations within the declared
nonfaulting contract. Raw private layout exchanges the four bytes at SP28
with SP20 under an explicit canonical entry-byte relation; exposed object
homes are literal. An independent T8/T9 allocation passes. Seven effective
controls reject surface home, heading half, disable category, count base,
retained pointer home, selector destination and frame restoration changes.
Void-return caller scratch registers and raw fault-prefix equality are not
credited. Nonvolatile public memory is stable between calls/stores.

Both final tools configurations pass **six fresh checks**, with zero failures,
errors or skips: **168.914s primary / 170.226s sibling overlay**.

- Both real padders process the complete owner and retain 15 neighbors.
  **12 GNU links** cover four independent symbol/carry layouts. **146 source
  controls** reject corruption of each 128 words and all 18 original bindings.
- **312 guard controls** cover 300 wrong expected/replacement/missing-word rows
  and 12 corrupted expected/replacement relocation-field cases in both padders.
  Exactly 50 rows append to the unchanged old CSV; no prior guard is retired.
- Original/raw/derived streams each pass **912 guest cases**, visiting every
  word. Independent references check all calls/arguments and exposed objects;
  complete compared RAM agrees under the private entry/layout relation.
  Cases include all 256 heading bytes, early exits, default/special/classified
  sources, disabled/selector categories, actor/source aliases, two stack phases
  and five mutable helper effects.
- Native32 source builds fresh at **O0/O2/O3**, each passing 912 finite fixtures
  under strict aliasing and UBSan. Eight effective negatives cover missing byte
  wrap, wrong heading half, disable category, transform matrix, selector,
  duration, output slot and missing surface preparation: **11 builds/runs**.
- All three original caller connections pass **112 cases per stream**. The
  eight-word prefix of func_15194794 covers its authentic call/delay slot;
  its full parent is not qualified. The complete 18-word func_15195650 and
  func_1507003C wrappers execute through the next effect and return. That next
  effect, func_151B09BC, remains an opaque provider. Three argument controls
  reject a changed incoming source. Target helpers remain modeled services.

Failed fixture/packaging attempts are retained and uncredited. The source
fixture initially overlapped the interpreter stack; final fixtures enforce
public/private disjointness. Random height bytes also exposed native x87
signaling-NaN quieting in the test serializer; final native height inputs are
finite, while the symbolic relation keeps opaque bytes/status. The first
packaged suite found a module/helper name collision and missing proof return;
both were repaired and both full final suites rerun. No candidate C words or
guard rows changed for these harness repairs. Hardware FP traps, timing,
arbitrary native padding values and gameplay acceptance are not claimed.

## Actual Make, complete image and installed validation

The independent shadow executes the actual five-command GLOBAL_ASM owner
recipe. Production Make compiles only this owner, pads it, relinks and recounts;
no prebuilt object is installed. Production equals the independent image:
`b7eb8c35497a3e257eb752019b560c18c570ed56947eb7378d9971694d4916a0`.

Strict complete-image accounting changes **442 bytes**, with **zero
exclusions**. The one named symbol/string reorder group is modeled explicitly;
definitions agree except the declared target size. Four controls reject symbol
value, name byte, protected data and target-word corruption. All other 6,050
bodies and all 6,051 addresses remain unchanged. Exactly one of 698 objects
changes, retaining15 neighbors. All **189,088 protected bytes / 720 owners**
remain exact. Progress classification rows are byte-identical.

Fresh installed-source compilation agrees on all 16 owner functions. Actual
production instructions pass another 912 guest cases and 112 cases for each
of the three caller connections per stream. Previous padder/link, symbolic and
native checks are reused only with exact task/input/fixture fingerprints.
Production match-progress, tools-check and independent actual-ELF recount pass.
The pre-existing duplicate generated_12D630 recipe warning is unchanged.

## Preservation and next work

The baseline freezes **1621 inputs** with no links to live-tree files.
Exactly four change: source, guard CSV, owner object and ELF. Nine maintained
task files and actual imported dependencies are separately fingerprinted.
The sibling's 2,434 dirty paths / 343 scoped dependencies remain unchanged;
testing uses an isolated overlay. Claude calls are 0. Host Release/saves remain
untouched; the adjacent host directory has no source checkout to synchronize.

Evidence is retained under `conker/build/game-next-151b01b8-private/adoption/`:
paired final suites/imports, independent derivation/proof, guard/padder/link
controls, guest/native/caller receipts, shadow Make/image prediction, real Make,
production audit/focus and actual recount. Native Graphify update fails closed
on its reduced scan. Scoped AST merging of eight code files retains all
65279 prior IDs and the explicit qualified target edge;
this is not a full-corpus extraction. Commit tools before consumer source,
guards, notes, aggregate README rows and pin, locally only.

Next inspect **func_151B09BC**, the **115-word** placeholder after the retained
blood assembly routine in the same owner. The 85% goal remains active.
