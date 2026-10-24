# Dual-Point Motion Match

Date: 2026-10-24. Consumer predecessor `c0391ee0`; tools predecessor
`27b4a975`. Qualification tools committed first as
`8e2e877cd377764882cb95eaa431a989805ef5ef`. No push requested/performed.
Routine work, zero Claude calls; no provider/dependency or host changes.

## Recovered Routine

`func_1518F058`, `conker/src/game/generated_1BA1D0.c`, replaces the
three-word zero-return placeholder with complete typed motion C.
VA `0x1518F058..0x1518F108`, ROM `0x1BC508..0x1BC5B8`, exclusive ends:
176 bytes / 44 words / frame zero / two bindings, no alignment tail.
All 44 words are executable and visited. Retain the address-based function
name and a local `DualPointMotion1BA1D0` view, not speculative shared types.

1. Capture damping at +0x150. Multiply velocity X/Z at +0x140/+0x148
   by damping; do not damp vertical velocity.
2. Add vertical acceleration (+0x14C) times an early `D_800BE9A4` read
   to velocity Y (+0x144). Preserve float32 operations and store/access order.
3. Reload the timestep after the velocity updates. Capture all three
   velocity-times-step displacements before changing either point.
4. Add the same captured displacement to position +0x34/+0x38/+0x3C
   and endpoint +0x40/+0x44/+0x48. Return exactly one as signed s32.

Guest timestep overlap with mutable fields distinguishes the early/late
reads and displacement capture. The typed native checks use disjoint
storage; they do not claim portable C global-alias or guest fault semantics.

## Derived Scheduling Guards

Normal O2/g3 emits the complete 44-word body and frame zero. Bounded
source/declaration/pointer-shape screens did not find a direct match.
Validate the entire raw hash and both symbolic bindings before deriving
20 changed words by these two independent transformations:

- Rename only the timestep-address GPR role from V0 to V1: word zero RT,
  word one RS/RT, and words eight/seventeen RS. V0 is then free for return.
- Require the unique `addiu v0,zero,1` at word 22 and move it to word five.
  Preserve the relative order of every floating instruction and memory access.

No inserted/omitted words, changed FPRs, frame/save changes, barriers,
profile changes, inline assembly or assembly-body replacement. The two
HI16/LO16 bindings to `D_800BE9A4` remain at offsets zero/four with exact
expected and replacement relocation specs. Other new guard rows bind no
relocations. Append only; every historical CSV byte remains unchanged.

This is guarded semantic C, not compiler-only matching. Fitted and original
complete private states agree, including access-prefix stops. Raw C agrees
on floating state, public memory/access traces, saved state and calls; do
not equate its different volatile V0/V1 allocation or fault-PC positions.

Raw payload SHA-256:
`5b0da6fb4d23890270aaf0d3bffeb52077855823711a217722bd216b67eaa1e4`.
Resolved retail body SHA-256:
`b5dcf3352427638d5d24889006cc09eae5888dc51ead8fa0bdfa4bbce391db6c`.

## Actual Callback Boundary

The target is slot eight of the 42-entry `D_80089CB8` table; its literal
pointer is at ROM `0x22E798`, VA `0x80089CD8`. An aligned full-ROM scan
finds exactly that pointer and no direct JAL site.

Execute the actual 16-word original `func_1513CFE4` window at
`0x1513D034..0x1513D074`, ROM `0x16A4E4`, in 192 phases. Cover zero/eight
selector, signed expiry bytes, two stack phases, six motion patterns and
exact-one/controlled-zero callback return. Selector zero skips the call;
the nonzero path passes one pointer and uses V0 to force expiry one on zero.
Do not invent selector-range/null checks absent from that original window.

The full larger parent in `conker/src/game_169510.c` remains a C stub and
uncredited. Neither its source nor object changes. Native validation uses
a correctly typed local 42-entry callback wrapper, not a full recovered C
parent. No full-parent, gameplay, FCSR or hardware acceptance is inferred.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation:
no failures/errors/skips/reused checks. Pre-install primary/mirror:
11.514s / 11.313s; installed: 12.076s / 12.150s. Both shared project-tool
checks exit zero. Reuse existing MIPS/frame/fault/native32, relocation,
owner/pool and real generated-object padder helpers.

- 5,184 original/raw/fitted guest phases include twelve timestep layouts:
  disjoint storage and every position, endpoint, velocity, acceleration and
  damping field. Cover float32 arithmetic, signed zero and denormals;
  three additional nonfinite model cases are not hardware/FCSR acceptance.
- Native32 O0/O2/O3 trap UBSan passes 2,304 direct and 2,304 typed-wrapper
  cases per optimization with full typed storage and ten effective defined
  wrong-C controls. A fixture-only wrong-axis control initially made dz
  unused; restrict it to the endpoint so strict warnings stay enabled.
- Two separately compiled wrong timestep-capture C bodies produce actual
  guest counterexamples: capture too early at layout seven/pattern one,
  and reload after the first point update at layout one/pattern one.
- One hundred fired literal root-access prefixes preserve complete fitted
  private state and raw floating/memory/events/saved state as qualified above.
- Forty-six normalizer corruptions reject every changed raw word, missing
  bindings and a short body. Two real padder corruptions reject bad expected
  words/relocation specs; historical-prefix corruption fails closed.
- Nine independent GNU links compare original, qualified padded and actual
  Make objects at three entry/timestep pairs, including HI/LO carry edges.
  Ninety-six rebased phases pass; three strict-image corruptions are rejected.

## Production And Preservation

Advance the previous checkpoint's five qualified overrides, then seal
15,974 baseline files. Add the two tools modules in both copies to reach
15,978 files / 29 focused inputs / all 1,454 linker objects. Verify native
and Linux-cache bytes using checked stdin/tar bridges, no DrvFS project reads.
Preserve all 1,616 previous mirror dirty statuses/hashes/HEAD; add only the
two owned modules, now 1,618 paths. Do not commit/reset that older mirror.

Actual Make uses the ordinary three-command compiler/padder/assembler
recipe, O2/g3. Preserve all 60 raw/padded neighbors, all owner pools and
the complete qualified padded object. Isolated diagnostics are empty;
whole-owner pointer/integer warnings are unchanged. Duplicate generated_12D630
Make warnings also remain; this is not a warning-free build claim.

Production Make exits zero in 0.483s and exactly reproduces the independently
predicted complete ELF: 147 changed bytes, 146 target code plus one function
size metadata byte, 12 to 176. Zero exclusions or unrelated image changes.
All other 6,054 bodies/all 6,055 addresses and protected Game data remain:
720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Audit all 15,978 live files around adoption with exactly four overrides:
target source, guard CSV, target object and linked ELF. Re-capture the
actual adopted native ELF and freshly recount those bytes through the
checked bridge. Updated ELF SHA-256:
`5b0c22080c309f37cd7424673424d4f2c98923c73da2bb9f73b3ed2c7a5bb12e`.

| Section | Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,779 / 5,505 (68.65%) | 0 | 1,726 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,106 / 4,832 (64.28%) | 0 | 1,726 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold remains 4,129 exact functions: 350 more needed. The
ELF-pinned screen now has 1,597 placeholders, 120 semantic/other definitions
and nine parser-unlocated entries. `func_1510D8C0` already has a `Gfx *`
body and stays a separate matching case. Next real placeholder:
`func_15192800`, owner `generated_1BFCB0`, 44 words, not yet qualified.
Private screens are uncredited. Keep `func_1509E730`, `func_1508CAD8` and
unmatched parent `func_15169070` separate. README changes only its two
aggregate rows; host Release, saves, configuration and sibling work untouched.
