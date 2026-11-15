# Game category record initializer: proven guarded match

Date: 2026-11-15. `func_150169A0` is adopted as complete semantic C with
**477 / 477 linked words**, original **single S0 save**, **frame 0x58** and
original saved/local homes. This closes the independent-proof and placement
boundary from [Note 2458](2458-game-category-record-initializer-save-native-and-projection-20261115.md).
The raw compiler body remains 481 words; **361 checked guard rows**, five
omissions and one duplicated source shift recover the original schedule.
This is a guarded match, with no compiler-profile or shared-header change.

The actual production recount is **4,497 / 5,515 (81.54%)** total and
**3,824 / 4,842 (78.98%)** Game, zero drift and **1,018** different.
Init remains **492 / 492**, Debugger **181 / 181**. Converted functions/bytes
are unchanged. Owner `generated_43D00` now has **2 / 3 exact** routines.
The active 85% goal needs **191** more matches to reach **4,688 / 5,515**.

## Recovered behavior and source ownership

The void initializer chooses the category's ROM record bank, allocates and
loads its base records, appends category records, captures the live count for
the byte/halfword buffers, clears them, applies player settings/resources and
positions, builds the resource cache and fills missing record identities.
It retains all three final submissions in their original order.

`Record150169A0` names the recovered 0x30-byte layout; coordinate casts and
the 0x32C actor stride preserve the existing 32-bit ABI. The original
address-named function is retained, with a semantic comment. The complete
body is in `conker/src/game/generated_43D00.c`; original assembly remains
in `conker/asm/43D00.s`. Both other raw and padded owner functions stay fixed.

The source keeps its 68 binding sites, original SP+0x20/0x24 saves, category
SP+0x58, bank SP+0x4C, count SP+0x40 and both distinct loop-index homes.
Its 481 raw words have SHA-256
`0028b0d4e468e23a1d1bd253c8286eca1bb2572ae5a2b659c83f467fdd8eb4ec`.
The generated 336-byte pool's 79 table entries are checked through the
inverse schedule against the existing data owner, including both float
constants and padding. The production data owner is retained unchanged.

## Independent scheduling proof

- [x] The symbolic executor consumes instructions, with no color or schedule
  template in its transfer engine. It compares canonical path predicates,
  ordered public reads/writes/calls, floating conversion/status effects,
  saved registers, stack homes and live loop roles.
- [x] **350 symbolic transfer paths** pass: prefix 39, header 2, player
  iteration 302, cache setup 2, identity iteration 4 and finalization 1.
  Arbitrary indices and 48-byte cursors close both inductive loop joins;
  opaque helpers can change mutable public data and caller-saved state.
- [x] The fixed state reset/player-count load commute is justified by their
  actual disjoint byte ranges. No record/actor/global disjointness is assumed
  among mutable public accesses. The actor-address move remains pure, and
  both scene paths keep the coordinate read after any scene-flag write.
- [x] Branch-likely annul behavior, the duplicated shift, constant-3 lifetime,
  removed SP+0x28 temporary and heading store in the branch delay are covered.
  A second valid T0/T1 allocation also passes, demonstrating that the engine
  does not merely compare with retail words or a fixed register-color table.
- [x] Seven supported-instruction controls reject wrong player/identity
  induction, the active marker, selector argument, coordinate address,
  annul behavior and cursor home. Separately, all **549** raw-word/binding
  corruption controls reject stale projection inputs.

The contract is normal execution with valid mapped/aligned storage, immutable
implementation code/literals and nonaliasing private stack/literal storage.
Providers preserve o32 saved state and cannot inspect caller code, return PC,
implementation literals or unpassed locals; their mutable public effects
remain opaque. Literal jump pointers may only feed JR and cannot escape
through stores, arithmetic, comparisons or helper arguments. Raw hardware
fault state and general portable-C undefined-input behavior are not claimed.

## Guest, native and original caller

- [x] Fresh pre-adoption and installed suites pass **686 cases / three
  streams**: original retail, independently based raw C and actual normalized
  owner code. All public bytes, helper-entry snapshots, saved GPR/FPR state
  and SP agree. **473 / 477** original words execute; the four remaining
  words retain structural unreachable proofs. Three effective guest controls
  reject changed category dispatch, active marker and coordinate output.
- [x] Raw 481-word execution stays at 0x14000000, avoiding overlap with the
  called `func_15017114`. The installed 477-word body fits exactly at
  **0x150169A0..0x15017114**, ROM **0x43E50..0x445C4**.
