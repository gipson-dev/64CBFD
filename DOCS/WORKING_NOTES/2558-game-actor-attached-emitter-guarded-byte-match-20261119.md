# Actor-attached emitter guarded byte match

Date: 2026-11-19. `func_150BB760` replaces its zero-return placeholder in
`conker/src/game/generated_E8C10.c`. The complete **255-word / 1,020-byte**
slot, VA `150BB760..150BBB5C`, ROM `E8C10..E900C`, is now byte-exact.
Semantic C emits **254 words** with the original **248-byte frame** and
**32 relocations**. **38 expected-word guards** derive the original call
schedule and temporary-register allocation, including **one inserted NOP**
and **zero omissions**. Compiler profiles and original ASM are unchanged.

Fresh production totals: **4,558 / 5,514 (82.66%)** overall,
**3,885 / 4,841 (80.25%)** Game, Init **492 / 492**, Debugger **181 / 181**,
zero drift and **956** still different. **129 more** matches reach 85%.
Conversion stays 5,514 / 6,048 (91.17%), 86.19% of bytes. The goal stays active.

## Recovered behavior and result boundary

The actor's **byte4 type read precedes its null check**, exactly as in retail.
Type other than 32 takes the explicit return-one path. The emission path also
requires a non-null actor, active word0 and nonzero model word `1D4`.
The other gates and the post-factory path have no total source-level return
contract. The known caller ignores the result. Do not replace these paths
with an invented unconditional return or move the null check ahead of byte4.

Signed16 dimensions at `E4`/`E6` are cached before helper calls. Two heading
samples reload actor halfword `76`, using its high byte and high byte+64;
motion at `3C` is read afterward for half-speed X/Z drift. The descriptor
uses flags `29E9`, resource 1, unit scale, actor ownership and a cached byte
from actor `3B`. A random byte and REAL sample choose a radial offset; a
second RNG result is obtained **before reloading heading** for a spread of
`heading - (random & 63) - 32`. This sequencing is explicit in the C source.

Further samples set speed `*5+3`, two global-driven size values and their
half-sum, three `*360` rotations, position offsets and vertical motion,
two `25 - sample*50` fields, duration `(random & 31)+60`, and final scalar
`sample*D_8009FEA4+0.25`. Preserve the late actor/global reads around helpers:
dimensions and computed drift stay cached while later positions, heading and
size globals observe intervening mutation. Once dead, the saved heading
sample's scalar is reused for the second size without adding a frame home.

The descriptor occupies **124 bytes**, with **112 initialized bytes** and
12 untouched bytes at `59..5B`, `69`, `6B`, `71`, and `76..7B`. Its owner
field is a real pointer. The call is
`func_15132A4C(&descriptor, 3, 255, 0, 255, 0)`; its result remains unused.
No memset or invented reserved-field values are introduced.

The aligned retail census finds one JAL at ROM `9C49C` and no aligned target
pointer literal. The complete 15-word caller `func_1506EFC8` reads
`D_800D154C`, skips the target for identity `8C`, and ignores its result.
The complete 15-word factory wrapper forwards all seven backend words:
`(descriptor, 3, 255, 0, 0, 255, 0)`. Its backend `func_1513264C` and allocator
remain modeled services, not newly qualified complete implementations.

## Closed normalization proof

The normalizer first checks the complete raw payload hash and all bindings,
then derives these changes and compares every resulting word/relocation to
the separately assembled frozen original:

- Source `154` is the RNG JAL, with a byte store at `158` in its delay slot.
  Retail executes that independent `SB T1,EC(SP)` first, then the JAL with an
  empty delay slot. The byte store does not use RA and the JAL does not alter
  SP/T1. The two source rows exchange their instruction and relocation roles;
  the second row inserts the one original NOP.
- Four forward branches at source `20`, `28`, `34`, `40` are retargeted across
  the expansion. All branch destinations are derived from signed displacements;
  none enters the exchanged instruction pair. All 32 relocation positions are
  mapped by instruction identity, including the exchanged JAL.
- Twenty floating-register words and twelve integer-register words normalize
  temporary values. The proof tracks each definition and consumer, requires
  equal load addresses and stored values, protects preserved registers, and
  checks helper arguments **after the call's delay word** before applying the
  helper clobber model. One floating add at retail `2F4` exchanges commutative
  operands. No opcode, constant, memory displacement or function target is
  supplied by an unrestricted word-copy normalizer.

The raw SHA-256 is
`416cac829340d26f4e7313ba8c8de93fa5ddfb95c56d2d8caaf260eda436d443`.
Guard CSV offsets refer to raw source positions. The guard generator writes
output order, while its branch/relocation map tracks instruction identity;
these are distinct operations. The old guard CSV bytes remain an unchanged
prefix, followed by exactly 38 derived rows.

This is a bounded C/ABI/value relation. Native checks use finite values and
the caller's unused-result contract; no arbitrary raw FCSR, private fault-state
or gameplay equivalence claim is made. The final production instructions,
including the add operand order and original call delay, are literal retail.

