# 2657 - Interpolated actor ring emitter guarded byte match

Date: 2026-11-23. The total 85% matching goal remains active.

`func_15196B4C` has its complete semantic C body in
`conker/src/game/generated_1C2C60.c`. The qualified guarded output matches all
**383 words / 1,532 bytes / frame 288**. Raw IDO output is **387 words / frame
288**, and is not directly byte-exact. The O2/g3/mips2/o32 profile is unchanged.
Original: `conker/asm/1C2C60.s:1440`, VA `15196B4C..15197148`, ROM
`1C3FFC..1C45F8`.

Production recount: **4,637 / 5,528 (83.88%) total**, Game
**3,964 / 4,855 (81.65%)**, Init **492 / 492**, Debugger **181 / 181**,
zero address drift, **891 different**. **62 more matches** reach 85% at this
denominator. This adds one match and changes no conversion rows.

## Recovered behavior and interfaces

`s32 func_15196B4C(u8 *owner)` captures the current payload and record pointers.
It rejects a missing attachment matrix, optionally obtains a scale callback
result, then transforms the attachment's two endpoints through one captured
matrix. It advances the floating phase, and, when that exceeds one, interpolates
the prior endpoints, elapsed time, speed and size across new ring records.
Each iteration accumulates two optional child-emitter counters, calls their
providers when needed, initializes a record, advances an unsigned random phase
by `((u32)random % 6U) + 3`, integrates gravity and position, and wraps the live
head/tail/count. Final endpoint copies use the captured payload destinations.
The function returns one to continue or zero for a missing matrix.

The C retains actual retail reloads and captured lifetimes. Opaque providers
may change public pointers, vectors, cursor bytes, payload fields and globals;
the second transform retains the originally selected matrix. Existing 0x90-byte
payload and 0x24-byte record types use real three-float arrays. Unknown fields
keep their existing offset names rather than speculative semantic renaming.

The complete original 100-word `func_15147740` dispatches this routine through
`D_8008A23C[2]`, passing one pointer word; zero leads to `func_1516972C`.
Its frozen compiled caller also matches all original words.

Two zero-return, no-argument placeholders now express their actual two-pointer
void interfaces: `func_15198D88(u8 *, f32 *)` and
`func_151990AC(u8 *, f32 *)`. Their bodies remain unrecovered. Each changes
from three to four compiler words and earns **zero additional credit**.
Original 201/194-word helper bodies and first-call parameter liveness establish
the two arguments. Their first provider `func_150ADA68` takes no arguments;
live unpassed entry registers are not silently presumed dead. An independent
ABI-only C variant preserves all 67 other functions; all 68 non-parent functions
in the selected owner match that variant. The remaining 66 neighbors, binding
identities, literal pools and diagnostics stay fixed. Both helper code windows
and declared sizes are explicitly included in image prediction.

## Closed transform and independent checks

The transform pins all **387 source words and nine binding sites**. Its index
and operand rows consume source operations, reallocate registers/private homes,
and schedule the same arithmetic, public accesses and calls. Four surplus
allocation operations are removed jointly with the storage rewrite: two NOPs,
one repeated ordinary RAM load in a quiet epoch, and one private spill. The spill
is not asserted dead in the unchanged raw stream. There are **zero insertions,
four omissions**. The complete old guard CSV is retained as its prefix.

An independent symbolic interpreter does not read the projection. It checks
five entry/setup paths, all 48 loop/exit paths from arbitrary related loop
states, and the complete identical 17-word epilogue. This establishes an
inductive relation for an unbounded number of iterations. Ordered public writes,
opaque call arguments and exposed vector contents, private logical values,
saved GPR/FPR lifetimes, and normal-completion FCSR endpoints agree. Public aliases
are conservatively invalidated after every store/provider. The one extra load
is permitted only within a quiet epoch of ordinary nonvolatile mapped RAM.