- [x] **48 authentic caller cases / two streams** pass with the original
  category-load delay slot. The separate **68-instruction** result-use proof
  and two controls show that the old V0 is overwritten before any read at
  0x1502ACAC. This qualifies the void interface, not the full caller/provider.
- [x] Native **639 cases each at O0/O2/O3**, with seven effective controls
  per profile, are **reused with exact fingerprints** from Note 2458.
  Source/oracle/native fixture/reader/writer/compiler, command profiles,
  generated C and all executable hashes are verified. No fresh native run
  is claimed. The SHA snapshots still cover all **29,090 public bytes**;
  the declared GNU native32 capacity remains 26 actors / 64 records.

The sibling check uses an ignored overlay of **11 byte-identical task files**.
It passes fresh **64 guest cases / three streams**, **48 caller cases / two
streams**, the independent proof/controls, both padders and four link layouts;
native receipts are explicitly reused. The final contract-docstring change
has identical implementation AST and a fresh sibling proof replay. Its HEAD
stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, all **2,439 dirty paths**
and status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
are preserved. The sibling checkout itself is not overwritten or committed.

## Placement, whole image and production adoption

- [x] Both complete-owner padders retain all three functions and bindings.
  **12 independent GNU links / four layouts** agree with assembled retail,
  including independent code/data rebases and low-half carry cases.
- [x] Three actual Make recipe commands agree with the independent raw owner.
  The private linked ELF predicts the complete production ELF before adoption.
- [x] Production Make rebuilds the owner and linked ELF. The actual ELF is
  byte-identical to the prediction. The strict full-file model accounts for
  the target slot/size and six closed symbol/string permutations: **1,609
  changed bytes**, **zero exclusions**. Every named symbol definition remains
  fixed except the target's declared 12-to-1,908-byte extent.
- [x] All **6,051 function addresses** stay fixed; only this function body
  changes. Of **698 objects**, only `generated_43D00.c.o` changes, in `.text`,
  `.rel.text`, `.symtab` and `.strtab`, matching the independent Make object;
  every other owner section is fixed. Both owner neighbors and padded pools stay
  fixed. All prior guard bytes remain an exact prefix; 361 new rows belong
  only to this target. Conversion rows and Makefile remain unchanged.
- [x] All **189,088 protected data bytes / 720 owners** are exact, SHA-256
  `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
  The other **808 / 812 frozen inputs** stay fixed, including **82 include
  inputs: 80 .h files and two .inc files**. This refines the earlier shorthand
  that called all 82 inputs headers; none was omitted from the hash checks.

Production ELF SHA-256:
`c70655daece8c7291df383fd5d17b7a373535eedf1bad3543e00dff9244c5784`.
Fresh shared `make tools-check` passes. The known duplicate
`generated_12D630` Make recipe warning is unchanged.

The fresh pre-adoption suite passes in **121.310 s**; the complete installed
suite, including the added projection checks, passes in **143.241 s**.

Detailed receipts, immutable prior snapshots and the pre-adoption reports
are retained in `conker/build/game-record-initializer-150169a0-private/`,
including `qualified-private-match/`. Normalization/proof/padder tools and
the focused installed suite are committed before the consumer source/pin.
Tools commit: `14bec65b0f5d88dcc42f223a1793d671d7658d32`. No push; no host
files, builds or Release artifacts were touched.

The read-only sibling applicability check finds only `.codex/` and
`recomp_scene/` at the recorded `64CBFDOGL` path, with no `.git` or root
`CMakeLists.txt`. Old generated copies of this routine are present, but that
path does not establish an active port checkout or its current source input.
Host adoption/applicability remains unverified; no host result is inferred
from the N64 match.

Graph refresh is a scoped AST merge of **12 files**, retaining all
**61,216 old IDs** with zero loss; **61,258 nodes /
115,081 links**, not full-corpus re-extraction. Routine Claude
calls: zero. README changes are limited to the measured aggregate rows.

## Resume

Next inspect **`func_15017114`**, the remaining **123-word slot: 121 instruction
words plus two alignment words**, at **0x15017114..0x15017300**. The parent checks do not qualify
its opaque internals or grant it a match. Continue with its complete body,
ABI/callers, source/native/guest, padders, image and production/recount gates.
The common particle updater remains private and uncredited. Keep the broader
85% goal active; do not treat this single-function checkpoint as completion.
