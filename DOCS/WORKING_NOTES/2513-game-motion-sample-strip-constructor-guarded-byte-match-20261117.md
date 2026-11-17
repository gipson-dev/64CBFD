# Motion-sample strip constructor recovery and guarded byte match - 2026-11-17

`s32 func_151ACBD4(void *descriptor, s32 extraBytes)` replaces the zero-return
placeholder with the complete twenty-sample and two-bank strip constructor.
Its **360-word / 1,440-byte retail slot and frame 0x40 are byte-exact**.
The complete semantic C emits **359 words**. **307 relocation-aware expected-word
guards and one inserted word** normalize allocation, address materialization,
constant/count handling and loop scheduling. There are **52 unchanged raw words**
at their original offsets and no omissions. This is a guarded C match, with no
compiler-profile change or handwritten function replacement.
VA 151ACBD4..151AD174, ROM 1DA084..1DA624.

Accepted total is **4,532 / 5,514 (82.19%)**, Game **3,859 / 4,841 (79.71%)**,
Init 492/492 and Debugger 181/181, with zero drift and **982** different.
**155 further matches** are needed for the active 85% goal. Conversion remains
5,514/6,048 (91.17%), covering 86.19% of bytes. Root README receives only the
Total and Game aggregate-row updates. Earlier private recovery and rejected
fits remain documented in [Note 2512](2512-game-strip-constructor-private-recovery-and-ordered-prefix-frontier-20261117.md).

## Recovered behavior and ABI

The constructor requests class 0x4E in category 0x2C, otherwise class 0x2F,
with the wrapped extra-byte count plus 0x58. A null first allocation returns
zero. It copies the 36-byte descriptor to record+0x10, computes reciprocal
scale, clears state/status, then allocates 480 bytes for twenty six-float
samples. X/Y/endY/Z are truncated in the original order. Each sample stores
start X/Z and a signed Y interpolation using wrapped 32-bit subtraction,
low-word multiplication, signed division by 19 and wrapped addition. Three
velocity fields are zeroed. The spacing retains the original CVT.S.W(19)
before converting the height difference and dividing.

It allocates 2,560 bytes for two banks of twenty four-vertex strips. Category
0xB selects texture 55/shift 4, otherwise texture 54/shift 5. Category 0x39
selects RGB 88/75/44, otherwise 255/255/255; alpha is 255. The 12-byte texture
table supplies width/height at +6/+8. The code initializes only vertex flags,
texture coordinates and colors, preserving vertex position bytes. It clears
the timer and returns the 32-bit record handle. The two buffer allocations
have no retail null guards, so none are invented.

Local byte-compatible record/sample/texture views preserve the shared
struct179/struct180 headers. The existing owner declaration of func_15167A68
now uses its definition's final u8 argument. The earlier private handoff's
implicit-factory assumption was incorrect: the owner already had a declaration.
Correcting it and the constructor comment leaves every emitted target word,
binding, neighbor and pool unchanged. The recovered return handle and two-word
interface agree with all six actual call sites.

## Complete relation and slot normalization

The useful v57 pair/remainder draft and the accepted v63 declaration/comment
repair emit identical raw words and bindings. The odd-count remainder peel is
ordinary recovery code, not evidence of the original C spelling. The count
capture is 20; the raw program's dormant remainder path is distinct from its
live paired sample loop. Every implemented statement remains semantic C.

An instruction-driven symbolic comparison passes **all ten complete modeled
provider/return paths directly**, with **zero private scheduling adjustments**.
It compares all public object bytes, all 80 private/incoming-home bytes,
ordered FP/FCSR operations, typed provider arguments, preserved registers and
return values. Both normalized streams separately pass the same relation.
Effective factory-size and copied-size controls reject. The final raw stack
restore word at +0x598 is replaced by JR RA; the original stack restore becomes
its inserted delay word. All other word/binding changes are expected-value
guarded. No instruction or FP operation is projected out of the comparison.

The model assumes fresh, mutually disjoint allocator objects and mapped,
aligned storage. It does not establish arbitrary allocation overlap, complete
fault-register identity, interrupts or hardware behavior. Native coordinate
truncations stay in the finite signed 32-bit domain. Guest/native checks do
not supply FP-status proof; the ordered symbolic comparison does.