Floating values retain exact operand order and numeric controls. Exception
flags accumulate and the final Cause comes from the common last operation;
Compare retains its condition semantics. A separately factored status lemma
checks 32 Boolean cases per IEEE exception lane, eight unimplemented-exception
cases, and five effective counterexamples. It allows arbitrary initial flags,
enables, rounding and flush controls. The architectural premises come from
[NEC VR4300 manual U10504EJ7V0UMJ1](https://hack64.net/docs/VR43XX.pdf), printed
pp213-214 and 237-238, checked against the SDK's `R4300.h` masks. This lemma alone
is not a function proof. Raw trap/fault-prefix identity, MMIO and data races are
outside the normal execution contract.

- Twenty-two effective machine-semantic mutations are rejected. Alternative
  GPR and FPR allocations and an independent float schedule are accepted.
- **604 guest cases per raw/normalized/padded/retail stream** pass independent
  public-memory, return and exact ordered-call comparisons. This includes 84
  actual-preset cases and eight large-capacity cases. Preset vectors, gravity,
  rates, duration/delay and size come from ROM; selectors and phase stay under
  fixture control. All saved GPR/FPRs restore.
  Normalized/padded full state agrees with retail. Raw private bytes are not
  claimed equal. The only unexecuted original words are an unreachable duplicate
  selector load and the zero-divisor BREAK for the constant divisor six.
- Three guest-only record/payload overlap cases, 38 connected complete-caller
  cases per stream, and **272 fired access-boundary prefix sets** pass. The last
  comparison is normalized/padded versus retail, including dispatched words;
  it does not claim raw C fault-state equality or actual helper internals.
- Native **SDK32 O0/O2/O3**, strict aliasing and UBSan checks pass all 604 cases
  with valid typed objects, real SDK actor layout, initialized arrays, padding,
  guard bytes and matrices. They check 12 owner, 30 payload and 12 record fields.
  Ten effective source-level semantic mutations fail by comparison.
- Both real padders reject every changed source word and binding: **792 effective
  rejections**, plus oversized-body rejections. Twelve GNU links across four
  independent code/global arrangements match original ASM, including HI/LO carry
  and JAL-region handling.

Fresh paired suites run five focused gates before and after installation:

| Run | Time | Checks |
| --- | --- | --- |
| preinstall-primary | 260.526s | 5 fresh / 0 reused |
| preinstall-sibling | 300.359s | 5 fresh / 0 reused |
| installed-primary | 249.983s | 5 fresh / 0 reused |
| installed-sibling | 287.979s | 5 fresh / 0 reused |


## Production and checkpoint

Actual Make replay reproduces the entire padded owner. The independent predictor
recompiles frozen old C with old guards, then uses only original target ASM and
the separate ABI-only C variant. It reconstructs all three changed code windows
and sizes, named definitions, symbol ordering and every string-pool byte.
Production equals that prediction at every byte: **1194 changed bytes,
zero exclusions**. All 189,088 protected Game data bytes and 720 owners remain
exact; shared headers and the complete debugger object remain frozen.
Shared `make tools-check` passes. All frozen inputs and real sibling tools
changes are audited against the explicit adoption plan.

```text
before ELF: 6909177ec67e462c17df17efb3c902e377fa85c7e8decfff9ad5d39a8fd0be2c
after ELF:  47817ce9cabf98e1ecc9fb9281bdd90e24bd3096ae21b3f6849326a5289ecd54
owner:      d3977602a45899fc94c47f47b8a45acf7894023e62bac1f74823c5aaa0cc3dfd
```

The paired tools overlay records sibling, primary-fallback and task origins;
the real dirty sibling's HEAD, status and dependencies remain intact. The two
inspected host scene configurations consume binary artifacts and do not reference
this C owner directly. No applicable direct C consumer or complete host build
root was found there; no host build or frozen Release artifact was used.

Tools are committed before consumer source/guards/pin/docs; nothing is pushed.
Graphify retains all prior IDs and qualification metadata after observed hook
producers terminate. Scoped AST retention is not full-corpus re-extraction.
README retains only aggregate status rows. Codex is the only writer; Claude
calls: zero. Next audit `func_15197148` or another measured unmatched Game target
under the same qualification gates. The 85% total goal remains open.