## Validation and production audit

Both final configurations pass **five tests**, zero failures/errors/skips,
**105.019s primary / 116.854s sibling overlay**,
with **317 imported tool fingerprints each**. The 873-file overlay contains
339 matching sibling files, 526 primary fallbacks, seven task files and one
bootstrap. The real sibling dirty HEAD/status and 343 dependency hashes remain
unchanged; conflicting edits were not overwritten or claimed tested.

- Full before/after owner compilation preserves **all eight neighbors** and
  pools. Both actual production padders reproduce the entire function, with
  **12 GNU rebases**, **286 rejected instruction/binding corruptions**, **80
  guard expected-word/relocation failures**, and **two effective inserted-word
  corruption controls**.
- **1,026 guest cases / 3,078 executions** compare raw C, normalized code and
  retail to an independent descriptor reference, covering all 255 retail
  words. Two mapped-null cases and three unmapped-byte4 fault checks preserve
  the early-read boundary. Three controls that replace that read with a
  constant demonstrate that the fault check detects its removal. Mapped-null
  cases are guest fixtures, not native null-pointer acceptance.
- **264 cases through the complete caller** and **128 through the complete
  factory wrapper**, each across three programs, preserve public state,
  descriptor observations, arguments and saved ABI. Every caller/wrapper
  word is visited; higher parents and the deeper backend remain outside scope.
- **512 SDK32 native cases at each of O0/O2/O3**, strict aliasing, no fast math
  and UBSan pass. All **18 semantic negative controls** fail. Typed actor
  backing respects the actual numeric subobjects; pointer identity and guest
  endian descriptor fields are checked. Twelve reserved descriptor bytes are
  not assigned invented native values. Fixtures ignore the result and suppress
  only the expected native return-type diagnostic for the original fallthrough.
- Actual Make and the independent full-image predictor agree on **843 explained
  changed bytes**, with four image corruptions rejected and **zero exclusions**.
  Production really recompiles the selected owner; no prebuilt object is copied.

Three exact symbol-record/string permutations are pinned and reconstructed:

| Original order | Rebuilt order |
| --- | --- |
| `D_8009FE9C, D_80096A9C` | `D_80096A9C, D_8009FE9C` |
| `D_8009FEA0, D_800A02A0` | `D_800A02A0, D_8009FEA0` |
| `D_8009FEA4, D_800A02A4` | `D_800A02A4, D_8009FEA4` |

These are distinct-address symbols. Complete named definitions are compared,
allowing only the explicit target size update from 12 to 1,020 bytes. No
metadata section or address range is excluded from the image comparison.

Only source, guard CSV, owner object and ELF change among **1,849 frozen
inputs**. All **698 objects** are audited; only this owner changes. All
**6,050 other function bodies, addresses and extents**, eight neighbors/pools,
and **189,088 protected bytes / 720 owners** remain unchanged. Progress rows,
original ASM, shared headers, Makefile and compiler inputs are byte-identical.
Production ELF SHA-256:
`dc89a9799fde80dc8fe3cccfbe4f55a32e3c8a0de4966ca950fe60d3dbef0292`.

Fresh installed checks recompile all nine owner functions/pools, derive and
compare the actual 255 production words, and rerun 1,026 guest, 264 caller
and 128 wrapper cases. Unchanged padder/rebase/guard/native/image receipts are
explicit fingerprinted reuses. Required `match-progress` and `tools-check`
pass; the pre-existing duplicate generated_12D630 recipe warning remains.

Historical private screens are retained. The first 255-word draft had 131
differences; separate scale stores and deferred size/velocity publication
recover the 254-word form. Explicit RNG sequencing changes only proved
temporary register allocation. The initial row generator confused output
position with instruction identity for the exchanged pair; both padder gates
caught that error. The corrected table has 38 rows and all final gates pass.
An early probe also attempted to execute a ROM metadata value as code; its
iteration now selects only program-word entries. Neither failed probe was
used to claim production acceptance.

Root README changes only two aggregate matching rows; detail stays here and
in five concise indexes. Graphify uses a native update attempt, six-file scoped
AST refresh, explicit target reference and old-ID retention, without a full
corpus extraction claim. Zero Claude calls and no REA/WSL reconfiguration.
The supplied host-port path still has captures rather than an identifiable
active checkout; no host/Release/save/capture changes or adoption are claimed.
Tools are committed before their consumer, with no automatic push or pause.

Next inspect **func_150BBB5C**, still a placeholder in this owner: **587 words /
624-byte frame**. Freeze its callers/providers against the new baseline before
drafting. The smaller listed `func_150AE280` is not a trivial C candidate:
its slot begins with a saved-SP restore and cross-entry branch, so ownership
must be resolved before treating its 55 listed words as one compiler routine.
No next-target candidate or additional match is credited.