## Fresh maintained qualification

All **five checks** pass in primary tools, the isolated sibling overlay and
installed production with identical **nine-file task fingerprints**. The final
report explicitly asserts 33 owner functions and 32 preserved neighbors;
preliminary reports with inherited count labels are superseded and retained.

- Both real padders preserve all 32 neighbors and normalized pools. An
  independently assembled original and **12 GNU links** agree under four
  code/data layouts, including independent global HI16 carries. All eight
  original bindings are accounted. **367 raw-word/binding corruptions**,
  **1,228 stale CSV controls** and **309 replacement/insertion controls** reject.
- **1,016 guest cases per retail/raw/strict/layout stream** compare all
  initialized public bytes, complete calls and preserved registers. The
  installed suite also executes a fresh production-ELF stream. Cases cover
  allocation failure, all descriptor byte tags, category branches, both stack
  phases, mutable providers, wrapped integer boundaries, extreme texture
  dimensions and scale zero/signed zero/NaN/infinities. Vertex positions and
  untouched record bytes remain preserved.
- **1,016 SDK32 C cases at O0/O2/O3** pass with strict aliasing and UB traps.
  A naive signed interpolation trips the overflow control. Wrong texture,
  class, UV scale and position-overwrite variants exit with the expected
  failure. All eight native executions have their expected results.
- **384 complete caller cases per stream** run the original 243-, 76- and
  36-word scene routines through all six sites. All mapped RAM, including
  private stack bytes, agrees across streams, alongside independent packet,
  constructor and scene-output references. Six wrong-extra-size controls and
  wrong-time-field/wrong-reciprocal controls reject. The four-call scene
  submits tags 1, 2, 3 and 5, preserving its overwritten fourth template; the
  loop scene submits tags 1..6 and the other scene one record. The measured
  caller word coverage is 217, 74 and 34. Other scene providers are bounded
  contracts, not full subsystem execution.

## Whole-image adoption and reproducibility

Baseline consumer **6960b4a3**, tools **17b6b00**. The final **1,498-input**
snapshot contains 1,495 verified immutable-snapshot links and three copied
files, with zero live-worktree hardlinks. Preliminary complete runs remain
intact. Actual shadow Make and production Make compile the C; no prebuilt
object is installed. Exactly four inputs change: source, guard CSV, owner
object and ELF. **1,494 inputs remain unchanged**. Only one of 698 objects
changes, with all 32 owner neighbors, all other **6,050 bodies**, every one
of **6,051 addresses**, pools and register metadata preserved. The old guard
CSV remains an exact byte prefix, with 307 target rows appended. Conversion
classification and compiler profiles stay unchanged.

Every ELF byte equals the independent prediction: **1,096 changed bytes,
zero exclusions**. No metadata serialization groups are needed.
All **20,289 named definitions** agree except the target's
1,440-byte extent. Four symbol/name/data/code corruption controls reject.
All **189,088 protected data bytes / 720 owners** remain exact. Shared progress
and tools checks pass. The duplicate generated_12D630 recipe warning is
pre-existing; the full build is not described as warning-free.
Production ELF SHA256: `7c1c2f7ef67741c05a3d512530e777e9e4e4de6f29df28ebc8a22e9b95e4af90`.

Selected raw SHA256:
`dc5c29763a42d15252d4171506768fe231eacfceae06c1ebbaf5dbf76ef8c14f`.
Use a fresh owned path in `CBFD_STRIP_CONSTRUCTOR_WORK` and run
`python3 -m unittest tools.tests.test_game_strip_constructor_151acbd4_recovery -v`.
Receipts and actual imported origins are retained under
`conker/build/game-next-151acbd4-private/adoption-final/`.

The sibling's 2,434 dirty paths and 339 scoped dependencies stay untouched.
The host path has diagnostic directories without a source checkout; no host,
Release or save changes are made. One bounded Claude analysis was used earlier
in the recovery; no additional call was used for adoption. Graphify retains old
IDs and an explicit tools-to-function reference; this is scoped refresh rather
than a full-corpus extraction. Commit tools before the consumer source/docs/pin.

Next inspect `func_151AD174` from the fresh unmatched list. The 85% goal remains active.
